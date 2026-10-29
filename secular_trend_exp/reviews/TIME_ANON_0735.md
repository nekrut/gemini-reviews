<Blinded Review: TIME_ANON_0735>
**Composite Score:** 6.8 / 10.0 (Rigor: 2.2/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.0/2.0)
**Scientific Core Score:** 5.8 / 8.0
**Bias Category:** Technical/Assay
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 6.8/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary (SUMMARY)
This hybrid wet-lab and molecular phylogenetics study characterizes duplicated growth hormone paralogs (*GHI* and *GHII*, 633 bp coding sequence across 5 exons) amplified from 23 species of tetraploid catostomid fishes (suckers) and compares them against cyprinid, cobitid, and gyrinocheilid outgroups. The authors document conserved 5-exon/4-intron gene architecture, identify a lineage-specific loss of the unpaired 5th cysteine (`Cys145` $\to$ `Tyr`) in catostomid *GHI*, show strong overall purifying selection ($d_N < d_S$), and investigate an anomalous phylogenetic placement in which *GHII* sequences from Tribe Catostomini cluster with Cyprinidae rather than with other catostomid *GHII* sequences. Using Templeton's nonparametric topology constraint tests, the authors transparently show that forcing Catostomidae *GHII* monophyly is not significantly worse than the unconstrained tree ($P = 0.0555$ and $P = 0.5034$). However, the study suffers from a major technical limitation: exons 4 and 5 (>50% of the coding sequence) could not be amplified for *GHII* in almost all catostomid species outside Tribe Catostomini and *Ictiobus bubalus*, creating a severe missing-data block right where the putative amino acid synapomorphies (`Val90Met`, `Leu169Met`) occur. In addition, Table 1 and GenBank accession numbers for the newly sequenced genes are missing from the manuscript file.

### 2. Methodological & Statistical Audit (STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT)
**Strengths:**
- **Transparent Hypothesis Testing of Topological Anomalies:** Rather than over-interpreting the anomalous clustering of Tribe Catostomini *GHII* with Cyprinidae (`Figure 1`), the authors explicitly perform Templeton's Wilcoxon signed-rank topology constraint tests (`lines 42–43`, `55–57`) under two constraint scenarios and report that neither constraint is statistically rejected ($P = 0.0555$ and $P = 0.5034$).
- **Careful Structural & Biochemical Annotation:** Maps all five cysteine residues (`Cys49, Cys158, Cys175, Cys183` plus the extra unpaired `Cys145` in carp/goldfish/catostomid *GHII* that is substituted by `Tyr145` in catostomid *GHI*) onto the known 4-$\alpha$-helix bundle disulfide bridge topology (`Cys49–Cys158` and `Cys175–Cys183`).

**Weaknesses & Methodological Flaws:**
- **Severe Non-Random Missing Data in *GHII* Confounds Paralog Phylogenetics (`lines 25–26, 36–37`):** The authors report that for *GHII*, exons 4 and 5 (containing `339 bp` of the `633 bp` coding region, i.e., `53.6%` of the gene) could not be amplified in any catostomid species outside Tribe Catostomini (`Catostomus`, `Chasmistes`, `Deltistes`, `Xyrauchen`) and `Ictiobus bubalus`. Crucially, two of the key amino acid characters linking Tribe Catostomini *GHII* to Cyprinidae (`Val90Met` and `Leu169Met`, `line 41`) reside in the region missing from most other catostomid *GHII* sequences (`Myxocyprinus`, `Cycleptus`, `Carpiodes`, `Hypentelium`, `Minytrema`, `Moxostoma`, `Thoburnia`, `Erimyzon`). Analysing an alignment where one clade has full-length 633 bp sequences and its sister clades are missing >50% of the characters (`339/633 bp`) is a classic recipe for systematic missing-data / long-branch attraction artifacts in Maximum Parsimony and Maximum Likelihood. The authors should have repeated the phylogenetic and Templeton tests restricted strictly to the shared `294 bp` (exons 1–3) region sequenced across all taxa.
- **Crude Selection Testing (`line 33`):** Purifying vs. positive selection is evaluated only via global alignment-wide Nei-Gojobori pairwise $d_N/d_S$ $Z$-tests in `MEGA 4.0` ($P = 0.003$ overall, $P = 0.008$ within *GHI*, $P = 0.002$ within *GHII*), rather than branch-site or site-specific codon models (`PAML`/`HyPhy`) that can test episodic post-duplication divergence between *GHI* and *GHII*.
- **Direct Sanger Sequencing of Paralogous PCR Products:** While paralog-specific primers (`Table 2`) were designed, PCR products were sequenced directly (`lines 26–27`) without cloning to verify the absence of chimeric PCR recombinants or allelic heterozygosity in tetraploid fishes.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *Catostomid fishes retain two distinct, expressed growth hormone paralogs (GHI and GHII) evolving predominantly under purifying selection.* `[Well Supported]` — Supported by distinct exon/intron sequences, absence of premature stop codons in sequenced regions, and significant excess of synonymous over nonsynonymous substitutions ($P \le 0.008$).
- **Claim 2:** *Catostomid GHI lost the unpaired fifth cysteine (`Cys145 -> Tyr`), whereas catostomid GHII retained `Cys145`.* `[Moderately Supported]` — Supported in all taxa where exon 4 was sequenced (`GHI` across catostomids; `GHII` in Catostomini and `Ictiobus bubalus`), though unverified in *GHII* of non-Catostomini genera where exon 4 failed to amplify.
- **Claim 3:** *The clustering of Tribe Catostomini GHII with Cyprinidae is driven by only 5 nucleotide characters and is not statistically distinguishable from monophyletic Catostomidae GHII.* `[Well Supported]` — Directly supported by character tracing and Templeton constraint tests ($P = 0.0555$ and $P = 0.5034$).

### 4. Reproducibility & Data Completeness
- **Strengths:** Primer sequences (`Table 2`), PCR thermal cycling profiles, `Garli v0.951` `GTR+I+G` parameters, and `PAUP* 4.0b10` parsimony settings are clearly reported.
- **Weaknesses:** `Table 1` (which is cited in `lines 20` and `45` as listing the 23 catostomid species, sample localities, and outgroup GenBank accession numbers) is completely omitted from the manuscript text, and no GenBank accession numbers are provided for the newly generated *GHI* and *GHII* sequences.
</Blinded Review: TIME_ANON_0735>
