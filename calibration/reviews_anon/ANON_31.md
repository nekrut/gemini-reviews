# Review of ANON_31

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.6 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 2.0/3.5 | Claims: 1.6/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.5/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript analyzes 7,666 public SARS-CoV-2 genome assemblies downloaded from GISAID as of April 19, 2020, to characterize early viral demographic history, global geographic distribution of clades, and recurrent mutations (homoplasies). Using root-to-tip regression in `BactDating` ($R^2 = 0.20, p < 0.001$) and strict-clock calibration in `TreeDater` with 50 parametric bootstrap replicates, the authors estimate a time to the most recent common ancestor (tMRCA) between October 6 and December 11, 2019. Using `MPBoot` and `HomoplasyFinder`, they identify 1,042 unfiltered homoplasies outside masked regions and apply heuristic filters—requiring variant frequency $\ge 0.1\%$ ($\ge 8$ isolates), nearest-neighbor phylogenetic clustering ($p_{nn} > 0.1$), representation across $>1$ originating and submitting laboratory, and absence of flanking ambiguous bases ($\pm 5\text{ bp}$)—to define 198 recurrently mutated sites, of which ~80% involve non-synonymous changes. They cross-check homoplasy calls in 348 samples with matching raw reads in the NCBI Short Read Archive (SRA) and provide a public R Shiny application alongside GitHub repositories for homoplasy filtering and SRA variant calling.

The study provides a useful early genomic snapshot and an accessible interactive tool, and the tMRCA and phylogeographic mixing conclusions are consistent with independent phylodynamic analyses. However, the core evolutionary interpretation of the 198 filtered homoplasies as candidates for ongoing host adaptation is weakened by three methodological limitations: (1) the $p_{nn} > 0.1$ nearest-neighbor filter, designed to remove singleton sequencing errors, actively retains systematic amplicon or bioinformatic errors that artificially group sequences in maximum parsimony trees (exemplified by top candidate site 13,402); (2) the claim that an ~80% non-synonymous fraction among homoplasies indicates positive selection lacks a neutral baseline accounting for the genetic code and the strong $C \to U$ mutational bias of SARS-CoV-2; and (3) several numerical, unit, and denominator errors appear in the main text and tables. These issues can be resolved through computational re-analysis against an explicit neutral mutational null model, primer/protocol artifact screening, and editorial corrections.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **All circulating SARS-CoV-2 sequences share a common ancestor in late 2019 (October 6 – December 11, 2019, 95% CI), ruling out widespread cryptic human circulation long before late 2019: [Well Supported].**  
  The `TreeDater` strict-clock estimate on 7,666 genomes aligns with the root-to-tip regression ($R^2 = 0.20$), low mean pairwise divergence (9.6 SNPs), and independent Bayesian phylodynamic estimates summarized in Table 1. However, keeping the maximum likelihood tree topology fixed during parametric Poisson bootstrapping of branch lengths (Section 2.3) underestimates topological uncertainty.

* **Viral genetic diversity within individual well-sampled countries (e.g., UK, USA, Iceland) recapitulates global clade diversity due to multiple independent introductions: [Well Supported].**  
  The phylogenetic distribution of country-specific isolates across all major clades (Figure 2a–c, Figure S2a) clearly demonstrates repeated seeding of local epidemics rather than single-introduction monophyly.

* **The filtering pipeline isolates 198 genuine evolutionary homoplasies from sequencing and assembly artifacts: [Fragile].**  
  Requiring $>1$ originating/submitting lab and $p_{nn} > 0.1$ removes lab-restricted singletons, and the 348-sample SRA re-calling is a constructive validation step. However, different laboratories share identical amplicon tiling protocols (such as ARTIC primers) and assembly pipelines, producing recurrent systematic errors across multiple labs. Furthermore, when systematic errors occur in low-diversity viral alignments, tree inference algorithms group the affected sequences together, inflating $p_{nn}$ above 0.1. Notably, one of the four highlighted top hits (>15 changes), nucleotide 13,402 (reported in Section 3.3 as introducing/removing a stop codon, `*13402Y`), is a prime candidate for a systematic sequencing or primer-proximal artifact rather than convergent evolution.

* **The ~80% proportion of non-synonymous changes among the 198 recurrent mutations (and >15 events at sites 11,083, 13,402, 16,887, and 21,575) suggests ongoing adaptive evolution in humans: [Overstated].**  
  Because of the structure of the standard genetic code, ~75% of random point mutations in coding regions are non-synonymous under purely neutral evolution without purifying selection. Without comparing the observed 232/290 (80.0%) non-synonymous ratio to a neutral simulation parameterized by the empirical SARS-CoV-2 substitution spectrum (which is heavily skewed toward $C \to U$ transitions driven by host APOBEC-like editing or replication slippage at poly-U tracts such as around 11,083), an 80% non-synonymous fraction cannot be distinguished from neutral mutation accumulation combined with incomplete purifying selection on recent terminal branches.

* **Comparative homoplasy analysis across SARS-CoV-1 ($n=15$) and MERS-CoV ($n=255$) points to shared adaptive hotspots in Orf1ab / Nsp6: [Fragile].**  
  The sample sizes differ by orders of magnitude (15 for SARS-CoV-1, 255 for MERS-CoV, 7,666 for SARS-CoV-2), no quality/artifact filtering was applied to the 350 MERS-CoV homoplasies (where recombination is prevalent, Section 3.3), and no formal statistical test of positional or domain-level enrichment across orthologous coordinates was conducted.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Benchmark Homoplasy Coding Enrichment Against a Mutational-Spectrum Null Model
* **WHY:** Observing that 80% of recurrent changes are non-synonymous does not demonstrate positive selection because random mutations in coronavirus ORFs yield ~75% non-synonymous changes under neutrality, and $C \to U$ hypermutation further skews amino acid replacements toward hydrophobic residues.
* **WHAT:** Test whether the non-synonymous fraction (232/290) and the hydrophilic $\to$ hydrophobic shift (Section 3.3, Figure S10) exceed neutral expectations conditioned on the empirical 12-rate nucleotide substitution matrix of SARS-CoV-2.
* **HOW:** Compute the empirical $4 \times 4$ nucleotide transition frequencies across the 7,666-genome alignment, simulate 1,000 neutral mutation sets across the Wuhan-Hu-1 coding sequence matching the observed site-mutation counts, and calculate two-sided empirical $p$-values for the proportion of non-synonymous mutations and Janin hydrophobicity shifts.

#### 2. Screen Candidate Homoplasies Against Amplicon Primer Sites and Local Sequence Context
* **WHY:** Shared wet-lab protocols (e.g., ARTIC multiplex PCR primers) and homopolymer tracts generate recurrent errors across multiple laboratories that cluster artificially on parsimony trees ($p_{nn} > 0.1$).
* **WHAT:** Annotate all 198 filtered homoplasies (Table S5)—especially the top four sites (11,083, 13,402, 16,887, 21,575) and the two putative stop-codon variants (`*13402Y`, `*26152G`)—for proximity to common amplicon primer binding sites and homopolymer runs.
* **HOW:** Intersect the coordinates of the 198 sites with the ARTIC V1–V3 primer BED files (flagging sites within $\pm 10\text{ bp}$ of primer ends) and flag homopolymer tracts of $\ge 5\text{ bp}$ (such as the poly-U tract adjacent to 11,083). Report how many of the 198 sites remain after masking primer-overlapping positions.

#### 3. Reconcile Numerical Denominators and Correct Rate Units
* **WHY:** Unit errors and unexplained changes in sample denominators confuse readers and hinder verification of the quantitative summaries.
* **WHAT & HOW:** Fix the following specific items in the text and tables:
  1. **Section 3.1 (Line 129):** Correct the substitution rate units from `~6 × 10−4 nucleotides/genome/year (CI: 4 × 10−4 –7 × 10−4)` to `substitutions per site per year` (at 29,903 bp, $6 \times 10^{-4}$ per site per year corresponds to ~18 substitutions per genome per year).
  2. **Table 1 (Line 76):** Correct the Duchene et al. 2020 strict-clock substitution rate point estimate from `1.23 × 10–4` to `1.23 × 10–3`, so that it is consistent with its reported 95% HPD `(5.63 × 10–4, 1.98 × 10–3)`.
  3. **Section 3.3 (Line 157):** Clarify the denominators for the amino acid property breakdown. After stating that 290 amino acid changes comprised 232 non-synonymous and 58 synonymous mutations (and 2 stop-codon changes), the text states *"53 of the remaining 101 non-synonymous mutations... 79 of the remaining 101... 87 of the remaining 110 non-synonymous mutations"*. Explicitly state whether 101 and 110 refer to unique genomic sites or specific ORF subsets rather than total non-synonymous events.
  4. **Section 3.3 (Line 157):** Clarify the notation `*13402Y` and `*26152G`, which mixes nucleotide coordinates (13,402 is in ORF1ab; 26,152 is in ORF3a) with single-letter amino acid/stop symbols; report both the nucleotide substitution and the exact gene/codon coordinate.
  5. **Highlights (Line 15) & Discussion (Line 178):** Fix the typo `COVID-2 pandemic` to `COVID-19 pandemic` (Line 15) and `Extensive genomic resources for SARS-CoV-1 should in principle also be key` to `SARS-CoV-2` (Line 178).
