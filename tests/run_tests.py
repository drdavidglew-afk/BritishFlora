"""Run the beginner test set (tests/plants.csv) against docs/data/species.json.

    python3 scripts/build.py && python3 tests/run_tests.py [--report tests/REPORT.md] [--fails]

Applies the same rules as docs/index.html (mismatches() and render()):
  * a "state" question: species with no value counts as 0.5 mismatch (unknown), a value that does not
    include the answer is 1 mismatch;
  * a "feature" question: the species must list the feature, otherwise 1 mismatch;
  * height: mismatch if the species' maximum height is below the chosen band;
  * month: mismatch if the species' flowering range excludes the month;
  * region: Ireland is a mismatch if the species has < 25 Irish hectads.
Ranking: fewest (mismatches + 0.5 x unknown) first; ties by family size of widespread species (families) or
described-first then hectads (species).

plants.csv columns: kew_id, name, common, family, family_answers, species_answers, note
Answers are "char=value;char=value". A plant passes when, at BOTH steps, the right family / species has no
mismatches and ranks in the top 3.
"""
import argparse, csv, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
J = json.load(open(ROOT / "docs" / "data" / "species.json", encoding="utf-8"))
CHARS = J["characters"]
BESPOKE, EXTENDS = set(J["bespoke"]), set(J.get("extends", []))
FAMS = {f["name"]: f for f in J["families"]}
SP = {s["id"]: s for s in J["species"]}
BY_FAM = {}
for s in J["species"]:
    BY_FAM.setdefault(s["family"], []).append(s)


def chars_for(stage):
    out = []
    for c in CHARS:
        st = c["stage"]
        if st == "all" or (stage == "family" and st == "family") or (
                stage != "family" and (st == "species" or st == (stage if stage in BESPOKE else "generic")
                                       or (stage in EXTENDS and st == stage))):
            out.append(c)
    return out


def in_season(m, ab):
    a, b = ab
    return a <= m <= b if a <= b else m >= a or m <= b


def mismatches(it, sel, stage):
    """Returns (list of reasons, number unknown). Mirrors mismatches() in docs/index.html."""
    ch = {c["char_id"]: c for c in chars_for(stage)}
    out, unk = [], 0
    for c, v in sel.items():
        if c not in ch:
            raise KeyError(f"'{c}' is not a question at the {stage} step")
        k = ch[c]
        if v not in {s[0] for s in k["states"]} and k["kind"] in ("state", "feature", "height", "region"):
            raise KeyError(f"'{v}' is not an answer to {c}")
        if k["kind"] == "state":
            have = it.get(c) or []
            if not have: unk += 1
            elif v not in have: out.append(f"{c} not {v}")
        elif k["kind"] == "feature":
            if v not in (it.get(c) or []): out.append(f"no {v}")
        elif k["kind"] == "height":
            if it.get("height") is not None and it["height"] < float(v): out.append(f"height max {it['height']} m")
        elif k["kind"] == "month":
            if it.get("months") and not in_season(int(v), it["months"]): out.append(f"month {v} outside {it['months']}")
        elif k["kind"] == "region" and v == "ie":
            if it.get("ie") is not None and it["ie"] < 25: out.append(f"rare in Ireland ({it['ie']})")
    return out, unk


def freq(s):
    return s.get("gb") if s.get("gb") is not None else (600 if s.get("common_nc") else 0)


def ranked(stage, sel):
    items = J["families"] if stage == "family" else BY_FAM.get(stage, [])
    rows = []
    for it in items:
        mm, unk = mismatches(it, sel, stage)
        rows.append((len(mm) + 0.5 * unk, mm, unk, it))
    if stage == "family":
        rows.sort(key=lambda r: (r[0], -r[3]["n_common"], -r[3]["n"]))
    else:
        rows.sort(key=lambda r: (r[0], 0 if r[3].get("described") else 1, -freq(r[3])))
    return rows


def parse(a):
    d = {}
    for part in (a or "").split(";"):
        part = part.strip()
        if part:
            c, v = part.split("=", 1)
            d[c.strip()] = v.strip()
    return d


def evaluate(row):
    fam = row["family"]
    res = dict(kew_id=row["kew_id"], name=row["name"], fam_name=fam)
    for stage, key, target in (("family", "family_answers", fam), ("species", "species_answers", row["kew_id"])):
        sel = parse(row[key])
        st = "family" if stage == "family" else fam
        rows = ranked(st, sel)
        pos = next(i for i, r in enumerate(rows) if (r[3]["name"] if stage == "family" else r[3]["id"]) == target)
        sc, mm, unk, it = rows[pos]
        fit = not mm
        nfit = sum(1 for r in rows if r[0] == 0)
        res[stage] = dict(n_answers=len(sel), fit=fit, mm=mm, unk=unk, rank=pos + 1, top3=pos < 3, n_fit=nfit,
                          ahead=[(r[3]["name"], r[0]) for r in rows[:3]], ok=fit and pos < 3)
    res["ok"] = res["family"]["ok"] and res["species"]["ok"]
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plants", default=str(ROOT / "tests" / "plants.csv"))
    ap.add_argument("--report", default=None)
    ap.add_argument("--fails", action="store_true", help="print failing plants")
    a = ap.parse_args()
    with open(a.plants, newline="", encoding="utf-8") as f:
        plants = list(csv.DictReader(f))
    results = []
    for p in plants:
        if p["kew_id"] not in SP:
            sys.exit(f"unknown kew_id {p['kew_id']} ({p['name']})")
        results.append(evaluate(p))
    n = len(results)
    cnt = lambda pred: sum(1 for r in results if pred(r))
    lines = []
    P = lines.append
    P("# Test report\n")
    P(f"{n} plants, {len({r['fam_name'] for r in results})} families. Data: docs/data/species.json.\n")
    P("| | family fits all answers | family in top 3 | species fits all answers | species in top 3 | both steps pass |")
    P("|---|---|---|---|---|---|")
    P(f"| plants | {cnt(lambda r: r['family']['fit'])} | {cnt(lambda r: r['family']['top3'])} | "
      f"{cnt(lambda r: r['species']['fit'])} | {cnt(lambda r: r['species']['top3'])} | **{cnt(lambda r: r['ok'])}** |")
    P(f"\nOverall pass rate: **{100*cnt(lambda r: r['ok'])/n:.1f}%**. Rank 1 at family step: {cnt(lambda r: r['family']['rank']==1)}; "
      f"rank 1 at species step: {cnt(lambda r: r['species']['rank']==1)}.\n")
    fails = [r for r in results if not r["ok"]]
    P(f"## Failures ({len(fails)})\n")
    for r in fails:
        for stage in ("family", "species"):
            s = r[stage]
            if s["ok"]: continue
            why = "does not fit: " + "; ".join(s["mm"]) if not s["fit"] else f"fits but ranks {s['rank']} ({s['n_fit']} fit all answers)"
            top = ", ".join(f"{n} ({sc})" for n, sc in s["ahead"])
            P(f"- **{r['name']}** ({r['fam_name']}), {stage} step: {why}. Top: {top}")
    P("\n## All plants\n")
    P("| plant | family | fam answers | fam fit | fam rank | sp answers | sp fit | sp rank (of fitting) |")
    P("|---|---|---|---|---|---|---|---|")
    for r in results:
        f, s = r["family"], r["species"]
        P(f"| {r['name']} | {r['fam_name']} | {f['n_answers']} | {'yes' if f['fit'] else 'NO'} | {f['rank']} | "
          f"{s['n_answers']} | {'yes' if s['fit'] else 'NO'} | {s['rank']} ({s['n_fit']}) |")
    text = "\n".join(lines) + "\n"
    if a.report:
        Path(a.report).write_text(text, encoding="utf-8")
    head = text.split("## All plants")[0]
    print(head if a.fails or not a.report else head.split("## Failures")[0])
    if a.fails:
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
