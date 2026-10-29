<Blinded Review: TIME_ANON_0533>
**Composite Score:** 7.5 / 10.0 (Rigor: 2.6/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.3/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 7.5/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This plant evolutionary genomics study sequences and assembles the complete chloroplast genomes (plastomes) of seven Australian perennial *Glycine* species spanning five nuclear genome groups (`G. syndetika` [A], `G. canescens` [A], `G. dolichocarpa` [allopolyploid A/D], `G. tomentella D3` [D], `G. falcata` [F], `G. stenophita` [B], and `G. cyrtoloba` [C]) by selecting two chloroplast-matching bacterial artificial chromosome (BAC) clones per species from *Hind*III genomic BAC libraries and sequencing sheared 3–4 kb subclone libraries with Sanger technology to `9x` depth (`Phrap` assembly). Comparing these seven perennial plastomes (`152,381` to `153,023 bp`, `111` unique genes plus divergent `ycf4`, `35.3%` GC) against cultivated annual soybean (`G. max`, `152,218 bp`, [G]) and outgroup phaseoloid/millettioid legumes (`Phaseolus vulgaris`, `Vigna radiata`, `Millettia pinnata`), the authors find complete conservation of gene order (retaining the ancestral papilionoid `51-kb` LSC inversion without novel inversions) and demonstrate that previous `REPuter` repeat counts (`85–108` repeats `>=30 bp`) are heavily inflated by overlapping length variants and multi-locus pairwise enumeration, collapsing to only `5–10` unique dispersed repeat sequences across `16–28` unique locations (`Table 2`, `Fig. 4`). Finally, comparing relaxed-clock Bayesian divergence time trees (`BEAST` `GTR` uncorrelated lognormal clock calibrated at `19.2 Mya` for `Phaseolus`–`Glycine`) of whole plastomes against nuclear `histone H3D` (`Fig. 5`) and pairwise SNP substitution rates (`Table 3`) confirms cyto-nuclear incongruence for `G. falcata` (which diverges basally at `~4.6 Mya` in nuclear `H3D` trees but nests inside the `A`-plastome clade at `~1.64 Mya`), dating an ancient hybridization and chloroplast capture event to `1–3 Mya`.

### 2. STRENGTHS
- **Critical De-Inflation of `REPuter` Plastome Repeat Statistics:** The authors perform a careful forensic audit of standard `REPuter` output (`>=30 bp`, Hamming distance `<=3`), showing that counting every overlapping sub-length match and every all-against-all pair inflates `85–108` reported repeats when there are actually only `5–10` unique dispersed repeat families occupying `16–28` unique genomic loci (`Table 2`, `Fig. 4`). This is a valuable methodological correction for the plastome comparative genomics field.
- **Thoughtful Analysis of Inter-BAC Polymorphism in `G. falcata` (`π = 0.00083`):** Rather than ignoring the `72` segregating sites across the `86,523-bp` overlap between the two sequenced `G. falcata` BACs (derived from a 5-plant pool of accession `G1718`), the authors sequence the `trnL-trnF` spacer across 11 additional `G. falcata` accessions (`π = 0.00225`) and transparently discuss both inter-individual polymorphism within the pooled accession and the possibility of a large nuclear integrant of plastid DNA (`NuPT`).
- **Quantitative Cyto-Nuclear Divergence Rate Comparison:** Integrating whole-plastome `BEAST` relaxed-clock dating (`Fig. 5A`), nuclear `histone H3D` dating (`Fig. 5B`), and pairwise substitution rate matrices (`Table 3`) clearly demonstrates that while `G. max` vs. perennial plastome divergence is clock-like (`~2.44–2.88 × 10^-9` substitutions/site/year), applying nuclear divergence dates within the `A`-plastome group yields an artificially depressed rate (`5.53–9.48 × 10^-10`), corroborating recent chloroplast introgression (`~1.64 Mya`) into `G. falcata`.

### 3. Methodological & Statistical Audit / WEAKNESSES & METHODOLOGICAL AUDIT
- **Internal Arithmetic Discrepancy in Table 1 for `G. cyrtoloba` LSC Length:** For every circular quadripartite chloroplast genome, the total genome length equals `LSC + SSC + 2 × IR`. Checking Table 1 (Lines 39–46):
  - `G. max`: `83,174 + 17,896 + 2(25,574) = 152,218` (Exact match)
  - `G. syndetika`: `83,844 + 17,840 + 2(25,555) = 152,794` (Exact match)
  - `G. dolichocarpa`: `83,815 + 17,807 + 2(25,591) = 152,804` (Exact match)
  - `G. canescens`: `83,559 + 17,844 + 2(25,565) = 152,533` (Exact match)
  - `G. tomentella D3`: `83,773 + 17,829 + 2(25,563) = 152,728` (Exact match)
  - `G. falcata`: `84,027 + 17,846 + 2(25,575) = 153,023` (Exact match)
  - `G. stenophita`: `83,937 + 17,817 + 2(25,432) = 152,618` (Exact match)
  - `G. cyrtoloba`: Table 1 reports `Total = 152,381`, `SSC = 17,801`, `IR = 25,505`, which requires `LSC = 152,381 - 17,801 - 2(25,505) = 83,570 bp`. However, Table 1 prints `LSC = 89,368` (`5,798 bp` too large, summing to `158,179 bp`!).
- **Secondary Calibration Without Fossil Priors and Single-Locus Nuclear Comparison:** The plastome `BEAST` tree is calibrated using a secondary point estimate (`19.2 Mya` for `Phaseolus`–`Glycine` from `matK` in Lavin et al.) rather than primary fossil priors with lognormal/exponential uncertainty distributions, and the nuclear comparison tree in `Fig. 5B` relies on a single predominantly intronic locus (`histone H3D`, calibrated at `5.25 Mya`), although the authors do cite unpublished transcriptome-wide SNP data (`80 / >27,000` genes) in the text (Line 128).
- **Unverified `ycf1` Premature Stop Codon in `G. cyrtoloba`:** The authors note (Line 77) that `ycf1` in `G. cyrtoloba` contains a premature stop codon in the SSC region, leaving open whether it is a Sanger assembly error, RNA-editing site, or pseudogene.

### 4. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** Perennial *Glycine* plastomes (`152.4–153.0 kb`) are colinear with annual *G. max* (`152.2 kb`), lack structural rearrangements, and contain only `5–10` unique dispersed repeat families once redundant `REPuter` hits are collapsed. `[Well Supported]` — Directly demonstrated by the 7 complete `9x` Sanger BAC-derived plastome assemblies (`Table 1–2`, `Fig. 2–4`), modulo the typographical error in `G. cyrtoloba` LSC length in Table 1.
- **Claim 2:** Whole-plastome phylogenomics and molecular dating support chloroplast capture of an ancestral `A`-group plastome by `G. falcata` (`F`-genome) via hybridization `~1–3 Mya` (`point estimate 1.64 Mya`). `[Well Supported]` — Strongly supported by whole-plastome vs. `histone H3D` topological and branch-length incongruence (`Fig. 5`), clock-rate comparisons (`Table 3`), and absence of deep ancestral plastome polymorphism across 11 additional `G. falcata` accessions (`trnL-trnF`).

### 5. Reproducibility & Data Completeness
- **Data Availability:** The whole-plastome sequence alignment is deposited in NCBI GenBank as `Popset 514252878`, comparative GenBank accessions (`DQ317523`, `DQ886273`, `JN673818`, `GQ893027`) are specified, and BAC clone details are provided in Supporting Information `Table S1`. (Note: in `Table 3` Lines 138–139, the automated year-scrubbing filter replaced two 4-digit SNP counts around `2000` with `[YEAR]`, which is an artifact of the anonymization script rather than an author error.)
</Blinded Review: TIME_ANON_0533>
