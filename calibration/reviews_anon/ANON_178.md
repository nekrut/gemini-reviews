# Review of ANON_178

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.5 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 2.0/3.5 | Claims: 1.5/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study investigates the association between the oral and gut (fecal) microbiome and clinical response to anti-PD-1 checkpoint blockade in patients with metastatic melanoma ($n=112$ enrolled; $n=89$ clinically evaluable by RECIST 1.1 at 6 months: 54 responders [R] and 35 non-responders [NR]). The authors perform 16S rRNA sequencing on oral ($n=109$; 86 evaluable: 54 R, 32 NR) and fecal ($n=53$; 43 evaluable: 30 R, 13 NR) samples, whole-genome shotgun (WGS) metagenomic sequencing on a subset ($n=25$: 14 R, 11 NR), tumor whole-exome sequencing ($n=10$), multiparameter immunohistochemistry ($n=21$) and peripheral blood immune profiling, and fecal microbiota transplantation (FMT) into germ-free (GF) mice ($n=5$ R-FMT vs. $n=6$ NR-FMT for baseline tumor growth; $n=2$–$3$ per group for anti-PD-L1 treatment). They report that gut alpha diversity (`Inverse Simpson`, $p < 0.01$) and abundance of *Ruminococcaceae*/*Faecalibacterium* are elevated in responders and associated with longer progression-free survival (PFS), whereas *Bacteroidales* is enriched in non-responders. Raw sequencing reads are deposited in ENA (`PRJEB22894`, `PRJEB22874`, `PRJEB22895`, `PRJEB22893`) and EGA (`EGAS00001002698`).

The manuscript provides a valuable multi-omic human dataset and plausible biological hypothesis linking gut commensals (*Faecalibacterium* vs. *Bacteroidales*) to intratumoral $\text{CD8}^+$ T cell infiltration. However, several statistical and design weaknesses undermine the strength of the conclusions. First, severe sample attrition across assays ($n=112 \to 43$ fecal 16S $\to 39$ in PFS analyses $\to 25$ WGS $\to 15$ matched fecal-tumor IHC $\to 2$ per group in multiplex IHC) introduces potential selection bias and leaves downstream analyses heavily underpowered. Second, key murine validation claims in the main text—specifically that R-FMT mice had "improved responses to anti-PD-L1 therapy (Fig. 4I)" and "a higher density of CD8+ T cells... (Fig. 4J)"—are contradicted by the Figure 4 caption, which reports $n=2$ vs. $n=3$ mice and non-significant Mann–Whitney $p$-values ($p=0.20$ and $p=0.30$). Third, survival models rely on post-hoc stratification schemes (tertiles for diversity, median split for taxa) and forward stepwise variable selection on $n=39$ patients without accounting for multiple testing or baseline clinical imbalance in the fecal subset. These issues can be addressed through rigorous statistical re-analysis, transparent reporting of sample attrition, and tempering of underpowered murine claims.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Higher baseline gut microbiome alpha diversity and *Ruminococcaceae*/*Faecalibacterium* abundance are associated with clinical response and prolonged PFS on anti-PD-1 therapy, whereas oral microbiome composition is not: [Moderately Supported].**  
  The difference in fecal alpha diversity (Fig. 1C, $n=30$ R vs. $n=13$ NR) and enrichment of *Clostridiales*/*Ruminococcaceae*/*Faecalibacterium* vs. *Bacteroidales* across 16S OTUs, LEfSe, crOTUs, and WGS metagenomic species (Fig. 2, Fig. 3A–B) are consistent across taxonomic methods. However, only 43 of 89 evaluable patients provided baseline fecal samples (with an enrichment of responders: 30/43 [70%] vs. 24/46 [52%] among those without fecal samples), and 4 additional fecal samples are unexplainedly dropped in the PFS curves ($n=39$ in Fig. 1D–E and Fig. 3C). Moreover, switching between tertiles (for Inverse Simpson, giving wide hazard ratio CIs of 1.02–12.74 and 1.02–12.52) and median splits (for *Faecalibacterium* and *Bacteroidales*, $p=0.03$ and $p=0.05$) without multiple-testing correction makes the survival thresholds fragile.

* **Metagenomic pathway reconstruction demonstrates enrichment of anabolic/amino acid biosynthesis pathways in responders and catabolic pathways in non-responders: [Fragile].**  
  In the $n=25$ WGS subset (14 R, 11 NR), unsupervised clustering of predicted MetaCyc pathways yields two clusters with response rates of 69.2% (9/13) and 41.7% (5/12) (Fig. 3D, misreferenced as Fig. 3E in the text). A Fisher's exact test on a $2 \times 2$ table of 9/13 vs. 5/12 is not statistically significant ($p = 0.24$), so the separation of responder status by functional pathway cluster is consistent with random variation in a small sample.

* **Gut *Faecalibacterium* abundance positively correlates with intratumoral $\text{CD8}^+$ T cell infiltration and antigen-presentation myeloid markers in patients: [Moderately Supported].**  
  In the matched baseline tumor IHC subset ($n=15$ fecal+IHC samples in Fig. 4B–C), univariate regression shows $r^2 = 0.42$ ($p < 0.01$) between fecal *Faecalibacterium* and intratumoral $\text{CD8}^+$ T cell density. However, the multiplex IHC analysis of antigen-processing myeloid markers (Fig. 4E–F) comprises only $n=2$ high-*Faecalibacterium* versus $n=2$ high-*Bacteroidales* patients, which is purely anecdotal and cannot support statistical inference.

* **Fecal microbiota transplantation from responders into germ-free mice causally enhances anti-PD-L1 efficacy and increases intratumoral and gut $\text{CD8}^+$ T cell density: [Overstated].**  
  While baseline tumor growth at day 14 prior to checkpoint blockade was lower in R-FMT ($n=5$) than NR-FMT ($n=6$) mice ($p=0.04$, Fig. 4H), the main text claims that *"mice transplanted with R-FMT also exhibited improved responses to anti-PD-L1 therapy (Fig. 4I)"* and *"tumors of mice receiving R-FMT had a higher density of CD8+ T cells... (Fig. 4J)"* and in the gut (Fig. 4K). Inspection of the Fig. 4I–K caption reveals that only $n=2$ R-FMT, $n=3$ NR-FMT, and $n=2$ Control mice were evaluated, and every reported Mann–Whitney test is statistically non-significant ($p=0.20$ for R-FMT vs. NR-FMT in Fig. 4I; $p=0.30$ in Fig. 4J; $p=0.17$ in Fig. 4K), with significance asterisks in Fig. 4J–K evidently computed by treating 5–12 microscopic high-power fields (HPFs) from just 2 mice per group as independent biological replicates (pseudoreplication).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Eliminate Pseudoreplication in Murine IHC and Align Main-Text Claims with Statistical Support
* **WHY:** In Fig. 4J and 4K, plotting and testing 5 to 12 microscopic fields (HPFs) from $n=2$ mice per group as independent observations violates statistical independence, and claiming significant anti-PD-L1 efficacy in Fig. 4I ($n=2$ vs. $n=3$ mice, $p=0.20$) misrepresents a null result as positive proof.
* **WHAT:** Recompute all murine statistical comparisons using the mouse (and human donor) as the biological unit of replication, and revise the main text to reflect the actual sample sizes and $p$-values.
* **HOW:** Average the HPF counts within each mouse before testing, or fit a linear mixed-effects model with mouse and donor ID as random intercepts. In the main text (page 206), explicitly state that the anti-PD-L1 treatment arm ($n=2$ R-FMT vs. $n=3$ NR-FMT, $p=0.20$) and the $n=2$ per group multiplex IHC (Fig. 4E–F) are preliminary descriptive observations rather than statistically significant effects.

#### 2. Account for Fecal Sample Attrition and Subset Covariate Balance
* **WHY:** Table S2 reportedly compares clinical covariates across all eligible patients ($n=89$), but all primary gut microbiome findings rest on the $n=43$ fecal 16S subset (and $n=39$ in the PFS analyses), where responder prevalence is higher (30 R vs. 13 NR) and 4 patients with fecal 16S data were excluded from survival analysis without explanation.
* **WHAT:** Report clinical covariate balance specifically within the $n=43$ fecal 16S cohort and the $n=25$ WGS cohort, and account for the 4 missing patients between Fig. 1C ($n=43$) and Fig. 1D–E / Fig. 3C ($n=39$).
* **HOW:** Add a column to Table S2 comparing age, sex, stage, prior therapy, and LDH between R ($n=30$) and NR ($n=13$) in the fecal cohort, include the 4 missing fecal samples in the KM/Cox models (or explicitly document why their PFS follow-up was unavailable), and report multivariable Cox models adjusting for prior immunotherapy, age, sex, and LDH simultaneously rather than relying on forward stepwise selection in $n=39$ patients.

#### 3. Standardize Survival Predictors as Continuous Variables to Avoid Threshold Fishing
* **WHY:** Using tertiles for Inverse Simpson diversity (Fig. 1E, where the lower 95% CI bound is 1.02) and median splits for *Faecalibacterium* and *Bacteroidales* (Fig. 3C, $p=0.03$ and $p=0.05$) introduces arbitrary threshold selection that can inflate Type I error.
* **WHAT:** Evaluate alpha diversity and log-transformed or centered-log-ratio (CLR) transformed relative abundances of *Faecalibacterium* and *Bacteroidales* as continuous predictors in Cox proportional hazards models.
* **HOW:** Fit univariate and multivariable Cox models using continuous standardized Inverse Simpson score and CLR-transformed taxon abundances across all available fecal samples, reporting the hazard ratio per standard deviation, 95% confidence interval, and Benjamini–Hochberg FDR-adjusted $p$-values.

#### 4. Apply Compositional Data Analysis (CoDA) Controls for Differential Taxon Abundance
* **WHY:** Standard Mann–Whitney tests and LEfSe on relative abundances are susceptible to compositional closure artifacts (e.g., a high relative abundance of *Bacteroidales* mechanically depresses the relative abundance of *Ruminococcaceae* even if absolute *Ruminococcaceae* load is unchanged).
* **WHAT:** Verify whether the reciprocal enrichment of *Faecalibacterium* (R) and *Bacteroidales* (NR) holds under compositionally aware transformations or log-ratio models.
* **HOW:** Compute the log-ratio of *Ruminococcaceae* (or *Faecalibacterium*) to *Bacteroidales* within each patient sample and test its association with responder status and PFS, or run `ANCOM-BC` / `ALDEx2` on the raw 16S OTU count matrix to confirm differential abundance independent of compositional closure.

#### 5. Fix Broken Figure Panel Cross-References in the Main Text
* **WHY:** Several panel letters in Figure 3 do not match their citations in the main text, confusing the reader.
* **WHAT & HOW:**
  1. Line 194: Change `"shortened PFS compared to those with a low abundance (p=0.05, Fig. 3D)"` to `"(p=0.05, Fig. 3C)"` (since Fig. 3C contains the KM PFS curves and Fig. 3D is the MetaCyc pathway heatmap).
  2. Line 196: Change all three references to `"Fig. 3E"` (`"response rates of 69.2% and 41.7% (Fig. 3E)"`, `"amino acid biosynthesis (Fig. 3E)"`, `"catabolic functions predominated in NR (Fig. 3E..."`) to `"Fig. 3D"` (there is no panel E in the Figure 3 caption).
  3. Line 204 (Fig. 4A caption): Justify why a one-sided Mann–Whitney test was used for baseline intratumoral $\text{CD8}^+$ T cell density when two-sided tests were used elsewhere, and report the two-sided $p$-value.
