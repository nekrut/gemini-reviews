# Forensic Scientific Review: FEXP_ANON_078

**Overall Score:** **2.0 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.5 / 8.0**
* **Score Breakdown:** Rigor: 0.6/3.5 | Claims: 0.4/2.5 | Biology: 0.5/2.0 | Reproducibility: 0.5/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Field & Subfield:** Cardiometabolic Epidemiology / Statistical Genetics / Microbiome & Metabolomics Research (Two-Sample and Two-Step Mediation Mendelian Randomization of 473 gut microbiota taxa and 233 circulating metabolites across five cardiometabolic diseases).
* **Perceived Study Design:** Public-summary-data univariable, bidirectional, and two-step mediation Mendelian Randomization combining 473 FINRISK 2002 fecal metagenomic taxa (`GCST90032172`–`GCST90032644`, Qin et al., $N = 5,959$), 233 NMR metabolomic traits (`GCST90301941`–`GCST90302173`, Karjalainen et al., $N = 136,016$), and five cardiometabolic disease GWASs (`CAD`, `T2D`, `Stroke`, `Heart Failure`, and `Hypertension`).

---

## 2. Executive Summary & Editorial Verdict
This manuscript conducts an unadjusted combinatoric screen of $473\text{ gut microbial taxa} \times 5\text{ cardiometabolic diseases} = 2,365\text{ tests}$ and $233\text{ circulating metabolites} \times 5\text{ diseases} = 1,165\text{ tests}$, culminating in five claimed two-step "mediation pathways" (`Section 3.4`, `Line 114`). Forensically, the central mediation findings of the paper are statistically null, and the univariable microbiome screen is indistinguishable from random noise. First and most fatally, **every single one of the five reported mediation effects in `Section 3.4` (`Line 114`) has a 95% confidence interval that squarely crosses zero** ($P \approx 0.10\text{ to }0.66$), meaning that **zero** statistically significant mediation pathways were actually identified despite the Abstract and Conclusion presenting them as established causal mediation mechanisms. Second, across the $473 \times 5 = 2,365$ gut microbiota–disease tests, at a nominal threshold of $\alpha = 0.05$, one expects $2,365 \times 0.05 = \mathbf{118.25}$ false-positive associations purely by chance; the authors observe $23 + 23 + 22 + 20 + 19 = \mathbf{107}$ nominal associations (fewer than expected under the global null!) and admit in `Line 68` that **zero** gut microbiota associations survive Bonferroni correction ($P < 1.057 \times 10^{-4}$). Third, `Section 3.1.2` (`Lines 78 and 85`) contains verbatim copy-paste numerical duplications where two completely distinct metabolites are assigned identical `OR`, `95% CI`, and `P`-values to four decimal places. Fourth, the hypertension outcome (`ukb-b-12493`, Elsworth et al. UK Biobank) is a linear probability model on the $0/1$ scale while the other four diseases are on the logistic log-odds scale, compressing all hypertension ORs into `[0.991, 1.019]` (`Lines 66, 94`), and the reverse MR uses an unjustifiably relaxed $P < 5 \times 10^{-5}$ instrument threshold (`Line 48`) despite massive disease GWAS sample sizes ($N = 446,696\text{ to }977,323$).

* **Claim 1:** *"Mediation analysis revealed five key pathways: CAG-488 sp000434055 mediates CAD via lactate levels... UBA3855 sp900316885 influences T2D through the ratio of omega-3 fatty acids to total fatty acids... Ruminococcus C sp000437255 affects HF via the triglycerides-to-total lipids ratio in medium VLDL... and CAG-882 and Atopobiaceae impact HT through the phospholipids-to-total lipids ratio in large HDL and very small VLDL, respectively."* — **`[Methodologically Flawed]`** (Every single one of the five reported mediation effects in `Section 3.4 Line 114` has a 95% CI spanning zero: `0.0146 [-0.0504, 0.0796]`, `0.0078 [-0.0034, 0.0191]`, `-0.0050 [-0.0221, 0.0121]`, `0.0010 [-0.0002, 0.0022]`, and `0.0022 [-0.0040, 0.0083]`; none is statistically significant).
* **Claim 2:** *"While several GM and blood metabolites showed potential causal associations with CMDs at P < .05, only a few blood metabolites remained statistically significant after Bonferroni correction, and no GM met the corrected threshold."* — **`[Well Supported]`** (This is an accurate admission in `Line 68`, though the authors immediately ignore it to build their main claims around the unadjusted nominal hits).
* **Claim 3:** *"Specifically, we found the following: (1) CAD: Three causal relationships were identified, including lactate levels (OR = 1.639, 95% CI: 1.123–2.392, P = .0104), the cholesteryl ester-to-total lipid ratio in very small VLDLs (OR = 1.639, 95% CI: 1.123–2.392, P = .0104)..."* — **`[Methodologically Flawed]`** (Verbatim copy-paste error assigning the exact same OR, 95% CI, and $P$-value to two distinct metabolites in `Line 78`, repeated again in `Line 85` for two HDL traits).

---

## 3. Forensic Defect Inventory

### 3.1 Major Statistical, Mathematical, and Reporting Defects

1. **All Five Reported Mediation Pathways Have Non-Significant 95% Confidence Intervals Crossing Zero (`Section 3.4`, `Line 114`):**
   * The primary selling point of the manuscript is its two-step MR mediation analysis (`GM -> Metabolite -> CMD`). Let us inspect the exact numbers reported by the authors in `Section 3.4` (`Line 114`) and recover their implied standard errors and $Z$-scores ($Z = \hat{\beta}_{\text{med}} / \text{SE}$, where $\text{SE} = (\text{CI}_{\text{upper}} - \text{CI}_{\text{lower}}) / 3.92$):
     1. **`CAG-488 sp000434055 -> Lactate -> CAD`:** $\hat{\beta}_{\text{med}} = 0.0146$, $\text{95\% CI} = [-0.0504, 0.0796]$ ($\text{SE} = 0.0332$, $Z = 0.44$, **$P = 0.660$**).
     2. **`UBA3855 sp900316885 -> Omega-3 ratio -> T2D`:** $\hat{\beta}_{\text{med}} = 0.0078$, $\text{95\% CI} = [-0.0034, 0.0191]$ ($\text{SE} = 0.00574$, $Z = 1.36$, **$P = 0.174$**).
     3. **`Ruminococcus C sp000437255 -> TG-to-total lipids in medium VLDL -> HF`:** $\hat{\beta}_{\text{med}} = -0.0050$, $\text{95\% CI} = [-0.0221, 0.0121]$ ($\text{SE} = 0.00872$, $Z = -0.57$, **$P = 0.567$**).
     4. **`CAG-882 -> PL-to-total lipids in large HDL -> HT`:** $\hat{\beta}_{\text{med}} = 0.0010$, $\text{95\% CI} = [-0.0002, 0.0022]$ ($\text{SE} = 0.00061$, $Z = 1.63$, **$P = 0.102$**).
     5. **`Atopobiaceae -> PL-to-total lipids in very small VLDL -> HT`:** $\hat{\beta}_{\text{med}} = 0.0022$, $\text{95\% CI} = [-0.0040, 0.0083]$ ($\text{SE} = 0.00314$, $Z = 0.70$, **$P = 0.483$**).
   * Not a single one of the five mediation pathways achieves even nominal statistical significance ($P < 0.05$). Worse, in `Section 2.3.3` (`Line 50`), the authors write: *"If the total effect is positive, both the direct and indirect effects must also be positive; if the total effect is negative, both the direct and indirect effects must also be negative. Mediators that do not meet this directional consistency are excluded from further mediation analysis."* Yet in `Line 114` they report `Ruminococcus C sp000437255 -> HF` with a negative mediation effect (`-0.0050`) that is not even listed among the top HF associations in `Section 3.1.1` (`Line 64`).

2. **Expected Null False-Positive Yield Across $2,365$ Gut Microbiota Tests (`Section 3.1.1`, `Lines 56–68`):**
   * The authors tested $473$ microbial taxa across $5$ cardiometabolic outcomes ($473 \times 5 = 2,365$ tests) using a relaxed instrument selection threshold of $P < 1 \times 10^{-5}$.
   * Under the complete null hypothesis of zero causal relationships, testing $2,365$ independent hypotheses at $\alpha = 0.05$ yields an expected $2,365 \times 0.05 = \mathbf{118.25}$ false-positive hits. The authors find $23\text{ (CAD)} + 23\text{ (T2D)} + 22\text{ (Stroke)} + 20\text{ (HF)} + 19\text{ (HT)} = \mathbf{107}$ hits at $P < 0.05$, and zero hits at the Bonferroni threshold ($P < 1.057 \times 10^{-4}$). Hence, the entire gut microbiome univariable screen shows no enrichment over pure random noise.

3. **Identical Duplicated Effect Estimates Assigned to Distinct Metabolites (`Section 3.1.2`, `Lines 78 and 85`):**
   * In `Line 78`, the manuscript states:
     > *"lactate levels (OR = 1.639, 95% CI: 1.123–2.392, P = .0104), the cholesteryl ester-to-total lipid ratio in very small VLDLs (OR = 1.639, 95% CI: 1.123–2.392, P = .0104)"*
   * Two completely unrelated NMR metabolites (`lactate levels` and `cholesteryl ester-to-total lipid ratio in very small VLDLs`) are reported with the exact same `OR` (`1.639`), `95% CI` (`1.123–2.392`), and `P`-value (`.0104`).
   * Seven lines later, in `Line 85`, two different HDL traits (`phospholipid ratio in medium HDLs` and `concentration of medium HDL particles`) are reported with the exact same `OR = 0.917, 95% CI: 0.848–0.992`.

4. **Linear Probability Scale Incompatibility for Hypertension (`Elsworth et al.`) and Relaxed $P < 5 \times 10^{-5}$ Reverse MR Threshold (`Lines 33, 48, 66, 94`):**
   * While `CAD`, `T2D`, `Stroke`, and `HF` are analyzed using case-control logistic GWAS summary statistics (`OR` values around `0.78–1.64`), `Hypertension` uses the Elsworth et al. MRC-IEU UK Biobank linear probability (`BOLT-LMM`) summary statistics (`119,731` cases / `343,202` controls; prevalence $\mu = 0.2587$), where $\beta_{\text{linear}} \approx \mu(1-\mu)\beta_{\text{logistic}} \approx 0.192\,\beta_{\text{logistic}}$. Because the authors exponentiated $\beta_{\text{linear}}$ directly without scale conversion, all reported Hypertension ORs (`Lines 66, 94`) are artificially compressed into `0.991–1.019`.
   * In `Section 2.3.2` (`Line 48`), for reverse MR where `CAD`, `T2D`, `Stroke`, `HF`, and `HT` are the exposures ($N = 446,696\text{ to }977,323$, each having dozens to hundreds of genome-wide significant loci at $P < 5 \times 10^{-8}$), the authors inexplicably relaxed the instrument selection threshold to **$P < 5 \times 10^{-5}$**, flooding the reverse MR with hundreds of weak and pleiotropic sub-threshold variants.
   * Finally, in `Section 2.2` (`Line 38`), the authors claim *"Initially, SNPs significantly associated with GM, blood metabolites, and CMDs were selected using a stringent threshold of P < 1 × 10^-5"*, contradicting `Figure 1` and `Section 2.3.1` (`Line 44`), which state that $P < 5 \times 10^{-8}$ was used for blood metabolites.

---

## 4. Quantitative Rubric Scoring

* **1. Methodological & Statistical Rigor (0.6 / 3.5):** All five claimed mediation effects are statistically non-significant (95% CIs cross zero); zero gut microbiota associations survive multiple-testing correction (107 nominal hits vs. 118 expected by chance); linear probability scale distortion for hypertension; and an inappropriate $P < 5 \times 10^{-5}$ threshold for large-sample reverse MR.
* **2. Substantiation of Claims & Internal Consistency (0.4 / 2.5):** Claiming five positive mediation pathways when all five confidence intervals include zero is a fundamental misrepresentation of the statistical output, compounded by verbatim duplicated numbers for distinct metabolites in `Section 3.1.2`.
* **3. Biological, Evolutionary, or Clinical Plausibility & Novelty (0.5 / 2.0):** Mechanical combinatoric execution of `TwoSampleMR` across 473 taxa and 233 metabolites without biological validation or credible mediation signal.
* **4. Reproducibility, Data Hygiene & Transparency (0.5 / 2.0):** Main text contains no structured results tables (relying entirely on inline lists with copy-pasted numbers and supplementary files), and instrument selection thresholds contradict between `Section 2.2` and `Section 2.3.1`.
