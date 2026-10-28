# Review of ANON_75

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.0 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.9/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript evaluates genome-wide association studies (GWAS) and genomic prediction (GP) across 195 global oat (*Avena sativa* L.) accessions phenotyped for seven agronomic traits (plant height [PH], cob/panicle length [CL], flag leaf length [FLL], flag leaf width [FLW], spikelets per panicle [SPP], stem diameter [SD], and tiller number [TN]) across two locations in Sichuan, China (Hongyuan, 3504 m; Chengdu, 500 m) over two growing seasons (2021–2023). Using 77,835 Super-GBS SNP markers, the authors characterize population structure ($K = 2, F_{\text{ST}} = 0.24$), estimate SNP heritability via `LDAK-Thin` ($h^2 = 0.55\text{--}0.76$), identify 94 trait-associated SNPs (TASs) using four GWAS models in `GAPIT3`, and compare fivefold cross-validation GP accuracy across GBLUP and six machine-learning (ML) models (Lasso, Ridge, ElasticNet, Kernel Ridge Regression [KRR], SVR-linear, and SVR-poly) using both all 77,835 SNPs and subsets of 100–5,000 GWAS-derived SNPs. Raw sequencing data are deposited in CNGBdb (`CNP0005721`), though no analysis code is provided.

While the multi-environment field dataset across contrasting elevations and the 77,835-SNP genotype panel in hexaploid oat represent a useful empirical resource, the manuscript's primary analytical conclusions are undermined by severe methodological and mathematical errors: (1) in Section 3.5, selecting the top 100–5,000 GWAS markers using GWAS conducted on the **entire 195-accession cohort** before performing fivefold cross-validation introduces classic test-set data leakage, artificially inflating prediction accuracy (especially at 100 markers); (2) in Section 3.4 and Table S6, every value reported as "MAE" is mathematically the **square** of the value reported as "MSE" (e.g., $\text{MSE} = 15.162, \text{MAE} = 229.88 = 15.162^2$; $\text{MSE} = 0.112, \text{MAE} = 0.012 \approx 0.112^2$), violating Jensen's inequality ($\text{MAE} \le \sqrt{\text{MSE}}$) and proving that RMSE/MAE and MSE were miscalculated or transposed; (3) GBLUP and linear Ridge Regression (RR-BLUP) are algebraically equivalent under an additive marker matrix, so GBLUP's reported failure alongside strong Ridge/SVR-linear performance indicates a model-fitting or scaling error; and (4) the regression equations in Section 2.6 contain multiple algebraic errors. Re-running GWAS strictly inside each cross-validation training fold and fixing the error metrics and GBLUP implementation are essential.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **GWAS-derived SNP subsets (100–5,000 markers) achieve higher genomic prediction accuracy than genome-wide markers, peaking at 100 markers for plant height: [Methodologically Flawed].**  
  The GWAS used to rank and select the top 100–5,000 markers (Sections 2.5, 3.3, 3.5) was performed on all 195 accessions jointly, including the 20% validation individuals in each cross-validation fold. When $p = 77,835 \gg n = 195$, ranking predictors by their correlation with the phenotype across the full dataset and then evaluating cross-validation accuracy on those pre-selected predictors leaks validation-set phenotypic information directly into feature selection ("winner's curse" leakage). Under full-sample pre-selection, even a purely random noise trait ($h^2 = 0$) yields high apparent cross-validation accuracy with 100 top SNPs, and accuracy predictably decays as more markers ($500\text{--}5,000$) dilute the overfitted top 100 hits—the exact pattern reported for PH in Figure 5 (line 261).

* **Machine-learning models (specifically linear Ridge Regression and SVR-linear) substantially outperform GBLUP across almost all traits in both correlation accuracy and MSE/MAE: [Methodologically Flawed].**  
  First, linear Ridge Regression on centered/scaled SNP genotypes ($\hat{\beta}_{\text{Ridge}}$) and GBLUP using the VanRaden additive genomic relationship matrix ($G = ZZ^\top / 2\sum p_j(1-p_j)$) are mathematically identical linear models (RR-BLUP $\equiv$ GBLUP) when the regularization parameter $\lambda$ corresponds to the variance ratio $\sigma_e^2/\sigma_u^2$. Reporting that Ridge and SVR-linear achieve $>60\%$ accuracy on FLL while GBLUP performs poorly on all traits except FLW (Figure 4, lines 8, 250) indicates an implementation bug, improper fixed-effect specification, or failure of variance-component convergence in the GBLUP software rather than biological nonlinearity. Second, the MSE and MAE values used to compare models (line 250, Table S6) are mathematically impossible as labeled: across all seven traits, the reported "MAE" equals the square of the reported "MSE" ($0.008^2 \approx 0.0001$; $0.112^2 \approx 0.012$; $14.341^2 = 205.66 \approx 205.68$; $15.162^2 = 229.89 \approx 229.88$; $12.965^2 = 168.09 \approx 168.08$; $17.311^2 = 299.67 \approx 299.66$; $0.105^2 = 0.011$). By Cauchy–Schwarz ($\text{MAE}^2 \le \text{MSE}$), $\text{MAE}$ can never exceed $\sqrt{\text{MSE}}$; the authors evidently reported RMSE (or MAE) as "MSE" and its square as "MAE."

* **The 195 global oat accessions form two differentiated genetic subpopulations ($K = 2, F_{\text{ST}} = 0.24$) with moderate-to-high trait heritabilities ($h^2 = 0.55\text{--}0.76$): [Moderately Supported].**  
  Concordance across `Admixture`, PCA ($\text{PC1} = 24.57\%, \text{PC2} = 9.68\%$), maximum-likelihood phylogenetics, and the kinship matrix supports the division into Group 1 ($n = 75$) and Group 2 ($n = 120$) (Figure 1). However, in Section 2.3 (line 86), retaining SNPs with up to **70% missing values** before `Beagle` imputation in a small ($n = 195$), structured panel introduces substantial genotype imputation uncertainty that is not accounted for in `LDAK-Thin` heritability estimates.

* **Multi-model GWAS identifies 94 Bonferroni-significant trait-associated SNPs across the seven agronomic traits, with 3 TASs stable across multiple environments: [Moderately Supported].**  
  Running four `GAPIT3` models (EMMAX/MLM, BLINK, FarmCPU, SUPER) with a Bonferroni threshold ($0.05 / 77,835$) is standard practice, and highlighting the three multi-environment loci (`chr3A_378078108`, `chr6C_25741715`, `chr5A_16429536`) is appropriately cautious (Section 3.3, 4.1).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Eliminate Data Leakage by Performing GWAS Strictly Inside Each Cross-Validation Training Fold
* **WHY:** Selecting the top 100–5,000 GWAS SNPs using the full 195-accession dataset leaks validation phenotypes into feature selection, causing severe upward bias in fivefold CV accuracy (Figure 5).
* **WHAT:** Re-run the GWAS-assisted GP analysis (Section 3.5) using nested feature selection: in each of the 5 folds, run GWAS using **only the 80% training accessions** ($n = 156$), rank SNPs by training-set GWAS $p$-value, train the GP model on the top $k \in \{100, 500, 1000, 3000, 5000\}$ SNPs in the 80% training fold, and predict the held-out 20% test fold ($n = 39$).
* **HOW:** Embed the `GAPIT` (or fast marginal/MLM association) step and BLUP calculation (`lme4`) inside the outer 5-fold CV loop so that the 20% test genotypes are completely masked during both phenotype BLUP adjustment and SNP ranking.

#### 2. Fix the Squared/Swapped MSE and MAE Calculations and Audit the GBLUP Implementation
* **WHY:** In Section 3.4 (line 250) and Table S6, every reported "MAE" is equal to $(\text{"MSE"})^2$, violating $\text{MAE} \le \sqrt{\text{MSE}}$. Furthermore, GBLUP and Ridge Regression should yield near-identical predictions when fitted on the same additive marker matrix.
* **WHAT:** Inspect the R/Python evaluation script that generated Table S6, correct the formulas for MSE ($\frac{1}{n}\sum (\hat{y}_i - y_i)^2$), RMSE ($\sqrt{\text{MSE}}$), and MAE ($\frac{1}{n}\sum |\hat{y}_i - y_i|$), and verify why GBLUP diverged from Ridge Regression.
* **HOW:** Check whether the script computed `mse = sqrt(mean((f - y)^2))` (or `mean(abs(f - y))`) and then computed the second column by squaring the first column (`mae = mse^2`). Re-compute true MSE, RMSE, and MAE on the original phenotypic units. For GBLUP, verify that the genomic relationship matrix $G$ is properly scaled and positive-definite (`G + 1e-4 * I`) and that the same training-fold centering is applied as in Ridge Regression.

#### 3. Account for Strong Subpopulation Structure ($F_{\text{ST}} = 0.24$) in Cross-Validation and BLUP Calculation
* **WHY:** In Equation (75) (line 75), the subpopulation group effect $\alpha_k$ ($k \in \{1, 2\}$) is included in the phenotypic linear model, and random 80/20 CV splits across a strongly structured cohort ($F_{\text{ST}} = 0.24$) conflate between-group population structure with within-group genomic prediction accuracy.
* **WHAT:** Specify whether $G_i$ BLUPs used as the target $y_c$ had the subpopulation effect $\alpha_k$ removed or retained, and report stratified/within-group cross-validation accuracy (predicting within Group 1 and within Group 2, as well as across groups).
* **HOW:** Run fivefold CV separately within Group 1 ($n = 75$) and Group 2 ($n = 120$), and compare against stratified 5-fold CV on the combined panel.

#### 4. Correct the Mathematical Equations in Section 2.6
* **WHY:** Equations in Section 2.6 contain multiple sign and notation errors that do not match the actual optimization problems of Ridge, Lasso, ElasticNet, and SVR.
* **WHAT & HOW:**
  1. **Lines 127, 137, 155, 163 (Bridge, Ridge, Lasso, ElasticNet):** Change the plus sign inside the squared residual term $\left(y_i + \sum_{j=1}^p x_{ij}\beta_j\right)^2$ to a minus sign: $\left(y_i - \sum_{j=1}^p x_{ij}\beta_j\right)^2$.
  2. **Line 141 (KRR header):** Fix *"The ElasticNet regression method is:"* on line 141 to *"The KRR method is:"*.
  3. **Line 163 (ElasticNet penalty):** Distinguish the L1 and L2 regularization weights (e.g., $\lambda_1 \sum_{j=1}^p |\beta_j| + \lambda_2 \sum_{j=1}^p \beta_j^2$).
  4. **Line 181 (SVR-linear objective):** Restore the missing response $y_i$, absolute value bars, and closing parenthesis: $\min_{\beta_0, \beta} \left(\frac{1}{2}\|\beta\|^2 + C \sum_{i=1}^n \max\left(0, |y_i - (\beta_0 + x_i^\top \beta)| - \varepsilon\right)\right)$.

#### 5. Technical and Editorial Cleanup
* **WHY:** Swapped geographic coordinates, missing SNP-filtering justification, and duplicate text blocks reduce clarity.
* **WHAT & HOW:**
  1. **Line 55 (Field trial coordinates):** Both latitudes are mislabeled as East longitude (`°E`), and the coordinates of Hongyuan and Chengdu are swapped (`Hongyuan... 103.71°E, 30.45°E` and `Chengdu... 102.32°E, 32.46°E`; Chengdu is near $104.06^\circ\text{E}, 30.67^\circ\text{N}$ at 500 m, whereas Hongyuan is near $102.54^\circ\text{E}, 32.80^\circ\text{N}$ at 3504 m). Correct the coordinates and change latitude units to `°N`. Also delete the duplicated phrase `"and site management followed local best practices."` at the end of line 55.
  2. **Lines 58–64:** Remove the duplicate `Core Ideas` block inserted inside Section 2.1.
  3. **Line 69 & Line 86:** Change `"FN was determined by counting the number of all the main stems and lateral branches"` to `"TN..."` (tiller number, line 69), and delete the duplicated sentence fragment in line 86 (`"and all the bases with a fastqc QC score of less than 20 at the 3′ end of the digest site"`).
  4. **Line 228:** Fix the typo `"LADK-Thin"` to `"LDAK-Thin"`.
