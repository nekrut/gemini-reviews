# Review of OOD_ANON_10

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.0 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.8/3.5 | Claims: 1.6/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.3/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This computational drug discovery study constructs a multi-stage virtual screening pipeline to identify novel small-molecule inhibitors of vascular endothelial growth factor receptor-2 (VEGFR2). Using 5,789 Rule-of-Five-compliant VEGFR2 bioactivity records from ChEMBL (dichotomized at $\text{pIC}_{50} = 6.8$ into 2,978 actives and 2,811 inactives) encoded with 2,048-bit Morgan3 fingerprints, the authors train Random Forest (RF), Support Vector Machine (SVM), and Artificial Neural Network (ANN) classifiers ($\text{RF test AUC} = 0.91, 5\text{-CV AUC} = 0.90 \pm 0.01$). They screen $\sim 10.5\text{ million}$ compounds from the eMolecules database, retain 61 PAINS-filtered hits with predicted active probability $> 85\%$, rank them by 2D fingerprint similarity (Morgan2 and MACCS Tanimoto/Dice) against seven FDA-approved VEGFR2 inhibitors, and select two top candidates (`molecule1` [PubChem CID 17379777] and `molecule2` [PubChem CID 4682044]). They then predict $\text{pIC}_{50}$ values via an RF regressor ($7.23$ and $7.31$), evaluate ADMET and ProTox-II toxicity profiles, and perform AutoDock Vina docking followed by triplicate all-atom GROMACS molecular dynamics (MD) simulations and MM-PBSA binding free energy calculations on PDB 4ASE, reporting binding free energies of $-89.1$, $-95.3$, and $-87.4\text{ kJ/mol}$ for `molecule1`, `molecule2`, and reference drug regorafenib, respectively.

The workflow has clear practical merits: unlike purely docking-based screens, it combines a large ChEMBL training set ($N = 5,789$) with triplicate explicit-solvent MD simulations and MM-PBSA free-energy calculations, provides exact PubChem CIDs for both candidate hits, and appropriately frames the two compounds as candidates for further investigation. However, the study has several methodological and technical weaknesses: (1) random 80/20 splitting of ChEMBL congeneric series without scaffold splitting inflates QSAR metrics, and in Table 3 the top-4 similarity results for Pazopanib and Axitinib are verbatim duplicates down to 6 decimal places; (2) the MD simulation duration is never stated in the Materials and Methods (only "the last 25 ns" is mentioned in the Results); (3) the regression formulas in the Methods contain typographical errors ($y_i$ vs. $\hat{y}$ and swapped definitions of $\bar{y}$ and $\hat{y}$); and (4) the external regression test set of "11 approved inhibitors" may overlap with the ChEMBL training set.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Triplicate MD stability and MM-PBSA binding free energy of `molecule1` ($-89.1\text{ kJ/mol}$) and `molecule2` ($-95.3\text{ kJ/mol}$) comparable to regorafenib ($-87.4\text{ kJ/mol}$) in VEGFR2 (PDB: 4ASE, Figure 8, Table S3): [Moderately Supported].**  
  Running triplicate explicit-solvent MD simulations in GROMACS with CHARMM36/CGenFF parameters and computing MM-PBSA binding free energies over the equilibrated trajectory is a substantial improvement over static docking alone. Furthermore, the per-residue energetic decomposition (identifying hydrophobic contacts with L840, V848, V916, F918, L1035, C1045, and F1047 in the DFG-out pocket of 4ASE) is biophysically consistent with known VEGFR2 Type II binding modes. However, the Materials and Methods section omits the total production MD simulation time (stating only $100\text{ ps}$ for NVT/NPT equilibration and later mentioning "the last 25 ns" in the Results), omits standard deviations across the तीन replicates for the MM-PBSA energies ($-89.1$ vs. $-87.4\text{ kJ/mol}$ is well within typical MM-PBSA thermal fluctuation of $\pm 10\text{ kJ/mol}$), and does not verify conserved hydrogen bonding to the hinge residue Cys919 or DFG Asp1046/Glu885.

* **2D fingerprint similarity ranking against seven approved VEGFR2 inhibitors (Table 3, Figure 5): [Fragile].**  
  In Table 3, the rows for `Pazopanib` and `Axitinib` are 100% identical across all four top molecules and all four similarity metrics down to the sixth decimal place:
  - `Pazopanib` top hits: Molecule 38 ($0.232877, 0.377778, 0.509804, 0.675325$), Molecule 23 ($0.226667, 0.369565, 0.750000, 0.857143$), Molecule 20 ($0.225352, 0.367816, 0.461538, 0.631579$).
  - `Axitinib` top hits: Molecule 38 ($0.232877, 0.377778, 0.509804, 0.675325$), Molecule 23 ($0.226667, 0.369565, 0.750000, 0.857143$), Molecule 20 ($0.225352, 0.367816, 0.461538, 0.631579$).
  Because Pazopanib (an indazolylpyrimidine sulfonamide) and Axitinib (an indazole-benzamide) have different chemical structures and different Morgan2/MACCS bit vectors, they cannot have identical 6-decimal Tanimoto and Dice similarities to Molecules 38, 23, and 20; the Pazopanib results were accidentally pasted into the Axitinib block (or vice versa). Additionally, Table 3 never explicitly states which numbered hit among the 61 compounds (e.g., Molecule 40, 16, 38, 23) corresponds to `molecule1` (CID 17379777) and `molecule2` (CID 4682044).

* **RF classification ($\text{AUC} = 0.91$) and RF regression ($\text{Test } R^2 = 0.7879$, external 11-drug $R^2 = 0.8173$) on 5,789 ChEMBL VEGFR2 compounds (Tables 1, 2, 4): [Moderately Supported].**  
  The 5,789 ChEMBL dataset is well-balanced ($2,978$ actives vs. $2,811$ inactives at $\text{pIC}_{50} = 6.8$) and evaluated via both an 80/20 test split and 5-fold cross-validation. However, two caveats apply: (1) random splitting of ChEMBL medicinal chemistry datasets places close structural analogs from the same publication into both training and test sets, yielding optimistic $R^2$ and AUC compared to Bemis-Murcko scaffold splitting; and (2) the "11 approved inhibitors" used as an external regression test set in Table 4 are standard clinical VEGFR2 inhibitors (such as sorafenib, pazopanib, regorafenib, axitinib, lenvatinib) whose bioactivities are extensively deposited in ChEMBL, meaning they were almost certainly present in the 5,789 ChEMBL training set unless explicitly filtered out prior to training.

* **ADMET and BOILED-Egg oral bioavailability characterization of `molecule1` and `molecule2` (Figure 7, Table 5): [Fragile].**  
  In the BOILED-Egg analysis (Figure 7 and accompanying text), `molecule2` falls in the gray zone outside the white ellipse, indicating predicted low passive gastrointestinal absorption, while `molecule1` is predicted to be poorly soluble by ESOL and is a P-gp efflux substrate (blue dot in Figure 7) with its lipophilicity vertex outside the optimal bioavailability radar (Supplementary Figure S3). The authors report these trade-offs honestly in the text, though the Conclusion overstates their readiness as "potent anti-cancer agents."

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct the Duplicated Axitinib/Pazopanib Rows in Table 3 and Map Hit IDs to PubChem CIDs
* **WHY:** In Table 3, the similarity scores for Axitinib are an exact copy-paste of Pazopanib, and readers cannot tell which numbered hit (e.g., 40, 16, 38, 23) is `molecule1` (CID 17379777) vs. `molecule2` (CID 4682044).
* **WHAT:** Recompute the Morgan2 and MACCS Tanimoto/Dice similarity scores for Axitinib (or Pazopanib) in Table 3, and explicitly label which compound numbers correspond to `molecule1` and `molecule2`.
* **HOW:** Re-run the RDKit similarity script for Axitinib against the 61 hits, update the Axitinib rows in Table 3, fix the typo `0.7660000` (7 decimals) in the Ki8751 row, and add a footnote or parenthetical label in Table 3 (e.g., `40 (molecule1, CID 17379777)` and `16 (molecule2, CID 4682044)`).

#### 2. Report Full MD Simulation Duration, Replicate Standard Deviations, and Hydrogen-Bond Occupancies
* **WHY:** The Methods section states the equilibration time ($100\text{ ps}$) but omits total production MD length, and reporting single MM-PBSA point estimates ($-89.1, -95.3, -87.4\text{ kJ/mol}$) without standard deviations across the three independent replicates prevents assessing whether the $1.7$–$7.9\text{ kJ/mol}$ differences from regorafenib are statistically meaningful.
* **WHAT:** Specify the total ns duration of each triplicate MD trajectory in the Methods, report `mean ± SD` across the 3 replicates for all MM-PBSA energy components in the main text and Supplementary Table S3, and report hydrogen-bond occupancies with Cys919, Glu885, and Asp1046.
* **HOW:** Using `gmx hbond` and `g_mmpbsa` across the three independent trajectories, calculate the mean and standard deviation of $\Delta G_{\text{bind}}$ over the 3 replicates and the percentage of frames over the last 25 ns in which `molecule1`, `molecule2`, and regorafenib maintain H-bonds with Cys919, Glu885, and Asp1046.

#### 3. Verify Exclusion of the 11 External Approved Drugs from the ChEMBL Training Set and Test Scaffold Splitting
* **WHY:** Approved VEGFR2 drugs (sorafenib, regorafenib, pazopanib, etc.) have dozens of $\text{pIC}_{50}$ entries in ChEMBL; if they were not removed from the 5,789 ChEMBL compounds before training the WEKA RF regressor, the "11 approved inhibitors" external test set in Table 4 ($R^2 = 0.8173$) suffers from training-test overlap.
* **WHAT:** Remove all ChEMBL entries matching the InChIKeys or canonical SMILES (and Tanimoto $> 0.95$ analogs) of the 11 approved drugs before training the RF regressor, and additionally report 5-fold Bemis-Murcko scaffold-split cross-validation metrics in Tables 2 and 4.
* **HOW:** Filter the 5,789 ChEMBL dataset in RDKit by canonical SMILES/InChIKey against the 11 reference inhibitors, retrain the RF regressor on the de-duplicated set, and update Table 4 and Figure 6.

#### 4. Fix Mathematical Formulas and Software Version Citations
* **WHY:** The MAE, RMSE, and $R^2$ equations in the Methods ("Evaluation metrics of predictive models") have missing parentheses, missing absolute value bars, unindexed $\hat{y}$, and swapped definitions of $\bar{y}$ and $\hat{y}$ ("where $\bar{y}$ and $\hat{y}$ represent the predicted value of $y$ and the mean value, respectively"), and Figure 3 and 5 captions cite `scikit-learn` for radar plots and RDKit similarity maps.
* **WHAT & HOW:**
  1. Rewrite the regression equations as $\text{MAE} = \frac{1}{N}\sum_{i=1}^N |y_i - \hat{y}_i|$, $\text{RMSE} = \sqrt{\frac{1}{N}\sum_{i=1}^N (y_i - \hat{y}_i)^2}$, and $R^2 = 1 - \frac{\sum_{i=1}^N (y_i - \hat{y}_i)^2}{\sum_{i=1}^N (y_i - \bar{y})^2}$, and swap the definitions so $\hat{y}_i$ is the predicted value and $\bar{y}$ is the mean experimental value.
  2. Correct the Figure 5 caption to cite `RDKit` (rather than `Scikit-learn v 0.23.1`) for generating the circular fingerprint similarity maps.
