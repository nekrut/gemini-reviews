<Blinded Review: TIME_ANON_0945>
**Composite Score:** 7.8 / 10.0 (Rigor: 2.8/3.5 | Claims: 2.0/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 7.8/10
VERDICT: PASS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary / SUMMARY
This comparative evolutionary genomics and molecular evolution study reconstructs the duplication, lineage-specific gene loss, and asymmetric sequence divergence of the androgen receptor (`AR`, `NR3C4`) across Actinopterygian fishes following the teleost-specific whole-genome duplication (3R WGD). Combining degenerate touchdown/nested RT-PCR cloning of 21 new `AR` cDNA fragments across diverse fish orders with in silico genome/EST mining, macrosynteny ("rose window") analysis across *Tetraodon nigroviridis*, *Oryzias latipes* (medaka), and *Danio rerio* (zebrafish), multi-method phylogenetic inference (`PhyML`, `MrBayes` v3, NJ, MP), branch-site/clade substitution pattern testing (`CoMap`/non-symmetric correspondence analysis with 500,000 permutations and `PAML` v4, $p = 1.69 \times 10^{-8}$), and 3D structural mapping onto the human AR ligand-binding domain (`1XNN.pdb`) and human Androgen Insensitivity Syndrome (AIS) mutation database, the authors establish a three-step evolutionary model:
1. Ancestral duplication of `AR` into `AR-A` and `AR-B` during the 3R WGD after the divergence of Acipenseriformes (*Acipenser baerii*) but before Osteoglossiformes (*Heterotis niloticus*).
2. Secondary loss of `AR-B` in Otophysi (including zebrafish, where `T1`–`Z14` synteny is scrambled and no pseudogene remains) and Salmoniformes (which instead carry two `AR-A` paralogs from the 4R salmonid autotetraploidization).
3. Episodic acceleration and amino acid divergence of `AR-B` (38 LBD and 22 DBD specific substitutions vs 14 LBD and 2 DBD in `AR-A`, $\chi^2 \ge 15.34$) specifically at the base of Percomorphs, while basal teleost `AR-B` (*Heterotis*, *Anguilla*) remains highly conserved.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### STRENGTHS
- **Definitive Syntenic Proof of 3R Duplication and Zebrafish Secondary Loss:** Rather than relying solely on PCR negative results, the authors combine exhaustive RT-PCR/genomic PCR and `Zv7` BLAST searches with whole-chromosome paralogon ("rose window") mapping between *Tetraodon* (`T7`/`T1`), medaka (`M14`/`M10`), and zebrafish (`Z5`/`Z14`), proving that `AR-A` and `AR-B` arose from the 3R WGD and that the `AR-B` region on zebrafish `Z14` underwent chromosomal scrambling and gene deletion.
- **Rigorous Statistical Testing of Asymmetric Divergence (`CoMap` + `PAML`):** To test whether `AR-A` and percomorph `AR-B` experienced distinct site-specific selective pressures independent of overall branch length, the authors apply non-symmetric correspondence analysis (`ade4`) on `CoMap` expected site/branch substitution matrices with a 500,000-replicate permutation test ($p = 0.0036$, keeping equal branch numbers by excluding eel) and corroborate the episodic shift on the stem percomorph `AR-B` branch using `PAML` v4 ($p = 1.69 \times 10^{-8}$).
- **Thoughtful Epistemic Restraint:** The authors explicitly state (line 125) that PAML cannot distinguish whether relaxed purifying selection or positive selection drove the stem percomorph `AR-B` acceleration, and emphasize that without biochemical ligand-binding comparisons across sturgeon `AR`, eel `AR-A`/`AR-B`, and medaka `AR-A`/`AR-B`, neofunctionalization remains a *putative* hypothesis.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Unspecified `PhyML` and `PAML` Substitution Models:** Line 84 and 89 state that *"Default parameters of PhyML were used"* without specifying the amino acid substitution matrix (e.g., JTT, WAG, LG) or among-site rate heterogeneity ($\Gamma + I$), and line 125 reports a PAML $p$-value of $1.688343 \times 10^{-8}$ without stating the specific codon model comparison (e.g., branch model `model=2` vs `model=0` or clade model C vs M2a_rel), $\omega$ ($d_N/d_S$) parameter estimates, or log-likelihoods ($2\Delta\ell$).
- **Non-Significant Overlap with Human AIS Categories (Table 2):** The comparison of fish `AR-B` substitutions with human CAIS vs PAIS/MAIS mutations in Table 2 (3 CAIS vs 6 PAIS+MAIS out of 38 LBD substitutions) is acknowledged as statistically non-significant (line 141) and is largely descriptive, as single-residue pathogenicity in human AR strongly depends on epistatic sequence context.
- **Taxonomic Spelling Typo:** In line 86, *Heterotis niloticus* is misspelled once as *"Heterodontis niloticus"* (though spelled correctly as *Heterotis niloticus* elsewhere in the text and Table 1).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** Teleost `AR-A` and `AR-B` originated from the 3R WGD at the base of Teleostei, followed by secondary loss of `AR-B` in Otophysi (zebrafish) and likely Salmoniformes. `[Well Supported]`
- **Claim 2:** `AR-B` remained conserved in basal teleosts (*Heterotis*, *Anguilla*) but underwent a marked episodic burst of sequence evolution and altered site-specific selective constraints at the base of Percomorphs. `[Well Supported]`
- **Claim 3:** The divergence of `AR-B` in Percomorphs represents a late neofunctionalization event potentially permissive for sex-determination plasticity and hermaphroditism in Percomorphs. `[Moderately Supported]` — Explicitly and commendably presented by the authors as a testable hypothesis requiring future in vitro transactivation/binding assays for DHT vs 11-ketotestosterone (11KT).

### 4. Reproducibility & Data Completeness
- **Accession Numbers & Primers:** Table 1 lists GenBank, Ensembl (`v48`), and SwissProt/TrEMBL accessions for all sequences (including new GenBank accessions `ABF50779`–`ABF50787`), and degenerate nested RT-PCR primer sequences are fully specified.
- **Software & Structural Data:** Software versions (`Muscle`, `PhyloWin`, `PhyML`, `MrBayes` v3, `CoMap`/`Bio++`, `ade4`, `PAML` v4, `PyMOL`) and the PDB structure (`1XNN.pdb`) are clearly documented.
</Blinded Review: TIME_ANON_0945>
