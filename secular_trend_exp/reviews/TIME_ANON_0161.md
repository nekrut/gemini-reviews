</Agent System Instructions>
<Blinded Review: TIME_ANON_0161>
**Composite Score:** 8.0 / 10.0 (Rigor: 2.9/3.5 | Claims: 2.2/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This biochemical and molecular virology study characterizes the secondary structure of the 76-nucleotide $3'(+)$ non-coding region (`NCR`) of the arterivirus simian hemorrhagic fever virus (`SHFV`) and identifies two host cellular proteins (`p56` and `p42`) from MA104 rhesus monkey kidney cytoplasmic extracts that bind specifically to the $3'(+)\text{NCR}$ RNAs of `SHFV`, equine arteritis virus (`EAV`), and porcine reproductive and respiratory syndrome virus (`PRRSV`). Using single-strand-specific ribonuclease probing (`RNase A`, `RNase T1`, and `RNase T2`) coupled to primer extension, the authors confirm an Mfold-predicted $3'$ stem-loop (`3'SL`) structure. Through structure-guided mutagenesis, covalent RNA affinity chromatography, LC-MS/MS peptide sequencing, Western blotting, immunoprecipitation of UV-crosslinked RNA–protein complexes, and reconstituted gel-shift binding curves with purified proteins, they identify `p56` as polypyrimidine tract-binding protein (`PTB1/PTB2`, apparent $K_d \approx 7\text{ nM}$) and `p42` as fructose-1,6-bisphosphate aldolase A (apparent $K_d \approx 69\text{ nM}$), mapping the `PTB` binding determinants to a pyrimidine-rich terminal loop and adjacent $3'$ bulge of the `3'SL`.

### 2. Methodological & Statistical Audit
- **Rigorous Orthogonal Protein Identification & Specificity Controls:**
  - The biochemical workflow is textbook in its use of orthogonal controls:
    1. **Competition EMSA & Cross-Linking Specificity:** Formation of the `SHFV` $3'(+)\text{NCR}$ ribonucleoprotein complex is completely competed by a $30\times$ molar excess of unlabeled homologous `SHFV` $3'(+)\text{NCR}$ RNA (and cross-competed by $25\text{--}75\times$ `EAV` or `PRRSV` $3'(+)\text{NCR}$ RNAs), while remaining completely resistant to $150\text{--}500\times$ molar excess of non-specific competitors (`poly(I)–poly(C)`, yeast tRNA, and structured West Nile virus $3'(+)\text{SL}$ RNA) both in crude S100 extracts (Figure 1B,E) and with purified recombinant `His-PTB` and `aldolase A` (Figure 7A,D).
    2. **Covalent RNA Affinity Purification & Mock Column Control:** Enrichment on an adipic-acid hydrazide `SHFV` $3'(+)\text{NCR}$ RNA column (paired with an identical no-RNA mock column control) followed by LC-MS/MS sequencing yielded 8 tryptic peptides from the upper `p56` band, 7 peptides from the lower `p56` band ($100\%$ match to `PTB1/2`), and 8 peptides from `p42` ($100\%$ match to `aldolase A`).
    3. **Direct Confirmation via Cross-Linked IP:** To prove that the abundant mass-spectrometry hits were indeed the UV-crosslinked RNA-binding proteins rather than co-migrating contaminants, the authors immunoprecipitated RNase-digested, $^{32}\text{P}$-labeled UV-crosslinked complexes with anti-PTB and anti-aldolase antibodies, including anti-`hnRNP A1` as a negative specificity control that precipitated neither band (Figure 6C).
- **Quantitative Binding & Hill Equation Considerations (Section 3.8, Figure 7C,F):**
  - The authors estimate apparent dissociation constants ($K_d \approx 7\text{ nM}$ for `His-PTB`, slope $n = 1.24$; $K_d \approx 69\text{ nM}$ for `aldolase A`, slope $n = 3.25$) using the linearized Hill equation $\log(\%\text{bound}/\%\text{unbound}) = n\log[\text{Protein}] - \log K_d$, and appropriately note that `His-PTB` was only partially purified and formed higher-order aggregates (`*` in Figure 7B,E) that were summed into the bound fraction.
  - Strictly speaking, in the Hill equation $\log(\theta/(1-\theta)) = n\log[P] - n\log K_{0.5}$, the intercept is $-n\log K_{0.5}$ (where $K_{0.5}$ is the half-saturating protein concentration); inspecting the saturation curves in Figure 7C ($50\%$ bound at $\sim 6\text{--}7\text{ nM}$ `His-PTB`) and Figure 7F ($50\%$ bound at $\sim 69\text{ nM}$ `aldolase`), the reported $7\text{ nM}$ and $69\text{ nM}$ values clearly represent the empirical half-saturation concentrations $K_{0.5}$, which is the standard biochemical quantity of interest.
- **Minor Omission in Table 1:**
  - The Methods text (lines 35 and 105) refers to RT-PCR primers `P1` and `P2` and primer-extension oligonucleotide `P11` as being listed in Table 1, but Table 1 only lists oligonucleotides `O1` through `O16`.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **[Well Supported]** The 76-nt `SHFV` $3'(+)\text{NCR}$ folds into a major $3'$ stem-loop (`3'SL`) and minor downstream stem-loop in solution, and specifically binds host `PTB` (`p56`, via the pyrimidine-rich terminal loop `5'-UCCCU-3'` and upper internal bulge `5'-AACU-3'`) and `fructose-1,6-bisphosphate aldolase A` (`p42`, via the upper stem-loop region).
- **[Well Supported]** The $3'(+)\text{NCR}$ RNAs of two divergent arteriviruses (`EAV` and `PRRSV`) cross-compete for and cross-link to the same `p56` (`PTB`) and `p42` (`aldolase`) host proteins.
- **[Well Supported / Appropriately Caveated]** The authors exercise commendable scientific restraint in the Abstract and Discussion, explicitly noting that while `PTB` and `aldolase` bind specifically with nanomolar affinity and may compete for overlapping sites in the upper `3'SL`, their functional roles in arterivirus RNA replication remain to be established in live-virus or replicon systems.

### 4. Reproducibility & Data Completeness
- **Experimental Detail & Accessions:** Virus strain (`SHFV LVR 42-0/M6941`, `NC_003092`), reference accessions (`EAV NC_002532`, `LDV NC_002534`, `PRRSV NC_001961`), oligonucleotide sequences `O1`–`O16` (Table 1), buffer compositions, RNase units, and LC-MS/MS peptide sequences (Figure 5C) are documented in detail; only primers `P1`, `P2`, and `P11` were omitted from Table 1.
</Blinded Review: TIME_ANON_0161>
