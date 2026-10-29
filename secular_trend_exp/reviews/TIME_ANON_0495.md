<Blinded Review: TIME_ANON_0495>
**Composite Score:** 6.4 / 10.0 (Rigor: 2.2/3.5 | Claims: 1.8/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.0/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Minor Revision
**Study Modality:** Dry-Lab Secondary Cohort/Database
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Translational/Preclinical/Biomarker

---

OVERALL_SCORE: 6.4/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2000s

### 1. Executive Summary / SUMMARY
This human genetics replication and fine-mapping study follows up on two chromosome 9q34.3 candidate loci—*CARD9* (`rs4077515`) and *SNAPC4* (`rs3812571`)—that showed suggestive association with ankylosing spondylitis (AS) in the Wellcome Trust Case Control Consortium (WTCCC) non-synonymous SNP genome-wide scan. In Part 1, the authors genotype `rs4077515` and `rs3812571` in 730 new British AS cases (modified New York criteria) and compare them against 2,879 historic WTCCC disease controls (`3Dis`: multiple sclerosis, autoimmune thyroid disease, and breast cancer), replicating both associations ($p = 0.0004$ and $p = 0.0003$; combined WTCCC + replication meta-analysis $p = 5 \times 10^{-6}$ and $6 \times 10^{-6}$, $\text{OR} = 1.2$, $95\%\text{ CI } 1.1\text{–}1.3$). In Part 2, the authors fine-map the *CARD9*–*SNAPC4* LD block by genotyping 13 HapMap tagging SNPs in 1,604 British AS cases (77% overlapping with Part 1) and 1,020 healthy Oxfordshire controls (`OxC`, plus 1,422 1958 Birth Cohort controls for `rs10870149`), imputing 17 untyped SNPs using `MACH v1.0`, and querying published lymphoblastoid cell line eQTL data ($n = 400$, `mRNA by SNP browser v1.0.1`), showing that AS-associated SNPs (`rs4077515`, `rs10781500`, `rs10870077`, `rs3812571`) correlate more strongly with *SNAPC4* ($p = 2.6 \times 10^{-6}$ to $1.6 \times 10^{-11}$) than *CARD9* ($p = 0.05$ to $1.3 \times 10^{-5}$) expression. While the genetic replication and eQTL contextualization are informative, the manuscript suffers from missing data tables in the text, inconsistent and overlapping case/control cohorts across parts and SNPs, use of autoimmune disease patients as "controls" in Part 1, and recurring SNP rsID typographical errors.

### 2. Methodological & Statistical Audit / WEAKNESSES & METHODOLOGICAL AUDIT
- **Omission of Tables 1 and 2 from the Manuscript Text:**
  - The Results text explicitly directs readers to `Table 1` (line 33: *"Genotyping a cohort of 730 new cases of AS and comparing these with a further 2879 historical boundaries controls (3Dis) shows significant association inside both SNPs (p = 0.0004 and 0.0003 respectively; table 1)"*) and `Table 2` (line 61: *"Strength of association of CARD9 and SNAPC4 polymorphisms with expression of both genes... table 2"*). While the two table captions appear at lines 36–37 and 61–62, the actual tabular genotype counts, allele frequencies, odds ratios, and SNP-by-SNP association/eQTL results for the 13 genotyped and 17 imputed SNPs are completely missing from the manuscript file.
- **Use of Other Autoimmune Diseases (`3Dis`) as "Controls" in Part 1 and Heterogeneous Control Blending in Part 2:**
  - In Part 1, the 730 new AS cases are compared not to healthy population controls, but to 2,879 WTCCC cases with multiple sclerosis, autoimmune thyroid disease, or breast cancer (`3Dis`). Because *CARD9* is a central innate immune signaling adaptor downstream of Dectin-1/Syk/NOD2 that is shared across inflammatory/autoimmune diseases (including Crohn's disease and ulcerative colitis), using MS and autoimmune thyroid disease patients as controls risks pleiotropic confounding (though, if anything, shared risk alleles would bias the case-control comparison toward the null).
  - In Part 2, the control group changes from SNP to SNP without clear justification: 12 tagging SNPs are compared against $n = 1,020$ healthy Oxfordshire controls (`OxC`), whereas one SNP (`rs10870149`) is merged with $n = 1,422$ WTCCC 1958 Birth Cohort (`58BC`) controls, and `rs4077515`/`rs3812571` are analyzed against `OxC + 58BC + 2Dis` (excluding autoimmune thyroid disease after noting it had a slightly higher minor allele frequency of 56.1% vs 58.3%, $p = 0.14$; line 46). Furthermore, 77% of the 1,604 AS cases in Part 2 overlap with the WTCCC + Part 1 cases, meaning Part 2 is not an independent cohort.
- **Recurring Typographical Error in SNP Identifier (`rs1080077` vs `rs10870077`):**
  - On line 20 (Abstract) and line 43 (Results), the most strongly associated *SNAPC4* intronic tagging SNP is written as `rs1080077` (a 7-digit number that refers to an unrelated locus), whereas on lines 44, 67, and 91 it is correctly written as `rs10870077` (8 digits).
- **Lack of Conditional Logistic Regression to Disentangle LD Between *CARD9* and *SNAPC4*:**
  - The authors note high linkage disequilibrium ($D' \ge 0.9$, $r^2 \ge 0.65$) across the region and rely on marginal single-SNP association p-values and LCL eQTL p-values to argue whether *SNAPC4* or *CARD9* is the primary driver, without performing formal two-locus conditional logistic regression or colocalization testing to assess whether `rs4077515` retains residual signal when conditioned on `rs10870077`/`rs3812571` (or vice versa).

### 3. Biological / Experimental Grounding & Claim Proportionality / STRENGTHS
- **Strengths:**
  - Large combined sample size (up to 1,604 AS cases and >3,000 controls) achieving robust replication ($p \approx 5 \times 10^{-6}$ combined) of a moderate-effect complex trait locus ($\text{OR} \approx 1.2$).
  - Integration of cis-eQTL data from 400 lymphoblastoid cell lines (`mRNA by SNP browser v1.0.1`), which constructively highlights that *CARD9* coding/intronic variants are in strong LD with *SNAPC4* variants that exert an even stronger cis-eQTL effect on *SNAPC4* expression ($p = 1.6 \times 10^{-11}$) than on *CARD9* expression ($p = 1.3 \times 10^{-5}$), cautioning against automatically assigning causality to the most immunologically obvious gene (*CARD9*) in a dense LD block.
  - Explicit verification of Hardy-Weinberg equilibrium across all SNPs and sensitivity check for control disease heterogeneity (identifying and excluding the autoimmune thyroid disease subgroup in Part 2).
- **Claim Proportionality:**
  - `[Well Supported]` Common genetic variation across the 9q34.3 *CARD9*–*SNAPC4* LD block is reproducibly associated with ankylosing spondylitis susceptibility in British cases ($\text{OR} \approx 1.2$).
  - `[Well Supported]` AS-associated SNPs in this LD block correlate with expression of both *SNAPC4* and *CARD9* in lymphoblastoid cell lines, preventing purely genetic discrimination between the two genes without functional dissection.

### 4. Reproducibility & Data Completeness
- Software versions (`PLINK v1.01`, `StatsDirect v2.5.7`, `MACH v1.0`, `mRNA by SNP browser v1.0.1`, HapMap CEU Build 36) and genotyping platforms ( Sequenom iPLEX vs Applied Biosystems TaqMan) are clearly documented.
- However, the omission of the actual body of Table 1 and Table 2 from the manuscript text prevents verification of the individual genotype counts, minor allele frequencies, and imputation quality metrics ($R^2$) across the 30 evaluated SNPs.
</Blinded Review: TIME_ANON_0495>
