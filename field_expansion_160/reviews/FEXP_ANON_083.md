# Review of FEXP_ANON_083

**Overall Score:** **6.7 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **5.2 / 8.0**  
* **Score Breakdown:** Rigor: 2.1/3.5 | Claims: 1.7/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.5/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Role / Domain:** Computational biology / machine learning methodology paper introducing a deep graph clustering algorithm (`DGCSG`) for single-cell RNA-seq cell-type clustering.
* **Blinded Document Assessment:** Well-structured algorithmic bioinformatics manuscript with public GitHub code, 14 benchmark datasets, 16 comparison baselines, sequencing-depth and dropout robustness experiments, and ablation analyses, tempered by several mathematical formulation ambiguities (dimensionality of the relaxed spectral partition matrix $S$ in intermediate GATE layers and equation typos in attention and KL target distributions), reliance on oracle cluster counts $K$, and seed-level statistical testing without multiple-comparison adjustment.

---

## 2. Executive Summary & Editorial Verdict

This manuscript presents Differentiable Graph Clustering with Structural Grouping (`DGCSG`), a dual-channel deep clustering framework for scRNA-seq data that couples a multi-layer Autoencoder (AE) with a Graph Attention Autoencoder (GATE). First, a cell–cell similarity graph is built from Pearson correlations refined via Network Enhancement (`Wang et al. 2018`). Second, node representations $Z^{(r)}$ from the AE are injected layer-by-layer into the GATE via $U^{(r)} = Z^{(r)} + H^{(r)}$. Third, to encourage cluster-aware message passing, the authors relax the discrete $K$-way normalized cut problem via Ky Fan's trace maximization theorem into a layer-wise differentiable loss $L_{SG}(l)$ combining an orthogonality penalty $\|\frac{1}{N}S^T S - I\|_F^2$ with a normalized Rayleigh trace term $-\frac{1}{NK}\text{tr}(S^T D^{-1/2} A D^{-1/2} S)$. Finally, decoupled Student-$t$ self-supervised KL losses ($L_{KL_z}$ and $L_{KL_h}$) optimize the AE and GATE embeddings. Across 14 public scRNA-seq datasets and 16 baselines, `DGCSG` achieves the top average NMI and ARI on 12/14 and 13/14 datasets, respectively, and maintains strong performance under sequencing-depth downsampling (`heart10k`, `neuron10k`) and simulated dropout.

**Editorial Verdict: Major Revision (Mixed / Salvageable).** The empirical benchmarking is broad, ablation experiments verify that each loss component contributes positively on average, and the source code is publicly available (`[GITHUB_REPO_REDACTED]`). However, three methodological and mathematical issues must be addressed before the work can be considered fully rigorous: (1) there is an unresolved dimensional and conceptual gap between the $N \times K$ relaxed spectral partition matrix $E$ in Equation (6) and the $N \times d_l$ pre-activation GATE hidden representation $S = \text{att} \cdot W_{\text{gat}}^{(l)} U^{(l-1)}$ in Equations (10)–(12), alongside algebraic typos in Equations (8) and (17); (2) hyperparameters ($\alpha, \beta$) and the exact number of ground-truth clusters $K$ appear to be fixed using oracle test-set information across the 14 benchmarks; and (3) statistical significance in Section 3.5 is evaluated via unadjusted one-sided paired $t$-tests across 10 random initialization seeds per dataset rather than dataset-level non-parametric tests (e.g., Wilcoxon signed-rank test across the 14 datasets).

### Specific Conclusions and Assessment of Support

* **Spectral relaxation of $K$-way normalized cuts into a layer-wise differentiable GATE objective $L_{SG}$: [Moderately Supported].**  
  While the derivation from discrete $K$-way normalized cut (Eq. 2) to Ky Fan trace maximization (Eq. 6) for an $N \times K$ soft partition matrix $E$ is mathematically standard, substituting the $l$-th layer pre-activation embedding $S = \text{att} \cdot W_{\text{gat}}^{(l)} U^{(l-1)} \in \mathbb{R}^{N \times d_l}$ directly for $E \in \mathbb{R}^{N \times K}$ in Equations (11)–(12) changes the rank of the subspace from $K$ to the hidden layer width $d_l$ unless $d_l = K$ at every layer. Moreover, because $S$ is the post-attention linear combination of neighbor features rather than an explicit term inside the attention logit calculation (Eq. 8), the claim that $L_{SG}$ directly *"allocates more attention scores to nodes in the same graph cluster"* is indirect (acting only via backpropagated gradients through $\text{att}$).
* **Superior clustering accuracy (ARI and NMI) of DGCSG over 16 baselines across 14 scRNA-seq benchmarks: [Well Supported].**  
  The benchmark suite spans diverse platforms, tissues, and sample sizes, and includes 16 relevant deep and graph clustering competitors (`scGAC`, `scDFC`, `scDFN`, `scLEGA`, `scSMD`, `SCGC`, etc.) averaged over 10 runs. Caveats are that `DGCSG` assumes the true cluster count $K$ is known a priori and tunes $\alpha, \beta$ across the benchmark suite.
* **Robustness to reduced sequencing depth (`heart10k`, `neuron10k`) and high dropout rates (up to 47.96%): [Well Supported].**  
  Downsampling reads on two 10k-cell datasets and varying dropout rates on simulated datasets provide controlled stress tests where `DGCSG` consistently degrades more gracefully than competing GNN baselines (`scDFC`, `scLEGA`).
* **Downstream utility for trajectory inference (`binary_tree_8`) and marker gene recovery (`Muraro`): [Moderately Supported].**  
  Trajectory metrics (HIM, F1 branches, F1 milestones) are evaluated on a single synthetic dataset (`binary_tree_8`) rather than real developmental scRNA-seq data, and marker gene analysis on `Muraro` relies on unadjusted Wilcoxon tests across predicted clusters (where rare epsilon cells, $n = 3$, are missed).

---

## 3. Forensic Defect Inventory

1. **Dimensional Mismatch Between Spectral Partition $E \in \mathbb{R}^{N \times K}$ and Layer Embedding $S \in \mathbb{R}^{N \times d_l}$ (Pillar 3 & Pillar 7):**
   * **Location:** Section 2.1 (Equation 6, lines 53–55) and Section 2.2 (Equations 9–12, lines 62–66).
   * **Defect:** In Equation (6), $E = D^{1/2}F(F^T D F)^{-1/2} \in \mathbb{R}^{N \times K}$ has $K$ columns corresponding to the $K$ target clusters. In Section 2.2, the authors set $S = \text{att} \cdot W_{\text{gat}}^{(l)} U^{(l-1)}$ at every layer $l = 1, \dots, L$ and substitute $S$ into Equation (12): $L_{SG}(l) = \|\frac{1}{N}S^T S - I\|_F^2 - \frac{1}{NK}\text{tr}(S^T D^{-1/2}A D^{-1/2}S)$. Because $U^{(r)} = Z^{(r)} + H^{(r)}$ requires the AE and GATE layers to share hidden dimension $d_l$ (typically $d_l \gg K$, e.g., $256$ or $64$), $S^T S$ is a $d_l \times d_l$ matrix rather than $K \times K$, meaning Equation (12) actually enforces orthogonality across $d_l$ latent feature dimensions while dividing the trace by $NK$ instead of $N d_l$.
2. **Algebraic Typos in Equations (8), (16), and (17) (Pillar 7):**
   * **Location:** Section 2.2 (Equation 8, line 62) and Section 2.3 (Equations 16–17, lines 79–81).
   * **Defect:**
     * In Equation (8), the denominator of the attention softmax sums over $k \in N_i$, but the summand is written with index $j$ instead of $k$: $\sum_{k \in N_i} \exp(\text{LeakyReLU}(a^T(W_{\text{gat}} h_i || W_{\text{gat}} h_j)))$ instead of $W_{\text{gat}} h_k$.
     * In Equation (17), the numerator of the target distribution $p_{ij}^z$ is missing the square on $q_{ij}$: it reads $p_{ij}^z = \frac{q_{ij} / \sum_{i=1}^N q_{ij}}{\sum_{k=1}^K (q_{ik}^2 / \sum_{i=1}^N q_{ik})}$. Without squaring $q_{ij}$ in the numerator (`q_{ij}^2`), $\sum_{j=1}^K p_{ij}^z \ne 1$, which invalidates the Kullback–Leibler divergence $KL(P_z || Q_z)$ in Equation (18) and contradicts the text stating *"by quadratically operating the soft cluster assignments $Q_z$ and $Q_h$."*
     * In Equations (16)–(17), only $q_{ij}$ (for $Z^{(L)}$) and $p_{ij}^z$ are explicitly defined; the authors never state whether $Q_h$ computes Student-$t$ distances to independent K-means centroids initialized on $H^{(L)}$ or shares the centroids $c_j$ initialized on $Z^{(L)}$.
3. **Hyperparameter Selection on the Evaluation Benchmarks and Oracle Cluster Count $K$ (Pillar 2 & Pillar 5):**
   * **Location:** Section 2.3 (line 79) and Section 3.4 (line 138).
   * **Defect:** In Section 3.4, the tradeoff weights $\alpha \in \{3\text{e-}6, \dots, 3\text{e-}4\}$ and $\beta \in \{4, \dots, 16\}$ are evaluated across all 14 benchmark datasets to select $\alpha = 3\text{e-}5, \beta = 10$. While showing stability across the grid is helpful, selecting the final operating point based on average test-set ARI/NMI represents mild hyperparameter leakage. Additionally, providing the ground-truth number of clusters $K$ to K-means and $L_{SG}$ relies on oracle information unavailable in de novo cell-type discovery.
4. **Uncorrected Seed-Level Paired $t$-Tests for Method Comparison (Pillar 4):**
   * **Location:** Section 3.5 ("Significance test", line 147).
   * **Defect:** Performing a one-sided paired $t$-test across 10 random seeds on a single fixed dataset tests only sensitivity to random weight/K-means initialization, where $p$-values can be made arbitrarily small by increasing the number of random seeds. Moreover, ~208 pairwise tests ($16 \text{ baselines} \times 13 \text{ datasets}$) are conducted without Benjamini–Hochberg or Holm–Bonferroni correction, and the direction of the one-sided null hypothesis is flipped post hoc depending on which method had the higher sample mean.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.1** | **3.5** | Solid architecture, ablation, and sparsity stress-testing, but penalized for the $d_l$ vs. $K$ dimensional mismatch in Eq. (12), post-hoc one-sided seed-level $t$-tests without multiple-testing correction, and oracle $K$ requirement. |
| **2. Claim-to-Evidence Alignment** | **1.7** | **2.5** | Empirical superiority across 14 benchmarks and sparsity regimes is well supported; claims that $L_{SG}$ directly modifies the attention mechanism to group same-cluster nodes overstate an indirect regularization on hidden layer features $S$. |
| **3. Data Integrity & Biological Plausibility** | **1.4** | **2.0** | Clean use of 14 standard scRNA-seq benchmarks and 2 large 10k-cell datasets; trajectory validation is limited to one synthetic dataset (`binary_tree_8`) and rare cell types ($n=3$ epsilon cells in `Muraro`) are absorbed into larger clusters. |
| **4. Reproducibility & Data Integrity** | **1.5** | **2.0** | Open-source GitHub repository (`DGCSG`) and public datasets are provided, but Equations (8), (12), (16), and (17) contain mathematical typos/omissions. |
| **Scientific Core Score** | **5.2** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **6.7** | **10.0** | **Mixed / Salvageable** |

---

### 5. Constructive and Doable Suggestions for Improvement

1. **Resolve the Dimensionality of $S$ in $L_{SG}(l)$ and Fix Equations (8), (16), and (17):** Clarify in Section 2.2 whether $S$ at layer $l$ has dimension $N \times d_l$ (in which case the trace normalization in Eq. 12 should be $\frac{1}{N d_l}$ and $I$ is $d_l \times d_l$, representing orthogonal feature decorrelation + Laplacian smoothing rather than a $K$-way partition) or whether a linear projection $P^{(l)} \in \mathbb{R}^{d_l \times K}$ maps $S$ to an $N \times K$ soft cluster matrix before computing $L_{SG}(l)$. Fix the index $h_j \to h_k$ in the denominator of Eq. (8), restore the square $q_{ij}^2$ in the numerator of Eq. (17), and explicitly write out the centroid definition for $Q_h$ in Eq. (16).
2. **Replace Post-Hoc Seed-Level $t$-Tests with Dataset-Level Non-Parametric Tests:** Perform a two-sided Wilcoxon signed-rank test (and Friedman test with Nemenyi post-hoc correction) on the mean ARI and NMI scores across the $N = 14$ independent datasets, and apply Holm–Bonferroni correction to any per-dataset comparisons.
3. **Evaluate Sensitivity to Estimated Cluster Count $\hat{K}$:** Add an experiment showing how `DGCSG` performs when $K$ is unknown and estimated upstream via Leiden modularity or eigengap heuristics.
