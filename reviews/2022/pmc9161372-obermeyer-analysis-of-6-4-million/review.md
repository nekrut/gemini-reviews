# Review of PMC9161372 (PMID:35608456)

**Manuscript Title:** Analysis of 6.4 million SARS-CoV-2 genomes identifies mutations associated with fitness  
**Authors:** Obermeyer F, Jankowiak M, Barkas N, Schaffner SF, Pyle JD, Yurkovetskiy L, Bosso M, Park DJ, Babadi M, MacInnis BL, Luban J, Luban J, Sabeti PC, Lemieux JE.  
**Journal / Preprint:** *Science* (2022; `PMC9161372` / `PMID:35608456` / `10.1126/science.abm1208`)  
**Calibration Study Cohort:** Cohort B — Validated Control (`B13` | Double-Blinded as `ANON_46`)  
**Overall Score:** **7.2 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.7/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces PyR0, a hierarchical Bayesian multinomial logistic regression framework implemented in Pyro and fit via GPU-accelerated stochastic variational inference (SVI) to 6,466,300 SARS-CoV-2 genomes from GISAID (as of January 20, 2022) across 1,560 geographic regions in 14-day time bins. By partitioning 1,544 PANGO lineages into 3,000 genetic clusters and regressing cluster growth rates linearly on 2,904 nonsynonymous amino acid substitutions, PyR0 estimates relative lineage fitness ($R/R_A$) and individual mutational fitness contributions ($\Delta \log R$). The authors supplement their computational inferences with lentiviral pseudotype single-cycle infectivity assays for top receptor-binding domain (RBD) mutations and compare RBD fitness estimates against deep mutational scanning (DMS) antibody-escape scores.

PyR0 is an impressive engineering achievement that scales hierarchical multinomial growth modeling to millions of viral genomes and correctly captures the macro-evolutionary shift toward RBD-mediated immune escape in late 2021. However, its mutation-level inferences suffer from severe collinearity (linkage disequilibrium) and phylogenetic pseudoreplication that undermine several key claims: (1) in Table 1, nearly all top 20 "most significantly associated" mutations are Omicron trunk substitutions that receive virtually identical effect sizes (1.038–1.041 fold increase) because the regularized linear model evenly splits Omicron's total clade growth across its linked defining mutations; (2) Table 1 miscounts the presence of ancestral mutations across Omicron sublineages as "independent" evolutionary emergences because PyR0 lacks a phylogenetic tree; (3) mean-field/factored SVI underestimates posterior standard deviations for collinear predictors, inflating the $z$-score ranking ($\mu/\sigma$); and (4) leave-one-lineage-out cross-validation leaks information across sibling sublineages sharing the same parental backbone. Addressing these collinearity artifacts, correcting the definition of independent emergence in Table 1, and fixing several broken figure cross-references and spliced caption blocks are essential.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **PyR0 accurately infers relative lineage growth rates across 1,560 regions and detects emerging Variants of Concern from early sequence counts: [Well Supported].**  
  Multinomial logistic regression over 14-day regional counts controls for region- and time-specific testing volume and non-pharmaceutical interventions. Lineage-level fitness estimates correlate strongly with standard multinomial regressions ($R = 0.95$) and remain stable across pre- and post-Omicron dataset freezes ($\rho = 0.78$).

* **High-scoring RBD mutations correlate with DMS antibody-escape scores rather than increased intrinsic pseudovirus infectivity in ACE2/TMPRSS2 cells, indicating immune escape drove the late-2021 fitness jump: [Well Supported].**  
  Single-cycle lentiviral pseudotype assays (Fig. 3A) show that most top-ranked RBD substitutions do not individually increase target-cell infectivity on a D614G background, while cluster-level RBD $\Delta \log R$ sums correlate with multi-antibody DMS escape calculators (Fig. 3B) and spike-attributable fitness jumps sharply with Omicron's emergence in November 2021 (Fig. 3, C–E).

* **PyR0 identifies the individual contributions of 2,904 amino acid substitutions and ranks the top causal fitness-enhancing mutations via convergent evolution (Table 1): [Fragile].**  
  Inspecting Table 1 reveals a striking collinearity artifact: all 20 top-ranked mutations (e.g., S:H655Y, S:T95I, ORF1a:P3395H, S:N764K, ORF1a:K856R, S:S371L, E:T9I, S:Q954H, ORF9b:P10S, S:L981F, N:P13L, S:G339D, S:S375F, S:S477N, S:N679K, S:S373P, M:Q19E, S:D796Y, S:N969K, S:T547K) are Omicron trunk mutations, and 18 of the 20 have an identical estimated fold increase in fitness of **1.038 to 1.041**. When Omicron emerged with $>30$ simultaneous trunk substitutions and high clade growth, the shrinkage prior distributed the log-growth advantage evenly across every linked mutation on the Omicron branch—including passengers—while SVI underestimated their marginal posterior standard deviations, driving up their $\mu/\sigma$ significance rank. Furthermore, the final column of Table 1 claims to report the "number of PANGO lineages in which each substitution emerged independently," listing 2 to 6 lineages for Omicron-specific mutations like S:L981F (2), ORF1a:K856R (2), S:S371L (3), S:T547K (3), and E:T9I (5). These do not represent independent convergent origins; they represent descendant PANGO sublineages of Omicron (e.g., BA.1, BA.1.1, BA.2, BA.3) that inherited the mutation from a single common ancestor.

* **Leave-one-out cross-validation proves PyR0 can predict the fitness of completely new lineages from their mutational profile ($R = 0.983$): [Overstated].**  
  Withholding a single PANGO lineage ( out of 1,544) while retaining its parent, sister, and descendant PANGO sublineages in the training set means that almost the exact same constellation of mutations remains in the model. Reporting $R = 0.983$ across all PANGO lineages measures interpolation across closely related sublineages (e.g., predicting AY.4.2 from AY.4, or BA.1.1 from BA.1), not de novo prediction of a saltational lineage like BA.1 from pre-Omicron training data. Indeed, the manuscript notes that individual amino acid effects correlated at only $\rho = 0.48$ between the August 2021 (pre-Omicron) and January 2022 (post-Omicron) fits.

* **Omicron BA.2 has a relative fitness ($R/R_A$) 8.9-fold (95% CI, 8.6–9.2) higher than the original Wuhan A lineage: [Overstated].**  
  Converting cumulative logistic growth rate differences into a fold multiplier on $R$ ($R/R_A = 8.9$) assumes a constant 5.5-day generation time across all variants and a constant susceptibility environment over two years. Because BA.2 spread in a heavily vaccinated and previously infected population where ancestral variants faced strong immune neutralization—and because Omicron exhibits a shorter generation time (~3–3.5 days) than ancestral Wuhan-Hu-1—the 8.9-fold quantity reflects net competitive growth advantage across sequential selective regimes rather than an 8.9-fold increase in intrinsic basic reproduction number ($R_0$).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct the Phylogenetically Confounded "Independent Emergence" Counts in Table 1 and Quantify Collinearity
* **WHY:** Counting the number of PANGO lineages carrying a mutation as the number of times it "emerged independently" (Table 1) is evolutionary pseudoreplication: descendant sublineages of a clade inherit ancestral trunk mutations by common descent, not convergent evolution. Moreover, the uniform ~1.040 fold-change estimates in Table 1 reflect ridge-like shrinkage splitting Omicron's clade effect across collinear trunk mutations.
* **WHAT:** Replace raw PANGO lineage presence counts with actual phylogenetic parsimony homoplasy counts on the global SARS-CoV-2 tree, and diagnose posterior collinearity among co-occurring Omicron mutations.
* **HOW:** Map the 2,904 mutations onto the UShER/PANGO phylogenetic tree of the 3,000 clusters to count true independent mutational origins along branches. In Table 1, report both the number of clusters carrying the mutation and the true number of independent branch origins, and add a sensitivity analysis comparing mutation rankings when mutations occurring on $<3$ independent phylogenetic branches are excluded or grouped into haplotype blocks.

#### 2. Perform Clade-Blocked Cross-Validation to Test De Novo Variant Prediction
* **WHY:** Leave-one-PANGO-lineage-out cross-validation leaks information from sibling sublineages sharing the same ancestral mutations.
* **WHAT:** Evaluate out-of-clade predictive accuracy by holding out entire WHO Variant of Concern clades (e.g., all Alpha, all Delta/AY.*, or all Omicron BA.* sublineages) simultaneously.
* **HOW:** Re-run the mutational prediction benchmark when holding out all clusters belonging to each major VoC clade (or evaluating the August 2021 pre-Omicron model's mutational coefficients on the initial BA.1 and BA.2 genotypes), and report the clade-blocked correlation alongside the single-lineage leave-one-out result.

#### 3. Calibrate SVI Posterior Uncertainty Against MCMC or Bootstrap Baselines and Vary Generation Time
* **WHY:** Stochastic variational inference with factored variational distributions systematically underestimates marginal posterior variance when regression predictors (mutations) are strongly correlated, producing overly narrow credible intervals (e.g., $R/R_A = 8.9$, 95% CI 8.6–9.2) and inflated $\mu/\sigma$ significance scores.
* **WHAT:** Quantify the degree of variance underestimation in SVI and test sensitivity of $R/R_A$ to shorter generation times in Delta and Omicron.
* **HOW:** On a regional subset of the data, compare the SVI posterior standard deviations of mutational effects against Hamiltonian Monte Carlo (NUTS in Pyro/NumPyro) or spatial block-bootstrapping across the 1,560 regions. Additionally, report a sensitivity interval for $R/R_A$ when generation time decreases from 5.5 days (ancestral) to 3.0–4.0 days (Omicron).

#### 4. Fix Spliced Figure Captions, Typos, and Broken Figure Cross-References
* **WHY:** The manuscript text contains multiple copy-editing errors where figure caption blocks are pasted directly into the body paragraphs, alongside misnumbered figure cross-references.
* **WHAT & HOW:**
  * Remove the orphaned caption fragments spliced into the main text at Lines 20, 28, 32, and 36 (which duplicate the Figure/Table captions at Lines 48 and 75–77).
  * Line 18: Fix the duplicate word typo *"typically stabilized typically stabilized"* $\rightarrow$ *"typically stabilized"*.
  * Line 34: Fix the broken cross-reference *"adjacent to the S-ACE2 interface (Fig. 3E)"* $\rightarrow$ *"(Fig. 2E)"* (since Fig. 2E shows the RBD-ACE2 interface, whereas Fig. 3E shows non-S-gene $\Delta \log R$).
  * Line 34: Fix the supplementary figure references for the viral replication and protein processing structures (*"fig. S15"* and *"fig. S16"* at the end of the paragraph conflict with *"the polymerase (fig. S23), and two proteases (fig. S24)"* two sentences earlier, whereas figs. S15 and S16 are correlation and convergent evolution plots).
