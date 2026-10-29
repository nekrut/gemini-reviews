# Forensic Peer Review: FEXP_ANON_114

**Overall Score:** **4.5 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **3.3 / 8.0**  
* **Score Breakdown:** Rigor: 1.1/3.5 | Claims: 1.1/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.2/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_114`
* **Perceived Domain & Topic:** Ecological Niche Modeling / Freshwater Conservation Biogeography; Ensemble Species Distribution Modeling (ESDM) of 11 freshwater mussel species (Unionidae and Mycetopodidae) in the Pánuco River Basin (PRB), México.
* **Perceived Empirical Scope:** 621 total records across 87 survey sites for 15 species, filtered to 11 focal species with $N = 10\text{–}43$ unique spatial occurrences per species; 10 terrestrial/climatic raster covariates at 30 arc-second (~0.9 km) resolution; 9 modeling algorithms in the R `sdm` package evaluated via 100 bootstrap 80%/20% splits with $2N$ random pseudo-absences.

---

## 2. Executive Summary & Editorial Verdict

This study compiles museum and recent (2017–2018) field survey records for freshwater mussels in the Pánuco River Basin (PRB), Central México, and fits ensemble species distribution models (ESDMs) across 9 algorithms (GLM, SVM, RF, BRT, MARS, MAXENT, CART, FDA, MDA) for 11 species with $\ge 10$ unique occurrence locations. Using 7 WorldClim variables, elevation, slope change, and land cover at 30 arc-second resolution, the authors report ensemble $\text{AUC} = 0.851\text{–}0.953$ and $\text{TSS} = 0.867\text{–}0.960$, conclude that elevation, warmest-quarter precipitation (BIO18), and driest-quarter temperature (BIO9) govern mussel occurrence while land cover is uninformative, and stack binary species maps to identify richness hotspots. Occurrence data are deposited in Dryad and MUSSELp.

**Editorial Verdict: Major Revision / Re-analysis Required (4.5 / 10.0).** While the underlying dataset of freshwater mussel occurrences in an understudied Mexican river basin is a valuable natural-history contribution, the statistical modeling and validation pipeline contains fundamental methodological flaws and mathematical impossibilities:
1. **Mathematically impossible True Skill Statistic (TSS) values in Table 3:** By definition, $\text{TSS} = \text{Sensitivity} + \text{Specificity} - 1$. In Table 3, for every single one of the 11 species, the reported `TSS` ($0.867\text{–}0.960$) violates this identity by $+0.06$ to $+0.18$ (e.g., *Disconaias disca* has $\text{Sensitivity} = 0.843$ and $\text{Specificity} = 0.844$, which yields $\text{TSS} = 0.687$, yet Table 3 reports $\text{TSS} = 0.867$). Furthermore, the fifth column promised in the Table 3 caption ("weighted average optimal threshold values") is omitted.
2. **Terrestrial pseudo-absence sampling and severe overparameterization ($p = 10$ covariates on $N_{\text{train}} = 8$ presences):** For obligate aquatic mussels restricted to stream channels, pseudo-absences were generated at $2N$ randomly across the entire $98,227\text{ km}^2$ terrestrial PRB polygon rather than along the hydrographic network. With only $N = 10\text{–}15$ unique presences for 5 of the 11 species (leaving 8 training presences and 2 test presences per 80/20 split), fitting 10 predictors across 9 machine-learning algorithms merely separates lowland river valleys from upland terrestrial mountains—explaining why terrestrial elevation dominates every species model and why the unclipped SDM predicts freshwater mussels inhabiting dry land (Figure 3a), requiring an ad-hoc 2 km stream buffer clip (Figure 3b).
3. **Biased richness stacking under fixed 1:2 prevalence:** Generating $2N$ pseudo-absences fixes modeled prevalence at $1/3$ for every species regardless of whether it occurs at 10 sites or 43 sites, and stacking binary thresholded maps without prevalence calibration systematically inflates predicted local species richness.

### Assessment of Specific Claims

* **Claim 1 (Single and ensemble SDMs achieve excellent predictive accuracy [$\text{AUC} > 0.85$, $\text{TSS} > 0.86$] for freshwater mussels with as few as 10 occurrence records): `[Methodologically Flawed]`.**  
  First, the ensemble TSS values in Table 3 violate $\text{TSS} = \text{Sensitivity} + \text{Specificity} - 1$ for all 11 species. Second, evaluating models on 2 test presences and 4 random terrestrial pseudo-absences while fitting 10 environmental variables inflates AUC/TSS because random terrestrial background points lie in non-riverine upland habitats; moreover, non-independent bootstrap resampling of 87 clustered stream sites leaks spatial autocorrelation between training and test splits.
* **Claim 2 (Elevation, precipitation of the warmest quarter [BIO18], and mean temperature of the driest quarter [BIO9] are the primary drivers of mussel occurrence, whereas land use has minimal influence): `[Fragile]`.**  
  Because pseudo-absences were drawn across the entire terrestrial basin rather than within stream reaches, `Elevation` simply acts as a proxy for lowland river channels versus the Sierra Madre Oriental and Central Plateau. Similarly, 30 arc-second local pixel land cover fails to capture upstream catchment agricultural runoff because covariates were extracted at pixel level rather than routed across upstream sub-catchments (e.g., HydroSHEDS).
* **Claim 3 (Stacked binary ensemble maps identify unsampled tributaries near Loma Alta and La Isla de Ocampo as high-priority biodiversity hotspots harboring $>8$ species): `[Overstated]`.**  
  Fixing pseudo-absences at $2N$ forces equal prior prevalence ($33.3\%$) for rare ($N=10$) and widespread ($N=43$) species, and summing binary thresholded maps (`0/1`) rather than continuous habitat suitability probabilities is known to overestimate local richness ($\alpha$-diversity).

---

## 3. Forensic Defect Inventory

### Defect 1: Mathematical Violation of the True Skill Statistic Identity in Table 3 [ Pillar 3, Pillar 4, Pillar 7 — Critical ]
* **Location:** Results (line 110) and Table 3 (lines 113–126).
* **Forensic Evidence:**
  The True Skill Statistic is strictly defined as $\text{TSS} = \text{Sensitivity} + \text{Specificity} - 1$ (Allouche et al. 2006). Across all 11 species in Table 3, the reported TSS is incompatible with the reported Sensitivity and Specificity:
  - *Actinonaias coyensis*: $\text{Sens} = 0.932$, $\text{Spec} = 0.933 \implies \text{Sens} + \text{Spec} - 1 = 0.865$ (Reported $\text{TSS} = 0.939$, error $+0.074$).
  - *Actinonaias medellina*: $\text{Sens} = 0.924$, $\text{Spec} = 0.932 \implies \text{Sens} + \text{Spec} - 1 = 0.856$ (Reported $\text{TSS} = 0.938$, error $+0.082$).
  - *Actinonaias signata*: $\text{Sens} = 0.927$, $\text{Spec} = 0.926 \implies \text{Sens} + \text{Spec} - 1 = 0.853$ (Reported $\text{TSS} = 0.932$, error $+0.079$).
  - *Disconaias disca*: $\text{Sens} = 0.843$, $\text{Spec} = 0.844 \implies \text{Sens} + \text{Spec} - 1 = 0.687$ (Reported $\text{TSS} = 0.867$, error $+0.180$; note also that in line 91 the individual-model mean TSS for *D. disca* is reported as $0.700 \pm 0.08$, which matches $0.687$ rather than $0.867$).
  - *Cyrtonaias tampicoensis*: $\text{Sens} = 0.886$, $\text{Spec} = 0.886 \implies \text{Sens} + \text{Spec} - 1 = 0.772$ (Reported $\text{TSS} = 0.895$, error $+0.123$).
  - *Nephronaias aztecorum*: $\text{Sens} = 0.879$, $\text{Spec} = 0.876 \implies \text{Sens} + \text{Spec} - 1 = 0.755$ (Reported $\text{TSS} = 0.900$, error $+0.145$).
  In addition, the Table 3 caption states that it reports *"AUC, TSS, sensitivity and specificity, and weighted average optimal threshold values"*, but only four numeric columns are present.
* **Fix:** Re-extract the exact evaluation metrics from the R `sdm` object (`getEvaluation()`), verify that $\text{TSS} = \text{Sensitivity} + \text{Specificity} - 1$ at the selected threshold for every species, and include the missing optimal threshold (OT) column in Table 3.

### Defect 2: Terrestrial Pseudo-Absence Sampling for Obligate Lotic Taxa and Extreme Small-Sample Overparameterization [ Pillar 2, Pillar 3, Pillar 5 — Critical ]
* **Location:** Methods (lines 75–82) and Figure 3 (line 145).
* **Forensic Evidence:**
  1. **Terrestrial background domain:** All 87 survey sites lie within river channels, but pseudo-absences were generated *"randomly ... within the extent of the PRB"* ($98,227\text{ km}^2$ terrestrial basin; line 80). Because >95% of random points in a terrestrial basin fall on non-riverine hillslopes and plateaus, the binary classifiers primarily learn to distinguish low-elevation river valleys from upland terrain. This is confirmed by Figure 3a, where predicted mussel "hotspots" cover large terrestrial areas away from rivers, forcing the authors to apply a post-hoc 2 km buffer around major streams in Figure 3b.
  2. **Events-per-variable violation ($N_{\text{train}} = 8$ presences vs. $p = 10$ predictors):** Three modeled species have $N = 10$ unique occurrences (*A. medellina*, *P. semirasa*, *A. cylindracea*), one has $N = 13$ (*N. aztecorum*), and one has $N = 15$ (*D. disca*). With $2N$ pseudo-absences and an 80%/20% split, models for $N = 10$ species are trained on **8 presences and 16 pseudo-absences** using **10 predictors** (0.8 presences per predictor) and evaluated on just **2 test presences and 4 test pseudo-absences**.
  3. **Target-group absence information ignored:** The authors surveyed 87 unique stream sites across the basin (line 32). When modeling a species recorded at 20 of the 87 surveyed mussel sites, the remaining 67 surveyed mussel sites provide direct target-group absence (or non-detection) records within the exact same lotic sampling frame, yet the authors discarded these 67 surveyed stream sites in favor of $2N$ random terrestrial points.
* **Fix:** Restrict the modeling domain and background/pseudo-absence sampling strictly to the hydrographic network (e.g., stream reaches using HydroSHEDS / RiverATLAS covariates with upstream catchment aggregation), or use the 87 surveyed mussel sites as a target-group background/absence pool. Reduce the predictor set to $\le 2\text{–}3$ orthogonal stream-reach variables for species with $N < 20$.

### Defect 3: Binary Stacking Under Artificial 1:2 Prevalence Distortion [ Pillar 3, Pillar 4 — Major ]
* **Location:** Methods (lines 80, 84) and Results (line 142).
* **Forensic Evidence:**
  By generating exactly $2N$ pseudo-absences for every species regardless of $N$, the sample prevalence in every model is artificially fixed at $N / (N + 2N) = 0.333$. Consequently, a rare species observed at only 10 sites (*A. medellina*) and a widespread species observed at 43 sites (*F. iridella*) are modeled with identical prior prevalence, and thresholding via maximum $(\text{Sensitivity} + \text{Specificity})$ produces comparably wide binary range maps for rare and common species alike. Summing these binary maps (`0/1`) rather than summing calibrated occurrence probabilities systematically inflates predicted species richness.
* **Fix:** Use a common target-group background (or fixed number of stream-network background points across all species) so empirical prevalence differences are preserved, and compute stacked species richness by summing calibrated probability surfaces ($\sum_i \hat{p}_{i,x}$) alongside thresholded maps.

### Defect 4: Truncated Tables, Missing Species Rows, and Predictor Name Inconsistencies [ Pillar 7 — Moderate ]
* **Location:** Abstract (line 5), Methods (lines 32, 75), Results (line 89), and Tables 1, 2, and 4.
* **Forensic Evidence:**
  1. **Missing species row in Table 1 and sample-size discrepancy:** Table 1 lists 14 species whose total observations sum to $610$, omitting the data row for the 15th species (*Anodontites cylindracea*, which has 11 total observations and 10 unique spatial observations to reach the reported 621 total). Furthermore, Abstract (line 5) and Results (line 89) state that *"A total of 11 species with 621 species-specific observations at 87 unique sites were used in our ensemble modeling after removing species with small sample sizes (i.e., n <= 10)"*, whereas 621 is the total *before* removing the 4 excluded species (which account for 15 unique / 25 total observations, leaving 596 observations across the 11 modeled species), and the exclusion rule was $n < 10$ (since three species with $n = 10$ were retained).
  2. **Truncated Tables 2 and 4:** Tables 2 and 4 present results for only 3 species (*Actinonaias coyensis*, *A. medellina*, *A. signata*), omitting the other 8 modeled species without explanation.
  3. **Covariate mismatch between Methods and Table 4:** Methods (line 75) lists `BIO3 = Isothermality` among the 10 retained predictors and excludes `BIO4 = Temperature seasonality`, but Table 4 (line 133) reports `Temp seasonality` instead of `Isothermality`.
  4. **Taxonomic/editorial typos:** Table 1 (line 58) misspells *Cyrtonaias* as `Crytonaias`; Results (line 89) abbreviates *Popenaias semirasa* as `Popenaias s.`.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.1** | **3.5** | Ensemble TSS values in Table 3 violate $\text{TSS} = \text{Sens} + \text{Spec} - 1$ for all 11 species; fitting 10 predictors across 9 algorithms on $N=10\text{–}15$ points with $2N$ terrestrial pseudo-absences severely overfits and confounds stream channel location with ecological niche. |
| **2. Claim-to-Evidence Alignment** | **1.1** | **2.5** | Claims of "excellent model fit" ($\text{AUC} > 0.9$, $\text{TSS} > 0.86$) for $N=10$ species and unimportance of land cover are artifacts of terrestrial pseudo-absence sampling and pixel-level (rather than upstream catchment) land-use extraction. |
| **3. Data Integrity & Biological Plausibility** | **1.1** | **2.0** | Useful primary compilation of 621 mussel records across 87 sites in an understudied drainage, but modeling obligate lotic bivalves across terrestrial grids without hydrographic network conditioning is biologically misspecified. |
| **4. Reproducibility & Data Integrity** | **1.2** | **2.0** | Raw occurrence data are publicly archived on Dryad (`10.5061/dryad.18931zczf`), but Tables 1, 2, 3, and 4 have omitted species/columns, arithmetic errors, and covariate label mismatches, and no R modeling scripts are provided. |
| **Total Composite Score** | **4.5** | **10.0** | **Flawed / Overstated** (Scientific Core Score: **3.3 / 8.0**) |
