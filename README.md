# British Flora Key

An open, multi-access identification key to the wild plants of Britain and Ireland. Pick any features you can see, in any order; species are ranked by how many of your answers they contradict, so one wrong answer won't hide the right plant. It installs on a phone and works with no signal.

**Status:** prototype covering 20 common members of the mint and dead-nettle family (Lamiaceae). The morphological scores are unverified drafts and need checking against specimens or a flora.

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
  taxa.csv          species in the key: kew_id, name, common name, tip
  characters.csv    the questions the key asks
  states.csv        the allowed answers for each question
  scores.csv        one row per species × character × value, with its source
  sources.csv       every data source, its licence, attribution and precedence
  kew/BI_MAIN.csv   Kew BIFloraExplorer table (names, height, Ellenberg, hectads)
scripts/
  build.py          validates the data and writes docs/data/species.json
docs/               the app itself (served by GitHub Pages)
  index.html, sw.js, manifest.webmanifest, icons/, data/species.json
```

Every score records where it came from. When sources disagree, the one with the lowest `precedence` number in `sources.csv` wins (own observations 1, Kew 2, Claude drafts 9).

## Add or correct data

1. Edit the CSV files in `data/` (a spreadsheet is fine; save as CSV, UTF-8).
   - New species: add a row to `taxa.csv` using its Kew ID from `data/kew/BI_MAIN.csv`.
   - New score: add rows to `scores.csv`. Use `source_id` `own-obs` for your own observations and put a photo link in `evidence_url` if you have one.
2. Run `python3 scripts/build.py` (needs `pip install pandas`). It stops with a clear message if a value isn't an allowed state or a Kew ID doesn't exist, and warns if two species can't be told apart.
3. In `docs/sw.js`, bump `VERSION` (e.g. `core-v2`) so installed copies update.
4. Commit and push.

## Licences

- **Code:** MIT (see `LICENSE`).
- **Key data** (`data/taxa.csv`, `characters.csv`, `states.csv`, `scores.csv`): CC-BY 4.0, British Flora Key contributors.
- **Kew data** (`data/kew/`): from [BIFloraExplorer](https://github.com/RBGKew/BIFloraExplorer), MIT licence (© 2020 Marie Henniges) and Open Government Licence. Cite: Henniges M.C. et al. (2022) A taxonomic, genetic and ecological data resource for the vascular plants of Britain and Ireland. *Scientific Data* 9:1. https://doi.org/10.1038/s41597-021-01104-5
- Only add data or photos that are your own or licensed CC0 / CC-BY. Don't transcribe from copyrighted floras.
