# Review of FEXP_ANON_129

**Overall Score:** **5.1 / 10.0** (Mixed / Salvageable)
* **Score Breakdown:** Rigor: 1.4/3.5 | Claims: 1.5/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.0/2.0
* **Scientific Core Score:** **4.1 / 8.0**

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_129`
* **Perceived Study Type:** Prospective clinical trial protocol (randomized, sham-controlled neuroimaging trial; ChiCTR2400084666; SPIRIT/STRICTA/ACURATE checklists).
* **Domain & Focus:** Integrative clinical neuroscience and neuroimaging (simultaneous resting-state EEG-fMRI and cognitive psychometric evaluation of 12-week manual acupuncture vs. superficial non-acupoint sham acupuncture in $N = 60$ patients with mild cognitive impairment [MCI]).
* **Empirical Data Status:** Protocol manuscript only ($N = 0$ enrolled/analyzed at $t_0$).

---

## 2. Executive Summary & Editorial Verdict

This manuscript presents a clinical trial protocol for a 12-week, 5-center randomized sham-controlled study ($N = 60$, allocated 1:1 to real acupuncture [RA] or superficial non-acupoint sham acupuncture [SA]) designed to evaluate clinical efficacy on the Alzheimer's Disease Assessment Scale-Cognitive subscale (ADAS-Cog) and resting-state simultaneous EEG-fMRI dynamics in patients with mild cognitive impairment (MCI). While the protocol incorporates standardized reporting checklists (SPIRIT, STRICTA, ACURATE) and centralizes EEG-fMRI acquisition on a single 3.0 T Siemens Skyra system with hardware clock synchronization (SyncBox), the methodological and statistical plan contains multiple internal contradictions, unpowered modeling choices, and template copy-paste errors where prospective procedures are described in the past tense as if already completed.

**Editorial Verdict:** **Major Revision Required (Protocol Salvageable via Statistical & Methodological Overhaul).** Because no empirical data have been analyzed yet, all identified defects can be corrected in the protocol and Statistical Analysis Plan (SAP) prior to unblinding. Specifically, the authors must power the trial for its primary clinical endpoint (or re-designate neuroimaging as the primary exploratory endpoint), replace unstratified randomization with center-stratified allocation across the five participating hospitals, replace simple two-sample $t$-tests with baseline- and site-adjusted linear mixed-effects or ANCOVA models, remove the severely underpowered Structural Equation Modeling (SEM) and circular post-hoc ROI correlation plans, and reconcile contradictory needling depths and practitioner qualifications between the text and tables.

### Assessment of Specific Protocol Claims & Design Commitments

* **Simultaneous EEG-fMRI acquisition and hardware synchronization design: [Moderately Supported].**  
  Centralizing scanning at a single site (Chengdu No. 4 People's Hospital) using a 64-channel MR-compatible cap synchronized to the scanner gradient switching clock via SyncBox is technically appropriate for minimizing gradient and ballistocardiographic artifact variability across the five recruiting hospitals.

* **Sample size justification ($N = 60$; 30 per arm) for primary clinical and multimodal neuroimaging endpoints: [Methodologically Flawed].**  
  The primary outcome is defined as the 12-week change in ADAS-Cog score, yet the sample size calculation (Section `Sample Size`) ignores ADAS-Cog entirely and relies solely on single-voxel task-fMRI simulation heuristics from 2002 ($n = 12\text{--}24$ subjects) without accounting for between-group longitudinal resting-state EEG-fMRI interaction variance or clinical minimal clinically important difference (MCID) on ADAS-Cog.

* **Statistical analysis plan for multicenter clinical and neuroimaging outcomes: [Methodologically Flawed].**  
  Randomization is performed without center stratification across five hospitals (`R` v4.1.2), and clinical outcomes are analyzed via simple two-sample $t$-tests or Mann–Whitney $U$-tests (`SPSS` v26.0) without adjusting for baseline ADAS-Cog or hospital site. In the neuroimaging plan, applying Structural Equation Modeling (SEM) to $n \le 30$ subjects per arm and correlating scale improvements exclusively with brain regions pre-selected for significant intergroup differences introduces severe small-sample instability and post-hoc circularity (double dipping).

* **Sham acupuncture blinding and physiological inertness control: [Fragile].**  
  The SA protocol uses penetrating needles ($2.5\text{--}7.5\text{ mm}$ depth) at four bilateral upper/lower-extremity non-acupoints (`NP-1` to `NP-4`), whereas the RA group receives cranial needling at `GV20` and `GV24` (scalp) plus three lower-extremity points (`KI3`, `KI4`, `SP6`). Because SA omits cranial needling entirely while penetrating the skin on the arms, patients can visually and somatically distinguish cranial vs. brachial needling, threatening participant blinding.

---

## 3. Forensic Defect Inventory

### 1. Retrospective Past-Tense Artifacts in a Prospective Protocol (Pillar 3 & Pillar 7)
* **Defect:** Although the manuscript is a prospective study protocol ("will enroll 60 patients"), multiple passages switch into past tense as if the trial and data imputation were already executed or pasted from a completed trial report:
  * Section `Withdrawal Criteria`: *"Participants demonstrating poor compliance or voluntarily withdrawing during treatment were also excluded. Those combining treatments prohibited by the protocol or failing to adhere to medical advice were likewise ineligible."*
  * Section `Outcome Measures`: *"Table 4 provides detailed information about the time points at which outcome assessments were conducted."*
  * Section `Clinical Data Analysis`: *"Data missing due to participant attrition was imputed utilizing the multivariate imputation by chained equations (MICE) method within the R Project for Statistical Computing (version 4.2.1)..."*
  * Section `Discussion`: *"Potential confounding factors... were controlled using mixed-effects models and further evaluated through sensitivity analyses."* (Notably, mixed-effects models are never mentioned in the `Statistical Analysis` section).
* **Actionable Fix:** Clarify whether enrollment and analysis have already occurred; if the trial is ongoing/prospective, harmonize all methods to prospective tense and align the `Discussion` with the actual models specified in `Statistical Analysis`.

### 2. Internal Contradictions in Needling Depth, Practitioner Qualifications, and Table Cross-References (Pillar 7)
* **Defect:**
  1. **Needling Depth:** `Table 1` (Item 2c) states that the depth of insertion for Real Acupuncture is *"From 15 to 25 mm."* However, `Table 3` specifies subcutaneous insertion of *"6–10 mm"* for `GV24 (Shenting)` and *"10–15 mm"* for `GV20 (Baihui)`.
  2. **Practitioner Experience:** Section `Intervention` states that treatments will be performed by an acupuncturist with *"more than 5 years of experience"*, whereas `Table 1` (Item 5) and `Table 2` (Item 5a) specify *"at least 6 years"* and *"more than 6 years of experience"*.
  3. **Broken Table Reference & Blinding Disclosure:** `Table 2` (Item 3a) refers to *"4 non-acupoints (Table 4 and Figure 3)"*, whereas `Table 4` is the SPIRIT schedule of assessments (acupoint locations are in `Table 3`). Furthermore, `Table 2` Item 6a states *"participants will be informed that they will be allocated to the acupuncture group or sham acupuncture group"*, directly contradicting Item 6b and Section `Randomization and Blinding`, which state that participants will be told they are receiving *"one of two effective interventions"* without mentioning "sham".
* **Actionable Fix:** Reconcile `Table 1` Item 2c to read `6–20 mm (point-dependent; see Table 3)`, unify practitioner experience requirements across text and tables, correct the `Table 4` typo in `Table 2` Item 3a to `Table 3`, and correct `Table 2` Item 6a to match the blinded consent script.

### 3. Unstratified Multicenter Randomization and Unadjusted Clinical Endpoint Testing (Pillar 3 & Pillar 4)
* **Defect:** Participants are recruited across five distinct hospitals in Chengdu, yet randomization (`R` v4.1.2) is unstratified by site. With $N = 60$ across 5 sites ($\sim 12$ patients/site), unstratified simple randomization can easily produce severe site imbalances between RA and SA. Furthermore, analyzing the primary outcome (change in ADAS-Cog) with unadjusted two-sample $t$-tests or Mann–Whitney $U$-tests ignores baseline ADAS-Cog covariance and hospital clustering.
* **Actionable Fix:** Implement block randomization stratified by study site, and specify a linear mixed-effects model (or ANCOVA) with baseline ADAS-Cog, age, sex, education, and site (random intercept or fixed effect) as covariates, reporting point estimates and 95% confidence intervals alongside $p$-values.

### 4. Underpowered Sample Size Justification, SEM Overparameterization, and Circular Neuroimaging Correlations (Pillar 2, Pillar 4 & Pillar 5)
* **Defect:**
  1. Citing Desmond & Glover (2002) single-voxel task-activation power curves ($n = 12\text{--}24$) does not establish power for a two-group longitudinal resting-state EEG-fMRI interaction ($\text{Group} \times \text{Time}$) or for the primary clinical outcome (ADAS-Cog).
  2. Section `Efficacy-Brain Network Correlation Analysis` proposes Structural Equation Modeling (SEM) and correlations restricted to *"parameter estimates of brain regions exhibiting significant intergroup differences"*. Fitting SEM on $n = 24\text{--}30$ completers per group fails minimum sample-to-parameter requirements for covariance structure modeling, and selecting ROIs based on post-treatment group differences (`RA vs. SA`) before correlating with clinical change inflates effect sizes via selection bias.
  3. Section `Data Analysis` lists five overlapping neuroimaging suites (`DPARSF` in MATLAB 2017b, `FSL`, `AFNI`, `MELODIC`, and `Brainstorm 3.0`) and vague multiple-testing corrections (*"Gaussian random field (GRF) theory, false discovery rate (FDR) control, and the like"*) without pre-specifying primary frequency bands, jICA component counts, or exact cluster-forming thresholds.
* **Actionable Fix:** Provide an explicit power calculation for the primary clinical endpoint (ADAS-Cog group-by-time interaction) and the minimum detectable effect size (Cohen's $d$) for $n = 24$ completers per arm; replace SEM with pre-specified linear regression or partial correlation on a priori anatomical/network ROIs (e.g., hippocampus, DMN, salience network); and lock a single reproducible preprocessing and jICA software pipeline with exact cluster-forming ($p < 0.001$) and FWE/FDR ($q < 0.05$) thresholds.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.4** | **3.5** | Unstratified randomization across 5 hospitals; no power calculation for the primary clinical endpoint (ADAS-Cog); unadjusted $t$-tests instead of baseline-adjusted ANCOVA/LMM; underpowered SEM ($n \le 30$/group) and circular post-hoc ROI selection; vague multi-software neuroimaging plan. |
| **2. Claim-to-Evidence Alignment** | **1.5** | **2.5** | Appropriately framed as a study protocol, but contains retrospective past-tense claims of completed MICE imputation and mixed-effects sensitivity analyses that are absent from the statistical methods. |
| **3. Data Integrity & Biological Plausibility** | **1.2** | **2.0** | Hardware-synchronized single-scanner EEG-fMRI acquisition is biologically and technically sound, but cranial + lower-limb real acupuncture vs. brachial + lower-limb penetrating sham acupuncture introduces somatic/topographical unblinding risk. |
| **4. Reproducibility & Data Integrity** | **1.0** | **2.0** | Trial registration (`ChiCTR2400084666`) and STRICTA/ACURATE tables are provided, but internal contradictions in needling depth (`15–25 mm` vs. `6–10 mm`), practitioner experience (`>5` vs. `≥6` years), and table cross-references (`Table 4` vs. `Table 3`) require correction. |
| **Scientific Core Score** | **4.1** | **8.0** | Sum of Rigor + Claims + Biology (`1.4 + 1.5 + 1.2`). |
| **Overall Composite Score** | **5.1** | **10.0** | **Mixed / Salvageable** (`1.4 + 1.5 + 1.2 + 1.0`). |
