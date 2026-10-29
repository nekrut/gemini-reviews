<Blinded Review: TIME_ANON_0790>
**Composite Score:** 7.5 / 10.0 (Rigor: 2.2/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.7/2.0)
**Bias Category:** Algorithmic/Model
**Verdict:** Minor Revision
**Study Modality:** Dry-Lab Secondary Cohort/Database
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 7.5/10
VERDICT: PASS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary (SUMMARY)
This study investigates the phylogenetic placement, duplication history, and selective constraints of six dormancy-associated MADS-box genes (*PpDAM1–6*) in peach (*Prunus persica*), which are transcriptionally silenced in the non-dormant *evergrowing* mutant. Analyzing 93 MIKC$^\text{C}$-type MADS-box coding sequences across *Arabidopsis thaliana* (39 genes), *Populus trichocarpa* (48 genes), and *Prunus persica* (6 genes) via Maximum Likelihood (`PAUP*`), Bayesian (`MrBayes 3.1.2`), and Maximum Parsimony phylogenetics alongside `PAML 4` (`CODEML`) site and branch-site models, the authors show that *PpDAM1–6* form a monophyletic clade within the *SVP*/*StMADS11* lineage (sister to poplar *PtMADS7* and *PtMADS21*), expanded via serial tandem duplications at a single locus on linkage group 1. `CODEML` analyses demonstrate strong purifying selection across the MIKC$^\text{C}$ family ($\omega_0 = 0.137$) and within the *PpDAM* clade ($\omega_0 = 0.434$), episodic positive selection on the ancestral branch leading to the *SVP*/*StMADS11* clade ($2\Delta\ell = 6.67$ for Model A1 vs. A2), and one putative positively selected C-terminal codon (site 239) within *PpDAM1–6*. While the phylogenetic placement and overarching conclusion of purifying constraint are solid, the site-selection inference on the 6-taxon *PpDAM* alignment relies on an underpowered taxon sample and Naive Empirical Bayes (NEB), and the Bayesian MCMC run for the *PpDAM* tree used only 10,000 generations.

### 2. Methodological & Statistical Audit (STRENGTHS, WEAKNESSES & METHODOLOGICAL AUDIT)
**Strengths:**
* **Multi-Method Phylogenetic Consensus:** The monophyly of *PpDAM1–6* within the *SVP*/*StMADS11* clade and their sister relationship to *PtMADS7*/*PtMADS21* are corroborated across Maximum Likelihood (`GTR+I+G`, 1,000 TBR bootstraps), Bayesian MCMC, and Maximum Parsimony, as well as conserved exon–intron structure (Figure 3).
* **Proper Branch-Site Null Comparison (Test 2):** In Table 1, the authors evaluate both the old branch-site comparison (`Model A1 vs M1a`, $df=2$, $2\Delta\ell = 19.82$) and the stringent Zhang–Nielsen–Yang Test 2 (`Model A1 vs A2` with $\omega_2 = 1$ fixed on the foreground branch, $df=1$, $2\Delta\ell = 6.67$, $p < 0.01$) for the ancestral *SVP*/*StMADS11* branch.

**Weaknesses & Methodological Audit:**
* **Underpowered 6-Taxon `CODEML` Site Analysis & Reliance on NEB:** In Table 2, site models (M0, M1a, M2a, M3, M7, M8) are fitted to only **6 peach sequences** (*PpDAM1–6*, plus outgroup *PtMADS27*). Simulation studies established that `CODEML` site-level empirical Bayes inference with $\le 6$ sequences has low statistical power and elevated false-positive rates for individual sites. Notably, the stringent `M2a vs. M1a` test is non-significant ($2\Delta\ell = 5.53$, $df=2$, $p = 0.063$), while `M8 vs. M7` is only marginally significant ($2\Delta\ell = 8.56$, $p < 0.05$). Moreover, the text states (line 136): *"The Naïve empirical Bayes of M3 and M8 models suggested one potential site under significant positive selection (Table 2): a serine-aspartate change of the C-terminal region (amino acid position 239)"*—Model M3 tests rate heterogeneity rather than positive selection, and Naive Empirical Bayes (NEB) fails to account for sampling errors in MLE parameters (unlike Bayes Empirical Bayes, BEB).
* **Insufficient MCMC Chain Length for the *PpDAM* Bayesian Tree:** In Methods ("Phylogenetic analyses", line 182), the `MrBayes` analysis for the *PpDAM* dataset was run for only **10,000 generations** (sampling every 10 generations, 250 trees burn-in), which is two orders of magnitude shorter than standard MCMC convergence practice (even for 7 taxa).
* **Minor Inconsistencies Between Text and Captions:**
  1. Methods (line 178) states the 93-taxon Bayesian tree was estimated *"using the best fit GTR+I+G substitution model"*, whereas the caption for Additional file 1 (line 203) states it was constructed using *"an HKY evolution model"*.
  2. Methods (line 191) states branch-site models were tested by *"comparing the following models: A1 vs. the null model M0"*, whereas Table 1 actually compares `A1 vs M1a [2]`.
  3. Methods (line 189) defines $\omega$ as *"ω (dS/dN rate ratio)"* (inverted numerator/denominator typo).

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim 1 (Peach *DAM1–6* genes are *SVP*/*StMADS11*-like MIKC$^\text{C}$ genes that expanded via serial tandem duplication at a single locus): `[Well Supported]`** — Strongly supported by monophyly in the 93-gene tree, physical clustering at the *evergrowing* locus on Prunus LG1, and conserved 8-exon architecture.
* **Claim 2 (Purifying selection is the predominant evolutionary force maintaining all six *PpDAM* paralogs): `[Well Supported]`** — Supported by $\omega < 1$ across pairwise comparisons, M0 ($\omega = 0.434$), and branch-homogeneous evolutionary rates ($2\Delta\ell = 11.63$, $df=11$, non-significant for free-ratio vs. M0), consistent with non-redundant seasonal expression profiles in peach buds.
* **Claim 3 (Codon 239 in the C-terminal domain of *PpDAM* experienced positive selection): `[Fragile]`** — Rests on two parallel Ser$\to$Asp substitutions (`PpDAM1` and `PpDAM3`) in a 6-gene alignment where `M2a vs. M1a` is non-significant and NEB was used under M3/M8.

### 4. Reproducibility & Data Completeness
* **High Reproducibility:** All GenBank accessions for *PpDAM1–6* (`DQ863250`–`DQ863256`), TAIR and *Populus* v1.1 gene IDs, ClustalX gap parameters, and complete aligned sequences (Figure 2 and Additional file 4) are provided directly with the manuscript.
</Blinded Review: TIME_ANON_0790>
