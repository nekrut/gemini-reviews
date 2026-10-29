# Review of FEXP_ANON_066

**Overall Score:** **2.8 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **2.1 / 8.0**  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.5/2.5 | Biology: 0.7/2.0 | Reproducibility: 0.7/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Subfield & Study Design:** Genetic Epidemiology / Univariable, Reverse, and Multivariable Two-Sample Mendelian Randomization (MR) investigating circulating cathepsins (B, E, F, G, H, O, S, L2, Z) and asthma risk.
* **Data Sources:** Plasma proteomics GWAS from the INTERVAL study ($N = 3,301$ European participants) and asthma GWAS from FinnGen (`J10_ASTHMA_EXMORE`, $46,684$ cases and $219,734$ controls).
* **Perceived Venue Tier:** Open-access general science or medical megajournal.

---

## 2. Executive Summary & Editorial Verdict

This study conducts two-sample univariable, reverse, and multivariable Mendelian randomization (MR) analyses to test for causal associations between plasma levels of nine cathepsins (derived from $N = 3,301$ individuals in the INTERVAL cohort) and asthma risk (derived from $N = 266,418$ individuals in FinnGen). Using SNPs selected at $P < 5 \times 10^{-6}$, the authors report a nominal positive association between genetically predicted cathepsin L2 levels and asthma risk in univariable IVW ($OR = 1.058$, $95\% \text{ CI}: 1.016\text{--}1.101$, $P = 0.006$) and multivariable MR ($OR = 1.060$, $P = 0.008$), alongside a reverse MR association from asthma to cathepsin B levels.

**Editorial Verdict: Reject (Fundamentally Invalid).** A forensic audit reveals multiple disqualifying defects, including an obvious citation-stuffed/AI-generated paragraph on computer vision algorithms (`DeepLab` and `Feature Pyramid Networks`) inserted into the Discussion, direct self-contradictions regarding the reverse MR and multivariable MR analyses, flawed instrument selection thresholds across both forward and reverse directions, and an unacknowledged failure of the primary association to survive leave-one-out sensitivity analysis or strict multiple-testing correction.

### Assessment of Specific Conclusions
* **Claim 1: Elevated cathepsin L2 levels causally increase asthma risk ($OR = 1.058, P = 0.006$ in UVMR; $OR = 1.060, P = 0.008$ in MVMR):** `[Fragile]`  
  First, the univariable $P$-value ($P = 0.006$) fails the Bonferroni threshold for testing 9 cathepsins ($\alpha = 0.05/9 = 0.00556$). Second, instruments were selected at a relaxed $P < 5 \times 10^{-6}$ threshold across the entire genome (combining *trans*-pQTLs with *cis*-pQTLs) from a small sample ($N = 3,301$), rather than restricting to biologically specific *cis*-variants at the *CTSV* (*CTSL2*) locus. Third, the authors admit in Section 3 (Line 91) that in the leave-one-out analysis, individual SNP exclusions cause the confidence interval to cross the null ("across zero line"), demonstrating that the nominal association is driven by single variants. Fourth, the MR-Egger intercept for cathepsin L2 shows a borderline trend toward directional pleiotropy ($\text{intercept} = 0.016, \text{SE} = 0.009, P = 0.090$).
* **Claim 2: Asthma causally increases circulating cathepsin B levels in reverse MR, but this reverse association is confounded by cathepsin L2 as shown by MVMR:** `[Methodologically Flawed]`  
  This claim in the Discussion (Lines 140 and 146) is logically incoherent. In Section 3 (Line 128), the authors report a reverse MR association where `Asthma (exposure) -> Cathepsin B (outcome)` is significant using a heavily relaxed $P < 5 \times 10^{-5}$ instrument threshold. Then in Section 4 (Line 146), they argue that because Cathepsin B was not significant in forward MVMR (`Cathepsins -> Asthma`), *"the initial univariate association observed between cathepsin B and asthma in reverse MR May have been confounded by other cathepsins, especially cathepsin L2."* Forward MVMR tests `Cathepsins -> Asthma` (where Cathepsin B was already null in univariable forward MR, Fig. 2); it cannot test or adjust for confounding in the reverse causal pathway (`Asthma -> Cathepsin B`).
* **Claim 3: Sensitivity analyses confirm the absence of heterogeneity or single-SNP instability for cathepsin L2:** `[Overstated]`  
  In Section 3 (Line 91), the authors explicitly state that leave-one-out analysis showed results crossing the null line (Supplementary Fig. S1), yet misinterpret this loss of statistical significance as "potential heterogeneity" and then claim in the Discussion (Line 144) that *"sensitivity analyses did not alter the findings of this study; thus, these results are robust."*

---

## 3. Forensic Defect Inventory

### 1. [Critical] Out-of-Context Computer Vision Insertion (`DeepLab` & `Feature Pyramid Networks`)
* **Location:** Discussion, Paragraph 7 (Line 150), References 48–49.
* **Defect:** In the middle of discussing the limitations of plasma versus lung tissue cathepsin levels in Mendelian randomization, the manuscript abruptly inserts a completely unrelated paragraph promoting computer vision architectures: *"Advanced computer vision algorithms, such as DeepLab [48] for semantic segmentation and Feature Pyramid Networks [49] for multi-scale feature extraction, could quantitatively analyze high-resolution imaging data (e.g., chest CT scans or histopathological slides) to map airway remodeling patterns. For instance, DeepLab's deep convolutional neural networks can segment bronchial wall thickness and mucus plugging, while FPN's hierarchical architecture captures both local and global structural changes."* No imaging, histopathology, or deep learning is performed anywhere in this summary-level genetic study. This is a textbook signature of coercive citation stuffing or unedited LLM text injection.
* **Remediation:** Delete the unrelated computer vision text and references [48, 49] entirely.

### 2. [Critical] Causal Directionality Confusion Between Reverse Univariable MR and Forward Multivariable MR
* **Location:** Abstract (Line 5), Results (Lines 128–130), and Discussion (Lines 140, 146).
* **Defect:** The authors conflate forward causal estimation ($\text{Cathepsins} \to \text{Asthma}$) with reverse causal estimation ($\text{Asthma} \to \text{Cathepsins}$). In forward univariable MR (Fig. 2), Cathepsin B has no significant effect on asthma. In reverse univariable MR (Supplementary Fig. S2), asthma has a significant effect on Cathepsin B. However, in the Discussion (Line 146), the authors claim that because only Cathepsin L2 remained significant in forward MVMR ($\text{Cathepsins} \to \text{Asthma}$, Fig. 3), *"the initial univariate association observed between cathepsin B and asthma in reverse MR May have been confounded by other cathepsins, especially cathepsin L2. The lack of significance of cathepsin B in multivariate analysis reinforces that its role in asthma may be secondary or reactive."* Conditioning on multiple exposures in forward MVMR does not adjust for pathways in reverse MR where asthma is the exposure.
* **Remediation:** Remove the invalid claim that forward MVMR explains or invalidates the reverse MR association between asthma and Cathepsin B.

### 3. [Major] Inappropriate Instrument Thresholds ($P < 5 \times 10^{-5}$ in Reverse MR; Genome-Wide *Trans* Signals at $P < 5 \times 10^{-6}$ in Forward MR)
* **Location:** Methods (Line 52) and Results (Line 128).
* **Defect:**
  1. **Forward MR:** Line 52 erroneously describes $P < 5 \times 10^{-6}$ as *"genome-wide significance ($P < 5 \times 10^{-6}$)"*. Selecting genome-wide SNPs at $P < 5 \times 10^{-6}$ in a small proteomic sample ($N = 3,301$) includes noisy *trans*-pQTLs (which have $10\text{--}12$ degrees of freedom in Table 3, meaning $11\text{--}23$ genome-wide SNPs per protein) that are highly prone to horizontal pleiotropy via general inflammatory or hematopoietic pathways, rather than restricting to biologically specific *cis*-pQTLs within $\pm 1\text{ Mb}$ of each cathepsin gene.
  2. **Reverse MR:** Despite using a massive FinnGen asthma GWAS ($N = 266,418$ with $46,684$ cases) that yields dozens of genome-wide significant loci at the standard $P < 5 \times 10^{-8}$ threshold, the authors relax the reverse MR selection threshold to $P < 5 \times 10^{-5}$ (Line 128). At $P < 5 \times 10^{-5}$, hundreds of false-positive / weak instruments ($F \approx 16.4$) are introduced, biasing two-sample IVW toward the null and invalidating the claim of "ruling out reverse causality."
* **Remediation:** Restrict forward protein MR to *cis*-pQTLs (or stratify *cis* vs. *trans* instruments) and perform reverse MR strictly using genome-wide significant asthma instruments ($P < 5 \times 10^{-8}$).

### 4. [Major] Misinterpretation of Leave-One-Out Fragility and Borderline Multiple Testing
* **Location:** Results (Lines 86, 91) and Discussion (Lines 138, 144).
* **Defect:** The headline association for Cathepsin L2 ($P = 0.006$) does not pass Bonferroni correction for 9 tested cathepsins ($P < 0.00556$). Furthermore, Line 91 notes that *"Leave-one-out analysis showed that the results of individual SNPs across zero line, which suggest potential heterogeneity (Supplementary Figure S1)."* Crossing the null line in leave-one-out analysis means that removing individual SNPs renders the causal estimate statistically non-significant—demonstrating that the $P = 0.006$ result is fragile, not "robust."
* **Remediation:** Explicitly report that the Cathepsin L2 association does not survive Bonferroni correction or leave-one-out single-SNP exclusion, and temper all causal claims accordingly.

### 5. [Minor] Missing Mathematical Formula and Malformed Tables
* **Location:** Section "Selection of instrumental variables" (Lines 62–64) and Tables 2–3 (Lines 94–127).
* **Defect:** The equation for the $F$-statistic referenced on Line 62 (*"The F-statistic is found from the formula [19, 20]:"*) is completely missing from the text (blank line between Line 62 and Line 64). Additionally, Tables 2 and 3 are mislabeled in their captions as *"of cathepsins L2 genetic variants"* despite containing rows for all nine cathepsins, and Table 2 formats negative intercepts using accounting parentheses `(0.007)` and `(0.010)` instead of minus signs.
* **Remediation:** Restore the missing $F$-statistic formula ($F = \frac{R^2(N - K - 1)}{K(1 - R^2)}$), fix the captions of Tables 2 and 3, and replace accounting parentheses with standard negative signs.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.9** | **3.5** | Relaxed $P < 5 \times 10^{-5}$ threshold in reverse MR despite $N=266,418$; reliance on $P < 5 \times 10^{-6}$ *trans*-pQTLs in $N=3,301$ without *cis*-validation or colocalization; causal directionality confusion between forward MVMR and reverse UVMR. |
| **2. Claim-to-Evidence Alignment** | **0.5** | **2.5** | Primary finding ($P = 0.006$) misses Bonferroni significance and fails leave-one-out sensitivity (crosses zero), yet is claimed as a robust, definitive causal target; reverse MR vs. MVMR interpretation is logically invalid. |
| **3. Data Integrity & Biological Plausibility** | **0.7** | **2.0** | Contains an out-of-context, citation-stuffed paragraph on `DeepLab` and `Feature Pyramid Networks`; plasma *trans*-pQTLs do not establish airway-specific protease activity. |
| **4. Reproducibility & Data Integrity** | **0.7** | **2.0** | Missing $F$-statistic equation in text; mislabeled captions for Tables 2 and 3; accounting parentheses for negative numbers in Table 2; main UVMR and MVMR tables relegated only to figures without full numeric tables in main text. |
| **Scientific Core Score** | **2.1** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **2.8** | **10.0** | **Fundamentally Invalid** (28 / 100 equivalent). |
