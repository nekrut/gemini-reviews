# Forensic Peer Review: FEXP_ANON_143

**Overall Score:** **3.5 / 10.0** (Flawed / Overstated)
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.8/2.5 | Biology: 0.8/2.0 | Reproducibility: 1.0/2.0
* **Scientific Core Score:** **2.5 / 8.0**

---

## 1. Blinded Metadata Perception

* **Perceived Subfield:** Dental / Endodontic Bioinformatics & *In Silico* Phytochemical Screening (AutoDock Vina virtual screening of 329 NPACT plant compounds against human Interleukin-1$\beta$ [hIL-1$\beta$, PDB `5R8Q`], SwissADME/pkCSM profiling, 100 ns GROMACS molecular dynamics, and `g_mmpbsa` binding energy calculations)
* **Perceived Paper Type:** Purely *In Silico* Molecular Docking and Molecular Dynamics Screening Article
* **Estimated Calendar Epoch:** 2024 (cites 2023–2024 dental and computational literature; uses GROMACS 2020.4)
* **Perceived Capability Tier:** Entry-level computational/dental academic group running standard point-and-click web servers (SwissADME, pkCSM, DrugBank) and routine single-trajectory AutoDock Vina + GROMACS + `g_mmpbsa` pipelines without wet-lab validation or thermodynamic sanity checks.

---

## 2. Executive Summary & Editorial Verdict

This purely computational manuscript screens 329 phytochemicals from the Naturally Occurring Plant-based Anti-cancer Compound-Activity-Target (NPACT) database for ADMET/Lipinski compliance, docks the 38 passing compounds against human Interleukin-1$\beta$ (hIL-1$\beta$, PDB `5R8Q`) using AutoDock Vina, and performs a single 100 ns GROMACS molecular dynamics simulation and `g_mmpbsa` calculation on the top hit, **Quercetin**, nominating it as a direct hIL-1$\beta$ inhibitor for endodontic inflammation (apical periodontitis). Forensic inspection of the tabulated data (`Tables 1, 3, 4, and 5`) exposes multiple mathematical and factual contradictions: (1) in `Table 1`, the reported AutoDock Vina binding energy for Quercetin (**$-10.3\text{ kcal/mol}$**) is **mathematically incompatible** with both its reported $\text{p}K_i$ (**$6.99$**, which corresponds to $\Delta G = -9.53\text{ kcal/mol}$) and its reported Ligand Efficiency (**$0.4182\text{ kcal/mol/non-H atom}$**, which for Quercetin's 22 heavy atoms corresponds to $\Delta G = -9.20\text{ kcal/mol}$), whereas every other compound in `Table 1` obeys the exact formulas $\text{p}K_i = -\Delta G / 1.364$ and $\text{LE} = -\Delta G / N_{\text{heavy}}$; (2) in `Results` (line 98) and `Discussion` (line 165), the authors repeatedly claim that the average RMSF of the `hIL1β–Quercetin` complex (`0.09 nm`) is **higher** than that of apo `hIL1β` (`0.11 nm`), when $0.09 < 0.11$; (3) in `Results` (line 151), the authors claim that **polar solvation energy** (`+128.856 kJ/mol` in `Table 5`) contributed **favorably** to binding, and the component means in `Table 5` do not sum to the reported total $\Delta E_{\text{Binding}}$; and (4) Quercetin is a notorious pan-assay interference compound (PAINS) and promiscuous polyphenol with zero experimental evidence of direct hIL-1$\beta$ neutralizing activity in this study.

### Claim-by-Claim Audit

* **Claim 1:** Among 38 ADMET-filtered NPACT phytochemicals, Quercetin exhibits a superior AutoDock Vina binding affinity of $-10.3\text{ kcal/mol}$ ($\text{p}K_i = 6.99$, $\text{LE} = 0.4182$) surpassing the co-crystallized reference ligand `T9C_168477827` ($-9.5\text{ kcal/mol}$, $\text{p}K_i = 6.97$, $\text{LE} = 0.2714$). — `[Methodologically Flawed]`
  * *Evidence:* Every other compound in `Table 1` strictly satisfies $\Delta G = -RT\ln(10)\cdot\text{p}K_i = -1.3636\cdot\text{p}K_i$ and $\text{LE} = -\Delta G / N_{\text{heavy}}$. For Quercetin ($C_{15}H_{10}O_7$, $N_{\text{heavy}} = 22$), $\text{p}K_i = 6.99$ implies $\Delta G = -9.53\text{ kcal/mol}$, and $\text{LE} = 0.4182$ implies $\Delta G = -22 \times 0.4182 = -9.20\text{ kcal/mol}$ (whereas $\Delta G = -10.3\text{ kcal/mol}$ would require $\text{p}K_i = 7.55$ and $\text{LE} = 0.4682$). Furthermore, the reference ligand `T9C` in PDB `5R8Q` is a crystallography fragment (`MW < 300 Da`, weak millimolar fragment from an XChem screen), not a validated potent inhibitor.
* **Claim 2:** 100 ns molecular dynamics simulations show that Quercetin binding induces a *"slightly higher RMSF in the complex"* compared to apo hIL-1$\beta$, which *"is consistent with an antagonist action."* — `[Methodologically Flawed]`
  * *Evidence:* `Table 3` and `Results` (line 98) report `Average RMSF = 0.11 nm` for `hIL1β (apo)` and `0.09 nm` for `hIL1β–Quercetin complex`. Because $0.09\text{ nm} < 0.11\text{ nm}$, the complex has a **lower** (not higher) average RMSF than the apo protein, directly contradicting the narrative in `Results` (line 98) and `Discussion` (line 165).
* **Claim 3:** MM-PBSA analysis (`Table 5`) confirms a highly favorable binding free energy (`−199.426 ± 13.796 kJ/mol`), with *"all components of the binding energy namely van der Waals, electrostatic, polar solvation, and non-polar solvation energies contributing favorably."* — `[Methodologically Flawed]`
  * *Evidence:* In `Table 5`, `ΔE Polar solvation` is **`+128.856 ± 18.385 kJ/mol`**—a large **positive (unfavorable)** desolvation penalty, not a favorable negative contribution. In addition, the sum of the four component means in `Table 5` is $-255.215 + (-48.757) + 128.856 + (-17.664) = \mathbf{-192.780\text{ kJ/mol}}$, which differs by $6.646\text{ kJ/mol}$ from the reported `ΔE Binding = −199.426 kJ/mol`.
* **Claim 4:** Quercetin is a promising direct hIL-1$\beta$ antagonist for clinical endodontic irrigants and intracanal medicaments. — `[Overstated]`
  * *Evidence:* Purely *in silico* docking of Quercetin—one of the most ubiquitous, promiscuous dietary flavonoids and known PAINS aggregators in chemical biology—without a single biochemical binding assay (SPR/ITC/ELISA) or dental pulp cell assay cannot support therapeutic claims.

**Editorial Verdict:** **Reject** (Flawed / Overstated; **3.5 / 10.0**). The mathematical inconsistency in Quercetin's `Table 1` docking metrics, inverted RMSF comparison, misinterpretation of positive polar solvation energy, and complete absence of wet-lab validation preclude publication.

---

## 3. Forensic Defect Inventory

### Defect 1: Mathematical Incompatibility Between `Binding Energy (-10.3 kcal/mol)`, `pKi (6.99)`, and `Ligand Efficiency (0.4182)` for Quercetin in `Table 1`
* **Location:** `Table 1` (*Docking values of filtered compounds*, line 91) and `Results` (lines 79–83).
* **Technical Description:** In `Methods` (lines 48–49), the authors state that $\text{p}K_i$ and Ligand Efficiency ($\text{LE}$, in $\text{kcal/mol}$ per heavy atom) were computed directly from the AutoDock Vina binding affinity ($\Delta G$, in $\text{kcal/mol}$) using standard thermodynamic equations:
  $$\text{p}K_i = -\log_{10}\left(\exp\left(\frac{\Delta G}{RT}\right)\right) = \frac{-\Delta G}{2.303 RT} \approx \frac{-\Delta G}{1.3636}, \qquad \text{LE} = \frac{-\Delta G}{N_{\text{heavy}}}$$
  Checking every other row of `Table 1` confirms that these exact deterministic formulas were used:
  - **Chrysin** ($C_{15}H_{10}O_4$, $N_{\text{heavy}} = 19$): $\Delta G = -7.2 \implies \text{p}K_i = 7.2 / 1.3636 = \mathbf{5.28}$ (reported: `5.28`); $\text{LE} = 7.2 / 19 = \mathbf{0.3789}$ (reported: `0.3789`).
  - **Curcumin** ($C_{21}H_{20}O_6$, $N_{\text{heavy}} = 27$): $\Delta G = -7.2 \implies \text{p}K_i = \mathbf{5.28}$ (reported: `5.28`); $\text{LE} = 7.2 / 27 = \mathbf{0.2667}$ (reported: `0.2667`).
  - **2',4'-Dihydroxychalcone** ($C_{15}H_{12}O_3$, $N_{\text{heavy}} = 18$): $\Delta G = -8.4 \implies \text{p}K_i = 8.4 / 1.3636 = \mathbf{6.16}$ (reported: `6.16`); $\text{LE} = 8.4 / 18 = \mathbf{0.4667}$ (reported: `0.4667`).
  - **Control `T9C_168477827`** ($N_{\text{heavy}} = 35$): $\Delta G = -9.5 \implies \text{p}K_i = 9.5 / 1.3636 = \mathbf{6.97}$ (reported: `6.97`); $\text{LE} = 9.5 / 35 = \mathbf{0.2714}$ (reported: `0.2714`).

  Now examine the top row of `Table 1`, **Quercetin** ($C_{15}H_{10}O_7$, $N_{\text{heavy}} = 22$):
  - Reported $\Delta G = \mathbf{-10.3\text{ kcal/mol}}$, Reported $\text{p}K_i = \mathbf{6.99}$, Reported $\text{LE} = \mathbf{0.4182}$.
  - If $\Delta G = -10.3\text{ kcal/mol}$, then $\text{p}K_i$ **must** be $10.3 / 1.3636 = \mathbf{7.55}$ (not `6.99`), and $\text{LE}$ **must** be $10.3 / 22 = \mathbf{0.4682}$ (not `0.4182`)!
  - Conversely, working backward from Quercetin's reported $\text{LE} = 0.4182 \times 22\text{ atoms}$ yields $\Delta G = \mathbf{-9.20\text{ kcal/mol}}$ ($\text{0.41818} = 9.2 / 22$), and working backward from $\text{p}K_i = 6.99 \times 1.3636$ yields $\Delta G = \mathbf{-9.53\text{ kcal/mol}}$!
  This proves that Quercetin's true AutoDock Vina score was $\mathbf{-9.2\text{ kcal/mol}}$ (when $\text{LE} = 0.4182$ was computed, worse than the control `-9.5 kcal/mol`!) or $\mathbf{-9.53\text{ kcal/mol}}$ (when $\text{p}K_i = 6.99$ was computed), and that the `-10.3 kcal/mol` value in `Table 1` was altered without updating $\text{p}K_i$ or $\text{LE}$.

### Defect 2: Direct Numerical Contradiction in RMSF Comparison (`0.09 nm` Claimed to be "Higher" Than `0.11 nm`)
* **Location:** `Table 3` (line 103), `Results` (*Root mean square fluctuation*, line 98), and `Discussion` (line 165).
* **Technical Description:** `Table 3` and `Results` (line 98) state:
  > *"The average RMSF for apo hIL1β was **0.11 nm**, and that for the hIL1β–Quercetin complex was **0.09 nm** (Table 3). The **slightly higher RMSF in the complex** suggests that Quercetin binding may have induced localized flexibility..."*
  `Discussion` (line 165) repeats this error verbatim:
  > *"Although the **average RMSF value for the complex was slightly higher than that for apo hIL1β**, it remained within an acceptable range. **Slightly higher RMSF values are consistent with an antagonist action**, where ligand binding induces conformational flexibility..."*
  Because **$0.09\text{ nm}$ is lower than $0.11\text{ nm}$**, the complex had a *lower* average RMSF than apo hIL-1$\beta$, falsifying the entire mechanistic argument built around "higher RMSF."

### Defect 3: Thermodynamic Sign Error (`+128.856 kJ/mol` Polar Solvation Claimed as "Favorable") and Arithmetic Discrepancy in `Table 5`
* **Location:** `Results` (*MM-PBSA Calculation*, line 151) and `Table 5` (line 154).
* **Technical Description:**
  1. **Sign Error:** In `Results` (line 151), the authors state: *"The results indicated that **all components of the binding energy namely van der Waals, electrostatic, polar solvation, and non-polar solvation energies contributed favorably** to the formation of a stable complex (Table 5)."* In `Table 5`, `ΔE Polar solvation` is **`+128.856 ± 18.385 kJ/mol`**. A positive $\Delta E > 0$ is thermodynamically **unfavorable** (opposing binding due to the desolvation penalty of burying polar groups).
  2. **Component Sum Mismatch:** In `g_mmpbsa`, $\Delta E_{\text{Binding}} = \Delta E_{\text{vdW}} + \Delta E_{\text{Elec}} + \Delta E_{\text{Polar}} + \Delta E_{\text{Apolar}}$. Summing the four component means in `Table 5` gives:
     $$-255.215 + (-48.757) + 128.856 + (-17.664) = \mathbf{-192.780\text{ kJ/mol}}$$
     Yet `Table 5` reports `ΔE Binding = −199.426 ± 13.796 kJ/mol`, an unexplained discrepancy of **$6.646\text{ kJ/mol}$**.
  3. **Proportion vs. Percentage Error in `Table 4`:** `Table 4` (line 138) is titled `Percentage of protein secondary structure (SS %)` and every column header carries a `(% )` symbol (`Coil (%)`, `B-Sheet (%)`, `A-Helix (%)`), yet the table entries are decimal fractions (`0.18, 0.47, 0.01, 0.14, 0.14, 0.06`, summing to `1.00` instead of `100%`).

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.9** | 3.5 | Purely computational workflow compromised by a mathematical contradiction in `Table 1` (Quercetin's $\Delta G = -10.3\text{ kcal/mol}$ is incompatible with its $\text{LE} = 0.4182 = 9.2/22$ and $\text{p}K_i = 6.99 = 9.53/1.364$), an arithmetic mismatch in `Table 5` ($-192.780$ vs. $-199.426\text{ kJ/mol}$), and single-replicate MD. |
| **2. Claim Calibration & Evidence Alignment** | **0.8** | 2.5 | Claims that $0.09\text{ nm}$ is "slightly higher" than $0.11\text{ nm}$ (`Results` line 98, `Discussion` line 165) and that a $+128.856\text{ kJ/mol}$ polar solvation penalty contributes "favorably" to binding (`Results` line 151). |
| **3. Biological Validity & Mechanistic Depth** | **0.8** | 2.0 | Nominates Quercetin—a well-known promiscuous polyphenol and PAINS compound—as a specific direct hIL-1$\beta$ protein–protein interaction inhibitor for endodontic disease without any experimental validation, while benchmarking against a weak crystallographic fragment (`T9C` in PDB `5R8Q`). |
| **4. Reproducibility, Data Hygiene & Transparency** | **1.0** | 2.0 | Uses publicly available PDB `5R8Q` and standard open-source tools (AutoDock Vina, GROMACS), and provides supplementary ADMET tables, but `Table 1`, `Table 4`, and `Table 5` contain obvious numerical/formatting errors. |
| **Scientific Core Score** | **2.5** | **8.0** | *(Sum of Rigor + Claims + Biology: $0.9 + 0.8 + 0.8 = 2.5$)* |
| **Overall Score** | **3.5** | **10.0** | **Flawed / Overstated** ($2.5 + 1.0 = 3.5$) |
