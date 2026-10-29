# Review of FEXP_ANON_069

**Overall Score:** **3.8 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.9 / 8.0**  
* **Score Breakdown:** Rigor: 1.1/3.5 | Claims: 0.9/2.5 | Biology: 0.9/2.0 | Reproducibility: 0.9/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Subfield & Study Design:** Genetic Epidemiology / Bidirectional Two-Sample Mendelian Randomization (MR) with Discovery and Replication Outcomes investigating 8 sarcopenia (SA)-related traits and cognitive performance.
* **Data Sources:** UK Biobank exposure GWASs from the MRC-IEU pipeline (`ukb-b-*`, $N = 454,672\text{--}461,089$ for right/left grip strength, appendicular and whole-body fat-free mass, and usual walking pace), discovery cognitive performance GWAS (`ebi-a-GCST006572`, Lee et al. 2018, $N = 257,841$), and replication cognitive function GWAS (`ieu-b-4838`, $N = 22,593$).
* **Perceived Venue Tier:** Open-access general medical megajournal.

---

## 2. Executive Summary & Editorial Verdict

This study conducts a bidirectional two-sample Mendelian randomization (MR) analysis examining the relationships between eight sarcopenia-related phenotypes in the UK Biobank (right and left hand grip strength, right and left arm fat-free mass, right and left leg fat-free mass, whole-body fat-free mass, and usual walking pace) and cognitive performance in a discovery dataset (`ebi-a-GCST006572`, $N = 257,841$) and a replication dataset (`ieu-b-4838`, $N = 22,593$). In the discovery cohort, random-effects IVW yields statistically significant positive associations for 7 of the 8 traits (all except left hand grip strength), and reverse MR identifies a positive association of cognitive performance on usual walking pace. In the replication cohort (`ieu-b-4838`), only 2 of the 8 traits (left leg fat-free mass, $P = 0.047$, and whole-body fat-free mass, $P = 0.013$) reach nominal significance, while grip strength and walking pace fail to replicate.

**Editorial Verdict: Reject / Major Revision Required (Flawed / Overstated).** The manuscript suffers from four major methodological flaws: (1) **Massive unacknowledged sample overlap ($\sim 86\%$)** between the UK Biobank exposure datasets and the discovery outcome dataset (`ebi-a-GCST006572`, in which $222,543$ of the $257,841$ participants are from the UK Biobank), compounded by relaxed LD clumping ($r^2 < 0.01$ within $1,000\text{ kb}$) that retains nearly 500 partially correlated SNPs per lean-mass trait; (2) **Uncontrolled confounding by body size (height/BMI), assortative mating, and dynastic effects** in unadjusted fat-free mass and walking pace instruments, which explains why 6 of the 8 traits—including the headline walking pace association—fail to replicate in the smaller within-sibship/replication dataset (`ieu-b-4838`); (3) **Misreporting linear regression slopes ($\beta$) for continuous cognitive scores as "Odds Ratios (OR)"** and misinterpreting higher ORs in the Methods as "increased risk of the outcome" when higher values actually represent *better* cognitive performance; and (4) **Multiple editorial, equation, and numerical formatting errors** across Tables 1 and 2 and Section 2.3.

### Assessment of Specific Conclusions
* **Claim 1: Genetically predicted usual walking pace has a strong bidirectional causal relationship with cognitive performance ($OR = 1.414, P < 0.001$ forward; $OR = 1.067, P < 0.001$ reverse):** `[Fragile]`  
  First, the forward effect fails to replicate in the `ieu-b-4838` cohort (Fig. 6, Line 118). Second, in the reverse MR (`Cognitive performance -> Usual walking pace`), the MR-Egger estimate is completely null (Line 132: *"However, the MR Egger method did not reveal any discernible causal effect"*), and Cochran's $Q$ shows extreme heterogeneity ($Q = 308.96, P < 0.001$, Table 3). Third, the discovery analysis suffers from ~86% sample overlap within the UK Biobank, where usual walking pace and cognitive test performance are heavily co-confounded by educational attainment, socioeconomic status, and general health.
* **Claim 2: Genetically predicted whole-body and appendicular fat-free mass causally improve cognitive performance:** `[Fragile]`  
  Whole-body fat-free mass (`ukb-b-13354`) and limb fat-free mass in the UK Biobank are unadjusted for height and total body weight; consequently, their ~450–497 genetic instruments primarily index stature and body size, which exhibit well-documented assortative mating and dynastic correlations with cognitive ability in population-level GWASs. Without multivariable MR adjusting for height, BMI, and educational attainment, attributing these associations to skeletal muscle mass per se (sarcopenia) is unsupported. Moreover, none of the replicate associations in `ieu-b-4838` ($P = 0.047$ and $P = 0.013$) survive multiple-testing correction across the 8 traits ($\alpha = 0.05/8 = 0.00625$).
* **Claim 3: Right hand grip strength ($OR = 1.112, P = 0.005$) causally increases cognitive performance:** `[Fragile]`  
  Right hand grip strength fails to replicate in `ieu-b-4838` (Fig. 6), left hand grip strength is non-significant in the discovery IVW analysis ($P > 0.05$, Line 86), and scaling grip strength without adjusting for height/body size confounds upper-body isometric strength with overall stature.

---

## 3. Forensic Defect Inventory

### 1. [Critical] Unacknowledged ~86% Sample Overlap Between UK Biobank Exposures and Discovery Outcome (`ebi-a-GCST006572`)
* **Location:** Section 2.2 (Lines 37–39) and Section 4 (Lines 167, 185).
* **Defect:** All eight sarcopenia exposure GWASs (`ukb-b-*`, $N = 454,672\text{--}461,089$) are derived from the UK Biobank. The discovery cognitive performance GWAS (`ebi-a-GCST006572`, Lee et al. 2018, $N = 257,841$) is a meta-analysis of the COGENT consortium ($N = 35,298$) and the UK Biobank ($N = 222,543$)—meaning 86.3% of the discovery outcome sample consists of the exact same UK Biobank participants as the exposure GWASs. Furthermore, the authors claim in the Discussion (Line 185: *"we utilized data on SA-related traits and cognitive performance from 2 independent GWAS datasets"*) that the exposure and outcome datasets are independent. In two-sample MR with substantial sample overlap and hundreds of polygenic instruments clumped at a liberal $r^2 < 0.01$ within $1,000\text{ kb}$ ($451\text{--}497$ SNPs per fat-free mass trait), weak-instrument and Winner's-curse bias pull the two-sample IVW estimate toward the confounded observational correlation.
* **Remediation:** Acknowledge the ~86% UK Biobank overlap in `ebi-a-GCST006572`, tighten clumping to the standard $r^2 < 0.001$ within $10,000\text{ kb}$, apply formal sample-overlap correction (`MRlap`), and apply Bonferroni/FDR correction across the 8 traits in both discovery and replication cohorts.

### 2. [Major] Failure to Adjust for Height, Body Size, and Socioeconomic Confounding via Multivariable MR
* **Location:** Section 2.2 (Line 37) and Section 3.1 (Lines 86, 118).
* **Defect:** Unlike clinical sarcopenia definitions (e.g., AWGS/EWGSOP2 appendicular skeletal muscle mass index, $\text{ASMI} = \text{ALM}/\text{height}^2$), the UK Biobank fat-free mass traits (`ukb-b-13354`, `ukb-b-19520`, etc.) and raw hand grip strength (`ukb-b-10215`, `ukb-b-7478`) are unscaled for height or BMI. Tall individuals have substantially greater absolute fat-free mass in all four limbs and greater absolute grip strength, and height is genetically correlated with cognitive test scores via assortative mating and dynastic stratification. This explains both the extreme heterogeneity across all 8 traits ($Q = 391\text{--}1201, P < 0.001$ in Table 2) and why 6 of the 8 traits fail to reach even nominal significance in `ieu-b-4838` (and none survive Bonferroni correction $P < 0.00625$ in `ieu-b-4838`).
* **Remediation:** Conduct multivariable MR (MVMR) conditioning on height, BMI, and educational attainment, or use height/BMI-adjusted appendicular lean mass summary statistics.

### 3. [Major] Misreporting Continuous Linear Effect Sizes ($\beta$) as Odds Ratios (ORs)
* **Location:** Abstract (Line 5), Section 2.4.1 (Line 68), and Section 3.1–3.2 (Lines 86, 118, 132).
* **Defect:** Cognitive performance (`ebi-a-GCST006572` and `ieu-b-4838`), fat-free mass, grip strength, and walking pace category are all continuous/ordinal quantitative variables analyzed via linear regression, not binary case-control outcomes. Exponentiating a linear $\beta$ (SD change in cognitive score per SD change in exposure) does not yield an Odds Ratio (OR). Worse, Section 2.4.1 (Line 68) states: *"A causal effect was considered statistically significant if the P-value was <.05, indicating a potentially increased risk of the outcome attributable to the exposure. Odds ratios (OR) with corresponding 95% confidence intervals (CIs) were used..."*—which confuses a positive linear effect on cognitive test performance ($\beta > 0$, better cognition) with an "increased risk" of disease.
* **Remediation:** Report $\beta$ coefficients and 95% CIs on their native SD scale instead of mislabeling $\exp(\beta)$ as an Odds Ratio.

### 4. [Minor] Missing $F$-Statistic Equation, Truncated Scientific Notation in Table 2, and Digit Grouping Errors in Table 1
* **Location:** Table 1 (Lines 42–54), Section 2.3 (Lines 58–60), and Table 2 (Line 101).
* **Defect:**
  1. The $F$-statistic formula referenced on Line 58 (*"The F-statistic was calculated utilizing the following formula:"*) is completely missing from the manuscript (blank line 59).
  2. In Table 2 (Line 101), the MR-Egger intercept for `Right leg fat-free mass -> Cognitive performance` is reported as `3.031` ($P = 0.959$), whereas all other fat-free mass traits have intercepts `<0.001`. An intercept of `3.031` per allele is impossible and reflects a truncated scientific notation exponent (e.g., `3.031e-05`).
  3. In Table 1 (Lines 45–54) and Line 39, numbers have corrupted comma placements: sample size `225,93` (instead of `22,593`), SNP count `671,966,1` and `6719,661` (instead of `6,719,661`), and `9851,867` (instead of `9,851,867`).
* **Remediation:** Insert the missing $F$-statistic equation, fix the truncated exponent on `3.031` in Table 2, and correct all comma placements in Table 1.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.1** | **3.5** | Unacknowledged ~86% UK Biobank sample overlap in discovery analysis; relaxed $r^2 < 0.01$ ($1,000\text{ kb}$) clumping; no MVMR adjustment for height/BMI/education; no multiple-testing correction across 8 correlated traits; continuous slopes misreported as ORs. |
| **2. Claim-to-Evidence Alignment** | **0.9** | **2.5** | Claims robust causal effects for grip strength and walking pace despite both failing to replicate in `ieu-b-4838` and reverse walking-pace MR failing in MR-Egger; conflates unadjusted body-size fat-free mass with clinical sarcopenia. |
| **3. Data Integrity & Biological Plausibility** | **0.9** | **2.0** | Raw limb/whole-body fat-free mass in UKB is heavily confounded by stature and body size rather than indexing sarcopenic muscle wasting; biological discussion is repetitive and speculative. |
| **4. Reproducibility & Data Integrity** | **0.9** | **2.0** | Missing $F$-statistic equation in Section 2.3; truncated scientific notation (`3.031` intercept) in Table 2; corrupted comma separators (`225,93`, `671,966,1`) in Table 1; public OpenGWAS IDs are documented. |
| **Scientific Core Score** | **2.9** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **3.8** | **10.0** | **Flawed / Overstated** (38 / 100 equivalent). |
