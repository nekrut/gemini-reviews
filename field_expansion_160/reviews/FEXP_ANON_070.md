# Review of FEXP_ANON_070

**Overall Score:** **6.5 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **4.8 / 8.0**  
* **Score Breakdown:** Rigor: 2.0/3.5 | Claims: 1.5/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.7/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Subfield & Study Design:** Human Complex Trait Genetics / Pre-registered Genome-Wide Association Study (GWAS), Meta-Analysis, LDSC Heritability Estimation, Functional Annotation (FUMA/MAGMA), and Polygenic Risk Score (PRS) Validation (`LDpred2-auto`) for Chronic Postsurgical Pain (CPSP).
* **Data Sources:** Individual-level genotype and linked primary-care (GP) prescription data from the UK Biobank ($N = 95,931$: $2,923$ cases and $93,008$ controls across $26,670$ major and $69,261$ minor surgical procedures), meta-analyzed with an external CPSP GWAS cohort (Parisien et al., $N = 1,350$; combined $N = 97,281$).
* **Perceived Venue Tier:** Specialty clinical/academic journal in anesthesiology or pain research.

---

## 2. Executive Summary & Editorial Verdict

This pre-registered study (`osf.io/h6cr9`) performs a genome-wide association study (GWAS) of chronic postsurgical pain (CPSP) in $95,931$ UK Biobank participants ($2,923$ cases and $93,008$ controls) by defining CPSP through primary-care (GP) analgesic prescription records ($\ge 4$ consecutive or non-consecutive 30-day intervals with NSAID or opioid prescriptions in the 12 months following an initial major or minor surgery). The authors conduct a binary meta-GWAS combining major and minor surgeries, an ordinal GWAS across prescription duration categories ($1\text{--}3$), a cross-cohort meta-analysis with a published CPSP dataset ($N = 97,281$), functional mapping in FUMA/MAGMA, SNP heritability estimation via LDSC, and polygenic risk score (PRS) validation via `LDpred2-auto`. They report one genome-wide significant locus at *GLRA3* (`rs17298280`, $P = 2.17 \times 10^{-9}$) in the binary meta-GWAS and an additional locus at *CRAMP1L* (`rs140330443`) in the ordinal GWAS, while transparently reporting that LDSC heritability for the combined meta-GWAS is below zero, MAGMA and S-PrediXcan yield no significant genes, and `LDpred2` PRSs explain virtually zero incremental variance ($\Delta R^2 = 0.000144\%$ to $0.01865\%$).

**Editorial Verdict: Major Revision (Mixed / Salvageable).** Unlike many formulaic summary-data studies, this manuscript represents a substantial, pre-registered primary data analysis with openly archived summary statistics (DANS `doi:10.17026/LS/486TJZ` and FUMA) and commendable scientific honesty regarding negative secondary results (reporting negative LDSC $h^2$, null MAGMA/TWAS, near-zero PRS $\Delta R^2$, and Cohen's $\kappa = 0.02$ against self-reported CPSP). However, three substantive methodological and numerical issues undermine the primary findings and require resolution: (1) **Severe phenotype misclassification ($\kappa = 0.02$) and collider/selection bias** arising from excluding participants without any GP prescription records and defining CPSP via $\ge 4$ *non-consecutive* months of general NSAID/opioid prescriptions over a year; (2) **Unaddressed case-control imbalance ($1 : 31.8$, case prevalence $3.05\%$) with linear/uncalibrated test statistics on low-frequency variants**, where 5 of the 10 suggestive lead SNPs in Table 2 have $\text{MAF} \le 0.008$ ($\sim 18\text{--}45$ minor alleles in cases); and (3) **A direct numerical contradiction between the main text and Table 2 regarding the allele frequencies and effect direction of the sole genome-wide significant SNP `rs17298280` (*GLRA3*)**, which also fails to replicate in the external CPSP cohorts.

### Assessment of Specific Conclusions
* **Claim 1: Intronic variant `rs17298280` in *GLRA3* is associated with CPSP at genome-wide significance ($P = 2.17 \times 10^{-9}$ in UKB; $P = 2.19 \times 10^{-9}$ in cross-study meta-analysis):** `[Fragile]`  
  First, there is an internal sign/allele contradiction between the text (Line 121: *"The minor allele (G) frequency in the cases and controls were 0.163 and 0.193, respectively"*, which indicates a *lower* frequency in cases, i.e., a protective effect of the minor allele) and Table 2 (Line 127: `Effect allele = C`, `MAF = 0.207`, `BETA = +0.0059 (0.0010)`, `Direction = ++`, indicating a *positive* risk effect of the minor allele). Second, adding the external published CPSP cohorts ($N = 1,350$) slightly *weakens* the $P$-value ($2.17 \times 10^{-9} \to 2.19 \times 10^{-9}$) and shows opposite effect directions in four of the six external cohorts (Line 137).
* **Claim 2: Nine additional loci (and `rs140330443` in *CRAMP1L* in the ordinal GWAS) show suggestive or genome-wide associations with CPSP:** `[Fragile]`  
  In Table 2, five of the nine suggestive loci (`rs186819635` $\text{MAF} = 0.003$, `rs140330443` $\text{MAF} = 0.005$, `rs184832856` $\text{MAF} = 0.006$, `rs138470454` $\text{MAF} = 0.007$, `rs145636748` $\text{MAF} = 0.008$) are rare/low-frequency variants tested under a $1:31.8$ case-control imbalance ($2,923$ cases vs. $93,008$ controls, split further across major and minor surgery GWASs) using linear-scale effect sizes (`BETA`). Without saddlepoint approximation (SPA, e.g., `REGENIE` or `SAIGE`) and an explicit minor allele count (MAC) filter in cases, linear or standard asymptotic tests produce severely inflated Type I error rates at $\text{MAF} < 0.01$ under $3\%$ case prevalence.
* **Claim 3: SNP heritability of the proxy CPSP phenotype is near zero ($h^2 < 0$ in combined meta-GWAS) and `LDpred2` PRSs explain negligible variance ($\Delta R^2 \le 0.019\%$):** `[Well Supported]`  
  The authors rigorously and transparently document that LDSC heritability estimates have standard errors larger than the point estimates (or fall below zero in the combined analysis) and that out-of-sample PRS prediction adds $0.000144\%$ to $0.01865\%$ variance explained.
* **Claim 4: The GP prescription-based proxy phenotype validly captures CPSP despite $\kappa = 0.02$ agreement with UK Biobank self-reported CPSP:** `[Overstated]`  
  A Cohen's $\kappa = 0.02$ indicates virtually zero agreement above chance with self-reported CPSP, and combined with a negative LDSC SNP-heritability estimate in the main meta-GWAS, strongly suggests that $\ge 4$ non-consecutive months of NSAID/opioid prescriptions within a year after minor or major surgery predominantly captures unrelated episodic/chronic analgesic utilization rather than surgery-induced chronic pain.

---

## 3. Forensic Defect Inventory

### 1. [Critical] Allele Coding and Direction Contradiction for Lead SNP `rs17298280` (*GLRA3*) Between Text and Table 2
* **Location:** Results Section "Genome-wide association analysis" (Lines 121, 137) vs. Table 2 (Line 127).
* **Defect:** Line 121 states: *"Within this locus, the most significant SNP was rs17298280 in the intronic region of the GLRA3 gene ($P = 2.17 \times 10^{-9}$). The minor allele (G) frequency in the cases and controls were 0.163 and 0.193, respectively."* If the minor allele is `G` and its frequency is lower in cases ($0.163$) than in controls ($0.193$), then the minor allele `G` is **protective** ($\text{OR} \approx \frac{0.163/0.837}{0.193/0.807} = 0.814$, $\beta_{\text{linear}} \approx -0.0059$) and the major allele `C` (frequency $0.837$ in cases vs. $0.807$ in controls) is the risk-increasing allele. However, Table 2 (Line 127) lists `Effect allele = C`, `MAF = 0.207`, `BETA (se) = 0.0059 (0.0010)`, and `Direction = ++`, and Line 137 states *"The C allele of this SNP was positively associated with CPSP"*. Either `C` is the major allele ($\text{EAF} \approx 0.81$, not $\text{MAF} = 0.207$) or the case/control frequencies ($0.163$ vs. $0.193$) in Line 121 are inverted!
* **Remediation:** Clarify the exact reference/effect/minor alleles (`C` vs. `G` on forward strand GRCh37 `4:175634898`) and report the exact effect allele frequency (EAF) in cases and controls alongside the odds ratio on the logistic scale.

### 2. [Major] Severe Case-Control Imbalance ($1:31.8$) and Low-MAF Type I Error Risk in Linear-Scale GWAS
* **Location:** Methods (Lines 68–72) and Table 2 (Lines 126–136).
* **Defect:** The study has a $3.05\%$ case proportion ($2,923$ cases vs. $93,008$ controls, divided into $26,670$ major and $69,261$ minor surgery participants). In Table 2, effect sizes (`BETA`) are reported on the raw linear probability scale (`0.0059` for `rs17298280`), and 5 of the 10 lead variants have $\text{MAF}$ between $0.003$ and $0.008$ (`rs186819635` $\text{MAF} = 0.003$, `rs140330443` $\text{MAF} = 0.005$, `rs184832856` $\text{MAF} = 0.006$, `rs138470454` $\text{MAF} = 0.007$, `rs145636748` $\text{MAF} = 0.008$). Under a $1:31.8$ case-control ratio, a variant with $\text{MAF} = 0.003\text{--}0.005$ has an expected minor allele count (MAC) of only $4\text{--}20$ in the major-surgery case stratum, where Gaussian linear models (`BOLT-LMM` / `PLINK` linear) or uncalibrated Wald tests suffer severe asymptotic breakdown and false-positive spikes.
* **Remediation:** Re-evaluate all genome-wide and suggestive loci using logistic mixed-model regression with Saddlepoint Approximation (`SAIGE` or `REGENIE --firth --approx`) and enforce a minimum minor allele count in cases ($\text{MAC}_{\text{cases}} \ge 20$, corresponding to $\text{MAF} \ge 0.01$ in each surgical stratum).

### 3. [Major] Phenotype Dilution from Non-Consecutive Prescription Criteria and Collider Conditioning on GP Prescription Presence
* **Location:** Methods Sections "Inclusion and exclusion criteria" and "Chronic postsurgical pain phenotype definition" (Lines 54–63) and Discussion (Line 238).
* **Defect:**
  1. **Non-consecutive prescription window:** Defining cases as individuals with $\ge 4$ *non-consecutive* 30-day intervals containing an NSAID or opioid prescription in the 12 months after a minor or major procedure classifies anyone receiving intermittent NSAIDs (e.g., ibuprofen/naproxen for episodic headache, dysmenorrhea, or osteoarthritis flares in months 1, 4, 8, and 11 after a minor skin/eye procedure) as a "chronic postsurgical pain" case. This explains why $69,261$ minor surgeries dominate the sample, why Cohen's $\kappa$ with self-reported CPSP is $0.02$, and why combined LDSC SNP heritability is $<0$.
  2. **Exclusion of zero-prescription participants:** Criterion (7) (Line 54) excludes participants *"without any prescription records in the GP data"*. Conditioning inclusion on having at least one GP prescription can induce collider bias if genetic liability to pain/health-seeking influences GP prescribing.
* **Remediation:** Perform a sensitivity analysis restricting the case definition to **consecutive** monthly analgesic prescriptions starting in month 1 post-surgery (months 1–4+ continuously) and compare the effect size of `rs17298280` (*GLRA3*) under the consecutive vs. non-consecutive definition.

### 4. [Minor] Summary Statistics Formatting and Typographical Inconsistencies
* **Location:** Table 1 (Lines 99–115), Line 121, and Line 194.
* **Defect:**
  1. In Table 1, the caption and rows report `median (sd)` for highly skewed prescription counts (`Opioid prescription number, median (sd): 3 (28.32)` vs. `12 (63.29)`), pairing a non-parametric location metric (median) with a parametric dispersion metric (standard deviation) instead of interquartile range (IQR).
  2. Line 121 prints the suggestive threshold as `P < 1 x 10 6` (missing minus sign in exponent), and Line 194 leaves an unformatted raw hyperlink title pasted inline (`MAGMA (Generalized Gene-Set Analysis of GWAS Data | PLOS Computational Biology. https://...)`).
* **Remediation:** Report `median (IQR)` for skewed prescription counts in Table 1, fix `P < 1 × 10⁻⁶` on Line 121, and replace the raw URL on Line 194 with a numbered citation.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.0** | **3.5** | Pre-registered workflow, comprehensive post-GWAS/LDSC/PRS validation, and honest reporting of null heritability/PRS results; penalized for linear/uncalibrated testing of $\text{MAF} = 0.003\text{--}0.008$ variants under $1:31.8$ case-control imbalance and noisy non-consecutive prescription proxy ($\kappa = 0.02$). |
| **2. Claim-to-Evidence Alignment** | **1.5** | **2.5** | Authors transparently report negative $h^2_{\text{SNP}}$, null MAGMA/TWAS, near-zero PRS $\Delta R^2$, and $\kappa = 0.02$; however, the *GLRA3* lead signal shows opposite directions in external cohorts and has an unresolved allele-frequency contradiction between text and Table 2. |
| **3. Data Integrity & Biological Plausibility** | **1.3** | **2.0** | *GLRA3* has a plausible prostaglandin $E_2$ spinal inflammatory pain mechanism, but the non-consecutive 1-year NSAID/opioid proxy phenotype after minor surgery has low biological specificity for true postsurgical pain. |
| **4. Reproducibility & Data Integrity** | **1.7** | **2.0** | Pre-registered on OSF (`osf.io/h6cr9`) with full summary statistics deposited at DANS (`doi:10.17026/LS/486TJZ`) and FUMA (`266351`); minor deduction for the `rs17298280` case/control allele frequency contradiction in Line 121 vs. Table 2. |
| **Scientific Core Score** | **4.8** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **6.5** | **10.0** | **Mixed / Salvageable** (65 / 100 equivalent). |
