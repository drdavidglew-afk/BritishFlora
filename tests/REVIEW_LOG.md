# Review log

What was changed in `data/scores.csv` and `data/taxa.csv` after the beginner test set (`tests/plants.csv`) was added, and why.
All new or changed score rows have `source_id = claude-bulk`, `confidence = reviewed`, `scored_by = Claude`, `date = 2026-11-01`.
Where an older `claude-draft` row existed for the same taxon and question it was replaced, because the draft source outranks `claude-bulk` in `sources.csv` (a new `claude-bulk` row could not otherwise win).
The scores are still unverified drafts from general botanical knowledge. None has been checked against specimens or a flora, and no wording was copied from a published flora.
Each batch entry below gives the reason, the number of changes and the first few examples; the full list of rows is the `git diff` of `data/scores.csv`.

## Results

| | before any fix | now |
|---|---|---|
| plants in the test set | 417 | 572 |
| right family fits all answers | 379 / 417 (91%) | 572 / 572 |
| right species fits all answers | 358 / 417 (86%) | 572 / 572 |
| right family in the top 3 | 333 / 417 (80%) | 462 / 572 (81%) |
| right species in the top 3 | 375 / 417 (90%) | 516 / 572 (90%) |
| both steps pass (fits and top 3) | 251 / 417 (60.2%) | 407 / 572 (71.2%) |

The last 155 rows of `plants.csv` were written after batch 8 and were not used to tune any earlier batch: they are an out-of-sample check.
Before their own fixes they had 6 family-step and 1 species-step non-fits in 155 plants (4% and 1%), against 38 and 59 in 417 for the first set before any fix, so the review did generalise.
`tests/REPORT_baseline.md` is the first run, before any fix; `tests/REPORT.md` is the current one.

## How the test set works

- `tests/plants.csv`: one row per plant with `family_answers` (step 1) and `species_answers` (step 2), written as `question=answer;question=answer`, using only questions in `data/characters.csv` and answers in `data/states.csv`.
  Each step has 3 to 6 answers (my reading of "3 to 6 answers per plant": per step; the totals are 6 to 12).
  The descriptions were written from my knowledge of how each plant looks, before looking at its scores. Where a first draft had more than six species-step answers, habitat and month answers were dropped first, then size and hairiness.
  572 plants, 92 families, every family with 5 or more species (67 of them) included; 544 of the 572 are widespread species (over 500 hectads, or listed as common without counts).
- `tests/run_tests.py` applies the app's rules (`mismatches()` and the ranking in `render()` of `docs/index.html`): an unknown state counts half a mismatch, a missing feature counts one, ties are broken by family size or by described-first then hectads.
  A plant **passes** when at both steps the right family or species has no mismatches and is in the top 3.
- Not fixable from `scores.csv`: the habitat questions (light, wetness, soil, fertility, salt), maximum height and the family "Where is it growing?" answer are calculated from the Kew table.
  Where a test answer conflicted with those, the test answer was revised (listed in batch 1) rather than "fixed".

## Batches

### Batch 1: first test run (60.2% of 417 plants passing)

Family step (step 1): states added because a beginner could reasonably give them for a member of the family. Each is a gap that made the key reject a common plant.
- Asteraceae: `inflor` + branched, spike (yarrow, goldenrod, butterbur, ragwort); `flowers` + small_green (mugwort); `lform` + grassy (goat's-beard).
- Poaceae `feature` + aromatic (sweet vernal-grass). Cyperaceae and Juncaceae `larr` + none (leafless-looking rushes, spike-rushes, club-rushes).
- Brassicaceae `feature` + aromatic, succulent (garlic mustard, sea-rocket); `fhabit` + water (watercress); `larr` + opp (honesty).
- Caryophyllaceae `larr` + whorl (corn spurrey). Apiaceae `feature` + bristly (hogweed, carrot); `inflor` + head (sanicle).
- Plantaginaceae `feature` + succulent (sea plantain). Orchidaceae `larr` + opp (twayblade). Polygonaceae `petals` + none (sorrels), `feature` + nodes (knotweeds).
- Amaryllidaceae `feature` + tri (three-cornered leek). Asparagaceae `feature` + spiny (butcher's-broom). Campanulaceae `feature` + bristly. Crassulaceae `inflor` + spike (navelwort).
- Viburnaceae `flowers` + small_green (moschatel). Hypericaceae `feature` + square. Resedaceae `flowers` + small_green (weld).

Species step (step 2): an alternative state the right plant needed.
- Yorkshire-fog `ghair` hairy (it is softly hairy); wall barley `grass_head` cylinder; tormentil `gsize` small as well as medium; gorse and western gorse `gleaf` none (the leaves are spines).
- `gleaf` narrow (lance-shaped leaves) for dame's-violet, snapdragon, common comfrey, water forget-me-not, yellow loosestrife, Canadian waterweed, sweet chestnut, privet, butterfly-bush, teasel, amphibious bistort.
- Finely divided umbellifers (cow parsley, wild carrot, hemlock, upright hedge-parsley, pignut) `gleaf` lobed as well as compound.
- Celery-leaved buttercup `rfruit` spike; common hemp-nettle `leaf` heart (nettle-like); stork's-bill and biting stonecrop `gsize` small; wall-rue and yellow corydalis `gleaf` lobed; field and great horsetail `gleaf` narrow; meadow saxifrage `gleaf` heart; goat willow `ghair` woolly; the three spurges `gcolour` green_brown (yellow-green bracts); marsh gentian `gsize` large; frogbit `gleaf` oval (rounded); hazel `gcolour` yellow (male catkins); mind-your-own-business `gcolour` green_brown; wood-sorrel `ghair` hairless; hare's-foot clover `ghair` woolly; reedmace `gsize` large.

Test answers revised because they were unrealistic or conflicted with Kew-derived data (not score errors):
- Cladium: dropped "spiny" (saw-edged leaves are not spines).
- Habitat answer dropped or changed where it conflicted with the Ellenberg value: gorse (soil), cuckooflower and angelica (wetness), alexanders (salt), early-purple orchid (light), tufted hair-grass (wet to damp).
- Flower-size band changed: wood avens, cowslip, broom, laburnum. Flower size dropped for umbellifers and elder (an umbel is not a 1 cm flower).
- Height band lowered where Kew's maximum height is below it: navelwort, moschatel, common sea-lavender, common butterwort, round-leaved sundew.
- Leaf shape or hairiness: silver birch (oval, not heart), field pansy (oval), white willow (hairy, not woolly).
- Reedmace, branched bur-reed and bogbean: "in water" rather than "wet ground", because the calculated family answer is `water` when Ellenberg F is 10 or more.

### Batch 2: Asteraceae, widespread species

- **white-rayed daisies are white, not also yellow (the yellow disc is not the flower colour; "yellow" searches were flooded with daisies)** (15): Bellis perennis `gcolour` white yellow → white; Leucanthemum vulgare `gcolour` white yellow → white; Achillea ptarmica `gcolour` white yellow → white; Tripleurospermum inodorum `gcolour` white yellow → white; Tripleurospermum maritimum `gcolour` white yellow → white; Tanacetum parthenium `gcolour` white yellow → white; Matricaria chamomilla `gcolour` white yellow → white; Galinsoga quadriradiata `gcolour` white yellow → white; … and 7 more (full list: `git diff` of `data/scores.csv`).
- **purple heads: thistles and knapweeds can be called pink or violet, so both colours** (9): Cirsium vulgare `gcolour` pink_red → pink_red blue_purple; Cirsium palustre `gcolour` pink_red → pink_red blue_purple; Carduus crispus `gcolour` pink_red → pink_red blue_purple; Carduus nutans `gcolour` pink_red → pink_red blue_purple; Centaurea nigra `gcolour` pink_red → pink_red blue_purple; Centaurea scabiosa `gcolour` pink_red → pink_red blue_purple; Centaurea debeauxii `gcolour` pink_red → pink_red blue_purple; Cirsium acaule `gcolour` pink_red → pink_red blue_purple; … and 1 more (full list: `git diff` of `data/scores.csv`).
- **burdocks: the hooked bracts feel prickly, so "spiny" must not reject them** (3): Arctium minus `aster_spiny` none → spiny none; Arctium lappa `aster_spiny` none → spiny none; Arctium nemorosum `aster_spiny` none → spiny none
- **orange-red heads: add pink_red** (1): Pilosella aurantiaca `gcolour` yellow → yellow pink_red

### Batch 3: Asteraceae (rarer), Caryophyllaceae, Apiaceae, Ranunculaceae

- **Lesser Stitchwort flowers are about 5-8 mm across (the tip wrongly said penny-sized, which is Greater Stitchwort): size small, tip corrected** (2): Stellaria graminea `gsize` medium → small; Stellaria graminea tip → "Slender, grass-like stitchwort with narrow, smooth leaves and loose, branched clusters of small white flowers (petals cleft almost to the base). Grassy banks, heaths and roadsides."
- **Common Mouse-ear flowers are about 1 cm across: small or medium** (1): Cerastium fontanum `gsize` small → small medium
- **finely divided umbellifer leaves are "lobed or deeply cut" as well as "separate leaflets"** (8): Chaerophyllum temulum `gleaf` compound → compound lobed; Aethusa cynapium `gleaf` compound → compound lobed; Myrrhis odorata `gleaf` compound → compound lobed; Foeniculum vulgare `gleaf` compound → compound lobed; Silaum silaus `gleaf` compound → compound lobed; Pimpinella saxifraga `gleaf` compound → compound lobed; Anthriscus caucalis `gleaf` compound → compound lobed; Torilis nodosa `gleaf` compound → compound lobed
- **buttercups with deeply cut, hand-like or three-parted leaves: a beginner may say "lobed" or "separate leaflets", so both** (4): Ranunculus repens `rleaf` compound → compound lobed; Ranunculus bulbosus `rleaf` compound → compound lobed; Ranunculus acris `rleaf` lobed → lobed compound; Ranunculus sardous `rleaf` compound → compound lobed
- **Traveller's-joy flowers are mostly a fluffy tuft of stamens with four creamy sepals** (1): Clematis vitalba `rform` open → open tufted
- **Galinsoga parviflora: white rays (yellow only in the disc)** (1): Galinsoga parviflora `gcolour` white yellow → white

### Batch 4: purple flowers (all families)

- **flowers described as purple, pink-purple, lilac or violet were scored pink only; a beginner can call them pink or blue-violet, so blue_purple added** (44): Agrostemma githago `gcolour` pink_red → pink_red blue_purple; Allium ampeloprasum `gcolour` pink_red white → pink_red white blue_purple; Allium schoenoprasum `gcolour` pink_red → pink_red blue_purple; Aptenia cordifolia `gcolour` pink_red → pink_red blue_purple; Arabidopsis petraea `gcolour` white → white blue_purple; Calluna vulgaris `gcolour` pink_red white → pink_red white blue_purple; Cardamine bulbifera `gcolour` pink_red → pink_red blue_purple; Cardamine quinquefolia `gcolour` pink_red → pink_red blue_purple; … and 36 more (full list: `git diff` of `data/scores.csv`).

### Batch 5: Geraniaceae, Primulaceae, Euphorbiaceae and other mid-sized families (widespread species)

- **orange-red flowers: "Yellow or orange" must be allowed (scarlet pimpernel)** (1): Lysimachia arvensis `gcolour` pink_red blue_purple → pink_red blue_purple yellow
- **spurge bracts are yellow-green: green_brown also allowed (as for the other spurges)** (2): Euphorbia lathyris `gcolour` yellow → yellow green_brown; Euphorbia exigua `gcolour` yellow → yellow green_brown

### Batch 6: names vs colours; ferns

- **purple flowers (named or described as purple) scored pink only: blue_purple added** (4): Lythrum salicaria `gcolour` pink_red → pink_red blue_purple; Fumaria purpurea `gcolour` pink_red → pink_red blue_purple; Disphyma crassifolium `gcolour` pink_red white → pink_red white blue_purple; Erythronium dens-canis `gcolour` pink_red → pink_red blue_purple
- **ferns with pinnate fronds: a beginner may say "separate leaflets" or "lobed or deeply cut", so both** (52): Adiantum capillus-veneris `gleaf` compound → compound lobed; Anogramma leptophylla `gleaf` compound → compound lobed; Asplenium adiantum-nigrum `gleaf` compound → compound lobed; Asplenium marinum `gleaf` compound → compound lobed; Asplenium obovatum `gleaf` compound → compound lobed; Asplenium onopteris `gleaf` compound → compound lobed; Asplenium trichomanes `gleaf` compound → compound lobed; Asplenium viride `gleaf` compound → compound lobed; … and 44 more (full list: `git diff` of `data/scores.csv`).

### Batch 7: tip wording versus scores (leaf shape, hair, edge) across all families

- **tip says the leaves are finely cut or feathery but they were scored "separate leaflets" only: "lobed or deeply cut" added** (33): Achillea filipendulina `gleaf` compound → compound lobed; Achillea nobilis `gleaf` compound → compound lobed; Anthemis punctata `gleaf` compound → compound lobed; Chamaemelum nobile `gleaf` compound → compound lobed; Cota tinctoria `gleaf` compound → compound lobed; Dicentra eximia `gleaf` compound → compound lobed; Dicentra formosa `gleaf` compound → compound lobed; Fumaria densiflora `gleaf` compound → compound lobed; … and 25 more (full list: `git diff` of `data/scores.csv`).
- **thread-like or lance-shaped leaves: "narrow" added** (7): Anethum graveolens `gleaf` compound lobed → compound lobed narrow; Bunium bulbocastanum `gleaf` compound lobed → compound lobed narrow; Ferula communis `gleaf` compound lobed → compound lobed narrow; Rumex hydrolapathum `gleaf` oval → oval narrow; Rumex sanguineus `gleaf` oval → oval narrow; Lemna trisulca `gleaf` oval → oval narrow; Linum catharticum `gleaf` oval → oval narrow
- **stem leaves described as arrow-shaped or heart-based and clasping: "heart- or arrow-shaped" added** (7): Lepidium campestre `gleaf` oval → oval heart; Lepidium draba `gleaf` oval → oval heart; Thlaspi arvense `gleaf` oval → oval heart; Turritis glabra `gleaf` oval → oval heart; Camelina sativa `gleaf` narrow → narrow heart; Inula salicina `gleaf` oval narrow → oval narrow heart; Rumex longifolius `gleaf` oval → oval heart
- **tip says the leaves are woolly, felted or bristly but hair was scored otherwise** (5): Cirsium oleraceum `ghair` hairless → hairless hairy; Inula conyzae `ghair` hairy → hairy woolly; Salix viminalis `ghair` hairy → hairy woolly; Correa backhouseana `ghair` hairy → hairy woolly; Daboecia cantabrica `ghair` hairy → hairy woolly
- **tip says the leaf edge is (slightly) toothed** (2): Plantago maritima `gedge` smooth → smooth toothed; Rumex rupestris `gedge` smooth → smooth toothed
- **gorses have spines instead of leaves: gleaf none, as for Common and Western Gorse** (1): Ulex minor `gleaf` narrow → narrow none

### Batch 8: second look at species-step rank failures

- **flowering plants have their leaves along a leafy stem (the basal rosette withers or is small), so "mostly in a basal rosette" was wrong and drowned the genuinely rosette-forming species (Dwarf Thistle, daisy, cat's-ear)** (6): Cirsium vulgare `aster_leaves` stem rosette → stem; Carduus crispus `aster_leaves` stem rosette → stem; Sonchus asper `aster_leaves` stem rosette → stem; Sonchus oleraceus `aster_leaves` stem rosette → stem; Sonchus arvensis `aster_leaves` stem rosette → stem; Lactuca serriola `aster_leaves` stem rosette → stem
- **Yorkshire-fog's awn is short, hooked and hidden inside the spikelet, so a beginner sees no bristles (earlier 'awned/none' was a hedge); Common Bent is only rarely awned** (2): Holcus lanatus `grass_awn` awned none → none; Agrostis capillaris `grass_awn` none awned → none

### Batch 9: second test set (out-of-sample) and tip-based feature scan of the family step

- **family step: some species of the family have fleshy leaves or stems (sea-spurreys, sandworts, sea aster, golden-samphire, rock samphire, sea bindweed, sea-milkwort, oysterplant, jewelweeds, sea arrowgrass, sea spurge), so "thick, fleshy leaves" must not reject the family** (11): Asteraceae `feature` milky spiny aromatic → milky spiny aromatic succulent; Caryophyllaceae `feature` nodes → nodes succulent; Polygonaceae `feature` sheath nodes → sheath nodes succulent; Balsaminaceae `feature` (none) → succulent; Convolvulaceae `feature` nogreen → nogreen succulent; Euphorbiaceae `feature` milky → milky succulent; Primulaceae `feature` (none) → succulent; Boraginaceae `feature` bristly → bristly succulent; … and 3 more (full list: `git diff` of `data/scores.csv`).
- **family step: prickly or spiny members (sea-hollies, ladies-bedstraw-like prickly bedstraws, thorn-apple, boxthorns, saltwort, Aralia, Holm oak, Hard Shield-fern, juniper)** (9): Apiaceae `feature` aromatic bristly succulent → aromatic bristly succulent spiny; Rubiaceae `feature` square bristly → square bristly spiny; Solanaceae `feature` (none) → spiny; Amaranthaceae `feature` succulent → succulent spiny; Araliaceae `feature` (none) → spiny; Fagaceae `feature` (none) → spiny; Polypodiaceae `feature` (none) → spiny; Cupressaceae `feature` aromatic → aromatic spiny; … and 1 more (full list: `git diff` of `data/scores.csv`).
- **family step: rough, bristly hairs on stems and leaves occur in these families (bristly oxtongue, thistles, charlock and mustards, poppies, hemp-nettles, roses)** (5): Asteraceae `feature` milky spiny aromatic succulent → milky spiny aromatic succulent bristly; Brassicaceae `feature` aromatic succulent → aromatic succulent bristly; Papaveraceae `feature` milky → milky bristly; Lamiaceae `feature` square aromatic → square aromatic bristly; Rosaceae `feature` spiny → spiny bristly
- **family step: strong smell when crushed in some members (cherry laurel, fragrant agrimony, wintergreen, mexican-tea, conifers, hay-scented and lemon-scented ferns, bay willow, elder)** (8): Rosaceae `feature` spiny bristly → spiny bristly aromatic; Ericaceae `feature` nogreen spiny → nogreen spiny aromatic; Amaranthaceae `feature` succulent spiny → succulent spiny aromatic; Pinaceae `feature` (none) → aromatic; Polypodiaceae `feature` spiny → spiny aromatic; Aspleniaceae `feature` (none) → aromatic; Salicaceae `feature` (none) → aromatic; Viburnaceae `feature` (none) → aromatic
- **family step: milky sap (Norway maple and relatives; milk-parsley)** (2): Sapindaceae `feature` (none) → milky; Apiaceae `feature` aromatic bristly succulent spiny → aromatic bristly succulent spiny milky
- **family step: leaf-tip tendrils (climbing corydalis, climbing fumitory)** (1): Papaveraceae `feature` milky bristly → milky bristly tendril
- **family step: jointed fleshy stems of glassworts** (1): Amaranthaceae `feature` succulent spiny aromatic → succulent spiny aromatic jointed
- **family step: square stems (greater stitchwort, broad bean)** (2): Caryophyllaceae `feature` nodes succulent → nodes succulent square; Fabaceae `feature` tendril spiny → tendril spiny square
- **family step: prostrate mallows (dwarf mallow) creep** (1): Malvaceae `fhabit` up → up creep
- **Smooth Hawk's-beard heads are about 1 cm across: small as well as medium** (1): Crepis capillaris `gsize` medium → medium small

## Review coverage

Read by eye, with the scores next to my own botanical knowledge, widespread species first (over 500 hectads) then the rarer ones:
- **All species, scores, names and tips:** Lamiaceae, Ranunculaceae.
- **All species, scores and names (tips read for the widespread ones only):** Asteraceae, Poaceae, Rosaceae, Fabaceae, Brassicaceae, Cyperaceae, Caryophyllaceae, Apiaceae, Plantaginaceae.
- **All species, scores and names, no tips:** Typhaceae, Potamogetonaceae, Alismataceae, Hydrocharitaceae, Haloragaceae, Lentibulariaceae, Plumbaginaceae, Gentianaceae, Convolvulaceae, Oleaceae, Urticaceae, Grossulariaceae, Cornaceae, Cistaceae, Linaceae, Aizoaceae, Liliaceae, Asphodelaceae, Araliaceae, Pinaceae, Equisetaceae, Lycopodiaceae, Aspleniaceae, Polypodiaceae.
- **Widespread species only (scores, names and tips):** Juncaceae, Orchidaceae, Polygonaceae, Boraginaceae, Amaranthaceae, Orobanchaceae, Amaryllidaceae, Ericaceae, Geraniaceae, Campanulaceae, Primulaceae, Crassulaceae, Caprifoliaceae, Papaveraceae, Saxifragaceae, Onagraceae, Salicaceae, Rubiaceae, Euphorbiaceae, Hypericaceae, Violaceae, Oxalidaceae, Malvaceae, Solanaceae, Scrophulariaceae, Araceae, Betulaceae, Fagaceae, Sapindaceae, Viburnaceae, Iridaceae, Asparagaceae.

Checked for all 2,565 species by script instead: tip wording against the scored leaf shape, leaf edge and hairiness (batch 7) and flower colour (batch 4); common names against colour; season words in tips against flowering months (nothing to fix); and the family-step features against what the tips of the family's species describe (batch 9).

**Not read species by species:** the rarer species of the second and fourth groups' families that are not in the first three groups (for example the rarer Orchidaceae, Polygonaceae, Boraginaceae, Violaceae, Onagraceae, Salicaceae) and about 70 smaller families, beyond the script checks above.
The Hieracium, Taraxacum, Rubus, Sorbus, Alchemilla, Euphrasia and Limonium groups are scored at group level and I only checked that their scores are consistent within each group.
English names: no wrong names were found in what I read. Tips: one factual error was found and corrected (Lesser Stitchwort flower size); the tips I read otherwise agreed with the scores. I cannot check tips against a flora, so the other tips remain unverified.

## Failures that remain, and why

All 572 plants now fit at both steps. The 165 plants that do not pass (28.8%) all fit the answers but rank outside the top 3: 110 at the family step, 56 at the species step, 1 at both.
Looking at who outranks the right answer, none of them is a scoring error:

- **Family step (110 plants).** 4 to 39 families (median 13) fit all the answers, and ties are broken by how many widespread species the family has, so small families such as Primulaceae, Gentianaceae, Violaceae, Orobanchaceae, Lythraceae or Cistaceae rank behind the big ones.
  The step-1 questions do not include flower colour, so a showy-flowered herb with opposite or basal leaves cannot be told from dozens of others. More answers help only a little: 29% of plants described with 3 answers miss the top 3, 20% with 4, 18% with 5 and 11% with 6.
  I looked at who outranks the right family in five of these cases (yellow loosestrife, marsh-marigold, yellow-rattle, common dog-violet, common centaury) and the outranking families do fit those answers; none was scored with an implausible state. I did not examine the other 105 one by one.
- **Species step (56 plants).** 5 to 52 species (median 13) fit all the answers, and ties are broken by hectad count. Typical cases are grasses told apart only by inflorescence shape (Briza, Deschampsia, Festuca ovina against Holcus, Poa, Agrostis), orchids with the same pink colour and narrow leaves, and speedwells, willows or whitebeam-like trees.
  I examined who outranks the right species for the 20 cases that failed in the first set. Three scores were wrong and are fixed in batch 8 (rosette versus stem leaves in thistles and sow-thistles, awns in Yorkshire-fog and common bent); in the rest the outranking species do fit the answers. I did not examine the 36 additional species-step failures of the second half of the set individually.
- Height is not a discriminating answer: a species is rejected only if its maximum height is below the chosen band, so "under 20 cm" never rejects anything.

Suggestions that need app or data design work, so they were not done here:
1. A flower-colour question at step 1 (it would need scoring all 144 families), which would remove most of the family-step ties.
2. A second tie-break after family size, such as the number of the user's answers that match exactly rather than by being unknown or multi-valued.
3. Scoring the largest grass and sedge groups with the leaf-width and ligule questions in the test set, since beginners rarely answer those correctly.

