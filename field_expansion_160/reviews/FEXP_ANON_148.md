# Review of FEXP_ANON_148

**Overall Score:** **2.6 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.9 / 8.0**  
* **Score Breakdown:** Rigor: 0.6/3.5 | Claims: 0.5/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.7/2.0

---

## 1. Blinded Metadata Perception

* **Anonymized Manuscript ID:** `FEXP_ANON_148`
* **Perceived Field & Subfield:** Computational Medicinal Chemistry & Structural Bioinformatics (Pharmacophore Screening, Molecular Docking, MD/MM-GBSA, and DFT of Carbonic Anhydrase IX Inhibitors).
* **Study Design Type:** Purely in silico drug discovery pipeline (MOE 2022 pharmacophore screening of ZINC15 and DrugBank, AutoDock Vina docking to PDB `5FL4`, ProTox 3.0 toxicity prediction, 100–200 ns GROMACS MD simulations, `gmx_MMPBSA` free energy estimation, and B3LYP/6-311G DFT calculations).

---

## 2. Executive Summary & Editorial Verdict

This study constructs two ligand-based 3D pharmacophore models from known carbonic anhydrase IX (CA IX) sulfonamide inhibitors (`9FK` and `CJK`/SLC-0111) to screen the ZINC15 and DrugBank libraries, obtaining 580 hits. After docking into CA IX (PDB `5FL4`) using AutoDock Vina, four compounds (`ZINC613262012`, `ZINC427910039`, `ZINC616453231`, and `DB00482`/celecoxib) are evaluated via ProTox 3.0 toxicity predictions, 100–200 ns GROMACS molecular dynamics simulations, MM-PBSA/MM-GBSA binding free energy calculations, B3LYP/6-311G DFT orbital analyses, and off-target docking against CA I and CA II. The authors conclude that `ZINC427910039` ($\Delta G_{\text{TOTAL}} = -18.77\text{ kcal/mol}$), `DB00482` ($-12.29\text{ kcal/mol}$), and `ZINC613262012` ($-10.92\text{ kcal/mol}$) are potent, non-toxic, and isoform-selective CA IX inhibitors with narrow HOMO–LUMO energy gaps ($0.17\text{--}0.19\text{ eV}$).

**Editorial Verdict: Reject (Fundamentally Invalid, 2.6 / 10.0).** The manuscript contains severe unit errors, multiple direct contradictions between the main text and its own tables, and flawed metalloenzyme modeling. First, in the DFT analysis (Section 2.8.1 and Table 6), the authors report Gaussian orbital eigenvalues in **atomic units (Hartrees)** directly as **electron volts (eV)** without multiplying by $27.2114\text{ eV/Ha}$, falsely claiming that wide-gap sulfonamides ($\Delta E \approx 4.76\text{--}5.16\text{ eV}$) have semiconductor-like HOMO–LUMO gaps of $0.17490\text{--}0.18964\text{ eV}$. Second, every single claim in the Toxicity section (Section 2.4) contradicts Table 3: Table 3 shows that lead compound `ZINC427910039` is hepatotoxic (`Active (0.51)`), `9FK` is carcinogenic, and `ZINC613262012` has $\text{LD}_{50} = 1000\text{ mg/kg}$, whereas the text claims `ZINC616453231` is the hepatotoxic compound, `CJK` is carcinogenic, and `ZINC613262012` has $\text{LD}_{50} = 5000\text{ mg/kg}$. Third, in Section 2.10, the text claims all three hits bind CA IX more strongly than off-target CA II, when Table 7 explicitly shows `ZINC613262012` binds CA II (`−8.1 kcal/mol`) more strongly than CA IX (`−8.0 kcal/mol`). Finally, Section 4.2 states that all co-crystallized non-protein molecules were deleted from PDB `5FL4` (`"All the molecules crystallized with CA IX were deleted, only the CA IX structure was kept"`), and the MM-GBSA electrostatic energies ($\Delta E_{\text{elec}} = -3.70\text{ kcal/mol}$ for reference inhibitor `CJK` and $-5.37\text{ kcal/mol}$ for `DB00482`) confirm that inner-sphere $\text{Zn}^{2+}$–sulfonamide coordination was not properly parameterized.

### Specific Conclusions and Assessment of Support

* **DFT calculations demonstrate that `ZINC613262012`, `DB00482`, and `ZINC427910039` have small HOMO–LUMO energy gaps ($0.17490\text{--}0.18964\text{ eV}$) and high chemical softness ($10.5\text{--}11.4\text{ eV}^{-1}$): [Methodologically Flawed].**  
  Gaussian outputs orbital eigenvalues in Hartrees ($\text{Ha}$), not electron volts ($\text{eV}$). The reported HOMO values ($-0.26193$ to $-0.25681$) and LUMO values ($-0.08551$ to $-0.06934$) are in Hartrees; converting to eV ($\times 27.2114\text{ eV/Ha}$) yields HOMO $\approx -7.13$ to $-6.99\text{ eV}$, LUMO $\approx -2.33$ to $-1.89\text{ eV}$, and true HOMO–LUMO gaps of $4.76\text{--}5.16\text{ eV}$. The biological interpretation of "small HOMO-LUMO excitation energies" is an artifact of failing to convert atomic units.

* **Lead compound `ZINC427910039` is non-hepatotoxic and `ZINC613262012` has the highest safety margin ($\text{LD}_{50} = 5000\text{ mg/kg}$): [Methodologically Flawed].**  
  Section 2.4 directly contradicts Table 3 on three separate facts: (1) Table 3 shows `ZINC427910039` is **Active (0.51)** for hepatotoxicity while `ZINC616453231` is Inactive, opposite to the text; (2) Table 3 shows `9FK` is Active for carcinogenicity while `CJK` is Inactive, opposite to the text; and (3) Table 3 shows `ZINC613262012` has $\text{LD}_{50} = 1000\text{ mg/kg}$ (with `CJK` at $5000\text{ mg/kg}$ and `ZINC427910039` at $3500\text{ mg/kg}$), opposite to the text.

* **Comparative docking proves that `ZINC613262012`, `ZINC427910039`, and `DB00482` are selective for CA IX over off-target isoforms CA I and CA II: [Overstated].**  
  In Table 7, `ZINC613262012` scores $-8.1\text{ kcal/mol}$ against CA II versus $-8.0\text{ kcal/mol}$ against CA IX (Table 1), refuting the text's claim that all three compounds prefer CA IX over CA II. For `ZINC427910039` ($-8.0$ vs. $-7.8\text{ kcal/mol}$) and `DB00482` ($-8.7$ vs. $-8.4\text{ kcal/mol}$), a $0.2\text{--}0.3\text{ kcal/mol}$ AutoDock Vina difference is well within the scoring function's intrinsic error ($\sim 2.0\text{ kcal/mol}$).

* **MD simulations and MM-PBSA/MM-GBSA confirm that `ZINC427910039`, `DB00482`, and `ZINC613262012` bind CA IX more strongly than reference inhibitors `9FK` and `CJK`: [Fragile].**  
  Sulfonamide inhibitors bind carbonic anhydrases via deprotonation ($\text{R-SO}_2\text{NH}^-$) and direct coordination to the catalytic $\text{Zn}^{2+}$ cofactor (coordinated by His94, His96, and His119—misidentified as His116 in line 14). Standard CGenFF/CHARMM additive force fields and AutoDock Vina do not model dative $\text{Zn}^{2+}$–$\text{N}^-$ coordination bonds, and Section 4.2 states that all co-crystallized non-protein entities were deleted from `5FL4`. Consequently, the reference inhibitor `CJK` (SLC-0111, a nanomolar clinical CA IX inhibitor) exhibits an unphysically weak MM-GBSA electrostatic energy ($\Delta E_{\text{elec}} = -3.70\text{ kcal/mol}$, $\Delta G_{\text{TOTAL}} = -5.62\text{ kcal/mol}$).

---

## 3. Forensic Defect Inventory

### 1. Failure to Convert Hartrees (Atomic Units) to Electron Volts (`eV`) in DFT Table 6
* **Location:** Section 2.8.1 (line 160), Table 6 (lines 163–180), and Section 3 (line 228).
* **Defect:** Table 6 reports `HOMO` (`−0.26193` to `−0.25681`), `LUMO` (`−0.08551` to `−0.06934`), and `Energy gap (eV)` (`0.17490` to `0.18964`) as electron volts (`eV`). These numbers are raw Gaussian output eigenvalues in **Hartrees ($\text{Ha}$)**. Multiplying by $27.2114\text{ eV/Ha}$ shows the actual HOMO–LUMO gaps are $4.76\text{--}5.16\text{ eV}$ and chemical hardness $\eta$ is $2.38\text{--}2.58\text{ eV}$ (not $0.087\text{--}0.095\text{ eV}$). Furthermore, Table 6 defines `Energy gap` as `E_HOMO − E_LUMO` (which yields a negative number), defines electronegativity as `χ = −1/2 (I + A)` (yielding negative electronegativities `−0.16711` to `−0.17296`), and miswrites Parr's electrophilicity formula as `ω = 2 (μ^2 / η)` while computing $\mu^2 / (2\eta)$.

### 2. Threefold Contradiction Between Toxicity Text (Section 2.4) and Table 3
* **Location:** Section 2.4 (lines 85–86) vs. Table 3 (lines 89–99).
* **Defect:**
  1. **Hepatotoxicity column swap:** Line 86 states that all compounds were inactive for hepatotoxicity *"except for compound ZINC616453231, which was found to be active with a Hepatotoxicity score of 0.51."* In Table 3, `ZINC616453231` is `Inactive`, whereas lead candidate **`ZINC427910039` is `Active (0.51)`**.
  2. **Carcinogenicity column swap:** Line 86 states that reference drug `CJK` was active for carcinogenicity, whereas Table 3 reports `9FK = Active` and `CJK = Inactive`.
  3. **$\text{LD}_{50}$ column misreading:** Line 86 states *"Compound ZINC613262012 had the highest LD50 of 5000 mg/kg,"* whereas Table 3 reports `LD50 = 1000 mg/kg` for `ZINC613262012` and `5000 mg/kg` for `CJK`.

### 3. Contradiction Between Text and Table 7 on CA II Isoform Selectivity
* **Location:** Section 2.10 (lines 207–222) and Table 7.
* **Defect:** Line 209 asserts that *"all three potential ligands showed better binding to CA IX than to the off-target isoforms CA I and CA II."* Comparing Table 1 (CA IX) with Table 7 (CA II) shows that `ZINC613262012` has a docking score of **$-8.0\text{ kcal/mol}$ in CA IX** versus **$-8.1\text{ kcal/mol}$ in CA II**—meaning it scored *better* against off-target CA II than against CA IX. Additionally, no PDB accession codes or grid coordinates are reported for the CA I and CA II structures used in Table 7.

### 4. Improper Metalloenzyme Handling ($\text{Zn}^{2+}$ Deletion / Unparameterized Sulfonamide Coordination)
* **Location:** Section 1 (line 14), Section 2.7 (Table 5), and Section 4.2 (second chunk, line 243).
* **Defect:**
  1. Section 4.2 states: *"All the molecules crystallized with CA IX were deleted, only the CA IX structure was kept."* Deleting all co-crystallized non-protein residues removes the catalytic $\text{Zn}^{2+}$ ion. Even if $\text{Zn}^{2+}$ was retained in some steps, standard AutoDock Vina and CGenFF do not parameterize inner-sphere $\text{R-SO}_2\text{NH}^-\cdots\text{Zn}^{2+}$ coordination, as evidenced by the tiny gas-phase electrostatic interaction energies in Table 5 for known $\text{Zn}^{2+}$-coordinating sulfonamides (`CJK`: $\Delta E_{\text{elec}} = -3.70\text{ kcal/mol}$; `DB00482`: $\Delta E_{\text{elec}} = -5.37\text{ kcal/mol}$).
  2. Line 14 and Figure 1 legend misidentify the third $\text{Zn}^{2+}$-coordinating histidine of CA IX as **His116** instead of **His119**.

### 5. Methodological Confusion (MM-PBSA vs. MM-GBSA), Missing Equations, and Residue Mismatches
* **Location:** Section 2.2 (lines 37–55), Table 1, Table 5, Section 4.6 (second chunk, lines 14–27), and Section 5 (line 36).
* **Defect:**
  1. **MM-PBSA vs. MM-GBSA:** The manuscript titles Sections 2.7 and 4.6 `MM-PBSA Analysis` (Poisson–Boltzmann), yet Table 5 reports `ΔEGB` (Generalized Born polar solvation energy) and Sections 2.10 and 5 refer to `MM-GBSA`.
  2. **Missing equations in Section 4.6:** Lines 16–18 state *"Gmx_MMPBSA estimates the binding free energy as follows: [blank] In the above equations −TΔS denotes the entropic contribution..."*—the equations were omitted during typesetting, and conformational entropy ($-T\Delta S$) was not actually calculated in Table 5 ($\Delta G_{\text{TOTAL}} = \Delta G_{\text{GAS}} + \Delta G_{\text{SOLV}}$).
  3. **Residue numbering mismatches:** Line 37 refers to `Thr200 and Thr203` instead of `Thr200 and Thr201`; line 55 says `ZINC613262012` H-bonds with `His68` while Table 1 lists `His86`.
  4. **Biological misstatement:** Conclusions line 36 states the goal was identifying small-molecule inhibitors targeting CA IX *"to knockdown its expression"*—small-molecule catalytic inhibitors inhibit enzymatic activity, not gene expression.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.6** | **3.5** | Raw Hartree eigenvalues reported as eV in DFT Table 6 (27.2-fold unit error); unparameterized/deleted $\text{Zn}^{2+}$ active-site coordination yielding $\Delta E_{\text{elec}} = -3.70\text{ kcal/mol}$ for reference sulfonamide `CJK`; single-replicate MD; conflation of MM-PBSA and MM-GBSA. |
| **2. Claim-to-Evidence Alignment** | **0.5** | **2.5** | Every claim in Section 2.4 (hepatotoxicity, carcinogenicity, and $\text{LD}_{50}$) directly contradicts Table 3; Section 2.10 claims selectivity over CA II when Table 7 shows `ZINC613262012` binds CA II ($-8.1$) better than CA IX ($-8.0$). |
| **3. Data Integrity & Biological Plausibility** | **0.8** | **2.0** | Physically impossible HOMO–LUMO gaps ($0.17\text{ eV}$) for organic sulfonamides due to Hartree-to-eV omission; misidentification of catalytic His119 as His116; claim that catalytic inhibitors "knockdown expression" of CA IX. |
| **4. Reproducibility & Data Integrity** | **0.7** | **2.0** | Missing equations in Section 4.6; missing PDB IDs and grid boxes for off-target CA I and CA II docking; residue mismatches between text and Table 1 (`Thr203` vs `Thr201`, `His68` vs `His86`). |
| **Scientific Core Score** | **1.9** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **2.6** | **10.0** | **Fundamentally Invalid Tier (1.0 – 2.9).** |
