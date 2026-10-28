# Review of OOD_ANON_17

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **2.4 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.5/3.5 | Claims: 0.6/2.5 | Biology: 0.6/2.0 | Reproducibility: 0.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This purely *in silico* study screens 200 ZINC compounds (selected via $\ge 50\%$ similarity to four FDA-approved gliptins) against dipeptidyl peptidase 4 (DPP4, PDB: `4A5S`) using AutoDock Vina, followed by selectivity docking against DPP8 (`7A3K`) and DPP9 (`6EOR`), 200 ns GROMACS molecular dynamics (MD) simulations, MM/PBSA binding free energy estimation, SwissADME/preADMET profiling, and B3LYP DFT calculations. The authors identify `ZINC000003015356` as the top hit (DPP4 docking score $= -10.8\text{ kcal/mol}$; MM/PBSA $\Delta G_{\text{binding}} = -151.11\text{ kJ/mol}$) and claim it is a potent, selective, non-toxic DPP4 inhibitor because it yields a docking binding energy of exactly $0.0\text{ kcal/mol}$ against both DPP8 and DPP9. No experimental enzymatic or cellular validation is performed, and neither input coordinates, grid box parameters, nor MD trajectories are deposited in a public repository.

The manuscript contains pervasive methodological failures, physical impossibilities, and direct self-contradictions across nearly every section. Most notably, obtaining a docking score of exactly $0.0\text{ kcal/mol}$ in AutoDock Vina for `ZINC000003015356` against DPP8 and DPP9 (and for all four FDA-approved gliptins against DPP9) is an artifact of mis-centering the $30 \times 30 \times 30\text{ \AA}$ docking grid box outside the protein binding site; in reality, sitagliptin, vildagliptin, saxagliptin, and linagliptin are all known to bind DPP9 in the micromolar-to-submicromolar range. Furthermore, the MM/PBSA table (Table 3) omits the polar solvation penalty ($\Delta G_{\text{polar}}$) and fails to add up mathematically, the DFT section contradicts its own numerical values ($4.77\text{ eV}$ vs. $3.75\text{ eV}$ HOMO–LUMO gap; Table 7 enthalpy vs. total energy), the text contradicts Table 6 on Ames mutagenicity, and the Introduction mischaracterizes the basic biochemical mechanism of DPP4 inhibitors and glitazones.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **`ZINC000003015356` is completely selective over DPP8 and DPP9 with a binding energy of $0\text{ kcal/mol}$, and FDA-approved gliptins have $0\text{ kcal/mol}$ binding energy on DPP9: [Methodologically Flawed].**  
  In AutoDock Vina, a reported affinity of $0.0\text{ kcal/mol}$ with the ligand floating outside the receptor (Figures 6 and 7b) occurs only when the user-defined grid box ($30 \times 30 \times 30\text{ \AA}$) is placed at incorrect $(x, y, z)$ coordinates (e.g., failing to transform grid coordinates between crystal frames of `4A5S`, `7A3K`, and `6EOR` or leaving the co-crystallized ligand inside the pocket). Experimentally, vildagliptin and saxagliptin are potent nanomolar inhibitors of both DPP8 and DPP9 ($K_i \approx 10\text{--}100\text{ nM}$), and sitagliptin inhibits DPP9 at micromolar concentrations. Claiming that `ZINC000003015356` and all four FDA-approved drugs have "zero" affinity for DPP9 based on an uncentered docking box is a fatal technical error.

* **Docking protocol validation and active-site interaction analysis for DPP4 (`4A5S`): [Methodologically Flawed].**  
  1. In Section "Virtual screening and molecular docking studies" (line 69), the authors report two different redocking RMSD values for `N7F` within four sentences (`0.4 Å` and then `0.31` repeated twice in a duplicated sentence).  
  2. An ROC curve ($\text{AUC} = 0.918$, Fig. 3) is presented without any description in the Methods of how many active compounds and decoys were used, where they were sourced from (e.g., DUD-E), or how they were docked.  
  3. The text (line 93) states that `ZINC000003007727` forms hydrogen bonds with `Arg125 and His740` and `ZINC000002876364` forms hydrogen bonds with `His740 and Ser630`, which contradicts Table 1 (`Val546, Ser630, His740` for `ZINC000003007727`; `Arg125, Asp545, Trp629, Ser630, His740` for `ZINC000002876364`). Similarly, Table 2 labels `Arg125, Asp545, Tyr547, His740` under the column header *"Residues involved in $\pi\text{--}\pi$ and hydrophobic interaction"* while listing *"Hydrogen bond"* as the interaction type.  
  4. In Table 4, `ZINC000002876364` and `ZINC000003007727` have identical MW (`431.48`), LogP (`1.34`), HBD (`0`), HBA (`4`), TPSA (`71.85`), and n-RB (`6`), suggesting stereoisomers or duplicate entries, yet their chemical structures in Table 1 are blank.

* **MM/PBSA binding free energy confirms superior affinity of `ZINC000003015356` ($\Delta G_{\text{binding}} = -151.108\text{ kJ/mol}$): [Methodologically Flawed].**  
  In `g_mmpbsa`, $\Delta G_{\text{binding}} = \Delta E_{\text{vdW}} + \Delta E_{\text{elec}} + \Delta G_{\text{polar}} + \Delta G_{\text{SASA}}$. Table 3 reports only $\Delta E_{\text{vdW}} = -194.242\text{ kJ/mol}$, $\Delta E_{\text{elec}} = -2.99\text{ kJ/mol}$, and $\Delta\text{SASA} = -17.833\text{ nm}^2$ (which is an area in $\text{nm}^2$, not an energy in $\text{kJ/mol}$, and burial of SASA upon binding yields a negative non-polar solvation energy $\Delta G_{\text{np}} = \gamma \Delta\text{SASA} + b \approx -17\text{ to }-22\text{ kJ/mol}$). Polar solvation energy ($\Delta G_{\text{polar}}$) is completely omitted from Table 3, and the reported components ($-194.242 + (-2.99) + (-17.833) = -215.065$) do not sum to $-151.108\text{ kJ/mol}$ (nor do they for `N7F`: $-166.415 - 6.112 - 17.071 = -189.598 \neq -114.874$). Furthermore, MM/PBSA was not computed for Sitagliptin or any of the FDA-approved controls simulated in the MD section.

* **`ZINC000003015356` has a favorable low-toxicity ADMET profile: [Overstated].**  
  The Abstract claims `ZINC000003015356` has *"low toxicity parameter"*, and the Introduction (line 17) motivates the entire study by stating that *"Sitagliptin and Vildagliptin exhibited genotoxicity effects... Therefore, it is important to find new selective DPP4 inhibitors that... show lower side effects."* Yet Table 6 and line 280 show that `ZINC000003015356` is predicted to be **Ames positive (`Mutagen`)** and **hERG `Medium-risk`**, while having $91.52\%$ plasma protein binding (leaving $<9\%$ free drug fraction, compared to $17.65\text{--}54.32\%$ for Vildagliptin/Saxagliptin/Sitagliptin). Claiming "no significant toxicity" when the compound fails the Ames mutagenicity test directly contradicts the study's premise.

* **DFT analysis shows `ZINC000003015356` has higher chemical reactivity and softness than Sitagliptin due to a lower HOMO–LUMO energy gap: [Methodologically Flawed].**  
  1. In Section "DFT analysis" (line 304), the authors write: *"The gap energies of Sitagliptin and ZINC000003015356 were obtained at 3.75 and 4.77 eV respectively. The results showed that the selective DPP4 inhibitor had higher chemical reactivity than Sitagliptin due to the lower energy gap between HOMO and LUMO."* Mathematically, $4.77\text{ eV} > 3.75\text{ eV}$: `ZINC000003015356` has a **larger** gap, not a lower gap.  
  2. In Table 7, the chemical hardness $\eta = \Delta E_{\text{gap}} / 2$ is reported as $\eta = 2.560\text{ eV}$ for `ZINC000003015356` (which implies $\Delta E_{\text{gap}} = 5.12\text{ eV}$, contradicting $4.77\text{ eV}$ in the text) and $\eta = 2.38\text{ eV}$ for Sitagliptin (implying $\Delta E_{\text{gap}} = 4.76\text{ eV}$, contradicting $3.75\text{ eV}$ in the text). Moreover, Table 7 shows `ZINC000003015356` has *lower* softness ($\sigma = 0.391\text{ eV}^{-1}$) than Sitagliptin ($\sigma = 0.42\text{ eV}^{-1}$).  
  3. In Table 7, `ZINC000003015356` has Total Energy $E_{\text{tot}} = -1499.321\text{ Hartree}$ and Gibbs Free Energy $G = -1499.413\text{ Hartree}$, but Enthalpy is reported as $H = -949.320\text{ Hartree}$—an impossible $+550\text{ Hartree}$ ($+345,000\text{ kcal/mol}$) discrepancy caused by a transcription typo for $-1499.320\text{ Hartree}$.  
  4. The Methods (line 61) state that DFT was performed at the `B3LYP/6-31G(d,p)` level, whereas Figures 14, 15, and Table 7 state `B3LYP/6-31+G(d,p)`.

* **Biochemical characterization of DPP4 inhibitors and antidiabetic drug classes in the Abstract and Introduction: [Methodologically Flawed].**  
  The Abstract (line 8) and Introduction (line 17) state that *"DPP4 inhibitors can control glucose homeostasis by increasing the level of GLP-1 incretins hormone due to dipeptidase mimicking"* and *"Since DPP4 inhibitors are GLP-1 mimicking rather than blocking DPP4, they disrupt the function of other dipeptide-degrading enzymes."* This is biochemically backwards: gliptins are competitive/covalent *inhibitors* (blockers) of the DPP4 enzyme that prevent GLP-1 degradation; they are neither "dipeptidase mimics" nor "GLP-1 mimetics" (which are peptide receptor agonists like exenatide). Line 17 also describes *"Glitazones as peroxisome receptor antagonists. (PPAR-$\gamma$) agonists"*, contradicting itself within four words.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Re-Run DPP8 and DPP9 Molecular Docking with Properly Centered Active-Site Grid Boxes
* **WHY:** A docking score of $0.0\text{ kcal/mol}$ in AutoDock Vina indicates that the $30 \times 30 \times 30\text{ \AA}$ search box was not centered on the catalytic triad/binding pocket of DPP8 (`7A3K`) and DPP9 (`6EOR`), invalidating all selectivity claims.
* **WHAT:** Extract the centroid coordinates $(x, y, z)$ of the co-crystallized ligands `QX8` in DPP8 (`7A3K`) and `9XH` in DPP9 (`6EOR`), remove the co-crystallized ligands and water molecules, validate redocking of `QX8` and `9XH` (confirming $\text{RMSD} < 2.0\text{ \AA}$), and re-dock `ZINC000003015356` and the four FDA-approved gliptins into the verified active sites.
* **HOW:** In AutoDockTools / Vina, compute the center of mass of `QX8` (`7A3K`) and `9XH` (`6EOR`), set `center_x`, `center_y`, `center_z` explicitly to those coordinates with `size_x = size_y = size_z = 30`, run Vina (`exhaustiveness = 100`), and report the true non-zero binding affinities ($\text{kcal/mol}$) and selectivity ratios in Section "Virtual screening and molecular docking studies".

#### 2. Report the Complete MM/PBSA Energy Breakdown Including Polar Solvation and Reference Drugs
* **WHY:** Table 3 omits $\Delta G_{\text{polar}}$, reports $\Delta\text{SASA}$ in $\text{nm}^2$ instead of non-polar solvation energy ($\Delta G_{\text{np}}$ in $\text{kJ/mol}$), and omits the FDA-approved reference drugs despite 200 ns MD trajectories having already been generated for them.
* **WHAT:** Re-tabulate the complete `g_mmpbsa` output ($\Delta E_{\text{vdW}}$, $\Delta E_{\text{elec}}$, $\Delta G_{\text{polar}}$, $\Delta G_{\text{SASA}}$ in $\text{kJ/mol}$, and $\Delta G_{\text{binding}}$) across the equilibrated window of the 200 ns trajectories for `ZINC000003015356`, `N7F`, and the four FDA-approved gliptins.
* **HOW:** Run `MmPbSaStat.py` on the `g_mmpbsa` output files for all six simulated complexes and update Table 3 so that $\Delta E_{\text{vdW}} + \Delta E_{\text{elec}} + \Delta G_{\text{polar}} + \Delta G_{\text{SASA}} = \Delta G_{\text{binding}}$ holds exactly.

#### 3. Reconcile All DFT Calculations, Orbital Gap Equations, and Basis Set Descriptions
* **WHY:** The text and Table 7 contradict each other on whether `ZINC000003015356` has a smaller or larger HOMO–LUMO gap than Sitagliptin ($4.77$ vs. $3.75\text{ eV}$), the hardness values ($2.560$ and $2.38\text{ eV}$) do not match half the stated energy gaps, and the enthalpy of `ZINC000003015356` in Table 7 ($-949.320\text{ Ha}$) is a 550-Hartree typo.
* **WHAT:** Extract the exact $\varepsilon_{\text{HOMO}}$ and $\varepsilon_{\text{LUMO}}$ eigenvalues from the Gaussian 09 `.log` files, recompute $\Delta E_{\text{gap}} = \varepsilon_{\text{LUMO}} - \varepsilon_{\text{HOMO}}$, $\eta = \Delta E_{\text{gap}}/2$, and $\sigma = 1/(2\eta)$, fix the enthalpy typo in Table 7, and state clearly whether `6-31G(d,p)` or `6-31+G(d,p)` was used.
* **HOW:** Check the Gaussian 09 thermochemistry output block (`Sum of electronic and thermal Enthalpies`), replace `-949.320` with `-1499.320` in Table 7, and revise lines 304–312 to accurately state that `ZINC000003015356` has a *larger* HOMO–LUMO gap (higher kinetic stability, lower reactivity/softness) than Sitagliptin.

#### 4. Correct the Biochemical Misstatements, ROC Validation Details, and Editorial Errors
* **WHY:** Misstating the mechanism of DPP4 inhibitors, omitting the ROC dataset protocol, and leaving figure/table mismatches intact undermine the credibility of the manuscript.
* **WHAT & HOW:**
  1. Rewrite the Abstract (line 8) and Introduction (line 17) to state that DPP4 inhibitors *block* the catalytic activity of DPP4 to prevent degradation of endogenous GLP-1/GIP, and that glitazones are PPAR-$\gamma$ *agonists*.
  2. Document the exact active and decoy sets used to generate the ROC curve in Figure 3.
  3. Reconcile the hydrogen-bonding residue lists between line 93 and Tables 1–2, include the 2D chemical structures in Table 1, and fix the mislabeled caption of Figure 13 (*"The scree plot for PC1 versus PC3"* $\to$ *"2D projection of trajectories onto PC1 and PC3"*).
  4. Temper the conclusion regarding low toxicity to acknowledge the predicted Ames mutagenicity and medium hERG risk in Table 6.
