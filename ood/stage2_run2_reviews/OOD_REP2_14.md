# Review of OOD_REP2_14

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.0 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.9/3.5 | Claims: 1.5/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.3/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This resting-state fMRI study investigates local spontaneous brain activity and seed-based functional connectivity (rsFC) abnormalities within the default mode network (DMN) in 56 non-manic patients with bipolar disorder (BD; 30 euthymic with $\text{HAMD} \le 7$, 26 depressed with $\text{HAMD} > 7$, all $\text{YMRS} < 7$) compared with 71 age-, sex-, and education-matched healthy controls (HC). Using DPABI v3.1 and SPM12 (controlling for age, sex, education, and mean framewise displacement; voxel $p < 0.001$, cluster FWE $p < 0.05$), the authors compute fractional amplitude of low-frequency fluctuation (fALFF), regional homogeneity (ReHo), and degree centrality (DC). They report reduced fALFF, ReHo, and DC in the left precuneus in BD patients, define a 47-voxel overlap cluster in the left precuneus as a seed for whole-brain rsFC, and find decreased rsFC with the local precuneus and medial prefrontal cortex (MPFC) alongside reduced negative rsFC ("anticorrelation") with the left putamen/insula. Two confirmation analyses—using the 57-voxel fALFF $\cap$ DC overlap and the anatomical Brainnetome Atlas precuneus seed (regions 153+154)—are conducted to test robustness.

The multi-index whole-brain screening strategy and the inclusion of an anatomical atlas-based confirmation analysis (Brainnetome A31) are positive methodological features. However, the study's main conclusions are weakened by four methodological and interpretive issues: (1) the left precuneus ReHo cluster actually failed the pre-specified cluster-level FWE threshold ($P_{\text{FWE}} = 0.135$; Table 2), yet the authors relaxed the threshold post hoc to uncorrected $p < 0.001$ to claim convergent three-index abnormality; (2) using a data-driven cluster selected for reduced ReHo (local connectivity) and DC (global connectivity) in BD vs. HC as the seed for a subsequent seed-based rsFC $t$-test in the *exact same sample* is circular (double dipping), and when replaced by the independent Brainnetome atlas seed (Table 3), both the local precuneus cluster and the left putamen/insula cluster disappear; (3) preprocessing included Global Signal Regression (GSR; line 66), which mathematically forces whole-brain correlations to sum to zero and induces artificial negative correlations ("anticorrelations"); and (4) $91\%$ of BD patients ($51/56$) were on psychotropic medications while $0\%$ of HCs were medicated. Re-framing the results around the non-circular atlas confirmation (where only precuneus–MPFC hypoconnectivity survives), repeating the rsFC test without GSR, and accurately reporting the non-significant ReHo FWE result will place the manuscript on solid ground.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Patients with BD exhibit significantly reduced local spontaneous activity in the left precuneus across fALFF, ReHo, and DC (Table 2, Fig. 1): [Overstated].**  
  Under the study's pre-specified statistical threshold (voxel $p < 0.001$, cluster-level $P_{\text{FWE}} < 0.05$; line 88), only fALFF ($69$ voxels, $P_{\text{FWE}} = 0.004$) and DC ($187$ voxels, $P_{\text{FWE}} = 0.017$) reached cluster-level significance in the left precuneus. ReHo did *not* survive cluster-level FWE correction ($106$ voxels, $P_{\text{FWE}} = 0.135$; Table 2). Switching to an uncorrected cluster threshold post hoc (line 131) to claim convergent three-index significance in the Abstract and Discussion overstates the ReHo result. Moreover, as the authors note on line 205, fALFF and DC are strongly collinear across subjects ($r = 0.671, P < 0.001$), so they do not represent three independent lines of evidence.

* **BD patients have decreased intra-DMN rsFC between the precuneus and the medial prefrontal cortex (MPFC; Table 3, Fig. 2): [Well Supported].**  
  Crucially, while the 47-voxel and 57-voxel data-driven seed analyses are affected by selection circularity, the precuneus–MPFC hypoconnectivity ($T = 4.50$, $126$ voxels, $P_{\text{FWE}} = 0.014$) replicates cleanly when using the independent, a priori anatomical Brainnetome Atlas seed (bilateral area 31, Nos. 153+154; Table 3, row 7). This provides non-circular support for reduced anterior–posterior DMN coupling in the BD cohort.

* **BD patients exhibit decreased local rsFC within the left precuneus and diminished negative connectivity ("anticorrelation") between the left precuneus and the left putamen/insula (salience network), confirmed across analysis strategies: [Methodologically Flawed].**  
  This claim suffers from two compounding methodological flaws:
  1. **Circular seed selection (double dipping) and failure to replicate in the atlas confirmation:** The 47-voxel (and 57-voxel) left precuneus seed was defined in the same 56 BD and 71 HC subjects as the locus showing significantly reduced DC (whole-brain summed connectivity) and ReHo (local 27-voxel neighborhood connectivity) in BD vs. HC. Re-testing the same subjects for voxel-wise seed connectivity from that exact cluster is statistically non-independent: reduced rsFC in the 97 voxels immediately surrounding the seed (peak $-2, -50, 36$ vs. seed $0, -52, 36$) is simply a rediscovery of the seed's reduced ReHo/DC, and whole-brain differences are guaranteed by the DC selection. When the circularity is removed in Confirmation Analysis 2 using the anatomical Brainnetome precuneus seed (Table 3, row 7), **neither the within-precuneus cluster nor the left putamen/insula cluster survives**—contradicting the Abstract's claim that *"The abnormalities in DMN functional connectivity were confirmed through various analysis strategies."*
  2. **Unacknowledged Global Signal Regression (GSR) artifact:** Methods line 66 states that *"the global mean signals"* were regressed out during preprocessing. Mathematically, GSR centers every subject's whole-brain seed correlation distribution near zero, artificially creating negative correlations and converting true reductions in positive intra-DMN connectivity into apparent shifts in negative connectivity elsewhere. Without a non-GSR sensitivity analysis, interpreting the putamen/insula difference as a biological loss of DMN–SN "anticorrelation" is unsupported.

* **Altered precuneus–putamen/insula and DMN functional patterns represent trait-like features and candidate diagnostic biomarkers for BD: [Overstated].**  
  First, no diagnostic classification analysis (ROC-AUC, sensitivity, specificity, or cross-validation) was performed, and none of the precuneus metrics correlated with clinical HAMD scores ($P > 0.017$; line 131). Second, in the subgroup analysis (line 195), the depressed BD subgroup (DP, $n = 26$) showed no significant FWE-corrected rsFC differences from HCs at the primary threshold, requiring an unquantified threshold reduction in the supplement. Third, $91\%$ of BD patients ($51/56$) were taking mood stabilizers ($n = 28$), antipsychotics ($n = 27$), and/or antidepressants ($n = 19$) vs. $0\%$ of HCs (Table 1), confounding disease effects with psychotropic medication effects.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Anchor Connectivity Claims on the Non-Circular Brainnetome Atlas Seed Analysis
* **WHY:** Defining a seed from a group contrast of DC (summed whole-brain rsFC) and ReHo (local rsFC) and testing seed-to-voxel rsFC in the same sample is circular double-dipping. The independent Brainnetome Atlas seed (Nos. 153+154) removes this circularity and shows that only the precuneus–MPFC cluster survives ($P_{\text{FWE}} = 0.014$), whereas the local precuneus and putamen/insula clusters do not (Table 3).
* **WHAT:** Promote the Brainnetome Atlas seed analysis (or an independent literature/meta-analytic precuneus coordinate) to the primary non-circular validation of the rsFC findings, and explicitly acknowledge in the Results and Discussion that the local precuneus and putamen/insula clusters did not replicate under the unbiased atlas seed.
* **HOW:** Revise the Abstract (lines 21–26), Results (lines 193–194), and Discussion (lines 210–221) to distinguish between the exploratory overlap-seed results and the confirmed atlas-seed result (precuneus–MPFC hypoconnectivity).

#### 2. Repeat the Seed-Based rsFC Analysis Without Global Signal Regression (GSR)
* **WHY:** Regressing out the global mean signal (line 66) mathematically forces negative correlations in seed-based rsFC maps and can manufacture group differences in "anticorrelation" when positive network coupling differs between groups.
* **WHAT:** Re-run the DPABI preprocessing and SPM12 two-sample $t$-test using white matter, CSF, and Friston-24 motion regressors (or CompCor) *without* Global Signal Regression, and check whether the left precuneus and left putamen/insula actually exhibit negative baseline correlation and significant group differences without GSR.
* **HOW:** In DPABI v3.1, uncheck `Global Signal` in the nuisance covariate regression step, recompute the Z-scored rsFC maps for the 57-voxel (fALFF $\cap$ DC) and Brainnetome (153+154) seeds, and report the non-GSR group comparison alongside Table 3.

#### 3. Test for Medication and Subgroup Confounding Within the BD Cohort
* **WHY:** Because 51 of 56 BD patients were taking mood stabilizers, antipsychotics, or antidepressants (often in combination), differences between BD and HC could be driven by psychotropic medication load rather than bipolar pathophysiology.
* **WHAT:** Compare left precuneus fALFF, DC, ReHo, and precuneus–MPFC rsFC across medication classes (or total medication load index) within the $N = 56$ BD group, and report direct two-sample comparisons between euthymic ($n = 30$) and depressed ($n = 26$) BD patients at the standard statistical threshold.
* **HOW:** Fit a multiple linear regression within the BD group (`metric ~ mood_stabilizer + antipsychotic + antidepressant + HAMD + age + sex + mean_FD`) in SPSS/R and report the $t$-statistics and $p$-values for each medication class in a supplementary table.

#### 4. Technical and Editorial Cleanup
* **WHY:** Accurately reporting statistical thresholds and fixing typographical errors improves transparency.
* **WHAT & HOW:**
  1. **Abstract (line 21) & Discussion (line 205):** Clarify that fALFF ($P_{\text{FWE}} = 0.004$) and DC ($P_{\text{FWE}} = 0.017$) survived cluster-level FWE correction in the left precuneus, whereas ReHo showed a trend at the cluster level ($P_{\text{FWE}} = 0.135$, peak voxel $P_{\text{FWE}} < 0.05$).
  2. **Line 252 (Abbreviations typo):** Correct `"ractional amplitude of low-frequency fluctuation"` to `"fractional amplitude of low-frequency fluctuation"` and include the missing abbreviation keys (`DMN`, `EP`, `DP`, `rs-fMRI`, `fALFF`, `ReHo`, `rsFC`, `MPFC`, `PCC`, `YMRS`, `HAMD`, `MPRAGE`, `KCC`) next to their definitions in lines 242–269.
  3. **Line 66:** Correct `"Resting state fMRI date was preprocessed"` to `"Resting-state fMRI data were preprocessed"`.
