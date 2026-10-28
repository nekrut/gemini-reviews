# Blinded Review: TIME_ANON_33
**Composite Score:** 5.6 / 10.0 (Rigor: 1.8/3.5 | Claims: 1.3/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.2/2.0)
**Bias Category:** Narrative Overreach on Null Mediating Link, Subgroup Count Discrepancies, and Unreported Dietary Analysis
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Epidemiological Observational

---

### 1. Executive Summary

This cross-sectional case-control study investigates lingual detection thresholds for oleic acid (OA), fasting metabolic/lipid profiles, and the `CD36` `rs1761667` (`G>A`) polymorphism in 165 Algerian adolescents aged 13–14 years (83 obese participants with BMI $z$-score $> 2$ and 82 lean controls with BMI $z$-score $< 1$). Using a 3-alternative forced-choice (AFC) ascending concentration staircase ($0.018$ to $12\text{ mmol/L}$ OA) and `HhaI` PCR-RFLP genotyping, the authors report that obese adolescents have a nearly twofold higher OA detection threshold than lean controls ($2.57 \pm 0.29$ vs. $1.33 \pm 0.15\text{ mmol/L}$, $p < 0.01$) and a marginally higher frequency of the `CD36` `rs1761667` A-allele ($68.1\%$ vs. $56.7\%$, $p = 0.041$). However, within this cohort, `CD36` genotype showed no association with either OA detection thresholds or BMI $z$-score ($p = 0.58$ and $p = 0.41$).

While the primary psychophysical finding—that obese adolescents exhibit higher oral detection thresholds for oleic acid alongside expected dyslipidemia and insulin resistance—is plausible and consistent with adult studies, the manuscript is weakened by several statistical and reporting flaws: (1) the Abstract frames `CD36` `rs1761667` and fat taste thresholds as jointly driving adolescent obesity despite the complete absence of an association between `CD36` genotype and OA threshold or BMI $z$-score in the data; (2) the subgroup counts in the Figure 2 legend do not sum to the group sample sizes ($45 + 41 = 86 \neq 83$ obese; $8 + 60 + 11 = 79 \neq 82$ controls); (3) genotype $p$-values in Table 2 are misreported without specifying the reference contrast; and (4) the Discussion claims an association between the A-allele and consumption of "soda and French fries" that is never described in the Methods or Results.

---

### 2. Methodological & Statistical Audit

* **Subgroup Arithmetic Mismatch in Figure 2 Legend [Methodologically Flawed]:**
  In Section 3.1 and Table 1, the sample sizes are fixed at $n = 82$ lean controls and $n = 83$ obese teenagers ($N = 165$). In the legend to Figure 2 (line 90), participants are stratified into High, Middle, and Low tasters:
  * Controls: High ($n = 8$) + Middle ($n = 60$) + Low ($n = 11$) $= 79 \neq 82$ (3 controls missing).
  * Obese: High ($n = 0$) + Middle ($n = 45$) + Low ($n = 41$) $= 86 \neq 83$ (3 extra obese subjects).
  Because $79 + 86 = 165$, three lean control subjects were erroneously shifted into the obese category when compiling the taster-group breakdown.

* **Ambiguous Genotype Testing and Uncorrected Multiple Comparisons in Table 2 [Fragile]:**
  In Table 2, genotype frequencies in Controls ($n=82$) vs. Obese ($n=83$) are `AA`: $30\ (36.6\%)$ vs. $35\ (42.2\%)$, `AG`: $33\ (40.2\%)$ vs. $43\ (51.8\%)$, and `GG`: $19\ (23.2\%)$ vs. $5\ (6.0\%)$. Table 2 lists `p = 0.008` next to `AA` and `p = 0.002` next to `AG`. A $2 \times 2$ comparison of `AA` vs. non-`AA` yields $\chi^2 = 0.54, p = 0.46$ (not $0.008$), and `AG` vs. non-`AG` yields $\chi^2 = 2.22, p = 0.14$ (not $0.002$). The reported $p = 0.008$ and $p = 0.002$ were obtained by testing $2 \times 2$ subtables of `AA` vs. `GG` ($30/19$ vs. $35/5$, Fisher's exact $p = 0.0076$) and `AG` vs. `GG` ($33/19$ vs. $43/5$, Fisher's exact $p = 0.0024$). Because both pairwise tests reuse the small `GG` count ($n = 5$ in the obese group) as the denominator without stating the reference category or reporting the $95\%$ confidence intervals for the odds ratios (Table 2 literally prints the text `"OR = 1.63; 95% CI"` and `"RR = 1.28; 95% CI"` with the numerical interval omitted in the table cell), the presentation exaggerates the statistical support for `AA` and `AG` enrichment.

* **Implausible Dispersion Estimate for Control BMI $z$-Score [Fragile]:**
  The control group is defined in Section 2.2 as lean adolescents with a BMI $z$-score $< 1$. Yet the control BMI $z$-score is reported as `0.03 ± 0.0001` in the Abstract (line 7) and `0.03 ± 0.00` in Table 1 and Section 3.1. An SEM of $0.0001$ across $n = 82$ individuals implies a standard deviation of $0.0009$—which is biologically impossible for a general population sample of 82 adolescents and indicates a calculation or spreadsheet error.

* **Extreme-Group Selection Design Without Continuous Covariate Adjustment [Moderately Supported]:**
  By excluding overweight adolescents with BMI $z$-scores between $1$ and $2$ (Section 2.2), the authors create a bimodal distribution of BMI $z$-scores ($0.03$ vs. $2.67$). Applying Spearman rank correlation across the pooled bimodal sample to claim a continuous correlation between BMI $z$-score and OA threshold (Section 3.3, $p < 0.01$) is confounded by the extreme-group gap unless also demonstrated within the lean and obese strata separately.

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **Disconnect Between `CD36` Genotype, Fat Taste Threshold, and Narrative Claims [Overstated]:**
  The central mechanistic hypothesis of the paper is that the `CD36` `rs1761667` A-allele reduces lingual CD36 expression, thereby raising the oral fat detection threshold and promoting obesity. However, Section 3.4 explicitly states: *"We did not find any significant difference between CD36 genotype and oleic acid oral sensitivity threshold. Similarly, we did not observe any significant difference between CD36 genotypes and BMI z-score neither in obese nor control teenagers (p = 0.58; p = 0.41, respectively)."* Furthermore, the actual mean OA detection thresholds stratified by `AA`, `AG`, and `GG` genotypes are never shown in a table or figure. While the Discussion candidly acknowledges this null result and speculates about circumvallate papillae maturation at ages 13–14, the Abstract glosses over the negative mediation test and implies that `rs1761667` and gustatory thresholds jointly explain adolescent obesity.

* **Unsubstantiated Dietary Claim in the Discussion [Overstated]:**
  In the Discussion (line 121), the authors write: *"A-allele was found to be associated with the intake of soda and French fries in obese children, suggesting that fat-containing products might influence, in the long-term, the fatty acid oro-sensory detection capacity."* No dietary assessment, food frequency questionnaire, or statistical analysis of soda and French fries intake is mentioned anywhere in the Experimental Section or Results (this appears to be an uncited carryover from an earlier study in younger children, Ref. 17, presented as a finding of the current study).

---

### 4. Reproducibility & Data Completeness

The psychophysical (3-AFC oleic acid emulsion preparation with $0.01\%$ acacia gum and nose clips) and genotyping (`HhaI` PCR-RFLP with primer sequences and restriction fragment lengths of $138\text{ bp}$ and $52\text{ bp}$) protocols are clearly described and reproducible. However, data completeness requires: (1) correcting the subgroup counts in Figure 2; (2) reporting the actual mean $\pm$ SEM oleic acid detection thresholds across the `AA`, `AG`, and `GG` genotypes in Table 2; (3) filling in the missing $95\%$ CI values in Table 2; (4) verifying the standard deviation/SEM of BMI $z$-score in the control group; and (5) removing or properly citing the unmeasured dietary intake claim in the Discussion.
