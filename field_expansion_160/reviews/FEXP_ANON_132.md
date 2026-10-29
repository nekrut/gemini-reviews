# Review of FEXP_ANON_132

**Overall Score:** **5.6 / 10.0** (Mixed / Salvageable)
* **Score Breakdown:** Rigor: 1.6/3.5 | Claims: 1.4/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.2/2.0
* **Scientific Core Score:** **4.4 / 8.0**

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_132`
* **Perceived Study Type:** Simultaneous FDG-PET and resting-state fMRI case-control study (NCT01931995; $n = 21$ unmedicated Major Depressive Disorder [MDD] patients vs. $n = 21$ age-matched healthy controls).
* **Domain & Focus:** Molecular and systems psychiatry (coupling between whole-brain normalized regional glucose metabolism [WBn-SUV] and seed-based hemodynamic functional connectivity [FC] across canonical 17-network parcellations).

---

## 2. Executive Summary & Editorial Verdict

This study uses a simultaneous MR-PET scanner to acquire static 18F-FDG-PET (45–65 min post-injection) and resting-state BOLD fMRI ($3 \times 6\text{ min}$ runs) in 21 unmedicated young adults with MDD (18 medication-naïve in their first major depressive episode) and 21 rigorously screened healthy controls. Because no voxel-wise FDG-PET differences survived family-wise error (FWE) correction, the authors thresholded the between-group FDG-PET contrast at $p < 0.01$ (uncorrected, cluster size $> 10$ voxels) to define composite "hypermetabolic" and "hypometabolic" seed masks, and then compared the seed-based BOLD FC of those masks between the same 21 MDD and 21 control participants. They report that hypermetabolic seeds show increased FC—and hypometabolic seeds show decreased FC—with overlapping prefrontal regions of the salience network.

**Editorial Verdict:** **Major Revision Required.** Recruiting 21 unmedicated (18 treatment-naïve) MDD patients and imaging them with simultaneous FDG-PET/fMRI is a valuable empirical contribution. However, the analytical pipeline suffers from three fundamental statistical and mathematical vulnerabilities that undermine the headline convergence claim: (1) no voxel-wise FDG-PET clusters survived multiple-comparison correction, and the ROI-level WBn-SUV permutation test in the cingulo-opercular (CO) network ($p = 0.016$ uncorrected across 18 tested ROIs) also fails to survive false discovery rate (FDR) or Bonferroni correction ($p_{\text{Bonf}} = 0.288$); (2) defining composite seed masks from an uncorrected $p < 0.01$ between-group FDG-PET contrast and testing between-group FC in the *same* 42 subjects introduces in-sample selection conditioning; and (3) the striking "mirror-image" convergence—where hypermetabolic seeds show increased FC and hypometabolic seeds show decreased FC to the *exact same* prefrontal salience cluster (`Figure 5`)—is mathematically predisposed by combining whole-brain PET normalization (`WBn-SUV`) with fMRI **Global Signal Regression (GSR)**, which constrains whole-brain correlations to sum to zero and induces anti-correlated seed time courses between complementary brain partitions.

### Assessment of Specific Conclusions & Support

* **Unmedicated MDD patients exhibit statistically significant network-level glucose hypermetabolism in the cingulo-opercular (CO) network and hypometabolism in the default network: [Fragile].**  
  At the voxel level, zero FDG-PET clusters survived FWE correction ($p < 0.05$). At the network ROI level, the authors performed 18 parallel permutation tests (17 Yeo networks plus the sgACC ROI) and reported $\Delta\text{WBn-SUV} = +0.016$ ($p = 0.016$, uncorrected) for the CO network and $\Delta\text{WBn-SUV} = -0.022$ ($p = 0.055$, uncorrected) for Default Network C. Across 18 tests, $p = 0.016$ does not survive Benjamini–Hochberg FDR ($q = 0.288$) or Bonferroni correction.

* **Null difference in subgenual anterior cingulate cortex (sgACC) resting glucose metabolism between unmedicated MDD and controls: [Well Supported].**  
  Both the a priori 10-mm spherical right sgACC ROI ($\Delta\text{WBn-SUV} = -0.002, p = 0.92$) and voxel-wise maps showed no evidence of sgACC hypermetabolism, providing a useful null replication in young, largely first-episode unmedicated MDD patients.

* **Hypermetabolic regions show stronger FC, and hypometabolic regions show weaker FC, to identical prefrontal salience network regions in MDD: [Methodologically Flawed].**  
  First, the hypermetabolic and hypometabolic seed masks were defined post-hoc from the uncorrected ($p < 0.01$) group difference in the same 42 subjects. Second, because fMRI preprocessing regressed out the whole-brain global signal (GSR), the correlation of any voxel with the global mean is zero. When two large composite masks (hypermetabolic and hypometabolic regions) are constructed from opposite tails of the group contrast and global signal is regressed out, their mean BOLD time courses are mathematically pushed toward negative covariance, guaranteeing that any target cluster positively coupled to one mask in MDD > HC will tend to show inverted (negative) coupling to the complementary mask (`Figure 5`).

---

## 3. Forensic Defect Inventory

### 1. Mathematical Mirroring Artifact Induced by Global Signal Regression (GSR) and Whole-Brain SUV Normalization (Pillar 3 & Pillar 5)
* **Defect:** In `FDG-PET data analysis`, regional PET uptake is normalized by the whole-brain mean (`WBn-suv`), which centers the brain-wide metabolic difference distribution around zero. In `fMRI preprocessing`, the **whole-brain global signal** is regressed out of every voxel's BOLD time series. Under GSR, for any target voxel $v$, the volume-weighted sum of its covariance with all brain voxels equals zero. Consequently, two composite seed masks drawn from opposite tails of the group contrast map often exhibit anti-correlated or complementary fluctuations after GSR, artificially generating the mirror-image overlap in `Figure 5` (where red `Hypermetabolic FC increase` and blue `Hypometabolic FC decrease` maps are nearly identical sign inversions).
* **Actionable Fix:** Re-compute the seed-based FC group comparisons **without Global Signal Regression** (using `aCompCor` white-matter/CSF principal components instead of whole-brain GSR) and report the within-subject correlation between the hypermetabolic mask time course and hypometabolic mask time course before and after GSR.

### 2. Uncorrected Multiple Comparisons Across 18 FDG-PET Network ROIs and In-Sample Seed Selection (Pillar 4)
* **Defect:** The ROI bar plot (`Figure 2C`) tests 17 Yeo networks plus the sgACC ROI (18 tests) without multiple-testing correction, treating $p = 0.016$ as statistically significant. Furthermore, defining the composite FDG-PET seed masks at $p < 0.01$ uncorrected in the same $21\text{ vs. }21$ sample used for the FC $t$-tests (`3dttest++`) fails to separate ROI discovery from hypothesis testing; because local metabolic activity and local BOLD amplitude/synchrony are coupled within the same simultaneous MR-PET session, in-sample selection inflates Type I error.
* **Actionable Fix:** Report FDR-adjusted $q$-values across all 18 FDG-PET ROIs, and validate the FC findings using a leave-one-pair-out (or 5-fold) cross-validation scheme where the $p < 0.01$ FDG-PET hyper-/hypometabolic seed masks are defined on the training folds and FC is extracted on the held-out subjects, or use the a priori anatomical CO and Default Network templates (`Figure S1`) as the primary FWE-corrected seeds.

### 3. Subjective Post-Hoc Exclusion of Orbitofrontal FDG-PET Clusters as "Susceptibility Artifacts" and Filter Description Error (Pillar 2 & Pillar 7)
* **Defect:**
  1. Section `FC data analysis` (line 67) states: *"Two clusters located in the left and right lateral orbitofrontal cortex were excluded from calculations of the FC seeds because they appeared to reflect susceptibility artifacts (left cluster: x = −40.5, y = 30, z = −21; right cluster: x = 49.5, y = 30, z = −16.5)."* Magnetic susceptibility dropout at air–tissue interfaces is an MRI $T_2^*$-weighted EPI artifact, not an 18F-FDG positron emission artifact (unless caused by MR-based attenuation correction segmentation error in the sinus cavity, or excluded after inspecting the fMRI signal). Excluding two bilateral OFC clusters ad hoc without a quantitative temporal SNR (tSNR) threshold introduces researcher degrees of freedom.
  2. Section `fMRI preprocessing` (line 62) states: *"Additionally, data was low-pass filtered to exclude signals < 0.08 Hz."* A low-pass filter at $0.08\text{ Hz}$ **retains** frequencies $< 0.08\text{ Hz}$ and excludes frequencies $> 0.08\text{ Hz}$!
  3. The software stack cited (`FSL version 4.0.3`, released in 2008, and `MATLAB version 7.4.0 [R2007a]`, released in 2007) alongside `SPM12` and `AFNI 16.3.13` indicates a mixed legacy preprocessing pipeline.
* **Actionable Fix:** Specify the quantitative tSNR or attenuation-map criterion used to mask out the lateral OFC voxels, correct the filter description to *"low-pass filtered to retain signals < 0.08 Hz (excluding frequencies > 0.08 Hz)"*, and report the exact SPM12 cluster-extent threshold ($k$) used for FWE cluster correction in `Figures 3 and 4`.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.6** | **3.5** | Uncorrected FDG-PET voxel maps ($p < 0.01$) and unadjusted 18-ROI tests ($p = 0.016, q_{\text{FDR}} = 0.288$); in-sample seed selection; GSR + WBn-SUV mathematical mirroring artifact driving the primary convergence result. |
| **2. Claim-to-Evidence Alignment** | **1.4** | **2.5** | Limitations candidly note the uncorrected PET threshold and small sample ($n = 21$/group), but the Abstract and Conclusion present the CO/DMN metabolic changes and prefrontal salience convergence as established pathobiological signatures. |
| **3. Data Integrity & Biological Plausibility** | **1.4** | **2.0** | Strong clinical phenotyping (21 unmedicated MDD, 18 treatment-naïve first-episode) and matched FDG dose/uptake timing, though comorbid anxiety/OCD was permitted in the MDD group without covariate adjustment. |
| **4. Reproducibility & Data Integrity** | **1.2** | **2.0** | Trial registration (`NCT01931995`) and clear coordinate reporting, but data/code are available only "upon reasonable request", low-pass filter direction is misstated, and legacy software (`FSL 4.0.3`, `MATLAB 7.4.0`) is used. |
| **Scientific Core Score** | **4.4** | **8.0** | Sum of Rigor + Claims + Biology (`1.6 + 1.4 + 1.4`). |
| **Overall Composite Score** | **5.6** | **10.0** | **Mixed / Salvageable** (`1.6 + 1.4 + 1.4 + 1.2`). |
