# Review of ANON_200

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.4 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.2/3.5 | Claims: 2.4/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript reports the findings of the international Colorectal Cancer Subtyping Consortium (CRCSC), which reconciled six independently published transcriptomic classification systems (spanning 27 individual subtype labels) across 18 colorectal cancer (CRC) datasets ($n = 4,151$ total patients; $n = 3,962$ post-QC primary tumors profiled by Affymetrix, Agilent, and Illumina RNA-seq across fresh-frozen and FFPE tissues). Using a blinded, federated workflow on Synapse where each of the six original expert groups applied their own classifier and an independent evaluation group performed Markov Cluster (MCL) network consensus clustering ($1,000$ subsampling iterations optimized by weighted Silhouette width at inflation factor $f = 3.8$), the authors establish four Consensus Molecular Subtypes (CMS): **CMS1** (MSI Immune, 14%: hypermutated,MSI-high, CIMP-high, *BRAF*-enriched, diffuse $\text{T}_{\text{H}}1$/cytotoxic immune infiltration, poor survival after relapse); **CMS2** (Canonical, 37%: epithelial, SCNA-high chromosomal instability, WNT/MYC target activation, left-sided, superior survival after relapse); **CMS3** (Metabolic, 13%: epithelial, lower SCNAs, CIMP-low, *KRAS*-enriched, prominent metabolic reprogramming, let-7 downregulation); and **CMS4** (Mesenchymal, 23%: EMT upregulation, TGF-$\beta$ activation, stromal/angiogenic infiltration, advanced stage, worst overall and relapse-free survival), alongside 13% mixed/indeterminate tumors. The authors integrate multi-omic TCGA profiles (mutations, GISTIC SCNAs, 27K/450K methylation, RPPA and LC-MS/MS proteomics, and GA/HiSeq miRNAs), clinical/survival data (including the PETACC-3 clinical trial), and release open data (`doi:10.7303/syn2623706`), code (`github.com/Sage-Bionetworks/crcsc`), and the `CMSclassifier` R package (containing both a population-level Random Forest classifier and a preprocessing-independent Single Sample Predictor [SSP]).

This is a landmark consortium study that sets a high standard for community-based molecular taxonomy reconciliation, blinded evaluation, multi-omic integration, and open tool dissemination. A few subtle methodological issues in the cross-dataset expression aggregation and classifier validation warrant clarification: (1) during data aggregation (`Online Methods` Section 5), `ComBat` was applied across all datasets using **MSI status (or an imputed transcriptomic MSI signature score)** as a protected covariate *prior* to the random 2/3 training vs. 1/3 validation split (`Section 6.1`), which introduces preprocessing coupling between training and validation samples and explicitly reinforces the MSI transcriptional axis (CMS1); and (2) CMS4's lower tumor purity (ABSOLUTE scores in `Supplementary Fig. 7e`) raises the question of how strongly macrodissection depth or stromal sampling variance influences boundaries between CMS2 and CMS4 (which accounts for the largest fraction, >23%, of mixed/unclassified tumors). Addressing these points will further strengthen the technical documentation of the CMS framework.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Six independent CRC gene-expression classification systems coalesce into four robust Consensus Molecular Subtypes (CMS1–4) covering 78% core consensus samples and 87% total classified tumors (Fig. 2, Supplementary Fig. 1): [Well Supported].**  
  The network consensus design—evaluating Jaccard similarity and BH-adjusted hypergeometric overlap ($P < 0.001$) across 27 subtype nodes from six independent groups, with MCL inflation parameter $f \in [1.6, 10]$ selected via 1,000-bootstrap stability-weighted Silhouette width—rigorously resolves prior discrepancies regarding the number and correspondence of non-MSI subtypes.

* **Multi-omic, epigenetic, proteomic, miRNA, and clinicopathological profiles distinctly characterize CMS1–4, while single driver mutations (*KRAS*, *BRAF*, *APC*, *TP53*) cannot substitute for transcriptomic subtyping (Figs. 3–5): [Well Supported].**  
  Integrative analyses across TCGA and consortium cohorts demonstrate that while *BRAF* mutations enrich in CMS1 and *KRAS* mutations in CMS3, canonical driver mutations and RTK/MAPK pathway alterations occur across multiple subtypes with distinct transcriptional and microenvironmental phenotypes. Concordance across 450K methylation (CIMP-H in CMS1, CIMP-L in CMS3), RPPA ($n=382$) and shotgun proteomics ($n=81$), and two independent TCGA miRNA cohorts (GA $n=197$, HiSeq $n=200$; `miR-17-92` in CMS2, `let-7` loss in CMS3, `miR-200` loss in CMS4) provides comprehensive biological validation.

* **CMS4 independently predicts worse overall and relapse-free survival, while CMS1 predicts poor survival after relapse (Fig. 4e–g, Supplementary Table 13): [Well Supported].**  
  Dataset-stratified univariate and multivariate Cox proportional hazards models (adjusted for clinicopathological stage, grade, site, MSI status, and *BRAF*/*KRAS* mutations) and separate validation within the uniformly followed PETACC-3 clinical trial ($n = 526$) confirm the independent prognostic value of CMS classification, including significant time-dependent AUC (tAUC) improvement in 2/3 training vs. 1/3 validation splits.

* **The Random Forest and Single Sample Predictor (`CMSclassifier`) accurately classify samples across platforms and fresh-frozen vs. FFPE tissues (>90% balanced accuracy; Supplementary Table 4 & 16): [Moderately Supported].**  
  While out-of-dataset validation on held-out TCGA RNA-seq and Affymetrix cohorts (`Section 6.4`, Supplementary Fig. 3g) and the normalization-free Single Sample Predictor (`Section 8`, Supplementary Table 16) confirm genuine cross-platform portability, two caveats apply to the Random Forest pipeline: (1) in `Section 5` (page 2, line 15), `ComBat` batch removal across the 18 datasets included known or expression-imputed MSI status as a covariate and was run on the full aggregated matrix before the random 2/3 vs. 1/3 split in `Section 6.1`; and (2) when trained on fresh-frozen samples and tested on held-out FFPE samples (PETACC-3, `Section 6.4`), sensitivity for CMS3 dropped to 0.70 (30% false-negative rate), indicating moderate FFPE degradation sensitivity for the metabolic subtype.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Evaluate the Impact of Including Imputed MSI Status in `ComBat` and Perform Pre-Processing Strictly Inside Training Splits
* **WHY:** In `Online Methods` Section 5 (page 2, line 15), when aggregating the 18 expression datasets, the authors state: *"We used ComBat to remove the per data set (batch) effect, adding MSI status as a covariate. For data that did not have MSI status, we imputed MSI status using the MSI signature score."* Passing a gene-expression-derived MSI signature score as a protected biological covariate into `ComBat` actively preserves and amplifies expression variance correlated with MSI across all 5,972 genes while shrinking orthogonal variance. Furthermore, running `ComBat` and reference-correlation probe selection (`G_REF`) across the entire 18-dataset matrix prior to splitting into training and validation sets (`Sections 6.1–6.4`) leaks test-set variance/batch parameters into the training features.
* **WHAT:** Quantify whether running `ComBat` *without* the MSI covariate (null model `mod = NULL`) alters the Random Forest validation accuracy for CMS1–4, and emphasize in the text that users classifying new external cohorts should use the Single Sample Predictor (`SSP`) or freeze the training normalization parameters rather than re-running `ComBat` with imputed MSI covariates.
* **HOW:** Re-run the `Section 6.1` and `Section 6.4` Random Forest validation splits on a `ComBat`-aggregated matrix generated with `mod = NULL` (no MSI covariate), report the resulting balanced accuracy in `Supplementary Table 4`, and add a note in `Online Methods Section 5` explaining why the `SSP` classifier (`Section 8`) is immune to cross-sample batch-correction leakage.

#### 2. Quantify the Sensitivity of CMS4 and "Mixed" Calls (CMS2–CMS4) to Stromal Admixture / Tumor Purity
* **WHY:** In `Section 7.10` (`Supplementary Fig. 7e`) and `Section 6.5` (`Supplementary Fig. 5d`), the authors show that CMS4 tumors have significantly lower tumor cell purity (higher stromal fraction by ABSOLUTE and ESTIMATE), and that the single most common mixture among the 519 unclassified samples is **CMS2–CMS4 (23%)**. Because bulk transcriptomics integrates epithelial cancer cells and surrounding cancer-associated fibroblasts, an epithelial CMS2 tumor biopsied at the invasive margin (high stroma) may shift toward CMS4 or a CMS2–CMS4 mixture.
* **WHAT:** Report a logistic or multinomial regression in the TCGA cohort ($n$ with ABSOLUTE purity) quantifying the probability of a sample being called CMS4 (or unclassified CMS2–CMS4) as a function of ABSOLUTE tumor purity, and clarify whether the multivariate Cox survival model in `Supplementary Table 13` remains significant for CMS4 vs. CMS2 when controlling for ESTIMATE stromal score or ABSOLUTE purity.
* **HOW:** In the TCGA subset with ABSOLUTE purity scores and survival data, add ABSOLUTE tumor purity (and/or ESTIMATE stromal score across all cohorts) as a covariate in the Cox model comparing CMS4 vs. CMS1–3, and discuss in the Discussion how intratumoral sampling depth (luminal core vs. invasive front) relates to the 23% CMS2–CMS4 mixed class.

#### 3. Technical and Editorial Cleanup
* **WHY:** A few minor typographical errors appear in the dataset list and figure pointers.
* **WHAT & HOW:**
  * **Line 23 (Results):** `GSE2109` is listed twice (`"GSE20916 , GSE2109 , GSE2109 , TCGA"`). Replace the duplicate entry with the 18th dataset identifier from `Supplementary Table 3` (e.g., `E-MTAB-990` / `PETACC-3`).
  * **Line 59 (Results):** Change `"( Fig. 2i , Supplementary Table 9 )"` to `"( Fig. 3i , Supplementary Table 9 )"`.
  * **Page 2, Line 64 (Online Methods Section 7):** Fix `"confirming similar variance of the groups been compared"` to `"being compared"`.
  * **Page 2, Line 142 (Online Methods Section 7.8):** Fix `"epithelial mesencgymal transition"` to `"epithelial mesenchymal transition"`.
