# Review of PMC9533319 (PMID:30936548)

**Manuscript Title:** Metagenomic analysis of colorectal cancer datasets identifies cross-cohort microbial diagnostic signatures and a link with choline degradation  
**Authors:** Thomas AM, Manghi P, Asnicar F, Pasolli E, Armanini F, Zolfo M, Beghini F, Manara S, Karcher N, Pozzi C, Gandini S, Serrano D, Tarallo S, Francavilla A, Gallo G, Trompetto M, Ferrero G, Mizutani S, Shiroma H, Shiba S, Shibata T, Yachida S, Yamada T, Wirbel J, Schrotz-King P, Ulrich CM, Brenner H, Arumugam M, Bork P, Zeller G, Cordero F, Dias-Neto E, Setubal JC, Tett A, Pardini B, Rescigno M, Waldron L, Naccarati A, Segata N.  
**Journal / Preprint:** *Nat Med* (2019; `PMC9533319` / `PMID:30936548` / `10.1038/s41591-019-0405-7`)  
**Calibration Study Cohort:** Cohort B — Validated Control (`B27` | Double-Blinded as `ANON_192`)  
**Overall Score:** **9.1 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.1/3.5 | Claims: 2.2/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents a comprehensive shotgun metagenomic meta-analysis of the colorectal cancer (CRC) fecal microbiome across nine cohorts totaling 969 samples (413 CRC, 143 adenoma, and 413 healthy controls). The authors sequence two new Italian cohorts ($n = 140$), combine them with five public CRC datasets ($n = 624$) for discovery and Leave-One-Dataset-Out (LODO) evaluation, and validate their findings on two independent cohorts from Germany and Japan ($n = 205$) as well as external non-CRC disease cohorts (Crohn's disease, ulcerative colitis, and type-2 diabetes). Using random-effects meta-analysis on standardized mean differences (adjusted for age, sex, and BMI) and Random Forest classifiers on MetaPhlAn2 and HUMAnN2 profiles, the authors demonstrate that: (1) CRC fecal metagenomes exhibit reproducibly higher species richness than controls ($P = 0.004$), partly driven by influx of oral cavity taxa ($P = 0.003$); (2) a core panel of CRC-enriched species (*Fusobacterium nucleatum*, *Peptostreptococcus stomatis*, *Parvimonas micra*, *Porphyromonas asaccharolytica*, *Solobacterium moorei*, *Clostridium symbiosum*) and amino acid putrefaction/gluconeogenesis pathways replicates across populations; (3) LODO training yields consistent cross-cohort CRC prediction (mean AUC 0.84; 0.90 and 0.81 on external validation cohorts), with near-maximal accuracy achieved using just 16 species; and (4) the choline trimethylamine-lyase gene (`cutC`) and its activating enzyme (`cutD`) are significantly enriched and overexpressed in CRC ($P = 0.001$), with disease association concentrated in specific sequence variants (*Hungatella hathewayi*, *Clostridium asparagiforme*, *Klebsiella oxytoca*, *Escherichia coli*). Raw reads (SRA SRP136711, ENA PRJEB27928, DDBJ DRA006684), processed profiles (`curatedMetagenomicData`), and machine-learning code (`bitbucket.org/CibioCM/multidataset_machinelearning`) are publicly available.

This is a rigorous, well-powered, and highly reproducible multi-cohort metagenomic study that directly resolves prior single-cohort overfitting issues through LODO validation, external cohort testing, rarefaction controls, confounder adjustment, and disease-specificity challenges. The primary limitations are minor statistical terminology errors (repeatedly mislabeling unpaired two-group comparisons as paired "Wilcoxon Signed-Rank tests"), high inter-study heterogeneity in total species richness ($I^2 = 74.8\%$), and the inability of fecal metagenomes to distinguish precancerous adenomas from healthy controls (LODO AUC 0.54), which requires tempering clinical "early screening / prognostic" framing in the Abstract.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Multi-cohort LODO Random Forest models accurately and specifically discriminate CRC from controls across geographically diverse populations (mean LODO AUC 0.84; validation AUCs 0.90 and 0.81; Figs. 2, 3, 5): [Well Supported].**  
  The authors contrast intra-cohort CV, single-dataset cross-prediction (where accuracy drops as low as AUC 0.50), and LODO validation across 7 training cohorts and 2 independent validation cohorts. Feature selection for minimal signatures (16 species or 64 gene families) is performed strictly inside training folds (excluding test cohorts) to prevent data leakage, and challenging the classifier with external UC, CD, and T2D cohorts produces only minor AUC reductions (3–9%), demonstrating disease specificity.

* **CRC metagenomes display higher total species richness ($P = 0.004$) and oral species richness/abundance ($P = 0.02$ / $P = 0.003$) than controls: [Well Supported].**  
  Because raw richness is sensitive to sequencing depth, the authors verify the increase after subsampling metagenomes to the 10th percentile of read depth in each cohort (Extended Data Fig. 1C, Fig. 5B) and after linear-model adjustment for age, sex, and BMI (Extended Data Fig. 1D–E). While between-cohort heterogeneity for total richness is substantial ($I^2 = 74.8\%, P = 0.0007$), the direction of effect is consistent across 6 of 7 discovery cohorts and replicated in both validation cohorts ($P = 0.0005$).

* **Choline TMA-lyase (`cutC`) and `cutD` genes are enriched and transcriptionally active in CRC, with clade-specific variant associations (Fig. 4, Extended Data Figs. 9–10): [Well Supported].**  
  Unlike carnitine degradation genes (`caiT`, `yeaW`), `cutC` and `cutD` show homogeneous enrichment across all 7 discovery cohorts ($\mu = 0.27, I^2 = 4.2\%, P = 0.001$ for `cutC`; $\mu = 0.32, I^2 = 0\%, P = 0.001$ for `cutD`) and replicate strongly in the validation cohorts ($P < 10^{-6}$). Reference-aided assembly further resolves why bulk gene abundance is only part of the signal: a prevalent *Lachnospiraceae* SGB 3957 `cutC` variant is control-enriched ($\text{OR} = 0.38$), whereas *Firmicutes* (*H. hathewayi* / *C. asparagiforme*, $\text{OR} = 2.14$) and *Enterobacteriaceae* ($\text{OR} = 1.85$) variants are CRC-enriched. Quantitative PCR on DNA ($n=35$) and cDNA ($n=46$) from Cohort 1 corroborates the metagenomic RPKM signal.

* **Fecal microbiome signatures cannot reliably distinguish colorectal adenomas from healthy controls (LODO AUC 0.54; zero differentially abundant species at FDR $< 0.05$): [Well Supported].**  
  Across 143 adenoma samples from 4 cohorts, both random-effects meta-analysis and LODO Random Forest classification show near-random discrimination between adenomas and healthy controls (AUC 0.46–0.58; mean 0.54). While this negative finding is transparently reported in Results (line 104), the Abstract concludes that the models *"can form the basis for clinical prognostic tests"*—which overstates prognostic/preventive utility given that the signature detects established carcinoma rather than precancerous adenoma or patient prognosis.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Audit and Correct Unpaired vs. Paired Wilcoxon Test Usage ("Wilcoxon Signed-Rank" vs. "Wilcoxon Rank-Sum")
* **WHY:** In lines 111, 114 (Fig. 4A, D, E caption), 127 (Fig. 5B caption), and 67 (Methods), the manuscript repeatedly states that $P$-values comparing CRC patients and controls were computed by *"Wilcoxon Signed-Rank test"* (e.g., comparing $n = 16$ CRC vs. $n = 19$ control DNA samples by qPCR in Cohort 1, and $n = 26$ CRC vs. $n = 20$ control cDNA samples). The Wilcoxon signed-rank test is a paired one-sample/matched-pair test that cannot be legally applied to two independent groups of unequal size ($16 \neq 19$ and $26 \neq 20$).
* **WHAT:** Verify in the R analysis scripts whether `wilcox.test(x, y, paired = FALSE)` (the Wilcoxon rank-sum / Mann-Whitney $U$ test) was actually executed, or if `wilcox.test` was inadvertently called in a one-sample mode, and correct both the text/captions and any affected $P$-values.
* **HOW:** Inspect the R calls generating Fig. 4A, Fig. 4D–E, and Fig. 5B. Ensure `wilcox.test(crc_values, ctrl_values, paired = FALSE)` is used for all independent case-control comparisons, report two-sided $P$-values alongside one-sided validation $P$-values, and replace *"Wilcoxon Signed-Rank test"* with *"Wilcoxon rank-sum (Mann-Whitney U) test"* in lines 111, 114, 127, and 67.

#### 2. Clarify Diagnostic vs. Prognostic and Early-Screening Scope in the Abstract and Discussion
* **WHY:** The Abstract states that the models *"can form the basis for clinical prognostic tests"*, but the study is cross-sectional (diagnosing existing CRC at colonoscopy, with no longitudinal survival or recurrence follow-up to assess prognosis) and fails to detect precancerous adenomas (AUC 0.54).
* **WHAT:** Replace "prognostic" with "non-invasive diagnostic / pre-colonoscopy screening for established CRC" and explicitly note in the Abstract or Discussion that adenoma detection remains a limitation of stool shotgun profiles.
* **HOW:** In the Abstract (line 8), change *"clinical prognostic tests"* to *"non-invasive diagnostic screening tests"*. In the Discussion (line 144), add a sentence noting that while carcinoma discrimination is high (AUC 0.84–0.90), the lack of signal in adenomas (AUC 0.54) indicates that the fecal taxonomic shift primarily reflects late-stage tumor microenvironment colonization rather than early pre-neoplastic initiation.

#### 3. Account for Rarefaction / Sequencing Depth Covariates in `cutC` Variant Presence/Absence Fisher Tests
* **WHY:** In line 116 and Extended Data Fig. 10B, Fisher's exact tests are applied to the number of samples in which a `cutC` sequence cluster achieved $>80\%$ breadth of coverage. Because breadth of coverage of a single-copy gene depends on both sequencing depth and overall `cutC` abundance, pooling samples across 7 cohorts with varying read depths in a crude $2 \times 2$ Fisher's exact test can be confounded by cohort-level depth differences (Simpson's paradox).
* **WHAT:** Confirm the `cutC` variant cluster associations using a stratified Cochran-Mantel-Haenszel test (blocking by cohort) or a logistic regression controlling for cohort and log library size.
* **HOW:** Run `mantelhaen.test` in R stratified by dataset (or `glm(VariantPresent ~ Group + Dataset + log10(Reads), family = binomial)`) for the four `cutC` clusters in Fig. 4C / Extended Data Fig. 10B and report the cohort-adjusted odds ratios and $P$-values.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Minor typos in figure captions and text reduce clarity regarding how overfitting was avoided and how confidence intervals behave.
* **WHAT & HOW:**
  * **Line 55 (Oral species richness meta-analysis):** The text reports *"increase was significant in meta-analysis ($\mu = 0.16$, 95% CI [$-0.03$, $0.35$], $P = 0.02$, Extended Data 2G)"*. A two-sided 95% CI of $[-0.03, 0.35]$ spans zero, which corresponds to $P \approx 0.098$, not $P = 0.02$ (unless $P = 0.02$ refers to the adjusted model or a one-sided test). Reconcile the $\mu$, 95% CI, and $P$-value with Extended Data Fig. 2G.
  * **Figure 5A caption (line 127):** Change *"Feature ranking of the 16-species model are obtained the testing cohort to avoid overfitting"* to *"Feature rankings for the 16-species model were obtained excluding the testing cohorts to avoid overfitting"*.
  * **Line 116:** Fix typo *"over the full lenght of the gene"* to *"length"*, and point *"Figure 4B"* (for the phylogenetic tree of `cutC` variants) to *"Figure 4C"*.
