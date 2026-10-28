# Peer Review: ANON_171

**Overall Score:** **4.8 / 10.0** (Flawed / Overstated)
* **Score Breakdown:** Rigor: 1.3/3.5 | Claims: 1.1/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.2/2.0

---

## 1. Executive Summary & Synthesis

This manuscript reports a multi-center 16S rRNA (V4 region) gut microbiome survey of 374 hospitalized patients from Departments of Pulmonary and Critical Care Medicine (PCCM) across three hospitals in southern China, compared against 105 healthy controls. The authors stratify patients into seven respiratory disease categories (non-small cell lung cancer, small cell lung cancer, pneumonia, COPD, asthma, pulmonary embolism/hypertension, and other pulmonary diseases) and perform alpha/beta diversity comparisons, community state (enterotype) clustering, distance-based redundancy analysis (db-RDA) against clinical variables, Spearman correlation networks, and a 15-genus Random Forest classification between inpatients and healthy controls.

While the clinical cohort size ($n = 374$ baseline admission fecal samples plus $n = 105$ controls) and multi-center sampling are potentially useful descriptive resources, the manuscript suffers from severe internal contradictions, statistical and causal inference flaws, and unadjusted confounding. Most notably, the Abstract and Discussion claim that *four* enterotypes were identified, directly contradicting the Results section and Figure 3C, which report *three* enterotypes (`Lachnospiraceae`, `Enterobacteriaceae`, and `Enterococcaceae`). Furthermore, the statistical comparisons between inpatients and healthy controls rely on univariate tests (Wilcoxon rank-sum, Kruskal-Wallis, ANOSIM) that do not adjust for major baseline confounders—specifically BMI ($21.37$ vs. $23.26\text{ kg/m}^2, P < 0.01$) and smoking ($53.5\%$ vs. $28.6\%, P < 0.01$)—despite an unsupported assertion in the Methods that analyses were adjusted for age and smoking. The db-RDA analysis also reverses temporal causality by treating *subsequent* total length of hospital stay and total hospitalization costs as explanatory drivers of Day-1 admission microbiota.

---

## 2. Claim-by-Claim Evaluation

* **Claim 1:** *Hospitalized patients with different pulmonary diseases share a common gut microbial dysbiosis pattern (elevated Enterococcaceae and Lactobacillaceae, depleted Lachnospiraceae and Ruminococcaceae) compared to healthy controls, irrespective of the specific pulmonary diagnosis.* — **[Moderately Supported]**
  * **Evidence & Critique:** The global divergence between the 374 PCCM inpatients and 105 healthy controls is visible in PCoA (`ANOSIM R = 0.098, P = 0.001`; Fig. 1D) and taxon abundance profiles (Fig. 2A–E), whereas cross-disease comparison among the seven inpatient subgroups yields no significant beta-diversity separation (`ANOSIM R = -0.021, P = 0.858`; Fig. 1E). However, this comparison is heavily confounded by unadjusted baseline differences between inpatients and healthy controls in BMI ($21.37 \pm 3.55$ vs. $23.26 \pm 3.16\text{ kg/m}^2, P < 0.01$), smoking prevalence ($53.5\%$ vs. $28.6\%$) and pack-years ($42.8 \pm 30.8$ vs. $19.2 \pm 14.3, P < 0.01$; Table 1), recent pre-admission out-of-hospital medications (only $1\text{ month}$ antibiotic exclusion), and dietary changes associated with acute illness prior to admission.

* **Claim 2:** *Four enterotypes—including an exclusive Enterococcaceae enterotype in PCCM inpatients—were identified across the cohort.* — **[Methodologically Flawed]**
  * **Evidence & Critique:** The manuscript directly contradicts itself regarding the number of enterotypes discovered. The Abstract (`Results`, line 21) states: *"Four enterotypes, including the exclusive Enterococcaceae enterotype in inpatients, were identified."* The Discussion (line 201) repeats: *"In the analysis of enterotypes, four enterotypes were identified."* Yet the Results section (`Gut microbial enterotypes in patients with pulmonary diseases`, line 146) and Figure 3C (`line 144`) explicitly state: *"The study identified three distinct enterotypes within the gut microbiota, characterized by the predominance of Lachnospiraceae (Enterotype 1), Enterobacteriaceae (Enterotype 2) and Enterococcaceae (Enterotype 3) (Fig. 3C)."* Furthermore, Methods (`Determination of enterotypes`, line 72) states that cluster count was selected using the Calinski-Harabasz (CH) index, yet no CH index curve across $k = 2 \dots 10$ or silhouette validation is shown to justify either $k = 3$ or $k = 4$.

* **Claim 3:** *Clinical indicators including days in hospital, medical costs, antibiotic dependency, and systemic inflammation (neutrophils, CRP, PCT, D-dimer) significantly explain gut microbial community variation at admission.* — **[Overstated]**
  * **Evidence & Critique:** According to Methods (`Participant recruitment`, line 64), *"On the first day of hospital admission, fresh fecal samples were collected before any examinations or treatments began."* Yet in the db-RDA ordination (`Key clinical indicators associated with the gut microbiota in inpatients`, line 170; Fig. 5B), the authors model total `days in hospital` ($8.5 \pm 5.3$ days) and total `medical costs` ($24,637.6 \pm 23,546.5$ RMB) as clinical covariates explaining the Day-1 baseline microbiome. Subsequent length of stay and cumulative hospital billing occur *after* Day-1 stool sampling and after in-hospital antibiotic administration ($43.3\%$ antibiotic use; Table 1). Treating downstream hospital outcomes as explanatory environmental arrows in db-RDA conflates baseline disease acuity with post-sampling hospital course. Moreover, the manuscript reports no multiple-testing correction (e.g., Benjamini-Hochberg FDR) for the `envfit` permutation tests across the 20 clinical indicators or the dense Spearman correlation matrix in Figure 5C.

* **Claim 4:** *A Random Forest model using 15 microbial genera distinguishes PCCM inpatients from healthy controls with an AUC of 0.75.* — **[Fragile]**
  * **Evidence & Critique:** Neither the Methods (`Statistical analysis`, line 76) nor the Results (`line 175`, Fig. 6A–B) specify whether the Random Forest classifier (`AUC = 0.75`, which is modest given the strong univariate depletion of `Faecalibacterium` and `Roseburia` shown in Fig. 2E) was evaluated on a held-out test split, via $k$-fold cross-validation, or via out-of-bag (OOB) predictions, nor whether feature selection of the 15 genera was performed inside or outside a cross-validation loop.

---

## 3. Technical & Methodological Critique

### Major Flaws

1. **Internal Contradiction on Enterotype Count (3 vs. 4 Enterotypes):**
   * As detailed under Claim 2, the Abstract (line 21) and Discussion (line 201) state that four enterotypes were identified, whereas the Results (line 146) and Figure 3C–E present three enterotypes (`Enterotype 1: Lachnospiraceae`, `Enterotype 2: Enterobacteriaceae`, `Enterotype 3: Enterococcaceae`). This discrepancy indicates that text from an earlier analysis ($k=4$) was left unedited in the Abstract and Discussion.

2. **Table 1 Arithmetic Error in Gender Percentage:**
   * In Table 1 (`Baseline characteristics of the study cohort`, line 98), under `All patients (n = 374)`, the row `Gender, M, n (%)` reports `252 (69.6)`. However, $252 / 374 = 67.38\%$, not $69.6\%$ (conversely, summing the male counts across the seven disease columns yields $56 + 15 + 77 + 50 + 13 + 7 + 34 = 252$, confirming $n = 252$ is the sum of the columns and the percentage `69.6%` is mathematically incorrect). In addition, Table 1 reports heavily skewed variables (such as `Smoking Index`, `Neutrophils/Lymphocytes`, `PCT`, `CRP`, `D-dimer`, `Total IgE`, and `Total costs`) as `mean ± SD` where the standard deviation exceeds the mean by up to 3.5-fold (e.g., `PCT`: $0.36 \pm 1.27\text{ ng/ml}$; `Total IgE`: $234.49 \pm 498.54\text{ IU/ml}$), implying massive positive skewness while using one-way ANOVA for $P$-values.

3. **Unfulfilled Covariate Adjustment Claim and Unadjusted Confounding:**
   * Methods (`Statistical analysis`, line 76) states: *"Baseline characteristics of the participants were evaluated using the Wilcoxon rank-sum test, Kruskal-Wallis test, and one-way ANOVA. Based on these results, analyses were further adjusted for age and smoking history."* However, every microbiome comparison reported in the Results and Figure legends—Figure 1B–C (`Wilcoxon rank-sum test` and `Kruskal-Wallis test` for Shannon/Chao1), Figure 1D–E (`ANOSIM`), Figure 2C, E (`Wilcoxon rank-sum test` and `Kruskal-Wallis test` for phyla/families/genera)—is a univariate non-parametric test that cannot incorporate covariate adjustments for age, smoking history, or BMI. No multivariable linear models (`MaAsLin2`, `ANCOM-BC`, or multivariable `PERMANOVA`/`adonis2` controlling for `BMI + Age + Smoking + Hospital_Center`) are presented anywhere in the paper.

4. **Outdated Bioinformatic Pipeline and Inconsistent Taxonomic Nomenclature:**
   * Sequence processing (`Bioinformatic analysis`, line 68) relies on `QIIME v1.9.1`, `USEARCH v7.0` 97% OTU clustering, and `GreenGenes v13.8` (last updated in 2013), rather than exact amplicon sequence variants (`DADA2`/ASVs) and modern taxonomy databases (`SILVA v138` or `GTDB`). Interestingly, the text mixes legacy GreenGenes phylum names (`Firmicutes`, `Bacteroidetes`, `Proteobacteria`, `Actinobacteria`) with the post-2021 validly published phylum name `Verrucomicrobiota` (lines 20, 128, 199), which does not exist in GreenGenes v13.8 (`Verrucomicrobia`).

---

## 4. Constructive Recommendations

1. **Reconcile the Enterotype Analysis:** Correct the contradiction between the Abstract/Discussion ("four enterotypes") and Results/Figure 3C ("three distinct enterotypes"), and provide the Calinski-Harabasz index and silhouette width values across $k = 2 \dots 10$ clusters.
2. **Perform Multivariable Adjustment for Confounders:** Replace univariate Wilcoxon and ANOSIM tests with multivariable `PERMANOVA` (`adonis2` marginal tests) and compositional differential abundance models (`MaAsLin2` or `ANCOM-BC2`) explicitly adjusting for `Age`, `Sex`, `BMI`, `Smoking status/pack-years`, and `Recruitment hospital`.
3. **Separate Baseline Clinical Covariates from Downstream Hospital Outcomes:** Remove prospective post-sampling outcomes (`Days in hospital` and `Total costs`) from the baseline db-RDA explanatory matrix, and instead test whether baseline microbiome composition (or Enterotype 3 status) predicts subsequent length of stay in a multivariable regression controlling for baseline disease severity and age.
4. **Clarify Random Forest Validation and Apply FDR Correction:** Specify the cross-validation or train/test splitting protocol used to compute `AUC = 0.75` in Figure 6, report its 95% confidence interval, and apply Benjamini-Hochberg false discovery rate (FDR) correction to all taxon-level comparisons, `envfit` vectors, and Spearman correlations.
5. **Fix Table 1 Arithmetic:** Correct `252 (69.6)` to `252 (67.4)` in Table 1 and report median (IQR) alongside non-parametric tests for highly skewed laboratory biomarkers.
