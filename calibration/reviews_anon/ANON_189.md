# Review of ANON_189

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.4 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.7/3.5 | Claims: 1.4/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates the association between baseline gut microbiota composition and clinical response to anti-PD-1/anti-CTLA-4 checkpoint blockade in 42 metastatic melanoma patients (16 responders [R], 26 nonresponders [NR]). Integrating 16S rRNA amplicon sequencing, metagenomic shotgun sequencing (in 39/42 patients), and targeted qPCR for 10 candidate species, the authors identify 63 differentially abundant operational taxonomic units (OTUs) and 10 species (8 enriched in R, including *Bifidobacterium longum*, *Collinsella aerofaciens*, and *Enterococcus faecium*; 2 enriched in NR). They further transfer fecal microbiota from 3 R and 3 NR patients into germ-free (GF) mice inoculated with B16.SIY melanoma cells, reporting slower tumor growth and enhanced anti-PD-L1 efficacy and SIY-specific CD8+ T cell responses in mice colonized with responder microbiota. Raw sequencing reads (SRA SRP116709) and analysis scripts (`[GITHUB_REPO_REDACTED]`) are publicly available.

While the multimodal profiling of clinical stool specimens and the gnotobiotic mouse transfer model provide an important proof-of-concept linking human gut commensals to checkpoint blockade efficacy, the statistical and experimental analyses suffer from three major methodological flaws: (1) unadjusted multiple hypothesis testing across hundreds of OTUs coupled with post-hoc inclusion of a borderline taxon (`OTU 559527`, $P = 0.058$) to match prior mouse findings; (2) severe circularity (data leakage) in evaluating PCA separation, composite qPCR scores, and the "beneficial-to-nonbeneficial OTU ratio" on the exact same 42-patient discovery cohort used for feature selection without cross-validation; and (3) pseudoreplication in the gnotobiotic mouse experiments, where heterogeneous engraftment (only 2/3 R and 2/3 NR cohorts matched donor clinical status) was followed by mechanistic and anti-PD-L1 testing restricted to a single R donor versus a single NR donor (groups A and B). Re-analyzing the human cohort with false discovery rate (FDR) control and nested cross-validation, and analyzing the mouse data with mixed-effects models accounting for donor-level clustering, are essential to align the statistical claims with the data.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Baseline human gut microbial composition significantly separates anti-PD-1 responders from nonresponders (63 OTUs; Fig. 1A, B): [Overstated].**  
  The 62 OTUs were selected using unadjusted permutation tests ($P < 0.05$) after filtering OTUs present in $<10\%$ of samples, without controlling the false discovery rate across the hundreds of tested taxa. Furthermore, a 63rd OTU (*Bifidobacteriaceae* `OTU 559527`, unadjusted $P = 0.058$) was manually added because it matched the authors' prior mouse study. Performing hierarchical clustering (Fig. 1A) and PCA (Fig. 1B) exclusively on features pre-selected for univariate differences on the same 42 samples guarantees visual separation even under a global null hypothesis.

* **A composite 10-species qPCR score ($P = 0.004$) and a beneficial-to-nonbeneficial OTU ratio $>1.5$ predict clinical response (Fig. 2D, E): [Methodologically Flawed].**  
  Both the 10-species summation qPCR score and the 43-OTU beneficial/nonbeneficial ratio were defined using the R vs. NR labels of the 42-patient cohort and then evaluated for predictive discrimination on the exact same patients without out-of-sample validation or cross-validation. Computing a Wilcoxon test ($P = 0.004$) or selecting a post-hoc decision threshold (ratio $> 1.5$) on the training set constitutes circular in-sample overfitting and cannot support claims of biomarker utility.

* **Microbiota differences outperform tumor mutational burden, PD-1/PD-L1 mRNA, and baseline CD8+ T cell infiltration in separating R from NR ($n = 15$ subset; fig. S6): [Fragile].**  
  In the 15-patient subset (5 R, 10 NR) with archived tumor tissue, comparing a pre-selected, in-sample-optimized microbiome signature against unoptimized single tumor biomarkers (nonsynonymous somatic mutations, PD-L1/PD-1 mRNA, CD8+ IHC) is an asymmetric comparison. With $n = 5$ responders, statistical power for univariate host/tumor markers is minimal, and the microbiome $P < 0.01$ reflects reusing features already selected on the parent cohort.

* **Fecal microbiota transfer from R vs. NR patients into germ-free mice recapitulates donor antitumor immunity and anti-PD-L1 efficacy (Fig. 3A–G): [Moderately Supported].**  
  Out of 6 human donors (3 R, 3 NR), 2 of 3 R cohorts and 2 of 3 NR cohorts showed the expected slow vs. fast B16.SIY baseline tumor growth (Fig. 3A), with the two discordant cohorts (C and D) exhibiting higher Bray-Curtis drift (0.7 vs. 0.5–0.6) from the human donor. However, all downstream immunological assays (IFN-$\gamma$ ELISPOT, SIY-specific CD8+ TILs, FoxP3+ Tregs) and the anti-PD-L1 efficacy experiment (Fig. 3C–F) were performed exclusively on groups A and B (representing $N = 1$ R donor [P28] and $N = 1$ NR donor [P06]). Treating 7–11 recipient mice per group as independent observations tests technical reproducibility between two specific donors rather than biological variance across R vs. NR patient populations.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Apply Global Permutational Testing and FDR Control to 16S and Shotgun Taxonomic Screens
* **WHY:** Selecting 62 OTUs at unadjusted $P < 0.05$ and manually appending a 63rd OTU at $P = 0.058$ inflates Type I error and invalidates PCA/clustering visualizations built on those selected features.
* **WHAT:** Report Benjamini-Hochberg FDR $q$-values for all tested 16S OTUs and shotgun metagenomic species, and test for global community separation prior to feature selection.
* **HOW:** Using the full unfiltered/prevalence-filtered OTU and shotgun species matrices in `sci2017_analysis`, run a global PERMANOVA (`vegan::adonis2` in R) on Bray-Curtis and UniFrac distances between R ($n=16$) and NR ($n=26$), and also on the anti-PD-1-only subset ($n=38$, excluding the 4 anti-CTLA-4 patients). Report the omnibus $R^2$ and $P$-value in Section 1 and update Tables S2, S4, and S6 with FDR-adjusted $q$-values.

#### 2. Eliminate Circularity in Biomarker Scoring via Nested Cross-Validation
* **WHY:** Evaluating the 10-species qPCR score (Fig. 2D) and the beneficial/nonbeneficial OTU ratio (Fig. 2E) on the same 42 patients used to define "beneficial" vs. "nonbeneficial" taxa produces severe optimistic bias.
* **WHAT:** Estimate out-of-fold predictive performance (AUC-ROC and sensitivity/specificity at the $>1.5$ ratio threshold) using leave-one-out or repeated stratified 5-fold cross-validation.
* **HOW:** Within each training fold (excluding the held-out test patients), identify differentially abundant OTUs ($P < 0.05$) to define the fold-specific "beneficial" and "nonbeneficial" sets, compute the ratio on the held-out patients, and aggregate out-of-fold predictions across all 42 patients to plot a cross-validated version of Fig. 2E and report the cross-validated Wilcoxon $P$-value and AUC-ROC.

#### 3. Account for Donor-Level Clustering (Pseudoreplication) in Mouse FMT Statistical Models
* **WHY:** In Fig. 3A–G, individual mice gavaged with stool from the same human donor are subsamples (technical/recipient replicates) of a single biological unit ($N = 3$ R vs. $N = 3$ NR donors in Fig. 3A; $N = 1$ R vs. $N = 1$ NR donor in Fig. 3C–F). Standard two-way ANOVA and Mann-Whitney tests across individual mice artificially inflate degrees of freedom.
* **WHAT:** Re-analyze the 6-donor tumor growth dataset (Fig. 3A) using a linear mixed-effects model with a random intercept/slope for human donor ID, and explicitly frame Fig. 3C–F as a within-donor pair (P28 vs. P06) mechanistic demonstration.
* **HOW:** Fit a linear mixed-effects model (`lme4::lmer(TumorVolume ~ DonorStatus * Day + (1 | DonorID/MouseID))`) across all 6 cohorts (A–F) to test the fixed effect of donor clinical response (`DonorStatus` = R vs. NR) on tumor growth kinetics, and report the donor-level $P$-value alongside the mouse-level curves.

#### 4. Temper Causal and Predictive Biomarker Claims in the Abstract and Text
* **WHY:** The Abstract states that FMT from responding patients leads to improved tumor control and that results suggest a mechanistic impact, while page 3 describes a "clean correlation... so that patients with a ratio over 1.5 all showed clinical response" without noting that this ratio was derived post-hoc on the same cohort and that 2 of 6 mouse FMT cohorts diverged from the donor phenotype.
* **WHAT:** Revise the Abstract and Discussion to distinguish exploratory in-sample associations from validated predictive biomarkers and to note engraftment drift in gnotobiotic mice.
* **HOW:** In the Abstract, specify that 62 OTUs were identified at unadjusted $P < 0.05$ and that FMT recapitulated donor tumor growth phenotypes in 4 of 6 tested patient donors. In the text describing Fig. 2D–E (line 32), explicitly state that the ratio $>1.5$ threshold is an in-sample exploratory summary requiring independent cohort validation.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Numerical and figure cross-reference typos between the main text and figure legends create confusion regarding OTU identifiers and figure panels.
* **WHAT & HOW:**
  * **Line 24 vs. Line 16 and Fig. 2A–C caption:** Line 24 refers to *B. longum* as `OTU 559627`, whereas Line 16 and the Fig. 1 and Fig. 2A–C captions refer to it as `OTU 559527`. Standardize the OTU ID across all text and tables.
  * **Line 44 vs. Fig. 3G:** Line 44 states *"six were observed in re-constituted mice, with the same pattern of enrichment as was seen in patients ( Fig. 2G )"*, but Fig. 2 only has panels A–E; this should reference `Fig. 3G`.
