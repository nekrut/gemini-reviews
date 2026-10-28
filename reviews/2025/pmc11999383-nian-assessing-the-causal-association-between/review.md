# Review of PMC11999383 (PMID:40198900)

**Manuscript Title:** Assessing the Causal Association Between COVID-19 and Graves Disease: Mendelian Randomization Study  
**Authors:** Nian H, Bai Y, Yu H.  
**Journal / Preprint:** *JMIR Form Res* (2025; `PMC11999383` / `PMID:40198900` / `10.2196/66003`)  
**Calibration Study Cohort:** Cohort A — Known Invalid / Refuted (`A45` | Double-Blinded as `ANON_91`)  
**Overall Score:** **2.8 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.7/3.5 | Claims: 0.7/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript applies two-sample Mendelian randomization (2SMR) to test whether genetic liability to COVID-19 susceptibility ($N = 1,683,768$), COVID-19 hospitalization ($N = 1,882,773$), or severe COVID-19 ($N = 1,388,342$) is causally associated with Graves disease (GD; OpenGWAS ID `bbj-a-123`, $2,176$ cases and $210,277$ controls). Selecting single nucleotide polymorphisms (SNPs) at a relaxed threshold of $P < 5 \times 10^{-6}$ (yielding 19, 21, and 27 SNPs for the three exposures) and clumping at $r^2 < 0.001$ using the 1000 Genomes European reference panel, the authors run inverse-variance weighted (IVW), weighted median, MR-Egger, simple mode, and MR-PRESSO analyses. They report null IVW odds ratios for COVID-19 susceptibility ($\text{OR} = 0.989$, 95% CI $0.405\text{--}2.851$, $P = 0.93$), hospitalization ($\text{OR} = 0.974$, 95% CI $0.852\text{--}1.113$, $P = 0.70$), and severity ($\text{OR} = 0.979$, 95% CI $0.890\text{--}1.077$, $P = 0.66$), concluding that COVID-19 does not cause or exacerbate GD.

The study is fatally compromised by an unrecognized ancestry mismatch between the exposure and outcome GWAS datasets, mathematical impossibilities in the reported confidence intervals and equations, directional confusion between exposure and outcome, and overinterpretation of underpowered null estimates. Specifically, the authors state in the Methods and Limitations that their analysis "primarily relied on data from the European population," overlooking that their GD outcome dataset (`bbj-a-123`, BioBank Japan) is an East Asian cohort. Performing 2SMR across European exposures (clumped with a European LD panel) and a Japanese outcome violates the core requirement of homogenous underlying populations. Furthermore, Table 2 reports an MR-Egger 95% CI ($0.786\text{--}1.245$) for COVID-19 susceptibility that is not centered on the point estimate ($\text{OR} = 1.047$) and is substantially narrower than the IVW 95% CI ($0.405\text{--}2.851$), which is mathematically impossible. Re-running the study with ancestry-matched GWAS summary statistics and correcting the statistical reporting is required before any conclusions can be drawn.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Two-sample Mendelian randomization rules out a causal effect of COVID-19 susceptibility on Graves disease ($\text{OR} = 0.989$, 95% CI $0.405\text{--}2.851$, $P = 0.93$), alleviating concerns about a pandemic surge in autoimmune thyroid disease: [Methodologically Flawed].**  
  First, an IVW 95% confidence interval spanning $0.405$ to $2.851$ is compatible with nearly a three-fold increase or a 60% reduction in GD risk; treating this wide, uninformative interval as evidence of no effect conflates low statistical power with proof of the null hypothesis. Second, combining European-predominant COVID-19 HGI exposure summary statistics (clumped using the 1000 Genomes European reference panel) with an East Asian outcome GWAS (`bbj-a-123`, BioBank Japan) introduces severe population stratification and LD mismatch. Third, in Table 2, the MR-Egger estimate for COVID-19 susceptibility ($\text{OR} = 1.047$, 95% CI $0.786\text{--}1.245$) is mathematically inconsistent: on the log scale, $\ln(1.047) = 0.046$, whereas the midpoint of $[\ln(0.786), \ln(1.245)] = [-0.241, 0.219]$ is $-0.011$ ($\text{OR} = 0.989$), and MR-Egger cannot have a smaller standard error than IVW ($0.405\text{--}2.851$).

* **Genetic liability to COVID-19 hospitalization ($\text{OR} = 0.974$) and severe COVID-19 ($\text{OR} = 0.979$) has no causal effect on Graves disease onset or exacerbation: [Methodologically Flawed].**  
  Beyond the European-to-East-Asian ancestry mismatch (`bbj-a-123`), genetic instruments for COVID-19 susceptibility/severity (such as *ABO*, *OAS1*, *IFNAR2*, and 3p21.31 variants) capture lifelong germline predisposition to testing positive or experiencing severe respiratory disease upon infection, not the acute environmental shock of a SARS-CoV-2 infection itself, and cannot test disease "exacerbation" in patients who already have GD (collider/index-event bias). Moreover, selecting instruments at $P < 5 \times 10^{-6}$ rather than $P < 5 \times 10^{-8}$ risks weak-instrument bias, and despite stating an (incorrect) $F$-statistic formula in the Methods, the authors never report the $F$-statistics or variance explained ($R^2$) for any instrument.

* **Sensitivity analyses, exposure/outcome directional specification, and data documentation confirm the robustness of the MR findings: [Methodologically Flawed].**  
  The manuscript repeatedly contradicts itself regarding which trait is the exposure and which is the outcome: the Results text (line 105) states that *"Regarding COVID-19 susceptibility, the IVW MR analysis indicated that GD did not significantly increase the risk"*, and Table 2 labels the columns *"Outcome: COVID-19 susceptibility | COVID-19 hospitalization | COVID-19 very severe"* and the row *"Graves disease"*, which is the exact reverse of Table 3 (*"Outcome: Graves disease | Exposure: COVID-19..."*) and the Methods. Furthermore, line 66 states that *"Detailed information regarding the genetic variants... is presented in 3/7/2025 [16]"*—an unedited date placeholder where a table of harmonized SNPs should appear.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Resolve the European–East Asian Ancestry Mismatch Between Exposure and Outcome GWAS
* **WHY:** Two-sample MR requires the exposure and outcome samples to represent the same underlying ancestral population so that instrumental SNPs share identical linkage disequilibrium (LD) tagging with causal variants and comparable allele frequencies. Pairing European COVID-19 HGI summary statistics and 1000G EUR clumping with BioBank Japan (`bbj-a-123`) violates this assumption, and claiming in the Limitations (line 181) that the study "primarily relied on data from the European population" is factually incorrect for `bbj-a-123`.
* **WHAT:** Re-run the 2SMR using ancestry-matched GWAS summary statistics for both exposure and outcome.
* **HOW:** Either (a) replace `bbj-a-123` with a European-ancestry Graves disease GWAS (e.g., FinnGen `finn-b-E4_GRAVES_STRICT` or UK Biobank / Sakaue et al. European summary statistics) while retaining European COVID-19 HGI exposures and 1000G EUR LD clumping, or (b) pair `bbj-a-123` exclusively with East Asian COVID-19 HGI summary statistics using the 1000 Genomes EAS LD reference panel.

#### 2. Audit and Re-Compute the Mathematically Impossible Confidence Intervals in Table 2
* **WHY:** In Table 2 (COVID-19 susceptibility), the MR-Egger 95% CI ($0.786\text{--}1.245$, log-width $0.460$) is asymmetrical around $\text{OR} = 1.047$ and less than one-fourth the width of the IVW 95% CI ($0.405\text{--}2.851$, log-width $1.951$). Under standard weighted linear regression theory, MR-Egger estimates an additional intercept parameter and always has a larger variance than IVW.
* **WHAT:** Re-run `TwoSampleMR::mr()` on the harmonized dataset and replace the corrupted values in Table 2.
* **HOW:** Export the exact output of `TwoSampleMR::generate_odds_ratios(mr_results)` directly from R without manual transcription, verify that $\ln(\text{OR}) = \frac{1}{2}[\ln(\text{CI}_{\text{lower}}) + \ln(\text{CI}_{\text{upper}})]$ for every row in Table 2, and check whether the IVW and MR-Egger rows or columns were transposed during table preparation.

#### 3. Correct the $F$-Statistic Equation, Report Instrument Lists, and Calculate Minimum Detectable Effect Sizes
* **WHY:** The formula in the Methods (line 76), $F = (R^2 / K) / [(1 - R^2)(N - K - 1)]$, places $(N - K - 1)$ in the denominator instead of the numerator, which yields $F \approx 0$ for large $N$. In addition, no SNP list or $F$-statistics are provided (line 66 contains the broken text `"in 3/7/2025 [16]"`), and wide CIs are misinterpreted as proof of no effect.
* **WHAT:** Correct the $F$-statistic formula, provide a complete supplementary table of all harmonized SNPs (rsID, effect/other allele, EAF, $\beta_{\text{exp}}$, $\text{SE}_{\text{exp}}$, $P_{\text{exp}}$, $\beta_{\text{out}}$, $\text{SE}_{\text{out}}$, $P_{\text{out}}$, and per-SNP $F$-statistic), and compute formal MR statistical power.
* **HOW:** Correct the equation to $F = \frac{N - K - 1}{K} \frac{R^2}{1 - R^2}$ (or per-SNP $F = \beta_{\text{exp}}^2 / \text{SE}_{\text{exp}}^2$). Use the mRnd power calculator (Brion et al.) given $N_{\text{outcome}} = 212,453$, case proportion $2,176 / 212,453 = 1.02\%$, and instrument $R^2$ to report the minimum odds ratio detectable at 80% power ($\alpha = 0.05$).

#### 4. Fix Exposure–Outcome Reversals and Temper Clinical Claims
* **WHY:** Line 105 and Table 2 state that GD is the exposure and COVID-19 is the outcome, contradicting the rest of the paper. Moreover, MR of genetic liability to COVID-19 cannot rule out environmentally triggered post-viral thyroiditis or GD relapse/exacerbation.
* **WHAT:** Standardize exposure/outcome labels across the text and tables, and reframe the Conclusions to state that genetic liability to COVID-19 showed no statistically significant association with GD within the precision limits of the instruments.
* **HOW:** Change Table 2's top header from `"Outcome"` to `"Exposure"` (and the row header `"Graves disease"` to `"Outcome: Graves disease"`), correct line 105 to state *"COVID-19 susceptibility did not significantly increase the risk of GD"*, and remove the claim in the Abstract that these results alleviate concerns about a pandemic-related surge in autoimmune thyroid disease or GD exacerbation.

#### 5. Technical and Arithmetic Cleanup in Table 1 and Text
* **WHY:** Sample sizes in the text do not match the sums of cases and controls in Table 1.
* **WHAT & HOW:**
  1. **Sample size arithmetic (line 62 vs. Table 1 line 99):** In line 62, COVID-19 hospitalization total sample size is stated as $n = 1,882,773$, whereas in Table 1, $9,986\text{ cases} + 1,877,672\text{ controls} = 1,887,658$. Verify the exact OpenGWAS accession IDs (e.g., `ebi-a-GCST011073`, `ebi-a-GCST011081`, `ebi-a-GCST011075`) and report both the OpenGWAS IDs and reconciled sample sizes in Table 1.
  2. **Broken reference/placeholder (line 66):** Replace `"is presented in 3/7/2025 [16]"` with a valid table reference and verify reference `[16]`.
