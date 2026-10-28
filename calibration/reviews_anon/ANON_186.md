# Review of ANON_186

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.7 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.7/3.5 | Claims: 1.4/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.3/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This descriptive study analyzes 10,022 SARS-CoV-2 genome sequences collected across 68 countries and downloaded between 1 February and 1 May 2020 from four repositories (GISAID, GenBank, CNGB/NGDC, and NMDC) after filtering out redundant sequences and genomes with $>50$ ambiguous bases. By performing global pairwise alignments of each sequence against the Wuhan-Hu-1 reference genome (`NC_045512`) using `EMBOSS needle`, the authors catalogue 65,776 total mutation events representing 5,775 distinct genome variants (2,969 missense, 1,965 synonymous, 484 non-coding SNVs, 142 non-coding deletions, 100 in-frame deletions, 66 non-coding insertions, 36 stop-gained, 11 frameshift deletions, and 2 in-frame insertions). Using Ward's hierarchical clustering on a binary sample-by-variant matrix, they classify the genomes into 6 major clades (`Basal`, `D614G`, `L84S`, `L3606F`, `D448del`, and `G392D`) and 14 subclades, and apply `BEAST v2.5` (HKY substitution model, strict molecular clock) to a random subset of 2,000 UTR-trimmed genomes to estimate a median evolutionary rate of $1.12 \times 10^{-3}$ substitutions per site per year and a median tree height of 5.1 months. A variant list is deposited in an external data repository.

As an early genomic snapshot of the first five months of the COVID-19 pandemic, the manuscript accurately captures the rapid global expansion of the `D614G` haplotype (`241C>T`, `3037C>T`, `14408C>T` [`RdRp P323L`], `23403A>G` [`S D614G`]), the strong `C>T` transition bias (consistent with host APOBEC-like deamination), and the predominance of European-derived `D614G` lineages in the United States. However, the technical execution and evolutionary interpretation exhibit several flaws: (1) pairwise alignment (`EMBOSS needle`) without masking error-prone 5′- and 3′-UTR ends or known sequencing/primer artifacts inflates the variant catalogue with hundreds of spurious UTR indels (256 non-coding deletions/insertions) and singleton frameshift/stop-gained calls; (2) hierarchical clustering on an Euclidean/Ward binary matrix is not a phylogenetic method and treats homoplasies (such as `11083G>T` / `L3606F`) as clade-defining synapomorphies; (3) the Discussion speculates without evidence on antiviral resistance (`remdesivir`/`favipiravir`) and on "at least two zoonotic transmissions of SARS-CoV-2 into the human population"; and (4) the text and tables contain multiple numerical, coordinate, and typographical errors (including an inverted 95% credible interval for the BEAST clock rate, misannotation of `1059C>T` as `NSP3` in the text vs. `NSP2` in Table 3, and mismatched table sums).

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The `D614G` clade (co-occurring with `241C>T`, `3037C>T`, and `ORF1ab P4715L` / `RdRp P323L`) became the most prevalent global SARS-CoV-2 lineage by May 2020, and US sequences largely cluster with European `D614G` introductions: [Well Supported].**  
  Across the 10,022 genomes, the four linked variants of the `D614G` haplotype occur in ~5,928–6,334 samples (Table 3), and both the variant clustering (Table 4) and the 2,000-genome `BEAST` phylogeny (Fig. 4) consistently demonstrate that outside the earliest Washington/California `L84S` and basal introductions from China, the majority of US genomes descend from European `D614G` (particularly `D614G/Q57H/T265I`) lineages.

* **SARS-CoV-2 single-nucleotide variants exhibit a pronounced `C>T` transition bias (~7:3 transition-to-transversion ratio) alongside elevated `G>T` transversions: [Well Supported].**  
  Counting distinct mutations in positive-sense orientation (Fig. 2) shows `1,670` distinct `C>T` variants, far exceeding any other substitution class, consistent with host cytidine deaminase editing and reactive oxygen species (`G>T`) damage (or library preparation artifacts).

* **The 10,022 genomes contain 5,775 genuine biological variants including 208 non-coding indels, 11 frameshift deletions, and 36 premature stop-gained mutations: [Overstated].**  
  While the authors filtered out genomes with $>50$ ambiguous bases (`N`s) and truncated the 5′- and 3′-UTRs for the `BEAST` analysis explicitly *"to adjust for length and sequencing errors"* (Methods line 157), they *did not* truncate or mask the 5′- and 3′-UTRs when compiling the variant counts in Table 1. As a result, Table 1 includes 347 variants in the 5′-UTR (265 bp) and 336 variants in the 3′-UTR (229 bp)—over 1.3 distinct variants per nucleotide site—along with non-recurrent singleton frameshifts and stop-gained calls in essential replicase proteins (`RdRp`, `ExoN`, `NSP3`, Table 2) that represent consensus-calling and amplicon-dropoff errors rather than viable circulating viruses.

* **Ward hierarchical clustering of binary variant matrices defines six monophyletic evolutionary clades (`Basal`, `D614G`, `L84S`, `L3606F`, `D448del`, `G392D`): [Fragile].**  
  Hierarchical clustering with Ward's linkage on a binary presence/absence matrix groups sequences by overallphenetic distance rather than shared derived ancestry (parsimony/maximum likelihood), and is sensitive to recurrent homoplasies. In particular, `11083G>T` (`ORF1ab L3606F` / `NSP6 L37F`) is a well-documented hypermutable homoplasy in SARS-CoV-2 that arose independently across multiple clades (`L84S`, `D614G`, and `Basal`), as reflected by the paraphyletic scattering of `L3606F` colors in the `BEAST` tree (Fig. 4).

* **Mutations in `RdRp` (`P323L`) suggest that strains resistant to remdesivir and favipiravir "may emerge quickly," and viral dissemination points to "at least two zoonotic transmissions of SARS-CoV-2 into the human population": [Overstated].**  
  `RdRp P323L` lies at the `NSP12–NSP8` interface outside the catalytic nucleotide-binding pocket targeted by remdesivir/favipiravir, and no phenotypic drug-susceptibility data are presented. Similarly, the statement in the Discussion (line 379) regarding *"the possibility of at least two zoonotic transmissions of SARS-CoV-2 into the human population"* is unsupported by any rooting, animal-reservoir sequence comparison, or phylodynamic test in the paper, and conflicts with the authors' own `BEAST` estimate of a single common ancestor 5.1 months prior (`95% HPD: 4.8–5.52 months`).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Mask Error-Prone 5′/3′ UTRs and Filter Singleton Indel/Stop-Gained Artifacts in Variant Summaries
* **WHY:** Retaining unmasked 5′-UTR (positions 1–265) and 3′-UTR (positions 29,675–29,903) alignments in `EMBOSS needle` generates hundreds of artificial terminal deletions/insertions caused by incomplete sequencing of genome ends, and singleton frameshifts in essential `ORF1ab` replicase subunits are sequencing errors rather than viable viral variants.
* **WHAT:** Apply the same 5′-UTR and 3′-UTR trimming used for `BEAST` (plus a minimum recurrence filter, e.g., observed in $\ge 2$ or $\ge 3$ independent genomes) to the variant summary tables, separating high-confidence recurrent variants from singleton sequencing calls.
* **HOW:** Re-run the Python variant-extraction script excluding terminal UTR bases (e.g., positions $<266$ and $>29,674$, except `241C>T`) and add a column or supplementary breakdown to Tables 1 and 2 showing how many missense, synonymous, frameshift, and stop-gained variants are observed in $\ge 2$ genomes versus singletons.

#### 2. Quantify Concordance Between Ward Hierarchical Clusters and the `BEAST` Phylogeny
* **WHY:** Ward hierarchical clustering on binary matrices can group sequences by shared homoplasies (such as `11083G>T` / `L3606F`) or by shared ancestral reference states (`Basal`).
* **WHAT:** Measure the monophyly / phylogenetic consistency of the 6 major clades and 14 subclades on the 2,000-genome `BEAST` maximum clade credibility (MCC) tree, and report posterior probabilities for each clade node.
* **HOW:** Annotate the internal nodes corresponding to the 6 major clades and 14 subclades on Fig. 4 with their `BEAST` posterior probability values, and explicitly note in the Results where `L3606F` (`11083G>T`) occurs homoplastically across distinct branches.

#### 3. Temper Speculative Claims on Antiviral Resistance and Multiple Zoonotic Spillovers
* **WHY:** Suggesting that `RdRp P323L` indicates rapid emergence of resistance to remdesivir/favipiravir, or that genomic diversity implies "at least two zoonotic transmissions," overreaches descriptive sequence counting.
* **WHAT & HOW:**
  1. In Discussion line 373, revise the sentence on `RdRp P323L` and remdesivir/favipiravir to clarify that `P323L` is outside the polymerase active site and that functional assays are required to determine whether any observed `RdRp` polymorphisms affect nucleoside analogue susceptibility.
  2. In Discussion line 379, remove the unsupported reference to *"at least two zoonotic transmissions of SARS-CoV-2 into the human population"* (or clarify that the `BEAST` molecular clock places the tMRCA of all sampled human clades at a single coalescence ~5.1 months prior in late 2019).

#### 4. Correct Numerical, Protein-Coordinate, and Typographical Errors Across the Text and Tables
* **WHY:** Several direct numerical contradictions and coordinate errors appear in the manuscript.
* **WHAT & HOW:**
  1. **Results line 366 (BEAST clock rate CI):** Change `"95% confidence interval, CI: 9.86 × 10^-4 to 1.85 × 10^-4"` to `"95% highest posterior density interval, HPD: 9.86 × 10^-4 to 1.85 × 10^-3"`. (An upper bound of `1.85 × 10^-4` is 10-fold smaller than the median `1.12 × 10^-3`).
  2. **Results line 233 (`T265I` NSP assignment):** Change `"ORF1ab T265I (NSP3 T85I; 2442 samples)"` to `"ORF1ab T265I (NSP2 T85I; 2442 samples)"` to match Table 3 (`"1059C > T | ORF1ab / NSP2 | T265I/T85I"`).
  3. **Table 1 vs. Table 2 (`ORF1ab` total and `NSP4` row sum):** In Table 2 (line 212), the row for `NSP4` has `116` missense + `113` synonymous + `1` in-frame deletion + `1` stop-gained = `231` (not `232`). Correcting `232` to `231` also fixes the `Total` in Table 2 (line 224) from `3329` to `3328`, making it match the `ORF1ab` total of `3328` in Table 1 (line 177).
  4. **Table 4 (line 308 and line 320):** Correct the truncated GenBank accession `"MN90894"` for Wuhan-Hu-1 to `"MN908947"` (or `"NC_045512"`), and remove the trailing comma in `"EPI_ISL_410486,"`.
  5. **Arabic Abstract (line 81) & Text Typos:** Correct `"L3606FK"` to `"L3606F"` in line 81; `"SD614G"` to `"S D614G"` in line 233; `"SARS-CO-2"` and `"SARS-Co-2"` to `"SARS-CoV-2"` in lines 348 and 371; and `"United Stated"` to `"United States"` in line 377.
