# Review of OOD_ANON_24

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **2.2 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.6/3.5 | Claims: 0.4/2.5 | Biology: 0.4/2.0 | Reproducibility: 0.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents a purely computational virtual screening pipeline aimed at discovering selective natural-product inhibitors of the PWWP1 domain of nuclear receptor-binding SET domain protein 2 (NSD2) from the SuperNatural 3.0 database (449,008 compounds). Using Schrödinger PHASE e-pharmacophore screening (filtering to 49,248 compounds), Glide HTVS and XP docking, QikProp ADME profiling, and 200 ns Desmond molecular dynamics (MD) simulations, the authors identify three top natural compounds (`SN0450102`, `SN0410255`, and `SN0142336`) with XP docking scores of $-12.041$, $-10.620$, and $-9.944\text{ kcal/mol}$ compared to $-9.355\text{ kcal/mol}$ for the co-crystallized reference ligand, concluding that these hits are stable, drug-like, selective NSD2 inhibitors for cancer therapy.

This study is fundamentally invalidated by a fatal target-identification error at the very first step of the pipeline: **PDB ID `6G2O` is the crystal structure of the PWWP1 domain of NSD3 (WHSC1L1) bound to the NSD3-selective chemical probe BI-9321, not NSD2.** Every active-site residue analyzed throughout the manuscript (`TYR-281`, `TRP-284`, `PHE-312`, `SER-314`, `GLN-316`, `GLU-318`, `ARG-319`, `ARG-363`, `GLU-364`, `SER-367`/`GLN-367`) belongs to the sequence and numbering of human NSD3-PWWP1 (residues 247–398), whereas human NSD2-PWWP1 spans residues 208–268 (with aromatic cage residues Trp236, Tyr233, Phe266, and Glu272). Even setting aside that the authors docked and simulated against the wrong protein while claiming NSD2 selectivity, the computational results directly contradict the manuscript's stability and pharmacokinetic claims: (1) protein and ligand RMSDs average $4.81\text{ \AA}$ and $4.54–5.60\text{ \AA}$ (exceeding the authors' own $1–3\text{ \AA}$ stability criterion and indicating major pose drift); (2) key docked hydrogen bonds vanish during MD (e.g., `SN0410255` contacts `SER-314` for only 4% of the trajectory); (3) the top two hits (`SN0450102` and `SN0410255`) are catechol polyphenols (3,4-dihydroxyphenyl / 2,3,6-trihydroxynaphthalene motifs) that are prototypical Pan-Assay Interference Compounds (PAINS); and (4) Table 2 shows that `SN0450102` and `SN0410255` violate the QikProp `QPlogHERG` cardiotoxicity threshold ($<-5.0$) and `SN0450102` has poor Caco-2 permeability ($16.17 < 25$), directly contradicting the text. The entire computational screen must be re-executed on an authentic NSD2-PWWP1 structure (e.g., PDB ID `7VLN` or `6UE6`) with PAINS filtering and cross-isoform counter-docking against NSD1 and NSD3.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Structure-based pharmacophore screening and docking against PDB ID `6G2O` identify selective inhibitors of the NSD2-PWWP1 domain: [Methodologically Flawed].**  
  PDB ID `6G2O` is the X-ray crystal structure of the human **NSD3** (WHSC1L1) PWWP1 domain co-crystallized with the NSD3-PWWP1 antagonist BI-9321 (as the authors themselves inadvertently note on line 121: *"The co-crystallized inhibitor was identified as the first potent and selective NSD3-PWWP1 antagonist (IC50 = 0.2 μM), which can disrupt the interactions between NSD3-PWWP1 and H3K36me2... [56]"*). All binding pocket residues reported in the text and figures (`TYR-281`, `TRP-284`, `PHE-312`, `SER-314`, `GLU-318`, `GLU-364`, `GLN-367`) correspond to NSD3 numbering. Furthermore, no counter-screening or comparative docking against NSD1, NSD2, and NSD3 was performed, making claims of "selective inhibitors for NSD2" entirely unsupported.

* **The top three hits (`SN0450102`, `SN0410255`, and `SN0142336`) are viable, non-cardiotoxic, membrane-permeable drug candidates: [Methodologically Flawed].**  
  First, chemically, `SN0450102` (8-(3,4-dihydroxybenzoyl)naphthalene-2,3,6-triol, containing both a catechol and a pyrogallol-like polyhydroxynaphthalene core) and `SN0410255` (2,5-bis(3,4-dihydroxyphenyl)furan-3-carbaldehyde, containing two catechol rings and an electrophilic aldehyde) are textbook PAINS scaffolds known for redox cycling, metal chelation, and non-specific protein reactivity. Second, the text (line 147) claims that "all the hit compounds under investigation exhibited favorable characteristics in terms of good cellular permeability" and "none of the compounds showed signs of cardiotoxicity," which is directly contradicted by Table 2: `SN0450102` has `QPPCaco-2 = 16.169` (below the `<25 poor` cutoff in Table 2), and both `SN0450102` (`QPlogHERG = -5.159`) and `SN0410255` (`QPlogHERG = -5.269`) fall below the $-5.0$ cardiotoxicity concern threshold.

* **200 ns MD simulations confirm high structural stability and persistent key active-site interactions for all three hit complexes: [Overstated].**  
  The text (line 169) states that "ensuring stability within a simulated system generally involves RMSD fluctuations within a span of 1 to 3 Å," yet immediately reports an average protein RMSD of **$4.81\text{ \AA}$** (unusually high for a small ~140-residue PWWP1 domain) and ligand RMSDs of **$4.54\text{ \AA}$, $5.06\text{ \AA}$, and $5.60\text{ \AA}$**. Moreover, the docked poses do not persist during MD: in docking (line 138), `SN0410255` forms direct hydrogen bonds with `SER-314` and `GLN-367`, whereas during the 200 ns MD trajectory (line 180), its direct H-bond with `SER-314` is present for only **4%** of the simulation time and `GLN-367` for **19%**. Similarly, `SN0450102` loses its direct H-bond with `SER-367`/`GLN-367` (retaining only a 10% water-mediated bridge).

* **MM-GBSA or free-energy validation of superior binding affinity over the co-crystallized reference ligand: [Fragile].**  
  The ranking of the top 10 compounds relies solely on rigid-receptor Glide XP docking scores (Table 1), which are well known to over-score polyhydroxylated polyphenolic compounds (`SN0450102` has 5 OH groups; `SN0410255` has 4 OH groups) due to additive hydrogen-bond terms without adequately penalizing desolvation of five polar hydroxyls (note in line 184 that the PSA of `SN0450102` is $280.0\text{ \AA}^2$ vs. $92.3\text{ \AA}^2$ for the reference ligand!). No post-MD MM-GBSA binding free energy calculations ($\Delta G_{\text{bind}}$) were computed across the trajectories to account for polar desolvation penalties.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Re-Run the Virtual Screening Pipeline Using an Authentic NSD2-PWWP1 Crystal Structure
* **WHY:** PDB ID `6G2O` is human NSD3-PWWP1, not NSD2-PWWP1. Screening against `6G2O` cannot identify NSD2 inhibitors unless explicitly framed as NSD3-PWWP1 inhibitor discovery or repeated on the actual NSD2-PWWP1 structure.
* **WHAT:** Download the solved crystal structure of human NSD2-PWWP1 bound to a selective chemical probe (e.g., PDB ID `7VLN`, NSD2-PWWP1 in complex with UNC6934, or `6UE6`), and repeat the e-pharmacophore generation, HTVS/XP docking, and MD simulations on NSD2-PWWP1.
* **HOW:** Prepare PDB ID `7VLN` in Schrödinger Protein Preparation Wizard, define the receptor grid around the co-crystallized NSD2-PWWP1 ligand (aromatic cage residues Trp236, Tyr233, Phe266), and dock the filtered compound library against both NSD2-PWWP1 (`7VLN`) and NSD3-PWWP1 (`6G2O`) in parallel to quantitatively evaluate isoform selectivity ($\Delta G_{\text{NSD2}} - \Delta G_{\text{NSD3}}$).

#### 2. Apply PAINS and Reactive Functional Group Filters Prior to Docking
* **WHY:** `SN0450102` and `SN0410255` contain catechol (1,2-dihydroxybenzene) and aldehyde moieties that act as pan-assay interference compounds (PAINS) and yield false-positive docking scores due to excessive hydrogen-bond donor density.
* **WHAT:** Filter the SuperNatural 3.0 screening hits through RDKit or Schrödinger Canvas PAINS and Brenk structural alert filters before selecting top hits for XP docking and MD simulation.
* **HOW:** Run Schrödinger's `LigFilter` with standard PAINS SMARTS patterns (excluding catechols, quinones, Michael acceptors, and unhindered aldehydes) so that only non-promiscuous, tractable scaffolds advance to MD evaluation.

#### 3. Compute Trajectory-Averaged MM-GBSA Free Energies and Re-Assess MD Pose Stability
* **WHY:** Glide XP docking ignores receptor flexibility and underestimates the high polar desolvation penalty of polyhydroxylated ligands ($\text{PSA} = 262–280\text{ \AA}^2$), while ligand RMSDs of $4.5–5.6\text{ \AA}$ indicate that the ligands drifted substantially from their initial docked poses.
* **WHAT:** Run Prime MM-GBSA (`thermal_mmgbsa.py`) across the equilibrated portion (80–200 ns) of the Desmond MD trajectories for both the candidate hits and the positive control, and report both ligand RMSD aligned on the protein backbone (`Lig fit Prot`, which measures translational/rotational drift in the pocket) and internal ligand RMSD (`Lig fit Lig`).
* **HOW:** Extract 100 evenly spaced frames from 80 to 200 ns for each complex, compute $\Delta G_{\text{bind}}$ and its polar solvation component ($\Delta G_{\text{solv,GB}}$), and discard any candidate whose `Lig fit Prot` RMSD exceeds $3.0\text{ \AA}$ or whose key pocket interactions persist for $<30\%$ of the trajectory.

#### 4. Correct Table 2 Errors, Residue Naming Inconsistencies, and Text-Table Contradictions
* **WHY:** Multiple errors in Table 2 and the text misrepresent the QikProp outputs and residue identities:
  1. In Table 2 (line 159), the acceptable range for Molecular Weight (`Mwt`) is printed as `>500` instead of `≤ 500` (or `130–500`), and the `QPPCaco-2` acceptable range is printed as `>25 poor <500 great` instead of `<25 poor, >500 great`.
  2. In Table 2, `SN0450102` has `QPPCaco-2 = 16.169` (poor permeability, $<25$) and a polar surface area of $280.0\text{ \AA}^2$ (line 184, far above the $140\text{ \AA}^2$ oral bioavailability limit), and both `SN0450102` ($-5.159$) and `SN0410255` ($-5.269$) violate the `QPlogHERG` threshold of $> -5.0$.
  3. Residue 367 is referred to as `SER-367` on line 136 and as `GLN-367` on lines 138, 140, and 180.
* **WHAT & HOW:** Correct the inequality signs in Row 4 of Table 2, fix the residue identity of position 367 throughout the text, and revise the Pharmacokinetic Profiling section (line 147) to accurately report that `SN0450102` exhibits poor predicted Caco-2 permeability and that `SN0450102` and `SN0410255` flag potential hERG liability.
