# Review of OOD_ANON_42

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.1 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.7/3.5 | Claims: 1.3/2.5 | Biology: 1.0/2.0 | Reproducibility: 1.1/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces GraphscoreDTA, a graph neural network (GNN) architecture for predicting protein–ligand binding affinity ($\text{p}K_a = -\log_{10} K_d, K_i, \text{ or } \text{IC}_{50}$) from 3D protein–ligand structures. The model combines three GNN blocks (protein residue contact graph at an 8 Å cutoff, ligand molecular graph with a virtual super node, and a radial distance-weighted pocket–ligand interaction graph) with a bi-transport cross-attention mechanism, gated recurrent units (GRUs), skip connections, and six pre-computed AutoDock Vina scoring terms (three steric terms, hydrophobic, hydrogen bond, and active rotatable bonds). The authors train on 13,851 complexes from PDBbind v2019 (split 7:1:2 via single-linkage clustering at a 0.3 similarity threshold) and evaluate on CASF2016 ($n = 279$) and CASF2013 ($n = 182$), as well as subsets of cyclin-dependent kinases (CDKs), AlphaFold2-predicted structures, and homologous protein families. Source code is provided on GitHub.

While integrating explicit physics-based Vina terms with pocket–ligand GNN representations is a reasonable engineering design, the study suffers from a major benchmark leakage flaw and internal mathematical inconsistencies that invalidate its primary generalization claims. Specifically, the authors filter the 13,851 PDBbind complejos only for exact ID non-overlap with CASF2016 and CASF2013 (Section 2.1, criterion v), and then apply compound-similarity and protein-similarity clustering solely within the 13,851 PDBbind dataset to form the 7:1:2 train/validation/internal-test split—while reporting Tables 1 and 2 exclusively on the fixed CASF2016 and CASF2013 benchmarks without removing training proteins or ligands that share $>0.3$ similarity (or identical targets, such as the CDK1/2/8/9 and homologous family complexes) with CASF2016/2013. In addition, Equations 1–10 contain dimension and index errors, and the CDK and homologous-family case studies are drawn directly from the constructed datasets without verifying train–test separation. Re-evaluating the model under strict cross-split de-duplication against CASF2016/2013 and correcting the mathematical formulations are necessary to establish the true performance of GraphscoreDTA.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **GraphscoreDTA outperforms existing sequence- and structure-based methods under compound-similarity and protein-similarity clustering on CASF2016 and CASF2013 (Tables 1 and 2): [Methodologically Flawed].**  
  In Section 2.1 (lines 36–44), the authors remove exact complex overlaps between PDBbind v2019 ($n = 13,851$) and the fixed CASF2016 ($n = 279$) and CASF2013 ($n = 182$) sets, and then cluster the 13,851 complexes at a 0.3 Smith–Waterman or compound similarity threshold to divide PDBbind into 7:1:2 training, validation, and internal test sets. However, CASF2016 is the core set of PDBbind, meaning virtually every one of the 279 CASF2016 complexes has dozens of homologous protein structures (often 90–100% sequence identity) and close chemical analogues in the remaining 13,851 PDBbind refined/general set. Because the similarity clustering was only applied to partition the 13,851 complexes into 7:1:2 (training on 70% of all clusters) rather than excluding training clusters that share $>0.3$ similarity with CASF2016/2013, evaluating the resulting models on CASF2016 and CASF2013 does not test out-of-cluster protein or compound generalization.

* **Case studies on CDK9/CDK1/CDK2/CDK8 (Section 3.6) and 8 homologous protein families (Section 3.8) demonstrate strong drug–target selectivity: [Fragile].**  
  Sections 3.6 and 3.8 state that complexes of CDK9 ($n=11$), CDK1 ($n=5$), CDK2 ($n=77$), CDK8 ($n=21$), and 8 homologous families ($n=191$ ligands) were *"collected from the constructed datasets"* (lines 293, 295, 311). The manuscript never specifies whether these complexes were restricted to the held-out 20% test split or included complexes from the 70% training and 10% validation splits, nor whether homologous kinase structures were excluded from training. Evaluating prediction error ($\text{RMSE} = 0.470$ on CDK9) on complexes that overlap with or are homologous to the training set confounds memorization with target selectivity.

* **Combining mutual information (bi-transport attention), individual GNNs, pocket–ligand GNNs, and Vina distance terms improves affinity prediction (Section 3.2, Supplementary Table S4): [Moderately Supported].**  
  The ablation experiments (Models I–IV and component removals) show consistent incremental improvements when evaluated on the same benchmark split, though no standard deviations across random seeds or statistical significance tests are reported despite training 100 times and selecting the single best validation model (Section 2.3, line 54).

* **GraphscoreDTA maintains predictive accuracy ($\text{RMSE} \approx 1.01$) when experimental structures are replaced by AlphaFold2 structures and AutoDock Vina docked poses (Section 3.5): [Fragile].**  
  In the first experiment (line 288), AlphaFold2 apo structures are structurally aligned to the native holo crystal structures and paired with the native co-crystallized ligand poses in the crystal coordinate frame, which leaks experimental binding site coordinates and ligand conformations. In the second experiment using AutoDock Vina docked poses, the authors do not specify whether binding site boxes were defined using the native co-crystallized ligand coordinates (redocking into a known site) or blind pocket prediction, and why the average RMSE on the 140 CASF2016 subset ($1.008\text{--}1.010$) is substantially lower than the crystal-structure RMSE on full CASF2016 ($1.249\text{--}1.349$ in Tables 1–2).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Enforce Strict Similarity-Based De-Duplication Between PDBbind Training Data and CASF2016/2013
* **WHY:** Clustering the 13,851 PDBbind complexes into 7:1:2 splits ensures that the 70% training set and 20% internal PDBbind test set live in disjoint clusters, but leaves ~70% of all protein families and compound scaffolds in the training set when testing on the external CASF2016 and CASF2013 benchmarks.
* **WHAT:** Report performance on (a) the actual held-out 20% PDBbind test splits generated by the compound-similarity and protein-similarity clustering, and (b) CASF2016/2013 after removing all PDBbind training complexes with Smith–Waterman protein similarity $>0.3$ (for protein-split) or Tanimoto ligand similarity $>0.3$ (for compound-split) to any complex in CASF2016/2013.
* **HOW:** Filter the 13,851 PDBbind dataset against CASF2016/2013 using the existing Smith–Waterman and Tanimoto distance matrices prior to training, retrain GraphscoreDTA and baseline models, and update Tables 1 and 2 with both internal-test and de-duplicated CASF results.

#### 2. Eliminate Training-Set Overlap in the CDK, Catechol, and Homologous Family Evaluations
* **WHY:** Selecting target subsets from *"the constructed datasets"* without holding out the entire target family during training invalidates selectivity claims.
* **WHAT:** Ensure that all complexes evaluated in Sections 3.6, 3.7, and 3.8 were strictly excluded from the training and validation sets.
* **HOW:** For the CDK evaluation (Section 3.6) and the 8 homologous families (Section 3.8), train the model on a split where the respective UniProt IDs (and homologs above 30% sequence identity) are held out entirely from training, and report the out-of-sample $R$, CI, RMSE, and top-$k$ hit rates.

#### 3. Report Multi-Seed Uncertainty and Statistical Comparisons Across Ablations and Baselines
* **WHY:** Training 100 times and picking the single run with the best validation score without reporting variance across runs makes it impossible to tell whether small differences (e.g., Model III vs. Model IV, or 8 Å vs. 10 Å cutoff) exceed random initialization noise.
* **WHAT:** Report mean $\pm$ SD across at least 5–10 independent random seeds and paired bootstrap or Wilcoxon signed-rank $p$-values comparing GraphscoreDTA to DeepDTAF and Fusion model.
* **HOW:** Aggregate test-set metrics across the top-performing independent training seeds in the existing pipeline and add $\pm\text{SD}$ columns to Tables 1, 2, and S4.

#### 4. Clarify Pocket Definition in the AlphaFold2 + AutoDock Vina Experiment
* **WHY:** In realistic structure-free scenarios, neither the crystal protein structure nor the crystal ligand coordinates are available to define the AutoDock Vina search box. Furthermore, the reported $\text{RMSE} = 1.010$ on the 140-complex subset is much lower than the $1.249$ full-CASF2016 RMSE, suggesting subset selection bias.
* **WHAT:** Report the baseline crystal-structure GraphscoreDTA RMSE on the exact same 140-complex subset for a matched comparison, and clarify how the docking box center and dimensions were determined on the unaligned AlphaFold2 structures.
* **HOW:** Compute the native-structure RMSE on those 140 PDB IDs, and run blind pocket detection (e.g., P2Rank or fpocket) on the unaligned AlphaFold2 structures before Vina docking to measure fully experimental-structure-free accuracy.

#### 5. Fix Mathematical Dimension and Indexing Errors in Equations 1–10 and 18
* **WHY:** Several equations in Section 2.3 have mismatched matrix dimensions or inconsistent head indices that prevent independent re-implementation from the text.
* **WHAT & HOW:**
  1. Equations 1–4 (lines 65–96): $X_p$ is defined as $\mathbb{R}^{n \times c}$, yet Eq. 3 writes $T = w_p X_p \in \mathbb{R}^{s \times n}$ and Eq. 4 writes $B = w_t X_p \in \mathbb{R}^{h \times n}$, which requires $X_p^T \in \mathbb{R}^{c \times n}$ with $w_p \in \mathbb{R}^{s \times c}$ and $w_t \in \mathbb{R}^{h \times c}$. Likewise, in Eq. 1, $g_i \in \mathbb{R}^{s \times 1}$ requires $w_g$ to map from $\mathbb{R}^{s \times 1}$ to $\mathbb{R}^{1 \times c}$ (e.g., $G_p = (\frac{1}{h}\sum_i g_i)^T W_g$).
  2. Equations 6–7 (lines 100–113): $X_l \in \mathbb{R}^{m \times c}$ and $G_p \in \mathbb{R}^{1 \times c}$, so $a_l = \text{softmax}(w_l X_l^T w_g G_p)$ has incompatible inner dimensions unless $X_l$ and $G_p^T$ are projected into a shared hidden dimension $d$ such that $a_l \in \mathbb{R}^{m \times 1}$ (or $\mathbb{R}^{m \times c}$). Specify the exact dimensions of $w_l$, $w_g$, and $a_l$.
  3. Equations 8–10 (lines 119–136): The text states *"we used $K = 4$ parallel attention heads"*, but Eqs. 9 and 10 write $k = 1, 2, 3$ instead of $k = 1, \dots, K$, and Eq. 9 writes *"where $i$ is the number of ligand atoms"* when $i \in \{1, \dots, n\}$ is the atom index.
  4. Equation 18 (line 198): The standard Behler–Parrinello cosine cutoff function is $\frac{1}{2}[\cos(\pi r_{ij}/R_C) + 1]$ so that $f_c(0) = 1$ and $f_c(R_C) = 0$. As written ($\frac{1}{2}\cos(\pi r_{ij}/R_C)$), the cutoff function becomes negative for $4\text{ Å} < r_{ij} \le 8\text{ Å}$ and discontinuous at $r_{ij} = 8\text{ Å}$ ($-0.5$ vs. $0$). Correct the missing $+1$ inside the parentheses.
