# Test report

417 plants, 92 families. Data: docs/data/species.json.

| | family fits all answers | family in top 3 | species fits all answers | species in top 3 | both steps pass |
|---|---|---|---|---|---|
| plants | 379 | 333 | 358 | 375 | **251** |

Overall pass rate: **60.2%**. Rank 1 at family step: 227; rank 1 at species step: 271.

## Failures (166)

- **Achillea millefolium** (Asteraceae), family step: does not fit: inflor not branched. Top: Geraniaceae (0.0), Asteraceae (1.0), Rosaceae (1.0)
- **Sonchus oleraceus** (Asteraceae), species step: fits but ranks 4 (14 fit all answers). Top: Scorzoneroides autumnalis (0.0), Sonchus asper (0.0), Crepis capillaris (0.0)
- **Artemisia vulgaris** (Asteraceae), family step: does not fit: flowers not small_green. Top: Asteraceae (1.0), Rosaceae (1.0), Plantaginaceae (1.0)
- **Petasites hybridus** (Asteraceae), family step: does not fit: inflor not spike. Top: Rosaceae (0.0), Brassicaceae (0.0), Fabaceae (0.0)
- **Solidago virgaurea** (Asteraceae), family step: does not fit: inflor not spike. Top: Rosaceae (0.0), Brassicaceae (0.0), Fabaceae (0.0)
- **Lapsana communis** (Asteraceae), family step: does not fit: inflor not branched. Top: Asteraceae (1.0), Rosaceae (1.0), Fabaceae (1.0)
- **Tragopogon pratensis** (Asteraceae), family step: does not fit: lform not grassy. Top: Asteraceae (1.0), Papaveraceae (1.0), Campanulaceae (1.0)
- **Jacobaea vulgaris** (Asteraceae), family step: does not fit: inflor not branched. Top: Rosaceae (0.0), Ranunculaceae (0.0), Geraniaceae (0.0)
- **Senecio squalidus** (Asteraceae), species step: fits but ranks 6 (14 fit all answers). Top: Achillea millefolium (0.0), Senecio vulgaris (0.0), Tripleurospermum inodorum (0.0)
- **Achillea ptarmica** (Asteraceae), family step: does not fit: inflor not branched. Top: Rosaceae (0.0), Fabaceae (0.0), Ranunculaceae (0.0)
- **Holcus lanatus** (Poaceae), species step: does not fit: grass_awn not none; ghair not hairy. Top: Festuca rubra (0.0), Danthonia decumbens (0.0), Agrostis capillaris (1.0)
- **Anthoxanthum odoratum** (Poaceae), family step: does not fit: no aromatic. Top: Poaceae (1.0), Cyperaceae (1.0), Juncaceae (1.0)
- **Briza media** (Poaceae), species step: fits but ranks 8 (21 fit all answers). Top: Agrostis capillaris (0.0), Poa trivialis (0.0), Festuca rubra (0.0)
- **Hordeum murinum** (Poaceae), species step: does not fit: grass_head not cylinder. Top: Anthoxanthum odoratum (0.0), Cynosurus cristatus (0.0), Alopecurus pratensis (0.0)
- **Deschampsia cespitosa** (Poaceae), species step: does not fit: moist not wet. Top: Molinia caerulea (0.0), Calamagrostis epigejos (0.0), Puccinellia rupestris (0.0)
- **Avena fatua** (Poaceae), species step: fits but ranks 4 (11 fit all answers). Top: Schedonorus arundinaceus (0.0), Schedonorus giganteus (0.0), Bromopsis ramosa (0.0)
- **Anisantha sterilis** (Poaceae), species step: fits but ranks 7 (35 fit all answers). Top: Holcus lanatus (0.0), Agrostis capillaris (0.0), Arrhenatherum elatius (0.0)
- **Festuca ovina** (Poaceae), species step: fits but ranks 4 (13 fit all answers). Top: Agrostis capillaris (0.0), Aira praecox (0.0), Danthonia decumbens (0.0)
- **Eleocharis palustris** (Cyperaceae), family step: does not fit: larr not none. Top: Poaceae (1.0), Cyperaceae (1.0), Juncaceae (1.0)
- **Schoenoplectus lacustris** (Cyperaceae), family step: does not fit: larr not none. Top: Poaceae (1.0), Cyperaceae (1.0), Juncaceae (1.0)
- **Cladium mariscus** (Cyperaceae), family step: does not fit: no spiny. Top: Poaceae (1.0), Cyperaceae (1.0), Juncaceae (1.0)
- **Cladium mariscus** (Cyperaceae), species step: fits but ranks 5 (8 fit all answers). Top: Bolboschoenus maritimus (0.0), Schoenoplectus tabernaemontani (0.0), Scirpus sylvaticus (0.0)
- **Potentilla erecta** (Rosaceae), species step: does not fit: gsize not small. Top: Potentilla erecta (1.0), Alchemilla mollis (1.0), Agrimonia eupatoria (1.0)
- **Geum urbanum** (Rosaceae), species step: does not fit: gsize not small. Top: Agrimonia eupatoria (0.0), Agrimonia procera (0.0), Potentilla argentea (0.0)
- **Alchemilla glabra** (Rosaceae), species step: fits but ranks 4 (18 fit all answers). Top: Alchemilla mollis (0.0), Aphanes arvensis (0.0), Aphanes australis (0.0)
- **Agrimonia eupatoria** (Rosaceae), species step: fits but ranks 4 (15 fit all answers). Top: Potentilla anserina (0.0), Geum urbanum (0.0), Potentilla reptans (0.0)
- **Prunus padus** (Rosaceae), species step: fits but ranks 4 (8 fit all answers). Top: Prunus avium (0.0), Prunus laurocerasus (0.0), Prunus domestica (0.0)
- **Juncus effusus** (Juncaceae), family step: does not fit: larr not none. Top: Poaceae (1.0), Cyperaceae (1.0), Juncaceae (1.0)
- **Juncus inflexus** (Juncaceae), family step: does not fit: larr not none. Top: Poaceae (1.0), Cyperaceae (1.0), Juncaceae (1.0)
- **Juncus squarrosus** (Juncaceae), species step: fits but ranks 4 (6 fit all answers). Top: Luzula multiflora (0.0), Juncus bulbosus (0.0), Luzula sylvatica (0.0)
- **Ulex europaeus** (Fabaceae), species step: does not fit: gleaf not none; soil not acid. Top: Spartium junceum (1.5), Ulex europaeus (2.0), Cytisus scoparius (2.0)
- **Cytisus scoparius** (Fabaceae), species step: does not fit: gsize not large. Top: Lotus corniculatus (1.0), Lathyrus pratensis (1.0), Cytisus scoparius (1.0)
- **Laburnum anagyroides** (Fabaceae), species step: does not fit: gsize not large. Top: Lotus corniculatus (1.0), Lathyrus pratensis (1.0), Cytisus scoparius (1.0)
- **Cardamine pratensis** (Brassicaceae), species step: does not fit: moist not damp. Top: Cardamine bulbifera (0.0), Cardamine raphanifolia (0.5), Cardamine quinquefolia (0.5)
- **Alliaria petiolata** (Brassicaceae), family step: does not fit: no aromatic. Top: Brassicaceae (1.0), Saururaceae (1.0), Asteraceae (2.0)
- **Nasturtium officinale** (Brassicaceae), family step: does not fit: fhabit not water. Top: Brassicaceae (1.0), Ranunculaceae (1.0), Plantaginaceae (2.0)
- **Lunaria annua** (Brassicaceae), family step: does not fit: larr not opp. Top: Brassicaceae (1.0), Plantaginaceae (1.0), Caryophyllaceae (1.0)
- **Hesperis matronalis** (Brassicaceae), species step: does not fit: gleaf not narrow. Top: Lunaria annua (1.0), Raphanus raphanistrum (1.0), Hesperis matronalis (1.0)
- **Cakile maritima** (Brassicaceae), family step: does not fit: no succulent. Top: Brassicaceae (1.0), Rosaceae (2.0), Plantaginaceae (2.0)
- **Arenaria serpyllifolia** (Caryophyllaceae), species step: fits but ranks 5 (11 fit all answers). Top: Cerastium fontanum (0.0), Stellaria media (0.0), Cerastium glomeratum (0.0)
- **Spergula arvensis** (Caryophyllaceae), family step: does not fit: larr not whorl. Top: Plantaginaceae (0.0), Ericaceae (0.0), Primulaceae (0.0)
- **Anthriscus sylvestris** (Apiaceae), species step: does not fit: gleaf not lobed. Top: Heracleum sphondylium (0.0), Anthriscus sylvestris (1.0), Chaerophyllum temulum (1.0)
- **Heracleum sphondylium** (Apiaceae), family step: does not fit: no bristly. Top: Apiaceae (1.0), Primulaceae (1.0), Araliaceae (1.0)
- **Daucus carota** (Apiaceae), family step: does not fit: no bristly. Top: Apiaceae (1.0), Primulaceae (1.0), Araliaceae (1.0)
- **Daucus carota** (Apiaceae), species step: does not fit: gleaf not lobed. Top: Heracleum sphondylium (0.0), Heracleum mantegazzianum (0.0), Angelica sylvestris (1.0)
- **Angelica sylvestris** (Apiaceae), species step: does not fit: moist not damp. Top: Heracleum sphondylium (0.0), Aegopodium podagraria (0.0), Daucus carota (0.0)
- **Conopodium majus** (Apiaceae), species step: does not fit: gsize not small; gleaf not lobed. Top: Sanicula europaea (0.0), Helosciadium inundatum (1.0), Anthriscus caucalis (1.0)
- **Conium maculatum** (Apiaceae), species step: does not fit: gleaf not lobed. Top: Helosciadium inundatum (0.0), Apium graveolens (0.0), Heracleum sphondylium (1.0)
- **Torilis japonica** (Apiaceae), species step: does not fit: gsize not small; gleaf not lobed. Top: Heracleum sphondylium (1.0), Heracleum mantegazzianum (1.0), Helosciadium inundatum (1.0)
- **Sanicula europaea** (Apiaceae), family step: does not fit: inflor not head. Top: Asteraceae (0.0), Rosaceae (0.0), Caprifoliaceae (0.0)
- **Smyrnium olusatrum** (Apiaceae), species step: does not fit: salt not coast. Top: Foeniculum vulgare (1.0), Smyrnium olusatrum (1.0), Levisticum officinale (1.5)
- **Veronica persica** (Plantaginaceae), species step: fits but ranks 4 (10 fit all answers). Top: Veronica serpyllifolia (0.0), Veronica chamaedrys (0.0), Veronica arvensis (0.0)
- **Antirrhinum majus** (Plantaginaceae), species step: does not fit: gleaf not narrow. Top: Digitalis purpurea (1.0), Linaria purpurea (1.0), Veronica scutellata (1.0)
- **Plantago maritima** (Plantaginaceae), family step: does not fit: no succulent. Top: Rosaceae (1.0), Brassicaceae (1.0), Plantaginaceae (1.0)
- **Caltha palustris** (Ranunculaceae), family step: fits but ranks 6 (25 fit all answers). Top: Asteraceae (0.0), Rosaceae (0.0), Brassicaceae (0.0)
- **Ranunculus flammula** (Ranunculaceae), family step: fits but ranks 8 (21 fit all answers). Top: Asteraceae (0.0), Rosaceae (0.0), Fabaceae (0.0)
- **Ranunculus sceleratus** (Ranunculaceae), family step: fits but ranks 6 (14 fit all answers). Top: Asteraceae (0.0), Rosaceae (0.0), Plantaginaceae (0.0)
- **Ranunculus sceleratus** (Ranunculaceae), species step: does not fit: rfruit not spike. Top: Ranunculus sceleratus (1.0), Ranunculus muricatus (1.0), Ranunculus acris (2.0)
- **Helleborus foetidus** (Ranunculaceae), family step: fits but ranks 7 (19 fit all answers). Top: Asteraceae (0.0), Rosaceae (0.0), Brassicaceae (0.0)
- **Ranunculus hederaceus** (Ranunculaceae), family step: fits but ranks 6 (10 fit all answers). Top: Asteraceae (0.0), Rosaceae (0.0), Plantaginaceae (0.0)
- **Galeopsis tetrahit** (Lamiaceae), species step: does not fit: leaf not heart. Top: Lamium purpureum (0.0), Lamium hybridum (0.0), Lamium maculatum (0.0)
- **Orchis mascula** (Orchidaceae), species step: does not fit: light not shade. Top: Serapias lingua (0.5), Dactylorhiza kerryensis (0.5), Orchis mascula (1.0)
- **Ophrys apifera** (Orchidaceae), species step: fits but ranks 4 (16 fit all answers). Top: Dactylorhiza fuchsii (0.0), Dactylorhiza maculata (0.0), Orchis mascula (0.0)
- **Neottia ovata** (Orchidaceae), family step: does not fit: larr not opp. Top: Plantaginaceae (0.0), Ranunculaceae (1.0), Orchidaceae (1.0)
- **Anacamptis pyramidalis** (Orchidaceae), species step: fits but ranks 5 (11 fit all answers). Top: Dactylorhiza fuchsii (0.0), Orchis mascula (0.0), Ophrys apifera (0.0)
- **Rumex acetosa** (Polygonaceae), family step: does not fit: petals not none. Top: Plantaginaceae (1.0), Polygonaceae (1.0), Amaranthaceae (1.0)
- **Persicaria maculosa** (Polygonaceae), family step: does not fit: no nodes. Top: Rosaceae (1.0), Brassicaceae (1.0), Fabaceae (1.0)
- **Reynoutria japonica** (Polygonaceae), family step: does not fit: no nodes. Top: Rosaceae (1.0), Fabaceae (1.0), Caryophyllaceae (1.0)
- **Persicaria amphibia** (Polygonaceae), species step: does not fit: gleaf not narrow. Top: Bistorta affinis (0.5), Koenigia campanulata (0.5), Rumex acetosella (1.0)
- **Symphytum officinale** (Boraginaceae), species step: does not fit: gleaf not narrow. Top: Lithospermum officinale (0.0), Plagiobothrys scouleri (0.0), Symphytum officinale (1.0)
- **Myosotis scorpioides** (Boraginaceae), species step: does not fit: gleaf not narrow. Top: Myosotis scorpioides (1.0), Myosotis secunda (1.0), Cynoglossum officinale (1.0)
- **Beta vulgaris** (Amaranthaceae), family step: fits but ranks 6 (15 fit all answers). Top: Rosaceae (0.0), Plantaginaceae (0.0), Ranunculaceae (0.0)
- **Rhinanthus minor** (Orobanchaceae), family step: fits but ranks 6 (11 fit all answers). Top: Plantaginaceae (0.0), Lamiaceae (0.0), Ranunculaceae (0.0)
- **Pedicularis sylvatica** (Orobanchaceae), family step: fits but ranks 6 (12 fit all answers). Top: Plantaginaceae (0.0), Lamiaceae (0.0), Apiaceae (0.0)
- **Odontites vernus** (Orobanchaceae), family step: fits but ranks 6 (12 fit all answers). Top: Plantaginaceae (0.0), Lamiaceae (0.0), Ranunculaceae (0.0)
- **Melampyrum pratense** (Orobanchaceae), family step: fits but ranks 6 (12 fit all answers). Top: Plantaginaceae (0.0), Lamiaceae (0.0), Ranunculaceae (0.0)
- **Allium triquetrum** (Amaryllidaceae), family step: does not fit: no tri. Top: Orchidaceae (1.0), Amaryllidaceae (1.0), Asparagaceae (1.0)
- **Ruscus aculeatus** (Asparagaceae), family step: does not fit: no spiny. Top: Rosaceae (0.0), Grossulariaceae (0.0), Rhamnaceae (0.0)
- **Erodium cicutarium** (Geraniaceae), species step: does not fit: gsize not small. Top: Geranium molle (0.0), Geranium dissectum (0.0), Geranium pusillum (0.0)
- **Campanula rotundifolia** (Campanulaceae), family step: fits but ranks 6 (14 fit all answers). Top: Asteraceae (0.0), Plantaginaceae (0.0), Boraginaceae (0.0)
- **Campanula trachelium** (Campanulaceae), family step: does not fit: no bristly. Top: Boraginaceae (0.0), Cucurbitaceae (0.0), Asteraceae (1.0)
- **Jasione montana** (Campanulaceae), family step: fits but ranks 4 (4 fit all answers). Top: Asteraceae (0.0), Rosaceae (0.0), Fabaceae (0.0)
- **Primula vulgaris** (Primulaceae), family step: fits but ranks 4 (7 fit all answers). Top: Plantaginaceae (0.0), Caprifoliaceae (0.0), Campanulaceae (0.0)
- **Primula veris** (Primulaceae), species step: does not fit: gsize not small. Top: Primula veris (1.0), Primula elatior (1.0), Primula vulgaris (2.0)
- **Lysimachia nummularia** (Primulaceae), family step: fits but ranks 7 (19 fit all answers). Top: Asteraceae (0.0), Plantaginaceae (0.0), Caryophyllaceae (0.0)
- **Lysimachia vulgaris** (Primulaceae), family step: fits but ranks 10 (21 fit all answers). Top: Asteraceae (0.0), Plantaginaceae (0.0), Caryophyllaceae (0.0)
- **Lysimachia vulgaris** (Primulaceae), species step: does not fit: gleaf not narrow. Top: Lysimachia vulgaris (1.0), Lysimachia thyrsiflora (1.0), Lysimachia ciliata (1.5)
- **Lysimachia arvensis** (Primulaceae), family step: fits but ranks 7 (18 fit all answers). Top: Asteraceae (0.0), Plantaginaceae (0.0), Caryophyllaceae (0.0)
- **Lysimachia nemorum** (Primulaceae), family step: fits but ranks 7 (18 fit all answers). Top: Asteraceae (0.0), Plantaginaceae (0.0), Caryophyllaceae (0.0)
- **Sedum acre** (Crassulaceae), species step: does not fit: gsize not small. Top: Rhodiola rosea (0.0), Chiastophyllum oppositifolium (0.0), Sedum acre (1.0)
- **Umbilicus rupestris** (Crassulaceae), family step: does not fit: inflor not spike. Top: Rosaceae (1.0), Brassicaceae (1.0), Plantaginaceae (1.0)
- **Umbilicus rupestris** (Crassulaceae), species step: does not fit: height max 0.4 m. Top: Umbilicus rupestris (1.0), Rhodiola rosea (1.0), Sedum spathulifolium (1.0)
- **Asplenium ruta-muraria** (Aspleniaceae), species step: does not fit: gleaf not lobed. Top: Asplenium ceterach (0.0), Onoclea sensibilis (0.5), Asplenium trichomanes (1.0)
- **Polystichum setiferum** (Polypodiaceae), species step: fits but ranks 5 (6 fit all answers). Top: Dryopteris dilatata (0.0), Dryopteris filix-mas (0.0), Dryopteris affinis (0.0)
- **Equisetum arvense** (Equisetaceae), species step: does not fit: gleaf not narrow. Top: Equisetum arvense (1.0), Equisetum palustre (1.0), Equisetum fluviatile (1.0)
- **Equisetum telmateia** (Equisetaceae), species step: does not fit: gleaf not narrow. Top: Equisetum fluviatile (1.0), Equisetum telmateia (1.0), Equisetum hyemale (1.0)
- **Dipsacus fullonum** (Caprifoliaceae), species step: does not fit: gleaf not narrow. Top: Dipsacus sativus (0.0), Succisa pratensis (1.0), Dipsacus fullonum (1.0)
- **Centranthus ruber** (Caprifoliaceae), family step: fits but ranks 6 (32 fit all answers). Top: Asteraceae (0.0), Plantaginaceae (0.0), Caryophyllaceae (0.0)
- **Sambucus nigra** (Viburnaceae), species step: does not fit: gsize not small. Top: Sambucus nigra (1.0), Sambucus canadensis (1.0), Viburnum opulus (2.0)
- **Adoxa moschatellina** (Viburnaceae), family step: does not fit: flowers not small_green. Top: Rosaceae (0.0), Rubiaceae (0.0), Typhaceae (0.0)
- **Adoxa moschatellina** (Viburnaceae), species step: does not fit: height max 0.12 m. Top: Adoxa moschatellina (1.0), Sambucus racemosa (2.0), Viburnum tinus (3.5)
- **Fumaria officinalis** (Papaveraceae), family step: fits but ranks 7 (12 fit all answers). Top: Plantaginaceae (0.0), Lamiaceae (0.0), Apiaceae (0.0)
- **Pseudofumaria lutea** (Papaveraceae), family step: fits but ranks 7 (12 fit all answers). Top: Plantaginaceae (0.0), Lamiaceae (0.0), Apiaceae (0.0)
- **Pseudofumaria lutea** (Papaveraceae), species step: does not fit: gleaf not lobed. Top: Chelidonium majus (0.0), Eschscholzia californica (0.0), Papaver atlanticum (0.0)
- **Chrysosplenium oppositifolium** (Saxifragaceae), family step: fits but ranks 5 (6 fit all answers). Top: Plantaginaceae (0.0), Caryophyllaceae (0.0), Ranunculaceae (0.0)
- **Saxifraga granulata** (Saxifragaceae), family step: fits but ranks 14 (27 fit all answers). Top: Asteraceae (0.0), Rosaceae (0.0), Plantaginaceae (0.0)
- **Saxifraga granulata** (Saxifragaceae), species step: does not fit: gleaf not heart. Top: Saxifraga hirsuta (0.0), Saxifraga rotundifolia (0.0), Saxifraga stolonifera (0.0)
- **Chamaenerion angustifolium** (Onagraceae), family step: fits but ranks 6 (11 fit all answers). Top: Rosaceae (0.0), Brassicaceae (0.0), Plantaginaceae (0.0)
- **Fuchsia magellanica** (Onagraceae), family step: fits but ranks 4 (11 fit all answers). Top: Lamiaceae (0.0), Ranunculaceae (0.0), Caprifoliaceae (0.0)
- **Salix caprea** (Salicaceae), species step: does not fit: ghair not woolly. Top: Salix cinerea (1.0), Salix caprea (1.0), Salix lapponum (1.0)
- **Salix alba** (Salicaceae), species step: does not fit: ghair not woolly. Top: Salix viminalis (1.0), Salix alba (1.0), Salix repens (1.0)
- **Salix repens** (Salicaceae), species step: fits but ranks 4 (6 fit all answers). Top: Salix cinerea (0.0), Salix caprea (0.0), Salix aurita (0.0)
- **Limonium vulgare** (Plumbaginaceae), family step: fits but ranks 14 (16 fit all answers). Top: Rosaceae (0.0), Ranunculaceae (0.0), Boraginaceae (0.0)
- **Limonium vulgare** (Plumbaginaceae), species step: does not fit: height max 0.4 m. Top: Limonium humile (0.0), Limonium procerum (0.0), Limonium binervosum (0.0)
- **Euphorbia helioscopia** (Euphorbiaceae), species step: does not fit: gcolour not green_brown. Top: Mercurialis annua (0.0), Euphorbia oblongata (0.0), Euphorbia stricta (0.0)
- **Euphorbia peplus** (Euphorbiaceae), species step: does not fit: gcolour not green_brown. Top: Mercurialis annua (0.0), Euphorbia oblongata (0.0), Euphorbia platyphyllos (0.0)
- **Mercurialis perennis** (Euphorbiaceae), family step: fits but ranks 5 (9 fit all answers). Top: Plantaginaceae (0.0), Caryophyllaceae (0.0), Amaranthaceae (0.0)
- **Euphorbia amygdaloides** (Euphorbiaceae), species step: does not fit: gcolour not green_brown. Top: Mercurialis perennis (0.0), Euphorbia hyberna (0.0), Euphorbia amygdaloides (1.0)
- **Hypericum tetrapterum** (Hypericaceae), family step: does not fit: no square. Top: Lamiaceae (0.0), Scrophulariaceae (0.0), Asteraceae (1.0)
- **Hypericum androsaemum** (Hypericaceae), family step: fits but ranks 4 (8 fit all answers). Top: Ranunculaceae (0.0), Caprifoliaceae (0.0), Ericaceae (0.0)
- **Centaurium erythraea** (Gentianaceae), family step: fits but ranks 16 (28 fit all answers). Top: Asteraceae (0.0), Plantaginaceae (0.0), Caryophyllaceae (0.0)
- **Blackstonia perfoliata** (Gentianaceae), family step: fits but ranks 17 (35 fit all answers). Top: Asteraceae (0.0), Plantaginaceae (0.0), Caryophyllaceae (0.0)
- **Gentiana pneumonanthe** (Gentianaceae), family step: fits but ranks 10 (15 fit all answers). Top: Asteraceae (0.0), Plantaginaceae (0.0), Lamiaceae (0.0)
- **Gentiana pneumonanthe** (Gentianaceae), species step: does not fit: gsize not large. Top: Gentiana pneumonanthe (1.0), Gentianella amarella (2.0), Gentianella campestris (2.0)
- **Malva sylvestris** (Malvaceae), family step: fits but ranks 9 (15 fit all answers). Top: Asteraceae (0.0), Rosaceae (0.0), Plantaginaceae (0.0)
- **Malva moschata** (Malvaceae), family step: fits but ranks 9 (15 fit all answers). Top: Asteraceae (0.0), Rosaceae (0.0), Plantaginaceae (0.0)
- **Hydrocharis morsus-ranae** (Hydrocharitaceae), species step: does not fit: gleaf not oval. Top: Elodea canadensis (1.0), Elodea nuttallii (1.0), Hydrocharis morsus-ranae (1.0)
- **Elodea canadensis** (Hydrocharitaceae), species step: does not fit: gleaf not narrow. Top: Elodea nuttallii (0.0), Lagarosiphon major (0.0), Vallisneria spiralis (0.0)
- **Betula pendula** (Betulaceae), species step: does not fit: gleaf not heart. Top: Betula pendula (1.0), Alnus cordata (1.0), Alnus glutinosa (2.0)
- **Corylus avellana** (Betulaceae), species step: does not fit: gcolour not yellow. Top: Corylus maxima (0.0), Corylus avellana (1.0), Alnus incana (1.0)
- **Hedera helix** (Araliaceae), family step: fits but ranks 4 (5 fit all answers). Top: Rosaceae (0.0), Ranunculaceae (0.0), Solanaceae (0.0)
- **Hydrocotyle vulgaris** (Araliaceae), family step: fits but ranks 23 (26 fit all answers). Top: Asteraceae (0.0), Rosaceae (0.0), Brassicaceae (0.0)
- **Pinguicula vulgaris** (Lentibulariaceae), species step: does not fit: height max 0.15 m. Top: Pinguicula vulgaris (1.0), Pinguicula grandiflora (1.0), Utricularia australis (3.0)
- **Utricularia vulgaris** (Lentibulariaceae), family step: fits but ranks 4 (4 fit all answers). Top: Plantaginaceae (0.0), Apiaceae (0.0), Ranunculaceae (0.0)
- **Fritillaria meleagris** (Liliaceae), family step: fits but ranks 6 (9 fit all answers). Top: Amaryllidaceae (0.0), Asparagaceae (0.0), Iridaceae (0.0)
- **Hemerocallis fulva** (Asphodelaceae), family step: fits but ranks 7 (9 fit all answers). Top: Amaryllidaceae (0.0), Asparagaceae (0.0), Iridaceae (0.0)
- **Convolvulus arvensis** (Convolvulaceae), family step: fits but ranks 4 (5 fit all answers). Top: Caprifoliaceae (0.0), Rubiaceae (0.0), Solanaceae (0.0)
- **Castanea sativa** (Fagaceae), species step: does not fit: gleaf not narrow. Top: Castanea sativa (1.0), Quercus ilex (2.0), Quercus cerris (3.0)
- **Ligustrum vulgare** (Oleaceae), family step: fits but ranks 6 (9 fit all answers). Top: Ranunculaceae (0.0), Caprifoliaceae (0.0), Ericaceae (0.0)
- **Ligustrum vulgare** (Oleaceae), species step: does not fit: gleaf not narrow. Top: Ligustrum vulgare (1.0), Syringa vulgaris (1.0), Jasminum officinale (2.0)
- **Typha latifolia** (Typhaceae), family step: does not fit: wet not wet. Top: Poaceae (0.0), Cyperaceae (0.0), Juncaginaceae (0.0)
- **Typha latifolia** (Typhaceae), species step: does not fit: gsize not large. Top: Sparganium erectum (1.0), Typha latifolia (1.0), Typha angustifolia (1.0)
- **Sparganium erectum** (Typhaceae), family step: does not fit: wet not wet. Top: Cyperaceae (0.0), Juncaceae (0.0), Poaceae (1.0)
- **Parietaria judaica** (Urticaceae), family step: fits but ranks 12 (21 fit all answers). Top: Rosaceae (0.0), Plantaginaceae (0.0), Ranunculaceae (0.0)
- **Soleirolia soleirolii** (Urticaceae), family step: fits but ranks 9 (12 fit all answers). Top: Rosaceae (0.0), Plantaginaceae (0.0), Caryophyllaceae (0.0)
- **Soleirolia soleirolii** (Urticaceae), species step: does not fit: gcolour not green_brown. Top: Parietaria judaica (0.0), Parietaria officinalis (0.0), Urtica urens (1.0)
- **Ribes sanguineum** (Grossulariaceae), family step: fits but ranks 6 (6 fit all answers). Top: Rosaceae (0.0), Ranunculaceae (0.0), Caprifoliaceae (0.0)
- **Cornus sanguinea** (Cornaceae), family step: fits but ranks 7 (9 fit all answers). Top: Ranunculaceae (0.0), Caprifoliaceae (0.0), Ericaceae (0.0)
- **Helianthemum nummularium** (Cistaceae), family step: fits but ranks 6 (7 fit all answers). Top: Asteraceae (0.0), Lamiaceae (0.0), Ranunculaceae (0.0)
- **Linum catharticum** (Linaceae), family step: fits but ranks 18 (28 fit all answers). Top: Asteraceae (0.0), Plantaginaceae (0.0), Caryophyllaceae (0.0)
- **Lemna minor** (Araceae), family step: fits but ranks 5 (13 fit all answers). Top: Plantaginaceae (0.0), Ranunculaceae (0.0), Polygonaceae (0.0)
- **Verbascum thapsus** (Scrophulariaceae), family step: fits but ranks 15 (24 fit all answers). Top: Rosaceae (0.0), Brassicaceae (0.0), Fabaceae (0.0)
- **Buddleja davidii** (Scrophulariaceae), family step: fits but ranks 5 (6 fit all answers). Top: Lamiaceae (0.0), Ranunculaceae (0.0), Onagraceae (0.0)
- **Buddleja davidii** (Scrophulariaceae), species step: does not fit: gleaf not narrow. Top: Buddleja davidii (1.0), Verbascum thapsus (2.0), Verbascum speciosum (2.0)
- **Solanum dulcamara** (Solanaceae), family step: fits but ranks 4 (4 fit all answers). Top: Rosaceae (0.0), Ranunculaceae (0.0), Caprifoliaceae (0.0)
- **Solanum nigrum** (Solanaceae), family step: fits but ranks 4 (8 fit all answers). Top: Rosaceae (0.0), Ranunculaceae (0.0), Ericaceae (0.0)
- **Oxalis acetosella** (Oxalidaceae), family step: fits but ranks 6 (7 fit all answers). Top: Rosaceae (0.0), Apiaceae (0.0), Ranunculaceae (0.0)
- **Oxalis acetosella** (Oxalidaceae), species step: does not fit: ghair not hairless. Top: Oxalis incarnata (0.0), Oxalis acetosella (1.0), Oxalis debilis (1.0)
- **Oxalis corniculata** (Oxalidaceae), family step: fits but ranks 6 (6 fit all answers). Top: Rosaceae (0.0), Fabaceae (0.0), Apiaceae (0.0)
- **Viola riviniana** (Violaceae), family step: fits but ranks 8 (15 fit all answers). Top: Fabaceae (0.0), Plantaginaceae (0.0), Apiaceae (0.0)
- **Viola odorata** (Violaceae), family step: fits but ranks 8 (11 fit all answers). Top: Fabaceae (0.0), Plantaginaceae (0.0), Lamiaceae (0.0)
- **Viola arvensis** (Violaceae), family step: fits but ranks 8 (15 fit all answers). Top: Fabaceae (0.0), Plantaginaceae (0.0), Apiaceae (0.0)
- **Viola arvensis** (Violaceae), species step: does not fit: gleaf not lobed. Top: Viola arvensis (1.0), Viola tricolor (1.0), Viola kitaibeliana (1.0)
- **Drosera rotundifolia** (Droseraceae), species step: does not fit: height max 0.18 m. Top: Drosera rotundifolia (1.0), Drosera anglica (1.0), Drosera intermedia (1.0)
- **Impatiens glandulifera** (Balsaminaceae), family step: fits but ranks 6 (9 fit all answers). Top: Plantaginaceae (0.0), Ranunculaceae (0.0), Onagraceae (0.0)
- **Menyanthes trifoliata** (Menyanthaceae), family step: does not fit: wet not wet. Top: Rosaceae (0.0), Brassicaceae (0.0), Fabaceae (0.0)
- **Nuphar lutea** (Nymphaeaceae), family step: fits but ranks 9 (12 fit all answers). Top: Plantaginaceae (0.0), Apiaceae (0.0), Ranunculaceae (0.0)
- **Lythrum salicaria** (Lythraceae), family step: fits but ranks 9 (10 fit all answers). Top: Plantaginaceae (0.0), Lamiaceae (0.0), Ranunculaceae (0.0)
- **Polygala vulgaris** (Polygalaceae), family step: fits but ranks 16 (21 fit all answers). Top: Fabaceae (0.0), Plantaginaceae (0.0), Apiaceae (0.0)
- **Reseda luteola** (Resedaceae), family step: does not fit: flowers not small_green. Top: Rosaceae (0.0), Plantaginaceae (0.0), Ranunculaceae (0.0)
- **Euonymus europaeus** (Celastraceae), family step: fits but ranks 8 (13 fit all answers). Top: Ranunculaceae (0.0), Onagraceae (0.0), Ericaceae (0.0)
- **Vinca minor** (Apocynaceae), family step: fits but ranks 13 (19 fit all answers). Top: Asteraceae (0.0), Plantaginaceae (0.0), Caryophyllaceae (0.0)
- **Montia fontana** (Montiaceae), family step: fits but ranks 18 (23 fit all answers). Top: Asteraceae (0.0), Plantaginaceae (0.0), Caryophyllaceae (0.0)
- **Buxus sempervirens** (Buxaceae), family step: fits but ranks 8 (8 fit all answers). Top: Ranunculaceae (0.0), Amaranthaceae (0.0), Euphorbiaceae (0.0)
- **Tamus communis** (Dioscoreaceae), family step: fits but ranks 5 (5 fit all answers). Top: Rosaceae (0.0), Ranunculaceae (0.0), Rubiaceae (0.0)
- **Frangula alnus** (Rhamnaceae), family step: fits but ranks 8 (13 fit all answers). Top: Rosaceae (0.0), Ranunculaceae (0.0), Ericaceae (0.0)
- **Daphne laureola** (Thymelaeaceae), family step: fits but ranks 9 (13 fit all answers). Top: Rosaceae (0.0), Ranunculaceae (0.0), Ericaceae (0.0)
- **Ulex gallii** (Fabaceae), species step: does not fit: gleaf not none. Top: Spartium junceum (0.5), Genista aetnensis (0.5), Ulex gallii (1.0)
- **Trifolium arvense** (Fabaceae), species step: does not fit: ghair not woolly. Top: Trifolium pratense (1.0), Vicia sativa (1.0), Trifolium medium (1.0)
- **Lysimachia tenella** (Primulaceae), family step: fits but ranks 7 (15 fit all answers). Top: Asteraceae (0.0), Plantaginaceae (0.0), Caryophyllaceae (0.0)
- **Cirsium acaule** (Asteraceae), species step: fits but ranks 5 (13 fit all answers). Top: Cirsium vulgare (0.0), Carduus crispus (0.0), Carduus nutans (0.0)
- **Juncus conglomeratus** (Juncaceae), family step: does not fit: larr not none. Top: Poaceae (1.0), Cyperaceae (1.0), Juncaceae (1.0)

## All plants

| plant | family | fam answers | fam fit | fam rank | sp answers | sp fit | sp rank (of fitting) |
|---|---|---|---|---|---|---|---|
| Bellis perennis | Asteraceae | 5 | yes | 1 | 5 | yes | 1 (3) |
| Taraxacum officinale agg. | Asteraceae | 5 | yes | 1 | 6 | yes | 1 (10) |
| Cirsium vulgare | Asteraceae | 6 | yes | 1 | 5 | yes | 1 (10) |
| Cirsium arvense | Asteraceae | 5 | yes | 1 | 6 | yes | 1 (7) |
| Senecio vulgaris | Asteraceae | 4 | yes | 1 | 5 | yes | 2 (11) |
| Leucanthemum vulgare | Asteraceae | 5 | yes | 1 | 6 | yes | 1 (5) |
| Achillea millefolium | Asteraceae | 5 | NO | 2 | 6 | yes | 1 (2) |
| Tussilago farfara | Asteraceae | 4 | yes | 1 | 5 | yes | 1 (3) |
| Centaurea nigra | Asteraceae | 4 | yes | 1 | 6 | yes | 1 (8) |
| Hypochaeris radicata | Asteraceae | 4 | yes | 1 | 6 | yes | 1 (39) |
| Sonchus oleraceus | Asteraceae | 4 | yes | 1 | 6 | yes | 4 (14) |
| Tanacetum vulgare | Asteraceae | 5 | yes | 1 | 5 | yes | 1 (8) |
| Artemisia vulgaris | Asteraceae | 5 | NO | 1 | 5 | yes | 1 (5) |
| Eupatorium cannabinum | Asteraceae | 4 | yes | 1 | 6 | yes | 2 (2) |
| Petasites hybridus | Asteraceae | 4 | NO | 27 | 5 | yes | 1 (1) |
| Solidago virgaurea | Asteraceae | 5 | NO | 23 | 5 | yes | 3 (21) |
| Pulicaria dysenterica | Asteraceae | 4 | yes | 1 | 6 | yes | 2 (6) |
| Cichorium intybus | Asteraceae | 5 | yes | 1 | 5 | yes | 1 (6) |
| Lapsana communis | Asteraceae | 4 | NO | 1 | 5 | yes | 1 (5) |
| Arctium minus | Asteraceae | 5 | yes | 1 | 5 | yes | 1 (3) |
| Tripleurospermum inodorum | Asteraceae | 5 | yes | 1 | 5 | yes | 2 (10) |
| Matricaria discoidea | Asteraceae | 5 | yes | 1 | 6 | yes | 1 (4) |
| Tragopogon pratensis | Asteraceae | 5 | NO | 1 | 6 | yes | 3 (31) |
| Jacobaea vulgaris | Asteraceae | 5 | NO | 8 | 5 | yes | 3 (7) |
| Carlina vulgaris | Asteraceae | 5 | yes | 1 | 5 | yes | 1 (2) |
| Scorzoneroides autumnalis | Asteraceae | 4 | yes | 1 | 5 | yes | 1 (41) |
| Galinsoga quadriradiata | Asteraceae | 4 | yes | 1 | 5 | yes | 2 (12) |
| Bidens tripartita | Asteraceae | 4 | yes | 1 | 5 | yes | 3 (11) |
| Cirsium palustre | Asteraceae | 5 | yes | 1 | 6 | yes | 1 (1) |
| Senecio squalidus | Asteraceae | 5 | yes | 1 | 5 | yes | 6 (14) |
| Sonchus arvensis | Asteraceae | 4 | yes | 1 | 6 | yes | 1 (2) |
| Gnaphalium uliginosum | Asteraceae | 4 | yes | 1 | 6 | yes | 1 (14) |
| Achillea ptarmica | Asteraceae | 5 | NO | 14 | 6 | yes | 2 (9) |
| Holcus lanatus | Poaceae | 4 | yes | 1 | 6 | NO | 51 (2) |
| Poa annua | Poaceae | 4 | yes | 1 | 6 | yes | 1 (9) |
| Lolium perenne | Poaceae | 5 | yes | 1 | 6 | yes | 1 (3) |
| Dactylis glomerata | Poaceae | 4 | yes | 1 | 6 | yes | 1 (1) |
| Arrhenatherum elatius | Poaceae | 4 | yes | 1 | 6 | yes | 2 (29) |
| Anthoxanthum odoratum | Poaceae | 4 | NO | 1 | 5 | yes | 1 (8) |
| Phleum pratense | Poaceae | 4 | yes | 1 | 5 | yes | 1 (7) |
| Alopecurus pratensis | Poaceae | 4 | yes | 1 | 6 | yes | 2 (2) |
| Phragmites australis | Poaceae | 5 | yes | 1 | 6 | yes | 3 (5) |
| Molinia caerulea | Poaceae | 4 | yes | 1 | 6 | yes | 1 (7) |
| Nardus stricta | Poaceae | 4 | yes | 1 | 5 | yes | 2 (2) |
| Briza media | Poaceae | 3 | yes | 1 | 6 | yes | 8 (21) |
| Festuca rubra | Poaceae | 3 | yes | 1 | 5 | yes | 2 (8) |
| Brachypodium sylvaticum | Poaceae | 4 | yes | 1 | 6 | yes | 1 (5) |
| Elymus repens | Poaceae | 4 | yes | 1 | 6 | yes | 3 (9) |
| Hordeum murinum | Poaceae | 4 | yes | 1 | 6 | NO | 35 (17) |
| Deschampsia cespitosa | Poaceae | 3 | yes | 1 | 6 | NO | 17 (5) |
| Glyceria maxima | Poaceae | 5 | yes | 1 | 6 | yes | 3 (3) |
| Poa trivialis | Poaceae | 3 | yes | 1 | 6 | yes | 2 (21) |
| Cynosurus cristatus | Poaceae | 4 | yes | 1 | 5 | yes | 1 (9) |
| Agrostis stolonifera | Poaceae | 3 | yes | 1 | 6 | yes | 1 (16) |
| Bromus hordeaceus | Poaceae | 4 | yes | 1 | 6 | yes | 1 (2) |
| Avena fatua | Poaceae | 3 | yes | 1 | 6 | yes | 4 (11) |
| Aira praecox | Poaceae | 3 | yes | 1 | 6 | yes | 2 (12) |
| Anisantha sterilis | Poaceae | 3 | yes | 1 | 6 | yes | 7 (35) |
| Festuca ovina | Poaceae | 3 | yes | 1 | 6 | yes | 4 (13) |
| Carex flacca | Cyperaceae | 5 | yes | 1 | 5 | yes | 1 (40) |
| Carex pendula | Cyperaceae | 4 | yes | 1 | 6 | yes | 1 (7) |
| Carex hirta | Cyperaceae | 4 | yes | 1 | 6 | yes | 1 (2) |
| Carex nigra | Cyperaceae | 5 | yes | 1 | 6 | yes | 2 (31) |
| Carex panicea | Cyperaceae | 4 | yes | 1 | 6 | yes | 2 (23) |
| Carex remota | Cyperaceae | 4 | yes | 1 | 6 | yes | 2 (13) |
| Carex otrubae | Cyperaceae | 4 | yes | 1 | 6 | yes | 3 (13) |
| Eleocharis palustris | Cyperaceae | 4 | NO | 2 | 6 | yes | 1 (3) |
| Eriophorum angustifolium | Cyperaceae | 4 | yes | 2 | 6 | yes | 1 (2) |
| Eriophorum vaginatum | Cyperaceae | 4 | yes | 2 | 6 | yes | 1 (1) |
| Carex sylvatica | Cyperaceae | 4 | yes | 1 | 6 | yes | 2 (15) |
| Carex arenaria | Cyperaceae | 4 | yes | 1 | 6 | yes | 2 (5) |
| Schoenoplectus lacustris | Cyperaceae | 4 | NO | 2 | 5 | yes | 1 (3) |
| Cladium mariscus | Cyperaceae | 5 | NO | 2 | 4 | yes | 5 (8) |
| Carex acutiformis | Cyperaceae | 5 | yes | 1 | 6 | yes | 2 (10) |
| Rubus fruticosus | Rosaceae | 6 | yes | 1 | 6 | yes | 1 (8) |
| Rosa canina | Rosaceae | 6 | yes | 1 | 6 | yes | 1 (8) |
| Crataegus monogyna | Rosaceae | 5 | yes | 1 | 6 | yes | 1 (3) |
| Prunus spinosa | Rosaceae | 4 | yes | 2 | 6 | yes | 1 (1) |
| Sorbus aucuparia | Rosaceae | 5 | yes | 1 | 6 | yes | 1 (4) |
| Fragaria vesca | Rosaceae | 5 | yes | 1 | 6 | yes | 1 (4) |
| Potentilla reptans | Rosaceae | 5 | yes | 1 | 6 | yes | 3 (16) |
| Potentilla erecta | Rosaceae | 4 | yes | 1 | 6 | NO | 1 (0) |
| Geum urbanum | Rosaceae | 6 | yes | 1 | 6 | NO | 8 (5) |
| Filipendula ulmaria | Rosaceae | 5 | yes | 1 | 6 | yes | 1 (5) |
| Alchemilla glabra | Rosaceae | 4 | yes | 1 | 6 | yes | 4 (18) |
| Agrimonia eupatoria | Rosaceae | 5 | yes | 1 | 6 | yes | 4 (15) |
| Malus sylvestris | Rosaceae | 4 | yes | 1 | 6 | yes | 2 (52) |
| Prunus avium | Rosaceae | 4 | yes | 1 | 6 | yes | 1 (12) |
| Rubus idaeus | Rosaceae | 6 | yes | 1 | 6 | yes | 1 (1) |
| Poterium sanguisorba | Rosaceae | 4 | yes | 1 | 6 | yes | 1 (4) |
| Potentilla anserina | Rosaceae | 5 | yes | 1 | 6 | yes | 1 (16) |
| Aphanes arvensis | Rosaceae | 3 | yes | 1 | 6 | yes | 2 (18) |
| Sanguisorba officinalis | Rosaceae | 4 | yes | 1 | 6 | yes | 2 (2) |
| Cotoneaster horizontalis | Rosaceae | 3 | yes | 1 | 6 | yes | 1 (13) |
| Rosa arvensis | Rosaceae | 6 | yes | 1 | 6 | yes | 3 (5) |
| Potentilla sterilis | Rosaceae | 4 | yes | 1 | 6 | yes | 2 (6) |
| Geum rivale | Rosaceae | 5 | yes | 1 | 6 | yes | 1 (2) |
| Prunus padus | Rosaceae | 4 | yes | 1 | 6 | yes | 4 (8) |
| Juncus effusus | Juncaceae | 5 | NO | 3 | 6 | yes | 1 (2) |
| Juncus inflexus | Juncaceae | 4 | NO | 3 | 5 | yes | 3 (3) |
| Juncus articulatus | Juncaceae | 4 | yes | 3 | 6 | yes | 1 (12) |
| Juncus bufonius | Juncaceae | 3 | yes | 3 | 5 | yes | 2 (25) |
| Luzula campestris | Juncaceae | 4 | yes | 3 | 6 | yes | 1 (3) |
| Luzula sylvatica | Juncaceae | 4 | yes | 3 | 6 | yes | 2 (3) |
| Juncus squarrosus | Juncaceae | 3 | yes | 3 | 6 | yes | 4 (6) |
| Lotus corniculatus | Fabaceae | 6 | yes | 1 | 5 | yes | 1 (26) |
| Trifolium repens | Fabaceae | 5 | yes | 1 | 5 | yes | 1 (15) |
| Trifolium pratense | Fabaceae | 5 | yes | 1 | 5 | yes | 1 (13) |
| Vicia cracca | Fabaceae | 6 | yes | 1 | 4 | yes | 1 (20) |
| Ulex europaeus | Fabaceae | 5 | yes | 1 | 6 | NO | 2 (0) |
| Cytisus scoparius | Fabaceae | 5 | yes | 1 | 5 | NO | 3 (0) |
| Lathyrus pratensis | Fabaceae | 6 | yes | 1 | 4 | yes | 2 (33) |
| Medicago lupulina | Fabaceae | 5 | yes | 1 | 5 | yes | 2 (18) |
| Vicia sepium | Fabaceae | 5 | yes | 1 | 4 | yes | 1 (11) |
| Anthyllis vulneraria | Fabaceae | 5 | yes | 1 | 6 | yes | 2 (12) |
| Laburnum anagyroides | Fabaceae | 6 | yes | 1 | 5 | NO | 5 (0) |
| Ononis repens | Fabaceae | 4 | yes | 1 | 5 | yes | 1 (1) |
| Cardamine pratensis | Brassicaceae | 6 | yes | 1 | 5 | NO | 4 (1) |
| Capsella bursa-pastoris | Brassicaceae | 5 | yes | 1 | 5 | yes | 1 (4) |
| Cardamine hirsuta | Brassicaceae | 5 | yes | 1 | 5 | yes | 2 (4) |
| Alliaria petiolata | Brassicaceae | 6 | NO | 1 | 5 | yes | 1 (3) |
| Sinapis arvensis | Brassicaceae | 6 | yes | 1 | 5 | yes | 2 (17) |
| Nasturtium officinale | Brassicaceae | 6 | NO | 1 | 6 | yes | 1 (3) |
| Brassica napus | Brassicaceae | 6 | yes | 1 | 4 | yes | 1 (2) |
| Barbarea vulgaris | Brassicaceae | 5 | yes | 1 | 6 | yes | 1 (4) |
| Lunaria annua | Brassicaceae | 6 | NO | 1 | 5 | yes | 1 (1) |
| Raphanus raphanistrum | Brassicaceae | 5 | yes | 1 | 5 | yes | 3 (17) |
| Hesperis matronalis | Brassicaceae | 6 | yes | 2 | 5 | NO | 3 (0) |
| Thlaspi arvense | Brassicaceae | 5 | yes | 1 | 5 | yes | 2 (18) |
| Cakile maritima | Brassicaceae | 5 | NO | 1 | 6 | yes | 1 (1) |
| Stellaria media | Caryophyllaceae | 4 | yes | 3 | 6 | yes | 2 (9) |
| Stellaria holostea | Caryophyllaceae | 5 | yes | 1 | 6 | yes | 2 (4) |
| Silene dioica | Caryophyllaceae | 5 | yes | 1 | 6 | yes | 1 (1) |
| Silene latifolia | Caryophyllaceae | 4 | yes | 3 | 6 | yes | 1 (5) |
| Silene flos-cuculi | Caryophyllaceae | 5 | yes | 3 | 6 | yes | 1 (1) |
| Silene vulgaris | Caryophyllaceae | 4 | yes | 3 | 6 | yes | 1 (4) |
| Cerastium fontanum | Caryophyllaceae | 4 | yes | 3 | 6 | yes | 1 (12) |
| Sagina procumbens | Caryophyllaceae | 4 | yes | 2 | 5 | yes | 1 (16) |
| Arenaria serpyllifolia | Caryophyllaceae | 4 | yes | 3 | 6 | yes | 5 (11) |
| Spergula arvensis | Caryophyllaceae | 4 | NO | 6 | 6 | yes | 1 (4) |
| Saponaria officinalis | Caryophyllaceae | 4 | yes | 3 | 6 | yes | 1 (1) |
| Agrostemma githago | Caryophyllaceae | 4 | yes | 3 | 6 | yes | 1 (1) |
| Anthriscus sylvestris | Apiaceae | 6 | yes | 1 | 5 | NO | 2 (1) |
| Heracleum sphondylium | Apiaceae | 5 | NO | 1 | 6 | yes | 1 (2) |
| Aegopodium podagraria | Apiaceae | 5 | yes | 1 | 5 | yes | 2 (32) |
| Daucus carota | Apiaceae | 5 | NO | 1 | 5 | NO | 5 (2) |
| Angelica sylvestris | Apiaceae | 4 | yes | 1 | 6 | NO | 6 (4) |
| Conopodium majus | Apiaceae | 4 | yes | 1 | 6 | NO | 7 (1) |
| Conium maculatum | Apiaceae | 4 | yes | 1 | 5 | NO | 7 (2) |
| Oenanthe crocata | Apiaceae | 5 | yes | 1 | 5 | yes | 1 (11) |
| Torilis japonica | Apiaceae | 4 | yes | 1 | 6 | NO | 6 (0) |
| Sanicula europaea | Apiaceae | 4 | NO | 7 | 6 | yes | 1 (1) |
| Smyrnium olusatrum | Apiaceae | 5 | yes | 1 | 5 | NO | 2 (0) |
| Pastinaca sativa | Apiaceae | 5 | yes | 1 | 5 | yes | 1 (1) |
| Helosciadium nodiflorum | Apiaceae | 5 | yes | 1 | 6 | yes | 2 (6) |
| Plantago major | Plantaginaceae | 6 | yes | 1 | 5 | yes | 1 (6) |
| Plantago lanceolata | Plantaginaceae | 5 | yes | 1 | 6 | yes | 1 (1) |
| Veronica chamaedrys | Plantaginaceae | 5 | yes | 1 | 6 | yes | 2 (12) |
| Veronica persica | Plantaginaceae | 4 | yes | 1 | 5 | yes | 4 (10) |
| Veronica beccabunga | Plantaginaceae | 5 | yes | 1 | 6 | yes | 1 (2) |
| Digitalis purpurea | Plantaginaceae | 5 | yes | 1 | 6 | yes | 1 (1) |
| Cymbalaria muralis | Plantaginaceae | 5 | yes | 1 | 5 | yes | 1 (2) |
| Linaria vulgaris | Plantaginaceae | 5 | yes | 2 | 5 | yes | 1 (2) |
| Antirrhinum majus | Plantaginaceae | 5 | yes | 1 | 5 | NO | 4 (0) |
| Callitriche stagnalis | Plantaginaceae | 4 | yes | 1 | 6 | yes | 1 (4) |
| Plantago coronopus | Plantaginaceae | 4 | yes | 3 | 6 | yes | 1 (1) |
| Plantago maritima | Plantaginaceae | 4 | NO | 3 | 6 | yes | 2 (5) |
| Ranunculus repens | Ranunculaceae | 6 | yes | 2 | 6 | yes | 1 (2) |
| Ranunculus acris | Ranunculaceae | 6 | yes | 2 | 6 | yes | 1 (1) |
| Ranunculus bulbosus | Ranunculaceae | 6 | yes | 2 | 5 | yes | 1 (4) |
| Ficaria verna | Ranunculaceae | 5 | yes | 2 | 6 | yes | 1 (1) |
| Caltha palustris | Ranunculaceae | 5 | yes | 6 | 5 | yes | 1 (1) |
| Anemone nemorosa | Ranunculaceae | 4 | yes | 3 | 6 | yes | 1 (4) |
| Clematis vitalba | Ranunculaceae | 5 | yes | 1 | 5 | yes | 1 (2) |
| Aquilegia vulgaris | Ranunculaceae | 4 | yes | 3 | 6 | yes | 1 (1) |
| Ranunculus aquatilis | Ranunculaceae | 5 | yes | 3 | 5 | yes | 1 (5) |
| Ranunculus flammula | Ranunculaceae | 6 | yes | 8 | 5 | yes | 1 (4) |
| Ranunculus sceleratus | Ranunculaceae | 4 | yes | 6 | 5 | NO | 1 (0) |
| Thalictrum flavum | Ranunculaceae | 4 | yes | 2 | 6 | yes | 1 (2) |
| Helleborus foetidus | Ranunculaceae | 4 | yes | 7 | 5 | yes | 1 (2) |
| Ranunculus hederaceus | Ranunculaceae | 5 | yes | 6 | 4 | yes | 1 (2) |
| Lamium album | Lamiaceae | 6 | yes | 1 | 6 | yes | 1 (1) |
| Lamium purpureum | Lamiaceae | 5 | yes | 1 | 5 | yes | 2 (9) |
| Glechoma hederacea | Lamiaceae | 5 | yes | 1 | 4 | yes | 1 (1) |
| Prunella vulgaris | Lamiaceae | 5 | yes | 1 | 5 | yes | 1 (1) |
| Ajuga reptans | Lamiaceae | 5 | yes | 1 | 5 | yes | 1 (1) |
| Stachys sylvatica | Lamiaceae | 5 | yes | 1 | 6 | yes | 1 (3) |
| Stachys palustris | Lamiaceae | 5 | yes | 1 | 4 | yes | 1 (2) |
| Teucrium scorodonia | Lamiaceae | 4 | yes | 1 | 5 | yes | 1 (1) |
| Mentha aquatica | Lamiaceae | 4 | yes | 1 | 5 | yes | 1 (2) |
| Origanum vulgare | Lamiaceae | 3 | yes | 1 | 4 | yes | 1 (8) |
| Thymus drucei | Lamiaceae | 4 | yes | 2 | 5 | yes | 2 (2) |
| Galeopsis tetrahit | Lamiaceae | 4 | yes | 1 | 5 | NO | 8 (5) |
| Lamium galeobdolon | Lamiaceae | 4 | yes | 1 | 4 | yes | 1 (2) |
| Clinopodium vulgare | Lamiaceae | 3 | yes | 1 | 4 | yes | 1 (7) |
| Lycopus europaeus | Lamiaceae | 4 | yes | 1 | 4 | yes | 1 (1) |
| Ballota nigra | Lamiaceae | 4 | yes | 1 | 5 | yes | 2 (3) |
| Scutellaria galericulata | Lamiaceae | 5 | yes | 1 | 4 | yes | 1 (1) |
| Dactylorhiza fuchsii | Orchidaceae | 6 | yes | 2 | 4 | yes | 1 (16) |
| Orchis mascula | Orchidaceae | 5 | yes | 2 | 5 | NO | 3 (0) |
| Ophrys apifera | Orchidaceae | 4 | yes | 2 | 4 | yes | 4 (16) |
| Neottia ovata | Orchidaceae | 6 | NO | 3 | 4 | yes | 1 (11) |
| Epipactis helleborine | Orchidaceae | 5 | yes | 2 | 5 | yes | 1 (3) |
| Anacamptis pyramidalis | Orchidaceae | 4 | yes | 2 | 5 | yes | 5 (11) |
| Dactylorhiza praetermissa | Orchidaceae | 5 | yes | 2 | 5 | yes | 3 (7) |
| Platanthera chlorantha | Orchidaceae | 4 | yes | 2 | 4 | yes | 3 (10) |
| Rumex acetosa | Polygonaceae | 5 | NO | 2 | 6 | yes | 1 (6) |
| Rumex obtusifolius | Polygonaceae | 4 | yes | 1 | 4 | yes | 1 (20) |
| Persicaria maculosa | Polygonaceae | 4 | NO | 6 | 5 | yes | 2 (14) |
| Polygonum aviculare | Polygonaceae | 5 | yes | 1 | 5 | yes | 3 (12) |
| Reynoutria japonica | Polygonaceae | 5 | NO | 6 | 5 | yes | 2 (5) |
| Persicaria amphibia | Polygonaceae | 5 | yes | 1 | 6 | NO | 6 (0) |
| Myosotis arvensis | Boraginaceae | 6 | yes | 1 | 6 | yes | 1 (9) |
| Symphytum officinale | Boraginaceae | 5 | yes | 1 | 5 | NO | 3 (2) |
| Echium vulgare | Boraginaceae | 5 | yes | 1 | 5 | yes | 1 (9) |
| Borago officinalis | Boraginaceae | 5 | yes | 1 | 6 | yes | 3 (8) |
| Myosotis scorpioides | Boraginaceae | 5 | yes | 1 | 6 | NO | 1 (0) |
| Pulmonaria officinalis | Boraginaceae | 5 | yes | 1 | 5 | yes | 1 (2) |
| Chenopodium album | Amaranthaceae | 4 | yes | 2 | 5 | yes | 1 (20) |
| Atriplex prostrata | Amaranthaceae | 4 | yes | 2 | 4 | yes | 1 (3) |
| Beta vulgaris | Amaranthaceae | 4 | yes | 6 | 6 | yes | 2 (6) |
| Salicornia europaea | Amaranthaceae | 5 | yes | 1 | 6 | yes | 1 (5) |
| Suaeda maritima | Amaranthaceae | 3 | yes | 1 | 6 | yes | 3 (6) |
| Rhinanthus minor | Orobanchaceae | 5 | yes | 6 | 5 | yes | 1 (4) |
| Pedicularis sylvatica | Orobanchaceae | 4 | yes | 6 | 6 | yes | 1 (2) |
| Odontites vernus | Orobanchaceae | 4 | yes | 6 | 6 | yes | 1 (2) |
| Melampyrum pratense | Orobanchaceae | 4 | yes | 6 | 5 | yes | 1 (4) |
| Lathraea squamaria | Orobanchaceae | 4 | yes | 2 | 5 | yes | 1 (1) |
| Orobanche minor | Orobanchaceae | 3 | yes | 2 | 4 | yes | 1 (7) |
| Allium ursinum | Amaryllidaceae | 6 | yes | 1 | 6 | yes | 1 (1) |
| Galanthus nivalis | Amaryllidaceae | 6 | yes | 1 | 5 | yes | 1 (5) |
| Narcissus pseudonarcissus | Amaryllidaceae | 6 | yes | 1 | 5 | yes | 1 (7) |
| Allium triquetrum | Amaryllidaceae | 5 | NO | 2 | 5 | yes | 1 (5) |
| Calluna vulgaris | Ericaceae | 6 | yes | 1 | 6 | yes | 1 (6) |
| Erica cinerea | Ericaceae | 5 | yes | 1 | 6 | yes | 2 (8) |
| Erica tetralix | Ericaceae | 6 | yes | 1 | 6 | yes | 2 (4) |
| Vaccinium myrtillus | Ericaceae | 5 | yes | 1 | 6 | yes | 1 (3) |
| Rhododendron ponticum | Ericaceae | 5 | yes | 2 | 6 | yes | 1 (1) |
| Arbutus unedo | Ericaceae | 4 | yes | 1 | 6 | yes | 1 (1) |
| Empetrum nigrum | Ericaceae | 4 | yes | 1 | 6 | yes | 1 (4) |
| Iris pseudacorus | Iridaceae | 6 | yes | 2 | 6 | yes | 1 (2) |
| Iris foetidissima | Iridaceae | 6 | yes | 3 | 6 | yes | 1 (1) |
| Hyacinthoides non-scripta | Asparagaceae | 6 | yes | 1 | 6 | yes | 1 (8) |
| Polygonatum multiflorum | Asparagaceae | 5 | yes | 1 | 6 | yes | 1 (2) |
| Ornithogalum umbellatum | Asparagaceae | 6 | yes | 2 | 5 | yes | 3 (5) |
| Convallaria majalis | Asparagaceae | 6 | yes | 1 | 6 | yes | 1 (1) |
| Ruscus aculeatus | Asparagaceae | 4 | NO | 7 | 5 | yes | 1 (1) |
| Geranium robertianum | Geraniaceae | 6 | yes | 1 | 6 | yes | 1 (15) |
| Geranium molle | Geraniaceae | 5 | yes | 1 | 6 | yes | 1 (3) |
| Geranium pratense | Geraniaceae | 6 | yes | 1 | 6 | yes | 1 (4) |
| Erodium cicutarium | Geraniaceae | 5 | yes | 1 | 6 | NO | 9 (5) |
| Geranium sanguineum | Geraniaceae | 6 | yes | 1 | 6 | yes | 2 (3) |
| Campanula rotundifolia | Campanulaceae | 5 | yes | 6 | 6 | yes | 1 (7) |
| Campanula trachelium | Campanulaceae | 6 | NO | 7 | 6 | yes | 1 (2) |
| Jasione montana | Campanulaceae | 4 | yes | 4 | 6 | yes | 2 (5) |
| Primula vulgaris | Primulaceae | 6 | yes | 4 | 6 | yes | 1 (3) |
| Primula veris | Primulaceae | 5 | yes | 2 | 6 | NO | 1 (0) |
| Lysimachia nummularia | Primulaceae | 5 | yes | 7 | 6 | yes | 2 (3) |
| Lysimachia vulgaris | Primulaceae | 5 | yes | 10 | 5 | NO | 1 (0) |
| Lysimachia arvensis | Primulaceae | 5 | yes | 7 | 6 | yes | 1 (4) |
| Lysimachia nemorum | Primulaceae | 5 | yes | 7 | 6 | yes | 1 (2) |
| Sedum acre | Crassulaceae | 5 | yes | 2 | 6 | NO | 3 (2) |
| Sedum album | Crassulaceae | 4 | yes | 2 | 5 | yes | 1 (6) |
| Umbilicus rupestris | Crassulaceae | 4 | NO | 12 | 4 | NO | 1 (0) |
| Hylotelephium telephium | Crassulaceae | 5 | yes | 1 | 5 | yes | 1 (2) |
| Athyrium filix-femina | Aspleniaceae | 4 | yes | 1 | 5 | yes | 1 (3) |
| Asplenium scolopendrium | Aspleniaceae | 4 | yes | 1 | 5 | yes | 1 (1) |
| Asplenium trichomanes | Aspleniaceae | 4 | yes | 1 | 4 | yes | 1 (6) |
| Asplenium ruta-muraria | Aspleniaceae | 4 | yes | 1 | 3 | NO | 5 (1) |
| Blechnum spicant | Aspleniaceae | 4 | yes | 1 | 5 | yes | 1 (1) |
| Dryopteris filix-mas | Polypodiaceae | 4 | yes | 2 | 4 | yes | 2 (6) |
| Dryopteris dilatata | Polypodiaceae | 4 | yes | 2 | 4 | yes | 1 (6) |
| Polypodium vulgare | Polypodiaceae | 4 | yes | 2 | 4 | yes | 1 (2) |
| Pteridium aquilinum | Dennstaedtiaceae | 4 | yes | 3 | 3 | yes | 1 (1) |
| Polystichum setiferum | Polypodiaceae | 4 | yes | 2 | 4 | yes | 5 (6) |
| Equisetum arvense | Equisetaceae | 5 | yes | 1 | 3 | NO | 1 (0) |
| Equisetum fluviatile | Equisetaceae | 5 | yes | 1 | 3 | yes | 1 (1) |
| Equisetum telmateia | Equisetaceae | 4 | yes | 1 | 3 | NO | 2 (0) |
| Huperzia selago | Lycopodiaceae | 4 | yes | 2 | 4 | yes | 1 (5) |
| Ophioglossum vulgatum | Ophioglossaceae | 3 | yes | 2 | 3 | yes | 1 (2) |
| Lonicera periclymenum | Caprifoliaceae | 6 | yes | 2 | 6 | yes | 1 (3) |
| Knautia arvensis | Caprifoliaceae | 5 | yes | 3 | 6 | yes | 1 (3) |
| Succisa pratensis | Caprifoliaceae | 4 | yes | 3 | 6 | yes | 1 (2) |
| Dipsacus fullonum | Caprifoliaceae | 4 | yes | 2 | 4 | NO | 3 (1) |
| Valeriana officinalis | Caprifoliaceae | 4 | yes | 3 | 6 | yes | 1 (1) |
| Centranthus ruber | Caprifoliaceae | 4 | yes | 6 | 6 | yes | 2 (3) |
| Sambucus nigra | Viburnaceae | 6 | yes | 3 | 6 | NO | 1 (0) |
| Viburnum opulus | Viburnaceae | 5 | yes | 3 | 5 | yes | 1 (1) |
| Adoxa moschatellina | Viburnaceae | 3 | NO | 22 | 6 | NO | 1 (0) |
| Symphoricarpos albus | Caprifoliaceae | 4 | yes | 2 | 6 | yes | 1 (1) |
| Papaver rhoeas | Papaveraceae | 6 | yes | 3 | 6 | yes | 1 (4) |
| Fumaria officinalis | Papaveraceae | 4 | yes | 7 | 6 | yes | 1 (2) |
| Chelidonium majus | Papaveraceae | 5 | yes | 1 | 4 | yes | 1 (2) |
| Pseudofumaria lutea | Papaveraceae | 4 | yes | 7 | 4 | NO | 10 (5) |
| Chrysosplenium oppositifolium | Saxifragaceae | 5 | yes | 5 | 6 | yes | 1 (2) |
| Saxifraga granulata | Saxifragaceae | 4 | yes | 14 | 6 | NO | 4 (3) |
| Epilobium hirsutum | Onagraceae | 6 | yes | 2 | 6 | yes | 1 (1) |
| Chamaenerion angustifolium | Onagraceae | 5 | yes | 6 | 6 | yes | 1 (1) |
| Epilobium montanum | Onagraceae | 4 | yes | 2 | 6 | yes | 1 (4) |
| Circaea lutetiana | Onagraceae | 3 | yes | 1 | 6 | yes | 2 (4) |
| Fuchsia magellanica | Onagraceae | 4 | yes | 4 | 6 | yes | 1 (1) |
| Potamogeton natans | Potamogetonaceae | 6 | yes | 2 | 6 | yes | 1 (11) |
| Potamogeton crispus | Potamogetonaceae | 5 | yes | 2 | 5 | yes | 1 (2) |
| Salix caprea | Salicaceae | 4 | yes | 1 | 5 | NO | 2 (0) |
| Salix alba | Salicaceae | 4 | yes | 1 | 5 | NO | 2 (0) |
| Populus tremula | Salicaceae | 3 | yes | 1 | 6 | yes | 1 (3) |
| Salix repens | Salicaceae | 4 | yes | 1 | 5 | yes | 4 (6) |
| Galium aparine | Rubiaceae | 5 | yes | 1 | 6 | yes | 1 (2) |
| Galium verum | Rubiaceae | 4 | yes | 2 | 5 | yes | 1 (1) |
| Galium saxatile | Rubiaceae | 4 | yes | 2 | 6 | yes | 1 (1) |
| Galium odoratum | Rubiaceae | 4 | yes | 2 | 6 | yes | 1 (1) |
| Galium palustre | Rubiaceae | 4 | yes | 2 | 6 | yes | 1 (8) |
| Armeria maritima | Plumbaginaceae | 5 | yes | 1 | 6 | yes | 1 (2) |
| Limonium vulgare | Plumbaginaceae | 4 | yes | 14 | 6 | NO | 7 (4) |
| Euphorbia helioscopia | Euphorbiaceae | 4 | yes | 1 | 6 | NO | 5 (3) |
| Euphorbia peplus | Euphorbiaceae | 4 | yes | 1 | 5 | NO | 10 (8) |
| Mercurialis perennis | Euphorbiaceae | 4 | yes | 5 | 6 | yes | 1 (4) |
| Euphorbia amygdaloides | Euphorbiaceae | 3 | yes | 1 | 6 | NO | 3 (2) |
| Hypericum perforatum | Hypericaceae | 6 | yes | 1 | 6 | yes | 3 (8) |
| Hypericum hirsutum | Hypericaceae | 4 | yes | 2 | 5 | yes | 1 (1) |
| Hypericum tetrapterum | Hypericaceae | 5 | NO | 11 | 5 | yes | 1 (3) |
| Hypericum androsaemum | Hypericaceae | 4 | yes | 4 | 5 | yes | 3 (10) |
| Centaurium erythraea | Gentianaceae | 4 | yes | 16 | 6 | yes | 1 (3) |
| Blackstonia perfoliata | Gentianaceae | 3 | yes | 17 | 5 | yes | 1 (1) |
| Gentiana pneumonanthe | Gentianaceae | 4 | yes | 10 | 6 | NO | 1 (0) |
| Carpobrotus edulis | Aizoaceae | 5 | yes | 2 | 6 | yes | 1 (1) |
| Malva sylvestris | Malvaceae | 5 | yes | 9 | 6 | yes | 2 (4) |
| Malva moschata | Malvaceae | 5 | yes | 9 | 5 | yes | 1 (4) |
| Tilia cordata | Malvaceae | 4 | yes | 3 | 6 | yes | 1 (2) |
| Hydrocharis morsus-ranae | Hydrocharitaceae | 5 | yes | 1 | 6 | NO | 3 (0) |
| Elodea canadensis | Hydrocharitaceae | 4 | yes | 3 | 6 | NO | 6 (4) |
| Pinus sylvestris | Pinaceae | 4 | yes | 1 | 4 | yes | 1 (10) |
| Picea abies | Pinaceae | 4 | yes | 1 | 3 | yes | 3 (10) |
| Larix decidua | Pinaceae | 4 | yes | 1 | 4 | yes | 2 (10) |
| Alisma plantago-aquatica | Alismataceae | 6 | yes | 1 | 6 | yes | 1 (3) |
| Sagittaria sagittifolia | Alismataceae | 5 | yes | 2 | 6 | yes | 1 (1) |
| Betula pendula | Betulaceae | 4 | yes | 1 | 6 | NO | 1 (0) |
| Alnus glutinosa | Betulaceae | 4 | yes | 1 | 6 | yes | 1 (2) |
| Corylus avellana | Betulaceae | 4 | yes | 1 | 6 | NO | 2 (1) |
| Carpinus betulus | Betulaceae | 3 | yes | 1 | 5 | yes | 3 (4) |
| Hedera helix | Araliaceae | 5 | yes | 4 | 6 | yes | 1 (1) |
| Hydrocotyle vulgaris | Araliaceae | 4 | yes | 23 | 6 | yes | 1 (2) |
| Pinguicula vulgaris | Lentibulariaceae | 5 | yes | 1 | 6 | NO | 1 (0) |
| Utricularia vulgaris | Lentibulariaceae | 5 | yes | 4 | 6 | yes | 2 (3) |
| Fritillaria meleagris | Liliaceae | 5 | yes | 6 | 6 | yes | 1 (2) |
| Hemerocallis fulva | Asphodelaceae | 6 | yes | 7 | 5 | yes | 1 (3) |
| Acer pseudoplatanus | Sapindaceae | 4 | yes | 1 | 6 | yes | 1 (1) |
| Acer campestre | Sapindaceae | 4 | yes | 1 | 5 | yes | 1 (2) |
| Aesculus hippocastanum | Sapindaceae | 5 | yes | 1 | 6 | yes | 1 (1) |
| Calystegia sepium | Convolvulaceae | 6 | yes | 3 | 6 | yes | 1 (2) |
| Convolvulus arvensis | Convolvulaceae | 5 | yes | 4 | 5 | yes | 1 (1) |
| Quercus robur | Fagaceae | 5 | yes | 1 | 6 | yes | 1 (2) |
| Fagus sylvatica | Fagaceae | 4 | yes | 2 | 5 | yes | 1 (2) |
| Castanea sativa | Fagaceae | 4 | yes | 2 | 5 | NO | 1 (0) |
| Fraxinus excelsior | Oleaceae | 4 | yes | 2 | 5 | yes | 1 (1) |
| Ligustrum vulgare | Oleaceae | 5 | yes | 6 | 6 | NO | 1 (0) |
| Typha latifolia | Typhaceae | 5 | NO | 6 | 6 | NO | 2 (0) |
| Sparganium erectum | Typhaceae | 5 | NO | 4 | 6 | yes | 1 (4) |
| Urtica dioica | Urticaceae | 5 | yes | 1 | 6 | yes | 1 (1) |
| Parietaria judaica | Urticaceae | 3 | yes | 12 | 6 | yes | 2 (4) |
| Soleirolia soleirolii | Urticaceae | 4 | yes | 9 | 6 | NO | 4 (2) |
| Ribes uva-crispa | Grossulariaceae | 5 | yes | 2 | 6 | yes | 1 (4) |
| Ribes rubrum | Grossulariaceae | 4 | yes | 3 | 6 | yes | 2 (4) |
| Ribes sanguineum | Grossulariaceae | 4 | yes | 6 | 5 | yes | 2 (2) |
| Cornus sanguinea | Cornaceae | 5 | yes | 7 | 6 | yes | 1 (3) |
| Myriophyllum spicatum | Haloragaceae | 5 | yes | 3 | 6 | yes | 2 (2) |
| Helianthemum nummularium | Cistaceae | 6 | yes | 6 | 6 | yes | 1 (4) |
| Linum catharticum | Linaceae | 4 | yes | 18 | 6 | yes | 1 (2) |
| Arum maculatum | Araceae | 5 | yes | 1 | 6 | yes | 1 (2) |
| Lemna minor | Araceae | 4 | yes | 5 | 5 | yes | 1 (6) |
| Scrophularia nodosa | Scrophulariaceae | 5 | yes | 2 | 6 | yes | 1 (3) |
| Verbascum thapsus | Scrophulariaceae | 4 | yes | 15 | 6 | yes | 1 (5) |
| Buddleja davidii | Scrophulariaceae | 4 | yes | 5 | 6 | NO | 1 (0) |
| Solanum dulcamara | Solanaceae | 6 | yes | 4 | 6 | yes | 1 (3) |
| Solanum nigrum | Solanaceae | 4 | yes | 4 | 5 | yes | 1 (4) |
| Oxalis acetosella | Oxalidaceae | 5 | yes | 6 | 6 | NO | 2 (1) |
| Oxalis corniculata | Oxalidaceae | 4 | yes | 6 | 5 | yes | 1 (4) |
| Viola riviniana | Violaceae | 6 | yes | 8 | 6 | yes | 1 (5) |
| Viola odorata | Violaceae | 5 | yes | 8 | 6 | yes | 2 (4) |
| Viola arvensis | Violaceae | 4 | yes | 8 | 5 | NO | 1 (0) |
| Ilex aquifolium | Aquifoliaceae | 4 | yes | 3 | 6 | yes | 1 (1) |
| Taxus baccata | Taxaceae | 4 | yes | 2 | 4 | yes | 1 (1) |
| Drosera rotundifolia | Droseraceae | 4 | yes | 2 | 6 | NO | 1 (0) |
| Impatiens glandulifera | Balsaminaceae | 5 | yes | 6 | 6 | yes | 1 (1) |
| Menyanthes trifoliata | Menyanthaceae | 4 | NO | 40 | 6 | yes | 1 (1) |
| Nymphaea alba | Nymphaeaceae | 6 | yes | 2 | 6 | yes | 1 (1) |
| Nuphar lutea | Nymphaeaceae | 5 | yes | 9 | 6 | yes | 1 (2) |
| Humulus lupulus | Cannabaceae | 4 | yes | 3 | 6 | yes | 1 (1) |
| Ulmus glabra | Ulmaceae | 4 | yes | 2 | 6 | yes | 1 (3) |
| Lythrum salicaria | Lythraceae | 5 | yes | 9 | 6 | yes | 1 (1) |
| Polygala vulgaris | Polygalaceae | 4 | yes | 16 | 5 | yes | 1 (2) |
| Reseda luteola | Resedaceae | 4 | NO | 32 | 6 | yes | 1 (1) |
| Euonymus europaeus | Celastraceae | 3 | yes | 8 | 6 | yes | 1 (1) |
| Vinca minor | Apocynaceae | 5 | yes | 13 | 6 | yes | 1 (1) |
| Montia fontana | Montiaceae | 3 | yes | 18 | 6 | yes | 1 (1) |
| Narthecium ossifragum | Nartheciaceae | 6 | yes | 3 | 6 | yes | 1 (1) |
| Thuja plicata | Cupressaceae | 4 | yes | 2 | 3 | yes | 1 (3) |
| Juglans regia | Juglandaceae | 4 | yes | 1 | 5 | yes | 1 (1) |
| Mahonia aquifolium | Berberidaceae | 5 | yes | 3 | 6 | yes | 1 (1) |
| Buxus sempervirens | Buxaceae | 4 | yes | 8 | 6 | yes | 1 (1) |
| Tamus communis | Dioscoreaceae | 5 | yes | 5 | 6 | yes | 1 (1) |
| Bryonia dioica | Cucurbitaceae | 5 | yes | 1 | 5 | yes | 1 (1) |
| Frangula alnus | Rhamnaceae | 4 | yes | 8 | 6 | yes | 1 (2) |
| Daphne laureola | Thymelaeaceae | 4 | yes | 9 | 6 | yes | 1 (1) |
| Rhamnus cathartica | Rhamnaceae | 5 | yes | 2 | 6 | yes | 1 (2) |
| Ulex gallii | Fabaceae | 5 | yes | 1 | 5 | NO | 3 (0) |
| Trifolium arvense | Fabaceae | 4 | yes | 1 | 5 | NO | 9 (0) |
| Hippuris vulgaris | Plantaginaceae | 5 | yes | 1 | 6 | yes | 1 (3) |
| Lysimachia tenella | Primulaceae | 5 | yes | 7 | 6 | yes | 3 (4) |
| Lotus pedunculatus | Fabaceae | 4 | yes | 1 | 5 | yes | 1 (2) |
| Vicia sativa | Fabaceae | 5 | yes | 1 | 5 | yes | 2 (7) |
| Cirsium acaule | Asteraceae | 4 | yes | 1 | 6 | yes | 5 (13) |
| Bromopsis ramosa | Poaceae | 3 | yes | 1 | 6 | yes | 3 (11) |
| Carex riparia | Cyperaceae | 5 | yes | 1 | 6 | yes | 3 (10) |
| Juncus conglomeratus | Juncaceae | 4 | NO | 3 | 6 | yes | 2 (3) |
| Luzula multiflora | Juncaceae | 4 | yes | 3 | 6 | yes | 2 (7) |
| Rumex crispus | Polygonaceae | 4 | yes | 1 | 4 | yes | 1 (9) |
