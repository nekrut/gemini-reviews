<Blinded Review: TIME_ANON_0296>
**Composite Score:** 8.5 / 10.0 (Rigor: 3.1/3.5 | Claims: 2.2/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.7/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This methodological and empirical quantitative genetics study evaluates the power, positional precision, and allelic phase/mode-of-action diagnostic accuracy of identity-by-descent (IBD)-weighted QTL mapping in outcrossing autopolyploids (autotetraploids and autohexaploids). Combining meiosis simulations in `PedigreeSim` with multipoint HMM inheritance probability reconstruction in `TetraOrigin`, the authors systematically compare a random-bivalent QTL regression model (`noDR`, 36 genotype states in tetraploids) against a full polysomic model incorporating multivalent pairing and double reduction (`DR`, 100 genotype states) across varying quadrivalent rates ($q = 0\text{–}0.5$ in tetraploids; $0\text{–}1.0$ in hexaploids), population sizes ($N = 200, 400$), heritabilities ($h^2 = 0.1, 0.2, 0.7$), QTL segregation types (`SxN`, `DxN`, `SxS`, multi-allelic), and additive vs. dominant actions. In parallel, they formulate a ploidy-independent per-homolog Genotypic Information Coefficient ($\text{GIC}_j = 1 - \frac{4}{N}\sum_{n=1}^N \pi_n(1-\pi_n)$) and demonstrate that uneven GIC across homologs acts as a powerful "attractor" biasing QTL peak locations and reducing detection power—an effect that vastly outweighs whether double reduction is explicitly modeled. Finally, they validate both models on 3-year field data ($N = 222$) from the `Altus × Colomba` tetraploid potato F₁ population, mapping plant maturity to *StCDF1* on chromosome 5 (`oooo × oooQ` additive) and tuber flesh color to *StChy2* on chromosome 3 (`oooo × QQoo` dominant).

### 2. Methodological & Statistical Audit
- **Mathematical Derivation & Simulation Design:** The Kempthorne main-effects weighted linear regression model (with sum-to-ploidy collinearity constraints $X_1+X_2+X_3+X_4=2$ and $X_5+X_6+X_7+X_8=2$), Churchill–Doerge chromosome-wide permutation thresholds (1,000–2,500 permutations per parameter setting at $\alpha = 0.05$), and the 224-model BIC phase/action diagnostic procedure are rigorously formulated and benchmarked.
- **Insightful Characterization of Per-Homolog GIC Bias:** Figure 3B–C and Table 2 provide an exceptionally clear demonstration of how a single simplex marker tagging an otherwise poorly covered homolog creates a local GIC maximum that pulls nearby QTL peaks toward itself even when detection power is 100%, and how `DxN`/`SxS` QTL power scales monotonically across `LL`, `LH/HL`, and `HH` homolog GIC classes.
- **Minor Technical Caveats:**
  - In `TetraOrigin`, parental phasing was run with `bivalentPhasing = True` for computational tractability before running offspring decoding under `bivalent_decoding = False` (`DR`), and in hexaploids multivalent formation was restricted to one parent at a time due to memory limits. While justified practically, this slightly favours `noDR` consistency during the phasing step.
  - Spline interpolation (`smooth.spline` in R) of discrete marker IBD probabilities onto a 1 cM grid followed by re-normalization is an approximation to exact HMM inter-marker emission-free decoding, though the authors appropriately re-map the empirical potato candidate peaks directly at unbinned marker positions in Figure 7 and Table 4.
  - Ordinal field phenotypes (maturity 1–9, flesh color 4–8) were analyzed via Gaussian linear mixed models (`nlme::lme` BLUEs) and Gaussian RSS-based LOD scores rather than ordinal probit/logit link models, although with $N = 222$ and 3-year averages the normal approximation performs well.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1: Per-homolog Genotypic Information Coefficient (GIC) uniformity and magnitude have a far greater impact on autopolyploid QTL power and positional precision than modeling double reduction.** `[Well Supported]` — Conclusively established by binomial GLMs on detection rate, linear models on threshold-adjusted LOD scores, and positional bias analyses across potato chromosomes 1 and 12.
- **Claim 2: Including double reduction (`DR` model) yields at most marginal (~5%) gains in QTL detection power under high quadrivalent pairing ($q = 0.5$) and low power ($N = 200, h^2 = 0.1$) for telomeric QTL, while LOD-1 support intervals are unreliable ($16\%\text{–}32\%$ miss rate even at $q = 0$).** `[Well Supported]` — Directly supported by the chromosome 12 simulation grid (Figure 5A–E).
- **Claim 3: Empirical validation in `Altus × Colomba` tetraploid potato accurately localizes *StCDF1* (chr 5, ~4.54 Mb) and *StChy2* (chr 3, ~43.94 Mb) within narrow LOD-2 intervals and diagnoses their allelic configurations.** `[Well Supported]` — Both known causal genes fall inside the saturated LOD-2 intervals (Table 4, Figure 7), and the authors thoughtfully explain why zero-centered F₁ contrast effects create apparent "balancing" negative effects on non-carrier homologs.

### 4. Reproducibility & Data Completeness
- **Data & Supplement Availability:** Extensive supplementary files (Files S1–S6, Tables S1, Figures S1–S9) and raw/processed datasets are publicly deposited on Figshare (`https://figshare.com/s/a97475f5802e3354f44e`). All software versions (`PedigreeSim`, `TetraOrigin` in Mathematica 10, `R v3.3.2`, `nlme`) and parameter settings (`epsF = 0`, `eps = 0.001`) are fully specified.
</Blinded Review: TIME_ANON_0296>
