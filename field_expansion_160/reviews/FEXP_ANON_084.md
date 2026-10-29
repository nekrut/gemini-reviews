# Review of FEXP_ANON_084

**Overall Score:** **4.3 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **3.3 / 8.0**  
* **Score Breakdown:** Rigor: 1.2/3.5 | Claims: 1.0/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.0/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Role / Domain:** Computational biology / deep learning algorithm paper proposing `scCCTR`, a pseudo-labeled iterative consensus and Transformer-based clustering method for scRNA-seq data.
* **Blinded Document Assessment:** Although framed as a methodological machine learning paper with a public GitHub link, forensic audit reveals severe mathematical and methodological flaws: a reversed stopping criterion in Equation (5), dimensional impossibilities in the residual encoder (Eq. 1) and Transformer FFN (Eq. 13), circular cluster-specific autoencoder reconstruction that is improperly fed into downstream differential gene expression testing, a mathematically inconsistent Fowlkes–Mallows Index ($\text{FMI} = 0.4$ when $\text{ARI} = 0.786$), and conflicting dataset counts across sections (16 vs. 14 vs. 12 vs. 8 datasets).

---

## 2. Executive Summary & Editorial Verdict

This paper introduces `scCCTR`, an unsupervised single-cell clustering pipeline framed as a "semi-supervised" classification model. In the first module ("iterative selection"), a residual autoencoder reduces dimensionality, K-means produces initial clusters $C^{(t)}$, and a consensus matrix $M^{(T)}$ across $T$ iterations is hierarchically clustered into $C'^{(T)}$. For each cluster $j = 1, \dots, k$, the cells closest to the cluster centroid $\mu_j$ are selected as a "core subset" $S_j^{(T)}$, reconstructed by a cluster-specific sub-autoencoder, and reinserted into the input matrix $H$. In the second module, a Transformer classifier is trained on the reconstructed core cells using their consensus cluster assignments as pseudo-labels and then used to predict cluster labels for all cells in $\hat{H}^*$. The method is compared against eight baselines (`Scanpy`, `SC3`, `Seurat`, `SIMLR`, `scGNN`, `scDeepCluster`, `scDSC`, `cellVGAE`) and applied to trajectory and differential expression analyses on human embryo (`E-MTAB-3929`) and mouse lymph node (`E-MTAB-10434`) datasets.

**Editorial Verdict: Reject (Flawed / Overstated).** While iterative pseudo-labeling and consensus clustering are reasonable heuristics, the manuscript contains fundamental methodological and mathematical defects that invalidate several core claims:
1. **Circular Cluster-Specific Reconstruction and Double-Dipping in Downstream DEG Analysis:** In the data reconstruction phase (Equations 7–9), `scCCTR` trains $k$ separate autoencoders—one for each putative cluster—and overwrites the gene expression matrix with these cluster-specific reconstructions. This procedure artificially collapses within-cluster variance toward $k$ separate low-rank manifolds. The authors then run differential gene expression (volcano plot with adjusted $p < 0.05$, Figure 6c–d) and trajectory inference directly on the `scCCTR`-reconstructed expression matrix rather than the observed counts, constituting textbook statistical double-dipping.
2. **Mathematical Errors in the Model Equations:** The convergence criterion in Equation (5), $|\text{ARI}(C'^{(T)}, C'^{(T-1)})| < \delta$, terminates when consecutive consensus partitions have near-zero similarity rather than when they converge ($\text{ARI} \to 1$); the residual encoder in Equation (1), $z_i^{(l)} = f(W^{(l)} z_i^{(l-1)} + b^{(l)}) + z_i^{(l-1)}$, is dimensionally invalid whenever layer $l$ reduces dimensionality; and the FFN weight matrix $W_2$ in Equation (13) has transposed dimensions ($\mathbb{R}^{d_{\text{model}} \times d_f}$ instead of $\mathbb{R}^{d_f \times d_{\text{model}}}$).
3. **Internal Contradictions in Benchmark Numbers:** The number of benchmark datasets is stated as **16** in the Introduction and Table 1, **14** in the Results header (lines 174, 179), **12** in Figure 2 and line 181, and **8** in the Conclusion (line 35). Table 1 also mislabels the `Human embryos` dataset (`E-MTAB-3929`) as `Mouse`, and line 181 reports an average $\text{FMI} = 0.4$ alongside $\text{ARI} = 0.786$, which is mathematically impossible because the Fowlkes–Mallows Index is bounded above ARI for standard contingency tables.

### Specific Conclusions and Assessment of Support

* **Cluster-specific sub-autoencoder reconstruction improves clustering precision and t-SNE separation: [Methodologically Flawed].**  
  Fitting $k$ independent autoencoders to each K-means/consensus cluster and reinserting the reconstructed values into $H$ (lines 89–93) bakes the preliminary cluster assignments directly into the gene expression matrix. Any subsequent embedding (t-SNE in Figure 3), internal cluster validity metric (`DBI` in Figure 2), or classifier trained on $\hat{H}^*$ reflects this artificial shrinkage of intra-cluster variance rather than genuine biological separation.
* **Superior ARI (0.786), NMI (0.814), ACC (0.832), and FMI (0.400) across the benchmark suite: [Fragile].**  
  First, it is unclear why 16 datasets are listed in Table 1, 14 are discussed in lines 174/179/181, only 12 are plotted in Figure 2, and 8 are claimed in the Conclusion. Second, reporting $\text{FMI} = 0.4$ when $\text{ARI} = 0.786$ and $\text{ACC} = 0.832$ is a mathematical contradiction, since $\text{FMI} \ge \text{ARI}$ in almost all nontrivial partitions. Third, hyperparameter tuning ($\alpha$ and $\beta$ in Fig. 4, plus dimensionality, iterations, and attention heads in the dropout study) was performed directly on the test datasets ("we applied the optimal parameter configurations for each method on each dataset and reported their best performance," line 179).
* **Transformer multi-head self-attention captures long-range feature (gene–gene) interactions (Contribution 3): [Overstated].**  
  In Equations (10)–(11), the input matrix $\tilde{X} \in \mathbb{R}^{N' \times d_{\text{model}}}$ is projected to $Q, K, V \in \mathbb{R}^{N' \times d_k}$, so the attention matrix $\text{softmax}(QK^T/\sqrt{d_k}) \in \mathbb{R}^{N' \times N'}$ computes **cell-to-cell** attention across samples in the batch rather than **gene-to-gene** (feature) interactions as claimed in Contribution 3 (line 28).
* **Differential gene expression and GO enrichment between `Naive_LN_LEC` and `EV_LN_LEC` using `scCCTR`-reconstructed expression data (Fig. 6c–d): [Methodologically Flawed].**  
  Performing differential expression testing (`|log2FC| > 1`, `p_val_adj < 0.05`, line 237) on autoencoder-reconstructed expression values—especially when subsets of cells were reconstructed by separate sub-autoencoders—violates the independence and distributional assumptions of DEG tests and fabricates denoised fold-changes.

---

## 3. Forensic Defect Inventory

1. **Inverted Convergence Criterion in Equation (5) (Pillar 3 & Pillar 7):**
   * **Location:** Methods ("Consensus clustering phase", lines 80–82, Equation 5).
   * **Defect:** The authors write: *"The process terminates when: (5) $|\text{ARI}(C'^{(T)}, C'^{(T-1)})| < \delta$. If the ARI difference between the current and previous consensus clustering results is smaller than $\delta$, the clustering result is considered stable."* The Adjusted Rand Index between two consecutive partitions $C'^{(T)}$ and $C'^{(T-1)}$ equals $1.0$ when the two partitions are identical and $0.0$ when they are independent. Thus, $|\text{ARI}(C'^{(T)}, C'^{(T-1)})| < \delta$ (for small $\delta > 0$) triggers termination only when consecutive iterations completely disagree, the exact opposite of convergence ($1 - \text{ARI}(C'^{(T)}, C'^{(T-1)}) < \delta$).
2. **Dimensional Impossibilities in Equations (1), (13), and (15) (Pillar 3 & Pillar 7):**
   * **Location:** Methods (Equation 1, line 53; Equation 13, line 108; Equation 15, line 112).
   * **Defect:**
     * **Equation (1):** $z_i^{(l)} = f(W^{(l)} z_i^{(l-1)} + b^{(l)}) + z_i^{(l-1)}$ adds the input vector $z_i^{(l-1)} \in \mathbb{R}^{d_{l-1}}$ directly to the layer output $f(\cdot) \in \mathbb{R}^{d_l}$. In a dimensionality-reducing encoder where $d_l < d_{l-1}$, vector addition is undefined without a linear projection $P^{(l)} z_i^{(l-1)}$.
     * **Equation (13):** $\text{FNN}(Z) = \text{ReLU}(Z W_1 + b_1) W_2 + b_2$ specifies $W_1 \in \mathbb{R}^{d_{\text{model}} \times d_f}$ and $W_2 \in \mathbb{R}^{d_{\text{model}} \times d_f}$ (and then writes $d_{ff}$ in the same sentence). Multiplying $\text{ReLU}(Z W_1 + b_1) \in \mathbb{R}^{N \times d_f}$ by $W_2$ requires $W_2 \in \mathbb{R}^{d_f \times d_{\text{model}}}$.
     * **Equation (15):** $L_{CE} = -\sum_{i=1}^{N_K} y_i \log \hat{y}_i$ omits the summation over the $C$ classes ($-\sum_{i=1}^{N_K} \sum_{c=1}^C y_{ic} \log \hat{y}_{ic}$).
3. **Circular Data Reconstruction by Cluster-Specific Sub-Autoencoders and Downstream DEG Double-Dipping (Pillar 2 & Pillar 3):**
   * **Location:** Methods ("Data reconstruction phase", lines 89–93) and Experimental results ("Downstream analysis", line 237, Fig. 6c–d).
   * **Defect:** Training $k$ independent autoencoders on each cluster's core cells $H'_j$ and inserting the reconstructed profiles back into $H$ forces cells assigned to cluster $j$ onto cluster $j$'s autoencoder subspace. Subsequently using this reconstructed matrix $\hat{H}^*$ to compute volcano plots and adjusted $p$-values between `Naive_LN_LEC` and `EV_LN_LEC` (line 237) constitutes circular post-selection inference.
4. **Mathematically Impossible Fowlkes–Mallows Index ($\text{FMI} = 0.4$) Relative to $\text{ARI} = 0.786$ (Pillar 4 & Pillar 7):**
   * **Location:** Experimental results ("Analysis of clustering results", line 181).
   * **Defect:** The text reports that `scCCTR` achieved average scores of $\text{ARI} = 0.786$, $\text{NMI} = 0.814$, $\text{ACC} = 0.832$, and $\text{FMI} = 0.4$. Because FMI is the geometric mean of pairwise precision and recall without chance adjustment while ARI is the chance-adjusted harmonic/arithmetic counterpart, $\text{FMI} > \text{ARI}$ holds across standard clustering partitions (an ARI of $0.786$ corresponds to $\text{FMI} \approx 0.83\text{--}0.86$). An average $\text{FMI}$ of $0.4$ is incompatible with $\text{ARI} = 0.786$.
5. **Contradictory Dataset Counts (16 vs. 14 vs. 12 vs. 8) and Species Mislabeling in Table 1 (Pillar 7):**
   * **Location:** Introduction (line 30: 16 datasets), Table 1 (line 127: 16 datasets), Results (lines 174, 179, 181: 14 datasets vs. 12 datasets), Figure 2 (12 datasets), and Conclusion (line 35 of chunk 2: 8 datasets).
   * **Defect:** Two datasets (`Human embryos` and `Mouse lymph node`) are used only for downstream trajectory/DEG visualization, leaving 14 datasets, of which only 12 appear in Figure 2 (`Mouse heart` and `5K PBMCs` are omitted from Fig. 2 without explanation), and the Conclusion claims 8 datasets. In Table 1 (line 144), `Human embryos` (`E-MTAB-3929`) is erroneously listed under `Species: Mouse`, and the `Biase` dataset (`GSE57249`) is misspelled as `Baise` throughout.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.2** | **3.5** | Cluster-specific sub-autoencoder reconstruction creates circular cluster separation and invalidates downstream DEG $p$-values; broken convergence inequality in Eq. (5); dimension errors in Eqs. (1) and (13); test-set hyperparameter tuning. |
| **2. Claim-to-Evidence Alignment** | **1.0** | **2.5** | Claims of "semi-supervised learning" (actually unsupervised pseudo-labeling) and "long-range feature interactions" (actually cell-to-cell attention across the batch) overstate the architecture; $\text{FMI} = 0.4$ contradicts $\text{ARI} = 0.786$. |
| **3. Data Integrity & Biological Plausibility** | **1.1** | **2.0** | Public datasets are authentic, but running DEG testing and GO enrichment on cluster-specific autoencoder-imputed values (Fig. 6c–d) inflates biological false positives; `Human embryos` is mislabeled as `Mouse` in Table 1. |
| **4. Reproducibility & Data Integrity** | **1.0** | **2.0** | A GitHub URL (`scCCTR`) and public accessions are provided, but dataset counts conflict across every section (16 vs. 14 vs. 12 vs. 8) and the mathematical equations in the text do not match a valid implementation. |
| **Scientific Core Score** | **3.3** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **4.3** | **10.0** | **Flawed / Overstated** |

---

### 5. Constructive and Doable Suggestions for Improvement

1. **Perform Downstream DEG Analysis Strictly on Unimputed Log-Normalized Counts:** Re-compute the `Naive_LN_LEC` vs. `EV_LN_LEC` differential expression volcano plot (Fig. 6c) and GO enrichment (Fig. 6d) using the original log-normalized count matrix rather than the `scCCTR` sub-autoencoder reconstructed matrix $\hat{H}^*$. Similarly, evaluate `DBI` and `Graph cLISI` on a shared, non-cluster-conditioned representation to avoid circularity.
2. **Correct Equations (1), (5), (13), and (15):**
   * Replace Equation (5) with $1 - \text{ARI}(C'^{(T)}, C'^{(T-1)}) < \delta$ (or $|\text{ARI}(C'^{(T)}, C'^{(T-1)}) - 1| < \delta$).
   * Include the linear residual projection matrix in Equation (1) when $d_l \ne d_{l-1}$.
   * Fix $W_2 \in \mathbb{R}^{d_f \times d_{\text{model}}}$ in Equation (13) and include the class summation in Equation (15).
3. **Reconcile Dataset Counts, Table 1 Metadata, and the FMI Metric:** Clarify across the Abstract, Introduction, Results, Figure 2, and Conclusion exactly how many datasets were evaluated in each experiment, include all 16 datasets in Figure 2, fix `Human embryos` species from `Mouse` to `Human` and `Baise` to `Biase` in Table 1, and recompute the mean FMI score in line 181.
4. **Separate Hyperparameter Tuning from Benchmark Evaluation:** Fix default hyperparameters ($\alpha, \beta$, learning rate, number of heads) on a held-out development set rather than reporting the best parameter configuration per test dataset.
