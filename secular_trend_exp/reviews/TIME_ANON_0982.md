<Blinded Review: TIME_ANON_0982>
**Composite Score:** 3.8 / 10.0 (Rigor: 1.0/3.5 | Claims: 1.0/2.5 | Biology: 0.9/2.0 | Reproducibility: 0.9/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Reject (Fundamental Flaws)
**Study Modality:** Dry-Lab Secondary Cohort/Database
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Observational

OVERALL_SCORE: 3.8/10
VERDICT: FAILED
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary / SUMMARY
This statistical genetics workshop paper re-analyzes pedigree microsatellite (STR) and Affymetrix SNP data from the Collaborative Study on the Genetics of Alcoholism (COGA) to address inconsistencies between genome-wide linkage scans for DSM-III-R (`Alc1`) and DSM-IV (`Alc2`) alcoholism diagnoses. The authors use canonical discriminant analysis (`SAS PROC CANDISC`) and principal component analysis (`PROC PRINCOMP`) on 13 electroencephalogram (EEG) variables and behavioral latent variables—explicitly ignoring pedigree non-independence—to select 5 behavioral symptoms (latent variables 1, 2, 7, 9, 11) that group with EEG traits, define 10 composite intersection phenotypes (`Ai_j`, where $i \in \{1,2\}$ and $j \in \{1,2,7,9,11\}$) plus two first-principal-component (PC1) phenotypes, and run Haseman-Elston model-free sib-pair linkage (`SIBPAL`) and family-based association testing (`FBAT`/`HBAT`) on chromosome 2q ($206\text{--}250\ \text{cM}$). While exploring endophenotype refinement in psychiatric genetics is a reasonable exploratory goal, the study suffers from severe circularity/data snooping, inappropriate application of i.i.d. multivariate methods (`CANDISC`/`PRINCOMP`) to related family members, misinterpretation of algebraic correlation among overlapping subset definitions as "robustness," and massive unadjusted multiple hypothesis testing across 12 correlated traits $\times$ 2 genetic models $\times$ all chromosome 2q SNPs and post-hoc selected haplotypes.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES

#### STRENGTHS
- **Joint comparison of STR and denser SNP linkage maps on chromosome 2q:** The authors compare microsatellite-only, Affymetrix SNP-only, and combined STR+SNP linkage scans (`SIBPAL`), noting how the apparent STR peak at $\sim 250\ \text{cM}$ shifts centromerically to $\sim 220\ \text{cM}$ when denser SNP markers are used.
- **Candid acknowledgment of violated statistical assumptions:** The authors transparently state in Methods (line 21) that normality and independence assumptions required for `CANDISC` and `PRINCOMP` were violated and in Discussion (line 53) that all `FBAT`/`HBAT` $p$-values are uncorrected across 24 phenotype-model combinations.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Trivial algebraic circularity in the "increased concordance" of `Ai_j` linkage signals:** The authors define `Ai_j` as an individual meeting diagnosis `Alc_i` ($i=1$ for DSM-III-R, $i=2$ for DSM-IV) **AND** exhibiting specific symptom $j$ (e.g., morning drinking or withdrawal symptoms). Because symptom $j$ is already a core severe dependence criterion shared by both DSM-III-R and DSM-IV, intersecting `Alc1` with symptom $j$ (`A1_j`) and intersecting `Alc2` with the exact same symptom $j$ (`A2_j`) restricts both affected groups to almost the exact same subset of severely dependent individuals! Finding that `A1_j` and `A2_j` yield more similar linkage curves (Fig. 2) than `Alc1` and `Alc2` is an algebraic tautology of intersecting both definitions with identical indicator variables, not independent validation of a genetic locus.
- **Violation of pedigree independence in `CANDISC` and `PRINCOMP`:** Treating related family members from COGA multiplex pedigrees as independent observations in canonical discriminant analysis (`CANDISC`) to select the 5 "significant" latent variables ($j = 1, 2, 7, 9, 11$) inflates type I error because familial aggregation of both EEG traits and drinking behaviors confounds the canonical correlations.
- **Severe unadjusted multiple testing and post-hoc circular haplotype selection (`Criterion 1`):**
  - For single-SNP association on chromosome 2q, the authors run `FBAT` across 12 phenotypes (10 `Ai_j` + 2 PC1s) $\times$ 2 inheritance models (additive and dominant) $= 24$ tests per SNP across hundreds of SNPs on chromosome 2q without any multiple-testing correction.
  - Even worse, in Figure 7 and `HBAT` haplotype testing (line 44), **Criterion 1** forms multi-SNP haplotypes specifically from *"consecutive SNPs that all showed a large number of significant results"* in the single-SNP scan, and then tests those exact SNPs again as haplotypes on the same dataset without permutation or multiple-testing correction, reporting uncorrected $p$-values as "strongly associated."
- **Omission of sample sizes, LOD/$p$-value magnitudes, and missing figures:** The text never states the number of pedigrees, sib-pairs, or genotyped individuals analyzed from COGA, nor does it report a single numerical $p$-value, $Z$-score, or LOD score anywhere in the text or tables (all quantitative values were only plotted in Figures 1–7, which are omitted from the text document, and there is a cross-reference typo in line 44 referring to *"Figure 6"* instead of *"Figure 7"* for the SNP significance counts).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim that intersecting DSM-III-R and DSM-IV diagnoses with identical severe symptom indicators increases correlation and linkage concordance between the two definitions:** `[Well Supported]` — Mathematically true by construction, as the intersection shrinks the discordant diagnostic boundary cases.
- **Claim that chromosome 2q ($206\text{--}250\ \text{cM}$) harbors haplotypes "strongly associated" with alcoholism and EEG principal components:** `[Overstated]` — Based on unadjusted $p$-values across 24 phenotype-model tests per marker and circular post-hoc haplotype selection (`Criterion 1`) without family-wise error control or replication.

### 4. Reproducibility & Data Completeness
The dataset is a standard benchmark cohort (COGA, Genetic Analysis Workshop), and software packages (`SAGE/SIBPAL`, `SAS v9.0`, `FBAT/HBAT`, `HAPLOVIEW`) and Affymetrix `tsc` SNP IDs (`tsc0548180`, `tsc0512074`, etc.) are explicitly named. However, no tables of numerical test statistics, sample sizes, or allele frequencies are included in the manuscript text.
</Blinded Review: TIME_ANON_0982>
