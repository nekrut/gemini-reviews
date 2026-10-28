# Review of OOD_ANON_38

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.9 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.3/3.5 | Claims: 1.2/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.3/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces `DeepTGIN`, a multimodal regression model for protein–ligand binding affinity prediction that combines two 4-layer Transformer encoders (operating on integer-encoded full protein sequences of length $\le 1000$ and binding-pocket residue sequences of length $\le 63$) with a 4-layer Graph Isomorphism Network (GIN, operating on RDKit ligand molecular graphs with 108-dimensional one-hot atom features across 10 atomic properties). Trained on the merged PDBbind v.2020 general and refined sets (excluding 1,000 random validation complexes and exact test-set IDs), `DeepTGIN` is evaluated on the PDBbind 2016 ($N = 285$) and PDBbind 2013 ($N = 195$) core sets against eight baseline models. Source code is publicly available on GitHub.

While the integration of global protein sequence, local pocket sequence, and ligand graph representations is straightforward, the study suffers from unaddressed train–test structural/sequence homology leakage, lack of multi-seed uncertainty quantification, and mathematical errors across its core equations. Most notably, in Table 2, `DeepTGIN` achieves substantially higher accuracy on the external PDBbind 2016 test set ($R = 0.834, \text{RMSE} = 1.203$) than on its own randomly sampled validation set ($R = 0.736, \text{RMSE} = 1.277$). Because the 57 target protein families of the CASF-2016 core set are heavily represented in the PDBbind 2020 general and refined sets—and only exact PDB ID duplicates were removed (line 64)—the dual sequence Transformers can memorize target-family pocket sequences without generalizing to unseen protein families. Furthermore, Equations 1, 2, 5, and 11 contain mathematical errors (including a Concordance Index formula in Eq. 11 that omits ground-truth labels $y_t$ entirely and normalizes by $N$ instead of comparable pairs $Z$). Re-evaluating the model under sequence/structure-clustered splits across multiple random seeds and correcting the mathematical formulations are necessary to establish its true generalization performance.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **DeepTGIN outperforms eight state-of-the-art baselines on the PDBbind 2016 and PDBbind 2013 core sets across $R$, RMSE, MAE, SD, and CI (Tables 2–4): [Fragile].**  
  First, only exact PDB ID duplicates of the 2016 and 2013 core sets were removed from the PDBbind 2020 general + refined training pool (line 64). Because PDBbind 2020 contains hundreds of complexes sharing identical or near-identical pocket sequences with the 57 CASF-2016 target proteins, the PDBbind 2016 test accuracy ($R = 0.834, \text{RMSE} = 1.203$) is markedly higher than the random validation set accuracy ($R = 0.736, \text{RMSE} = 1.277$, Table 2). Second, all results in Tables 2–6 are single-run point estimates without random-seed standard deviations or statistical significance tests; on PDBbind 2013 (Table 4), the difference between `DeepTGIN` ($R = 0.787, \text{RMSE} = 1.388$) and `IGN` ($R = 0.782, \text{RMSE} = 1.411$) or `GIGN` ($R = 0.780, \text{RMSE} = 1.407$) is well within typical run-to-run variance ($\pm 0.015\text{--}0.025$). Third, `DeepDTA` is included in Table 3 (2016 test set) but omitted without explanation from Table 4 (2013 test set).

* **Adding 5 extra atomic properties to the ligand graph (`chiral tag`, `formal charge`, `number of radical electrons`, `hybridization`, `is in ring`) increases $R$ from $0.723$ to $0.834$ and reduces RMSE by 25.6% on PDBbind 2016 (Tables 5 and 6): [Overstated].**  
  In Tables 5 and 6, the 5-feature variant is mislabeled `DeepTGIN_without_ligand` even though the ligand graph and GIN encoder remain present (line 405). More importantly, a drop from $R = 0.834$ ($\text{RMSE} = 1.203$) to $R = 0.723$ ($\text{RMSE} = 1.512$) from removing 5 atomic features (several of which, like `number of radical electrons`, are zero for virtually all drug-like ligands in PDBbind) would make `DeepTGIN` with 5 atom features plus full protein and pocket Transformers perform substantially *worse* than `DeepDTA` ($R = 0.782, \text{RMSE} = 1.351$) and `DeepDTAF` ($R = 0.758, \text{RMSE} = 1.438$). This suggests either a hyperparameter/training-convergence mismatch in the ablation runs or test-set overfitting in the main model.

* **Transformer attention visualization identifies biologically critical proline residues (`PRO151, PRO152, PRO153, PRO219, PRO222, PRO223`) driving ligand binding (Fig. 5): [Fragile].**  
  Line 355 does not state the PDB identifier or protein name for the complex shown in Fig. 5, and evaluates only a single cherry-picked example where attention weights peak almost exclusively on proline (`P`) residues in both the full sequence and pocket sequence. No quantitative evaluation across the 285 test complexes is provided to test whether high-attention residues correspond to true $< 5\text{ \AA}$ ligand-contacting residues.

* **Mathematical formulation of the GIN encoder, batch normalization, multi-head attention, and Concordance Index (Equations 1, 2, 5, and 11): [Methodologically Flawed].**  
  1. **Eq. 1 (line 120):** Presents the graph-level readout $h_G = \text{CONCAT}(f_r(\{h_v^k \mid v \in G\}))$ while mischaracterizing it as the per-layer GIN message-passing update rule of Xu et al. [43].  
  2. **Eq. 2 (line 130):** Writes $\hat{h}_G = \gamma \times \frac{\hat{h}_G - \bar{h}_G}{\delta(h_G) + \epsilon} + (1 - \gamma)$, which recursively places the output $\hat{h}_G$ inside the numerator on the right-hand side instead of the input $h_G$, and replaces the free shift parameter $\beta$ with $(1 - \gamma)$.  
  3. **Eq. 5 (line 161):** Defines the output projection matrix dimension as $W^O \in \mathbb{R}^{h d_v \times d_k}$ instead of $\mathbb{R}^{h d_v \times d}$.  
  4. **Eq. 11 (line 240):** Writes $\text{CI} = \frac{1}{N}\sum_{y_p(i) > y_p(j)} f(y_p(i) - y_p(j))$, which omits the ground-truth affinities $y_t(i) > y_t(j)$ from the summation condition (making $f(y_p(i) - y_p(j)) \equiv 1$ for all summed terms) and divides by sample size $N$ instead of the number of valid ordered pairs $Z = \sum_{i,j}\mathbb{I}(y_t(i) > y_t(j))$.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Evaluate Generalization Under Protein-Sequence / Structural Clustering and Report Multi-Seed Variance
* **WHY:** Removing only exact PDB ID matches leaves hundreds of sequence-identical or homologous target pockets in the PDBbind 2020 training set, explaining why CASF-2016 test performance ($R = 0.834$) far exceeds random validation performance ($R = 0.736$).
* **WHAT:** Evaluate `DeepTGIN` and the top baselines (`CAPLA`, `GIGN`, `IGN`) across 5 independent random seeds on both the standard split and a homology-filtered split (e.g., excluding training proteins with $> 30\%$ or $> 50\%$ sequence identity or $\text{TM-score} > 0.8$ to any CASF test target).
* **HOW:** Train 5 replicates with different random seeds (`seed = 0..4`) to report $\text{mean} \pm \text{SD}$ in Tables 2–6, add the missing `DeepDTA` row to Table 4, and report performance on a sequence-clustered / CleanSplit partition of PDBbind 2020.

#### 2. Audit and Rename the Ligand Feature Ablation (`DeepTGIN_without_ligand`) and Add a True No-Ligand / No-Protein Control
* **WHY:** Labeling a 5-atom-feature model as `DeepTGIN_without_ligand` is misleading, and a complete ligand-removal ablation (alongside single-property drop-one ablations) is needed to separate true ligand-protein interaction learning from pocket memorization.
* **WHAT:** Rename the 5-feature variant to `DeepTGIN_5atom_props`, add a true `DeepTGIN_no_ligand` ablation (removing the GIN branch entirely) and a `DeepTGIN_no_protein_seq` ablation (retaining only pocket + ligand), and perform drop-one ablations for the 5 removed atomic properties.
* **HOW:** Verify that `DeepTGIN_5atom_props` uses the exact same learning-rate schedule and early-stopping patience as the full model, and report a table showing which of the 5 removed RDKit atom properties (`chiral tag`, `formal charge`, `radical electrons`, `hybridization`, `is in ring`) accounts for the performance difference.

#### 3. Quantify Attention-to-Contact Alignment Across the Test Set
* **WHY:** Showing a single unnamed complex in Fig. 5 where attention weights cluster on proline residues does not establish interpretability.
* **WHAT:** State the PDB ID of the complex in Fig. 5 and compute the average enrichment or ROC-AUC of top-attended pocket residues against heavy-atom ligand contacts ($< 4.5\text{ \AA}$) across all 285 complexes in CASF-2016.
* **HOW:** Extract the final-layer attention weights of the pocket Transformer for all 285 test complexes, rank the non-padded residues by attention weight, and compare against ground-truth PDB ligand-contacting residues.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Incorrect equations in the Methods section prevent accurate re-implementation.
* **WHAT & HOW:**
  1. **Eq. 1 (line 120):** Add the standard GIN node update equation $h_v^{(k)} = \text{MLP}^{(k)}\left((1 + \epsilon^{(k)})h_v^{(k-1)} + \sum_{u \in \mathcal{N}(v)} h_u^{(k-1)}\right)$ before the graph-level readout equation.
  2. **Eq. 2 (line 130):** Replace $\hat{h}_G$ in the numerator on the right-hand side with $h_G$, and clarify whether $(1 - \gamma)$ or an independent learnable bias $\beta$ was implemented in the code.
  3. **Eq. 5 (line 161):** Correct the dimension of $W^O$ from $\mathbb{R}^{h d_v \times d_k}$ to $\mathbb{R}^{h d_v \times d}$.
  4. **Eq. 11 (line 240):** Correct the Concordance Index formula to $\text{CI} = \frac{1}{Z}\sum_{y_t(i) > y_t(j)} f(y_p(i) - y_p(j))$ with $Z = \sum_{i,j}\mathbb{I}(y_t(i) > y_t(j))$.
