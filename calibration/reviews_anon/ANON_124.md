# Critical Peer Review (`ANON_124`)

## Section 1: Overall Assessment & Quantitative Scorecard

**Overall Score:** **9.1 / 10.0** (Exemplary)
* **Score Breakdown:** Rigor: 3.2/3.5 | Claims: 2.3/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.8/2.0

**Executive Verdict:**
This multi-cohort shotgun metagenomic meta-analysis investigates the reproducibility, diagnostic specificity, and functional gene content of the fecal microbiome in colorectal cancer (CRC) across eight geographically and technically diverse cohorts ($N = 768$ total samples: five discovery cohorts of $N = 574\text{--}575$ including newly sequenced German cases and controls, plus three independent external validation cohorts of $N = 193$). The statistical and machine learning methodology—combining variance partitioning across host confounders, blocked Wilcoxon permutation tests (`coin`), generalized fold change (gFC), strictly nested cross-validation (`SIAMCAT`) with frozen normalization parameters, leave-one-study-out (LOSO) transfer, specificity benchmarking against external inflammatory bowel disease, type 2 diabetes, and Parkinson's disease cohorts, compositional log-ratio sensitivity checks, and orthogonal qPCR/RT-qPCR validation of the bile acid-inducible (`bai`) operon—sets a high standard for clinical microbiome biomarker discovery. Only minor sample-size discrepancies across text/tables and collinearity of colonoscopy timing in the newly generated German cohort detract slightly from the presentation.

---

## Section 2: Audit of Key Claims

1. **Claim 1:** *"Through a combined analysis of heterogeneous CRC cohorts, we identified reproducible microbiome biomarkers and accurate disease-predictive models that can form the basis for clinical prognostic tests and hypothesis-driven mechanistic studies."* (Section: Abstract, p. 1; Results, pp. 2–5)
   * **Tag:** `[Well Supported]`
   * **Evidence & Audit:** Across the five discovery cohorts, a core set of 29 mOTUs is significantly enriched in CRC at an FDR of $0.005$ (blocked Wilcoxon test accounting for study and colonoscopy status, Fig. 1b), including *Fusobacterium nucleatum*, *Parvimonas micra*, *Peptostreptococcus stomatis*, *Gemella morbillorum*, *Porphyromonas* spp., and *Solobacterium moorei*. LASSO classifiers trained in a LOSO design achieve an average AUROC of $0.80$ (range $0.71\text{--}0.85$, Fig. 2b), and applying these locked LOSO models to two independent Italian validation cohorts (IT1, IT2) and one Japanese cohort (JP) yields comparable AUROCs ($0.76\text{--}0.86$ after pooling, Fig. 2e), confirming cross-continental generalizability without data leakage.

2. **Claim 2:** *"Increased abundance of the bai operon was confirmed by targeted quantification showing strong association with CRC matching the power of best nasal/fecal biomarkers."* (Section: Results, "Functional characterization of the CRC microbiome", p. 6; Fig. 4c–e)
   * **Tag:** `[Well Supported]`
   * **Evidence & Audit:** Metagenomic HMM profiling of the eight-gene `bai` operon from *Clostridium* cluster XIVa species (*C. scindens*, *C. hylemonae*, *C. hiranonis*, *C. sordellii*) shows consistent enrichment across all five discovery cohorts (blocked FDR $< 10^{-5}$, Fig. 4c). The authors validate this metagenomic signal orthogonally via `baiF`-specific qPCR on fecal genomic DNA ($\text{AUROC} = 0.77$, $P = 0.001$) and RT-qPCR on fecal cDNA ($P = 4.6 \times 10^{-4}$, Fig. 4d–e) in a subset of German CRC and control samples, linking high meat/fat dietary patterns to secondary bile acid production in CRC.

3. **Claim 3:** *"To assess how predictive models of CRC perform when presented with data from patients suffering from other disorders... the false positive rate (FPR) stayed comparably low at around 10% (the expectation set for models on external healthy controls) across all inclusion criteria when presenting tasks from T2D, PD or ulcerative colitis (UC) patients."* (Section: Results, p. 5; Extended Data Fig. 4e)
   * **Tag:** `[Well Supported]`
   * **Evidence & Audit:** Unlike most microbiome machine learning studies that evaluate classifiers solely on healthy versus diseased splits within a single indication, the authors explicitly challenge their locked LOSO CRC models (calibrated at a $10\%$ FPR threshold on healthy controls) with external metagenomes from ulcerative colitis, Crohn's disease, type 2 diabetes, and Parkinson's disease cohorts. Only Crohn's disease shows a moderately elevated FPR ($21\%$ in composite models), whereas UC, T2D, and PD remain at $9\text{--}13\%$ FPR, demonstrating disease specificity.

4. **Claim 4:** *"Functional analysis using all genes of the integrated gene catalog (IGC) required cross-study aggregation... Single-gene biomarkers derived by minimum redundancy maximum relevance (mRMR) feature selection were able to classify CRC internally with high accuracy (AUROC >= 0.96, Fig. 3b), and external prediction accuracy increased with the number of discovery studies."* (Section: Results, p. 5; Fig. 3b–c)
   * **Tag:** `[Moderately Supported]`
   * **Evidence & Audit:** In Figure 3b, single-study IGC models selected via mRMR achieve near-perfect internal 5-fold cross-validation AUROCs ($\ge 0.96$), yet their external transfer AUROCs drop sharply to $0.60\text{--}0.79$. Reviewing the Methods ("Feature selection for catalog genes", p. 11) indicates that IGC genes were pre-filtered ($\ge 15\%$ non-zero across samples) and discretized into tertiles (`discretize()` in `infotheo`) before running mRMR to select 100 genes out of $>10^6$ IGC candidates. If mRMR selection or tertile discretization was performed across the full study prior to the 5-fold CV split (rather than nested strictly inside each fold), selecting 100 features from $>10^6$ genes guarantees severe in-sample overfitting ($\text{AUROC} \ge 0.96$) and explains the steep drop upon external transfer.

---

## Section 3: Technical Critique & Actionable Recommendations

### Major Methodological & Statistical Issues

1. **Collinearity of Colonoscopy Timing with Disease Status in the Newly Sequenced German (DE) Cohort (Pillar 3):**
   * **Issue:** In the Methods ("German (DE) colorectal cancer cohort and sample collection", p. 18; "Confounder analysis", p. 10), the authors note that for the newly recruited Heidelberg samples, all 60 CRC patients provided stool *after* diagnostic colonoscopy, whereas the 60 healthy controls from the PRÄVENT study did *not* undergo colonoscopy. Consequently, within the DE cohort, recent bowel preparation/colonoscopy is $100\%$ collinear with CRC status and cannot be separated from disease effect within that study alone (blocking for `colonoscopy` could only be executed within the CN cohort where sampling before vs. after colonoscopy was balanced across cases and controls).
   * **Remediation:** While the LOSO design across the remaining seven cohorts (where sampling occurred prior to colonoscopy or >1 week post-colonoscopy) confirms that the core 29-species signature is not an artifact of bowel purgatives, this complete confounding within the DE cohort should be explicitly stated as a study design limitation in the main text alongside Figure 1a.

2. **Apparent Feature-Selection Leakage in Within-Study IGC mRMR Cross-Validation (Pillar 3 & Pillar 4):**
   * **Issue:** In Figure 3b, within-study 5-fold cross-validation of 100 mRMR-selected IGC genes yields AUROCs of $0.96\text{--}0.99$ across all five cohorts, compared to $0.73\text{--}0.88$ for taxonomic LASSO models (Fig. 2a), even though external transfer of those same IGC models is inferior to taxonomic models ($0.60\text{--}0.79$ vs. $0.71\text{--}0.85$). The Methods (p. 11) describe running `mRMR.classic` to select 100 genes and subsequently training LASSO models in `SIAMCAT`, suggesting that the mRMR step was executed on the entire study dataset outside the cross-validation loop.
   * **Remediation:** Verify whether `mRMR.classic` was executed inside each training fold of the 5-fold CV in Figure 3b; if it was run on the full study prior to CV splitting, re-run mRMR strictly inside each training fold or label the diagonal of Figure 3b as in-sample feature-selected CV to prevent misinterpreting the $\ge 0.96$ AUROC as out-of-sample generalization.

### Minor Presentation & Numerical Discrepancies

1. **Sample Size Arithmetic Inconsistencies Across Text, Table 1, and Figure Captions (Pillar 7):**
   * **Abstract vs. Main Text vs. Table 1:** The Abstract reports $N = 768$ faecal metagenomes, which matches the sum of Table 1 ($386\text{ CRC cases} + 382\text{ controls} = 768$). However, the Introduction (p. 2, final paragraph) states *"386 cancer cases and 392 tumor-free controls"* (which sums to $778$, a 10-sample typo in the control count).
   * **Discovery Cohort Total ($n = 574$ vs. $n = 575$):** Summing the five discovery cohorts in Table 1 gives $114\text{ (FR)} + 109\text{ (AT)} + 128\text{ (CN)} + 104\text{ (US)} + 120\text{ (DE)} = 575$ samples, which matches Figure 1b, Figure 3c, and Figure 4a ($n = 575$). However, Figure 1a, Figure 1d, Extended Data Figure 1a, and Extended Data Figure 3 report $n = 574$ without noting which single sample was excluded.
   * **qPCR Sample Count ($n = 44$ vs. $n = 47$):** The Methods ("Quantification of `baiF` and 16S rRNA genes by qPCR", p. 13) state that qPCR was performed on *"20 control and 24 colorectal cancer samples"* ($n = 44$), whereas the Figure 4d–e legend states *"in a subset of 47 samples from the DE study"*. These counts should be reconciled.
