# Review of PMC7523107 (10.1101/2020.09.24.311845)

**Manuscript Title:** An evolutionary portrait of the progenitor SARS-CoV-2 and its dominant offshoots in COVID-19 pandemic  
**Authors:** Sudhir Kumar, Qiqing Tao, Steven Weaver, Maxwell Sanderford, Marcos A. Caraballo-Ortiz, Sudip Sharma, Sergei L. K. Pond, Sayaka Miura  
**Journal / Venue:** *bioRxiv* (Preprint v3; subsequently published in *Molecular Biology and Evolution*, 2021) (ID / DOI: `PMC7523107` / `10.1101/2020.09.24.311845`)  
**Overall Score:** **7.9 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.9/3.5 | Claims: 2.0/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

Kumar et al. adapt a maximum-likelihood Mutation Order Approach (MOA; implemented via SCITE), originally designed for single-cell tumor phylogenetics, to reconstruct the early mutational backbone and most recent common ancestor ("progenitor" genome, `proCoV2`) of human SARS-CoV-2 without inferring a traditional bifurcating tree. Analyzing three progressively larger GISAID snapshots—29,681 genomes through July 7, 2020 (`29KG`, 49 SNVs with variant frequency $>1\%$), 68,057 genomes through October 12, 2020 (`68KG`, 84 SNVs), and 172,480 genomes through December 30, 2020 (`172KG`)—the authors orient variants using a three-sarbecovirus outgroup consensus (`RaTG13`, `RmYN02`, and pangolin `MT121216.1`) refined by co-occurrence index (COI) optimization. They infer that `proCoV2` predates the reference `Wuhan-Hu-1` genome by three sequential $\alpha$ mutations ($\alpha_1$: C18060U, $\alpha_2$: U8782C, $\alpha_3$: C28144U) plus three synonymous $\mu$ variants (positions 2416, 19524, 23929), and define a Greek-letter barcode nomenclature ($\mu, \nu, \alpha, \beta, \gamma, \delta, \varepsilon, \zeta, \eta$) deployed in an interactive client-side classification dashboard (`http://sars2evo.datamonkey.org/`).

This study makes a creative, computationally scalable methodological contribution to early pandemic phylodynamics: decoupling backbone mutation ordering from massive, poorly resolved comb phylogenies and providing a live browser-based classification tool using `HyPhy` codon-aware alignments (`codon-msa` + `MAFFT`) and `minimap2`. However, the manuscript exhibits several important analytical tensions: (1) SCITE's infinite-sites assumption conflicts with SARS-CoV-2 homoplasy and APOBEC-mediated $\text{C}\to\text{U}$ hypermutation, forcing ad-hoc polarity reversals that risk circularity; (2) the timing and "progenitor" framing of `proCoV2` rely on naive mutational counting rather than a joint phylodynamic model integrating temporal and epidemiological priors; and (3) Extended Data Tables 1 and 2 contain pervasive OCR/typesetting corruptions and temporal ordering anomalies that undermine presentation polish. Addressing these points through targeted sensitivity analyses and text refinements will substantially strengthen the work.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Inferring `proCoV2` as Ancestral to `Wuhan-Hu-1` via Three $\alpha$ Mutations (18060, 8782, 28144): Moderately Supported.**  
  The observation that outgroup sarbecoviruses share the Pango lineage A states (8782U, 28144C, 18060C) whereas `Wuhan-Hu-1` (lineage B) carries derived states is well grounded in comparative data and supported by 896 intermediate genomes in `29KG` (BCL = 100%). However, designating the 49-site / 84-site barcode root as the definitive *index-case progenitor* overstates the resolution of frequency-weighted MOA: position 18060 ($\text{C}\to\text{U}$) is a recurrent $\text{C}\to\text{U}$ transition, and rooting purely on outgroup consensus + COI without accounting for early Wuhan epidemiological ascertainment bias leaves alternative rootings (e.g., a polytomous A/B ancestral network or recombinant sarbecovirus outgroup homoplasy across a $\sim 1,200$-nt gap) statistically plausible.

* **Pre-December 2019 Emergence Timeline (Late October – Mid-November 2019): Moderately Supported / Naive Estimator.**  
  Subtracting 3 substitutions from December 24, 2019 using a point HPD substitution rate ($6.64\times 10^{-4}$ to $9.27\times 10^{-4}$ subs/site/year) yields a timeline (5.8–8.1 weeks prior) that happens to align with Bayesian phylodynamic studies (e.g., Pekar et al., Rambaut et al.). Methodologically, however, dividing an integer difference of $k=3$ mutations by an average clock rate ignores Poisson mutational variance on short branches and conflates the time of the most recent common ancestor (tMRCA) with the index zoonotic transmission event. Furthermore, citing a 409-bp Italian Spike amplicon—which lacks all 49 diagnostic positions—as confirming `proCoV2` in Europe in early December is speculative and should be tempered.

* **Robustness of the Mutational Backbone Across Expanding GISAID Snapshots (`29KG` vs. `68KG`): Well Supported.**  
  The core sequential path ($\mu \to \alpha_1 \to \alpha_2 \to \alpha_3 \to \beta_1\text{--}\beta_3 \to \{\gamma\delta, \varepsilon, \zeta, \eta\}$) reproduces cleanly when more than doubling the sample size from 29,681 to 68,057 genomes, with high co-occurrence indices ($\text{COI} > 96.7\%$) and strong concordance (74 of 80 Pango lineages mapping at $>90\%$ purity to single MOA fingerprints).

* **Infinite-Sites Assumption & COI-Guided Polarity Reversal (Positions 3037, 28657, 28854): Fragile.**  
  SCITE assumes a single-origin, clonal infinite-sites process where high variant frequency implies early origin and deviations represent sequencing error ($\text{FNR}/\text{FPR}$). In SARS-CoV-2, host-driven APOBEC $\text{C}\to\text{U}$ editing and selective sweeps (e.g., D614G / $\beta_2$ hitchhiking with $\beta_1$ C3037U and $\beta_3$ C14408U) violate both assumptions. Reversing outgroup-assigned polarity whenever $\text{COI} < 70\%$ (as done at positions 3037 and 28657) optimizes the tree to fit the infinite-sites model, risking circular confirmation of the backbone and misclassifying recurrent homoplasies (such as C28854U, $\beta_{3b}$) as single-origin offshoots or "sequencing errors."

* **Episodic Accumulation of Variant Groups ($\beta, \varepsilon, \zeta, \eta$): Moderately Supported.**  
  The observation that multi-mutation haplotypes ($\beta_1\text{--}\beta_3$, $\varepsilon_1\text{--}\varepsilon_3$, $\zeta_1\text{--}\zeta_6$) co-occur vastly more often than intermediate single-mutant steps is empirically undeniable. However, the $\varepsilon_1\text{--}\varepsilon_3$ cluster (28881–28883, `GGG` $\to$ `AAC` in Nucleocapsid) is a well-characterized single-event trinucleotide/slippage substitution rather than three independent sequential point mutations. Treating 28881, 28882, and 28883 as three separate independent variants inflates the runs-test statistic for "episodic mutation accumulation."

* **Global Spatiotemporal Turnover & Convergent N501Y Emergence: Well Supported (with Sampling Caveats).**  
  Tracking across 172,480 genomes clearly captures the persistence of $\alpha\beta\gamma\delta$ (clade 20C / B.1.2) in North America versus the sweep of $\alpha\beta\zeta$ (20A.EU1 / B.1.177) and $\alpha\beta\varepsilon$ (20B / B.1.1) in Europe, as well as the independent emergence of Spike N501Y on $\alpha\beta\gamma\delta$ (South Africa) vs. $\alpha\beta\varepsilon$ (UK). As the authors rightly acknowledge, regional proportion curves remain sensitive to extreme GISAID sequencing skew (UK and US dominating global submissions in 2020).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Separate Mutational Homoplasy from Sequencing Error ($\text{FNR}/\text{FPR}$) and Audit COI Polarity Reversals
* **WHY:** SCITE absorbs all violations of the infinite-sites assumption into global false-positive ($\text{FPR} \approx 0.003$) and false-negative ($\text{FNR} \approx 0.004$) sequencing error rates. In high-coverage consensus viral genomes, true sequencing error at common sites ($>1\%$) is orders of magnitude lower than $0.3\%$; most discrepancies reflect real recurrent mutations ($\text{C}\to\text{U}$ hypermutation) or early recombination. Moreover, flipping ancestral/derived coding when $\text{COI} < 70\%$ (positions 3037 and 28657) risks circularity.
* **WHAT:** Quantify how much of the estimated $\text{FPR}/\text{FNR}$ is driven by known homoplasic hotspots and justify polarity reversals independently of COI maximization.
* **HOW:** Report site-specific discrepancy rates across the 49/84 positions to show which sites drive the global $\text{FPR}/\text{FNR}$ (e.g., C28854U, G11083U, C14805U). For position 3037, explicitly explain *why* the three sarbecovirus outgroups carry `U` while `proCoV2` is recoded to `C` (i.e., outgroup homoplasy along the long bat/pangolin branch vs. back-mutation inside humans).

#### 2. Treat Nucleocapsid 28881–28883 ($\varepsilon_1\text{--}\varepsilon_3$) as a Single Complex Mutational Event in Episodic Tests
* **WHY:** Positions 28881, 28882, and 28883 (`GGG` $\to$ `AAC`) mutate simultaneously via template-switching/slippage at a TRS-like motif. Counting them as three independent sequential mutations in SCITE and in the Wald-Wolfowitz runs test artificially inflates temporal clustering.
* **WHAT:** Ensure statistical tests of episodic spread are not driven by linked multi-nucleotide mutations.
* **HOW:** Collapse $\varepsilon_1\text{--}\varepsilon_3$ into a single composite locus (`N:28881-28883`) and re-run the Wald-Wolfowitz runs test on `29KG` and `68KG` to verify that $P \ll 0.01$ holds for genuinely independent genomic sites.

#### 3. Reconcile Temporal Discordances in `68KG` Offshoots ($\zeta_1$ vs. $\zeta_2\text{--}\zeta_7$ and $\eta_1$ vs. $\eta_2\text{--}\eta_6$)
* **WHY:** In the `29KG` dataset, the authors highlight that 47/49 mutations appear in chronological order ($t_f(\text{child}) \ge t_f(\text{parent})$). However, in Extended Data Table 2 (`68KG`), major parent nodes are dated *months later* than their downstream descendants: $\zeta_1$ is listed at Day 179 while its descendants $\zeta_2\text{--}\zeta_7$ appear at Days 78–96; similarly, $\eta_1$ is at Day 86 while $\eta_2$ is at Day 51 and offshoots $\eta_{1e}, \eta_{1g}, \eta_{1i}$ appear at Days 55–73.
* **WHAT:** Audit and explain or fix the first-appearance timestamps ($t_f$) in Extended Data Table 2.
* **HOW:** Check whether Day 179 for $\zeta_1$ (position 445) and Day 51 for $\eta_2$ (position 18555) reflect metadata date errors in GISAID, sporadic early homoplasies outside the 20A.EU1 clade, or a table lookup bug, and report the temporal concordance fraction ($X/84$) for `68KG` just as was done for `29KG` ($47/49$).

#### 4. Replace Point-Subtraction Emergence Dating with a Formal Uncertainty Interval
* **WHY:** Multiplying 3 substitutions by an inverse clock rate ignores Poisson variance (3 mutations can arise in 1 day or 10 weeks) and assumes `Wuhan-Hu-1` lies on a single linear lineage from the index case without selective sweeps or sampling lag.
* **WHAT:** Present the late-October to mid-November 2019 estimate with appropriate coalescent/Poisson confidence bounds.
* **HOW:** Compute a gamma/Poisson credible interval around $k=3$ substitutions integrated over the substitution rate distribution, and remove or qualify the claim that the 409-bp Italian Spike sequence (which contains zero informative MOA sites) specifically validates `proCoV2`.

#### 5. Clarify the Synonymous $\mu_1\text{--}\mu_7$ Basal Layer vs. `proCoV2` Definition
* **WHY:** The text states on page 4 that `proCoV2` is "the same as the NCBI reference genome with base differences corresponding to $\alpha_1\text{--}\alpha_3$ mutations at positions 18060, 8782, and 28144," yet Figure 1 and Extended Data Tables 1–2 place three (`29KG`: $\mu_1\text{--}\mu_3$) or seven (`68KG`: $\mu_1\text{--}\mu_7$) basal U$\to$C synonymous mutations *above* $\alpha_1$ at 95.6%–99.0% frequency.
* **WHAT:** Eliminate ambiguity over whether the downloadable `proCoV2` FASTA carries `U` or `C` at the $\mu_1\text{--}\mu_7$ sites (positions 2416, 6286, 15933, 19524, 22444, 23929, 27944).
* **HOW:** Explicitly state in the "Progenitor genome" section and Methods whether `proCoV2` is defined at the root above $\mu_1$ (carrying ancestral `U` shared with bat/pangolin outgroups, making it 6 or 10 nucleotides different from `Wuhan-Hu-1` across all 49/84 sites, while remaining protein-identical) or at the $\mu_3/\mu_7$ node (3 nucleotides different from `Wuhan-Hu-1`).

#### 6. Technical, Typographical, and Table Cleanup
* **WHY:** Extended Data Tables 1 and 2 and the Methods text contain numerous formatting/OCR corruptions and typos that detract from the rigor of the paper.
* **WHAT & HOW:**
  * **Fix Greek/Symbol Corruptions in Extended Data Tables 1 & 2:**
    * Replace `0RF3a` and `0RF8` (spelled with a leading zero `0`) with `ORF3a` and `ORF8` across both tables.
    * Replace capital `V1` and `V2` (at the bottom of Tables 1 and 2, positions 17858 and 17747) with Greek nu (`ν1`, `ν2`).
    * In Table 2, fix row `5,` (at position 1059, ORF1ab) which is a corrupted `δ1`, and fix shifted labels where `γ1` is misaligned onto the `β3d` row (position 25429) and `δ1` is misaligned onto the `γ1` row (position 25563).
    * In Table 1, two different mutations (positions 13862 and 10798) are both labeled `β3f` (the second should be `β3g`, as in Table 2).
    * In Table 2, replace lowercase `l` in amino acid changes `T>l` and `M>l` (positions 13862, 1059, 4002, 19542, 19718, 26060) with capital `I` (`T>I`, `M>I`).
    * Standardize European comma decimals (`2,0%`, `2,7%`, `2,5%`, `1,2%`) in Table 1 to periods (`2.0%`, `2.7%`, etc.).
  * **Fix Main Text & Methods Typos:**
    * In the "Testing episodic spread" Methods section, correct `64KG` (twice) to `68KG`.
    * In the "Analysis of 68KG dataset" section, verify the variant count arithmetic: the text states `68KG` has "72 common variants ($>1\%$)" plus "12 variants that were common on 29KG... 84 variants in total," whereas the Figure 3b caption says "The 68KG dataset contains 12 additional variants" (which would be $49 + 12 = 61$, not 84).
    * Fix `"P < 1−8"` in the Results text (page 6) to `"P < 10^{-8}"`.
    * Fix `"29,861 genomes"` in Methods (pages 10–11, four occurrences) to match `"29,681 genomes"` reported in the Results and Methods page 8.
    * Fix `"B.1.350"` (page 7) to `"B.1.351"` (the South African 501Y.V2 lineage).
