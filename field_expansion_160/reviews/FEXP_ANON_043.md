# Forensic Review of FEXP_ANON_043

**Manuscript ID:** `FEXP_ANON_043`  
**Overall Score:** **2.5 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.6 / 8.0**  
* **Score Breakdown:** Rigor: 0.5/3.5 | Claims: 0.5/2.5 | Biology: 0.6/2.0 | Reproducibility: 0.9/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Subfield:** Cancer Bioinformatics & Tumor Microbiome Prognostic Modeling (Endometrial Carcinoma / TCGA Re-analysis).
* **Study Design:** Retrospective bioinformatic analysis of 502 TCGA endometrial carcinoma (EC) patients combining cBioPortal microbial genus abundance tables (1,406 genera) with TCGA RNA-seq, somatic mutation (TMB/MSI), TCIA immunophenoscore (IPS), and imputed drug IC50 profiles.
* **Primary Methods:** Univariate ($p < 0.01$) and multivariate ($p < 0.05$) Cox proportional hazards regression on 1,406 genera, median-split Kaplan-Meier log-rank tests, time-dependent ROC curves, `immunedeconv` (xCell) and ssGSEA immune deconvolution, DESeq2 TF–IRG correlation networks, `maftools` TMB/MSI comparisons, and `pRRophetic`/`oncopredict` chemotherapy IC50 imputation.

---

## 2. Executive Summary & Editorial Verdict

This study downloads the 1,406-genus TCGA endometrial carcinoma (EC, $N = 502$) microbial abundance matrix from cBioPortal and runs univariate followed by multivariate Cox regression against overall survival (OS) to construct a 9-genus "Resident Microbiome of Endometrium" (RME) prognostic risk score. Stratifying the 502 patients at the median RME score, the authors report 1-, 3-, and 5-year ROC AUCs of 0.741, 0.709, and 0.694, and correlate low RME scores with higher T/NK cell infiltration, higher microsatellite instability (MSI), higher TCIA immunophenoscores, and differential imputed chemotherapy IC50s (including stratifying patients by *Roseiflexus* abundance for Foretinib and Dabrafenib sensitivity).

**Editorial Verdict: Reject (Fundamentally Invalid).** The manuscript's "Resident Microbiome of Endometrium" (RME) signature is a bioinformatic artifact built on environmentally impossible bacterial taxa and unvalidated statistical overfitting: (1) 8 of the 9 genera comprising the RME score (*Zooshikella*, *Caldimonas*, *Candidatus Accumulibacter*, *Nonlabens*, *Roseiflexus*, *Streptosporangium*, *Zavarzinella*, and *Derxia*) are marine tidal-flat mud bacteria, $55^\circ\text{C}$ hot-spring thermophiles, municipal sewage sludge bacteria, and Siberian peat-bog microbes that do not inhabit the human endometrium, arising from well-documented Kraken k-mer false positives and sequencing-center batch artifacts in the cBioPortal/TCGA pan-cancer microbiome dataset; (2) the 1,406 genera were screened by unadjusted univariate Cox regression ($p < 0.01$) and entered into a multivariate Cox model on the entire 502-patient cohort without any train/test split, cross-validation, or external validation, evaluating ROC AUCs on the exact same data used for feature discovery and coefficient fitting; and (3) the RME score is strongly confounded by established TCGA-UCEC molecular subtypes (MSI-high/POLE endometrioid vs. copy-number-high serous tumors, Fig. 4B–C), which were omitted from the multivariate clinical Cox model.

### Specific Conclusions and Assessment of Support

* **Nine bacterial genera (*Zooshikella*, *Caldimonas*, *Candidatus Accumulibacter*, *Nonlabens*, *Roseiflexus*, *Streptosporangium*, *Zavarzinella*, *Derxia*, and *Shigella*) constitute a biologically meaningful "Resident Microbiome of Endometrium" (RME) that independently predicts EC survival: [Methodologically Flawed].**  
  First, the taxonomy of the 9 selected genera is biologically implausible for the human uterus: *Roseiflexus* is an obligate thermophilic filamentous photosynthetic bacterium restricted to geothermal hot springs; *Caldimonas* is a hot-spring thermophile; *Zooshikella* and *Nonlabens* are marine sediment/seawater bacteria; *Candidatus Accumulibacter* is an uncultured wastewater activated-sludge bacterium; and *Zavarzinella*, *Streptosporangium*, and *Derxia* are peat-bog and soil bacteria. These counts represent human sequence misalignment and reagent/batch artifacts in the cBioPortal Kraken pipeline (see Gihawi et al. 2023, *mBio*). Second, screening 1,406 features at unadjusted $p < 0.01$ (finding 130 hits) and fitting a multivariate Cox model on the same $N = 502$ dataset without cross-validation or an independent test set severely inflates apparent prognostic discrimination (1-year $\text{AUC} = 0.741$).
* **The RME score is an independent prognostic indicator after adjusting for clinical covariates: [Methodologically Flawed].**  
  The multivariate Cox model and nomogram (Fig. 2A,B,E) adjust only for patient age and clinical stage, omitting the most important prognostic drivers in endometrial cancer: histological subtype (endometrioid vs. serous/clear-cell), tumor grade, and TCGA molecular subtype (*POLE*, MSI-hypermutated, copy-number-low, copy-number-high/*TP53*-mutant).
* **Low RME scores reflect "hot" tumors with higher T/NK cell infiltration, higher MSI, and superior immunotherapy sensitivity: [Overstated].**  
  Figure 4B–C demonstrates that low RME scores correlate with high MSI status and higher somatic mutation burden. Because TCGA MSI-high endometrioid carcinomas are well known to harbor dense Neoantigen-driven T/NK cell infiltrates and favorable survival compared to MSS serous carcinomas—and were processed in distinct TCGA sequencing batches—the RME score is acting as a confounded surrogate for MSI/histological subtype rather than demonstrating a causal microbial effect on the tumor immune microenvironment.
* **The RME score and *Roseiflexus* abundance predict patient sensitivity to AZD1332, WEHI-539, Foretinib, and Dabrafenib: [Methodologically Flawed].**  
  `pRRophetic`/`oncopredict` imputes cell-line drug IC50s solely as a linear ridge-regression projection of bulk tumor host gene expression (which already differs between MSI-high and MSS tumors). Stratifying endometrial cancer patients by the abundance of a boiling hot-spring photosynthetic bacterium (*Roseiflexus*, Fig. 5E–F) to recommend targeted BRAF/MET inhibitors is biologically and clinically baseless.

---

## 3. Forensic Defect Inventory

### 1. Biologically Implausible Environmental/Thermophilic Taxa from Contaminated cBioPortal Kraken Tables (Pillars 2 & 6)
* **WHY:** The cBioPortal TCGA microbiome matrix was generated by mapping unaligned TCGA sequencing reads against a microbial database containing human genome contamination and draft environmental assemblies, followed by batch normalization that imprinted hospital/sequencing-center signals across all taxa. In Section "Microbiome signatures were associated with EC prognosis" (line 59), 8 of the 9 genera selected for the RME score (*Roseiflexus*, *Caldimonas*, *Zooshikella*, *Nonlabens*, *Candidatus Accumulibacter*, *Zavarzinella*, *Streptosporangium*, *Derxia*) are extremophiles, marine sediment bacteria, or sewage-sludge organisms that cannot colonize human endometrial tissue.
* **WHAT:** Audit the 1,406 genera against human-associated vaginal/uterine microbial reference catalogs and remove non-human environmental extremophiles, marine bacteria, and false-positive human-read k-mer matches.
* **HOW:** Restrict candidate genera to validated human-associated urogenital/mucosal taxa confirmed after rigorous human read depletion (GRCh38 + T2T-CHM13) and sequencing-center (`center_id` / `plate_id`) batch removal.

### 2. Data Leakage and Overfitting from Screening 1,406 Genera and Evaluating ROC on the Full Training Cohort (Pillars 3, 4 & 5)
* **WHY:** In Section "Construction of microbial abundance prognostic scoring model" (lines 31, 59), all 502 TCGA-UCEC patients were used to screen 1,406 genera by univariate Cox regression ($p < 0.01$ without FDR correction), fit a multivariate Cox model on the 130 passing genera, and then compute Kaplan-Meier log-rank $p$-values and 1-, 3-, and 5-year ROC AUCs on the *exact same 502 patients*. Evaluating a multi-step feature-selected model on its own discovery set without an independent test set or nested cross-validation guarantees optimistic bias.
* **WHAT:** Implement nested cross-validation or a strict train/test split and apply Benjamini-Hochberg FDR correction during univariate screening.
* **HOW:** Split the cohort into a training set (e.g., 70%) and held-out test set (30%) stratified by TCGA sequencing center and event status, perform univariate FDR screening and LASSO-Cox penalized selection strictly within the training set, and report out-of-sample C-index and time-dependent AUCs with 95% bootstrap confidence intervals on the held-out test set.

### 3. Omission of Essential Endometrial Cancer Confounders (MSI, Histologic Subtype, Grade, and TCGA Batch) (Pillars 3 & 5)
* **WHY:** Figure 4B–C shows a significant correlation between the RME score and Microsatellite Instability (MSI). In TCGA-UCEC, MSI status, histological type (serous vs. endometrioid), histological grade, and TCGA tissue source site / sequencing center strongly affect both survival and immune infiltration (xCell/ssGSEA). Because Figure 2B only adjusts for age and clinical stage, the apparent prognostic and immunological associations of the RME score are confounded by unmodeled molecular subtypes and technical batch effects.
* **WHAT:** Include histological subtype, grade, MSI/POLE molecular classification, and TCGA sequencing center in the multivariate Cox regression model.
* **HOW:** Fit `coxph(Surv(OS_time, OS_status) ~ RME_score + Age + Stage + Grade + Histologic_Type + MSI_status + strata(Sequencing_Center))` and report whether the RME score retains any independent prognostic value ($p < 0.05$).

### 4. Internal Discrepancy in Drug Prediction Software (`pRRophetic` vs. `oncopredict`) (Pillar 7)
* **WHY:** Materials and Methods (line 46) states that the `"pRRophetic"` R package was used to predict chemotherapeutic IC50 values, whereas Results (line 91) states that the `"oncopredict"` package was used.
* **WHAT & HOW:** Reconcile lines 46 and 91 to specify the exact package version and training pharmacogenomic database (GDSC1/GDSC2 or CTRPv2) actually executed.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.5** | **3.5** | Severe overfitting and circularity: 1,406 genera screened at unadjusted $p < 0.01$ and entered into multivariate Cox regression on $N=502$ with zero train/test splitting or cross-validation; multivariate Cox model omits histological subtype, grade, MSI status, and TCGA sequencing batch. |
| **2. Claim-to-Evidence Alignment** | **0.5** | **2.5** | Claims that 9 genera represent a functional "Resident Microbiome of Endometrium" driving immune infiltration and guiding personalized Foretinib/Dabrafenib therapy (via *Roseiflexus* stratification) are invalid artifacts of contaminated k-mer tables and unadjusted MSI confounding. |
| **3. Data Integrity & Biological Plausibility** | **0.6** | **2.0** | 8 of the 9 "endometrial resident" genera (*Roseiflexus*, *Caldimonas*, *Zooshikella*, *Nonlabens*, *Candidatus Accumulibacter*, *Zavarzinella*, *Streptosporangium*, *Derxia*) are boiling hot-spring thermophiles, marine mud bacteria, and sewage-sludge microbes that cannot inhabit human uterine tissue. |
| **4. Reproducibility & Data Integrity** | **0.9** | **2.0** | Underlying TCGA and cBioPortal datasets are public and Supplementary Tables S1–S2 are included, but no analysis code or 9-genus Cox coefficient formula is provided in the text, and Methods (line 46, `pRRophetic`) contradicts Results (line 91, `oncopredict`). |
| **Scientific Core Score** | **1.6** | **8.0** | Sum of Rigor + Claims + Biology (`0.5 + 0.5 + 0.6`). |
| **Total Composite Score** | **2.5** | **10.0** | **Fundamentally Invalid** (`0.5 + 0.5 + 0.6 + 0.9`). |
