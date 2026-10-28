# Review of OOD_REP2_12

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.7 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.8/3.5 | Claims: 1.5/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.1/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study presents a multistage structure- and ligand-based virtual screening pipeline to discover small-molecule inhibitors of c-Jun N-terminal kinase 3 (JNK3), followed by biochemical and cellular assays and molecular dynamics (MD) simulations. Starting from an in-house compilation of ~1.6 million compounds (ChemDiv and MedChemExpress libraries), the authors apply hierarchical Glide docking (HTVS $\to$ SP $\to$ XP) against the human JNK3 structure (PDB: 7S1N) to retain 9,000 compounds. They then rescore candidates using Prime MM/GBSA, DeepDock, and a custom Graph Attention Network–Multilayer Perceptron (GAT-MLP) regression model trained on 1,072 ChEMBL JNK3 inhibitors ($8:1:1$ split; test $R^2 = 0.7228$). Ten selected compounds are tested in vitro at $25\text{ }\mu\text{M}$ against recombinant JNK3 kinase, identifying Compound 6 (`N-(4-(2-ethyl-4-(m-tolyl)thiazol-5-yl)pyridin-2-yl)benzamide`) with $99.73\%$ inhibition and an $\text{IC}_{50}$ of $130.1\text{ nM}$. In LPS-stimulated RAW264.7 macrophages, Compound 6 ($5\text{–}10\text{ }\mu\text{M}$) reduces supernatant TNF-$\alpha$ and IL-6 levels. Finally, binding pose metadynamics (BPMD) and Amber MD simulations characterize hydrogen bonds between Compound 6 and Met149/Lys93.

The inclusion of prospective wet-lab biochemical validation ($\text{IC}_{50} = 130.1\text{ nM}$) and cytokine release assays places this work well above purely computational screening papers. However, the manuscript suffers from three substantive limitations: (1) Table 1 demonstrates that the computational rescoring metrics (GNN predicted $\text{pIC}_{50}$, DeepDock, MM/GBSA, and Glide XP) actually correlate *negatively* ($r = -0.16$ for GNN $\text{pIC}_{50}$) with experimental inhibition across the 10 tested compounds, with 9 of the 10 candidates failing to reach $50\%$ inhibition even at $25\text{ }\mu\text{M}$; (2) the cellular anti-inflammatory assay in RAW264.7 macrophages lacks a parallel cytotoxicity/viability control (at $5\text{–}10\text{ }\mu\text{M}$ over 48 hours) and uses a peripheral macrophage line that predominantly expresses JNK1/2 rather than brain-specific JNK3, without kinase selectivity profiling; and (3) the Materials and Methods and Results sections contain direct contradictions regarding MD simulation durations ($100\text{ ns}$ vs. $40\text{ ns} + 30\text{ ns}$) and docking protocols. Reconciling the protocol contradictions, acknowledging the high false-positive rate of the rescoring pipeline in Table 1, and controlling for cellular viability and isoform selectivity are needed to align the claims with the evidence.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Compound 6 inhibits recombinant JNK3 kinase activity in vitro with an $\text{IC}_{50}$ of $130.1\text{ nM}$ ($99.73 \pm 0.44\%$ inhibition at $25\text{ }\mu\text{M}$; Table 1, Fig. 4A–B): [Well Supported].**  
  The HTRF kinase assay uses a 7-point 10-fold dilution series ($0.1\text{ nM}$ to $10,000\text{ nM}$) with positive reference controls (Staurosporine and JNK Inhibitor VIII) and shows a clean sigmoidal dose–response curve (Fig. 4B). However, selectivity against JNK1, JNK2, and off-target kinases is not measured.

* **The hybrid AI rescoring workflow (DeepDock + GAT-MLP GNN, test $R^2 = 0.7228$, plus MM/GBSA) reliably predicts JNK3 binding affinity and enriches potent inhibitors: [Overstated].**  
  In Table 1, the GNN predicted $\text{pIC}_{50}$ values (`5.30` to `6.84`, corresponding to predicted $\text{IC}_{50}$ values of $0.14\text{ to }5.0\text{ }\mu\text{M}$) fail to rank or predict the experimental outcomes of the 10 tested compounds:
  1. Compound 3 has the highest GNN predicted $\text{pIC}_{50}$ (`6.84`, predicted $\text{IC}_{50} \approx 145\text{ nM}$), yet shows the lowest experimental inhibition of all 10 compounds ($5.70 \pm 1.02\%$ at $25\text{ }\mu\text{M}$).
  2. Compound 1 (best XP score $-13.871$, best DeepDock $-185.12$, GNN $\text{pIC}_{50} = 6.25$) and Compound 9 (best MM-GBSA $-87.01$, second-best XP $-13.694$, second-best GNN $\text{pIC}_{50} = 6.34$) achieve only $17.50\%$ and $34.81\%$ inhibition at $25\text{ }\mu\text{M}$, respectively.
  3. Across all 10 compounds in Table 1, the Pearson correlation between GNN `pIC50 Predicted` and experimental `Inhibition Rate (%)` is $-0.16$ (Spearman $\rho = -0.10$), and 9 of the 10 compounds have experimental $\text{IC}_{50} > 25\text{ }\mu\text{M}$ ($\text{pIC}_{50} < 4.6$). Compound 6 ($\text{IC}_{50} = 130.1\text{ nM}$, experimental $\text{pIC}_{50} = 6.89$) was ranked 6th out of 10 by the GNN (`pIC50 Predicted` $= 5.82$). Furthermore, the ChEMBL GNN dataset ($N = 1,072$) was split randomly ($8:1:1$) without scaffold splitting, inflating the reported test $R^2 = 0.7228$.

* **Compound 6 suppresses neuroinflammation by inhibiting JNK3-mediated TNF-$\alpha$ and IL-6 release in LPS-induced RAW264.7 macrophages (Fig. 4C–D): [Fragile].**  
  First, as the authors state in the Introduction (line 15), *"JNK1 and JNK2 are ubiquitously expressed, while JNK3 is predominantly expressed in the brain."* RAW264.7 is a murine peripheral peritoneal macrophage cell line in which LPS-induced TNF-$\alpha$/IL-6 production is driven by JNK1/JNK2 and p38 MAPK, not neuronal JNK3. Because Compound 6 is an ATP-competitive hinge binder (interacting with conserved Met149 and Lys93), its cellular effect in RAW264.7 cells likely reflects pan-JNK (JNK1/2) or off-target kinase inhibition. Second, RAW264.7 cells were incubated with $5\text{ }\mu\text{M}$ and $10\text{ }\mu\text{M}$ of Compound 6 ($\sim 40\text{–}77\times$ its biochemical $\text{IC}_{50}$) for 48 hours total ($24\text{ h}$ pretreatment $+ 24\text{ h}$ LPS) without an MTT/CCK-8 cell viability assay; compound-induced cytotoxicity or cytostasis over 48 hours would directly reduce cytokine accumulation in the supernatant.

* **Binding pose metadynamics and MD simulations establish the stable binding mode of Compound 6 with JNK3 (Figs. 5–6): [Moderately Supported].**  
  Using BPMD (`PoseScore` and `PersScore`) across multiple docking engines (AutoDock-GPU, Vina, LeDock, Glide) to select the starting pose for MD and MM/GBSA per-residue decomposition is sound practice, and the identified hinge hydrogen bonds with Met149 match canonical kinase crystal structures. However, the simulation length described in Results Section 2.7 ($3 \times 100\text{ ns}$ parallel trajectories) directly contradicts Materials and Methods Section 4.8 ($40\text{ ns}$ NPT equilibration followed by $30\text{ ns}$ production with a $1\text{ fs}$ timestep).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile the Contradictory MD and Docking Protocols Between Results and Methods
* **WHY:** Results Section 2.7 (line 137) states that three parallel $100\text{ ns}$ MD simulations were performed and analyzed over the final $20\text{ ns}$ / $1\text{ ns}$, whereas Methods Section 4.8 (line 207) describes a single run of $40\text{ ns}$ NPT equilibration followed by $30\text{ ns}$ production. Similarly, Results Section 2.3 (line 51) describes three sequential Glide precision tiers (HTVS with OPLS_2005 $\to$ SP with OPLS4 $\to$ XP with OPLS4), whereas Methods Section 4.4 (line 177) states that *"all docking was performed using the Glide_SP tool."*
* **WHAT:** Audit the simulation logs and docking scripts and correct Sections 2.3, 2.7, 4.4, and 4.8 so that the exact simulation lengths, number of replicates, force fields, and docking precision modes are consistent throughout the manuscript.
* **HOW:** Inspect the `ptraj`/`cpptraj` input scripts and Figure 6A–B time axes (which span $0\text{–}100\text{ ns}$) and update Section 4.8 to match the actual $3 \times 100\text{ ns}$ protocol (and clarify why SHAKE with a $1\text{ fs}$ timestep was used instead of the standard $2\text{ fs}$).

#### 2. Benchmark the GNN Model Under Scaffold Splitting and Discuss Score-vs.-Assay Discordance
* **WHY:** In Table 1, 9 out of 10 top-ranked compounds showed $<44\%$ inhibition at $25\text{ }\mu\text{M}$, and the GNN predicted $\text{pIC}_{50}$ did not correlate positively with experimental inhibition among the 10 tested hits.
* **WHAT:** Re-evaluate the GAT-MLP GNN on the 1,072 ChEMBL compounds using Bemis–Murcko scaffold splitting (comparing it against baseline RF/XGBoost on Morgan fingerprints and raw Glide XP/MM-GBSA scores), and add an explicit paragraph in the Discussion analyzing why Compounds 1, 3, and 9 failed in the biochemical assay despite top computational scores.
* **HOW:** Group the 1,072 ChEMBL molecules by Murcko scaffold in RDKit, re-run the $8:1:1$ train/validation/test split by scaffold, and report the scaffold-split $R^2$ and RMSE alongside the random-split metrics in Section 2.3.

#### 3. Add Cell Viability Controls and Clarify Isoform Selectivity (JNK1/2 vs. JNK3)
* **WHY:** Reducing TNF-$\alpha$ and IL-6 in RAW264.7 macrophages after 48 hours of exposure to $5\text{–}10\text{ }\mu\text{M}$ Compound 6 can be confounded by cell death or proliferation arrest, and RAW264.7 macrophages primarily express JNK1/2 rather than neuronal JNK3.
* **WHAT:** Report CCK-8/MTT cell viability data for Compound 6 at $5\text{ }\mu\text{M}$ and $10\text{ }\mu\text{M}$ in RAW264.7 cells (or qualify the cytokine results if viability was not measured), and explicitly note in the Discussion that activity in RAW264.7 macrophages likely reflects pan-JNK (JNK1/2/3) inhibition at the conserved ATP site.
* **HOW:** Normalize ELISA cytokine levels to cell viability (or total cellular protein) if available; otherwise, add an explicit limitation in Section 3 stating that cytotoxicity in RAW264.7 cells and biochemical selectivity against JNK1 and JNK2 ($\text{IC}_{50}$ ratios) must be determined in follow-up work.

#### 4. Technical and Editorial Corrections
* **WHY:** Typographical errors in target names and missing code/structures reduce clarity and reproducibility.
* **WHAT & HOW:**
  1. **Line 154 (Target name typo):** Correct *"design and development of JAK3 inhibitors"* to **JNK3 inhibitors**.
  2. **Table 1 (line 60):** Provide the SMILES strings and commercial catalog IDs (ChemDiv / MCE IDs) for all 10 tested compounds in Table 1 or Supplementary Information, and deposit the DGL GAT-MLP training and inference code in a public repository.
  3. **Figure 4A (line 115):** State the concentration of the reference compound Staurosporine used in Figure 4A and report its numerical $\text{IC}_{50}$ alongside Compound 6 ($130.1\text{ nM}$).
