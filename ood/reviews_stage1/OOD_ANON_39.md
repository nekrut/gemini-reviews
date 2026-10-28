# Review of OOD_ANON_39

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **3.5 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.0/3.5 | Claims: 0.9/2.5 | Biology: 0.9/2.0 | Reproducibility: 0.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This computational study builds a 3-descriptor multiple linear regression (MLR) 2D-QSAR model ($\text{pIC}_{50}$ predicted from polar surface area `PSA`, dipole moment $\mu$, and molecular weight `MW`) on 50 literature acetylcholinesterase (AChE) inhibitors (5-phenyl-1,3,4-oxadiazole and *N*-benzylpiperidine analogs). Using this equation, the authors design 11 virtual analogs (`M1`–`M11`), screen 5 candidates (`M1, M2, M6, M9, M10`) using SwissADME and pkCSM, dock `M1, M2, M6`, and Donepezil into human AChE (`PDB: 4EY7`), and run 100 ns Desmond molecular dynamics (MD) simulations and MM-GBSA free-energy calculations on `M1, M2`, and Donepezil. No experimental synthesis or biochemical AChE assay is performed, and the chemical structures and descriptor values of the 50 dataset molecules and 11 designed molecules are omitted from the text tables (Tables 4 and 8).

The manuscript is undermined by pervasive internal contradictions across its statistical metrics, compound selection rules, and physical parameters. First, the primary QSAR validation metrics reported in the Abstract and Conclusions ($R^2 = 0.701, Q^2_{\text{CV}} = 0.638, R^2_{\text{test}} = 0.76, \text{RMSE} = 0.336$) directly contradict the values reported in the Results section ($R^2 = 0.64, Q^2_{\text{CV}} = 0.56, R^2_{\text{test}} = 0.72, \text{RMSE} = 0.35$; line 36). Second, the Applicability Domain critical leverage threshold is stated as $h^* = 0.300$ in Section 2.3 (line 99) but as $h^* = 0.450$ in Section 2.4 (line 142), and leverage values are omitted for 5 of the 11 designed molecules in Table 4. Third, Section 2.5 concludes that "only compounds M1, M2, and M9 presented an ADMET profile" suitable for docking (line 186), yet Section 2.6 immediately docks `M1, M2, and M6` instead of `M9` (line 199). Because the 2D-QSAR model relies solely on bulk molecular size and polarity (`MW`, `PSA`, $\mu$) without pharmacophore or 3D steric terms, maximizing predicted $\text{pIC}_{50}$ simply inflates molecular weight and lipophilicity ($\log P = 5.90\text{--}6.86$).

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The 3-descriptor MLR 2D-QSAR model achieves high internal and external predictive validity ($R^2 = 0.701, Q^2_{\text{CV}} = 0.638, R^2_{\text{test}} = 0.76, \text{RMSE} = 0.336$ in Abstract/Conclusions vs. $R^2 = 0.64, Q^2_{\text{CV}} = 0.56, R^2_{\text{test}} = 0.72, \text{RMSE} = 0.35$ in Results): [Methodologically Flawed].**  
  Every validation statistic in the Abstract (line 8) and Conclusions (line 361) conflicts with the Results text (line 36). Checking the reported Fisher statistic ($F = 21.54$ at $n_{\text{train}} = 40, K = 3, df = 3, 36$) confirms that $R^2 = \frac{3 \times 21.54}{3 \times 21.54 + 36} = 0.642$, matching the lower figures in Section 2 rather than the inflated numbers in the Abstract and Conclusions. Furthermore, pooling two distinct chemical scaffolds (5-phenyl-1,3,4-oxadiazoles and *N*-benzylpiperidines from refs. [46, 47]) into a model containing only `MW`, `PSA`, and $\mu$ captures gross scaffold-size differences rather than specific structure–activity relationships, and selecting descriptors by correlation screening on the full 50-compound dataset prior to the 80/20 train/test split (Sections 3.2–3.3, lines 312–317) introduces feature-selection leakage into $R^2_{\text{test}}$ and $Q^2_{\text{CV}}$.

* **All 11 designed molecules (`M1`–`M11`) lie inside the QSAR model's Applicability Domain (Table 4): [Methodologically Flawed].**  
  For $K = 3$ descriptors and $n = 40$ training compounds, the critical leverage is $h^* = 3(K+1)/n = 12/40 = 0.300$ (correctly stated in line 99), yet line 142 inexplicably changes the threshold to $h^* = 0.450$. In Table 4 (lines 131–136), leverage values ($h_i$) and `Outlier/Inside` classifications are completely missing (`-`) for compounds `M3, M4, M5, M7`, and `M8`.

* **Designed candidates exhibit favorable drug-likeness, blood–brain barrier (BBB) permeability, and ADMET profiles (Tables 5 and 6): [Overstated].**  
  First, because Eq. (1) rewards higher `MW` ($+0.010\,\text{MW}$) and lower `PSA` ($-0.007\,\text{PSA}$), the top designed compounds (`M1, M2, M6, M9`) have high lipophilicity ($\log P = 5.90\text{--}6.86$, Table 5), exceeding Lipinski's $\log P \le 5$ limit and nearing the $\text{MW} \le 500\text{ Da}$ ceiling ($476.5\text{--}492.5\text{ Da}$). Second, the text in Section 2.5 contradicts Table 6: line 167 states that "compounds with $\text{LogBB} > 0.3$ have the ability to cross the BBB... compounds M1, M2, M6, and M9 show the ability to cross the BBB," yet Table 6 shows that only `M1` ($\text{log BB} = 0.39$) exceeds $0.3$, while `M2` ($0.001$), `M6` ($0.12$), and `M9` ($-0.96$) do not. Third, line 149 states that `M4` failed Caco-2 permeability ($< 0.9$), whereas Table 6 does not include `M4` and instead shows `M9` failing Caco-2 permeability ($0.457$). Fourth, line 186 selects `M1, M2, and M9` for docking, but line 199 docks `M1, M2, and M6` instead.

* **Docking and 100 ns MD simulations confirm that `M1` and `M2` bind human AChE (`4EY7`) more strongly and stably than Donepezil: [Fragile].**  
  While redocking reproduces the crystal pose of Donepezil ($\text{RMSD} = 0.28\text{ \AA}$, line 191), in the 100 ns MD simulation of the native `4EY7` AChE–Donepezil crystal complex (line 250), the authors report that Donepezil's RMSD remained "at around $5.1\text{ \AA}$ (Figure 6d)." A ligand RMSD of $5.1\text{ \AA}$ for the co-crystallized reference drug Donepezil indicates either substantial drift of the reference ligand or an atom-selection/alignment error in the Desmond RMSD calculation, calling into question the baseline MD protocol and MM-GBSA comparison ($-64.78$ and $-80.66\text{ kcal/mol}$ vs. $-65.38\text{ kcal/mol}$ for Donepezil, reported without standard deviations across trajectory frames; line 272).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile QSAR Validation Statistics and Perform Feature Selection Strictly Inside the Training Set
* **WHY:** Reporting two incompatible sets of QSAR metrics ($R^2 = 0.701$ vs. $0.64$; $Q^2_{\text{CV}} = 0.638$ vs. $0.56$; $R^2_{\text{test}} = 0.76$ vs. $0.72$) and screening descriptors on the full 50-compound dataset before train/test splitting invalidates the statistical validation.
* **WHAT:** Reconcile the exact XLSTAT output for Equation (1), perform correlation/stepwise descriptor selection strictly on the 40 training-set compounds, and report all Golbraikh–Tropsha external validation criteria ($r^2, r_0^2, r_0'^2, k, k', r_m^2$).
* **HOW:** Re-run the MLR fit on the 40 training compounds, print the regression coefficients to 5 decimal places so that plugging Table 4 descriptors into Eq. (1) exactly reproduces the Table 4 $\text{pIC}_{50}$ column, and ensure identical metrics appear in the Abstract, Section 2, and Section 4.

#### 2. Provide Complete Chemical Structures (SMILES) and Descriptors in Tables 4 and 8, and Fix Leverage Calculations
* **WHY:** Tables 4 and 8 omit the chemical structures (or SMILES strings) of the 50 dataset compounds and 11 designed molecules, making the entire study impossible to verify or reproduce, and Table 4 omits leverage values for 5 designed compounds.
* **WHAT:** Add SMILES strings, `MW`, `PSA`, $\mu$, training/test set assignment, experimental $\text{pIC}_{50}$, predicted $\text{pIC}_{50}$, and leverage $h_i$ for all 50 dataset compounds in Table 8 and all 11 designed compounds in Table 4.
* **HOW:** Compute $h_i = x_i^\top (X_{\text{train}}^\top X_{\text{train}})^{-1} x_i$ for `M1`–`M11` against the consistent threshold $h^* = 3(3+1)/40 = 0.300$, and fill in the missing entries for `M3, M4, M5, M7`, and `M8` in Table 4.

#### 3. Audit the Donepezil MD Trajectory ($5.1\text{ \AA}$ RMSD) and Report Frame-Wise MM-GBSA Uncertainties
* **WHY:** Co-crystallized Donepezil in `4EY7` should remain tightly bound ($< 2.0\text{ \AA}$ ligand RMSD) in a properly parameterized OPLS3e MD simulation; a $5.1\text{ \AA}$ RMSD indicates either ligand unbinding or a periodic-boundary/superposition artifact, and single-number MM-GBSA values without standard deviations cannot distinguish $-64.78$ from $-65.38\text{ kcal/mol}$.
* **WHAT:** Inspect the `4EY7`–Donepezil trajectory in Desmond (checking piperidine nitrogen protonation state at pH 7.4 and protein-aligned vs. ligand-aligned RMSD) and report $\text{mean} \pm \text{SD}$ of $\Delta G_{\text{bind}}$ across 100 equally spaced trajectory snapshots from the equilibrated $60\text{--}100\text{ ns}$ window.
* **HOW:** Re-run the Desmond Simulation Interaction Diagram and `thermal_mmgbsa.py` script over the last $40\text{ ns}$ (every $0.4\text{ ns}$) for `M1, M2`, and protonated Donepezil, and report $\Delta G_{\text{bind}} \pm \text{SD}$ along with component breakdowns ($\Delta G_{\text{vdW}}, \Delta G_{\text{Coulomb}}, \Delta G_{\text{Lipo}}, \Delta G_{\text{Solv}}$).

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Inconsistent compound labels, software version errors, and physical unit mistakes confuse the reader.
* **WHAT & HOW:**
  1. **Section 2.5–2.6 (lines 149, 167, 186, 199):** Reconcile the discrepancies between `M4` vs. `M9` (Caco-2 permeability) and `M6` vs. `M9` (which 3 compounds were selected from Table 6 for docking in Table 7).
  2. **Section 3.1 (line 280):** Change `"converted into logarithmic form (logIC50)"` to `"negative logarithmic form (pIC50 = -log10(IC50 [M]))"`.
  3. **Sections 2.6 & 3.7 (lines 215, 345, 349):** Correct `"AutoDock vina software version 1.5.7"` (`1.5.7` is the version of `AutoDockTools / MGLTools`; report the actual version of `AutoDock Vina`, e.g., `1.1.2` or `1.2.3`).
  4. **Section 3.8 (line 356):** Correct the unit conversion `"1 ATM (101,325 bar)"` to `"1 atm (1.01325 bar / 101,325 Pa)"`.
