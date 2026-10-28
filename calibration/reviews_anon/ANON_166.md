# Review of ANON_166

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **3.8 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.0/3.5 | Claims: 1.0/2.5 | Biology: 1.0/2.0 | Reproducibility: 0.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates shared transcriptional biomarkers for sepsis and sepsis-induced acute respiratory distress syndrome (ARDS) by integrating bulk blood/PBMC transcriptomic datasets from GEO and ArrayExpress with single-cell RNA-seq (GSE167363 and GSE151263), WGCNA, and three feature-selection algorithms (LASSO, Random Forest, and Boruta). The authors converge on three downregulated genes (`CX3CR1`, `PID1`, and `PTGDS`), construct diagnostic nomograms and a 3-gene Cox prognostic signature for 28-day mortality, perform CIBERSORT immune deconvolution, build ceRNA/TF/PPI networks, screen candidate small molecules via CMap/Enrichr followed by MOE molecular docking, and conduct RT-qPCR and histological/ELISA assays in human PBMCs (16 sepsis, 15 ARDS, 12 controls) and mouse cecal ligation and puncture (CLP) and intratracheal LPS models.

While the clinical question—identifying which septic patients will progress to ARDS or die—is relevant, the study's bioinformatics pipeline, validation design, and mechanistic claims suffer from severe methodological and data-integrity flaws. First, the ARDS validation cohorts (E-MTAB-5273 and E-MTAB-5274) compare *healthy controls* against *sepsis+ARDS patients*, whereas the ARDS discovery cohorts (GSE32707 and GSE10474) compare *sepsis alone* against *sepsis+ARDS*; consequently, the high validation AUCs merely reflect general sepsis-associated gene downregulation rather than ARDS-specific discrimination. Second, dataset GSE95233 is used both for discovery (DEG screening and WGCNA mortality correlation) and as an "external validation" cohort for survival prediction, constituting direct data leakage. Third, the manuscript contains multiple numerical and provenance contradictions—including impossible DEG counts ($3621 + 3641 = 6038$), duplicated GSM sample accessions across two unrelated scRNA-seq studies, and molecular docking claims where small molecules are docked to downregulated protective proteins (including docking energy values that fail the authors' own threshold). Major computational re-analysis and removal of unsupported docking/mechanistic claims are required.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **`CX3CR1`, `PID1`, and `PTGDS` are shared diagnostic biomarkers that accurately distinguish both sepsis and ARDS across external validation cohorts: [Methodologically Flawed].**  
  In Table 1, the ARDS discovery cohorts (GSE32707, GSE10474) compare *sepsis patients* against *sepsis+ARDS patients*, whereas the ARDS validation cohorts (E-MTAB-5273, $n=10$ healthy vs. $n=127$ sepsis+ARDS; E-MTAB-5274, $n=10$ healthy vs. $n=42$ sepsis+ARDS) compare *healthy individuals* against *sepsis+ARDS patients*. Because `CX3CR1`, `PID1`, and `PTGDS` are strongly downregulated in sepsis relative to healthy controls, evaluating the 3-gene model on healthy vs. sepsis+ARDS in E-MTAB-5273/5274 (yielding an AUC up to 1.0, Discussion line 96) tests sepsis vs. healthy status rather than whether the signature distinguishes ARDS from uncomplicated sepsis. Furthermore, initial DEG screening (Sections 2.1–2.2) used unadjusted $P < 0.05$ without multiple-testing correction and an arbitrary fold-change threshold ($|\text{FC}| > 0.3$).

* **The 3-gene Cox regression signature externally validates 28-day mortality prediction in GSE95233 and ARDS prognosis in E-MTAB-5274: [Methodologically Flawed].**  
  GSE95233 was used during feature discovery to identify common DEGs (Fig. 2B, D), to select the WGCNA turquoise module correlated with sepsis mortality (`outcome`, Fig. 3B), and to screen survival-associated gene expression (Fig. 5A–C). Presenting GSE95233 in Section 3.7 (Fig. 5I, $\text{AUC} = 0.856$) as an "external validation" dataset introduces circularity and data leakage. In addition, single-gene Kaplan–Meier curves (Section 2.7) dichotomized patients using the "best threshold value" (optimal cutpoint selection) without correcting $p$-values for multiple cutpoint testing.

* **Single-cell RNA-seq analysis of GSE167363 and GSE151263 defines cell-type-specific expression and NK/T-cell depletion in sepsis-induced ARDS: [Fragile].**  
  In Section 2.14, the sample provenance for GSE151263 is corrupted: the text lists `GSM5511352 (SA1, PBMCs from non-survivors)` and `GSM5511354 (S1, PBMCs from patients with sepsis and ARDS)` as belonging to GSE151263, even though `GSM5511352` and `GSM5511354` are samples from GSE167363 (gram-negative sepsis without ARDS annotation, listed one paragraph earlier as `NS2` and `S1`). Moreover, Table 1 states that GSE151263 contains only 4 samples ($n=2$ sepsis, $n=2$ sepsis+ARDS), contradicting the 6 samples described in Section 2.14. Even if the correct 2 vs. 2 samples were analyzed, $n=2$ per group is insufficient to support claims of "significantly fewer NK cells and T cells" across patient groups.

* **Withaferin A, SB216763, Epothilone B, and Dichloroacetic Acid act by directly binding PTGDS, PID1, and CX3CR1 target proteins: [Overstated].**  
  First, `CX3CR1`, `PID1`, and `PTGDS` are *downregulated* in sepsis and ARDS, and higher levels are protective (as confirmed by the authors' finding that the CX3CR1 inhibitor AZD8797 exacerbates lung injury and IL-6 in mice, Figs. 10E, 11D). Blind molecular docking in MOE only estimates static steric/electrostatic complementarity and typically models competitive inhibition, not transcriptional upregulation or receptor agonism. Second, the reported docking energy for dichloroacetic acid (a 129 Da metabolic pyruvate dehydrogenase kinase inhibitor) to the GPCR CX3CR1 is $-3.9131\text{ kcal/mol}$ (Section 3.11), which fails the authors' own stated threshold in the next sentence (*"Docking energy values below -4.25 kcal/mol suggest some binding activity"*). While the four compounds reduce general LPS/CLP inflammation in mice (n=3 per group for histology/ELISA), this reflects their known pleiotropic anti-inflammatory/metabolic effects (e.g., NF-$\kappa$B, GSK3$\beta$, microtubule, and PDK inhibition) rather than specific target engagement with PTGDS, PID1, or CX3CR1.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Eliminate Data Leakage and Match Case-Control Phenotypes in External Validation
* **WHY:** Validating an ARDS classifier on Healthy vs. Sepsis+ARDS cohorts (E-MTAB-5273/5274) conflates sepsis diagnosis with ARDS diagnosis, and testing the survival model on GSE95233 after using GSE95233 mortality labels in WGCNA module selection inflates predictive performance.
* **WHAT:** (1) Remove GSE95233 from the external survival validation set or re-run DEG and WGCNA discovery strictly within GSE65682; (2) evaluate ARDS diagnostic discrimination strictly between *Sepsis alone* and *Sepsis+ARDS* (e.g., using GSE32707 as training and GSE10474 as an independent Sepsis vs. Sepsis+ARDS test cohort, or vice versa).
* **HOW:** Re-compute the 3-gene logistic regression/nomogram weights on GSE32707 (58 sepsis vs. 31 sepsis+ARDS) and report the out-of-sample ROC AUC, calibration curve, and decision curve on GSE10474 (21 sepsis vs. 13 sepsis+ARDS). Apply Benjamini–Hochberg FDR correction ($\text{FDR} < 0.05$) during limma DEG screening.

#### 2. Audit and Correct Single-Cell RNA-seq Sample Accessions and Group Sizes
* **WHY:** Section 2.14 lists `GSM5511352` and `GSM5511354` under both GSE167363 and GSE151263 with contradictory clinical phenotypes, and Table 1 conflicts with Section 2.14 on the sample size of GSE151263 (4 vs. 6 samples).
* **WHAT:** Verify which exact GSM files were loaded into Seurat for Figure 9E–H, remove any accidentally merged GSE167363 samples from the GSE151263 analysis, and reconcile Table 1 with Section 2.14.
* **HOW:** Inspect the Seurat metadata table (`object@meta.data$orig.ident`) for the ARDS scRNA-seq analysis, re-generate Figure 9E–H using only authentic GSE151263 samples, and refrain from claiming statistically significant cell-proportion differences when group sizes are $n=2$ patients.

#### 3. Reframe CMap Drug Screening and Remove Unsupported Direct-Binding Claims
* **WHY:** Docking small molecules to proteins whose mRNA is *downregulated* in disease does not explain how those compounds restore expression or protective signaling, and dichloroacetic acid ($-3.91\text{ kcal/mol}$) does not meet the minimum binding threshold ($-4.25\text{ kcal/mol}$).
* **WHAT:** Present the CMap compounds (Withaferin A, SB216763, Epothilone B, Dichloroacetic acid) strictly as transcriptome-reversal/anti-inflammatory candidates rather than direct ligands of PTGDS, PID1, and CX3CR1, and remove the DCA–CX3CR1 docking claim.
* **HOW:** Revise Sections 3.11, 3.13, and the Discussion (page 9) to state that CMap identifies compounds predicted to reverse the global sepsis/ARDS transcriptional signature, whereas only recombinant PTGDS protein and the selective CX3CR1 antagonist AZD8797 directly perturb the hub gene targets in vivo.

#### 4. Provide Complete Clinical Baseline Data for Healthy Controls and Increase Animal Sample Reporting Transparency
* **WHY:** Figure 11I reports RT-qPCR data for 12 healthy controls (`n=12`), but Section 2.16 and Table 2 only describe 16 sepsis and 15 ARDS patients with no mention of how healthy controls were recruited or whether they were age- and sex-matched to the ~70-year-old ICU cohorts.
* **WHAT:** Add a "Healthy Controls ($n=12$)" column to Table 2 (reporting age, sex, and inclusion criteria) and reconcile the "Focus of infection" rows in Table 2 where the sepsis counts sum to 19 ($14 + 3 + 2$) across 16 patients.
* **HOW:** Update Table 2 and Section 2.16 with the demographic data of the 12 healthy volunteers and clarify whether patients with multiple infection sites account for the sum exceeding $n=16$.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Multiple arithmetic errors and duplicated phrases appear in the manuscript.
* **WHAT & HOW:**
  1. **Section 3.2 (page 5, line 239):** Fix the impossible arithmetic in *"An overall number of 6038 DEGs were discovered in the sepsis dataset GSE65682. Of these DEGs, 3621 were up-regulated, whereas 3641 were down-regulated."* ($3621 + 3641 = 7262$, which appears to have been copied from the next sentence's 7260 DEGs in GSE95233: $3620 + 3640 = 7260$). Report the true upregulated and downregulated counts that sum to 6038.
  2. **Section 2.1 (page 2, line 49) vs. Table 1:** Correct *"We have retrospectively enrolled 11 datasets"* to **14 datasets** to match the 14 accession rows in Table 1.
  3. **Section 1 (page 1, line 35):** Remove the duplicate phrase *"low blood oxygen levels"* in *"sudden development of low blood oxygen levels, noncardiogenic pulmonary edema, low blood oxygen levels"*.
  4. **Section 2.16 (page 4, line 165):** Remove the duplicated clause *"Our study was approved by the Research Ethics Committee of Our study was approved by the Research Ethics Committee of Shanghai Lung Hospital"*.
  5. **Section 2.17 (page 4, line 214):** Fix the garbled sentence *"lung samples and peripheral blood were gathered for subsequent examination was collected from mice"*.
