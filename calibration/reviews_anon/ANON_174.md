# Peer Review: ANON_174

**Overall Score:** **7.9 / 10.0** (Strong / Sound)
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 2.1/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.6/2.0

---

## 1. Executive Summary & Synthesis

This manuscript systematically evaluates how missing cell types in single-cell RNA-seq (scRNA-seq) reference profiles affect bulk RNA-seq deconvolution (`MuSiC`, `BayesPrism`, `CIBERSORT`, `nnls`) and tests whether non-negative matrix factorization (NMF) applied to deconvolution residuals ($R = Y - \hat{P} S$) can recover the proportions and transcriptional signatures of the unmeasured cell types. To mirror realistic tissue dissociation biases rather than arbitrary cell-type removal, the authors leverage two biological testbeds: (1) human white adipose tissue (`GSE176067`, `GSE176171`, `GSE174475`), where single-nucleus RNA-seq (snRNA-seq) captures adipocytes and mesothelial cells that are lost during enzymatic dissociation in paired scRNA-seq, and (2) high-grade serous ovarian cancer (`HGSOC`, `GSE217517`), where matched bulk RNA-seq was generated both before (`Classic`) and after (`Dissociated`) single-cell dissociation across 8 tumors.

The study is thoughtfully designed, refreshingly transparent about its scope and limitations, and highly reproducible (`[GITHUB_REPO_REDACTED]` and Zenodo archive). Rather than overselling a heuristic residual-factorization wrapper as a standalone tool, the authors explicitly state that NMF on residuals breaks down when missing cell types exceed ~50% of tissue composition alongside realistic noise, and use controlled simulations (varying reference-to-missing cell-type correlation in `PBMC3k` and missing fraction from 10% to 90% in adipose tissue) to diagnose *why* current linear deconvolution algorithms fail. The primary technical limitation lies in how negative entries in the residual matrix $R = Y - \hat{P} S$ are handled prior to NMF: adding a global constant $-\min(R)$ to shift the entire residual matrix to non-negative values introduces a rank-1 constant offset ($c \mathbf{1}\mathbf{1}^T$) that distorts the bilinear nonnegative mixing geometry.

---

## 2. Claim-by-Claim Evaluation

* **Claim 1:** *Omitting cell types present in bulk tissue from the deconvolution reference systematically degrades proportion estimates (`r` and `RMSE`) across `MuSiC`, `BayesPrism`, `CIBERSORT`, and `nnls`, with error severity governed by both the transcriptional similarity between missing and reference cell types and the total fraction of missing cells.* — **[Well Supported]**
  * **Evidence & Critique:** Using realistic adipose pseudo-bulk mixtures (built from snRNA-seq containing adipocytes and mesothelial cells, deconvolved using scRNA-seq lacking them; Fig. 1B–C), PBMC3k correlation-perturbation experiments (where CD4+ T cell profiles were synthetically mixed with B cell profiles to tune reference similarity; Fig. 3D–E), and adipose missing-percentage titrations (10% to 90%; Fig. 4A–B), the authors clearly demonstrate that missing cell types are absorbed into transcriptionally correlated reference cell types. This provides a clean empirical demonstration of collinearity bias under model misspecification.

* **Claim 2:** *Factorizing the bulk deconvolution residual matrix via NMF recovers latent factors that correlate strongly with missing cell-type proportions (`r > 0.80`) when missing cell types represent a small-to-moderate fraction of the bulk tissue (<50%) or under low noise, but degrades substantially (`r = 0.24–0.65`) in realistic high-missingness (>50%) and noisy regimes.* — **[Well Supported]**
  * **Evidence & Critique:** Figure 2A–B (`No noise` vs. `Noise` in realistic adipose pseudo-bulks where adipocytes + mesothelial cells exceed 50% of cells) and Figure 4C–D (10% to 90% missing proportion titration) honestly present both the successes and failure modes of residual NMF. The authors do not cherry-pick favorable regimes and explicitly highlight in the Discussion (`lines 125–133`) that NMF requires knowing or tuning the latent rank $k$ and struggles when missing populations dominate the tissue.

* **Claim 3:** *Comparing matched `Classic` (undissociated) and `Dissociated` bulk RNA-seq in HGSOC (`GSE217517`) reveals dissociation-induced loss of adipocytes and erythrocytes (`GSEA` on differential genes) and enables partial recovery of dissociation-sensitive components from deconvolution residuals.* — **[Moderately Supported]**
  * **Evidence & Critique:** The gene set enrichment analysis (`fgsea` against Hallmark pathways) of differentially expressed genes between `Classic` and `Dissociated` bulk RNA-seq confirms enrichment of adipogenesis and heme metabolism pathways in undissociated tissue (Fig. 5B), consistent with loss of adipocytes and red blood cells during dissociation and RBC lysis. However, the statistical comparison of estimated proportions and residual NMF/PCA factors between `Classic` and `Dissociated` bulk samples ($n = 8$ matched patients; Fig. 5D–F; Supplementary Fig. S7) uses unpaired two-sample $t$-tests across the 8 tumors (`Methods: High-grade serous ovarian carcinoma analysis`, offset 46080, lines 24–28) rather than paired tests matched by donor, reducing statistical power in a small ($n=8$) paired cohort.

---

## 3. Technical & Methodological Critique

### Major Methodological Considerations

1. **Global Constant Shift ($R \leftarrow R - \min(R)$) Prior to NMF Distorts Linear Mixing Geometry:**
   * In `Methods: Residual factorization and evaluation` (offset 46080, line 13), the residual matrix is defined as $R = Y - \hat{P}_{\text{ref}} S_{\text{ref}}$ (genes $\times$ samples). Because incomplete references cause over-estimation of correlated reference cell types ($\hat{P}_{\text{ref}} > P_{\text{ref}}$), $R$ contains negative entries. To satisfy NMF's non-negativity constraint, the authors state: *"The minimum value is subtracted from the residual matrix to ensure non-negativity (all values $\ge 0$ in the residual matrix)"*—that is, $\tilde{R}_{gs} = R_{gs} - \min_{g',s'}(R_{g's'})$.
   * Mathematically, if the true residual is $R \approx S_{\text{miss}} P_{\text{miss}} - S_{\text{ref}} \Delta P_{\text{ref}}$, adding a scalar constant $c = |\min(R)| > 0$ to every entry adds a rank-1 constant matrix $c \mathbf{1}_G \mathbf{1}_N^T$:
     $$\tilde{R} = R + c \mathbf{1}_G \mathbf{1}_N^T.$$
     Because a single large negative outlier in any gene/sample sets $c = |\min(R)|$ globally across the entire matrix, $\tilde{R}$ becomes dominated by the uniform baseline $c$, which forces NMF factors to absorb the constant offset and degrades correlation with $P_{\text{miss}}$ (especially when Gaussian noise is added, which makes $\min(R)$ much more negative!). Zero-clipping negative residuals ($\tilde{R}_{gs} = \max(R_{gs}, 0)$) or using Semi-NMF (which permits mixed-sign input $R$ and non-negative proportions $P$) avoids injecting a global constant offset across all genes and samples. This mathematical detail likely explains why adding Gaussian noise in Fig. 2B and Fig. 4D caused such a sharp drop in NMF correlation.

2. **Unpaired vs. Paired Statistical Testing in the Matched $n=8$ HGSOC Dataset:**
   * In `GSE217517`, `Classic` and `Dissociated` bulk RNA-seq profiles come from the *same* 8 tumor specimens. In `Methods: High-grade serous ovarian carcinoma analysis` (offset 46080, lines 20–28), the authors state that they used a *"non-parametric Wilcoxon t-test"* (line 22; ambiguous terminology between Wilcoxon rank-sum/signed-rank and Student's $t$-test) for estimated proportions and *"conducted a two-sample t-test on each component"* for NMF and PCA factors (`t = -3.9, p = 0.0018`, line 104). Because inter-patient tumor heterogeneity in HGSOC is large, paired tests (`paired t-test` or `Wilcoxon signed-rank test` on within-patient differences $d_i = x_{i,\text{Classic}} - x_{i,\text{Dissociated}}$) should be used throughout Figure 5.

3. **Minor Editorial and Cross-Referencing Typos:**
   * **Abstract (`line 21`):** Grammatical omission in *"Ultimately, our findings provide a path to improve existing deconvolution methods and help improve their to better account for all cell types..."* (missing noun after *"their"*, e.g., *"their ability"*).
   * **Discussion (`line 120`):** Cites `(Fig. 2)` for the PBMC3k CD4+ T cell / B cell similarity simulation (*"When a missing cell type is transcriptionally similar to reference cell types, Current methods struggle to estimate cellular proportions accurately (Fig. 2)"*); this experiment is actually **Figure 3D, E**, whereas Figure 2 is the adipose NMF residual analysis.
   * **Methods (`line 148`):** States *"Noticeably, adipocytes and mesothelial cells are missing from the single-cell data compared to the single-cell"*—the second *"single-cell"* should read *"single-nucleus"*.
   * **Authors' contributions (`offset 46080, line 50`):** Repeats *"All authors read and approved the final manuscript. All authors read and approved the final manuscript."* twice.

---

## 4. Constructive Recommendations

1. **Compare Zero-Thresholding ($\max(R, 0)$) and Semi-NMF Against Constant Shifting ($R - \min(R)$):** Evaluate whether truncating negative residuals at zero ($\max(R, 0)$) or using Semi-NMF substantially improves missing cell-type recovery in the noisy adipose simulations (Figs. 2B and 4D), since global shifting by $-\min(R)$ scales with the most extreme negative noise outlier.
2. **Use Paired Tests for Matched HGSOC Tumors:** Replace two-sample unpaired $t$-tests in Figure 5D–F and Supplementary Fig. S7 with paired $t$-tests or Wilcoxon signed-rank tests matched by patient ID (`n = 8` pairs), and clarify the exact test meant by *"Wilcoxon t-test"* in the Methods.
3. **Correct Textual Cross-References and Typos:** Fix the Figure 2 vs. Figure 3 citation in the Discussion (line 120), the grammatical error in the Abstract (line 21), the *"single-cell"* vs. *"single-nucleus"* typo in the Methods (line 148), and the duplicate sentence in Authors' contributions.
