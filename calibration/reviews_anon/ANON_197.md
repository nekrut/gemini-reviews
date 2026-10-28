# Review of ANON_197

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.5 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.1/3.5 | Claims: 1.0/2.5 | Biology: 1.0/2.0 | Reproducibility: 1.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript profiles the lower respiratory tract microbiome (via shotgun metagenomics at 20M reads/sample) and untargeted metabolome (via UPLC-Q-Exactive Orbitrap MS) in bronchoalveolar lavage fluid (BALF) collected from 70 lung cancer patients and 25 patients with benign pulmonary lesions at two hospitals in Tianjin, China. Using Kraken2/MetaPhlAn, HUMAnN2, LEfSe, and OPLS-DA, the authors report 104 differentially abundant microbial species (78 enriched in lung cancer, 26 in benign lesions) and 261 differentially abundant metabolites (144 upregulated, 117 downregulated in lung cancer). Applying Sequential Forward Feature Selection and a Random Forest classifier with 10-fold cross-validation to the differentially abundant species, they construct a 7-species diagnostic model (*Pseudomonas tolaasii*, *Rothia mucilaginosa*, *Klebsiella pneumoniae*, *Bifidobacterium dentium*, *Bifidobacterium longum*, *Schizosaccharomyces pombe*, and *Caulobacter* sp. FWC26) that reports an AUC of 0.931 (95% CI: 0.916–0.946). Sequencing data are deposited in the Genome Sequence Archive (GSA CRA031764).

While integrating BALF metagenomics and metabolomics in patients undergoing diagnostic bronchoscopy is a clinically relevant study design, the manuscript's primary conclusions are compromised by four severe methodological and biological flaws: (1) **asymmetric exclusion criteria and clinical confounding**—patients with interstitial lung disease (ILD), chronic bronchitis, and COPD were explicitly excluded from the lung cancer group (line 47), yet constitute **48% (12/25) of the benign control group** (Table 1: 28% ILD, 20% chronic bronchitis/COPD); (2) **data leakage in machine-learning feature selection**—the 7-species Random Forest classifier was trained via Sequential Forward Feature Selection on species *already pre-selected by LEfSe across the entire 95-patient dataset*, inflating the 10-fold CV AUC (0.931) and reporting a statistically impossible 95% confidence interval ($\pm 0.015$) for a control sample size of $n = 25$; (3) **uncontrolled low-biomass reagent/kit contamination**—no negative bronchoscope flushes, saline blanks, or DNA extraction blanks were sequenced, and key "diagnostic biomarkers" (*Schizosaccharomyces pombe* [fission yeast], *Caulobacter* sp. FWC26, *Cutibacterium acnes*, *Kocuria rhizophila*, *Acidovorax*) are classic molecular biology reagent, water, or skin contaminants; and (4) **attribution of host/eukaryotic KEGG pathways to bacteria**—reporting that HUMAnN2 bacterial metagenomics upregulated human signaling pathways (`HIF-1 signaling pathway`, `PI3K-Akt signaling pathway`) and metabolomics downregulated `Thermogenesis` and `Bile secretion`. Substantial re-analysis with contamination filtering, nested cross-validation, and confounder stratification is required.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **A 7-species BALF microbial Random Forest model distinguishes lung cancer from benign pulmonary lesions with $\text{AUC} = 0.931$ (95% CI: 0.916–0.946; Fig. 3B–C): [Methodologically Flawed].**  
  First, features were pre-filtered using LEfSe across all 95 samples before running Sequential Forward Feature Selection and 10-fold cross-validation on the same 95 samples (line 76 and line 191). Selecting features on the full dataset leaks test-fold labels into feature selection, producing severe optimistic bias. Second, with only $n = 25$ controls and $n = 70$ cases, the exact Delong/binomial 95% confidence interval around an empirical AUC of $0.931$ has a width of approximately $\pm 0.055$ to $\pm 0.065$ (i.e., $\sim [0.86, 0.99]$), not $[0.916, 0.946]$ ($\pm 0.015$). Third, two of the seven selected "biomarker" species are *Schizosaccharomyces pombe* (a model laboratory fission yeast commonly present as a carrier nucleic acid/reagent contaminant or Kraken2 k-mer false positive against residual human repetitive DNA) and *Caulobacter* sp. FWC26 (a well-known water and DNA extraction kit contaminant).

* **Taxonomic differences between lung cancer and benign control BALF reflect tumor-specific microbiota rather than clinical or environmental confounders (Table 1–2, Fig. 2): [Methodologically Flawed].**  
  In *Participants and methods* (line 47), the authors explicitly excluded patients with *"interstitial lung disease, chronic obstructive pulmonary disease (COPD)... chronic bronchitis"* from the lung cancer group, yet included 7 patients with ILD (28%) and 5 patients with chronic bronchitis/COPD (20%) in the 25-patient control group (Table 1). Thus, nearly half of the control group suffers from diffuse parenchymal or obstructive airway diseases that were barred from the cancer group. Furthermore, 71.4% (50/70) of the lung cancer patients had advanced Stage III–IV tumors (often causing post-obstructive retention of oral secretions, consistent with the enrichment of oral *Streptococcus*, *Rothia*, *Veillonella*, and *Bifidobacterium dentium*), whereas only 10 patients (14.3%) had Stage I–II disease.

* **Lung cancer patients exhibit "significantly reduced $\beta$-diversity" ($p = 0.005$ in Abstract vs. $p = 0.05, R^2 = 0.0312$ in Results line 143; Fig. 2C): [Overstated].**  
  First, the Abstract reports $p = 0.005$ while Results (line 143) reports $p = 0.05, R^2 = 0.0312$. Second, PERMANOVA ($R^2 = 0.0312$, meaning group status explains only 3.1% of Bray-Curtis variance) tests for a shift in community centroids between groups, not whether within-group $\beta$-dispersion is lower in lung cancer; visual dispersion in PCoA/NMDS is also distorted by the $70$ vs. $25$ sample size imbalance and heterogeneous control diagnoses.

* **HUMAnN2 microbial gene prediction shows upregulation of `HIF-1 signaling` and `PI3K-Akt signaling` in lung cancer microbiota (Fig. 4A–B), and BALF metabolomics shows altered `Central carbon metabolism in cancer`, `Glucagon signaling`, `Bile secretion`, and `Thermogenesis` (Fig. 5D–E): [Methodologically Flawed].**  
  Prokaryotes do not possess the eukaryotic HIF-1 or PI3K-Akt intracellular signaling cascades; their appearance in KEGG pathway mapping of HUMAnN2 outputs (or unaligned host reads) is an artifact of mapping housekeeping metabolic enzymes (e.g., enolase, GAPDH, kinases) onto global human KEGG pathway maps. Similarly, reporting unadjusted Student's $t$-test $P < 0.05$ across 1,249 identified metabolites without false discovery rate (FDR) correction (Fig. 5D caption) inflates false positives, and mapping host/microbial BALF metabolites to liver/adipose KEGG pathways (`Bile secretion`, `Thermogenesis`, `Glucagon signaling`) is biologically inappropriate for airway lavage fluid.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Eliminate Feature-Selection Data Leakage Using Nested Cross-Validation and Recompute Exact AUC Confidence Intervals
* **WHY:** Performing LEfSe and Sequential Forward Feature Selection across all 95 samples before 10-fold cross-validation leaks test-set information into the model and severely overestimates diagnostic accuracy.
* **WHAT:** Re-evaluate the Random Forest classifier using a strictly nested cross-validation pipeline where differential abundance filtering and forward feature selection are performed *exclusively inside each training fold*, and report the DeLong 95% confidence interval on the out-of-fold predictions.
* **HOW:** In each outer fold of 10-fold stratified CV ($n \approx 85$ train, $n \approx 10$ test), run Wilcoxon/LEfSe filtering and Sequential Forward Feature Selection only on the 85 training samples, fit the Random Forest, and predict the held-out 10 test samples. Aggregate the 95 out-of-fold predicted probabilities, compute the ROC curve and DeLong 95% CI using `pROC::ci.auc(roc_obj, method = "delong")` in R, and update the Abstract, line 191, and Fig. 3C.

#### 2. Match Exclusion Criteria by Removing COPD/ILD Controls and Perform Stage I–II Subgroup Sensitivity Analysis
* **WHY:** Excluding ILD, chronic bronchitis, and COPD from the cancer group while allowing them to make up 48% (12/25) of the control group introduces a severe design asymmetry.
* **WHAT:** Repeat the taxonomic and metabolomic comparisons restricting the control group to the 12 patients with focal benign nodules/masses (`Sarcoidosis/hamartoma/inflammatory nodules/granulomas`), and evaluate how the classifier performs on early-stage (Stage I–II, $n = 10$) versus late-stage (Stage III–IV, $n = 50$) lung cancer.
* **HOW:** Filter the cohort to compare Lung Cancer ($n = 70$, and separately Stage I–II $n = 10$) against Focal Benign Nodules ($n = 12$, excluding the 7 ILD, 5 COPD/chronic bronchitis, and 1 sleep apnea patients). Report whether *Streptococcus*, *Rothia mucilaginosa*, *Haemophilus influenzae*, and *Veillonella parvula* remain significantly enriched when matched against focal benign lesions.

#### 3. Screen and Filter Low-Biomass Reagent, Kit, and Eukaryotic Database Contaminants
* **WHY:** BALF has low microbial biomass and is processed with nuclease, Tween-20, QIAamp UCP Pathogen kits, reverse transcriptase (cDNA was also synthesized according to line 63, though never explained), and Nextera XT—all well-documented sources of "kitome" DNA (*Caulobacter*, *Acidovorax*, *Kocuria*, *Cutibacterium*, *Pseudomonas*) and eukaryotic database misassignments (*Schizosaccharomyces pombe*).
* **WHAT:** Apply established contaminant filtering (`decontam` using library DNA concentration measured by Qubit/qPCR in line 63, plus blacklisting known reagent/eukaryotic database artifacts) and clarify why cDNA synthesis was performed in line 63.
* **HOW:**
  1. Remove false-positive eukaryotic/fungal k-mer assignments (*Schizosaccharomyces pombe*, which frequently arises from human pericentromeric/low-complexity reads escaping GRCh38 filtering in Kraken2) by verifying whether reads assigned to *S. pombe* align to genuine *S. pombe* coding genes via BLASTn.
  2. Run the `decontam` R package (frequency method using the Q-PCR library concentrations measured in Section *Metagenomic sequencing*, line 63) to flag and remove inverse-biomass reagent contaminants (*Caulobacter* sp. FWC26, *Acidovorax*, *Kocuria rhizophila*).
  3. Clarify in *Metagenomic sequencing* (line 63) why *"cDNA transcription is performed using reverse transcriptase and dNTPs"* during a DNA metagenomic workflow.

#### 4. Apply FDR Correction to Metabolomics and Restrict Pathway Enrichment to Biologically Valid Microbial/Host Databases
* **WHY:** Testing 1,249 metabolites at unadjusted $P < 0.05$ yields $\sim 62$ false positives by chance, and reporting bacterial enrichment of `HIF-1 signaling` / `PI3K-Akt signaling` or BALF enrichment of `Thermogenesis` / `Bile secretion` reflects uncurated KEGG pathway mapping.
* **WHAT & HOW:**
  * Apply Benjamini-Hochberg FDR correction ($q < 0.05$) to all 1,249 metabolites in Fig. 5D and to the Spearman correlation matrix in Fig. 6A–B.
  * In Fig. 4A–B, report native MetaCyc microbial pathways from HUMAnN2 rather than human disease/signaling KEGG maps (`HIF-1`, `PI3K-Akt`).
  * Reconcile the $\beta$-diversity $P$-value between the Abstract ($p = 0.005$), Results line 143 ($p = 0.05$), and Fig. 2C.
