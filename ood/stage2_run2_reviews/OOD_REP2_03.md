# Review of OOD_REP2_03

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.3 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.3/3.5 | Claims: 1.2/2.5 | Biology: 1.1/2.0 | Reproducibility: 0.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study applies Maximum Entropy (MaxEnt) species distribution modeling to predict the current and future (2050 and 2070 under RCP 4.5 and RCP 8.5) habitat suitability across Iran for three medicinal thyme species (*Thymus fedtschenkoi*, *T. pubescens*, and *T. transcaucasicus*). Using occurrence records compiled from Iranian herbaria, GBIF, literature, and fieldwork alongside 9 candidate environmental predictors (5 WorldClim bioclimatic variables, 1 SoilGrids edaphic variable, and 3 topographic variables at 30 arc-second resolution), the authors report 10-fold cross-validation $\text{AUC}$ values of $0.940$–$0.975$ and project net habitat contractions of $8.71\%$ to $29.89\%$ across scenarios. Occurrence coordinates and analysis scripts are not publicly archived ("available... on reasonable request").

While mapping climate vulnerability for endemic Irano-Turanian and Hyrcanian medicinal plants is a worthwhile conservation goal, the study's modeling pipeline and reporting suffer from major methodological and technical flaws. First, the manuscript never reports the sample size ($N$ of occurrence records) for any of the three species, nor does it apply spatial thinning to correct for herbarium and roadside collection bias. Second, static non-climatic predictors (altitude, solar radiation, slope, and soil organic carbon) account for $63.2\%$ to $81.2\%$ of the MaxEnt percent contribution (and $88.7\%$ of permutation importance in *T. fedtschenkoi*), confounding temperature lapse rates with static elevation and artificially constraining upslope range shifts under future warming. Third, variable selection was performed inconsistently across species over the same national extent based on post-hoc model contribution. Finally, the manuscript contains pervasive figure/table cross-reference errors, swapped latitude/longitude coordinates, incorrect physical units, and an arithmetic error in Table 3. Addressing these flaws requires reporting full occurrence counts, applying spatial rarefaction, removing static altitude from climate-change projections, and correcting the manuscript's tables and cross-references.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **MaxEnt models achieve excellent predictive accuracy ($\text{AUC} = 0.940$–$0.975$) for the three *Thymus* species across Iran: [Fragile].**  
  When modeling narrow-ranged montane species (restricted to the Alborz and Zagros mountains) across an entire national bounding box of $1.65 \times 10^6\text{ km}^2$ dominated by arid central deserts (Dasht-e Kavir and Dasht-e Lut), random background points fall overwhelmingly in desert environments. Under this setup, $\text{AUC} > 0.94$ is an artifact of an overly broad background extent and unthinned spatial clustering of herbarium records. Moreover, the manuscript omits the number of presence records ($N$) per species, the standard deviation of $\text{AUC}$ across the 10 cross-validation folds, the number of background points, the regularization multiplier, and the omission error rates at the chosen binarization threshold.

* **Altitude and soil organic carbon are the primary physiological determinants of *Thymus* distribution ($33.8\%$–$47.9\%$ and $34.6\%$ contribution): [Methodologically Flawed].**  
  In Results (line 94) and Table 2, static topographic and edaphic layers (`Alt`, `Solar`, `Slope`, `Ocr`) comprise $68.3\%$ of the total percent contribution for *T. fedtschenkoi* (and $88.7\%$ of its permutation importance, with `Solar` alone at $65.6\%$), $81.2\%$ for *T. pubescens*, and $63.2\%$ for *T. transcaucasicus*. As the authors note in the Discussion (line 189), elevation acts biologically through the atmospheric thermal lapse rate and precipitation gradients. Including static `Altitude` alongside temperature (`bio9`, `bio2`) in a climate-change SDM creates severe collinearity and treats meters above sea level as a direct physiological requirement. Furthermore, the authors state (lines 49 and 94) that Pearson's $|r| > 0.70$ was used to exclude collinear variables across Iran, yet different pairs of climatic variables (`bio2`, `bio9`, `bio14`, `bio15`) were excluded for different species after inspecting their MaxEnt percent contributions (line 95).

* **All three *Thymus* species will experience $8.71\%$ to $29.89\%$ net habitat loss by 2050 and 2070 under RCP 4.5 and RCP 8.5: [Fragile].**  
  Because $63\%$–$81\%$ of model suitability is anchored to static topographic/edaphic layers that remain invariant between 2020 and 2070, a species warming out of its current thermal niche at lower elevations is prevented from migrating upslope into higher elevations if those elevations fall outside the static `Altitude` response curve fitted to current occurrences. Additionally, the manuscript never specifies which probability threshold (e.g., maximum training sensitivity plus specificity, 10th percentile training presence, or an arbitrary cutoff) was used to binarize continuous MaxEnt suitability into "Gain" and "Loss" percentages in Table 3, nor does it report the variance across the 16 pooled General Circulation Models (GCMs).

* **The MaxEnt ecological niche characterizations match prior autecological studies of *T. fedtschenkoi*: [Overstated].**  
  On line 198, the authors state that highly suitable habitats for *T. fedtschenkoi* are "distinguished by an elevation of 1400–3500 m," and immediately follow this in the next sentence by stating that autecology studies in Mazandaran province "revealed that the suitable distribution altitude range of the mentioned species was from sea level to 1400 m.a.s.l. Our findings are in line with the mentioned studies." An inferred range of $1,400$–$3,500\text{ m}$ is mutually exclusive with $0$–$1,400\text{ m}$, directly contradicting the claim of agreement.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Report Exact Occurrence Counts, Apply Spatial Thinning, and Restrict the Background Extent
* **WHY:** Without knowing whether each species was modeled with $N = 10$ or $N = 200$ points, readers cannot evaluate model degrees of freedom or overfitting, and unthinned herbarium records across a country-wide desert background inflate $\text{AUC}$.
* **WHAT:** Report total and post-filtering occurrence counts ($N$) for each species in Materials and Methods and Table 2, spatially thin occurrences to match the environmental grid resolution, and restrict background sampling to accessible montane ecoregions (or use a target-group bias file).
* **HOW:** Use the `spThin` package in R (e.g., thinning distance $\ge 5$–$10\text{ km}$) on the verified coordinates of each species, sample 10,000 background points within a $100\text{ km}$ buffer around known *Thymus* occurrences (Irano-Turanian and Hyrcanian montane zones), and report the mean $\pm$ SD of 10-fold cross-validation $\text{AUC}$ and True Skill Statistic ($\text{TSS}$).

#### 2. Remove Static Altitude from Climate-Change Projections and Standardize Collinearity Filtering
* **WHY:** Including static `Altitude` ($18.1\%$–$47.9\%$ contribution) in future climate projections prevents species from tracking shifting isotherms upslope and conflates topographic proxy effects with climate sensitivity. Moreover, Pearson collinearity among national environmental rasters is a property of the study area (or background), not of the MaxEnt output.
* **WHAT:** Compute the variance inflation factor (VIF $< 10$) and pairwise $|r| \le 0.70$ consistently prior to MaxEnt fitting, exclude `Altitude` from models projected under future climate scenarios (retaining `Slope` and `Ocr` as edaphic/geomorphological constraints), and compare projections with and without static topographic variables.
* **HOW:** Use `usdm::vifcor` in R on the stacked environmental rasters to select a non-collinear predictor set, refit MaxEnt using `dismo::maxent`, and report the explicit binarization threshold value (e.g., `equal_sens_spec` or `spec_sens` from `dismo::evaluate`) used to calculate Table 3 range changes.

#### 3. Archive Occurrence Coordinates and R Scripts
* **WHY:** The occurrence records compiled from Iranian herbaria (HSBU, IRAN, TARI) and field verifications are the primary empirical contribution of the study, yet they are unavailable to readers.
* **WHAT:** Provide a supplementary CSV table containing the decimal latitude, longitude, and species label for all verified records (or coarsened to $0.05^\circ$ if conservation-sensitive), along with the R `dismo` script.
* **HOW:** Upload the occurrence table and R modeling script as Supplementary Data files or deposit them in Zenodo/Figshare.

#### 4. Correct Specific Factual, Arithmetic, and Cross-Reference Errors
* **WHY:** Numerous errors in coordinates, units, table arithmetic, species spelling, and figure citations confuse readers and indicate insufficient proofreading.
* **WHAT & HOW:** Correct the following items across the manuscript:
  1. **Study Area Coordinates (line 33):** Change "between 44°–64°E latitude and 25°–40°N longitude" to "between 44°–63.5°E longitude and 25°–40°N latitude."
  2. **Table 1 Units (line 63):** Change the unit of `bio15` (Precipitation seasonality, coefficient of variation) from `mm` to `%` (dimensionless percentage).
  3. **Software Version (line 76):** Correct "MaxEnt version 1.0–3" to the actual MaxEnt Java version used (e.g., version 3.4.3 or 3.4.4).
  4. **Table 3 Arithmetic Error (line 170):** For *T. transcaucasicus* under RCP 8.5 in 2070, $\text{Gain} = 2.5\%$ and $\text{Loss} = 23.14\%$, which yields $\text{Change} = 2.50 - 23.14 = -20.64\%$ (or if $\text{Gain} = 2.05\%$, $-21.09\%$); fix the typo so $\text{Gain} - \text{Loss} = \text{Change}$.
  5. **Broken Figure and Table Cross-References (lines 94, 129, 140, 173, 187, 198–207):** Fix the mismatch where Figure 3 is described in the caption as maps of environmental variables (line 124) but cited in the text as 9 panels (`A`–`I`) of response curves (line 94) and as current habitat suitability maps for the three species (lines 129, 198–200, 207, which actually correspond to Figure 4A–C). Fix line 187, which cites `Table 3` instead of `Table 2` for variable contributions, and lines 140 and 173, which omit `Fig. 7` when citing future projection maps for all three species.
  6. **Taxonomic and Geographic Spelling:** Standardize spelling of *Thymus fedtschenkoi* (misspelled `T. fedschenkoi` in Table 2, Fig. 5, lines 140, 187, 191, 198), *Thymus pubescens* (misspelled `T. pubescense` in Fig. 7, lines 212, 217), and province names (`East Azerbaijan`, `Kurdistan`, `Mazandaran` on lines 17, 129).
