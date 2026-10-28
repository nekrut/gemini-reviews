# Review of OOD_ANON_34

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.4 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.7/3.5 | Claims: 2.0/2.5 | Biology: 1.7/2.0 | Reproducibility: 2.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript audits structural train–test data leakage and within-training-set redundancy between the PDBbind (v.2020, $N = 18,623$) database and the CASF-2013 ($N = 195$) and CASF-2016 ($N = 285$) protein–ligand binding affinity benchmarks. Using a multimodal filtering pipeline combining protein structural alignment (TM-align), ligand chemical similarity (2048-bit radius-2 count Morgan Tanimoto), pocket-aligned ligand nearest-atom RMSD, and affinity differences ($\Delta\text{p}K$), the authors construct `PDBbind CleanSplit` by removing 711 train–test overlapping complexes and 1,451 redundant training complexes. They show that a 5-nearest-neighbor lookup baseline (`Search top 5 complexes`) achieves $R = 0.716$ ($\text{RMSE} = 1.517$) on unfiltered PDBbind, and that retraining Pafnucy and GenScore on CleanSplit degrades their CASF-2016 accuracy. They also introduce GEMS, a sparse heterogeneous protein–ligand graph neural network (GATv2Conv and EdgeConv) initialized with ESM2, Ankh, and ChemBERTa-2 embeddings, which achieves $\text{RMSE} = 1.308$ ($R = 0.803$) on CASF-2016 when trained on CleanSplit. Complete code, model weights, Docker containers, precomputed graphs, and full pairwise similarity matrices are publicly archived on GitHub and Zenodo.

This is a well-designed, highly reproducible methodological and benchmarking study backed by informative controls (5-NN memorization baselines, ligand-only protein-ablation experiments, evaluation on the 144-complex pre-filtering independent subset of CASF-2016, and external OOD testing). Two methodological caveats warrant attention: first, the train–test filtering rule conditions on the test set's ground-truth affinity label ($|\Delta\text{p}K| \le 1.0$; Fig. 1b), which retains structurally homologous train–test pairs that differ in affinity by $> 1\text{ p}K$ unit ("activity cliffs") and therefore means `CleanSplit` is not strictly free of target/ligand homologs; second, GEMS underwent architectural and embedding optimization after observing initial CleanSplit results (line 97), whereas baseline models (Pafnucy, GenScore) were evaluated with fixed off-the-shelf hyperparameters. Both issues can be addressed through targeted sensitivity analyses using the authors' precomputed similarity matrices.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Unfiltered PDBbind suffers from extensive train–test overlap with CASF-2016 (affecting 49% of CASF complexes), allowing simple nearest-neighbor memorization to match published deep-learning scoring functions: [Well Supported].**  
  The `Search top 5 complexes` ($R = 0.716, \text{RMSE} = 1.517$) and `Search top 5 ligands` ($R = 0.707, \text{RMSE} = 1.539$) baselines (Table 1, Fig. 3a–b), combined with the ligand-only ablation of GEMS on unfiltered PDBbind ($\text{RMSE} = 1.424$, Fig. 5a), provide direct empirical proof that memorization of homologous complexes and ligands drives a large fraction of reported CASF-2016 performance.

* **Removing within-training-set redundancy ($N = 1,451$ complexes) lowers cross-validation scores (by curbing within-cluster memorization) while improving generalization to the independent CASF subset: [Well Supported].**  
  Figure 5b–c and Extended Data Fig. 2b–c demonstrate that training GEMS on `CleanSplit` improves RMSE on the 144 strictly independent CASF-2016 complexes from $1.483$ (unfiltered PDBbind) to $1.367$ (`CleanSplit`), and that removing protein nodes on `CleanSplit` collapses performance ($\text{RMSE} = 1.572$, Fig. 5a), confirming that the model relies on protein–ligand interaction features when leakage is removed.

* **`PDBbind CleanSplit` excludes all training complexes that remotely resemble any CASF test complex, turning CASF into a strictly independent external test set: [Overstated].**  
  In Main text lines 25, 51, and 138, the authors state that "all protein–ligand complexes that remotely resembled any from the CASF test set were excluded from training." However, as shown in Fig. 1b and Methods ("Removal of train–test overlap"), a training complex with $\text{TM-score} > 0.8$ and $T + (1 - \text{r.m.s.d.}) > 0.8$ is *only* excluded if its experimental affinity is within $\pm 1.0\text{ p}K$ of the test complex, and proteins sharing the same target fold ($\text{TM-score} > 0.8$) are retained whenever $T + (1 - \text{r.m.s.d.}) \le 0.8$. Conditioning train–test filtering on the test label $y_{\text{test}}$ leaks test-label information into the split definition and selectively leaves behind structural homologs whose affinities diverge by $> 1.0\text{ p}K$ from the test complex, which actively penalizes nearest-neighbor interpolators on those complexes.

* **GEMS substantially outperforms Pafnucy and GenScore under leakage-free training on `PDBbind CleanSplit`: [Moderately Supported].**  
  Across 5 random seeds of 5-fold cross-validation, GEMS ($\text{RMSE} = 1.308, R = 0.803$) outperforms GenScore ($\text{RMSE} = 1.362, R = 0.780$) and Pafnucy ($\text{RMSE} = 1.484, R = 0.746$) on `CleanSplit` (Fig. 3). However, line 97 notes that GEMS underwent "substantial architectural optimizations and the integration of language model embeddings" after initial training on `CleanSplit` yielded lower benchmark performance, whereas Pafnucy and GenScore were retrained with their default architectures and lacks pretrained ESM2/Ankh/ChemBERTa-2 features.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Evaluate a Label-Agnostic Structural Split ($\Delta\text{p}K$ Criterion Removed)
* **WHY:** Filtering train–test pairs based on $|\text{p}K_{\text{train}} - \text{p}K_{\text{test}}| \le 1.0$ uses the ground-truth test label to curate the training set and selectively retains structurally homologous "activity cliff" pairs with $|\Delta\text{p}K| > 1.0$, which biases local similarity methods downward and contradicts the claim that all structurally similar complexes were removed.
* **WHAT:** Generate a strictly label-agnostic variant of `CleanSplit` (removing the $\Delta\text{p}K \le 1.0$ condition in layer 1 of Fig. 1b) and report the performance of `Search top 5 complexes`, Pafnucy, GenScore, and GEMS on this split.
* **HOW:** Using the precomputed pairwise similarity matrices on Zenodo, remove all training complexes with $(\text{TM-score} > 0.8 \text{ and } T + 1 - \text{r.m.s.d.} > 0.8)$ or $(T > 0.9)$ regardless of $\Delta\text{p}K$, retrain the 5-fold models, and add this comparison to Fig. 5c / Extended Data Fig. 4.

#### 2. Add a Cold-Target ($\text{TM-score} \le 0.8$ or $\le 0.5$) Generalization Benchmark
* **WHY:** Because the current filtering allows training complexes with $\text{TM-score} > 0.8$ (identical target protein to a CASF cluster) to remain in `CleanSplit` whenever their bound ligands have $T + (1 - \text{r.m.s.d.}) \le 0.8$, models can still leverage target-specific binding-pocket embeddings learned from other ligands bound to the same protein.
* **WHAT:** Quantify how GEMS, GenScore, and Pafnucy perform when all training complexes with $\text{TM-score} > 0.8$ (and $\text{TM-score} > 0.5$) to any CASF-2016 target are excluded regardless of ligand similarity.
* **HOW:** Extend Extended Data Fig. 4d–f to include a pure protein-structure exclusion threshold ($\text{TM-score} > 0.5$ and $> 0.8$ without requiring ligand overlap) to measure true zero-shot target generalization.

#### 3. Normalize the Pocket-Aligned Ligand RMSD Term in the Combined Similarity Metric
* **WHY:** In the criterion $T + (1 - \text{r.m.s.d.}) > 0.8$, Tanimoto similarity $T \in [0, 1]$ is dimensionless whereas $\text{r.m.s.d.}$ is in Ångströms ($\text{\AA}$) and unbounded above $1\text{ \AA}$. Consequently, an $\text{r.m.s.d.}$ of $1.3\text{ \AA}$ (still well within the same binding pocket) yields $1 - \text{r.m.s.d.} = -0.3$, allowing chemically similar ligands ($T = 0.85$) in the same pocket to pass unfiltered ($0.85 - 0.30 = 0.55 \le 0.8$).
* **WHAT:** Clarify or compare a bounded transformation of ligand RMSD, such as $\exp(-\text{r.m.s.d.}/d_0)$ or $\max(0, 1 - \text{r.m.s.d.}/d_{\max})$ with $d_{\max} \approx 2\text{--}4\text{ \AA}$.
* **HOW:** Document the exact distribution of $T + (1 - \text{r.m.s.d.})$ in the Methods and report whether clipping or scaling the $\text{r.m.s.d.}$ term alters the set of 711 excluded overlap complexes.

#### 4. Temper Claims of Complete Structural Separation in the Abstract, Main Text, and Discussion
* **WHY:** Statements that "all protein–ligand complexes that remotely resembled any from the CASF test set were excluded from training" (line 25; also lines 51, 138) overstate a filter that retains homologous proteins ($\text{TM} > 0.8$) bound to different ligands as well as homologous protein–ligand poses with $|\Delta\text{p}K| > 1.0$.
* **WHAT:** Revise these sentences to accurately describe the joint protein-structure, ligand-pose, and affinity-similarity criteria.
* **HOW:** Replace "all protein–ligand complexes that remotely resembled any from the CASF test set" in line 25 with "all training complexes sharing high protein, ligand, binding-pose, and affinity similarity with any CASF test complex."
