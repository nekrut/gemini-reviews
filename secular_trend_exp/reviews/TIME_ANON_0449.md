<Blinded Review: TIME_ANON_0449>
**Composite Score:** 7.8 / 10.0 (Rigor: 2.7/3.5 | Claims: 2.1/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Translational/Preclinical/Biomarker

OVERALL_SCORE: 7.8/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary (SUMMARY)
This study integrates targeted methylated DNA immunoprecipitation tiling arrays (MeDIP-chip; NimbleGen 385k covering >21 Mb across 122 T2D/obesity GWAS, monogenic, and imprinted regions) with Bayesian methylation deconvolution (`BATMAN` in 100-bp windows) in peripheral blood DNA from 60 women (30 T2D cases, 30 controls), followed by bisulfite pyrosequencing validation in 80 blood samples and 14 post-mortem human brain samples (4 hypothalamus, 10 prefrontal cortex). Testing 15 T2D/obesity GWAS LD blocks for genotype-dependent methylation, the authors identify a significant haplotype-specific methylation (HSM) increase on the *FTO* intron 1 obesity-risk haplotype tagged by `rs8050136` A ($p = 9.40 \times 10^{-4}$; 10,000-permutation $p = 1.0 \times 10^{-3}$), which peaks in a 7.7-kb window ($p = 1.13 \times 10^{-7}$) and a 900-bp sub-peak ($p = 1.94 \times 10^{-5}$) adjacent to an H3K4me1-marked long-range enhancer (HCNE element 6 targeting *IRX3*). Crucially, rather than over-claiming trans-acting epigenetic reprogramming, the authors dissect the sequence architecture and prove via bisulfite pyrosequencing that the MeDIP signal is directly driven by three in-phase CpG-creating SNPs (`rs7206629`, `rs7202116`, `rs7202296`) on the risk haplotype that increase the number of methylatable CpG sites from 7 to 10 in the 900-bp window without altering methylation of neighboring non-polymorphic CpGs. This is a self-correcting, mechanistically transparent study, with minor statistical caveats regarding unadjusted multi-scale sliding-window $p$-values.

### 2. Methodological & Statistical Audit (STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT)
#### Strengths
* **Rigorous Dissection of Genetic vs. Epigenetic Confounding via Pyrosequencing:** A major pitfall of array-based MeDIP/BATMAN studies is that reference-genome CpG density normalization cannot account for polymorphic CpG-creating SNPs (`YpG`/`CpR`). Instead of stopping at the array association, the authors sequenced the underlying region by bisulfite pyrosequencing in $N=80$ blood and $N=14$ brain samples, demonstrating that `rs7202296` is $98.6\%$ methylated when genetically CpG (`AA` risk homozygotes) vs. $11.5\%$ background in `CC` homozygotes, while adjacent non-SNP CpGs (`52379221`, `52379251`, `52379254`) are invariant across genotypes (Table 5).
* **Transparent Reporting of Negative Results:** The authors explicitly report that: (i) the case-control comparison (30 T2D vs. 30 non-T2D) yielded zero differentially methylated regions (DMRs) after FDR correction; (ii) 14 of 15 T2D GWAS LD blocks showed no block-wide haplotype methylation effect; (iii) non-SNP CpGs showed no *cis* allele-specific methylation (hepitype spreading); (iv) *FTO* and *IRX3* showed no detectable eQTL/ASE effect in HapMap CEU LCLs or 6 cerebellum RNA-seq samples; and (v) iHS/XP-EHH showed no recent positive selection sweep.
* **Appropriate Sex and Age Controls:** Restricting the discovery cohort to 60 females eliminated X-inactivation and sex-specific autosomal methylation confounding, and age was explicitly tested and excluded as a confounder ($p = 0.676$ for the 46-kb block; $p = 0.444$ for the 7.7-kb window).

#### Weaknesses & Methodological Audit
* **Multiple-Testing Inflation in the Exhaustive Multi-Scale Sliding-Window Scan:** To localize the peak within the 46-kb *FTO* LD block (334 BATMAN windows of 100 bp), the authors tested all possible window sizes from $w=1$ to $w=334$ sliding one window at a time—roughly $334 \times 335 / 2 \approx 55,945$ correlated tests—and reported the minimum nominal linear regression $p$-value ($p = 1.13 \times 10^{-7}$ or $1.33 \times 10^{-7}$ at window size 60) and point-wise 10,000-permutation $p < 1 \times 10^{-5}$ without adjusting for the massive search over all $(w, \text{start})$ pairs. While the block-level test ($p = 9.40 \times 10^{-4}$ across 15 tested LD blocks, Bonferroni $\alpha = 0.05/15 = 0.0033$) and independent pyrosequencing validation confirm the biological signal, the $10^{-7}$ sliding-window $p$-value suffers from look-elsewhere ("winner's curse") inflation.
* **BATMAN Reference-Genome Bias Not Re-Fitted with Genotype-Specific CpG Coupling:** As the authors note in the Discussion, `BATMAN` estimates absolute methylation by dividing MeDIP IP/input log-ratios by a local CpG coupling factor computed from the hg18 reference genome (which carries only 7 CpGs in the 900-bp window). Because `AA` risk homozygotes actually carry 10 physical CpGs in that 900-bp window (a $43\%$ higher CpG density than hg18), `BATMAN` systematically overestimates per-CpG fractional methylation on the `AA` haplotype when physical CpG count increases.
* **Minor Numerical Discrepancies in Text vs. Table 2 and Subject Counts:**
  1. For the 7.7-kb broad peak linear regression $p$-value, Abstract and Table 2 report `$1.13 \times 10^{-7}$` (`1.133×10⁻⁷`), whereas the Results text (line 72) and Figure 4 legend report `$1.33 \times 10^{-7}$`.
  2. In Results (line 53), the non-risk allele of `rs8050136` is referred to as "G homozygotes with 0.497", whereas in Table 2 and Figure 4 it is correctly labeled `CC` (an A/C SNP).
  3. Line 129 has a typo in the SNP ID `rs7202996` (should be `rs7202296`).

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim 1: The *FTO* obesity/T2D risk haplotype exhibits higher aggregate DNA methylation capacity in a 7.7-kb / 900-bp intronic region driven by in-phase CpG-creating SNPs (`rs7206629`, `rs7202116`, `rs7202296`) `[Well Supported]`.** Directly demonstrated by MeDIP-chip across 60 samples and validated at single-base resolution by bisulfite pyrosequencing in 80 blood and 14 brain samples.
* **Claim 2: The CpG-creating SNPs do not induce *cis*-spreading of differential methylation to adjacent non-polymorphic CpGs `[Well Supported]`.** Table 5 and text values for nine neighboring non-SNP CpGs show virtually identical methylation across `AA`, `AC`, and `CC` genotypes in both blood and brain.
* **Claim 3: Haplotype-specific methylation in the 7.7-kb region modulates enhancer activity regulating *IRX3* or *FTO* expression `[Fragile]`.** Presented appropriately as a functional hypothesis in the Discussion; the region overlaps an H3K4me1 mark and a published zebrafish enhancer (HCNE 6), but the authors' own eQTL and cerebellum RNA-seq analyses found no expression differences.

### 4. Reproducibility & Data Completeness
* **Public Repository Deposition:** Raw and normalized NimbleGen MeDIP-chip array data for all 60 subjects are deposited in NCBI GEO under accession `GSE20553`, and exact hg18 genomic coordinates are provided for all LD blocks, peaks, and pyrosequenced CpGs. Pyrosequencing primer sequences and custom R/Perl scripts are stated as available upon request.
</Blinded Review: TIME_ANON_0449>
