# Review of ANON_157

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.0 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.0/3.5 | Claims: 0.9/2.5 | Biology: 0.9/2.0 | Reproducibility: 1.2/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript profiles global protein abundance and lysine acetylation (Kac) in the cecal tissue of juvenile male C57BL/6J mice (3 weeks old) following a 2-week broad-spectrum antibiotic cocktail regimen (ABX: ampicillin, vancomycin, neomycin, and metronidazole; $n = 8$ per group for growth monitoring, $n = 3$ per group for LC-MS/MS proteomics/acetylomics, histology, and immunohistochemistry). Using antibody-based Kac peptide enrichment and dia-PASEF mass spectrometry, the authors identify 7,491 proteins (7,480 quantified) and 16,579 acetylation sites across 5,218 proteins (16,179 sites across 5,156 proteins quantified). Using unadjusted $p < 0.05$ and fold-change thresholds ($>1.5$ or $<0.667$), they report 793 differentially expressed proteins (DEPs) and 1,223 differentially acetylated sites (DASs), concluding that early-life gut microbiota dysbiosis disrupts host cecal metabolism (specifically the TCA cycle, glycolysis/gluconeogenesis, and butanoate metabolism) via global lysine acetylation.

While the dia-PASEF mass spectrometry dataset provides a deep catalog of mouse cecal protein and lysine acetylation sites (deposited in ProteomeXchange under `PXD064558`), the study's primary biological and statistical conclusions are undermined by four severe flaws: (1) differential acetylation intensities were not normalized to underlying protein expression levels, confounding PTM stoichiometry changes with bulk protein and cell-type composition shifts in damaged cecal tissue; (2) differential testing across 16,179 acetylation sites and 7,480 proteins ($n = 3$ mice/group) relies on unadjusted Student's $t$-test $p < 0.05$ without multiple-testing correction, under which ~809 false-positive acetylation sites are expected by chance alone; (3) the ABX protocol induced severe water and food aversion during Week 1 alongside stunted growth (Figure 1C–G) and used $0.1\text{ M}$ acetic acid (a direct acetyl-CoA precursor) to dissolve metronidazole in Week 2 without a pair-fed or vehicle-matched control, confounding microbiota depletion with acute caloric restriction, dehydration, and acetate supplementation; and (4) the manuscript directly contradicts itself on SIRT1 expression, reporting significant SIRT1 downregulation in Section 3.1 (Figure 1J) and significant SIRT1 upregulation in Section 3.2 (Figure S1A) and the Discussion.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Antibiotic cocktail treatment in postweaning mice reduces fecal bacterial DNA, impairs body weight and length gain, damages cecal mucosal architecture, and alters cecal proteome and acetylome profiles: [Moderately Supported].**  
  Fecal DNA reduction, growth retardation, cecal enlargement, and epithelial sloughing are documented in Figure 1B–I, and PCA separates ABX and CON proteomes and acetylomes (Figures 2A, 3A). However, the authors performed no 16S rRNA or metagenomic sequencing to characterize community composition ("dysbiosis"), relying solely on Qubit total fecal DNA concentration. Moreover, because ABX mice consumed markedly less water and food during Week 1 (Figure 1F,G), the observed growth stunting and metabolic shifts are heavily confounded by acute undernutrition and dehydration.

* **ABX treatment simultaneously downregulates SIRT1 (Section 3.1) and markedly upregulates SIRT1 (Section 3.2 and Discussion) in mouse cecal tissue: [Methodologically Flawed].**  
  The manuscript contains an unacknowledged internal contradiction regarding the deacetylase SIRT1. In Section 3.1 (line 65), the authors state: *"Our results reveal that ABX treatment significantly downregulated P300 as well as the deacetylases HDAC2, SIRT1, and SIRT6 (Figure 1J)."* In Section 3.2 (line 76) and the Discussion (line 9 of the second section), they state the exact opposite: *"We observed significant upregulation of SIRT1 (Figure S1A)"* and *"Furthermore, SIRT1 is markedly upregulated in the cecum of ABX-treated mice."* No explanation is provided for why immunohistochemistry (Figure 1J) and LC-MS/MS proteomics (Figure S1A) yield opposite directions of change for the same protein in the same tissue.

* **1,223 lysine acetylation sites across metabolic pathways (TCA cycle, glycolysis/gluconeogenesis, and butanoate metabolism) are significantly regulated by gut microbiota dysbiosis: [Methodologically Flawed].**  
  First, testing 16,179 quantified acetylation sites with $n = 3$ biological replicates per group at an unadjusted Student's $t$-test threshold of $p < 0.05$ without false discovery rate (FDR) control yields an expected $16,179 \times 0.05 \approx 809$ false positives under the global null hypothesis—representing two-thirds of the 1,223 reported differential sites. Second, acetyl-peptide intensities were not normalized to the abundance of their corresponding parent proteins across the 7,480 quantified proteins. Because ABX caused mucosal epithelial sloughing (Figure 1I) and altered the abundance of 793 proteins (enriched in metabolic pathways including glycolysis/gluconeogenesis and oxidative phosphorylation; Figure 2E), unnormalized Kac peptide changes reflect changes in protein abundance and tissue cellularity rather than site-specific acetylation stoichiometry.

* **Early-life gut microbiota dysbiosis specifically drives host cecal hypo/hyper-acetylation via microbial SCFA depletion rather than caloric restriction or vehicle effects: [Overstated].**  
  Fast-growing 3-week-old mice subjected to foul-tasting antibiotic water (Week 1) and daily gavage of antibiotics dissolved in saline and $0.1\text{ M}$ acetic acid (Week 2) experienced substantial reductions in food and water intake (Figure 1F,G). Fasting and caloric restriction are well-known primary drivers of mitochondrial and glycolytic protein acetylation in intestinal and hepatic tissues, and $0.1\text{ M}$ acetic acid is exogenous acetate that converts directly to acetyl-CoA. Without a pair-fed control group or explicit confirmation that CON mice received identical $0.1\text{ M}$ acetic acid gavage, causal attribution to the gut microbiota is unsupported.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Normalize Acetyl-Peptide Intensities to Parent Protein Abundance and Apply Multiple-Testing Correction
* **WHY:** Calling differentially acetylated sites (DASs) from raw enriched peptide intensities without dividing by total protein abundance conflates changes in protein expression with changes in PTM stoichiometry, and using unadjusted $p < 0.05$ across 16,179 tests with $n = 3$ guarantees hundreds of false positives.
* **WHAT:** Compute protein-normalized acetylation stoichiometry ratios for all overlapping proteins, apply Benjamini–Hochberg FDR correction across all tested proteins and Kac sites, and re-run the GO/KEGG/WikiPathways enrichments on the normalized, FDR-controlled set.
* **HOW:** For each quantified Kac site $i$ on protein $P$ in sample $j$, calculate $\log_2(\text{Normalized Kac}_{ij}) = \log_2(\text{Kac intensity}_{ij}) - \log_2(\text{Protein intensity}_{Pj})$ using the matched proteome dataset (`Table S1`). Use empirical Bayes moderated $t$-statistics (`limma` in R, which borrows variance information across features and is far better calibrated for $n = 3$ proteomics than ordinary Student's $t$-tests) and report Benjamini–Hochberg adjusted $q$-values alongside unadjusted $p$-values in Tables S1 and S6.

#### 2. Reconcile the Contradiction Between IHC and Proteomics for SIRT1 (and Quantify IHC)
* **WHY:** Claiming that SIRT1 is significantly downregulated in Section 3.1 (Figure 1J) and significantly upregulated in Section 3.2 (Figure S1A) and the Discussion invalidates the mechanistic narrative linking deacetylase expression to cecal Kac changes.
* **WHAT & HOW:** Inspect the raw IHC optical density / H-scores in Figure 1J and the peptide-level MS quantification for SIRT1, P300, HDAC2, and SIRT6 in Table S1. Report quantitative IHC densitometry (mean $\pm$ SD across $n = 3$ mice) for Figure 1J, explicitly address the discrepancy between IHC and MS for SIRT1 in Section 3.2 and the Discussion, and remove contradictory directional claims.

#### 3. Explicitly Document Control Vehicle Treatment and Acknowledge Nutritional/Caloric Restriction Confounding
* **WHY:** In Section 2.2 (line 32), the authors state that in Week 2, ABX mice were gavaged daily with antibiotics where metronidazole was diluted in $0.1\text{ M}$ acetic acid, but they never state what the CON group received during Week 1 and Week 2 (nor how much acetate was delivered). Furthermore, the severe drop in food and water intake in ABX mice (Figure 1F,G) is a major metabolic confounder.
* **WHAT & HOW:**
  1. In Section 2.2, specify the exact gavage volume and vehicle administered to the CON group in Week 2 (specifically whether CON mice were gavaged with $0.1\text{ M}$ acetic acid / saline or left un-gavaged).
  2. Add a dedicated paragraph in the Discussion acknowledging that reduced caloric and water intake in the ABX group (Figure 1F,G), direct antibiotic effects on enterocytes, and acetic acid vehicle administration are major confounders that cannot be separated from microbiota depletion without pair-fed and germ-free controls.

#### 4. Correct Mathematical and Reporting Errors in the Text and Figures
* **WHY:** Several numerical statements in the text and figure captions are mathematically impossible or internally inconsistent.
* **WHAT & HOW:**
  * **Discussion (Line 144):** The text states *"among the 5156 quantified proteins and 16,179 acetylation sites, 1223 acetylation sites on 1560 proteins exhibited differential regulation under antibiotic exposure, accounting for 69.66% of the proteome."* A set of 1,223 sites cannot be distributed across 1,560 proteins (which would require $<1$ site per protein), and $69.66\%$ is $5,218 / 7,491$ (the proportion of *all* identified proteins that carry at least one Kac site, as stated in Section 3.3 line 87), not the differentially regulated fraction. Correct the exact counts of upregulated and downregulated sites and proteins from Figure 3D / Table S6.
  * **Figure 2C Caption (Line 82):** Change `with p value < 0.5` to `with p value < 0.05`.
  * **Section 2.1 vs. Section 2.5 (Lines 27, 47, 57):** Clarify the sample size calculation. Line 27 states $n = 8$/group was calculated for 80% power at $\alpha = 0.05$, but only $n = 3$/group was used for HE, IHC, proteomics, and acetylomics, and line 57 says "All experiments were performed in triplicate" (confusing $n = 3$ biological replicates with technical triplicates). Explicitly state $n = 8$/group for body weight/length/intake and $n = 3$ biological replicates/group for histology and MS.
  * **Section 3.2 (Line 76):** Fix the broken cross-reference `Figure S2B, Table S3` (should be `Figure S1B, Table S3`, since Figure S2 is histone/TCA/butanoate acetylation).
