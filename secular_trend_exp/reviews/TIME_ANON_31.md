# Blinded Review: TIME_ANON_31
**Composite Score:** 2.8 / 10.0 (Rigor: 0.8/3.5 | Claims: 0.7/2.5 | Biology: 0.7/2.0 | Reproducibility: 0.6/2.0)
**Bias Category:** Severely Underpowered Null Claim, Internal Table/Text Contradictions, and Defective Primer Specification
**Verdict:** Reject
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Epidemiological Observational

---

### 1. Executive Summary

This manuscript reports a single-center case-control study investigating the association of two *ADIPOQ* gene polymorphisms (`rs1501299` and `rs17300539`) with polycystic ovary syndrome (PCOS) and clinical hormone levels in 45 PCOS patients and 45 healthy controls in Turkey. Genotyping was performed via SYBR Green real-time PCR, and clinical variables and genotype distributions were evaluated by univariate tests and logistic regression. The authors find no statistically significant differences in allele or genotype frequencies between cases and controls ($p > 0.05$) and conclude that neither polymorphism is associated with PCOS in this population.

This study is fundamentally invalid due to four converging methodological and reporting failures: (1) the sample size ($n = 45$ per group) yields a post-hoc statistical power of 5% for `rs1501299` and 13% for `rs17300539`, rendering the primary conclusion of "no association" an uninformative Type II error; (2) the Abstract directly contradicts the Results and Table 3 by claiming that testosterone and progesterone levels were "significantly affected by polymorphisms"; (3) Table 3 ("Comparison of clinical characteristics between genotypes in the case group") contains impossible means and duplicated cells indicating that cases and controls were pooled or miscalculated; and (4) the custom primer sequences reported for genotyping are oriented on the same DNA strand and cannot support PCR amplification as written.

---

### 2. Methodological & Statistical Audit

* **Conflation of Near-Zero Power with Evidence of No Association [Methodologically Flawed]:**
  In the Power Analysis section (line 146), the authors report that their study achieved a statistical power of $0.05$ (effect size $0.02$) for `rs1501299` and $0.13$ (effect size $0.08$) for `rs17300539` at $\alpha = 0.05$. A power of $0.05$ at $\alpha = 0.05$ means the test has zero discriminatory ability beyond random coin-flipping. For `rs17300539`, the minor allele frequency is $0.04$–$0.06$, with only 4 control and 5 PCOS heterozygotes (`GA`) and zero `AA` homozygotes. Despite acknowledging this limitation in the Discussion, both the Abstract (line 13) and Conclusion (line 151) state unqualified negative conclusions (*"we conclude that both rs1501299 and rs17300539 of the ADIPOQ gene are not associated with PCOS"*).

* **Direct Self-Contradiction Between Abstract and Results/Table 3 [Methodologically Flawed]:**
  The Abstract concludes (line 13): *"Testosterone and progesterone levels were significantly affected by polymorphisms."* However, the Results section (line 95) and Table 3 explicitly show that no clinical hormone parameter—including testosterone and progesterone—differed significantly across `rs1501299` or `rs17300539` genotypes ($p > 0.05$ for all comparisons except an unadjusted $p = 0.031$ for TSH under the `rs1501299` dominant model, which does not survive the stated Bonferroni correction). Testosterone and progesterone differed only between the overall PCOS and control groups (Table 1).

* **Arithmetic and Cohort-Pooling Errors in Tables 2 and 3 [Methodologically Flawed]:**
  1. **Duplicate and impossible subgroup means in Table 3:** Table 3 is titled *"Comparison of clinical characteristics between genotypes in the case group"* ($n = 45$). Yet in Table 1, the PCOS case group ($n = 45$) has a mean testosterone of $1.82 \pm 0.78\text{ nmol/L}$ and a mean progesterone of $3.88 \pm 7.8$. In Table 3, the three `rs1501299` genotypes in the "case group" have mean testosterone levels of $1.64$ (`GG`), $1.52$ (`GT`), and $1.43$ (`TT`), and mean progesterone levels of $12.0$ (`GG`), $7.1$ (`GT`), and $14.2$ (`TT`). It is mathematically impossible for every mutually exclusive subgroup of the case cohort to have a mean testosterone below $1.65$ when the overall case cohort mean is $1.82$, or for every subgroup to have a mean progesterone between $7.1$ and $14.2$ when the overall case cohort mean is $3.88$. Conversely, pooling the $n = 45$ controls (mean testosterone $1.30$, mean progesterone $15.6$) and $n = 45$ cases (mean testosterone $1.82$, mean progesterone $3.88$) yields grand means of $1.56\text{ nmol/L}$ and $9.74$, which exactly match the weighted averages of the values in Table 3 (e.g., for `rs17300539`, $81 \times 9.98 + 9 \times 7.48 / 90 = 9.73$). Thus, Table 3 was computed on the pooled $N = 90$ sample (cases + controls combined) while mislabeled as the case group.
  2. **Copy-paste duplication across different SNPs in Table 3:** In Table 3, the BMI values for `rs1501299` `GG` ($n=37$ pooled) and `GT` ($n=45$ pooled) are reported as `23.6±3.69` and `26.1±6.77`. Under `rs17300539`, where the genotype counts are completely different (`GG` $n=81$ pooled, `GA` $n=9$ pooled), the BMI values for `GG` and `GA` are reported as the exact same numbers: `23.6±3.69` and `26.1±6.77`.
  3. **Internal inconsistency between identical `GG` columns in Table 3:** For `rs1501299`, the `GG` reference group is identical in the Additive model and the Dominant model (`GG` vs. `GT+TT`). Yet Table 3 reports different means/SDs for the same `GG` group across the two columns: BMI is `23.6±3.69` vs. `23.5±3.69`, Insulin is `166±123` vs. `167±123`, Progesterone is `12.0±14.8` vs. `11.0±14.7`, and Prolactin is `12.8±7.15` vs. `12.85±7.15`.
  4. **Percentage typo in Table 2:** In Table 2, the PCOS `GG` count for `rs1501299` is listed as `17 (38)` under the three-genotype comparison ($17/45 = 37.8\%$), but four lines below under the dominant model comparison it is listed as `17 (28)`.

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **Defective Primer Design and Unspecified SYBR Green Genotyping Assay [Methodologically Flawed]:**
  In the Methods section (line 37), the authors state that genotyping was performed by *"The Ct threshold method using cybergreen dye"* using the following primer pairs:
  * `rs1501299` forward: `3'-TGTGTCTAGGCCTTAGTTAATAATGAATTC-5'` and reverse: `3'-CTGTGTCTAGGCCTTAGTTAATAATGAATTA-5'`
  * `rs17300539` forward: `3'-AGAATGTGTGGCTTGCAAGAACTG-5'` and reverse: `3'-CAGAATGTGTGGCTTGCAAGAACTA-5'`
  In both pairs, the "forward" and "reverse" primers are identical sequences on the same strand differing only by a single terminal base (`C` vs. `A`, or `G` vs. `A`) and one extra nucleotide at the opposite end. These are two allele-specific primers in the same orientation, not a forward and reverse PCR primer pair; without a common reverse primer on the complementary strand, PCR amplification is biochemically impossible.

* **Uncontrolled Menstrual Cycle Timing and Unit Ambiguity for Hormones [Fragile]:**
  Patients were diagnosed using only two of the Rotterdam criteria (oligo/anovulation and polycystic ovaries), and the timing of blood draw relative to the menstrual cycle phase (follicular vs. luteal phase) is never specified. Because progesterone rises more than 10-fold during the luteal phase following ovulation, comparing random-phase progesterone between ovulatory controls ($15.6 \pm 13.1$) and oligo/anovulatory PCOS patients ($3.88 \pm 7.8$) simply reflects the presence vs. absence of a corpus luteum rather than a primary genetic effect. Moreover, Tables 1 and 3 label the row simultaneously as `Progesterone (ng/mL) (nmol/L)`, which differ by a molecular weight conversion factor of $3.18$. Finally, serum adiponectin protein levels were not measured, preventing any functional validation of *ADIPOQ* expression.

---

### 4. Reproducibility & Data Completeness

Reproducibility is severely deficient. Raw genotype and clinical data are withheld ("available from the corresponding author upon reasonable request"). As documented above, the primer sequences in the Methods section omit the reverse primers required to run the PCR reaction and reverse standard `5'->3'` notation. The covariates used in the "Adjusted model a" of Table 2 lack a corresponding table footnote (the Discussion mentions HOMA-IR on line 135, whereas Table 2 provides no definition of `a`), and the summary statistics in Table 3 cannot be reconciled with Table 1.
