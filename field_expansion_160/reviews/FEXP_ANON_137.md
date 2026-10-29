# Review of FEXP_ANON_137

**Overall Score:** **7.6 / 10.0** (Strong / Sound)
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 1.9/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.5/2.0
* **Scientific Core Score:** **6.1 / 8.0**

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_137`
* **Perceived Study Type:** Prospective multi-center observational neuroimaging and longitudinal neurocognitive cohort study (TRACK-TBI; $N = 265$ Siemens discovery cohort [$n = 216$ acute mild traumatic brain injury (mTBI), $n = 49$ orthopedic trauma controls], replicated in $N = 155$ GE and $N = 166$ Philips cohorts).
* **Domain & Focus:** Clinical neurotrauma and connectomics (whole-brain voxel-to-voxel functional connectivity multivariate pattern analysis [fc-MVPA] in `CONN` 22.a at 2 weeks and 6 months post-injury, post-hoc seed-to-voxel mapping, and linear mixed-effects modeling of 2-week, 6-month, and 12-month cognitive recovery trajectories).

---

## 2. Executive Summary & Editorial Verdict

This study leverages the multi-center TRACK-TBI cohort (available via the controlled-access NIH FITBIR repository) to investigate whole-brain functional connectivity alterations at 2 weeks and 6 months post-mTBI relative to orthopedic trauma controls using unbiased voxel-to-voxel functional connectivity multivariate pattern analysis (`fc-MVPA`, 20 group-level SVD eigenpatterns, cluster-forming $p < 0.001$, cluster-level $p_{\text{FWE/FDR}} < 0.05$). To avoid cross-vendor harmonization artifacts, the authors analyze the Siemens 3T Trio subsample ($n = 216$ mTBI, $n = 49$ orthopedic controls across 7 sites) as the discovery dataset and replicate the primary fc-MVPA analysis in independent GE ($n = 155$) and Philips ($n = 166$) scanner cohorts, controlling for age, sex, education, household income, site, and mean framewise displacement (FD). They identify 8 significant fc-MVPA clusters at 2 weeks (with paracingulate/DMN, superior frontal/FPN, and occipital/VIS clusters replicating across scanner vendors), report no significant group-by-time connectome changes between 2 weeks and 6 months, and use linear mixed-effects models to link 2-week post-hoc seed connectivity with 12-month Trail Making Test (TMT-A and TMT-B) recovery slopes.

**Editorial Verdict:** **Accept with Minor Revisions.** The study design—featuring orthopedic trauma controls, multi-vendor replication cohorts, unbiased whole-brain fc-MVPA, and explicit adjustment for demographic, site, and head-motion covariates—is methodologically strong. However, several textual and tabular inconsistencies must be corrected prior to publication: (1) the `Abstract` contradicts the `Results`, `Figure 4`, and `Discussion` regarding the direction of frontal pole–anterior cingulate connectivity associated with better TMT-B recovery (stating *"hypoconnectivity"* in the Abstract, whereas `Figure 4` and the `Discussion` show that higher positive connectivity [`+1SD` above the mean / less anti-correlation] predicted steeper TMT-B improvement); (2) `Table 2` contains a typesetting corruption where the comma between numerator and denominator degrees of freedom was stripped (`(1243)` instead of `(1, 243)`); (3) a confidence interval bound in the `Results` text has a sign typo (`CI = 5.676, −22.295`); and (4) `Table 3` reports parametric $p_{\text{FDR}}$ values from post-hoc seed-to-voxel tests on clusters already selected via fc-MVPA in the same sample without flagging that those post-hoc $p$-values are conditioned on the first-stage selection.

### Assessment of Specific Conclusions & Support

* **Subacute mTBI (2 weeks post-injury) is associated with reproducible whole-brain connectome alterations in the paracingulate/superior frontal cortex (DMN/FPN) and occipital cortex (VIS) relative to orthopedic controls: [Well Supported].**  
  The primary omnibus `fc-MVPA` analysis ($p < 0.001$ voxel, $p < 0.05$ cluster-corrected, adjusting for age, sex, education, income, site, and mean FD) identified 8 clusters in the Siemens discovery sample ($N = 265$), with anatomical convergence in the paracingulate gyrus, superior frontal gyrus, and occipital cortex across the independent GE ($N = 155$) and Philips ($N = 166$) replication samples.

* **No significant group-level longitudinal whole-brain connectivity changes occur between 2 weeks and 6 months post-injury: [Well Supported].**  
  The authors transparently report the null longitudinal fc-MVPA interaction from 2 weeks to 6 months and appropriately discuss test–retest reliability and individual recovery heterogeneity.

* **Two-week functional connectivity between FPN–VIS, cerebellum–SMN, and frontal pole–ACC interacts with time to predict 12-month visual-motor (TMT-A) and executive (TMT-B) trajectories in mTBI: [Moderately Supported].**  
  Linear mixed-effects models with participant-specific random intercepts and slopes and FDR correction across cognitive tests support the $\text{FC} \times \text{Time}$ interactions on TMT-A and TMT-B. However, as noted in the `Discussion`, patients with `+1SD` frontal pole–ACC connectivity had *worse* baseline (2-week) TMT-B scores that converged toward the group mean by 12 months (`Figure 4`), meaning the steeper improvement slope partially reflects recovery from greater acute impairment (or regression to the mean) rather than superior absolute 12-month cognitive performance.

* **Post-hoc seed-to-voxel cluster significance ($p_{\text{FDR}} = 0.000000$ in `Table 3`): [Overstated].**  
  Although the `Limitations` section correctly notes that statistical inference must rest on the initial fc-MVPA model because post-hoc seed-to-voxel maps use seeds defined by the same group contrast, `Table 3` still presents unadjusted parametric cluster $p_{\text{FDR}}$ values as if they were independent confirmatory tests.

---

## 3. Forensic Defect Inventory

### 1. Contradiction Between `Abstract` and `Results`/`Figure 4`/`Discussion` on Frontal Pole–ACC Connectivity Direction (Pillar 1 & Pillar 7)
* **Defect:** In the `Abstract` (line 5), the authors write: *"Additionally, **hypoconnectivity** between the frontal pole (LIM) and anterior cingulate gyrus (salience network [SAL]) was associated with better executive functions performance measured by TMT-B over 12 months post-mTBI."* Conversely, `Figure 4` (line 162) states: ***"Less anti-correlation at two weeks post injury between these two regions (+1SD FC z-score above the mean) was associated with a greater improvement in TMT-B"***, and the `Discussion` (lines 1, 17, 19) explicitly states: ***"Higher positive connectivity (hyperconnectivity compared to controls) between the right frontal pole and the anterior cingulate cortex was associated with greater improvement in executive set shifting abilities over 12 months."*** Similarly, for inferior temporal–occipital pole (`FPN–VIS`), the `Abstract` says *"increased anticorrelation"* was associated with better TMT-A, whereas `Discussion` (line 1) says *"Higher positive connectivity (hyperconnectivity compared to controls) between the inferior temporal gyrus and bilateral occipital gyrus was associated with greater improvement in visuo-motor skills"* (`+1SD` slope $\beta = -3.76\text{ s}$ faster completion time vs. `-1SD` $\beta = -0.98\text{ s}$ in `Figure 3A`).
* **Actionable Fix:** Reconcile the `Abstract` with `Figures 3–4` and the `Discussion` so that `+1SD` vs. `-1SD` connectivity and completion-time reductions on TMT-A/B (where lower seconds = better performance) are described with consistent polarity throughout the manuscript.

### 2. Typesetting Corruption of Degrees of Freedom in `Table 2` and Confidence Interval Sign Typo in `Results` (Pillar 7)
* **Defect:**
  1. In `Table 2` (lines 74–88, `TRACK-TBI cognitive assessment (Siemens sub-sample)`, $N = 265$), the `df` column for the ANCOVAs reports `(1243)`, `(1238)`, `(1187)`, `(1236)`, `(1186)`, `(1241)`, `(1239)`, `(1184)`. Because the Siemens subsample has $N = 265$ participants at 2 weeks (with slight attrition at 6 and 12 months), these are clearly **`(1, 243)`**, **`(1, 238)`**, **`(1, 187)`**, etc., from which the comma separating numerator $df_1 = 1$ and denominator $df_2$ was accidentally deleted!
  2. In `Results` (line 152), the 95% confidence interval for the cerebellum–superior parietal interaction ($\beta = 13.98, p_{\text{FDR}} = 0.002$) is printed as `CI = 5.676, −22.295` (the upper limit should be `+22.295`, not `−22.295`).
  3. In `Methods` (line 68), the authors write: *"Model assumptions were checked using Q–Q residual versus fitted plots to assume dichotomy of outcome variables"* ("dichotomy" is a malapropism for *normality and homoscedasticity* of continuous cognitive scores), and report `RStudio Version 1.7` (an invalid version number) and `Cooke's distance` (typo for *Cook's distance*).
  4. In `Abstract` (line 5) and `Results` (line 97), family-wise error is misspelled as `FEW cluster-level p < 0.05` instead of `FWE`.
* **Actionable Fix:** Restore the commas in `Table 2` (`(1, 243)`, etc.), change `−22.295` to `22.295` in line 152, replace "dichotomy of outcome variables" with "normality and homoscedasticity of residuals", and fix `FEW` $\to$ `FWE` and `Cooke's` $\to$ `Cook's`.

### 3. Sample Size Discrepancies Across Text for GE and Philips Replication Cohorts (Pillar 7)
* **Defect:**
  * For the **GE** replication sample: `Abstract` (line 5) says $n = 165$, `fMRI Acquisition` (line 51) says $125\text{ mTBI} + 29\text{ controls} = \mathbf{154}$, and `Results` (line 97) says $n = 155$.
  * For the **Philips** replication sample: `Abstract` (line 5) says $n = 155$, whereas `fMRI Acquisition` (line 51) and `Results` (line 97) say $149\text{ mTBI} + 17\text{ controls} = \mathbf{166}$.
  * For the **Siemens** discovery sample: `Abstract` says *"18 and 83 years old"*, whereas `Results` (line 92) says *"aged 17–83 years"*; `Participants` (line 31) says MRI within *"10–18 days"*, whereas `fMRI Acquisition` (line 51) says *"5–18 days"*.
* **Actionable Fix:** Harmonize the exact participant counts for the GE ($n = 154$ or $155$) and Philips ($n = 166$) replication cohorts and the age/day ranges across the `Abstract`, `Methods`, and `Results`.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.5** | **3.5** | Strong whole-brain `fc-MVPA` discovery + 2-scanner replication design with orthopedic controls and comprehensive covariate adjustment (age, sex, education, income, site, mean FD); minor deduction for presenting post-hoc seed-to-voxel $p_{\text{FDR}}$ values in `Table 3` without adjusting for first-stage MVPA selection. |
| **2. Claim-to-Evidence Alignment** | **1.9** | **2.5** | Well-calibrated discussion of heterogeneity, null 6-month longitudinal connectome findings, and baseline impairment vs. recovery slope; minor deduction for the `Abstract` polarity contradiction ("hypoconnectivity" vs. "hyperconnectivity"). |
| **3. Data Integrity & Biological Plausibility** | **1.7** | **2.0** | Prospective multi-center level-1 trauma cohort with orthopedic controls and vendor-stratified analysis avoids cross-scanner batch confounding. |
| **4. Reproducibility & Data Integrity** | **1.5** | **2.0** | Controlled-access NIH FITBIR data availability (full credit per rubric) and detailed `CONN` 22.a parameters, but deductions for `Table 2` `df` comma stripping (`(1243)`), CI sign typo (`−22.295`), and GE/Philips $n$ discrepancies between Abstract and text. |
| **Scientific Core Score** | **6.1** | **8.0** | Sum of Rigor + Claims + Biology (`2.5 + 1.9 + 1.7`). |
| **Overall Composite Score** | **7.6** | **10.0** | **Strong / Sound** (`2.5 + 1.9 + 1.7 + 1.5`). |
