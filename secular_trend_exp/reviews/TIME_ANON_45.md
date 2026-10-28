# Blinded Review: TIME_ANON_45
**Composite Score:** 2.2 / 10.0 (Rigor: 0.4/3.5 | Claims: 0.6/2.5 | Biology: 0.6/2.0 | Reproducibility: 0.6/2.0)
**Bias Category:** Severe Arithmetic/Statistical Inconsistency, Truncated Tables & Underpowered Candidate-Gene Case-Control Flaws
**Verdict:** Reject
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Epidemiological Observational

---

### 1. Executive Summary

This manuscript reports a single-center hospital-based case-control candidate-SNP study investigating the association between the *KRAS* 3'UTR `rs61764370` (T>G) polymorphism (located in a *let-7* miRNA complementary site) and lung cancer risk in 100 Iranian lung cancer patients and 100 healthy controls. Genotyping was performed by PCR-RFLP using the restriction enzyme *HinfI* with Sanger sequencing confirmation. The authors report genotype counts of `68 TT / 32 TG / 0 GG` in cases versus `93 TT / 7 TG / 0 GG` in controls, concluding that the `TG` genotype ($\text{OR} = 6.25$, $95\%\ \text{CI} = 2.605\text{--}15.00$) and `G` allele ($\text{OR} = 5.252$, $95\%\ \text{CI} = 2.259\text{--}12.208$) are strongly associated with lung cancer risk.

A forensic audit of the text and tables reveals pervasive arithmetic, statistical, and epidemiological failures that invalidate the manuscript's quantitative reporting: (1) the patients' mean age ($52\ \text{years}$) vs control mean age ($61\ \text{years}$) in the text contradicts the median ages ($57$ and $63\ \text{years}$) in Table 1, and a 9-year age gap between 100 cases and 100 controls is statistically highly significant despite the text claiming "no significant difference"; (2) Table 1 fails to present any demographic or smoking data for the 100 controls, and the smoking counts for the 100 cases in Table 1 sum to only 95 (`34 + 24 + 29 + 13 = 95`); (3) the percentages in Table 1 are not percentages at all, but exact copy-pastes of the raw counts `N` into the `%` column (even copying the median ages `57.0` and `63.0` as `57%` and `63%`!); (4) the $p$-values in Table 1 and Table 2 are mathematically impossible for the reported contingency tables; and (5) the Cases genotype distribution (`68 TT / 32 TG / 0 GG`) violates Hardy–Weinberg equilibrium ($p = 0.058$ exact, $\chi^2 = 3.63$) with a complete absence of `GG` homozygotes despite a $16\%$ minor allele frequency, raising concern for PCR-RFLP partial digestion artifacts.

---

### 2. Methodological & Statistical Audit

* **Copy-Paste Fabrication of Percentages and Missing Cases in Table 1:**
  In Table 1 (*Association between rs61764370 polymorphisms and clinicopathological parameters of lung cancer patients*), there are 68 `TT` patients and 32 `TG/GG` patients. Instead of computing column or row percentages, the authors simply copied the raw integer `N` into the `%` column for every single row:
  - For Age: `Median (quartile)` under `TT` is `N = 57.0` and `% = 57` (and no quartiles are given); under `TG/GG` it is `N = 63.0` and `% = 63`!
  - For Gender: under `TG/GG` ($N = 32$), `Male` has `N = 21` and `% = 21` (true percentage is $21/32 = 65.6\%$ or $21/68 = 30.9\%$).
  - For Smoking: the counts across all four cells are `TT Never = 34`, `TG/GG Never = 24`, `TT Smokers = 29`, `TG/GG Smokers = 13`. Their sum is $34 + 24 + 29 + 13 = 95$, leaving 5 patients unaccounted for without explanation.

* **Mathematically Impossible $p$-Values in Table 1 and Table 2:**
  When recomputing Pearson's $\chi^2$ (and Fisher's exact test) directly from the 2$\times$k contingency tables reported in Table 1 and Table 2, almost every $p$-value reported by the authors is wrong:
  1. **Table 1 — Gender (`47, 21` vs `21, 11`):** True $\chi^2 = 0.119$, $p = 0.730$ (Fisher's exact $p = 0.821$). The authors report `P = 0.37`.
  2. **Table 1 — Smoking (`34, 24` vs `29, 13`):** True $\chi^2 = 1.158$, $p = 0.282$ (Fisher's exact $p = 0.301$). The authors report `P = 0.52`.
  3. **Table 1 — Stage (`15, 5` / `19, 3` / `21, 9` / `13, 15` across Stages I–IV):** Notice that Stage IV has 13 `TT` and 15 `TG/GG` whereas Stages I–II have 34 `TT` and 8 `TG/GG`. The true 4$\times$2 $\chi^2 = 8.950$ ($df = 3$), yielding **$p = 0.030$**! Yet the authors report `P = 0.76`!
  4. **Table 1 — Grading (`19, 6` / `25, 10` / `15, 12` / `9, 4`):** True $\chi^2 = 2.912$ ($df = 3$), $p = 0.405$. The authors report `P = 0.92`.
  5. **Table 2 — Allele comparison (`T: 168 vs 193`, `G: 32 vs 7`):** While the allelic Odds Ratio is indeed $(32 \times 193) / (168 \times 7) = 6176 / 1176 = 5.2517$ ($95\%\ \text{CI} = 2.259\text{--}12.208$), the true allelic $\chi^2$ test statistic is $\chi^2 = 17.75$ ($df = 1$), which corresponds to **$p = 2.5 \times 10^{-5}$** (Fisher's exact $p = 2.6 \times 10^{-5}$). Yet in the text (Section *The association...*) and Table 2, the authors report `P = 0.011` (while reporting `P = 0.000` in the Abstract for the exact same allelic comparison, and truncating the genotype $p$-value in Table 2 as `0.`)!

* **Uncontrolled Confounding and Missing Control Group Demographics:**
  In *Clinical features of the subjects*, the authors state: *"The average age of patients group and control group were 52 years (range: 77–35 years) and 61 years (range: 77–34 years), respectively. There was no significant difference between the control group and the patients group in terms of age, sex and cigarette smoking and lung cancer occurrence."* First, a 9-year difference in mean age ($52$ vs $61\ \text{years}$) in $N = 100$ per group yields $t \approx 5.5\text{--}6.5$ ($p < 10^{-6}$) for any realistic age standard deviation ($\text{SD} \approx 10\text{--}12\ \text{years}$), and if the median age of cases in Table 1 is `57.0` (for TT) and `63.0` (for TG), it is nearly impossible for the overall mean age of cases to be `52 years`. Second, stating that there was *"no significant difference... in terms of cigarette smoking and lung cancer occurrence"* in a lung cancer study indicates severe selection bias in control recruitment, and no table of control sex or smoking rates is provided. Third, only unadjusted crude odds ratios are calculated without multivariable logistic regression adjusting for age, sex, and smoking pack-years.

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **PCR-RFLP Genotyping Design and Absence of `GG` Homozygotes (`[Methodologically Flawed]`):**
  In the *rs61764370 Genotype Determination* section, the PCR protocol contains multiple nonsensical parameters: reaction volume is stated as *"20mL"* (instead of $20\ \mu\text{L}$), thermal cycler is called *"Thermosocker"*, and the denaturation step is described as *"95 °C for two periods of 15 minutes and 10 seconds"* (a 15-minute incubation at $95^\circ\text{C}$ destroys standard *Taq* polymerase activity unless it is a specific hot-start enzyme, which is not named, and repeating 15-minute denaturation in 32 cycles is physically impossible). More importantly, `rs61764370` (T>G) is assayed by *HinfI* digestion (`5'-G^ANTC-3'`). The authors never state the amplicon length or the expected restriction fragment lengths for the `T` and `G` alleles, nor whether the amplicon contains a constitutive internal *HinfI* control site. In PCR-RFLP where the minor `G` allele creates or destroys a single restriction site, incomplete enzymatic digestion of `TT` homozygotes produces an uncut + cut double band identical to a `TG` heterozygote, while never producing a `GG` homozygote—matching the suspicious observation of `32 TG / 0 GG` in cases ($p_{\text{HWE}} = 0.058$).

* **Overstated Biomarker Claim (`[Overstated]`):**
  Claiming that `rs61764370` can be used as a clinical biomarker for early lung cancer detection based on an unadjusted $N = 100$ case-control study with corrupted statistical tables and an implausible $\text{OR} = 6.25$ (when large-scale GWAS and meta-analyses of lung cancer find $\text{OR} \approx 1.00\text{--}1.08$ for `rs61764370`) is unsupported.

---

### 4. Reproducibility & Data Completeness

* **Deficiencies:**
  1. The restriction fragment sizes before and after *HinfI* cleavage are completely omitted from the Methods and Figure 1 legend.
  2. Demographic and exposure data (age distribution, sex, smoking history) for the 100 healthy controls are completely missing from the manuscript.
  3. Multiple typographical errors pervade the text (`thinformation forms`, `20mL`, `Thermosocker`, `KARS gene`, `rs6176437`, `span/play`, `they span described`, and `Rs61764370 G>T` in Table 2 contradicting `T>G` in the text).
