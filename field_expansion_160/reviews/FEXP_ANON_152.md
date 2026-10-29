# Review of FEXP_ANON_152

**Overall Score:** **3.3 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.5 / 8.0**  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.7/2.5 | Biology: 0.9/2.0 | Reproducibility: 0.8/2.0

---

## 1. Blinded Metadata Perception

* **Anonymized Manuscript ID:** `FEXP_ANON_152`
* **Perceived Field & Subfield:** Computational Medicinal Chemistry & Cheminformatics (3D-QSAR, Pharmacophore Modeling, Virtual Screening, Glide Docking, Prime MM/GBSA, and MD Simulations of Coumarin Acetylcholinesterase Inhibitors for Alzheimer's Disease).
* **Study Design Type:** Purely in silico drug design workflow (Schrödinger PHASE field-based 3D-QSAR and pharmacophore modeling on 60 literature coumarins, virtual screening of 400,000 PubChem coumarins against human AChE PDB `4M0E`, Glide HTVS/SP/XP docking, Prime MM/GBSA, QikProp ADME, and 100 ns GROMACS MD simulations).

---

## 2. Executive Summary & Editorial Verdict

The authors compile 60 coumarin derivatives with reported acetylcholinesterase (AChE) $\text{IC}_{50}$ values ($0.059\text{--}83.76\text{ }\mu\text{M}$) to build a Gaussian field-based 3D-QSAR model (selecting PLS factor 7) and a 5-point PHASE pharmacophore hypothesis (`ADHRR_1`). They use `ADHRR_1` to screen 400,000 PubChem coumarin records against human AChE (PDB ID: `4M0E`) via PHASE, Glide HTVS, SP, and XP docking, and Prime MM/GBSA, narrowing 245 compounds exceeding donepezil ($-8.271\text{ kcal/mol}$) to 10 hits (`HIT1`–`HIT10`). Following QikProp ADME evaluation, `HIT1` (`CID 134139986`) and `HIT2` (`CID 134155007`) are selected as leads and simulated for 100 ns using GROMACS 2021.6 (CHARMM36 force field) to propose a generic coumarin scaffold ("lead formula I").

**Editorial Verdict: Reject (Flawed / Overstated, 3.3 / 10.0).** While the sequential Schrödinger/GROMACS workflow is coherent in structure, the selected models and leads fail standard quantitative validation criteria reported in the manuscript's own tables. First, the chosen 3D-QSAR model at PLS factor 7 (trained on only $\sim 42$ compounds) is severely overfitted: its internal leave-one-out cross-validated $R^2_{\text{CV}}$ is **0.1945** (far below the minimum $0.50$ threshold), its $Y$-scrambling $R^2_{\text{Scramble}}$ is **0.8208** (indicating that random label permutation achieves $R^2 = 0.82$), its stability drops to **0.25**, and its external test-set $Q^2$ ($0.595$) and RMSE ($0.87$) are actually *worse* than at PLS factor 5 ($Q^2 = 0.6979$, $\text{RMSE} = 0.75$). Second, the pharmacophore enrichment table (Table 3) claims **65 active compounds** were ranked when the entire compiled library (actives + inactives combined) contained only **60 molecules** (lines 35, 122). Third, QikProp Table 5 contradicts the text's claim of favorable ADMET and toxicological profiles: all 10 hits fail the hERG cardiotoxicity threshold (`QPlogHERG > −5.0`), with `HIT1` exhibiting the worst predicted cardiotoxicity (`−7.753`) and extreme aqueous insolubility (`QPlogS = −8.156`).

### Specific Conclusions and Assessment of Support

* **The field-based 3D-QSAR model at PLS factor 7 is the best-validated and most predictive model for AChE inhibition: [Methodologically Flawed].**  
  Fitting 7 PLS latent factors to 42 training molecules (70% of 60) violates the rule of thumb of $\ge 10$ molecules per PLS component and produces severe overfitting in Table 1: cross-validated $R^2_{\text{CV}} = 0.1945$ (unacceptable as $R^2_{\text{CV}} < 0.5$), $Y$-scrambling $R^2_{\text{Scramble}} = 0.8208$ (confirming chance correlation), and model stability $= 0.25$. Moreover, test-set predictivity peaks at PLS factor 5 ($Q^2 = 0.6979$, $\text{RMSE} = 0.75$) and degrades at PLS factor 7 ($Q^2 = 0.595$, $\text{RMSE} = 0.87$).

* **Pharmacophore hypothesis `ADHRR_1` is the best-performing model, recovering 65 out of 65 active compounds in decoy enrichment testing: [Methodologically Flawed].**  
  Sections "Ligand preparation" (line 35) and "Pharmacophore modelling" (line 122) state that the entire dataset consisted of **60 molecules** spanning $\text{pIC}_{50} = 4.08\text{--}7.23$, of which only those with $\text{pIC}_{50} \ge 6.5$ were defined as active. It is arithmetically impossible for a subset of 60 molecules to contain **65 actives** (Table 3, line 146). Moreover, in Table 3, hypothesis `ADHRR_5` outperforms `ADHRR_1` on both `EF1%` ($13.41$ vs. $11.92$) and `BEDROC160.9` ($0.86$ vs. $0.64$).

* **All 10 hits display drug-like ADMET and favorable toxicological profiles, with `HIT1` and `HIT2` having the optimal CNS pharmacokinetic and MM/GBSA profiles: [Overstated].**  
  In Table 5, every single hit violates QikProp's hERG cardiotoxicity safety threshold (`QPlogHERG > −5.0`), with `HIT1` scoring `−7.753` (high risk of QT prolongation) and `HIT2` scoring `−6.755`. `HIT1` also violates QikProp's aqueous solubility limit (`QPlogS = −8.156` vs. recommended $-6.5\text{ to }0.5$). In Table 4, `HIT1` ($-60.19\text{ kcal/mol}$, ligand efficiency $-1.77$) and `HIT2` ($-60.16\text{ kcal/mol}$) rank 6th and 7th in MM/GBSA $\Delta G_{\text{Bind}}$ behind `HIT6` ($-70.94$), `HIT4` ($-69.63$), `HIT3` ($-68.70$), `HIT9` ($-65.67$), and `HIT7` ($-60.66\text{ kcal/mol}$), while `HIT5` and `HIT8` have superior BBB penetration (`QPlogBB = −0.795` and `−0.790`) and solubility (`QPlogS = −5.17` and `−5.20`).

* **100 ns MD simulations confirm thermodynamic stability of `HIT1` and `HIT2` in complex with AChE (`4M0E`): [Moderately Supported].**  
  The backbone RMSD ($0.20\text{--}0.28\text{ nm}$), $R_g$ ($2.30\text{--}2.33\text{ nm}$), ligand RMSF ($0.02\text{--}0.37\text{ nm}$), and hydrogen-bond occupancy profiles over 100 ns are physically plausible for human AChE, though no reference simulation of Donepezil–`4M0E` or apo-`4M0E` and no independent trajectory replicates ($n=1$) were included for baseline comparison.

---

## 3. Forensic Defect Inventory

### 1. Severe Overfitting and Chance Correlation in the PLS-7 3D-QSAR Model (Table 1)
* **Location:** Section *Field-based 3D-QSAR modelling* (lines 87–100) and Table 1.
* **Defect:** At PLS factor 7, Table 1 reports $R^2_{\text{CV}} = 0.1945$, $R^2_{\text{Scramble}} = 0.8208$, and $\text{Stability} = 0.25$. In QSAR validation (OECD and Golbraikh–Tropsha criteria), a valid model requires $R^2_{\text{CV}} > 0.50$ and $R^2_{\text{Scramble}} \ll R^2$ (typically $< 0.30$). An $R^2_{\text{Scramble}}$ of $0.8208$ means that randomly shuffling the biological activities yields an $R^2$ of $0.82$, proving that 7 PLS components overfit the 42 training molecules. Furthermore, test-set $Q^2$ and RMSE deteriorate from PLS 5 ($Q^2 = 0.6979, \text{RMSE} = 0.75$) to PLS 7 ($Q^2 = 0.595, \text{RMSE} = 0.87$).

### 2. Arithmetic Contradiction in Pharmacophore Active Count (`65 Actives` Out of `60 Total Molecules`) and Decoy MW Error
* **Location:** Lines 35, 45, 122, 146, and Table 3 (lines 149–161).
* **Defect:**
  1. Lines 35 and 122 state that 60 coumarin molecules in total were collected, and those with $\text{pIC}_{50} \ge 6.5$ were assigned as active while those with $\text{pIC}_{50} \le 4.5$ were assigned as inactive. Yet line 146 and Table 3 report `Total Actives = 65` and `Ranked Actives = 65`.
  2. Line 122 states that the 60 compounds fell *"within the range of $\text{pIC}_{50}$ values of $4.5\text{--}6.5$,"* which contradicts both line 35 ($\text{IC}_{50} = 0.059\text{--}83.76\text{ }\mu\text{M} \implies \text{pIC}_{50} = 4.08\text{--}7.23$) and the activity cutoffs ($\text{pIC}_{50} \ge 6.5$ and $\le 4.5$).
  3. Line 45 states that decoys had `Avg. M.W. = 400 kDa` ($400,000\text{ Da}$) instead of $400\text{ Da}$.
  4. Line 146 writes *"whereas BEDROC160.9, Phase Hypo Score scores were 11.92, 0.64 and 0.90, respectively,"* mistakenly repeating `11.92` (`EF1%`).

### 3. Unacknowledged QikProp Toxicity/Solubility Failures and Missing `QPPCaco` Column in Table 5
* **Location:** Section *ADMET* (lines 210–228) and Table 5.
* **Defect:**
  1. **Cardiotoxicity (`QPlogHERG`):** Table 5 specifies the safe range as `(above −5.0)`, yet all 10 hits are below $-5.9$, with lead `HIT1` at `−7.753` and `HIT2` at `−6.755`.
  2. **Insolubility (`QPlogS`) and Misprinted Header:** Table 5 misprints the recommended `QPlogS` range as `(<5.0)` instead of QikProp's standard `−6.5 to 0.5`; `HIT1` has `QPlogS = −8.156` (severe insolubility).
  3. **Backwards `PSA` header:** Table 5 lists the recommended range as `PSA (above 100)`, which both `HIT1` (`95.537`) and `HIT2` (`97.119`) fail.
  4. **Missing `QPPCaco`:** Line 212 discusses `QPPCaco (>70)`, which is absent from Table 5 (Table 5 only reports `QPPMDCK`, where `HIT2 = 230.009` falls below the header's `Great: >500 nm/s`).

### 4. Active-Site Residue Typos, Missing Equations, and Software Version Discrepancies
* **Location:** Lines 25, 36, 55, 66, 178, 189, 212, 231, 236.
* **Defect:**
  1. **Residue numbering typos in human AChE (`4M0E`):** Line 178 lists `TRP 284` and `TYR 41` (and repeats `SER 203` twice), and line 236 lists `TYR 34`; the actual PAS residues in human AChE (`4M0E`) are `TRP 286` and `TYR 341`.
  2. **Missing equations:** The $\text{pIC}_{50}$ conversion formula (line 36) and MM/GBSA Equation (1) (line 66) are blank in the text.
  3. **Software version discrepancies:** Maestro/Schrödinger versions are inconsistently cited as `Maestro 12.9` (lines 25, 35, 45, 60), `Maestro 12.5` (line 55), and `Schrödinger 10.7` (line 212).
  4. **Typo in MD description:** Line 231 states $R_g$ had *"negligible variation during trajectory of ~3 nm"* instead of $100\text{ ns}$ (or $0.03\text{ nm}$ variation).

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.9** | **3.5** | Severe 3D-QSAR overfitting at PLS 7 ($R^2_{\text{CV}} = 0.1945$, $R^2_{\text{Scramble}} = 0.8208$, degraded test $Q^2$ vs. PLS 5); arithmetic contradiction of 65 actives from a 60-ligand dataset; no MD positive control (`Donepezil–4M0E`) or replicates. |
| **2. Claim-to-Evidence Alignment** | **0.7** | **2.5** | Claims `HIT1` and `HIT2` have favorable toxicological and ADME profiles when Table 5 shows severe `QPlogHERG` cardiotoxicity alerts (`−7.753`, `−6.755`) and extreme insolubility for `HIT1` (`QPlogS = −8.156`). |
| **3. Data Integrity & Biological Plausibility** | **0.9** | **2.0** | `400 kDa` decoy molecular weight error; AChE active-site residue typos (`TRP 284`, `TYR 41`, `TYR 34` instead of `TRP 286`, `TYR 341`); selection of `HIT1`/`HIT2` despite inferior MM/GBSA $\Delta G_{\text{Bind}}$, ligand efficiency, and BBB permeability compared to `HIT5`/`HIT8`. |
| **4. Reproducibility & Data Integrity** | **0.8** | **2.0** | PubChem CIDs for `HIT1`–`HIT10` and PDB ID `4M0E` are provided, but the 60-compound training table (`Table S1`) and equations (lines 36, 66) are missing from the main text, `QPPCaco` is omitted from Table 5, and data are available only on request. |
| **Scientific Core Score** | **2.5** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **3.3** | **10.0** | **Flawed / Overstated Tier (3.0 – 4.9).** |
