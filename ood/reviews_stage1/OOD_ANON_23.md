# Review of OOD_ANON_23

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.6 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 2.1/3.5 | Claims: 1.6/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces `iNGNN-DTI`, a deep learning architecture for binary drug–target interaction (DTI) prediction that integrates (1) a $k$-subgraph nested graph neural network (NGNN) with a virtual node operating on RDKit molecular graphs and AlphaFold2-derived $8\text{ \AA}$ $\text{C}_\alpha$ contact graphs, (2) a cross-attention-free transformer (cross-AFT) interaction module, and (3) pre-trained 1D sequence embeddings from Chemformer (for SMILES) and ESM (for protein sequences). Evaluated across three benchmark datasets (DAVIS, KIBA, and BIOSNAP) under random 7:1:2 train/validation/test splits and on unseen-drug/unseen-protein splits of DAVIS, the model achieves modest gains in AUROC and AUPRC over four baselines (DeepDTA, MolTrans, ML-DTI, and DGraphDTA). The authors also visualize implicit cross-AFT weights on four crystal structures and conduct a virtual screening case study against human ACE2 using BIOSNAP drugs. Source code is publicly provided on GitHub.

Combining 3D contact graphs predicted by AlphaFold2 with $k$-hop subgraph pooling and pre-trained sequence encoders is a sensible architectural synthesis. However, the manuscript has several methodological and mathematical issues that weaken its core claims: (1) the mathematical formulation of the feature fusion and implicit attention equations (Equations 2, 9–12, and 15) contains dimensionality mismatches and indexing errors (omitting the graph-level pooling operator needed to collapse node-level matrices $Y_{\text{drug}} \in \mathbb{R}^{N_{\text{drug}} \times d}$ before concatenating with global vectors $P_{\text{drug}} \in \mathbb{R}^{128}$); (2) the ablation study (Table 6) contradicts the narrative that combining cross-AFT and pre-trained embeddings improves both metrics, as NGNN + cross-AFT *without* pre-trained models achieves higher AUPRC ($0.478$) than the full `iNGNN-DTI` model ($0.473$); (3) on the realistic unseen-drug split (Table 5), variance across the five runs is large ($\text{AUROC} = 0.763 \pm 0.049$ vs. $0.744 \pm 0.054$ for MolTrans) with no formal significance testing; and (4) the COVID-19 case study relies on uncalibrated docking scores that favor high-molecular-weight compounds (such as erythromycin at $-14.5\text{ kcal/mol}$) and conflates host metalloproteinase inhibition (marimastat) with direct ACE2 receptor binding. These issues can be addressed through rigorous ablation extensions, statistical testing on cold-start splits, and mathematical corrections.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **`iNGNN-DTI` outperforms baseline models on random 7:1:2 splits of DAVIS, KIBA, and BIOSNAP: [Moderately Supported].**  
  Under random pair splitting (Table 4), `iNGNN-DTI` achieves the highest mean AUROC and AUPRC across all three datasets, with the largest gain on imbalanced DAVIS ($\text{AUPRC} = 0.473 \pm 0.0167$ vs. $0.381 \pm 0.0247$ for ML-DTI) and a minimal gain on KIBA ($\text{AUROC} = 0.915$ vs. $0.912$). However, because DAVIS ($68 \times 442 = 30,056$ pairs) is a fully dense Cartesian matrix of 68 drugs and 442 kinases, random pair splitting is purely transductive: every drug and every protein in the test set is already seen dozens of times during training. Furthermore, the baselines were not augmented with Chemformer and ESM embeddings, making it unclear on KIBA and BIOSNAP how much of the gain comes from the NGNN/cross-AFT architecture versus the 250M-sequence ESM and 100M-SMILES Chemformer pre-trained representations.

* **`iNGNN-DTI` generalizes significantly better to unseen drugs and unseen protein targets: [Fragile].**  
  In Table 5 (unseen drugs and unseen proteins on DAVIS), `iNGNN-DTI` has the highest point estimates, but the standard deviations across the 5 random splits are very wide and overlap heavily with the baselines (unseen drug AUROC: $0.763 \pm 0.0490$ for `iNGNN-DTI` vs. $0.744 \pm 0.0540$ for MolTrans; unseen drug AUPRC: $0.224 \pm 0.0640$ vs. $0.169 \pm 0.0730$ for ML-DTI; unseen protein AUROC: $0.867 \pm 0.0357$ vs. $0.840 \pm 0.0357$ for ML-DTI). Moreover, the manuscript does not evaluate the hardest cold-start regime (both drug and protein simultaneously unseen), nor does it perform unseen-drug/target experiments on KIBA or BIOSNAP (given that DAVIS has only 68 drugs total, a 20% test split contains only ~13 drugs).

* **Both the cross-AFT interaction module and the pre-trained sequence encoders contribute synergistically to model performance: [Overstated].**  
  In the ablation study on DAVIS (Table 6), adding pre-trained embeddings alone to NGNN (Test 4 vs. Test 2) causes AUPRC to *drop* from $0.464 \pm 0.0357$ to $0.431 \pm 0.0103$, and the model with NGNN + cross-AFT alone (Test 3) achieves the highest AUPRC in the entire paper ($0.478 \pm 0.0222$), outperforming the full `iNGNN-DTI` model (Test 5: $0.473 \pm 0.0167$). In addition, no ablation is provided for the unseen-drug/unseen-protein splits, where pre-trained sequence encoders are explicitly hypothesized to help most, nor is an ablation provided for the virtual node (Equations 5–6).

* **Cross-AFT implicit attention weights accurately localize protein binding pockets and identify valid ACE2-binding COVID-19 therapeutics: [Overstated].**  
  As the authors candidly note in the Conclusion (line 422), "the attention weights assigned to the protein target do not always exhibit a strong correlation with the actual positions of the residues." Quantitative enrichment of binding-site residues (e.g., ROC-AUC or precision@$k$ against true PDB contact residues within $5\text{ \AA}$ of the ligand) is not computed; instead, four qualitative examples are shown. In the COVID-19 ACE2 case study (Section 3.5), comparing mean blind docking scores of the top 50 ($-6.84\text{ kcal/mol}$) vs. top 50–100 ($-6.49\text{ kcal/mol}$) predicted compounds without controlling for molecular weight or comparing against random BIOSNAP molecules is uninformative. Moreover, citing marimastat (a broad-spectrum matrix metalloproteinase inhibitor that blocks host MMP-mediated viral entry, not ACE2) as validation of predicted ACE2 binding conflates distinct biological targets.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct Mathematical Equations for Feature Readout, Implicit Attention, and PPM
* **WHY:** Equations (2), (9)–(12), and (15) contain mathematical and dimensional errors that prevent a reader from reproducing the architecture from the text:
  1. In Equations (9)–(10), $Y_{\text{drug}} \in \mathbb{R}^{N_{\text{drug}} \times d}$ and $Y_{\text{prot}} \in \mathbb{R}^{N_{\text{prot}} \times d}$ are variable-length node-level matrices, whereas $P_{\text{drug}}, P_{\text{prot}} \in \mathbb{R}^{128}$ in Equations (11)–(12) are fixed-length graph-level vectors. Concatenating $Y_{\text{drug}}$ and $P_{\text{drug}}$ directly via $F_{\text{drug}} = \text{FC}([Y_{\text{drug}} \cdot P_{\text{drug}}])$ is dimensionally invalid without an explicit node-pooling/readout operation (e.g., global mean or max pooling over $N_{\text{drug}}$).
  2. In Equation (15), the drug query index and protein key index are both written as $n$, and the pairwise bias in the numerator is written as $w_n$ instead of $w_{n,n'}$.
  3. In Equation (2), the pseudocount term in the numerator is $p/4$ (appropriate for 4 nucleotides, not $R = 20$ or $21$ amino acids).
* **WHAT & HOW:**
  1. Explicitly write the readout pooling function $\tilde{y}_{\text{drug}} = \text{Pool}_{n=1}^{N_{\text{drug}}}(Y_{\text{drug}}^n) \in \mathbb{R}^d$ between Equations (10) and (11), and use $\tilde{y}_{\text{drug}}$ and $\tilde{y}_{\text{prot}}$ in Equations (11)–(12).
  2. Fix Equation (15) to distinguish drug atom index $m \in \{1,\dots,N_{\text{drug}}\}$ from protein residue index $n \in \{1,\dots,N_{\text{prot}}\}$:
     $$a_{\text{drug}}^{m,n,i} = \sigma_q(Q_{\text{drug}}^{m,i}) \frac{\exp(K_{\text{prot}}^{n,i} + w_{m,n})}{\sum_{n'=1}^{N_{\text{prot}}} \exp(K_{\text{prot}}^{n',i} + w_{m,n'})}.$$
  3. Check and correct the PPM pseudocount prior in Equation (2) ($p/20$ or $p/21$, or explain why $p/4$ was used in the preprocessing code). Also fix Table 2 descriptions for "Number of Hydrogens" and "Number of implicit Hydrogens", which represent covalent attached hydrogen counts, not "Number of hydrogen bonds".

#### 2. Expand the Ablation Study to Cold-Start Splits and Isolate the Effect of Pre-Trained Encoders
* **WHY:** In Table 6 (random split on DAVIS), adding Chemformer + ESM to NGNN + cross-AFT slightly reduces AUPRC ($0.478 \to 0.473$), leaving the practical benefit of the pre-trained sequence encoders unproven in the main ablation. Conversely, pre-trained models should provide the largest gains when generalizing to unseen drugs and unseen proteins (Table 5).
* **WHAT:** Run the 5-row ablation configuration of Table 6 on the unseen-drug and unseen-protein splits of DAVIS (and ideally KIBA), and add a row ablating the virtual node (Equations 5–6) and a baseline where DGraphDTA is also given the Chemformer + ESM features.
* **HOW:** Using the existing training scripts in `iNGNN-DTI`, evaluate configurations 1–5 from Table 6 on the 5 unseen-drug and 5 unseen-protein folds, report paired $t$-tests or Wilcoxon signed-rank tests across folds, and discuss why AUPRC decreased when adding unsupervised features on the random split (Test 4 vs. Test 2).

#### 3. Quantify Binding-Site Localization Accuracy Across All PDB-Mapped Complexes
* **WHY:** Visual inspection of four selected proteins (Section 3.3.1) does not establish whether cross-AFT implicit attention weights statistically enrich for true binding-site residues above random chance or surface-loop baselines.
* **WHAT:** Compute a quantitative binding-site localization metric across all positive DTI pairs in the test set that have solved co-crystal structures in the PDB.
* **HOW:** For each solved complex, define ground-truth binding residues as those with heavy atoms within $5.0\text{ \AA}$ of the co-crystallized ligand. Rank all protein residues by their L2-norm or mean across dimensions $i=1,\dots,d$ of the implicit attention score $\sum_{m} a_{\text{drug}}^{m,n,i}$, and report the mean AUROC and top-$k$ precision compared to a random baseline.

#### 4. Add a Random-Drug Null Control and Correct Target Attribution in the COVID-19 Case Study
* **WHY:** Reporting that the top 50 predicted drugs have a mean docking score of $-6.84\text{ kcal/mol}$ vs. $-6.49\text{ kcal/mol}$ for ranks 51–100 does not compare against the background distribution of the 4,510 BIOSNAP compounds, and citing marimastat (an MMP inhibitor) as literature support for ACE2 binding is biologically inaccurate.
* **WHAT:** Compare the top-50 docking score distribution (and ligand efficiency, i.e., docking score divided by heavy atom count) against 50 randomly sampled BIOSNAP drugs using a Mann–Whitney U test, and revise the text on marimastat and erythromycin to clarify that literature associations with SARS-CoV-2 entry pathways do not constitute experimental confirmation of direct ACE2 binding.
* **HOW:** Sample 50 random drugs from BIOSNAP, run the identical DockCoV2 pipeline, plot their distribution alongside the top 50 and top 50–100 in Figure 7, and revise Section 3.5 (line 399) to accurately distinguish host metalloproteinase inhibition from direct ACE2 receptor antagonism.
