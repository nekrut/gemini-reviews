# Review of OOD_REP2_13

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.3 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.5/3.5 | Claims: 1.5/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.2/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This computational study aims to identify dual Type-II kinase inhibitors simultaneously targeting vascular endothelial growth factor receptor-2 (VEGFR2) and focal adhesion kinase (FAK). After aligning the kinase domain sequences ($34\%$ identity, $54\%$ positives) and DFG-out crystal structures of VEGFR2 (PDB: 4ASD) and FAK (PDB: 4K9Y) to confirm 3D superposition of key hinge (Cys919/Cys502), $\alpha\text{C}$-helix (Glu885/Glu471), and DFG-loop (Asp1046/Asp564) residues, the authors manually construct 109 receptor-based 3D pharmacophore models for VEGFR2 (from 8 PDB structures) and 14 models for FAK (from 2 PDB structures) in MOE. They evaluate these models on compiled test sets (39 or 40 actives + 1,200 DEKOIS 2.0 decoys for VEGFR2; 17 actives + 983 DUD-E/literature decoys for FAK), selecting `VEGFR2_Ph4_109` ($\text{Se} = 0.95$, $\text{Sp} = 0.93$) and `FAK_Ph4_12` ($\text{Se} = 0.88$, $\text{Sp} = 0.98$). Screening the ZINC purchasable database via ZINCPharmer yields 42,616 and 28,475 hits, which are filtered by drug/lead-likeness (Lipinski, Veber, Oprea, PAINS, mutagenicity) to 13,023 and 6,832 compounds with 124 shared hits. Rigid-receptor MOE docking narrows these to 13 compounds forming the required Type-II hydrogen bonds in both targets, and SwissADME filtering selects a single non-BBB-permeant, P-gp non-substrate candidate (`ZINC09875266`).

The structural rationale for dual Type-II inhibition of VEGFR2 and FAK in the DFG-out conformation is clearly presented and supported by binding-pocket superposition. However, the study is limited by a major spreadsheet calculation error in Table 3 that corrupts the hit counts ($N$), yield of actives ($\text{Ya}$), enrichment factors ($E$), and $F_1$ scores across all 109 VEGFR2 pharmacophore models; iterative tuning of excluded volumes on the single test set without an independent validation set; construction of the FAK pharmacophore from only two crystal structures (one of which has a weak $\text{IC}_{50}$ of $7,000\text{ nM}$); reliance on rigid-receptor docking without induced-fit refinement, molecular dynamics, or main-text docking scores; and the absence of any experimental biochemical validation. Fixing the Table 3 arithmetic errors, separating pharmacophore tuning from test-set evaluation, and reporting complete docking energetics in the main text are essential revisions.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **VEGFR2 and FAK kinase domains share conserved 3D DFG-out binding site geometry at the hinge (Cys919/Cys502), gatekeeper/$\alpha\text{C}$-helix (Glu885/Glu471), and DFG motif (Asp1046/Asp564), supporting the feasibility of dual Type-II inhibition: [Well Supported].**  
  The sequence alignment (Fig. 3) and 3D structural superposition of PDB 4ASD and 4K9Y (Fig. 5) clearly demonstrate spatial convergence of the donor/acceptor and hydrophobic back-pocket sub-sites required for Type-II DFG-out inhibitors.

* **Pharmacophore validation metrics in Table 3 establish `VEGFR2_Ph4_109` ($\text{Ya} = 0.31$, $E = 9.66$, $F_1 = 0.48$) as a top-performing model on the VEGFR2 test set: [Methodologically Flawed].**  
  Table 3 contains a systematic formula error in column `N` (total hits retrieved) that propagates into Yield of Actives ($\text{Ya} = \text{TP}/N$), Enrichment ($E$), and $F_1$:
  1. Whereas in Table 4 (FAK) column `N` is correctly calculated as total retrieved hits $N = \text{TP} + \text{FP}$ (e.g., for `FAK_Ph4-12`, $\text{TP} = 15, \text{FP} = 17 \implies N = 32, \text{Ya} = 15/32 = 0.47$), in Table 3 (VEGFR2) column `N` was erroneously calculated as $N = \text{FP} + 40$ (the sum of false positives plus total active compounds)!
  2. For example, in `VEGFR2_Ph4-21`, $\text{TP} = 0$ and $\text{FP} = 1$ (only 1 hit retrieved), yet Table 3 reports $N = 41$ ($1 + 40$). In `VEGFR2_Ph4-17`, $\text{TP} = 3$ and $\text{FP} = 4$ (7 hits retrieved, true precision $\text{Ya} = 3/7 = 0.43$, true $E = 13.3$, true $F_1 = 0.13$), yet Table 3 reports $N = 44$ ($4 + 40$), $\text{Ya} = 3/44 = 0.07$, and $E = 2.11$. In `VEGFR2_Ph4-12`, $\text{TP} = 16$ and $\text{FP} = 23$ (39 hits retrieved, true $\text{Ya} = 16/39 = 0.41$, true $E = 12.7$, true $F_1 = 0.41$), yet Table 3 reports $N = 63$ ($23 + 40$), $\text{Ya} = 16/63 = 0.25$, and $E = 7.87$. For `VEGFR2_Ph4-109`, $\text{TP} = 38$ and $\text{FP} = 82$ ($\text{TP} + \text{FP} = 120$), yet Table 3 reports $N = 122$ ($82 + 40$), and line 216 states $E = 9.82$ while Table 3 states $E = 9.66$.
  3. Furthermore, the text (lines 137 and second part line 10) states that the VEGFR2 test set contains **39** active inhibitors and 1,200 decoys (which sums to 1,239, not 1,240), whereas every row of Table 3 and line 216 uses $\text{TP} + \text{FN} = \mathbf{40}$ actives.
  4. Finally, all 109 VEGFR2 models and 14 FAK models (including fine-tuning between 359 and 378 excluded volumes in `VEGFR2_Ph4_108` vs. `109`) were iteratively tuned and selected on the same test set without an external validation set, and the FAK model was built from only 2 crystal structures, one of which (`4KAO`, $\text{IC}_{50} = 7,000\text{ nM}$; Table 2) is a weak micromolar binder.

* **Thirteen ZINC hits (and lead candidate `ZINC09875266`) identified via rigid-receptor docking are promising dual VEGFR2/FAK inhibitors: [Fragile].**  
  The docking evaluation relies entirely on rigid-receptor docking in MOE (`Triangle Matcher` + `London dG`) without receptor side-chain flexibility, MM-GBSA/PBSA rescoring, or molecular dynamics stability assessment. Moreover, the manuscript never reports the docking scores of `ZINC09875266` or the other 12 hits in the main text or tables (relegating them to Additional file 1 Section S4.2), preventing direct comparison against the co-crystallized reference ligands ($-15.24$ and $-16.02\text{ kcal/mol}$). No in vitro enzymatic or cellular assays are performed.

* **`ZINC09875266` possesses favorable oral bioavailability, non-BBB permeability, P-gp non-substrate status, and synthetic accessibility ($\text{SA} = 2.42$): [Moderately Supported].**  
  The SwissADME BOILED-Egg (wLogP vs. TPSA) and P-gp classification follow standard rule-based cheminformatics filters, though they remain unvalidated computational estimates.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Fix the Spreadsheet Formula Bug in Table 3 (and Table S4) and Reconcile Test Set Counts
* **WHY:** Setting $N = \text{FP} + 40$ instead of $N = \text{TP} + \text{FP}$ in Table 3 severely distorts Yield of Actives ($\text{Ya} = \text{TP}/N$) and Enrichment ($E = \text{Ya} / (A / D)$) for every model, particularly penalizing high-specificity models with low $\text{FP}$.
* **WHAT:** Recompute $N = \text{TP} + \text{FP}$, $\text{Ya} = \text{TP}/(\text{TP}+\text{FP})$, $E = \frac{\text{TP}/(\text{TP}+\text{FP})}{40/1240}$, and $F_1 = \frac{2\,\text{TP}}{2\,\text{TP} + \text{FP} + \text{FN}}$ across all rows of Table 3 and Supplementary Table S4, and correct the discrepancy between 39 actives (line 137) and 40 actives (Table 3 and line 216).
* **HOW:** Update the Excel/MOE evaluation sheet with $N = \text{TP} + \text{FP}$, verify whether the test set contained 39 or 40 active compounds, and revise Table 3, Table S4, and the Results text (lines 144, 216) accordingly.

#### 2. Incorporate Induced-Fit Docking and Report Main-Text Docking Energies for the 13 Common Hits
* **WHY:** Rigid-receptor docking into a single static crystal structure (4ASD and 4K9Y) cannot account for side-chain rearrangements in the DFG-out allosteric back pocket, and omitting the docking scores of the 13 hits from the main text hides how their predicted affinities compare to the co-crystallized reference inhibitors.
* **WHAT:** Perform Induced Fit Docking (IFD) in MOE (allowing side-chain flexibility within $6\text{ \AA}$ of the ligand and applying GBVI/WSA dG rescoring) for the 13 common compounds, and include a main-text table listing the ZINC IDs, chemical structures/SMILES, VEGFR2 docking scores, FAK docking scores, and key hydrogen-bond distances alongside the co-crystallized controls (Sorafenib in 4ASD and the 4K9Y ligand).
* **HOW:** Run MOE's `Induced Fit` refinement protocol with `GBVI/WSA dG` rescoring on the 13 hits in both 4ASD and 4K9Y, and promote Supplementary Table S4.2 (updated with IFD scores and RMSD/interaction distances) into the main text as Table 6.

#### 3. Validate Top Hit Complex Stability via Molecular Dynamics or Cross-Docking
* **WHY:** Without experimental kinase assays, a single static docking pose is insufficient to establish stable dual binding across two distinct kinases.
* **WHAT:** Either perform 50–100 ns explicit-solvent molecular dynamics simulations of `ZINC09875266` bound to VEGFR2 and FAK to verify persistence of the Cys919/Cys502, Glu885/Glu471, and Asp1046/Asp564 hydrogen bonds, or cross-dock the 13 hits across all 8 VEGFR2 PDB structures and both FAK PDB structures (ensemble docking).
* **HOW:** Using the 8 aligned VEGFR2 structures (Table 1) and 2 FAK structures (Table 2) already prepared in MOE, dock the 13 common hits into all 10 structures and report the mean $\pm$ SD docking score and pose conservation across the structural ensemble.

#### 4. Technical and Editorial Cleanup
* **WHY:** Minor typos in residue numbering and text formatting detract from readability.
* **WHAT & HOW:**
  1. **Line 228 (Residue numbering typo):** Correct *"interacting with Asp1064"* to **Asp1046** (to match line 220 and the rest of the text).
  2. **Line 216 vs. Table 3:** Reconcile the enrichment value of `VEGFR2_Ph4_109` between line 216 ($E = 9.82$) and Table 3 ($E = 9.66$) once $N = \text{TP} + \text{FP} = 120$ is corrected ($E = (38/120)/(40/1240) = 9.82$).
  3. **Line 319:** Fix capitalization typo (`"identified. a lead-like compound"` $\to$ `"identified. A lead-like compound"`).
