# Forensic Scientific Review of `ANON_87`

**Overall Score:** **4.5 / 10.0** (Flawed / Overstated)
* **Score Breakdown:** Rigor: 1.3/3.5 | Claims: 1.0/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.1/2.0

---

## 1. Executive Summary & Synthesis

`ANON_87` reports a genome-wide association study (`GWAS`) of speech-in-noise (`SIN`) deficits among individuals with self-reported normal hearing in quiet using the UK Biobank cohort ($N = 279,911$: $58,844$ cases and $221,067$ controls), identifying 996 genome-wide significant SNPs ($p < 5 \times 10^{-8}$) across four genomic loci (`MHC` region on chr6, `GRM3` on chr7, and `MAPT` on chr17) and 720 suggestive SNPs ($p < 10^{-6}$) across 21 loci. The authors perform heritability and tissue/cell-type enrichment analyses (`LDSC`, `FUMA`, `MAGMA`, and mouse cochlear `scRNA-seq` regression) and conduct a follow-up replication study on $N = 242$ healthy young adults phenotyped with the 12-item Speech, Spatial, and Quality of Hearing scale (`SSQ12`), pure-tone hearing thresholds (`HTs`, $0.25\text{--}16\text{ kHz}$ across two ears), and distortion-product otoacoustic emissions (`DPOAEs`, $1\text{--}16\text{ kHz}$ across two ears).

While the discovery `GWAS` in the UK Biobank (`REGENIE`, `LDSC`, `FUMA`/`MAGMA`) is appropriately powered and shows negligible population stratification (`LDSC intercept = 1.003`), forensic inspection of the statistical models and summary tables uncovers a **critical pseudoreplication flaw in the replication linear mixed models (`LMMs`)** alongside multiple severe tabular and numerical errors:
1. **Severe Pseudoreplication (Omission of Subject Random Intercepts) in the Replication `LMMs` (`Methods`, lines 67–87; `Table 4`, lines 240–261):**
   - Each of the $N = 242$ replication participants contributed 12 repeated responses for `SSQ12` ($2,904$ total observations), 28 repeated measurements for `HTs` (14 frequencies $\times$ 2 ears = $6,776$ observations), and 24 repeated measurements for `DPOAEs` (12 frequencies $\times$ 2 ears = $5,808$ observations).
   - In `Methods` (lines 71–87), the `lme4` model formulas are specified as:
     $$\text{SSQ12} = \text{Intercept} + \text{Age} + \text{Sex} + \text{Ethnicity} + \text{PC1}\cdots + \text{PC10} + (1 \mid \text{Question\#}) + \text{SNP}_i$$
     $$\text{HTs} = \text{Intercept} + \text{Age} + \text{Sex} + \text{Ethnicity} + \text{PC1}\cdots + \text{PC10} + (1 \mid \text{RandomEffect}) + \text{SNP}_i$$
     $$\text{DPOAEs} = \text{Intercept} + \text{Age} + \text{Sex} + \text{Ethnicity} + \text{PC1}\cdots + \text{PC10} + (1 \mid \text{RandomEffect}) + \text{SNP}_i$$
     where `RandomEffect` is nested `Frequency` and `Ear`.
   - **No random intercept for Subject/Participant (`(1 | Subject_ID)`) was included in any of the three models!** Because `SNP_i` varies between subjects (`N = 242`) rather than within subjects, omitting `(1 | Subject_ID)` causes `lme4` to treat all 12 questions (or all 24–28 ear-frequency measurements) from the same person as independent subjects. This inflates the effective sample size by $12\times$ to $28\times$, shrinking standard errors by $\sqrt{12}\text{--}\sqrt{28}$ ($\approx 3.5\text{--}5.3\times$) and multiplying $\chi^2 / Z^2$ test statistics by $12\text{--}28\times$.
   - This error directly explains the biologically impossible $p$-values reported in `Table 4` for a sample of just $N = 242$ young adults: for example, `rs713522` (`MAPT`, $\text{MAF} = 0.42$), which had a tiny effect in the discovery `GWAS` of $279,911$ people ($\beta = 0.0376$, $p = 2.3 \times 10^{-8}$), is reported in `Table 4` as achieving **$p = 5.2 \times 10^{-14}$** ($|Z| = 7.53$) for `HTs` and **$p = 7.0 \times 10^{-17}$** ($|Z| = 8.35$) for `DPOAEs` in only $N = 242$ people! In a true sample of $N = 242$ independent individuals, $|Z| = 8.35$ would require a single common SNP to explain $>22\%$ of the total phenotypic variance ($R^2 = Z^2 / (Z^2 + N) = 69.7 / 311.7 = 22.4\%$). In reality, dividing $Z^2 = 69.7$ by the 24 repeated DPOAE measurements per subject yields a true subject-level $Z^2 \approx 69.7 / 24 = 2.90$ ($|Z| \approx 1.70$, $p \approx 0.09$), which does not even reach nominal significance, let alone $p < 0.0002748$!
2. **Mislabeling of Pearson $\chi^2$ Statistics as "Odds Ratios" in `Table 2` and Swapped Field IDs in `Table 1`:**
   - In `Table 2` (lines 117–135), the column header states `Odds ratio`, reporting `290.2` for Sex, `1938.5` for Age (a 3-level categorical variable that does not even have a single odds ratio), and `11.2` for Ethnicity. Direct calculation from the cell counts in `Table 2` shows that the true Odds Ratio for Sex (Male vs. Female) is $\frac{29,973 \times 130,813}{90,254 \times 28,871} = \mathbf{1.505}$ (not `290.2`), and the true Odds Ratio for Ethnicity (Irish vs. British) is $\frac{1,802 \times 214,871}{6,196 \times 57,042} = \mathbf{1.095}$ (not `11.2`). The number `11.2` is the Pearson $\chi^2$ statistic ($\chi^2 = 11.21, \text{df} = 1$), and `1938.5` and `290.2` are likewise $\chi^2$ test statistics mislabeled as Odds Ratios.
   - In `Table 1` (lines 106–112), the UK Biobank data-field numbers are swapped relative to `Methods` (line 33): `Table 1` labels general hearing difficulty as `data field: 2257` and hearing difficulty in noise as `data field: 2247`, whereas in reality `2247` is general hearing difficulty and `2257` is hearing difficulty in noise.

---

## 2. Claim-by-Claim Audit

1. **Four genomic loci (`CD83P1/RNU6-471P` and `HLA-DQA1/HLA-DRB1` on chr6, `GRM3` on chr7, and `MAPT` on chr17) are associated with self-reported `SIN` deficits in individuals reporting normal hearing in quiet (`Table 3`, `Fig. 1`):** `[Well Supported]`
   - The discovery `GWAS` ($N = 279,911$) was conducted with `REGENIE` controlling for age, $\text{age}^2$, sex, $\text{age} \times \text{sex}$, batch, assessment center, and 10 PCs. `LDSC` confirms polygenic signal (`h2 = 0.039`, `SE = 0.0026`) with no confounding stratification (`intercept = 1.003`, `SE = 0.0077`).

2. **`SIN` deficit heritability is significantly enriched in cortical brain regions (dorsolateral prefrontal, anterior cingulate, entorhinal, and inferior temporal cortices) and shows no significant enrichment in mouse cochlear cell types (`Figs. 4–5`, lines 203–223):** `[Moderately Supported]`
   - Partitioned `LDSC` and `MAGMA` tissue/chromatin analyses (`Fig. 4`) robustly support central auditory-cognitive enrichment, and sensitivity analyses removing the `HLA` region (`Supplementary file S3`, line 232) confirm that cortical enrichment and `LDSC` heritability (`h2 = 0.0425`) persist. However, the null finding in mouse cochlear `scRNA-seq` (`Fig. 5`) is limited by cross-species orthology mapping (`10-month-old CFW mice` to human Entrez IDs) and bulk nuclear soma transcriptomes that may miss peripheral ribbon-synapse transcripts (`line 25`, chunk 2).

3. **In the replication cohort of $N = 242$ healthy young adults, 73 SNPs replicated for `SSQ12`, 119 for `HTs`, 187 for `DPOAEs`, and 12 (or 13) SNPs in `MAPT`, `GRM3`, and `HLA-DQA1` replicated across all three audiological measures with $p$-values down to $7.0 \times 10^{-17}$ (`Table 4`, `Figs. 6–8`):** `[Methodologically Flawed]`
   - As proven in Section 1, the `lme4` models (`lines 71–87`) omitted the subject-level random intercept `(1 | Subject_ID)`, treating 12–28 repeated within-subject measurements per participant as independent sample units. The resulting $p$-values (`Table 4`) are inflated by many orders of magnitude due to pseudoreplication and cannot support statistical replication at the adjusted threshold ($p < 0.0002748$).

4. **Male sex and older age have Odds Ratios of `290.2` and `1938.5` for `SIN` deficits (`Table 2`, lines 117–135):** `[Methodologically Flawed]`
   - The values `290.2`, `1938.5`, and `11.2` in the `Odds ratio` column of `Table 2` are $\chi^2$ test statistics, not Odds Ratios (true ORs are $1.51$ for Sex and $1.10$ for Irish vs. British ethnicity).

---

## 3. Technical & Methodological Critique

### 3.1. Mathematical Anatomy of the Pseudoreplication Error in `lme4` (`Lines 67–87`)
- In a mixed-effects model where predictor $X_i$ ($\text{SNP}_i$) is measured at the subject level ($i = 1, \dots, 242$) and outcome $Y_{ij}$ is measured across $J$ repeated conditions ($j = 1, \dots, 12$ questions for `SSQ12`, or $j = 1, \dots, 28$ ear-by-frequency combinations for `HTs`), the data-generating variance has a between-subject component $\sigma_u^2$ ($u_i \sim \mathcal{N}(0, \sigma_u^2)$) and a within-subject residual $\sigma_e^2$.
- When the model is fit as `Y ~ Age + Sex + Ethnicity + PC1..10 + (1 | Question#) + SNP` **without `(1 | Subject_ID)`**, the random intercept `(1 | Question#)` only centers the mean of each question across the 242 subjects; it leaves the between-subject covariance $\text{Cov}(Y_{ij}, Y_{ij'}) = \sigma_u^2$ completely unmodeled!
- Consequently, the variance of the OLS/GLS estimator $\hat{\beta}_{\text{SNP}}$ is incorrectly computed by `lme4` as:
  $$\widehat{\text{Var}}_{\text{naive}}(\hat{\beta}_{\text{SNP}}) \approx \frac{\sigma_u^2 + \sigma_e^2}{J \sum_{i=1}^N (X_i - \bar{X})^2}$$
  whereas the true variance accounting for within-subject correlation $\rho = \sigma_u^2 / (\sigma_u^2 + \sigma_e^2)$ is:
  $$\text{Var}_{\text{true}}(\hat{\beta}_{\text{SNP}}) = \frac{\sigma_u^2 + \sigma_e^2 / J}{\sum_{i=1}^N (X_i - \bar{X})^2} = \widehat{\text{Var}}_{\text{naive}}(\hat{\beta}_{\text{SNP}}) \times \left[1 + (J - 1)\rho\right]$$
  Since audiometric thresholds and DPOAEs across 24–28 adjacent frequencies and both ears within the same young adult have high intra-individual correlation ($\rho \approx 0.5\text{--}0.8$), the variance inflation factor $\text{VIF} = 1 + (J - 1)\rho$ is $\approx 13\text{--}22$, meaning the $Z$-statistics in `Table 4` are inflated by $\sqrt{13}\text{--}\sqrt{22} \approx 3.6\text{--}4.7\times$!

### 3.2. Internal Numerical Contradictions Across the Manuscript
- **Case Count Discrepancy:** The `Abstract` (line 8), `Discussion` (line 274), and `Conclusions` (chunk 2, line 39) state `$58,847$ cases and $221,067$ controls` (which sums to $279,914$, contradicting the stated total $N = 279,911$), whereas `Methods` (line 38) and `Table 2` ($28,871 + 29,973 = 58,844$) state `$58,844$ cases` ($58,844 + 221,067 = 279,911$).
- **`Lambda GC` Discrepancy:** `Results` line 139 reports `GC lambda = 1.155`, whereas line 205 and line 232 report `Lambda GC = 1.20`.
- **Replicated SNP Count Discrepancy (`12` vs. `13`):** `Abstract` (line 8), `Results` (line 237, sentence 7), and `Conclusions` (chunk 2, line 39) state that `12 SNPs` were replicated in all analyses, whereas the very next sentence on line 237 (`"Table 4 presents 13 SNPs replicated in all analyses"`) and `Discussion` (line 274: `"13 SNPs were replicated for SSQ12, HTs, and DPOAEs"`) claim `13 SNPs`, while `Table 4` itself contains exactly **12 rows**.
- **Genomic Coordinate Unit Error (Line 232):** Line 232 states that the `HLA` region was removed at `(Chr:6, Position: 25–34 GB)` instead of `25–34 Mb` (a $1,000\times$ unit error).
- **Incomplete Quality-Control Sentence (Line 50):** In `Methods` (line 50), the sentence *"Nuclei that had the number of detected mitochondrial genes were removed"* is missing its numerical predicate.
- **Inequality Sign Typo (Line 281):** In `Discussion` (line 281), the authors state *"showed no association between SIN deficits and genetic variants in APOE (e.g., rs429358 and rs7412, p < 0.05)"*, writing `p < 0.05` where `p > 0.05` is intended.

---

## 4. Actionable Recommendations

1. **Refit All Three Replication `LMMs` with a Random Intercept for Participant `(1 | Subject_ID)`:**
   - Update the `lme4` model specifications in `Methods` (lines 71–85) to include `(1 | Subject_ID)` alongside `(1 | Question#)` and `(1 | Frequency:Ear)` (or test subject-level composite averages of `SSQ12`, `HTs`, and `DPOAEs` using standard linear regression across the $N = 242$ participants), and recompute all replication $p$-values and `Table 4`.
2. **Correct `Table 1` and `Table 2`:**
   - In `Table 1`, swap the data-field labels so that `2247` corresponds to general hearing difficulty and `2257` corresponds to hearing difficulty in noise.
   - In `Table 2`, replace the mislabeled `Odds ratio` column (`290.2`, `1938.5`, `11.2`) with the actual $\chi^2$ column header and report true Odds Ratios (with 95% confidence intervals) where applicable.
3. **Harmonize Sample Sizes, `Lambda GC`, and Replicated SNP Counts:**
   - Correct `58,847` to `58,844` in the Abstract, Discussion, and Conclusions; reconcile `GC lambda = 1.155` vs. `1.20`; reconcile `12` vs. `13` replicated SNPs; and fix `25–34 GB` to `25–34 Mb` on line 232.
