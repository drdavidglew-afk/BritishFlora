"""Build docs/data/species.json from the CSV files in data/.

Run from the repository root:  python3 scripts/build.py
Needs pandas (pip install pandas).
"""
import csv, json, math, sys
from collections import defaultdict
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "docs" / "data" / "species.json"

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
kew = pd.read_csv(DATA / "kew" / "BI_MAIN.csv", encoding="latin1", low_memory=False).set_index("kew_id")

# ---- validate ----
errors = []
allowed = defaultdict(set)
for s in states: allowed[s["char_id"]].add(s["state_id"])
taxon_ids = {t["kew_id"] for t in taxa}
for i, r in enumerate(scores, start=2):
    if r["kew_id"] not in taxon_ids: errors.append(f"scores.csv line {i}: unknown kew_id {r['kew_id']}")
    if r["source_id"] not in prec: errors.append(f"scores.csv line {i}: unknown source {r['source_id']}")
    if r["char_id"] in allowed and r["value"] not in allowed[r["char_id"]]:
        errors.append(f"scores.csv line {i}: '{r['value']}' is not a state of {r['char_id']}")
for t in taxa:
    if t["kew_id"] not in kew.index: errors.append(f"taxa.csv: {t['name']} kew_id {t['kew_id']} not in Kew table")
if errors:
    sys.exit("Validation failed:\n" + "\n".join(errors))

# ---- merge: for each taxon/character keep values from the highest-precedence source ----
by = defaultdict(list)
for r in scores: by[(r["kew_id"], r["char_id"])].append(r)
def best(kid, cid):
    rs = by.get((kid, cid), [])
    if not rs: return [], None
    top = min(prec[r["source_id"]] for r in rs)
    keep = [r for r in rs if prec[r["source_id"]] == top]
    return [r["value"] for r in keep], keep[0]["source_id"]

state_chars = [c["char_id"] for c in chars if c["kind"] == "state"]
species, sigs = [], defaultdict(list)
for t in taxa:
    k = kew.loc[t["kew_id"]]
    sp = dict(kew_id=t["kew_id"], name=t["name"], common=t["common"], tip=t["tip"], group=t["group"], src={})
    for c in state_chars:
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
    sigs[tuple(tuple(sorted(sp[c])) for c in state_chars)].append(t["name"])

for names in sigs.values():
    if len(names) > 1: print("Warning: identical scores, the key cannot separate:", ", ".join(names))

out = dict(
    built="", characters=[dict(c, states=[[s["state_id"], s["label"]] for s in states if s["char_id"] == c["char_id"]]) for c in chars],
    sources=sources, species=species)
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"Wrote {OUT.relative_to(ROOT)}: {len(species)} species, {OUT.stat().st_size/1024:.0f} KB")
