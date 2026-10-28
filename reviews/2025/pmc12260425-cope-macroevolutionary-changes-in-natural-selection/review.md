# Review of PMC12260425 (PMID:40591602)

**Manuscript Title:** Macroevolutionary changes in natural selection on codon usage reflect evolution of the tRNA pool across a budding yeast subphylum  
**Authors:** Cope AL, Shah P.  
**Journal / Preprint:** *Proc Natl Acad Sci U S A* (2025; `PMC12260425` / `PMID:40591602` / `10.1073/pnas.2419889122`)  
**Calibration Study Cohort:** Cohort C — Wild Literature Sample (`C51` | Double-Blinded as `ANON_181`)  
**Overall Score:** **8.0 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 1.9/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript applies a population-genetic model of codon usage bias—the Ribosomal Overhead Cost version of the Stochastic Evolutionary Model of Protein Production Rates (`ROC-SEMPPR`, implemented in `AnaCoDa`)—across 327 species in the *Saccharomycotina* budding yeast subphylum. For each species, the authors estimate codon-specific scaled selection coefficients ($\Delta \eta \propto 2 N_e s$), mutation biases ($\Delta M = \log(\mu_{i\to 0}/\mu_{0\to i})$), and evolutionary-average gene expression ($\phi_g$). To control for within-genome GC heterogeneity (such as GC-biased gene conversion), they partition genes into two clusters using correspondence analysis and `CLARA` clustering, comparing a constant-mutation (`ConstMut`) and variable-mutation (`VarMut`) model against empirical RNA-seq data (available for 49 species and mapped via one-to-one orthologs to the remaining 278 species). They find that 58/327 species ($\approx 18\%$) are better fit by `VarMut`, that predicted $\phi_g$ correlates moderately with empirical RNA-seq ($\text{median } \rho = 0.51$), and that within-species $\Delta \eta$ correlates strongly with relative tRNA adaptation index ($\Delta(1/\text{tAI})$, $\text{median } \rho = 0.70$). After excluding 34 poorly fitting outlier species, phylogenetic independent contrasts (PIC) and phylogenetic generalized least squares (PGLS) across the remaining 293 species show that across-species shifts in $\Delta \eta$ for NNA/G codons covary with changes in relative tRNA gene copy number ($\Delta(1/\text{tGCN})$), predicted expression of the Elongator Complex subunit `IKI3`, and genome-wide GC%. All analysis code (`GitHub`) and underlying genomic data (`Figshare`) are publicly available.

This is a thorough, mechanistically grounded comparative study that bridges population-genetic parameter inference with macroevolutionary phylogenetic comparative methods (`PIC`, `PGLS`, multivariate Blomberg's $K$). The explicit modeling of within-genome compositional heterogeneity (`VarMut`) and separation of NNA/G purine transitions from I34-wobble-translated NNC/T pyrimidine transitions provide clear biological insight into why tGCN co-evolves with GC content for purine-ending codons but not pyrimidine-ending codons. Nevertheless, three methodological caveats merit attention: (1) a statistical circularity in the tRNA modification analysis (Fig. 5), where the "expression" of Elongator Complex genes (`IKI3`, `ELP2`, `ELP3`) is not measured empirically via RNA-seq, but is instead the `ROC-SEMPPR` predicted $\phi_g$ inferred from the codon usage of those same genes using the species' $\Delta \eta$ vector; (2) an arbitrary 25% correlation-improvement cutoff for selecting `VarMut` over `ConstMut` that relies on cross-species ortholog mapping of RNA-seq from 49 yeasts to 278 unmeasured species; and (3) post-hoc removal of 34 species (10.4% of the dataset) based on hierarchical clustering of $\Delta \eta$. All three issues can be addressed via targeted sensitivity analyses using the authors' existing dataset and codebase.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Translational selection shapes within-genome codon usage across the majority of *Saccharomycotina* yeasts, with ~18% of species exhibiting substantial within-genome nonadaptive nucleotide heterogeneity: [Well Supported].**  
  Across 327 species, `ROC-SEMPPR` predicted expression $\phi_g$ positively correlates with empirical RNA-seq ($\text{median } \rho = 0.51$, 95% of species $\rho > 0.26$, Fig. 3B), and within-species $\Delta \eta$ strongly tracks $\Delta(1/\text{tAI})$ ($\text{median } \rho = 0.70$, 309/327 species $P < 0.05$, Fig. 3D). Accounting for within-genome GC3 heterogeneity via `VarMut` prevents regional GC biases (such as GC-biased gene conversion) from confounding $\Delta \eta$ in 58 species.

* **Across-species shifts in natural selection ($\Delta \eta$) on NNA/G codons covary with evolutionary changes in tRNA gene copy number ($\Delta(1/\text{tGCN})$) and genome-wide GC%: [Well Supported].**  
  Using phylogenetically controlled contrasts (`PIC` and `PGLS`) across 293 species, 16 of 25 testable codons show significant positive correlations between $\Delta \eta$ and $\Delta(1/\text{tGCN})$ after Benjamini–Hochberg correction (Fig. 4C–D). Furthermore, both absolute tGCN and transition selection coefficients ($\Delta \eta_{\text{NNG}} - \Delta \eta_{\text{NNA}}$) correlate significantly with genome-wide GC% for NNA/G codons ($P = 0.0005$ and $P = 0.005$, Fig. 6), whereas NNC/T codons (translated via shared $\text{tRNA}_{\text{GNN}}$ or $\text{tRNA}_{\text{INN}}$ wobble) show correlations centered near zero ($P = 0.19$–$0.71$).

* **Natural selection and mutation bias parameters exhibit low phylogenetic signal across the subphylum, with mutation biases varying more strongly among close relatives than selection coefficients: [Moderately Supported].**  
  Both cophenetic correlation ($c = 0.35$ for $\Delta \eta$ vs. $c = 0.14$ for $\Delta M$) and multivariate Blomberg's $K$ indicate rapid turnover among closely related yeasts. However, because `ConstMut` (1 mutation vector) and `VarMut` (2 mutation vectors, where only the Lower GC3% or Higher GC3% set is plugged into the clustering in Fig. 2C) are mixed together across the tree—when neighboring species sit on opposite sides of the 25% `VarMut` threshold, one species contributes a genome-wide average $\Delta M$ while its sister species contributes a partitioned sub-genome $\Delta M$, artificially inflating apparent divergence in $\Delta M$ between close relatives.

* **Across-species variation in the expression of tRNA modification enzymes (Elongator Complex `IKI3`) independently drives changes in natural selection on `AAA`, `CAA`, and `GAA` codons: [Fragile].**  
  To test whether Elongator Complex expression predicts $\Delta \eta$ for `AAA`, `CAA`, and `GAA` (Fig. 5), the authors use the `ROC-SEMPPR` *predicted* gene expression $\phi_g$ of `IKI3`, `ELP2`, and `ELP3` as the independent variable in PGLS. However, inside `ROC-SEMPPR` (Eq. 8), $\phi_g$ for gene $g$ is inferred directly from the codon counts of gene $g$ weighted by the species' $\Delta \eta_i$ and $\Delta M_i$ parameters. Because `IKI3`, `ELP2`, and `ELP3` are single genes (~400–1,300 codons) whose sequences contain `AAA`, `CAA`, and `GAA` codons, their posterior mean $\phi_g$ is mathematically coupled to $\Delta \eta_{\text{AAA}}$, $\Delta \eta_{\text{CAA}}$, and $\Delta \eta_{\text{GAA}}$ and carries substantial single-gene estimation noise. Testing this hypothesis without circularity requires validating the relationship in the 49 species with actual empirical RNA-seq measurements (or re-estimating $\phi_{\text{IKI3}}$ excluding the focal codons `AAA`/`CAA`/`GAA`).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Eliminate Mathematical Circularity in the Elongator Complex (`IKI3`/`ELP2`/`ELP3`) Analysis
* **WHY:** In Eq. [8], the posterior estimate of $\phi_g$ for a single gene (`IKI3`, `ELP2`, or `ELP3`) is a direct mathematical function of the species' selection coefficients $\Delta \eta_i$ and mutation biases $\Delta M_i$ acting on the codons present in that gene. Using $\phi_{\text{IKI3}}$ to predict $\Delta \eta_{\text{CAA}}$, $\Delta \eta_{\text{AAA}}$, and $\Delta \eta_{\text{GAA}}$ in PGLS (Fig. 5) introduces algebraic coupling between the predictor and outcome.
* **WHAT:** Validate the relationship between Elongator Complex expression and selection on `AAA`, `CAA`, and `GAA` using (a) direct empirical RNA-seq TPMs across the 49 species with measured transcriptomes, and (b) leave-focal-amino-acid-out estimates of $\phi_{\text{IKI3}}$.
* **HOW:**
  1. Subset the PGLS regression in Fig. 5B to the 49 species with direct RNA-seq data, replacing predicted $\phi_{\text{IKI3}}$ with empirical $\log(\text{TPM}_{\text{IKI3}})$.
  2. For the full 293-species analysis, compute $\phi_{\text{IKI3}}$, $\phi_{\text{ELP2}}$, and $\phi_{\text{ELP3}}$ using the posterior likelihood of Eq. [8] evaluated *only* over the remaining 17 amino acids (excluding `K-Lys`, `Q-Gln`, and `E-Glu` codons) so that $\Delta \eta_{\text{AAA}}$, $\Delta \eta_{\text{CAA}}$, and $\Delta \eta_{\text{GAA}}$ have zero algebraic contribution to the inferred expression of the Elongator subunits.

#### 2. Control for Model-Switching Artifacts (`ConstMut` vs. `VarMut`) When Quantifying Phylogenetic Signal of $\Delta M$
* **WHY:** Combining `ConstMut` species (where $\Delta M$ averages over all genes) with `VarMut` species (where $\Delta M$ is estimated on only half the genome after `CLARA` partitioning) in the hierarchical clustering and Blomberg's $K_{\text{multi}}$ calculation (Fig. 2C) creates discontinuous jumps in $\Delta M$ whenever one sister species passes the 25% `VarMut` cutoff and the other falls just below it (e.g., 24% improvement).
* **WHAT:** Recompute the cophenetic correlation and multivariate Blomberg's $K_{\text{multi}}$ for $\Delta M$ and $\Delta \eta$ using a uniform model specification across all 293 species.
* **HOW:** Calculate $c$ and $K_{\text{multi}}$ (a) using the `ConstMut` parameter estimates for all 293 species, and (b) restricting to the 235 `ConstMut`-only species, and report whether $\Delta M$ still exhibits lower phylogenetic signal than $\Delta \eta$ when model-switching discontinuities are removed.

#### 3. Perform Sensitivity Analysis on the 25% `VarMut` Selection Threshold and Cross-Species RNA-Seq Mapping
* **WHY:** Selecting `VarMut` over `ConstMut` based on a hard 25% relative improvement in Spearman correlation with empirical RNA-seq—where 278 of 327 species do not have their own RNA-seq data and instead borrow empirical expression from a distant relative—penalizes species whose closest measured relative has diverged in gene expression or whose baseline `ConstMut` correlation is already high (e.g., improving from $\rho = 0.65$ to $0.81$ is much harder than improving from $\rho = 0.20$ to $0.25$).
* **WHAT:** Evaluate whether `VarMut` assignment and downstream `PIC`/`PGLS` slopes are sensitive to the model-selection criterion.
* **HOW:** Compare the 58 species selected by the 25% relative threshold against (a) an absolute improvement threshold ($\Delta \rho \ge 0.05$ or statistically significant Steiger's $Z$-test for dependent correlations) and (b) penalized likelihood / DIC from the `AnaCoDa` MCMC chains, and verify that the across-species tGCN and GC% correlations in Figs. 4 and 6 remain invariant.

#### 4. Propagate Parameter Estimation Uncertainty into Cross-Species Regressions and Include the 34 Outlier Species as a Sensitivity Check
* **WHY:** Both `PIC` and `PGLS` treat the posterior mean $\Delta \eta$ of each species as known without error, and removing 34 species (10.4%) post-hoc based on clustering of $\Delta \eta$ could truncate real biological variance (e.g., lineages with small $N_e$ near the drift barrier).
* **WHAT:** Report sensitivity analyses for Figs. 4 and 6 across all 327 species (without excluding the 34 outliers) and weight or adjust for posterior standard errors of $\Delta \eta$.
* **HOW:** Re-run the `PIC` Spearman correlations in Fig. 4D and Fig. 6A–B on the complete 327-species tree and include the comparison in the Supplementary Material so readers can see that the core findings do not depend on excluding the 34 outlier taxa.

#### 5. Minor Editorial and Caption Corrections
* **WHY:** Several minor typographical errors appear in the figure captions and text.
* **WHAT & HOW:**
  1. Fig. 2A caption (line 59): *"Red indicates a codon is selected relative to the reference synonymous codon..., while blue indicates the codon is selected relative to the reference codon."* — Both red and blue are described as `"selected"`; change red to `"selectively disfavored ($\Delta \eta > 0$)"` and blue to `"selectively favored ($\Delta \eta < 0$)"` to match the text (line 27) and Fig. 2C caption.
  2. Line 115: *"For the other eight codons... These seven codons are mostly..."* — Reconcile `"eight codons"` vs. `"seven codons"`.
  3. Fig. 3 caption (line 74): Fix the sentence fragment *"For most species, empirical gene expressions were taken from the closest relative for which such estimates were available. using the single-copy one-to-one orthologs."*
