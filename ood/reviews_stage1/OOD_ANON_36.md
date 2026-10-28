# Review of OOD_ANON_36

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.0 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.1/3.5 | Claims: 1.1/2.5 | Biology: 1.0/2.0 | Reproducibility: 0.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study compiles 560 occurrence records (175 field sign and camera-trap records from 2021–2023 and 385 literature records, spatially thinned to 159 points at $1\text{ km}^2$ resolution) for the Endangered Indian pangolin (*Manis crassicaudata*) across northern Pakistan and Azad Jammu and Kashmir (AJ&K). Using MaxEnt (v.3.4.1) and four WorldClim variables (`bio1`, `bio4`, `bio12`, `bio15`) projected under a single general circulation model (`HadGEM3-GC31-LL`) across three SSPs (SSP126, SSP245, SSP585) and three future periods (2041–2060, 2061–2080, 2081–2100), the authors estimate current habitat suitability and future range loss, gain, and stability. Neither the thinned occurrence coordinates/rasters nor the analysis scripts are deposited in a public repository.

While the field survey effort across northern Pakistan and AJ&K provides useful occurrence data for an endangered mammal, the quantitative habitat change projections in Tables 1 and 2 contain fundamental mathematical contradictions, and the SDM design is confounded by unmodeled elevational sampling bias. Specifically, in Table 2, the sum of `Stable` and `Loss`—which must identically equal the baseline current suitable habitat area across every future scenario—varies between $42,742\text{ km}^2$ and $60,370\text{ km}^2$ across columns, and none of these totals match the current suitable habitat areas reported in Table 1 ($19,688\text{ km}^2$ for highly + moderately suitable, or $69,534\text{ km}^2$ including less suitable). Similarly, in Table 1, the total area of the study region jumps from $\sim 337,889\text{ km}^2$ to $406,071\text{ km}^2$ in a single row (`2041–2060 SSP245`). Finally, field surveys were truncated at $< 2,000\text{ m}$ elevation in only accessible plots (line 153), whereas MaxEnt background points were sampled across the full northern Pakistan domain (reaching $5,846\text{ m}$ and $-14^\circ\text{C}$), confounding survey accessibility with climatic niche limits. Re-running the GIS raster algebra and incorporating a target-group/elevation sampling bias file are required to salvage the quantitative projections.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Suitable habitat loss for Indian pangolin is greatest (26.97% under SSP585 and 23.67% under SSP126) during 2061–2080, while 64.60–83.85% of habitat remains stable (Table 2): [Methodologically Flawed].**  
  By conservation of area, any grid cell that is currently suitable must either remain suitable (`Stable`) or become unsuitable (`Loss`) in a future period; thus, $\text{Area}(\text{Stable}) + \text{Area}(\text{Loss}) \equiv \text{Area}(\text{Current Suitable})$ must be invariant across all nine future columns of Table 2. Instead, $\text{Stable} + \text{Loss}$ in Table 2 equals $49,378\text{ km}^2$ (2041–2060 SSP126), $44,343\text{ km}^2$ (2041–2060 SSP585), $60,370\text{ km}^2$ (2061–2080 SSP126), $52,221\text{ km}^2$ (2061–2080 SSP585), and $42,742\text{ km}^2$ (2081–2100 SSP585). Furthermore, none of these values match the current suitable area in Table 1 ($7,270 + 12,418 = 19,688\text{ km}^2$ for probability $> 0.4$, or $69,534\text{ km}^2$ for probability $> 0.1$), and the percentages in Table 2 were computed by dividing by $(\text{Stable} + \text{Gain} + \text{Loss})$ rather than by baseline current suitable area.

* **Current highly, moderately, less, and unsuitable habitat areas across time periods and SSPs (Table 1): [Methodologically Flawed].**  
  In Table 1, summing the four mutually exclusive habitat classes yields a consistent total study area of $336,975\text{--}337,889\text{ km}^2$ across eight of the ten rows, but in the `2041–2060 SSP 245` row (line 53), the areas sum to $7,222 + 16,189 + 53,729 + 328,931 = 406,071\text{ km}^2$ (an impossible $+68,182\text{ km}^2$ expansion of the geographic boundary of northern Pakistan, likely caused by reporting raw pixel counts instead of projected $\text{km}^2$). In addition, the "Study area" section (line 145) describes only AJ&K ($13,297\text{ km}^2$), omitting the remaining $\sim 324,592\text{ km}^2$ of northern Pakistan (KPK, Punjab, Gilgit-Baltistan) included in the rasters.

* **Annual mean temperature (`bio1`, 33.4%) and annual precipitation (`bio12`, 29.3%) are the primary drivers of Indian pangolin distribution, with high model accuracy ($\text{AUC} = 0.885, \text{TSS} = 0.695$): [Fragile].**  
  Field surveys were explicitly restricted to elevations $< 2,000\text{ m}$ and accessible plots (line 153), whereas background points ($n = 10,000$) were drawn uniformly across the entire northern Pakistan extent (up to $5,846\text{ m}$, where high-altitude glaciers and alpine zones have `bio1` down to $-14^\circ\text{C}$). Without a sampling-effort bias grid or restricting background selection to the surveyed $< 2,000\text{ m}$ elevational buffer, `bio1` acts as a proxy for the $2,000\text{ m}$ survey boundary, artificially inflating AUC and TSS. In addition, the response curve description for `bio4` (line 69: suitability decreases from $1$ to $0.48$, then increases to $0.96$ above $1050$) indicates unregularized hinge/threshold overfitting at the edge of the environmental domain.

* **Future range projections based solely on `HadGEM3-GC31-LL` and bioclimatic variables provide a reliable basis for designating new protected areas: [Overstated].**  
  `HadGEM3-GC31-LL` has a notably high equilibrium climate sensitivity compared to the CMIP6 ensemble median; projecting species distributions from a single GCM without multi-model ensemble averaging understates climate projection uncertainty. Moreover, key proximal determinants of pangolin occupancy acknowledged in the Introduction—soil/burrow substrate, canopy cover, land cover, and human settlement/poaching pressure (lines 21–25)—were excluded from the model.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Re-Run GIS Raster Change Detection and Fix Area/Percentage Calculations in Tables 1 and 2
* **WHY:** In Table 1 (`2041–2060 SSP245`), total study area is $406,071\text{ km}^2$ instead of $\sim 337,889\text{ km}^2$, and in Table 2, $\text{Stable} + \text{Loss}$ fails to equal the baseline current suitable habitat area across scenarios.
* **WHAT:** Reproject all current and future binary suitability rasters into an equal-area projection (e.g., UTM Zone 43N or Asia North Albers Equal Area Conic), explicitly define the binary suitability threshold used for Table 2 (e.g., logistic probability $> 0.4$ or maximum training sensitivity plus specificity), and recompute `Stable`, `Loss`, and `Gain`.
* **HOW:** In ArcGIS or R (`terra`), define binary suitability $B_t = \mathbb{I}(P_t \ge \tau)$ using a single fixed threshold $\tau$. For each future scenario $t$, compute $\text{Stable} = \sum \mathbb{I}(B_0 = 1 \land B_t = 1)$, $\text{Loss} = \sum \mathbb{I}(B_0 = 1 \land B_t = 0)$, and $\text{Gain} = \sum \mathbb{I}(B_0 = 0 \land B_t = 1)$. Verify that $\text{Stable} + \text{Loss} \equiv \sum \mathbb{I}(B_0 = 1)$ in every column of Table 2, and express `% Loss`, `% Stable`, and `% Gain` relative to baseline suitable area $\sum \mathbb{I}(B_0 = 1)$.

#### 2. Control for Elevational and Accessibility Survey Bias in MaxEnt Background Selection
* **WHY:** Restricting field surveys to accessible sites $< 2,000\text{ m}$ while drawing random background points up to $5,846\text{ m}$ confounds survey effort with thermal niche limits (`bio1`).
* **WHAT:** Restrict background point sampling using a target-group/accessibility bias layer or a $2,000\text{ m}$ elevation + buffer mask, and use spatially blocked cross-validation rather than random 10-fold replication.
* **HOW:** Using `ENMeval` in R, generate a kernel density bias raster from the surveyed $10 \times 10\text{ km}$ grid cells and literature localities, draw 10,000 bias-weighted background points, tune the regularization multiplier ($0.5\text{--}3.0$) and feature classes using $\Delta\text{AICc}$ under spatial block partitioning, and report which regularization multiplier was selected (currently omitted in line 163).

#### 3. Incorporate Topographic/Anthropogenic Predictors and Multi-GCM Ensemble Uncertainty
* **WHY:** Pangolin burrow construction and survival depend on slope, land cover, and poaching proximity, and single-GCM projections (`HadGEM3-GC31-LL`) are vulnerable to GCM-specific warming bias.
* **WHAT:** Add static topographic/edaphic predictors (slope, soil texture) and average future projections across at least 3 CMIP6 GCMs (e.g., `HadGEM3-GC31-LL`, `MIROC6`, `MPI-ESM1-2-HR`).
* **HOW:** Include DEM-derived slope in the predictor correlation screening and report the mean $\pm$ SD of suitable habitat area across the multi-GCM ensemble for each SSP and time window.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Residual uncorrected text errors and incomplete study-area descriptions confuse readers.
* **WHAT & HOW:**
  1. **Results line 40:** Despite the published correction notice (line 190), line 40 still reads `"followed by mean temperature of coldest quarter (bio 12, 29.3%)"`—change this to `"annual precipitation (bio 12, 29.3%)"`.
  2. **Materials and Methods line 145:** Expand the "Study area" description to cover the entire $\sim 337,889\text{ km}^2$ modeled extent across northern Pakistan (KPK, northern Punjab, Gilgit-Baltistan, and AJ&K) rather than describing only the $13,297\text{ km}^2$ of AJ&K.
  3. **Data Availability (line 180):** Provide the $1\text{ km}^2$ predicted suitability rasters and degraded/district-level occurrence data in the Supplementary Information or Zenodo/Dryad.
