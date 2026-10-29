# Forensic Review of `FEXP_ANON_098`

**Overall Score:** **3.2 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.5 / 8.0**
* **Score Breakdown:** Rigor: 0.8/3.5 | Claims: 0.7/2.5 | Biology: 1.0/2.0 | Reproducibility: 0.7/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Field & Subfield:** Cancer Bioinformatics & Experimental Oncology (Single-cell and bulk transcriptomic machine-learning prognostic modeling of SUMOylation-related genes in stomach adenocarcinoma, paired with in vitro cell line assays).
* **Study Design Archetype:** Multi-cohort bioinformatic pipeline (`GSE167297` scRNA-seq from TISCH, `TCGA-STAD` and `GSE62254` bulk transcriptomics) running `ComBat`, `ConsensusClusterPlus`, 69-combination machine-learning survival benchmark (selecting Random Survival Forest), `IOBR` immune deconvolution, `TIDE`, and `pRRophetic`, supplemented by shRNA knockdown of `L3MBTL2` and `VHL` in AGS cells (Western blot, CCK-8, scratch, and Transwell assays).
* **Temporal & Venue Signals:** Recent (2023–2025) "10-algorithm / 69-combination ML signature + basic wet-lab validation" template paper.

---

## 2. Executive Summary & Editorial Verdict

This study investigates 200 SUMOylation-related genes (SRGs) in stomach adenocarcinoma (STAD) across a public scRNA-seq dataset (`GSE167297`, 22,464 cells) and two bulk transcriptomic cohorts (`TCGA-STAD`, $n=375$; `GSE62254`, $n=300$). The authors identify 42 prognosis-associated SRGs via univariate Cox regression, define two consensus clusters (Subtypes A and B), benchmark 69 machine-learning models across 10 algorithms to construct a Random Survival Forest (RSF)-based SUMOylation Risk Score (SRS), and perform in vitro shRNA knockdown of `L3MBTL2` and `VHL` in AGS gastric cancer cells.

**Editorial Verdict: Reject (Flawed / Overstated).** The headline machine-learning claim—that the RSF-based SRS model achieves an `AUC = 0.97` (1-year AUC = 0.974, 3-year AUC = 0.963)—is an artifact of two textbook methodological errors: (1) **pre-split training–validation leakage**, where `TCGA-STAD` (training) and `GSE62254` (validation) were merged and batch-corrected with `ComBat`, and the 42 candidate prognostic SRGs were selected via univariate Cox regression ($p < 0.001$) on the *merged* cohort before splitting into training and validation sets; and (2) **in-sample overfitting of Random Survival Forest (RSF)**, where non-parametric tree ensembles evaluated on their own training data routinely yield near-1.0 AUCs (~0.97) while external validation AUCs are omitted from the main text. Moreover, the Methods section erroneously states that the RSF risk score is computed as a linear dot product ($\sum \text{coefficient} \times \text{expression}$), which is mathematically invalid for survival forest ensembles. While the in vitro AGS knockdown assays for `L3MBTL2` and `VHL` provide preliminary functional data, they rely on a single cell line, lack shRNA target sequences, conflate transient shRNA knockdown with gene "knockout," and do not test SUMOylation mechanisms.

### Assessment of Specific Claims

* **The RSF-based SUMOylation Risk Score (SRS) achieves high predictive accuracy with AUC = 0.97 (Abstract, line 9; Highlights, line 18; Results, line 176): `[Methodologically Flawed]`**  
  First, the 42 SRGs input into the 69 ML models were pre-selected by running univariate Cox regression ($p < 0.001$) on the *merged* `TCGA-STAD + GSE62254` dataset (Methods, line 58; Results, line 151), leaking survival information from the `GSE62254` validation cohort directly into feature selection. Second, the reported AUCs of 0.974 (1-year) and 0.963 (3-year) are in-sample training set evaluations of a Random Survival Forest (`RSF`) model on `TCGA-STAD` (Fig. 7E); non-parametric random forests memorize training outcomes when evaluated in-sample without out-of-bag (OOB) cross-prediction, and the authors fail to report the numerical AUCs for the validation cohort (`GSE62254`) anywhere in the text.
* **High-risk SRS patients exhibit reduced overall immune infiltration alongside elevated ESTIMATE immune scores (Results, line 204; Fig. 10A): `[Methodologically Flawed]`**  
  In Results (line 204), the authors state that *"ESTIMATE results showed reduced tumor purity but elevated immune and stromal scores in the high-risk group"*, and in the very next sentence claim that *"the overall level of immune cell infiltration was lower than that in the low-risk group"*, which Fig. 10B caption repeats (*"High-score groups exhibit low immune infiltration"*). An elevated ESTIMATE Immune Score by definition indicates *higher* bulk immune infiltration; the authors directly contradict their own deconvolution output to force alignment with an "immune-excluded" narrative.
* **Knockdown of L3MBTL2 and VHL promotes proliferation, migration, and invasion in AGS cells (Abstract, line 9; Results, line 220; Fig. 12): `[Moderately Supported]`**  
  Western blots, CCK-8, wound-healing, and Transwell assays in AGS cells show increased proliferation and motility following shRNA depletion of `L3MBTL2` or `VHL`. However, experiments are restricted to a single cell line (`AGS`), appear to use only one shRNA construct per gene without rescue or a second independent hairpin to exclude off-target effects, omit all shRNA target sequences, and do not assay SUMOylation status.
* **High SUMOylation activity in STAD specifically depletes B cells and activates proliferative pathways in epithelial cells (Results, lines 134–146; Figs. 2–3): `[Fragile]`**  
  Categorizing all single cells across 9 lineage types (epithelial, endothelial, fibroblasts, T cells, B cells, myeloid cells) into "high" and "low" SUMOylation groups based on a global median GSVA score (line 134) confounds intrinsic cell-lineage transcriptional baseline differences (highly proliferative malignant epithelial cells naturally express higher cell-cycle/DNA-repair SRGs such as `PCNA`, `BRCA1`, `INCENP`, and `SMC1A` than quiescent B cells) with intra-lineage SUMOylation regulation.

---

## 3. Forensic Defect Inventory

### 3.1. Pre-Split Feature Selection & Batch-Correction Data Leakage (Pillar 2 & Pillar 3)
* **Location:** Methods ("Data collection and integration", line 41; "Identification of SRGs in STAD", line 58; "Machine learning-based risk signature construction", line 68) and Results (lines 151, 176).
* **Defect:** The authors merged `TCGA-STAD` ($n=375$) and `GSE62254` ($n=300$) and ran `ComBat` batch correction across the combined cohort (line 41). Next, *"From the merged dataset, 200 SRGs were analyzed... univariate Cox regression were conducted... identifying 42 genes significantly associated with prognosis (Cox p < 0.001)"* (line 58; repeated in line 151). Only *after* selecting these 42 prognostic genes on the combined dataset did the authors designate `TCGA-STAD` as the training set and `GSE62254` as the external validation set to fit the 69 ML models (lines 68, 176). Selecting survival-associated features using the validation cohort's outcomes invalidates `GSE62254` as an independent test set.

### 3.2. RSF In-Sample Overfitting & Mathematical Misrepresentation of the Risk Formula (Pillar 3 & Pillar 4)
* **Location:** Abstract (line 9), Highlights (line 18), Methods (line 68), and Results (line 176; Fig. 7D–E).
* **Defect 1 (RSF Overfitting):** In Figure 7A, the standalone Random Survival Forest (`RSF`) model is chosen because it has the highest average C-index (0.774), driven by a near-1.0 C-index on the `TCGA` training cohort and a substantially lower C-index on the validation cohort. The headline `AUC = 0.97` (0.974 at 1 year, 0.963 at 3 years) reported in the Abstract and Highlights is the unpenalized *in-sample training AUC* of the RSF tree ensemble.
* **Defect 2 (Invalid Linear Formula for RSF):** Methods (line 68) states: *"Risk score for each dataset was calculated via the following formula: risk score = $\Sigma$ (coefficient $\times$ expression) (34)."* A Random Survival Forest is a non-parametric ensemble of survival decision trees whose predicted risk is the ensemble cumulative hazard function (or mortality score); it has no linear regression coefficients $\beta_i$.

### 3.3. Numerical, Textual, and Reproducibility Defects (Pillar 7)
* **Sample Size Contradiction ($654$ vs. $675$):** Methods (line 41) states that merging `TCGA-STAD` (375 samples) and `GSE62254` (300 samples) produced *"a combined cohort of 654 STAD samples"*. However, Results (line 168) and Figure 6 caption (line 171) report that the merged cohort comprises *"Group A (450 samples) and Group B (225 samples)"*, which sums to $450 + 225 = 675$ samples.
* **Missing Formula in Methods:** Methods ("Wound healing scratch assay", line 109) ends mid-sentence with: *"the wound closure rate was calculated using the following formula:"*, with the equation completely omitted.
* **Somatic Mutation Reporting Errors:** Results (line 212) states: *"TTN, TP53, LRP18, MUC16, SYNE1 were identified as the top three genes with the highest mutation frequencies"*, listing five genes as "the top three" and misspelling `LRP1B` as `LRP18` (also writing `"MAFTOOL"` instead of `maftools`).
* **Wet-Lab Terminology & Reagent Omissions:** Methods (line 83) and Results (line 220) repeatedly refer to transient PEI-mediated shRNA plasmid transfection as *"gene knockout of L3MBTL2 and VHL"*, confusing post-transcriptional shRNA knockdown with genomic knockout. Crucially, the nucleotide target sequences of the shRNAs against `L3MBTL2` and `VHL` (and the scramble control) are never reported.
* **Code Availability:** No GitHub repository, code archive, or trained RSF model object is provided.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.8** | 3.5 | Pre-split feature selection (`Cox p < 0.001`) and `ComBat` normalization on the merged training + validation dataset; unacknowledged in-sample overfitting of RSF (`AUC = 0.974`); mathematically false claim that RSF scores are $\sum (\text{coefficient} \times \text{expression})$. |
| **2. Claim-to-Evidence Alignment** | **0.7** | 2.5 | Headline claim of `AUC = 0.97` in Abstract/Highlights reports overfitted in-sample RSF training performance while omitting validation AUC numbers; internal contradiction claiming high-risk tumors have both elevated ESTIMATE immune scores and lower overall immune infiltration. |
| **3. Data Integrity & Biological Plausibility** | **1.0** | 2.0 | Single-cell median GSVA split confounds cell-type identity (proliferating epithelium vs. B cells) with SUMOylation activity; in vitro AGS knockdown assays support a functional phenotype for `L3MBTL2` and `VHL` but lack shRNA sequences, second hairpins, and SUMOylation assays. |
| **4. Reproducibility & Data Integrity** | **0.7** | 2.0 | Merged sample size contradiction ($654$ vs. $450+225=675$); omitted wound-healing equation in line 109; listing 5 genes as "top three" (`LRP18` typo); missing shRNA sequences and analysis code. |
| **Total Composite Score** | **3.2** | **10.0** | **Flawed / Overstated** (**Scientific Core Score: 2.5 / 8.0**) |
