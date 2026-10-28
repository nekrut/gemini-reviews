# Review of OOD_ANON_29

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.4 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.6/3.5 | Claims: 1.4/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.1/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript combines a multi-stage virtual screening cascade (Glide HTVS $\to$ SP $\to$ XP on 1.6 million ChemDiv and MedChemExpress molecules against human JNK3, PDB ID: `7S1N`) with MM/GBSA, DeepDock, and a custom Graph Attention Network (GAT) rescoring model trained on 1,072 ChEMBL JNK3 inhibitors. Ten candidate compounds were selected for *in vitro* kinase testing at $25\text{ \mu M}$, yielding one potent hit—Compound 6 (*N*-(4-(2-ethyl-4-(*m*-tolyl)thiazol-5-yl)pyridin-2-yl)benzamide)—with $99.73\%$ inhibition at $25\text{ \mu M}$ and an enzymatic $\text{IC}_{50}$ of $130.1\text{ nM}$. Compound 6 was subsequently tested at $5\text{ \mu M}$ and $10\text{ \mu M}$ in LPS-stimulated RAW264.7 macrophages for TNF-$\alpha$ and IL-6 suppression and analyzed by Binding Pose Metadynamics (BPMD) and Amber molecular dynamics (MD) simulations.

Unlike purely *in silico* screens, this study includes wet-lab biochemical validation that successfully identifies a genuine $130.1\text{ nM}$ JNK3 inhibitor (Compound 6). However, the computational and biological methodology has several substantial flaws and internal contradictions: (1) Table 1 shows that the custom GNN rescoring model actually ranked Compound 6 poorly (`pIC50 Predicted = 5.82`, 5th of 10), whereas its highest-predicted molecule (Compound 3, `pIC50 Predicted = 6.84`) was completely inactive in the biochemical assay ($5.70\%$ inhibition at $25\text{ \mu M}$), yielding a negative correlation ($r = -0.15$) between GNN predictions and wet-lab inhibition across the 10 tested compounds; (2) the cellular anti-inflammatory assay in RAW264.7 macrophages ($5–10\text{ \mu M}$ for 48 hours total incubation) lacks a cytotoxicity/cell-viability control (e.g., CCK-8/MTT) and tests a brain-specific kinase (JNK3) in peripheral macrophages without assessing off-target JNK1/JNK2/p38 inhibition; (3) the MD simulation duration in the Results (Section 2.7: *"three parallel sets of 100 ns molecular dynamics simulations"*) directly contradicts the Materials and Methods (Section 4.8: *"40 ns of... NPT... to equilibrate the system, which was followed by 30 ns of production simulation"*); and (4) neither the GNN source code nor the 1072-compound training split is publicly archived. Addressing these issues requires transparent benchmark evaluation of the GNN, reconciling the MD and docking protocols, and adding cytotoxicity/selectivity controls or qualifying the macrophage claims.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Compound 6 is a potent *in vitro* enzymatic inhibitor of JNK3 ($\text{IC}_{50} = 130.1\text{ nM}$) interacting with the hinge residue Met149 and Lys93: [Well Supported].**  
  The biochemical HTRF/TR-FRET kinase assay across a 6-point 10-fold dilution series ($0.1\text{ nM}$ to $10,000\text{ nM}$; Figure 4B) and the single-concentration screen at $25\text{ \mu M}$ ($99.73 \pm 0.44\%$ inhibition; Table 1) provide solid experimental evidence of nanomolar enzymatic inhibition, and the 2-aminopyridine/benzamide hinge-binding motif forming bidentate hydrogen bonds with Met149 in BPMD/MD is structurally consistent with known kinase hinge binders.

* **The DeepDock + GAT Graph Neural Network rescoring model accurately predicts JNK3 potency ($R^2 = 0.7228$) and drives the successful selection of active hits: [Overstated].**  
  First, the ChEMBL dataset ($n = 1,072$) was split randomly 8:1:1 rather than by molecular scaffold, which allows close structural analogs in congeneric medicinal chemistry series to leak between training and test sets. Second, when evaluated prospectively on the 10 purchased compounds (Table 1), the GNN's `pIC50 Predicted` values show no positive correlation with experimental `% Inhibition` ($r = -0.15$): the top GNN-scored molecule (Compound 3, $\text{pIC}_{50} = 6.84$) achieved only $5.70\%$ inhibition at $25\text{ \mu M}$, while the top XP/DeepDock-scored molecules (Compounds 1 and 9, $\text{pIC}_{50} = 6.25$ and $6.34$) achieved only $17.50\%$ and $34.81\%$ inhibition. Moreover, Section 2.3 (line 84) reveals that final selection from the 9,000 XP hits relied on unquantified manual curation by medicinal chemists rather than ranking by the GNN score.

* **Compound 6 suppresses pro-inflammatory TNF-$\alpha$ and IL-6 release in LPS-induced RAW264.7 macrophages via JNK3 inhibition: [Fragile].**  
  First, as stated in the Introduction (line 15), JNK3 is predominantly expressed in the central nervous system (neurons), whereas peripheral macrophages such as RAW264.7 express primarily JNK1 and JNK2. Because Compound 6 is an ATP-competitive inhibitor targeting the conserved Met149 hinge and Lys93 catalytic lysine, its activity in RAW264.7 cells at $5\text{ \mu M}$ and $10\text{ \mu M}$ ($38\times$ and $77\times$ its JNK3 $\text{IC}_{50}$) likely reflects unmeasured pan-JNK (JNK1/2) or p38 MAPK inhibition, or general cytotoxicity over the 48-hour incubation ($24\text{ h}$ drug pre-treatment + $24\text{ h}$ LPS; Section 4.6), as no cell viability assay (MTT/CCK-8) is reported. Second, the Discussion (line 150) claims Compound 6 "significantly curtailed the release of both IL-6 and TNF$\alpha$," which overstates Results Section 2.5 (line 121: "slight inhibition of IL-6 secretion") and Figure 4D.

* **Molecular dynamics simulations over three parallel 100 ns trajectories confirm binding stability during the final 20 ns: [Moderately Supported].**  
  While the BPMD comparison across docking engines (Figure 5) and MM/GBSA per-residue decomposition (Figure 6C) are informative, there is a direct contradiction in simulation length between Section 2.7 (line 137: *"three parallel sets of 100 ns molecular dynamics simulations"*) and Section 4.8 (line 207: *"40 ns of constant pressure and temperature simulation (NPT) was carried out to equilibrate the system, which was followed by 30 ns of production simulation"*, with a $1\text{ fs}$ timestep despite SHAKE constraints).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Evaluate the GNN Model Under Scaffold Splitting and Clarify Exact Selection Thresholds for the 10 Tested Compounds
* **WHY:** Random 8:1:1 splitting of ChEMBL congeneric series inflates test $R^2$, and in Table 1 the GNN model assigned higher $\text{pIC}_{50}$ predictions to four weakly active/inactive compounds (Compounds 1, 2, 3, 7, 9) than to Compound 6 ($\text{pIC}_{50\text{ pred}} = 5.82$). Furthermore, it is unclear how 10 compounds with predicted $\text{pIC}_{50}$ values as low as $5.30–5.35$ (Compounds 4, 5, 8, 10) were selected from 9,000 XP hits.
* **WHAT:** (1) Re-evaluate the GAT regression model on the 1,072 ChEMBL compounds using Bemis-Murcko scaffold splitting and report the scaffold-split $R^2$ and RMSE. (2) Explicitly state the quantitative filtering cutoffs (for XP score, MM-GBSA, DeepDock score, predicted $\text{pIC}_{50}$, and chemical clustering) used to narrow 9,000 compounds down to the 10 tested candidates.
* **HOW:** Use `rdkit.Chem.Scaffolds.MurckoScaffold` to group the 1,072 ChEMBL compounds into non-overlapping scaffold train/validation/test sets (8:1:1), retrain the DGL GAT model, and report both random-split and scaffold-split metrics alongside an ablation comparing XP score, MM-GBSA, DeepDock, and GNN rankings on the 10 experimental compounds.

#### 2. Add Cell Viability Data and Address Kinase Isoform Selectivity (JNK1/JNK2 vs. JNK3)
* **WHY:** Incubating RAW264.7 macrophages with $5\text{ \mu M}$ and $10\text{ \mu M}$ of a lipophilic ($\text{XLogP3} = 5.6$) ATP-competitive kinase inhibitor for 48 hours without an MTT/CCK-8 viability control cannot distinguish cytokine suppression from cell death or proliferation arrest. Moreover, RAW264.7 macrophages are a peripheral monocyte/macrophage line where JNK1/2, not brain-specific JNK3, drive LPS-induced TNF-$\alpha$ production.
* **WHAT:** Report cell viability (CCK-8 or MTT at $5\text{ \mu M}$ and $10\text{ \mu M}$ after 48 h in RAW264.7 cells) if measured, or explicitly state the absence of viability and JNK1/JNK2 selectivity profiling as a key limitation in the Discussion. Also report the numerical $\text{IC}_{50}$ of the positive control (Staurosporine in Figure 4A / JNK Inhibitor VIII in Figure 4C) alongside Compound 6.
* **HOW:** Revise Discussion Section 3 (lines 150, 154) to: (a) match Results Section 2.5 regarding the modest effect on IL-6; (b) note that TNF-$\alpha$ reduction in RAW264.7 cells at $5–10\text{ \mu M}$ likely involves concurrent JNK1/JNK2 inhibition given the high sequence identity of the ATP pocket across JNK1/2/3; and (c) fix the typographical error on line 154 (`"development of JAK3 inhibitors"` $\to$ `"development of JNK3 inhibitors"`).

#### 3. Reconcile the Contradictions in MD Simulation Length (Section 2.7 vs. Section 4.8) and Glide Docking Settings (Section 2.3 vs. Section 4.4)
* **WHY:** Two sections of the manuscript contradict each other on the exact computational protocols executed:
  1. **MD simulation protocol:** Section 2.7 (line 137) states three parallel **100 ns** simulations were run ( matches the 0–100 ns axis in Figure 6A–B), whereas Section 4.8 (line 207) describes **40 ns NPT equilibration + 30 ns production** with a 1 fs timestep.
  2. **Glide docking protocol:** Section 2.3 (line 51) describes a 3-stage cascade (`HTVS` under OPLS_2005 $\to$ `SP` under OPLS4 $\to$ `XP` under OPLS4), whereas Section 4.4 (line 177) states `"all docking was performed using the Glide_SP tool"`. Also note in Section 2.3 (line 51) that the SP cutoff ($\le -8.689\text{ kcal/mol}$) is stricter than the subsequent XP cutoff ($\le -8.101\text{ kcal/mol}$).
* **WHAT & HOW:** Update Section 4.8 and Section 4.4 to match the actual Amber19 and Glide input scripts used to generate Figures 5–6 and Table 1.

#### 4. Deposit the GNN Code, Trained Model Weights, and SMILES Table of the 10 Tested Compounds
* **WHY:** The Data Availability Statement (line 222) only provides generic homepage URLs (`https://www.ebi.ac.uk/chembl/`, `https://www.targetmol.com/`, `https://www.medchemexpress.com/`), which does not allow readers to reproduce the DeepDock + GAT rescoring pipeline or access the exact ChEMBL training set and SMILES/catalog IDs of Compounds 1–10.
* **WHAT & HOW:** Deposit the DGL/Optuna Python training code, the curated 1,072-compound ChEMBL CSV, and a table listing the vendor catalog numbers and SMILES strings for Compounds 1–10 in a public GitHub or Zenodo repository.
