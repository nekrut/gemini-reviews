# Review of ANON_39

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.3 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.1/3.5 | Claims: 0.9/2.5 | Biology: 1.0/2.0 | Reproducibility: 1.3/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript analyzes 137 complete SARS-CoV-2 genomes downloaded from GISAID as of February 23, 2020, alongside related bat (`RaTG13`, `ZC45`, `ZXC21`, `GX2013`, `HKU3-1`) and pangolin (`Pangolin_2019`, `Pangolin_2017`) sarbecoviruses. The authors compute pairwise $dN$ and $dS$ across coding regions, construct a median-joining haplotype network (`Network 10`) to re-polarize the site frequency spectrum (correcting outgroup polarization errors caused by recurrent $C \to T$ transitions along the branch to `RaTG13`), estimate $dN/dS$ across two epidemic periods split at January 21/22, 2020 (around the January 23 Wuhan lockdown), and run a BEAST v1.10.4 uncorrelated lognormal relaxed-clock Bayesian skyline analysis (estimating a substitution rate of $2.4 \times 10^{-3}\text{ subs/site/year}$ and a tMRCA of December 11, 2019; 95% HPD: November 13 – December 23, 2019). From these analyses, the authors conclude that the Spike receptor-binding domain (RBD) similarity between SARS-CoV-2 and `Pangolin_2019` reflects an ancient intergenomic introgression ~40 years ago, that SARS-CoV-2 shows relaxation of selection rather than positive adaptation, that the Wuhan lockdown halted viral effective population size ($N_e$) growth and drove frequency shifts of `ORF8 L84S` and `ORF3a G251V`, and that *"SARS-CoV-2 might have cryptically circulated within humans for years before being discovered."*

While the manuscript makes a valid methodological point regarding outgroup mispolarization of the site frequency spectrum when using a divergent outgroup (`RaTG13`, $dS = 0.168$) in the presence of strong $C \to T$ transition bias (Figure 1a vs. 1b), its major evolutionary and epidemiological conclusions are undermined by internal contradictions, algebraic fallacies, and severe spatio-temporal sampling confounding: (1) the claim that SARS-CoV-2 cryptically circulated in humans for years directly contradicts the authors' own BEAST tMRCA estimate of December 11, 2019 (95% HPD: November 13 – December 23, 2019) and singleton-dominated site frequency spectrum ($\theta = 13.92 \times 10^{-4}$ vs. $\pi = 1.81 \times 10^{-4}$); (2) the equation used to date the RBD introgression to ~40 years ago (`t = dS / (rate × 2 × 3)`) circularly divides the RBD $dS$ by 3 simply because RBD $dS$ is 3-fold higher than the genome average; (3) the claim of strong positive selection on `orf8` ($dN/dS = 9.57$) and `orf3` ($dN/dS = 2.68$) in Table 3 relies on an invalid ad-hoc substitution of genome-wide $dS$ when gene-specific $dS = 0$; and (4) attributing the BEAST skyline plateau and `L84S`/`G251V` frequency shifts to the January 23 Wuhan lockdown ignores that all 24 Wuhan genomes in the dataset were sampled before January 5, 2020.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Outgroup polarization using `RaTG13` creates an artificial excess of high-frequency derived synonymous variants due to multiple hits and $C \to T$ transition bias; network-based polarization reveals a singleton-dominated spectrum consistent with recent expansion: [Well Supported].**  
  Cross-referencing the 29 non-singleton polymorphisms in Table 2 against the median-joining haplotype network (Figure 2) and phylogeny demonstrates that apparent high-frequency derived alleles under `RaTG13` outgroup rooting (such as `C10138T` restricted to 3 February 2020 Singapore isolates, or `L84S` at 28,144 alongside `T8782C`) are recent derived or homoplastic changes, yielding an L-shaped frequency spectrum (Figure 1b) and an 8-fold excess of Watterson's $\theta$ over $\pi$ (Table 4).

* **SARS-CoV-2 might have cryptically circulated within humans for years before December 2019: [Methodologically Flawed].**  
  This headline conclusion in the Abstract, Discussion (lines 274–276), and Conclusion (line 289) is directly refuted by the manuscript's own results. If SARS-CoV-2 had circulated in humans for years prior to December 2019, human isolates would harbor deep coalescent branches, high pairwise nucleotide diversity ($\pi$), and a pre-2019 tMRCA. Instead, the authors' BEAST analysis dates the tMRCA of all 137 human genomes to December 11, 2019 (95% HPD: November 13 – December 23, 2019; line 233), with $\pi = 1.81 \times 10^{-4}$ (~5 nucleotide differences per genome). Even if ancestral recombination in the RBD occurred decades ago among bat/pangolin reservoirs and purifying selection maintained the RBD amino acid sequence in animal hosts, that wildlife evolutionary history provides zero evidence for cryptic multi-year circulation in humans.

* **The RBD sequence similarity between SARS-CoV-2 and `Pangolin_2019` resulted from an ancient intergenomic introgression approximately 40 years ago (95% HPD: 31–69 years): [Methodologically Flawed].**  
  In the Discussion (line 274), the authors write: *"Assuming a synonymous substitution rate of $2.9 \times 10^{-3}\text{/site/year}$, the recombination was estimated to have occurred approximately 40 years ago (95% HPD: 31–69 years; divergence time (t) = divergence (dS)/(substitution rate × 2 × 3), considering dS in RBD is 3-fold of genome average)."* Because $dS$ in the RBD between SARS-CoV-2 and `Pangolin_2019` is 0.710 (~3-fold higher than the genome-wide SARS-CoV-2 vs. `RaTG13` average of 0.168, and higher than the rest of the Spike gene at 0.651; Table 1), dividing $dS$ by an arbitrary factor of 3 simply erases the elevated RBD synonymous divergence (`0.710 / (2.9e-3 × 2 × 3) = 40.8 years`, whereas the standard molecular clock formula $t = dS / (2\mu)$ gives `0.710 / (2 × 2.9e-3) = 122.4 years`). Furthermore, applying a short-term human tip-calibrated clock rate ($2.9 \times 10^{-3}\text{/site/year}$ estimated over 8 weeks) to deep inter-species divergence ($dS = 0.710$, approaching synonymous saturation) is evolutionarily invalid.

* **The January 23, 2020 Wuhan lockdown caused the viral effective population size ($N_e$) to plateau and drove frequency fluctuations in `ORF8 84S` and `ORF3a 251V`, while `orf8` ($dN/dS = 9.57$) and `orf3` ($dN/dS = 2.68$) experienced strong positive selection: [Methodologically Flawed].**  
  First, as acknowledged on lines 233 and 280, all 24 Wuhan sequences in this dataset were collected on or before January 5, 2020, whereas samples collected after January 21 (Episode II, $N = 79$) came from international travelers and secondary clusters outside Wuhan. Thus, the skyline plateau (Figure 4) and the trajectory of `84S` and `251V` (Figure 3) reflect a complete shift in geographic sampling ascertainment and founder bottlenecks rather than a causal effect of the January 23 Wuhan lockdown. Second, in Table 3, `orf8` and `orf3` had **zero** non-singleton synonymous polymorphisms ($dS = 0$). Substituting the genome-wide $dS$ ($1.70 \times 10^{-4}$ and $1.98 \times 10^{-4}$) into the denominator of short genes (`orf8` is 121 codons; `orf3` is 274 codons) because each carries a single non-singleton nonsynonymous variant (`L84S` or `G251V`) is statistically invalid; a Fisher's exact test of 1 nonsynonymous vs. 0 synonymous polymorphic sites in `orf8` or `orf3` against genome-wide expectations yields $P > 0.30$ (fully compatible with neutrality).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Remove the Contradictory Claim of Multi-Year Cryptic Human Circulation and Correct the RBD Divergence Calculation
* **WHY:** Claiming that SARS-CoV-2 circulated cryptically in humans for years contradicts the manuscript's own December 11, 2019 tMRCA estimate and L-shaped site frequency spectrum, and dividing $dS$ by 3 in `t = dS / (rate × 2 × 3)` is mathematically invalid.
* **WHAT:** Revise the Abstract, Discussion, and Conclusion to state clearly that the human outbreak originated in late 2019 (consistent with the BEAST tMRCA of November–December 2019), while pre-pandemic evolution and recombination of the RBD occurred in animal reservoirs prior to spillover. Remove the factor of 3 from the divergence time equation.
* **HOW:** Replace the ad-hoc `dS / (rate × 2 × 3)` calculation on line 274 with a proper codon-model or synonymous-site BEAST relaxed-clock divergence estimate on the non-recombining genomic partitions (accounting for rate decay over evolutionary timescales), and note that $dS = 0.710$ in the RBD between SARS-CoV-2 and `Pangolin_2019` indicates that `Pangolin_2019` is not the immediate donor of the RBD, but diverged from the donor lineage decades ago in wildlife reservoirs.

#### 2. Test Gene-Specific Selection and Episode Differences Using Formal Statistical Tests Rather Than Ad-Hoc $dS$ Substitution
* **WHY:** Substituting genome-wide $dS$ when a short ORF has 0 synonymous mutations artificially manufactures $dN/dS = 9.57$ (`orf8`) and $2.68$ (`orf3`) from a single polymorphism (`L84S` or `G251V`), and comparing Episode I ($dN/dS = 0.20$) vs. Episode II ($dN/dS = 0.39$) without confidence intervals or permutation tests ignores sampling noise across only 29 non-singleton sites.
* **WHAT:** Test whether `orf8` or `orf3` significantly exceed neutral expectations using a Fisher's exact test or McDonald–Kreitman test on polymorphic nonsynonymous vs. synonymous counts, and compute bootstrap 95% confidence intervals for the genome-wide $dN/dS$ in Episode I vs. Episode II.
* **HOW:** Resample codons with replacement (1,000 bootstrap replicates) within Episode I ($N = 57$) and Episode II ($N = 79$) to test whether the difference between $dN/dS = 0.20$ and $0.39$ is statistically significant ($P < 0.05$), and remove the asterisked imputed $dN/dS$ ratios for `orf3` and `orf8` in Table 3.

#### 3. Control for Spatio-Temporal Sampling Confounding in the Bayesian Skyline and Allele Trajectory Analyses
* **WHY:** Because Wuhan sampling ended on January 5, 2020, and non-Wuhan sampling dominated Episode II, time is completely confounded with geographic location.
* **WHAT:** Re-evaluate the `L84S` and `G251V` frequency trajectories (Figure 3) and $dN/dS$ comparisons (Table 3) stratified by geographic region (China Outside Wuhan vs. Rest of the World, excluding the pre-Jan 5 Wuhan cluster).
* **HOW:** Compute the frequency of `84S` and `251V` and the Episode I vs. Episode II $dN/dS$ restricting strictly to the $N = 40$ "Rest of China" or $N = 113$ non-Wuhan sequences to verify whether the temporal shifts persist when Wuhan sampling cutoff bias is removed.

#### 4. Technical and Editorial Cleanup
* **WHY:** Several date, coordinate, and codon-number typos appear across the manuscript.
* **WHAT & HOW:**
  1. **Results ("Genetic variation of SARS-CoV-2", line 106):** Change `downloaded 137 SARS-CoV-2 genomes available from GISAID as of 2/23/2019` to `2/23/2020`.
  2. **Results ("Genetic variation of SARS-CoV-2", line 174):** Change `position 28,814 which alters Leucine (L) to Serine (S) in orf8 protein (L84S)` and `28814C mutated to T` to `position 28,144` and `28144C` (matching Table 2).
  3. **Discussion & Conclusion (lines 280, 284, 289):** Change all five occurrences of `215 V in orf3 protein` to `251V in orf3 protein` (matching `G251V` in the Abstract, Results line 179, and Table 2).
  4. **Discussion (line 282):** Fix the malformed citation bracket `(41–45 [ 41 – 45 ]` to `[ 41 – 45 ]`.
