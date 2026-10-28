# Review of OOD_REP2_08

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.4 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.4/3.5 | Claims: 1.2/2.5 | Biology: 0.9/2.0 | Reproducibility: 0.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents a purely computational virtual screening pipeline aimed at identifying small-molecule inhibitors of vascular endothelial growth factor receptor-2 (VEGFR2). Using 5,789 Lipinski-compliant bioactivity records from ChEMBL (binarized at $\text{pIC}_{50} = 6.8$), the authors train random forest (RF), support vector machine (SVM), and artificial neural network (ANN) classifiers on 2,048-bit Morgan3 fingerprints via the TeachOpenCADD platform. They apply the RF classifier to ~10.5 million compounds from the eMolecules library, filter to 61 PAINS-free hits with predicted active probability $>85\%$, and select two candidate molecules (`molecule1`, PubChem CID 17379777; `molecule2`, PubChem CID 4682044) based on 2D Tanimoto and Dice fingerprint similarity to seven clinically approved VEGFR2 inhibitors. They subsequently predict $\text{pIC}_{50}$ values (7.23 and 7.31) using a WEKA RF regressor trained on 1,024-bit ECFP descriptors, evaluate ADMET and toxicity profiles via SwissADME, ProTox-II, and pkCSM, and perform AutoDock Vina docking (PDB: 4ASE) followed by triplicate GROMACS molecular dynamics (MD) simulations and MM-PBSA binding free energy calculations ($-89.1$, $-95.3$, and $-87.4\text{ kJ/mol}$ for `molecule1`, `molecule2`, and regorafenib, respectively).

While integrating ligand-based machine learning with structure-based simulation is a standard virtual screening strategy, the study's conclusions rest on a self-defeating screening design, uncalibrated statistical comparisons, and severe technical and editorial errors. Specifically, after screening 10.5 million compounds to find novel inhibitors, the authors select their final two candidates by maximizing 2D structural similarity to known drugs (reaching MACCS Dice similarity of 0.921 to sorafenib and regorafenib), which undermines structural novelty and inflates random-split QSAR performance due to analog bias. Furthermore, Table 3 contains an exact copy-paste duplication of similarity values across structurally distinct reference drugs (pazopanib and axitinib), mathematical definitions in the Methods section are corrupted and inverted, MD simulation durations and MM-PBSA uncertainty estimates are omitted, and no experimental biochemical validation is performed. Resolving these issues requires fixing the corrupted tables and equations, implementing scaffold-based cross-validation, reporting full MD trajectory lengths and MM-PBSA standard deviations across replicates, and tempering claims to reflect unvalidated in silico predictions.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Machine learning classification and regression accurately predict VEGFR2 inhibitory activity ($\text{AUC} = 0.91$, test $R^2 = 0.7879$) and yield $\text{pIC}_{50}$ predictions of 7.23 and 7.31 for the two candidates: [Overstated].**  
  Both the classification (Table 1) and regression (Table 4) models rely on random 80/20 train/test splits of ChEMBL congeneric series without scaffold or cluster splitting, which allows near-identical structural analogs to span training and test sets. In addition, the Methods state that model hyperparameters were adjusted on the split to "achieve the best performance" without nested cross-validation, and the 11 approved VEGFR2 inhibitors used as an "external test set" in Table 4 are well-represented in ChEMBL (nor is any check reported to ensure they and their close analogs were excluded from the 5,789 ChEMBL training compounds).

* **Two candidate compounds (`molecule1` and `molecule2`) selected via similarity screening against seven approved drugs represent promising novel VEGFR2 inhibitors: [Methodologically Flawed].**  
  Selecting hits from a 10.5-million-compound ML screen by picking the molecules with the highest 2D fingerprint similarity to existing FDA-approved drugs (sorafenib and regorafenib; Table 3 shows `Tanimoto_maccs` $= 0.854$ and `Dice_maccs` $= 0.921$ for compound 40) defeats the purpose of machine learning virtual screening and merely recovers close structural analogs of known urea/biaryl kinase inhibitors. Worse, Table 3 is internally corrupted: the rows for Pazopanib (compounds 38, 23, 20) and Axitinib (compounds 38, 23, 20) report the exact same Tanimoto and Dice similarity values to six decimal places (`0.232877`, `0.226667`, `0.225352`, `0.509804`, `0.750000`, `0.461538`), which is mathematically impossible given the distinct chemical structures of pazopanib and axitinib. The text also fails to map which compound indices in Table 3 correspond to `molecule1` (CID 17379777) and `molecule2` (CID 4682044).

* **MD simulations and MM-PBSA free energy calculations ($-89.1$ and $-95.3\text{ kJ/mol}$ vs. $-87.4\text{ kJ/mol}$ for regorafenib) demonstrate comparable or superior binding affinity to VEGFR2: [Fragile].**  
  The Methods section (lines 70–73) never specifies the total production MD simulation duration (mentioning only $100\text{ ps}$ of NVT/NPT equilibration, while the Results refer to "the last 25 ns"). Single-point MM-PBSA binding energies are reported without standard deviations or standard errors of the mean across the three independent trajectories or across frames. Differences of $1.7\text{ to }7.9\text{ kJ/mol}$ ($0.4\text{ to }1.9\text{ kcal/mol}$) lie well within the typical statistical and force-field uncertainty of MM-PBSA calculations ($\sim 15\text{–}25\text{ kJ/mol}$) and cannot support claims of stronger binding without error bars and experimental enzymatic assays.

* **In silico ADMET and toxicity predictions indicate favorable safety and bioavailability profiles for `molecule1` and `molecule2`: [Moderately Supported].**  
  The SwissADME, BOILED-Egg, ProTox-II, and pkCSM calculations follow standard web-server protocols, but the results themselves highlight substantial liabilities that contradict a uniformly favorable framing: `molecule1` is predicted to be poorly soluble and an effluxed P-gp substrate with lipophilicity outside the optimal bioavailability radar, while `molecule2` falls in the gray BOILED-Egg zone (low passive gastrointestinal absorption) and has a predicted $\text{LD}_{50}$ ($393\text{ mg/kg}$) less than half that of regorafenib ($800\text{ mg/kg}$).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Implement Scaffold Splitting and Eliminate Training-Test Leakage in QSAR Models
* **WHY:** Random 80/20 splitting of ChEMBL kinase datasets places congeneric analogs in both training and test partitions, inflating ROC-AUC and $R^2$ while failing to measure generalization to new scaffolds. Furthermore, evaluating an "external test set" of 11 approved VEGFR2 inhibitors without deduplicating them from the ChEMBL training set introduces direct data leakage.
* **WHAT:** Re-evaluate the classification (Table 1) and regression (Table 4) models using Bemis–Murcko scaffold splitting and verify that all 11 approved drugs (and any compound with Morgan2 Tanimoto $> 0.85$ to them) are strictly excluded from the ChEMBL training data.
* **HOW:** Using RDKit (`rdkit.Chem.Scaffolds.MurckoScaffold`), group the 5,789 ChEMBL compounds by Bemis–Murcko scaffold, assign scaffolds to 5 cross-validation folds and an 80/20 scaffold-split test set, perform hyperparameter tuning strictly within the training folds via `GridSearchCV`, and report the updated test and external-set metrics.

#### 2. Audit and Correct Table 3 and Explicitly Map Candidate Compound Identifiers
* **WHY:** In Table 3, the similarity entries under Pazopanib and Axitinib are identical to six decimal places for compounds 38, 23, and 20, indicating a copy-paste error during table assembly. Additionally, the reader cannot tell which numbered hits in Table 3 (e.g., 40, 16, 38, 23) correspond to `molecule1` (CID 17379777) and `molecule2` (CID 4682044).
* **WHAT:** Recompute the Morgan2 and MACCS Tanimoto and Dice similarities for Axitinib and Pazopanib, fix the typo in the Ki8751 row (`0.7660000` vs. `0.863636`), and explicitly label the compound numbers in Table 3 that correspond to `molecule1` and `molecule2`.
* **HOW:** Re-run the RDKit `DataStructs.TanimotoSimilarity` and `DataStructs.DiceSimilarity` script across all seven reference drugs and the 61 filtered hits, replace the duplicated Axitinib rows in Table 3, and add a column or footnote mapping internal hit IDs to PubChem CIDs and SMILES strings.

#### 3. Report Complete MD Simulation Protocols and Propagate MM-PBSA Uncertainty Across Replicates
* **WHY:** Reporting single MM-PBSA point estimates ($-89.1$, $-95.3$, $-87.4\text{ kJ/mol}$) without variance across the triplicate trajectories makes it impossible to assess whether the $1.7\text{–}7.9\text{ kJ/mol}$ differences are statistically distinguishable from thermal noise, and omitting total trajectory length prevents independent reproduction.
* **WHAT:** State the exact total production MD duration per replicate in the Methods section and report mean $\pm$ SD (and SEM) across the three independent trajectories for total MM-PBSA binding free energy and all energy components (van der Waals, electrostatic, polar solvation, SASA).
* **HOW:** Compute the block-averaged `g_mmpbsa` binding free energy over the last $25\text{ ns}$ separately for each of the three replicate trajectories of `molecule1`, `molecule2`, and regorafenib, and update the Abstract, Results text (line 250), and Supplementary Table S3 with $\text{mean} \pm \text{SD}$.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Corrupted equations in the Methods section and unshared screening outputs hinder reproducibility and reader confidence.
* **WHAT & HOW:**
  1. **Lines 58–62 (Evaluation metrics equations):** Fix the corrupted equations for MAE, RMSE, and $R^2$: add absolute value bars to $\text{MAE} = \frac{1}{N}\sum_{i=1}^N |y_i - \hat{y}_i|$, add the missing opening parentheses and square root to $\text{RMSE} = \sqrt{\frac{1}{N}\sum_{i=1}^N (y_i - \hat{y}_i)^2}$, and fix the inverted variable definitions on line 62 so that $\hat{y}$ is defined as the predicted value and $\bar{y}$ as the mean of the observed values (currently reversed: *"where, $\bar{y}$ and $\hat{y}$ represent the predicted value of y and the mean value, respectively"*).
  2. **Lines 93, 133, 185 (Figure captions):** Figures 3 and 5 are molecular property radar plots and RDKit similarity maps, not outputs of `scikit-learn v 0.23.1` as stated in their captions; cite RDKit/matplotlib accurately.
  3. **Data Availability:** Deposit the SMILES list of the 61 filtered hits, the trained RF classification/regression models, and the docked PDB coordinates of `molecule1` and `molecule2` in the Supplementary Materials or a public repository.
