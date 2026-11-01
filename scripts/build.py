"""Build docs/data/species.json from the CSV files in data/.

Run from the repository root:  python3 scripts/build.py
Needs pandas (pip install pandas).

Two steps in the app:
  * families - rows in taxa.csv with rank=family (id "fam:<Family>"), scored on stage=family characters.
  * species  - every native, ancient or naturalised species in the Kew table, grouped by family.

Character stages (characters.csv):
  family       step 1 questions
  <Family>     extra species questions for that family only (e.g. Lamiaceae)
  generic      standard species questions, used for families without their own set
  species      used in every species key (month, region, and the Kew habitat questions)
  all          used in both steps (height)

Calculated from the Kew table, not scored by hand:
  wet (families)              union of the wetness classes of the family's species
  light, moist, soil, fertility, salt (species)   from Ellenberg values (PLANTATT, else Doring)
  height                      maximum vegetative height (families: tallest species)

Optional files written by scripts/enrich.py (the monthly GitHub job):
  data/auto/english_names.csv  kew_id, common, source_id
  data/auto/flowering.csv      kew_id, flower_start, flower_end, n_records, source_id
"""
import csv, json, math, sys
from collections import defaultdict
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "docs" / "data" / "species.json"
IN_SCOPE = lambda s: isinstance(s, str) and (s in ("N", "?N", "Neonative", "Neo-natd") or s.startswith("Arch"))
AUTO_SPECIES = ("light", "moist", "soil", "fertility", "salt")

def rows(name, optional=False):
    p = DATA / name
    if optional and not p.exists():
        return []
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def num(v):
    try:
        v = float(v)
        return None if math.isnan(v) else v
    except (TypeError, ValueError):
        return None

taxa, chars, states, sources, scores = (rows(n) for n in ["taxa.csv", "characters.csv", "states.csv", "sources.csv", "scores.csv"])
auto_names = rows("auto/english_names.csv", optional=True)
auto_flower = rows("auto/flowering.csv", optional=True)
prec = {s["source_id"]: int(s["precedence"]) for s in sources}

kew_all = pd.read_csv(DATA / "kew" / "BI_MAIN.csv", encoding="latin1", low_memory=False)
kew = kew_all.set_index("kew_id")
flora = kew_all[kew_all.extinct_species_marker.isna() & kew_all.StaceIV_nativity.map(IN_SCOPE)]
# drop synonym rows whose accepted name is itself in the flora (avoids listing a species twice)
flora = flora[~((flora.taxonomic_status != "Accepted") & flora.accepted_name.isin(flora.taxon_name_binom))]

# ---- validate ----
errors = []
allowed = defaultdict(set)
for s in states: allowed[s["char_id"]].add(s["state_id"])
taxon_ids = {t["kew_id"] for t in taxa} | set(flora.kew_id)
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
missing = sorted(set(flora.family) - fam_names)
if missing: print("Warning: families in the flora with no family row:", ", ".join(missing))
if errors:
    sys.exit("Validation failed:\n" + "\n".join(errors))

# ---- merge: for each taxon/character keep values from the highest-precedence source ----
by = defaultdict(list)
for r in scores: by[(r["kew_id"], r["char_id"])].append(r)
for r in auto_flower:
    for c in ("flower_start", "flower_end"):
        by[(r["kew_id"], c)].append(dict(value=r[c], source_id=r["source_id"]))
def best(tid, cid):
    rs = [r for r in by.get((tid, cid), []) if r["source_id"] in prec]
    if not rs: return [], None
    top = min(prec[r["source_id"]] for r in rs)
    keep = [r for r in rs if prec[r["source_id"]] == top]
    return [r["value"] for r in keep], keep[0]["source_id"]

def bands(v, spec):
    """Overlapping classes: spec = [(state, lo, hi), ...] inclusive."""
    return [] if v is None else [s for s, lo, hi in spec if lo <= v <= hi]

def ell(k, letter):
    v = num(getattr(k, f"{letter}_PLANTATT"))
    return v if v is not None else num(getattr(k, f"{letter}_Doring", None))

def wet_states(F):
    out = set()
    for f in F.dropna():
        out.add("water" if f >= 10 else "wet" if f >= 8 else "land")
    return sorted(out)

fam_chars = [c["char_id"] for c in chars if c["stage"] == "family" and c["kind"] in ("state", "feature") and c["char_id"] != "wet"]
bespoke = {c["stage"] for c in chars if c["stage"] not in ("family", "generic", "species", "all")}
generic_chars = [c["char_id"] for c in chars if c["stage"] == "generic" and c["kind"] in ("state", "feature")]

families, fam_lookup = [], {}
for t in [t for t in taxa if t["rank"] == "family"]:
    sub = flora[flora.family == t["name"]].sort_values("GB_Man_hectads_post2000", ascending=False)
    fam = dict(id=t["kew_id"], name=t["name"], common=t["common"], tip=t["tip"])
    for c in fam_chars:
        fam[c], _ = best(t["kew_id"], c)
    if fam.get("flowers") == ["none"]:  # flowerless (ferns, conifers): any answer about flower parts is a mismatch
        for c in ("inflor", "sym", "ovary", "stamens"):
            fam[c] = ["n/a"]
    fam["wet"] = wet_states(sub.F_PLANTATT)
    fam["height"] = num(sub.max_veg_height.max())
    fam["n"] = int(len(sub)); fam["n_native"] = int((sub.StaceIV_nativity == "N").sum())
    fam["n_common"] = int((sub.GB_Man_hectads_post2000.fillna(0) > 500).sum())
    fam["genera"] = list(dict.fromkeys(sub.genus))
    fam["top"] = [[r.taxon_name_binom, int(r.GB_Man_hectads_post2000) if not pd.isna(r.GB_Man_hectads_post2000) else None] for r in sub.head(12).itertuples()]
    fam["bespoke"] = t["name"] in bespoke
    families.append(fam); fam_lookup[t["name"]] = fam

extra = {t["kew_id"]: t for t in taxa if t["rank"] == "species"}
names = {r["kew_id"]: r["common"] for r in auto_names if r.get("common")}
species, sigs = [], defaultdict(list)
for k in flora.itertuples():
    kid = k.kew_id
    t = extra.get(kid, {})
    fam = k.family
    own_chars = [c["char_id"] for c in chars if c["stage"] == fam and c["kind"] in ("state", "feature")] or generic_chars
    sp = dict(id=kid, name=t.get("name") or k.taxon_name_binom, common=t.get("common") or names.get(kid, ""),
              tip=t.get("tip", ""), family=fam, genus=k.genus)
    scored = 0
    for c in own_chars:
        sp[c], _ = best(kid, c)
        scored += bool(sp[c])
    sp["described"] = scored >= max(2, len(own_chars) // 2)
    fs, _ = best(kid, "flower_start"); fe, _ = best(kid, "flower_end")
    sp["months"] = [int(fs[0]), int(fe[0])] if fs and fe else None
    L, F, R, N, S = (ell(k, x) for x in "LFRNS")
    sp["light"] = bands(L, [("shade", 1, 5), ("part", 5, 7), ("open", 7, 9)])
    sp["moist"] = bands(F, [("dry", 1, 4), ("damp", 4, 7), ("wet", 7, 9), ("water", 10, 12)])
    sp["soil"] = bands(R, [("acid", 1, 4), ("neutral", 4, 7), ("lime", 7, 9)])
    sp["fertility"] = bands(N, [("poor", 1, 3), ("average", 3, 6), ("rich", 6, 9)])
    sp["salt"] = [] if S is None else (["coast", "inland"] if 1 <= S <= 3 else ["coast"] if S >= 4 else ["inland"])
    h = num(k.max_veg_height); hf = False
    if h is None:
        hv, _ = best(kid, "max_height_m"); h = num(hv[0]) if hv else None; hf = h is not None
    gb, ie = num(k.GB_Man_hectads_post2000), num(k.Ire_hectads_post2000)
    if gb == 0 and ie == 0: gb = ie = None
    sp.update(status=k.StaceIV_nativity, height=h, height_filled=hf, F=F, R=R, gb=gb, ie=ie)
    species.append(sp)
    if sp["described"]:
        sigs[(fam,) + tuple(tuple(sorted(sp[c])) for c in own_chars)].append(sp["name"])

fsigs = defaultdict(list)
for f in families: fsigs[tuple(tuple(sorted(f[c])) for c in fam_chars + ["wet"])].append(f["name"])
for nm in list(fsigs.values()):
    if len(nm) > 1: print("Warning: identical family scores, the key cannot separate:", ", ".join(nm))
same = [nm for nm in sigs.values() if len(nm) > 1]
if same: print(f"Note: {len(same)} groups of described species share identical scores (habitat questions may still separate them)")

# compact: drop empty lists and false flags to keep the file small
def slim(d):
    return {k: v for k, v in d.items() if v not in ([], None, "", False)}
out = dict(
    characters=[dict(c, states=[[s["state_id"], s["label"]] for s in states if s["char_id"] == c["char_id"]]) for c in chars],
    sources=sources, families=families, species=[slim(s) for s in species], bespoke=sorted(bespoke))
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
n_desc = sum(s["described"] for s in species)
print(f"Wrote {OUT.relative_to(ROOT)}: {len(families)} families, {len(species)} species ({n_desc} described), {OUT.stat().st_size/1024:.0f} KB")
