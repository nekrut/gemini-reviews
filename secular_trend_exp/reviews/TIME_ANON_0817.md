<Blinded Review: TIME_ANON_0817>
**Composite Score:** 7.2 / 10.0 (Rigor: 2.5/3.5 | Claims: 2.0/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.3/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 7.2/10
VERDICT: PASS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary / SUMMARY
This forensic virology and bioinformatics study demonstrates that two sequences deposited in GenBank as angiotensin II-upregulated human kidney mesangial cell genes—`Angrem52` (`AY040225` / `AAK76747`) and `Angrem104` (`AF367870`)—are actually viral transcripts from a previously uncharacterized paramyxovirus ("orphan paramyxovirus", OPmV, concurrently described as J-virus/Beilong-like rodent paramyxovirus by Schomacker et al.). Specifically, `Angrem52` (3,170 nt) is a bicistronic read-through cDNA encoding a full-length paramyxovirus Matrix (M) protein (nt 16–1038; 337 aa; 53% identity / 73% similarity to Nipah virus M), a canonical paramyxovirus gene-end/intergenic/gene-start junction, and a Fusion (F) protein ORF (beginning at nt 1393; requiring 4 single-nucleotide indels to restore a 546-aa full-length F protein with 32% identity / 53% similarity to Nipah virus F, complete with signal peptide, cleavage site, fusion peptide, and two heptad repeats). `Angrem104` (1,690 nt) encodes a paramyxovirus Phosphoprotein (P) gene (requiring 1 single-T insertion between nt 1130–1131 to restore a 496-aa P ORF, plus an overlapping 163-aa C ORF and a conserved `AAAAAAGGG` RNA-editing motif capable of generating a cysteine-rich V protein and W protein). Follow-up wet-lab experiments (human 12-tissue Northern blot and RT-PCR/immunoblotting across 4 lots of primary human mesangial cells ± angiotensin II) confirmed these are not human genomic sequences.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### STRENGTHS
- **Incisive forensic sequence analysis:** The identification of canonical paramyxovirus non-coding cis-acting transcriptional signals (gene-end, trinucleotide intergenic region, gene-start between M and F in `Angrem52`), the P-gene RNA editing site (`3'-UUUUUUCCC-5'` genomic sense) producing a conserved 7-cysteine zinc-finger V-protein C-terminus, and the overlapping C ORF leaves zero doubt that `Angrem52` and `Angrem104` are paramyxoviral rather than human genes.
- **Experimental falsification of endogenous human origin:** Rather than stopping at BLAST and phylogenetic trees, the author tested a 12-tissue human Northern blot and 4 independent lots of Clonetics primary human mesangial cells treated with angiotensin II by RT-PCR and custom polyclonal antisera against recombinant OPmV M and P proteins, confirming absence of endogenous expression.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Ad hoc manual frameshift correction without raw trace access:** To reconstruct full-length F and P proteins, the author manually deleted an A at nt 2110, deleted a T at nt 2155, inserted a C/T between nt 2296–2297, and deleted a T at nt 2461 in `Angrem52`, and inserted a T between nt 1130–1131 in `Angrem104`. While biologically plausible as sequencing errors in the original `Angrem` submissions (or lethal mutations in a defective persistent genome), these edits are speculative without re-sequencing the original cDNA clones.
- **Phylogenetic methodology is basic and lacks bootstrap support values:** In Figure 2, Neighbor-Joining trees of M, F, and P proteins are constructed in MEGA 2.1 from Vector NTI ClustalW alignments without reporting amino acid substitution models, gamma rate heterogeneity, or bootstrap node support values. Moreover, there is a database accession typo in Figure 2's legend: both Dolphin morbillivirus (DMV) and Canine distemper virus (CDV) are listed with the same accession number (`NC_005283`).
- **Extensive reliance on "data not shown":** Pairwise alignments, nucleotide comparisons, Northern blots, RT-PCR primer sets, and Western blot experiments are all cited as "(data not shown)".

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** `Angrem52` and `Angrem104` are paramyxovirus M–F read-through and P/V/C transcripts rather than human mesangial cell genes. `[Well Supported]`
- **Claim 2:** OPmV clusters near Henipaviruses and Tupaia/Mossman paramyxoviruses as a distinct paramyxovirus lineage/genus. `[Well Supported]`
- **Claim 3:** Putative OPmV may cause human infections. `[Fragile]` — As the author rightly notes in the Conclusions, cell-culture contamination (e.g., from rodent or bovine reagents/co-cultures in the laboratory that originally isolated `Angrem52`/`104`) or PCR contamination cannot be excluded, and all 4 tested lots of primary human mesangial cells and human multi-tissue Northern blots were completely negative.

### 4. Reproducibility & Data Completeness
- **Accession numbers:** All GenBank accessions for the focal sequences (`AAK76747`, `AY040225`, `AF367870`) and 21 reference paramyxoviruses are explicitly provided (with the minor duplicate typo `NC_005283` for CDV).
- **Missing experimental details:** Primer sequences for the negative RT-PCR screens and immunization details for the anti-M and anti-P antibodies are omitted ("data not shown").
</Blinded Review: TIME_ANON_0817>
