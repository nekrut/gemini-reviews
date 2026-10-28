# Review of ANON_148

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **2.1 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.5/3.5 | Claims: 0.6/2.5 | Biology: 0.6/2.0 | Reproducibility: 0.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This short cross-sectional study investigates gut microbiota composition in 132 adult outpatients (72 diagnosed with non-alcoholic fatty liver disease [NAFLD] via abdominal ultrasonography and 60 age- and sex-matched healthy controls, aged 25–60 years) at a tertiary care hospital using Illumina MiSeq V3–V4 16S rRNA amplicon sequencing. The text summarizes ten unnumbered/external tables (`Table 1 (see PDF)` through `Table 10 (see PDF)`), asserting that NAFLD patients had higher BMI, waist circumference, blood pressure, ALT, AST, fasting glucose, insulin, and HOMA-IR, reduced alpha diversity (Shannon, Simpson, Chao1), increased *Firmicutes* and *Proteobacteria* with decreased *Bacteroidetes*, elevated *Escherichia*, *Enterococcus*, and *Clostridium* with reduced *Bacteroides* and *Prevotella*, a severity gradient across mild/moderate/severe steatosis, and an ROC AUC $> 0.79$ for the Shannon index and *Firmicutes* abundance. No raw sequencing reads, accession numbers, bioinformatic pipeline details, ethics approval identifiers, or numerical data tables are included in the manuscript text.

As a scientific report, this manuscript is fundamentally incomplete and unverifiable. Throughout the entire Results section (line 25), almost no numerical values, means, standard deviations, odds ratios, confidence intervals, correlation coefficients, or exact $p$-values are reported—apart from a single inequality (`AUC > 0.79`) and the sample counts ($N = 132, 72, 60$)—with the text instead consisting of generic qualitative prose descriptions pointing to ten missing tables (`Table 1 (see PDF)` to `Table 10 (see PDF)`). Furthermore, the Methods section omits the entire 16S rRNA bioinformatic workflow (no mention of primer sequences, read depth, denoising/clustering software such as DADA2/QIIME2, taxonomic reference database, rarefaction depth, or compositional normalization), offers no multiple-testing correction across taxa, and fails to provide an Institutional Review Board (IRB) approval number or a public sequencing data accession (SRA/ENA). In its current state, the manuscript provides no auditable quantitative evidence to support its claims.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **NAFLD patients exhibit significantly reduced alpha diversity (Shannon, Simpson, Chao1), increased *Firmicutes* and *Proteobacteria*, reduced *Bacteroidetes*, and altered genus-level abundances (*Escherichia*, *Enterococcus*, *Clostridium*, *Bacteroides*, *Prevotella*) compared to controls: [Methodologically Flawed].**  
  Not a single mean, median, interquartile range, relative abundance percentage, test statistic, or $p$-value is presented in the text (`Table 3 (see PDF)`, `Table 4 (see PDF)`, `Table 5 (see PDF)` are omitted), and the Methods fail to specify how 16S V3–V4 reads were processed, assigned to taxa, rarefied, or corrected for multiple hypothesis testing (FDR) or compositional closure.

* ***Firmicutes* abundance and HOMA-IR are independent predictors of NAFLD in multivariate logistic regression after adjusting for age, BMI, and lipid profile, and Shannon diversity / *Firmicutes* achieve AUC $> 0.79$ for NAFLD detection: [Methodologically Flawed].**  
  Because ultrasound-diagnosed NAFLD is strongly coupled with obesity and metabolic syndrome (as acknowledged in the description of Table 1, where NAFLD patients had significantly higher BMI, waist circumference, and blood pressure), entering unstandardized compositional phylum percentages alongside HOMA-IR and BMI without reporting regression coefficients ($\beta$), odds ratios, 95% CIs, collinearity diagnostics (VIF), or internal cross-validation for the ROC curve (`Table 8` and `Table 9` are absent) precludes any verification that the microbiome adds predictive value beyond BMI and HOMA-IR.

* **Gut microbiota dysbiosis exhibits a progressive dose-response gradient across mild, moderate, and severe hepatic steatosis (`Table 7`): [Unsupported / Overstated].**  
  Standard B-mode abdominal ultrasonography has limited sensitivity for mild steatosis ($<20\text{–}30\%$ hepatocyte fat) and poor inter-observer reproducibility for grading mild vs. moderate vs. severe steatosis compared to FibroScan (CAP), MRI-PDFF, or biopsy. Neither the grading criteria, the subgroup sample sizes ($n_{\text{mild}}, n_{\text{moderate}}, n_{\text{severe}}$), nor the multi-group test statistics (ANOVA/Kruskal-Wallis) are reported.

* **Data shows that gut microbiota imbalance plays a contributory role in the pathogenesis of NAFLD and microbial imbalance directly influences liver injury: [Overstated].**  
  The Abstract (line 8) and Results (line 25) make causal claims (`"plays a contributory role in the pathogenesis of NAFLD"`, `"reinforcing the microbial-hepatic axis and suggesting that microbial imbalance directly influences liver injury"`), which are unsupported by a cross-sectional observational sample confounded by obesity, diet, and insulin resistance.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Embed All Ten Quantitative Data Tables Directly in the Manuscript and Report Exact Statistics in the Text
* **WHY:** A scientific manuscript cannot consist solely of qualitative prose summaries (`"Table 1 (see PDF) presents..."`) without embedding the actual data tables or reporting quantitative values (mean $\pm$ SD or median [IQR], effect sizes, 95% CIs, and exact $p$-values) in the Results text.
* **WHAT:** Include the complete numerical contents of Tables 1–10 in the manuscript body and revise the Results section to state the exact quantitative values and $p$-values for every comparison.
* **HOW:** For each of Tables 1–10, provide the full table rows with units, sample sizes ($n$), summary statistics, test statistics ($t$, $U$, $\chi^2$, $r$, OR), and both raw $p$-values and Benjamini-Hochberg FDR-adjusted $q$-values.

#### 2. Specify the Complete 16S rRNA Bioinformatic Pipeline and Deposit Raw Sequencing Reads
* **WHY:** The Materials and Methods section (line 20) states only: `"Microbial DNA was extracted using a standardized commercial kit, and the V3-V4 region of the 16S rRNA gene was amplified and sequenced using Illumina MiSeq technology. Bioinformatic analysis was performed to determine microbial diversity and relative abundance at phylum and genus levels."` This omits every detail required to evaluate or reproduce a microbiome study.
* **WHAT:** Document the exact DNA extraction kit, V3–V4 PCR primer sequences (e.g., 341F/805R), read length and per-sample read count distribution, quality filtering and chimera removal tool (e.g., `DADA2` / `QIIME2`), taxonomic reference database and version (e.g., `SILVA v138`), rarefaction depth for alpha diversity, and compositional differential abundance method (e.g., `ANCOM-BC2`, `MaAsLin2`, or CLR-transformed Wilcoxon test with FDR control). Deposit the raw FASTQ files in NCBI SRA or ENA.
* **HOW:** Upload the 132 demultiplexed V3–V4 FASTQ files to NCBI SRA, add a Data Availability section with the BioProject accession number, and add a dedicated `16S rRNA Bioinformatic Processing` paragraph in the Methods detailing each software version and parameter.

#### 3. Account for Compositional Constraints, Multiple Testing, and Metabolic Confounding
* **WHY:** Relative abundances at the phylum level (*Firmicutes*, *Bacteroidetes*, *Proteobacteria*) sum to ~100%; an increase in *Firmicutes* mathematically forces a decrease in *Bacteroidetes* even if absolute *Bacteroidetes* load is unchanged. Furthermore, testing multiple genera and phyla with unadjusted $t$-tests/Mann-Whitney tests inflates false positives, and evaluating ROC AUCs on the training sample without cross-validation or comparison to a clinical baseline (`BMI + HOMA-IR + ALT`) overstates diagnostic utility.
* **WHAT:** Apply centered log-ratio (CLR) transformation (or `ANCOM-BC2`) with Benjamini-Hochberg FDR correction ($q < 0.05$) for taxonomic comparisons, include dietary intake/medication covariates if available, and compare the cross-validated ROC AUC of `Clinical (BMI + HOMA-IR)` vs. `Clinical + Microbiome` using DeLong's test.
* **HOW:** In R or SPSS, compute 5-fold cross-validated predicted probabilities for logistic models with and without the microbiome markers, report the DeLong test $p$-value for $\Delta\text{AUC}$ in Table 9, and report variance inflation factors (VIF) alongside adjusted ORs (per 1 SD increase) in Table 8.

#### 4. Provide Institutional Ethics Approval Details and Temper Causal Language
* **WHY:** Although the Methods state `"After obtaining informed consent"`, no Institutional Ethics Committee / IRB name or approval protocol number is provided. Additionally, the Abstract and Results use causal phrasing (`"plays a contributory role in the pathogenesis"`, `"directly influences liver injury"`) that contradicts the cross-sectional design acknowledged at the end of the Discussion.
* **WHAT & HOW:** Add the exact hospital name, IRB/Ethics Committee name, and approval reference number to the Materials and Methods section (line 20), and revise the Abstract (line 8) and Results (line 25) to replace causal language with associative wording (`"is associated with NAFLD and markers of insulin resistance"`).
