# Review of ANON_134

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.6 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.6/3.5 | Claims: 1.3/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study estimates genetic parameters, evaluates single-step genomic prediction (`ssGBLUP`), and performs single-step genome-wide association mapping (`ssGWAS`) across nine litter size and piglet survival traits (`TNB`, `NBA`, `NHB`, `rNHB`, `NWB`, `NDF`, `NSB`, `MUMM`, and `LBWT`) in a commercial Large White pig population from southern China (170,027 farrowing records from $>62,000$ sows collected between 2010 and 2020, within a 325,263-animal pedigree). Using Genotyping-by-Sequencing (GBS) on 2,096 pigs, the authors retain 153,782 imputed autosomal SNPs, fit univariate and bivariate repeatability animal models in `BLUPF90`, compare pedigree `BLUP` and `ssGBLUP` via 10-fold cross-validation, and scan 0.3 Mb genomic windows for regions explaining $>1.0\%$ of additive genetic variance. They report low heritabilities ($0.01\text{–}0.06$), a 6.38%–13.33% gain in expected accuracy under `ssGBLUP`, favorable genetic correlations for selecting on number of healthy births (`NHB`) and litter birth weight (`LBWT`) over total number born (`TNB`), and six candidate QTL windows—highlighting `GPR12` on SSC11 for `TNB` and `NWB`. Raw GBS genotypes are publicly archived in the European Variation Archive (`PRJEB79359`).

The large phenotypic dataset and the multi-trait genetic correlation analysis (Table 4) provide a solid empirical basis for the breeding recommendation to prioritize `NHB` and `LBWT` over `TNB` so as not to increase weak, deformed, or stillborn piglets. However, the genomic prediction and `ssGWAS` conclusions are weakened by three methodological issues: (1) the 10-fold cross-validation evaluates model-derived theoretical reliability ($R_g = \sqrt{1 - \text{PEV}/\sigma_a^2}$ from the mixed-model equations) rather than empirical predictive correlation against masked phenotypes, and does not specify whether folds were split by sow or by individual litter record; (2) `ssGWAS` and enrichment claims rely heavily on zero-inflated, highly skewed count traits (`NDF` and `MUMM`, skewness $2.8\text{–}3.1$, kurtosis $9.0\text{–}10.5$) whose estimated heritabilities ($0.01 \pm 0.01$) are not statistically distinguishable from zero; and (3) several variance components and sample counts disagree across the text and tables. These issues can be resolved through computational re-analysis using the existing `BLUPF90` outputs.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Selecting for Number of Healthy Births (`NHB`) and Litter Birth Weight (`LBWT`) is superior to selecting for Total Number Born (`TNB`) to improve live-born litter performance without increasing piglet mortality: [Well Supported].**  
  The bivariate animal model genetic correlations across 170,027 litters (Table 4) clearly show that `TNB` has moderate-to-high positive genetic correlations with weak births (`NWB`, $r_g = 0.54$), stillbirths (`NSB`, $r_g = 0.41$), mummified fetuses (`MUMM`, $r_g = 0.49$), and deformed fetuses (`NDF`, $r_g = 0.36$), whereas `NHB` and `LBWT` maintain strong positive genetic correlations with `NBA` ($r_g = 0.87$ and $0.73$) while exhibiting near-zero or negative genetic correlations with `NWB` ($0.10$ and $-0.04$) and `NSB` ($-0.11$ and $-0.07$).

* **`ssGBLUP` improves genomic prediction accuracy by 6.38%–13.33% over pedigree `BLUP` in 10-fold cross-validation: [Methodologically Flawed].**  
  In Section 2.3 and Table 5, although the authors describe a 10-fold cross-validation scheme, they compute accuracy using the theoretical reliability formula $R_g = \sqrt{1 - \text{PEV}/\sigma_a^2}$ rather than the empirical cross-validation predictive accuracy (e.g., $\text{cor}(\widehat{\text{GEBV}}, y_c) / \sqrt{h^2}$ or the Legarra–Reverter LR validation statistics). Because adding genomic relationships ($\mathbf{G}^{-1} - \mathbf{A}_{22}^{-1}$) to $\mathbf{H}^{-1}$ always increases the diagonal information of the mixed-model coefficient matrix for genotyped animals, $\text{PEV}$ is algebraically guaranteed to decrease in `ssGBLUP` relative to `BLUP` even if the SNP markers have zero true predictive power for masked phenotypes. Furthermore, the Methods do not clarify whether the 10-fold split partitioned the 2,036 genotyped sows by *animal* (blocking all parities of a validation sow together) or by *record* (which leaks a sow's permanent environmental effect and breeding value across parities).

* **Six 0.3 Mb genomic windows explain 1.07%–1.77% of additive genetic variance across litter traits, with `SSC11: 4.33–4.50 Mb` (`GPR12`) and `SSC3: 127.1–127.4 Mb` (`ASAP2`/`MBOAT2`) as the top two candidate QTLs: [Fragile].**  
  While the `SSC11: 4.33–4.50 Mb` window (`GPR12`) is consistently detected across `TNB` (1.22% variance) and `NWB` (1.33% variance) and has a plausible biological link to oocyte cAMP signaling and meiotic arrest, the remaining hits are fragile for three reasons:
  1. **Zero-inflated traits with near-zero heritability:** Two of the six windows—including the highest-ranked window overall (`SSC3: 127.1–127.4 Mb`, 1.77% variance for `MUMM`) and `SSC5: 98.90–98.93 Mb` (1.26% variance for `NDF`)—come from rare defect/mummification traits with extreme skewness ($2.80\text{–}3.14$), kurtosis ($8.97\text{–}10.46$), and estimated additive genetic variance $\sigma_a^2 = 0.01 \pm 0.00$ ($h^2 = 0.01 \pm 0.01$, Table 3). Partitioning a nearly non-existent genetic variance ($\sigma_a^2 = 0.01$) across 153,782 SNPs using a Gaussian linear model produces noisy ratio spikes ($\text{Var}(a_i)/\sigma_a^2$).
  2. **Sparse SNPs in nominal 0.3 Mb windows:** In Table 6, the `TNB` window on SSC14 (`130.94–130.95 Mb`) spans only 10 kb and contains just 4 SNPs, and the `NBA` window on SSC9 (`117.31–117.37 Mb`) spans 60 kb and contains only 3 SNPs.
  3. **No formal significance threshold or permutation/bootstrap calibration:** Relying solely on an arbitrary $>1\%$ variance threshold without $p$-values (which `postGSf90` can compute via standardized SNP effects) does not control the genome-wide false positive rate.

* **GO and Reactome functional enrichment of the 26 positional candidate genes identifies key biological pathways governing litter size (Table 7): [Overstated].**  
  Selecting all 26 neighboring genes within $\pm 0.3\text{ Mb}$ of six physical windows introduces physical clustering bias (adjacent paralogs or co-regulated gene clusters within the same window inflate Fisher's exact counts), and Table 7 reports unadjusted Fisher's exact $p$-values ($p < 0.01$) mapped to human Reactome/GO databases without multiple-testing (FDR) correction.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Compute Empirical Predictive Accuracy and LR Validation Metrics in the 10-Fold Cross-Validation
* **WHY:** Reporting $R_g = \sqrt{1 - \text{PEV}/\sigma_a^2}$ from the mixed-model equations measures theoretical model reliability assuming the model is exact, rather than out-of-sample predictive accuracy on masked validation phenotypes.
* **WHAT:** Compute empirical predictive accuracy and the Legarra–Reverter (LR) cross-validation estimators, blocking folds strictly at the individual sow level among the 2,036 genotyped animals.
* **HOW:** Partition the 2,036 genotyped sows into 10 mutually exclusive animal folds (masking *all* parity records of the ~204 validation sows in each fold). For each fold, compute: (a) the Pearson correlation between predicted $(\text{G})\text{EBV}$ and yield-deviations (phenotypes adjusted for fixed farm-year-month and parity effects) divided by $\sqrt{h^2}$, and (b) the LR accuracy and dispersion/bias slope ($b_1$ from regressing whole-data $\widehat{\text{GEBV}}_w$ on partial-data $\widehat{\text{GEBV}}_p$). Report these empirical validation metrics alongside $R_g$ in Table 5.

#### 2. Report Formal SNP $p$-Values in `ssGWAS` and Caution Against Overinterpreting `NDF` and `MUMM` Peaks
* **WHY:** `NDF` and `MUMM` violate Gaussian mixed-model assumptions (kurtosis $>8.9$) and have $\sigma_a^2 = 0.01$ ($h^2 = 0.01 \pm 0.01$), making percentage-of-genetic-variance windows ($\text{Var}(a_i)/\sigma_a^2 > 1\%$) unstable.
* **WHAT:** Output formal single-SNP $p$-values from `postGSf90` (`OPTION pvalue`) and apply a genome-wide Bonferroni or Benjamini–Hochberg FDR threshold, or fit a threshold/Poisson model (`THRGIBBS1F90`) for the discrete mortality counts.
* **HOW:** Re-run `postGSf90` with `OPTION windows_variance 0.3` and `OPTION pvalue` to obtain test statistics $t_j = \hat{u}_j / \text{SE}(\hat{u}_j)$ and two-sided $p$-values for the top SNPs in Table 6, and explicitly note in Sections 3.5 and 4.3 that the `MUMM` and `NDF` signals should be treated as tentative due to $h^2 = 0.01$ and severe positive skewness.

#### 3. Clarify the Homozygote Count Filter in Quality Control
* **WHY:** Section 2.2 states that SNPs were excluded if *"the number of individuals in both homozygous genotypes (i.e., AA and BB) was less than 30"*. In $N = 2,096$ genotyped pigs, requiring $\ge 30$ minor homozygotes ($\text{BB} \ge 30$) under Hardy–Weinberg equilibrium requires $q^2 \times 2096 \ge 30 \implies \text{MAF} \ge 0.12$, which would eliminate all SNPs with $0.01 \le \text{MAF} < 0.12$.
* **WHAT:** Clarify the exact PLINK/custom filter applied to homozygote counts and state the actual minimum MAF observed among the 153,782 retained SNPs.
* **HOW:** Check the genotype QC log to confirm whether the filter excluded SNPs where the *sum* of homozygotes or *either* homozygous class was $<30$, and report the empirical MAF distribution (mean, median, and minimum MAF) of the 153,782 SNPs in Section 2.2.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Several sample counts, variance components, and truncated digits disagree between the text and Tables 1–3.
* **WHAT & HOW:**
  * **Section 2.1 vs. Table 1 (Sow Count):** Reconcile the number of sows with phenotypic records between Section 2.1 (*"62,208 Large White sows"*) and Table 1 (*"Number of animals with records: 62,445"*).
  * **Table 2 vs. Table 3 (Phenotypic Variance vs. Standard Deviation):** In Table 2, `NWB` has $\text{SD} = 2.32$ ($\text{SD}^2 = 5.38$), whereas in Table 3 $\sigma_p^2 = 2.17$ ($\sqrt{\sigma_p^2} = 1.47$); conversely for `NDF`, Table 2 has $\text{SD} = 0.26$ ($\text{SD}^2 = 0.068$), whereas Table 3 has $\sigma_p^2 = 0.25$ ($\sqrt{\sigma_p^2} = 0.50$). Check whether the `SD` values for `NWB` and `NDF` in Table 2 were swapped or computed prior to outlier filtering.
  * **Table 3 (Truncated Digits and Standard Errors):** Restore the dropped second decimal places in Table 3 for `NWB` ssGBLUP $\sigma_p^2$ (`2.1` $\to$ `2.17`), `NDF` BLUP $\sigma_p^2$ (`0.2` $\to$ `0.27`), `NSB` BLUP $\sigma_p^2$ (`2.5` $\to$ `2.55`), and `LBWT` BLUP $\sigma_a^2$ standard error (`0.81 (0.00)` $\to$ `0.81 (0.06)`).
  * **Section 2.1:** Clarify *"Records of reproductive performance of 8 pairs or more were all considered '8'"*—change *"8 pairs"* to *"parity 8 or higher"*.
