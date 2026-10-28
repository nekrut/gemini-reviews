# Review of PMC11668851 (PMID:39719433)

**Manuscript Title:** Gut microbiota dysbiosis promotes cognitive impairment via bile acid metabolism in major depressive disorder  
**Authors:** Jia M, Fan Y, Ma Q, Yang D, Wang Y, He X, Zhao B, Zhan X, Qi Z, Ren Y, Dong Z, Zhu F, Wang W, Gao Y, Ma X.  
**Journal / Preprint:** *Transl Psychiatry* (2024; `PMC11668851` / `PMID:39719433` / `10.1038/s41398-024-03211-4`)  
**Calibration Study Cohort:** Cohort C — Wild Literature Sample (`C59` | Double-Blinded as `ANON_105`)  
**Overall Score:** **6.0 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.7/3.5 | Claims: 1.4/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This cross-sectional multi-omics study investigates associations among the gut microbiome, serum metabolome (specifically bile acids and neurotransmitter-like metabolites), and cognitive function (measured via the digitized THINC-it battery) in Major Depressive Disorder (MDD). In Cohort 1 ($104$ MDD patients and $77$ healthy controls [HCs] with untargeted LC-MS serum metabolomics, of whom $79$ MDD and $60$ HCs underwent fecal shotgun metagenomic sequencing), the authors identify $123$ differentially abundant bacterial species and $1,236$ altered metabolic features, highlighting elevated conjugated primary bile acids (GCDCA, TCDCA) and secondary glycolithocholic acid (GLCA) alongside depleted secondary bile acids (LCA, TLCA, GUDCA, TUDCA) and tryptophan metabolites. HUMAnN functional profiling links reduced *Lachnospiraceae* abundance to decreased bile salt hydrolase (`EC:3.5.1.24`) gene abundance and elevated *Escherichia coli*/*Klebsiella* to increased $7\alpha$-hydroxysteroid dehydrogenase (`EC:1.1.1.159`). Using LASSO regression, GUDCA and TUDCA positively associate with THINC-it cognitive scores while GLCA and GCDCA negatively associate. A second cohort ($40$ MDD and $40$ HCs) underwent targeted LC-MS/MS profiling of amino acids and bile acids. Fecal metagenomic sequencing reads are deposited in the Genome Sequence Archive (`CRA019246`), though metabolomics matrices and analysis code are not publicly archived.

Combining shotgun metagenomics, untargeted and targeted serum bile acid quantification, and standardized cognitive testing across 261 participants provides a valuable multi-omic dataset. However, the statistical analysis and framing suffer from three main limitations: (1) the reported diagnostic Random Forest classifiers ($\text{AUC} = 0.99$ in Figure 4D and Supplementary Figure 7) suffer from data leakage and in-sample overfitting because input features (`LDA > 2.5, P < 0.05` and `VIP > 1, FDR < 0.05`) were pre-selected across the entire dataset without nested cross-validation or external test evaluation; (2) Cohort 2 ($N = 80$, which has both targeted bile acid measurements and THINC-it cognitive scores) is only shown as a KEGG pathway bubble plot (Figure 3D) rather than being used as an out-of-sample test set for the bile acid classifier and LASSO cognitive models; and (3) section headings and figure titles make causal claims ("mediated," "promote cognitive impairment") from cross-sectional correlations. All three issues can be resolved through computational re-analysis of the existing two-cohort data.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **A combinatorial Random Forest marker classifier of gut microbes and bile acids (or neurotransmitter-like metabolites) robustly differentiates MDD patients from HCs with an AUC of 0.99 (and 0.88–0.93 for metabolites alone): [Methodologically Flawed].**  
  As described in the Methods (line 61), microbial features (`LDA > 2.5` and $P < 0.05$) and metabolic features (`VIP > 1` and $\text{FDR} < 0.05$) were first selected using the full Cohort 1 case–control labels, and the Random Forest classifier was then trained and evaluated on the same cohort without an independent train/test split or nested cross-validation, while variables were further subsetted to "those that yielded the maximum Area Under the Curve." This circular feature selection and in-sample evaluation severely inflates the AUC to $0.99$. Furthermore, the bile-acid-only classifier ($\text{AUC} = 0.88$) was never tested on Cohort 2 ($40$ MDD, $40$ HCs), where targeted bile acids were measured.

* **Patients with MDD exhibit altered serum bile acid and tryptophan profiles alongside decreased microbial bile salt hydrolase (`EC:3.5.1.24`) and increased $7\alpha$-HSDH (`EC:1.1.1.159`) gene abundance: [Moderately Supported].**  
  The concordance between shotgun metagenomic enzymatic abundance (`EC:3.5.1.24` in *Lachnospiraceae* and `EC:1.1.1.159` in *Enterobacteriaceae*) and serum primary/secondary bile acid shifts is biologically coherent. However, in the untargeted LC-MS analysis of Cohort 1 (Figure 3A–B), $1,236$ of $4,147$ total features ($29.8\%$) differed at $\text{FDR} < 0.05$ with an OPLS-DA $Q^2 = 0.903$, an unusually massive global separation that suggests potential pre-analytical or LC-MS batch effects between patient and control recruitment. Moreover, for the targeted validation in Cohort 2, the main text only displays a pathway enrichment bubble plot (Figure 3D) without reporting metabolite-level effect sizes, $p$-values, and directional concordance with Cohort 1.

* **Secondary bile acids (GUDCA, TUDCA, GLCA) and conjugated primary bile acid GCDCA are associated with THINC-it cognitive performance in MDD after adjusting for age, sex, BMI, and education: [Moderately Supported].**  
  LASSO regression in Cohort 1 adjusts for education level (the only demographic variable that differed significantly between MDD and HCs; Results line 69). However, the authors did not test whether the LASSO-selected bile acid predictors (GUDCA, TUDCA, GLCA, GCDCA) replicate their association with THINC-it Objective and Composite Cognition in Cohort 2, even though all 80 participants in Cohort 2 completed the THINC-it battery and targeted bile acid profiling (Results line 69).

* **Gut microbiota dysbiosis mediates abnormal bile acid metabolism to promote cognitive impairment in MDD: [Overstated].**  
  While the Discussion (chunk 2, line 5) appropriately notes that the cross-sectional design cannot establish causality, the Results headings and Figure 4–6 captions explicitly claim directional causation ("Gut microbiota dysbiosis in patients with MDD contribute to the abnormalities of serum metabolites," "Gut microbes mediated abnormal bile acid metabolic pathway," "Gut microbes influence bile acid metabolism, promoting cognitive impairment"). In addition, the Random Forest models predicting serum bile acids from gut species explain only $10.9\%$–$11.2\%$ of variance in GUDCA and GLCA (Figure 4B), and no formal statistical mediation model (nor partial correlation controlling for depression severity HAMD-17 or education in the CIA/network plots) was performed.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Eliminate Feature-Selection Leakage and Validate the Bile Acid Classifier Out-of-Sample in Cohort 2
* **WHY:** Selecting differential species and metabolites on the entire cohort and evaluating Random Forest ROC curves on the same samples produces overfitted AUCs ($0.99$).
* **WHAT:** Re-evaluate the Cohort 1 multi-omics classifiers using repeated 10-fold nested cross-validation (where differential feature selection is performed strictly inside each training fold), and evaluate the Cohort 1–trained bile acid and amino acid classifiers directly on the independent Cohort 2 ($40$ MDD, $40$ HCs).
* **HOW:** In R (`caret` or `tidymodels` with `randomForest`), wrap the Wilcoxon/LEfSe and $t$-test/VIP feature-filtering step inside each training fold of a 10-fold CV loop on Cohort 1 ($N = 139$) to compute an unbiased out-of-fold AUC and 95% CI. Then, take the targeted bile acid / amino acid Random Forest model trained purely on Cohort 1 ($N = 181$) and predict case–control status in Cohort 2 ($N = 80$), plotting both the cross-validated Cohort 1 ROC curve and the external Cohort 2 validation ROC curve in Figure 4D.

#### 2. Report Metabolite-Level Replication and Cognitive Association Validation in Cohort 2
* **WHY:** All 80 participants in Cohort 2 have targeted LC-MS/MS bile acid/amino acid measurements and complete THINC-it cognitive assessments (Results line 69), yet Cohort 2 is only used for a single KEGG bubble plot (Figure 3D).
* **WHAT:** Provide a side-by-side comparison table of individual bile acids and tryptophan metabolites across Cohort 1 (untargeted) and Cohort 2 (targeted quantitative concentrations in $\mu\text{M}$ or $\text{ng/mL}$), and test whether GUDCA, TUDCA, GLCA, and GCDCA predict THINC-it Objective and Composite Cognition in Cohort 2.
* **HOW:** Add a main-text table reporting mean $\pm$ SD (or median/IQR), $\log_2$ fold change, Wilcoxon/$t$-test $p$-value, and BH-adjusted FDR for each targeted bile acid and amino acid in Cohort 1 vs. Cohort 2. Fit the age-, sex-, BMI-, and education-adjusted regression models (and LASSO predictions) for THINC-it scores in Cohort 2 and report the replication $R^2$, $\beta$ coefficients, and $p$-values in Section 6 of Results.

#### 3. Control for Education Level, Depression Severity, and Intermittent Medication Use in Multi-Omic Networks
* **WHY:** Education differed significantly between MDD and HCs (line 69) and strongly influences THINC-it performance; depression severity (HAMD-17/PHQ-9) correlates with both microbiome composition (PERMANOVA, line 74) and cognitive scores; and 11 MDD patients in Cohort 1 had recent antidepressant exposure (sertraline/escitalopram).
* **WHAT:** Compute partial Spearman correlations adjusted for age, sex, BMI, education, and HAMD-17 score for the network in Figure 6E, and run a sensitivity analysis excluding the 11 patients with recent sertraline/escitalopram use.
* **HOW:** Use the `ppcor` package in R (`pcor.test(..., method = "spearman")`) controlling for `age + sex + BMI + education + HAMD17`, apply Benjamini–Hochberg FDR $< 0.05$ across all pairwise edges in Figures 4B–C, 5H, and 6E, and verify in a supplementary table that key differential taxa and bile acids remain significant when restricted to the 93 medication-naïve Cohort 1 MDD patients.

#### 4. Align Section Headings and Figure Titles with the Cross-Sectional Design
* **WHY:** Causal verbs in Results subheadings and figure titles contradict the observational, cross-sectional study design acknowledged in the Discussion.
* **WHAT & HOW:**
  * Revise the Results subheadings at lines 102, 115, and 130 and the titles of Figures 4, 5, and 6 to use associative language (e.g., change *"Gut microbes influenced bile acid metabolism promote cognitive impairment in MDD"* to *"Associations among gut microbial bile acid pathways, serum bile acids, and cognitive impairment in MDD"*).

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Package name errors, duplicated species names, and acronym typos reduce clarity.
* **WHAT & HOW:**
  * **Introduction (line 21):** Change "40 patents with MDD" to "40 patients with MDD".
  * **Methods (line 40) & Results (line 69):** Change "Spotter, and Trials" to "Spotter, and Trails" (Trail Making Test).
  * **Methods (line 61):** Change "The random 4.6-12 package" to "The `randomForest` (v4.6-12) R package".
  * **Results (line 104):** Remove the duplicate listing of `Blautia_massiliensis` in the sentence listing negative predictors of GLCA.
  * **Results (line 132):** Change "PQD-5-D" to "PDQ-5-D".
  * **Data Availability:** Deposit the de-identified Cohort 1 and Cohort 2 serum metabolomics abundance matrices in MetaboLights or Metabolomics Workbench and provide the accession ID.
