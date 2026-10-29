# Review of FEXP_ANON_145

**Overall Score:** **2.8 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **2.0 / 8.0**  
* **Score Breakdown:** Rigor: 0.7/3.5 | Claims: 0.5/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.8/2.0

---

## 1. Blinded Metadata Perception

* **Anonymized Manuscript ID:** `FEXP_ANON_145`
* **Perceived Field & Subfield:** Computational Structural Biology / In Silico Drug Discovery (Virtual Screening, Molecular Docking, and Molecular Dynamics against BCR::ABL1 T315I in Chronic Myeloid Leukemia).
* **Study Design Type:** Purely computational virtual screening pipeline (AutoDock Vina via PyRx, SwissADME/pkCSM filtering, 100 ns GROMACS molecular dynamics, PCA/FEL/DCCM, and `g_mmpbsa` free energy calculations) with zero wet-lab biochemical or cellular validation.

---

## 2. Executive Summary & Editorial Verdict

This study screens 1,830 fungal secondary metabolites from the MeFSAT database against the T315I gatekeeper mutant of the BCR::ABL1 tyrosine kinase domain (PDB ID: 3IK3) using PyRx/AutoDock Vina, filters top-scoring hits using SwissADME and pkCSM, and performs 100 ns molecular dynamics (MD) simulations (CHARMM27 force field, GROMACS 2023.2) and MM/PBSA calculations on three candidate complexes—Phellifuropyranone A (`MSID001271`), `(+)-(R)-grifolinone C` (`MSID000080`), and Meshimakobnol B (`MSID001179`)—alongside co-crystallized ponatinib (`0LI`). The authors report that 27 metabolites achieved docking scores $\le -10.0\text{ kcal/mol}$ compared to $-9.9\text{ kcal/mol}$ for ponatinib, and conclude that Phellifuropyranone A ($\Delta G_{\text{bind}} = -22.88 \pm 4.28\text{ kcal/mol}$) and Meshimakobnol B ($\Delta G_{\text{bind}} = -25.86 \pm 3.51\text{ kcal/mol}$) have potency comparable to ponatinib ($-25.54 \pm 6.31\text{ kcal/mol}$).

**Editorial Verdict: Reject (Fundamentally Invalid, 2.8 / 10.0).** The manuscript suffers from fatal internal contradictions, basic cheminformatics errors, and an invalidated positive-control MD simulation. First, Table 2 claims that `(+)-(R)-grifolinone C` ($\text{C}_{44}\text{H}_{60}\text{O}_5$, $\text{MW} = 668.94\text{ Da}$) satisfies all five drug-likeness rules (Lipinski, Ghose, Veber, Egan, and Muegge), which is mathematically impossible given Lipinski's ($\text{MW} \le 500\text{ Da}$), Ghose's ($160 \le \text{MW} \le 480\text{ Da}$, $\le 70$ atoms), and Muegge's ($\text{MW} \le 600\text{ Da}$) hard cutoffs. Second, Table 3 predicts that lead compound Phellifuropyranone A is AMES mutagenic ("Yes"), directly contradicting the text's claim of acceptable toxicity. Third, the positive-control MD trajectory of ponatinib bound to its own co-crystal structure (3IK3) exhibits an unphysical C$\alpha$ backbone RMSD of $0.86\text{ nm}$ ($8.6\text{ \AA}$, peaking at $1.20\text{ nm}$ or $12.0\text{ \AA}$) and loses hydrogen bonding for 60 ns—an obvious simulation or periodic boundary condition (PBC) artifact that the authors misinterpret as genuine structural instability of an FDA-approved nanomolar inhibitor.

### Specific Conclusions and Assessment of Support

* **27 fungal metabolites bind T315I-BCR::ABL1 with higher affinity ($\le -10.0\text{ kcal/mol}$) than ponatinib ($-9.9\text{ kcal/mol}$): [Fragile].**  
  AutoDock Vina scoring functions have standard errors of $\sim 2.0\text{ kcal/mol}$, making a $0.1\text{--}1.3\text{ kcal/mol}$ difference statistically indistinguishable. Furthermore, redocking validation was never properly performed: Table 1 reports `rmsd/ub = 0` and `rmsd/lb = 0` for all 28 ligands, which is merely Vina's trivial self-RMSD of Mode 1 against itself rather than the heavy-atom RMSD of redocked ponatinib against the crystallographic pose in PDB 3IK3.

* **Eight top fungal metabolites, including `(+)-(R)-grifolinone C`, pass Lipinski, Ghose, Veber, Egan, and Muegge drug-likeness rules and exhibit acceptable toxicity: [Methodologically Flawed].**  
  `(+)-(R)-grifolinone C` has formula $\text{C}_{44}\text{H}_{60}\text{O}_5$ and $\text{MW} = 668.94\text{ Da}$, violating Lipinski ($\text{MW} \le 500$), Ghose ($\text{MW} \le 480$, atoms $\le 70$), and Muegge ($\text{MW} \le 600$). Moreover, Table 3 explicitly reports that Phellifuropyranone A (`MSID001271`) and Phellibaumin A (`MSID001266`) are AMES-toxicity positive (mutagenic), and `(+)-(R)-grifolinone C` is hepatotoxic, contradicting the Discussion's assertion of acceptable toxicity.

* **Phellifuropyranone A and Meshimakobnol B form more stable complexes with T315I-BCR::ABL1 than ponatinib during 100 ns MD simulations: [Methodologically Flawed].**  
  The claim rests on comparing single ($n=1$) 100 ns trajectories in which the positive control (ponatinib in PDB 3IK3) suffered a catastrophic C$\alpha$ RMSD jump to mean $0.86\text{ nm}$ (max $1.20\text{ nm}$, or $12\text{ \AA}$) while its radius of gyration ($R_g = 2.09\text{ nm}$) and RMSF ($0.15\text{ nm}$) remained unchanged. A $12\text{ \AA}$ C$\alpha$ RMSD without a change in $R_g$ or RMSF is a textbook GROMACS periodic boundary condition (PBC) centering/imaging artifact or ligand-topology failure, not biological instability of ponatinib.

* **Phellifuropyranone A and Meshimakobnol B show significant potency as T315I-BCR::ABL1 inhibitors comparable to ponatinib and may act as synergistic clinical agents: [Overstated].**  
  No enzymatic $\text{IC}_{50}$ assay, cellular proliferation assay in $\text{Ba/F3}^{\text{T315I}}$ or CML lines, or combination index testing was performed. Inferring potency and drug synergy from single-trajectory MM/PBSA enthalpies (which omit conformational entropy $-T\Delta S$) is scientifically unfounded.

---

## 3. Forensic Defect Inventory

### 1. Mathematical and Cheminformatics Impossibility in Drug-Likeness Filtering (Table 2)
* **Location:** Section *Fungal secondary metabolites are drug-like compounds* (lines 123–137) and Table 2.
* **Defect:** Table 2 lists `MSID000080 ((+)-(R)-grifolinone C)` with formula $\text{C}_{44}\text{H}_{60}\text{O}_5$ and $\text{MW} = 668.94\text{ g/mol}$ as `"Yes"` under the column `Drug-likeness (Lipinski, Ghose, Veber, Egan, and Muegge rule)`, whereas Ponatinib ($\text{MW} = 532.56\text{ g/mol}$) is marked `"No"`. By definition, Lipinski's rule requires $\text{MW} \le 500\text{ Da}$ and $\text{MLOGP} \le 4.15$; Ghose's filter requires $160 \le \text{MW} \le 480\text{ Da}$, $-0.4 \le \text{WLOGP} \le 5.6$, and $20 \le \text{atoms} \le 70$ ($\text{C}_{44}\text{H}_{60}\text{O}_5$ has 109 atoms); and Muegge's filter requires $200 \le \text{MW} \le 600\text{ Da}$ and $\text{XLOGP3} \le 5$. `(+)-(R)-grifolinone C` fails Lipinski, Ghose, and Muegge on molecular weight, atom count, and lipophilicity, yet was promoted to one of the three lead compounds for MD simulation.

### 2. Unrecognized PBC / Trajectory Artifact in Positive-Control Ponatinib MD Simulation
* **Location:** Section *Trajectory analysis of simulated complexes* (lines 167–180) and Fig. 4A.
* **Defect:** For the control T315I-BCR::ABL1–ponatinib complex, the authors report a C$\alpha$ RMSD mean of $0.86\text{ nm}$ ($8.6\text{ \AA}$) and maximum of $1.20\text{ nm}$ ($12.0\text{ \AA}$), compared to $0.17\text{--}0.29\text{ nm}$ for the fungal metabolites. Simultaneously, they report that the ponatinib complex has the exact same C$\alpha$ RMSF ($0.15\text{ nm}$, line 172), radius of gyration ($R_g = 2.09\text{ nm}$, line 174), and SASA ($157.81\text{ nm}^2$, line 179) as the other complexes. It is geometrically impossible for a globular kinase domain to undergo a $12\text{ \AA}$ C$\alpha$ structural deviation without inflating RMSF, $R_g$, or SASA unless the protein or ligand jumped across the periodic box boundary during `gmx trjconv` fitting or the least-squares fit group was misspecified. Treating this artifact as evidence that ponatinib binds unstably to its own crystal structure invalidates the comparative MD baseline.

### 3. Misinterpretation of AutoDock Vina Self-RMSD (`rmsd/ub = 0`, `rmsd/lb = 0`) as Redocking Validation
* **Location:** Section *Results* (line 83) and Table 1 (lines 89–120).
* **Defect:** Table 1 includes columns `rmsd/ub` and `rmsd/lb` with values of `0` and `0` for all 27 fungal hits and ponatinib. In AutoDock Vina output tables, the top-ranked pose (Mode 1) always has `rmsd/ub = 0.000` and `rmsd/lb = 0.000` because Modes $1\dots k$ are measured relative to Mode 1. The authors never computed the heavy-atom superposition RMSD between the redocked ponatinib pose and the crystallographic ligand coordinates in PDB 3IK3 to verify that their docking protocol reproduces the native DFG-out binding mode.

### 4. Direct Contradiction Between Predicted Mutagenicity (Table 3) and Safety Claims
* **Location:** Table 3 (lines 141–153) vs. Discussion (line 37, second chunk).
* **Defect:** In Table 3, pkCSM predicts `AMES toxicity = Yes` for lead compound Phellifuropyranone A (`MSID001271`) and for Phellibaumin A (`MSID001266`), `Hepatotoxicity = Yes` for `(+)-(R)-grifolinone C` (`MSID00080`), and `hERG II inhibitor = Yes` for 7 of the 8 compounds (including both lead candidates Phellifuropyranone A and Meshimakobnol B). The text never discloses or discusses that Phellifuropyranone A is predicted to be AMES-mutagenic, instead stating that all eight compounds *"demonstrated acceptable toxicity levels."*

### 5. Unphysical Simulation Box Specification and Single-Replicate MM/PBSA Limitations
* **Location:** Section *Molecular dynamics simulations* (line 53) and *Binding free energy analysis* (second chunk, lines 15–30).
* **Defect:**
  1. Line 53 states that unit cells were defined *"employing a cubic box of 10 Å dimensions."* A $10\text{ \AA}$ ($1.0\text{ nm}$) cubic box cannot enclose a protein with $R_g = 2.08\text{ nm}$ (diameter $> 40\text{ \AA}$); the authors confused box edge length with the solute-to-wall buffer distance (`-d 1.0`).
  2. Only $n=1$ trajectory of 100 ns was run per complex, with no independent velocity seeds.
  3. MM/PBSA calculations (`g_mmpbsa`) were averaged over all 100 ns without excluding equilibration frames, omitted conformational entropy ($-T\Delta S$), and used an unspecified internal dielectric constant.
  4. Multiple sign and numerical typos appear in the text: Discussion line 45 reports Phellifuropyranone A binding energy as positive `22.88 ± 4.28 kcal/mol` (missing minus sign), Per-residue decomposition line 29 writes double negatives `PHE317 (−-1.16 kcal/mol)` and `LEU370 (−-0.99 kcal/mol)`, and Discussion line 45 states that ILE315 *"contributed less binding free energies for Phellifuropyranone A, Meshimakobnol B, than the standard Ponatinib"*, reversing the magnitude of $-1.63$ and $-1.27\text{ kcal/mol}$ vs. $-1.03\text{ kcal/mol}$.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.7** | **3.5** | Unvalidated redocking (confusing Vina Mode 1 self-RMSD = 0 with crystallographic pose RMSD); catastrophic $0.86\text{--}1.20\text{ nm}$ C$\alpha$ RMSD PBC artifact in the ponatinib positive control; $n=1$ MD trajectories without replicates; single-trajectory MM/PBSA without entropy. |
| **2. Claim-to-Evidence Alignment** | **0.5** | **2.5** | Abstract and Discussion claim "significant potency comparable to ponatinib," "acceptable toxicity," and utility as "synergistic agents" without wet-lab assays, while Table 2 and Table 3 directly refute the drug-likeness of `MSID000080` and the non-mutagenicity of `MSID001271`. |
| **3. Data Integrity & Biological Plausibility** | **0.8** | **2.0** | Impossible drug-likeness classification for a $668.94\text{ Da}$ triterpenoid/meroterpenoid (`MSID000080`); unphysical interpretation of a $12\text{ \AA}$ C$\alpha$ RMSD jump in the ponatinib crystal complex as genuine ligand instability. |
| **4. Reproducibility & Data Integrity** | **0.8** | **2.0** | Public database accessions (MeFSAT, PDB 3IK3) are cited, but docking grid coordinates/dimensions are omitted, box size is misstated as $10\text{ \AA}$ total dimension, no input topologies or trajectories are deposited, and multiple sign errors appear in the text (`22.88`, `−−1.16`). |
| **Scientific Core Score** | **2.0** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **2.8** | **10.0** | **Fundamentally Invalid Tier (1.0 – 2.9).** |
