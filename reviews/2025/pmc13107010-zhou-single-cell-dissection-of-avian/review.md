# Review of PMC13107010 (PMID:41158070)

**Manuscript Title:** Single-cell dissection of avian (chicken) H1N1 influenza virus coinfection dynamics in mammalian (mouse) and avian (chicken) hosts  
**Authors:** Zhou Y, Zhang X, Chen F, Deng W, Wang P.  
**Journal / Preprint:** *Acta Biochim Biophys Sin (Shanghai)* (2025; `PMC13107010` / `PMID:41158070` / `10.3724/abbs.2025184`)  
**Calibration Study Cohort:** Cohort A — Known Invalid / Refuted (`A50` | Double-Blinded as `ANON_173`)  
**Overall Score:** **2.2 / 10.0** (Fundamentally Invalid)
* **Score Breakdown:** Rigor: 0.5/3.5 | Claims: 0.5/2.5 | Biology: 0.5/2.0 | Reproducibility: 0.7/2.0

---

## 1. Executive Summary & Synthesis

This manuscript purports to investigate avian H1N1 influenza virus infection and baloxavir marboxil treatment across mouse (*Mus musculus*) and chicken (*Gallus gallus*) hosts using single-cell RNA sequencing (scRNA-seq) of lung and tracheal tissues collected at 0, 3, 7, and 14 days post-infection (dpi).

A forensic audit of the study design, bioinformatic pipeline, figures, and biological interpretation reveals catastrophic methodological and biological invalidity across multiple pillars:
1. **Cross-species and cross-tissue merging into a single unstratified UMAP and cell-proportion barplot:** Despite claiming to profile two species belonging to different vertebrate classes (birds vs. mammals), two organs (lung and trachea), and four timepoints (0, 3, 7, 14 dpi) aligned separately to `Gallus_gallus-6.0` and `GRCm39`, all results (Figures 1–5) present a *single* merged UMAP and *single* set of three groups (`Healthy`, `Flu`, `Treatment`) without ever separating chicken cells from mouse cells, lung from trachea, or 3, 7, and 14 dpi.
2. **Self-contradictory species attribution of the same Figure 1C barplot:** In the Results (`line 34`), the authors attribute the single barplot in Figure 1C (`neutrophils increasing from 5% to 30%` and `CD4+ T cells markedly decreased`) to **chickens** (*"suggesting the suppression of helper T-cell-mediated responses in chickens"*). Yet in the Discussion (`line 64`), they attribute the *exact same* CD4+ T-cell suppression to **mammalian hosts** in contrast to chickens (*"In contrast, mammalian hosts exhibited CD4+ T-cell suppression"*).
3. **Impossible avian immunology and cross-species annotation artifacts:** The authors claim that `neutrophils` increased from 5% to 30% in avian hosts (`lines 34, 64`) and that dendritic cells expressed `HLA-DR` (`line 42`). **Birds (chickens) do not have neutrophils** (they have *heterophils*, which lack myeloperoxidase), and neither chickens (`BLB1/BLB2`) nor mice (`H2-Ab1/H2-Eb1`) possess the human MHC class II gene `HLA-DR`. This artifact stems from annotating chicken and mouse single cells using `SingleR` with **human PBMC (Human Cell Atlas) and pig bulk RNA-seq reference datasets** (`line 32`)!
4. **False "coinfection" framing in Title and Discussion:** Both the Title (`line 9`: *"scRNA-seq reveals H1N1 coinfection dynamics in mouse and chicken"*) and Discussion (`line 64`) claim to study "coinfection dynamics," yet the experiment involves single-pathogen inoculation with one H1N1 strain (`A/chicken/Guangdong/2023`) and no co-infecting pathogen.

---

## 2. Claim-by-Claim Evaluation

* **Claim 1:** *scRNA-seq reveals distinct H1N1 "coinfection dynamics" in mouse and chicken hosts, with avian hosts showing neutrophil expansion from 5% to 30% and mammalian hosts showing CD4+ T-cell suppression (Title, lines 9, 34, 64).* — **[Methodologically Flawed]**
  * **Evidence & Critique:** First, no coinfection was performed (`Materials and methods: Animal experiments and ethical approval`, line 22: mice and chickens were inoculated intranasally with $10^5\text{ EID}_{50}$ of a single strain, `A/chicken/Guangdong/2023 (H1N1)`, or sterile PBS). Second, Figures 1A–C do not stratify cells by species (chicken vs. mouse), tissue (lung vs. trachea), or timepoint (0, 3, 7, 14 dpi); there is only a single barplot (`Healthy`, `Flu`, `Treatment`) in Figure 1C. Third, the text contradicts itself on which species Figure 1C represents: Line 34 states that Figure 1C shows *"the suppression of helper T-cell-mediated responses in chickens"*, whereas Line 64 states *"In contrast, mammalian hosts exhibited CD4+ T-cell suppression"* while attributing the neutrophil increase from the very same Figure 1C barplot to avian hosts. Fourth, chickens do not possess neutrophils (avian granulocytes are heterophils).

* **Claim 2:** *Single-cell transcriptomes of chicken (`Gallus_gallus-6.0`) and mouse (`GRCm39`) lung and trachea were accurately annotated into 11 immune and structural cell types using `SingleR` against Human Cell Atlas PBMC and pig ENA bulk RNA-seq references, identifying `HLA-DR` upregulation in dendritic cells (lines 28–42).* — **[Methodologically Flawed]**
  * **Evidence & Critique:** Aligning chicken sequencing libraries to `Gallus_gallus-6.0` and mouse libraries to `GRCm39` produces count matrices in chicken and mouse gene symbol/Ensembl namespaces, respectively (`line 28`). Passing chicken and mouse count matrices directly into `SingleR v2.0` using **human PBMC (`Human Cell Atlas`)** and **pig (`Sus scrofa`) bulk RNA-seq** references (`line 32`) without orthology mapping is bioinformatically invalid, and human PBMC references lack respiratory epithelial, endothelial, and fibroblast populations altogether. Furthermore, reporting human gene symbols such as `HLA-DR` (`line 42`) and `IL8` (`line 34`; mice lack an orthologous *IL8/CXCL8* gene) as differentially expressed markers in a mouse/chicken experiment demonstrates that the reported gene markers do not correspond to the stated `GRCm39` and `Gallus_gallus-6.0` alignments.

* **Claim 3:** *Monocle 3 pseudotime analysis reveals bifurcated macrophage differentiation into M1 (`iNOS/TNF-alpha`) and M2 (`Arg1/IL-10`) branches and linear NK cell differentiation across five states (lines 46–52, Figure 2).* — **[Methodologically Flawed]**
  * **Evidence & Critique:** In addition to pooling unknown mixtures of species, tissues, and timepoints into a single trajectory, the main text citations of Figure 2 (`line 46`) do not match the Figure 2 panels or caption (`line 52`):
    * Line 46 cites `(Figure 2A)` for the bifurcated macrophage trajectory and `(Figure 2B)` for the linear NK cell trajectory, whereas the Figure 2 caption (`line 52`) states that `(A)` is a *"Unified global trajectory of all immune cells"*, `(B)` is the *"Macrophage trajectory stratified into five states"*, and `(C)` is the *"NK cell trajectory across five developmental states"*.
    * Line 46 cites `(Figure 2C)` for macrophage state expansion, `(Figure 2D)` for NK cell state proportions, `(Figure 2E)` for macrophage pseudotime, and `(Figure 2F)` for NK pseudotime; whereas the caption (`line 52`) defines `(D)` as a heatmap of state-defining genes, `(E)` as macrophage state distribution, `(F)` as macrophage pseudotime, `(G)` as NK state distribution, and `(H)` as NK pseudotime.

* **Claim 4:** *Baloxavir marboxil treatment at 10 mg/kg orally once daily from 1 dpi restores immune homeostasis, suppresses `TNF-alpha`, `IL-6`, and `IL-1beta`, and rebalances M1/M2 macrophage and NK states across both hosts (lines 22, 34–64).* — **[Fragile]**
  * **Evidence & Critique:** No viral load measurements (e.g., $\text{TCID}_{50}$, $\text{EID}_{50}$, or viral RNA RT-qPCR copies in lung or trachea), body weight curves, survival curves, or histopathological scores are presented anywhere in the manuscript to confirm productive infection or antiviral efficacy of baloxavir marboxil in either mice or chickens. Moreover, no accession number (NCBI GEO, SRA, or GSA) or code repository is provided (`Data availability statement`, line 81: *"Available from the corresponding author upon reasonable request"*).

---

## 3. Technical & Methodological Critique

### Major Flaws

1. **Unexplained Cross-Species Matrix Integration and Missing Stratification:**
   * According to `Materials and methods` (`line 22`), the experimental design comprises 2 species (`BALB/c mice` and `SPF White Leghorn chickens`) $\times$ 3 groups (`Control`, `Infected`, `Treated`) $\times$ 4 timepoints (`0, 3, 7, 14 dpi`, with 5 animals/timepoint) $\times$ 2 tissues (`lung` and `trachea`). That design corresponds to up to 48 biological condition-tissue-species-timepoint combinations. Yet the manuscript never reports how many scRNA-seq libraries were actually sequenced, how many cells passed QC per species or tissue, or how chicken (`Gallus_gallus-6.0`) and mouse (`GRCm39`) feature spaces were combined into a single Seurat object (`Single-cell data integration and clustering`, line 30). Presenting a single UMAP (Fig. 1B) and single proportion barplot (Fig. 1C) without separating chicken from mouse or lung from trachea renders every quantitative cell-type percentage and differential expression test biologically meaningless.

2. **Biological Errors in Avian and Murine Immunology:**
   * **Avian neutrophils:** Chickens lack neutrophils; their functionally analogous polymorphonuclear granulocyte is the heterophil. Claiming that scRNA-seq identified a 6-fold expansion of "neutrophils" in avian hosts (`lines 34, 64`) is biologically incorrect.
   * **Non-existent murine/avian gene symbols (`HLA-DR`, `IL8`):** Mice lack the `IL8` (*CXCL8*) gene (relying instead on `Cxcl1/KC` and `Cxcl2/MIP-2`), and neither mice nor chickens have the human `HLA-DR` locus.
   * **Human PBMC and Porcine References for Chicken/Mouse Lung Annotation:** Using `SingleR` with human PBMC and pig bulk RNA-seq datasets (`line 32`) to annotate chicken and mouse respiratory tissues is methodologically indefensible.

3. **Direct Contradiction Between Results and Discussion on Host Species:**
   * Line 34 (`Results`): *"...whereas the percentage of CD4+ T cells markedly decreased (Figure 1C), suggesting the suppression of helper T-cell-mediated responses in chickens."*
   * Line 64 (`Discussion`): *"In contrast, mammalian hosts exhibited CD4+ T-cell suppression, a finding that contrasts with prior reports of persistent CD8+ T-cell activation in mice."*
   * The authors interpret the exact same bar in Figure 1C as chickens in the Results and as mammals in the Discussion.

4. **Statistical Reporting Without Sample Sizes or Degrees of Freedom:**
   * The manuscript reports isolated $p$-values (`P < 0.001` in line 34, `P = 0.003` in line 40, `P < 0.01` in line 46, `r = 0.72, P < 0.001` in line 60) without stating the unit of replication ($n$ libraries vs. $n$ cells), test statistic, or multiple-testing adjustment across cell types.

---

## 4. Constructive Recommendations

1. **Separate Mouse and Chicken Datasets Completely:** Analyze and present `Mus musculus` (`GRCm39`) and `Gallus gallus` (`Gallus_gallus-6.0`) scRNA-seq libraries in separate Seurat objects, separate UMAP embeddings, and separate cell-proportion tables, further stratified by organ (lung vs. trachea) and timepoint (0, 3, 7, 14 dpi).
2. **Use Species-Appropriate Cell-Type Annotations and Gene Nomenclature:** Replace the human PBMC and pig `SingleR` references with validated mouse lung cell atlases (e.g., Tabula Muris / LungMAP) for mouse samples and chicken respiratory/immune marker panels (correctly annotating avian heterophils and `BLB1/BLB2` MHC-II genes) for chicken samples.
3. **Deposit Raw Sequencing Data and Provide Library QC Table:** Deposit all raw FASTQ files and processed count matrices in a public repository (GEO/SRA/GSA) and add a supplementary table listing every sequenced library, species, organ, dpi, treatment group, read count, and post-QC cell count.
4. **Correct Title and Figure 2 Panel Citations:** Remove the inaccurate term "coinfection" from the Title and Discussion, and reconcile all Figure 2 panel callouts (`2A–2F` vs. `2A–2H`) between the main text and figure legend.
