# Forensic Review of `FEXP_ANON_101`

**Overall Score:** **3.8 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **3.0 / 8.0**
* **Score Breakdown:** Rigor: 1.0/3.5 | Claims: 0.9/2.5 | Biology: 1.1/2.0 | Reproducibility: 0.8/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Field & Subfield:** Agricultural Ecology / Biogeography / Species Distribution Modeling (MaxEnt habitat suitability projection for cultivated mango *Mangifera indica* in China under CMIP6 climate scenarios).
* **Study Design Archetype:** Standard single-GCM (`BCC-CSM2-MR`) MaxEnt 3.4.4 modeling pipeline using 109 thinned occurrence records and 16 environmental predictors (selected from 51 initial variables), `kuenm` parameter tuning, centroid shift tracking (`SDMtoolbox`), and Multivariate Environmental Similarity Surface (`MESS` / `MoD`) analysis across SSP126 and SSP585 (2041–2100).
* **Temporal & Venue Signals:** Typical 2024–2025 regional single-species MaxEnt projection paper.

---

## 2. Executive Summary & Editorial Verdict

This manuscript models the current and future (2041–2060, 2061–2080, 2081–2100) potential suitable habitat of mango (*Mangifera indica* L.) across China under CMIP6 SSP126 and SSP585 scenarios (`BCC-CSM2-MR`) using MaxEnt (`n = 109` occurrence points after $2.5'\times 2.5'$ spatial thinning) and 16 environmental variables. The authors conclude that mango's suitable area in China is primarily determined by Mean Temperature of the Coldest Quarter (`Bio11`, 71.3% contribution) and Annual Accumulated Temperature $\ge 10^\circ\text{C}$ (`TEMJW10`, 6.2% contribution), and recommend expanding commercial mango plantations northward into the Sichuan–Chongqing basin.

**Editorial Verdict: Reject (Flawed / Overstated).** The study suffers from three major methodological and physical flaws:
1. **Climatological Inconsistency in Future Projections:** In Methods (line 47), the authors include four dynamic climatic/phenological variables outside the standard WorldClim set—most notably Annual Accumulated Temperature $\ge 10^\circ\text{C}$ (`TEMJW10`, the second most important predictor in the model), Annual Relative Humidity (`RHU`), Annual Sunshine Duration (`SSD`), and `NDVI`—and explicitly hold them **constant at their 1970–2000 values** during 2041–2100 climate change projections while updating only the WorldClim bioclimatic variables (`Bio11`, `Bio19`, `Bio3`, `Bio13`). Holding accumulated temperature ($\ge 10^\circ\text{C}$), humidity, and sunshine duration static under SSP585 warming ($+8.5\text{ W/m}^2$) violates physical consistency between predictors.
2. **Direct Mathematical Contradictions Between Table 2 and Table 3:** Every row of Table 2 (`Expansion`, `Stability`, `Contraction`) is mathematically incompatible with the total suitable areas reported in Table 3 (`Current` and future `Suitable` areas). For example, under `SSP126 (1970–2000)–(2041–2060)`, Table 2 reports a `Stability` area of $525,199.03\text{ km}^2$, which exceeds the *entire* current suitable habitat reported in Table 3 ($481,081.40\text{ km}^2$) by more than $44,000\text{ km}^2$.
3. **Agronomic Misapplication of Wild Niche Theory:** Treating an intensively managed tropical orchard crop as a wild species limited by natural seed-dispersal barriers ("niche conservation" and "lack of transmission media", line 178) ignores the well-known meteorological constraints (winter radiation fog, low solar insolation, and spring frost/anthracnose) that actually restrict commercial mango production in the Chongqing/central Sichuan basin.

### Assessment of Specific Claims

* **Mean Temperature of the Coldest Quarter (Bio11, 71.3% contribution) is the primary macroclimatic determinant of current mango distribution in southern China (Abstract; Results, line 108; Table 1): `[Moderately Supported]`**  
  Cold-season thermal minima (`Bio11 > 9.29°C`) plausibly delineate the northern boundary of tropical/subtropical mango cultivation in southern China, although collinearity between `Bio11` and `TEMJW10` ($\ge 10^\circ\text{C}$ accumulated temperature) inflates the dominance of `Bio11`.
* **Future suitable habitat areas and expansion/contraction dynamics under SSP126 and SSP585 are accurately quantified in Tables 2 and 3 (Results, lines 116–149; Tables 2–3): `[Methodologically Flawed]`**  
  Table 2 and Table 3 contradict each other by $8.5\text{--}9.3\%$ across all six scenario periods because Table 3 normalizes percentages to a nominal total area of $9,600,000.00\text{ km}^2$ whereas Table 2 computes pixel areas on an uncalibrated/different projection totaling $\sim 10.48\times 10^6\text{ km}^2$. Furthermore, holding `TEMJW10` ($\ge 10^\circ\text{C}$ accumulated temperature), `RHU`, and `SSD` constant at 1970–2000 values during future projections corrupts the projected suitability surfaces.
* **Annual sunshine duration (SSD) in central Sichuan will have a positive effect on future mango growth based on MoD analysis (Discussion, line 189; Fig. 7B, D): `[Methodologically Flawed]`**  
  Because `SSD` was held static at its 1970–2000 baseline in the future projections (Methods, line 47), any `MoD` flag for `SSD` merely reflects spatial differences between the reference training envelope and the Sichuan Basin's notoriously low baseline sunshine duration, not a beneficial future change in `SSD`.
* **Absence of current mango cultivation in Chongqing is explained by the evolutionary niche conservation hypothesis, mountain barriers, and lack of dispersal media (Discussion, line 178): `[Overstated]`**  
  Mango in China is an anthropogenically planted orchard tree, not a naturally dispersing wild species. Its absence from most of Chongqing and the central Sichuan Basin reflects agronomic unsuitability (extremely low sunshine duration, high humidity, and frost episodes) rather than natural dispersal lag.

---

## 3. Forensic Defect Inventory

### 3.1. Arithmetic Incompatibility Between Table 2 and Table 3 (Pillar 3 & Pillar 7)
* **Location:** Results (lines 100, 116, 122–144; Table 2 and Table 3).
* **Defect:** For any transition from period $t_1$ to $t_2$, the area of suitable habitat must satisfy $\text{Suitable}(t_1) = \text{Stability} + \text{Contraction}$ and $\text{Suitable}(t_2) = \text{Stability} + \text{Expansion}$. Auditing Table 2 against Table 3 reveals pervasive discrepancies:
  * **Baseline (`1970–2000`):** Table 3 states `Current Suitable` $= 481,081.40\text{ km}^2$ ($5.01\%$ of $9,600,000.00\text{ km}^2$). Yet Table 2 states that from `1970–2000` to `2041–2060`, `Stability + Contraction` $= 525,199.03 + 557.46 = 525,756.49\text{ km}^2$ under SSP126 (and $525,604.45 + 152.03 = 525,756.48\text{ km}^2$ under SSP585)—a $44,675.09\text{ km}^2$ ($+9.29\%$) discrepancy.
  * **SSP126 (`2041–2060`):** Table 3 reports `Suitable` $= 707,529.71\text{ km}^2$. Table 2 Row 1 implies $\text{Stability} + \text{Expansion} = 525,199.03 + 242,771.84 = 767,970.87\text{ km}^2$ ($+8.54\%$ higher).
  * **SSP585 (`2081–2100`):** Table 3 reports `Suitable` $= 1,113,810.96\text{ km}^2$. Table 2 Row 6 implies $\text{Stability} + \text{Expansion} = 1,005,218.72 + 190,801.77 = 1,196,020.49\text{ km}^2$ ($+7.38\%$ higher).
  The text indiscriminately mixes Table 3 totals ($4.81\times 10^5\text{ km}^2$) with Table 2 expansion figures ($242,771.84\text{ km}^2$).

### 3.2. Freezing Dynamic Climatic Variables (`TEMJW10`, `RHU`, `SSD`, `NDVI`) in Future Scenarios (Pillar 3)
* **Location:** Methods ("Environmental factors", line 47; Table 1, lines 56–64).
* **Defect:** The authors state: *"we believe environmental factors other than bioclimatic factors will not undergo significant changes in this study... Future projections (2041-2060, 2061-2080, and 2081-2100) employed updated bioclimatic components for each period, but other factors remained constant."* However, the "other factors" held constant include **Annual accumulated temperature ($\ge 10^\circ\text{C}$, `TEMJW10`)**, **Annual relative humidity (`RHU`)**, **Annual sunshine duration (`SSD`)**, and **`NDVI`**, as well as baseline datasets from mismatched historical decades (1970–2000 climate, 2003 land cover, 2004–2013 UV-B, and 2023 soil data). Under global warming scenarios (SSP126 and SSP585), accumulated temperature $\ge 10^\circ\text{C}$ (`TEMJW10`) increases substantially alongside `Bio11`; holding `TEMJW10` fixed at 1970–2000 values creates artificial clamping and invalidates the projected response.

### 3.3. Unreported `kuenm` Tuning Parameters, Single-GCM Reliance, and Metadata Contradictions (Pillar 4, 5, 7)
* **Missing `kuenm` Outputs:** Methods (line 76) describes testing 1,240 candidate models (40 RM $\times$ 29 FC combinations) in `kuenm`, yet the Results section never reports which Regularization Multiplier (`RM`), Feature Class (`FC`), partial ROC, omission rate, or $\Delta\text{AICc}$ was actually selected, nor whether the reported AUC ($0.989$), TSS ($0.910$), and Kappa ($0.870$) represent training or 25% held-out test metrics (and omits standard deviations across the 10 bootstrap replicates).
* **Single Climate Model (`BCC-CSM2-MR`):** Future projections rely solely on a single GCM (`BCC-CSM2-MR`) rather than a multi-GCM ensemble, providing no quantification of inter-model structural climate uncertainty.
* **Contradictory Spatial Resolutions in Text vs. Data Availability:** Methods (line 47) states that the Digital Elevation Model (DEM) had a resolution of **250 m** and land cover indices had a resolution of **30"** (30 arc-seconds). In contrast, the Data Availability Statement (lines 203, 218) states that the DEM had a resolution of **25 m** and land cover indices had a resolution of **15 sec** (15 arc-seconds).
* **Missing Occurrence Coordinates:** The 109 filtered occurrence coordinates used to train the MaxEnt model are not provided in the manuscript or supplementary files.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.0** | 3.5 | Freezing dynamic climate variables (`TEMJW10` accumulated temperature $\ge 10^\circ\text{C}$, `RHU`, `SSD`) at 1970–2000 levels during 2041–2100 projections; $8.5\text{--}9.3\%$ mathematical contradiction between Table 2 and Table 3; unreported `kuenm` optimal RM/FC parameters and replicate variance; single GCM. |
| **2. Claim-to-Evidence Alignment** | **0.9** | 2.5 | Recommending commercial mango expansion into central Sichuan/Chongqing and attributing current absence to wild "niche conservation" and "lack of transmission media" overreaches correlative SDM outputs. |
| **3. Data Integrity & Biological Plausibility** | **1.1** | 2.0 | `Bio11` cold-quarter temperature constraint is biologically plausible for mango, but holding $\ge 10^\circ\text{C}$ accumulated temperature constant while warming `Bio11` is physically implausible. |
| **4. Reproducibility & Data Integrity** | **0.8** | 2.0 | Incompatible area calculations between Tables 2 and 3; contradictory DEM (`250 m` vs `25 m`) and land cover (`30"` vs `15"`) resolutions between Methods and Data Availability; 109 occurrence coordinates not deposited. |
| **Total Composite Score** | **3.8** | **10.0** | **Flawed / Overstated** (**Scientific Core Score: 3.0 / 8.0**) |
