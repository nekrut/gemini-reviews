<Blinded Review: TIME_ANON_0955>
**Composite Score:** 5.8 / 10.0 (Rigor: 1.8/3.5 | Claims: 1.5/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.3/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Dry-Lab Secondary Cohort/Database
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Clinical/Observational

OVERALL_SCORE: 5.8/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This genome-wide association study (GWAS) investigates late-onset Alzheimer disease (`LOAD`) by combining a previously published GWAS cohort (492 cases, 496 controls on Illumina `HumanHap550` / `1M-Duo`) with newly genotyped Caucasian cases and controls on the Illumina `1M-Duo` beadchip, yielding a stated discovery dataset of 931 cases and 1,104 controls (483,399 autosomal SNPs passing QC, Bonferroni threshold $\alpha = 1.03 \times 10^{-7}$). The authors test top discovery signals ($p < 10^{-5}$) across four independent replication datasets (`ADNI`, `Framingham Heart Study SHARe`, `TGEN/Reiman`, and an `ADRC` clinical cohort). Beyond confirming the canonical `APOE`/`TOMM40`/`PVRL2` locus on 19q13 (`rs2075650`, discovery $p = 1.30 \times 10^{-36}$), the authors report a novel genome-wide significant association at an intronic low-frequency SNP (`rs11754661`, $\text{MAF} \approx 0.07$) in `MTHFD1L` (methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 1-like) on chromosome 6q25.1 (Discovery $\text{OR} = 2.03$, $p = 4.70 \times 10^{-8}$, Bonferroni-adjusted $p = 0.022$; Replication $\text{OR} = 2.34$, $p = 0.00187$; Combined $p = 1.90 \times 10^{-10}$), and technically validate genotyping accuracy at 4 adjacent LD-proxy SNPs (`rs803424`, `rs2073067`, `rs2072064`, `rs17349743`) using TaqMan assays to rule out array genotyping artifacts.

While the study applies standard population stratification controls (10 `EIGENSTRAT` principal components reducing $\lambda_{\text{GC}}$ from `1.08` to `1.04`) and performs important technical re-genotyping for a low-MAF hit, forensic audit of the text and tables reveals multiple severe internal arithmetic contradictions in cohort sample sizes and statistically impossible meta-analytic odds ratios and $p$-values in Table 2.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### Major Statistical & Arithmetic Flaws
1. **Severe Internal Contradictions in Discovery, Replication, and Combined Sample Sizes:**
   - **Discovery Cohort:** The Abstract, Introduction, and Table 1 state that the discovery sample comprises `931 cases` and `1,104 controls` ($931 + 1,104 = 2,035$ individuals). However, Table 1 lists the total sample size (`All`) as `2,036` (`931` cases + `1,104` controls $\neq 2,036$). Worse, Methods line 129 states: *"Applying the quality control criteria gave a final analytical sample of 440 new cases and 608 new controls. These were combined with the 492 cases and 496 controls from our previous GWAS..."* Yet $440 + 492 = 932$ cases (not 931).
   - **Replication and Combined Cohorts:** The Abstract (line 13), Introduction (line 45), and Methods (lines 145–155: `ADNI` 147 cases / 182 controls + `Framingham` 86 cases / 1,200 controls + `TGEN` 859 cases / 552 controls + `ADRC` 246 cases / 69 controls) sum to **1,338 cases and 2,003 controls** in the replication sample. However, Results line 75 and Supplementary Figure S1/S2 captions state that the replication sample consists of **`1,242 cases and 1,737 controls`**, and that the combined discovery + replication dataset consists of **`2,174 cases and 2,181 controls`**! Even under the `1,242 / 1,737` replication numbers, $931 + 1,242 = 2,173$ cases (or $932 + 1,242 = 2,174$) and $1,104 + 1,737 = \mathbf{2,841}$ controls—not `2,181` controls (a discrepancy of 660 controls).
2. **Mathematically Impossible Combined Odds Ratios and $p$-values in Table 2:**
   - Look at the top hit `rs2075650` (`TOMM40`) in Table 2:
     - **Discovery:** $\text{OR} = 2.96\ (95\%\ \text{CI}: 2.50, 3.50)$, $p = 1.30 \times 10^{-36}$.
     - **Replication:** $\text{OR} = 5.72\ (95\%\ \text{CI}: 3.63, 9.02)$, $p = 6.24 \times 10^{-14}$ (direction `+`, same risk allele).
     - **Combined:** $\text{OR} = 2.94\ (95\%\ \text{CI}: 2.48, 3.47)$, $p = 4.87 \times 10^{-36}$.
     - **Audit:** How can combining a Discovery study with $\text{OR} = 2.96\ (p = 1.30 \times 10^{-36})$ and an independent Replication study in the *same direction* with $\text{OR} = 5.72\ (p = 6.24 \times 10^{-14})$ yield a Combined $\text{OR} = 2.94$ that is **smaller than both component studies** and a Combined $p$-value ($4.87 \times 10^{-36}$) that is **less significant than Discovery alone**?! Under any valid inverse-variance or Mantel-Haenszel meta-analysis or pooled logistic regression, combining a $Z \approx 12.6$ ($p = 1.3 \times 10^{-36}$) signal with a concordant $Z \approx 7.5$ ($p = 6.2 \times 10^{-14}$) signal must yield $p \ll 10^{-45}$ and an OR strictly between $2.96$ and $5.72$ (approx. $3.22$).
   - The exact same anomaly occurs throughout Table 2: for `rs6859` (`PVRL2`), Discovery is $\text{OR} = 1.41\ (1.24, 1.60)$, $p = 1.06 \times 10^{-7}$ and Replication is $\text{OR} = 1.98\ (1.47, 2.66)$, $p = 6.13 \times 10^{-6}$, yet Combined is $\text{OR} = 1.41\ (1.24, 1.60)$, $p = 9.60 \times 10^{-8}$ (virtually identical to Discovery alone, completely ignoring the replication cohort). This indicates that the "Combined" column in Table 2 for array SNPs Not genotyped in ADRC or imputed across cohorts was either miscalculated or omitted the replication cohorts entirely for those rows.
3. **Low Minor Allele Frequency (`MAF = 0.068`) and Winner's Curse Risk at `rs11754661`:**
   - `rs11754661` has a control MAF of ~0.05–0.07, meaning only ~130 risk alleles exist among 1,104 controls and ~180 among 931 cases, with very few minor-allele homozygotes. In three of the four replication cohorts (`ADNI`, `Framingham`, `TGEN`), `rs11754661` was *imputed* via `MACH` rather than directly genotyped (`ADNI` $p = 0.032$, `Framingham` $p = 0.145$, `TGEN` $p = 0.562$), and most of the replication significance came from the small clinical `ADRC` cohort (`246 cases, 69 controls`, $p = 0.00298$) which had a 3.5:1 case-to-control imbalance.
   - Notably, the authors candidly report in the Discussion (line 113) that their own previously celebrated genome-wide significant hit from the first half of this exact cohort (`rs11610206` on 12q13, $p = 3.45 \times 10^{-7}$ in the initial 492 cases / 496 controls) failed to replicate when expanded with the new samples, dropping by three orders of magnitude to $p = 4.61 \times 10^{-4}$.

#### Strengths
1. **Technical Validation via Independent Platform (`TaqMan`):** Recognizing that low-MAF single-SNP associations (`rs11754661` had no high-$r^2$ proxies on the Illumina array itself) are frequently driven by cluster-calling artifacts, the authors genotyped four nearby HapMap SNPs in strong LD (`r^2 = 0.67–0.85`) via TaqMan across 872 cases and 1,038 controls, confirming concordant effect sizes ($\text{OR} = 1.78–1.92$, $p = 7.7 \times 10^{-6}$ to $4.3 \times 10^{-7}$).
2. **Candidate Locus Replication Reporting:** Table 3 transparently reports both positive (`CLU`, `PICALM`, `CR1`, `BIN1`) and null (`EXOC3L2`, `GAB2`, `PCDH11X`) replication results for previously published LOAD loci.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** `APOE`/`TOMM40` (`rs2075650`) and previously reported loci (`CLU`, `PICALM`, `CR1`, `BIN1`) are significantly associated with LOAD in this cohort. `[Well Supported]`
- **Claim 2:** `MTHFD1L` (`rs11754661`) is a novel genome-wide significant risk locus for LOAD ($\text{OR} \approx 2.10, p = 1.90 \times 10^{-10}$) that may act via mitochondrial tetrahydrofolate/homocysteine metabolism. `[Moderately Supported]` — Technical genotyping error is ruled out by TaqMan proxy validation, and biological plausibility via one-carbon/homocysteine pathways is reasonable, but replication across the three imputed cohorts was weak/inconsistent (`TGEN` $p=0.56$, `Framingham` $p=0.15$) and heavily reliant on the small unstratified `ADRC` TaqMan sample (69 controls), while Table 2 contains major meta-analytic calculation errors.

### 4. Reproducibility & Data Completeness
- **Data Availability:** External cohort usage (`ADNI`, `dbGaP` Framingham `SHARe`, `TGEN`) is cited, though no `dbGaP` accession number is provided for the authors' newly genotyped discovery cohort.
- **Reporting Flaws:** The conflicting sample sizes between Abstract/Methods (`1,338 cases / 2,003 controls`) and Results/Supplement (`1,242 cases / 1,737 controls` and `2,174 / 2,181`) and the impossible Combined OR/$p$-value rows in Table 2 must be corrected from the primary analysis scripts.
</Blinded Review: TIME_ANON_0955>
