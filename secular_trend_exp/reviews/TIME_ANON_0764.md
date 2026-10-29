<Blinded Review: TIME_ANON_0764>
**Composite Score:** 6.8 / 10.0 (Rigor: 2.2/3.5 | Claims: 1.6/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.6/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 6.8/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This comparative and population genomics study presents a chromosome-level reference genome assembly for the Tibetan plateau/Yangtze tributary loach *Triplophysa bleekeri* (Nemacheilidae), generated from 100.87 Gb (~160$\times$) PacBio Sequel long reads, 81.7 Gb (~129$\times$) Illumina HiSeq X Ten short reads, and 83.5 Gb (~132$\times$) Hi-C proximity ligation reads, yielding a ~620–628 Mb assembly (contig N50 = 3.11–3.82 Mb, scaffold N50 = 22.89 Mb, 96.2% anchored onto 25 chromosomes, 92.9% BUSCO `actinopterygii_odb9` completeness) with 21,198 annotated protein-coding genes supported by 11.1 Gb of pooled 12-tissue RNA-seq. The authors perform comparative phylogenomics (`OrthoMCL`, `RAxML`, `PAML MCMCTree` across 1,364 single-copy orthologs), gene family expansion/contraction (`CAFE`), branch-site positive selection scans (`PAML codeml`) across *T. bleekeri*, *T. tibetana*, and *T. siluroides*, demographic history reconstruction (`PSMC`), and whole-genome resequencing of $N = 28$ individuals across three Daning River reaches (`LHK` $n=11$, `XX` $n=11$, `BY` $n=6$). While the chromosome-scale genome assembly and multi-tissue annotation are high-quality resources, the evolutionary and population genetic analyses suffer from several methodological flaws: comparing a cypriniform loach exclusively against distantly related low-altitude outgroups (only *Danio rerio* is an ostariophysan, while the other 7–9 species are percomorphs, gadiforms, holosteans, and chondrichthyans!) confounds lineage-specific cypriniform biology with "high-altitude adaptation"; the 73,887-bp alignment length for 1,364 genes implies severe `Gblocks` truncation (~54 bp/gene); and the population selective sweep scan uses noisy 1-kb windows with $n=6$ in the `BY` population.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES

#### STRENGTHS
- **High-Contiguity Hybrid Chromosome Assembly:** Combining 160$\times$ PacBio Sequel long reads (`Falcon` + `Arrow`), 129$\times$ Illumina polishing (`Pilon` + `Redundans`), and 132$\times$ Hi-C scaffolding anchored 596.96 Mb (96.2%) of the assembly onto 25 chromosomes matching the species karyotype ($2n = 50$), with strong BUSCO completeness (92.9%).
- **Candid Acknowledgment of Demographic Confounding on Selection Scans:** In the Discussion, the authors explicitly note that severe Pleistocene population bottlenecks (the ~70-fold `PSMC` decline from $N_e \approx 7 \times 10^5$ at 0.6–0.7 Mya to $1 \times 10^4$ at 60 kya) can inflate false-positive signatures in selection scans (`[98]`).
- **Exemplary Data Deposition:** All raw PacBio, Illumina, Hi-C, and RNA-seq reads (`SRA: SRP200140`), the chromosome assembly (`BioProject: PRJNA545014`, `VFQW00000000`), and GigaDB supporting annotations are publicly deposited.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Phylogenetically Confounded Outgroup Selection for "High-Altitude Adaptation" (`CAFE` & `codeml`):** To identify expanded gene families (`CAFE`) and positively selected genes (`codeml` branch-site model) associated with high-altitude adaptation in *T. bleekeri*, the authors compare *T. bleekeri* against 8–10 "non-QTP" fish species: *Danio rerio*, *Oryzias latipes*, *Xiphophorus maculatus*, *Takifugu rubripes*, *Tetraodon nigroviridis*, *Larimichthys crocea*, *Gadus morhua*, *Gasterosteus aculeatus*, *Lepisosteus oculatus*, and *Callorhinchus milii* (plus *Cyprinus carpio* only in homology annotation).
  1. Aside from *Danio rerio* (diverged ~110–150 Mya), **none** of the comparator species belong to Cypriniformes or even Ostariophysi! Seven are Neoteleostei/Acanthomorpha (~230 Mya divergence), one is a holostean gar (~320 Mya), and one is a cartilaginous elephant shark (~470 Mya), and several (*Gadus morhua*, *Larimichthys crocea*, *Takifugu*, *Callorhinchus*) are marine cold/deep-water species!
  2. Furthermore, as stated in the Introduction (line 22), *T. bleekeri* actually inhabits elevations from **200 to 3,000 m** (and the Daning River sampling site at $31.157^\circ\text{N}, 109.892^\circ\text{E}$ near Wuxi Town is in the Three Gorges / Daba Mountains region at modest elevation, $<1,648\text{ m}$), unlike true extreme-altitude plateau species (*T. tibetana* at 4,000–5,000 m). Without including low-altitude cypriniform/cobitoid sister taxa (e.g., *Misgurnus anguillicaudatus*, *Paramisgurnus*, or low-elevation nemacheilids), every cypriniform- or cobitoid-specific gene family change since splitting from zebrafish 100+ Mya is falsely attributed to "high-altitude QTP adaptation."
- **Extreme `Gblocks` Alignment Truncation (73,887 bp across 1,364 Single-Copy Orthologs):** On line 177, the authors state: *"Using single-copy genes among species [1,364 single-copy orthologs], a concatenated alignment matrix was generated with a total length of 73,887 bp"*. Dividing $73,887\text{ bp}$ by $1,364\text{ genes}$ yields an average of only **54.17 base pairs (18 codons) per gene**! Running `Gblocks` with default stringent parameters across an alignment spanning teleosts to elephant shark (*Callorhinchus milii*) stripped away $>95\%$ of the coding sequence of each gene, leaving only tiny ultra-conserved domain cores for both phylogenomics and `codeml` positive selection scans!
- **Underpowered Sample Size ($n=6$) and Ultra-Short 1-kb Windows in Selective Sweep Scans:**
  1. The `BY` population comprises only **$n=6$ diploid individuals** (12 chromosomes), for which allele frequency and nucleotide diversity ($\theta_\pi$) estimates have large sampling variance.
  2. Scanning a 628-Mb genome in **1-kb non-overlapping windows** (line 114 & 213) with ~3 million SNPs averages only ~4.8 SNPs per 1-kb window! Ranking the top 1% of $Z(F_{ST})$ and $\log_2(\theta_\pi\text{ ratio})$ in 1-kb windows with ~5 SNPs and $n=6$ samples is heavily dominated by stochastic sampling variance rather than classic hitchhiking sweeps (which typically span 10–100 kb).
- **Taxonomy Typo in Methods:** Line 75 refers to *"three-spined sticklebacks (Xiphophorus maculatus)"*, whereas *Xiphophorus maculatus* is the southern platyfish (and three-spined stickleback is *Gasterosteus aculeatus*). Similarly, Table 1 vs. text has minor discrepancies in clean read totals (81.69 vs 81.7 Gb, 10.6 vs 11.1 Gb transcriptome, 82.9 vs 83.5 Gb Hi-C).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *The ~620–628 Mb chromosome-level assembly of T. bleekeri spans 25 chromosomes with 96.2% anchoring and 92.9% BUSCO completeness.* `[Well Supported]` — Directly supported by PacBio + Illumina + Hi-C metrics (Tables 1–2).
- **Claim 2:** *Daning River populations `LHK` and `XX` are genetically connected, whereas `BY` is genetically differentiated across natural gorge and dam barriers.* `[Well Supported]` — Consistently supported by whole-genome NJ tree, PCA (PC1 = 14.5%), and `ADMIXTURE` clustering (Fig. 5).
- **Claim 3:** *Gene family expansions in lipid metabolism/immunity and positive selection in DNA repair pathways represent adaptive convergence of T. bleekeri to high-altitude QTP environments.* `[Fragile]` — Severely confounded by the lack of low-altitude cobitoid/cypriniform outgroups, the 54-bp/gene `Gblocks` alignment truncation, and the fact that *T. bleekeri* occurs down to 200 m elevation in fast-flowing river tributaries rather than on the high-elevation plateau proper.

### 4. Reproducibility & Data Completeness
- **Public Repository Completeness:** Exemplary; NCBI BioProject `PRJNA545014`, assembly accession `VFQW00000000`, SRA accession `SRP200140`, and GigaDB deposition provide full access to raw reads, chromosomal fasta, and gene annotations, and software versions (`Falcon v0.3.0`, `Pilon v1.23`, `Redundans v0.14a`, `BUSCO v3.0`, `MAKER`, `OrthoMCL v1.2`, `RAxML v8.2.10`, `PAML`, `CAFE v4.2.1`, `GATK v4.1.8.1`, `PSMC v0.6.5`) are thoroughly documented with RRIDs.
</Blinded Review: TIME_ANON_0764>
