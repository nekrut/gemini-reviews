# Review of ANON_104

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.2 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.2/3.5 | Claims: 2.3/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces ExtRaINSIGHT, a maximum-likelihood framework that estimates the prevalence of strong purifying selection ("ultraselection," parameterized by $\lambda_s$) across coding and noncoding genomic elements by measuring the fractional depletion of rare variants ($\text{MAF} < 0.001$) in 71,702 whole genomes from gnomAD v3 relative to interspersed putatively neutral sequences. To control for mutation rate heterogeneity, the authors construct a linear-logistic mutational model conditioning on heptanucleotide sequence context ($3\text{ bp}$ flanking each side), local G+C content, CpG islands, sequencing depth, and a 150 kb sliding-window regional scaling factor, excluding CpG dinucleotides. Contrasting $\lambda_s$ with divergence-scale selection ($\rho$ from INSIGHT2), they find strong rare-variant depletion in splice sites ($\lambda_s = 0.45$, $s_{\text{het}} \approx 0.02$), evolutionarily conserved miRNAs ($\lambda_s = 0.34$; seed regions $\lambda_s = 0.39$), 0-fold degenerate coding sites ($\lambda_s = 0.22$), and neuronal genes ($\lambda_s = 0.27$), but modest ultraselection in ultraconserved noncoding elements (UCNEs, $\lambda_s = 0.09$) and near-zero levels in most other noncoding RNAs and transcription factor binding sites (TFBSs). Genome-wide accounting estimates that $0.37\%$–$0.73\%$ of the human genome is ultraselected, corresponding to $0.26$–$0.51$ strongly deleterious de novo mutations per diploid zygote. Source code, key data files, and a web server are publicly available.

This is a rigorous, transparent contribution to human population genetics. The analytical derivations of the closed-form unbiased estimator $\hat{\lambda}_s$, its variance, and its harmonic-mean relationship to $s_{\text{het}}$ under mutation–selection balance are sound, and the authors' forthright investigation of local mutation-model misspecification in 5' UTRs, promoters, and TFBSs is exemplary. A few methodological nuances—specifically the extrapolation of non-CpG $\lambda_s$ estimates to CpG-inclusive genome-wide mutation counts, multi-ancestry sample structure in gnomAD v3 versus single-population European simulations, and minor numerical discrepancies between the main text and Tables 1–2—can be addressed through targeted text and table revisions.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Splice sites ($\lambda_s = 0.45$), ancient miRNAs ($\lambda_s = 0.34$), and 0-fold degenerate coding sites ($\lambda_s = 0.22$) experience substantial ultraselection, whereas young miRNAs, lncRNAs, snoRNAs, snRNAs, and 4-fold degenerate sites ($\lambda_s = -0.008$) do not: [Well Supported].**  
  The contrast between 0d and 4d sites, the monotonic scaling of $\lambda_s$ across LOEUF deciles ($\lambda_s = 0.28$ to $0.008$; Figure 1B), and the independent validation of the background mutation model against 174,122 de novo mutations (Supplementary Figure 3) provide strong internal validation.

* **Ultraconserved noncoding elements (UCNEs) exhibit only modest ultraselection ($\lambda_s = 0.09$), indicating that their extreme cross-species conservation reflects spatially uniform intermediate purifying selection ($s_{\text{het}} \approx 0.003$–$0.005$) rather than pervasive lethality: [Well Supported].**  
  This result reconciles long-standing experimental observations (viability of UCNE knockout mice and enhancer resilience to mutagenesis) with evolutionary conservation, and is backed by forward demographic simulations in Supplementary Figure 8.

* **Approximately 0.4–0.7% of the human genome is ultraselected, yielding 0.26–0.51 strongly deleterious mutations per potential zygote: [Moderately Supported].**  
  While the two background-subtraction baselines (nonconserved introns $\lambda_s = 0.009$ in Table 1 vs. nonconserved intergenic $\lambda_s = 0.003$ in Supplementary Table 1) bracket the range well, two assumptions affect the exact mutation burden: (i) CpG sites are excluded when estimating $\lambda_s$, yet Table 1 multiplies $\lambda_s$ by the total site count (`2875.1M`) and the genome-wide average mutation rate ($\mu = 1.2 \times 10^{-8}$, which includes hypermutable CpGs); and (ii) clamping negative $\lambda_s$ in 5' UTRs/promoters to zero ignores ultraselected sites in those elements that are masked by elevated local mutation rates.

* **Negative $\lambda_s$ estimates in 5' UTRs ($\lambda_s = -0.16$) and core promoters ($\lambda_s = -0.13$) reflect localized mutation-model misspecification, driven in part by mutagenic effects of transcription factor binding ($p = 2.8 \times 10^{-13}$): [Well Supported].**  
  The window-based spatial decay analysis (Figure 3B), ChromHMM covariate tests, and the paired comparison of Ensembl TFBSs against their immediate 10 bp flanks within extended promoters (Figure 3C) thoroughly isolate the phenomenon and prevent false biological claims.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Account for CpG Exclusion When Extrapolating Genome-Wide Deleterious Mutation Rates
* **WHY:** ExtRaINSIGHT excludes all CpG dinucleotides during estimation (`Methods`, line 15), but Table 1 and Table 2 multiply the non-CpG $\lambda_s$ and $\rho$ estimates by total genomic site counts and the overall per-nucleotide mutation rate ($\mu = 1.2 \times 10^{-8}$). Because CpG transitions occur at $\sim 10\times$ the non-CpG rate and are enriched in coding exons and 5' regions, assuming identical $\lambda_s$ and uniform $\mu$ across CpG and non-CpG sites can bias category-specific mutation load estimates (`exp. s-del.`).
* **WHAT:** Clarify in the Methods and Table 1 footnotes whether `no. sites (M)` includes CpG sites, and provide a sensitivity calculation separating non-CpG sites ($\mu_{\text{non-CpG}} \approx 0.85 \times 10^{-8}$) from CpG sites (or explicitly state the invariance assumption required to extrapolate $\lambda_s$ to CpGs).
* **HOW:** Compute the fraction of CpG dinucleotides in each of the 10 genomic partitions in Table 1; using published gnomAD CpG vs. non-CpG mutation rates, report how the $0.26$–$0.51$ strongly deleterious mutations/zygote estimate changes if CpG sites in CDS and splice sites experience the same $\lambda_s$ at their elevated mutation rate.

#### 2. Assess Multi-Ancestry Sample Composition on the $\lambda_s$–$s_{\text{het}}$ Calibration
* **WHY:** The forward simulations calibrating Equation (12) ($s_{\text{het}} \approx \frac{2N/c}{1 - \lambda_s}$) simulate $N = 71,702$ diploids from a single panmictic European demographic history (`Methods`, line 184). However, gnomAD v3 ($N = 71,702$) is a multi-ancestry cohort ($\sim 52\%$ European, $\sim 29\%$ African/African-American, plus Admixed American and Asian samples), where population structure and higher African $N_e$ increase the number of distinct rare variants ($\text{MAF} < 0.001$) discovered at neutral sites ($\bar{P} = 0.162$) while strongly deleterious alleles at mutation–selection balance ($s_{\text{het}} \ge 0.02$) remain confined to recent lineages within each subpopulation.
* **WHAT:** Discuss how multi-ancestry pooling in gnomAD v3 affects $c = \bar{P}/\mu$ relative to a single European population, or check Equation (12) in a two-population (African + European) demographic simulation.
* **HOW:** Compare the empirical neutral rare-variant probability $\bar{P} = 0.162$ in gnomAD v3 against the simulated single-population European $\bar{P}$ (noted in `Methods` line 184 as "similar, but not identical"), and note in the section *Relationship between $s_{\text{het}}$ and $\lambda_s$* that empirically plug-in $c = \bar{P}_{\text{obs}}/\mu$ automatically absorbs demographic inflation of neutral polymorphism, whereas the MAF $< 0.001$ cutoff pooled across ancestries slightly alters the rare-variant boundary for moderate $s_{\text{het}}$.

#### 3. Reconcile Numerical Discrepancies Between Main Text and Tables 1–2
* **WHY:** Several numbers and footnotes in the genome-wide accounting section do not match the values printed in Tables 1 and 2.
* **WHAT & HOW:**
  * **Results (line 132) vs. Table 1 (`exp. prop.` column):** Line 132 states "with 44% of ultraselected sites falling in CDSs, 13% in conserved introns, 11% in conserved intergenic regions, 12% in conserved lncRNAs, 5% in 3' UTRs and 3% in splice sites" (which sums to 88%), and line 134 states "23% from introns." In Table 1, the actual values in column `exp. prop.` are `43.5%` (CDS), `20.1%` (conserved intron), `17.0%` (conserved intergenic), `9.8%` (conserved lncRNA), `6.2%` (3' UTR), and `3.3%` (splice), which sum to `100.0%`. Update lines 132 and 134 to match Table 1.
  * **Table 2 Footnote `a` (line 162):** Footnote `a` states "the estimate for nonconserved introns (0.022) was subtracted from each estimate of $\rho$." In Table 2 (line 155), `0.022` is the *standard error* (`± stderr`), whereas the point estimate for nonconserved introns is `0.042` (and $0.042$ is the number that was actually subtracted to compute `exp. no. (M)` in Table 2, e.g., $(0.624 - 0.042) \times 33.8 = 19.7$). Change `(0.022)` to `(0.042)`.
  * **Table 1 Footnote `a` (line 120):** Footnote `a` ("The similar values of the standard errors (equal after rounding) reflect the maximum of 1M sites used for estimation") is attached to Table 1 (where standard errors range 12-fold from `0.0001` to `0.0012` and all sites were used), whereas 1M-site subsampling and nearly identical standard errors (`~0.020`) actually apply to INSIGHT in **Table 2** (`Methods` line 170). Move or clarify this footnote in Table 2.
  * **Discussion (chunk 2, line 3):** Change "the difference $\lambda_s - \rho$ as a measure of selection that is weaker" to "$\rho - \lambda_s$" (since $\rho > \lambda_s$).
  * **Methods (chunk 2, line 149):** "provides an explanation for the downward bias observed in Supplementary Fig. 1" should reference **Supplementary Fig. 6** (where the variable-$s_{\text{het}}$ simulations are plotted), not Supplementary Fig. 1 (mutation model calibration).
