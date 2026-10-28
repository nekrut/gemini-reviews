# Review of PMC12185455 (PMID:40557150)

**Manuscript Title:** Construction of a novel inflammatory-related prognostic signature of acute myelocytic leukemia based on conjoint analysis of single-cell and bulk RNA sequencing  
**Authors:** Huang Y, Yi P, Wang Y, Wang L, Cao Y, Lu J, Fang K, Cheng Y, Miao Y.  
**Journal / Preprint:** *Front Immunol* (2025; `PMC12185455` / `PMID:40557150` / `10.3389/fimmu.2025.1565954`)  
**Calibration Study Cohort:** Cohort C — Wild Literature Sample (`C97` | Double-Blinded as `ANON_89`)  
**Overall Score:** **4.0 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.2/3.5 | Claims: 1.0/2.5 | Biology: 1.0/2.0 | Reproducibility: 0.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript combines an internal bone marrow single-cell RNA-seq (scRNA-seq) cohort of 11 acute myeloid leukemia (AML) patients and 2 controls with four public bulk transcriptomic cohorts (GSE114868, GSE37642, TCGA-LAML, and GSE106291) to construct an inflammation-related prognostic signature for AML. Using `SingleR` annotation and `Seurat::FindAllMarkers` on 97,531 cells, the authors identify 1,594 marker genes across four myeloid/progenitor clusters (GMP, HSC/Prog, Mono/Macro, and myelocytes), intersect them with WGCNA module genes and differentially expressed genes (DEGs) from GSE114868 to yield 35 candidate genes, and apply univariate Cox and LASSO regression in GSE37642 ($n = 417$) to derive a five-gene risk score (`CALR`, `KDM1A`, `SUCNR1`, `TMEM220`, and `ADM`). The risk score is evaluated in TCGA-LAML ($n = 130$) and GSE106291 ($n = 250$), correlated with `ESTIMATE` immune/stromal scores and `oncoPredict` IC50 estimates, and mapped back onto the scRNA-seq clusters. Public GEO/TCGA accession IDs are cited, but raw sequencing data for the 13 internal scRNA-seq samples and analysis code are not publicly deposited.

While integrating single-cell bone marrow profiling with external survival cohorts is a reasonable strategy for biomarker discovery, the manuscript is undermined by internal mathematical contradictions, cell-level pseudoreplication, unadjusted clinical confounding, and overstated predictive accuracy. Most critically, the sign of the LASSO coefficient for `KDM1A` ($+0.28535$, indicating higher risk with higher expression) directly contradicts the Results text claiming that low `KDM1A` expression predicts poor survival and worsens across cytogenetic risk groups. In the scRNA-seq analysis, treating 97,531 cells from 11 AML patients and 2 non-healthy controls as independent statistical units invalidates the differential proportion and ssGSEA p-values, and subgroup comparisons across cytogenetic risk strata rely on $n = 1$ patient in the favorable group. Finally, the model achieves time-dependent ROC AUCs only slightly above 0.60 and is never tested in a multivariable Cox model controlling for age or ELN cytogenetic risk, despite the risk score being strongly elevated in patients older than 60 years. Resolving these issues requires reconciling the survival direction of `KDM1A`, aggregating scRNA-seq comparisons to the patient (pseudobulk) level, and demonstrating prognostic value independent of age and cytogenetics.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Bone marrow scRNA-seq reveals significant depletion and ssGSEA downregulation of GMP, HSC/Prog, Mono/Macro, and myelocyte populations in AML patients compared to healthy donors, with progressive `CALR` and `KDM1A` decline across risk groups 0 to 3: [Methodologically Flawed].**  
  First, the control group consists of only $n = 2$ individuals with "monophyletic reduction" (Materials and Methods, line 40), who are neither healthy donors (despite being labeled "healthy donors" in the Figure 1H caption) nor a statistically powered baseline. Second, differential marker discovery (`FindAllMarkers`) and cell-level ssGSEA comparisons (Figure 2B) treat 97,531 individual cells as independent observations rather than nesting cells within patients ($N = 13$), causing severe pseudoreplication. Third, the favourable cytogenetic risk group (group 1) contains only $n = 1$ patient (Table 1, line 57), rendering the claim of a gradual decrease across groups 0 to 3 (Figure 7C) statistically uninformative.

* **Intersection of scRNA-seq core markers, WGCNA MEblue module genes, and GSE114868 DEGs identifies a five-gene LASSO signature (`CALR`, `KDM1A`, `SUCNR1`, `TMEM220`, `ADM`) with consistent prognostic direction: [Methodologically Flawed].**  
  The explicit LASSO formula in the Results (line 146) is $\text{Risk score} = -0.44751 \times \text{CALR} + 0.28535 \times \text{KDM1A} + 0.11832 \times \text{ADM} - 0.20546 \times \text{TMEM220} - 0.06282 \times \text{SUCNR1}$, where `KDM1A` has a positive weight ($+0.28535$, meaning higher `KDM1A` increases risk). Two sentences later (line 146), the text reports that *low* expression of `KDM1A` is associated with poor prognosis in Kaplan–Meier analysis (Figure 4E), and line 169 reports that `KDM1A` decreases from control (group 0) to unfavorable risk (group 3), whereas the Discussion (line 193) cites `KDM1A` as an oncogene whose inhibition treats AML. Additionally, the number of WGCNA AML-associated genes is reported as 2,067 in the Abstract (line 16) and Discussion (line 193), but as 2,967 in the Results (line 135).

* **The five-gene risk model accurately distinguishes survival outcomes in external validation cohorts (TCGA-LAML and GSE106291): [Overstated].**  
  In TCGA-LAML, time-dependent ROC AUCs at 1, 2, 3, and 4 years are merely described as ">0.6" (line 146; Figure 5C), which represents weak discrimination only modestly above random chance (0.50). No ROC AUCs or Harrell's C-indices are reported for the training cohort (GSE37642) or second validation cohort (GSE106291). Crucially, the authors show that the risk score is significantly higher in patients aged $>60$ years across both validation sets (Figures 5E and 6C), yet they perform no multivariable Cox regression adjusting for age, WBC count, or ELN cytogenetic risk, nor do they benchmark the five-gene score against standard clinical risk stratification.

* **High-risk patients exhibit altered inflammatory microenvironments and differential sensitivity to nine chemotherapy/targeted agents: [Fragile].**  
  Higher `ESTIMATE` ImmuneScore and StromalScore in high-risk bulk AML samples (Figure 5F–G) largely reflect variation in leukemic blast purity and myelomonocytic differentiation rather than non-malignant immune infiltration, because myeloid blasts themselves express hematopoietic immune signature genes used by `ESTIMATE`. Similarly, `oncoPredict` drug sensitivity values (Figure 8) are imputed directly from cancer cell line linear ridge regressions on the same bulk gene expression matrix; correlating imputed IC50 values with the genes used to stratify the samples is mathematically circular without wet-lab or ex vivo pharmacological validation.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Resolve the Mathematical Contradiction in `KDM1A` Survival Direction
* **WHY:** A biomarker cannot simultaneously carry a positive hazard coefficient ($+0.28535$) in the linear risk predictor and be protective (low expression associated with poor survival) in univariate Kaplan–Meier and scRNA-seq progression analyses without either a coding error in group labeling or severe collinearity/sign reversal.
* **WHAT:** Audit the univariate Cox hazard ratios, LASSO coefficients, and Kaplan–Meier high/low group labels for all five signature genes in GSE37642, TCGA-LAML, and GSE106291.
* **HOW:** Extract and tabulate the exact univariate Cox $\beta$, hazard ratio (HR), 95% confidence interval, $p$-value, and LASSO $\beta$ for each of the 7 univariate-significant genes in GSE37642. Verify whether the median split in Figure 4E inverted the high/low labels for `KDM1A`, and correct either the risk formula or the text/figures accordingly.

#### 2. Test Independent Prognostic Value via Multivariable Cox Regression and Clinical Benchmarks
* **WHY:** Age $\ge 60$ years is one of the strongest established predictors of mortality in AML (as noted in the Introduction, line 28), and Figures 5E and 6C show that the five-gene score is strongly associated with age $>60$. Without multivariable adjustment, the signature may simply act as a transcriptomic surrogate for age.
* **WHAT:** Perform multivariable Cox proportional hazards regression and compare C-indices against clinical covariates in GSE37642, TCGA-LAML, and GSE106291.
* **HOW:** Using `survival::coxph` in R, fit models including the continuous risk score alongside age, sex, WBC count, and cytogenetic/ELN risk category. Report the adjusted HRs, 95% CIs, and $p$-values in a new table, and compute `survcomp::concordance.index` comparing Clinical-only, Signature-only, and Combined models across all three cohorts.

#### 3. Replace Cell-Level Testing with Patient-Level Pseudobulk Aggregation in scRNA-seq
* **WHY:** Testing differential expression and ssGSEA scores across 97,531 cells treats cells from the same bone marrow aspirate as independent samples, yielding artificially tiny $p$-values (`**** p < 0.0001` in Figure 2B) when the true sample size is $n = 11$ AML vs. $n = 2$ controls.
* **WHAT:** Aggregate scRNA-seq counts and cell-type proportions at the patient level before statistical testing, and remove statistical trend claims across cytogenetic risk groups where $n = 1$.
* **HOW:** Use `Seurat::AggregateExpression(seurat_obj, group.by = c("celltype", "patient_id"))` to generate patient-level pseudobulk profiles, compute patient-level ssGSEA scores and cell-type proportions (13 values per cell type), and compare AML ($n = 11$) vs. control ($n = 2$) using exact Wilcoxon rank-sum tests with explicit acknowledgment that $n = 2$ controls precludes definitive inference.

#### 4. Temper Claims of Predictive Accuracy and Clarify Dataset Modalities
* **WHY:** Describing AUCs barely above 0.60 as "remarkable prognostic value" and "accurately distinguish[ing] survival outcomes" overstates the empirical performance, and referring to GSE37642 (an Affymetrix Human Genome U133 Plus 2.0 / U133A microarray cohort) as "Bulk RNA-seq" is technically inaccurate.
* **WHAT:** Report exact numerical AUCs with 95% confidence intervals for all cohorts and accurately describe microarray versus RNA-seq platforms.
* **HOW:** Use `timeROC` in R to compute 1-, 2-, 3-, and 4-year AUCs and 95% CIs for GSE37642, TCGA-LAML, and GSE106291; add these exact numbers to the Abstract and Results; and revise the Methods (line 90) to describe GSE37642 and GSE114868 as bulk transcriptomic/microarray datasets where applicable.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Numerical discrepancies between sections, table arithmetic errors, and missing data accessions impede verification and reproducibility.
* **WHAT & HOW:**
  1. **WGCNA gene count discrepancy (Abstract line 16, Results line 135, Discussion line 193):** Reconcile whether the `MEblue` module contains 2,067 genes (Abstract/Discussion) or 2,967 genes (Results line 135).
  2. **Table 1 arithmetic and headers (lines 71–80):** Under "Extramedullary infiltration," `No: 10 (100%)` out of 11 patients is mathematically incorrect (10/11 is 91%, with 1 patient missing or positive); under "Fusion gene (n, 10%)," change `10%` to `%`.
  3. **Control cohort nomenclature (line 40 vs. line 119):** Replace "healthy donors" in the Figure 1H caption with "control individuals with monophyletic reduction" to match the Materials and Methods.
  4. **Data and code availability (line 210):** Deposit the raw/processed scRNA-seq count matrices for the 13 bone marrow samples in GEO or GSA-Human and provide the accession number and R analysis scripts.
