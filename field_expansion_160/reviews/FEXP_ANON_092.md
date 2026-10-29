# Review of FEXP_ANON_092

**Overall Score:** **5.2 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **4.1 / 8.0**  
* **Score Breakdown:** Rigor: 1.5/3.5 | Claims: 1.3/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.1/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Role / Domain:** Neuro-oncology bioinformatics and translational study identifying a three-gene interferon-stimulated "macrophage-related" prognostic signature (`ISG20`, `PARP12`, `IFIT5`) in glioblastoma (GBM) using `TCGA-GBM` ($n = 159$), `CGGA-GBM` ($n = 374$), `IMMUcan scDB` (`GSE131928`), and Akoya Opal multiplex immunofluorescence ($n = 5$ FFPE samples).
* **Blinded Document Assessment:** Unlike template papers that conceal negative results or omit model parameters, this manuscript transparently reports its multivariate Cox coefficients, C-index (`0.63`), validation AUROCs (`0.607–0.633`), non-significant subgroup log-rank test in classical/mesenchymal GBM ($p = 0.0997$), and cell-type expression percentages (`ISG20` in 68.9% of T cells vs. 16.1% of macrophages). Nevertheless, the study's central conclusions are weakened by `IDH1`/G-CIMP confounding under modern WHO CNS5 diagnostic criteria, collinearity among the three co-expressed interferon-stimulated genes (causing `IFIT5` to flip to a negative coefficient against `ISG20` and `PARP12`), and the fact that `ISG20` is predominantly expressed in T cells and dendritic cells rather than macrophages.

---

## 2. Executive Summary & Editorial Verdict

The authors apply CIBERSORT and WGCNA to `TCGA-GBM` ($n = 159$) and identify a 129-gene `light-yellow` module positively correlated with M1 macrophage abundance ($r = 0.48, p = 6 \times 10^{-11}$). Univariate Cox regression ($p < 0.05$, 9 genes), LASSO regression (6 genes), and multivariate Cox regression yield a three-gene risk score (`0.471 * ISG20 + 0.263 * PARP12 - 0.511 * IFIT5`), which is validated in `CGGA-GBM` ($n = 374$ pooled from `mRNAseq-693` and `mRNAseq-325`). The authors evaluate clinical covariates, GSEA pathways, ESTIMATE scores, immune checkpoint expression, TCIA Immunophenoscore (IPS), and `pRRophetic` drug sensitivity, and examine `ISG20` expression in `GSE131928` (10 GBM scRNA-seq cases via `IMMUcan scDB`) and by 5-color multiplex immunofluorescence (`ISG20`, `PD-1`, `CD68`, `CD163`, `DAPI`) in five clinical GBM specimens.

**Editorial Verdict: Major Revision (Mixed / Salvageable).** The workflow is clearly documented and includes multiplex immunofluorescence on clinical tissue, but four substantive issues undermine the primary claims:
1. **Confounding by `IDH1` Mutation / G-CIMP Status and Loss of Prognostic Significance in Classical/Mesenchymal GBM:** Under the 2021 WHO CNS5 classification, `IDH1`-mutant / G-CIMP+ tumors are classified as *Astrocytoma, IDH-mutant, WHO grade 4* rather than GBM. In `TCGA-GBM`, the low-risk group is enriched for `IDH1`-mutant, G-CIMP+, and neural/proneural cases (Figure 3A). When restricted to `classic plus mesenchymal` tumors (which are predominantly `IDH1`-wildtype true GBMs), the risk score fails to significantly stratify survival ($\text{log-rank } p = 0.0997$, line 100, Figure 3D), and external validation discrimination in `CGGA-GBM` is modest ($\text{AUROC} = 0.615, 0.607, 0.633$ at 1, 2, and 3 years; line 84).
2. **Multicollinearity and Sign Inversion Among Co-Expressed Interferon-Stimulated Genes (Table 1):** `ISG20`, `PARP12`, and `IFIT5` all come from the same positively co-expressed WGCNA module (`light-yellow`) and are all canonical Type I/II interferon-stimulated genes (ISGs). Because they are positively correlated, fitting an unpenalized multivariate Cox model after LASSO caused suppressor-variable sign inversion: `ISG20` ($\beta = +0.471, p = 0.0032$) and `PARP12` ($\beta = +0.263, p = 0.0571$, non-significant) receive positive weights, whereas `IFIT5` ($\beta = -0.511, p = 0.0001$) receives a large negative weight despite having a positive univariate hazard ratio in Figure 2A!
3. **`ISG20` Is Predominantly Expressed in T Cells (68.9%) and Dendritic Cells (38.5%), Not Macrophages (16.1%):** While framed as a "macrophage-related gene signature," the authors' own single-cell analysis of `GSE131928` (line 116, Figure 5D) shows that `ISG20` is expressed in 68.9% of T cells and 38.5% of DCs versus only 16.1% of macrophages, and neither `PARP12` nor `IFIT5` is evaluated in the scRNA-seq or immunofluorescence experiments.
4. **Unquantified Multiplex Immunofluorescence ($n = 5$):** Figure 5F presents a single micrograph without quantifying the fraction of $\text{CD68}^+/\text{CD163}^+$ macrophages co-expressing `ISG20` and `PD-1` across the five patient samples.

### Specific Conclusions and Assessment of Support

* **WGCNA identification of the 129-gene `light-yellow` module correlated with CIBERSORT M1 macrophages: [Well Supported].**  
  The WGCNA network construction ($\beta = 8, R^2 = 0.854$) and module–trait correlation ($r = 0.48, p = 6 \times 10^{-11}$) are standard and well documented, though bulk interferon modules reflect shared interferon signaling across multiple infiltrating leukocyte and tumor populations.
* **Three-gene signature (`ISG20`, `PARP12`, `IFIT5`) has "favorable accuracy" as an independent prognostic factor in GBM: [Fragile].**  
  The training C-index is `0.63`, validation AUROCs in `CGGA-GBM` are `0.607–0.633`, `PARP12` is not statistically significant in the multivariate model ($p = 0.0571$), `IFIT5` flips sign due to collinearity with `ISG20`/`PARP12`, and the signature does not significantly stratify survival in classical/mesenchymal GBM ($p = 0.0997$, line 100).
* **The signature predicts immunotherapy resistance/sensitivity and chemotherapy response in GBM: [Overstated].**  
  First, the Abstract (line 9) states the signature predicts *"resistance of immuno- and chemo-therapy,"* whereas Results line 108 (Figure 4F) claims PD-1 and CTLA4 blockade have *"significantly better treatment efficacy in the high-risk subgroup"* based solely on TCIA IPS scores. Second, computational IPS and `pRRophetic` scores are unvalidated surrogates in GBM, where clinical trials of PD-1 blockade have not shown survival benefit.
* **Co-expression and co-localization of `ISG20` and `PD-1` in GBM macrophages: [Moderately Supported].**  
  Multiplex immunofluorescence (Fig. 5F) qualitatively shows `ISG20`/`PD-1`/`CD68`/`CD163` co-staining in a subset of cells, but `ISG20` is 4-fold more prevalent in T cells (68.9%) than in macrophages (16.1%) in `GSE131928` (line 116), and no quantitative cell segmentation counts across the 5 FFPE specimens are reported.

---

## 3. Forensic Defect Inventory

1. **Collinearity-Induced Sign Inversion in Multivariate Cox Regression (`IFIT5` $\beta = -0.511$ vs. `ISG20` $\beta = +0.471$) (Pillar 3 & Pillar 4):**
   * **Location:** Results ("Construction and validation of a macrophage-related gene signature...", line 84, Figure 2A–B, and Table 1, lines 90–96).
   * **Defect:** All nine univariate Cox candidate genes in the `light-yellow` module are positively co-expressed interferon-stimulated genes associated with higher risk in univariate analysis (Fig. 2A). Passing six LASSO-selected collinear ISGs into stepwise/multivariate Cox regression induced severe multicollinearity: `IFIT5` was assigned a strong negative weight ($\beta = -0.511, p = 0.0001$) canceling against `ISG20` ($\beta = +0.471, p = 0.0032$) and `PARP12` ($\beta = +0.263, p = 0.0571$).
2. **Confounding by `IDH1`-Mutant / G-CIMP+ Cases and Non-Significance in Classical/Mesenchymal Subtypes (Pillar 2 & Pillar 6):**
   * **Location:** Results ("The macrophage-related gene signature is an independent risk factor...", line 100, Figure 3A–D).
   * **Defect:** Historical `TCGA-GBM` and `CGGA-GBM` cohorts include `IDH1`-mutant (G-CIMP+) grade IV astrocytomas, which are biologically distinct from `IDH1`-wildtype GBM under WHO CNS5 criteria and have lower ISG expression and much longer 3-year survival (explaining why the training 3-year AUROC is `0.834` while 1- and 2-year AUROCs are `0.694` and `0.686`). When tested in `classic plus mesenchymal` GBM (which lacks `IDH1`-mutant cases), survival stratification is non-significant ($\text{log-rank } p = 0.0997$, Fig. 3D). Also, pooling `CGGA mRNAseq-693` and `mRNAseq-325` into a single 374-patient validation cohort (line 28) without describing batch-effect correction can distort median risk cutoffs.
3. **Lineage Specificity Mismatch in scRNA-seq (`ISG20` in 68.9% of T Cells vs. 16.1% of Macrophages) and Omission of `PARP12`/`IFIT5` (Pillar 1 & Pillar 5):**
   * **Location:** Results ("scRNA-seq analysis and multiplexed immunofluorescence...", line 116, Figure 5C–F).
   * **Defect:** Although the signature is termed a "macrophage-related gene signature," Figure 5D shows `ISG20` is expressed primarily in T cells (68.9%) and DCs (38.5%) and only in 16.1% of macrophages. `PARP12` and `IFIT5` are omitted from both the scRNA-seq and multiplex IF validations.
4. **Discrepancy Between Text and Figure Legends (`CD68` vs. `PDCD1` in Fig. 5E; Duplicate Caption in Fig. 4E) and Formula Typo (Pillar 7):**
   * **Location:** Methods (line 43, line 58), Results (line 116), and Figure legends 4E (line 111) and 5E (line 119).
   * **Defect:**
     * Line 43 writes the risk score formula as $\text{risk score} = \sum_{i=1}^n \beta_i * i$, using the index $i$ as both the summation index and the gene expression value.
     * Line 58 misspells `UMAP Plot` as `UAMP Plot`.
     * Figure 4E caption (line 111) repeats the Figure 4C caption verbatim (*"Violin plot comparing the stromal, immune and ESTIMATE scores..."*) instead of describing the immune checkpoint genes plotted in Figure 4E (`CD200`, `CD274`, `CTLA4`, `PDCD1`, `PDCD1LG2`, `TNFRSF14`).
     * Results line 116 states Figure 5E shows the overlap of `ISG20` with `CD68`, `CD86`, `IRF5`, `CD163`, and `STAT6`, whereas the Figure 5E caption (line 119) states it shows `ISG20 and PDCD1` (omitting `CD68`).

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.5** | **3.5** | Transparent reporting of coefficients, AIC, C-index (`0.63`), and subgroup $p$-values, but penalized for collinear ISG sign reversal in multivariate Cox, `IDH1`-mutant confounding, unquantified $n=5$ mIF, and pooling two CGGA batches without batch correction details. |
| **2. Claim-to-Evidence Alignment** | **1.3** | **2.5** | Claims of "favorable accuracy" (`AUROC 0.607–0.633` in validation; $p=0.0997$ in classical/mesenchymal GBM) and "macrophage-related" specificity (`ISG20` in 68.9% of T cells vs. 16.1% of macrophages) are overstated; Abstract ("resistance") conflicts with Fig. 4F ("better efficacy"). |
| **3. Data Integrity & Biological Plausibility** | **1.3** | **2.0** | Authentic TCGA/CGGA/GSE131928 datasets and real 5-color Opal mIF with IRB approval (`S2018-089-02`); biological framing should reflect pan-leukocyte/tumor interferon signaling rather than macrophage-restricted expression. |
| **4. Reproducibility & Data Integrity** | **1.1** | **2.0** | Explicit regression coefficients and public accessions are provided, but no analysis code is shared, `InForm` single-cell mIF quantification tables are missing, and Figure 4E/5E captions conflict with the text. |
| **Scientific Core Score** | **4.1** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **5.2** | **10.0** | **Mixed / Salvageable** |

---

### 5. Constructive and Doable Suggestions for Improvement

1. **Restrict Survival Modeling to `IDH1`-Wildtype GBM (WHO CNS5 Standard):** Repeat the training (`TCGA-GBM`) and validation (`CGGA-GBM`, accounting for batch effects between `mRNAseq-693` and `mRNAseq-325`) analyses after excluding `IDH1`-mutant / G-CIMP+ astrocytomas to determine whether the signature retains prognostic value in true `IDH1`-wildtype GBM.
2. **Use LASSO Penalized Coefficients Directly Without Unpenalized Multivariate Cox Refitting:** Retain the L1/L2-penalized Cox regression weights (or a composite ISG module score) rather than refitting an unpenalized multivariate Cox model on collinear interferon-stimulated genes that forces `IFIT5` to take a negative coefficient.
3. **Quantify Multiplex Immunofluorescence Across All 5 Patients and Profile `PARP12`/`IFIT5` in scRNA-seq:** Export cell-level segmentation counts from Akoya `InForm` software across all 5 FFPE GBM cases to report the mean $\pm$ SD percentage of $\text{CD68}^+/\text{CD163}^+$ macrophages (and $\text{CD68}^-$ lymphocytes) positive for `ISG20` and `PD-1`, and add scRNA-seq feature plots for `PARP12` and `IFIT5` in `GSE131928`.
4. **Fix Formula and Caption Errors:** Correct the risk score equation in line 43 to $\sum_{i=1}^n \beta_i x_i$, fix `UAMP` to `UMAP` in line 58, update the duplicated Figure 4E caption to match the immune checkpoint violin plots, and reconcile `CD68` vs. `PDCD1` between Results line 116 and the Figure 5E caption.
