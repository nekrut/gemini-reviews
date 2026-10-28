# Review of PMC12732342 (PMID:41465100)

**Manuscript Title:** Characterization of the Mitochondrial Genome of &lt;i&gt;Cavariella salicicola&lt;/i&gt;: Insight into the Codon Usage Bias and Phylogenetic Implications in Aphidinae  
**Authors:** Jing TX, Zhang YJ, Li PX, Wang Q, Yang J, Su HH, Zhang S.  
**Journal / Preprint:** *Genes (Basel)* (2025; `PMC12732342` / `PMID:41465100` / `10.3390/genes16121427`)  
**Calibration Study Cohort:** Cohort C — Wild Literature Sample (`C55` | Double-Blinded as `ANON_153`)  
**Overall Score:** **5.4 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.5/3.5 | Claims: 1.3/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.3/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript reports the sequencing, assembly, and annotation of the complete mitochondrial genome of the aphid *Cavariella salicicola* (15,720 bp; GenBank accession PV837988) collected from *Oenanthe javanica* in Yangzhou, China, alongside a comparative annotation of *C. theobaldi* extracted from public whole-genome data (OZ060905.1). The authors characterize gene organization, nucleotide skew, amino acid composition, relative synonymous codon usage (RSCU), effective number of codons (ENc), Parity Rule 2 (PR2), neutrality plots (GC12 vs. GC3), sliding-window nucleotide diversity ($\pi$), and pairwise $K_a/K_s$ across 38 aphid mitogenomes. Finally, they reconstruct Maximum Likelihood (IQ-TREE) and Bayesian Inference (MrBayes) phylogenies across 57 aphid mitogenomes (13 protein-coding genes and 2 rRNAs partitioned into 41 blocks), resolving *Cavariella* as a monophyletic sister group to the remaining sampled species of the tribe Macrosiphini.

While the newly sequenced mitogenome is a useful resource for hemipteran systematics and the core phylogenetic placement of *Cavariella* basal to other sampled Macrosiphini is consistent across ML and BI methods, the manuscript suffers from multiple methodological flaws and internal numerical contradictions. Specifically, the conclusion that codon usage bias is driven primarily by natural selection rather than mutational pressure is an artifact of applying nuclear genetic code tools and neutral expectation curves to short, extreme AT-rich (83.8% AT; 93.3% AT at third codon positions) mitochondrial genes. Furthermore, the phylogenetic taxon sampling omits the genus *Pterocomma* despite framing the *Cavariella*–*Pterocomma* hypothesis as a primary motivation in the Introduction, and there are numerous discrepancies between the main text and Tables 1–2 regarding start/stop codons, gene overlaps, strand assignments, and region lengths. Resolving these issues requires computational re-analysis of codon usage and evolutionary rates, taxon-sampling caveats, and careful table reconciliation.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The *C. salicicola* mitogenome is a 15,720 bp circular molecule with 37 standard genes, conserved Aphidinae synteny, and population-level repeat polymorphism in the control and repeat regions: [Moderately Supported].**  
  The assembly is supported by Illumina sequencing and comparison with *C. theobaldi* and a previously sequenced Gansu population of *C. salicicola* (`NC_022682.1`). However, internal numerical inconsistencies undermine confidence in the exact annotation coordinates: Table 1 and Table 2 report the repeat region as 274 bp (positions 6096–6369), whereas Section 3.6 (line 225) states it is "280 bp" and comprises "two copies of a 106 bp tandem unit separated by a 93 bp spacer sequence" ($106 \times 2 + 93 = 305\text{ bp}$). Similarly, `rrnS` is reported as 776 bp in Table 1 and Section 3.5, but 765 bp in Table 2; Section 3.1 (line 73) lists 10 tRNA names (`His` and `Pro` are duplicated) while stating there are "eight tRNAs" on the N strand; and Section 3.3 (line 166) states that `cox2` and `atp6` initiate with `ATA`, contradicting Table 1 where both are listed as `ATT`.

* **Codon usage bias in *Cavariella* mitochondrial protein-coding genes is predominantly shaped by natural selection rather than mutational pressure: [Methodologically Flawed].**  
  The authors base this claim on three plots (ENc vs. GC3s, PR2, and GC12 vs. GC3 neutrality plots; Section 3.4, Figure 4). First, CodonW v1.3 and EMBOSS CUSP default to the standard nuclear genetic code unless configured for the invertebrate mitochondrial code (where `UGA` encodes Trp, `AUA` encodes Met, and `AGA`/`AGG` encode Ser), and Wright's (1990) expected ENc curve assumes 61 sense codons and equal A/T and G/C frequencies. Second, mitochondrial PCGs are short (e.g., *atp8* is 52 codons, *nad4l* is 96 codons, *nad3* is 117 codons), where finite-sample stochasticity and missing synonymous codon families artificially depress ENc below the theoretical curve. Third, when third-codon positions are 93.3% AT (GC3 restricted to a narrow 3.5%–10.2% band across $n=13$ genes), linear regression of GC12 on GC3 has virtually zero horizontal variance, guaranteeing a near-zero slope ($R^2 = 0.0009$ and $0.0137$) even under pure mutational and replication-strand skew pressure.

* **Differences in the proportions of Phe, Trp, and Tyr between *C. salicicola* and *C. theobaldi* imply distinct metabolic loads and stress resource allocation strategies: [Overstated].**  
  In Section 3.3 (line 168), the authors leap from minor compositional differences in aromatic amino acids encoded by AT-rich codons (e.g., `UUU` for Phe, `UAU` for Tyr, `UGA` for Trp) between two mitogenomes to an ecological claim about metabolic load and stress allocation without any physiological measurements, expression data, or statistical testing against neutral compositional drift.

* **All 13 mitochondrial PCGs across 38 Aphidinae species evolve under purifying selection ($K_a/K_s < 1$), with *atp8* showing the highest evolutionary rate: [Moderately Supported].**  
  While strong purifying selection on core mitochondrial subunits (`cox1`, `cox2`, `cytb`) and relaxed constraint on *atp8* are standard across insects, the authors compute $K_a/K_s$ in DnaSP v6.0 across 38 species using pairwise Nei–Gojobori distances (Section 2.3). Pairwise comparisons across a 38-taxon tree treat $\binom{38}{2} = 703$ phylogenetically non-independent pairs as independent observations and fail to correct for extreme AT compositional bias and synonymous substitution saturation ($K_s$) across divergent tribes.

* ***Cavariella* is monophyletic and forms a sister group to all other sampled Macrosiphini species: [Moderately Supported].**  
  Both ML and BI trees recover `C. salicicola + C. theobaldi` as sister to the remaining sampled Macrosiphini with high support (Figures 7–8). However, the Introduction frames the central taxonomic controversy around whether *Cavariella* clusters with *Pterocomma* (Pterocommatinae), yet no *Pterocomma* sequences are included in the 57-taxon dataset. Additionally, third codon positions (93.3% AT) were included in the supermatrix without testing for substitution saturation or compositional heterogeneity.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Re-evaluate Codon Usage Bias Accounting for the Invertebrate Mitochondrial Code and Strand Skew
* **WHY:** Wright's standard ENc curve and unweighted GC12–GC3 regressions do not account for the invertebrate mitochondrial genetic code (Code 5), extreme AT mutational bias (93.3% AT at third positions),replication-driven strand asymmetry (J vs. N strand), or small gene length (52–573 codons).
* **WHAT:** Recompute ENc and RSCU explicitly under NCBI Translation Table 5, separate J-strand and N-strand genes in the PR2 analysis, and replace the uncalibrated "natural selection dominates" claim with an assessment of mutational AT bias and strand-specific replication skew.
* **HOW:** Use a codon usage tool that supports Translation Table 5 (e.g., `vhcub` or custom R/Python scripts using `Biopython`) to compute $\text{ENc}$ and its compositional expectation under empirical nucleotide frequencies (e.g., Sun et al. 2013 improved $\text{ENc}$ formula), and perform a permutation simulation shuffling third-codon bases within each gene to generate an empirical 95% null envelope on the ENc–GC3s plot.

#### 2. Use Phylogeny-Aware Codon Models Instead of Pairwise DnaSP Estimates for $K_a/K_s$
* **WHY:** DnaSP computes unweighted Nei–Gojobori pairwise distances, ignoring phylogenetic non-independence across the 38 species and underestimating $K_s$ in highly AT-biased, saturated mitochondrial alignments.
* **WHAT:** Estimate lineage-wide $\omega$ ($d_N/d_S$) for each of the 13 PCGs using maximum-likelihood codon models along the inferred phylogeny.
* **HOW:** Run `codeml` (PAML, Model M0 with `icode = 4` for invertebrate mitochondrial code and `CodonFreq = 2` or `3` to account for extreme base composition) or HyPhy (`FitMG94`) on each of the 13 aligned PCGs (after excluding frameshifted annotations in *Schizaphis graminum* and *Hormaphis betulae*), and report tree-based $\omega$ alongside 95% confidence intervals.

#### 3. Test for Third-Codon Position Saturation and Clarify Taxon Sampling Limits in Phylogenetics
* **WHY:** Including 93.3% AT third codon positions across 57 species spanning multiple subfamilies risks long-branch attraction and compositional artifacts, and the absence of *Pterocomma* prevents testing the *Cavariella*–*Pterocomma* sister hypothesis discussed in the Introduction and Section 3.7.
* **WHAT:** Perform substitution saturation tests on each codon position and run a sensitivity phylogeny excluding third codon positions (PCG12 + rRNAs) or using amino acid sequences. Explicitly state in the Abstract and Discussion that *Pterocomma* could not be tested due to lack of complete mitogenome data.
* **HOW:** Run Xia's saturation test in DAMBE (or compute $R^2$ of uncorrected $p$-distance vs. patristic ML distance for 1st, 2nd, and 3rd codon positions), and run IQ-TREE on the PCG12+rRNA matrix and under site-heterogeneous protein models (`MtArt+F+I+G4` or `C20`) to verify that the basal placement of *Cavariella* within Macrosiphini holds.

#### 4. Temper Adaptive Storytelling on Amino Acid Composition
* **WHY:** Attributing a slightly higher count of Phe, Trp, and Tyr in *C. salicicola* vs. *C. theobaldi* to "distinct metabolic loads and resource allocation strategies... when under stress" (Section 3.3, line 168) has no empirical or statistical support.
* **WHAT:** Remove the speculative metabolic stress claim and test whether amino acid frequency differences between *C. salicicola* and *C. theobaldi* exceed neutral expectations given their overall AT content (83.8% vs. *C. theobaldi*).
* **HOW:** Perform a $\chi^2$ or Fisher's exact test on the $20 \times 2$ amino acid count contingency table between *C. salicicola* and *C. theobaldi* (Table S3) and revise lines 168–169 to report whether any difference is statistically significant.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Multiple contradictions between the text and tables compromise the reliability of the genome annotation.
* **WHAT & HOW:**
  * **Section 2.2 (Line 32):** Clarify why contigs were mapped against *Aphis gossypii* (`NC_024581`) rather than the conspecific *C. salicicola* Gansu reference mitogenome (`NC_022682.1`, cited in Section 3.6, line 225).
  * **Section 3.1 (Line 73):** Fix the N-strand tRNA list `(tRNA-Cys, Gln, His, Leu, Tyr, Phe, Pro, His, Pro, and Val)`, which duplicates `His` and `Pro` and omits the `Leu1` designator. Cross-check against Table 1 (`tRNA-Gln`, `Cys`, `Tyr`, `Phe`, `His`, `Pro`, `Leu1`, `Val` = 8 tRNAs).
  * **Table 1 vs. Section 3.3 (Line 166):** Reconcile start and stop codons. Line 166 states five genes (`cox1`, `cox2`, `atp6`, `nad3`, `nad2`) use `ATA`, whereas Table 1 lists `ATT` for `cox2` (line 93) and `atp6` (line 97). Line 166 also states "most PCGs use a complete TAA stop codon. However, cox1, nad2, nad4, and cytb terminate with an incomplete single 'T' residue," omitting `cox3`, which is listed with stop codon `TA` in Table 1 (line 98).
  * **Table 1 (Lines 97–98):** `atp6` ends at 4571 and `cox3` starts at 4571, which is a 1 bp overlap (`-1`), not `0` in the Intergenic column. Verify all intergenic/overlap arithmetic across Table 1.
  * **Table 1 & Table 2 vs. Section 3.5 & Section 3.6:** Reconcile `rrnS` length (`776 bp` in Table 1 line 121 and Section 3.5 line 204 vs. `765 bp` in Table 2 line 158) and Repeat region length (`274 bp` in Table 1 line 106 and Table 2 line 160 vs. `280 bp` in Section 3.6 line 225, where $2 \times 106 + 93 = 305\text{ bp}$).
  * **Section 3.5 (Line 204):** Fix the malformed GenBank accession `NC_043903.11` for *A. citricidus* (should be `NC_043903.1`).
  * **Supplementary Materials (Line 259):** Fix typo `C. theobald` to `C. theobaldi`.
