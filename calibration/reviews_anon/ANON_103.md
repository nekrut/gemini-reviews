# Review of ANON_103

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.5 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.9/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript constructs and validates genome-wide polygenic scores (GPS) for five common complex diseases—coronary artery disease (CAD), atrial fibrillation (AF), type 2 diabetes (T2D), inflammatory bowel disease (IBD), and breast cancer—using external European-ancestry GWAS summary statistics. For each disease, 31 candidate predictors (24 pruning-and-thresholding scores and 7 LDpred Bayesian shrinkage scores across causal fraction parameter $\rho \in [0.001, 1.0]$) were tuned in the UK Biobank Phase 1 validation cohort ($N = 120,280$) and evaluated in an independent UK Biobank Phase 2 testing cohort of white British ancestry ($N = 288,978$). The authors report that the top tails of the polygenic distributions identify $8.0\%$, $6.1\%$, $3.5\%$, $3.2\%$, and $1.5\%$ of the population at an odds ratio (OR) $\ge 3.0$ relative to the remainder of the population for CAD, AF, T2D, IBD, and breast cancer, respectively, with $19.8\%$ of individuals falling into the $\text{OR} \ge 3.0$ tail for at least one of the five diseases. Score weights and software pipelines (PLINK, LDpred, Hail, R) are publicly available.

This is a well-executed, statistically powered study with a strict separation between external discovery GWAS datasets, hyperparameter tuning (UK Biobank Phase 1), and out-of-sample testing (UK Biobank Phase 2), complemented by sensitivity analyses excluding related individuals ($N = 222,529$). Two methodological and interpretive issues warrant clarification. First, defining "carriers" of $\ge 3$-fold risk as the entire upper tail slice whose *aggregate* odds ratio vs. the remainder equals $3.0$ overstates the risk of individuals near the threshold: because the tail average is pulled upward by extreme percentiles ($\text{OR} > 5$), individuals between the 92nd and 95th percentiles for CAD actually have an individual marginal OR well below $3.0$. Second, Table 1 reports AUCs ($0.81$ for CAD, $0.77$ for AF) from logistic models that include age and sex alongside the GPS, without displaying the baseline covariate-only AUC or the GPS-only AUC in the main table. Both issues can be resolved through straightforward reporting additions and precise phrasing.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **LDpred genome-wide polygenic scores outperform pruning-and-thresholding and previously published smaller scores across four of the five diseases, with virtually identical discrimination in validation and testing cohorts: [Well Supported].**  
  The two-stage validation ($N = 120,280$) and independent testing ($N = 288,978$) design prevents overfitting of the tuning parameter $\rho$, and Supplementary Table 10 confirms robustness after removing third-degree or closer relatives.

* **8.0%, 6.1%, 3.5%, 3.2%, and 1.5% of the population inherit a genetic predisposition conferring $\ge 3$-fold increased risk for CAD, AF, T2D, IBD, and breast cancer, respectively: [Overstated].**  
  In Tables 2 and 3, the authors determine the upper tail proportion $p$ by setting the group-level odds ratio of the top $p\%$ versus the remaining $(100 - p)\%$ to $\ge 3.0$. Because this compares the mean risk across the entire upper tail against the mean risk of the lower $(100 - p)\%$, individuals near the cutoff (e.g., the 92nd percentile for CAD) do not have a 3-fold risk relative to the population mean or even relative to the bottom $92\%$. As Table 3 shows for CAD, the top $10\%$ vs. remaining $90\%$ has $\text{OR} = 2.89$ and the top $5\%$ vs. remaining $95\%$ has $\text{OR} = 3.34$; by algebraic decomposition, individuals in the 90th–95th percentile slice have an OR of roughly $2.1$–$2.3$ relative to the bottom $90\%$. Thus, $8.0\%$ is the size of a high-risk group whose *average* odds ratio is $3.0$, not the fraction of individuals whose personal genetic risk is $\ge 3$-fold.

* **The CAD polygenic predictor achieves an AUC of 0.81 in the testing dataset: [Moderately Supported].**  
  In the text (line 46: "The predictors had AUC ranging from 0.79–0.81... with AUC of 0.81") and Table 1, the reported AUC is for a joint logistic regression model containing GPS, age, sex, genotyping array, and four genetic PCs. In UK Biobank, age and sex alone account for most of the discriminative capacity for CAD and AF, whereas the incremental $\Delta\text{AUC}$ from the GPS itself is much smaller (as reflected by IBD having an AUC of $0.63$ where age and sex contribute minimally). Presenting the joint model AUC as the performance of "the predictor" without listing the covariate-only baseline AUC in Table 1 obscures the genetic contribution.

* **Conventional clinical risk factors cannot identify the high-GPS CAD subgroup in the absence of genotype information: [Moderately Supported].**  
  While family history ($44\%$ vs. $35\%$) and hypercholesterolemia ($20\%$ vs. $13\%$) show only modest enrichment in the top $8\%$ GPS tail, clinical risk factors and prevalent CAD in UK Biobank were ascertained cross-sectionally at middle age (mean age 57), when many high-risk individuals and prevalent CAD cases were already receiving lipid-lowering or antihypertensive therapy, attenuating unmedicated biomarker differences.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Distinguish Marginal Individual Risk at the Cutoff from Average Tail-Group Odds Ratios
* **WHY:** Grouping everyone above the 92nd percentile and reporting that the group as a whole has $\text{OR} = 3.0$ relative to the bottom $92\%$ conflates the group average (driven by the 99th+ percentile) with the marginal risk of an individual at the 92nd percentile, and using the bottom $(100 - p)\%$ as the reference group shifts the baseline as $p$ changes.
* **WHAT:** Report (i) the percentile threshold at which an *individual's marginal predicted risk* (or narrow percentile bin risk, e.g., 1%-wide bins in Figures 2c and 3) reaches $3.0\times$ the population mean (or median decile 45–55%), alongside (ii) the cumulative tail group average OR currently in Table 2.
* **HOW:** Using the per-percentile prevalence estimates already computed for Figures 2c and 3 and the continuous logistic model $\text{logit}(P(Y=1)) = \alpha + \beta \cdot \text{GPS} + \gamma^T Z$, compute the standardized GPS value $z^*$ where $\exp(\beta z^*) = 3.0$ (relative to the population mean $\text{GPS} = 0$) and report the tail probability $1 - \Phi(z^*)$ alongside Table 2. Clarify in the Abstract and text that Table 2 reflects the *average risk of the upper tail subgroup relative to the remainder of the cohort*.

#### 2. Report Covariate-Only and GPS-Only AUCs Alongside Joint Model AUCs in Table 1
* **WHY:** Readers interpreting Table 1 ("AUC in testing dataset: 0.81" for CAD vs. "0.63" for IBD) may attribute the 0.81 AUC to the polygenic score rather than to age and sex.
* **WHAT:** Add columns to Table 1 (or expand the existing AUC columns) showing: (1) Covariates-only AUC (age, sex, array, 4 PCs), (2) GPS-only AUC, and (3) Full model AUC (GPS + covariates), along with the incremental $\Delta\text{AUC}$.
* **HOW:** Extract the predicted probabilities from the baseline covariate-only logistic regression models (already fitted to compute incremental Nagelkerke's pseudo-$R^2$ in Supplementary Table 9) and the GPS-only models (already fitted for Supplementary Figures 2–3), compute their `pROC` AUCs and 95% CIs, and include them in Table 1.

#### 3. Separate Prevalent and Incident Disease Ascertainment
* **WHY:** Combining retrospective self-reported/hospitalized prevalent cases at enrollment with incident cases in a cross-sectional logistic regression is vulnerable to survival bias (fatal early-onset CAD cases are missing from enrollment) and treatment confounding.
* **WHAT:** Provide a sensitivity table comparing GPS effect sizes (hazard ratios via Cox proportional hazards regression) restricted to incident cases occurring after UK Biobank baseline assessment against the prevalent case odds ratios.
* **HOW:** Stratify the composite EHR/OPCS-4 outcomes in the testing set ($N = 288,978$) by diagnosis date relative to recruitment date, fit age- and sex-adjusted Cox models for incident cases among baseline-free participants, and report the hazard ratios for the top $20\%, 10\%, 5\%, 1\%$, and $0.5\%$ GPS strata.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Minor numerical and formatting discrepancies across the text, tables, and figure captions should be corrected for consistency.
* **WHAT & HOW:**
  * **Online Methods (line 210):** Correct the testing dataset sample size typo from "$288,278$ participants" to "$288,978$ participants" (matching lines 18, 44, 191, and Tables 1–2).
  * **Table 2 (lines 70, 71, 83):** Insert the missing division slashes `/` in the testing dataset fractions for Type 2 diabetes (`10,099/288,978`), Inflammatory bowel disease (`9,209/288,978`), and Atrial fibrillation OR $\ge 5.0$ (`2,020/288,978`).
  * **Table 1 (line 33):** Fix the notation typo "`r/ 2 < 0.2`" to "$r^2 < 0.2$".
  * **Figure 2b–c (line 54) and Figure 3 (line 100) Captions:** Verify whether panels 2b, 2c, and Figure 3 plot the *validation cohort* ($N = 120,280$, as stated in the captions) or the *testing cohort* ($N = 288,978$, as implied in the main text lines 48–56 and 94), and harmonize the labels accordingly.
