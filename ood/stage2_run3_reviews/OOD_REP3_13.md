# Review of OOD_REP3_13

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.0 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.4/3.5 | Claims: 1.2/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.2/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This resting-state fMRI study investigates local spontaneous brain activity and seed-based functional connectivity (rsFC) of the default mode network (DMN) in 56 non-manic patients with bipolar disorder (BD; 30 euthymic with $\text{HAMD} \le 7$, 26 depressed with $\text{HAMD} > 7$, all $\text{YMRS} < 7$) and 71 demographically matched healthy controls (HCs) re-analyzed from a previously published cohort. Using DPABI and SPM12 (controlling for age, sex, education, and mean framewise displacement), the authors compute voxel-wise fractional amplitude of low-frequency fluctuation (fALFF), regional homogeneity (ReHo), and degree centrality (DC; $r_0 > 0.2$). They define a 47-voxel overlapping cluster in the left precuneus (BA 31/7) as a seed for whole-brain rsFC, reporting reduced rsFC within the precuneus and with the medial prefrontal cortex (MPFC), alongside reduced negative rsFC (weaker anticorrelation) with the left putamen/insula. Two confirmation analyses—one using the 57-voxel overlap of fALFF and DC only, and another using an anatomical precuneus seed from the Human Brainnetome Atlas (regions 153+154)—are also reported. Raw neuroimaging data are not publicly deposited ("available from the first and the corresponding authors").

While the study applies an appropriate primary cluster-forming threshold ($P_{\text{voxel}} < 0.001$ with cluster-level $P_{\text{FWE}} < 0.05$ for fALFF and DC) and includes an anatomical atlas seed check, the primary analytical pipeline is undermined by three methodological flaws: (1) **circularity (double-dipping)** between seed selection and rsFC testing—selecting a 47-voxel seed because it exhibits lower local synchronization (ReHo) and lower whole-brain summed connectivity (DC) in BD vs. HC, and then testing that same seed for rsFC differences in the same 127 subjects, which mathematically guarantees reduced local precuneus connectivity and biases whole-brain connectivity; (2) **post-hoc threshold relaxation**, where ReHo failed cluster-level FWE correction ($P_{\text{FWE}} = 0.135$, Table 2) and subgroup analyses failed FWE correction, yet both are presented as positive findings after dropping FWE correction; and (3) **contradiction with the anatomical seed control (Table 3)**, where replacing the data-driven seed with the independent Brainnetome precuneus seed eliminates both the left putamen/insula finding and the local precuneus finding, leaving only the precuneus–MPFC hypoconnectivity intact. These issues can be resolved through computational re-analysis (leave-one-out or split-half seed definition, non-GSR sensitivity checks) and reframing of the claims.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Patients with BD exhibit significantly reduced fALFF ($P_{\text{FWE}} = 0.004$) and degree centrality ($P_{\text{FWE}} = 0.017$) in the left precuneus, as well as reduced rsFC between the precuneus and MPFC ($P_{\text{FWE}} = 0.014\text{--}0.023$): [Moderately Supported].**  
  Both the whole-brain fALFF and DC reductions in the left precuneus survive cluster-level FWE correction ($P_{\text{FWE}} < 0.05$ at voxel-level $P < 0.001$, Table 2), and the precuneus–MPFC hypoconnectivity replicates when using the independent anatomical Brainnetome precuneus seed (regions 153+154: $T = 4.50$, $126\text{ voxels}$, $P_{\text{FWE}} = 0.014$, Table 3). However, because $91.1\%$ ($51/56$) of BD patients were taking psychotropic medications (mood stabilizers, antipsychotics, antidepressants) compared to $0\%$ of HCs, medication effects cannot be ruled out as a driver of reduced local BOLD amplitude and connectivity.

* **Patients with BD show significantly reduced ReHo in the left precuneus: [Overstated].**  
  As shown in Table 2, the left precuneus ReHo cluster ($106\text{ voxels}$, peak $T = 5.29$) failed to meet the pre-specified cluster-level family-wise error threshold, yielding $P_{\text{FWE}} = 0.135$. Relaxing the threshold post-hoc to cluster-level uncorrected $P < 0.001$ (p. 6) and reporting in the Abstract and Conclusions that "the BD group showed reduced fALFF, ReHo, and DC values in the left precuneus" misrepresents a statistically non-significant cluster-level result as convergent support.

* **Patients with BD exhibit decreased rsFC within the left precuneus ($T = 5.29$, $P_{\text{FWE}} = 0.014$) and diminished negative connectivity (anticorrelation) between the left precuneus and left putamen/insula ($T = 4.92$, $P_{\text{FWE}} < 0.001$), confirmed across analysis strategies: [Methodologically Flawed].**  
  First, the within-precuneus rsFC reduction (peak MNI `-2, -50, 36`, $T = 5.29$, Table 3) is a circular artifact of selecting the 47-voxel seed at MNI `0, -52, 36` based on reduced ReHo (which measures 27-voxel local connectivity at `0, -52, 36` with the exact same peak $T = 5.29$, Table 2) and reduced DC (which measures summed whole-brain connectivity) in the same dataset. Second, when the circular data-driven seed is replaced by the unbiased anatomical Brainnetome A31 seed (No. 153+154) in the second confirmation analysis (Table 3, bottom row), *neither* the within-precuneus cluster *nor* the left putamen/insula cluster survives whole-brain correction. Claiming in the Abstract that all DMN and salience network (putamen/insula) connectivity abnormalities were "confirmed through various analysis strategies" is directly contradicted by Table 3. Third, preprocessing included Global Signal Regression (GSR; p. 4), which mathematically centers every subject's whole-brain correlation distribution around zero and can artificially induce or shift negative correlations ("anticorrelations") between large networks.

* **Altered DMN–Salience Network connectivity is a state-independent trait biomarker of BD associated with cognitive dysfunction and rumination: [Overstated].**  
  In the subgroup comparison (p. 7), depressed BD patients (DP, $n = 26$) vs. HCs showed no significant clusters at the primary FWE threshold until the authors "reduc[ed] the threshold", and no direct comparison between euthymic (EP, $n = 30$) and depressed (DP, $n = 26$) patients is reported. Furthermore, fALFF, ReHo, and DC did not correlate with HAMD scores ($P > 0.017$), BD-I and BD-II subtypes were pooled without recorded counts, and no cognitive tests, rumination scales, or diagnostic classification metrics (ROC-AUC, sensitivity, specificity) were collected or evaluated.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Eliminate Circular Seed Selection and Anchor Primary rsFC Claims to the Unbiased Atlas Seed or Split-Half Validation
* **WHY:** Defining a seed ROI from a voxel-wise BD vs. HC contrast on local/global connectivity (ReHo and DC) and testing seed-to-voxel connectivity on the same subjects constitutes double-dipping (Kriegeskorte et al., 2009), inflating false positives for local precuneus connectivity and any connections contributing to DC.
* **WHAT:** Promote the unbiased Human Brainnetome Atlas precuneus seed (regions 153+154, or left A31 region 153 alone to match the left-hemisphere lateralization) to the primary non-circular rsFC analysis, or use out-of-fold / split-half seed localization.
* **HOW:** Run the seed-based rsFC analysis using left A31 (Brainnetome ROI 153) as well as bilateral A31 (ROIs 153+154) across all 127 subjects. Additionally, perform a 2-fold split-half validation: define the fALFF $\cap$ DC precuneus cluster in Half A and test its seed-based rsFC in Half B (and vice versa). Restrict claims of confirmed rsFC abnormalities to connections that survive FWE correction in the non-circular analyses.

#### 2. Perform a Sensitivity Analysis Without Global Signal Regression (GSR) for the Putamen/Insula Anticorrelation
* **WHY:** Regressing out the global mean signal forces the sum of whole-brain correlation weights to be non-positive, which can create spurious negative correlations and distort between-group comparisons of anticorrelations between the DMN and Salience Network.
* **WHAT:** Re-compute the precuneus seed-based rsFC maps using preprocessing with white matter, CSF, and Friston-24 motion regression *without* GSR (or using anatomical CompCor).
* **HOW:** In DPABI v3.1, re-run the nuisance regression step omitting the global mean signal (keeping WM, CSF, and Friston-24 parameters) and inspect the within-group one-sample $t$-maps and between-group two-sample $t$-maps for the left precuneus–putamen/insula connection to determine whether true negative connectivity and group differences persist without GSR.

#### 3. Enforce Consistent FWE Statistical Thresholds Across ReHo and Affective State Subgroup Analyses
* **WHY:** Lowering the cluster threshold post-hoc when ReHo ($P_{\text{FWE}} = 0.135$) and the Depressed (DP) subgroup fail FWE correction inflates the family-wise false positive rate.
* **WHAT:** Report ReHo as a non-significant trend at the cluster level ($P_{\text{FWE}} = 0.135$, while noting its voxel-level FWE peak if applicable), and report a formal 3-group ANCOVA (EP vs. DP vs. HC) and direct two-sample test (EP vs. DP) under the fixed $P_{\text{voxel}} < 0.001, P_{\text{FWE}} < 0.05$ threshold.
* **HOW:** Extract mean $Z$-transformed rsFC and fALFF/DC values from the unbiased Brainnetome left precuneus ROI for EP ($n=30$), DP ($n=26$), and HC ($n=71$). Run a one-way ANCOVA in SPSS/R controlling for age, sex, education, and mean FD, followed by Bonferroni-corrected post-hoc pairwise comparisons (EP vs. HC, DP vs. HC, EP vs. DP), and report exact effect sizes (Cohen's $d$ and 95% CIs) rather than lowering whole-brain voxel thresholds.

#### 4. Temper Biomarker, Rumination, and Confirmation Claims in the Abstract and Discussion
* **WHY:** The study did not measure rumination or cognition, did not evaluate diagnostic classification accuracy, failed to achieve cluster-level FWE significance for ReHo, and did not replicate the putamen/insula cluster using the Brainnetome seed.
* **WHAT:** Revise the Abstract, Results, and Discussion to match the empirical findings.
* **HOW:**
  1. In the Abstract (Results), revise `showed reduced fALFF, ReHo, and DC values` to `showed significantly reduced fALFF and DC values (cluster-level P_FWE < 0.05) and a trend-level reduction in ReHo (P_FWE = 0.135) in the left precuneus`.
  2. In the Abstract and Results, clarify that while precuneus–MPFC hypoconnectivity was replicated using the anatomical Brainnetome atlas seed, the putamen/insula and within-precuneus clusters were only observed with the data-driven seed.
  3. Condense the speculative paragraphs on rumination and working memory in the Discussion, and remove the claim that DMN alterations serve as a diagnostic biomarker unless out-of-sample classification sensitivity/specificity are demonstrated.

#### 5. Technical and Editorial Corrections
* **WHY:** Typographical errors and incomplete data availability statements reduce clarity and reproducibility.
* **WHAT & HOW:**
  1. **Abbreviations List (p. 10):** Fix `ractional amplitude of low-frequency fluctuation` to `fractional amplitude of low-frequency fluctuation`, and insert the missing abbreviations keys (`DMN`, `EP`, `DP`, `rs-fMRI`, `fALFF`, `ReHo`, `rsFC`, `MPFC`, `PCC`, `YMRS`, `HAMD`, `MPRAGE`, `KCC`) alongside their definitions.
  2. **Public Data Deposition:** Deposit the unthresholded group $T$-maps for fALFF, ReHo, DC, and rsFC on NeuroVault (`https://neurovault.org/`) so that future meta-analyses can access the whole-brain statistical maps.
