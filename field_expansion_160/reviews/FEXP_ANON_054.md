# Review of FEXP_ANON_054

**Overall Score:** **2.7 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **2.1 / 8.0**  
* **Score Breakdown:** Rigor: 0.7/3.5 | Claims: 0.9/2.5 | Biology: 0.5/2.0 | Reproducibility: 0.6/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Field & Subfield:** Clinical Multi-Omics / Intratumoral Microbiome and Untargeted Metabolomics in Pancreatic Cancer
* **Study Design:** Paired tumor vs. adjacent normal tissue study combining V3–V4 16S rDNA amplicon sequencing and untargeted UHPLC-Q-TOF-MS metabolomics, supplemented by public database (`TCMbio`) and internal cohort Kaplan–Meier survival curves.
* **Model System & Sample Size:** Resected human pancreatic cancer (T) and paired adjacent normal (N) tissues ($N = 47$ pairs collected; reduced post-hoc to $N = 16$ pairs for 16S microbiome analysis after PCoA outlier pruning, while $N = 42$ patients are used in the *Pseudomonas* survival curve in Figure 7C).
* **Perceived Methodological Maturity:** Extremely low; invalidated by explicit post-hoc cherry-picking of 16 out of 47 patients based on PCoA clustering dispersion, unremoved low-biomass reagent contamination (*Pseudomonas*, *Acinetobacter*, *Aeromonas*), misidentification of perioperative pharmaceuticals (`Dobutamine`, `Zaleplon`, `Terbutaline`) and industrial/lab chemicals (`Melamine`, `IBMX`) as endogenous tumor metabolites, and verbatim peer-review rebuttal text pasted directly into the Discussion.

---

## 2. Executive Summary & Editorial Verdict

This study performs V3–V4 16S rDNA sequencing and untargeted LC–MS/MS metabolomics on paired human pancreatic cancer (T) and adjacent non-cancerous (N) tissues ($N = 47$ pairs enrolled). After inspecting the 16S Principal Coordinates Analysis (PCoA), the authors discard 31 of the 47 patients (66% of the cohort) due to "high dispersion" and analyze only the remaining 16 paired patients, reporting significant differences in Shannon/Simpson alpha diversity ($P = 0.026, 0.021$), Bray–Curtis ANOSIM beta diversity ($P = 0.001$), and LEfSe enrichment of *Pseudomonas* in tumor tissues versus *Acinetobacter* and *Aeromonas* in adjacent normal tissues. In the untargeted metabolome, 298 features ($|\log_2\text{FC}| > 0.585$, unadjusted $t$-test $P < 0.05$, OPLS-DA $\text{VIP} > 1$) are flagged as altered, including numerous di-/tri-peptides, amino acid intermediates, and exogenous compounds. Correlating differential taxa with differential metabolites via Spearman rank correlation and Mantel tests, the authors conclude that intratumoral *Pseudomonas* regulates branched-chain amino acid and glutamate metabolism in pancreatic cancer and predicts worse overall survival ($P = 0.037$ in $n = 42$ internal patients; $P = 0.049$ in `TCMbio`).

**Editorial Verdict: Reject (Fundamentally Invalid).** Although the authors added extensive caveat paragraphs in the Discussion acknowledging that their mechanistic hypotheses (BCAA–mTOR and IRE1–autophagy) are unverified, the underlying empirical data and statistical analyses suffer from three fatal defects:
1. **Post-Hoc Circular Subsampling ("Cherry-Picking" 16 of 47 Patients by PCoA Dispersion):** In the Methods (line 61) and Discussion (chunk 2, line 3), the authors explicitly state that because intratumoral microbiota varied widely across the 47 patients, *"only 16 patients in the microbiome were included in the subsequent data analysis based on PCoA component analysis"* in order *"to exclude samples with high dispersion in a paired manner. This approach ensured a relatively ideal consistency within the samples of each group."* Filtering out two-thirds of the study cohort *after* inspecting the ordination plot to force tight within-group clustering and between-group separation completely invalidates all subsequent alpha diversity, ANOSIM ($P = 0.001$), LEfSe, and multi-omics correlation $P$-values.
2. **Severe Pharmaceutical, Reagent, and Industrial Chemical Contamination in the Metabolome and Microbiome:** In Results line 100 (Figure 4A) and line 113 (Figure 6), the top "upregulated metabolites in pancreatic cancer tissues" include **Dobutamine** (a synthetic intravenous inotrope used during general anesthesia/surgery), **Zaleplon** (a prescription sedative-hypnotic drug), **Terbutaline** (a synthetic bronchodilator), **1-methyl-3-isobutylxanthine (IBMX)** (a synthetic laboratory reagent), and **Melamine** (an industrial plastic/resin contaminant, which line 113 claims *"Pseudomonas may promote tumor progression by upregulating metabolites like Acetylcarnitine, Nonanoic acid, and Melamine"*!). Similarly, the dominant 16S taxa (*Pseudomonas* in T, *Acinetobacter* and *Aeromonas* in N) are canonical water/extraction-kit contaminants ("kitome") in low-biomass tissue sequencing, analyzed without any negative extraction controls or `decontam` filtering.
3. **Internal Sample-Size Contradictions and Copy-Pasted Rebuttal Text:** After excluding 31 of 47 patients from the 16S dataset (leaving $n = 16$), Figure 7C presents a Kaplan–Meier survival curve stratified by *Pseudomonas* abundance for $n = 42$ patients from the same cohort without explanation. Furthermore, the Discussion contains several pages of repetitive, unedited peer-review response text (`Our explanations and proposed solutions are as follows: ①... ②...`), broken sentences (`necroptosis and (Fig. 2 B)`), and mistranslations (`biosynthesis of unsecured fatty acids` / `unstructured fatty acids`).

### Specific Conclusions and Assessment of Support

* **Pancreatic cancer tissues exhibit distinct alpha and beta microbial diversity and significant enrichment of *Pseudomonas* compared to adjacent normal tissues: [Methodologically Flawed].**  
  Excluding 31 of 47 patient pairs (66%) based on PCoA dispersion to achieve "ideal consistency within the samples of each group" introduces extreme post-hoc selection bias that invalidates the Wilcoxon ($P = 0.021, 0.026$), ANOSIM ($P = 0.001$), and LEfSe tests. In addition, no negative blank controls or reagent decontamination procedures were executed to distinguish intratumoral *Pseudomonas* and *Acinetobacter* from DNA extraction kit/water contamination.

* **Untargeted metabolomics identifies 298 endogenous tumor-associated metabolites enriched in amino acid and peptide pathways: [Methodologically Flawed].**  
  Differential metabolites were screened using unadjusted two-sample $t$-tests ($P < 0.05$ without Benjamini–Hochberg FDR correction) rather than paired tests across the matched T/N design, and the top reported upregulated tumor metabolites (`Dobutamine`, `Zaleplon`, `Terbutaline`, `1-methyl-3-isobutylxanthine`, `Melamine`) are perioperative medications, synthetic lab chemicals, and plasticizers rather than endogenous pancreatic metabolites.

* ***Pseudomonas* regulates tumor progression by downregulating $\alpha$-ketoisovaleric acid and upregulating acetylcarnitine, nonanoic acid, and melamine: [Methodologically Flawed].**  
  Claiming that intratumoral *Pseudomonas* promotes pancreatic cancer progression by upregulating **melamine** (a synthetic triazine compound not synthesized by bacteria or mammals) based on unadjusted Spearman correlations in a post-hoc selected $n = 16$ subset is biologically and statistically untenable.

* **High intratumoral *Pseudomonas* abundance is associated with shorter overall survival in pancreatic cancer: [Fragile].**  
  In the public `TCMbio` PAAD analysis (Methods line 71, Figure 7A), the authors used an arbitrary **70% cutoff** for Overall Survival ($P = 0.049$, borderline significant only at that non-standard percentile) while using the **50% median cutoff** for Disease-Free Interval ($P = 0.015$). In their own cohort (Figure 7C, $P = 0.037$), they report $n = 42$ patients despite stating on line 61 that 31 of the 47 patients had unusable/dispersed 16S profiles and were excluded.

---

## 3. Forensic Defect Inventory

### 1. Post-Hoc PCoA Outlier Pruning of 66% of the Cohort (31/47 Patients) (Pillars 2, 3, 4)
* **Defect:** Section "Microbiome analysis (16S rDNA sequencing)" (line 61) states: *"Due to the wide variation in the expression of individual abundance of intratumoral microbiota in pancreatic adenomas, only 16 patients in the microbiome were included in the subsequent data analysis based on PCoA component analysis."* In the Discussion (chunk 2, line 3), the authors confirm that they excluded 31 pairs *"to exclude samples with high dispersion in a paired manner. This approach ensured a relatively ideal consistency within the samples of each group."* Yet Figure 7C subsequently plots 16S *Pseudomonas* survival across $n = 42$ patients.
* **WHY:** Removing two-thirds of a clinical cohort after inspecting the PCoA plot because they do not cluster cleanly by group (T vs. N) is a fatal form of circular data dredging. Under the null hypothesis (no difference between T and N), selecting the 16 pairs that happen to fall in opposite regions of PCoA space guarantees artificially small $P$-values for ANOSIM, Shannon diversity, and LEfSe.
* **WHAT:** Restore all 47 paired pancreatic tumor and adjacent normal samples to the primary 16S microbiome and multi-omics correlation analyses, and reconcile the discrepancy between $n = 47$ (enrolled), $n = 42$ (Figure 7C survival), and $n = 16$ (PCoA-pruned subset).
* **HOW:** Re-run alpha diversity (paired Wilcoxon signed-rank test), beta diversity (PERMANOVA stratified by patient ID to account for the paired design), LEfSe, and Spearman correlation analyses on the complete unpruned cohort ($N = 47$ pairs), applying Benjamini–Hochberg FDR correction ($q < 0.05$) to all tests.

### 2. Misidentification of Perioperative Drugs and Industrial Contaminants as Tumor Metabolites (Pillars 2, 4, 6)
* **Defect:** Results line 100 (Figure 4A) and line 113 (Figure 6) report `Zaleplon`, `Dobutamine`, `Terbutaline`, `1-methyl-3-isobutylxanthine`, and `Melamine` as key upregulated pancreatic cancer metabolites, and line 113 claims that *Pseudomonas* promotes tumor progression by upregulating `Melamine`. Moreover, metabolite screening used unpaired $t$-tests at unadjusted $P < 0.05$ instead of FDR-corrected paired tests.
* **WHY:** `Dobutamine`, `Terbutaline`, and `Zaleplon` are exogenous hospital medications administered to surgical patients; `1-methyl-3-isobutylxanthine` (IBMX) and `Melamine` are exogenous synthetic chemicals/contaminants. Including uncurated spectral library hits (MSI Level 3/4) and pharmaceutical xenobiotics distorts OPLS-DA models, volcano plots, and microbe–metabolite correlation networks.
* **WHAT:** Perform rigorous chemical curation to remove exogenous drugs, anesthetics, plasticizers, and LC–MS background artifacts, and re-compute differential abundance using paired $t$-tests (or paired Wilcoxon tests) with Benjamini–Hochberg FDR $< 0.05$.
* **HOW:** Cross-reference all annotated MS/MS features against HMDB endogenous metabolite filters and hospital medication records to strip xenobiotics (`Dobutamine`, `Zaleplon`, `Terbutaline`, `IBMX`, `Melamine`); recompute paired fold-changes and BH-adjusted $q$-values across all 47 patient pairs; and rebuild Figures 3–6 using verified endogenous metabolites.

### 3. Uncontrolled Low-Biomass Bacterial Contamination and Post-Hoc Survival Cutoffs (Pillars 2, 4, 5, 6)
* **Defect:** (a) No negative extraction controls, paraffin/tissue processing blanks, or statistical decontamination (`decontam`) were applied to the 16S dataset, where the top taxa (*Pseudomonas*, *Acinetobacter*, *Aeromonas*) are classic water/reagent contaminants. (b) In `TCMbio` survival analysis (line 71), the authors set the group cutoff to **70%** for OS ($P = 0.049$) but **50%** for DFI ($P = 0.015$).
* **WHY:** Tuning survival percentile cutoffs to achieve $P = 0.049$ inflates Type I error, and low-biomass tissue 16S profiles without blank controls cannot distinguish endogenous tumor colonization from extraction kit background.
* **WHAT & HOW:** Report the `TCMbio` OS curve using the same pre-specified 50% median cutoff used for DFI and internal OS (as well as continuous Cox proportional hazards regression), and apply abundance/batch contaminant filtering (`decontam` frequency method using DNA concentration) to the 16S ASV table.

### 4. Editorial Cleanup of Pasted Rebuttal Text, Mistranslations, and Data Repository Compliance (Pillar 7)
* **Defect:**
  1. The Discussion (second chunk, lines 1–5) contains ~3,000 words of unedited point-by-point peer-review rebuttal text (`Our explanations and proposed solutions are as follows: ①... ②... (v) Hypothesis-Verification Gap...`) that repeats the same arguments three times.
  2. Line 84 ends mid-clause: *"glutamatergic synapse, GABAergic_synapse, necroptosis and (Fig. 2 B)."*
  3. Line 105 mistranslates *"biosynthesis of unsaturated fatty acids"* twice—first as *"biosynthesis of unsecured fatty acids"* and then as *"biosynthesis of unstructured fatty acids"*.
  4. Line 61 refers to pancreatic ductal adenocarcinoma as *"pancreatic adenomas"* (which are benign lesions).
  5. Data Availability (line 41/73) links only to a password-protected personal Baidu Netdisk folder (`pan.baidu.com`, extraction code `6666`) rather than an international permanent repository, and the hospital name and IRB approval number are omitted in Section "Pancreatic samples sources" (line 48: *"obtained from our hospital"*), while the Acknowledgments (chunk 2, line 29) name Xiangya Hospital, Central South University.
* **WHY:** Pasted rebuttal templates, mistranslated pathway names, and non-archival cloud links do not meet scientific publishing standards.
* **WHAT & HOW:** Condense the repetitive rebuttal lists in the Discussion into a single concise Limitations paragraph; fix *"unsecured/unstructured fatty acids"* to *"unsaturated fatty acids"* and *"pancreatic adenomas"* to *"pancreatic adenocarcinomas"*; complete the broken sentence on line 84; state the exact Institutional Review Board approval number in the Methods; and deposit the raw 16S FASTQ files and raw LC–MS/MS `mzXML` files in permanent public repositories (e.g., NCBI SRA / CNCB GSA and MetaboLights / OMIX).

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.7** | **3.5** | Fatal post-hoc circularity: 31 of 47 patients (66%) were discarded after inspecting PCoA plots to remove "samples with high dispersion"; unadjusted unpaired $t$-tests used on paired metabolomics data; arbitrary 70% percentile cutoff used to obtain $P = 0.049$ in `TCMbio` OS. |
| **2. Claim-to-Evidence Alignment** | **0.9** | **2.5** | While the Conclusion adds disclaimers about causality, the Results and Discussion claim that *Pseudomonas* is the dominant intratumoral bacterium regulating amino acid metabolism and promoting tumor progression via metabolites including `Melamine`. |
| **3. Data Integrity & Biological Plausibility** | **0.5** | **2.0** | Perioperative drugs (`Dobutamine`, `Zaleplon`, `Terbutaline`), lab reagents (`IBMX`), and industrial contaminants (`Melamine`) are misidentified as endogenous pancreatic cancer metabolites; canonical reagent contaminants (*Pseudomonas*, *Acinetobacter*) reported without negative controls; unexplained jump from $n=16$ to $n=42$ in Figure 7C. |
| **4. Reproducibility & Data Integrity** | **0.6** | **2.0** | Data hosted only on a transient personal Baidu Netdisk link rather than a recognized sequence/metabolomics archive; verbatim peer-review rebuttal blocks pasted into the Discussion; mistranslations (*"unsecured/unstructured fatty acids"*, *"pancreatic adenomas"*) and missing IRB protocol number. |
| **Scientific Core Score** | **2.1** | **8.0** | Sum of Rigor (0.7) + Claims (0.9) + Biology (0.5). |
| **Overall Composite Score** | **2.7** | **10.0** | **Fundamentally Invalid Tier** (Sum of all four dimensions). |
