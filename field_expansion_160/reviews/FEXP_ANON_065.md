# Review of FEXP_ANON_065

**Overall Score:** **2.5 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **2.0 / 8.0**  
* **Score Breakdown:** Rigor: 0.7/3.5 | Claims: 0.4/2.5 | Biology: 0.9/2.0 | Reproducibility: 0.5/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Subfield & Study Design:** Genetic Epidemiology / Two-Sample Mendelian Randomization (MR) evaluating 11 branched-chain amino acid (BCAA) and metabolite exposures against 6 frailty-related phenotypes.
* **Data Sources:** Publicly available summary statistics from the MRC-IEU OpenGWAS database (metabolite GWASs, including chronic kidney disease [CKD]-specific metabolite cohorts) and European/Swedish frailty meta-GWAS / UK Biobank physical capability traits ($N = 164,610$ European and $N = 10,616$ Swedish participants).
* **Perceived Venue Tier:** Open-access general medical megajournal (template-driven two-sample MR report).

---

## 2. Executive Summary & Editorial Verdict

This manuscript performs a two-sample Mendelian randomization screen across 11 BCAA-related exposures (leucine, isoleucine, valine, total BCAAs, and downstream catabolites including acetoacetate, succinate, propionylcarnitine, isobutyrylcarnitine, and branched-chain ketoacids) and 6 frailty-related outcomes (frailty index, hand grip strength [left and right], physical activity, usual walking pace, and weight loss). Using inverse-variance weighted (IVW) meta-analysis as the primary estimator alongside MR-Egger, weighted median, weighted mode, and MR-PRESSO sensitivity analyses, the authors report multiple nominal associations ($P < 0.05$) and conclude that BCAAs and their metabolites have causal effects on frailty that support clinical BCAA supplementation.

**Editorial Verdict: Reject (Fundamentally Invalid).** The study suffers from fatal methodological, statistical, and logical defects that invalidate its conclusions. First, the authors test $11 \times 6 = 66$ exposure-outcome pairs without any multiple-testing correction, and when primary IVW estimates are non-significant, they selectively apply MR-PRESSO outlier removal—even when the MR-PRESSO distortion test is completely non-significant ($P = 0.38$ to $0.94$)—to manufacture post-hoc $P < 0.05$ associations ("results turn significant", Section 3.3). Second, Tables 1, 2, and 3 are truncated mid-way through the alphabetized exposure list, omitting 32 of the 66 tested pairs (including all primary results for valine, total BCAAs, propionylcarnitine, and succinate cited in the text). Third, there are direct numerical contradictions between the MR-PRESSO outlier-corrected estimates in Table 3 and the "eliminated outliers" IVW estimates in Table 4. Fourth, the authors exponentiate linear regression slopes for continuous traits (frailty index, grip strength, walking pace) and misreport them as "Odds Ratios," while combining CKD-restricted metabolite GWASs with general-population UK Biobank outcomes. Finally, the clinical conclusion in the Discussion—recommending BCAA supplementation to mitigate frailty—directly contradicts the direction of the authors' own MR estimates, which show that higher genetically predicted BCAAs *increase* the frailty index and *reduce* walking pace and grip strength.

### Assessment of Specific Conclusions
* **Claim 1: Genetically predicted leucine, isoleucine, valine, and total BCAAs causally increase the frailty index and decrease usual walking pace and right-hand grip strength:** `[Methodologically Flawed]`  
  In the primary IVW analysis (Table 1), leucine is not significantly associated with the frailty index ($P = 0.0583$) or right-hand grip strength ($P = 0.257$). The authors obtain nominal significance ($P = 0.009$ and $P = 0.0465$ in Table 4) only after removing SNPs via MR-PRESSO despite non-significant distortion tests (Distortion $P = 0.926$ and $P = 0.663$ in Table 3), and even in Table 3 the MR-PRESSO outlier-corrected estimate for leucine on right grip strength is non-significant ($\text{O.OR} = 0.9757$, $\text{O.P} = 0.0914$). None of the primary associations in Table 1 survive a Bonferroni threshold ($\alpha = 0.05/66 = 7.58 \times 10^{-4}$) or Benjamini-Hochberg FDR control across the 66 tests.
* **Claim 2: Propionylcarnitine ($OR = 15.95, P = 0.048$) and isobutyrylcarnitine ($OR = 1.48, P = 0.002$) causally increase weight loss:** `[Methodologically Flawed]`  
  The propionylcarnitine estimate ($OR = 15.9473$, 95% CI: $1.0279\text{--}247.4089$, $P = 0.048$) is absent from Table 1, relies on an underpowered instrument set (Table 4 shows only $2\text{--}3$ SNPs for propionylcarnitine), and exhibits a 240-fold confidence interval width indicative of extreme estimation instability. The isobutyrylcarnitine association with weight loss is null in primary IVW ($OR = 1.2773, P = 0.1309$, Table 1) and only becomes nominally significant after removing 1 of 6 SNPs in MR-PRESSO despite a non-significant distortion test ($P = 0.382$, Table 3).
* **Claim 3: Acetoacetate and CKD-specific plasma isobutyrylcarnitine (C4) levels causally increase hand grip strength:** `[Fragile]`  
  These effects ($P = 0.0476$, $P = 0.024$, and $P = 0.0177$) are nominal findings from 66 uncorrected tests using a relaxed instrument threshold ($P < 5 \times 10^{-6}$). Furthermore, using a GWAS of plasma isobutyrylcarnitine measured exclusively in chronic kidney disease patients introduces severe index-event (collider) bias when applied to general-population grip strength.
* **Claim 4: The MR findings support BCAA supplementation as an effective clinical strategy to mitigate frailty:** `[Overstated]`  
  This claim inverts the direction of the manuscript's own quantitative findings: the authors' MR estimates indicate that higher BCAA levels are detrimental (increasing the frailty index and slowing walking pace), yet Section 4 (Paragraph 5) cites these exact results as genetic support for administering BCAA supplements to mitigate frailty.

---

## 3. Forensic Defect Inventory

### 1. [Critical] Post-Hoc Outlier Removal ("$P$-Hacking" via MR-PRESSO) and Uncorrected Multiple Testing
* **Location:** Section 2.3–2.4, Section 3.2–3.3 (Lines 54, 97), and Tables 1, 3, and 4.
* **Defect:** The study evaluates 11 exposures across 6 outcomes ($66$ primary tests) with no adjustment for multiple comparisons. In primary IVW (Table 1), none of the associations meet a Bonferroni-adjusted threshold ($P < 7.58 \times 10^{-4}$). Crucially, when primary IVW fails to reach $P < 0.05$, the authors use MR-PRESSO to strip out SNPs and report in the Abstract and Section 3.3 that null traits "turn significant" (e.g., leucine $\to$ frailty index shifts from $P = 0.0583$ to $P = 0.009$; leucine $\to$ right grip strength shifts from $P = 0.257$ to $P = 0.0465$; isobutyrylcarnitine $\to$ weight loss shifts from $P = 0.1309$ to $P = 0.0022$). However, Table 3 shows that the MR-PRESSO Distortion Test $P$-values for these exact pairs are completely non-significant ($0.92645$, $0.6626$, and $0.38185$, respectively), meaning outlier removal did not significantly alter the causal estimate and cannot be used to upgrade null primary results into positive headline claims.
* **Remediation:** Apply Benjamini-Hochberg FDR or Bonferroni correction across all 66 primary IVW tests, and report the pre-outlier-removal IVW (or multiplicative random-effects IVW) as the primary estimate when the MR-PRESSO distortion test is non-significant ($P \ge 0.05$).

### 2. [Critical] Direct Numerical Contradictions Between Table 3 (`O.OR`) and Table 4 ("Eliminated Outliers")
* **Location:** Table 3 (Lines 140–174) vs. Table 4 (Lines 178–199).
* **Defect:** The outlier-corrected estimates in Table 3 (`O.OR` and `O.P`) contradict the post-outlier-elimination IVW results in Table 4:
  1. **Leucine $\to$ Hand grip strength (right):** Table 1 has $\text{nsnp} = 16$ ($OR = 0.9797, P = 0.257$). Table 3 reports 3 outliers removed, yielding an outlier-corrected $\text{O.OR} = 0.9757$ ($95\% \text{ CI}: 0.9502\text{--}1.0019, \text{O.P} = 0.09139$). Yet Table 4 (also with $\text{nsnp} = 16 - 3 = 13$) reports $OR = 0.9733$ ($95\% \text{ CI}: 0.9476\text{--}0.9996, P = 0.0465$), crossing the $P < 0.05$ threshold and driving a headline claim in the Abstract!
  2. **Leucine $\to$ Frailty index:** Table 1 reports $OR = 1.0645$ ($P = 0.0583$), whereas Table 3 reports raw $\text{R.OR} = 1.062$ ($P = 0.0771$) and outlier-corrected $\text{O.OR} = 1.0638$ ($P = 0.0213$), while Table 4 reports $OR = 1.0665$ ($P = 0.009$).
  3. **Isoleucine $\to$ Hand grip strength (left and right):** Table 1 has $\text{nsnp} = 9$. Table 3 states `Number of outliers = 2` with $\text{O.OR} = 0.9834$ ($P = 0.468$) for left grip and $\text{O.OR} = 0.9894$ ($P = 0.610$) for right grip. However, Table 4 lists $\text{nsnp} = 6$ (implying 3 SNPs were removed, not 2) and reports $OR = 0.9983$ ($P = 0.9326$) and $OR = 1.0005$ ($P = 0.9824$).
* **Remediation:** Audit the underlying R script (`TwoSampleMR` vs. `MR-PRESSO` harmonisation and SNP exclusion lists) to reconcile why different SNP counts and different IVW estimates are reported across Tables 1, 3, and 4 for the same exposure-outcome pairs.

### 3. [Critical] Truncation of Primary Tables 1, 2, and 3 (32 of 66 Pairs Missing)
* **Location:** Table 1 (Lines 59–94), Table 2 (Lines 102–136), and Table 3 (Lines 140–174).
* **Defect:** Tables 1, 2, and 3 list only 34 rows, cutting off abruptly after `Plasma isobutyrylcarnitine (C4) levels in chronic kidney disease -> Physical activity`. All results for `Plasma isobutyrylcarnitine (C4) levels in CKD -> Usual walking pace / Weight loss`, `Plasma succinate levels in CKD`, `Propionylcarnitine levels`, `Succinate levels`, `Total concentration of BCAAs`, and `Valine` are missing from the main tables, despite the Results text (Lines 54 and 97) explicitly citing Table 1 and Table 2 for those exact exposures.
* **Remediation:** Provide complete, un-truncated tables containing all 66 exposure-outcome comparisons across Tables 1–3.

### 4. [Major] Misreporting Continuous Linear Slopes as Odds Ratios and Index-Event Bias in CKD Exposures
* **Location:** Section 2.1, Section 2.3, Section 3.2, and Tables 1, 3, and 4.
* **Defect:** First, continuous outcomes (Frailty Index, right/left hand grip strength in kg, physical activity, and usual walking pace category score) are analyzed via linear GWAS models, so $\exp(\beta)$ is not an Odds Ratio (OR). Second, three of the 11 exposure GWASs were conducted exclusively within chronic kidney disease (CKD) cohorts (e.g., plasma isobutyrylcarnitine in CKD). Conditioning exposure genetic associations on a severe chronic disease (CKD) induces collider bias and invalidates two-sample MR when paired with general-population frailty outcomes. Third, UK Biobank Nightingale metabolomics (leucine, isoleucine, valine, total BCAAs, acetoacetate) and UK Biobank frailty/grip/walking pace outcomes share substantial participant overlap, which is unacknowledged and unaddressed.
* **Remediation:** Report $\beta$ (with 95% CIs in SD units) for continuous outcomes, remove disease-conditioned (CKD-restricted) exposure GWASs or perform formal collider-bias correction, and quantify sample overlap between the UK Biobank metabolomic and frailty GWAS cohorts.

### 5. [Major] Logical Inversion of Effect Direction in Clinical Interpretation and Translation Errors
* **Location:** Section 3.3 (Line 97) and Section 4 (Lines 205–213).
* **Defect:** The authors' MR estimates show that genetically higher BCAA levels *increase* the Frailty Index ($OR > 1$) and *slow* usual walking pace ($OR < 1$). Yet in Section 4 (Line 213), the authors write: *"This study supported the causal association between BCAAs and their metabolites and frailty, suggesting that BCAA supplementation may be an effective strategy to improve nutritional status and mitigate frailty."* Furthermore, Line 97 contains egregious translation artifacts, referring to horizontal pleiotropy as *"level polytropy"* and forest plots as *"Foster plots"*.
* **Remediation:** Remove the unsupported recommendation for clinical BCAA supplementation that contradicts the direction of the genetic estimates, and correct all terminology errors.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.7** | **3.5** | 66 uncorrected tests; post-hoc MR-PRESSO outlier removal used to turn null primary IVW estimates into "significant" findings despite non-significant distortion tests; continuous linear slopes misreported as ORs; unaddressed UK Biobank sample overlap and CKD collider bias. |
| **2. Claim-to-Evidence Alignment** | **0.4** | **2.5** | Headline causal claims rely on uncorrected nominal $P$-values or post-hoc outlier removal; clinical conclusion recommending BCAA supplementation directly inverts the harmful direction of the authors' own MR estimates; unstable $OR = 15.95$ (CI: $1.03\text{--}247.41$) over-interpreted. |
| **3. Data Integrity & Biological Plausibility** | **0.9** | **2.0** | Use of CKD-stratified metabolite GWASs with relaxed $P < 5 \times 10^{-6}$ instruments introduces index-event bias and weak-instrument/pleiotropy risk; biological discussion is internally contradictory. |
| **4. Reproducibility & Data Integrity** | **0.5** | **2.0** | Tables 1, 2, and 3 are truncated after row 34 (omitting 32 of 66 pairs cited in text); direct numerical contradictions between Table 3 (`O.OR`/`nsnp`) and Table 4; severe translation errors ("level polytropy", "Foster plots"). |
| **Scientific Core Score** | **2.0** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **2.5** | **10.0** | **Fundamentally Invalid** (25 / 100 equivalent). |
