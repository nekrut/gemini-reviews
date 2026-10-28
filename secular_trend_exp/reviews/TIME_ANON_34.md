# Blinded Review: TIME_ANON_34
**Composite Score:** 4.9 / 10.0 (Rigor: 1.5/3.5 | Claims: 1.4/2.5 | Biology: 1.2/2.0 | Reproducibility: 0.8/2.0)
**Bias Category:** Sample-Size/Denominator Inconsistencies, Pseudoreplication of Paired Tissues, and Unverified Nested-PCR Co-Infection Claims
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Epidemiological Observational

---

### 1. Executive Summary

This manuscript investigates the distribution of Hepatitis C Virus (HCV) genotypes (Okamoto/Kato types I–IV, corresponding to `HCV-US`, `HCV-J`/`K1`, and `HCV-K2`) in sera and liver biopsy specimens from 70 second-generation anti-HCV EIA-positive individuals in Korea (37 with sporadic chronic hepatitis [CH], 12 with hepatocellular carcinoma [HCC], 16 with post-transfusion non-A, non-B hepatitis [PT-NANBH], 4 blood donors, and 1 healthy family member). Genotyping was performed via RT-nested PCR targeting the NS5 region using a universal outer primer pair (`#166`/`#167R`) followed by four type-specific inner primer pairs. The authors report that in serum, type II accounted for $75.0\%$ and type III for $25.0\%$ of cases with $0\%$ co-infection, whereas in 27 liver tissue specimens, type II accounted for $63.0\%$, type III for $3.7\%$, and mixed type II + III co-infection for $18.5\%$.

While this is an early descriptive molecular epidemiology survey demonstrating the predominance of HCV type II (genotype 1b) in Korean chronic liver disease patients, the manuscript exhibits substantial internal numerical contradictions, pseudoreplication of paired tumor and non-tumor tissues from the same HCC patients, complete omission of all five data/primer tables referenced in the text, and reliance on ethidium-bromide band presence after 65 cycles of nested PCR without sequencing verification or negative carryover controls to claim a high rate ($18.5\%\text{--}25.0\%$) of mixed HCV type II + III co-infection in liver tissue.

---

### 2. Methodological & Statistical Audit

* **Internal Contradictions in Serum Sample Counts and Positivity Rates [Methodologically Flawed]:**
  The counts of RT-nested PCR-positive and typed serum samples do not agree across consecutive paragraphs of the Results:
  1. **HCC serum positivity discrepancy:** Under *Positivity in RT-nested PCR* (line 57), the authors state: *"Among 12 patients with HCC, 5 cases (62.5%) of 8 sera, 10 cases (83.3%) of 12 frozen tumorous tissue specimens and 5 cases (71.4%) of 7 non-tumorous tissue specimens were positive."* Yet in the very next section (line 70) and again on line 89, the authors state: *"All cases of 6 HCC and 9 PT-NANBH showed only type II HCV"* and *"In sera, 6 cases which were positive in RT-nested PCR among 12 HCC patients, were all type II HCV"* (5 positive sera vs. 6 positive sera).
  2. **Total typed serum denominator discrepancy:** Line 68 states: *"Among a total 70 individuals, available 43 serum samples were typed by RT-nested PCR. The prevalence of type II HCV was 75%, type III HCV was 25%..."* However, summing the subgroup counts reported in lines 68–70 gives: $37$ sporadic CH ($24$ type II + $13$ type III) $+ 6$ HCC (all type II) $+ 9$ PT-NANBH (all type II) $+ 4$ blood donors ($3$ type II + $1$ type III) $= 56$ typed serum samples ($42$ type II and $14$ type III). Notably, $42/56 = 75.0\%$ and $14/56 = 25.0\%$, whereas $43$ cannot yield exact $75.0\%$ and $25.0\%$ integer proportions ($43 \times 0.75 = 32.25$). Thus, the stated total of `43` serum samples on line 68 contradicts the subgroup counts ($N = 56$) from which the $75.0\% / 25.0\%$ percentages were actually calculated.

* **Pseudoreplication of Paired Tumor and Non-Tumor Liver Specimens [Methodologically Flawed]:**
  In Materials and Methods (line 26), frozen liver biopsies were obtained from 20 patients ($8$ sporadic CH and $12$ HCC). However, in the Abstract and Results (lines 6, 75, 79), the authors pool $8$ sporadic CH biopsies, $12$ HCC tumorous biopsies, and $7$ paired non-tumorous liver specimens from the same $12$ HCC patients to create a denominator of $27$ "cases" ($8 + 12 + 7 = 27$). Counting paired tumorous and non-tumorous samples from the same liver as independent patients inflates the sample size and violates independence. Furthermore, in this $N=27$ denominator, the authors report $63.0\%$ type II ($17/27$), $3.7\%$ type III ($1/27$), and $18.5\%$ co-infection ($5/27$), which sum to $23/27$ ($85.2\%$)—because the 4 PCR-negative tissue specimens ($2$ tumorous and $2$ non-tumorous from line 57) were left in the denominator when computing genotype percentages! If genotype percentages are calculated among the $23$ HCV RNA-positive tissues, the proportions are $17/23$ ($73.9\%$), $1/23$ ($4.3\%$), and $5/23$ ($21.7\%$).

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **Unverified Co-Infection Claims from 65-Cycle Multiplex/Nested PCR [Fragile]:**
  The protocol performs 35 cycles of first-round PCR with low-stringency annealing ($40^\circ\text{C}$ for 1 min) followed by 30 cycles of second-round PCR ($55^\circ\text{C}$ annealing) in four separate type-specific tubes. No negative extraction controls, no-template controls across nested transfers, or synthetic single-template cross-reactivity controls (testing whether high-titer cloned type II template cross-primes with `#151`/`#153R` type III primers after 35 first-round cycles at $40^\circ\text{C}$) are described, nor were any of the putative dual-band liver samples cloned or sequenced. Given the well-known susceptibility of 65-cycle RT-nested PCR to cross-priming and amplicon carryover, the claim that $18.5\%\text{--}25.0\%$ of liver biopsies harbor true mixed type II + III co-infection while $0\%$ of matched sera show co-infection remains fragile without sequencing confirmation.

* **Unpublished Sequence Homology Claims in Discussion [Overstated]:**
  In the Discussion (line 102), the authors state that *"the homologies of type II HCV isolated from Korean patients to representative reference sequences isolated from Japan were relatively high, more than 90% at the nucleic acid level and 95% at the amino-acid level (unpublished)"*, and also discuss interferon-alfa responder vs. non-responder clinical subgroups (line 104) for which no data or methods are presented in the paper.

---

### 4. Reproducibility & Data Completeness

Reproducibility is poor because all five tables (`Table 1` through `Table 5`) and the figures (`Fig. 1` through `Fig. 4`) referenced in the text are missing from the manuscript file. In particular, because `Table 1` is absent, the actual nucleotide sequences of the 10 oligonucleotide primers (`#166`, `#167R`, `#192`, `#193R`, `#194`, `#195R`, `#173`, `#174R`, `#151`, `#153R`) are not available in the document (only their HCV-J nucleotide coordinates are listed on lines 40–42). No sequence accessions are deposited. Revising the manuscript would require providing all five tables, resolving the `43` vs. `56` serum sample discrepancy and the `5` vs. `6` HCC serum discrepancy, separating patient-level ($N=20$) from specimen-level ($N=27$) liver biopsy counts, and computing genotype proportions over PCR-positive samples ($N=23$) rather than total biopsies ($N=27$).
