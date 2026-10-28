# Review of ANON_142

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.3 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.1/3.5 | Claims: 1.2/2.5 | Biology: 1.1/2.0 | Reproducibility: 0.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study evaluates the effects of a 12-month dietary salt intervention (1.5 g/day for months 0–6, increased to 2.0 g/day for months 6–12) on blood pressure (BP), serum biochemistry, and gut microbiome composition (via Ion Torrent 16S rRNA V2–V9 sequencing at baseline $T_0$ and 6 months $T_6$) in 16 captive-bred adult vervet monkeys (*Chlorocebus aethiops*, $n = 8$ control, $n = 8$ experimental; 4 males and 4 females per group). The authors report that systolic BP in the experimental group rose from $125.5 \pm 41.9\text{ mmHg}$ at $T_0$ to $171.3 \pm 35.4\text{ mmHg}$ at $T_{12}$ ($p = 0.0034$ vs. control at $T_{12}$), while serum chloride ($p = 0.004$ global) and alkaline phosphatase (ALP) showed time-point differences. In the 16S rRNA analysis (~2.7 million mapped reads per time point), alpha diversity (Chao1, Shannon, Simpson) and beta diversity (Bray-Curtis PCoA) did not differ significantly between control and experimental groups at $T_0$ or $T_6$, although both groups exhibited large longitudinal shifts between $T_0$ and $T_6$ ($p < 0.0001$). Raw 16S sequencing reads are deposited in the NCBI SRA under PRJNA903662, though analysis scripts and intermediate OTU tables are not provided.

While non-human primate dietary intervention datasets are logistically challenging and valuable, the statistical design, group allocation, and microbiome analysis suffer from severe methodological flaws that undermine the manuscript's conclusions. First, groups were allocated based on baseline lipid levels rather than randomized or stratified by blood pressure, resulting in significant baseline imbalances in total cholesterol ($p = 0.04$) and HDL-C ($p = 0.01$), a borderline-hypertensive control group at baseline ($134.7\text{ mmHg}$), and unphysiologically large within-group BP standard deviations ($\pm 38.8$ to $\pm 41.9\text{ mmHg}$ under ketamine anesthesia). Second, the global repeated-measures mixed model for systolic BP is not statistically significant ($p = 0.09$, Table 2), yet the authors claim a definitive salt-induced hypertensive effect based on unadjusted post-hoc cross-sectional $t$-tests at $T_{12}$ while control BP inexplicably drops by $14.3\text{ mmHg}$. Third, stool samples were only analyzed at $T_0$ and $T_6$—when systolic BP did not significantly differ between groups ($p = 0.16$)—making it impossible to test whether the hypertension observed at $T_{12}$ is associated with gut dysbiosis. A thorough statistical re-analysis and reframing of claims are required.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Dietary salt supplementation (1.5–2.0 g/day) significantly induces hypertension and demonstrates salt sensitivity in the experimental vervet monkey group: [Overstated].**  
  In Table 2, the overall repeated-measures mixed-model global $p$-value for systolic BP across $T_0, T_6, T_{12}$ is $p = 0.09$ (non-significant), and diastolic BP is $p = 0.69$. The claimed effect relies on an isolated time-point comparison at $T_{12}$ ($p = 0.0034$), which is inflated by a concurrent $14.3\text{ mmHg}$ drop in the control group ($134.7 \to 120.4\text{ mmHg}$). Furthermore, at $T_6$ (after 6 months of 1.5 g/day salt), the between-group systolic BP difference is not statistically significant ($p = 0.16$).

* **Dietary salt intake causes significant alterations in serum chloride and alkaline phosphatase (ALP): [Fragile].**  
  The authors test 13 biochemical parameters across multiple time points without multiple-testing correction (Bonferroni or Benjamini-Hochberg FDR). For chloride (Table 2), the experimental group mean actually changes by only $+1.63\text{ mmol/L}$ over 12 months ($108.75 \to 110.38\text{ mmol/L}$, identical to the control baseline of $110.38\text{ mmol/L}$), so the apparent difference at $T_{12}$ ($p = 0.05$ in Table 2, inconsistently reported as $p = 0.03$ in the text) is driven by a decrease in the control group ($110.38 \to 107.75\text{ mmol/L}$) rather than hyperchloremia in the salt-fed animals.

* **Salt-induced hypertension in vervet monkeys is not associated with gut microbiome dysbiosis: [Methodologically Flawed].**  
  Stool samples were only sequenced at $T_0$ and $T_6$, when the experimental group did not have statistically significant hypertension compared to controls (systolic BP $p = 0.16$; diastolic BP $p = 1.00$), and no microbiome samples were collected at $T_{12}$ when the higher salt dose (2.0 g/day) and significant BP elevation occurred. Additionally, with $n = 8$ per group, the study is severely underpowered to detect moderate microbiome shifts, so failing to reject the null hypothesis at $T_6$ cannot be interpreted as evidence of no association.

* **Both control and experimental groups experienced highly significant longitudinal shifts in alpha diversity ($p < 0.0001$) and family/genus PCA scores between $T_0$ and $T_6$: [Methodologically Flawed].**  
  In the Methods, the authors state that a Wilcoxon signed-rank test was used to compare $T_0$ and $T_6$ within each group of $n = 8$ animals. However, for a paired sample of size $n = 8$, the minimum possible two-sided exact $p$-value for a Wilcoxon signed-rank test is $2 / 2^8 = 1/128 = 0.0078$ (and for an unpaired Mann-Whitney test with $n_1 = n_2 = 8$, the minimum possible $p$-value is $2 / \binom{16}{8} = 0.000155$). Reporting $p < 0.0001$ for Chao1, Shannon, and Simpson within $n = 8$ groups (Results and Fig. 3) is mathematically impossible for a valid animal-level test and indicates either pseudoreplication (testing across OTUs/reads rather than animals) or a software misapplication.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct the Longitudinal Mixed-Model Specification and Adjust for Baseline Covariates
* **WHY:** Allocating animals based on lipid profiles produced a non-randomized baseline with higher total cholesterol ($p = 0.04$) and HDL-C ($p = 0.01$) in the experimental group and higher baseline systolic BP in the control group ($134.7$ vs. $125.5\text{ mmHg}$). Moreover, Table 2 reports raw cross-sectional differences alongside mixed-model estimates without clearly testing the `Group × Time` interaction or adjusting for multiple comparisons across the 13 biochemical analytes.
* **WHAT:** Re-fit the linear mixed-effects models with baseline ($T_0$) outcome values, sex, age, and baseline lipids as covariates, explicitly report the `Group × Time` interaction $p$-value, and apply Benjamini-Hochberg FDR correction across the biochemical panel.
* **HOW:** In SAS (`PROC MIXED`) or R (`lme4`/`nlme`), specify `Y_t ~ Group * Time + Y_0 + Sex + Age + (1 | Animal_ID)` for $t \in \{T_6, T_{12}\}$. Report the exact `Group × Time` interaction $F$-test and FDR-adjusted $q$-values in Table 2.

#### 2. Audit and Correct the Impossible $p < 0.0001$ Alpha-Diversity Test Statistics and Compositional PCA
* **WHY:** As noted above, a Wilcoxon signed-rank test on $n = 8$ paired animals cannot yield $p < 0.0001$ (minimum exact $p = 0.0078$). In addition, performing standard PCA on raw OTU counts subsets within individual phyla (Table 4) violates compositional data constraints (closure/simplex geometry) and ignores zero-inflation.
* **WHAT:** Recompute animal-level paired Wilcoxon signed-rank tests (reporting exact $p$-values) for Chao1, Shannon, and Simpson indices, and replace phylum-subsetted raw PCA with centered log-ratio (CLR) transformation and PERMANOVA (`adonis2`) on Bray-Curtis and Aitchison distances.
* **HOW:** Using the `vegan` and `stats` packages in R (`wilcox.test(x_T0, x_T6, paired = TRUE, exact = TRUE)`), verify that each animal contributes exactly one summary value per time point. For beta diversity (Figure 4), run `vegan::adonis2(dist_matrix ~ Group * Time, permutations = 9999, strata = Animal_ID)` and report the $R^2$ and permutation $p$-values for `Group`, `Time`, and `Group:Time`.

#### 3. Investigate and Resolve Data Anomalies and Numerical Inconsistencies in Table 2
* **WHY:** Table 2 contains severe numerical anomalies and mismatches with the main text:
  1. For Control Sodium at $T_6$, Table 2 reports `130.50 ± 52.75 mmol/L` (compared to `149.88 ± 2.42` at $T_0$ and `149.88 ± 2.42` at $T_{12}$). A serum sodium SD of $52.75\text{ mmol/L}$ implies values below $50\text{ mmol/L}$ (incompatible with life) and is almost certainly a data-entry error (e.g., a missing value coded as `0` or a misplaced decimal) that also corrupted the $T_6$ mixed-model estimate (`2.04` vs. a raw mean difference of `20.50`).
  2. In the Results text (line 103), the authors state `"14% of the control group and 87.5% of the experimental group were hypertensive"`. With $n = 8$ animals in the control group, $1/8 = 12.5\%$ (or $1/7 = 14.3\%$ if an animal was dropped without disclosure).
  3. In the Results text (line 103), chloride at $T_{12}$ is reported as `p = 0.03`, whereas Table 2 (line 136) reports `p = 0.05`.
  4. In Table 2, the mixed-model `Estimates` row does not match the difference of the reported group means (e.g., for Systolic BP at $T_6$, $157.8 - 130.5 = 27.3$, but Estimate is `23.53`; for Diastolic BP at $T_6$, $76.1 - 70.0 = 6.1$, but Estimate is `0.07`; for Diastolic BP at $T_{12}$, $81.3 - 68.8 = 12.5$, but Estimate is `16.72`).
* **WHAT & HOW:** Audit the raw biochemistry spreadsheet for the $T_6$ Control Sodium outlier, state explicitly if any control animal was missing at $T_6$ or $T_{12}$ (explaining the 14% = 1/7 figure and the discrepancies between raw means and LS-means), and reconcile all $p$-values between the text and Table 2.

#### 4. Temper Claims Regarding Microbiome Dysbiosis and Salt Sensitivity
* **WHY:** Because microbiome sequencing was terminated at $T_6$ (before the 2.0 g/day dose escalation and before any statistically significant between-group difference in BP emerged) and both groups experienced massive synchronous shifts in alpha and beta diversity between $T_0$ and $T_6$ (likely due to seasonal diet variations in fresh produce or batch effects), the study cannot evaluate the microbiome at the hypertensive endpoint ($T_{12}$).
* **WHAT:** Revise the Abstract, Discussion, and Conclusion to state clearly that microbiome profiling was limited to the 6-month 1.5 g/day phase when BP was not yet significantly elevated relative to controls.
* **HOW:** Replace the Conclusion statement `"salt administration (1.5–2 g/day) did not cause gut microbiome dysbiosis"` with `"six months of 1.5 g/day dietary salt supplementation did not produce detectable differences in gut microbial alpha or beta diversity relative to controls, though strong longitudinal shifts occurred in both groups and microbiome composition was not assessed after the 2.0 g/day dose escalation at 12 months."`

#### 5. Technical and Editorial Cleanup
* **WHY:** Pipeline version numbers and database references contain errors.
* **WHAT & HOW:**
  1. **Materials and methods, line 90:** Correct `"Quantitative Insight In Microbial Ecology pipeline (QIIME -version 5.12.2)"`—neither QIIME 1 (which ended at v1.9.1) nor QIIME 2 (dated by year.month) has a version `5.12.2` (this likely refers to the Ion Reporter software version `5.12.2`).
  2. **Abbreviations section (lines 285–312):** Add the missing acronym keys (`ALT`, `CVD`, `GGT`, `HDL`, `LDL-C`, `OTU`, `PCA`, `PCoA`, `PUDAC`, `QIIME`, `SAMRC`, `SCFA`, `SRA`) alongside their expanded definitions.
