# Review of ANON_32

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.6 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.8 / 8.0**  
* **Score Breakdown:** Methodological Rigor: 2.8/3.5 | Claim-Evidence Alignment: 2.0/2.5 | Biological Plausibility: 2.0/2.0 | Reproducibility: 1.8/2.0  
* **Score Breakdown (Compact):** Rigor: 2.8/3.5 | Claims: 2.0/2.5 | Biology: 2.0/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript constructs a single-cell transcriptional atlas of the adult human lung by profiling 75,066 cells (65,662 via 10x Chromium and 9,404 via Smart-Seq2 [SS2]) across proximal, medial, and distal lung tissue compartments and matched peripheral blood from $N=3$ surgical resection donors, supplemented by bulk RNA-seq of 21 FACS-purified circulating immune populations and comparison to ~35,522 mouse lung cells (from Tabula Muris Senis and lineage-labeled *Axin2-Cre-ERT2* and *Tbx4-LME-Cre* mice). Using compartment-balanced MACS/FACS enrichment, subject-stratified iterative Louvain clustering in Seurat v2.3, and orthogonal spatial validation via single-molecule FISH (RNAscope smFISH) and immunohistochemistry in independent donors, the authors define 58 molecular cell populations—capturing 41 of 45 canonical histological lung cell types and identifying 14 novel populations or states across epithelial (e.g., signaling AT2-s, proximal basal Bas-px), endothelial (bronchial Bro1/Bro2, capillary aerocytes Cap-a and general Cap), stromal (alveolar vs. adventitial fibroblasts, fibromyocytes, lipofibroblasts), and immune (IGSF21+, EREG+, and TREM2+ dendritic cells) compartments. Raw and processed datasets are deposited in controlled-access and open repositories (EGA `EGAS00001004344`, Synapse `syn21041850`, NCBI SRA `PRJNA632939`, re-annotations of `GSE122960` and `GSE130148`, and GitHub `[GITHUB_REPO_REDACTED]`).

As a foundational organ atlas, the experimental design—combining compartment balancing across five orders of magnitude in cell abundance, dual-platform scRNA-seq (high-throughput 10x plus deep full-length SS2), bulk immune reference profiling, and extensive smFISH anatomical localization—is exceptionally thorough. The primary statistical and methodological limitations arise in the downstream cross-species evolutionary comparisons and cell-level differential expression tests: (1) applying cell-level `MAST` tests ($p < 10^{-5}$) without subject-level pseudobulk aggregation across only $N=3$ human donors treats thousands of cells from the same individual as independent replicates, inflating false discovery rates; and (2) the claim that mice "lack 17 (29%) of the 58 human lung types" and that "just 6% of expressed genes had fully conserved expression patterns (Type 0)" is heavily confounded by anatomical sampling asymmetry (mouse lungs lack pseudostratified intrapulmonary bronchi and bronchial circulation, and the mouse dataset had $\sim 2\times$ fewer cells and lacked matched compartment-depletion protocols) and by the brittle compound binarization rule across dozens of cell types, where a single threshold crossing in any one cluster reclassifies a conserved gene as diverged.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Identification and anatomical localization of 58 transcriptionally distinct cell populations in the adult human lung, including 41 of 45 canonical cell types and 14 novel populations/states: [Well Supported].**  
  The combination of MACS/FACS compartment balancing, iterative within-compartment clustering across both 10x and SS2 platforms, bulk RNA-seq correlation for 21 FACS-sorted immune subsets (Extended Data Figure 2), and systematic smFISH/immunohistochemistry validation in at least two independent donors per marker panel (Figures 1–2, Extended Data Figures 3–5) provides strong orthogonal validation of the primary atlas deliverable.

* **Identification of optimal cell-type marker panels (MCC-ranked), cell-selective transcription factors (such as *MYRF* in AT1 cells and *TBX5* in pericytes), immune residency signatures, and cellular expression maps of Mendelian/GWAS lung disease genes and viral entry receptors: [Well Supported].**  
  The Matthews Correlation Coefficient (MCC) marker optimization (Extended Data Figure 5b) demonstrates that ~200 genes saturate classification accuracy across all 58 types, and key transcription factor and disease-gene assignments (*MYRF* in AT1, *TBX5* and *KCNK3* in pericytes, *ACVRL1* in capillaries, *SERPINA1* and *HHIP* in AT2 cells) are directly confirmed in situ by smFISH (Extended Data Figures 5c–d, 8c–e).

* **Mice lack 17 (29%) of the 58 human lung molecular cell types, including 12 of the 14 newly discovered types, reflecting major evolutionary diversification of cell types in the human lineage: [Overstated].**  
  While genuine anatomical differences exist between human and mouse lungs (e.g., mouse intrapulmonary airways lack cartilage, submucosal glands, and a separate systemic bronchial vasculature), attributing the absence of 17 clusters in the mouse scRNA-seq dataset to evolutionary gain/loss is confounded by technical and sampling asymmetries: only one human subject (Patient 3) contributed proximal bronchial tissue (`Proximal 3`), several human clusters are transient proliferative/differentiating states (Bas-p, Bas-d, NK/T-p) or capillary intermediates (Cap-i1, Cap-i2) or single-donor clusters (clusters 45 and 56), and the ~35,000 mouse cells from Tabula Muris Senis were dissociated without elastase (human lungs used Liberase DL + elastase; mouse lungs used Liberase DL alone) and without identical MACS depletion gates.

* **Only ~6% of expressed genes have conserved cellular expression patterns (Type 0) between human and mouse lung, while 94% undergo evolutionary gain/loss, expansion/contraction, or cell-type switching: [Methodologically Flawed].**  
  To classify genes into Types 0–3, the authors binarize expression (1 vs. 0) in each of $K \approx 40$ homologous cell types using a compound cutoff (median non-zero expression and percent non-zero cells exceeding the global median $\pm 2\text{ SD}$) and require *every single element* of the difference vector $V = (a - b) + 2ab$ across all $\sim 40$ cell types to agree ($V_k \in \{0, 2\}\ \forall k$) to be called "Conserved (Type 0)." Under simple probability theory, even if every cell type has a $95\%$ probability of concordant binary calling between species, requiring simultaneous binary concordance across 40 cell types yields $0.95^{40} = 12.8\%$ Type 0 conservation purely from independent boundary noise and dropout/capture differences between NextSeq 500 (mouse) and NovaSeq 6000 (human) SS2 libraries. Meanwhile, targeted examples validated by smFISH (such as the *HHIP* and *SERPINA1* switch between mouse stromal cells and human AT2 cells, and *HOPX* expansion to human AT2 cells in Figure 4c–d) are well supported individually.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Replace Hard Multi-Cluster Binarization with a Probabilistic Model for Cross-Species Expression Conservation
* **WHY:** Requiring exact binary (0/1) identity across ~40 homologous cell types simultaneously guarantees that sampling variance in small clusters ($n \ge 5$ cells cutoff in Methods) and arbitrary threshold crossings classify $>90\%$ of genes as evolutionarily diverged (Types 1–3), which is why the 602 "Type 0" genes are almost exclusively restricted to genes expressed in just 1 cell type ($67\%$) or all cell types ($33\%$, Extended Data Figure 12h).
* **WHAT:** Re-estimate the proportion of evolutionarily conserved versus diverged genes using a continuous cross-species specificity correlation or a hierarchical Bayesian mixture model that accounts for within-species donor variance and cluster sample size.
* **HOW:** For each orthologous gene pair, compute the cosine similarity or Pearson correlation of log-normalized pseudobulk expression across the homologous cell types (weighted by cell count and estimated measurement error from the $N=3$ human donors and mouse replicates), and compare the observed cross-species similarity against a null distribution generated by permuting donor labels within species (or comparing 3-month vs. 24-month mice in Extended Data Figure 11e using the exact same Type 0–3 binary pipeline as a technical noise baseline).

#### 2. Account for Donor-Level Pseudoreplication and Anatomical Region Sampling
* **WHY:** Only $N=3$ human donors were profiled, with uneven regional sampling (`Proximal 3` came solely from Patient 3; `Medial 2` from Patients 2 and 3; Patient 1 had mild emphysema and only distal samples), and `MAST` was run at the single-cell level ($n=100$ or $500$ downsampled cells) without donor random effects, which treats cells from the same patient as independent biological replicates.
* **WHAT:** Add donor-level pseudobulk differential expression p-values and explicitly annotate which of the 58 clusters were detected across all 3 donors versus driven by the single proximal bronchial sample (`P3`).
* **HOW:** Aggregate counts by donor $\times$ cluster (`DESeq2` or `edgeR` pseudobulk, or `MAST` with a random effect `(1|Subject)`), and include a summary column in Supplementary Table 2 indicating the donor and regional (Proximal/Medial/Distal) replicability of each of the 58 clusters.

#### 3. Editorial and Methodological Cleanup
* **WHY:** Several minor typographical errors appear in the text and figure legends.
* **WHAT & HOW:**
  1. Line 29: Fix doubled preposition *"by by bulk RNA sequencing"* to *"by bulk RNA sequencing"*.
  2. Line 87 (Figure 4c, d legend): Fix *"Staining repreated on 3 subjects"* to *"Staining repeated on 3 subjects"*.
  3. Line 118 (Methods): Clarify why Patient 3's medial sample is labeled *"(‘Medial 2’)"* instead of *"(‘Medial 3’)"*.
  4. Bioinformatic Methods (line 59): Fix *"plus/minus two standard decisions"* to *"plus/minus two standard deviations"*.
  5. Extended Data Figure 4b legend (line 89): Fix *"Frfr4"* to *"Fgfr4"*.
