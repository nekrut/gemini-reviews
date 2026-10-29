# Forensic Peer Review: FEXP_ANON_113

**Overall Score:** **4.3 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **3.3 / 8.0**  
* **Score Breakdown:** Rigor: 1.2/3.5 | Claims: 1.0/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.0/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_113`
* **Perceived Domain & Topic:** Ecological Niche Modeling / Species Distribution Modeling (SDM); MaxEnt climate-change habitat projection for the subtropical broadleaf tree *Betula alnoides* in China.
* **Perceived Empirical Scope:** 251 compiled occurrence records (thinned to 206 points at 2.5′ × 2.5′ resolution) across China; 38 initial environmental predictors thinned to 17 variables (WorldClim v2.1 bioclimatic layers, SRTM topography, HWSD v2.0 soil, MODIS NDVI, and Human Footprint Index); future projections for the 2050s, 2070s, and 2090s using a single CMIP6 GCM (`BCC-CSM2-MR`) under SSP126, SSP370, and SSP585.

---

## 2. Executive Summary & Editorial Verdict

This study constructs a tuned MaxEnt species distribution model (`ENMeval`, RM = 0.5, FC = LQ) for *Betula alnoides* in China using 206 spatially thinned occurrence records and 17 environmental variables. The authors report high cross-validated discrimination (AUC = 0.956, TSS = 0.880), identify temperature seasonality (Bio4, 57.9% contribution) and MODIS NDVI (19.6% contribution) as the dominant predictors, estimate a current suitable habitat area of $179.32 \times 10^4\text{ km}^2$, and project future habitat contractions and northwestward centroid shifts under SSP126, SSP370, and SSP585. Location records and environmental variable tables are noted as included in the Supplementary Materials, though no analysis scripts or raster outputs are deposited.

**Editorial Verdict: Reject / Major Re-analysis Required (4.3 / 10.0).** While the use of `ENMeval` to tune MaxEnt regularization and feature classes is appropriate in principle, the manuscript suffers from severe internal numerical contradictions, methodological inconsistencies between the Methods and Discussion, and biologically flawed projection assumptions:
1. **Mathematical impossibility in habitat change accounting (Sections 3.3–3.5 and Table 1):** For every single future scenario and period in Table 1, the reported "retained/stable" habitat area (`Stability`) is **larger** than the *entire* suitable habitat area reported for that same scenario and period in Section 3.4 (e.g., 2050s-SSP126 total suitable area = $124.89 \times 10^4\text{ km}^2$ in Section 3.4, yet `Stability` alone = $136.22 \times 10^4\text{ km}^2$ in Table 1). Moreover, $\text{Stability} + \text{Contraction}$ (which must equal the baseline current suitable area of $179.32 \times 10^4\text{ km}^2$) instead sums to $\approx 218.8 \times 10^4\text{ km}^2$ across Table 1—an unacknowledged $39.5 \times 10^4\text{ km}^2$ ($395,000\text{ km}^2$) area inflation likely caused by computing polygon areas in unprojected geographic coordinates (WGS84 degrees) in one workflow versus an equal-area projection in another.
2. **Static NDVI in century-scale climate projections and predictor circularity:** NDVI accounts for 19.6% of model contribution (second highest overall) and is held completely static at present-day MODIS values through the 2090s, while simultaneously representing an emergent property of existing subtropical forest cover rather than an exogenous abiotic driver.
3. **Unreported validation protocols appearing only in the Discussion:** Discussion Section 4.1 claims that the authors "employed spatially biased background points weighted by human footprint and verified robustness with k-fold block CV (AUC 0.93–0.96)," and Discussion Section 4.0 claims the use of "CMIP6 ensembles," none of which appear in the Methods (which specify 10,000 random background points, random cross-validation/split, and a single GCM `BCC-CSM2-MR`) or Results.

### Assessment of Specific Claims

* **Claim 1 (Tuned MaxEnt model RM = 0.5 / FC = LQ achieves lower complexity and 34.45% lower $\text{OR}_{10}$ than default parameters while maintaining AUC = 0.956): `[Moderately Supported]`.**  
  Parameter tuning via `ENMeval` using $\Delta\text{AICc}$ and 10% training omission rate ($\text{OR}_{10}$ dropping from 0.1895 to 0.1409) is sound, although the validation protocol is inconsistently described across sections (75%/25% stratified random split vs. 10-fold `Crossvalidate` in Section 2.3.2 vs. unsubstantiated "k-fold block CV" in Section 4.1).
* **Claim 2 (Distribution of *B. alnoides* is governed primarily by Bio4 [57.9%] and NDVI [19.6%], with optimal NDVI $\ge 0.57$ reflecting competitive forest subcanopy requirements): `[Fragile]`.**  
  Using contemporary satellite vegetation greenness (MODIS NDVI) as a predictor for a canopy/subcanopy forest tree introduces circularity (dense subtropical forests have high NDVI by definition) and confounds land-cover realization with fundamental climatic suitability. Furthermore, the single-factor response descriptions in Section 3.2 misinterpret flat tail extrapolations (e.g., claiming *B. alnoides* exhibits "drought tolerance (Bio9 range: −31.88–27.27 °C)" in Section 4.2 based on clamped boundary values of the response curve).
* **Claim 3 (Future suitable habitat contracts to $98.79\text{–}136.19 \times 10^4\text{ km}^2$ in Section 3.4 while retaining $100.54\text{–}143.69 \times 10^4\text{ km}^2$ of stable habitat in Table 1): `[Methodologically Flawed]`.**  
  A subset of suitable habitat (`Stability`) cannot exceed the total suitable habitat ($\text{Stability} + \text{Expansion}$), nor can $\text{Stability} + \text{Contraction}$ equal $218.8 \times 10^4\text{ km}^2$ when current suitable habitat is $179.32 \times 10^4\text{ km}^2$. Additionally, holding present-day NDVI constant through 2100 invalidates the future suitability maps.
* **Claim 4 (*B. alnoides* suitable habitat undergoes a $>480\text{ km}$ northwestward shift under SSP585 requiring assisted migration because natural wind dispersal [60–120 m] would take 1200–2000 years): `[Overstated]`.**  
  First, the reported $482.21\text{ km}$ shift is the sum of three sequential polyline segments ($253.49 + 208.79 + 19.93\text{ km}$, the last of which reverses southwestward), not net displacement. Second, the northwestward shift of the binary polygon centroid is primarily a geometric artifact of severe habitat loss (`Contraction`) in the southeastern part of the range (Guangxi/Guizhou/Guangdong) rather than newly colonized territory in the northwest, making the comparison between centroid drift velocity ($2.5\text{–}5\text{ km yr}^{-1}$) and seed dispersal distance ecologically invalid.

---

## 3. Forensic Defect Inventory

### Defect 1: Mathematically Impossible Habitat Area Accounting Between Section 3.3, Section 3.4, and Section 3.5 (Table 1) [ Pillar 3, Pillar 4, Pillar 7 — Critical ]
* **Location:** Section 3.3 (line 105), Section 3.4 (lines 113, 121, 123), Section 3.5 (lines 128–149), and Table 1.
* **Forensic Evidence:**
  Both Section 3.4 (suitability grading) and Section 3.5 (habitat stability/expansion/contraction) define total suitable habitat using the exact same logistic probability threshold ($\text{MTSPS} = 0.1022$). By fundamental set arithmetic, let $S_0$ be the set of currently suitable pixels and $S_t$ be the set of suitable pixels in future scenario/period $t$. Then:
  $$\text{Area}(S_0) = \text{Stability}_t \,(\text{Area}(S_0 \cap S_t)) + \text{Contraction}_t \,(\text{Area}(S_0 \setminus S_t))$$
  $$\text{Area}(S_t) = \text{Stability}_t \,(\text{Area}(S_0 \cap S_t)) + \text{Expansion}_t \,(\text{Area}(S_t \setminus S_0))$$
  Comparing the numbers reported in the manuscript reveals systematic violations in every single scenario:
  1. **Current baseline mismatch:** Section 3.3 states $\text{Area}(S_0) = 179.32 \times 10^4\text{ km}^2$ ($119.21 + 34.00 + 26.10 = 179.31 \times 10^4\text{ km}^2$). Yet in Table 1, $\text{Stability}_t + \text{Contraction}_t$ equals $218.82$ (2050s-SSP126), $218.90$ (2070s-SSP126), $218.73$ (2090s-SSP126), $218.75$ (2050s-SSP370), $219.01$ (2070s-SSP370), $218.84$ (2090s-SSP370), $218.78$ (2050s-SSP585), $218.86$ (2070s-SSP585), and $218.90 \times 10^4\text{ km}^2$ (2090s-SSP585). The baseline area in Table 1 is inflated by $\approx 39.5 \times 10^4\text{ km}^2$ (+22.0%).
  2. **Retained area exceeds total future suitable area:** In every scenario and period, `Stability` in Table 1 exceeds the total suitable area ($\text{Low} + \text{Moderate} + \text{High}$) in Section 3.4, and $\text{Stability} + \text{Expansion}$ exceeds Section 3.4 by ~22%:
     - **2050s-SSP126:** Section 3.4 total = $124.89 \times 10^4\text{ km}^2$; Table 1 `Stability` = $136.22 \times 10^4\text{ km}^2$ ($\text{Stability} + \text{Expansion} = 151.93 \times 10^4\text{ km}^2$).
     - **2070s-SSP126:** Section 3.4 total = $112.30 \times 10^4\text{ km}^2$; Table 1 `Stability` = $119.92 \times 10^4\text{ km}^2$ ($\text{Stability} + \text{Expansion} = 135.18 \times 10^4\text{ km}^2$).
     - **2090s-SSP126:** Section 3.4 total = $125.32 \times 10^4\text{ km}^2$; Table 1 `Stability` = $128.04 \times 10^4\text{ km}^2$ ($\text{Stability} + \text{Expansion} = 152.25 \times 10^4\text{ km}^2$).
     - **2090s-SSP370:** Section 3.4 total = $98.79 \times 10^4\text{ km}^2$; Table 1 `Stability` = $102.59 \times 10^4\text{ km}^2$ ($\text{Stability} + \text{Expansion} = 119.77 \times 10^4\text{ km}^2$).
     - **2070s-SSP585:** Section 3.4 total = $99.22 \times 10^4\text{ km}^2$; Table 1 `Stability` = $100.54 \times 10^4\text{ km}^2$ ($\text{Stability} + \text{Expansion} = 120.17 \times 10^4\text{ km}^2$).
  3. **Misdefined "Rate of Change (%)" in Table 1:** The three percentage columns in Table 1 sum to $100.0\%$ in every row because each component was divided by the union $\text{Area}(S_0 \cup S_t) = \text{Stability} + \text{Expansion} + \text{Contraction}$ rather than the baseline current suitable area $\text{Area}(S_0)$.
  4. **Text–Table transcription error:** Line 149 reports 2050s-SSP585 gained habitat as "$12.85 \times 10^4\text{ km}^2$ (9.08%)", whereas Table 1 reports "$21.85 \times 10^4\text{ km}^2$ (9.08%)".
* **Fix:** Recompute all raster and vector area statistics under a single, consistent equal-area projection (e.g., Albers Equal Area Conic for China) so that $\text{Stability}_t + \text{Contraction}_t \equiv \text{Area}(S_0)$ and $\text{Stability}_t + \text{Expansion}_t \equiv \text{Area}(S_t)$ across all sections, figures, and tables. Express gain and loss percentages relative to baseline current suitable area $\text{Area}(S_0)$.

### Defect 2: Unacknowledged Static Non-Climatic Predictors (NDVI) and Endogenous Predictor Circularity [ Pillar 2, Pillar 3, Pillar 6 — Major ]
* **Location:** Section 2.2 (lines 34–36), Section 3.2 (line 90), and Section 3.4 (lines 111–124).
* **Forensic Evidence:**
  1. MODIS NDVI contributes 19.6% to the MaxEnt model (the second largest predictor). Because no future projections of MODIS NDVI, HFI, or soil variables are used, these layers are kept fixed at their contemporary values when projecting into the 2050s, 2070s, and 2090s. Under +2.7°C to +4.4°C warming (SSP370/SSP585), vegetation greenness and canopy density will shift substantially; holding contemporary NDVI static anchors predicted suitability to current forest cover patterns.
  2. NDVI measures existing vegetation canopy greenness. For a forest tree species occurring in subtropical montane forests, high NDVI is partly a consequence of forest presence rather than an independent environmental predictor, inflating apparent model AUC while biasing projections against currently deforested or recovering habitats.
* **Fix:** Run a paired climate + topography + soil model (excluding static contemporary NDVI and HFI) and compare its historical cross-validation metrics and future projections against the full 17-variable model to quantify how much of the projected range retention/contraction is an artifact of static present-day NDVI.

### Defect 3: Unsubstantiated Methods Claimed in the Discussion ("CMIP6 Ensembles", "Block CV", and "HFI-Weighted Background") [ Pillar 1, Pillar 3, Pillar 5 — Major ]
* **Location:** Section 2.2 (line 34), Section 2.3.2 (line 49), Discussion Section 4.0 (line 162), and Section 4.1 (line 167).
* **Forensic Evidence:**
  1. In Discussion Section 4.1 (line 167), the authors state: *"To mitigate this, we employed spatially biased background points weighted by human footprint and verified robustness with k-fold block CV (AUC 0.93–0.96), confirming that predictions remain reliable under residual bias."* Neither HFI-weighted background point sampling nor spatial block cross-validation (`k-fold block CV`) is described in Section 2.3.2 or reported in Section 3.1.
  2. Even within Section 2.3.2 (line 49), the validation scheme is self-contradictory: it states that the 206 points were partitioned into a 75% training set (155 points) and 25% testing set (51 points), and in the next sentence states that the `Crossvalidate` repeated run mode with 10 replicates was adopted (which in MaxEnt performs 10-fold cross-validation using 90% training / 10% testing per fold).
  3. Discussion line 162 claims the study integrates *"multi-factor parameter optimization with CMIP6 ensembles"*, whereas Section 2.2 (line 34) explicitly relies on a single global climate model (`BCC-CSM2-MR`). Relying on a single GCM fails to capture inter-model structural uncertainty in future East Asian monsoon precipitation.
* **Fix:** Reconcile the Methods, Results, and Discussion. If spatial block cross-validation and HFI-weighted background sampling were actually performed, document the exact implementation and fold metrics in Sections 2.3 and 3.1; if they were not performed, remove those claims from Section 4.1. Remove the "CMIP6 ensembles" claim or incorporate at least 3–5 CMIP6 GCMs to quantify inter-GCM variance.

### Defect 4: Misinterpretation of Response Curve Extrapolation and Centroid Shift Velocity [ Pillar 1, Pillar 6 — Moderate ]
* **Location:** Section 3.2 (line 95), Section 3.6 (line 154), Section 4.2 (line 10 of chunk 2), and Section 4.3 (lines 15–17 of chunk 2).
* **Forensic Evidence:**
  1. **Clamped response tails:** In Section 3.2 (line 95), the authors report that presence probability "remains stable" for NDVI between $-0.26$ and $-0.17$ and for Bio9 between $-31.88\,^\circ\text{C}$ and $-27.36\,^\circ\text{C}$, and in Section 4.2 they cite "Bio9 range: $-31.88\text{–}27.27\,^\circ\text{C}$" as evidence of *B. alnoides*' drought/thermal tolerance. Those flat tails at $-31.88\,^\circ\text{C}$ (far outside the subtropical distribution of *B. alnoides*) are standard MaxEnt clamping plateaus beyond the training environmental domain, not physiological tolerance.
  2. **Centroid drift vs. biological migration:** In Section 4.3, the authors sum the three sequential step distances under SSP585 ($253.49 + 208.79 + 19.93 = 482.21\text{ km}$, ignoring the directional reversal in the 2090s) to claim a $>480\text{ km}$ shift ($2.5\text{–}5\text{ km yr}^{-1}$), and contrast this with wind dispersal (60–120 m). However, Table 1 and Figure 9 show that the northwestward shift of the centroid is overwhelmingly driven by the *loss* of low- and moderate-suitability areas in southeastern China (Guangxi, Guangdong, Hunan, Jiangxi) rather than a 480 km colonization jump into northwestern China.
  3. **Minor technical typos:** Section 2.2 (line 34) defines the 2070s as "2061–2070" instead of the standard 20-year CMIP6 period "2061–2080". Section 2.3.1 (line 44) states "nine combinations of feature classes (FC) were constructed, including L, H, LQ, HPT, LQH, QHPP, QHPT, and LQHPT" (listing only 8 combinations, with "QHPP" containing a duplicate P instead of LQHP).

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.2** | **3.5** | `ENMeval` tuning ($\Delta\text{AICc}$, $\text{OR}_{10}$) is appropriate, but undermined by mathematically impossible area tables (`Stability > Total Suitable Area` in every row of Table 1; $39.5 \times 10^4\text{ km}^2$ baseline area discrepancy), static NDVI in future projections, single-GCM reliance, and contradictory validation descriptions. |
| **2. Claim-to-Evidence Alignment** | **1.0** | **2.5** | Claims of "CMIP6 ensembles," "k-fold block CV," and "HFI-weighted background points" in the Discussion are unsupported by the Methods/Results; centroid shift velocity is conflated with biological migration distance. |
| **3. Data Integrity & Biological Plausibility** | **1.1** | **2.0** | Occurrence thinning (206 points at 2.5′) is reasonable, but using present-day MODIS NDVI (19.6% contribution) as a static predictor through 2100 and interpreting MaxEnt clamping plateaus ($-31.88\,^\circ\text{C}$) as physiological tolerance are biologically flawed. |
| **4. Reproducibility & Data Integrity** | **1.0** | **2.0** | Occurrence coordinates and environmental tables are provided in Supplementary Materials, but severe internal numerical discrepancies between Section 3.3, Section 3.4, and Table 1, plus multiple text–table and methodological typos, prevent quantitative reproduction. |
| **Total Composite Score** | **4.3** | **10.0** | **Flawed / Overstated** (Scientific Core Score: **3.3 / 8.0**) |
