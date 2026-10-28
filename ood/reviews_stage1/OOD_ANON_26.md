# Review of OOD_ANON_26

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.0 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.9/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.2/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study uses Maximum Entropy (Maxent) ecological niche modeling to project current and future (2021–2100) climatic suitability across Europe for three medically important tick vectors: *Ixodes ricinus* ($n = 2,803$ thinned grid cells), *Dermacentor reticulatus* ($n = 866$), and *Dermacentor marginatus* ($n = 1,121$). Combining cleaned GBIF and literature records (1970–2020) with six low-collinearity WorldClim v2.0 bioclimatic predictors (`bio04`, `bio05`, `bio06`, `bio12`, `bio14`, `bio15` at 2.5 arc-minute resolution) and projections from the CNRM-ESM2-1 climate model across four SSP scenarios (SSP1-2.6, SSP2-4.5, SSP3-7.0, SSP5-8.5), the authors project substantial northeastward range expansions and broadened central European co-occurrence for all three species, driven primarily by winter minimum temperature (`bio06`).

The modeling workflow incorporates several sound methodological practices, including removing artefactual cross-variable bioclimatic layers (`bio08`, `bio09`, `bio18`, `bio19`), hierarchical correlation clustering ($1 - |r_P| > 0.3$), disabling hinge features to enforce smooth response curves, running Multivariate Environmental Similarity Surface (MESS) extrapolation checks, and providing a balanced discussion of non-climatic confounders (land cover, host density, microhabitat buffering). However, the study's quantitative projections are limited by (1) relying exclusively on a single global climate model (`CNRM-ESM2-1`) rather than a CMIP6 multi-model ensemble to capture inter-model climate uncertainty; (2) correcting spatial sampling bias only by 2.5 arc-minute grid-cell deduplication without background target-group weighting or spatial block cross-validation, which leaves Central European reporting bias unaddressed and understates *I. ricinus* suitability in Iberia and Eastern Europe; (3) leaving the explicit thermal-optimum hypotheses posed in the Introduction untested in the Results; and (4) not depositing the compiled occurrence dataset or R/Maxent scripts in an open repository. These limitations can be addressed through straightforward computational additions and data archiving.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **All three tick species are projected to expand their climatically suitable ranges toward northeastern Europe under SSP1-2.6 through SSP5-8.5, with net habitat gains exceeding Mediterranean losses: [Moderately Supported].**  
  The northeastward shift of thermal suitability under warming scenarios is biologically consistent with winter cold constraints on tick survival and development, and the MESS analysis (Figure S9) confirms minimal novel-climate extrapolation within Europe. However, all future projections depend on a single general circulation model (`CNRM-ESM2-1`). Because precipitation seasonality (`bio15`, contributing ~21% for *I. ricinus* and *D. reticulatus*) and summer extremes (`bio05`) vary substantially across CMIP6 models over continental Europe, single-GCM projections do not quantify inter-model variance.

* **Minimum temperature of the coldest month (`bio06`) is the primary climatic driver of European distribution limits across all three tick species: [Well Supported].**  
  The dominance of `bio06` in Maxent percent contribution across all three species aligns with established physiological cold-tolerance thresholds (e.g., lethal acute exposure below $-15^\circ\text{C}$ in *D. marginatus* vs. lower supercooling points in *I. ricinus* and *D. reticulatus*) and matches prior independent modeling studies.

* ***Ixodes ricinus* exhibits the broadest ecological niche, and *Dermacentor marginatus* possesses a temperature niche shifted toward a higher thermal optimum than *D. reticulatus*: [Fragile].**  
  Although the authors explicitly formulate these two hypotheses at the end of the Introduction (line 44), the Results section never presents marginal or univariate Maxent response curves for `bio05`/`bio06`, thermal optima, or formal niche-breadth metrics (such as Levins' $B$ or tolerance ranges) to test them. Instead, the comparison rests purely on visual inspection of geographic maps.

* **Reducing occurrence records to one point per 2.5 arc-minute cell accounts for sampling bias and reflects local abundances: [Overstated].**  
  In the Discussion (line 133), the authors state that "While our models use point distribution data (and thus also account for abundances), the ECDC data refer to species' presence or absence in the administrative areas." In a presence-background model like Maxent, retaining at most one record per $2.5\text{ arc-minute}$ ($\sim 4.5\text{ km}$) cell does not measure biological abundance; rather, dense clusters of occupied cells in countries with intensive acarological surveying (e.g., Germany) reflect regional sampling effort, which biases the fitted suitability surface toward Central European climates and causes the model to underpredict known *I. ricinus* presence in Portugal, Spain, and Eastern Europe (lines 131–133).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Incorporate Multi-GCM Ensemble Projections to Quantify Climate Model Uncertainty
* **WHY:** Relying on a single CMIP6 model (`CNRM-ESM2-1`) provides no measure of structural climate uncertainty, particularly for precipitation seasonality (`bio15`) and summer heat extremes (`bio05`).
* **WHAT:** Project the fitted Maxent models across an ensemble of at least 3–5 CMIP6 GCMs available on WorldClim v2.1 (e.g., adding `MPI-ESM1-2-HR`, `UKESM1-0-LL`, `EC-Earth3-Veg`, and `IPSL-CM6A-LR`) and report the ensemble mean and inter-GCM standard deviation of suitable area ($\text{km}^2$) in Figure 4 and Table S2.
* **HOW:** Download the corresponding 2.5 arc-minute WorldClim CMIP6 rasters for the additional GCMs, batch-project the 10 replicate Maxent models onto each GCM, apply the 10% training omission threshold, and plot error bars showing inter-GCM range across each SSP in Figure 4.

#### 2. Control for Country-Level Sampling Bias and Evaluate with Spatially Blocked Cross-Validation
* **WHY:** Random 10-fold cross-validation on spatially clustered European tick records yields overly optimistic AUC values with artificially tiny standard deviations ($\text{SD} = 0.0006–0.0011$, lines 87–99) because training and test points fall within the same heavily sampled regions. Moreover, uneven national reporting intensity in GBIF/literature data pulls the background ratio toward Central Europe.
* **WHAT:** (1) Apply a larger spatial thinning distance (e.g., 20–30 km via `spThin`) or include a spatial sampling bias grid (e.g., kernel density of all European tick/arthropod GBIF records) as a Maxent `biasfile`. (2) Report spatially blocked cross-validation AUC and omission rates (using `blockCV` or `ENMeval` checkerboard/lat-lon blocks).
* **HOW:** Generate a Gaussian kernel density raster from the combined occurrence points of all three species (or all Ixodidae in GBIF Europe), pass it to Maxent via the `biasfile` argument, and compare the resulting suitability predictions in under-sampled regions (Iberia, Balkans, Scandinavia) against ECDC administrative presence maps.

#### 3. Formally Test the Thermal Niche and Niche Breadth Hypotheses Stated in the Introduction
* **WHY:** The Introduction (line 44) explicitly hypothesizes that *I. ricinus* has the broadest niche and that *D. marginatus* has a higher thermal optimum than *D. reticulatus*, but no quantitative niche breadth or response-curve analysis is reported.
* **WHAT:** Add a figure or table comparing the marginal Maxent response curves for `bio06` and `bio05` (showing optimal temperature ranges where logistic suitability $> 0.5$) and compute Levin's niche breadth ($B_2$) in `ENMTools` for all three species.
* **HOW:** Extract the marginal response curves (`species_bio06.dat` and `species_bio05.dat`) from the Maxent output folders, plot all three species on a shared temperature axis with 10-replicate confidence bands, and report the temperature optimum and Levins' $B$ statistic in the Results.

#### 4. Correct the Abundance Claim and Archive Cleaned Occurrence Data and Scripts
* **WHY:** Presence-only records thinned to 1 point per 2.5 arc-minute grid cell do not measure local population abundance (line 133), and the manuscript lacks a Data Availability Statement or repository link for the cleaned coordinate tables (2,803 + 866 + 1,121 points) and R/Maxent scripts.
* **WHAT & HOW:** Revise line 133 to state that higher spatial density of occupied grid cells reflects finer-scale spatial prevalence (and regional sampling intensity) rather than local tick abundance. Deposit the cleaned, thinned occurrence coordinates (CSV) and R workflow scripts on Zenodo or Figshare and add the DOI to the Declarations section.
