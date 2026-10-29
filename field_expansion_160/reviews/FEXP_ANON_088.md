# Review of FEXP_ANON_088

**Overall Score:** **8.0 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.2 / 8.0**  
* **Score Breakdown:** Rigor: 2.8/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.8/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Role / Domain:** Large-scale single-cell and spatial transcriptomics atlas resource paper (`uniLUNG`) integrating 9.2 million human lung cells from 62 datasets and 1,807 donors across healthy and 17 pulmonary disease states.
* **Blinded Document Assessment:** A technically rigorous, large-scale community resource paper featuring systematic ambient RNA (`DecontX`) and doublet (`DoubletFinder`) filtering, an 18-method `scIB` integration benchmark on an 854,935-cell core atlas, a 4-level ontology-mapped annotation hierarchy (`uHAF`), donor-aware compositional (`scCODA`) and pseudobulk (`Libra`/`edgeR`) statistical testing, and full open data/code deposition (Zenodo, GitHub, and web portal). The primary limitations lie in the biological interpretation of the two exploratory vignettes—specifically whether `T-like B cells` and `Lym-monocytes` represent intrinsic transcriptional states versus physical cell–cell complexes/trogocytosis, and whether a `Monocle3` trajectory fit across independent LUAD, LUSC, and SCLC donors captures longitudinal NSCLC-to-SCLC histological transformation versus cross-sectional non-neuroendocrine SCLC plasticity.

---

## 2. Executive Summary & Editorial Verdict

The authors construct `uniLUNG` (`https://lung.unifiedcellatlas.org`), an integrated single-cell transcriptomic reference of the human lung comprising 9,201,161 cells from 1,807 donors across 62 published datasets spanning health and 17 lung diseases. Starting from raw count matrices standardized to 43,878 HGNC gene symbols and filtered with `DecontX` and `DoubletFinder`, they assemble a 34-batch `uniLUNG core` (854,935 cells from 311 donors across 14 datasets and 11 lung conditions), benchmark 18 integration pipelines using eight `scIB` metrics, select `scANVI`, and perform four-round hierarchical clustering and manual curation within a 122-type Universal Hierarchical Annotation Framework (`uHAF`, resolving 60 cell types in the core). Regularized `CellTypist` logistic regression models transfer labels to the 9.2M-cell extended atlas. Using this resource, the authors present two biological case studies: (1) a cross-disease immune analysis (1.64M cells) using `scCODA`, NMF, `Libra`/`edgeR` pseudobulk DEGs, `SCENIC`, `scArches`, and CITE-seq projection that identifies `Lym-monocytes` and `T-like B cells`; and (2) a lung cancer multi-omics analysis (1.68M scRNA-seq cells from 290 LUAD, 89 LUSC, and 21 SCLC patients plus 20 spatial transcriptomic sections analyzed with `SEDR`, `Cancer-Finder`, `SpaGene`, `COMMOT`, `cell2location`, and `NCEM`) characterizing a putative `NSCLC-like SCLC` malignant state.

**Editorial Verdict: Minor Revision (Strong / Sound).** The primary deliverable—the `uniLUNG` core and extended reference atlas, `uHAF` taxonomy, 18-method integration benchmark, `uGT` database, and open downloads—is methodologically sound and adheres to modern single-cell statistical standards (including donor-stratified `scCODA` compositional modeling and donor-adjusted `edgeR` pseudobulk differential expression). However, the causal framing of the lung cancer histological transition vignette should be tempered: running `Monocle3` across pooled malignant cells from *different* LUAD, LUSC, and SCLC patients cannot prove longitudinal lineage evolution from NSCLC to SCLC without intra-patient paired biopsies or clonal lineage tracing, as cells from SCLC patients clustering near NSCLC (`NSCLC-like SCLC`) may instead represent the established non-neuroendocrine (`SCLC-Y` / `POU2F3` / `REST`-high) SCLC transcriptional state, and scoring spatial spots with a proliferation-enriched signature (`TOP2A`, `MKI67`, `TPX2`) in treatment-naive LUAD/LUSC sections may reflect proliferative NSCLC niches rather than impending SCLC transformation.

### Specific Conclusions and Assessment of Support

* **Construction and `scIB` benchmarking of the 854,935-cell `uniLUNG core` and 9.2M-cell extended atlas via `uHAF`, `scANVI`, and `CellTypist`: [Well Supported].**  
  Reprocessing from raw counts with uniform QC (`DecontX` $\le 0.2$, `DoubletFinder`), benchmarking 18 integration variants across four batch-correction and four bio-conservation metrics (`scIB`), iterative manual curation of 60 core cell types, and transparent documentation of the distinction between manually curated core labels and automated `CellTypist` extension labels (Methods line 82) provide a well-validated reference resource.
* **Cross-disease compositional shifts and identification of `Lym-monocytes` and `T-like B cells` via `scCODA`, pseudobulk `edgeR`, `scArches`, and CITE-seq: [Moderately Supported].**  
  Compositional comparisons appropriately use `scCODA` stratified by tissue/site with donor and platform covariates ($\text{FDR} < 0.05$), and DEGs are validated via donor-adjusted `Libra`/`edgeR` pseudobulk models (`~ donor_ID + group`). While multi-algorithm computational doublet filtering and CITE-seq surface protein mapping support the reproducible detection of `T-like B cells` (`TRBC1`, `GZMA`, `CD3` + `CD19`/`CD20`) and `Lym-monocytes`, computational doublet detectors and droplet CITE-seq cannot fully exclude physical in vivo T–B or T–monocyte cell conjugates or trogocytosis without imaging flow cytometry or FACS singlet sorting.
* **`NSCLC-like SCLC` represents a transitional malignant subpopulation driving histological NSCLC-to-SCLC transformation: [Overstated].**  
  The `NSCLC-like SCLC` cluster consists of malignant cells derived from SCLC patients that co-embed along a `Monocle3` partition with LUAD and LUSC malignant cells from unrelated donors (Fig. 5d–g). Because no longitudinal pre-/post-transformation biopsies or shared somatic mutation / TCR / CNV phylogenies link an individual patient's NSCLC clone to SCLC, inter-patient transcriptional continuity in UMAP/Monocle3 space reflects phenotypic similarity (e.g., non-neuroendocrine SCLC plasticity) rather than demonstrated temporal NSCLC-to-SCLC transdifferentiation.
* **Spatial microenvironment remodeling (CAF-ECM-`ITGB1` colocalization, `MIF`/`MK` signaling flow, TLS enrichment, and `NCEM` sender–receiver dependencies) in LUAD/LUSC regions scoring high for the `NSCLC-like SCLC` signature: [Moderately Supported].**  
  The spatial multi-omics pipeline (`SEDR`, `SpaGene`, `COMMOT`, `cell2location`, `NCEM`) is technically sophisticated and internally consistent across 12 LUAD and 8 LUSC sections. However, because the `NSCLC-like SCLC` signature is heavily weighted toward mitotic/proliferation genes (`TOP2A`, `MKI67`, `TPX2`, Fig. 5f/i), high signature scores in multi-cell spatial spots (~30 cells/spot) of primary LUAD/LUSC tumors may track highly proliferative, poorly differentiated NSCLC clones rather than physical SCLC transition.

---

## 3. Forensic Defect Inventory

1. **Cross-Patient Pseudotime Trajectory Interpreted as Longitudinal NSCLC-to-SCLC Histological Transformation (Pillar 1, Pillar 3 & Pillar 6):**
   * **Location:** Methods ("Trajectory construction", line 170) and Results ("Cross-diseases atlas reveals transitional NSCLC-SCLC state of malignant cells", chunk 2, lines 20–29, Figure 5d–h).
   * **Defect:** `Monocle3` was applied to pooled malignant cells from independent LUAD ($n = 290$), LUSC ($n = 89$), and SCLC ($n = 21$) donors, and trajectory directionality was assigned using clinical tumor stage across patients. Pseudotime across genetically distinct tumors from different individuals measures transcriptional gradients between tumor types, not within-patient somatic evolution from NSCLC to SCLC. Furthermore, in spatial transcriptomics (chunk 2, line 34, Fig. 6d), scoring LUAD/LUSC spots with a signature enriched in cell-cycle genes (`TOP2A`, `MKI67`, `TPX2`) conflates proliferative NSCLC states with neuroendocrine SCLC transformation.
2. **Inability of Computational Filtering and Droplet CITE-seq to Exclude Physical T–B / Monocyte–Lymphocyte Conjugates or Trogocytosis (Pillar 5 & Pillar 6):**
   * **Location:** Results (lines 272–279; chunk 2, lines 6–10, Figures 3–4).
   * **Defect:** While the authors ran `DoubletFinder` and secondary computational doublet callers (Supplementary Figs. S13–S14) and mapped onto COVID-19 CITE-seq data, biologically adhered T–B cell complexes and monocyte–T cell rosettes encapsulated in the same droplet co-express both mRNA and surface ADT proteins of both lineages and frequently pass computational doublet filters when their gene expression matches the intermediate cluster centroid.
3. **Inconsistency in NMF Subpopulation Counts for Monocytes and B Cells (Pillar 7):**
   * **Location:** Methods ("NMF analysis of monocytes and B cells", line 117) and Figure 3d caption (line 270) vs. Methods (line 122) and Results (line 272).
   * **Defect:** Methods line 117 states *"yielding a rank of 3 for monocytes and 4 for B cells"*, and Figure 3d caption states *"NMF analysis divided B cells and monocytes into 3 and 4 subpopulations, respectively"* (swapping which lineage had 3 vs. 4), whereas Methods line 122 and Results line 272 state that both lineages were divided into *three* subpopulations (`CD16`, `CD14`, and `Lym-monocyte` for monocytes; `memory`, `activated`, and `T-like B cells` for B cells).
4. **Omitted Equation and Minor Editorial Truncations (Pillar 7):**
   * **Location:** Methods (line 51 and line 64), Results (chunk 2, line 29), and Figure 6d caption (chunk 2, line 37).
   * **Defect:**
     * Line 51 ends with an incomplete one-word sentence: *"Subsequently."*
     * Line 64 states *"To ensure interpretability, all LISI scores were normalised to a 0–1 scale, where higher values denote better performance. The calculation formula is as follows:"* followed by a blank line where the equation was dropped.
     * Chunk 2, line 29 repeats a phrase verbatim: *"(a trajectory-associated gene also enriched in this signature a trajectory-associated gene also enriched in this signature)"*.
     * Figure 6d caption (chunk 2, line 37) terminates mid-sentence: *"suggesting."*

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.8** | **3.5** | Rigorous primary resource pipeline (`DecontX`, `DoubletFinder`, 18-method `scIB` benchmark, `scCODA` compositional modeling, donor-aware `Libra`/`edgeR` pseudobulk DEGs, `cell2location`, `NCEM`); minor deduction for cross-patient `Monocle3` trajectory and missing LISI formula. |
| **2. Claim-to-Evidence Alignment** | **1.8** | **2.5** | Primary atlas claims are well supported and extension caveats are transparently stated; causal claims that `NSCLC-like SCLC` drives NSCLC-to-SCLC transformation overreach cross-sectional inter-patient data. |
| **3. Data Integrity & Biological Plausibility** | **1.6** | **2.0** | Comprehensive curation across 62 datasets (9.2M cells, 1,807 donors); biological interpretation of `T-like B cells`/`Lym-monocytes` and `NSCLC-like SCLC` requires caveats regarding physical cell complexes/trogocytosis and proliferation-signature confounding. |
| **4. Reproducibility & Data Integrity** | **1.8** | **2.0** | Full open access via interactive web portal, two Zenodo repositories, and GitHub source code; minor deduction for omitted LISI formula (line 64), 3 vs. 4 NMF cluster count discrepancy, and minor text truncations. |
| **Scientific Core Score** | **6.2** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **8.0** | **10.0** | **Strong / Sound** |

---

### 5. Constructive and Doable Suggestions for Improvement

1. **Reframe the `NSCLC-like SCLC` Trajectory and Spatial Claims Around Cross-Sectional Plasticity:** Explicitly state in the Abstract, Results, and Discussion that because the `Monocle3` trajectory was constructed across independent LUAD, LUSC, and SCLC donors rather than longitudinal biopsies from patients undergoing histological transformation, `NSCLC-like SCLC` represents a transcriptionally intermediate/plastic state (potentially corresponding to non-neuroendocrine `SCLC-Y`/`REST`+ SCLC) rather than proven temporal lineage conversion.
2. **Control for Proliferation Confounding in the Spatial `NSCLC-like SCLC` Score:** Re-compute the spatial `NSCLC-like SCLC` module score in the 12 LUAD and 8 LUSC sections after removing canonical cell-cycle/proliferation markers (`TOP2A`, `MKI67`, `TPX2`, `CCNB1`, `CDK1`) or regressing out S/G2M phase scores to verify that spatial enrichment is not solely driven by mitotic rate.
3. **Discuss In Vivo Cell–Cell Complexes and Trogocytosis for `T-like B Cells` and `Lym-monocytes`:** Expand the Discussion to note that physiologically adhered T–B conjugates or membrane exchange (trogocytosis) can survive computational doublet filtering and CITE-seq mapping, and recommend imaging flow cytometry (ImageStream) or spatial single-cell proteomics (CODEX/IMC) for definitive physical singlet validation.
4. **Restore the Missing LISI Formula and Fix Editorial Typos:** Insert the missing LISI normalization equation at Methods line 64, reconcile the NMF rank count (3 vs. 4 for B cells and monocytes) between Methods lines 117/122 and Figure 3d, delete the stray word *"Subsequently."* at line 51, fix the duplicated phrase at chunk 2 line 29, and complete the truncated sentence in the Figure 6d legend.
