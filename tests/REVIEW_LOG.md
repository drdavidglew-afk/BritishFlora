# Review log

What was changed in `data/scores.csv` and `data/taxa.csv` after the beginner test set (`tests/plants.csv`) was added, and why.
All new or changed score rows have `source_id = claude-bulk`, `confidence = reviewed`, `scored_by = Claude`, `date = 2026-11-01`.
Where an older `claude-draft` row existed for the same taxon and question it was replaced (the draft source outranks `claude-bulk` in `sources.csv`, so a new `claude-bulk` row could not otherwise win).
Everything here is still an unverified draft written from general botanical knowledge; none of it has been checked against specimens or a flora, and no wording was copied from a published flora.

## How the test set works

- `tests/plants.csv`: one row per plant, with `family_answers` (step 1) and `species_answers` (step 2), written as `question=answer;question=answer` using only questions in `data/characters.csv` and answers in `data/states.csv`.
  Each step has 3 to 6 answers (my reading of "3 to 6 answers per plant": per step). Descriptions were written from my knowledge of how each plant looks, before looking at the scores.
  Where a first draft had more than six species-step answers, habitat and month answers were dropped first, then size and hairiness.
- `tests/run_tests.py` applies the same rules as `mismatches()` and `render()` in `docs/index.html` and writes `tests/REPORT.md`.
  A plant **passes** only if at both steps the right family or species has no mismatches and is in the top 3 of the ranking the app would show.
- `tests/REPORT_baseline.md` is the first run, before any fix.

Not fixable from `scores.csv`: the habitat questions (light, wetness, soil, fertility, salt), maximum height and the family "Where is it growing?" answer are calculated from the Kew table.
Tests whose answers conflicted with those were revised (listed below) rather than "fixed".

## Batches

### Batch 1: first test run (60.2% of plants passing, 417 plants)

Family step (step 1), states added because a beginner could reasonably give them for a member of the family:
- **Asteraceae**: `inflor` + branched, spike (yarrow, goldenrod, butterbur, ragwort); `flowers` + small_green (mugwort); `lform` + grassy (goat's-beard).
- **Poaceae** `feature` + aromatic (sweet vernal-grass). **Cyperaceae**, **Juncaceae** `larr` + none (leafless-looking rushes, spike-rushes, club-rushes).
- **Brassicaceae** `feature` + aromatic, succulent (garlic mustard, sea-rocket); `fhabit` + water (watercress); `larr` + opp (honesty).
- **Caryophyllaceae** `larr` + whorl (corn spurrey). **Apiaceae** `feature` + bristly (hogweed, carrot); `inflor` + head (sanicle).
- **Plantaginaceae** `feature` + succulent (sea plantain). **Orchidaceae** `larr` + opp (twayblade). **Polygonaceae** `petals` + none (sorrels), `feature` + nodes (knotweeds).
- **Amaryllidaceae** `feature` + tri (three-cornered leek). **Asparagaceae** `feature` + spiny (butcher's-broom). **Campanulaceae** `feature` + bristly. **Crassulaceae** `inflor` + spike (navelwort).
- **Viburnaceae** `flowers` + small_green (moschatel). **Hypericaceae** `feature` + square. **Resedaceae** `flowers` + small_green (weld).

Species step (step 2):
- Added a missing alternative state for the right plant: Yorkshire-fog (`ghair` hairy, `grass_awn` awned or none), wall barley (`grass_head` cylinder), tormentil (`gsize` small as well as medium), gorse and western gorse (`gleaf` none: the leaves are spines), dame's-violet, snapdragon, willowherb-like lance-shaped leaves (`gleaf` narrow) for Persicaria amphibia, common comfrey, water forget-me-not, yellow loosestrife, Canadian waterweed, sweet chestnut, privet, butterfly-bush and teasel; finely divided umbellifers (cow parsley, wild carrot, hemlock, upright hedge-parsley, pignut) `gleaf` lobed as well as compound; celery-leaved buttercup `rfruit` spike; common hemp-nettle `leaf` heart (nettle-like); stork's-bill and biting stonecrop `gsize` small; wall-rue and yellow corydalis `gleaf` lobed; field horsetail and great horsetail `gleaf` narrow; meadow saxifrage `gleaf` heart; goat willow `ghair` woolly; the three spurges `gcolour` green_brown (yellow-green bracts); marsh gentian `gsize` large; frogbit `gleaf` oval (rounded); hazel `gcolour` yellow (male catkins); mind-your-own-business `gcolour` green_brown; wood-sorrel `ghair` hairless; hare's-foot clover `ghair` woolly; reedmace `gsize` large.
- Tests revised because my answer was unrealistic or conflicted with Kew-derived data (not score errors): Cladium (dropped "spiny"); Yorkshire gorse, cuckooflower, angelica, alexanders, early-purple orchid (dropped a habitat answer that conflicts with the Ellenberg value); wood avens, cowslip, broom, laburnum (flower size band); umbellifers and elder (dropped flower size: an umbel is not a 1 cm flower); wall-lettuce-like height bands for navelwort, moschatel, sea-lavender, butterwort, sundew (Kew maximum height is below the band I chose); silver birch and field pansy leaf shape; white willow hairiness; reedmace, branched bur-reed and bogbean "in water" rather than "wet ground" (the calculated family answer is `water` when Ellenberg F is 10 or more); tufted hair-grass "moist".
### Batch 2: Asteraceae, widespread species

- **white-rayed daisies are white, not also yellow (the yellow disc is not the flower colour; "yellow" searches were flooded with daisies)** (15): Bellis perennis `gcolour` white yellow → white; Leucanthemum vulgare `gcolour` white yellow → white; Achillea ptarmica `gcolour` white yellow → white; Tripleurospermum inodorum `gcolour` white yellow → white; Tripleurospermum maritimum `gcolour` white yellow → white; Tanacetum parthenium `gcolour` white yellow → white; Matricaria chamomilla `gcolour` white yellow → white; Galinsoga quadriradiata `gcolour` white yellow → white; Erigeron canadensis `gcolour` white yellow → white; Achillea millefolium `gcolour` white pink_red yellow → white pink_red; Erigeron acris `gcolour` blue_purple yellow → blue_purple; Erigeron karvinskianus `gcolour` white pink_red yellow → white pink_red; Symphyotrichum lanceolatum `gcolour` white blue_purple yellow → white blue_purple; Symphyotrichum novi-belgii `gcolour` blue_purple pink_red yellow → blue_purple pink_red; Tripolium pannonicum `gcolour` blue_purple yellow → blue_purple
- **purple heads: thistles and knapweeds can be called pink or violet, so both colours** (9): Cirsium vulgare `gcolour` pink_red → pink_red blue_purple; Cirsium palustre `gcolour` pink_red → pink_red blue_purple; Carduus crispus `gcolour` pink_red → pink_red blue_purple; Carduus nutans `gcolour` pink_red → pink_red blue_purple; Centaurea nigra `gcolour` pink_red → pink_red blue_purple; Centaurea scabiosa `gcolour` pink_red → pink_red blue_purple; Centaurea debeauxii `gcolour` pink_red → pink_red blue_purple; Cirsium acaule `gcolour` pink_red → pink_red blue_purple; Cirsium heterophyllum `gcolour` pink_red → pink_red blue_purple
- **burdocks: the hooked bracts feel prickly, so "spiny" must not reject them** (3): Arctium minus `aster_spiny` none → spiny none; Arctium lappa `aster_spiny` none → spiny none; Arctium nemorosum `aster_spiny` none → spiny none
- **orange-red heads: add pink_red** (1): Pilosella aurantiaca `gcolour` yellow → yellow pink_red

### Batch 3: Asteraceae (rarer), Caryophyllaceae, Apiaceae, Ranunculaceae

- **Lesser Stitchwort flowers are about 5-8 mm across (the tip wrongly said penny-sized, which is Greater Stitchwort): size small, tip corrected** (2): Stellaria graminea `gsize` medium → small; Stellaria graminea tip → "Slender, grass-like stitchwort with narrow, smooth leaves and loose, branched clusters of small white flowers (petals cleft almost to the base). Grassy banks, heaths and roadsides."
- **Common Mouse-ear flowers are about 1 cm across: small or medium** (1): Cerastium fontanum `gsize` small → small medium
- **finely divided umbellifer leaves are "lobed or deeply cut" as well as "separate leaflets"** (8): Chaerophyllum temulum `gleaf` compound → compound lobed; Aethusa cynapium `gleaf` compound → compound lobed; Myrrhis odorata `gleaf` compound → compound lobed; Foeniculum vulgare `gleaf` compound → compound lobed; Silaum silaus `gleaf` compound → compound lobed; Pimpinella saxifraga `gleaf` compound → compound lobed; Anthriscus caucalis `gleaf` compound → compound lobed; Torilis nodosa `gleaf` compound → compound lobed
- **buttercups with deeply cut, hand-like or three-parted leaves: a beginner may say "lobed" or "separate leaflets", so both** (4): Ranunculus repens `rleaf` compound → compound lobed; Ranunculus bulbosus `rleaf` compound → compound lobed; Ranunculus acris `rleaf` lobed → lobed compound; Ranunculus sardous `rleaf` compound → compound lobed
- **Traveller's-joy flowers are mostly a fluffy tuft of stamens with four creamy sepals** (1): Clematis vitalba `rform` open → open tufted
- **Galinsoga parviflora: white rays (yellow only in the disc)** (1): Galinsoga parviflora `gcolour` white yellow → white

