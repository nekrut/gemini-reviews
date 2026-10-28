# Review of PMC7854630 (PMID:33531494)

**Manuscript Title:** A practical solution to pseudoreplication bias in single-cell studies  
**Authors:** Zimmerman KD, Espeland MA, Langefeld CD.  
**Journal / Preprint:** *Nat Commun* (2021; `PMC7854630` / `PMID:33531494` / `10.1038/s41467-021-21038-1`)  
**Calibration Study Cohort:** Cohort B — Validated Control (`B45` | Double-Blinded as `ANON_83`)  
**Overall Score:** **7.5 / 10.0** (Strong / Sound)
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.8/2.0

---

## 1. Executive Summary & Synthesis

`ANON_83` investigates a pervasive statistical error in multi-donor single-cell RNA sequencing (scRNA-seq) differential expression (DE) studies: treating individual cells from the same biological specimen or donor as statistically independent experimental units (pseudoreplication). By analyzing $40,775$ cells across 10 cell types from four public scRNA-seq datasets (`GSE81861`, `GSE72056`, `E-MTAB-5061`, and `EGAS00001004082`) and conducting large-scale hierarchical simulations ($250,000$ null iterations for Type I error and $1,000$ replicates per fold-change increment for power), the authors demonstrate that positive intra-individual correlation severely inflates Type I error rates across standard cell-level DE methods (`MAST` default, `Monocle` Tobit, `Tweedie GLM`, `ROTS`) and that applying `ComBat` batch correction across individuals prior to DE testing exacerbates false positives to $0.60\text{--}0.86$ at $\alpha = 0.05$.

The manuscript's diagnosis of pseudoreplication and its critique of pre-DE inter-individual `ComBat` adjustment are timely, mathematically sound, and empirically well-supported. However, the benchmark comparison between generalized linear mixed models (`MAST+RE`, `Tweedie GLMM`) and `DESeq2` pseudo-bulk aggregation (`Mean` and `Sum`) is compromised by a critical implementation artifact in the `DESeq2` simulation pipeline. Specifically, in the Methods (Evaluation of Type 1 error, line 178, and Evaluation of power, chunk 2 line 8), the authors forced all `DESeq2` size factors to $1.0$ (`sizeFactors = 1`) and simulated single genes in isolation using transcripts-per-million (`TPM`) distributions modeled on Smart-Seq2 pancreatic $\alpha$-cells. When cell counts per donor vary across individuals (Poisson or negative binomial imbalance), the unnormalized **Sum** of expression across cells within an individual scales linearly with the number of captured cells $n_j$. Fixing `DESeq2` size factors to $1.0$ prevents library-size / cell-count normalization, artificially inflating between-donor variance for the `Sum` aggregation and causing `DESeq2` pseudo-bulk `Sum` to appear overly conservative (Type I error $0.008\text{--}0.035$) and severely underpowered (Fig. 3e–f). Furthermore, at small donor sample sizes ($N = 5$ individuals per group), both `MAST+RE` and `Tweedie GLMM` still exhibit anti-conservative Type I error rates ($0.064\text{--}0.084$ at $\alpha = 0.05$, Table 2) due to asymptotic Wald/likelihood-ratio approximations without small-sample degrees-of-freedom corrections.

---

## 2. Claim-by-Claim Audit

1. **Positive intra-individual correlation is universally present across diverse cell types and scRNA-seq platforms (`Fig. 1b`, `Table 1`):** `[Well Supported]`
   - The authors document elevated intra-individual versus inter-individual Spearman correlations across 10 cell types from four public datasets spanning Smart-Seq, Smart-Seq2, and 10x Genomics droplet platforms. This empirically establishes the hierarchical variance structure ($V_{\text{inter}} > 0$) that invalidates naive cell-level independence assumptions.

2. **Treating cells as independent units or applying `ComBat` across individuals prior to cell-level DE testing causes catastrophic Type I error inflation (`Table 2`, `Fig. 2`):** `[Well Supported]`
   - Under the hierarchical null simulation, naive cell-level methods (`MAST` default, `Tweedie GLM`, `Monocle`, `ROTS`) yield Type I error rates of $0.17\text{--}0.60$ at $\alpha = 0.05$, which climb with increasing cells per individual. Applying `ComBat` to remove inter-individual variance shrinks the denominator of the test statistic while leaving residual group means intact, driving Type I error rates to $0.60\text{--}0.86$ (`Table 2`).

3. **Generalized linear mixed models (`MAST+RE` two-part hurdle model and `Tweedie GLMM`) properly control Type I error across sample sizes (`Table 2`, `Fig. 3`):** `[Moderately Supported]`
   - While `MAST+RE` and `Tweedie GLMM` dramatically reduce false positives relative to unclustered cell-level models, `Table 2` shows that at $N = 5$ individuals per group (`5 Individuals`), `MAST+RE` has a Type I error rate of $0.064\text{--}0.068$ and `Tweedie GLMM` has a Type I error rate of $0.065\text{--}0.084$ at $\alpha = 0.05$ (and $0.015\text{--}0.025$ at $\alpha = 0.01$). Asymptotic $\chi^2$ and Wald tests in GLMMs are anti-conservative when the number of independent clusters ($2N = 10$) is small unless Kenward–Roger or Satterthwaite degrees-of-freedom adjustments or parametric bootstraps are applied.

4. **Mixed-effects models (`MAST+RE`) consistently outperform `DESeq2` pseudo-bulk aggregation (`Sum` and `Mean`), particularly when cell counts per individual are imbalanced (`Fig. 3d–f`, lines 92–104):** `[Methodologically Flawed]`
   - This comparative claim is an artifact of how `DESeq2` was parameterized in the single-gene simulation pipeline:
     1. In `Methods` (line 178 and chunk 2 line 8), the authors state: *"To control for any differences in library size that DESeq2 might be falsely estimating, we fixed all of DESeq2's size factors to one."*
     2. In `Fig. 3f`, the number of cells per individual $m_j$ is drawn from a negative binomial distribution with overdispersion $1$. For a gene with mean per-cell expression $\mu$, the pseudo-bulk **Sum** in individual $j$ has expectation $\mathbb{E}[\text{Sum}_j \mid m_j] = m_j \mu$. When size factors are fixed to $1.0$ instead of scaling by $m_j$ (or estimating library size across a multi-gene transcriptome), all variance in cell numbers $m_j$ across donors is absorbed directly into the within-group residual variance of $\text{Sum}_j$. This artificially inflates the dispersion estimate in `DESeq2`, driving its Type I error down to $0.008\text{--}0.017$ (`Table 2`) and collapsing its statistical power (`Fig. 3f`).
     3. Conversely, for pseudo-bulk **Mean**, averaging across $m_j$ continuous `TPM` values and rounding to integers before passing to `DESeq2` with `sizeFactors = 1` violates the negative binomial mean–variance relationship (since averaging $m_j$ cells scales the variance by $1/m_j$ without changing the mean), causing `DESeq2`'s parametric dispersion model to misestimate variance.

---

## 3. Technical & Methodological Critique

### 3.1. Single-Gene `TPM` Simulation Versus Multi-Gene UMI Count Pseudo-Bulk Workflows
- The simulation engine (`Fig. 1a`, lines 142–172) simulates continuous `TPM` values parameterized from Smart-Seq2 pancreatic $\alpha$-cells (`E-MTAB-5061`) one gene at a time. In real multi-gene scRNA-seq studies (especially droplet-based UMI count datasets), pseudo-bulk `Sum` aggregates raw integer UMI counts across cells for all $\sim 15,000\text{--}20,000$ genes simultaneously, and `DESeq2` or `edgeR` computes donor-level normalization factors (`median-of-ratios` or `TMM`) across the entire transcriptome, which naturally accounts for varying cell numbers $m_j$ and sequencing depth per donor. Evaluating `DESeq2` on single-gene rounded `TPM` sums with hardcoded `sizeFactors = 1` does not reflect how pseudo-bulk `DESeq2` operates on real multi-gene count matrices.

### 3.2. Small-Cluster Asymptotics in `MAST+RE` and `Tweedie GLMM`
- Most multi-donor scRNA-seq experiments compare $N = 3\text{--}8$ donors per condition. As shown in `Table 2` (`5 Individuals`), `MAST+RE` yields a $6.8\%$ false positive rate and `Tweedie GLMM` yields an $8.4\%$ false positive rate at a nominal $\alpha = 0.05$, whereas `GEE1` with Huber–White sandwich variance estimation yields $10.0\text{--}10.8\%$ (`Table 2`) because sandwich estimators require bias correction (e.g., Mancl–DeRouen or Kauermann–Carroll adjustment) when cluster counts are $<20$. The manuscript should explicitly caution readers that unadjusted GLMMs and GEEs remain anti-conservative at $N \le 5$ donors per group.

### 3.3. Mathematical Notation Inconsistencies in Equations (2) and (3)
- In `Methods` (`Mixed-effects hurdle model`, lines 184–196), Equations (2) and (3) write the indicator and continuous response with subscripts $k$ and $i$:
  $$\text{logit}\left(P(Z_{ki} = 1)\right) = X_i \beta_k^D + W_i \gamma_{kj}^D \quad (2)$$
  $$Y_{ki} = X_i \beta_k^C + W_i \gamma_{kj}^C + \epsilon_{ki}, \quad Z_{ki} = 1 \quad (3)$$
  Immediately below (line 194), the variable definitions switch subscripts incoherently: *"where $Y_{ig}$ is the expression level for gene $i$ and cell $k$, $Z_{ig}$ is an indicator for whether gene $i$ is expressed in cell $k$... $\gamma_{kj}^D$ and $\gamma_{kj}^C$ are normally distributed random-effects for individual $j$ with mean zero and variance $\sigma_{\gamma k}^2$."* Here, $Y_{ki}$ in Eq. (3) becomes $Y_{ig}$ in the prose, and the gene index switches between $k$, $i$, and $g$.

---

## 4. Actionable Recommendations

1. **Correct the `DESeq2` Pseudo-Bulk Benchmark Under Cellular Imbalance:**
   - Re-evaluate `DESeq2` pseudo-bulk `Sum` by either (a) simulating multi-gene count matrices ($G \ge 1,000$ genes, with $90\%$ null genes) and allowing `DESeq2::estimateSizeFactors()` to estimate donor size factors naturally, or (b) setting each donor's size factor proportional to the number of aggregated cells ($s_j = m_j / \bar{m}$) in single-gene simulations so that cell-count differences across donors are properly normalized.
2. **Incorporate Small-Sample Degrees-of-Freedom Adjustments:**
   - Benchmark Satterthwaite or Kenward–Roger degrees-of-freedom approximations (or `edgeR` quasi-likelihood `QLFTest` on pseudo-bulk counts) at $N = 3\text{--}5$ donors per group to provide well-calibrated Type I error control ($\le 0.05$) in small-cohort designs.
3. **Fix Subscript Notation in Equations (2) and (3):**
   - Harmonize the indices for gene ($g$ or $i$), cell ($k$), and individual ($j$) between Equations (2)–(3) and the accompanying variable definitions on line 194.
