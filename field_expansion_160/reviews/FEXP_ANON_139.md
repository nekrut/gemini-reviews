# Review of FEXP_ANON_139

**Overall Score:** **2.7 / 10.0** (Fundamentally Invalid)
* **Score Breakdown:** Rigor: 0.7/3.5 | Claims: 0.7/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.5/2.0
* **Scientific Core Score:** **2.2 / 8.0**

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_139`
* **Perceived Study Type:** Single-center observational cohort/case-control study ($N$ stated as both 131 and 149: 73 ICU patients with PCR-confirmed Herpes Simplex Encephalitis [HSE] and 76 [or 58] cognitively unimpaired controls).
* **Domain & Focus:** Neuroinfectious disease and multimodal neuroimaging (FSL Voxel-Based Morphometry [VBM], seed-based resting-state fMRI functional connectivity, Montreal Cognitive Assessment [MoCA], and CSF opening pressure, protein, and cytokines IL-1$\beta$, IL-2, IL-4, IL-5, IL-6, IL-10, IL-12).

---

## 2. Executive Summary & Editorial Verdict

This manuscript reports a single-center study of 73 ICU-admitted patients with acute PCR-confirmed Herpes Simplex Encephalitis (HSE) and a group of cognitively unimpaired controls, examining grey matter volume (VBM), resting-state functional connectivity (FC), MoCA cognitive scores, and CSF pressure, protein, and inflammatory cytokines.

**Editorial Verdict:** **Reject (Fundamentally Invalid Due to Severe Data Integrity Discrepancies, Altered Denominators, and Implausible Statistical Results).** A forensic audit uncovers multiple irreconcilable numerical contradictions that indicate the control cohort denominator was changed without updating the underlying counts or test statistics, alongside statistically and biologically implausible correlation matrices:
1. **Smoking-Gun Sample Size and Demographic Table Manipulation (`n = 58` Altered to `n = 76`):**
   * In `Results` (line 84), the authors write: *"As summarized in Table 1, **131 participants** were enrolled (**76 controls and 73 with HSE**)."* Simple addition shows $76 + 73 = \mathbf{149}$, NOT $131$—whereas $131 - 73 = \mathbf{58}$!
   * Even more damningly, the `Results` text (duplicated almost verbatim twice in paragraph 1 of `Results`, line 84!) states that controls vs. HSE had a *"proportion of males (**75.86%** vs. 80.82%; p = 0.636), prevalence of hypertension (**34.48%** vs. 42.47%; p = 0.453)"*. Yet **`Table 1` (lines 91–92)** reports Controls ($n = 76$) as having **`44 (57.89%)`** males and **`20 (26.31%)`** with hypertension, while still listing the exact same $p$-values (`p = 0.636` and `p = 0.453`)!
   * Notice the exact arithmetic: $\frac{44}{58} = \mathbf{75.862\%}$ and $\frac{20}{58} = \mathbf{34.483\%}$, whereas $\frac{44}{76} = \mathbf{57.895\%}$ and $\frac{20}{76} = \mathbf{26.316\%}$! Furthermore, for $44/58$ vs. $59/73$, the continuity-corrected $\chi^2$ $p$-value is indeed $p = 0.636$ (and for $20/58$ vs. $31/73$, $p = 0.453$), whereas for `Table 1`'s $44/76$ vs. $59/73$, the true $\chi^2$ test is **highly significant ($\chi^2 = 9.17, p = 0.0025$, NOT $p = 0.636$)**! This proves beyond doubt that the control group size in `Table 1` was changed from $n = 58$ to $n = 76$ and the percentages (`44/76`, `20/76`) were recalculated by dividing the old $n = 58$ counts by $76$, while leaving the old counts (`44`, `20`), old $p$-values (`0.636`, `0.453`), and old text (`131 participants`, `75.86%`, `34.48%`) intact!
2. **Biologically and Statistically Implausible Pairwise Correlations ($r = 0.83\text{ to }0.96$ and $r = -0.89\text{ to }-0.76$) and Nonsensical `Env-cor` Composite Variable:** `Figure 2` claims pairwise Pearson correlations between acute ICU MoCA scores, CSF cytokines, VBM grey matter volumes, and rs-fMRI connectivity ranging from **$r = 0.83$ to $0.96$**, and `Figure 3` claims correlations between CSF pressure/protein and MRI metrics of **$r = -0.89$ to $-0.76$**! In human clinical neuroimaging, raw bivariate correlations of $0.83\text{--}0.96$ between CSF cytokines, structural VBM volumes, resting-state BOLD FC, and MoCA scores are virtually impossible and strongly suggest that predicted/fitted values from a regression model (or synthetic colinear variables) were correlated instead of raw measurements. Moreover, the authors state they adjusted for confounders in a 2-way Pearson correlation matrix by including `Env-cor` (*"a composite of age, gender, hypertension, fever"* included *"as a single variable in all pairwise analyses"*), which does not statistically control for covariates in pairwise correlations between other variables.
3. **Seed-Region Contradiction Between `Methods` and `Results`:** `Methods` (line 67) explicitly defines three VBM-derived seeds: **right hippocampal gyrus**, left precuneus, and left posterior cingulate gyrus. Yet the `Abstract`, `Results` (line 114), and `Figure 1B` report enhanced FC for the **left hippocampus (`Hip_L`)**—a region that was never defined as a seed—and report nothing for the right hippocampal seed!

### Assessment of Specific Conclusions & Support

* **Baseline demographic comparability between HSE ($n = 73$) and controls ($n = 76$): [Methodologically Flawed].**  
  Invalidated by the arithmetic discrepancy between $N = 131$ (`58 + 73`) and $N = 149$ (`76 + 73`), where `Table 1` divides the counts for $n = 58$ controls (`44` males, `20` hypertensive) by $76$ to get `57.89%` and `26.31%` while retaining the $p$-values ($0.636$ and $0.453$) from $n = 58$ and reporting `75.86%` and `34.48%` in the text.

* **HSE patients exhibit reduced VBM grey matter volume in the right hippocampal gyrus, left precuneus, and left posterior cingulate gyrus, and enhanced left hippocampal–mPFC functional connectivity: [Methodologically Flawed].**  
  The seed-based FC analysis is internally inconsistent: `Methods` (line 67) specifies that seeds were 6-mm spheres centered on the three VBM peaks (**right** hippocampal gyrus, left precuneus, left posterior cingulate gyrus), yet `Results` (line 114) and `Figure 1B` report FC results for the **left** hippocampus (`Hip_L`). Additionally, `Methods` contradicts itself on fMRI voxel resolution (`2 × 2 × 2 mm` in line 57 vs. `3 mm isotropic voxel size` in line 67).

* **Cerebral VBM/FC metrics correlate with MoCA and CSF cytokines at $r = 0.83\text{--}0.96$ and CSF pressure/protein at $r = -0.89\text{ to }-0.76$, with IL-6 moderation: [Methodologically Flawed].**  
  Pairwise Pearson correlations of $0.83\text{--}0.96$ across noisy cross-modal clinical, biochemical, and neuroimaging variables in acute ICU encephalitis patients are biologically implausible, and including a composite demographic variable (`Env-cor`, which includes `fever`—a variable that wasn't even measured in controls!) as an extra node in a 2-way Pearson correlation matrix does not adjust pairwise correlations for confounding.

---

## 3. Forensic Defect Inventory

### 1. Forensic Evidence of Altered Control Sample Size ($n = 58 \to 76$) and Corrupted `Table 1` Statistics (Pillar 2 & Pillar 7)
* **Defect:**
  * `Results` (line 84): *"131 participants were enrolled (76 controls and 73 with HSE)."* ($76 + 73 = 149 \ne 131$; $131 - 73 = 58$).
  * `Results` (line 84, repeated twice in the same paragraph): *"proportion of males (75.86% vs. 80.82%; p = 0.636), prevalence of hypertension (34.48% vs. 42.47%; p = 0.453)"*.
  * `Table 1` (lines 91–92): Lists Controls ($n = 76$) as `Males: 44 (57.89%)`, `p = 0.636`, and `Hypertension: 20 (26.31%)`, `p = 0.453`.
  * Mathematical proof: $44 / 58 = 75.86\%$ and $20 / 58 = 34.48\%$. When the header of `Table 1` was changed from $n = 58$ to $n = 76$, someone recomputed $44 / 76 = 57.89\%$ and $20 / 76 = 26.31\%$ without changing the numerators (`44`, `20`), the $\chi^2$ $p$-values (for $44/76$ vs. $59/73$, true $p = 0.0025 \ne 0.636$), or the main text!
* **Actionable Fix:** Provide the raw participant log and audit trail explaining whether 58 or 76 controls were scanned, recompute all demographic counts, percentages, and $\chi^2$ tests from the verified raw dataset, and remove the duplicated text block in `Results` paragraph 1.

### 2. Implausible Cross-Modal Correlations ($r = 0.83\text{--}0.96$) and Invalid `Env-cor` Confounder Adjustment (Pillar 3, Pillar 4 & Pillar 6)
* **Defect:**
  1. `Statistical analyses` (line 77) is duplicated almost word-for-word across two consecutive paragraphs (lines 75 and 77) and states: *"All correlations are pairwise (2-way) Pearson correlations between two variables... No 3-way or partial correlations are displayed. Env-cor is a composite covariate included as a single variable in all pairwise analyses."* Adding a composite variable (`Env-cor`) as an extra row/column in a 2-way correlation matrix does nothing to partial out age, sex, hypertension, or fever from the correlations between brain metrics, cytokines, and MoCA.
  2. `Figure 2` and `Figure 3` report pairwise correlation coefficients of $r = 0.83\text{--}0.96$ and $r = -0.89\text{ to }-0.76$ between CSF markers, MRI metrics, and MoCA. Furthermore, in `Figure 4`, the standardized interaction coefficients ($\beta$) for `IL-6 × cerebral metric` are plotted on an x-axis of `0–0.05` (extremely tiny standardized effects: $\beta < 0.05$), yet are reported as `p < 0.001 to p = 0.007` in a sample of only $n = 73$ patients! With $n = 73$, a standardized regression coefficient of $\beta < 0.05$ cannot achieve $p < 0.001$ ($t < 0.45$ under unit-variance standardization) unless the variables were unstandardized raw units (where IL-6 has mean $349.14$) mislabeled as "standardized $\beta$ coefficients"!
* **Actionable Fix:** Replace the 2-way correlation matrices (`Figures 2–3`) with genuine partial correlation matrices controlling for age, sex, education, hypertension, and fever; audit why raw correlations exceeded $0.83$ (verifying that raw data rather than model-predicted values were plotted); and clarify whether `Figure 4` plots unstandardized $B$ (per $\text{pg/mL}$ of IL-6) or standardized $\beta$.

### 3. Unexplained Switch from Right Hippocampal VBM Seed to Left Hippocampal FC Result and Voxel-Size Contradiction (Pillar 3 & Pillar 7)
* **Defect:**
  1. `Seed-based resting-state functional connectivity analysis` (line 67) states that three VBM peak seeds were tested: **right hippocampal gyrus**, left precuneus, and left posterior cingulate gyrus. Yet `Results` (line 114) and `Figure 1B` report FC for the **left hippocampus (`Hip_L`)** and never mention the right hippocampal gyrus seed.
  2. Line 57 states that fMRI data were resampled to `2 × 2 × 2 mm (Granerod et al., 2010) voxels` (attaching an epidemiological encephalitis reference to an SPM/CAT12 voxel-size parameter!), whereas line 67 states that `3D-ClustSim` minimum cluster size (20 voxels) was *"adjusted for our 3 mm isotropic voxel size"*.
* **Actionable Fix:** Reconcile why `Hip_L` appears in `Figure 1B` when the VBM peak and defined seed were in the right hippocampus, and clarify whether the preprocessed fMRI voxel size was $2\text{ mm}$ or $3\text{ mm}$ isotropic.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.7** | **3.5** | Invalid `Env-cor` pairwise correlation method that fails to partial out covariates; biologically/statistically implausible correlations ($r = 0.83\text{--}0.96$) and incompatible standardized $\beta < 0.05$ with $p < 0.001$ at $n = 73$; seed mismatch (`Right` VBM peak vs. `Left` hippocampus FC). |
| **2. Claim-to-Evidence Alignment** | **0.7** | **2.5** | Headline claims of tight coupling among CSF cytokines, VBM/FC, and acute ICU MoCA rest on internally inconsistent tables and implausible correlation matrices. |
| **3. Data Integrity & Biological Plausibility** | **0.8** | **2.0** | Direct arithmetic proof that the control denominator in `Table 1` was changed from $n = 58$ ($131 - 73$) to $n = 76$ while keeping the $n = 58$ numerators (`44`, `20`) and $p$-values (`0.636`, `0.453`); acute ICU MoCA in febrile encephalitic patients is heavily confounded by delirium/sedation. |
| **4. Reproducibility & Data Integrity** | **0.5** | **2.0** | Duplicated paragraphs in `Methods` (lines 75/77) and `Results` (line 84); $N = 131$ vs. $76 + 73 = 149$ contradiction; $2\text{ mm}$ vs. $3\text{ mm}$ voxel contradiction; misplaced citation on voxel dimensions. |
| **Scientific Core Score** | **2.2** | **8.0** | Sum of Rigor + Claims + Biology (`0.7 + 0.7 + 0.8`). |
| **Overall Composite Score** | **2.7** | **10.0** | **Fundamentally Invalid** (`0.7 + 0.7 + 0.8 + 0.5`). |
