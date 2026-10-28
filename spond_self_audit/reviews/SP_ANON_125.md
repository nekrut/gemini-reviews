# Blinded Review: SP_ANON_125

**Composite Score:** 6.4 / 10.0 (Rigor: 2.0/3.5 | Claims: 1.5/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** Confounded Epidemic Sub-Structure & Misapplied RELAX/Transmission-Index Models
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Clinical/Epidemiological Observational

---

## 1. Executive Summary

This manuscript combines 454 deep sequencing of 74 acute HIV-1 subtype B infections (55 MSM, 19 IDU) with a meta-analysis of 354 acute infections and a comparative sequence analysis of 131 Fiebig stage I–III founder *env* sequences (65 HSX, 66 MSM) to address two questions: (1) whether multiplicity of founder virus infection differs between men who have sex with men (MSM) and heterosexuals (HSX), and (2) whether selective pressures and amino acid signatures at the transmission bottleneck differ by risk group. While the development of the Average Pairwise Hamming Distance (`APHD`) classifier and the finding that Fiebig stage (I–III vs. IV–VI) strongly confounds multivariant transmission estimates ($\text{OR} = 3.86, p = 0.002$) are rigorous and convincing, the second half of the paper—claiming stronger purifying selection in MSM via HyPhy `RELAX`, higher "Transmission Index" scores in HSX, and 20 risk-group transmission signature sites—suffers from serious methodological flaws, training-set circularity, and confounding by chronic viral population structure.

---

## 2. Methodological & Statistical Audit

* **Misapplication of the HyPhy `RELAX` Selection Framework (Methods lines 31–33; Results line 66):** The standard `RELAX` test evaluates whether selection stringency is relaxed ($K < 1$) or intensified ($K > 1$) on test branches relative to reference branches via a 1-degree-of-freedom likelihood ratio test comparing the Null model ($K=1$) against the Alternative model ($K$ free). Here, however, the authors do **not** report the relaxation parameter $K$ or compare Null vs. Alternative. Instead, they compare both the Null model ($p = 0.009$) and the Alternative model ($p = 0.008$) against the unconstrained **Partitioned Exploratory model** (which fits completely independent 3-rate $\omega$ distributions to MSM and HSX branches), and then interpret raw point estimates of the unconstrained $\omega$ categories (e.g., claiming $85\%$ of sites have $\omega = 0.064$ in MSM vs. $62\%$ with $\omega = 0.068$ in HSX, and $\omega_3 = 9.81$ at $3.1\%$ of sites in HSX vs. $\omega_3 = 2.71$ at $14.6\%$ of sites in MSM). In random-effects codon models, the proportions $p_k$ and rate values $\omega_k$ of the unconstrained exploratory model are strongly negatively correlated and notoriously unstable; comparing raw point estimates of $(\omega_k, p_k)$ across partitions when the constrained RELAX Alternative model is rejected is statistically invalid.
* **Training-Set Circularity in the "Transmission Index" Comparison (Results lines 68–70):** To test whether HSX founder viruses are under stronger selection for "transmission fitness" than MSM founder viruses, the authors score the 131 subtype B founder sequences using the sequence-based Transmission Index of Carlson et al. [12]. However, Carlson et al. parameterized and trained that index on **heterosexual (HSX) linked transmission cohorts** and clade B database conservation! Applying weights trained on HSX transmission pairs to test whether HSX founder viruses score higher than MSM founder viruses ($p = 0.004$) introduces circular ascertainment bias: any demographic or sub-epidemic lineage differences between North American/European MSM and HSX sub-epidemics will automatically make HSX sequences match the HSX-trained weights better.
* **Permissive False Discovery Thresholds and Confounding by Chronic Sub-Epidemic Segregation (Results lines 72–76):** The phylogenetic logistic regression screen for risk-group signature sites uses permissive false discovery rate thresholds of $q < 0.2$ (identifying 6 sites) and $q < 0.4$ (identifying 20 sites across *gp120*), meaning up to 40% of the called signatures are expected to be false positives. Even more critically, when the authors check Dataset 4 (590 chronic subtype B sequences from MSM vs. HSX), **12 of the 20 signature sites show the exact same amino acid differences between chronic MSM and chronic HSX viruses** (Fig. 3C). Despite using Bhattacharyya's affinity and leaf-swapping on the combined tree, the presence of the same residue frequency differences in chronic infection demonstrates that these sites reflect partial epidemiological network segregation between MSM and HSX sub-epidemics rather than differential mucosal selection at the acute transmission bottleneck.

---

## 3. Biological / Experimental Grounding & Claim Proportionality

* **`[Well Supported]` Comparable Single-Variant Founder Proportions in MSM (83%) and HSX After Controlling for Fiebig Stage:** The demonstration that later acute sampling (Fiebig IV–VI vs. Fiebig I–III) inflates inferred multivariant transmission 3.86-fold, and that MSM and HSX have statistically indistinguishable multivariant transmission rates ($p = 0.167$) once Fiebig stage is accounted for, is well supported by both the 74 deep-sequenced samples and the 354-subject meta-analysis.
* **`[Well Supported]` Calibration of the APHD Classifier on Deep Sequencing Reads:** Validating the logistic regression `APHD` cutoff across 127 published SGA/S datasets, `ART_454` pyrosequencing error simulations, and 6 paired SGA/S controls provides a solid, practical metric for classifying infection multiplicity in short-read amplicons.
* **`[Methodologically Flawed]` Stronger Purifying Selection in MSM and Stronger Diversifying Selection in HSX via RELAX:** Grounded in raw point estimates from an unconstrained Partitioned Exploratory model rather than a valid RELAX $K$-parameter test, this claim is unsupported by the statistical evidence presented.
* **`[Overstated]` Risk-Group-Specific Transmission Signatures Driven by Mucosal Bottleneck Differences:** Given $q < 0.4$ thresholds and the replication of 12/20 signatures in chronic MSM vs. HSX viruses, attributing these polymorphisms to rectal vs. cervicovaginal mucosal selection rather than demographic founder effects between partially segregated transmission networks is overstated.

---

## 4. Reproducibility & Data Completeness

* **Data & Code Availability:** The manuscript states that sequence alignments are available on GitHub (`github.com/[USER_REDACTED]/hiv_wide_deep`) and raw reads are deposited in the NCBI SRA (`SRP049715`), though the text also contains an unfulfilled placeholder on line 43 (`"Data are available from the NCBI Sequence Read Archive (accession numbers pending)"`).
