"""Build docs/data/species.json from the CSV files in data/.

Run from the repository root:  python3 scripts/build.py
Needs pandas (pip install pandas).

Two stages:
  * families  - rows in taxa.csv with rank=family (kew_id "fam:<Family>"), scored on stage=family characters.
  * species   - rows with rank=species, scored on their family's stage characters (e.g. stage=Lamiaceae).
Species inherit every family-stage score from their family unless they have their own score for that character.
Some characters are calculated from the Kew table rather than scored by hand:
  * wet    - family: union of In water (Ellenberg F >= 10), Wet ground (8-9), Dry or damp (<= 7) over its species
  * height - maximum vegetative height; for families, the tallest species
"""
import csv, json, math, sys
from collections import defaultdict
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "docs" / "data" / "species.json"
IN_SCOPE = lambda s: isinstance(s, str) and (s in ("N", "?N", "Neonative", "Neo-natd") or s.startswith("Arch"))

def rows(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def num(v):
    try:
        v = float(v)
        return None if math.isnan(v) else v
    except (TypeError, ValueError):
        return None

taxa, chars, states, sources, scores = (rows(n) for n in ["taxa.csv", "characters.csv", "states.csv", "sources.csv", "scores.csv"])
prec = {s["source_id"]: int(s["precedence"]) for s in sources}
kew_all = pd.read_csv(DATA / "kew" / "BI_MAIN.csv", encoding="latin1", low_memory=False)
kew = kew_all.set_index("kew_id")
flora = kew_all[kew_all.extinct_species_marker.isna() & kew_all.StaceIV_nativity.map(IN_SCOPE)]

# ---- validate ----
errors = []
allowed = defaultdict(set)
for s in states: allowed[s["char_id"]].add(s["state_id"])
taxon_ids = {t["kew_id"] for t in taxa}
char_ids = {c["char_id"] for c in chars}
for i, r in enumerate(scores, start=2):
    if r["kew_id"] not in taxon_ids: errors.append(f"scores.csv line {i}: unknown taxon {r['kew_id']}")
    if r["source_id"] not in prec: errors.append(f"scores.csv line {i}: unknown source {r['source_id']}")
    if r["char_id"] in allowed and r["value"] not in allowed[r["char_id"]]:
        errors.append(f"scores.csv line {i}: '{r['value']}' is not a state of {r['char_id']}")
    if r["char_id"] not in char_ids and r["char_id"] not in ("flower_start", "flower_end", "max_height_m"):
        errors.append(f"scores.csv line {i}: unknown character {r['char_id']}")
fam_names = {t["name"] for t in taxa if t["rank"] == "family"}
for t in taxa:
    if t["rank"] == "species" and t["kew_id"] not in kew.index: errors.append(f"taxa.csv: {t['name']} kew_id {t['kew_id']} not in Kew table")
    if t["rank"] == "species" and t["family"] not in fam_names: errors.append(f"taxa.csv: {t['name']} family {t['family']} has no family row")
missing = sorted(set(flora.family) - fam_names)
if missing: print("Warning: families in the flora with no family row:", ", ".join(missing))
if errors:
    sys.exit("Validation failed:\n" + "\n".join(errors))

# ---- merge: for each taxon/character keep values from the highest-precedence source ----
by = defaultdict(list)
for r in scores: by[(r["kew_id"], r["char_id"])].append(r)
def best(tid, cid):
    rs = by.get((tid, cid), [])
    if not rs: return [], None
    top = min(prec[r["source_id"]] for r in rs)
    keep = [r for r in rs if prec[r["source_id"]] == top]
    return [r["value"] for r in keep], keep[0]["source_id"]

def wet_states(F):
    out = set()
    for f in F.dropna():
        out.add("water" if f >= 10 else "wet" if f >= 8 else "land")
    return sorted(out)

fam_chars = [c["char_id"] for c in chars if c["stage"] == "family" and c["kind"] in ("state", "feature") and c["char_id"] != "wet"]
families, fam_lookup = [], {}
for t in [t for t in taxa if t["rank"] == "family"]:
    sub = flora[flora.family == t["name"]].sort_values("GB_Man_hectads_post2000", ascending=False)
    fam = dict(id=t["kew_id"], name=t["name"], common=t["common"], tip=t["tip"], src={})
    for c in fam_chars:
        fam[c], fam["src"][c] = best(t["kew_id"], c)
    if fam.get("flowers") == ["none"]:  # flowerless (ferns, conifers): any answer about flower parts is a mismatch
        for c in ("inflor", "sym", "ovary", "stamens"):
            fam[c] = ["n/a"]
    fam["wet"] = wet_states(sub.F_PLANTATT); fam["src"]["wet"] = "kew-bife"
    fam["height"] = num(sub.max_veg_height.max())
    fam["n"] = int(len(sub)); fam["n_native"] = int((sub.StaceIV_nativity == "N").sum())
    fam["n_common"] = int((sub.GB_Man_hectads_post2000.fillna(0) > 500).sum())
    fam["genera"] = list(dict.fromkeys(sub.genus))
    fam["top"] = [[r.taxon_name_binom, int(r.GB_Man_hectads_post2000) if not pd.isna(r.GB_Man_hectads_post2000) else None] for r in sub.head(12).itertuples()]
    families.append(fam); fam_lookup[t["name"]] = fam

state_chars = [c["char_id"] for c in chars if c["kind"] in ("state", "feature") and c["stage"] not in ("family", "all")]
species, sigs = [], defaultdict(list)
for t in [t for t in taxa if t["rank"] == "species"]:
    k = kew.loc[t["kew_id"]]
    sp = dict(id=t["kew_id"], kew_id=t["kew_id"], name=t["name"], common=t["common"], tip=t["tip"], family=t["family"], src={})
    for c in fam_chars:  # inherit family scores unless the species has its own
        own, src = best(t["kew_id"], c)
        sp[c], sp["src"][c] = (own, src) if own else (fam_lookup[t["family"]][c], "family")
    for c in [c["char_id"] for c in chars if c["stage"] == t["family"] and c["kind"] in ("state", "feature")]:
        sp[c], sp["src"][c] = best(t["kew_id"], c)
    fs, _ = best(t["kew_id"], "flower_start"); fe, _ = best(t["kew_id"], "flower_end")
    sp["months"] = [int(fs[0]), int(fe[0])] if fs and fe else None
    h = num(k.max_veg_height); hf = False
    if h is None:
        hv, _ = best(t["kew_id"], "max_height_m"); h = num(hv[0]) if hv else None; hf = h is not None
    gb, ie = num(k.GB_Man_hectads_post2000), num(k.Ire_hectads_post2000)
    if gb == 0 and ie == 0: gb = ie = None
    sp.update(status=k.StaceIV_nativity if isinstance(k.StaceIV_nativity, str) else None, height=h, height_filled=hf,
              F=num(k.F_PLANTATT), R=num(k.R_PLANTATT), gb=gb, ie=ie, powo=k.POWO_URL)
    species.append(sp)
    sigs[(t["family"],) + tuple(tuple(sorted(sp[c])) for c in state_chars if c in sp)].append(t["name"])

fsigs = defaultdict(list)
for f in families: fsigs[tuple(tuple(sorted(f[c])) for c in fam_chars + ["wet"])].append(f["name"])
for names in list(sigs.values()) + list(fsigs.values()):
    if len(names) > 1: print("Warning: identical scores, the key cannot separate:", ", ".join(names))

keyed = sorted({s["family"] for s in species})
for f in families: f["has_key"] = f["name"] in keyed
out = dict(
    characters=[dict(c, states=[[s["state_id"], s["label"]] for s in states if s["char_id"] == c["char_id"]]) for c in chars],
    sources=sources, families=families, species=species, keyed=keyed)
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"Wrote {OUT.relative_to(ROOT)}: {len(families)} families, {len(species)} species, {OUT.stat().st_size/1024:.0f} KB")
