# Forensic Peer Review: FEXP_ANON_124

**Overall Score:** **4.4 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **3.4 / 8.0**  
* **Score Breakdown:** Rigor: 1.1/3.5 | Claims: 1.1/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.0/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_124`
* **Perceived Domain & Topic:** Clinical Neuroimaging / Adolescent Psychiatry / Connectomics; pre-treatment resting-state fMRI graph-theoretical network predictors of 8-week SSRI antidepressant response in first-episode, drug-naïve adolescents with major depressive disorder (MDD).
* **Perceived Empirical Scope:** $N = 69$ first-episode, drug-naïve adolescent MDD patients (aged 13–18 years) stratified after 8 weeks of SSRI treatment into Responders ($n = 37$, $\ge 50\%$ HAMD-17 reduction) and Non-responders ($n = 32$, $< 50\%$ HAMD-17 reduction); 3T Siemens Skyra rs-fMRI parcellated with the 90-node AAL atlas (`DPABI v9.0` / `DPABINet 1.3`, sparsity $0.10\text{–}0.34$); permutation/t-tests, partial correlations, and forward LR logistic regression.

---

## 2. Executive Summary & Editorial Verdict

This study investigates whether baseline resting-state fMRI graph-theoretical metrics (9 global and 4 nodal metrics across the 90-region AAL atlas, integrated over sparsity thresholds $0.10\text{–}0.34$) distinguish 8-week SSRI responders ($n = 37$) from non-responders ($n = 32$) in first-episode, drug-naïve adolescents with MDD. The authors report significant baseline differences in four global segregation/small-world metrics ($\gamma$, $E_{\text{loc}}$, modularity, $\sigma$) and 19 nodal metric-by-region tests (Table 3), partial correlations with symptom changes ($\Delta\text{HAMD-17}$), and forward likelihood-ratio logistic regression models identifying right inferior parietal lobule (IPL) nodal efficiency ($\text{AUC} = 0.692$) and left pallidum clustering coefficient ($\text{AUC} = 0.655$) as significant predictors of treatment response. Notably, the authors performed a supplementary sensitivity check using unsmoothed fMRI data (Supplementary Table 1).

**Editorial Verdict: Major Revision / Uncorrected Multiple Testing Misrepresented as FDR-Corrected (4.4 / 10.0).** Studying first-episode, drug-naïve adolescent MDD patients followed prospectively over 8 weeks of SSRI therapy is a clinically valuable design, and the authors deserve credit for checking sensitivity to spatial smoothing. However, the statistical analysis of nodal network topology suffers from a critical false-discovery flaw and circular predictive modeling:
1. **Claimed FDR correction ($\alpha = 5\%$) was not applied to the nodal results in Table 3, and the 19 "significant" nodal findings match the exact number of false positives expected by chance ($360 \times 0.05 = 18$):** Section "Statistical analysis" (line 52) states that group differences were tested via 10,000-iteration permutation tests and *"Statistical significance for nodal measures was then corrected using false discovery rate (FDR) method ($\alpha = 5\%$)."* Yet Table 3 reports parametric $T$-statistics ($|T| = 2.03\text{ to }2.74$) whose $P$-values ($P = 0.008\text{ to }0.046$) are the **exact uncorrected two-tailed Student's $t$-test $p$-values for $\text{df} = 67$**. Across 90 AAL nodes, the smallest $p$-value in Table 3 ($P = 0.0079$ for $T = 2.74$) has a Benjamini–Hochberg FDR-adjusted $q$-value of **$q = 0.71$**—meaning **zero nodal metrics survive the stated 5% FDR correction**. Furthermore, testing 4 nodal metrics across 90 AAL nodes ($360$ tests) at uncorrected $P < 0.05$ yields an expected $360 \times 0.05 = \mathbf{18.0}$ false positives under complete randomness, which is virtually identical to the **19** significant rows reported in Table 3.
2. **In-sample circular screening for logistic regression and unstandardized Odds Ratios ($\text{OR} = 0.002$ and $54.944$):** Selecting the 19 uncorrected $P < 0.05$ nodal variables on the $N = 69$ cohort and running forward stepwise logistic regression and ROC curves on the same 69 patients without cross-validation inflates predictive performance. In addition, entering unstandardized sparsity-integrated AUC metrics (which have standard deviations of $\sim 0.01\text{–}0.02$) into logistic regression produces extreme, uninterpretable Odds Ratios per $+1.0$ unit change ($\text{OR} = 0.002$ and $\text{OR} = 54.944$, 95% CI: $1.626\text{–}1857.049$).
3. **Mislabeled definitions and figure-text discrepancies:** Figure 1 defines the sparsity integral (`AUC`) as *"area under the receiver operating characteristic curve,"* Figure 3 and the Results text disagree on which nodal variables were correlated with $\Delta\text{HAMD-17}$, and high-resolution T1 images were not used for spatial normalization.

### Assessment of Specific Claims

* **Claim 1 (SSRI non-responders exhibit significantly higher baseline global network segregation metrics [$\gamma$, $E_{\text{loc}}$, modularity, $\sigma$] than responders at uncorrected $P < 0.05$): `[Moderately Supported]`.**  
  Table 2 shows nominal group differences in $E_{\text{loc}}$ ($P = 0.010$), modularity ($P = 0.029$), $\gamma$ ($P = 0.035$), and $\sigma$ ($P = 0.049$), though only $E_{\text{loc}}$ remains marginal ($q = 0.09$) if adjusted across the 9 correlated global metrics, and no global metric correlated significantly with continuous $\Delta\text{HAMD-17}$ (line 123).
* **Claim 2 (Nineteen nodal topological metrics across frontal, limbic, parietal, and striatal regions significantly differentiate responders from non-responders after 5% FDR correction): `[Methodologically Flawed]`.**  
  The $P$-values in Table 3 ($0.008\text{–}0.046$) are uncorrected Student's $t$-test $p$-values ($\text{df} = 67$). None of the 19 nodal findings survive the 5% FDR correction stated in line 52 ($q_{\min} = 0.71$), and finding 19 hits at uncorrected $P < 0.05$ out of $4 \times 90 = 360$ tests equals the null expectation of $18.0$ false positives.
* **Claim 3 (Nodal metrics correlate significantly with continuous symptom improvement [$\Delta\text{HAMD-17}$]): `[Fragile]`.**  
  Testing correlations specifically on the 19 nodes pre-selected for differing between the responder and non-responder groups (which are themselves defined by $\Delta\text{HAMD-17} / \text{HAMD-17}_{\text{pre}} \ge 50\%$) introduces circularity between group selection and continuous $\Delta\text{HAMD-17}$ correlation, and differs between the Abstract ("reduction rate") and Figure 3 ("Pre minus Post").
* **Claim 4 (Lower right IPL nodal efficiency and higher left pallidum clustering coefficient significantly predict 8-week SSRI treatment response): `[Overstated]`.**  
  Derived from in-sample forward stepwise selection over 360 candidate nodal features without out-of-sample cross-validation, yielding modest in-sample AUCs ($0.692$ and $0.655$) and unstable unscaled odds ratios (95% CI up to $1,857$).

---

## 3. Forensic Defect Inventory

### Defect 1: Uncorrected Student's $t$-Test $P$-Values Reported in Table 3 Despite Claiming 5% FDR Correction Across 90 Nodes [ Pillar 3, Pillar 4 — Critical ]
* **Location:** Section "Statistical analysis" (line 52), Section "Comparison of graph theory indicators" (line 76), and Table 3 (lines 98–119).
* **Forensic Evidence:**
  1. **Verification that Table 3 $P$-values are uncorrected:** Line 52 states that nodal differences were evaluated via 10,000-permutation tests and *"corrected using false discovery rate (FDR) method ($\alpha = 5\%$)."* However, for every row in Table 3, the printed $P$-value matches the exact **uncorrected** two-tailed $t$-distribution survival function $2 \cdot (1 - F_{t, 67}(|T|))$ for $N = 69$ ($\text{df} = 67$):
     - $T = 2.74 \implies p_{\text{uncorr}} = 0.00786$ (Table 3 prints $0.008$)
     - $T = 2.61 \implies p_{\text{uncorr}} = 0.01116$ (Table 3 prints $0.011$)
     - $T = -2.45 \implies p_{\text{uncorr}} = 0.01690$ (Table 3 prints $0.017$)
     - $T = 2.41 \implies p_{\text{uncorr}} = 0.01870$ (Table 3 prints $0.019$)
     - $T = 2.40 \implies p_{\text{uncorr}} = 0.01918$ (Table 3 prints $0.019$)
     - $T = 2.38 \implies p_{\text{uncorr}} = 0.02017$ (Table 3 prints $0.020$)
     - $T = 2.07 \implies p_{\text{uncorr}} = 0.04230$ (Table 3 prints $0.042$)
     - $T = 2.03 \implies p_{\text{uncorr}} = 0.04632$ (Table 3 prints $0.046$)
  2. **Failure to pass FDR correction and match to null false-positive expectation:** Across 90 AAL regions, the minimum uncorrected $p$-value ($0.00786$) yields a Benjamini–Hochberg adjusted $q = 0.00786 \times 90 = 0.707 > 0.05$. Across all 4 nodal metrics $\times$ 90 regions $= 360$ tests, the expected number of false positives at uncorrected $p < 0.05$ under the global null hypothesis is $360 \times 0.05 = 18.0$, compared to 19 rows reported in Table 3.
* **Fix:** Explicitly state in the Methods, Results, and Discussion that no nodal comparisons survived FDR correction ($\alpha = 0.05$) across the 90 AAL regions and that the 19 regions in Table 3 represent **uncorrected exploratory ($p < 0.05$)** findings, or use a multivariate/network-level approach (e.g., Network-Based Statistic or regularized whole-connectome classification) that avoids 360 unadjusted univariate nodal tests.

### Defect 2: In-Sample Stepwise Selection Circularity and Unstandardized Predictor Scaling in Logistic Regression (Table 4) [ Pillar 3, Pillar 4 — Major ]
* **Location:** Section "Statistical analysis" (line 52), Results (line 123), Figure 4 (line 129), and Table 4 (lines 132–136).
* **Forensic Evidence:**
  1. **Unscaled Odds Ratios:** In Table 4, `Right inferior parietal lobule nodal efficiency` has $\text{OR} = 0.002$ ($95\%\text{ CI}: 0.000\text{–}0.258$) and `Left pallidum clustering coefficient` has $\text{OR} = 54.944$ ($95\%\text{ CI}: 1.626\text{–}1857.049$). Because the predictors are sparsity-integrated AUCs over $[0.10, 0.34]$ (whose values are $\sim 0.10\text{–}0.15$ with $\text{SD} \approx 0.01$), a $+1.0$ unit increase in the predictor is $\sim 50\text{–}100$ standard deviations wide, causing $\exp(\hat{\beta})$ to blow up or vanish.
  2. **In-sample selection bias:** Pre-screening 360 nodal metrics on the full $N = 69$ dataset at $P < 0.05$ and running forward LR stepwise regression on the survivors on the same data without cross-validation overfits the sample, and notice there is a marginal sex imbalance between groups in Table 1 ($14/23$ males/females in responders vs. $6/26$ in non-responders, $P = 0.081$) that was not controlled for in the univariate nodal $t$-tests or logistic regression.
* **Fix:** Z-score standardize all graph metrics ($\text{mean} = 0, \text{SD} = 1$) prior to logistic regression so Odds Ratios represent per-1-SD changes, include age, sex, and baseline HAMD-17 as covariates, and evaluate ROC AUC using nested $k$-fold cross-validation.

### Defect 3: Misdefined Graph-Metric Sparsity `AUC` in Figure 1 and Inconsistencies Between Text and Figure 3 [ Pillar 7 — Moderate ]
* **Location:** Abstract (line 9), Methods (lines 40, 45), Figure 1 caption (line 79), Results (line 123), and Figure 3 caption (line 126).
* **Forensic Evidence:**
  1. **Misdefined `AUC` in Figure 1:** In DPABINet graph analysis (line 47), `AUC` is the **area under the topological metric curve across sparsity thresholds ($0.10\text{–}0.34$)**. However, the Figure 1 caption (line 79) erroneously defines `AUC` as *"area under the receiver operating characteristic curve."*
  2. **Mismatch between Results text and Figure 3 panels:** Results line 123 states that nodal efficiency in the `left hippocampus` correlated negatively with $\Delta\text{HAMD-17}$ and makes no mention of clustering coefficients in the left hippocampus, left parahippocampal gyrus, or left amygdala. Conversely, Figure 3 (line 126) omits `left hippocampus nodal efficiency` and instead plots clustering coefficients in `HIP.L (CC)` (panel G), `PHG.L (CC)` (panel H), and `AMYG.L (CC)` (panel I).
  3. **Anatomical label typos in Figure 3 caption:** Line 126 defines `(C) PAL.L (Betweeness), Betweeness in the left postcentral gyrus` (`PAL.L` is left pallidum, not left postcentral gyrus, which is already in panel B) and defines `(M) SMG.R (DC), Degree centrality in the left supramarginal gyrus` (`SMG.R` vs. `left`).
  4. **Abstract vs. Results outcome definition:** The Abstract (line 9) states that partial correlations were computed with the *"reduction rate in Hamilton Depression Rating Scale-17 score"* ($(\text{Pre} - \text{Post})/\text{Pre}$), whereas Methods (line 52), Results (line 123), and Figure 3 (line 126) state they were computed with the raw difference $\Delta\text{HAMD-17} = \text{Pre} - \text{Post}$ and *"absolute HAMD-17 scores."*
  5. **Unused T1 MPRAGE and omitted CSF regression:** Although 1-mm isotropic MPRAGE T1 images were acquired (line 40), line 45 states that functional images were normalized directly to an EPI template without T1 co-registration/segmentation, and nuisance regression omitted cerebrospinal fluid (CSF) signals.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.1** | **3.5** | Claims 5% FDR correction for nodal metrics in Methods, but reports uncorrected $t$-test $p$-values in Table 3 where 0 of 19 hits survive FDR ($q_{\min} = 0.71$) and the 19 hits match the 18.0 expected by chance across 360 tests; circular in-sample stepwise logistic regression with unscaled ORs. |
| **2. Claim-to-Evidence Alignment** | **1.1** | **2.5** | Presents uncorrected nodal false-positive noise and in-sample stepwise selection ($\text{AUC} = 0.655\text{–}0.692$) as "robust predictors of SSRIs efficacy." |
| **3. Data Integrity & Biological Plausibility** | **1.2** | **2.0** | Valuable clinical cohort of 69 first-episode, drug-naïve adolescents with MDD followed for 8 weeks, and includes an unsmoothed fMRI sensitivity analysis; limited by EPI-template normalization, omitted CSF nuisance regression, and unadjusted concomitant medications. |
| **4. Reproducibility & Data Integrity** | **1.0** | **2.0** | Figure 1 misdefines sparsity `AUC` as ROC AUC; Figure 3 panels and labels (`PAL.L`, `SMG.R`, `HIP.L`) contradict the Results text; Abstract ("reduction rate") contradicts Figure 3 ($\text{Pre} - \text{Post}$); data only available upon request. |
| **Total Composite Score** | **4.4** | **10.0** | **Flawed / Overstated** (Scientific Core Score: **3.4 / 8.0**) |
