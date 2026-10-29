# Forensic Peer Review: `FEXP_ANON_111`

**Overall Score:** **2.5 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.9 / 8.0**
* **Score Breakdown:** Rigor: 0.6/3.5 | Claims: 0.5/2.5 | Biology: 0.9/2.0 | Reproducibility: 0.5/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Field & Subfield:** Ecological Niche Modeling (ENM) / Species Distribution Modeling (SDM), Plant Biogeography, and Ornamental/Medicinal Germplasm Management (*Hibiscus mutabilis* L., Malvaceae, in China).
* **Perceived Study Design:** Single-algorithm (`MaxEnt v.3.4.4`), single-GCM (`BCC-CSM2-MR`) correlative bioclimatic projection across 374 Chinese occurrence records and 19 WorldClim variables (reduced to 11 variables) under contemporary (1970–2000) and future (2050s, 2070s, 2090s; SSP1-2.6, SSP2-4.5, SSP5-8.5) scenarios.
* **Implicit Temporal Horizon:** Herbarium/GBIF collection records accessed May 2024, paired with 1970–2000 baseline climate and CMIP6 projections through the 2090s.

---

## 2. Executive Summary & Editorial Verdict

This manuscript applies default-parameter `MaxEnt v.3.4.4` to 374 Chinese occurrence records of *Hibiscus mutabilis* (Confederate rose / Cotton rose) and 11 WorldClim bioclimatic variables to project contemporary and future habitat suitability under three SSP scenarios using a single climate model (`BCC-CSM2-MR`). A forensic audit reveals that every single quantitative table and figure referenced in the manuscript (`Table 1`, `Table 2`, `Table 3`, and `Figures 1–8`) is completely absent from the text, despite the Data Availability Statement claiming *"Data are contained within the article."* Furthermore, the manuscript contains direct internal contradictions on the geographic coordinates of the contemporary and future distribution centroids, garbled and self-contradictory numerical reporting of future habitat area changes, failure to separate cultivated/ornamental plantings from wild populations, and reliance on an uncalibrated single-GCM default `MaxEnt` pipeline.

### Claim-by-Claim Evaluation

1. **Claim 1:** Under low-to-medium emission scenarios (`SSP1-2.6` and `SSP2-4.5`), the highly suitable habitat area for *H. mutabilis* decreases in the 2050s and 2070s by precisely stated amounts, whereas under `SSP5-8.5` it increases before decreasing (Abstract; Section 3.3.2, line 85; Table 2). **`[Methodologically Flawed]`**
   * **Audit Verification:** First, `Table 2` is completely missing from the manuscript, making it impossible to verify the baseline or future area breakdowns across suitability classes. Second, the prose reporting these numbers in Section 3.3.2 (line 85) is garbled and self-contradictory: *"Under the SSP126 and SSP245 climate scenarios, the area of suitable habitats will initially decrease and then increase. Specifically, by the 2050s and 2070s, the area of highly suitable habitats will decrease by 13.06 × 10⁴ km² and 7.64 × 10⁴ km² and 7.64 × 10⁴ km² and 3.06 × 10⁴ km², respectively."* Not only is `7.64 × 10⁴ km²` duplicated without specifying which number corresponds to which SSP scenario or decade, but the Abstract (line 5) and Conclusion (line 135) make conflicting statements about whether `total suitable area` or `highly suitable area` decreases throughout `SSP1-2.6` and `SSP2-4.5`. Third, all future projections rely exclusively on a single Global Climate Model (`BCC-CSM2-MR`; Section 2.1.2, line 32), so inter-decadal oscillations reflect single-GCM internal realization variability rather than a multi-model CMIP6 ensemble signal.
2. **Claim 2:** The contemporary distribution centroid of *H. mutabilis* is located at `109°23′53″ E, 27°30′08″ N`, and under `SSP1-2.6` it shifts to `Zhijiang Dong Autonomous County, Huaihua City, Hunan Province (109°45′42″ E, 27°37′40″ N)` in the 2070s and then relocates to `Songtao Miao Autonomous County, Tongren City, Guizhou Province (109°45′42″ E, 27°37′40″ N)` in the 2090s (Section 3.4.2, lines 98–104; Section 4.2, line 123). **`[Methodologically Flawed]`**
   * **Audit Verification:** The centroid analysis contains two blatant geographic and coordinate contradictions:
     - **Identical Coordinates Assigned to Two Different Provinces and Distances:** In Section 3.4.2 (line 100), the 2070s `SSP1-2.6` centroid in `Zhijiang Dong Autonomous County, Huaihua City, Hunan Province` (38.81 km NE of the contemporary center) and the 2090s `SSP1-2.6` centroid in `Songtao Miao Autonomous County, Tongren City, Guizhou Province` (72.84 km from the contemporary center) are given the **exact same latitude and longitude (`109°45′42″ E, 27°37′40″ N`)**. Moreover, `109°45′42″ E, 27°37′40″ N` actually lies in Hecheng/Zhongfang (east of Zhijiang in Hunan), whereas Songtao County in Guizhou lies around `109°00′–109°12′ E, 28°00′–28°15′ N`.
     - **Contradictory County Identification and Azimuth Directions:** Section 3.4.2 (line 98) identifies `109°23′53″ E, 27°30′08″ N` generally as `Huaihua City, Hunan Province`, whereas Section 4.2 (line 123) states it is in `Zhijiang Dong Autonomous County`, even though line 100 says the centroid only moves *to* Zhijiang in the 2070s. Similarly, in Section 3.4.2 (line 104), the 2090s `SSP5-8.5` centroid in `Sinan County, Tongren City, Guizhou Province (108°00′37″ E, 27°43′47″ N)` is described as moving *"approximately 150.25 km northeast from the contemporary center (`109°23′53″ E, 27°30′08″ N`)"*, even though moving from `109°23′53″ E` to `108°00′37″ E` is a shift of $1^\circ 23'$ **west** (specifically west-northwest, not northeast).
3. **Claim 3:** Precipitation of the driest month (`bio14`) and annual precipitation (`bio12`) account for `82.2%` of the model contribution (`Table 1`), proving that natural distribution limits of *H. mutabilis* are governed primarily by drought intolerance (Section 3.2, lines 68–70; Section 4.1, lines 112–113). **`[Fragile]`**
   * **Audit Verification:** First, `Table 1` is missing from the manuscript, and Section 3.2 reports only `MaxEnt` heuristic percent contribution rates (`bio14` + `bio12` = 82.2%) while omitting all permutation importance values (despite Abstract line 5 and Section 2.2.1 line 40 claiming permutation importance was analyzed). Because `bio14` and `bio12` are collinear precipitation metrics and five precipitation variables (`bio14`, `bio12`, `bio19`, `bio18`, `bio8`, `bio15` — actually six precipitation variables!) were simultaneously retained alongside five temperature variables, heuristic path-dependent percent contribution is confounded by residual collinearity. Second, as acknowledged in Section 1 (line 14), *H. mutabilis* is *"a common ornamental plant... extensively planted and utilized for its outstanding landscape aesthetics"*. The authors did not filter out cultivated/urban park specimen records from GBIF/CVH/NSII (Section 2.1.1, line 27), nor did they apply target-group background correction for collection bias across densely populated southeastern Chinese cities.

---

## 3. Forensic Defect Inventory

### Defect 1: Complete Omission of All Quantitative Tables (`Tables 1–3`) and Figures (`Figures 1–8`) (`[Critical / Fatal]`)
* **Location:** Section 2.1.1 (line 27, citing `Figure 1` and `Figure 2`), Section 3.1 (line 63, citing `Figure 3`), Section 3.2 (lines 68–70, citing `Table 1` and `Figure 4`), Section 3.3 (lines 78–85, citing `Figure 5`, `Figure 6`, and `Table 2`), Section 3.4 (lines 93–98, citing `Figure 7`, `Table 3`, and `Figure 8`), and Data Availability Statement (line 140).
* **Mechanism:** None of the three data tables (`Table 1`: variable contributions/permutation importance; `Table 2`: suitable habitat areas across periods/SSPs; `Table 3`: spatial retention/loss/gain areas) or eight figures exist anywhere in the manuscript, and no raw occurrence coordinates or supplementary files are provided, rendering the Data Availability Statement (*"Data are contained within the article"*) false.

### Defect 2: Geographic Coordinate Duplication and Directional Contradictions in Centroid Migration Analysis (`[Critical]`)
* **Location:** Section 3.4.2 (lines 98–104) and Section 4.2 (line 123).
* **Mechanism:**
  1. Line 100 assigns the exact same coordinate pair (`109°45′42″ E, 27°37′40″ N`) to both `Zhijiang Dong Autonomous County, Huaihua City, Hunan Province` (2070s `SSP1-2.6`, 38.81 km NE) and `Songtao Miao Autonomous County, Tongren City, Guizhou Province` (2090s `SSP1-2.6`, 72.84 km away).
  2. Line 104 claims that shifting from `109°23′53″ E, 27°30′08″ N` (Huaihua, Hunan) to `108°00′37″ E, 27°43′47″ N` (Sinan County, Guizhou) is a `150.25 km northeast` migration, when $108^\circ 00'\text{ E}$ is $1^\circ 23'$ **west** of $109^\circ 23'\text{ E}$ (and the great-circle distance between those two coordinates is $\approx 139.3\text{ km}$ WNW, not $150.25\text{ km}$ NE).
  3. Line 100 also claims that shifting from `109°23′53″ E, 27°30′08″ N` to `109°45′42″ E, 27°37′40″ N` is `38.81 km northeast` and that shifting to `108°59′49″ E, 27°27′10″ N` (line 102) is `40.45 km`—numbers that are inconsistent with the stated coordinate pairs when `Songtao` is given the duplicate coordinate.

### Defect 3: Garbled Numerical Reporting in Section 3.3.2 and Single-GCM / Default-MaxEnt Methodological Fragility (`[Major]`)
* **Location:** Section 2.1.2 (line 32), Section 2.2.2 (line 45), Section 2.2.4 (line 55), and Section 3.3.2 (line 85).
* **Mechanism:**
  1. Line 85 reads: *"Specifically, by the 2050s and 2070s, the area of highly suitable habitats will decrease by 13.06 × 10⁴ km² and 7.64 × 10⁴ km² and 7.64 × 10⁴ km² and 3.06 × 10⁴ km², respectively."* This unedited duplication of `7.64 × 10⁴ km²` leaves the reader unable to determine the actual projected changes under `SSP1-2.6` vs. `SSP2-4.5`.
  2. Section 2.2.4 (line 55) makes the nonsensical methodological statement that *"Using the current suitable habitat area as a reference, the MaxEnt model was employed to cross-validate the suitable habitats under past and future scenarios"*, even though no paleoclimatic ("past") scenarios were run and `MaxEnt` cannot "cross-validate" future projections for which no occurrence data exist.
  3. Section 3.1 (line 63) claims *"In the output results for the three different climate scenarios across three future periods, the AUC values for both the training and testing datasets are also above 0.9."* Because `MaxEnt` projects a trained contemporary model onto future climate layers (or if the authors mistakenly re-fitted `MaxEnt` using contemporary 2024 occurrence points against 2050s/2070s/2090s future climate layers!), reporting distinct "future training and testing AUC values" either reflects a fundamental misunderstanding of SDM projection or an invalid re-fitting of contemporary presences onto future climate grids.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Max | Awarded | Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **3.5** | **0.6** | Default-parameter `MaxEnt` on unscreened ornamental/cultivated records, single-GCM (`BCC-CSM2-MR`) projections, retention of 6 collinear precipitation variables, invalid claim of "future training and testing AUC" / "cross-validating past and future scenarios", and coordinate/direction math errors. |
| **2. Claim-Evidence Alignment** | **2.5** | **0.5** | Every table (`Tables 1–3`) and figure (`Figures 1–8`) is missing; text contains garbled duplicate numbers (`7.64 × 10⁴ km² and 7.64 × 10⁴ km²`) and assigns identical coordinates to counties in Hunan and Guizhou while reversing east and west. |
| **3. Biological / Domain Validity** | **2.0** | **0.9** | The general association of *H. mutabilis* with warm, humid subtropical monsoon climates in southeastern China and its frost sensitivity in northern China is biologically sound, though conflating ornamental plantings with wild niche limits weakens ecological inference. |
| **4. Reproducibility & Transparency** | **2.0** | **0.5** | All tables, figures, occurrence coordinates, and scripts are absent despite the false Data Availability Statement (*"Data are contained within the article"*). |
| **TOTAL** | **10.0** | **2.5** | **Scientific Core Score: 1.9 / 8.0** (Fundamentally Invalid) |
