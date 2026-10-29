<Blinded Review: TIME_ANON_0698>
OVERALL_SCORE: 2.3/10
VERDICT: FAILED
ESTIMATED_DECADE: 2010s
**Composite Score:** 2.3 / 10.0 (Rigor: 0.6/3.5 | Claims: 0.6/2.5 | Biology: 0.6/2.0 | Reproducibility: 0.5/2.0)
**Bias Category:** Technical/Assay
**Verdict:** Reject (Fundamental Flaws)
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Translational/Preclinical/Biomarker

---

### SUMMARY
### 1. Executive Summary
This study attempts to identify peptide inhibitors of duck hepatitis B virus (DHBV) replication by panning an M13 C7C phage display peptide library against synthetic peptides spanning the YMDD catalytic motif of DHBV polymerase (DHBVP). Eight phage-derived heptapeptides ("mimic peptides") were synthesized and tested in DHBV-infected primary duck hepatocytes via either direct extracellular addition to culture media or intracellular plasmid transfection alongside an entecavir positive control and PBS/pEGFP-N1 negative controls over 10 days. Using SYBR-Green qPCR on supernatant, cytoplasmic, and nuclear DNA fractions, the authors claim that peptides 2 and 7 inhibit DHBV replication by ~90–98% in supernatant and cytoplasm, and that intracellular expression of peptide 7 reduces nuclear DHBV-DNA by 85.8%.

### STRENGTHS
- **Use of Primary Duck Hepatocytes and Entecavir Control:** Primary duck hepatocytes infected with DHBV-positive duck serum and treated with entecavir represent a biologically relevant classical model for hepadnaviral replication.

### WEAKNESSES & METHODOLOGICAL AUDIT
### 2. Methodological & Statistical Audit
- **Fundamental Plasmid Construction Contradiction (`pGEM` Prokaryotic Vector Cloning DHBVP Instead of Mimic Peptides):** In the section "Construction of mimic peptide-expressing recombinant plasmids" (line 51), the authors state: *"Purified DHBVP PCR products (8 µl) were obtained... These products were thoroughly mixed with 1.5 µl BamHI, 1.5 µl HindIII... Purified pGEM (4 µl; Promega) was digested similarly... and the DHBVP fragment was ligated into the pGEM vector using T4 DNA ligase."* First, `pGEM` is a bacterial cloning vector lacking a eukaryotic RNA polymerase II promoter (such as CMV or SV40) and cannot drive intracellular expression in transfected avian hepatocytes. Second, the protocol describes cloning a `DHBVP PCR product` (the viral polymerase target!) rather than synthetic DNA oligonucleotides encoding the phage-selected heptapeptides (mimic peptides 1–8). This renders the entire "intracellularly expressed mimic peptide" experiment biologically and technically incoherent.
- **Terminological Confusion ("Mimic Peptides") and Flawed ELISA Plate Panning Protocol:** Peptides selected by panning a phage library against a synthetic DHBVP YMDD peptide are *binding peptides* (ligands), not "mimic peptides" (mimotopes). Furthermore, in the panning protocol (line 22), wells were "coated with peptide solution [100 µg/ml in DMSO] and then treated with 150 µl synthesized peptide (1 mg/ml)" without carrier-protein conjugation (e.g., BSA/KLH or biotin-streptavidin capture), and no negative-selection counter-panning or binding affinity ($K_d$ / competitive ELISA) validation was performed to show that peptides 2 or 7 actually bind DHBVP protein.
- **Failure to Distinguish Nuclear cccDNA from Relaxed Circular DNA (rcDNA):** The Introduction frames nuclear covalently closed circular DNA (cccDNA) as the key target, and the Results claim intracellular peptide 7 reduces "nuclear DHBV-DNA" by 85.8%. However, the nuclear isolation protocol (line 42: simple 1,500 $\times g$ pelleting in TBS buffer followed by RIPA/proteinase digestion and phenol-chloroform extraction, without Hirt extraction, Plasmid-Safe ATP-dependent DNase, or T5 exonuclease treatment, and using generic SYBR-Green qPCR rather than nick-spanning cccDNA-specific primers) heavily co-purifies abundant cytoplasmic/perinuclear rcDNA and integrated/linear viral DNA with the nuclear pellet.
- **Unexplained Extracellular Uptake of Unconjugated C7C Peptides & Dosing Unit Confusion:** In line 37, the authors state "30 µl (100 µmol) mimic peptide solution was added to each well, and 3 µl (10 mmol) entecavir stock solution..." Adding $100\ \mu\text{mol}$ in $30\ \mu\text{l}$ would require a physically impossible $3.33\text{ M}$ stock solution (a confusion between molar concentration $\mu\text{M}$ and molar amount $\mu\text{mol}$, resulting in an actual final concentration of $1\ \mu\text{M}$ in 3 ml medium). Moreover, unmodified hydrophilic disulfide-cyclized C7C peptides lack cell-penetrating sequences to cross the hepatocyte plasma membrane and reach cytoplasmic DHBVP.
- **Underpowered Non-Parametric Statistics ($n = 3$ with Kruskal-Wallis Across 10 Groups):** With $n = 3$ replicates per group across 10 groups, pairwise rank comparisons lack statistical power to achieve $P < 0.05$ after multiplicity adjustment, and no post-hoc multiple-comparison test (e.g., Dunn's test) is specified.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1 (Phage-selected peptides 2 and 7 specifically bind DHBVP and inhibit DHBV replication via polymerase blockade): `[Methodologically Flawed]`** — No biophysical or biochemical assay demonstrates binding to full-length DHBVP or inhibition of polymerase priming/reverse transcription activity.
- **Claim 2 (Intracellular plasmid expression of mimic peptide 7 reduces nuclear DHBV DNA by 85.8%): `[Methodologically Flawed]`** — The Methods describe ligating a DHBVP PCR product into a prokaryotic `pGEM` vector lacking a eukaryotic promoter, and the nuclear DNA extraction and SYBR-Green qPCR do not isolate or specifically amplify cccDNA.

### 4. Reproducibility & Data Completeness
- **Missing Sequences, Primers, and Tables:** The manuscript text omits the actual sequences of mimic peptides 1–8 (`Table I` is referenced but absent from the file), the quantitative DNA copy numbers (`Tables II–III` are absent), and the DHBV qPCR primer sequences, amplicon coordinates, and standard curve efficiencies.
</Blinded Review: TIME_ANON_0698>
