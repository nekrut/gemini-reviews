<Blinded Review: TIME_ANON_0514>
**Composite Score:** 7.6 / 10.0 (Rigor: 2.6/3.5 | Claims: 2.0/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.3/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 7.6/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This proof-of-principle quantitative genetics study evaluates the statistical power and mapping resolution of a moderate-sized panel of 110 Collaborative Cross (CC) recombinant inbred mouse strains (genotyped on the 77,808-SNP MegaMUGA array at inbreeding generation $\ge\text{N16}$, imputed to 8 founder haplotypes via `PedPhase 3` + `HAPPY`, and projected onto 329,141 variants from the JAX Mouse Diversity Array and Sanger founder sequences) using Mendelian and oligogenic coat-color traits (albino, agouti, black, cinnamon, chocolate, and white-belly). Using 8-founder haplotype logistic regression, Fisher's exact tests, multinomial regression (`R-Multinom`), and linear models with Benjamini-Yekutieli FDR control, the authors map five traits to their known causal loci (`Tyr` on Chr 7 for albino, `a`/agouti on Chr 2 for agouti/black and white-belly, `Tyrp1` on Chr 4 for cinnamon, and the digenic interaction of `Tyrp1` + `a` for chocolate) and identify causal missense variants (`rs31191169` C103S in `Tyr`; `rs28091500` C110Y in `Tyrp1`). They also perform subsampling scans ($1,150$ random subsets of $n=50$ strains and all $\binom{9}{n} = 501$ combinations of $n=2\text{--}8$ chocolate strains) to benchmark small-panel sensitivity. While the empirical demonstration is well-executed, extrapolating mapping power from fully penetrant Mendelian/digenic coat-color loci ($h^2 \approx 1.0$) to polygenic complex traits is overly optimistic, and standard GLM/Fisher's exact tests omit a polygenic kinship random effect.

### 2. STRENGTHS
- **Clear End-to-End Validation from Founder Haplotypes to Causal Missense Variants:** Demonstrates the full CC workflow—from 8-founder `HAPPY` haplotype reconstruction and `DOQTL` log-odds founder coefficient plots (cleanly pinpointing which founder strains contribute the trait allele, e.g., `NOD` + `A/J` at `Tyr`, `A/J` at `Tyrp1`, `129S1` at `A^w`) down to Sanger founder sequence intersection and tissue-expression (`GXD`) + `PROVEAN` filtering.
- **Transparent Reporting of Both Successes and Structural Variant Limitations:** In the agouti scan (Chr 2: 153.8–158.0 Mb), the authors candidly report that SNP-wise association and missense filtering failed to identify the causal variant because the `C57BL/6J` and `A/J` non-agouti allele is caused by an intronic retrotransposon insertion rather than a coding SNP.
- **Empirical Subsampling Benchmarks for Small CC Panels ($n=50$ and Rare Traits):** Exhaustively testing all 501 combinations of $n=2\text{--}8$ out of 9 chocolate strains (Table 2) provides a concrete empirical floor ($n \ge 6\text{--}7$ strains) for mapping rare recessive/digenic Mendelian traits in the CC.

### 3. Methodological & Statistical Audit / WEAKNESSES & METHODOLOGICAL AUDIT
- **Extrapolation from 100%-Penetrance Mendelian/Oligogenic Traits to Polygenic Complex Traits:** All phenotypes analyzed (albino `Tyr`, agouti `Asip`, brown/cinnamon `Tyrp1`) are classical Mendelian coat-color loci where the single-locus or three-locus genetic architecture explains nearly 100% of phenotypic variance without environmental noise. In the $n=50$ subsampling experiment (Table 1), all three high-penetrance loci simultaneously reached genome-wide significance in only $27 / 1,150 = 2.3\%$ of random 50-strain subsets (and suggestive significance in $27\%$). Presenting this as evidence that 50–100 CC strains can reliably map genuinely complex polygenic traits (where individual QTLs typically explain 2–10% of variance alongside environmental variance) overstates statistical power.
- **Omission of Kinship Random Effects in Logistic/Multinomial Regression and Fisher's Exact Tests:** Although the authors compute genome-wide kinship across the CC lines (noting pairwise kinship is generally $<60\%$ and up to $<80\%$ in lines 57–58), their primary mapping models (`R-GLM` logistic regression, `R-Multinom`, and $8 \times 2$ Fisher's exact tests) treat the 110 CC strains as independent observations without a linear mixed model (LMM/GLMM) kinship variance component. Furthermore, Fisher's exact test on an $8 \times 2$ table requires integer counts, rounding heterozygous founder weights (`0.5`).
- **Typographical Error in Figure 2 Legend Thresholds:** In the Figure 2A legend (line 75), both threshold lines are given identical p-value labels: *"The two threshold lines drawn represent 99.99% (adjusted P < 0.0001) confidence and 99.9% (adjusted P < 0.0001) confidence"* (the second should be `adjusted P < 0.001`). Similarly, line 53 states $N=110$ genotyped strains, whereas line 57 gives the haplotype weight matrix dimension as $N = 118$ strains without explaining the 8-strain difference.

### 4. Biological / Experimental Grounding & Claim Proportionality
- **A panel of 110 CC strains maps high-effect Mendelian and digenic coat-color traits (`Tyr`, `Asip`, `Tyrp1`) to 1–5 Mb intervals and identifies causal coding SNPs when the causal variant is a missense substitution:** `[Well Supported]` — Directly demonstrated across Figures 2–6.
- **Multinomial logistic regression outperforms naive 1–5 linear scoring for mapping a 3-locus epistatic coat-color system (`Tyr`, `Asip`, `Tyrp1`):** `[Well Supported]` — Demonstrated in Figure 7, where multinomial regression recovers all three loci (`Chr 2`, `Chr 4`, `Chr 7`) whereas naive ordinal linear regression misses `Tyrp1` on Chr 4.
- **A 50-strain CC scan is sufficient to map complex polygenic traits:** `[Overstated]` — Even for fully penetrant 3-gene coat color, $n=50$ recovers all 3 loci at genome-wide significance only $2.3\%$ of the time (Table 1); polygenic traits with lower heritability and smaller locus effect sizes require substantially larger sample sizes or targeted validation crosses.

### 5. Reproducibility & Data Completeness
- **Public Genotypes and Pipeline Guide:** Founder and CC MegaMUGA genotypes are linked to the UNC Collaborative Cross repository (`http://csbio.unc.edu/CCstatus/`), and strain phenotypes, residual heterozygosity, kinship matrices, and step-by-step code/instructions are provided in `File S1` and `Tables S1–S3`.
</Blinded Review: TIME_ANON_0514>
