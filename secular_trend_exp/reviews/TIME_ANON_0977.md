<Blinded Review: TIME_ANON_0977>
**Composite Score:** 6.8 / 10.0 (Rigor: 2.3/3.5 | Claims: 1.8/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.2/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 6.8/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This molecular epidemiology and viral phylodynamics study sequences 7 new complete genomes ($15,948\ \text{nt}$) of Peste des petits ruminants virus (PPRV; 4 from lineage III and 3 from lineage IV) and integrates them with 7 publicly available full genomes ($n = 14$ total; $n = 12$ field isolates after excluding 2 serially passaged vaccine strains, `Nigeria/1975/1` and `Sungri`) and $n = 159$ partial nucleoprotein (*N*) gene sequences ($255\ \text{nt}$, positions $1,253\text{--}1,507$, sampled 1968–present across 30 locations) to estimate selective pressures ($\text{SLAC}$ $d_N/d_S$), evolutionary substitution rates, times to most recent common ancestor ($\text{TMRCA}$), demographic history (Bayesian skyline plot), and discrete phylogeographic diffusion in `BEAST v1.8.0`. The authors thoughtfully evaluate the impact of including vs. excluding attenuated vaccine strains (`Nigeria/1975/1` and `Sungri`), showing that vaccine strains artificially depress evolutionary rate estimates and push back the inferred root $\text{TMRCA}$ ($1904 \to 1891$). However, the study chooses an exponential growth coalescent prior solely because it yielded narrower $95\%$ HPD intervals despite non-significant Bayes factor support ($2\ln\text{BF} < 2$), contains a 10-fold typographical error in Table 4 (`UCLD/BSP` mean rate printed as $2.89 \times 10^{-3}$ outside its own $95\%$ HPD upper bound of $6.92 \times 10^{-4}$), and draws discrete phylogeographic origin claims from flat root state posterior probabilities ($12.69\%$ and $17.20\%$).

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES

#### STRENGTHS
- **Generation of 7 complete $15,948\ \text{nt}$ morbillivirus genomes and explicit vaccine-strain sensitivity analysis:** Prior to this work, full-genome representation of PPRV lineages III and IV was sparse. By explicitly running `BEAST` with ($n = 14$) and without ($n = 12$) the laboratory-passaged vaccine strains (`Nigeria/1975/1` and `Sungri`), the authors demonstrate empirically how passage history distorts tip-dated molecular clock calibrations.
- **Systematic clock and demographic model comparison:** Table 4 reports marginal log-likelihoods, substitution rates, and $\text{TMRCA}$s across 12 combinations of 4 clock models (strict, UCLD, UCED, random local) and 3 coalescent priors (BSP, constant size, exponential growth) for both the complete genome ($n = 12$) and partial *N* gene ($n = 159$) datasets.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Model selection based on narrow $95\%$ HPD intervals rather than marginal likelihood:** In Section "Evolutionary Rate Estimates" (line 105), the authors note that Bayes factors did not distinguish among the three demographic models under the UCED clock ($2\ln\text{BF} < 2$; in Table 4, $-\log L$ is $-46,933.82$ for BSP, $-46,933.98$ for CS, and $-46,933.96$ for EG), and state: *"However, the exponential demographic model was chosen because it provided a narrow margin of 95% highest posterior density (HPD) estimates."* Selecting a parametric exponential growth prior because it tightens posterior credible intervals—especially when the authors' own Bayesian Skyline Plot (Fig. 4) shows a flat effective population size until the mid-1990s followed by a late decline—artificially understates parameter uncertainty.
- **Numerical inconsistencies and typos in Table 4:**
  - In Table 4 row 4 (`PPRV complete genome (12)`, `GTR + G/UCLD/BSP`), the mean nucleotide substitution rate is reported as `2.89 x 10^-3`, which lies completely outside its own reported $95\%$ HPD interval (`3.21 x 10^-8 – 6.92 x 10^-4`); this is a 10-fold exponent typo for $2.89 \times 10^{-4}$.
  - In Table 4 row 27 (`P CDS (12)`), the mean substitution rate is `1.11 x 10^-3` with $95\%$ HPD `3.46 x 10^-4 – 1.29 x 10^-3`, where `1.29 x 10^-3` is almost certainly a typo for `1.92 x 10^-3` (given `P complete gene` immediately below has `3.46 x 10^-4 – 2.03 x 10^-3`).
  - Marginal likelihoods in `Tracer v1.5` (harmonic mean estimator / smoothed AICM) are known to be high-variance estimators compared to path sampling / stepping-stone sampling.
- **Severe lineage and geographic sampling imbalance in discrete phylogeography:** In the $n = 12$ field-isolate complete genome dataset, Lineage I ($n = 1$, Ivory Coast) and Lineage II ($n = 1$, Nigeria) are represented by single sequences. In the discrete trait phylogeographic analysis (`BSSVS`), the root location posterior probabilities are nearly uniform across the 10 sampled countries ($9.02\%\text{--}12.69\%$ in Fig. 5; peak $17.20\%$ for Nigeria vs. $14.28\%$ for Ghana in Fig. 6). While the final paragraph of the Discussion rightly urges caution, earlier text states *"Our phylogeographic analysis indicated that Nigeria was the geographic origin of the most recent common ancestor of PPRV because of the highest root location state probability,"* over-interpreting a $17.2\%$ marginal probability driven by historical sampling density in West Africa.
- **Sliding-window $d_N/d_S$ truncation artifact in Figure 1:** Figure 1 plots 5-codon sliding-window Nei-Gojobori $d_N/d_S$ across the concatenated genome, capping values at $\ge 10$ (which occur whenever $d_S = 0$ in a 5-codon window), whereas the gene-wide maximum likelihood `SLAC` estimates in Table 3 correctly show strong purifying selection across all genes ($d_N/d_S = 0.06\text{--}0.45$).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim that PPRV evolves under strong purifying selection across all six structural genes ($d_N/d_S = 0.06\text{--}0.45$) with highest constraint in *M* and *L* and lowest in *P*:** `[Well Supported]` — Supported by codon-level `SLAC` and codon-position relative substitution rates ($\text{CP3} \gg \text{CP1} > \text{CP2}$) in Table 3.
- **Claim that the complete-genome PPRV substitution rate is $\sim 8\text{--}9 \times 10^{-4}\ \text{substitutions/site/year}$ with a 20th-century root $\text{TMRCA}$ ($\approx 1904$, $95\%$ HPD $1730\text{--}1966$):** `[Moderately Supported]` — Consistent between complete genomes and partial *N* gene datasets, though wide $95\%$ HPDs reflect the small number of early historical genomes ($n = 12$).
- **Claim that Nigeria is the geographic origin of ancestral PPRV:** `[Fragile]` — Root state posterior probabilities ($12.69\%$ in full genomes, $17.20\%$ in partial *N* genes) are barely above the uniform prior and heavily sensitive to geographic sampling bias.

### 4. Reproducibility & Data Completeness
All 14 complete genome GenBank accession numbers (including the 7 newly sequenced genomes: `KJ867540`–`KJ867545`, `KC594074`) and the 4 outgroup RPV/MV accessions (`AB547189`, `X98291`, `AF266288`, `JF791787`) are listed in Table 1. Software versions (`BioEdit v7.2.0`, `jModelTest v2.1.4`, `BEAST v1.8.0`, `Tracer v1.5`, `FigTree v1.4.0`) and MCMC settings ($2$ runs, $10\%$ burn-in, $\text{ESS} > 200$) are clearly documented. The accession list for the 159 partial *N* sequences and the `BEAST` XML input files are not included in the main text.
</Blinded Review: TIME_ANON_0977>
