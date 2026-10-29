<Blinded Review: TIME_ANON_0332>
**Composite Score:** 6.6 / 10.0 (Rigor: 2.1/3.5 | Claims: 1.8/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** Algorithmic/Model
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This descriptive molecular virology study reports the complete genome sequences and phylogenetic characterization of two orthohepeviruses obtained from liver tissues of an African giant shrew (*Crocidura olivieri*, strain `Co-KY2016`, 7,019 nt excluding poly(A) tail) and a black rat (*Rattus rattus*, strain `Rr-KY2016`, 6,942 nt) captured in Kitale, western Kenya. Using RNA-seq on an Illumina HiSeq 3000 platform (`fastp` filtering, `Bowtie2` rRNA depletion against SILVA, `MEGAHIT` de novo assembly) followed by gap-filling nested RT-PCR, 5'/3' RACE, and TA-cloning Sanger verification, the authors recover full-length genomes and analyze their genomic organization, pairwise nucleotide/amino acid identities, SimPlot sliding-window similarity, and ORF1/ORF2 phylogenetic placement. Strain `Co-KY2016` clusters in a distinct monophyletic lineage alongside recently reported shrew hepeviruses from Germany (*Crocidura russula*, `OR713884`, 74.5% nt identity) and Ethiopia (*Crocidura olivieri*, `PQ489619`, 74.2% nt identity) while sharing $<55\%$ identity with established *Orthohepevirinae* genera. Strain `Rr-KY2016` falls within *Rocahepevirus ratti* genotype C1 (HEV-C1), sharing 86.9% whole-genome nt identity and 94.7% ORF2 amino acid identity with a human-infecting rat HEV strain from France (`OR633290`).

The wet-lab genome completion (including 5' and 3' RACE) and GenBank deposition (`PV861666`, `PV861667`) are solid, providing valuable genomic surveillance data from East Africa. However, the evolutionary and phylogenetic methodology relies on dated Neighbor-Joining distance methods with a simplistic Poisson amino acid model, and the manuscript omits basic epidemiological denominators from the field trapping survey.

### 2. Methodological & Statistical Audit
- **Suboptimal Phylogenetic Inference Model:** In the Methods and Figure 4/5 legends, phylogenetic trees for divergent viral ORF1 (1,546–1,709 aa) and ORF2 (635–660 aa) proteins across all genera of *Hepeviridae* are reconstructed using the **Neighbor-Joining (NJ) method with a Poisson correction model and pairwise deletion** in MEGA 7.0. For deep genus-level viral protein phylogenies where pairwise amino acid identities drop below 35–55% (Table 1), distance-based NJ with an equal-rate Poisson model and pairwise deletion is well known to suffer from long-branch attraction and systematic underestimation of multiple substitutions at variable sites. Standard practice requires Maximum Likelihood inference (e.g., IQ-TREE or RAxML) with model selection (such as `LG+F+I+G4`) and complete/site-filtered alignment handling.
- **Inaccurate Statement Regarding ICTV Demarcation Criteria:** In the Discussion (line 97), the authors state that "in the latest guidelines from the International Committee on Taxonomy of Viruses (ICTV), the p-distance values that define genera and species within the family Hepeviridae are not specified." In fact, the ICTV *Hepeviridae* Study Group taxonomy report explicitly defines evolutionary distance thresholds in conserved methyltransferase, helicase, and RdRp domains (and whole-genome/ORF2 p-distances) for species and genotype demarcation.
- **Missing Field Survey Denominators and Viral Load Metrics:** Although this study derives from a small-mammal trapping survey in Kitale (referencing a prior hantavirus publication), the manuscript never states how many *Crocidura olivieri* shrews and *Rattus rattus* rats were screened to identify `Co-KY2016` and `Rr-KY2016`, nor does it report sequencing read depth/coverage across the viral genomes or RT-qPCR viral loads in the liver vs. other tissues.
- **Absence of Recombination Testing:** Although SimPlot sliding-window similarity plots are presented (Fig. 3), no formal statistical recombination tests (e.g., BootScan or RDP4/RDP5) were executed to verify the absence of intragenic recombination.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **[Well Supported]** `Co-KY2016` (7,019 nt) and `Rr-KY2016` (6,942 nt) represent authentic, complete orthohepevirus genomes with verified 5' and 3' termini.
- **[Well Supported]** `Co-KY2016` forms a well-supported *Crocidura* shrew-associated clade (with `OR713884` and `PQ489619`) possessing a distinct genomic architecture (non-overlapping ORF2 and ORF3, absence of ORF4) that likely merits classification as a novel genus or species within *Orthohepevirinae*.
- **[Well Supported]** `Rr-KY2016` is a canonical *Rocahepevirus ratti* genotype C1 strain possessing the conserved overlapping ORF4 and high capsid identity (94.7% aa) to zoonotic human-infecting rat HEV-C1 strains.

### 4. Reproducibility & Data Completeness
- **Strengths:** Complete genome sequences of `Co-KY2016` and `Rr-KY2016` are publicly deposited in GenBank under accessions `PV861666` and `PV861667`, and all comparison reference accessions are clearly listed in Tables 1–2 and Figures 4–5.
- **Deficiencies:** Raw Illumina HiSeq 3000 metatranscriptomic reads (SRA/ENA accession) are not deposited; primer sequences used for gap-filling nested RT-PCR and 5'/3' RACE are referred to a supplementary table not embedded in the main text; field sample size denominators are omitted.
</Blinded Review: TIME_ANON_0332>
