# Review of FEXP_ANON_147

**Overall Score:** **2.5 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.9 / 8.0**  
* **Score Breakdown:** Rigor: 0.6/3.5 | Claims: 0.5/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.6/2.0

---

## 1. Blinded Metadata Perception

* **Anonymized Manuscript ID:** `FEXP_ANON_147`
* **Perceived Field & Subfield:** Food Chemistry, Natural Product Characterization & In Silico Cheminformatics (Extra Virgin Olive Oil Profiling, Antioxidant/Antimicrobial Assays, Network Pharmacology, Molecular Docking, and DFT).
* **Study Design Type:** Hybrid wet-lab analytical characterization (GC-FID fatty acids, HPLC phenolics, SPME-GC-MS volatiles, spectrophotometric DPPH/ABTS/TPC, disk-diffusion antimicrobial assay) and computational modeling (SwissTargetPrediction/ClusterProfiler, AutoDock 4.2/Vina against ACE and AT1R, SwissADME/ADMETlab 2.0, and B3LYP/6-311++G(d,p) DFT).

---

## 2. Executive Summary & Editorial Verdict

This study characterizes extra virgin olive oil (EVOO) extracted from a single harvest of the Turkish olive cultivar "Sarı Ulak" (Tarsus, Türkiye) using GC-FID (fatty acids), HPLC-PDA (phenolic compounds), SPME-GC-MS (40 volatile compounds), sensory evaluation, and disk-diffusion antimicrobial testing. It then subjects four phenolic constituents (hydroxytyrosol, oleuropein, pinoresinol, and apigenin) to network pharmacology (`SwissTargetPrediction` and `ClusterProfiler`), molecular docking against angiotensin-converting enzyme (`ACE`, PDB `1O8A`) and angiotensin II type 1 receptor (`AT1R`, PDB `4YAY`), ADMET profiling, and density functional theory (DFT) calculations.

**Editorial Verdict: Reject (Fundamentally Invalid, 2.5 / 10.0).** While the basic wet-lab quality measurements (FFA, PV, $K_{232}$, $K_{270}$) are routine, the manuscript is riddled with severe analytical, mathematical, and quantum-chemical errors, as well as out-of-context boilerplate text. First, in Table 4 (Fatty Acid Profile), palmitoleic acid (`C16:1`, misspelled "Palmiteloic acid") is entered *twice* (`0.73%` and `0.731%`) and summed twice into the total MUFA percentage ($71.85 + 0.73 + 0.23 + 0.27 + 0.731 = 73.81\%$). Second, in the DFT analysis (Table 16), hydroxytyrosol is reported with $E_{\text{LUMO}} = -7.91\text{ eV}$ lower than $E_{\text{HOMO}} = -6.62\text{ eV}$, yielding a physically impossible *negative* HOMO–LUMO energy gap ($\Delta E = -1.28\text{ eV}$), *negative* chemical hardness ($\eta = -0.64\text{ eV}$), and *negative* softness ($s = -1.55\text{ eV}^{-1}$). Third, the DFT Methods section (line 141) contains bizarre electrochemistry/corrosion boilerplate claiming that *"cholesterol is a good option for a chelating agent"* that alters *"the dielectric properties of the double electric layer,"* and line 129 claims that AutoDock Vina 1.1.2 was used to investigate *"optical spectra in EVOO."*

### Specific Conclusions and Assessment of Support

* **Sarı Ulak EVOO exhibits a standard fatty acid profile with $73.81 \pm 3.93\%$ MUFAs and a volatile profile dominated by estragole ($38.94\%$), 3-methoxycinnamaldehyde ($12.98\%$), and 7-hydroxyheptene-1 ($10.48\%$): [Methodologically Flawed].**  
  In Table 4, `Palmiteloic acid (C16:1)` is listed twice (`0.73 ± 0.10` and `0.731 ± 0.09`)—and three times in the text (line 156)—and both entries were added together to obtain `MUFAs = 73.81%`. In Table 7, volatile identification relied solely on NIST11/Wiley9 mass spectral library matching without authentic standards or Kovats retention index verification against literature values, leading to physically implausible assignments such as headspace SPME detection of `hexatriacontane` ($\text{C}_{36}\text{H}_{74}$ heavy paraffin wax, $\text{BP} = 497\text{ }^\circ\text{C}$) at $\text{RI} = 2189$. Furthermore, the authors fail to note that estragole ($38.94\%$) and methyleugenol ($3.61\%$) are classified as genotoxic hepatocarcinogens.

* **Sarı Ulak EVOO exerts a $69.57\%$ antimicrobial inhibition effect against *Pseudomonas aeruginosa* relative to sulbactam/ampicillin: [Methodologically Flawed].**  
  The $69.57\%$ figure is calculated by dividing the raw inhibition zone diameter of $15\text{ }\mu\text{L}$ neat oil ($8.0 \pm 0.0\text{ mm}$) by that of $20\text{ }\mu\text{g}$ sulbactam/ampicillin ($11.5 \pm 0.7\text{ mm}$) without subtracting the $6.0\text{ mm}$ sterile paper disk diameter (which reduces the net inhibition zone to $2.0\text{ mm}$ vs. $5.5\text{ mm}$, or $36.4\%$). Moreover, applying neat hydrophobic triglyceride oil to an aqueous agar surface in a disk-diffusion assay violates CLSI standards because non-polar oil cannot diffuse uniformly through hydrogel media.

* **Molecular docking demonstrates that apigenin ($-8.5\text{ kcal/mol}$) binds ACE (`1O8A`) more strongly than oleuropein, pinoresinol, and lisinopril: [Overstated].**  
  The main text (line 272) contradicts Table 10: in Table 10, *oleuropein* has the strongest docking score against `1O8A` ($-8.7\text{ kcal/mol}$), exceeding apigenin ($-8.5\text{ kcal/mol}$). Furthermore, Methods line 118 states that *"seven proteins that cause cardiovascular diseases were selected (Table 2),"* whereas Table 2 and the results include only two proteins (`1O8A` and `4YAY`).

* **DFT calculations (B3LYP/6-311++G(d,p)) validate the electronic stability, reactivity, and esterification energetics of EVOO constituents and cholesterol: [Methodologically Flawed].**  
  Table 16 reports a negative HOMO–LUMO energy gap ($\Delta E = -1.28\text{ eV}$) and negative hardness ($\eta = -0.64\text{ eV}$) for hydroxytyrosol ($E_{\text{HOMO}} = -6.62\text{ eV}$, $E_{\text{LUMO}} = -7.91\text{ eV}$), violating the Aufbau principle. In addition, the energetic comparison of cholesterol ($-1013.7\text{ au}$) + oleic acid ($-856.9\text{ au}$) $\to$ cholesteryl oleate ($-1794.2\text{ au}$) omits the eliminated water molecule ($\text{H}_2\text{O} \approx -76.4\text{ au}$) and misinterprets an endothermic difference of $+76.4\text{ Hartree}$ as a stabilizing reduction in total energy.

---

## 3. Forensic Defect Inventory

### 1. Violation of the Aufbau Principle in DFT Table 16 ($E_{\text{LUMO}} < E_{\text{HOMO}}$ and Negative Hardness for Hydroxytyrosol)
* **Location:** Section *Density functional theory analysis* (first chunk, lines 139–141) and Table 16 (second chunk, lines 106–120).
* **Defect:**
  1. For hydroxytyrosol in Table 16 (line 115), the authors report $E_{\text{HOMO}} = -6.62\text{ eV}$ and $E_{\text{LUMO}} = -7.91\text{ eV}$, resulting in $\Delta E = E_{\text{LUMO}} - E_{\text{HOMO}} = -1.28\text{ eV}$, hardness $\eta = -0.64\text{ eV}$, and softness $s = -1.55\text{ eV}^{-1}$. For any ground-state closed-shell molecule, $E_{\text{LUMO}}$ must be strictly greater than $E_{\text{HOMO}}$ ($\Delta E > 0, \eta > 0$).
  2. In line 141 (first chunk), the text misassigns the three descriptors for cholesterol relative to Table 16: the text states *"hardness electronegativity, and softness were 2.200 eV, $0.628\text{ eV}^{-1}$, and 1.594 eV, respectively,"* whereas Table 16 lists $\chi = 2.20\text{ eV}$, $\eta = 1.59\text{ eV}$, and $s = 0.62\text{ eV}^{-1}$.
  3. In line 120 (second chunk), the authors compare $E(\text{Cholesterol}) = -1013.7\text{ au}$ and $E(\text{Oleic acid}) = -856.9\text{ au}$ (sum $= -1870.6\text{ au}$) with $E(\text{Cholesterol\_Oleic acid}) = -1794.2\text{ au}$, failing to include $E(\text{H}_2\text{O}) \approx -76.4\text{ au}$ on the product side of the esterification reaction and falsely claiming that changing from $-1013.7$ and $-856.9\text{ au}$ to $-1794.2\text{ au}$ is a stabilizing *"diminishing in the total energy."*

### 2. Out-of-Context Corrosion/Electrochemistry Boilerplate and Software Capabilities Fabrication
* **Location:** Section *Molecular modeling* (line 129) and Section *Density functional theory analysis* (line 141).
* **Defect:**
  1. Line 141 states: *"It's been proven that cholesterol has potent adsorption properties. Because of this, the cholesterol molecule is a good option for a chelating agent... The strength of the dipole moment (1.9001 D), which can change the dielectric properties of the double electric layer, increases the probability of cholesterol sticking."* References to metal adsorption, chelating agents, and the electrochemical "double electric layer" are verbatim artifacts from metal-corrosion inhibition papers and have no scientific relevance to olive oil or atherosclerosis.
  2. Line 129 states: *"Using the Autodock Vina 1.1.2 and Discovery Studio 2020 programs, the optical spectra in EVOO and ligand–protein interactions were investigated"*. AutoDock Vina and Discovery Studio are classical force-field docking/modeling tools that cannot compute optical spectra.

### 3. Duplicate Fatty Acid Entry (`Palmiteloic acid`) Double-Counted in Total MUFAs (Table 4)
* **Location:** Results text (first chunk, line 156) and Table 4 (lines 159–177).
* **Defect:** In Table 4, `Palmiteloic acid (C16:1)` appears in row 6 (`0.73 ± 0.10`) and again in row 13 (`0.731 ± 0.09`). In line 156, it is written three times in a single sentence. Summing the individual MUFAs in Table 4 (`Oleic 71.85 + Palmitoleic 0.73 + Cis-10-heptadecenoic 0.23 + 11-eicosenoic 0.27 + duplicate Palmitoleic 0.731`) yields `73.811%`, which matches the reported `MUFAs = 73.81 ± 3.93%`—proving that `C16:1` was double-counted in the MUFA total. Additionally, `Arachidic acid (C20:0)` is reported as `0.45 ± 0.8%` ($\text{SD} > \text{mean}$) and `Tricosanoic acid (C23:0)` is reported at an implausible `1.18 ± 0.1%`.

### 4. Internal Contradictions in Target Protein Count, Docking Rankings, and Interaction Tables
* **Location:** Section *Protein system* (line 118), Table 2 (lines 121–125), line 272, Table 10, and Table 11.
* **Defect:**
  1. Line 118 states: *"A total of seven proteins that cause cardiovascular diseases were selected by literature review (Table 2)."* Table 2 lists only **two** proteins (`1O8A` and `4YAY`).
  2. Line 272 states that for `1O8A`, *"apigenin (−8.5 kcal/mol) had a better binding score than pinoresinol and oleuropein lisinopril,"* whereas Table 10 reports `Oleuropein = −8.7 kcal/mol` and `Apigenin = −8.5 kcal/mol`.
  3. In Table 11 (second chunk, lines 25–26), all hydrogen-bond and hydrophobic interaction cells for Apigenin in `4YAY` (`−8.2 kcal/mol`) and H-bond cells for Losartan (`−8.5 kcal/mol`) are empty.
  4. In Methods line 129, docking is described using AutoDock 4.2.6 (Lamarckian genetic algorithm, $80 \times 80 \times 80$ grid points with $0.375\text{ \AA}$ spacing) AND AutoDock Vina 1.1.2 without specifying which program generated Table 10 or what grid center coordinates were used for `1O8A` and `4YAY`.

### 5. Unit Omissions, Unverified GC-MS Library Assignments, and IOC Sensory Protocol Deviations
* **Location:** Methods lines 54, 59, 79; Tables 5, 6, 7, 8, and 9.
* **Defect:**
  1. **Unit mismatch and missing $\text{IC}_{50}$ units:** Methods lines 54 and 59 define TPC, DPPH (TAC), and ABTS in $\text{mg GAE/100 g}$ and $\text{mg TE/100 g}$, respectively. However, Table 5 reports DPPH (`413.5 ± 217`) and ABTS (`211.8 ± 16.2`) as `IC50` with **no units specified** (and a $>52\%$ relative SD for DPPH), while Table 6 reports TPC in $\text{mg GAE}\cdot\text{kg}^{-1}$.
  2. **Implausible SPME-GC-MS assignment:** Table 7 reports `Hexatriacontane` ($\text{C}_{36}\text{H}_{74}$, MW = 507 Da) at $\text{RI} = 2189$ on a DB-HeavyWax column via headspace SPME. $\text{C}_{36}\text{H}_{74}$ is a non-volatile solid wax whose retention index is $3600$, not $2189$.
  3. **IOC sensory statistics mismatch:** Methods line 79 states sensory scores are expressed as *medians* per IOC standards, but Table 8 reports `Mean ± Std`.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.6** | **3.5** | Double-counting of palmitoleic acid in MUFA sum; negative HOMO–LUMO gap ($\Delta E = -1.28\text{ eV}$) and negative hardness in DFT Table 16; omission of $\text{H}_2\text{O}$ in esterification energy balance; unsubtracted disk diameter in antimicrobial percentage calculation; missing $\text{IC}_{50}$ units. |
| **2. Claim-to-Evidence Alignment** | **0.5** | **2.5** | Claims 7 target proteins in Methods but models 2; claims apigenin outscores oleuropein in `1O8A` when Table 10 shows the opposite; includes irrelevant corrosion-inhibition boilerplate about cholesterol as a "chelating agent" in the double electric layer. |
| **3. Data Integrity & Biological Plausibility** | **0.8** | **2.0** | Physically impossible DFT orbital energies for hydroxytyrosol; unverified NIST library hit for a $\text{C}_{36}$ wax (`hexatriacontane`) in headspace SPME at $\text{RI} = 2189$; unacknowledged presence of genotoxic hepatocarcinogens (`estragole` at $38.94\%$ and `methyleugenol` at $3.61\%$). |
| **4. Reproducibility & Data Integrity** | **0.6** | **2.0** | Duplicate rows in Table 4; swapped descriptors between text (line 141) and Table 16; missing docking grid centers; missing cells in Table 11; data available only upon request. |
| **Scientific Core Score** | **1.9** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **2.5** | **10.0** | **Fundamentally Invalid Tier (1.0 – 2.9).** |
