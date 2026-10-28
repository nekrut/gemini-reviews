# Review of OOD_ANON_33

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **3.5 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.0/3.5 | Claims: 0.9/2.5 | Biology: 0.9/2.0 | Reproducibility: 0.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This cross-sectional case-control study examines 5-minute eyes-closed resting-state EEG recordings (16 region-of-interest scalp electrodes from a 24-channel system) across 260 older adults in Shanghai communities: 65 cognitively healthy controls (MoCA 26–30), 100 individuals with mild cognitive impairment (MCI, MoCA 20–25), and 95 individuals with moderate-to-severe cognitive impairment (MoCA $\le 19$). The authors compute four functional connectivity metrics (PLV, COH, PLI, WPLI) across six frequency bands and four EEG microstates (A–D) and use ANCOVA and correlation analyses to evaluate associations with cognitive group, age, education, physical activity (IPAQ-S), and sleep quality (PSQI). Raw EEG data and analysis scripts are not publicly available.

While the community sample size ($N = 260$) and joint evaluation of phase-lag connectivity metrics alongside microstates are potentially useful, the manuscript exhibits major statistical anomalies, internal contradictions, and methodological artifacts. Most critically, the ANCOVA $F$-statistics reported for microstate duration, coverage, and transition probabilities reach $F = 695.8$ to $1091.2$ ($df = 2, 253$, implying $\eta_p^2 \approx 0.90$), an order of magnitude beyond physiologically plausible human EEG group differences and indicative of back-fitting microstates to group-specific rather than pooled template maps (Fig. 2E). In addition, the reported partial correlation signs in line 137 ($r = +0.271$ between MoCA and PSQI; $r = -0.156$ between MoCA and education) directly contradict the authors' textual conclusion that higher PSQI is a risk factor and higher education is protective. Extensive re-analysis—starting with pooled microstate template clustering across all 260 subjects and auditing variable coding—is required to determine which findings are genuine.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Static and dynamic features of EEG microstates A, B, C, and D strongly differentiate healthy, MCI, and moderate-to-severe cognitive impairment groups ($F = 695.8\text{--}1091.2, P < 0.001$): [Methodologically Flawed].**  
  Line 171 reports ANCOVA $F$-statistics of $695.786, 951.307, 733.074, 1091.157, 782.276, 948.391, 825.959,$ and $1072.705$ for microstate duration and coverage, and line 176 reports $F$-statistics up to $994.741$ for transition probabilities. For $N = 260$, $F(2, 253) = 1091.2$ implies that group status alone accounts for $89.6\%$ of the total variance across individuals. In the MS 1.0 toolbox workflow (line 114 and Fig. 2E), if AAHC clustering is run separately within each cognitive group and each subject's EEG is back-fitted to its own group's template maps, differences in template spatial topography artificially induce massive between-group shifts in temporal parameters.

* **Age and poor sleep quality (PSQI) are risk factors for cognitive decline, whereas higher education and physical activity (IPAQ) are protective factors: [Methodologically Flawed].**  
  In line 137, the authors report partial correlation coefficients with MoCA of $r = -0.213$ for age, $r = +0.271$ ($P < 0.001$) for PSQI, $r = -0.156$ ($P = 0.012$) for education level, and $r = +0.388$ ($P < 0.001$) for IPAQ. Because higher MoCA scores indicate better cognition (line 83) and higher PSQI scores indicate worse sleep disturbance (line 91), a positive correlation ($+0.271$) means worse sleep is associated with *better* MoCA scores, and a negative correlation ($-0.156$) means higher education is associated with *worse* MoCA scores—the exact opposite of the authors' claim in the immediately following sentence. Furthermore, MoCA scores were already adjusted by adding 1–2 bonus points for low education (line 83), introducing circularity when correlating education-adjusted MoCA with education.

* **Average functional connectivity strength and density in the $\delta$ and $\theta$ bands increase with severity of cognitive impairment ($F = 5.38\text{--}7.81, \eta_p^2 = 0.041\text{--}0.058$): [Moderately Supported].**  
  Requiring simultaneous significance across volume-conduction-sensitive (PLV, COH) and volume-conduction-resistant (PLI, WPLI) metrics in ANCOVA adjusted for age, education, PSQI, and IPAQ (line 145) is a reasonable safeguard against zero-lag volume conduction artifacts. However, the Bonferroni threshold ($\alpha = 0.05/6 = 0.0083$) only corrects for 6 frequency bands rather than 6 bands $\times$ 4 metrics ($24$ tests, $\alpha = 0.0021$), and the critical $F$-value in line 121 uses $df_2 = 257$ (unadjusted ANOVA) rather than the ANCOVA denominator degrees of freedom ($df_2 = 260 - 3 - 4 = 253$).

* **Changes in microstates A–D reflect specific cortical network sources (posterior cingulate cortex, insula, frontoparietal and dorsal attention networks) and progressive compensatory-to-rigid neural plasticity: [Overstated].**  
  The study records from only 16 scalp ROI electrodes (line 96) without MRI head models or distributed source imaging, which cannot localize deep structures such as the insula or posterior cingulate cortex. Moreover, the design is cross-sectional (acknowledged in second chunk line 6) and cannot establish longitudinal progression from compensation to rigidity.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Re-Run Microstate Back-Fitting Using a Single Pooled Global Template Across All 260 Participants
* **WHY:** Back-fitting each group to separate group-derived microstate templates confounds spatial map differences with temporal duration/coverage parameters and generates artificial $F > 600\text{--}1000$ statistics.
* **WHAT:** Compute a single grand-average set of 4 microstate template maps (A, B, C, D) across all 260 participants (or via balanced bootstrap across the three groups) before back-fitting individual recordings.
* **HOW:** In EEGLAB/MS 1.0, concatenate the group-level GFP peak maps across all 260 subjects, run AAHC clustering once to obtain 4 shared canonical maps, back-fit every subject's continuous EEG to these identical 4 templates, and recompute the ANCOVA $F$-values and $\eta_p^2$ in SPSS.

#### 2. Audit Variable Coding and Reconcile Partial Correlation Signs with Logistic Regression
* **WHY:** Reporting $r(\text{MoCA}, \text{PSQI}) = +0.271$ and $r(\text{MoCA}, \text{Education}) = -0.156$ directly contradicts the claim that higher PSQI is a risk factor and higher education is protective.
* **WHAT:** Verify whether cognitive group code ($1 = \text{healthy}, 2 = \text{MCI}, 3 = \text{moderate/severe}$) was inadvertently entered in place of raw MoCA score, or whether education/PSQI coding was reversed in SPSS.
* **HOW:** Inspect the SPSS syntax for the partial correlation analysis (line 137), re-run partial correlations using raw unadjusted MoCA scores (before adding the $\le 12$-year education bonus points) and raw years of education, and report a complete table of means $\pm$ SD by group alongside exact partial $r$ values.

#### 3. Correct ANCOVA Degrees of Freedom, Post-Hoc Pairwise Comparisons, and Multiple-Testing Thresholds
* **WHY:** Line 121 reports $df = (2, 257)$ for ANCOVA even though 4 covariates were included ($df_2 = 253$), and omnibus $F$-tests alone do not establish significant differences between every pair of groups (Healthy vs. MCI vs. Moderate/Severe).
* **WHAT:** Report exact ANCOVA $df = (2, 253)$ and Bonferroni-corrected post-hoc pairwise comparisons between the three cognitive groups.
* **HOW:** In SPSS `UNIANOVA`, include `/EMMEANS=TABLES(Group) COMPARE ADJ(BONFERRONI)` with covariates `Age`, `Education`, `PSQI`, and `IPAQ`, and apply Bonferroni correction across all 24 connectivity tests ($\alpha = 0.05/24 = 0.00208$) and all 24 microstate parameters ($\alpha = 0.05/24 = 0.00208$).

#### 4. Clarify Network Density Thresholding and Remove Unsupported Source-Localization Claims
* **WHY:** Line 150 states that connectivity density was compared using "the average brain functional connectivity strength of all older adults... as a reference," which conflates overall coupling strength with topological density, and 16 scalp channels cannot resolve insular or posterior cingulate activity.
* **WHAT:** Evaluate topological network properties across proportional sparsity thresholds (e.g., top 10%–30% of edges) independent of mean strength, and temper deep anatomical source claims in the Discussion.
* **HOW:** Recompute graph density and clustering coefficients across fixed proportional thresholds in MATLAB, and revise Discussion line 190 to state that microstates A–D correspond to scalp potential topographies previously associated with large-scale networks in combined EEG-fMRI literature rather than direct source measurements in this cohort.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Missing equations, empty table artifacts, future-tense protocol remnants, and self-contradictory sentences impair readability and reproducibility.
* **WHAT & HOW:**
  1. **Line 56:** Change future-tense phrasing ("This research will take place... A total of 195 older adults... will be included") to past tense.
  2. **Line 72:** Replace "triple-blind design" with "blinded outcome assessment," as this is an observational cross-sectional case-control study with no randomized treatment intervention.
  3. **Line 87:** Insert the missing IPAQ-S MET-minutes/week formula after "The formula for calculation is as follows:".
  4. **Lines 110 & 114:** Remove the empty broken table (`| | 1 |`) and insert the missing Global Field Power equation $\text{GFP}(t) = \sqrt{\frac{1}{K}\sum_{i=1}^{K}(V_i(t) - V_{\text{mean}}(t))^2}$ referenced as "(5)".
  5. **Line 121 vs. Fig. 2H:** Reconcile "32 comparisons" in line 121 with "24 microstate parameters" in the Fig. 2H caption (12 static + 12 transition probabilities $= 24$).
  6. **Line 181:** Fix the self-contradiction where PSQI is stated to have "no correlation with the microstate parameters (all P-values > 0.05)" and in the next sentence is listed as one of the "influencing factors contributing to the differences in microstate parameters."
