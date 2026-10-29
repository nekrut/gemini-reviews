# Review of FEXP_ANON_130

**Overall Score:** **4.0 / 10.0** (Flawed / Overstated)
* **Score Breakdown:** Rigor: 1.1/3.5 | Claims: 1.0/2.5 | Biology: 1.1/2.0 | Reproducibility: 0.8/2.0
* **Scientific Core Score:** **3.2 / 8.0**

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_130`
* **Perceived Study Type:** Case-control observational resting-state fMRI study ($n = 23$ patients with acute toothache [TA] vs. $n = 30$ healthy controls [HC]).
* **Domain & Focus:** Pain neuroimaging and resting-state functional connectivity (75-component group Independent Component Analysis [ICA], voxel-wise intra-network functional connectivity [FC], inter-network Granger Causality Analysis [GCA], and clinical scale correlations with VAS, HAMA, and HAMD).

---

## 2. Executive Summary & Editorial Verdict

This study compares resting-state fMRI data from 23 patients with acute odontogenic toothache (duration $< 7$ days; 2 excluded from 25 enrolled due to head motion) and 30 matched healthy controls using 75-component group ICA (`GIFT`), voxel-wise intra-network two-sample $t$-tests across 14 template-matched resting-state networks (RSNs), autoregressive Granger Causality Analysis (GCA) between RSN time courses, and Spearman correlations with pain (VAS), anxiety (HAMA), and depression (HAMD) scores.

**Editorial Verdict:** **Reject / Fundamentally Flawed Without Complete Re-Analysis.** The manuscript contains a mathematically impossible correlation coefficient ($r = -4.93, p = 0.017$) reported in both the Abstract and Results text, relies on an automated template-matching procedure that accepted ICA components with near-zero spatial correlation to canonical RSN templates (e.g., $r = 0.148$ for the basal ganglia network and $r = 0.271$ for the language network), applies voxel-level Gaussian Random Field (GRF) cluster correction at an anti-conservative primary threshold ($p < 0.01$ across 14 separate network masks without family-wise correction across networks), and infers directed neural "information flow" from slow ($TR = 2.0\text{ s}$) hemodynamic signals via autoregressive GCA without accounting for regional hemodynamic response function (HRF) latency differences. Extensive production and translation corruptions (uncompiled raw LaTeX preamble code in the text, "anterior protrusion network" for anterior salience network, "Leigh hand" for handedness) further compromise technical reliability.

### Assessment of Specific Conclusions & Support

* **Reduced right precuneus FC correlates negatively with pain intensity (VAS), anxiety (HAMA), and depression (HAMD): [Methodologically Flawed].**  
  Both the Abstract and Section `Analysis of Correlations` report a Spearman correlation of $r = -4.93$ ($p = 0.017$) between right precuneus FC and VAS scores, which violates the mathematical bounds of a correlation coefficient ($r \in [-1, +1]$). Furthermore, the right precuneus cluster was pre-selected because it showed a group difference between TA and HC ($T = -4.33$), and the manuscript fails to specify whether the HAMA ($r = -0.46, p = 0.027$) and HAMD ($r = -0.563, p < 0.01$) correlations were computed strictly within the TA group ($n = 23$) or pooled across TA and HC (which creates a spurious two-cluster correlation since TA and HC differ strongly on both precuneus FC and HAMA/HAMD [$p < 0.001$]).

* **Patients with toothache exhibit intra-network FC increases in the anterior salience network (left superior temporal gyrus) and auditory network (right Rolandic operculum) and decreases in the precuneus network: [Fragile].**  
  Voxel-wise group comparisons were performed separately across 14 RSN masks using two-sample $t$-tests thresholded at voxel-level $p < 0.01$ and cluster-level $p < 0.05$ (GRF-corrected). Parametric GRF cluster inference at a primary cluster-forming threshold of $p < 0.01$ is known to produce severely inflated false-positive rates, and no multiple-testing correction was applied across the 14 separate network masks tested.

* **Increased directed causal information flow from the language network to the precuneus network in toothache patients: [Methodologically Flawed].**  
  First, the "language network" component (`IC 47`) had a spatial template correlation of only $r = 0.271$ (and the "precuneus network" `IC 24` had $r = 0.303$), indicating poor spatial correspondence with canonical networks. Second, applying autoregressive GCA to resting-state BOLD time series sampled at $TR = 2.0\text{ s}$ conflates neural directionality with regional differences in neurovascular coupling and HRF time-to-peak across cortical territories. Third, the GCA coefficient showed no correlation with any clinical symptom scale (VAS, HAMA, HAMD).

---

## 3. Forensic Defect Inventory

### 1. Mathematically Impossible Correlation Coefficient ($r = -4.93$) and Ambiguous Group Pooling (Pillar 4 & Pillar 7)
* **Defect:** In both the `Abstract` (line 9) and Section `Analysis of Correlations` (line 125), the Spearman correlation between right precuneus FC and VAS is reported as `r = −4.93, p = 0.017`. Because Spearman's $\rho$ is bounded in $[-1, +1]$, $r = -4.93$ is mathematically impossible (likely a decimal-point transcription error for $r = -0.493$, which yields $t = -2.596, p = 0.0169$ for $n = 23$). In addition, Section `Statistical Analysis` states that FC differences were correlated with VAS, HAMA, and HAMD controlling for age and sex (partial correlation), whereas the `Results` state `Spearman correlation analysis` without specifying whether HAMA/HAMD correlations were restricted to the $n = 23$ TA patients or pooled across $N = 53$ participants.
* **Actionable Fix:** Correct the correlation value ($r = -0.493$), clarify whether age- and sex-adjusted partial Spearman correlations were computed strictly within the TA cohort ($n = 23$), and apply false discovery rate (FDR) correction across all tested brain-region $\times$ clinical-scale pairs (3 clusters $\times$ 3 scales = 9 tests).

### 2. Unvalidated Low-Correlation ICA Components Used as Canonical Networks (Pillar 3)
* **Defect:** In Section `Group Independent Component Analysis (ICA)` and `Spatial Distribution and Correlation Coefficients of RSNs`, 14 components from a 75-component decomposition were selected via maximum spatial correlation with Shirer et al. templates. However, several retained components had negligible spatial correlation with the template: basal ganglia network (`IC 44`, $r = 0.148$), language network (`IC 47`, $r = 0.271$), left executive control network (`IC 37`, $r = 0.294$), and precuneus network (`IC 24`, $r = 0.303$). A spatial correlation of $0.148\text{--}0.271$ does not establish valid network identity.
* **Actionable Fix:** Apply a minimum spatial overlap threshold (e.g., $r \ge 0.40$ or Dice coefficient validation) accompanied by visual anatomical verification, or compute seed/ROI connectivity directly within the validated Shirer et al. functional parcels rather than poorly matched ICA components.

### 3. Anti-Conservative Voxel-Level GRF Thresholding Across 14 Networks Without Family-Wise Correction (Pillar 4 & Pillar 5)
* **Defect:** Two-sample $t$-tests were run across 14 RSN masks using GRF correction at voxel $p < 0.01$ and cluster $p < 0.05$. At voxel $p < 0.01$ with 8-mm FWHM smoothing, spatial autocorrelation violates GRF Gaussianity assumptions, and testing 14 independent network masks at $\alpha = 0.05$ without Bonferroni/FDR adjustment yields an expected family-wise false-positive rate $> 50\%$ under the global null. Furthermore, the mask construction (`concurrent sets were then taken as the total mask`, i.e., intersection vs. union of one-sample $t$-tests) is ambiguously defined.
* **Actionable Fix:** Re-run the group comparisons using non-parametric permutation testing (` randomise ` / `PALM` with 5,000 permutations and TFCE or cluster-forming $p < 0.001$) and correct for multiple comparisons across all 14 networks.

### 4. Hemodynamic Confounding of Granger Causality Analysis on 2.0-s TR BOLD Data (Pillar 3 & Pillar 6)
* **Defect:** Autoregressive GCA was applied to $TR = 2.0\text{ s}$ resting-state BOLD time courses across $14 \times 13 = 182$ directed RSN pairs. Because the sluggish hemodynamic response varies in onset and time-to-peak by $0.5\text{--}2.5\text{ s}$ across brain regions (especially between perisylvian/insular cortex and medial parietal precuneus), lag-based autoregressive prediction on unfiltered or low-pass BOLD signals reflects vascular latency differences rather than directed neuronal signaling. Moreover, the `Figure 3` caption misdescribes the color bar as *"the spectrum (0–0.25 Hz) of blood oxygenation levels"* when time-domain GCA outputs autoregressive causal coefficients, not frequency spectra.
* **Actionable Fix:** Either perform blind hemodynamic deconvolution prior to connectivity estimation or reframe the GCA result strictly as lagged hemodynamic predictability rather than causal neural information flow, and correct the `Figure 3` legend.

### 5. Severe Editorial, Translation, and LaTeX Compilation Corruptions (Pillar 7)
* **Defect:**
  1. `Abstract` (line 9): Refers to the anterior salience network (`aSN`) as the *"anterior protrusion network"* (a literal machine mistranslation of Chinese *突显网络* [salience network]) and alternates between *"language network"* and *"verbal network"*.
  2. `Section Statistical Analysis` (line 69): Contains raw uncompiled LaTeX header code pasted directly into the prose: `\documentclass[12pt]{minimal} \usepackage{wasysym}... \begin{document} $\overline x\pm {{\rm s}}$\end{document}`.
  3. `Table 1` (line 83–85): Lists handedness as *"Leigh hand (right/Left)"*; additionally, the independent $t$-test for Age (`26.96 ± 3.72` vs. `28.33 ± 4.07` for $n_1 = 23, n_2 = 30$) gives $t = 1.26, p = 0.21$, whereas `Table 1` reports `t = 1.60, P = 0.21`.
  4. `Figure 2` and `Figure 4` captions: `Figure 2` states *"inter-network FC differences"* when the analysis is *intra-network* FC (`Table 2`); `Figure 4` states *"functional correctional values"* instead of *"functional connectivity values"*.
  5. `Data Acquisition` (line 42): Reports acquisition matrix units as `256×256 mm` and `64×64 mm` (matrix dimensions are dimensionless pixels/voxels, not millimeters).
* **Actionable Fix:** Clean up all machine-translation errors, remove raw LaTeX preamble strings, recompute the age $t$-statistic ($t = 1.26$), and fix all figure captions and matrix units.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.1** | **3.5** | Mathematically impossible correlation ($r = -4.93$); liberal GRF thresholding ($p < 0.01$) across 14 networks without cross-network correction; ICA template matching accepting $r = 0.148\text{--}0.271$; unvalidated GCA on $2.0\text{ s}$ TR BOLD. |
| **2. Claim-to-Evidence Alignment** | **1.0** | **2.5** | Claims of directed neural information flow from language to precuneus network and compensatory cognitive-emotional reorganization overreach the cross-sectional, unvalidated ICA/GCA findings. |
| **3. Data Integrity & Biological Plausibility** | **1.1** | **2.0** | Acute odontogenic pain cohort ($n = 23$) and matched controls ($n = 30$) are clinically reasonable, but laterality of toothache (left vs. right dental quadrants) was not controlled despite reporting lateralized cortical effects. |
| **4. Reproducibility & Data Integrity** | **0.8** | **2.0** | Raw LaTeX code in text, mistranslated network names ("anterior protrusion network", "Leigh hand"), $r = -4.93$ error, mismatched $t$-value in Table 1, and data available only upon email request with no code repository. |
| **Scientific Core Score** | **3.2** | **8.0** | Sum of Rigor + Claims + Biology (`1.1 + 1.0 + 1.1`). |
| **Overall Composite Score** | **4.0** | **10.0** | **Flawed / Overstated** (`1.1 + 1.0 + 1.1 + 0.8`). |
