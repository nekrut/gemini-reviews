# Review of FEXP_ANON_090

**Overall Score:** **5.6 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **4.3 / 8.0**  
* **Score Breakdown:** Rigor: 1.7/3.5 | Claims: 1.4/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.3/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Role / Domain:** Computational biology / deep learning methodology manuscript proposing `scZAG`, a ZINB-based adaptive graph contrastive learning and APPNP graph convolution framework for scRNA-seq clustering.
* **Blinded Document Assessment:** A recognizable deep single-cell clustering algorithm paper combining established building blocks (`ZINB` autoencoder from `DCA`/`scTAG`, `APPNP` propagation from Klicpera et al. 2019, adaptive PageRank-weighted graph contrastive learning from `GCA` [Zhu et al. 2021], and DEC Student-$t$ KL clustering) with open-source code (`[GITHUB_REPO_REDACTED]`). While the architectural synthesis is plausible and ablation experiments are included, the manuscript omits the overall joint objective function and loss weights, contains mathematical errors in its preprocessing and ZINB/APPNP equations, excludes the very contrastive-learning scRNA-seq baselines (`contrastive-sc`, `scNAME`, `scTAG`) discussed in its Introduction from its empirical comparison, and applies an unpaired Mann–Whitney U test instead of a paired test across the 10 benchmark datasets.

---

## 2. Executive Summary & Editorial Verdict

The authors present `scZAG`, an unsupervised scRNA-seq clustering model that constructs a $K$-nearest neighbor ($K = 15$) cell graph on the top 500 highly variable genes (HVGs) and trains a two-layer Approximate Personalized Propagation of Neural Predictions (`APPNPGCN`, hidden dimensions 128 and 15) encoder coupled to a three-layer ZINB decoder (128, 256, 512) and a Student-$t$ KL divergence clustering module. During training, two augmented graph views are generated via PageRank-centrality-guided edge dropping and node-attribute masking and contrasted via an InfoNCE loss. Evaluated across 10 real scRNA-seq datasets (averaged over 5 runs) against five baselines (`scziDesk`, `GraphSCC`, `scGAE`, `scDeepCluster`, `AutoClass`), `scZAG` achieves the highest ARI on 9/10 datasets and highest NMI on 8/10 datasets.

**Editorial Verdict: Major Revision (Mixed / Salvageable).** The source code and benchmark datasets are publicly accessible, and the ablation study (replacing APPNPGCN with standard GCN, removing adaptive graph contrastive learning, and removing the ZINB loss) supports the utility of each module. However, several methodological, mathematical, and benchmarking deficiencies require revision:
1. **Omission of the Overall Multi-Task Loss Function and Training Schedule Coupling:** Section 4 defines three separate objectives—InfoNCE contrastive maximization $J$ (Eq. 3), ZINB negative log-likelihood minimization $L_{\text{ZINB}}$ (Eq. 20), and KL clustering loss minimization $L_c$ (Eq. 21)—but never specifies the combined loss function $L_{\text{total}}$, the balancing hyperparameters weighting these three terms during the 1,000-epoch pre-training and 300-epoch main training phases, or whether $Z$ in the ZINB/KL modules is computed from the unaugmented graph $G$ or fused from the augmented embeddings $U$ and $V$.
2. **Mathematical Formulation Errors in Preprocessing (Eq. 1), APPNP (Eq. 14), and ZINB (Eqs. 15–20):** Section 4.2 states that the authors *"filter out genes that are expressed in more than 1% of cells"* (an inversion of $<1\%$) and writes Equation (1) as $N X_{ij} = \ln(m(X)\frac{X_{ij}}{\sum_o X_{io}})$ without a pseudocount ($+1$), which evaluates to $-\infty$ for all zero counts. Equation (14) applies a classification `softmax` to the 15-dimensional latent embedding $Z^{(K)}$, and Equations (15)–(20) omit cell-specific library size factors $s_i$ from the ZINB mean parametrization.
3. **Omission of Single-Cell Contrastive and ZINB-GNN Baselines Discussed in the Introduction:** Although the Introduction specifically critiques `contrastive-sc` [17], `scNAME` [18], and `scTAG` [13], none of these methods are included in the benchmark comparison (which is restricted to five 2019–2021 non-contrastive baselines).

### Specific Conclusions and Assessment of Support

* **Superior ARI (9/10 datasets) and NMI (8/10 datasets) of `scZAG` over five baseline clustering algorithms: [Moderately Supported].**  
  `scZAG` outperforms `scziDesk`, `GraphSCC`, `scGAE`, `scDeepCluster`, and `AutoClass` across 10 datasets, but direct scRNA-seq contrastive/GNN competitors (`contrastive-sc`, `scNAME`, `scTAG`) were omitted, hyperparameters ($K = 15$ and $\text{HVGs} = 500$) were selected by maximizing average ARI/NMI across the 10 test datasets (Section 2.4), and the statistical test in Section 2.2 used an unpaired Mann–Whitney U test rather than a paired Wilcoxon signed-rank test across matched datasets.
* **Positive contribution of APPNPGCN, adaptive graph contrastive learning (GCA), and ZINB reconstruction in ablation experiments (Section 2.5): [Well Supported].**  
  The three ablation variants directly isolate the propagation scheme, contrastive augmentation module, and ZINB likelihood on the 10 datasets.
* **PageRank-guided adaptive augmentation preserves core cell-graph topology while perturbing noisy edges and features: [Moderately Supported].**  
  The formulation in Section 4.5 adapts GCA (`Zhu et al. 2021`), but no ablation comparing adaptive PageRank augmentation against uniform random edge dropping / feature masking is presented to prove that the adaptive centrality weighting outperforms uniform augmentation on scRNA-seq KNN graphs.

---

## 3. Forensic Defect Inventory

1. **Missing Joint Objective Function, Loss Weights, and View-Fusion Specification (Pillar 3 & Pillar 7):**
   * **Location:** Section 2.1 (line 26) and Sections 4.4–4.8 (lines 86–140).
   * **Defect:** The manuscript defines $J$ (Eq. 3, to be maximized), $L_{\text{ZINB}}$ (Eq. 20, to be minimized), and $L_c$ (Eq. 21, to be minimized), yet never writes the unified objective function or specifies the tradeoff weights connecting them. Nor does it explain whether the ZINB decoder $f_D(Z)$ and Student-$t$ similarity $q_{iu}$ operate on the unperturbed graph embedding $Z^{(K)}$ or on an aggregation of the two augmented views $U$ and $V$.
2. **Mathematical Errors in Gene Filtering, Log Normalization (Eq. 1), APPNP Output Activation (Eq. 14), and ZINB Mean Scaling (Eq. 18) (Pillar 3 & Pillar 7):**
   * **Location:** Section 4.2 (line 78, Eq. 1), Section 4.6 (line 126, Eq. 14), and Section 4.7 (line 131, Eqs. 15–20).
   * **Defect:**
     * Line 78 states *"we filter out genes that are expressed in more than 1% of cells"* instead of *fewer* than 1% of cells.
     * Equation (1), $N X_{ij} = \ln(m(X)\frac{X_{ij}}{\sum_o X_{io}})$, omits $+1$ inside the logarithm, which is undefined ($\ln 0 = -\infty$) for zero UMI counts.
     * Equation (14) applies `softmax` to the final APPNP layer $Z^{(K)}$, constraining the 15-dimensional latent space to a probability simplex prior to Euclidean K-means/spectral clustering.
     * Equations (15)–(20) evaluate the discrete ZINB likelihood (which contains $x_i!$ in Eq. 15) without multiplying the decoded mean $\mu = \exp(W_\mu f_D(Z))$ by each cell's library size factor $s_i$, and mix scalar ($x, x_i$) and matrix ($X$) notation.
3. **Inconsistent Baseline Counts and Improper Unpaired Statistical Testing (Pillar 4 & Pillar 5):**
   * **Location:** Section 2.2 (lines 31, 33, 35).
   * **Defect:** Line 31 lists **five** baselines (`scziDesk`, `GraphSCC`, `scGAE`, `scDeepCluster`, `AutoClass`), line 33 suddenly refers to `scDCC` (*"including scziDesk and scDCC demonstrated better and more stable clustering performance"*), and line 35 states *"determine the presence of significant differences between scZAG and the other **four** methods."* Furthermore, comparing two algorithms evaluated on the same 10 benchmark datasets requires a **paired** Wilcoxon signed-rank test, not an independent-sample Mann–Whitney U test (line 35), and contrastive scRNA-seq baselines (`contrastive-sc`, `scNAME`, `scTAG`) are omitted.
4. **Hyperparameter Selection on the Evaluation Benchmarks (Pillar 2):**
   * **Location:** Section 2.4 (lines 45–47).
   * **Defect:** The KNN neighborhood size $K = 15$ and HVG count ($500$) were selected by evaluating average ARI and NMI across all 10 benchmark datasets rather than on a separate validation set.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.7** | **3.5** | Sensible architectural combination and 3-way ablation study, but penalized for missing joint loss equation/weights, `ln(0)` and ZINB/APPNP equation errors, test-set hyperparameter tuning, and unpaired Mann–Whitney test. |
| **2. Claim-to-Evidence Alignment** | **1.4** | **2.5** | Outperforms 5 older baselines (2019–2021), but omits recent contrastive/ZINB-GNN methods (`contrastive-sc`, `scNAME`, `scTAG`) and lacks an ablation comparing adaptive PageRank augmentation vs. uniform random augmentation. |
| **3. Data Integrity & Biological Plausibility** | **1.2** | **2.0** | Evaluates on 10 authentic scRNA-seq datasets from `cblast.gao-lab.org`, though no biological downstream validation (marker recovery, rare cell identification, or trajectory analysis) is included. |
| **4. Reproducibility & Data Integrity** | **1.3** | **2.0** | Open-source GitHub repository (`scZAG`) and public dataset links are provided with hardware/epoch details, but the mathematical text omits the total loss function and contains inconsistent baseline counts (5 vs. 4 vs. `scDCC`). |
| **Scientific Core Score** | **4.3** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **5.6** | **10.0** | **Mixed / Salvageable** |

---

### 5. Constructive and Doable Suggestions for Improvement

1. **Write Out the Complete Joint Loss Function and Training Procedure:** Add an explicit equation in Section 4.8 defining $L_{\text{total}} = L_{\text{ZINB}} - \lambda_1 J + \lambda_2 L_c$, report the exact numerical values of $\lambda_1, \lambda_2$, temperature $\tau$, edge-drop probability $p_e$, feature-mask probability $p_f$, cutoff $p_\tau$, and APPNP teleport probability $\alpha$, and clarify how $Z$, $U$, and $V$ are routed during pre-training and main training.
2. **Fix Mathematical Equations (1), (14), and (15)–(20):** Correct "more than 1% of cells" to "fewer than 1% of cells" in line 78, add $+1$ inside the logarithm in Equation (1) ($\ln(m(X)\frac{X_{ij}}{\sum_o X_{io}} + 1)$), clarify whether `softmax` or an activation such as `ReLU`/linear is used at the encoder output in Equation (14), and document how raw counts vs. library-size factors are handled in the ZINB loss (Eqs. 15–20).
3. **Benchmark Against Contrastive/GNN Baselines and Use Paired Statistical Tests:** Add `contrastive-sc`, `scNAME`, and `scTAG` to the 10-dataset comparison, add an ablation comparing adaptive PageRank augmentation against uniform random augmentation, remove the stray reference to `scDCC` (and fix "four methods" to "five methods") in Section 2.2, and use a two-sided paired Wilcoxon signed-rank test with Holm–Bonferroni correction across the 10 datasets.
