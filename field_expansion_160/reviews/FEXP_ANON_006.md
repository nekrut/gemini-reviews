# Review of FEXP_ANON_006

**Overall Score:** **7.4 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.6 / 8.0**  
* **Score Breakdown:** Rigor: 2.2/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.8/2.0

---

## 1. Blinded Metadata Perception
* **Anonymized Manuscript ID:** `FEXP_ANON_006`
* **Perceived Domain & Design:** Viral phylodynamics and molecular epidemiology; genomic, phylogeographic, and age-distribution analysis of seasonal influenza resurgence (predominantly influenza B/Victoria clades 3a1 and 3a2) in mainland China during COVID-19 non-pharmaceutical interventions and international border closures (2020–2021; $n = 2,299$ Chinese and $n = 955$ global sequences from GISAID plus WHO GISRS surveillance records).
* **Blinding Integrity:** Double-blind review maintained; evaluated strictly on internal phylogenetic, phylodynamic, and epidemiological merits at $t_0$.

---

## 2. Executive Summary & Editorial Verdict

This study investigates the cryptic persistence and 2020–2021 resurgence of seasonal influenza in mainland China during COVID-19 international border closures. Using WHO GISRS surveillance counts ($98.7\%$ of $n = 11,082$ confirmed cases between Oct 2020 and Sept 2021 were influenza B/Victoria) and GISAID whole-genome sequences ($n = 2,299$ from China), the authors show that whereas A(H1N1), A(H3N2), and B/Yamagata largely disappeared, two B/Victoria subclades (3a1, $n=430$; 3a2, $n=243$) persisted endemically from 2019 ancestors and expanded across China starting in late 2020. Whole-genome tanglegrams and RDP5 analyses reveal that Chinese 3a2 viruses retained an un-reassorted 3a backbone and acquired a unique HA1 H122Q substitution (characteristic of B/Yamagata), whereas global 3a2 viruses outside China (including vaccine strain B/Austria/1359417/2021) were inter-clade reassortants carrying NA, PB2, PA, MP, and NS segments from clade V1A. Using BEAST (GMRF Skyride, Bayesian Skyline, BSSVS discrete phylogeography across 6 region groups with subsampling sensitivity checks of $<10$ sequences/province/month, and BEAST2 BDSKY), the authors reconstruct inter-regional spread (identifying eastern China / Jiangxi province as a primary source) and note a shift in the age distribution of sequenced cases toward individuals $>10$ years old ($35\% \to 45\%$).

**Editorial Verdict: Minor Revision (Strong / Sound).** This is an informative, biologically perceptive study with strong open-data compliance (supplementary data and GitHub repository `[GITHUB_REPO_REDACTED]`). Its core genomic findings—endemic persistence of non-reassorted 3a1/3a2 in China, global 3a2 reassortment, and the China-specific HA1 H122Q mutation—are solid. However, the phylodynamic and epidemiological analyses contain three technical flaws that require correction or tempering: (1) an internal contradiction between the Methods (line 33) and Figure 4 legend (line 70) regarding how $R_e(t)$ was estimated, alongside an improper two-stage BDSKY procedure where the tree topology was fixed from a *coalescent* GMRF Skyride model and re-analyzed under a *strict clock* with fixed rates to infer birth-death $R_e$; (2) over-interpretation of holiday-associated $R_e$ fluctuations and early $R_e = 4.0$ ($95\%\text{ HPD } [0.2, 9.1]$) when intervals span below 1.0; and (3) unadjusted ascertainment bias in the age distribution of GISAID-sequenced cases during 2020–2021 (when school closures and adult fever-clinic COVID-19 screening altered age-specific testing rates).

### Assessment of Specific Claims
* **Claim 1 (Seasonal influenza resurgence in China in 2020–2021 was overwhelmingly driven by domestic persistence of B/Victoria clades 3a1 and 3a2, with Chinese 3a2 carrying a novel HA1 H122Q mutation and lacking the 5-segment V1A reassortment seen in global 3a2): [Well Supported].**  
  Demonstrated by 8-segment ML trees, tanglegrams (Figure 2), RDP5 screening, and sequence conservation analysis across $>20$ years of B/Victoria and B/Yamagata HA1 sequences.
* **Claim 2 (Eastern China [specifically Jiangxi province] acted as the primary source for nationwide dissemination of clades 3a1 and 3a2, with northwest and southwest China acting as secondary sources): [Moderately Supported].**  
  Supported by BSSVS discrete-trait phylogeography ($BF > 100$) and verified via downsampling ($<10$ sequences per province per month, Supplementary Fig. S8) to mitigate geographic sampling skew. However, grouping 31 provinces into 6 broad macro-regions while making province-specific claims about Jiangxi (based on Supplementary Data S3) should be presented with explicit Bayes factor support at the provincial level.
* **Claim 3 (Fluctuations in $R_e$ followed major holiday periods [National Day, Spring Festival, summer vacation], starting at $R_e = 4.0$ for clade 3a2 in late September 2020): [Fragile].**  
  First, the reported initial $R_e = 4.0$ for clade 3a2 has a $95\%\text{ HPD}$ of $0.2\text{–}9.1$ (line 67), which spans from near-zero to 9 and provides no statistical resolution. Second, the slight bumps around holidays have heavily overlapping HPDs (e.g., $1.5$ [$0.8\text{–}2.3$] to $1.8$ [$1.5\text{–}2.2$]) and no formal time-series or changepoint test linking holiday mobility to $R_e$. Third, the BDSKY estimation procedure itself is methodologically inconsistent (see Defect 1 below).
* **Claim 4 (The age profile of B/Victoria infections shifted toward older individuals [$>10$ years increasing from $<35\%$ to $\sim 45\%$] in 2020–2021, and the early-2000s birth cohort exhibits immune imprinting protection): [Fragile].**  
  Figure 6 is computed exclusively from *sequenced isolates submitted to GISAID*, not age-stratified surveillance incidence denominators. During 2020–2021 in China, stringent COVID-19 fever-clinic screening for working-age adults (20–30 years) and school closures for children (10–20 years) directly altered which age groups presented to sentinel hospitals and had specimens sequenced, without any statistical test or denominator adjustment.

---

## 3. Forensic Defect Inventory

1. **Pillar 3 & 7 Violation — Contradictory and Incompatible BDSKY $R_e$ Inference Protocol (Methods line 33 vs. Figure 4 Legend line 70):**  
   * **Contradiction between Methods and Figure 4:** Methods (line 33) states that $R_e$ was estimated in BEAST v2.6.3 using a birth-death serial skyline (BDSKY) model on a fixed tree topology from the GMRF Skyride coalescent model. However, the Figure 4 legend (line 70) states: *"Curves coloured by clades (3a1, 3a2, and V1A.3-China) represent the mean effective reproductive rate ($R_e$) with 95 per cent confidence intervals based on influenza B/Victoria positive cases per week reported from China to GISRS."* Wait: GISRS weekly positive case counts are not typed to subclades 3a1, 3a2, and V1A.3-China, so Figure 4 must be from sequence-based BDSKY, making the Figure 4 legend inaccurate!
   * **Incompatible Coalescent-to-Birth-Death Conditioning and Clock Switch:** In line 33, the authors inferred the tree topology in BEAST v1.10.4 (misspelled `v.10.1.4`) under an *uncorrelated lognormal relaxed clock* and a *GMRF Skyride coalescent* prior, then fixed that topology in BEAST v2.6.3 and re-estimated internal node heights under a *strict clock* (fixing rates to $1.35 \times 10^{-3}$ and $1.65 \times 10^{-3}$) with a *BDSKY birth-death* prior. Conditioning a birth-death skyline model on a fixed coalescent tree topology while switching from a relaxed clock to a fixed-rate strict clock suppresses topological uncertainty and distorts branching-time intervals near the tips.
2. **Pillar 2 & 4 Violation — Unadjusted Selection Bias in GISAID Sequence Age Distributions and Missing Statistical Tests (Results line 83, Figure 6):**  
   The claim that infections in individuals $>10$ years increased from $<35\%$ to $\sim 45\%$ in 2020–2021 and that the early-2000s birth cohort had fewer infections is presented purely as descriptive histograms of GISAID sequence metadata (Figure 6) without any $\chi^2$, Kolmogorov-Smirnov, or age-period-cohort regression model, and without normalizing by the age distribution of ILI/SARI sentinel testing during China's 2020–2021 COVID-19 control regime.
3. **Pillar 2 Violation — Exclusion of 2019 Clade 3a2 Sequences Due to "Poor Temporal Signal" Before Estimating 3a2 tMRCA and $R_e$ (Results line 58, Methods line 33):**  
   Line 58 notes that the 2019 Chinese 3a2 sequences ($n=2$) were excluded from the phylodynamic dataset "due to poor temporal signal or incorrect metadata," and line 33 sets a hard lower bound on the BDSKY origin prior of 3a2 at `1 January 2020`. Excluding the 2019 ancestral sequences and truncating the origin prior at Jan 1, 2020 artificially forces the post-lockdown 3a2 tMRCA to late 2020 (Sept 18, 2020) and inflates the initial September 2020 $R_e$ estimate ($4.0$, HPD $0.2\text{–}9.1$).
4. **Pillar 7 Violation — Software Version Typo and Missing Quantitative Uncertainty on Age Claims:**  
   * Line 33 twice refers to `BEAST (v.10.1.4)` instead of `BEAST (v.1.10.4)`.
   * Line 58 has a typo: `a well as V1A.3-China` $\to$ `as well as V1A.3-China`.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.2** | **3.5** | Solid 8-segment reassortment analysis, RDP5 verification, and downsampled phylogeographic sensitivity checks; penalized for the ad-hoc two-stage coalescent-topology $\to$ strict-clock BDSKY $R_e$ pipeline and absence of formal statistical tests on age distributions and holiday $R_e$ shifts. |
| **2. Claim-to-Evidence Alignment** | **1.8** | **2.5** | Core evolutionary and phylogeographic claims are well supported; claims of holiday-driven $R_e$ fluctuations and birth-cohort immune imprinting are speculative relative to the wide HPDs and unadjusted sequence metadata. |
| **3. Data Integrity & Biological/Behavioral Plausibility** | **1.6** | **2.0** | Strong biological insight on HA1 H122Q and inter-clade reassortment; dropping 2019 3a2 sequences and truncating the 3a2 origin prior at Jan 1, 2020 biases early 2020 3a2 dynamics. |
| **4. Reproducibility & Data Integrity** | **1.8** | **2.0** | Complete GISAID accession tables and analysis files deposited on GitHub (`vjlab/fluduringCOVID-China`); minor deduction for the Figure 4 legend contradiction (GISRS cases vs. BDSKY sequence inference) and `BEAST v.10.1.4` typo. |
| **Total Composite Score** | **7.4** | **10.0** | **Strong / Sound** (Scientific Core Score: **5.6 / 8.0**) |

---

### Constructive and Doable Suggestions for Improvement

1. **Estimate BDSKY $R_e(t)$ Jointly with Tree Topology and Relaxed Clock in BEAST2, and Correct the Figure 4 Legend:**  
   * **WHY:** Fixing a GMRF coalescent tree topology and switching to a fixed-rate strict clock in BEAST2 underestimates posterior uncertainty in node heights and $R_e$, and the Figure 4 legend erroneously attributes clade-specific $R_e$ curves to weekly GISRS case counts.  
   * **WHAT & HOW:** Run the BDSKY serial model directly on the concatenated alignments in BEAST 2.6.3 with an uncorrelated lognormal relaxed clock (jointly sampling topology and node heights), relax the `1 January 2020` hard lower bound on the 3a2 origin prior, and correct the Figure 4 legend to accurately describe the sequence-based BDSKY inference.
2. **Add Formal Statistical Testing and Surveillance Denominator Caveats to the Age-Distribution Analysis:**  
   * **WHY:** Comparing raw proportions of GISAID sequences by age before vs. during COVID-19 is confounded by age-specific changes in school attendance and fever-clinic testing.  
   * **WHAT & HOW:** Report formal contingency-table or multinomial regression $p$-values/CIs for the shift in age distribution across waves in Figure 6B, and explicitly test whether the dip in the early-2000s birth cohort (aged 15–20 in 2020–2021) is simply an age effect (lower testing/incidence in 10–20 year-olds across all subtypes, as noted on line 83) rather than a birth-cohort imprinting effect.
3. **Fix Editorial Typos:**  
   * **WHAT & HOW:** Correct `BEAST (v.10.1.4)` to `BEAST (v.1.10.4)` (line 33, two occurrences) and `a well as` to `as well as` (line 58).
