# Review of OOD_ANON_07

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.1 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.2/3.5 | Claims: 2.3/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study systematically benchmarks how the choice of pairwise interaction statistic shapes the reconstruction, topology, biological alignment, and predictive utility of resting-state fMRI functional connectivity (FC) networks. Using resting-state BOLD time series from $N = 326$ unrelated healthy young adults in the Human Connectome Project (HCP), the authors apply the `pyspi` library to compute 239 distinct pairwise interaction statistics spanning 49 measures across 6 mathematical families (covariance, precision, distance, information-theoretic, spectral, and miscellaneous). They evaluate all 239 FC representations across six canonical neurobiological and statistical benchmarks: hub topography and weight-distance decay, diffusion MRI structure-function coupling, alignment with five independent multimodal neurophysiological networks (Allen Human Brain Atlas gene co-expression, BigBrain laminar similarity, 18-tracer PET neurotransmitter receptor similarity, MEG electrophysiological connectivity, and dynamic FDG-PET metabolic connectivity), individual fingerprinting and out-of-sample brain-behavior prediction (nested 10-fold cross-validation across 5 ICA behavioral dimensions), and integrated information decomposition ($\Phi\text{ID}$) into 16 information-flow atoms. Finally, they validate the stability of the similarity structure across parcellations (Schaefer 100, Schaefer 200, Desikan-Killiany), global signal regression, motion confounds, and six external replication cohorts ($N = 10$ to $592$).

This is an exceptionally thorough, well-controlled, and transparent methodological benchmark. The authors avoid claiming a single "best" universal estimator, instead demonstrating how precision (inverse covariance) measures excel at isolating direct anatomically mediated interactions, aligning with chemoarchitectural/electrophysiological networks, and maximizing individual fingerprinting ($\text{identifiability} > 2.1$), whereas spectral and phase-based statistics sample distinct non-redundant information-flow motifs (such as unique storage, migration, and upward/downward causation). All code, Singularity containers, and precomputed `pyspi` outputs are publicly archived on GitHub and OSF. Only minor methodological refinements—such as accounting for spatial autocorrelation (spin-test nulls) in multimodal map comparisons and preventing full-sample quartile dispersion pre-filtering prior to cross-validation—are needed.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Taxonomic clustering of 239 pairwise statistics and divergence of hub and weight-distance architectures (Figures 1–2): [Well Supported].**  
  The edge-wise Spearman correlation profiling across 239 statistics (Figure 1) and split-half stability ($r > 0.999$ across 1,000 splits, Figure 6a) robustly demonstrate that FC matrices cluster by mathematical family but exhibit wide variation in degree distributions and hub locations. In particular, the finding that precision-based estimators shift hubs from unimodal visual/somatomotor cortex toward transmodal default-mode and frontoparietal networks (Figure 2b) while preserving strong distance decay and yielding the highest structure-function coupling ($R^2 \approx 0.25$, Figure 2d) is both mathematically well-explained (by the removal of transitive/common inputs) and empirically replicated across parcellations and external datasets.

* **Differential alignment with multimodal neurophysiological networks across spatial and temporal scales (Figure 3): [Well Supported].**  
  Comparing the 239 fMRI FC matrices against five independent biological similarity matrices (transcriptomic, cytoarchitectonic, chemoarchitectonic PET, MEG amplitude-envelope connectivity, and FDG-PET metabolic covariance) plus Neurosynth cognitive co-activation provides a comprehensive multi-scale validation. The strong correspondence of covariance and precision statistics with PET receptor similarity and MEG electrophysiological connectivity—contrasted with the weak correspondence with FDG-PET metabolic connectivity—is carefully presented without overstatement, though edge-level correlations could be further strengthened by spatial autocorrelation-preserving null models.

* **Superior individual fingerprinting of precision statistics and context-dependent brain-behavior prediction (Figure 4, Supplementary Figures 7–10): [Well Supported].**  
  The fingerprinting analysis across 4 scans per participant ($N=326$) clearly shows that precision-based estimators achieve the highest individual identifiability ($> 2.1$ vs. $\sim 1.5$ for Pearson correlation), while the complementary ICC test-retest analysis (Supplementary Figure 7) clarifies how precision emphasizes inter-individual variance relative to common group structure. In the brain-behavior prediction benchmark ($N=310$), the authors properly standardize predictors within the nested 10-fold cross-validation loop and replicate across four regression models (linear KRR, cosine KRR, ridge, and LASSO), though the initial edge pre-filtering via quartile coefficient of dispersion (QCoD between 10th and 90th percentiles) was computed across the full $N=310$ cohort outside the CV loop.

* **Integrated information decomposition ($\Phi\text{ID}$) revealing that classic FC captures redundant storage while spectral/directed statistics capture unique and synergistic flow (Figure 5): [Well Supported].**  
  Using Gaussian time-delayed mutual information decomposition and dominance analysis to partition each pairwise statistic into 16 $\Phi\text{ID}$ information-flow atoms provides a principled mechanistic explanation for why different FC statistics behave differently: covariance, precision, and mutual information primarily reflect redundant information storage ($\text{Red} \to \text{Red}$), whereas partial coherence, directed transfer function, phase lag value, and transfer entropy sample unique storage, migration, and synergistic encryption/decryption.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Move Quartile Coefficient of Dispersion (QCoD) Edge Filtering Inside the Cross-Validation Loop
* **WHY:** In the "Behavior prediction" Methods section, the authors state that they computed the 10th and 90th QCoD percentiles across the $N=310$ participants to filter region pairs prior to nested 10-fold cross-validation. Although QCoD is an unsupervised variance filter (not using behavioral labels), computing edge dispersion on the full sample slightly violates strict fold isolation.
* **WHAT:** Compute the 10th–90th percentile QCoD mask strictly on the training split of each outer fold and apply that mask to the test split.
* **HOW:** Inside the outer 10-fold CV loop in the `liu_fc-pyspi` behavior prediction script, calculate `QCoD_train` across the $90\%$ training subjects, select the edge indices within the $[10\%, 90\%]$ quantile range, and index both `X_train` and `X_test` with those training-derived indices before fitting the KRR model.

#### 2. Incorporate Spatial Autocorrelation-Preserving Nulls (Moran Spectral Randomization / Spin Permutations) for Multimodal Network Alignment
* **WHY:** Both fMRI FC and biological similarity networks (gene co-expression, receptor similarity, laminar similarity, MEG) share a strong spatial distance decay ($0.2 < |r| < 0.3$ in Figure 2c). Consequently, raw Spearman rank correlations between upper-triangular matrices in Figure 3 are partially driven by shared spatial proximity rather than specific biological coupling.
* **WHAT:** Quantify the alignment in Figure 3 after regressing out Euclidean distance from both matrices or evaluate significance against spatial autocorrelation-preserving spin tests.
* **HOW:** Using `netneurotools`, compute partial Spearman correlations between each of the 239 SPI matrices and the 5 biological networks controlling for inter-regional Euclidean distance (or compare observed correlations against 1,000 cortical spin permutations of the Schaefer 100 parcellation) and add this as a supplementary panel to contextualize Figure 3.

#### 3. Quantify the Impact of Time-Series Length ($T$) on Regularization-Sensitive Precision and Information-Theoretic Estimators
* **WHY:** Precision matrices ($P \times P$ inverse covariance) and nonlinear information-theoretic estimators have estimation variance that scales with the ratio of nodes to time points ($P/T$). While HCP runs have $T = 1,200$ frames ($P/T = 100/1200 = 0.083$), typical clinical fMRI scans have $T \approx 150$–$250$ frames where unregularized precision matrices become ill-conditioned.
* **WHAT:** Add a downsampling/truncation curve showing how the identifiability and structure-function coupling of top-performing precision vs. shrinkage/covariance statistics degrade as scan duration $T$ decreases from $1,200$ to $200$ frames.
* **HOW:** On a subset of representative SPIs (e.g., Pearson correlation, empirical precision, Ledoit-Wolf shrinkage precision, and mutual information), recompute the matrices on truncatedHCP time series of length $T \in \{200, 400, 600, 800, 1200\}$ and plot fingerprinting identifiability and structure-function $R^2$ as a function of $T$.
