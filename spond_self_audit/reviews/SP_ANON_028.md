# Blinded Review: SP_ANON_028
**Composite Score:** 5.2 / 10.0 (Rigor: 1.5/3.5 | Claims: 1.1/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** Base-Rate Fallacy in Refusing Multiple-Testing Correction Across 296 Codon Sites
**Verdict:** Major Revision
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This manuscript introduces two maximum-likelihood codon substitution tests in HyPhy: (1) Internal Fixed Effects Likelihood (IFEL), which estimates site-specific synonymous ($\alpha_s$) and nonsynonymous ($\beta_s^I, \beta_s^L$) rates separately on internal ($I$) versus terminal/leaf ($L$) branches to filter out transient deleterious or recent within-host escape mutations; and (2) a population-level Differential Selection likelihood ratio test comparing internal-branch nonsynonymous rates ($\omega_1^I = \omega_2^I$) between two viral populations. The authors apply these methods to HIV-1 subtype C protease (PR) and reverse transcriptase (RT) sequences from Southern African (South Africa/Zambia, $n=74$) and Ethiopian Falasha ($n=63$) treatment-naive cohorts, reporting elevated $dN/dS$ on terminal vs. internal branches and claiming 7 codons (1 in PR, 6 in RT) evolve under significantly different population-level selective pressures ($p \le 0.05$ unadjusted), which they attribute to host HLA class I differences between Southern Africans and Ethiopians.

---

### 2. Methodological & Statistical Audit
* **Base-Rate Fallacy Used to Justify Unadjusted $p \le 0.05$ Across 296 Codons:** The authors test 296 individual codon sites (99 in PR, 197 in RT) for differential selection between the two clades and report 7 sites with nominal $p \le 0.05$ without any multiple-testing correction (e.g., Benjamini-Hochberg FDR or Holm-Bonferroni). To justify omitting multiple-testing adjustment, the authors argue: *"Positive predictive value (PPV) of the test was calculated at 98.8%, hence it is unlikely that detected sites are false positives. In particular, a high PPV estimate strongly suggests that site-wise testing procedures in this context do not require a correction for multiple testing."* This is a textbook base-rate fallacy:
  1. In their parametric simulations (Table S2), PPV ($\text{TP} / (\text{TP} + \text{FP})$) was 98.8% only because the simulation planted a high prior proportion of truly differentially selected sites with large effect sizes and used a discrete 5-bin rate distribution where the "null" bin happened to be ultra-conservative ($\text{FPR} \approx 0.1\%$).
  2. Under the global null hypothesis across $M = 296$ independent tests at a nominal significance level of $\alpha = 0.05$ (or even a slightly conservative empirical $\alpha = 0.025$), the expected number of false-positive sites by chance alone is $E[\text{FP}] = 296 \times 0.025 \approx 7.4$ sites—which is **identical to the 7 sites reported in the empirical dataset**! None of the 7 reported sites would survive standard Benjamini-Hochberg FDR control at $q < 0.10$.
* **Sound Formulation of the IFEL Separation of Internal vs. Terminal Branches:** The mathematical parameterization of IFEL ($\alpha_s, \beta_s^I, \beta_s^L$) and the empirical demonstration that terminal branches exhibit significantly higher $dN/dS$ than internal branches in HIV-1 subtype C *pol* are methodologically solid and provide a useful phylogenetic tool for separating population-level transmission fitness from recent within-host adaptation.
* **Confounding of Clade Background and Sampling Structure in the Two-Population Test:** The Ethiopian clade forms a monophyletic sub-cluster with a distinct founder bottleneck history compared to the Southern African sequences. A site-specific difference in $\beta_s^I$ between two monophyletic subtrees can arise from epistatic background differences fixed at the root of the Ethiopian sub-epidemic rather than ongoing differential host immune selection.

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim:** *Nonsynonymous substitution rates on terminal branches exceed those on internal branches in HIV-1 subtype C pol, reflecting maladaptive within-host immune escape mutations that are purged or revert upon transmission.* **[Well Supported]** — The global and site-level comparison of $\beta^L$ vs. $\beta^I$ confirms theoretical expectations and aligns with known transmission fitness costs in *pol*.
* **Claim:** *Seven codons in PR and RT are under differential population-level selection between Southern African and Ethiopian HIV-1 clade C epidemics due to population-specific HLA alleles.* **[Overstated / Statistically Fragile]** — Not only is the count of 7 sites at unadjusted $p \le 0.05$ across 296 tests indistinguishable from the expected null false-positive count, but neither cohort has any HLA typing data; invoking host MHC differences is pure post-hoc speculation.

---

### 4. Reproducibility & Data Completeness
* **Software Availability:** IFEL and the differential selection test are implemented in the public HyPhy package (`http://www.hyphy.org`), and GenBank accessions for the sequences are cited.
* **Missing Table Contents in Manuscript:** In the manuscript text, Tables 1 and 2 contain only their captions ("Table: Sequences Analyzed in This Study", "Table: Sites found to be under positive and/or differential selection") with the tabular body omitted in the text extraction, although the specific codon numbers and rates are discussed in the text and supplementary tables.
