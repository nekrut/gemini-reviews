# Review of OOD_ANON_04

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **3.7 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.9/2.5 | Biology: 0.9/2.0 | Reproducibility: 1.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This bioinformatics study introduces `DTI-MHAPR`, a computational framework for drug-target interaction (DTI) prediction that integrates drug chemical structure similarity, target protein sequence similarity, and Gaussian interaction profile (GIP) kernel similarities into a heterogeneous graph attention network (HAN), concatenates multi-layer node embeddings, applies Principal Component Analysis (PCA) for dimensionality reduction, and classifies drug-target pairs using a Random Forest (RF). Evaluated via 5-fold cross-validation on two public benchmark datasets—DC (708 drugs, 1,512 proteins, 1,923 known DTIs) and FSL (862 drugs, 1,517 proteins, 3,583 known DTIs)—with 1:1 random negative subsampling, the authors report AUCs of 0.9950 (DC) and 0.9890 (FSL), outperforming seven baseline methods.

While the authors provide a public GitHub repository and conduct extensive classifier and dimensionality-reduction comparisons, the near-perfect benchmark performance ($\text{AUC} = 0.9950$) is undermined by severe transductive data leakage, mathematical errors in equations and variable definitions, and an invalid case-study validation design. Specifically, the Gaussian interaction profile (GIP) kernel similarity matrices and the heterogeneous graph metapaths (`drug-edge-target` and `target-edge-drug`) appear to be constructed using the full set of known DTIs prior to cross-validation splitting, leaking test-fold interaction edges directly into the node features and message-passing topology. Moreover, baseline models (`CGHCN` and `HFHLMDA`) were handicapped by being fed reduced inputs ("we only used the drug-target similarity matrix as training data"), the dimensionality reduction comparison applies transductive non-parametric methods (`t-SNE` with 3 components) across the dataset, and the case study (Tables 10–12) validates the model by checking whether top predictions for Olanzapine, Quetiapine, and Cabergoline appear in DrugBank—the exact database from which the training positives were extracted.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Near-perfect DTI prediction performance ($\text{AUC} = 0.9950$ on DC and $0.9890$ on FSL) outperforming seven state-of-the-art baselines (Tables 2–3, Figures 2–3): [Methodologically Flawed].**  
  Three methodological flaws invalidate the benchmark comparison:
  1. *Transductive label leakage via GIP similarity and HAN metapaths:* In Sections "Overview of processes" and "Multi-view similarity feature integration," the heterogeneous graph and the Gaussian interaction profile kernel matrices ($G_t, G_d$) are constructed from "known DTIs information" before the 5-fold cross-validation split is applied to the balanced positive/negative sample pairs. Because the HAN aggregates neighbor features along `drug-edge-target` and `target-edge-drug` metapaths (which ARE the DTI edges being predicted), any test-set positive DTI left in the graph topology or used to compute $G_t$ and $G_d$ leaks the test labels directly into the node embeddings.
  2. *Asymmetric handicapping of baselines:* In Section "Experiments and results," the authors state: "For the single-modal models CGHCN [52] and HFHLMDA [51], we only used the drug-target similarity matrix as training data," depriving those baselines of the drug structure and target sequence similarities given to `DTI-MHAPR`.
  3. *Internal mathematical contradiction in Table 2:* For baseline `DTI-CNN` on the balanced DC dataset (50% positives, 50% negatives), Table 2 reports $\text{Recall (Sensitivity)} = 0.8685$ and $\text{Specificity} = 0.8726$, yet reports $\text{Accuracy} = 0.9412$. Mathematically, Accuracy is a convex combination of Sensitivity and Specificity ($\text{Acc} = \pi \cdot \text{Recall} + (1-\pi)\cdot \text{Spec} \approx 0.8705$); an accuracy of $0.9412$ is impossible when both Recall and Specificity are $\sim 0.87$.

* **PCA dimensionality reduction retaining 99.80% variance compresses 1,536 dimensions into 2–12 components and outperforms t-SNE and LLE (Tables 4–7): [Fragile].**  
  In Section "An investigation of the effect of PCA downscaling index," the authors report that retaining $99.80\%$ of cumulative variance reduces a $1,536$-dimensional multi-layer HAN embedding to just $2$–$6$ dimensions on FSL and $8$–$12$ dimensions on DC. This extreme rank collapse (where $>99.8\%$ of variance across 1,536 channels lies in $\sim 4$ dimensions) indicates that the 4- to 6-layer HAN has suffered severe oversmoothing, collapsing node representations onto a low-rank subspace. Furthermore, in Tables 4 and 5, the authors benchmark PCA against `t-SNE` (`Best_n_components = 3`) and `LLE` applied to "the normalised dataset" prior to ML classification; `t-SNE` is a non-parametric manifold visualization algorithm that has no out-of-sample projection matrix, confirming that dimensionality reduction was fit transductively on the combined training and test data.

* **Case study validation of top-20 predicted targets for Olanzapine, Quetiapine, and Cabergoline in DrugBank (Tables 10–12): [Methodologically Flawed].**  
  In Section "Case study," the authors select three drugs with a "high number of interactions among the known DTIs" extracted from DrugBank, rank their top 20 predicted targets, and claim validation because 16/20 (Olanzapine), 18/20 (Quetiapine), and 17/20 (Cabergoline) are recorded in DrugBank. However, Section "Data collection" states that "known DTIs... were extracted from the DrugBank database." Evaluating whether a model recovers its own training set positives in DrugBank measures training-set memorization, not prospective discovery of novel DTIs. Even more concerningly, the top-20 target lists for Quetiapine (Table 11) and Cabergoline (Table 12) are identical in exact rank order from Rank 1 to Rank 14 (`P28223`, `P08913`, `P08172`, `P14416`, `P35368`, `P08908`, `P35348`, `P18089`, `P28222`, `P28221`, `P08173`, `P21728`, `P20309`, `P35462`), indicating either a copy-paste error between tables or that the RF classifier outputs nearly identical target rankings regardless of the query drug.

* **Mathematical formulation of similarity integration, HANlayers, and PCA (Equations 1–15): [Fragile].**  
  The mathematical exposition contains multiple indexing and notation errors:
  1. In Equations 1–2, $S_t \in \mathbb{R}^{T \times T}$ is mislabeled as "the drug structure similarity matrix" and $S_d \in \mathbb{R}^{D \times D}$ is mislabeled as "the target sequence similarity matrix" (swapping $d$ and $t$).
  2. In Equation 6, the summation index is $k \in \mathcal{N}_i^\phi$, but the summand is $\alpha_{ij}^\phi \cdot h_j'$ (summing over $k$ while indexing by $j$).
  3. In Equation 9, the left-hand side is $f(\phi_i)$ while the right-hand side sums over $i \in V$ for metapath $\phi_p$.
  4. Equation 11 defines $Z_{\text{M-view}} = \text{Concat}(Z_{\text{conv1}}, Z_{\text{conv2}}, Z_{\text{conv3}})$ (3 layers), whereas the text states that 6 layers were used for FSL and 4 layers for DC.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Eliminate Transductive Data Leakage in GIP Kernel Computation, HAN Message Passing, and PCA
* **WHY:** Computing Gaussian interaction profile similarities ($G_d, G_t$), HAN metapaths, and PCA/t-SNE across all known DTIs before cross-validation leaks test edges into the training features, artificially inflating AUC toward $0.995$.
* **WHAT:** Recompute $G_d, G_t$, the heterogeneous graph adjacency matrix, and the PCA transformation matrix $W_k$ strictly within each training fold.
* **HOW:** In each fold of the 5-CV: (1) zero out all test-fold positive DTI edges in the interaction matrix $Y_{\text{train}}$; (2) compute $G_d$ and $G_t$ solely from $Y_{\text{train}}$; (3) construct the HAN metapath adjacency matrices using only $Y_{\text{train}}$; (4) fit the PCA eigenvectors $W_k$ on the training-fold node pair embeddings and project the test-fold pairs using $Z_{\text{test, final}} = (Z_{\text{test}} - \mu_{\text{train}}) W_k$. In addition, evaluate under cold-start drug and cold-start target splits.

#### 2. Remove Training Positives from the Case Study and Audit Tables 11 and 12
* **WHY:** Counting known DrugBank training interactions among the top-20 predictions as "validated" tests memorization rather than de novo prediction, and Tables 11 and 12 have identical top-14 rankings.
* **WHAT:** Exclude all known training DTIs before ranking candidate targets for Olanzapine, Quetiapine, and Cabergoline, and validate novel predictions against independent databases (e.g., ChEMBL, BindingDB, CTD, or Therapeutic Target Database) not used to build the DC/FSL datasets.
* **HOW:** Mask all pairs with $Y_{ij} = 1$ in the training set, rank the remaining unknown targets ($Y_{ij} = 0$), and check whether the top-20 unmasked predictions are supported by external bioassay records in ChEMBL/BindingDB. Audit the code that generated Tables 11 and 12 to determine why Ranks 1–14 are identical between Quetiapine and Cabergoline.

#### 3. Evaluate Under Realistic Class Imbalance (1:10 or Full Unbalanced Matrix)
* **WHY:** Table 1 shows that true DTIs represent only $0.17\%$ (DC) and $0.27\%$ (FSL) of all drug-target pairs, so 1:1 balanced sampling inflates AUPR and Precision compared to real-world virtual screening.
* **WHAT:** Report AUPR and Recall@$K$ across unbalanced test sets (e.g., 1:10 positivo-to-negative ratio or all unknown pairs).
* **HOW:** Keep the 5-CV evaluation on a 1:10 negative sample ratio and report the AUPR and Precision@20 alongside the 1:1 results in Tables 2 and 3.

#### 4. Correct Mathematical Equations and Table 2 Baseline Metrics
* **WHY:** Swapped definitions in Equations 1–2, mismatched indices in Equations 6 and 9, and impossible accuracy values in Table 2 undermine technical credibility.
* **WHAT & HOW:**
  1. In Equations 1–2, swap the text descriptions so $S_t, G_t \in \mathbb{R}^{T \times T}$ denote target sequence and Gaussian similarities, and $S_d, G_d \in \mathbb{R}^{D \times D}$ denote drug structure and Gaussian similarities.
  2. In Equation 6, change $\sum_{k \in \mathcal{N}_i^\phi} \alpha_{ij}^\phi \cdot h_j'$ to $\sum_{j \in \mathcal{N}_i^\phi} \alpha_{ij}^\phi \cdot h_j'$.
  3. Re-check the evaluation script for `DTI-CNN` in Table 2 where $\text{Acc} = 0.9412$ contradicts $\text{Recall} = 0.8685$ and $\text{Spec} = 0.8726$.
