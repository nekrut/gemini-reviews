# Forensic Peer Review: FEXP_ANON_123

**Overall Score:** **3.8 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.9 / 8.0**  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 1.0/2.5 | Biology: 1.0/2.0 | Reproducibility: 0.9/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_123`
* **Perceived Domain & Topic:** Clinical Neuroimaging / Post-COVID-19 Sleep Medicine / Psychiatry; longitudinal resting-state fMRI functional connectivity (rs-FC) of sleep problems (SP) following SARS-CoV-2 infection.
* **Perceived Empirical Scope:** $N = 88$ post-COVID-19 participants at baseline ($n = 55$ with new-onset sleep problems [`COVID_SP`, post-COVID $\text{PSQI} > 7$, pre-COVID $\text{PSQI} \le 7$] and $n = 33$ without sleep problems [`COVID_NSP`, pre- and post-COVID $\text{PSQI} \le 7$]), with $N = 58$ retained at 2-month follow-up ($n = 39$ `COVID_SP`, $n = 19$ `COVID_NSP`); 3T Siemens Prisma rs-fMRI analyzed in DPABI v8.1 across all 246 Brainnetome Atlas seeds; PSQI, GAD-7, and PHQ-9 scales evaluated via RM-ANOVA and voxelwise correlation maps.

---

## 2. Executive Summary & Editorial Verdict

This study compares resting-state functional connectivity (rs-FC) and clinical sleep/mood scales (PSQI, GAD-7, PHQ-9) between COVID-19 survivors with new-onset sleep problems (`COVID_SP`, $n = 55$ at baseline, $n = 39$ at 2 months) and those without sleep problems (`COVID_NSP`, $n = 33$ at baseline, $n = 19$ at 2 months). Using all 246 regions of the Brainnetome Atlas as whole-brain seeds with Gaussian Random Field (GRF) correction, the authors report baseline hyperconnectivity in `COVID_SP` (involving precentral gyrus, lateral occipital cortex, inferior parietal lobule, superior/inferior frontal gyri, and hippocampus), widespread longitudinal FC changes at 2-month follow-up correlating with PSQI, GAD-7, and PHQ-9 shifts, and significant group-by-time interactions in RM-ANOVA.

**Editorial Verdict: Reject / Severe Multiple-Testing Inflation and Pervasive Tabular/Anatomical Errors (3.8 / 10.0).** While the Limitations section is unusually candid in acknowledging the absence of pre-infection MRI, retrospective recall bias in pre-COVID PSQI ratings, and evening scan timing (18:00–22:00), the statistical analysis and data tables contain critical flaws:
1. **Unadjusted whole-brain testing across 246 Brainnetome Atlas seeds at lenient GRF thresholds:** The authors computed 246 separate seed-to-whole-brain voxelwise connectivity maps per contrast and applied GRF correction at primary voxel thresholds of $p < 0.005$ or $p < 0.001$ (cluster $p < 0.05$, two-tailed) without any family-wise or FDR correction across the **246 seeds**. At $\alpha = 0.05$ per seed map (and with parametric GRF at voxel $p < 0.005$ already known to exhibit inflated false-positive rates; Eklund et al. 2016), testing 246 seeds guarantees $>12$ false-positive seed maps per contrast by chance alone.
2. **Swapped rows, miscalculated $t$-tests, and impossible $p$-values in Tables 1 and 4:**
   - In **Table 1** (line 100), baseline age is $30.89 \pm 8.51$ ($n = 55$) vs. $26.40 \pm 8.95$ ($n = 33$), which yields $t_{86} = 2.350, \mathbf{p = 0.021}$ (a statistically significant baseline age difference), yet Table 1 reports $P = 0.274$.
   - In **Table 4** (lines 162–163), the repeated-measures $F$ and $p$ statistics for `COVID SP` ($F = 0.349, p = 0.707$) and `COVID NSP` ($F = 14.536, p < 0.001$) are **swapped between the two rows**, directly contradicting the means and post-hoc symbols in the same row and the narrative in line 148. Moreover, the bottom row of Table 4 (line 165) reports $F = 1.37, P = 0.024$, whereas $F_{1,56} = 1.37$ corresponds to $p = 0.247$ (as correctly printed in Table 2, line 138).
3. **Anatomical and MNI coordinate contradictions in the main findings:** The baseline PSQI correlation is attributed to the **left** hippocampus in the Abstract (line 11), Figure 3B (line 180), and Discussion (line 216), but to the **right** hippocampus in the Results (line 177). At follow-up, the PSQI correlation at MNI `[54, -9, -27]` is labeled as right middle **frontal** gyrus (`MFG`) in the Results (line 198), but `[54, -9, -27]` lies in the right middle **temporal** gyrus (`MTG`, as written in Discussion line 220).

### Assessment of Specific Claims

* **Claim 1 (PSQI, GAD-7, and PHQ-9 scores increased significantly after COVID-19 in the `COVID_SP` group and partially recovered by the 2-month follow-up): `[Moderately Supported]`.**  
  The longitudinal improvement from baseline to 2-month follow-up is prospective, although the "pre-COVID" baseline was collected retrospectively after infection (subject to recall bias), the group split was defined on post-COVID PSQI $>7$, and Table 4 has swapped row statistics and a mistyped $p$-value ($0.024$ instead of $0.247$).
* **Claim 2 (At baseline, `COVID_SP` exhibits elevated seed-to-voxel FC in `PrG_R`, `IPL_L`, and `Hipp_L`, and hippocampal–right SFG FC correlates positively with PSQI): `[Fragile]`.**  
  Conducting 246 unadjusted whole-brain seed analyses at voxel $p < 0.005$ (cluster GRF $p < 0.05$) without correcting for 246 seeds produces severe multiplicity inflation. Additionally, the text contradicts itself on whether the correlated seed is the left hippocampus (lines 11, 180, 216) or right hippocampus (line 177).
* **Claim 3 (Over the 2-month follow-up, widespread FC changes across dozens of frontal, temporal, parietal, occipital, and subcortical regions correlate with changes in PSQI, GAD-7, and PHQ-9): `[Methodologically Flawed]`.**  
  With 34% attrition ($30/88$ dropouts), running unadjusted whole-brain paired $t$-tests and voxelwise correlation maps across 246 seeds $\times$ 3 clinical scales at voxel $p < 0.005$ generates massive false-positive sprawl, compounded by mislabeling temporal MNI coordinates (`[54, -9, -27]`) as middle frontal gyrus (`MFG`).
* **Claim 4 (RM-ANOVA of extracted baseline-defined ROI pairs demonstrates significant group $\times$ time interactions in `PrG_R–PrG_R`, `IPL_L–SFG_R`, and `Hipp_L–IFG_R`): `[Fragile]`.**  
  Selecting clusters that differed significantly between groups at baseline ($t_1$) and testing them for group $\times$ time interaction across $t_1$ and $t_2$ without independent ROI definition is susceptible to regression-to-the-mean between baseline and follow-up.

---

## 3. Forensic Defect Inventory

### Defect 1: Uncorrected Multiplicity Across 246 Brainnetome Seeds and Copy-Pasted ALFF Preprocessing Steps [ Pillar 3, Pillar 4 — Critical ]
* **Location:** Section "MRI Data Processing" (line 81), Section "Statistical Analysis" (line 86), and Results (lines 177, 193, 198).
* **Forensic Evidence:**
  1. **246 unadjusted whole-brain seed maps:** Line 81 states that all 246 regions of the Brainnetome Atlas were used as seed points for voxelwise whole-brain connectivity. Line 86 and Results lines 177 and 198 show that GRF correction was applied at the single-map level (`voxel p < 0.001/0.005, cluster p < 0.05, two-tailed`) without any correction across the 246 seeds. Even if single-map FWE were controlled at $\alpha = 0.05$, testing 246 seeds yields an expected $246 \times 0.05 = 12.3$ false-positive clusters per contrast under the global null; moreover, two-tailed GRF at primary threshold $p < 0.005$ in smoothed fMRI data has substantially inflated false-positive rates (Eklund et al. 2016).
  2. **ALFF steps erroneously inserted into the FC pipeline:** In line 81, steps (7) and (8) state: *"(7) Power spectrum calculation: each voxel's time series was transformed into the frequency domain using a fast Fourier transform to calculate the power spectrum. (8) Frequency band selection: the square root of each voxel's signal within the 0.01–0.08 Hz frequency band was calculated and mean-centered."* Taking the square root of the FFT power spectrum computes a single static **ALFF** scalar per voxel, not a temporal BOLD time series for Pearson correlation in step (10).
* **Fix:** Either compute the $246 \times 246$ ROI-to-ROI functional connectivity matrix and control false discovery rate (FDR $q < 0.05$ or Network-Based Statistic, NBS) across all $246 \times 245 / 2 = 30,135$ edges, or restrict seed-to-voxel analyses to a small number of a priori hypothesis-driven seeds with Bonferroni correction ($\alpha = 0.05 / K$) and stringent permutation/non-parametric cluster thresholding ($p_{\text{voxel}} < 0.001$). Remove the erroneous ALFF description from steps (7)–(8) of line 81.

### Defect 2: Miscalculated Baseline Age $p$-Value, Swapped Table Rows, and Mistyped $p$-Values in Tables 1 and 4 [ Pillar 4, Pillar 7 — Critical ]
* **Location:** Table 1 (lines 100, 109), Table 2 (line 138), and Table 4 (lines 159–165).
* **Forensic Evidence:**
  1. **Baseline age difference misreported as non-significant in Table 1:** In Table 1 (line 100), `Age (years)` is $30.89 \pm 8.51$ ($n = 55$) in `COVID_SP` vs. $26.40 \pm 8.95$ ($n = 33$) in `COVID_NSP`. A two-sample $t$-test yields $t_{86} = 2.350, \mathbf{p = 0.021}$ (Welch's $t_{64.7} = 2.321, \mathbf{p = 0.023}$), contradicting the reported $P = 0.274$ and the Abstract's claim (line 9) that the groups were *"matched for demographics."*
  2. **Impossible SD for pre-COVID habitual sleep efficiency in Table 1:** Line 109 reports `Habitual sleep efficiency`: $0.47 \pm 0.06$ ($n = 55$) and $0.42 \pm 0.07$ ($n = 33$). Because PSQI component scores only take integer values $\{0, 1, 2, 3\}$, a sample with mean $0.47$ must have $\text{SD} \ge \sqrt{\frac{n}{n-1}(0.47)(0.53)} = 0.504$; values of $0.06$ and $0.07$ are either standard errors (SEM) or decimal typos.
  3. **Swapped `F` and `p` rows in Table 4:** In Table 4 (lines 162–163), the `COVID SP` row ($2.282 \to 5.513 \to 3.718$) is assigned $F = 0.349, p = 0.707$, while the `COVID NSP` row ($2.000 \to 2.684 \to 2.632$) is assigned $F = 14.536, p < 0.001$. The $F$ and $p$ values of the two rows were transposed.
  4. **Mistyped follow-up $p$-value in Table 4:** In the bottom row of Table 4 (line 165), the follow-up between-group comparison reports $F = 1.37, P = 0.024$. For $F_{1,56} = 1.37$, the exact $p$-value is **$0.247$** (matching Table 2 line 138: $P = 0.247$), not $0.024$.
* **Fix:** Correct the baseline age $p$-value in Table 1 ($p = 0.021$), verify whether `0.06`/`0.07` in line 109 are SEMs, unswap the `F` and `p` values between `COVID SP` and `COVID NSP` in Table 4, and correct `0.024` to `0.247` in Table 4 line 165.

### Defect 3: Anatomical Lateralization Contradictions, Mislabeled MNI Coordinates, and Inconsistent Participant Counts [ Pillar 6, Pillar 7 — Major ]
* **Location:** Abstract (line 11), Methods (line 68), Results (lines 94, 177, 180, 198), and Discussion (lines 216, 220).
* **Forensic Evidence:**
  1. **Left vs. Right Hippocampus contradiction:** The baseline correlation with PSQI is reported as involving the **left hippocampus** in the Abstract (line 11), Figure 3B caption (line 180), and Discussion (line 216), but as the **right hippocampus** in the Results text (line 177: *"regarding the FC for the right hippocampus and right SFG"*).
  2. **MNI coordinate `[54, -9, -27]` mislabeled as Right MFG:** Results line 198 reports *"changes in FC between the right BG and right MFG (R2 = 0.3801... peak MNI coordinates: 54, -9, -27)"*, whereas Discussion line 220 refers to *"the FC between the right BG and right MTG."* In MNI152 space, coordinates $(+54, -9, -27)$ are located in the **right middle/inferior temporal gyrus (`MTG`/`ITG`)**, nowhere near the middle frontal gyrus (`MFG`).
  3. **Participant count contradiction:** Results line 94 states that *"Initially, 115 individuals completed both baseline and follow-up scans"*, and after 27 exclusions ($6 + 1 + 10 + 10 = 27$), 88 participants remained. However, Methods line 68 and Tables 1–2 show that 88 participants completed the **baseline** scan, after which 30 participants dropped out ($16$ SP + $14$ NSP), leaving only **58** participants who completed both baseline and follow-up scans.
  4. **Abbreviation error:** Line 6 (chunk 2) defines `PSQI` as *"Pittsburgh Sleep Quality Index-9"* (PSQI has 7 components / 19 items, not 9).

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.9** | **3.5** | Runs 246 unadjusted whole-brain seed analyses at lenient GRF thresholds (`voxel p < 0.005`); swaps row $F$/$p$ values and misprints $p=0.247$ as $0.024$ in Table 4; miscalculates baseline age $t$-test ($p=0.021$ reported as $0.274$). |
| **2. Claim-to-Evidence Alignment** | **1.0** | **2.5** | While the Limitations section candidly acknowledges retrospective PSQI recall bias, evening scan timing, and lack of pre-COVID MRI, the Results and Abstract present unadjusted 246-seed false-positive sprawl and contradicted anatomical regions as robust findings. |
| **3. Data Integrity & Biological Plausibility** | **1.0** | **2.0** | Longitudinal 2-month follow-up of 58 COVID-19 survivors is useful, but undermined by anatomical coordinate mislabeling (`[54, -9, -27]` temporal cortex labeled as `MFG`) and left/right hippocampal contradictions. |
| **4. Reproducibility & Data Integrity** | **0.9** | **2.0** | Multiple arithmetic and transcription errors across Tables 1 and 4, contradictory participant counts ($115$ vs. $88$ vs. $58$), copy-pasted ALFF steps in the FC pipeline, and data only available upon request. |
| **Total Composite Score** | **3.8** | **10.0** | **Flawed / Overstated** (Scientific Core Score: **2.9 / 8.0**) |
