# Review of ANON_177

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.8 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.5/3.5 | Claims: 1.2/2.5 | Biology: 1.2/2.0 | Reproducibility: 0.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This short communication examines the full-genome genetic relationships of the novel human coronavirus (2019-nCoV; prototype strain `NC_045512`) within the subgenus *Sarbecovirus* and tests for putative recombination. Using a MAFFT full-genome alignment, sliding-window similarity plots (`Simplot v3.5.1`, 450-nt window, 50-nt step), `RDP4`, and fragment-level phylogenetic reconstruction (`PAUP*` neighbor-joining/maximum likelihood under `GTR+G` and `MrBayes v3.2.7`), the authors confirm that 2019-nCoV is most closely related across its genome to `BatCoV RaTG13` (96.3% nucleotide identity; $p$-distance = 0.0369). They further observe that in the 5′ region (positions 1–11,498 of `NC_045512`) and 3′ region (positions 24,341–30,696), 2019-nCoV and `RaTG13` cluster with two bat SARS-like coronaviruses (`MG772933` and `MG772934`), whereas in the central region spanning the 3′ end of ORF1a, ORF1b, and the first half of Spike (positions 11,499–24,340), 2019-nCoV and `RaTG13` form a separate lineage distant from `MG772933`/`MG772934`. No custom scripts, alignment files, or phylogenetic tree files are deposited, though sequence accessions for key strains are cited.

While the basic observation of genome-wide similarity between 2019-nCoV and `RaTG13` and phylogenetic discordance relative to `MG772933`/`MG772934` is empirically accurate, the manuscript's primary conclusion—that 2019-nCoV is "not a mosaic" and that "the hypothesis of emergence of 2019-nCoV as a result of a recent recombination event is rejected"—overreaches what this limited taxon set and coarse sliding-window design can resolve. Discordant clustering between the `(2019-nCoV, RaTG13)` clade and `(MG772933, MG772934)` establishes that recombination occurred among these lineages, but cannot by itself polarize which lineage is the recombinant across all sub-regions or rule out recombination between 2019-nCoV and unsampled sarbecoviruses (particularly within the Spike receptor-binding domain, where `RaTG13` diverges sharply from 2019-nCoV). Furthermore, although `RDP4` is listed in the Methods, zero `RDP4` test statistics, $p$-values, or breakpoint confidence intervals are reported in the Results. Resolving these limitations requires reporting formal recombination test outputs, analyzing ungrouped individual sequences at finer resolution across the Spike gene, and tempering claims regarding the absence of mosaicism.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **2019-nCoV is closely related across its genome to BatCoV RaTG13 (96.3% nucleotide similarity), supporting a bat reservoir origin but indicating RaTG13 is not the immediate progenitor: [Well Supported].**  
  The genome-wide $p$-distance of 0.0369 (~1,100 nucleotide differences across ~29.9 kb) between `NC_045512` and `RaTG13` is accurately calculated and incompatible with direct, immediate spill-over without decades of evolutionary divergence.

* **The (2019-nCoV, RaTG13) clade exhibits discordant phylogenetic clustering relative to bat SARS-like coronaviruses `MG772933` and `MG772934` between the flanking regions (1–11,498; 24,341–30,696) and the central region (11,499–24,340): [Well Supported].**  
  Both the `Simplot` profile (Fig. 1B) and the region-specific ML and Bayesian trees (Fig. 1C) with 100% bootstrap and 1.0 posterior probability support at key nodes demonstrate topological incongruence between the central ORF1ab/S1 fragment and the flanking regions relative to the Zhoushan bat viruses (`MG772933`/`MG772934`).

* **2019-nCoV is "not-mosaic" and the hypothesis that 2019-nCoV emerged via recombination is rejected: [Overstated].**  
  Showing that 2019-nCoV and `RaTG13` co-segregate across three broad genomic blocks (11.5 kb, 12.8 kb, and 6.4 kb) only demonstrates that the breakpoint separating them from `MG772933`/`MG772934` predates the split between 2019-nCoV and `RaTG13` (or occurred in the `MG772933`/`MG772934` ancestor). It does not test for recombination between 2019-nCoV and `RaTG13` (or other sarbecoviruses) within localized regions such as the Spike receptor-binding motif, where sequence identity between 2019-nCoV and `RaTG13` drops substantially in Fig. 1B (~position 21,500–22,500 of the alignment).

* **Formal recombination detection using RDP4 confirms the breakpoint structure and non-mosaic nature of 2019-nCoV: [Methodologically Flawed].**  
  The Abstract and Methods state that putative recombination was investigated using `RDP4` (Martin, 2015), which implements multiple statistical algorithms (`RDP`, `GENECONV`, `BootScan`, `MaxChi`, `Chimaera`, `SiScan`, `3Seq`) to infer breakpoints, major/minor parents, and multiple-testing-corrected $p$-values. However, no `RDP4` results, breakpoint coordinates, parental assignments, or $p$-values appear anywhere in the text, figures, or captions; the boundaries (10,901 and 22,830 in the alignment) appear to have been eye-balled from the `Simplot` curves.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Report Complete RDP4 Statistical Outputs and Parental Polarity Tests
* **WHY:** Claiming that `RDP4` was used to investigate recombination without reporting any of its statistical outputs leaves breakpoint placement and recombinant versus parental polarization unverified.
* **WHAT:** Provide a summary table of all statistically significant recombination events detected by `RDP4` across the sarbecovirus alignment.
* **HOW:** Run the full `RDP4` suite (`RDP`, `GENECONV`, `BootScan`, `MaxChi`, `Chimaera`, `SiScan`, `3Seq`) on the ungrouped alignment, and report for each detected event: the 95% confidence intervals of the beginning and ending breakpoints (in both alignment and `NC_045512` coordinates), the inferred recombinant sequence(s), the inferred major and minor parental lineages, and the Bonferroni-corrected $p$-values for each detection method.

#### 2. Perform High-Resolution Sliding-Window and Sub-Region Phylogenetics Across the Spike Gene
* **WHY:** Grouping reference sequences by clade in `Simplot` and partitioning the genome into only three coarse fragments (1–11,498; 11,499–24,340; 24,341–30,696) splits the Spike gene in half and masks localized divergence between 2019-nCoV and `RaTG13` within the S1 receptor-binding domain (visible as the sharp dip in the `RaTG13` similarity curve around alignment positions 21,000–22,500 in Fig. 1B).
* **WHAT:** Conduct a dedicated sliding-window similarity analysis and phylogenetic tree comparison across the Spike coding region (specifically comparing the N-terminal domain, receptor-binding domain, and S2 subunit) using individual ungrouped sarbecovirus sequences.
* **HOW:** Extract the Spike region (positions 21,563–25,384 in `NC_045512`), run `Simplot` and `BootScan` with a 200–300 nt window and 20 nt step against individual sarbecovirus accessions (rather than averaged group profiles), and reconstruct separate ML trees for the NTD, RBD, and S2 domains to test whether 2019-nCoV and `RaTG13` maintain uniform divergence across Spike.

#### 3. Reframe Conclusions on Mosaicism and Recombination Polarity
* **WHY:** In a three-taxon or four-taxon comparison without a closely related outgroup for every genomic segment, topological discordance between `(2019-nCoV, RaTG13)` and `(MG772933, MG772934)` is symmetric and impacted by incomplete taxon sampling of bat reservoirs.
* **WHAT:** Revise the Abstract, Highlights, and Discussion to distinguish between (a) rejecting recent recombination between `MG772933`/`MG772934` and 2019-nCoV after its divergence from `RaTG13`, and (b) ruling out any mosaic ancestry along the lineage leading to 2019-nCoV.
* **HOW:** Replace the Highlight *"Evidence that the hypothesis of emergence of 2019-nCoV as a result of a recent recombination event is rejected"* and the Abstract claim *"the novel coronavirus (2019-nCov) is not-mosaic"* with precise statements that 2019-nCoV and `RaTG13` share a common ancestral backbone relative to `MG772933`/`MG772934`, while noting that recombination within the `2019-nCoV`/`RaTG13` lineage (or involving unsampled sarbecovirus lineages in the RBD) cannot be excluded without denser sampling of related bat viruses.

#### 4. Provide Complete Sequence Accession Lists and Technical Corrections
* **WHY:** The manuscript does not list the GenBank/GISAID accession numbers of the sequences included in the `Simplot` groups (`Bat_SL_CoV`, `Bat_SARS-like`, `SARS-CoV`), and contains several typographical and software citation errors that hinder reproducibility.
* **WHAT & HOW:**
  1. Add a table or supplementary list of all viral sequences and accession numbers used in Fig. 1 and Fig. 2, specifying which accessions were collapsed into each colored group in Fig. 1B.
  2. Correct the software version in the Methods (line 53): `"MEGA v1.0 (Stecher et al., 2020)"` should be `"MEGA X (Stecher et al., 2020)"`.
  3. Correct the truncated accession number in the Fig. 2 caption (line 67): change `"NC_0455_Wuhan_Hu_1"` to `"NC_045512 (Wuhan-Hu-1)"`.
  4. Fix the double preposition in Results (line 55): change `"Specifically in in the 5′-part"` to `"Specifically, in the 5′-part"` and standardize `"2019-nCov"` (line 26) to `"2019-nCoV"`.
