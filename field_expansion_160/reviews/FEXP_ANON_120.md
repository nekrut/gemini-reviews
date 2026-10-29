# Forensic Peer Review: FEXP_ANON_120

**Overall Score:** **7.2 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.6 / 8.0**  
* **Score Breakdown:** Rigor: 2.4/3.5 | Claims: 1.7/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.6/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_120`
* **Perceived Domain & Topic:** Marine Movement Ecology / Marine Mammal Conservation / Species Distribution Modeling; climate-driven shifts in habitat suitability and inter-specific overlap among Baltic gray seals (*Halichoerus grypus*), harbor seals (*Phoca vitulina*), and harbor porpoises (*Phocoena phocoena*) in the southwestern Baltic Sea, Danish Straits, and Kattegat.
* **Perceived Empirical Scope:** Satellite telemetry (Argos and GPS) from $N = 237$ tagged marine mammals (31 Baltic gray seals, 74 harbor seals, 132 harbor porpoises) collected across 1997–2020; 7 static and dynamic oceanographic predictors (HELCOM and Bio-ORACLE CMIP5 ensemble); MaxEnt models tuned via `ENMeval` (`L`, `Q`, `LQ` features; $\text{RM} \in [0.5, 5.0]$), MESS novel-environment masking, and multi-threshold (`Kappa`, `MSSS`, `P10`) projections to 2091–2100 under RCP 6.0 and RCP 8.5.

---

## 2. Executive Summary & Editorial Verdict

This study uses a 24-year satellite telemetry dataset ($N = 237$ tagged individuals across Baltic gray seals, harbor seals, and harbor porpoises) in the southwestern Baltic Sea to model contemporary (1997–2020) and end-of-century (2091–2100, RCP 6.0 and RCP 8.5) habitat suitability and inter-specific spatial overlap using MaxEnt. The authors restrict feature classes to linear and quadratic functions (`ENMeval`, $\text{OR}_{10} < 0.09$, $\text{AUC} > 0.71$), account for sampling bias via species-specific Gaussian kernel density background weighting, incorporate regional glacial isostatic adjustment into sea-level rise inundation of seal haulout sites, mask out novel environmental domains via Multivariate Environmental Similarity Surfaces (MESS), and evaluate changes in suitable area and spatial clustering (`NNI`) across three probability thresholds (`Kappa`, `MSSS`, `P10`). They project declines in gray seal and (under RCP 8.5) harbor seal suitability—driven primarily by haulout inundation and salinity shifts—alongside slight increases in harbor porpoise suitability, resulting in a near-complete loss of three-species high-suitability overlap under RCP 8.5. Data are archived on Dryad and an ODMAP protocol is provided in Appendix S1.

**Editorial Verdict: Strong / Sound Empirical Study with Manageable Methodological Caveats (7.2 / 10.0).** Unlike many correlative SDM projection studies, this manuscript follows best-practice ecological modeling standards (ODMAP reporting, parsimonious `L`/`Q` response curves, explicit MESS extrapolation masking, multi-threshold sensitivity analysis, and transparent discussion of historical recolonization and unmodeled anthropogenic stressors). Nevertheless, three methodological issues affect the precision of the quantitative forecasts and should be addressed:
1. **Unaccounted individual-level pseudoreplication and unequal tag duty cycles:** Pooling thousands of telemetry fixes across 31–132 individuals without inverse-individual weighting or individual-blocked cross-validation allows long-tracked and GPS-tagged animals (subsampled every 6 hours) to dominate model likelihoods relative to Argos-tagged animals (duty-cycled every 1–4 days).
2. **Sensitivity of future seal projections to subjective haulout elevation judgments and MESS domain truncation:** Because "distance to nearest haulout" is a primary driver of seal suitability, relying on subjective co-author judgment rather than coastal LiDAR/DEM elevation profiles to remove flooded haulouts—without allowing adjacent coastal haulout replacement—mechanically forces large habitat losses. Additionally, masking out novel climate pixels via MESS (white areas in Figure 3) shrinks the spatial domain available for future suitability counting unless areas are normalized by the non-masked extent.
3. **Minor inconsistencies in future timeframe labels (`2091–2100` vs. `2090–2100` vs. `2080–2100`) and linear vs. areal resolution units (`500 m^2`, `9.2 km^2`).**

### Assessment of Specific Claims

* **Claim 1 (Contemporary habitat suitability of Baltic gray seals, harbor seals, and harbor porpoises is well captured by parsimonious MaxEnt models [$\text{AUC} > 0.71$, $\text{OR}_{10} < 0.09$] driven by sea surface salinity, distance to haulouts, and seabed slope): `[Well Supported]`.**  
  Collinearity screening ($\text{VIF} < 3$, $|\rho| < 0.6$), kernel bias correction, restriction to `L`/`Q` features, and low omission rates provide a well-calibrated representation of contemporary space use, and the authors appropriately caveat that the apparent negative salinity response of Baltic gray seals partly reflects southern tagging bias during ongoing Kattegat recolonization.
* **Claim 2 (Under RCP 6.0 and RCP 8.5, Baltic gray seal and harbor seal habitat suitability will decline largely due to sea-level-rise inundation of current haulout sites and changing salinity): `[Moderately Supported]`.**  
  While the mechanism (submergence of low-lying sandbars and skerries under $0.39\text{–}0.65\text{ m}$ eustatic rise plus isostatic adjustment) is biologically sound, haulout inundation was determined by qualitative co-author judgment rather than high-resolution coastal elevation models, and the model prohibits establishment of alternative haulouts along adjacent shorelines.
* **Claim 3 (Harbor porpoise habitat suitability will remain stable or increase slightly by 2091–2100 across thresholds): `[Moderately Supported]`.**  
  Consistent with intermediate-salinity preferences and prior regional models (Edrén et al. 2010), though pooled seasonal layers (averaging monthly values over 2000–2014) smooth over seasonal foraging migrations.
* **Claim 4 (Inter-specific overlap in highly suitable [`Kappa`] habitats increases slightly from $40\text{ km}^2$ to $140\text{ km}^2$ under RCP 6.0 but disappears for three-species combinations under RCP 8.5): `[Fragile]`.**  
  The absolute area of three-species `Kappa` overlap is very small ($40\text{ km}^2$ corresponds to $\sim 1\text{–}5$ grid cells at $9.2\text{ km}$ resolution), making the binary overlap count sensitive to threshold choice (`Kappa` vs. `MSSS`), MESS pixel masking, and the deterministic removal of judged-inundated haulout sites.

---

## 3. Forensic Defect Inventory

### Defect 1: Unweighted Pooling of Individual Telemetry Trajectories and Asymmetric Argos vs. GPS Duty Cycles [ Pillar 2, Pillar 3, Pillar 4 — Moderate ]
* **Location:** Section "Location data" (line 34) and Section "Habitat suitability analyses" (lines 64–66).
* **Forensic Evidence:**
  The dataset combines Argos tags (duty-cycled to transmit every 1 to 4 days) and GPS tags (subsampled to every 6 hours, i.e., 4 locations/day) across 31 gray seals, 74 harbor seals, and 132 harbor porpoises (line 34). Consequently, a GPS-tagged animal tracked for several months contributes an order of magnitude more presence points than an Argos-tagged animal tracked for a few weeks. Treating all subsampled fixes as independent presence records in MaxEnt without inverse-individual weighting or blocking `ENMeval` cross-validation folds by individual animal ID causes (1) pseudo-replication within individual tracks to inflate test AUC and depress $\text{OR}_{10}$, and (2) population-level habitat suitability to be weighted toward long-tracked GPS individuals.
* **Fix:** Subsample both Argos and GPS tracks to a uniform temporal resolution (e.g., 1 daily location per individual) or weight presence records inversely by the total number of fixes per individual ($w_i = 1 / n_i$), and partition `ENMeval` cross-validation folds by **individual ID** rather than random/spatial point splits.

### Defect 2: Qualitative Judgment of Haulout Inundation and Unnormalized MESS Domain Masking in Future Area Comparisons [ Pillar 3, Pillar 5, Pillar 6 — Moderate ]
* **Location:** Section "Environmental data" (line 42), Section "Habitat suitability analyses" (line 68), and Figures 3, 5, and 6.
* **Forensic Evidence:**
  1. **Subjective haulout removal:** Line 42 notes: *"Accurate elevation data for seal haulout sites in this area are not known but were based on judgment by two co-authors (AG and JT) who are familiar with these haulout sites. The forecasted water-level rises effectively removed some currently available haulout sites from future use."* Because `distance to nearest haulout` is a dominant predictor for both seal species, removing specific haulouts by expert judgment without a sensitivity analysis (e.g., comparing suitability changes with and without haulout removal, or using national coastal LiDAR DEMs available for Denmark, Sweden, and Germany) conflates oceanographic climate change (SST, salinity) with assumed complete loss of local haulout capacity.
  2. **MESS masking vs. total suitable area calculation:** Line 68 and Figure 3 state that areas with novel environmental conditions identified by MESS (white cells in Figure 3) were excluded from future predictions. When computing absolute change in suitable area ($\text{km}^2$, Figure 5) and inter-specific overlap ($\text{km}^2$, Figure 6), excluding MESS-masked cells reduces the total evaluable area in 2091–2100 relative to 1997–2020.
* **Fix:** Add a factorial sensitivity run holding current haulout locations constant under RCP 6.0 and RCP 8.5 to partition how much of the projected seal habitat loss is driven by oceanographic shifts (salinity/SST) versus haulout submergence, and report suitable habitat areas both in absolute $\text{km}^2$ and as a percentage of the unmasked (non-novel MESS) study domain.

### Defect 3: Inconsistent Future Time-Window Labels and Linear vs. Areal Grid Resolution Notation [ Pillar 7 — Minor ]
* **Location:** Abstract (line 5), Section "Introduction" (line 16), Table 1 (lines 47–56), Section "Environmental data" (line 57), Section "Results" (lines 88, 99, 101, 106), and Figures 3–6 (lines 91, 94, 97, 109).
* **Forensic Evidence:**
  1. **Three different future period labels:** The future projection period is reported as **`2091–2100`** in the Abstract (line 5), Introduction (line 16), and Methods (line 57); as **`2090–2100`** in the Results text (lines 88, 99, 101, 106) and Figures 3–4 captions (lines 91, 94); and as **`2080–2100`** in the captions of Figures 5 and 6 (lines 97, 109). (Bio-ORACLE v2.0 future layers represent the 2090–2100 decade).
  2. **Resolution unit notation (`m^2` and `km^2` vs. linear `m` and `km`):** Table 1 (lines 48–56) and line 57 report raster resolutions as `500 m^2`, `300 m^2`, and `9.2 km^2`. In Bio-ORACLE (Assis et al. 2018), 5 arc-minute resolution equals **$9.2\text{ km}$ linear resolution** ($\approx 9.2\text{ km} \times 9.2\text{ km}$ at the equator, or $\approx 9.2\text{ km} \times 5.1\text{ km} \approx 47\text{ km}^2$ at $56^\circ\text{N}$), and HELCOM bathymetry is **$500\text{ m}$ linear resolution** ($500\text{ m} \times 500\text{ m} = 0.25\text{ km}^2$), not $500\text{ m}^2$.
* **Fix:** Standardize the future timeframe label (`2090–2100`) across all text sections and figure legends, and correct the spatial resolution units in Table 1 and line 57 from `500 m^2`, `300 m^2`, and `9.2 km^2` to `500 m`, `300 m`, and `9.2 km` (or `5 arc-min`).

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.4** | **3.5** | Rigorous ODMAP workflow, VIF/Spearman screening, kernel bias files, parsimonious `L`/`Q` feature tuning (`OR10 < 0.09`), MESS extrapolation masking, and 3-threshold sensitivity checks; tempered by unblocked individual telemetry pseudoreplication, unequal Argos/GPS duty cycles, and subjective haulout inundation. |
| **2. Claim-to-Evidence Alignment** | **1.7** | **2.5** | Balanced and transparent Discussion that explicitly flags the southern tagging bias for gray seals in Kattegat, haulout emergence uncertainty, and unmodeled anthropogenic stressors; overlap loss under `Kappa` ($40 \to 0\text{ km}^2$) is somewhat sensitive to threshold and haulout assumptions. |
| **3. Data Integrity & Biological Plausibility** | **1.5** | **2.0** | Extensive multi-species telemetry dataset ($N=237$ animals over 24 years) with post-capture 24h filtering and speed outlier removal, plus physically realistic inclusion of regional glacial isostatic adjustment in Baltic sea-level rise. |
| **4. Reproducibility & Data Integrity** | **1.6** | **2.0** | Data publicly archived on Dryad and ODMAP protocol provided in Appendix S1; minor deductions for inconsistent future period labels (`2091–2100` vs. `2090–2100` vs. `2080–2100`) and linear resolution unit typos (`500 m^2`, `9.2 km^2`). |
| **Total Composite Score** | **7.2** | **10.0** | **Strong / Sound** (Scientific Core Score: **5.6 / 8.0**) |
