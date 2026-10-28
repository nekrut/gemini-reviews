# Review of ANON_90

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.0 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents a longitudinal multi-omics investigation of 30 hospitalized COVID-19 patients (22 mild/moderate, WHO OSCI 1–4; 8 severe/critical, OSCI 5–8) sampled between March and June 2020 and 15 age- and sex-matched uninfected controls. Across repeated sampling timepoints, the authors integrate stool and oropharyngeal (OP) shotgun metagenomics (72 stool and 75 OP samples post-QC), plasma and urine metabolomics (96 plasma and 77 urine samples via Biocrates MxP Quant 500, GC-MS, and targeted tryptophan UPLC-MS), plasma cytokine profiling, and T/B-cell-depleted PBMC scRNA-seq (14 early COVID-19 patients and 11 controls). Using linear mixed-effects models with patient random intercepts (`(1|PatientID)`) and nested likelihood ratio tests (`metadeconfoundR`), the authors systematically evaluate confounding by antibiotic exposure, comorbidities, and hospitalization duration. They report that OP microbiome perturbations are largely driven by antibiotic therapy, whereas severe COVID-19 is associated with gut commensal depletion (including *Faecalibacterium* and *Lachnospiraceae*), reduced plasma tryptophan, indole derivatives, secondary bile acids, and lysophosphatidylcholines, and elevated plasma kynurenine and proinflammatory cytokines. Raw sequencing reads (PRJNA909223), metabolomics data (MTBLS6600), and reproducible `targets`/`renv` R workflows on GitHub are provided.

This is a carefully executed observational study whose primary strength is its explicit post-hoc confounder auditing, which prevents attributing antibiotic-driven oropharyngeal dysbiosis to SARS-CoV-2 severity. Nevertheless, three methodological caveats temper the strength of the conclusions. First, the severe COVID-19 subgroup is very small ($n = 8$ patients, 62.5% receiving concurrent antibiotics vs. 18.2% in mild cases and 0% in controls), which limits statistical power in the likelihood ratio tests used to declare features "unconfounded." Second, OP shotgun metagenomes were rarefied to only 600 reads per sample, and targeted UPLC-MS tryptophan metabolites are plotted in absolute concentration units ($\text{ng/mL}$) in Figure 4 despite the Methods noting that calibration inaccuracy restricts them to relative quantification. Third, the cross-omics nested models cannot resolve causal directionality between kynurenine and IFN$\gamma$ (where IFN$\gamma$-inducible IDO1 drives kynurenine synthesis). These limitations can be addressed through sensitivity analyses, multivariable joint confounder checks, and minor presentation adjustments without generating new data.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Oropharyngeal microbiota alterations in hospitalized COVID-19 patients are primarily confounded by antibiotic exposure rather than disease status or severity: [Well Supported].**  
  Beta-diversity ordination (Figure 2b) and `metadeconfoundR` nested linear mixed models (Figure 5a–b, Supplementary Figure 1c) convincingly show that naive associations between OP bacterial taxa and COVID-19 severity lose significance when adjusted for recent or concurrent antibiotic intake. One technical caveat is that OP samples were rarefied to 600 mOTU reads per sample (Methods, "Taxonomic profile pre-processing"), which provides low sensitivity for rare taxa, though it is sufficient to capture dominant antibiotic-driven shifts.

* **COVID-19 severity is associated with elevated plasma kynurenine, depleted tryptophan and microbial indole derivatives, reduced secondary bile acids (glycodeoxycholic acid), and reduced lysophosphatidylcholines: [Well Supported].**  
  The metabolic shifts are large in magnitude (e.g., tryptophan $\rho = -0.68$, kynurenine $\rho = 0.70$, glycodeoxycholic acid $\rho = -0.42$; all $\text{FDR} < 0.001$), consistent across early ($\le 10$ days) and late ($>10$ days) sampling windows (Figure 4, Supplementary Figure 3a), and biologically coherent with host IDO1 activation and impaired microbial bile acid deconjugation. However, Figure 4 plots tryptophan metabolites in $\text{ng/mL}$ even though the Methods ("Tryptophan metabolite analysis using UPLC-MS") explicitly state that measurements fell systematically outside the calibration range and "cannot be considered as absolutely but as relatively quantified."

* **Depletion of gut commensals (such as *Faecalibacterium*, *Intestinimonas*, and *Turicibacter*) is directly associated with COVID-19 status/severity independent of antibiotics and hospitalization length: [Moderately Supported].**  
  In `metadeconfoundR`, an association between a taxon $Y$ and severity $D$ is labeled "deconfounded" if adding a clinical covariate $C$ (`rank(Y) ~ D + C + (1|PatientID)`) still yields a significant LRT for $D$ or fails to yield a significant LRT for $C$. Because the severe group has only $n = 8$ patients (5 on current antibiotics, median CCI 3.5) and covariates are tested one at a time rather than jointly, collinear confounders (simultaneous antibiotic exposure, ICU stay, enteral nutrition, and comorbidities) may not be fully disentangled by single-covariate nested tests.

* **Depletion of *Faecalibacterium* drives reduced plasma tryptophan/indole metabolites, which in turn contribute to excessive proinflammatory cytokine (IFN$\gamma$, TNF$\alpha$, IP-10) production: [Fragile].**  
  While the cross-omics correlations (Figure 5c) are statistically significant, the cross-omics LRT framework (`rank(IFNγ) ~ disease_status + kynurenine`) is purely associative and symmetric with respect to causal direction. Biologically, IFN$\gamma$ and TNF$\alpha$ potently upregulate host indoleamine 2,3-dioxygenase 1 (IDO1), accelerating host tryptophan-to-kynurenine catabolism; thus, systemic inflammation likely drives tryptophan depletion and kynurenine accumulation rather than (or in addition to) gut *Faecalibacterium* depletion causing cytokine dysregulation.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Perform Joint Multivariable Confounder Sensitivity Checks and Antibiotic-Free Subgroup Analysis
* **WHY:** Testing clinical confounders one by one in `metadeconfoundR` with $n = 8$ severe patients can miss cumulative confounding when antibiotic use, length of hospitalization, and Charlson Comorbidity Index act together, or when power to detect the covariate effect in the nested LRT is low.
* **WHAT:** Add a sensitivity analysis restricting the control vs. mild comparison to antibiotic-naive patients, and test top severity-associated features in a joint multivariable mixed model.
* **HOW:** For the key highlighted features (*Faecalibacterium*, Shannon diversity, tryptophan, kynurenine, glycodeoxycholic acid), fit `lme4::lmer(rank(feature) ~ OSCI_binary + Antibiotics + Hospitalization_days + CCI + (1|PatientID))` and report the multivariable-adjusted effect sizes and confidence intervals alongside a subgroup check in patients without current or prior 3-month antibiotic exposure.

#### 2. Harmonize Figure 4 Metabolite Units with the Calibration Limitations Stated in Methods
* **WHY:** The Methods transparently state that UPLC-MS tryptophan pathway measurements fell outside the standard calibration curve and had insufficient QC calibration accuracy, mandating relative quantification. Plotting these values in $\text{ng/mL}$ in Figure 4 can mislead readers into treating them as absolute clinical reference concentrations.
* **WHAT:** Update Figure 4 axes or caption to reflect relative/calibrated-extrapolated units and indicate the limits of quantification (LOQ).
* **HOW:** Either plot internal-standard-normalized, batch-corrected relative intensities (or $\log_{10}$ relative abundance) in Figure 4, or shade the concentration regions below LLOQ / above ULOQ and add an explicit note in the Figure 4 caption stating that $\text{ng/mL}$ values represent extrapolated relative estimates.

#### 3. Assess Sensitivity of Oropharyngeal Diversity to the 600-Read Rarefaction Threshold
* **WHY:** Rarefying shotgun metagenomic mOTU profiles to 600 reads/sample for OP swabs is very shallow and introduces substantial multinomial sampling variance into Shannon alpha-diversity and Bray–Curtis beta-diversity estimates.
* **WHAT:** Verify that the OP alpha- and beta-diversity conclusions hold at a higher rarefaction depth (e.g., 2,000–5,000 reads/sample) or using unrarefied library-size-adjusted models.
* **HOW:** Re-compute Shannon diversity and PCoA on the subset of OP samples passing a 2,500-read threshold (or include $\log(\text{library size})$ as a covariate in `metadeconfoundR`) and report in Supplementary Figure 1 whether the antibiotic-confounding pattern remains unchanged.

#### 4. Clarify Causal Directionality in the Cross-Omics Tryptophan–IDO1–Cytokine Network
* **WHY:** In the Abstract and Results, the phrasing ("tryptophan decrease and kynurenine increase were linked to enhanced production of inflammatory cytokines") and the regression specification (`rank(IFNγ) ~ disease_status + kynurenine`) can be read as metabolites driving cytokine production, whereas IFN$\gamma$ is the canonical transcriptional inducer of host IDO1.
* **WHAT:** Explicitly frame the tryptophan–kynurenine–IFN$\gamma$ axis as bidirectional or cytokine-driven host catabolism in the Results and Figure 5 legend.
* **HOW:** Add a brief clarification in the Results section ("Integrated analysis reveals associations...") noting that the nested LRTs test conditional statistical independence rather than causal direction, and that elevated kynurenine/tryptophan ratios reflect IFN$\gamma$-induced IDO1 activity alongside microbial indole depletion.
