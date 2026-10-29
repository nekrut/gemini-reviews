# Review of FEXP_ANON_091

**Overall Score:** **3.7 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.9 / 8.0**  
* **Score Breakdown:** Rigor: 1.0/3.5 | Claims: 0.9/2.5 | Biology: 1.0/2.0 | Reproducibility: 0.8/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Role / Domain:** Translational oncology and bioinformatics study developing an "immune system development-related signature" (`ISDRS`) via 167 machine learning combinations in hepatocellular carcinoma (HCC) to predict prognosis and sorafenib resistance, supplemented by `Scissor` scRNA-seq analysis (`GSE149614`/`GSE109211`) and institutional qRT-PCR/IHC for `BATF` ($n = 64$ HCC, $n = 10$ sorafenib-treated).
* **Blinded Document Assessment:** A template "10 machine learning algorithms / 167 combinations + 73 published signatures" prognostic paper marred by validation-set model selection leakage, omitted risk score equation, unadjusted $P < 0.05$ screening, repeated self-contradictions regarding the direction of `IL-6`/`IL-6R` association with Tregs and `ISD`, and an underpowered $n = 10$ clinical sorafenib subgroup.

---

## 2. Executive Summary & Editorial Verdict

The authors retrieve 1,029 "immune system development-related genes" (`ISDGs`) from MSigDB, compute `ssGSEA` scores across `TCGA-LIHC` ($n = 374$ tumors), `ICGC-LIRI-JP` ($n = 240$), `GSE144269` ($n = 70$), and `GSE109211` ($n = 67$ sorafenib-treated HCCs), and cluster patients via NMF ($k = 2$). Intersecting unadjusted between-cluster DEGs (313 genes), tumor-vs.-normal DEGs (699 genes), and univariate Cox genes (301 genes) yields 98 candidate `ISDGs`. They then evaluate 167 combinations of 10 machine learning survival algorithms, select `RSF + stepwise Cox (direction = both)` to define a 7-gene signature (`ISDRS`: `ZMPSTE24`, `CTNNB1`, `IRF2BP2`, `BATF`, `TREM2`, `ALAS1`, `IL7R`), benchmark it against 73 published signatures, apply `Scissor` to map `GSE109211` sorafenib resistance onto `GSE149614` scRNA-seq (10 tumors, 16,709 cells) to identify `BATF`+ sorafenib-resistant Tregs, and assay `BATF` by qRT-PCR and IHC in an institutional cohort (`MCHH`, 64 HCCs, 26 paracancer tissues, including 10 sorafenib-treated patients).

**Editorial Verdict: Reject (Flawed / Overstated).** Despite combining multiple bulk datasets, single-cell `Scissor` mapping, and institutional IHC, the study's central statistical claims and mechanistic narrative are compromised by severe methodological flaws:
1. **Validation-Set Leakage in Selecting the Winning Model Out of 167 Pipelines:** Rather than selecting the final algorithm using cross-validation strictly within the `TCGA` training cohort and testing once on locked external cohorts, the authors selected `RSF + stepwise Cox` because it achieved *"the highest C-index in all validation cohorts with the mean C-index of 0.740"* (Methods line 55, Results line 116). Choosing the best of 167 models based on validation-cohort C-index directly overfits the validation sets and invalidates the subsequent post-hoc superiority claim against 73 published signatures (Figure 4). In addition, `ComBat` batch correction was run jointly across `TCGA`, `ICGC`, and `GSE144269` prior to modeling (line 30), and the `meta-cohort` is a non-independent pooled composite of the same datasets.
2. **Repeated Direct Self-Contradictions on the Direction of the `IL-6` / `IL-6R` Axis:** The manuscript contradicts itself four times regarding whether `IL-6`/`IL-6R` is positively or negatively associated with `ISD` and Treg infiltration:
   * Results line 100 states that *"both ISD levels and **IL-6R were significantly increased in the high-Tregs infiltration group** compared with the low-Tregs infiltration group (both P < 0.05, Fig. 2D),"* yet the very next sentence and Results line 133 state that `ISD`, `ISDRS`, and `Tregs` are **negatively correlated with `IL-6R`** and that `IL-6` and `IL-6R` are **significantly decreased** in the high-`ISDRS`/high-Treg group!
   * Similarly, Discussion line 163 refers to the *"observed downregulation of the IL-6/IL-6R axis in resistant cases,"* whereas Discussion line 165 claims *"a pronounced increase in Treg infiltration correlated with elevated ISD levels, further associated with enhanced IL-6 expression."*
3. **Omitted `ISDRS` Formula and Underpowered Sorafenib Clinical Subgroup ($n = 10$):** Methods line 60 states *"The ISDRS of each patient was determined using Equation:"* followed by a blank line where the formula was omitted. In the clinical validation, only $n = 10$ patients received sorafenib (line 35), with no disclosure of the resistant vs. sensitive group sizes or objective response criteria (e.g., RECIST).

### Specific Conclusions and Assessment of Support

* **Superiority of the 7-gene `ISDRS` over 73 published HCC signatures across `TCGA`, `ICGC`, `GSE144269`, and the `meta-cohort`: [Methodologically Flawed].**  
  The 98 input genes were screened using unadjusted $P < 0.05$ thresholds in `limma` and univariate Cox regression (line 50), `ComBat` was applied across training and validation sets combined (line 30), and the winning model (`RSF + stepwise Cox`) was picked from 167 candidate models by maximizing the mean C-index across the validation datasets (lines 55, 116). Comparing a model selected for maximum validation-set performance against 73 fixed external signatures is an asymmetric, biased benchmark.
* **`ISD` and `ISDRS` promote Treg infiltration and sorafenib resistance via the `IL-6`/`IL-6R` axis: [Methodologically Flawed].**  
  The text contradicts itself between lines 100, 133, 163, and 165 on whether `IL-6` and `IL-6R` increase or decrease with Treg infiltration and `ISD` levels. Moreover, all claims are purely correlative `ssGSEA` / `GSVA` associations without functional perturbation of `IL-6`, `IL-6R`, or Tregs.
* **Single-cell `Scissor` identification of `BATF`+ sorafenib-resistant Tregs in `GSE149614`: [Moderately Supported].**  
  Integrating bulk sorafenib response phenotypes (`GSE109211`) with HCC scRNA-seq (`GSE149614`) via `Scissor` and showing elevated `BATF` in `Scissor`+ Tregs is an interesting computational hypothesis, although cell-level violin comparisons (Fig. 5F, Fig. 6B–I) suffer from pseudoreplication across the 10 tumors and unadjusted $P < 0.05$ testing.
* **Clinical validation of `BATF` expression in sorafenib-resistant HCC (`MCHH` cohort, Figure 7): [Fragile].**  
  While paired tumor vs. paracancer ($n = 26$ pairs) and overall survival ($n = 64$) qRT-PCR/IHC analyses of bulk `BATF` have reasonable sample sizes, the sorafenib-treated subset consists of only $n = 10$ total patients (lines 35, 146) without reporting the exact split between responders and non-responders or dual-staining `BATF` with `FOXP3` to confirm that the `BATF`+ cells in IHC are actually Tregs rather than other lymphoid/myeloid subsets.

---

## 3. Forensic Defect Inventory

1. **Test-Set Selection Leakage Across 167 Machine Learning Models and Joint `ComBat` Normalization (Pillar 2, Pillar 3 & Pillar 5):**
   * **Location:** Materials and methods ("Data sources", line 30; "Identification of hub ISDG", line 50; "Integrated ISDRS generated by machine learning", line 55) and Results (line 116).
   * **Defect:** First, `ComBat` batch correction was applied jointly to `TCGA`, `ICGC`, and `GSE144269` before splitting into training and validation analyses. Second, DEGs and univariate Cox genes were screened at unadjusted $P < 0.05$. Third, 167 ML models were evaluated on the validation cohorts (`ICGC`, `GSE144269`, and the redundant pooled `meta-cohort`), and the model with the highest average validation C-index (`0.740`) was chosen as the final `ISDRS`.
2. **Direct Internal Contradictions on the Direction of `IL-6` and `IL-6R` Expression (Pillar 3 & Pillar 7):**
   * **Location:** Abstract (line 5), Results (line 100 vs. line 133), and Discussion (line 163 vs. line 165).
   * **Defect:** Results line 100 claims *"both ISD levels and IL-6R were significantly increased in the high-Tregs infiltration group compared with the low-Tregs infiltration group (both P < 0.05, Fig. 2D),"* immediately before stating that `ISD` and `Tregs` are *negatively* correlated with `IL-6R` (Fig. 2E, Fig. S7B–C). Discussion line 163 states `IL-6`/`IL-6R` is *downregulated* in resistant cases, while Discussion line 165 states elevated `ISD` and Treg infiltration are *"further associated with enhanced IL-6 expression."*
3. **Omitted `ISDRS` Mathematical Formula and Figure Misnumbering (Pillar 7):**
   * **Location:** Materials and methods ("Validation of ISDRS", line 60) and Results (line 146, Figure 7 caption).
   * **Defect:**
     * Line 60 reads *"The ISDRS of each patient was determined using Equation:"* followed by an empty line; the linear predictor equation and numerical coefficients are missing from the text.
     * Results line 146 cites *"Fig. 8J-M"*, which does not exist (the panels are in Figure 7, whose legend skips panel `L`: `(J)... (K)... (M)`).
     * Figure 3 caption (line 114) and Figure 4 caption (line 126) misspell `meta-cohort` as `mate-cohort`, and line 62 misspells `survminer` as `survmine`.
4. **Inconsistent Single-Cell Filtering Criteria and Confused Integration Methods (Pillar 3 & Pillar 7):**
   * **Location:** Materials and methods ("Single-cell RNA sequencing (scRNA-seq) data quality control and processing", line 77).
   * **Defect:** Line 77 states that cells were first filtered to express *"at least 250 genes, resulting in a total of 16,709 cells,"* and then *"additional criteria were applied, including each cell expressed 100 to 5000 genes"* (a lower bound of 100 genes cannot filter any cells after a $\ge 250$-gene filter). The next sentences state *"the canonical correlation analysis (CCA) method was used to identify the sample batch, and the ten samples were integrated using the 'harmony' R package. Anchors were obtained through principal component analysis (PCA) dimensionality reduction,"* conflating three distinct integration workflows (Seurat CCA, Harmony, and PCA/RPCA anchors).
5. **Underpowered Clinical Sorafenib Cohort ($n = 10$) Without Treg Co-Staining (Pillar 4 & Pillar 6):**
   * **Location:** Materials and methods (lines 35, 87) and Results (line 146, Figure 7A–C).
   * **Defect:** Only 10 sorafenib-treated patients were available in the `MCHH` cohort, with no breakdown of $n_{\text{resistant}}$ vs. $n_{\text{sensitive}}$ or RECIST definition, and single-marker `BATF` IHC (at an unusually dilute `1:15000` antibody titer, line 87) cannot distinguish `BATF`+ Tregs from `BATF`+ $\text{CD8}^+$ T cells, Th17 cells, or B cells in tissue sections without `FOXP3` multiplex staining.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.0** | **3.5** | Validation-cohort C-index used to pick the winning model out of 167 ML pipelines; joint `ComBat` across train/test cohorts; unadjusted $P < 0.05$ screening; cell-level scRNA-seq pseudoreplication. |
| **2. Claim-to-Evidence Alignment** | **0.9** | **2.5** | Self-contradictory claims across sections on whether `IL-6`/`IL-6R` is upregulated or downregulated with `ISD`/Tregs; bulk single-marker `BATF` IHC in $n=10$ patients over-interpreted as validating `BATF`+ Tregs. |
| **3. Data Integrity & Biological Plausibility** | **1.0** | **2.0** | Authentic public and institutional cohorts, but `CTNNB1` and `ALAS1` (hepatocyte/metabolic genes) are framed as "immune system development" drivers of Tregs, and single-cell QC/integration steps in line 77 are internally inconsistent. |
| **4. Reproducibility & Data Integrity** | **0.8** | **2.0** | A cloud link (`jianguoyun.com`) is provided, but the `ISDRS` equation is omitted at line 60, `Fig. 8J-M` is misreferenced, and $n_{\text{resistant}}$ vs. $n_{\text{sensitive}}$ in the 10-patient clinical cohort is unreported. |
| **Scientific Core Score** | **2.9** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **3.7** | **10.0** | **Flawed / Overstated** |

---

### 5. Constructive and Doable Suggestions for Improvement

1. **Eliminate Validation-Set Model Selection Leakage:** Select the optimal ML algorithm and hyperparameters strictly via cross-validation within the `TCGA-LIHC` training cohort before evaluating once on independently normalized `ICGC` and `GSE144269` cohorts (removing the redundant pooled `meta-cohort`), and insert the explicit 7-gene `ISDRS` formula and coefficients at Methods line 60.
2. **Resolve the `IL-6` / `IL-6R` Sign Contradictions:** Audit the code for Figure 2D–E and Figure S7B–C to determine why `IL-6R` is reported as both significantly *increased* in the high-Treg group (line 100) and *negatively correlated* with Tregs/`ISD`/`ISDRS` (lines 5, 100, 133), and correct the contradictory statement in Discussion line 165.
3. **Clarify the $n = 10$ Sorafenib Clinical Subgroup and Treg Specificity:** Report the exact number of sorafenib-sensitive and sorafenib-resistant patients among the $n = 10$ `MCHH` cases, state the clinical response criteria (e.g., RECIST 1.1), and either perform dual immunofluorescence (`BATF` + `FOXP3`) or temper the claim that single-plex `BATF` IHC specifically measures Tregs.
4. **Clean Up Single-Cell Methods and Figure Numbering:** Reconcile the redundant gene-count filter (`>= 250` vs. `100–5000`) and integration method (`CCA` vs. `Harmony`) in line 77, and fix `Fig. 8J-M` to `Fig. 7J-M` (and restore missing label `L` in the Figure 7 legend).
