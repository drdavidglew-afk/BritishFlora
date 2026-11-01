# British Flora Key

An open, multi-access identification key to the wild plants of Britain and Ireland. Pick any features you can see, in any order; species are ranked by how many of your answers they contradict, so one wrong answer won't hide the right plant. It installs on a phone and works with no signal.

**Status:**
- **Step 1, family key:** all 144 families of native and established plants in the Kew list (about 2,600 species), scored on 15 general features.
- **Step 2, species keys:** every family, covering all 2,564 native, ancient and naturalised species in the Kew list.
  - Every species can be narrowed by Kew data with no hand scoring: light, wetness, soil pH, fertility, salt (Ellenberg values), height and distribution.
  - Described so far: 653 species. The mint family (20 species) and buttercup family (45 species) have their own questions; other families use a standard set (flower colour and size, leaf shape and edge, hairiness). That covers the widespread species (in more than 500 hectads) of every family except the daisy, grass, rose and sedge families, which come next, plus about 25 common species missing from Kew's distribution counts.
  - Species not yet described are shown, but ranked below described ones.
  - Most widespread species were bulk-drafted by a smaller Claude model and spot-checked by Claude (source `claude-bulk`); all scores are unverified until checked by a botanist.

All feature scores are unverified drafts written by Claude and need checking against specimens or a flora. In a test with 25 well-known plants described as a beginner would, each landed in the correct family with no mismatches.

## Use it

Once GitHub Pages is switched on (below), the key lives at
`https://drdavidglew-afk.github.io/BritishFlora/`

- **Android / Chrome:** open the link, then menu → *Install app*.
- **iPhone:** open in Safari, then Share → *Add to Home Screen*. Install it rather than bookmarking, so iOS keeps the offline copy.

## Switch on GitHub Pages (one-off)

Settings → Pages → *Build and deployment* → Source: **Deploy from a branch** → Branch: **main**, folder **/docs** → Save. The site appears a minute or two later.

## How it's organised

```
data/
  taxa.csv          families (rank=family, id "fam:<Family>") and species (rank=species, Kew ID)
  characters.csv    the questions the key asks; stage = family (step 1), a family name (that family's own species questions),
                    generic (standard species questions for other families), species (every species key) or all
  states.csv        the allowed answers for each question
  scores.csv        one row per species × character × value, with its source
  sources.csv       every data source, its licence, attribution and precedence
  kew/BI_MAIN.csv   Kew BIFloraExplorer table (names, height, Ellenberg, hectads)
scripts/
  build.py          validates the data and writes docs/data/species.json
docs/               the app itself (served by GitHub Pages)
  index.html, sw.js, manifest.webmanifest, icons/, data/species.json
```

Species inherit their family's step 1 scores unless they have their own. Two features are calculated from the Kew table rather than scored by hand: a family's "Where is it growing?" (from its species' Ellenberg wetness values) and maximum height.

Every score records where it came from. When sources disagree, the one with the lowest `precedence` number in `sources.csv` wins (own observations 1, Kew 2, Claude drafts 9).

## Add or correct data

1. Edit the CSV files in `data/` (a spreadsheet is fine; save as CSV, UTF-8).
   - New species: add a row to `taxa.csv` (rank `species`, its family, its Kew ID from `data/kew/BI_MAIN.csv`).
   - New species key for a family: add that family's own questions to `characters.csv` with `stage` set to the family name, their answers to `states.csv`, then score the species. The app adds a "Key out the species" button automatically.
   - New score: add rows to `scores.csv`. Use `source_id` `own-obs` for your own observations and put a photo link in `evidence_url` if you have one.
2. Run `python3 scripts/build.py` (needs `pip install pandas`). It stops with a clear message if a value isn't an allowed state or a Kew ID doesn't exist, and warns if two species can't be told apart.
3. In `docs/sw.js`, bump `VERSION` (e.g. `core-v2`) so installed copies update.
4. Commit and push.

## Monthly open-data update

A GitHub job (`.github/workflows/enrich.yml`) runs `scripts/enrich.py` on the 2nd of each month, or whenever you start it from the **Actions** tab ("Fetch English names and flowering months" → *Run workflow*). It:

- fetches English names from **Wikidata** (CC0) into `data/auto/english_names.csv`;
- works out flowering months from **iNaturalist** observations in Britain and Ireland marked "Flowering" (counts per month only) into `data/auto/flowering.csv`;
- rebuilds the key and commits the result.

Hand-entered names and observations still take priority. The flowering run takes one to two hours, because iNaturalist asks for about one request a second; it costs nothing.

## Licences

- **Code:** MIT (see `LICENSE`).
- **Key data** (`data/taxa.csv`, `characters.csv`, `states.csv`, `scores.csv`): CC-BY 4.0, British Flora Key contributors.
- **Kew data** (`data/kew/`): from [BIFloraExplorer](https://github.com/RBGKew/BIFloraExplorer), MIT licence (© 2020 Marie Henniges) and Open Government Licence. Cite: Henniges M.C. et al. (2022) A taxonomic, genetic and ecological data resource for the vascular plants of Britain and Ireland. *Scientific Data* 9:1. https://doi.org/10.1038/s41597-021-01104-5
- Only add data or photos that are your own or licensed CC0 / CC-BY. Don't transcribe from copyrighted floras.
