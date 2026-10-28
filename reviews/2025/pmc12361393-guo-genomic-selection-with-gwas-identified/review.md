# Review of PMC12361393 (PMID:40826273)

**Manuscript Title:** Genomic selection with GWAS-identified QTL markers enhances prediction accuracy for quantitative traits in poplar (Populus deltoides)  
**Authors:** Guo C, Yin T, Wu H, Dai X, Chen Y, Wei S.  
**Journal / Preprint:** *Commun Biol* (2025; `PMC12361393` / `PMID:40826273` / `10.1038/s42003-025-08700-w`)  
**Calibration Study Cohort:** Cohort C — Wild Literature Sample (`C79` | Double-Blinded as `ANON_117`)  
**Overall Score:** **4.5 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.2/3.5 | Claims: 1.1/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study characterizes phenotypic variation, genome-wide associations (GWAS), and QTL-assisted genomic selection (GS) across ten growth, wood property, disease resistance, and leaf morphology traits in a *Populus deltoides* germplasm plantation established with 12 clonal ramets per accession in Jiangsu, China, originating from Texas, Louisiana, and Mississippi. Whole-genome resequencing (>10× depth) yielded 685,181 filtered SNPs across 19 chromosomes. Using the BLINK model in GAPIT3 at $P < 1 \times 10^{-5}$, the authors report 69 significant QTLs encompassing 130 candidate genes, evaluate phenotypic correlations with favorable allele counts, and incorporate multi-trait GWAS-significant SNP sets ($P < 10^{-5}$ to $10^{-2}$) as a separate random-effect group in Bayesian Ridge Regression (BRR), BayesA, and BayesC genomic prediction models. Raw sequencing reads are deposited in NCBI SRA (PRJNA1298496), though no analysis scripts are provided.

While the multi-trait clonal phenotyping and whole-genome resequencing of *P. deltoides* represent a useful empirical dataset for forestry genetics, the statistical analyses and biological interpretations suffer from several severe methodological flaws and internal contradictions. First, the reported genomic prediction accuracies after incorporating multi-trait QTLs (e.g., increasing lignin prediction accuracy by $+0.48$ when lignin heritability is only $6.23\%$) exceed the theoretical upper bound $\sqrt{h^2} \approx 0.25$ for predicting raw phenotypes of low-heritability traits, strongly suggesting information leakage from the validation fold via the combined 10-trait GWAS step. Second, the manuscript conflates broad-sense clonal repeatability ($V_G / (V_G + V_E)$) with narrow-sense heritability ($h^2$), misinterprets pairwise $F_{st}$ values of $0.20$–$0.40$ as "low genetic differentiation," and evaluates favorable allele correlations in the exact same discovery cohort (winner's curse). Third, the text contains direct internal contradictions—reporting $N = 237$ accessions throughout the Results/Methods but $N = 198$ in the Discussion, and referring to a nonexistent "transcriptomic correlation" in the Statistics section. Re-analyzing the genomic selection pipeline under strict multi-trait cross-validation isolation and correcting the genetic parameter definitions are essential before the conclusions can be trusted.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Ten growth, wood, disease, and leaf traits in *P. deltoides* exhibit narrow-sense heritabilities ranging from 6.23% to 66.84% and approximate normal distributions: [Methodologically Flawed].**  
  In the Methods (Section "Plant materials and phenotyping"), narrow-sense heritability is defined as $h^2 = V_G / (V_G + V_E)$ where $V_G$ is the genotypic variance estimated across clonal ramets. In a clonal trial without pedigree or additive genomic relationship partitioning, variance among clones estimates total genetic variance ($V_G = V_A + V_D + V_I$), which defines *broad-sense* heritability ($H^2$), not narrow-sense heritability ($h^2 = V_A / V_P$). Furthermore, the Results state that "all traits followed a bell-shaped curve, suggesting an approximate normal distribution... The Shapiro–Wilk test results indicated that DBH, BD, and LVA followed a normal distribution ($P > 0.05$)"—meaning that 7 of the 10 traits (including black spot disease infection rate, which spans $0.62\%$ to $75.51\%$ with $\text{CV} = 73.49\%$) significantly violated normality ($P \le 0.05$) but were analyzed without transformation.

* **The *P. deltoides* population from Louisiana, Mississippi, and Texas lacks clear genetic structure and exhibits low genetic differentiation ($F_{st} = 0.2$–$0.4$): [Methodologically Flawed].**  
  The Results report pairwise $F_{st}$ values of $0.2$ (Louisiana vs. Mississippi), $0.3$ (Louisiana vs. Texas), and $0.4$ (Texas vs. Mississippi) and conclude that these values indicate "a low level of genetic differentiation among these subgroups." Under standard Wright's fixation index criteria, $F_{st} > 0.15$ indicates great differentiation and $F_{st} = 0.20$–$0.40$ represents very strong population divergence—the exact opposite of the authors' claim, or else an artifact of miscalculating or mislabeling $F_{st}$.

* **GWAS identifies 69 significant QTLs and 130 candidate genes whose favorable allele counts strongly correlate with trait values ($r = 0.37$–$0.48$): [Fragile].**  
  First, the manuscript contradicts itself regarding the GWAS sample size: the Abstract and Methods state that GWAS was performed on all 237 accessions, whereas the Discussion (Paragraph 2) states *"In this study, GWAS was performed using 198 germplasms."* Second, the GWAS was performed on LD-pruned markers (`--indep-pairwise 50 5 0.2`, retaining 685,181 SNPs); aggressive LD pruning at $r^2 = 0.2$ prior to GWAS risks removing causal or tightly linked tagging variants. Third, selecting "favorable alleles" at $P < 10^{-5}$ in the discovery sample and then correlating the sum of those same alleles with the same individuals' phenotypes (Fig. 4) is circular post-selection inference (Beavis effect), which naturally inflates correlation coefficients regardless of true out-of-sample genetic architecture.

* **Incorporating multi-trait GWAS QTLs as random effects in BRR, BayesA, and BayesC increases genomic selection accuracy by 0.06 to 0.48 across all traits: [Methodologically Flawed].**  
  For lignin content, the reported heritability is $6.23\%$ ($h = \sqrt{0.0623} \approx 0.25$), yet integrating the $10^{-4}\text{sig}$ and $10^{-3}\text{sig}$ multi-trait marker sets into BRR increases the Pearson correlation between predicted genetic values and observed phenotypes by $+0.48$ (Fig. 5, reaching $r > 0.50$). In cross-validation against noisy phenotypes $y = g + e$, the expected correlation $\text{Cor}(\hat{g}, y) = r_{g,\hat{g}} \sqrt{h^2}$ cannot exceed $\sqrt{h^2} \approx 0.25$ unless the selected markers are overfitting residual environmental noise $e$ via data leakage. Specifically, while the Methods state that GWAS was run within the 190-accession training fold, the marker sets were pooled from "the combined GWAS results of the ten traits"—if the GWAS for the other nine correlated traits used all 237 individuals, or if the 69 full-data BLINK QTNs were included, validation phenotypes leaked into marker selection. Moreover, in standard BRR, assigning two marker groups independent Gaussian priors only alters predictions if the group-specific variance components are differentially scaled, which is not specified in Equation 2.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Eliminate Multi-Trait Leakage in the 5-Fold Cross-Validation GS Pipeline
* **WHY:** Achieving a phenotypic prediction correlation $r > 0.50$ on a trait with $6.23\%$ heritability (lignin) violates the theoretical bound $r_{\max} = \sqrt{h^2} \approx 0.25$ unless environmental residuals from the validation fold leaked into the marker selection step (either by using full-sample GWAS results or by including validation-fold phenotypes of correlated traits during multi-trait SNP selection).
* **WHAT:** Re-run the 5-fold cross-validation ensuring that for each fold split (190 training, 47 validation), all 47 validation accessions are completely masked from *all ten traits* before running GAPIT/BLINK GWAS and before computing any BLUP/phenotypic adjustments.
* **HOW:** Within each of the $10 \times 5 = 50$ training splits, subset the genotype and phenotype matrices to the 190 training clones across all 10 traits, run BLINK on those 190 clones only, extract the top SNPs at $P < 10^{-5}, 10^{-4}, 10^{-3}, 10^{-2}$, fit `BGLR` with a two-component `ETA` list on the 190 training clones, and report both raw predictive correlation $\text{Cor}(\hat{y}_{\text{val}}, y_{\text{val}})$ and accuracy divided by $\sqrt{H^2}$.

#### 2. Correctly Distinguish Broad-Sense Clonal Repeatability ($H^2$) from Narrow-Sense Heritability ($h^2$)
* **WHY:** Partitioning variance among clones with 12 ramets estimates total genotypic variance $V_G$ (broad-sense heritability $H^2 = V_G / (V_G + V_E)$), whereas narrow-sense heritability $h^2 = V_A / V_P$ requires estimating additive genetic variance $V_A$ via an additive genomic relationship matrix (GRM).
* **WHAT:** Report both broad-sense clonal repeatability ($H^2$) from the ramet-level linear mixed model and narrow-sense SNP heritability ($h^2_{\text{SNP}}$) from a genomic REML (GREML) model.
* **HOW:** Use `GCTA` or the `sommer` / `BGLR` package in R to construct VanRaden's additive genomic relationship matrix $G$ from the 685,181 SNPs, estimate $V_A$ and $V_E$ via REML ($h^2_{\text{SNP}} = V_A / (V_A + V_E)$), and update Supplementary Table 1 and the text accordingly.

#### 3. Resolve the Sample Size Discrepancy and Apply Rank-Based Normal Transformation for Non-Normal Traits
* **WHY:** The manuscript states $N = 237$ in the Results/Methods but $N = 198$ in the Discussion (line 91), creating uncertainty about which accessions were analyzed; additionally, 7 of the 10 traits failed the Shapiro–Wilk normality test ($P \le 0.05$), which can induce false-positive GWAS hits in GLM/BLINK driven by extreme phenotypic outliers (such as BSD infection rates up to $75.51\%$).
* **WHAT:** Clarify whether 237 or 198 accessions were used in GWAS, and verify that the 69 QTLs remain robust after normal-score transformation of the skewed traits.
* **HOW:** Apply an inverse-normal rank transformation (`qnorm((rank(y) - 0.5) / length(y))`) or Box–Cox transformation to the 7 non-normal traits, re-run BLINK GWAS, and report the overlap with the original 69 QTLs in Supplementary Table 2.

#### 4. Audit the $F_{st}$ Calculation and Population Structure Interpretation
* **WHY:** Reporting pairwise $F_{st} = 0.2, 0.3, 0.4$ among Texas, Louisiana, and Mississippi while claiming "low genetic differentiation" and "no definitive genetic structure" is a contradiction in population genetics, as wind-pollinated *P. deltoides* populations along the Mississippi River basin typically show $F_{st} < 0.05$.
* **WHAT:** Check the `VCFtools --weir-fst-pop` output logs to determine whether the reported numbers ($0.2, 0.3, 0.4$) are actually $0.02, 0.03, 0.04$ (a decimal-point typo) or maximum single-SNP $F_{st}$ values rather than genome-wide weighted mean $F_{st}$.
* **HOW:** Re-run `vcftools --vcf input.vcf --weir-fst-pop pop1.txt --weir-fst-pop pop2.txt`, extract the `"Weir and Cockerham weighted Fst estimate"` from the log file, and correct the values and Supplementary Fig. 4.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Copy-paste errors from unrelated studies and contradictory allele definitions undermine the reliability of the Methods section.
* **WHAT & HOW:**
  1. **Methods — Statistics and reproducibility (line 151):** Remove the erroneous statement *"Linear regression analysis was used in Fig. 4 to assess the relationship between genomic prediction accuracy and transcriptomic correlation"* (no transcriptomic data exist in this study) and replace it with the actual regression performed in Fig. 4 (ordinary least squares regression of trait phenotype on the number of homozygous favorable alleles per individual).
  2. **Methods — Linkage disequilibrium, GWAS and QTL identification (line 131):** Fix the contradictory sentence *"Genotypes that associated with increased DBH, BD, hemicellulose, cellulose, lignin, BSD, LA, LL, and LW values, or with decreased BSD values were considered favorable alleles"* by removing `"BSD"` from the list of increased traits and adding `"LVA"`.
  3. **Code Availability (line 19):** Deposit the R scripts used to run GAPIT3 BLINK, construct the multi-trait SNP sets, and execute the 5-fold cross-validation in `BGLR` on GitHub or Zenodo.
