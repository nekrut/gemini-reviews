</Agent System Instructions>
<Blinded Review: TIME_ANON_0077>
**Composite Score:** 9.7 / 10.0 (Rigor: 3.4/3.5 | Claims: 2.4/2.5 | Biology: 2.0/2.0 | Reproducibility: 1.9/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This landmark study identifies and characterizes the budding yeast `SKP1` gene, isolated as a high-copy dosage suppressor of the temperature-sensitive kinetochore mutant `ctf13-30` (encoding the 58 kDa subunit of the centromere CDEIII-binding CBF3 complex). Through an elegant combination of yeast genetics, biochemical gel-mobility shift and antibody supershift assays, random PCR mutagenesis with in vivo gap repair, quantitative chromosome transmission fidelity assays, flow cytometry, and cross-species cDNA cloning, the authors establish three major discoveries: (1) Skp1p (22.3 kDa) is an essential, previously unrecognized fourth intrinsic subunit of the CBF3 kinetochore complex present in equimolar stoichiometry with Ctf13p; (2) temperature-sensitive `skp1` alleles separate into two distinct functional classes that exhibit intragenic complementation—`skp1-4` (Leu146Ser), which causes >100-fold elevated chromosome missegregation and G2/M preanaphase arrest with short spindles, and `skp1-3` (Ile172Asn), which arrests at G1/S with 1C DNA and multiply elongated buds phenocopying `cdc4`/`cdc34`/`cdc53` without chromosome loss; and (3) `SKP1` is highly conserved across eukaryotes (*C. elegans*, *A. thaliana*, *H. sapiens*), with the human homolog being identical to p19 (`SKP1`), a subunit of the cyclin A–CDK2 complex.

### 2. Methodological & Statistical Audit
- **Biochemical Stoichiometry & Supershift Controls:** To test whether Skp1p is physically part of the CBF3–CDEIII complex, the authors engineered two independent N-terminal epitope tags (a 60-aa tandem coronavirus E1 tag and an influenza HA tag), first verifying that both fusion constructs rescue a `skp1-Δ1::TRP1` null strain. In native electrophoretic mobility shift assays (EMSA) with a 100 bp $^{32}\text{P}$-labeled CDEIII probe, the 60-aa E1 tag on Skp1p produced an intrinsic upward mobility shift identical in magnitude to the same 60-aa E1 tag on Ctf13p (Fig. 2A, lanes 3–6), establishing a 1:1 molar stoichiometry independent of antibody binding efficiency. Anti-HA antibodies produced a complete, quantitative supershift in two independent transformants matching HA-Ctf13p (Fig. 2B).
- **Single-Copy Chromosomal Integration & Interallelic Complementation:** Rather than relying on episomal plasmids with variable copy number, both `skp1-3` and `skp1-4` single-missense alleles were integrated at the `LEU2` locus (confirmed by OFAGE pulsed-field gel Southern blotting) in a `skp1-Δ1::TRP1` background, and homozygous (`skp1-3/skp1-3`, `skp1-4/skp1-4`) as well as heteroallelic (`skp1-3/skp1-4`) diploids were constructed. Half-sector colony color assays quantitatively demonstrated a >100-fold increase in chromosome loss (3.9% per division; 1:0) and nondisjunction (1.7% per division; 2:0) in `skp1-4/skp1-4`, whereas `skp1-3/skp1-3` had wild-type fidelity and `skp1-3/skp1-4` fully complemented both viability at $37^\circ\text{C}$ and chromosome segregation fidelity.
- **Reciprocal Dosage Suppression Specificity:** Overexpression of `CTF13` (even on a low-copy `CEN` vector) suppressed the chromosome missegregation and temperature sensitivity of `skp1-4` (but not `skp1-3`), whereas high-copy `2μ NDC10` had no effect (Fig. 3), demonstrating subunit-specific genetic interaction between Skp1p and Ctf13p.
- ** evolutionary Insertion Deletion Test:** Observing a yeast-specific 28-amino-acid insertion (residues 37–64) relative to multicellular homologs, the authors constructed an exact in-frame deletion (`skp1-Δ2`, Fig. 1E) and proved it rescues the `skp1-Δ1` null allele.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *"The 22.3 kDa Skp1 protein is an essential fourth subunit of CBF3 present at an equimolar ratio with Ctf13p."* — `[Well Supported]`
  - Unambiguously supported by 2+:2− tetrad lethality of `skp1-Δ1::TRP1` (20 tetrads), reciprocal suppression with `CTF13`, comigrating intrinsic EMSA shifts of E1-Skp1p and E1-Ctf13p, and quantitative HA-Skp1p supershifts (Fig. 2).
- **Claim 2:** *"Temperature-sensitive mutations in SKP1 define two distinct phenotypic classes... suggesting two independent functions for the Skp1 protein: a G2/M function required for kinetochore activity and chromosome segregation and a G1/S function required for cell cycle progression."* — `[Well Supported]`
  - Directly supported by flow cytometry (Fig. 4A), nuclear/spindle morphometry ($n=203$, Fig. 5), half-sector chromosome loss rates, allele-specific suppression by `CTF13`, and intragenic complementation in `skp1-3/skp1-4` diploids.
- **Claim 3:** *"Skp1p represents an intrinsic kinetochore protein conserved throughout eukaryotic evolution and may be directly involved in linking kinetochore function with the cell cycle-regulatory machinery."* — `[Well Supported]`
  - Supported by full-length sequencing of *C. elegans*, *A. thaliana*, and human EST clones (>60% pairwise identity, with both `skp1-3` Ile172 and `skp1-4` Leu146 residing at 100% invariant residues across 7 homologs, Fig. 6), while mechanistic models of how Skp1p bridges G1/S proteolysis and G2/M kinetochore assembly are thoughtfully and cautiously discussed.

### 4. Reproducibility & Data Completeness
- **Strain, Allele, and Construct Documentation:** Table 1 lists exact codon, nucleotide, and amino acid changes for all four ts alleles (`skp1-1` through `skp1-4`), and Table 2 provides complete genotypes for all 11 S288C-derived yeast strains (`YPH972R` through `YPH1208`).
- **Experimental Detail:** Library construction, gap-repair PCR mutagenesis conditions ($3\text{ mM }\text{MgCl}_2$, $60\ \mu\text{M}$ dNTPs), restriction sites, oligonucleotide sequences (`PH139`), and EMSA protocols are reported with exemplary completeness.
</Blinded Review: TIME_ANON_0077>
