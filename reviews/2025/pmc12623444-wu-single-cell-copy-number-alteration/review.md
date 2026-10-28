# Review of PMC12623444 (PMID:41249471)

**Manuscript Title:** Single-cell copy number alteration signature analysis reveals masked patterns and potential biomarkers for cancer  
**Authors:** Wu C, Tao Z, Chen W, Wang N, Wang J, Shen J, Wu T, Qiu D, Diao K, Zhao X, Lu T, Zhang L, Wang W, Li X, Li X, Xiong X, Liu XS.  
**Journal / Preprint:** *Commun Biol* (2025; `PMC12623444` / `PMID:41249471` / `10.1038/s42003-025-08994-w`)  
**Calibration Study Cohort:** Cohort C — Wild Literature Sample (`C100` | Double-Blinded as `ANON_85`)  
**Overall Score:** **3.8 / 10.0** (Flawed / Overstated)
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.8/2.5 | Biology: 0.9/2.0 | Reproducibility: 1.2/2.0

---

## 1. Executive Summary & Synthesis

`ANON_85` proposes a copy number alteration (CNA) mutational signature framework in hepatocellular carcinoma (HCC) by defining 90 segment-level features across four categories (`Copy Number`, `Segment Length`, `Segment Change`, `Segment Shape`) and applying non-negative matrix factorization (`SigProfiler` / `sigminer`) to single-cell shallow whole-genome sequencing (`scDNA-seq`, $0.4\times$ depth, $1,222$ cells from $10$ HCC patients, `HRA000094`) alongside three bulk cohorts (`ICGC` $0.3\times$ sWGS, $n=160$; `PCAWG` WGS, $n=178$; `TCGA` SNP arrays, $n=371$). The authors extract seven single-cell signatures (`scSig1–scSig7`), infer their temporal ordering during tumor evolution (`scSig7` early vs. `scSig1/2` late), project the single-cell signatures back onto bulk `TCGA`/`PCAWG` samples to test overall survival, and correlate signature weights with drug sensitivity in `GDSC` cell lines.

Forensic audit of the feature engineering, phylogenetic inference, and cross-platform projection reveals three fundamental methodological flaws that invalidate the study's central biological conclusions:
1. **Conflation of Baseline Unaltered Diploid Chromosomes with a "Mutational Signature" (`scSig3`):** The feature extraction pipeline includes whole chromosomes/segments with normal diploid copy number ($\text{CN} = 2$, length $>10\text{ Mb}$ `L`, adjacent difference $\le 2$ `AA`) as active counts in the NMF input matrix (lines 136–146). Consequently, a normal diploid cell with zero CNAs produces a dominant signature (`scSig3`, described on line 63 as *"reflects characteristics of a normal genome"* and on line 106 as *"resembling a normal genome"*). Treating the absence of copy number alterations (normal diploid karyotype) as an active "CNA mutational process" violates the mathematical definition of mutational signature decomposition, where exposures must decompose somatic alterations relative to the germline/diploid baseline.
2. **Circular Phylogenetic Tree Construction from Continuous NMF Signature Proportions (`Fig. 6A`, lines 87, 154) and a Flawed Shared-Breakpoint Timing Equation (`Eq. on line 163`):** To infer the evolutionary trajectory of signatures (`Fig. 6A`), the authors constructed a Maximum Parsimony tree (`phangorn` Parsimony Ratchet) **directly from the continuous `scSig` NMF signature exposure matrix** rather than from discrete genomic copy-number states or somatic mutations (lines 87, 154: *"we first inferred phylogenetic trees inside each tumor using single-cell CNA signature value matrix with maximum parsimony"*). Building a tree from signature proportions and then claiming that signatures evolve along the branches of that tree is completely circular. Furthermore, their independent temporal metric—the average breakpoint-sharing frequency $S_j$ (`line 163`)—contains mismatched index variables ($I_{ki}$ vs. $I_{ij}$ and $I$) and conflates late clonal sweeps (high sample prevalence) and low total breakpoint count ($L_j$) with early evolutionary origin (`Fig. 6B`).
3. **Self-Contradictory Projection of Single-Cell Signatures onto Bulk SNP Arrays (`Fig. 7`, lines 76–82 vs. 97–100):** In Section `Comparison of bulk and single-cell CNA signatures` (`Fig. 5C–D`, lines 76–82), the authors demonstrate that bulk sequencing distorts single-cell signatures—for example, in patient `P04`, the bulk profile is $96.7\%$ `scSig4`, whereas the constituent single cells are predominantly `scSig3` ($46.1\%$) and `scSig7` ($26.3\%$). Yet in `Fig. 7` (lines 97–100), they project `scSig1–7` onto **bulk** `TCGA` SNP arrays and **bulk** `PCAWG` WGS to claim prognostic value for `scSig4` (`Fig. 7B`), directly contradicting their own finding that bulk `scSig4` is an aggregation artifact of single-cell heterogeneity.

---

## 2. Claim-by-Claim Audit

1. **Seven single-cell CNA signatures (`scSig1–scSig7`) capture distinct mutational processes in HCC (`Fig. 2`, lines 58–65):** `[Methodologically Flawed]`
   - Because the 90-feature table includes normal diploid segments ($\text{CN}=2$, `L >10Mb`, `AA <=2`), `scSig3` is simply the unaltered baseline diploid karyotype (or non-malignant diploid cells / low-aneuploidy cells) rather than a mutational process generating CNAs. Moreover, the Cartesian product of the four stated feature bins in Methods (line 139: $6\text{ CN states} \times 3\text{ lengths} \times 2\text{ changes} \times 3\text{ shapes} = 108\text{ combinations}$) does not equal the claimed 90 features without undocumented bin-merging or exclusion rules.

2. **`scSig7` (small CNAs) occurs early in HCC clonal evolution whereas `scSig1` and `scSig2` (large CNAs) occur late (`Fig. 6A–E`, lines 85–95):** `[Methodologically Flawed]`
   - Three lines of evidence are used to support this claim, and each is flawed:
     1. In `Fig. 6A` (lines 87, 154), the Maximum Parsimony tree was inferred directly from the `scSig` exposure matrix rather than from genomic characters, making the clustering of `scSig` along the tree circular.
     2. In `Fig. 6B` (lines 88, 163), the breakpoint-sharing score for cell $j$:
        $$S_j = \frac{1}{L_j} \sum_{i=1}^{L_j} \frac{\sum_{k=1}^M I_{ki}}{M}$$
        averages the sample-wide frequency of breakpoints present in cell $j$. If a cell has only a few ancestral truncal breakpoints ($L_j$ small, all shared across the tumor), $S_j \approx 1.0$. Conversely, a cell that retains those same ancestral breakpoints *plus* 30 private small focal deletions (`scSig7`) will have a **lower** average $S_j$ unless the focal deletions themselves are shared across most cells in the sample ($M$) due to a late clonal sweep. Thus, high $S_j$ measures clonal dominance and low private breakpoint burden, not early chronological origin.
     3. In `Fig. 6C–D`, `MEDICC2` trees built on actual copy number profiles are shown for only 3 of the 10 patients (`P02`, `P08`, `P09`), and their topologies conflict with the `scSig` parsimony trees (`Fig. S10`).

3. **Bulk tissue masks single-cell CNA signatures (`Fig. 5C–D`, lines 76–82), yet `scSig1`, `scSig3`, and `scSig4` stratified on bulk `TCGA` SNP arrays and `PCAWG` WGS predict patient survival (`Fig. 7B`, `Fig. S14`, lines 97–100):** `[Overstated]`
   - If bulk profiles distort single-cell signature compositions (e.g., turning a mixture of `scSig3` and `scSig7` cells into $96.7\%$ `scSig4` in `P04`, line 80), fitting `scSig` weights onto bulk `TCGA` SNP array data does not measure single-cell signature activity. Furthermore, line 99 states that *"Multivariable Cox regression identified scSig1 as the only independent prognostic factor (Fig. S14A)"*, yet the main text figure (`Fig. 7B`) highlights `scSig4`, which failed multivariable significance.

4. **`scSig` exposures in bulk `GDSC` cell lines predict sensitivity and resistance to targeted therapies (`Fig. 7C–D`, lines 101–103):** `[Fragile]`
   - The analysis fits HCC single-cell signatures derived from $0.4\times$ `scDNA-seq` of 10 primary tumors onto bulk `GDSC` cell line copy number profiles (`line 101`) and reports unadjusted marginal Spearman correlations ($|R| \approx 0.3\text{--}0.4$) across hundreds of screened compounds without false discovery rate (FDR) correction or adjustment for overall chromosomal instability / ploidy.

---

## 3. Technical & Methodological Critique

### 3.1. Inclusion of Unaltered Diploid Segments (`CN = 2`) in NMF Feature Counts
- In somatic mutational signature analysis (e.g., SNV or structural variant signatures), NMF decomposes a count matrix $V \approx WH$ of **somatic alterations** relative to a normal reference genome; a normal diploid cell has $\mathbf{v} = \mathbf{0}$. In `ANON_85` (`Methods`, lines 136–146), the authors segmented the genome into $500\text{ kb}$ bins (`variable_500000_100_bwa`) and counted every contiguous segment across the 22 autosomes and sex chromosomes, **including normal diploid segments ($\text{CN} = 2$)**. As a result:
  - A completely normal diploid cell has 23–24 whole-chromosome segments of state `CN = 2`, length `L (>10 Mb)`, change `AA (<=2)`, and shape `OT`, generating a strong artificial "signature" (`scSig3`).
  - Any genuine focal amplification or deletion that splits a normal diploid chromosome into three segments (`diploid` – `CNA` – `diploid`) simultaneously **increases** the count of `CN = 2` flanking segments while decreasing their length from `L` to `M` or `S`. This couples the count of unaltered diploid background segments to the number of focal CNAs, confounding the NMF basis vectors (`Fig. S1`).

### 3.2. Broken Mathematical Notation in the Shared Breakpoint Formula (Line 163)
- On lines 163–167, the shared breakpoint frequency is written as:
  $$S_j = \frac{1}{L_j} \sum_{i=1}^{L_j} \frac{\sum_{k=1}^M I_{ki}}{M}$$
  *"where $S_j$ is the frequency of shared break point of cell $j$ in the sample, $M$ is the number of cells in the sample, $L_j$ is the number of shared breakpoints in cell $j$, and $I_{ij}$ represents the existence of the shared breakpoint $I$ in cell $j$."*
  1. The summand uses $I_{ki}$ (existence of breakpoint $i$ in cell $k$), whereas the definition writes $I_{ij}$ and refers to breakpoint $I$ (capital $I$, the same symbol used for the indicator function) instead of breakpoint $i$.
  2. If $L_j$ is defined as *"the number of shared breakpoints in cell $j$"* (excluding private breakpoints unique to cell $j$), then dividing only by shared breakpoints $L_j$ ignores how many private derived breakpoints cell $j$ has accumulated since diverging from the common ancestor.

### 3.3. Improper Application of Maximum Parsimony (`phangorn`) to Continuous NMF Weights
- On lines 154–156, the authors state: *"A random tree was initially generated (`ape` R package), and the evolutionary trees were inferred using the Parsimony Ratchet method (`phangorn` R package) based on the single-cell CNA signature exposure matrix."* Maximum Parsimony (`phangorn::pratchet`) is a discrete character-state phylogenetic algorithm designed for nucleotide, amino acid, or discrete morphological/copy-number matrices (`phyDat` objects). Passing continuous or discretized NMF exposure proportions as phylogenetic characters violates character independence (since relative signature exposures sum to 1 or reflect composite NMF loadings) and renders any downstream observation that signatures map onto clades of that tree tautological.

---

## 4. Actionable Recommendations

1. **Exclude Unaltered Diploid Baseline Segments ($\text{CN} = 2$) from the CNA Feature Matrix:**
   - Re-extract CNA signatures after filtering out baseline diploid chromosome arms/segments ($\text{CN} = 2$ with zero copy change from baseline ploidy) so that the NMF matrix $V$ counts only somatic copy number alterations, eliminating the artifactual "normal genome" signature (`scSig3`).
2. **Document the Exact Mapping of the 90 Features:**
   - Explicitly specify which 18 combinations of the $6 \times 3 \times 2 \times 3 = 108$ Cartesian product bins (`CN` $\times$ `Length` $\times$ `Change` $\times$ `Shape`) were merged or omitted to arrive at 90 features.
3. **Infer Phylogenies Strictly from Genomic Copy Number Profiles (`MEDICC2`) Across All 10 Patients:**
   - Remove `Fig. 6A` (the circular parsimony tree built from NMF signature weights) and the flawed $S_j$ metric (`Fig. 6B`). Instead, reconstruct integer copy-number phylogenies across all 10 tumors using `MEDICC2` (expanding `Fig. 6C–D` from 3 patients to all 10 patients) and map the somatic CNA events inferred along each internal and terminal branch (`truncal` vs. `subclonal` branch mutations) onto the signature basis.
