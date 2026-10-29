# Review of FEXP_ANON_135

**Overall Score:** **4.8 / 10.0** (Flawed / Overstated)
* **Score Breakdown:** Rigor: 1.4/3.5 | Claims: 1.1/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.1/2.0
* **Scientific Core Score:** **3.7 / 8.0**

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_135`
* **Perceived Study Type:** Cross-sectional observational resting-state EEG study ($N = 70$ children aged 5–12 years: $n = 35$ Autism Spectrum Disorder [ASD] Level 1 vs. $n = 35$ age- and sex-matched neurotypical [NT] controls, stratified into 5–8 yr [$n = 20$/group] and 9–12 yr [$n = 15$/group] subgroups).
* **Domain & Focus:** Developmental neurophysiology and EEG biomarker analysis (19-channel eyes-open spectral band power, peak alpha frequency [PAF], and Kraskov–Stögbauer–Grassberger [KSG] Transfer Entropy [TE] effective connectivity).

---

## 2. Executive Summary & Editorial Verdict

This study analyzes 19-channel eyes-open resting-state EEG recordings from 35 children with DSM-5 ASD Level 1 and 35 age- and sex-matched neurotypical (NT) children (ages 5–12 years), comparing absolute/relative spectral power, regional peak alpha frequency (PAF), and sensor-space KSG Transfer Entropy (TE) both between diagnostic groups and across cross-sectional age strata (5–8 years, $n = 20$/group vs. 9–12 years, $n = 15$/group).

**Editorial Verdict:** **Major Revision / Re-Analysis Required (Core Developmental Claims Flawed by Interaction Fallacy and Sensor-Space TE Confounding).** While the group-level reduction in posterior alpha power in ASD ($p < 10^{-5}$ at O1/O2, Bonferroni-corrected) is well supported and consistent with prior literature, the manuscript's central claims of "disrupted developmental trajectories" across age in alpha power, PAF, and Transfer Entropy rest on the **difference-in-nominal-significance fallacy** (comparing separate within-group $p$-values without ever testing a $\text{Group} \times \text{Age}$ interaction). In fact, for occipital PAF (`Figure 5a`), the continuous age correlation in ASD ($\rho = 0.544, p = 0.0044$) is virtually identical to that in NT ($\rho = 0.564, p = 0.0025$), and in the parietal and temporal lobes, age correlations are statistically significant *only* in the ASD group ($\rho = 0.582$ and $\rho = 0.567$) and not in NT ($\rho = 0.327$ and $\rho = 0.438$)—directly contradicting the narrative of impaired PAF maturation in ASD! Furthermore, computing KSG Transfer Entropy directly on 19 scalp-referenced channels without surface Laplacian/source reconstruction, without specifying embedding dimensions ($k, l$) or time lag, and across variable-length concatenated recordings ($7.2 \pm 2.3\text{ min}$, range $5\text{--}30\text{ min}$) confounds directed information flow with volume conduction, alpha signal-to-noise differences, and sample-length estimator bias.

### Assessment of Specific Conclusions & Support

* **Children with ASD Level 1 exhibit reduced posterior (occipital/parietal) absolute and relative alpha power during eyes-open rest compared with neurotypical controls: [Well Supported].**  
  Two-tailed Mann–Whitney $U$-tests with Bonferroni correction across 76 channel-band pairs (19 channels $\times$ 4 bands) demonstrate robust reductions in occipital log-alpha power (`O1`: $p = 6.89 \times 10^{-6}$; `O2`: $p = 1.06 \times 10^{-6}$) and relative alpha power (`O1`: $p = 0.0010$; `O2`: $p = 0.00014$) in the matched $35\text{ vs. }35$ sample.

* **Age-related maturation of occipital alpha power is disrupted in ASD compared with NT children: [Fragile].**  
  In continuous analyses (`Figure 4a`), occipital alpha power correlates negatively with age in NT ($\rho = -0.469, p = 0.027$) and negatively in ASD ($\rho = -0.318, p = 0.375$). However, a formal Fisher $z$-test comparing these two correlation coefficients ($\rho = -0.469$ vs. $\rho = -0.318$ at $n = 35$) yields $z = -0.72, p = 0.47$, demonstrating **no statistically significant difference in age slopes between ASD and NT**. Dichotomizing age into small subgroups ($n = 20$ vs. $n = 15$) and contrasting $p = 0.012$ in NT against $p = 0.131$ in ASD without an interaction test does not establish a group difference in trajectory.

* **Occipital peak alpha frequency (PAF) shows disrupted age-related neurodevelopmental progression in ASD: [Methodologically Flawed].**  
  Directly contradicted by the authors' own continuous correlation data in `Figure 5a–c`: occipital PAF increases strongly and almost identically with age in both ASD ($\rho = 0.544, p = 0.0044$) and NT ($\rho = 0.564, p = 0.0025$), while parietal ($\rho = 0.582, p = 0.0015$) and temporal ($\rho = 0.567, p = 0.0023$) PAF increase significantly with age in ASD but *not* in NT ($p = 0.333$ and $p = 0.051$). Claiming that PAF maturation is disrupted in ASD based solely on a dichotomized subgroup split ($n = 20$ vs. $n = 15$) where NT reached $p = 0.036$ and ASD did not is a textbook statistical artifact of arbitrary age binning.

* **Transfer Entropy (TE) reveals a severe developmental disruption of directed brain network maturation in ASD (7 significant age-pairs in ASD vs. 150 in NT): [Methodologically Flawed].**  
  First, KSG Transfer Entropy was computed on raw 19-channel scalp potentials (`A1/A2` reference) without volume-conduction mitigation; instantaneous volume conduction and strong group differences in occipital alpha amplitude/SNR corrupt sensor-space TE. Second, TE was computed over the *"full epoch window"* of retained data, which varied widely in duration across subjects ($7.2 \pm 2.3\text{ min}$, from $5$ to $30\text{ min}$); KSG $k$-NN entropy estimators exhibit systematic bias as a function of time-series length $N$. Third, no $\text{Group} \times \text{Age}$ interaction test was performed in the Network-Based Statistics (NBS) framework.

---

## 3. Forensic Defect Inventory

### 1. Failure to Test `Group × Age` Interactions (Difference-in-Nominal-Significance Fallacy) and Contradictory PAF Correlations (Pillar 3, Pillar 4 & Pillar 5)
* **Defect:** Throughout `Figures 4, 5, and 7`, the authors test age effects separately within NT ($n = 35$, or $20\text{ vs. }15$) and within ASD ($n = 35$, or $20\text{ vs. }15$), concluding that maturation is disrupted whenever NT crosses $p < 0.05$ and ASD does not. As shown by Nieuwenhuis et al. (2011), comparing two nominal $p$-values without testing the interaction term ($\text{Group} \times \text{Age}$) has an error rate up to 50%. In `Figure 5a`, continuous age correlations for occipital PAF are virtually identical in ASD ($\rho = 0.544$) and NT ($\rho = 0.564$), yet the authors use an underpowered binary split ($20\text{ vs. }15$) to claim disrupted PAF maturation in ASD.
* **Actionable Fix:** Fit formal linear/rank regression models including the $\text{Group} \times \text{Age}$ interaction term ($Y = \beta_0 + \beta_1\text{Group} + \beta_2\text{Age} + \beta_3(\text{Group} \times \text{Age}) + \epsilon$) for alpha power, PAF, and TE (and in NBS, test the $2 \times 2$ interaction contrast `(NT_9-12 - NT_5-8) - (ASD_9-12 - ASD_5-8)` via permutation). Temper all developmental claims where $\beta_3$ is non-significant.

### 2. Uncontrolled Epoch-Length Bias, Missing Embedding Parameters, and Volume Conduction in KSG Transfer Entropy (Pillar 3 & Pillar 7)
* **Defect:**
  1. **Variable Recording Length Bias:** Section `EEG acquisition and preprocessing` notes that recordings lasted *"at least 5 min (30 min maximum)"* with retained data averaging $7.2 \pm 2.3\text{ min}$ ($110,592 \pm 35,328$ samples at $256\text{ Hz}$). Section `Transfer entropy` states: *"For each subject, TE was computed across the full epoch window"*. Because KSG conditional mutual information estimates depend on neighbor distances in state space, unequal sample counts $N$ across subjects introduce systematic bias and variance differences, and concatenating manually spliced artifact-free segments introduces discontinuous jumps at splice boundaries.
  2. **Missing Mathematical Parameters & Broken Equations:** In Section `Transfer entropy` (lines 130–133 and offset lines 1–5), all mathematical symbols and equations were stripped or left blank (`where [blank] is the future value...`), and the embedding history lengths $k$ and $l$, the time delay $\tau$, the prediction horizon $u$, and the KSG neighbor parameter ($k_{\text{NN}}$, described only as *"typically 4–5"*) are never specified!
  3. **Volume Conduction & High Impedance:** Scalp potentials recorded with a 50 $\text{k}\Omega$ impedance threshold (`maintained below 50 kΩ`) and linked-ear reference (`A1/A2`) suffer from instantaneous volume conduction, which produces spurious directed TE whenever two coupled or common-reference channels differ in signal-to-noise ratio (such as the large occipital alpha power difference between NT and ASD).
* **Actionable Fix:** Standardize TE computation to a fixed total duration (e.g., non-overlapping 4-s or 10-s artifact-free epochs totaling exactly $4\text{ min}$ per subject, computing TE within contiguous epochs rather than across spliced discontinuities), apply a Surface Laplacian (Current Source Density) transformation or time-reversed TE control ($\Delta\text{TE} = \text{TE}_{X \to Y} - \text{TE}_{X_{\text{rev}} \to Y_{\text{rev}}}$) to eliminate volume-conduction artifacts, and restore all missing equations and exact parameter values ($k, l, \tau, k_{\text{NN}}$).

### 3. Mathematical Error in Cliff's Delta ($\delta > 1$) Across Four Figure Legends and Excessive Numerical Precision (Pillar 7)
* **Defect:**
  1. Cliff's delta ($\delta = \frac{\#(x_i > y_j) - \#(x_i < y_j)}{n_x n_y}$) is strictly bounded on the closed interval $[-1, +1]$. However, the captions of `Figure 2` (line 49), `Figure 3` (line 54), `Figure 6` (line 82), and `Figure 7` (line 87) all state: *"Warm colors (reds) display a positive value ($\delta > 1$), indicating ASD power is more than NT power. In contrast, cool colors (blues) present a negative value ($\delta < 1$)... Near-zero (white or neutral colors) represent no meaningful difference in the magnitude between the two groups ($\delta < 1$)."* Writing $\delta > 1$ and $\delta < 1$ instead of $\delta > 0$, $\delta < 0$, and $|\delta| \approx 0$ is mathematically impossible.
  2. In `Results` (lines 59–74), Spearman's $\rho$ and $p$-values for $n = 35$ are reported to 9–13 significant digits (e.g., $\rho = -0.469220535, p = 0.026772192$; $p = 0.0000000828547$), representing unrounded floating-point output.
* **Actionable Fix:** Correct all four figure legends to read $\delta > 0$, $\delta < 0$, and $|\delta| < 0.147$ (negligible effect threshold), and round test statistics and $p$-values to 3 significant figures.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.4** | **3.5** | Proper Bonferroni/NBS corrections for simple two-group comparisons, but developmental trajectory claims rely on comparing separate within-group $p$-values without testing $\text{Group} \times \text{Age}$ interactions, and KSG TE is confounded by variable recording lengths and volume conduction. |
| **2. Claim-to-Evidence Alignment** | **1.1** | **2.5** | Claims that occipital PAF maturation is disrupted in ASD directly conflict with continuous correlations showing identical occipital age slopes ($\rho = 0.54$ vs. $0.56$) and stronger parietal/temporal age slopes in ASD than NT. |
| **3. Data Integrity & Biological Plausibility** | **1.2** | **2.0** | Exact age and sex matching ($35\text{ vs. }35$) and medication-free ASD Level 1 cohort are strengths, but high electrode impedance ($< 50\text{ k}\Omega$), missing IQ/cognitive scores, and unmitigated scalp volume conduction limit biological specificity. |
| **4. Reproducibility & Data Integrity** | **1.1** | **2.0** | Missing equations and undefined embedding parameters ($k, l, \tau$) in the Transfer Entropy section; impossible $\delta > 1$ Cliff's delta bounds in four figure captions; data/code available only upon request. |
| **Scientific Core Score** | **3.7** | **8.0** | Sum of Rigor + Claims + Biology (`1.4 + 1.1 + 1.2`). |
| **Overall Composite Score** | **4.8** | **10.0** | **Flawed / Overstated** (`1.4 + 1.1 + 1.2 + 1.1`). |
