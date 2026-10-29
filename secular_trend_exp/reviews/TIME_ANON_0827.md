<Blinded Review: TIME_ANON_0827>
**Composite Score:** 3.4 / 10.0 (Rigor: 0.9/3.5 | Claims: 0.8/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.9/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Reject (Fundamental Flaws)
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Observational

OVERALL_SCORE: 3.4/10
VERDICT: FAILED
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This candidate-gene case-control association study genotypes two functional nonsynonymous SNPs in low-affinity IgG Fc receptors—`FCGR2A` H131R (`rs1801274`) and `FCGR3A` F158V (`rs396991`)—in 172 individuals from Baltimore, MD: 70 HIV-negative healthy controls, 43 HIV-positive Natural Virus Suppressors (NVS / elite controllers without HAART), and 59 HAART-treated HIV-positive progressors (Table 1). Using ABI SNaPshot primer extension, the authors report that carrying the high-activity `FCGR3A` V158 allele is associated with HIV seropositivity ($\text{OR} = 2.0$, $95\%\ \text{CI}: 1.07\text{–}3.73$, $p = 0.0398$), that the homozygous `158VV` genotype is enriched in HIV progressors vs NVS (6/59 [10%] vs 0/43 [0%], $p = 0.038$), and simultaneously that the double-homozygous low-activity genotype `FCGR3A 158FF + FCGR2A 131RR` is also enriched in HIV progressors vs NVS (11/60 vs 1/40 in text, $p = 0.025$, $\text{OR} = 8.76$).

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### STRENGTHS
- **Clinically distinct HIV elite controller (NVS) phenotype:** Comparing untreated HIV natural virus suppressors (mean infection duration 8.1 years) against HAART-treated progressors (mean 8.7 years) and seronegative controls from the same clinic catchment area (93–100% African American) minimizes gross continental ancestry stratification.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Severe internal sample-size contradictions and missing data across Tables 1, 2, and Text:**
  1. **Missing `FCGR2A` genotypes in Table 2 without explanation:** Table 1 states sample sizes are Controls $n=70$, Progressors $n=59$, and NVS $n=43$ (total $N=172$). In Table 2, the `FCGR3A` rows sum to $36+32+2 = 70$ Controls, $14+29+0 = 43$ NVS, and $21+32+6 = 59$ Progressors. However, in the very same Table 2, the `FCGR2A` rows sum to only **$4+21+7 = 32$ Controls** (38/70 missing!), **$9+26+10 = 45$ NVS** (2 more NVS than the 43 subjects said to exist in Table 1 and the Methods!), and **$4+20+12 = 36$ Progressors** (23/59 missing!).
  2. **Contradictory denominators in the main text (Line 37):** In Results line 37, the authors write: *"Out of 60 HIV progressors, 11 had this combined genotype [RR:FF] compared to 1/40 for NVS and 3/34 for HIV negative controls."* Where did 60 progressors, 40 NVS, and 34 controls come from when Table 1 says 59 progressors, 43 NVS, and 70 controls, and Table 2 has only 36 progressors, 45 NVS, and 32 controls genotyped for `FCGR2A`?! Even worse, in Table 2 only **12** progressors have the `RR` genotype at `FCGR2A` out of 36 typed; if 11 of them are `RR:FF`, why was the denominator changed from 36 (the number actually typed for `FCGR2A`) to 60?! Changing the denominator of a two-locus genotype frequency depending on whether `FCGR2A` failed genotyping invalidates the contingency table test.
- **Violation of Hardy-Weinberg Equilibrium (HWE) in the NVS group (`FCGR3A`):** Look at the `FCGR3A` genotype counts in the NVS cohort in Table 2: `FF = 14 (33%)`, `FV = 29 (67%)`, `VV = 0 (0%)` ($n=43$, allele frequencies $p_F = 57/86 = 0.663$, $q_V = 29/86 = 0.337$). Under HWE, the expected counts are $\text{FF} = 18.9$, $\text{FV} = 19.2$, $\text{VV} = 4.9$. Observing 29 heterozygotes (67.4% heterozygosity, exceeding the theoretical maximum HWE heterozygosity of 50% for a biallelic SNP!) and 0 `VV` homozygotes yields a severe HWE departure ($\chi^2 = 11.1$, $p = 0.00086$). In the highly homologous *FCGR3A*/*FCGR3B* segmental duplication locus on 1q23 (where *FCGR3B* constitutively carries a phenylalanine [F] at position 158 and copy number variation is common), excess `FV` heterozygotes and missing `VV` homozygotes is a classic technical artifact of co-amplifying paralogous *FCGR3B* sequences (which adds a constant `F` peak to `VV` samples, misclassifying `VV` as `FV`) when PCR specificity varies across DNA batches!
- **Incorrect description of `FCGR2A` SNP in the Introduction (Line 20):** Line 20 states: *"A single nucleotide polymorphism (SNP) in FCGR3A, substituting histidine for arginine at position 131, was linked to recurring bacterial infection in children [5]."* The H131R polymorphism is in **FCGR2A**, not `FCGR3A`.
- **Multiple post-hoc genetic models without multiple-testing correction and biologically contradictory post-hoc storytelling:** To get $p = 0.0398$ for HIV acquisition, the authors pool NVS + Progressors and test dominant V-allele carriage (or allelic association). Then, to compare Progressors vs NVS, they switch to a recessive `VV` model ($6/59$ vs $0/43$, driven by the HWE-violating $0/43$ in NVS) claiming **high-activity** FcR causes progression; then two paragraphs later they test the double-homozygous **low-activity** `FF+RR` combination ($p = 0.025$) and claim low-activity FcR *also* causes progression! None of these $p$-values ($0.0398, 0.038, 0.025$) survive Bonferroni correction across two loci, three cohorts, and multiple inheritance models (allelic, dominant, recessive, two-locus combinations).
- **Severe gender confounding (Table 1):** Controls are 38% male / 62% female, NVS are 49% male / 51% female, whereas Progressors are 70% male / 30% female, with no logistic regression adjustment for sex or age.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** The `FCGR3A` V158 allele increases susceptibility to acquiring HIV infection in seronegative individuals. `[Methodologically Flawed]` — Marginal unadjusted $p = 0.0398$ in a small sample ($N=172$) compromised by severe HWE violation in the `FV`/`VV` calls ($67\%$ `FV`, $0\%$ `VV` in NVS, $\chi^2 = 11.1, p < 0.001$) indicative of *FCGR3B* paralog cross-amplification.
- **Claim 2:** Both the homozygous high-activity `FCGR3A 158VV` genotype and the double-homozygous low-activity `FCGR3A 158FF + FCGR2A 131RR` genotype predispose to HIV disease progression. `[Methodologically Flawed]` — Relies on contradictory denominators (36 vs 59 vs 60 progressors; 45 vs 43 vs 40 NVS), unadjusted post-hoc model fishing, and unacknowledged missing genotypes for `FCGR2A` in >40% of Controls and Progressors.

### 4. Reproducibility & Data Completeness
- **Inconsistent tabular data:** Sample totals in Table 1 ($70, 59, 43$), Table 2 `FCGR2A` ($32, 36, 45$), and the main text ($34, 60, 40$) are mutually inconsistent, preventing reconstruction of the exact $2 \times 2$ contingency tables.
</Blinded Review: TIME_ANON_0827>
