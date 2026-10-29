<Blinded Review: TIME_ANON_0831>
**Composite Score:** 7.7 / 10.0 (Rigor: 2.6/3.5 | Claims: 2.0/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.6/2.0)
**Bias Category:** Technical/Assay
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 7.7/10
VERDICT: PASS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This evolutionary genomics resource paper presents an annotated chromosome-level reference genome assembly (`OSU_ERuf_1`, `GCA_041146395.1` / `GCF_041146395.1`) for a captive female red-fronted brown lemur (*Eulemur rufifrons*, individual "Redbay" from the Duke Lemur Center) using PacBio Sequel II HiFi reads (6 SMRT cells, 89.7 Gb, mean read length 16.5 kb, $37\times$ raw / $15\times$ filtered Q20 CCS coverage mentioned in text) and Illumina NovaSeq 6000 Hi-C proximity ligation data. Assembled with `hifiasm` and scaffolded with `yahs`, the 2.41-Gb assembly spans 647 scaffolds (30 pseudochromosomes aligned to *Eulemur mongoz* `GCA_028534055.1`), achieving a contig N50 of 91 Mb, scaffold N50 of 100.8 Mb, 16 telomere-to-telomere capped chromosomes (plus 11 single-end capped), nucleotide BUSCO completeness of 95.3% (protein annotation BUSCO 97.1% across 13,780 primate orthologs), and 19,514 annotated protein-coding genes. Synteny analysis shows 99.4% chromosomal conservation of single-copy BUSCOs with *E. mongoz*. Phylogenomic analyses across 17 Lemuridae assemblies using `MAFFT` + `RAxML-ng` gene trees in `ASTRAL-IV` and `PhyloNetworks` (`SNaQ`) reveal pervasive gene-tree discordance (gCF $< 50\%$ on 86.7% of nodes) and place the focal captive individual sister to *Eulemur rufus* in `ASTRAL-IV` or within a reticulate *E. rufifrons* clade ($H=1$) in `SNaQ`.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### STRENGTHS
- **High-contiguity chromosome-scale assembly and RefSeq annotation:** Achieving a 91-Mb contig N50 and 100.8-Mb scaffold N50 with 27/30 pseudochromosomes having at least one telomeric cap (16 capped at both ends) and 97.1% proteome BUSCO completeness provides a high-quality reference genome for *Lemuridae*.
- **Appropriate coalescent and network phylogenomic methods:** Combining `ASTRAL-IV` species tree estimation with `IQ-TREE2` gene/site concordance factors (`gCF`/`sCF`) and `SNaQ` multispecies coalescent network inference ($H=0\text{–}5$) properly distinguishes high local posterior probability (`1.0` at all nodes due to large gene count) from underlying biological gene-tree conflict (`gCF` 9.87–21.0% in the *E. fulvus* complex).
- **Full open-science reproducibility:** Raw reads (`PRJNA1104249`), annotated RefSeq assembly (`GCF_041146395.1`), and all bash/R analysis scripts on GitHub are publicly available.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Internal typographical and accession errors in the Results and Figure legends:**
  1. **Unit typo in Results line 65:** Line 65 states: *"there were 647 scaffolds with a N50 of 100.8 Gb and a total size of 2.41 Gb"* (`100.8 Gb` is a typo for `100.8 Mb`, which is correctly listed in the Abstract and Table 1).
  2. **Mitogenome length discrepancy between Text and Table 1:** Line 65 states: *"The reconstructed mitochondrial genome was 17,079 nucleotides in length with a GC content of 39%, similar to the ring-tailed lemur mitogenome (length = 17,086, GC = 38%)."* However, Table 1 lists *E. rufifrons* "Mitochondrion length (bp): `17,086`" and "Mitochondrion GC content: `38%`"—accidentally copying the *Lemur catta* reference numbers into Table 1!
  3. **Wrong GenBank accession printed in Figure 3 legend:** Figure 3 legend states: *"Synteny plot comparing our chromosome-scale E. rufifrons genome (GCA_963574465.1) and the E. mongoz chromosome-scale genome (GCA_028534055.1)."* Yet `GCA_963574465` is the accession for **Eulemur rufus** (as stated on line 140: *"Eulemur rufus (GCA_963574465)"*), whereas the authors' *E. rufifrons* assembly is `GCA_041146395.1` (Table 1)!
  4. **Coverage calculation discrepancy:** Line 65 states that 6 SMRT cells yielded `89.7 Gb` of nucleotide data for a `2.41 Gb` genome ($89.7 / 2.41 = 37.2\times$ coverage), yet two sentences later reports *"a mean depth of coverage of 15x"* without explaining whether >50% of reads were filtered out at Q20 or if $15\times$ refers to each phased haplotype.
- **Unverified taxonomic provenance of the focal captive individual ("Redbay"):** As the authors candidly admit (lines 23 and 155), Redbay's pedigree at the Duke Lemur Center was lost, her wild geographic origin is unknown, and *E. rufifrons* and *E. rufus* were historically managed as a single taxon (*E. fulvus rufus*) in captivity! Thus, the finding that Redbay clusters with *E. rufus* in `ASTRAL-IV` (Fig. 4) and has $2n=60$ (30 chromosomes) whereas the wild eastern *E. rufifrons* genome from Ranomafana National Park (`GCA_043251655`) has 28 chromosomes (line 155) very likely reflects that Redbay is either a captive *E. rufus* $\times$ *E. rufifrons* hybrid or a western *E. rufifrons*/*E. rufus* lineage rather than pure wild *E. rufifrons*.
- **Omission of the X chromosome:** Even though the sequenced individual is female (XX), chromosomes were named 1–30 solely by alignment to an *E. mongoz* assembly that lacked sex chromosome labels, leaving the X chromosome unidentified among the 30 pseudochromosomes.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** The `OSU_ERuf_1` assembly is a highly contiguous, nearly complete chromosome-scale genome (N50 = 100.8 Mb, 97.1% protein BUSCO completeness) showing 99.4% single-copy gene synteny with *E. mongoz*. `[Well Supported]`
- **Claim 2:** Low gene and site concordance factors across the *Eulemur* radiation reflect pervasive incomplete lineage sorting and/or historical introgression. `[Well Supported]`
- **Claim 3:** Discordant placement of `OSU_ERuf_1` relative to the wild Ranomafana *E. rufifrons* assembly reflects natural wild parapatric/allopatric introgression vs captive hybrid ancestry. `[Moderately Supported]` — The authors appropriately acknowledge the lost captive pedigree of Redbay as a caveat.

### 4. Reproducibility & Data Completeness
- **Exemplary data and code availability:** NCBI BioProject `PRJNA1104249`, RefSeq `GCF_041146395.1`, and complete GitHub workflow repository are provided.
</Blinded Review: TIME_ANON_0831>
