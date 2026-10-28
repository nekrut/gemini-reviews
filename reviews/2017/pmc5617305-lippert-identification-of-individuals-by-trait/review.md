# Review of PMC5617305 (PMID:28874526)

**Manuscript Title:** Identification of individuals by trait prediction using whole-genome sequencing data  
**Authors:** Lippert C, Sabatini R, Maher MC, Kang EY, Lee S, Arikan O, Harley A, Bernal A, Garst P, Lavrenko V, Yocum K, Wong T, Zhu M, Yang WY, Chang C, Lu T, Lee CWH, Hicks B, Ramakrishnan S, Tang H, Xie C, Piper J, Brewerton S, Turpaz Y, Telenti A, Roby RK, Och FJ, Venter JC.  
**Journal / Preprint:** *Proc Natl Acad Sci U S A* (2017; `PMC5617305` / `PMID:28874526` / `10.1073/pnas.1711125114`)  
**Calibration Study Cohort:** Cohort A — Known Invalid / Refuted (`A20` | Double-Blinded as `ANON_21`)  
**Overall Score:** **4.4 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.5/3.5 | Claims: 0.9/2.5 | Biology: 1.1/2.0 | Reproducibility: 0.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript evaluates whether whole-genome sequencing (WGS) data (>30x coverage) can be used to predict biometric traits—3D facial morphology, voice embeddings, biological age, height, weight, BMI, eye color, and skin color—and subsequently re-identify individuals by matching predicted traits to observed phenotypic profiles in a multi-ethnic cohort of 1,061 participants from San Diego. Using ridge regression on 1,000 genomic principal components (PCs), demographic covariates, and known SNPs for individual traits, followed by a maximum-entropy bipartite matching algorithm, the authors report re-identifying >8 of 10 individuals in an ethnically mixed lineup ($m_{10} = 83\%$, $s_{10} = 74\%$) and ~5 of 10 individuals within African American or European strata. Genomic data are placed under a custom managed-access agreement, and no source code is provided.

While the dataset combining >30x WGS with standardized 3D facial imaging and quantitative phenotyping across 1,061 individuals is a potentially useful resource, the manuscript's central claim—that individualized genomic prediction of complex biometric traits such as 3D facial structure and voice enables personal re-identification—is severely overstated and confounded by demographic and ancestry variables. The authors' own internal controls show that known facial SNPs add zero predictive power ($R^2_{CV}$ unchanged in Fig. 3), their landmark GWAS yields zero significant associations, known height SNPs explain only $R^2_{CV} = 0.06\text{--}0.08$, and 97 of 100 voice identity-vector dimensions have $R^2_{CV} \le 0.10$. Instead, the apparent predictive accuracy and small-pool ($N=10$) matching performance are driven almost entirely by biological sex, continuous continental/sub-continental admixture proportions, pigmentation, and age. Resolving these issues requires a transparent ablation against a baseline model containing only sex, continuous genomic ancestry, pigmentation SNPs, and age; nested cross-validation to prevent leakage between trait prediction and maximum-entropy weight learning; and substantial reframing of the title, abstract, and forensic claims.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Claim 1: Whole-genome sequencing enables individualized prediction of 3D facial structure and voice embeddings. [Overstated]**  
  In Fig. 3 and the accompanying text, the authors admit that sex and 1,000 genomic PCs account for nearly all facial shape prediction accuracy, whereas previously reported facial morphology SNPs provide zero incremental improvement and a GWAS on 36 3D facial landmark distances yields no significant hits. Similarly, Fig. 4 confirms that per-pixel $R^2_{CV}$ simply tracks average anatomical differences between African and European ancestry groups and between males and females (plus age and BMI). For voice, pitch prediction ($R^2_{CV} = 0.70$) reflects chromosomal sex differences in vocal fold anatomy, while 97 of 100 speaker identity-vector dimensions fail to exceed $R^2_{CV} = 0.10$. The model does not reconstruct an individual's face or voice; it generates a demographic/ancestry group average.

* **Claim 2: Integrating multiple genomic trait predictions via maximum entropy re-identifies >8 of 10 individuals in mixed cohorts and ~5 of 10 within single ethnicities beyond demographic information. [Methodologically Flawed]**  
  The evaluation of re-identification in tiny lineups ($N=10$) conflates complex biometric trait prediction with basic demographic filtering. First, the "3D face" feature set in the matching pipeline does not isolate craniofacial morphology: as described in *Materials and Methods* and Table 1, the facial embedding explicitly incorporates face color and image-derived predictions of sex ($R^2_{CV} = 0.84$), age ($R^2_{CV} = 0.82$), and genetic ancestry ($R^2_{CV} = 0.89$ for AFR, $0.84$ for EUR). Second, comparing this continuous, multi-variable facial embedding against coarse, discrete self-reported ethnicity creates an asymmetric baseline. Even within self-reported "African American" or "European" strata in San Diego, Fig. 1B shows substantial continuous variation in European, African, and Native American admixture proportions, alongside a 50/50 sex split and a 64-year age span (18–82 years). In a lineup of $N=10$ people, matching on sex (reducing the pool from 10 to ~5), continuous admixture, pigmentation, and age accounts for the ~5/10 accuracy without requiring any polygenic prediction of facial geometry, voice identity, height, or BMI.

* **Claim 3: Somatic telomere shortening and mosaic sex chromosome loss estimated from WGS read depth predict chronological age with $R^2_{CV} = 0.44$ ($\text{MAE} = 8.0\text{ years}$). [Fragile]**  
  The authors report $R^2_{CV} = 0.29$ for age prediction from telomere repeat read fraction alone in the 1,061-person cohort, yet note in the same paragraph that the identical sequencing pipeline applied to a 1,960-female validation cohort yielded $R^2 = 0.05$ (matching the established literature benchmark of $R^2 \approx 0.05$). Anearly six-fold inflation in variance explained ($0.29$ vs. $0.05$) between two cohorts processed on the same platform strongly suggests technical confounding in the 1,061-person sample—such as DNA extraction method, library preparation/sequencing batch effects, or blood cell-type composition correlating with participant recruitment age—that is exploited by random 10-fold cross-validation.

* **Claim 4: Eye color and skin color can be predicted as continuous 3D RGB values with per-channel $R^2_{CV}$ of 0.77–0.82. [Moderately Supported]**  
  Because human pigmentation has high heritability dominated by large-effect oligogenic loci (e.g., *HERC2/OCA2*, *SLC24A5*, *SLC45A2*, *MC1R*) and correlates strongly with continental ancestry, high cross-validated $R^2$ across the full multi-ethnic cohort is biologically plausible. However, the manuscript does not report within-ancestry $R^2_{CV}$ for continuous RGB eye and skin color, making it impossible to separate locus-specific prediction accuracy from between-continent stratification.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Add a Symmetric Demographic + Pigmentation Baseline Ablation to the Re-identification Benchmark
* **WHY:** The manuscript attributes high $s_N$ and $m_N$ matching accuracy to biometric phenotype prediction (3D face, voice, height, weight, BMI), when those embeddings primarily act as proxies for chromosomal sex, continuous genomic ancestry (admixture), skin/eye pigmentation, and age.
* **WHAT:** Introduce an explicit baseline predictor into Table 2 and Figs. 6–7 that uses *only* chromosomal sex, the top genomic ancestry PCs, continuous eye/skin pigmentation SNPs, and predicted age, and test whether adding 3D facial shape residuals, voice identity vectors, height, weight, and BMI yields any statistically significant gain in $s_N$ or $m_N$.
* **HOW:** Residualize the 3D facial mesh coordinates, voice embeddings, height, weight, and BMI against sex, age, and the top 10 genomic ancestry PCs within each training fold. Re-run the maximum-entropy matching algorithm comparing (a) the demographic/ancestry/pigmentation baseline alone vs. (b) the baseline plus residualized biometric traits across all pool sizes $N \in \{2, 10, 50, 100\}$ and within joint sex-by-ancestry strata.

#### 2. Implement Strict Nested Cross-Validation and Audit High-Dimensional PC Overfitting
* **WHY:** Using 1,000 genomic PCs as predictors in a sample of $N = 1,061$ individuals (where each 90% training fold has ~955 individuals) means the PC matrix spans the entire sample space, capturing cryptic relatedness/kinship rather than generalizable population structure. Furthermore, learning the embedding functions ($\psi_P, \phi_P$) and the maximum-entropy similarity weights ($w_d$ in Eq. 1) on the same 10-fold split risks data leakage.
* **WHAT:** Restrict genomic ancestry covariates to the top informative PCs (e.g., 5–20 PCs derived from an external reference panel such as 1000 Genomes) and enforce a strict two-level nested cross-validation scheme.
* **HOW:** Project the 1,061 genomes onto PCs computed from 1000 Genomes reference populations (removing closely related individuals with $\hat{\pi} > 0.0625$). In each outer CV fold (10% held out exclusively for $s_N/m_N$ testing), train all ridge regression trait models and learn the maximum-entropy weights $w_d$ strictly using out-of-fold predictions generated within the 90% training split via an inner 9-fold CV loop.

#### 3. Control for Sequencing Batch Confounding in Telomere and Sex Chromosome Age Prediction
* **WHY:** The discrepancy between $R^2_{CV} = 0.29$ in the main cohort and $R^2 = 0.05$ in the 1,960-female cohort on the same sequencing pipeline indicates potential batch or pre-analytical confounding in read-depth-based telomere and X/Y copy-number estimates.
* **WHAT:** Audit and adjust for sequencing run/flowcell batch, DNA source/extraction batch, and mean autosomal coverage depth in the age prediction model.
* **HOW:** Regress telomere repeat fraction and normalized X/Y coverage against sequencing batch IDs, library preparation dates, and GC-bias metrics, and perform batch-stratified cross-validation (holding out entire sequencing batches rather than random subsets) to quantify the true biological $R^2_{CV}$ of the age predictor.

#### 4. Align Claims with Empirical Findings on Individualized vs. Demographic Prediction
* **WHY:** Framing group-level demographic/ancestry averages as individualized genomic reconstructions of faces and voices misleads readers, policymakers, and forensic practitioners about the actual capabilities of polygenic trait prediction.
* **WHAT:** Revise the Abstract, Results, and Discussion to state explicitly that current genomic data cannot reconstruct individual-specific facial morphology or voice beyond sex, ancestry, and age, and that re-identification in small pools ($N=10$) is driven by demographic and ancestry stratification.
* **HOW:** Replace claims that the model predicts individual 3D facial structure and voice with precise statements reflecting Fig. 3 and Table 1: namely, that known facial SNPs contribute $0\%$ additional variance explained and that re-identification performance reflects matching genomic sex, continuous admixture proportions, pigmentation, and somatic age markers against facial photographs and demographic metadata.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Missing table data, typographical errors in the core similarity equation, and the absence of analysis code prevent independent verification.
* **WHAT & HOW:**
  * **Table 2 (Results, line 116):** Populate the missing table body for Table 2 ("Top one accuracy in match and select"), which is currently rendered as a blank cell despite being cited in the text for pool sizes $N=2$ to $50$.
  * **Equation 1 (Materials and Methods, line 156):** Fix the notation in $\delta_P(\psi_P(p), \phi_P(g)) = \sum_{d=1}^D w_d / \psi_P(p)_d - \phi_P(g)_d /$. Replace the forward slashes `/` with absolute value bars $|\psi_P(p)_d - \phi_P(g)_d|$, and clarify the sign convention (since absolute differences measure *dissimilarity*/distance rather than *similarity*, either a negative sign $-\sum_{d=1}^D w_d |\cdot|$ is omitted or $w_d$ must be constrained to negative values).
  * **Code Availability:** Deposit the complete scripts for the PCA embeddings, ridge regression models, and maximum-entropy bipartite matching (`m_N` and `s_N`) in a permanent public repository (e.g., GitHub/Zenodo).
