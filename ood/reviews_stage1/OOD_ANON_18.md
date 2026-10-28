# Review of OOD_ANON_18

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **1.8 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.3/3.5 | Claims: 0.4/2.5 | Biology: 0.6/2.0 | Reproducibility: 0.5/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study proposes QKDTI (Quantum Kernel Drug–Target Interaction), a hybrid quantum–classical support vector regression (QSVR) framework using an 8-qubit parameterized quantum circuit (`H`, `RY`, `RZ`, and `CZ` gates in PennyLane/Qiskit) and a 50-landmark Nyström kernel approximation to predict drug–target binding affinities on the DAVIS, KIBA, and BindingDB benchmark datasets. The authors apply log transformation, Z-score normalization, and PCA dimensionality reduction to molecular and protein descriptors, fit an $\epsilon$-SVR model ($C = 1.0, \epsilon = 0.1$), and report "prediction accuracy" values of 94.21% on DAVIS, 99.99% on KIBA, and 89.26% on BindingDB alongside MSE, RMSE, $R^2$, Pearson $r$, and AUC-ROC metrics (Table 8) and paired $t$-test / Wilcoxon comparisons against classical and quantum baselines (Table 9). Code is not publicly available ("will be made available... based on the request"), and all 16 numbered mathematical equations in the manuscript are blank.

A forensic audit of the mathematical definitions, dataset statistics, and performance tables reveals that this manuscript is fundamentally invalid due to severe mathematical inconsistencies, internally contradictory tables, and unphysical/fabricated statistical test outputs:
1. All 16 equations (Equations 1–16) are completely missing from the text (rendered as empty tables).
2. The reported MSE, RMSE, target variance ($\sigma$), and $R^2$ values in Tables 4 and 8 violate the mathematical identities $\text{RMSE} = \sqrt{\text{MSE}}$ and $R^2 = 1 - \text{MSE}/\sigma^2$.
3. The main text (Section "Comparative analysis", line 20) reports completely different RMSE, $R^2$, and Pearson $r$ numbers for QKDTI on BindingDB and DAVIS than Table 8.
4. Table 9 ("Statistical analysis of classical and quantum models") contains two different rows for `QKDTI (Proposed)` with different $t$-statistics and $p$-values on KIBA, identical copy-pasted 4-decimal numbers across distinct datasets and models (e.g., Gradient Boosting and LightGBM on BindingDB have identical $t = 6.2202, p = 0.0001$; VQC has identical $t = 2.8114$ on DAVIS and BindingDB), and impossible Wilcoxon signed-rank $p$-values (e.g., $W = 0.0$ yielding $p = 0.1250$, $p = 0.008$, and $p = 0.0020$ across columns of the same experiment).
5. Precomputing PCA, Z-score standardization, and kernel matrices across the entire dataset prior to splitting (Section "Data preprocessing", line 249) constitutes textbook data leakage.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **QKDTI achieves 94.21% accuracy ($R^2 = 0.8531$) on DAVIS, 99.99% accuracy ($R^2 = 0.6415$) on KIBA, and 89.26% accuracy ($R^2 = 0.5928$) on BindingDB (Table 8): [Methodologically Flawed].**  
  The numbers reported in Table 4, Table 8, and the main text violate elementary mathematical identities:
  1. **Violation of $\text{RMSE} = \sqrt{\text{MSE}}$:** In Table 8, for DAVIS, $\text{MSE} = 0.255$, whose square root is $\sqrt{0.255} = 0.5050$, not the reported $\text{RMSE} = 0.5212$ ($0.5212^2 = 0.2716$). For BindingDB, Table 8 reports $\text{MSE} = 0.4592$ and $\text{RMSE} = 0.534$, whereas $\sqrt{0.4592} = 0.6776$ ($0.534^2 = 0.2852$).
  2. **Contradiction between main text and Table 8:** In Section "Comparative analysis" (line 20 of part 2), the text states that on BindingDB, QKDTI achieved $\text{RMSE} = 0.9722$ and $R^2 = 0.521$, and on DAVIS achieved $\text{MSE} = 0.25$ and Pearson $r = 0.921$, directly contradicting Table 8 ($\text{RMSE} = 0.534, R^2 = 0.5928$ on BindingDB; $\text{MSE} = 0.255, r = 0.924$ on DAVIS).
  3. **Violation of $R^2 = 1 - \text{MSE}/\sigma_y^2$:** In Table 4, the standard deviation of log-transformed KIBA scores is reported as $\sigma = 0.031$ ($\sigma^2 = 0.000961$). With $\text{MSE} = 0.0003$ (Table 8), $1 - 0.0003/0.000961 = 0.6878 \neq 0.6415$ (moreover, the actual KIBA benchmark in TDC has raw scores around $11\text{--}12$ with $\sigma \approx 0.84$, not $\sigma = 0.031$, and achieving $99.99\%$ "accuracy" is a trivial scale artifact of dividing a small $\text{MSE}$ or error on a heavily compressed scale with $\sigma = 0.031$). For DAVIS, Table 4 gives $\sigma = 0.826$ ($\sigma^2 = 0.6823$); with $\text{MSE} = 0.255$, $1 - 0.255/0.6823 = 0.6263$, which makes the reported $R^2 = 0.8531$ mathematically impossible. For BindingDB, Table 4 gives $\sigma = 1.372$ ($\sigma^2 = 1.8824$); with $\text{MSE} = 0.4592$, $1 - 0.4592/1.8824 = 0.7561 \neq 0.5928$.
  4. **Violation of $R^2 \le r^2$:** For a calibrated regression model on DAVIS, Pearson $r = 0.924$ implies $r^2 = 0.8538$, whereas on KIBA $r = 0.7924 \implies r^2 = 0.6279 < R^2 = 0.6415$ (impossible, as $R^2$ cannot exceed the squared Pearson correlation $r^2$ in least-squares/unbiased regression).

* **Paired $t$-tests and Wilcoxon signed-rank tests prove QKDTI significantly outperforms classical and quantum baselines (Table 9): [Methodologically Flawed].**  
  Table 9 exhibits multiple hallmarks of synthetic or corrupted statistical entries:
  1. **Self-comparison and duplicate conflicting rows:** Table 9 lists `QKDTI (Proposed)` *twice*—once under "Classical Models" with KIBA paired $t$-test $(4.200, 0.003)$ and Wilcoxon $(0.0, 0.008)$, and a second time under "Quantum Models" with KIBA paired $t$-test $(3.050, 0.014)$ and Wilcoxon $(2.0, 0.031)$. Furthermore, a paired test compares *two* models against each other, so `QKDTI (Proposed)` cannot have a paired $t$-test against itself.
  2. **Impossible Wilcoxon $p$-values and implied sample sizes:** For a two-sided exact Wilcoxon signed-rank test, a test statistic of $W = 0.0$ yields $p = 0.1250$ when $n = 4$ pairs ($2/2^4 = 0.125$), $p = 0.0625$ when $n = 5$ pairs, $p = 0.0078 \approx 0.008$ when $n = 8$ pairs, and $p = 0.0020$ when $n = 10$ pairs ($2/2^{10} = 0.00195$). In Table 9, within the *same* DAVIS column, `QKDTI` has $W = 0.0, p = 0.1250$ ($n=4$) while `VQC` has $W = 0.0, p = 0.0625$ ($n=5$), and in BindingDB `Linear Regression` has $W = 0.0, p = 0.0010$ ($n=11$) while `QKDTI` has $W = 0.0, p = 0.0020$ ($n=10$) and `QFFR`/`QNN` have $p = 0.6250$ / $0.2500$ ($n=4$). Testing models on test sets of 6,012 (DAVIS) or 23,651 (KIBA) drug–target pairs cannot produce $n = 4$ to $n = 11$ inconsistent sample sizes across rows.
  3. **Identical copy-pasted test statistics across different models and datasets:** In BindingDB, `Gradient Boosting` and `LightGBM` have the exact same 4-decimal paired $t$-test $(6.2202, 0.0001)$ and Wilcoxon $(0.0, 0.0020)$. Across datasets, `VQC` has the exact same $t$-statistic `2.8114` on both DAVIS and BindingDB.

* **8-qubit quantum feature mapping with 50-landmark Nyström approximation captures complex protein–ligand interactions and generalizes to 1,000,000 BindingDB pairs: [Methodologically Flawed].**  
  1. **Dimensionality bottleneck and Nyström rank collapse:** The authors state (Section "Data preprocessing", line 249) that PCA was applied to retain 95% of variance from molecular fingerprints and ProtBERT protein embeddings (hundreds of dimensions), yet the quantum circuit (Table 5) has only **8 qubits**, with one feature encoded per qubit via $R_Y(x_i) R_Z(x_i)$. Encoding only 8 scalar values discards almost all drug and protein sequence information. Worse still, approximating a kernel matrix over 24,044 (DAVIS), 94,603 (KIBA), or 1,000,000 (BindingDB) drug–target pairs using only **50 Nyström landmark points** (Table 6) restricts the kernel matrix to rank $\le 50$ in an 8-qubit Hilbert space, which is equivalent to a low-rank classical feature map and cannot capture complex biochemical interactions across 1,500 target proteins.
  2. **Preprocessing data leakage:** Line 249 states that Z-score standardization, mean imputation, PCA dimensionality reduction, and conversion into a precomputed kernel format were performed on the datasets *before* training/testing, leaking test-set distribution statistics and principal components into training.
  3. **Subset sampling undisclosed:** Line 181 notes that *"we deliberately limited the training and test datasets to subset samples"*, yet Table 3 lists the full DAVIS (30,056), KIBA (118,254), and BindingDB (~1,000,000) counts without ever reporting the actual subset sizes used in the experiments.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Restore All 16 Missing Equations and Reconcile All Numerical Contradictions Across Tables 4, 8, and 9
* **WHY:** Equations 1–16 are completely blank, Table 8 violates $\text{RMSE} = \sqrt{\text{MSE}}$ and $R^2 = 1 - \text{MSE}/\sigma^2$, the main text contradicts Table 8, and Table 9 contains duplicate conflicting rows and impossible Wilcoxon statistics.
* **WHAT:** Insert the explicit mathematical expressions for Equations 1–16, recompute all regression metrics ($\text{MSE}, \text{RMSE}, R^2, r$, Concordance Index) directly from authentic out-of-sample model predictions, and replace Table 9 with valid paired comparisons on a consistent evaluation split.
* **HOW:**
  1. Populate Equations 1–16 with their standard mathematical formulas (noting the exact formula used for "Prediction Accuracy" in Equation 14 and the exact affinity threshold used to compute AUC-ROC).
  2. Re-run the evaluation script to verify that $\text{RMSE} = \sqrt{\text{MSE}}$ and $R^2 = 1 - \sum (y_i - \hat{y}_i)^2 / \sum (y_i - \bar{y})^2$ hold to all reported decimal places across DAVIS, KIBA, and BindingDB, and remove the conflicting numbers in Section "Comparative analysis".
  3. In Table 9, specify what each baseline model is being compared *against* (e.g., Baseline vs. QKDTI across $K=10$ cross-validation folds), remove the duplicate `QKDTI (Proposed)` rows, and report exact paired $t$ and Wilcoxon signed-rank statistics computed on the same number of folds $K$ for all models.

#### 2. Eliminate Preprocessing Data Leakage and Document Exact Subset Sizes and Feature Encodings
* **WHY:** Fitting Z-score scalers, PCA projections, and Nyström landmark kernels on the combined dataset before splitting leaks test data into the training pipeline, and mapping both a drug SMILES and a protein FASTA sequence into 8 qubits is underspecified.
* **WHAT:** Fit all preprocessing transforms (`StandardScaler`, `PCA`, and Nyström landmark selection) strictly on the training split of each dataset, explicitly report the exact number of training, test, and validation pairs used after subsetting, and specify how drug and protein features were concatenated or fused into the 8-qubit input vector $x \in \mathbb{R}^8$.
* **HOW:** Use a `scikit-learn` `Pipeline` where `StandardScaler()`, `PCA(n_components=8)`, and Nyström landmark sampling are fitted only on `X_train`, and transform `X_test` and `X_val` using the frozen training parameters.

#### 3. Perform an Ablation Study Comparing the 8-Qubit Quantum Kernel Against Classical RBF/Polynomial SVR on Identical 8-PCA Features
* **WHY:** Because an 8-qubit circuit with $R_Y(x_i)R_Z(x_i)$ and nearest-neighbor $CZ$ gates spans a small, efficiently simulable Hilbert space ($\dim = 2^8 = 256$) further compressed to rank 50 via Nyström approximation, any performance difference relative to classical SVR could be due to hyperparameter settings rather than quantum entanglement.
* **WHAT:** Compare QKDTI (with and without $CZ$ entanglement gates, and with 50 vs. 500 Nyström landmarks) against classical RBF-SVR and Random Forest trained on the exact same 8 PCA components with matched hyperparameter tuning.
* **HOW:** Run classical `SVR(kernel='rbf')` with grid-searched $(C, \gamma, \epsilon)$ on the identical 8-dimensional PCA training features and report its MSE, RMSE, $R^2$, and wall-clock runtime alongside QKDTI.

#### 4. Publicly Deposit the Complete Executable Codebase
* **WHY:** Given the missing equations and severe numerical discrepancies in Tables 8 and 9, independent verification requires immediate public access to the PennyLane/Qiskit and Scikit-learn scripts.
* **WHAT & HOW:** Upload the complete training, Nyström kernel approximation, and evaluation scripts (alongside the exact random seeds and data subset indices) to a public GitHub/Zenodo repository and include the direct URL in the Data Availability Statement.
