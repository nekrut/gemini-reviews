# Review of OOD_ANON_03

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.5 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.7/3.5 | Claims: 1.5/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.2/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This computational medicinal chemistry study seeks to identify novel dual Type II kinase inhibitors simultaneously targeting vascular endothelial growth factor receptor-2 (VEGFR2) and focal adhesion kinase (FAK) to suppress tumor angiogenesis and metastasis. The authors align crystal structures of VEGFR2 (8 PDB structures) and FAK (2 PDB structures) bound to Type II (DFG-out) inhibitors, manually construct 109 VEGFR2 and 14 FAK receptor-based 3D pharmacophore models with excluded volumes in MOE, and evaluate them against compiled decoy sets (39 or 40 actives and 1,200 DEKOIS 2.0 decoys for VEGFR2; 17 actives, 28 experimental inactives, and 955 DUD-E decoys for FAK). Using the selected models (`VEGFR2_Ph4_109` and `FAK_Ph4_12`), they screen the ZINC purchasable database via ZINCPharmer, filter hits by Lipinski/Veber/Oprea/PAINS criteria to obtain 124 overlapping compounds, dock them into VEGFR2 (PDB: 4ASD) and FAK (PDB: 4K9Y), and apply SwissADME filtering to highlight a single lead candidate (`ZINC09875266`).

The study addresses a biologically well-motivated dual-target hypothesis—exploiting the structural conservation of the hinge (Cys919/Cys502), $\alpha$C-helix (Glu885/Glu471), and DFG-loop (Asp1046/Asp564) residues in the DFG-out conformation—and properly states in the Discussion that its findings are strictly computational predictions requiring *in vitro* and *in vivo* validation. However, the virtual screening and validation pipeline has several methodological weaknesses: the FAK pharmacophore model is derived from only two crystal structures from a single publication (one of which has a weak $\text{IC}_{50}$ of $7,000\text{ nM}$); pharmacophore models were manually tuned across 109 and 14 variants on the same test set used to report final validation metrics without an external hold-out set; the docking evaluation relies solely on rigid-receptor docking with the coarse London dG scoring function without molecular dynamics (MD) or MM-PBSA rescoring; and there are numerical discrepancies in the VEGFR2 test-set active counts ($39$ vs. $40$) and residue numbering (Asp1046 vs. Asp1064).

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Structural and topological conservation of the Type II DFG-out binding pocket between VEGFR2 and FAK (Section "Protein structure similarity assessment", Figures 3–5): [Well Supported].**  
  The sequence alignment (34% identity, 54% positives across the kinase domain) and 3D structural superposition of PDB 4ASD (VEGFR2) and PDB 4K9Y (FAK) clearly establish that the key Type II recognition residues—hinge Cys919/Cys502, $\alpha$C-helix Glu885/Glu471, and DFG Asp1046/Asp564—converge in 3D space, providing a sound biophysical basis for dual Type II inhibitor design.

* **Statistical validation and optimality of pharmacophore models `VEGFR2_Ph4_109` and `FAK_Ph4_12` (Tables 3–4, Figures 6–7): [Fragile].**  
  First, the authors manually generated 109 VEGFR2 and 14 FAK pharmacophore models by varying feature sizes and the number of excluded volumes (e.g., 359 vs. 378 excluded volumes in `VEGFR2_Ph4_108` vs. `109`; 68 vs. 10 in `FAK_Ph4_12` vs. `13`) and evaluated all models on a single test set to pick the winners. Optimizing excluded-volume counts on the test set without an independent external validation set risks overfitting to the test set's specific ligand/decoy geometries. Second, for FAK, only two PDB structures exist (4K9Y with $\text{IC}_{50} = 266\text{ nM}$ and 4KAO with $\text{IC}_{50} = 7000\text{ nM}$, Table 2), providing a very narrow structural training basis. Third, the authors state that F1 score was "used as the metric of choice for best model selection," yet they bypass the highest-F1 models (`VEGFR2_Ph4_104`, $\text{F1} = 0.52$; `FAK_Ph4_9/10`, $\text{F1} = 0.65$) in favor of third-ranked models (`VEGFR2_Ph4_109`, $\text{F1} = 0.48$; `FAK_Ph4_12`, $\text{F1} = 0.61$) based on qualitative SAR arguments without showing why the top-F1 models failed to capture the SAR.

* **Identification of 13 dual-binding hits and selection of `ZINC09875266` via rigid-receptor docking (Section "Molecular docking", Figure 9): [Fragile].**  
  The 124 overlapping hits were docked using a rigid-receptor protocol with Triangle Matcher placement and scored solely with the empirical London dG scoring function in MOE. Rigid-receptor docking into a single static crystal structure (4ASD and 4K9Y) ignores induced-fit side-chain rearrangements in the flexible DFG-loop and allosteric back pocket, and London dG is a fast placement scoring function rather than a refined free-energy estimator (e.g., GBVI/WSA dG, MM-PBSA, or explicit-solvent MD). Furthermore, the main text never reports the actual docking scores ($S$) of the 13 hits or `ZINC09875266` relative to the co-crystallized reference inhibitors ($-15.24$ and $-16.02\text{ kcal/mol}$), relegating them to Supplementary Section S4.2.

* **Numerical consistency in test set composition and pharmacophore metrics (Section "Test set compilation", Table 3): [Moderately Supported].**  
  In "Test set compilation" (both Results and Methodology), the authors state that the VEGFR2 test set contains $1,240$ compounds consisting of $39$ active inhibitors and $1,200$ decoys ($39 + 1200 = 1239$, not $1240$). In Table 3 and Section `VEGFR2_Ph4_109`, however, $\text{TP} + \text{FN} = 38 + 2 = 40$ active compounds ($40 + 1200 = 1240$). In addition, under `VEGFR2_Ph4_109`, the text reports an enrichment ($E$) of $9.82$, whereas Table 3 reports $E = 9.66$ for `VEGFR2_Ph4_109`, and page 9 refers to Asp1046 as "Asp1064".

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Separate Training/Test Ligands and Justify Model Selection Over Higher-F1 Candidates
* **WHY:** Tuning the number of excluded volumes (e.g., 359 vs. 378) across 109 models on the test set inflates discrimination metrics, and selecting the third-ranked F1 model contradicts the stated selection rule.
* **WHAT:** Verify zero overlap between the PDB training ligands (Tables 1–2) and the active test sets (Tables S1–S2), and explicitly compare the feature compositions of `VEGFR2_Ph4_103/104` vs. `109` and `FAK_Ph4_9/10` vs. `12`.
* **HOW:** Add a column or note to Table 3 and Table 4 specifying which essential Type II pharmacophoric feature (e.g., hinge Acc, DFG Acc, $\alpha$C Don, hydrophobic back-pocket Hyd, or Aro) was missing in `VEGFR2_Ph4_103/104` and `FAK_Ph4_9/10` that necessitated choosing `VEGFR2_Ph4_109` and `FAK_Ph4_12`.

#### 2. Perform Induced-Fit Rescoring and Molecular Dynamics Stability Checks on Top Hits
* **WHY:** Rigid-receptor docking with only the initial London dG scoring function is prone to false-positive pose artifacts, especially in the large, flexible DFG-out allosteric pocket.
* **WHAT:** Re-score the top 13 common hits using MOE's induced-fit (flexible side-chain) refinement with the GBVI/WSA dG scoring function, and bring the docking score comparison table into the main text.
* **HOW:** In MOE, run a tethered induced-fit refinement (allowing side chains within $6\text{ \AA}$ of the ligand to relax under Amber10:EHT) followed by GBVI/WSA dG rescoring for the 13 hits and the two co-crystallized reference ligands (Sorafenib in 4ASD and the 4K9Y ligand). Include a main-text table reporting the ZINC IDs, SMILES/structures, London dG scores, refined GBVI/WSA dG scores, and hydrogen-bond distances to Cys919/Cys502, Glu885/Glu471, and Asp1046/Asp564.

#### 3. Benchmark Dual-Target Selectivity Against the Inactive FAK Test Compounds
* **WHY:** In the Methodology ("Test set compilation"), the authors note that the FAK test set included 28 experimentally confirmed inactive compounds ($\text{IC}_{50} > 10\text{ }\mu\text{M}$) alongside 955 DUD-E decoys, whereas Table 4 pools all 983 non-actives together.
* **WHAT:** Report how well `FAK_Ph4_12` and the docking protocol reject the 28 experimentally verified FAK inactive molecules specifically, as opposed to synthetic DUD-E decoys.
* **HOW:** Compute the false positive rate of `FAK_Ph4_12` on the 28 experimental inactives separately from the 955 DUD-E decoys and report this breakdown in the text accompanying Table 4.

#### 4. Correct Numerical and Typographical Inconsistencies
* **WHY:** Discrepancies between text and tables reduce confidence in the reported virtual screening statistics.
* **WHAT & HOW:**
  1. Reconcile the number of VEGFR2 active test compounds: change "39 active inhibitors" in the "Test set compilation" sections to "40 active inhibitors" (to match $\text{TP}+\text{FN} = 38+2 = 40$ and $N_{\text{total}} = 1240$ in Table 3), or update Table 3 if one active was excluded.
  2. Correct the enrichment value of `VEGFR2_Ph4_109` in the text from $9.82$ to $9.66$ to match Table 3.
  3. Fix the residue typo "Asp1064" to "Asp1046" in the `VEGFR2_Ph4_109` section.
