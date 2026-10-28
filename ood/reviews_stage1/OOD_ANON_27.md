# Review of OOD_ANON_27

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.7 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.3/3.5 | Claims: 1.2/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study models the current (2010–2020) and projected future (2050–2060 and 2090–2100 under SSP1-2.6, SSP3-7.0, and SSP5-8.5) habitat distributions of three commercially harvested East Asian marine fishes—the benthic sciaenid *Collichthys lucidus* ($n = 92$), and the pelagic clupeids *Konosirus punctatus* ($n = 355$) and *Clupanodon thrissa* ($n = 19$)—using GBIF/OBIS occurrence records and Bio-ORACLE v2/v3 marine layers. Combining `kuenm` Maxent tuning with a five-algorithm ensemble (Maxent, GLM, RF, BRT, SVM) in the `sdm` R package and overlaying World Database on Protected Areas (WDPA) polygons, the authors report future range contraction for *C. lucidus* (up to 18% loss), large range expansions for *K. punctatus* (up to 69% gain) and *C. thrissa* (up to 230% gain), and low MPA coverage (2%–7% of total range).

Although regional climate risk assessments for East Asian coastal fisheries are needed, the manuscript suffers from major methodological flaws, severe small-sample overfitting, and glaring internal inconsistencies between its figures, tables, and text: (1) *Clupanodon thrissa* is modeled with only $n = 19$ total occurrence points (~13 training points per 70/30 split) across 5 machine learning algorithms including Random Forest, BRT, and SVM, producing an overfitted ensemble ($\text{AUC} = 0.960, \text{TSS} = 0.920$) within an artificially truncated calibration area; (2) the environmental variables reported in the Abstract and Results Section 3.2 (`Chl`, `Mlotst`, `PO4`, `Si`) do not match the variables defined in the Figure 2 caption (`O2`, `so`, `phyc`, `terr_char`, `sws`, `dfe`, `thetao`, `swd`), which also contains unedited speculative draft notes (`"(likely sea surface temperature or bottom temperature variable used in SDMs)"`) and misidentifies Bio-ORACLE's dissolved iron code (`dfe`) as `"Sea floor depth/current (bathymetry-related)"`; (3) the spatial `blockCV` and `kuenm` calibration described in the first paragraph of Section 2.3 is abandoned in the second paragraph in favor of random 70/30 bootstrap splits in the `sdm` package; and (4) the continuous suitability area changes in Table 2 contradict the binary range expansion/contraction areas in Table 3 because scenario-specific thresholds were applied instead of a fixed historical threshold. Re-running the models with consistent predictor sets, a single fixed binary threshold per species, and appropriate sample size/complexity constraints for *C. thrissa* is necessary before the projections can be trusted.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Dissolved oxygen and salinity drive the distribution of *C. lucidus*, whereas chlorophyll/mixed-layer depth and phosphate/silicate drive *K. punctatus* and *C. thrissa*: [Methodologically Flawed].**  
  There is a direct contradiction between the main text (Abstract line 16; Section 3.2 line 120; Discussion line 246) and Figure 2 (line 58). While Section 3.2 states that chlorophyll-a (`Chl`) and mixed layer depth (`Mlotst`) were the strongest predictors for *K. punctatus* and phosphate (`PO4`) and silicate (`Si`) were the strongest for *C. thrissa*, the Figure 2 caption lists a completely different set of variables (`O2`, `so`, `phyc`, `terr_char`, `sws`, `dfe`, `thetao`, `swd`) and includes unedited placeholder commentary guessing what its own variable codes mean: `terr_char = Temperature at certain depth/climatological habitat range (likely sea surface temperature or bottom temperature variable used in SDMs); dfe = Sea floor depth/current (bathymetry-related)`. In Bio-ORACLE, `dfe` is dissolved iron concentration ($\mu\text{mol/m}^3$), not seafloor depth or current.

* ***Clupanodon thrissa* is accurately modeled ($\text{AUC} = 0.960, \text{TSS} = 0.920$) and will experience up to a 230% range expansion under climate change: [Methodologically Flawed].**  
  Only $n = 19$ occurrence records were obtained for *C. thrissa* (Table 1), despite *C. thrissa* being a common, heavily harvested coastal clupeid distributed from Vietnam to Korea/Japan. Fitting five complex non-parametric and parametric algorithms (RF, BRT, SVM, Maxent, GLM) with 5 predictors on 70% of 19 points ($n \approx 13$ presence points vs. 700 pseudo-absences per bootstrap) severely overfits the sparse sample. Worse, because the calibration area was restricted to MEOW polygons containing at least one occurrence record (line 52), missing GBIF records in adjacent ecoregions caused the entire Yellow Sea and Sea of Japan to be excluded from *C. thrissa*'s calibration region (total area $1.76\times 10^6\text{ km}^2$ vs. $4.65\times 10^6\text{ km}^2$ for *K. punctatus*; Table 2). Furthermore, in Table 2, *C. thrissa*'s combined Highly + Medium Suitable area in 2090–2100 under SSP3-7.0 ($328,370\text{ km}^2$) and SSP5-8.5 ($293,964\text{ km}^2$) is *smaller* than under Current conditions ($342,862\text{ km}^2$), directly contradicting Table 3's claim of $+37\%$ and $+54\%$ net range expansion in those exact same scenarios.

* ***Collichthys lucidus* will suffer consistent habitat contraction across future scenarios (including a 14% loss vs. 4% gain under SSP1-2.6 in 2050–2060): [Fragile].**  
  Table 2 and Table 3 contradict each other for *C. lucidus* under SSP1-2.6: in Table 2, Highly Suitable habitat increases by $+30.8\%$ under SSP1-2.6 in both 2050–2060 ($92,393 \to 120,840\text{ km}^2$) and 2090–2100 ($120,390\text{ km}^2$), and total Highly + Medium Suitable area remains constant ($403,400 \to 404,064\text{ km}^2$). Yet Table 3 reports a $42,659\text{ km}^2$ ($14\%$) range contraction vs. $12,069\text{ km}^2$ ($4\%$) expansion for SSP1-2.6 in 2050–2060. This discrepancy arises because Section 2.3 (Table 2) used scenario-specific Jenks natural breaks in ArcMap, whereas Section 2.4 (Table 3) binarized each future raster "using the threshold value for each climate scenario" rather than holding the historical baseline threshold fixed.

* **Existing Marine Protected Areas (MPAs) cover only 2%–7% of the total distributional ranges (and 18%–39% of highly suitable coastal habitats) of the three species: [Moderately Supported].**  
  The spatial overlay with WDPA and Chinese National Aquatic Genetic Resources Protection Areas (Table 4) clearly demonstrates that East Asian coastal MPAs cover a small fraction of continental shelf waters, though the exact percentages depend on the arbitrary Jenks natural-breaks classification of continuous suitability rasters.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile the Environmental Predictor Variables Between Figure 2, Section 3.2, and Tables S1–S2
* **WHY:** A manuscript cannot report one set of top predictors (`Chl`, `Mlotst`, `PO4`, `Si`) in the Abstract, Results, and Discussion while plotting and defining a completely different set (`phyc`, `terr_char`, `sws`, `dfe`, `thetao`, `swd`) with speculative placeholder text in Figure 2.
* **WHAT:** Audit the exact R script used to run `usdm::vifstep` and `sdm::getVarImp`, replace either Figure 2 or Section 3.2 so both reflect the actual fitted models, and remove the draft commentary from the Figure 2 caption.
* **HOW:** Export the exact variable importance table from `sdm::getVarImp(ensemble_model)`, verify the official Bio-ORACLE variable names and units (e.g., `o2`, `so`, `chl`, `phyc`, `mlotst`, `po4`, `si`, `thetao`, and bathymetry from GEBCO/Bio-ORACLE terrain layers), and regenerate Figure 2 with accurate labels.

#### 2. Fix the Thresholding Methodology Comparing Present and Future Range Sizes (Tables 2 and 3)
* **WHY:** Applying Jenks natural breaks independently to each future scenario raster (Section 2.3, line 69) or applying scenario-specific binary thresholds (Section 2.4, line 74) shifts the suitability cutoff in every time period, creating artificial expansions or contractions even when raw predicted suitability declines.
* **WHAT:** Use a single, time-invariant binary threshold (e.g., Maximum Training Sensitivity plus Specificity [MTSS/maxSSS] estimated on the **current** baseline model) for each species to binarize both current and all future projections in `biomod2::BIOMOD_RangeSize`, and use fixed suitability intervals (e.g., $<$ threshold = Unsuitable/Low, threshold–$0.6$ = Medium, $>0.6$ = High) in Table 2.
* **HOW:** Extract the baseline maxSSS threshold $T_0$ for each species under current conditions, classify all present and future rasters using $T_0$, and recompute Tables 2, 3, and 4 so that the area of `Highly + Medium Suitable` in Table 2 equals `Stable + Range Contraction` (at present) and `Stable + Range Expansion` (in the future) in Table 3.

#### 3. Unify the Cross-Validation and Model Calibration Pipeline (`kuenm` + `blockCV` vs. `sdm`) and Address Small Sample Size in *C. thrissa*
* **WHY:** In Section 2.3, the authors tune Maxent using 5 spatial blocks (`blockCV`) in `kuenm`, but then switch to 10 random 70/30 bootstrap splits in `sdm` across five algorithms without spatial blocking, and for *K. punctatus* they average the regularization multiplier numbers (`RM = 6` and `RM = 8` $\to$ `RM = 7`) rather than averaging model predictions. For *C. thrissa* ($n = 19$), fitting 5 algorithms on ~13 training points is severely overparameterized.
* **WHAT:** (1) Augment *C. thrissa* occurrence records using regional fisheries survey literature and FishBase/National Specimen datasets (or restrict *C. thrissa* to simple, strongly regularized models—Maxent with L/Q features and GLM—using leave-one-out/jackknife cross-validation and an ecologically realistic calibration area covering the Yellow, East China, and South China Seas). (2) Pass the spatially blocked folds from `blockCV` directly into the `sdm` evaluation rather than reverting to random 70/30 bootstrap splits.
* **HOW:** In R, pass the `blockCV` fold indices into `sdmData` or evaluate the ensemble on the held-out spatial blocks. In Section 3.1, fix the transposed counts of feature classes (31) and regularization multipliers (17) on line 99, and correct the cross-references on line 99 from `Table S2` to `Table S4`.

#### 4. Correct Species Spelling, Figure Cross-References, and Data Archiving
* **WHY:** Multiple editorial and cross-reference errors reduce clarity, and the cleaned occurrence coordinates ($92 + 355 + 19$ points) are not provided in the supplementary files.
* **WHAT & HOW:**
  1. Correct the misspelling of *Clupanodon thrissa* (printed as `Clupanodun thrissa` in the captions of Figures 2, 3, and 4, lines 58, 80, and 86).
  2. On line 211, change `Figure 3 c` to `Figure 3 b` for *K. punctatus*.
  3. Include a supplementary CSV table containing the cleaned, thinned latitude/longitude coordinates for all three species so the SDM workflow is reproducible.
