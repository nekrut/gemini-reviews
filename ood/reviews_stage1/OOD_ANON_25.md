# Review of OOD_ANON_25

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.1 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.4/3.5 | Claims: 1.2/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.3/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study investigates resting-state functional connectivity (rs-fMRI) of the Salience Network (SN) in 29 adult males with Autism Spectrum Disorder (ASD) and 29 age-matched typically developing (TD) males from the Barrow Neurological Institute (BNI) site of the public ABIDE II repository. Using the CONN toolbox (v21.b), the authors perform (1) ROI-to-ROI connectivity (RRC) across seven SN nodes (anterior cingulate cortex [ACC] and bilateral anterior insula [AI], rostral prefrontal cortex [RPFC], and supramarginal gyrus [SMG]), and (2) whole-brain seed-based connectivity (SBC) from each of the seven SN seeds, testing between-group differences (ASD vs. TD), group-by-SRS-2 subscale interactions, and within-ASD regressions against ADOS-2 scores. While all RRC analyses are null, the SBC analyses report reduced RPFC–left cerebellum connectivity, increased right SMG–temporal/parietal connectivity, and several seed-to-cluster associations with SRS-2 and ADOS-2 subscales.

Although the dataset is publicly available and the preprocessing pipeline in CONN (CompCor denoising, ART scrubbing, motion regression) follows standard practice, the statistical inference and anatomical reporting suffer from major methodological weaknesses: (1) in the seed definition (Figure 1a caption, line 90), the MNI $x$-coordinates for all six lateralized seeds are inverted relative to their hemisphere labels (negative $x$-coordinates are labeled "Right" and positive $x$-coordinates are labeled "Left"); (2) the study executes 84 separate whole-brain voxelwise SBC searches (7 seeds $\times$ [1 group contrast + 6 SRS-2 scales + 5 ADOS-2 scales]) at a liberal cluster-forming threshold of $p < 0.005$ uncorrected without correcting for multiple comparisons across the 7 seeds or 11 clinical scales; (3) Tables 2–4 report peak-voxel correlation coefficients ($r = 0.49–0.87$, $r^2 = 0.24–0.75$) extracted from clusters selected for passing a whole-brain significance threshold, a classic circular "voodoo correlation" (selection bias) that severely inflates effect sizes; and (4) the sample has a bimodal age distribution with a 15-year gap (ages 18–25 and 40–64, with zero participants aged 26–39), yet age is not controlled for in the second-level GLMs. Re-analyzing the data with a stringent $p < 0.001$ cluster-forming threshold, seed-level multiple testing correction, age adjustment, and corrected hemisphere labels is required to determine which findings are robust.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Intra-network ROI-to-ROI functional connectivity within the Salience Network does not differ between ASD and TD adults or correlate with SRS-2/ADOS-2 scores: [Well Supported].**  
  The direct hypothesis test of connectivity among the seven core SN nodes (RRC analysis; lines 117, 137, 156) yielded no statistically significant differences between groups or associations with clinical scores. However, this null finding for the primary intra-SN hypothesis is downplayed in the Abstract and Discussion in favor of exploratory whole-brain seed-to-voxel results.

* **ASD adults exhibit reduced seed-based connectivity between bilateral RPFC and left cerebellum (Crus I / Lobule VI) and increased connectivity between right SMG and left aMTG / right AG: [Fragile].**  
  These four clusters (Table 2, cluster sizes 236–655 voxels) were identified using a cluster-forming voxel threshold of $p < 0.005$ uncorrected and cluster-size $p\text{-FDR} < 0.05$ without correcting across the 7 SN seeds tested. Parametric random-field cluster inference at $p < 0.005$ with 8 mm smoothing is known to yield inflated family-wise false-positive rates (Eklund et al., 2016), and the cluster $p$-values ($p = 0.001$ to $0.002$) are close to the Bonferroni-adjusted threshold across 7 seeds ($0.05 / 7 = 0.0071$). Furthermore, because the MNI $x$-coordinates of the left and right seeds are swapped in Figure 1a, it is ambiguous which hemisphere was actually seeded for `SMG-r`.

* **Salience Network seed connectivity shows strong correlations ($r = 0.63–0.87$, explaining $40\%–75\%$ of variance) with SRS-2 and ADOS-2 subscales in ASD: [Overstated].**  
  Testing 7 seeds across 6 SRS-2 scores (42 whole-brain interaction maps) and 5 ADOS-2 scores (35 whole-brain regression maps in $n = 29$ ASD subjects) without correcting across seeds or subscales guarantees false-positive clusters by chance. More importantly, reporting peak-voxel $r = 0.63–0.66$ in Table 3 and $r = 0.68–0.87$ ($r^2 = 0.47–0.75$) in Table 4 computes the correlation at the single most extreme voxel selected from a whole-brain search in $n = 29$ subjects. This post-selection circularity ("voodoo correlation") overestimates true brain-wide behavioral correlations in small rs-fMRI samples by several-fold.

* **Age-independent generalization of Salience Network connectivity alterations across adulthood in ASD: [Fragile].**  
  As reported in Methods (line 23), the BNI sample consists of two non-overlapping age strata: young adults aged 18–25 years ($n = 13$ ASD, $n = 10$ TD) and older adults aged 40–64 years ($n = 16$ ASD, $n = 19$ TD), with no participants between 26 and 39 years. Despite emphasizing in the Introduction (line 15) that SN connectivity in ASD is age-dependent, the second-level GLMs did not include age or age-cohort as a covariate, nor did they test for group-by-age-stratum interactions.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Verify and Correct Left/Right MNI Coordinate Labels for All Six Lateralized Seeds
* **WHY:** In standard MNI space, $x < 0$ is the left hemisphere and $x > 0$ is the right hemisphere. Yet the Figure 1a caption (line 90) lists negative $x$-coordinates for all three "Right" seeds (`right AI`: MNI $-44, 13, 1$; `right RPFC`: MNI $-32, 45, 27$; `right SMG`: MNI $-60, -39, 31$) and positive $x$-coordinates for all three "Left" seeds (`left AI`: MNI $47, 14, 0$; `left RPFC`: MNI $32, 46, 27$; `left SMG`: MNI $62, -35, 32$). Note that CONN's default `networks.Salience` atlas uses $(+47, 14, 0)$ for Right AI and $(-44, 13, 1)$ for Left AI.
* **WHAT:** Check the CONN project file to determine whether only the text in the Figure 1a caption was transposed, or whether the seed labels were swapped inside the CONN analysis itself (which would mean every result reported for `AI-r`, `RPFC-r`, and `SMG-r` in Tables 2–4 and the Discussion is actually from the **left** hemisphere, and vice versa).
* **HOW:** Inspect the ROI coordinates corresponding to `Seed Region` in the CONN second-level results directory and update Figure 1a, Tables 2–4, and all hemispheric interpretations in the Results and Discussion accordingly.

#### 2. Apply Stringent Cluster-Forming Thresholds ($p < 0.001$) and Correct Across All 7 Seeds and Behavioral Scales
* **WHY:** Conducting 84 whole-brain voxelwise analyses at an uncorrected cluster-forming threshold of $p < 0.005$ without adjusting for the 7 seeds or 11 clinical scales creates a severe multiple-testing problem. Additionally, Methods line 101 states that RRC analyses used "cluster formation threshold $p < 0.05$ at the voxel level," which is a voxelwise description inapplicable to an ROI-to-ROI matrix.
* **WHAT:** Re-threshold all SBC analyses using the standard CONN cluster-forming threshold of $p < 0.001$ (uncorrected voxel level) and apply Bonferroni or FDR correction across the 7 SN seeds (e.g., cluster $p\text{-FDR} < 0.05 / 7 = 0.0071$). Fix the RRC thresholding description in line 101 to accurately describe connection-level and ROI-level FDR correction in CONN.
* **HOW:** In the CONN GUI second-level SBC results explorer, set the voxel threshold to $p < 0.001$ and cluster threshold to $p\text{-FDR} < 0.0071$ (or use CONN's multivariate omnibus test across all 7 seeds simultaneously via an $F$-contrast `eye(7)` before conducting post-hoc seed tests). For SRS-2 and ADOS-2, restrict primary hypothesis testing to the Total Scores and treat the 9 subscale regressions as exploratory.

#### 3. Replace Circular Peak-Voxel $r$ and $r^2$ Values with Cluster-Averaged Effect Sizes
* **WHY:** Reporting $r$ and $r^2$ calculated from the peak $T$-statistic of a cluster selected by whole-brain thresholding in $n = 29$ subjects (e.g., $T(27) = 8.92 \implies r = 0.87, r^2 = 0.75$ in Table 4) is circular and misleads readers into believing that single resting-state connections explain 75% of variance in clinical autism severity.
* **WHAT:** Remove the circular peak-voxel $r$ and $r^2$ columns from Tables 2, 3, and 4 (or explicitly label them as biased peak-voxel statistics and report cluster-averaged connectivity values alongside leave-one-out cross-validated $r$ values). Also fix the sign typo in Table 4 Row 5 (`Social Interaction`, `AI-r`), where $T(27) = -5.87$ and $\beta = -0.06$ are negative, but $r$ is printed as `+0.75` instead of `-0.75`.
* **HOW:** Use CONN's `Import values` tool to extract the mean Fisher-$z$ connectivity across the entire cluster (or an independent anatomical ROI from the Harvard-Oxford atlas) for each participant, plot the actual scatterplots for the SRS-2 and ADOS-2 associations, and check for high-leverage outliers driving the regressions.

#### 4. Control for the Bimodal Age Structure and Mean Framewise Displacement in Second-Level GLMs
* **WHY:** Resting-state functional connectivity and head motion vary strongly with age, and this sample spans 18–64 years across two disconnected age cohorts (18–25 vs. 40–64 years). Furthermore, residual micromotion in ASD vs. TD can induce distance-dependent connectivity artifacts (reduced long-range RPFC–cerebellar FC and increased short-range local FC).
* **WHAT:** Include chronological age (or age cohort) and subject-level mean framewise displacement (FD) as second-level covariates in all group and behavioral GLMs, and report mean FD for the ASD and TD groups in Table 1. Also clarify the sample size for the SRS-2 and ADOS-2 analyses (Table 1 $t$-values for SRS-2 and Table 3 $T(54)$ imply $n = 58$, whereas ADOS-2 in Table 4 has $T(27)$).
* **HOW:** Add `Age` and `QC_MeanMotion` (automatically generated by CONN during ART scrubbing) to the second-level model covariates (`AllSubjects`, `ASD`, `TD`, `Age`, `QC_MeanMotion`) and verify whether the RPFC–cerebellum and SMG–MTG/AG clusters remain significant.
