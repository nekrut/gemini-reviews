# Review of ANON_141

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.4 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.3/3.5 | Claims: 2.4/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents a quantitative deep mutational scan (DMS) of all 3,819 possible single amino acid substitutions across the 201-residue receptor-binding domain (RBD, residues N331–T531) of the SARS-CoV-2 Wuhan-Hu-1 spike protein. Using duplicate independently mutagenized and N16-barcoded yeast-surface-display libraries (~100,000 variants per library, averaging 2.7 amino acid substitutions per variant, linked via long-read PacBio circular consensus sequencing at >99.8% empirical accuracy), the authors sort cells across fluorescence bins to measure both folded RBD surface expression ($\Delta\log(\text{MFI})$, 99.5% coverage) and apparent binding affinity across a 16-point titration of natively dimeric human ACE2 ($\Delta\log_{10}(K_{D,\text{app}})$, 99.6% coverage). Single-mutant effects are decomposed from multi-mutant backgrounds via Cauchy-likelihood global epistasis regression (`dms_variants`), yielding high inter-library replicate concordance ($R^2 = 0.93$ for expression, $R^2 = 0.95$ for binding). The DMS measurements are extensively validated against isogenic yeast titrations, biolayer interferometry (BLI) of mammalian-expressed RBDs with monomeric and dimeric ACE2, size-exclusion chromatography (SEC) and thermal denaturation ($T_m$) of stability-enhancing variants, and spike-pseudotyped lentiviral entry assays, and are further applied to evaluate sarbecovirus ACE2 tropism, antibody epitope constraints, and early pandemic GISAID sequence variation ($N = 31,570$). Full raw sequencing reads (SRA PRJNA639956), barcode lookup tables, and an automated Snakemake/computational notebook pipeline are publicly available.

This is a benchmark experimental and quantitative genomics study with rigorous internal controls, careful attention to ligand-depletion stoichiometry, and transparent uncertainty handling. The few methodological limitations are minor and well-documented: (1) binding titrations use dimeric ACE2 against multivalent yeast-displayed RBD, measuring avidity-enhanced apparent affinity ($K_{D,\text{app}} = 3.9 \times 10^{-11}\text{ M}$) rather than 1:1 monomeric affinity, and the global epistasis link function for binding saturates near the wild-type plateau, preventing affinity-enhancing calls for the 5.7% of mutations inferred solely via multi-mutant interpolation; (2) integer-weighted mean-bin averaging for binding titration points introduces slight discretization bias compared to censored normal maximum-likelihood estimation; and (3) permutation tests on GISAID mutation counts treat total isolate occurrences as independent observations rather than phylogenetic emergence events. None of these caveats alter the core conclusions, and all can be addressed via minor statistical extensions or caveats in the text.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **High-throughput yeast-display FACS-seq accurately quantifies single-mutant effects on RBD expression and apparent ACE2 affinity across 99.5%–99.6% of all possible substitutions: [Well Supported].**  
  Independent biological duplicate libraries show strong concordance ($R^2 = 0.93$ for global-epistasis-decomposed expression; $R^2 = 0.97$ for directly sampled single-mutant binding and $R^2 = 0.95$ after interpolating unsampled singletons), internal stop-codon and synonymous controls behave as expected, and isogenic yeast re-cloning, mammalian BLI, and pseudotyped lentiviral entry assays independently confirm the dynamic range and directionality of the high-throughput measurements (Figures 2, 4, S2, S4).

* **The SARS-CoV-2 RBD exhibits substantial mutational plasticity at the ACE2 interface, including multiple single-residue substitutions (e.g., at Q493, Q498, N501) that enhance human ACE2 binding affinity: [Well Supported].**  
  Forty-six percent of single amino acid substitutions maintain $K_{D,\text{app}}$ at least as tight as SARS-CoV-1 RBD, and specific interface substitutions (such as N501F, N501T, and Q498Y) are directly confirmed in isogenic titrations and spike-pseudotyped lentiviral entry assays (Figures 3B, 4A–B, 4H, 5D–E).

* **Additivity of single-mutant interface effects explains ACE2 affinity variation within the close SARS-CoV-2 sarbecovirus clade (GD-Pangolin, RaTG13) but breaks down across deeper divergences (SARS-CoV-1) due to epistatic entrenchment: [Well Supported].**  
  Summing single-mutant $\Delta\log_{10}(K_{D,\text{app}})$ values at interface positions accurately predicts the higher affinity of GD-Pangolin (driven by Q498H) and lower affinity of RaTG13 (driven by Y449F and N501D), whereas individual SARS-CoV-1 interface states are predominantly deleterious when introduced singly into the SARS-CoV-2 background despite SARS-CoV-1 RBD binding human ACE2 efficiently (Figure 5F).

* **Core-RBD expression-enhancing mutations (e.g., V367F, I358F, Y365F, Y365W, F392W) increase mammalian soluble RBD yield and thermal stability without disrupting ACE2 or CR3022 antigenicity: [Well Supported].**  
  Purification from mammalian Expi293F cells confirms 2.3- to 4.8-fold increases in monomeric SEC yield and increases in non-equilibrium melting temperature up to $+3.9^\circ\text{C}$ (for V367F), while maintaining BLI binding to human ACE2 and CR3022 (Figures 4E–G, S4G–I).

* **Circulating SARS-CoV-2 RBD mutations up to May 2020 are shaped primarily by purifying selection on folding and ACE2 binding, with no statistical evidence of positive selection for enhanced ACE2 affinity: [Moderately Supported].**  
  The permutation tests in Figures 7A and S7B–D appropriately restrict the null pool to single-nucleotide-accessible amino acid substitutions from Wuhan-Hu-1, demonstrating that observed mutations are significantly less deleterious than random accessible mutations ($p < 10^{-6}$). However, stratifying mutations by raw GISAID sequence counts ($\ge 1, \ge 2, \ge 6$) conflates independent mutational origins (homoplasies) with epidemiological founder effects and uneven geographic sequencing, which reduces the effective sample size of the higher-frequency strata.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Account for Global Epistasis Ceiling Truncation in Interpolated Binding Estimates
* **WHY:** In the STAR Methods ("Decomposing single-mutant effects from multiple-mutant genotypes") and Figures S2H and S2K, the fitted monotonic spline for the binding global epistasis model plateaus near the wild-type phenotype ($\Delta\log_{10}(K_{D,\text{app}}) \approx 0$). Consequently, the ~14% of mutations per library (~5.7% across both libraries) whose binding effects are interpolated from multi-mutant backgrounds via global epistasis are mathematically prevented from taking positive (affinity-enhancing) values.
* **WHAT:** Explicitly flag interpolated vs. directly measured single mutants in Table S2 and test whether a less restrictive spline parameterization or local background averaging recovers positive effects for double mutants containing known affinity-enhancing partners.
* **HOW:** Add a boolean column (`direct_single_mutant`) to `single_mut_effects.csv` (Table S2) indicating whether the reported binding value comes from direct single-mutant barcodes or global epistasis interpolation, and report in the text the exact count of mutations where only one or zero libraries had a direct single-mutant barcode.

#### 2. Compare Censored Maximum-Likelihood vs. Integer Mean-Bin Reconstruction for Titration Curves
* **WHY:** For expression sorts, the authors use censored Gaussian maximum likelihood (`fitdistrplus`) over the exact log-fluorescence gate boundaries, whereas for ACE2 binding titrations they compute a simple integer-weighted average of bins 1–4 ($\overline{\text{bin}}_{[\text{ACE2}]} = \sum_{i=1}^4 i \cdot n_i / N$). Because bin 1 and bin 4 are semi-infinite censored intervals (capturing 95% of unbound or saturated wild-type cells), integer-bin averaging compresses variance in the tails and can slightly bias the Hill slope and plateau parameters ($a, b$).
* **WHAT:** Quantify the sensitivity of inferred $K_{D,\text{app}}$ values to integer-bin averaging versus censored normal MLE reconstruction on the log-PE fluorescence scale.
* **HOW:** Using the recorded FACS Aria II log-PE gate boundaries for bins 1–4 across the 16 ACE2 concentrations in `compute_binding_Kd.md`, apply the same `fitdistrplus` censored normal estimator used for expression to a subset of 1,000 barcodes (including the internal homolog standards and isogenic controls) and report the correlation with the integer-bin $K_{D,\text{app}}$ fits.

#### 3. Stratify GISAID Purifying/Positive Selection Permutation Tests by Independent Mutational Occurrences
* **WHY:** In Figures 7A and S7B–D, circulating RBD variants are thresholded by total isolate count in GISAID ($\ge 1, \ge 2, \ge 6$). Because a single neutral mutation introduced into an early expanding transmission cluster can appear in hundreds of GISAID sequences without independent selection, raw isolate count is a noisy proxy for evolutionary persistence.
* **WHAT:** Repeat the permutation tests in Figure S7B and S7D stratifying mutations either by the number of distinct geographic regions/lineages or by parsimony-inferred independent mutational occurrences (homoplasies).
* **HOW:** Using the geographic region count already tabulated in Figure 7B (or the phylogenetic homoplasy counts cited from van Dorp et al., 2020), run the $10^6$-iteration single-nucleotide-accessible permutation script in `circulating_variants.md` on mutations observed in $\ge 2$ and $\ge 3$ regions/lineages, and report the resulting empirical $p$-values alongside the raw count thresholds.

#### 4. Propagate Post-Sort Plasmid Retention Uncertainty into Titration Weights
* **WHY:** In the STAR Methods ("Fluorescence-activated cell sorting (FACS) of yeast libraries"), the authors note that while all expression sort bins were plated to measure exact cell recovery and plasmid retention (which dropped to 20% in FITC-negative bin 1), the 64 binding titration sort bins were only spot-checked across 6 samples (showing 66% cell recovery and 46% plasmid retention) and weighted using raw FACS event counts.
* **WHAT:** Incorporate the empirical 46% plasmid retention factor when computing the effective cell count ($N_{\text{eff}}$) used to weight the nonlinear least-squares titration fits and downweight Illumina read counts.
* **HOW:** In `count_variants.md` and `compute_binding_Kd.md`, scale the FACS event counts for the binding titration bins by the spot-checked plasmid retention factor (0.46) when calculating the read-to-cell ratio and empirical variance weights, and verify that the 5% normalized mean-square residual filter remains invariant.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Minor typographical errors appear in the STAR Methods text.
* **WHAT & HOW:**
  1. **STAR Methods, "Decomposing single-mutant effects from multiple-mutant genotypes":** Correct `"correlated moderately well between replicates (R 2 = 88, Figure S2 F)"` to `"(R 2 = 0.88, Figure S2 F)"`, and fix `"likely to do partial collinearities"` to `"likely due to partial collinearities"`.
  2. **STAR Methods, "Pseudotyped lentiviral particle infection assays":** Correct `"ACE2 binding (L455Y, N501D and G502)"` to specify the mutant residue `"G502D"` (matching Figure 4H).
  3. **STAR Methods, "Experimental Model and Subject Details":** Remove the duplicated word in `"grown at at 37°C"`.
