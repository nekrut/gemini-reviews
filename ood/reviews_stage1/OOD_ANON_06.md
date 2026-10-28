# Review of OOD_ANON_06

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **2.2 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.4/3.5 | Claims: 0.6/2.5 | Biology: 0.7/2.0 | Reproducibility: 0.5/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study investigates resting-state EEG microstate dynamics across 31 suicide attempt (SA) survivors, 33 individuals with suicidal ideation (SI), and 33 normal controls (NP) using 3-minute 64-channel eyes-open EEG recordings. Applying $k$-means clustering into five canonical microstate topographies (A–E), the authors compare mean duration, occurrence per second, percentage temporal coverage, and pairwise transition probabilities across the three groups via one-way ANOVAs, and regress suicide risk scores (SBQ-R) against microstate parameters across the combined SA + SI cohort ($n = 64$). They conclude that SA survivors and SI individuals share elevated occurrence and coverage of perceptual microstates A and B compared to controls, while SA survivors are distinguished from the SI group by higher occurrence and transition probabilities of microstates D (dorsal attention) and E (salience) and shorter durations of microstates C, D, and E.

Although identifying electrophysiological markers that distinguish suicide attempters from ideators is an important clinical goal, forensic audit of the reported tables reveals severe mathematical and numerical impossibilities that invalidate the empirical data in Tables 1, 2, and 3. Specifically: (1) in Table 3, the means, standard errors, $F$-values, and $p$-values for transitions `B to A`, `B to C`, `B to D`, and `B to E` are verbatim duplicates of `A to B`, `A to C`, `A to D`, and `A to E` down to two decimal places; (2) in Table 2, the reported group means for Duration, Occurrence, and Coverage violate the fundamental identity $\text{Coverage}_k \approx \text{Duration}_k \times \text{Occurrence}_k$, and the sum of coverages across all five microstates in the NP and SI groups is only $63.9\%$ and $72.8\%$ instead of $100\%$; (3) in Table 1, the marital status percentages are mathematically impossible (e.g., $24/33 = 72.7\%$, but reported as $6.06\%$; $19/33 = 57.6\%$, but reported as $21.21\%$); and (4) the text of the Results and Discussion directly contradicts Table 2 regarding microstate D coverage. Furthermore, no public data or code are provided.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Altered inter-state transition probabilities distinguishing SA from SI and NP (Section "Microstate Transition Probabilities", Table 3): [Methodologically Flawed].**  
  In Table 3, four entire rows of transition probabilities from microstate B (`B to A`, `B to C`, `B to D`, `B to E`) are exact copy-paste duplicates of the transitions from microstate A (`A to B`, `A to C`, `A to D`, `A to E`):
  - `A to B`: SA = $2.55(0.11)$, SI = $3.12(0.17)$, NP = $1.02(0.14)$, $F = 60.43, p < 0.01$ vs. `B to A`: SA = $2.55(0.11)$, SI = $3.12(0.17)$, NP = $1.02(0.14)$, $F = 60.43, p < 0.01$.
  - `A to C`: SA = $2.53(0.13)$, SI = $4.14(0.25)$, NP = $1.01(0.13)$, $F = 74.85, p < 0.01$ vs. `B to C`: SA = $2.53(0.13)$, SI = $4.14(0.25)$, NP = $1.01(0.13)$, $F = 74.85, p < 0.01$.
  - `A to D`: SA = $2.81(0.14)$, SI = $1.47(0.25)$, NP = $1.03(0.20)$, $F = 20.21, p < 0.01$ vs. `B to D`: SA = $2.81(0.14)$, SI = $1.47(0.25)$, NP = $1.03(0.20)$, $F = 20.21, p < 0.01$.
  - `A to E`: SA = $3.07(0.17)$, SI = $1.06(0.16)$, NP = $1.39(0.19)$, $F = 36.15, p < 0.01$ vs. `B to E`: SA = $3.06(0.17)$, SI = $1.06(0.16)$, NP = $1.39(0.19)$, $F = 36.15, p < 0.01$.
  In directional Markov transition matrices, $P(B \to C)$ and $P(B \to D)$ cannot have identical means, SEM, and $F$-statistics to $P(A \to C)$ and $P(A \to D)$. In addition, the sum of all 20 transition probabilities in Table 3 is $57.2\%$ for SA, $44.9\%$ for SI, and $30.1\%$ for NP, neither summing to $100\%$ (total transitions) nor summing to $100\%$ per outgoing state.

* **Group differences in microstate Duration, Occurrence, and Coverage (Table 2, Figure 2, Discussion): [Methodologically Flawed].**  
  In EEG microstate analysis, every time point is assigned to one of the $K=5$ microstates, so the percentage of total time spent in state $k$ ($\text{Coverage}_k$, in $\%$) must equal $\text{Duration}_k\text{ (s)} \times \text{Occurrence}_k\text{ (s}^{-1}\text{)} \times 100$, and $\sum_{k=A}^E \text{Coverage}_k = 100\%$. In Table 2:
  1. The sum of mean coverages across microstates A–E is $75.01\%$ for SA, $72.82\%$ for SI, and only $63.90\%$ for NP, leaving $25\%$–$36\%$ of the recording unaccounted for.
  2. In Table 2, the omnibus ANOVA for Occurrence of microstate B is **non-significant** ($F = 2.43, p = 0.09$), yet the table lists significant post-hoc comparisons (`SA/SI > NP`), and the Abstract, Results, and Discussion repeatedly claim that SA and SI had significantly greater occurrence of microstate B than NP.
  3. The Discussion (page 9) states: "Our study revealed that the SA group exhibited more extensive microstate D coverage compared to the SI group," and "regression analyses revealed significant positive correlations between suicide risk severity scores and microstate coverage for both microstate D and microstate E." Both statements are contradicted by Table 2 (where microstate D coverage is $16.80$ vs. $16.47$, $F = 0.86, p = 0.42$, non-significant) and Figure 3 / Section "Regression Analysis" (which reports no correlation for microstate D coverage).

* **Demographic and clinical comparability of the SA, SI, and NP cohorts (Table 1): [Methodologically Flawed].**  
  Table 1 contains pervasive arithmetic impossibilities in the Marriage and Education rows where the percentages from the Education row were pasted into the Marriage row:
  - For SI ($n_2 = 33$), Unmarried is $N = 19$ ($57.58\%$), First marriage is $N = 12$ ($36.36\%$), and Others is $N = 2$ ($6.06\%$), yet Table 1 reports $21.21\%, 66.67\%, 12.12\%$—which are the exact percentages of the SI Education row ($7/33 = 21.21\%$, $22/33 = 66.67\%$, $4/33 = 12.12\%$).
  - For NP ($n_3 = 33$), Unmarried is $N = 24$ ($72.73\%$) and First marriage is $N = 9$ ($27.27\%$), yet Table 1 reports $6.06\%, 81.82\%, 12.12\%$—which are the exact percentages of the NP Education row ($2/33 = 6.06\%$, $27/33 = 81.82\%$, $4/33 = 12.12\%$).
  - Furthermore, the Methods ("Participants") state that "the presence of... anxiety symptoms" was an exclusion criterion, yet Table 1 lists 2 participants in the SI group with a clinical diagnosis of "Anxiety disorder" and 2 with "Bipolar disorder," as well as 6/33 ($18.18\%$) of the "Normal people controls (NP)" having a clinical diagnosis of Depression.

* **Pooled regression of SBQ-R suicide risk scores against microstate D and E occurrences ($n = 64$, Figure 3): [Fragile].**  
  Pooling the SA group (mean SBQ-R $= 13.45$, mean E occurrence $= 2.46$) and SI group (mean SBQ-R $= 9.00$, mean E occurrence $= 0.81$) into a single bivariate regression ($n = 64$) confounds within-group continuous dose-response relationships with the massive between-group mean shift already tested in Table 2 ($F = 94.38$). Without controlling for group membership (SA vs. SI), the linear regressions in Figure 3 simply rediscover the group difference between attempters and ideators.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Re-Export Raw Microstate Metrics from EEGLAB and Audit Table 2 and Table 3
* **WHY:** The duplicate rows in Table 3 (`B to A/C/D/E` identical to `A to B/C/D/E`), coverage sums far below $100\%$ in Table 2, and post-hoc claims on non-significant ANOVAs ($p = 0.09$ for Occurrence B) invalidate the primary results.
* **WHAT:** Re-run the EEGLAB Microstate toolbox export script on the 97 preprocessed EEG files and replace Tables 2 and 3 with verified summary statistics.
* **HOW:** Verify that for every subject $i$, $\sum_{k=A}^E \text{Coverage}_{i,k} = 100\%$ and $\text{Coverage}_{i,k} = \text{Duration}_{i,k} \times \text{Occurrence}_{i,k}$. Re-export the 20 directional transition probabilities $T_{j \to k}$ ensuring that transitions out of state B are actually extracted from row B of the transition matrix rather than duplicated from row A. Apply false discovery rate (FDR) correction across the 15 state metrics in Table 2 and the 20 transition tests in Table 3.

#### 2. Remove Unsupported Claims About Microstate B Occurrence and Microstate D Coverage
* **WHY:** Occurrence of microstate B is non-significant ($F = 2.43, p = 0.09$) and Coverage of microstate D is non-significant ($F = 0.86, p = 0.42$).
* **WHAT:** Remove `SA/SI > NP` from the Occurrence B row of Table 2, and delete the claims in the Abstract, Results, and Discussion that microstate B occurrence and microstate D coverage differed significantly between groups or correlated with suicide risk.
* **HOW:** Update the Abstract, Section "Microstate Duration, Occurrence, and Coverage," and the fifth and sixth paragraphs of the Discussion to reflect only statistically significant effects after multiple-testing correction.

#### 3. Test Within-Group Associations in the Suicide Risk Regressions
* **WHY:** Regressing SBQ-R on microstate parameters across the pooled SA+SI cohort ($n=64$) is driven by ecological clustering (Simpson's paradox / group confounding) between the SA and SI groups.
* **WHAT:** Include Group (SA vs. SI) and BDI-II depression score as covariates in the regression models, and report within-group correlations separately for SA ($n=31$) and SI ($n=33$).
* **HOW:** Fit the multiple linear regression $\text{SBQ-R}_i = \beta_0 + \beta_1 \text{Microstate}_i + \beta_2 \mathbb{I}(\text{Group}_i = \text{SA}) + \beta_3 \text{BDI-II}_i + \epsilon_i$ and report the partial $R^2$ and $p$-value for $\beta_1$.

#### 4. Correct Table 1 Demographic Calculations and Clarify Inclusion/Exclusion Criteria
* **WHY:** Table 1 has Education percentages pasted into the Marriage rows, and includes depressed individuals in the "normal control" group and anxiety patients despite an anxiety exclusion rule.
* **WHAT & HOW:**
  1. Recompute the Marriage percentages in Table 1: for SI ($n=33$), $19/33 = 57.58\%$, $12/33 = 36.36\%$, $2/33 = 6.06\%$; for NP ($n=33$), $24/33 = 72.73\%$, $9/33 = 27.27\%$, $0/33 = 0.00\%$; and recompute the $\chi^2$ statistic ($2.35$ is incorrect for these counts).
  2. Explain in the "Participants" section why 6/33 ($18.18\%$) of "normal people controls (NP)" had a clinical diagnosis of Depression and why 2 SI participants had Anxiety disorder despite the exclusion criteria, or re-run the microstate ANOVAs after excluding clinically depressed controls.
