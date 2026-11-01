"""Fetch open data that fills gaps the Kew table leaves. Run by the monthly GitHub job.

    python3 scripts/enrich.py              # names + flowering months for every species
    python3 scripts/enrich.py --names      # English names only (fast, a few minutes)
    python3 scripts/enrich.py --flowering  # flowering months only (slow: about 1 to 2 hours)
    python3 scripts/enrich.py --counts     # GBIF record counts only (about 30 to 45 minutes)
    python3 scripts/enrich.py --limit 20   # try a few species first

Writes:
  data/auto/english_names.csv  English names from Wikidata (property P1843, en-gb preferred). Licence CC0.
  data/auto/flowering.csv      Flowering months from iNaturalist observations in Britain and Ireland that
                               observers annotated "Flowering". Only counts per month are used.
  data/auto/inat_taxa.csv      Cache of iNaturalist taxon IDs, so later runs are quicker.
  data/auto/gbif_counts.csv    Number of GBIF occurrence records in Great Britain (+ Isle of Man) and in Ireland.
                               build.py turns these into estimated hectad counts for species the Kew table
                               has no counts for, by matching rank order against species that have both.

Hand-entered values in data/ always win over these (see precedence in data/sources.csv).
Needs: pandas, requests.
"""
import argparse, csv, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AUTO = ROOT / "data" / "auto"
UA = "BritishFloraKey/1.0 (https://github.com/drdavidglew-afk/BritishFlora)"
WIKIDATA = "https://query.wikidata.org/sparql"
INAT = "https://api.inaturalist.org/v1"
GBIF = "https://api.gbif.org/v1"
# Britain and Ireland (a box; clips a little of northern France)
BOX = dict(swlat=49.85, swlng=-10.7, nelat=60.9, nelng=1.8)
MIN_RECORDS = 15       # fewer flowering records than this: leave months blank
THRESHOLD = 0.10       # a month counts if it has at least 10% of the peak month's records


def flora():
    import pandas as pd
    k = pd.read_csv(ROOT / "data" / "kew" / "BI_MAIN.csv", encoding="latin1", low_memory=False)
    s = k.StaceIV_nativity
    keep = k.extinct_species_marker.isna() & (s.isin(["N", "?N", "Neonative", "Neo-natd"]) | s.fillna("").str.startswith("Arch"))
    f = k[keep]
    f = f[~((f.taxonomic_status != "Accepted") & f.accepted_name.isin(f.taxon_name_binom))]
    out = [(r.kew_id, r.taxon_name_binom) for r in f.itertuples()]
    # species added by hand that the Kew table lacks (ids "agg:<name>")
    with open(ROOT / "data" / "taxa.csv", newline="", encoding="utf-8") as fh:
        out += [(r["kew_id"], r["kew_id"][4:]) for r in csv.DictReader(fh) if r["kew_id"].startswith("agg:")]
    return out


def british_case(name):
    """'meadow buttercup' -> 'Meadow Buttercup'; 'ground-ivy' -> 'Ground-ivy' (BSBI style)."""
    return " ".join(w[:1].upper() + w[1:] for w in name.strip().split())


def wikidata_names(species, post, batch=150):
    out = {}
    for i in range(0, len(species), batch):
        chunk = species[i:i + batch]
        values = " ".join('"%s"' % n.replace('"', "") for _, n in chunk)
        q = ('SELECT ?name ?common (LANG(?common) AS ?lang) WHERE { VALUES ?name { %s } '
             '?item wdt:P225 ?name . ?item wdt:P1843 ?common . '
             'FILTER(LANG(?common) = "en-gb" || LANG(?common) = "en") }' % values)
        data = post(WIKIDATA, data={"query": q, "format": "json"})
        found = {}
        for b in data["results"]["bindings"]:
            n, c, lang = b["name"]["value"], b["common"]["value"], b.get("lang", {}).get("value", "en")
            rank = 0 if lang == "en-gb" else 1
            if n not in found or (rank, len(c)) < found[n][0]:
                found[n] = ((rank, len(c)), c)
        for kid, n in chunk:
            if n in found:
                out[kid] = (n, british_case(found[n][1]))
        print(f"  Wikidata: {min(i + batch, len(species))}/{len(species)}, {len(out)} names so far", flush=True)
        time.sleep(1)
    return out


def flowering_range(hist):
    """hist: {month(int): count}. Returns (start, end, total) or None."""
    total = sum(hist.values())
    if total < MIN_RECORDS:
        return None
    peak = max(hist.values())
    months = [m for m in range(1, 13) if hist.get(m, 0) >= THRESHOLD * peak]
    return (months[0], months[-1], total) if months else None


def inat_taxon_id(name, get, cache):
    if name in cache:
        return cache[name] or None
    data = get(f"{INAT}/taxa", params={"q": name, "rank": "species", "per_page": 10})
    tid = ""
    for r in data.get("results", []):
        if r.get("name") == name or r.get("matched_term") == name:
            tid = str(r["id"]); break
    cache[name] = tid
    return tid or None


def inat_flowering(species, get, cache, pause=1.1):
    out = {}
    for i, (kid, n) in enumerate(species, 1):
        try:
            cached = n in cache
            tid = inat_taxon_id(n, get, cache)
            if not cached: time.sleep(pause)
            if tid:
                data = get(f"{INAT}/observations/histogram", params=dict(
                    taxon_id=tid, term_id=12, term_value_id=13, interval="month_of_year",
                    date_field="observed", verifiable="true", **BOX))
                hist = {int(m): int(c) for m, c in data["results"]["month_of_year"].items()}
                rng = flowering_range(hist)
                if rng: out[kid] = (n,) + rng
                time.sleep(pause)
        except Exception as e:  # keep going; one failure shouldn't stop the run
            print(f"  iNaturalist: {n}: {e}", file=sys.stderr)
        if i % 100 == 0 or i == len(species):
            print(f"  iNaturalist: {i}/{len(species)}, {len(out)} with flowering months", flush=True)
    return out


def gbif_counts(species, get, pause=0.15):
    out = {}
    for i, (kid, n) in enumerate(species, 1):
        try:
            m = get(f"{GBIF}/species/match", params={"name": n, "kingdom": "Plantae"})
            key = m.get("acceptedUsageKey") or m.get("usageKey")
            if key and m.get("matchType") in ("EXACT", "FUZZY") and m.get("rank") in ("SPECIES", None):
                c = {}
                for label, countries in (("gb", ["GB", "IM"]), ("ie", ["IE"])):
                    c[label] = 0
                    for cc in countries:
                        r = get(f"{GBIF}/occurrence/search", params={"taxonKey": key, "country": cc, "limit": 0})
                        c[label] += int(r.get("count", 0)); time.sleep(pause)
                out[kid] = (n, key, c["gb"], c["ie"])
            time.sleep(pause)
        except Exception as e:
            print(f"  GBIF: {n}: {e}", file=sys.stderr)
        if i % 200 == 0 or i == len(species):
            print(f"  GBIF: {i}/{len(species)}, {len(out)} counted", flush=True)
    return out


def read_cache():
    p = AUTO / "inat_taxa.csv"
    if not p.exists(): return {}
    with open(p, newline="", encoding="utf-8") as f:
        return {r["name"]: r["inat_id"] for r in csv.DictReader(f)}


def write(name, header, rows):
    AUTO.mkdir(parents=True, exist_ok=True)
    with open(AUTO / name, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(header); w.writerows(rows)
    print(f"Wrote data/auto/{name}: {len(rows)} rows")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--names", action="store_true"); ap.add_argument("--flowering", action="store_true")
    ap.add_argument("--counts", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args(argv)
    everything = not (a.names or a.flowering or a.counts)
    do_names, do_flower, do_counts = a.names or everything, a.flowering or everything, a.counts or everything
    import requests
    s = requests.Session(); s.headers["User-Agent"] = UA
    def get(url, params=None):
        for attempt in range(4):
            r = s.get(url, params=params, timeout=60)
            if r.status_code == 429: time.sleep(30 * (attempt + 1)); continue
            r.raise_for_status(); return r.json()
        r.raise_for_status()
    def post(url, data=None):
        r = s.post(url, data=data, headers={"Accept": "application/sparql-results+json"}, timeout=120)
        r.raise_for_status(); return r.json()
    sp = flora()
    if a.limit: sp = sp[:a.limit]
    print(f"{len(sp)} species")
    if do_names:
        names = wikidata_names(sp, post)
        write("english_names.csv", ["kew_id", "name", "common", "source_id"],
              sorted([kid, n, c, "wikidata"] for kid, (n, c) in names.items()))
    if do_flower:
        cache = read_cache()
        fl = inat_flowering(sp, get, cache)
        write("flowering.csv", ["kew_id", "name", "flower_start", "flower_end", "n_records", "source_id"],
              sorted([kid, n, s0, e0, t, "inat-pheno"] for kid, (n, s0, e0, t) in fl.items()))
        write("inat_taxa.csv", ["name", "inat_id"], sorted(cache.items()))
    if do_counts:
        gc = gbif_counts(sp, get)
        write("gbif_counts.csv", ["kew_id", "name", "gbif_key", "gb_records", "ie_records"],
              sorted([kid, n, k, g, i] for kid, (n, k, g, i) in gc.items()))


if __name__ == "__main__":
    main()
