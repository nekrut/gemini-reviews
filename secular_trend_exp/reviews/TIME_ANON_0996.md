</Agent System Instructions>
<Blinded Review: TIME_ANON_0996>
**Composite Score:** 8.8 / 10.0 (Rigor: 3.1/3.5 | Claims: 2.3/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 8.8/10
VERDICT: PASS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary / SUMMARY
This landmark conservation genetics and phylogeography study evaluates the evolutionary history and intraspecific taxonomy of the tiger (*Panthera tigris*) across 134 voucher specimens of verified geographic origin (100 strict wild-born/verified-parentage vouchers plus 34 supplementary individuals, including 28 historical pelts/hair samples analyzed under ancient-DNA clean-room precautions). The authors assay three independent marker systems: (1) 4,078 bp of cytoplasmic mitochondrial DNA (`Cymt`, $n = 100$ tigers, 54 variable sites, 25 haplotypes) amplified using primer sets specifically engineered to exclude the 12.8-kb autosomal nuclear mitochondrial pseudogene (`Numt`) on *Panthera* chromosome F2; (2) MHC class II *DRB* exon variation via SSCP ($n = 21$ tigers, 7 alleles); and (3) 30 mapped felid nuclear microsatellite loci ($n = 113$ tigers). The data demonstrate strong, concordant phylogeographic partitioning ($F_{ST} = 0.838$ for mtDNA; $R_{ST} = 0.31$ for microsatellites, $p < 0.0001$) across five major extant lineages, notably uncovering a deep genetic division within traditional Indochinese tigers (*P. t. corbetti*) across the Isthmus of Kra into northern Indochinese (*P. t. corbetti* I) and Malayan Peninsula (*P. t. jacksoni* / *P. t. corbetti* II) subspecies (pairwise mtDNA $F_{ST} = 0.797$, microsatellite $R_{ST} = 0.225$). In addition, 3 of 5 captive South China tigers (*P. t. amoyensis*) cluster within northern *P. t. corbetti* I while 2 individuals (`Pti-219`, `Pti-220`) form a distinct lineage (`AMO1`), and linearized-tree molecular clock calibration against leopard (*P. pardus*) dates the modern tiger mtDNA coalescence to 72,000–108,000 years ago ($N_{ef} \approx 13,350$).

### 2. Methodological & Statistical Audit / STRENGTHS, WEAKNESSES & METHODOLOGICAL AUDIT

#### Strengths
- **Rigorous Resolution of the *Panthera* `Numt` Confounder**: By aligning the complete 12.8-kb chromosome F2 `Numt` sequence against cytoplasmic mtDNA to design 15 `Cymt`-specific primer pairs spanning 6,026 bp, the authors overcome the paralogous co-amplification artifact that invalidated earlier *Panthera* mitochondrial studies.
- **Triangulation Across Matrilineal, Biparental Neutral, and Adaptive Markers**: Concordance between 4,078 bp of mtDNA (MP, ME, ML trees and `TCS` parsimony networks), 30 unlinked nuclear microsatellites (`Dps`/`Dkf` NJ trees, `ARLEQUIN` $R_{ST}$, and Bayesian `STRUCTURE` clustering), and MHC class II *DRB* alleles provides robust multi-locus support for the six phylogeographic units.
- **Hypothesis-Driven AMOVA Testing**: Explicitly comparing four nested biogeographic subdivision models (2-group island vs. mainland; 3-group separating Amur; 4-group classical subspecies; 5-group splitting Indochinese at the Isthmus of Kra) via 10,000-permutation AMOVA quantitatively demonstrates that the 5-group model maximizes between-group variance for both mtDNA ($F_{ST} = 0.838$) and microsatellites ($R_{ST} = 0.31$).
- **Careful Handling of Captive *P. t. amoyensis* Introgression**: Rather than overclaiming the status of the captive South China tiger, the authors transparently show that 3 of 5 sampled *P. t. amoyensis* vouchers (Suzhou Zoo) carry northern *P. t. corbetti* I maternal and nuclear genotypes, leaving only 2 Chongqing Zoo individuals (`AMO1`) as tentative representatives of an authentic *amoyensis* lineage.

#### Weaknesses & Methodological Audit
1. **Pre-Screening Ascertainment Bias in the 4,078-bp mtDNA Subset**:
   - Five of the 15 `Cymt` primer segments (1,948 bp out of 6,026 bp) showed no polymorphism in an initial screen of 15 tigers and were excluded from sequencing in the remaining 85 tigers (lines 14, 35, 38). While the authors transparently report the density of variable sites for both the 4,078-bp variable subset (1 per 75 bp) and the full 6,026-bp region (1 per 112 bp) in the Discussion (line 119), estimating $\theta = 0.00255$ per site and $N_{ef} = 13,350$ from the 4,078-bp variable subset without including the 1,948 invariant bases inflates per-site $\theta$ by a factor of $6026 / 4078 = 1.48\times$ (though the leopard–tiger clock calibration uses a 3,217-bp homologous subset of the same genes, mitigating bias in $T_{\text{MRCA}}$).
2. **Limited Sample Size and SSCP Resolution for MHC-*DRB***:
   - The MHC class II *DRB* analysis examines only $n = 21$ tigers overall (including only $n = 1$ Bengal tiger, $n = 2$ *corbetti* I, and $n = 2$ *corbetti* II) and scores alleles visually by autoradiographic SSCP mobility rather than cloning and sequencing the amplicons across multiple *DRB* paralogs.
3. **Coding of Haploid mtDNA inside `STRUCTURE`**:
   - In the combined `STRUCTURE` analysis (chunk 2, line 27), haploid mtDNA was coded as a diploid locus with the second allele set to missing (`-9`) alongside 30 diploid microsatellites; while a common workaround, `STRUCTURE` assumes unlinked mendelian loci in Hardy–Weinberg equilibrium within clusters.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1**: Extant tigers partition into five well-supported phylogeographic subspecies (*altaica*, *corbetti* I, *jacksoni* [*corbetti* II], *sumatrae*, *tigris*) plus a tentative sixth (*amoyensis*, $n = 2$). `[Well Supported]` — Strongly supported across 134 voucher specimens by mtDNA phylogenetics, 30 nuclear microsatellites, AMOVA, and biogeographic concordance at the Isthmus of Kra.
- **Claim 2**: Modern tiger mtDNA coalesces to a relatively recent common ancestor 72,000–108,000 years ago (95% CI: 39,000–157,000 ya), roughly contemporaneous with the Late Pleistocene Toba eruption (~73.5 ka), with northern Indochina/southern China acting as the Pleistocene refugial center of radiation. `[Well Supported]` — Grounded in linearized molecular clock calibration (2–3 MY leopard–tiger divergence) and highest microsatellite allelic richness and continuity in *P. t. corbetti* I.

### 4. Reproducibility & Data Completeness
- **Accession Numbers & Marker Reporting**: GenBank accession numbers `AY736559`–`AY736808` (250 sequence entries) and all 30 `FCA` microsatellite locus IDs, PCR cycling conditions, and software parameters (`PAUP`, `MODELTEST 3.06`, `TCS 1.13`, `ARLEQUIN 2.0`, `LINTRE`, `DnaSP 4.0`, `GENEPOP 3.1c`, `MICROSAT`, `STRUCTURE`) are fully documented.
- **Omitted Table Cells in Markdown**: In the text conversion, the tabular contents of Tables 1–8 are represented only by their titles, although the primary numerical results are stated in the main text.
</Blinded Review: TIME_ANON_0996>
