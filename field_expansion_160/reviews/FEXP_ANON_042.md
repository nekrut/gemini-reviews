# Forensic Review of FEXP_ANON_042

**Manuscript ID:** `FEXP_ANON_042`  
**Overall Score:** **2.6 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.9 / 8.0**  
* **Score Breakdown:** Rigor: 0.7/3.5 | Claims: 0.6/2.5 | Biology: 0.6/2.0 | Reproducibility: 0.7/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Subfield:** Cancer Microbiome & Untargeted Metabolomics / Pancreatic Ductal Adenocarcinoma (PDAC) Tumor Microenvironment.
* **Study Design:** Observational paired tumor vs. adjacent non-tumor tissue study of 23 resected PDAC patients—15 with pancreatic head cancer (`Head T` vs. `Head N`) and 8 with pancreatic body/tail cancer (`Body/Tail T` vs. `Body/Tail N`).
* **Primary Methods:** `E.Z.N.A. soil DNA Kit` extraction, 16S rRNA V3–V4 amplicon sequencing (338F/806R, UPARSE 97% OTUs), UHPLC-Q Exactive untargeted LC-MS metabolomics (Progenesis QI + HMDB/Metlin annotation), Majorbio Cloud pipeline (alpha/beta diversity, LEfSe, Wilcoxon signed-rank test, `ropls` OPLS-DA, `MASS` stepwise AIC regression, and Spearman correlation heatmaps).

---

## 2. Executive Summary & Editorial Verdict

This study profiles 16S rRNA amplicons and untargeted LC-MS metabolites in resected tumor and matched adjacent non-tumor tissues from 15 pancreatic head cancer (PHC) and 8 pancreatic body/tail cancer (PBTC) patients. Using LEfSe, Wilcoxon tests, OPLS-DA (`VIP > 1, p < 0.05` with Bonferroni correction), and stepwise AIC regression, the authors report site-specific intratumoral bacterial shifts (such as elevated *Bradyrhizobium* in `Head T` and elevated *Ileibacterium* in `Body/Tail T`), 102 Bonferroni-significant metabolites in `Head T` vs. `Head N` compared to 4 in `Body/Tail T` vs. `Body/Tail N`, and Spearman correlations linking bacterial genera to tissue metabolites.

**Editorial Verdict: Reject (Fundamentally Invalid).** Both the 16S microbiome and untargeted metabolomics datasets are dominated by unrecognised experimental, chemical, and statistical artifacts: (1) extracting ultra-low-biomass pancreatic surgical tissue with a soil DNA kit (`E.Z.N.A. soil DNA Kit`) without any negative extraction, buffer, or operating-room blank controls yields a textbook "kitome" profile dominated by reagent and environmental water/soil contaminants (*Achromobacter* and *Pedobacter* as the #1 and #2 most abundant genera in every tissue group, alongside *Bradyrhizobium*, *Pseudoxanthomonas*, *Novosphingobium*, *Curtobacterium*, and photosynthetic *Cyanobacteriales* and *Chloroplast* sequences); (2) untargeted MS1 database matching without MS/MS chemical standard verification misannotates endogenous peaks or hospital medications as synthetic laboratory crosslinkers (`N-Succinimidyl 6-maleimidohexanoate`), synthetic chemotherapy/cardiac/chelating drugs (`arabinofuranosylcytosine` [cytarabine], `buthionine sulfoximine`, `thymopentin`, `deferoxamine`, `propafenone`, `ditekiren`), and exotic plant/toad natural products (`neoporrigenin B`, `glycyrrhizin`, `cinobufotalin`, `zedoarondiol`, `kukoamine D`, `deoxyloganin`); and (3) OPLS-DA models on $n=8$ and $n=15$ samples exhibit extreme permutation overfitting ($R^2Y_{\text{perm intercept}} = 0.9001$ and $0.9676$), while comparing discovery counts between $n=15$ (102 metabolites) and $n=8$ (4 metabolites) conflates sample-size statistical power with anatomical tumor biology.

### Specific Conclusions and Assessment of Support

* **Pancreatic tumor and non-tumor tissues are colonized by resident microbiota dominated by *Achromobacter*, *Pedobacter*, *Pseudomonas*, and *Acinetobacter*, with PHC-specific enrichment of *Bradyrhizobium* and *Cyanobacteriales*: [Methodologically Flawed].**  
  Low-biomass pancreatic tissue was processed with a soil DNA extraction kit without negative reagent blanks or computational decontamination (`decontam`). *Achromobacter*, *Pedobacter*, *Pseudomonas*, *Acinetobacter*, *Bradyrhizobium* (a nitrogen-fixing legume root symbiont), *Pseudoxanthomonas*, *Novosphingobium*, and photosynthetic *Cyanobacteriales* / *Chloroplast* (lines 95, 106, 114, 122) are canonical reagent/water contaminants. Furthermore, theMethods section (line 77) states that amplicons were sequenced on an *"Illumina MiSeq PE300 platform/NovaSeq PE250 platform"*—mixing two different sequencing platforms with different read lengths (PE300 vs. PE250) and error profiles across a 23-patient cohort introduces severe technical batch bias.
* **PHC (`Head T` vs. `Head N`) exhibits 102 Bonferroni-significant differential metabolites whereas PBTC (`Body/Tail T` vs. `Body/Tail N`) exhibits only 4, demonstrating distinct site-specific metabolic reprogramming: [Methodologically Flawed].**  
  First, no direct statistical comparison between `Head T` and `Body/Tail T` (or interaction test `(Head T - Head N) vs. (Body/Tail T - Body/Tail N)`) was performed; finding 102 hits at $n=15$ pairs versus 4 hits at $n=8$ pairs under a stringent Bonferroni threshold is a predictable consequence of much lower statistical power at $n=8$. Second, the OPLS-DA permutation tests in Figures 5B and 6B report permuted $R^2$ intercepts of `0.9001` (`Head`) and `0.9676` (`Body/Tail`)—far above the standard $<0.30\text{--}0.40$ validity criterion—demonstrating severe overfitting where random label permutations explain >90% of class variance. Third, the highlighted "differential tissue metabolites" (lines 127, 135, 143) consist largely of synthetic crosslinkers (`N-Succinimidyl 6-maleimidohexanoate`), synthetic drugs (`arabinofuranosylcytosine`, `buthionine sulfoximine`, `thymopentin`, `deferoxamine`, `propafenone`, `ditekiren`), and herbal/toad compounds (`cinobufotalin`, `glycyrrhizin`, `zedoarondiol`, `neoporrigenin B`, `kukoamine D`, `deoxyloganin`), which are either MS1 database false-positive annotations or perioperative medications rather than endogenous pancreatic cancer metabolites.
* **Spearman correlations between stepwise-selected genera (*Eubacterium*, *Corynebacterium*, *Bacillus*, *Ileibacterium*) and carnitine/linoleic acid metabolites reflect functional microbiome–metabolome interactions in PDAC: [Overstated].**  
  Running `MASS::stepAIC` stepwise selection on dozens of pre-filtered genera and metabolites in cohorts of $n=8$ and $n=15$ patients and then computing unadjusted Spearman correlations (`* p < 0.05`, Fig. 7) compounds post-selection inference bias with small-sample noise.

---

## 3. Forensic Defect Inventory

### 1. Uncontrolled Low-Biomass "Kitome" Contamination and Mixed MiSeq PE300 / NovaSeq PE250 Platforms (Pillars 2, 5 & 6)
* **WHY:** Surgical pancreatic tissue has extremely low bacterial biomass. Extracting DNA with the `E.Z.N.A. soil DNA Kit` (line 77) without sequencing negative extraction blanks, surgical/paraffin controls, or PCR no-template controls violates fundamental standards for low-biomass microbiome research (RIDE criteria; Eisenhofer et al. 2019). Consequently, the reported microbiome is dominated by *Achromobacter*, *Pedobacter*, *Pseudomonas*, *Acinetobacter*, *Bradyrhizobium*, *Novosphingobium*, and plastid/cyanobacterial sequences (*Chloroplast*, *Cyanobacteriales*). In addition, line 77 states samples were sequenced on *"an Illumina MiSeq PE300 platform/NovaSeq PE250 platform"* without clarifying whether `Head` and `Body/Tail` samples were split across platforms.
* **WHAT:** Clarify which samples were sequenced on MiSeq PE300 versus NovaSeq PE250, remove chloroplast/mitochondrial/cyanobacterial and known kitome reagent contaminants, and retract claims that soil/water bacteria (*Bradyrhizobium*, *Pedobacter*, *Achromobacter*) are resident intratumoral drivers.
* **HOW:** Filter out all `Chloroplast`, `Mitochondria`, and `Cyanobacteriales` reads, apply abundance/frequency decontamination (`decontam` using DNA concentration from NanoDrop or a standard reagent contaminant blacklist), and verify whether any taxa remain significantly different between paired `T` and `N` tissues after Benjamini-Hochberg FDR correction.

### 2. Misannotated Exogenous Drugs, Synthetic Crosslinkers, and Plant/Toad Xenobiotics in Untargeted LC-MS (Pillars 2 & 6)
* **WHY:** In Sections "Differences in the metabolome..." (lines 127, 135, 143) and Figures 5D and 6D, automated Progenesis QI matching against HMDB/Metlin without filtering exogenous xenobiotics or verifying MS/MS spectra reports synthetic chemical reagents (`N-Succinimidyl 6-maleimidohexanoate`, `buthionine sulfoximine`), synthetic pharmaceuticals (`arabinofuranosylcytosine` [cytarabine, despite Exclusion Criterion II excluding preoperative chemotherapy!], `propafenone`, `deferoxamine`, `thymopentin`, `ditekiren`), and traditional Chinese medicine/plant compounds (`cinobufotalin`, `glycyrrhizin`, `zedoarondiol`, `neoporrigenin B`, `deoxyloganin`, `kukoamine D`) as top discriminative PDAC tissue metabolites.
* **WHAT:** Audit the LC-MS feature table to remove exogenous drugs, synthetic laboratory reagents, and unverified plant/animal secondary metabolite MS1 matches.
* **HOW:** Restrict metabolite reporting to endogenous human/microbial metabolites confirmed at MSI Level 1 or Level 2 (matched MS/MS fragmentation spectra and retention time), and explain whether compounds such as `cinobufotalin`, `glycyrrhizin`, `propafenone`, and `deferoxamine` reflect perioperative patient medications or isobaric MS1 misannotations.

### 3. Overfitted OPLS-DA Permutation Intercepts ($R^2Y_{\text{perm}} > 0.90$), Asymmetric Power ($n=15$ vs. $n=8$), and Unpaired Multivariate Analysis (Pillars 3, 4 & 5)
* **WHY:**
  1. In OPLS-DA permutation validation, a valid non-overfitted model requires not only $Q^2_{\text{intercept}} < 0$ but also $R^2Y_{\text{intercept}} < 0.30\text{--}0.40$. Here, the reported $R^2$ intercepts are `0.9001` (Fig. 5B, `Head`) and `0.9676` (Fig. 6B, `Body/Tail`), meaning models fit to randomly permuted class labels still explain 90%–97% of the variance in $Y$.
  2. `Head T` vs. `Head N` ($n=15$ pairs) and `Body/Tail T` vs. `Body/Tail N` ($n=8$ pairs) are paired within-patient designs, yet standard OPLS-DA and LEfSe ignore patient pairing.
  3. Comparing the count of Bonferroni-significant metabolites in `Head` (102 hits at $n=15$) against `Body/Tail` (4 hits at $n=8$) without subsampling `Head` to $n=8$ or testing the direct interaction `(Head T - Head N) - (Body/Tail T - Body/Tail N)` mistakes sample-size power differences for biological differences.
  4. Running `MASS::stepAIC` stepwise regression on $n=8$ samples is statistically invalid when the number of candidate predictors approaches or exceeds $n$.
* **WHAT:** Account for within-patient pairing, perform a direct statistical test comparing `Head` tumor-vs-normal log-fold changes against `Body/Tail` tumor-vs-normal log-fold changes, and remove `stepAIC` on $n=8$ samples.
* **HOW:** Compute within-patient paired differences $\Delta_i = \log_2(\text{Tumor}_i / \text{Normal}_i)$ for each patient, run multilevel (paired) PCA/PLS-DA using `mixOmics::pca(..., multilevel = patient_id)`, and test `Head` ($\Delta_{\text{Head}}, n=15$) vs. `Body/Tail` ($\Delta_{\text{Body/Tail}}, n=8$) directly via a two-sample Wilcoxon rank-sum test with Benjamini-Hochberg FDR adjustment.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.7** | **3.5** | OPLS-DA permutation intercepts ($R^2 = 0.9001$ and $0.9676$) indicate severe high-dimensional overfitting; unpaired LEfSe/OPLS-DA ignores the matched tumor-normal design; `stepAIC` stepwise regression on $n=8$ samples is invalid; and comparing hit counts at $n=15$ (102 hits) vs. $n=8$ (4 hits) conflates statistical power with biology. |
| **2. Claim-to-Evidence Alignment** | **0.6** | **2.5** | Core claims of distinct intratumoral microbiota and endogenous metabolic reprogramming between PHC and PBTC rest on soil-kit reagent contaminants, MS1 misannotations of synthetic drugs/crosslinkers/herbal compounds, and unadjusted $n=15$ vs. $n=8$ power asymmetry. |
| **3. Data Integrity & Biological Plausibility** | **0.6** | **2.0** | Zero negative extraction blanks in a low-biomass pancreatic tissue study using a soil DNA kit (`Achromobacter`, *Pedobacter*, *Bradyrhizobium*, *Chloroplast*, *Cyanobacteriales* reported as pancreatic flora), mixed MiSeq PE300/NovaSeq PE250 sequencing, and implausible synthetic chemical crosslinkers/drugs (`N-Succinimidyl 6-maleimidohexanoate`, `arabinofuranosylcytosine`, `buthionine sulfoximine`) reported as tissue metabolites. |
| **4. Reproducibility & Data Integrity** | **0.7** | **2.0** | Raw 16S FASTQ reads and LC-MS peak tables are not deposited in any public repository ("available from the corresponding authors... upon reasonable request"), and key sequencing batch details (which samples were sequenced on MiSeq PE300 vs. NovaSeq PE250) are omitted. |
| **Scientific Core Score** | **1.9** | **8.0** | Sum of Rigor + Claims + Biology (`0.7 + 0.6 + 0.6`). |
| **Total Composite Score** | **2.6** | **10.0** | **Fundamentally Invalid** (`0.7 + 0.6 + 0.6 + 0.7`). |
