# Review of OOD_ANON_44

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.3 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.9/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents RNAmigos2, a structure-based deep learning virtual screening (VS) pipeline for RNA targets that represents 3D RNA binding pockets as directed 2.5D Leontis-Westhof base-pairing graphs enriched with 640-dimensional RNA-FM language model embeddings and 4-hop structural context. The framework uses two pre-trained encoders—an rGCN RNA encoder pre-trained via graphlet edit-distance metric learning on 200,000 non-redundant RNA 2-hop neighborhoods and an OptiMol GCN/VAE ligand encoder pre-trained on 1.5M ZINC compounds—paired with two decoders trained on 1,740 PDB RNA–ligand complexes clustered by 3D structural similarity (`RMalign` cutoff 0.75 into 367 training and 69 test binding-site groups): a binary compatibility decoder (`Compat`) trained with binary cross-entropy and a target-swapping margin loss to distinguish native PDB ligands from decoys, and a surrogate affinity decoder (`Aff`) trained to predict quantile-normalized `rDock` intermolecular scores across 1.3M synthetic docking runs (500 diverse drug-like ChEMBL compounds plus 264 PDB native ligands across the 1,740 pockets). Combining the two decoders via max-rank ensembling (`Mixed` / RNAmigos2) yields a mean AuROC of 0.972 (top 2.8% rank) on the 69 held-out PDB test pockets in seconds—outperforming standalone `rDock` (0.959 AuROC, $p = 0.026$) at a $10,000\times$ speedup—and achieves positive zero-shot enrichment (mean $\text{EF}_{1\%} = 2.93$, AuROC up to 0.66) across four unseen riboswitch targets (TPP, ZTP, $\text{SAM\_II}$, $\text{PreQ}_1$) in the 24,572-compound ROBIN in vitro small-molecule microarray dataset. All code, datasets, and trained weights are archived on GitHub and Zenodo.

The study is well-executed and addresses a genuine bottleneck in computational RNA drug discovery. The authors apply rigorous 3D structural clustering (`RMscore` $< 0.75$) for train/test splitting, explicitly test target specificity via Volkov-style target-shuffling controls, evaluate robustness to binding-site localization noise, and validate zero-shot generalization on a large independent experimental screening library (ROBIN). However, two methodological issues warrant closer scrutiny and refinement: (1) on the PDB/ChEMBL benchmark, the positive ligands are PDB co-crystallized ligands (many of which are cofactors, metabolites, or antibiotics) whereas the 500 negative decoys per pocket were filtered from ChEMBL using strict Lipinski-like drug-likeness cuts ($\text{MW} < 400$, rotatable bonds $< 5$, $\text{HBD} < 5$), creating a strong chemical distribution shift between actives and decoys that explains why target-shuffled RNAmigos2 still achieves 0.956 AuROC (vs. 0.981 unshuffled, line 74); and (2) several numerical inconsistencies appear between the main text, figures, and captions regarding test-set sample sizes ($n = 69$ vs. $n = 65$) and unperturbed AuROC values ($0.972$ vs. $0.981$). Addressing this active-vs-decoy chemical covariate shift and reconciling the numerical discrepancies will strengthen the paper.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **RNAmigos2 (`Mixed`) achieves a $10,000\times$ computational speedup over molecular docking (`rDock`) while matching or exceeding its virtual screening accuracy on structurally distinct RNA binding sites: [Well Supported].**  
  Timing benchmarks (5.8 ms/compound from SMILES and 1.6 ms/compound from precomputed graphs vs. 65 core-seconds/compound for `rDock`) and structural generalization across the `RMscore` $< 0.75$ split (Figs. 2c, 3a–b, 4b) confirm that the surrogate + compatibility ensemble reproduces and improves upon `rDock` rankings at a fraction of the compute cost.

* **RNAmigos2 generalizes zero-shot to unseen riboswitch targets in a 24,572-compound in vitro microarray screen (ROBIN), matching `rDock` enrichment and retrieving more chemically diverse active scaffolds: [Well Supported].**  
  On the four unseen ROBIN riboswitch targets (TPP, ZTP, $\text{SAM\_II}$, $\text{PreQ}_1$; Fig. 5, Supplementary Table 3), where both actives ($n_+ = 163\text{--}171$) and inactives ($n_- = 18,585\text{--}24,340$) come from the exact same experimental library (eliminating artificial PDB-vs-ChEMBL decoy bias), RNAmigos2 achieves statistically significant enrichment ($p = 3.73 \times 10^{-15}$ to $1.61 \times 10^{-6}$, mean $\text{EF}_{1\%} = 2.93$) in 2 CPU minutes vs. 1,000 CPU hours for `rDock`, while hybrid presorting (`RNAmigos++`) consistently improves time-bounded screening efficiency (Fig. 5c).

* **The margin loss equips RNAmigos2 with strong target specificity in the PDB/ChEMBL benchmark as demonstrated by the target-shuffling experiment: [Overstated].**  
  In the target-swapping control on the PDB/ChEMBL test set (Results, line 74; Fig. 2c), shuffling target–ligand pairings drops `Compat` by 41.7 AuROC points, but the `Aff` model drops by only 2.0 points and the final `RNAmigos2` (`Mixed`) model drops by only 2.5 points—from **98.1% to 95.6% AuROC**. A model that still achieves **0.956 AuROC** when tested on completely random, mismatched RNA pockets is primarily exploiting ligand-only chemical differences between the 264 PDB co-crystallized ligands (which did not undergo Lipinski filtering) and the 500 ChEMBL decoys (which were strictly filtered for $\text{MW} < 400$, rotatable bonds $< 5$, $\text{HBD} < 5$, $\text{HBA} < 10$, $\log P < 5$; lines 50 and 141). While the 2.5-point gap over the shuffled baseline is real and the ROBIN assay confirms true target-dependent signal, claiming high pocket specificity on the ChEMBL decoy benchmark when 95.6% AuROC is retained under random target permutation overstates the specificity of the max-rank ensemble.

* **RNAmigos2 is robust to binding-site boundary perturbations ($h$-hop noising and boundary shifting): [Moderately Supported].**  
  The perturbation experiments (Fig. 3c, d) show only a 0.7%–3.0% AuROC drop on the ChEMBL decoy benchmark when nodes are randomly sampled or shifted around the pocket. However, because the target-shuffled baseline on this same benchmark already yields 95.6% AuROC (a 2.5% drop) due to the 4-hop BFS graph expansion and ligand-only chemical bias, a 1.8%–3.0% drop under pocket shifting is nearly identical to replacing the pocket with an unrelated RNA structure.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Control for Active-vs-Decoy Chemical Property Bias in the PDB/ChEMBL Benchmark
* **WHY:** Applying strict drug-likeness filters ($\text{MW} < 400$, $<5$ rotatable bonds, $<5$ H-bond donors) exclusively to the ChEMBL decoys while leaving the 264 PDB native ligands unfiltered allows any ligand encoder (and `rDock`'s size-dependent intermolecular energy term) to separate PDB actives from ChEMBL decoys without using the RNA pocket structure, resulting in the 0.956 shuffled-target AuROC in Fig. 2c.
* **WHAT:** Report two bias-controlled metrics on the 69-group PDB test set: (a) native-ligand recovery ranking each test pocket's native ligand exclusively against the other 263 PDB native ligands (`PDB-only decoy set`), and (b) property-matched ChEMBL decoys where either the same Lipinski filter is applied to the test actives or decoys are matched to each active by molecular weight, heavy atom count, and $\log P$ (DUD-E style property matching).
* **HOW:** Using the existing precomputed `rDock` and `RNAmigos2` score matrices ($1740 \times (264 + 500)$), recompute test-set AuROC and shuffled-target AuROC when ranking solely within the 264 PDB ligands and within the subset of test actives that pass the ChEMBL drug-likeness filter.

#### 2. Evaluate Pocket Perturbation Sensitivity on the Unbiased ROBIN Dataset or `Compat`-Only Scores
* **WHY:** In Fig. 3c–d, the 1.8%–3.0% AuROC drop under severe pocket shifting is bounded below by the 95.6% ligand-bias floor of the `Aff` decoder on the ChEMBL decoy set, masking how much true pocket-specific signal is lost when the binding site is mislocalized.
* **WHAT:** Plot the pocket perturbation curves (noised and shifted, $h \in \{1, 2, 3\}$) separately for `Compat` (which drops 41.7 points under target shuffling) and on the 4 ROBIN riboswitch targets (where active and inactive ligands share the same library distribution).
* **HOW:** Run the 10-replicate node-sampling perturbation script (Supplementary Section E.2) on the 4 ROBIN PDB structures (`2gdi`, `5btp`, `2qwy`, `3fu2`) and on the `Compat` decoder alone, and add these curves to Fig. 3c–d or the Supplement.

#### 3. Replace Unweighted Max-Rank Ensembling with Tunable Weighted Rank/Score Mixing to Preserve Pocket Specificity
* **WHY:** Taking the simple maximum of the normalized ranks of `Aff` and `Compat` ($\max(r_{\text{Aff}}, r_{\text{Compat}})$) allows a ligand that scores near the top of `Aff` due to generic size/charge properties to receive a top final score even when `Compat` assigns it near-zero pocket compatibility, which collapses the 41.7-point specificity gap of `Compat` down to 2.5 points in `Mixed`.
* **WHAT:** Evaluate a weighted geometric or arithmetic mean of `Compat` and `Aff` ranks ($w \cdot r_{\text{Compat}} + (1-w) \cdot r_{\text{Aff}}$) across $w \in [0, 1]$ to characterize the Pareto frontier between unshuffled AuROC and target-shuffled specificity gap ($\Delta\text{AuROC}_{\text{swap}}$).
* **HOW:** Using the validation split or out-of-fold predictions, plot unshuffled AuROC, swapped AuROC, and ROBIN $\text{EF}_{1\%}$ as a function of the mixing weight $w$.

#### 4. Reconcile Numerical Discrepancies Between Main Text and Figure Captions
* **WHY:** Several sample sizes and AuROC values fluctuate across paragraphs without explanation.
* **WHAT & HOW:**
  1. Test-set pocket count: Lines 52, 66, and 150 state that the test set contains **69** binding site groups (and Fig. 3a caption states $n = 69$), whereas Fig. 2c caption (line 60) and line 64 state **$n = 65$**. Clarify why 4 binding sites were excluded in Fig. 2c / line 64.
  2. `Mixed` / `RNAmigos2` baseline AuROC: Line 64 reports **0.972** AuROC for `Mixed`, whereas lines 74 and 83 report **98.1%** (0.981) AuROC for the exact same unperturbed `RNAmigos2` model on the same test set. Harmonize or explain the difference between the 0.972 and 0.981 figures.
  3. ROBIN compound count: The Abstract (line 8) and Introduction (line 25) state *"20,000 compounds"*, Discussion (line 117) states *"25k compounds"*, and Results (line 108) states *"24,572 assayed molecules"*, while Fig. 5b caption lists target-specific totals of $163+24340 = 24,503$ (TPP) down to $171+18585 = 18,756$ (ZTP). State the exact library size ($24,572$) consistently across sections.
  4. Typo in Introduction (line 17): Fix *"risdipalm"* to *"risdiplam"*, and in Methods (line 127): complete the truncated sentence *"come from protein chains, following."* (missing reference number).
