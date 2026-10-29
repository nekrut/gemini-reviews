# Blinded Review: SP_ANON_025
**Composite Score:** 7.6 / 10.0 (Rigor: 2.5/3.5 | Claims: 2.0/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.6/2.0)
**Bias Category:** Outer Cross-Validation Feature-Count ($F$) Selection Leakage
**Verdict:** Minor Revision
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Translational/Preclinical/Biomarker

---

### 1. Executive Summary
This manuscript presents IDEPI (IDentifying EPItopes), an open-source Python software package for learning interpretable genotype-to-phenotype predictive models from protein or nucleotide sequence alignments. IDEPI combines profile Hidden Markov Model (HMMER) sequence alignment, rich customizable feature extraction (site-specific amino acids, physicochemical properties, $k$-mers, and motifs such as potential N-linked glycosylation sites [PNGS]), minimum Redundancy Maximum Relevance (mRMR) feature ranking, and $L_1/L_2$-regularized linear support vector machines (LSVMs). The authors validate IDEPI on simulated resistance/epitope alignments and four classic HIV-1 benchmarks: Nevirapine (NVP) drug resistance, V3 loop coreceptor tropism, HIV-associated dementia (HAD) brain compartmentalization signatures, and broadly neutralizing antibody (bNAb) epitope mapping across seven mAbs.

---

### 2. Methodological & Statistical Audit
* **Hyperparameter Selection Leakage on the Outer Cross-Validation Grid (Table 2):** While the soft-margin penalty $C$ is properly tuned via nested 5-fold cross-validation inside each training fold, the number of mRMR features ($F$) reported in Table 2 was chosen by evaluating a predefined grid ($F \in [1, 90]$) and picking the value of $F$ that maximized the outer 5-fold cross-validation Matthews Correlation Coefficient (MCC) ("The number of features ($F$) was chosen by selecting a value from a pre-defined grid to maximize cross-validation MCC"). Selecting $F$ post-hoc to maximize the outer CV metric introduces optimistic selection bias, particularly in small or highly imbalanced datasets where performance fluctuates across feature counts (e.g., HAD with $N=95$ sequences and $F=90$ features, or PG9 where training accuracy reaches 0.96 at $F=60$ while CV MCC is 0.43). Fortunately, for NVP, Tropism, HAD, and PGT-121, the authors also evaluate independent held-out test cohorts, which mitigates this concern for those specific benchmarks.
* **Lack of Explicit Phylogenetic / Population Structure Control:** Linear SVMs with mRMR treat viral sequences as independent and identically distributed (i.i.d.) observations. In viral alignments spanning multiple HIV-1 subtypes (e.g., clade B vs. clade C in the PhenoSense bNAb panels), clade-defining lineage markers co-segregate with subtype-specific neutralization susceptibility. IDEPI partially addresses this by reporting correlated features ($r \ge 0.5$) alongside each mRMR-selected feature, which successfully uncovers known epistatic pairs (such as N301 and N332 for PGT-121), but does not include a phylogenetic kinship matrix or clade covariate in the classifier itself.
* **Low Sensitivity on Conformational/Balanced bNAb Epitopes:** In Table 2, performance on complex or continuous bNAbs is modest: 10E8 (MCC = 0.23, Sensitivity = 0.30), 8ANC131 (MCC = 0.19, Sensitivity = 0.28), and b12 (MCC = 0.36). The authors transparently report these numbers and explain why linear binary sequence features struggle when resistance is mediated by diverse polygenic escape pathways or subtle conformational shifts.

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim:** *IDEPI matches or outperforms specialized state-of-the-art domain tools for drug resistance (NVP), coreceptor tropism (geno2pheno/wetcat), and HAD brain signatures using a single unified linear modeling framework.* **[Well Supported]** — On independent validation datasets, IDEPI achieves MCC = 0.83 on NVP (recovering Y181C and K103N), MCC = 0.78 on V3 tropism (achieving 0.905 accuracy vs. 0.86 for specialized tools on the 137-sequence clinical validation set), and 10/10 accuracy on the Holman & Gabuzda HAD validation cohort.
* **Claim:** *mRMR + LSVM accurately recovers known structural epitope contacts and glycan dependencies for HIV-1 bNAbs directly from neutralization panels.* **[Well Supported]** — Without structural priors, IDEPI identifies K665/A667 for MPER antibody 2F5, PNGS N160 for V1/V2 apex antibody PG9, PNGS N301/N332 for V3-glycan antibody PGT-121, and PNGS N234/N276 for gp120–gp41 interface antibody 8ANC195.

---

### 4. Reproducibility & Data Completeness
* **Software and Data Packaging:** Exceptional reproducibility. IDEPI and its Cython `sklmrmr` dependency are released under open-source licenses on GitHub (`[GITHUB_REPO_REDACTED]` and `[GITHUB_REPO_REDACTED]`), packaged on PyPI, and distributed as a self-contained VirtualBox virtual machine with all benchmark alignments, validation datasets, and exact command-line workflows pre-configured.
