# Blinded Review: SP_ANON_030
**Composite Score:** 8.6 / 10.0 (Rigor: 3.1/3.5 | Claims: 2.2/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Accept
**Study Modality:** Hybrid Computational + Wet-Lab Functional Validation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This structural, functional, and evolutionary study defines a key site of vulnerability at the membrane-distal apex (domain III, residues Lys60–Lys80) of the prefusion Nipah virus fusion glycoprotein (NiV-F). The authors determine a 3.2 Å X-ray crystal structure of prefusion-stabilized NiV-F in complex with a potent neutralizing rabbit Fab (Fab66; PDB: 6T3F), demonstrating that Fab66 binds a conserved loop at the trimer apex adjacent to the N-linked glycan at Asn67 (NiV-F2). Through targeted glycan deletion and reciprocal site-directed mutagenesis between Nipah virus (NiV) and Hendra virus (HeV) at positions 70 and 74 (Q70K + S74T), tested via cell-surface flow cytometry and VSV-$\Delta$G-RLuc pseudovirus neutralization assays against mAb66, HeV-specific mAb36, and polyclonal antiserum pAb835, they prove that these two surface residues govern type-specific neutralization while the Asn67 glycan partially shields the epitope without preventing antibody binding. Codon-based selection analyses ($dN/dS$ via CODEML and HyPhy FUBAR) across NiV-F, Measles virus F (MeV-F), and Parainfluenza virus 5 F (PIV5-F) confirm that the fusion glycoprotein evolves under strong purifying selection ($\omega \ll 1$) across all structural domains.

---

### 2. Methodological & Statistical Audit
* **Crystallographic and Biophysical Rigor:** The 3.2 Å crystal structure (Table S1: $R_{\text{work}} / R_{\text{free}} = 0.228 / 0.268$, 96.6% Ramachandran favored, 0% outliers) cleanly resolves the ternary prefusion NiV-F trimer bound to three Fab66 molecules, including electron density for the GlcNAc2Man2 core of the Asn67 (F2) glycan abutting CDRL1.
* **Reciprocal Gain-of-Function and Loss-of-Function Mutagenesis:** Rather than relying solely on alanine scanning (which can non-specifically disrupt local folding), the authors perform reciprocal residue swaps between NiV-F and HeV-F at the two variable positions within the footprint (Q70K and S74T). Introducing Q70K+S74T into NiV-F completely ablates mAb66 neutralization while conferring full gain-of-function susceptibility to HeV-specific mAb36 ($\text{IC}_{50} = 0.09\ \mu\text{g/mL}$, matching WT HeV-F at $0.14\ \mu\text{g/mL}$); conversely, introducing K70Q+T74S into HeV-F confers full susceptibility to NiV-specific mAb66 ($\text{IC}_{50} = 0.08\ \mu\text{g/mL}$). This bidirectional swap provides air-tight mechanistic proof of the structural epitope.
* **Comparative Evolutionary Selection Analysis:** Recognizing that the 28 publicly available NiV-F sequences have low divergence and limited statistical power for site-specific $dN/dS$ inference, the authors supplement NiV-F with larger alignments of related paramyxovirus fusion proteins (MeV-F and PIV5-F) and compare F against the attachment glycoprotein G/H/HN using both PAML (M1a/M2a, M7/M8) and HyPhy FUBAR. This confirms that paramyxovirus F proteins experience strong purifying selection ($\omega \approx 0.06\text{–}0.15$) even at surface-exposed apex residues.
* **Minor Statistical Presentation Issue in Table 1:** In Table 1, pseudovirus neutralization $\text{IC}_{50}$ values (e.g., $0.29\ \mu\text{g/mL}$ for WT NiV-F vs. $0.05\ \mu\text{g/mL}$ for NiV-F2 glycan knockout) are reported as single point estimates without 95% confidence intervals or standard deviations across the three independent replicates, and curves in Figure 3 are compared via two-way ANOVA across dilution points rather than formal nonlinear regression parameter tests on $\log\text{IC}_{50}$.

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim:** *The DIII apex of prefusion NiV-F (residues 60–80) is a dominant target of both monoclonal (mAb66, mAb36) and vaccine-elicited polyclonal (pAb835) neutralizing antibodies, with residues 70 and 74 determining NiV vs. HeV specificity.* **[Well Supported]** — Conclusively established by the 3.2 Å crystal structure, reciprocal NiV/HeV chimeras, and serum depletion/neutralization shifts with pAb835.
* **Claim:** *The Asn67 (F2) N-linked glycan kinetically or sterically modulates neutralization potency (~6-fold shift in $\text{IC}_{50}$) without altering steady-state cell-surface binding.* **[Well Supported]** — Supported by parallel flow-cytometry MFI titration curves (no shift) and pseudovirus neutralization curves (6-fold enhanced potency upon N67Q/T69A knockout).

---

### 4. Reproducibility & Data Completeness
* **Structural and Sequence Depositions:** Atomic coordinates and structure factors for the NiV-F–Fab66 complex and unliganded Fab66 are deposited in the Protein Data Bank under accession codes `6T3F` and `6T3G`. GenBank accession numbers for all analyzed paramyxovirus sequences are listed in the supplementary materials.
* **Experimental Detail:** Construct boundaries, expression vectors, purification protocols, crystallization conditions, and assay parameters are documented in full.
