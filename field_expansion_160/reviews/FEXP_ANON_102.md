# Forensic Review of `FEXP_ANON_102`

**Overall Score:** **4.1 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **3.3 / 8.0**
* **Score Breakdown:** Rigor: 1.1/3.5 | Claims: 1.0/2.5 | Biology: 1.2/2.0 | Reproducibility: 0.8/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Field & Subfield:** Conservation Biology / Biogeography / Mammalian Ecology (Species distribution and landscape connectivity modeling of giant flying squirrels *Petaurista magnificus* and *Petaurista nobilis* in the Eastern Himalayas and Indo-Burma hotspots).
* **Study Design Archetype:** Comparative MaxEnt 3.4.4 species distribution modeling study comparing a Habitat–Climate Model (HCM, 10 variables) vs. a Climate-Only Model (COM, 7 variables) trained on small GBIF/iNaturalist occurrence sets ($n = 22$ for *P. magnificus*, $n = 36$ for *P. nobilis*), paired with `Circuitscape` corridor modeling, `FRAGSTATS` patch geometry metrics, and CMIP6 (`HadGEM3-GC31-LL`) future projections under SSP245 and SSP585 (2041–2080).
* **Temporal & Venue Signals:** Recent (2024–2025) regional conservation SDM study.

---

## 2. Executive Summary & Editorial Verdict

This study models current and future (2041–2060, 2061–2080) habitat suitability, landscape corridor connectivity (`Circuitscape`), centroid shifts (`SDMtoolbox`), and patch fragmentation (`FRAGSTATS`) for two Himalayan giant flying squirrels, *Petaurista magnificus* and *Petaurista nobilis*, across their IUCN-designated ranges using MaxEnt under a Habitat–Climate Model (HCM) and a Climate-Only Model (COM). The authors report that only 3.92% (*P. magnificus*) and 14.17% (*P. nobilis*) of the current IUCN range is suitable under HCM, and project future climate-driven habitat declines of up to 81.90% and 89.88%, respectively.

**Editorial Verdict: Reject / Major Revision Required (Flawed / Overstated).** While addressing an important conservation gap for two understudied arboreal mammals, the modeling workflow suffers from fundamental statistical and methodological defects:
1. **Severe Overfitting on Small Sample Sizes & Reliance on Training AUC:** With only $n \le 22$ occurrence records for *P. magnificus* and $n \le 36$ for *P. nobilis*, fitting 10 predictor variables in MaxEnt (~2.2 occurrences per variable for *P. magnificus*) without regularization multiplier (`RM`) or feature class (`FC`) tuning creates severe overfitting. Worse, model accuracy is evaluated exclusively via **average training AUC** (Results, line 57: `0.971 ± 0.009` and `0.933 ± 0.021`), with no held-out test AUC, True Skill Statistic (TSS), or omission rate reported.
2. **Conflation of Bootstrapping and Leave-One-Out ($n-1$) Jackknife Replication:** Methods Section 2.4 (line 39) states that the model used a *"bootstrapping replication approach"* where *"training data for each occurrence point were treated as $n - 1$, and model execution was evaluated over 50 replicate runs"*, conflating leave-one-out jackknife cross-validation ($n-1$ training points across $n$ runs) with bootstrap resampling ($n$ points drawn with replacement across 50 runs).
3. **Contradictory Occurrence Data Filtering, Uncalibrated Trigonometric Centroid Bearings, and Omitted Main-Text Tables:** Methods Section 2.1 (line 24) states that museum records were collected from the Zoological Survey of India (`Table S1`, $n=6$ and $9$) and immediately states in the next sentence that *"records from captive and museum specimens were excluded"*, leaving the final post-thinning sample size unstated. Furthermore, `Table 1`, `Table 2`, and `Table 3` are cited throughout the Results (lines 59, 66, 73) but are completely omitted from the manuscript text.

### Assessment of Specific Claims

* **MaxEnt HCM and COM models achieve "exceptional predictive performance" based on AUCs > 0.92 (Results, line 57): `[Methodologically Flawed]`**  
  Results Section 3.1 explicitly reports *"average training area under the curve (AUC)"* (`0.971` and `0.968` for *P. magnificus*; `0.933` and `0.921` for *P. nobilis*) on small occurrence datasets ($n \le 22$ and $n \le 36$) fitted with 10 and 7 predictors under default un-tuned MaxEnt settings. High training AUC in low-$n$, high-dimensional MaxEnt models reflects in-sample overfitting rather than out-of-sample predictive skill, and explica why the binary model classifies only 3.92% of *P. magnificus*'s IUCN range as suitable.
* **Future climate change will cause 81.90% (P. magnificus) and 89.88% (P. nobilis) habitat loss by 2061–2080 under SSP585 (Abstract; Results, line 66): `[Fragile]`**  
  Projections rely on a single global climate model (`HadGEM3-GC31-LL`—a high-climate-sensitivity GCM) and hold non-climatic variables constant (Elevation, Slope, Aspect, Human Influence Index, and Euclidean distance to evergreen/montane forest, which together account for $>51\%$ of model contribution in *P. magnificus*). Because the current model is tightly overfitted around 22 points without regularization tuning or Multivariate Environmental Similarity Surface (`MESS`) clamping checks, shifting temperature/precipitation variables pushes pixels outside the narrow training envelope, inflating projected range collapse.
* **Centroid shift analysis predicts a northwestward shift (151°–160°) for P. magnificus and a westward shift (182°–185°) for P. nobilis (Abstract; Results, line 68): `[Moderately Supported]`**  
  The authors report raw trigonometric polar angles output by `SDMtoolbox` (where $0^\circ = \text{East}$ and angles increase counterclockwise, so $151^\circ\text{--}160^\circ$ is WNW and $182^\circ\text{--}185^\circ$ is W) as if they were standard geographic compass bearings (where $151^\circ\text{--}185^\circ$ would be SSE to South), without defining the coordinate convention.
* **Elevation Contribution (25.1% vs. 9.4%) proves P. magnificus occupies higher elevations than P. nobilis (Discussion, line 80): `[Methodologically Flawed]`**  
  In Discussion (line 80), the authors argue: *"elevation is a key factor, contributing 25.1% to P. magnificus, which is higher than its 9.4% contribution to P. nobilis, indicating that P. magnificus occupies higher elevations than P. nobilis."* In MaxEnt, percentage contribution measures how much training gain is explained by a variable across the background extent, **not** the sign or mean elevation of the species' niche (indeed, Section 2.2 line 29 notes that *P. magnificus* occurs down to $400\text{ m}$ a.s.l. whereas *P. nobilis* is restricted to $1500\text{--}3000\text{ m}$ a.s.l.).

---

## 3. Forensic Defect Inventory

### 3.1. Overfitting, Training-Only AUC Evaluation, and Confused Replication Design (Pillar 3 & Pillar 4)
* **Location:** Methods Sections 2.1 (line 24) and 2.4 (line 39); Results Section 3.1 (line 57).
* **Defect 1 (Events-Per-Variable & Un-Tuned Complexity):** For *P. magnificus*, at most 22 GeoCAT points (prior to $1\text{ km}^2$ spatial filtering) are fitted against 10 predictors in HCM (2.2 points per predictor). For small sample sizes ($n < 30$), default MaxEnt feature classes (hinge, product, threshold) severely overfit unless regularized via `ENMeval` or `kuenm`.
* **Defect 2 (Training AUC Reported as Model Validation):** Results (line 57) evaluates model accuracy using only *"average training area under the curve (AUC)"*, omitting held-out test AUC, omission error rate, and True Skill Statistic (TSS).
* **Defect 3 (Bootstrap vs. $n-1$ Jackknife Confusion):** Methods (line 39) states: *"The model development employed a bootstrapping replication approach... During this process, training data for each occurrence point were treated as $n - 1$, and model execution was evaluated over 50 replicate runs"*. Bootstrapping samples $n$ observations with replacement; leave-one-out jackknife uses $n-1$ observations for exactly $n$ runs, not 50 runs.

### 3.2. Contradictory Museum Record Handling & Unreported Post-Thinning Sample Size (Pillar 2 & Pillar 7)
* **Location:** Methods Section 2.1 (line 24).
* **Defect:** The authors write: *"Additionally, locality information was collected for both species (P. magnificus = 6; P. nobilis = 9) from the museum collections archived in the National Zoological Collections of the Zoological Survey of India (Table S1). Hence, to minimize overfitting and bias in model interpretation, records from captive and museum specimens were excluded to clearly depict their presence areas within the natural habitat."* It is self-contradictory to collect and tabulate museum specimen localities in `Table S1` and immediately state that museum specimens were excluded. Furthermore, the number of occurrence points remaining after $1\text{ km}^2$ spatial correlation filtering in `SDM Toolbox v2.4` is never reported.

### 3.3. Omitted Main-Text Tables & Internal Text Inconsistencies (Pillar 7)
* **Missing Tables 1, 2, and 3:** Results Sections 3.1, 3.2, and 3.3 repeatedly cite `Table 1` (variable contributions, line 59), `Table 2` (future habitat area dynamics, line 66), and `Table 3` (`FRAGSTATS` patch metrics, line 73), but none of these three tables are present in the manuscript file, leaving the full list of 10 HCM and 7 COM variables and the exact area/fragmentation numbers unverifiable.
* **Contradictory Global Species Counts:** Introduction (line 12) states *"Globally, **57 species** of flying squirrels, classified under 15 genera... are widely distributed across Eurasia and North America"*, whereas the very next paragraph (line 14) states *"Specifically, among the **37 globally recognized species** of flying squirrels..."*.
* **Inconsistent Software Versioning:** Methods (lines 34, 39, 44) alternates between `ArcGIS v.10.8` and `ArcGIS 10.6` within the same pipeline.
* **Data Availability:** Occurrence coordinates and output suitability/corridor rasters are not publicly deposited (*"provided upon request"*, line 97).

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.1** | 3.5 | Overparameterized MaxEnt model (22 points, 10 predictors) without feature/regularization tuning; reliance on training AUC rather than test AUC/TSS; confusion of bootstrap (50 runs) with $n-1$ jackknife; single GCM (`HadGEM3-GC31-LL`). |
| **2. Claim-to-Evidence Alignment** | **1.0** | 2.5 | Overfitting around 22 points likely drives both the tiny baseline suitability (3.92% of IUCN range) and the extreme projected range loss (81.9–89.9%); misinterprets MaxEnt percentage contribution (25.1% vs 9.4%) as proving higher mean elevation occupancy. |
| **3. Data Integrity & Biological Plausibility** | **1.2** | 2.0 | Sensible ecological framing of Himalayan transboundary arboreal habitats and corridor connectivity, but undermined by contradictory inclusion/exclusion of museum specimens and unstated post-thinning sample sizes. |
| **4. Reproducibility & Data Integrity** | **0.8** | 2.0 | `Table 1`, `Table 2`, and `Table 3` are missing from the manuscript text; contradictory global species counts (57 vs 37); trigonometric angles reported as compass bearings without convention; data only available upon request. |
| **Total Composite Score** | **4.1** | **10.0** | **Flawed / Overstated** (**Scientific Core Score: 3.3 / 8.0**) |
