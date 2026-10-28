# Review of PMC7375454 (PMID:32699345)

**Manuscript Title:** SARS-CoV-2 genomic variations associated with mortality rate of COVID-19  
**Authors:** Toyoshima Y, Nemoto K, Matsumoto S, Nakamura Y, Kiyotani K.  
**Journal / Preprint:** *J Hum Genet* (2020; `PMC7375454` / `PMID:32699345` / `10.1038/s10038-020-0808-9`)  
**Calibration Study Cohort:** Cohort A — Known Invalid / Refuted (`A13` | Double-Blinded as `ANON_02`)  
**Overall Score:** **3.4 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.8/2.5 | Biology: 0.7/2.0 | Reproducibility: 1.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript analyzes 12,343 SARS-CoV-2 genome sequences deposited in GISAID through 7 May 2020 across 28 countries (each with $>30$ sequences) and 17 U.S. states to test whether viral amino acid mutations, national BCG vaccination policies, and population-level HLA allele frequencies correlate with country-level COVID-19 case fatality rates (CFR) and confirmed cases per million. Using hierarchical clustering on 16 common mutations and bivariate Pearson correlations, the authors group the 28 countries into three clusters and report that ORF1ab P4715L and Spike D614G frequencies correlate positively with country-level CFR ($r = 0.41, P = 0.029$ and $r = 0.43, P = 0.022$), while routine BCG vaccination ($P = 0.031$) and East Asian-enriched HLA alleles (HLA-A\*11:01, HLA-A\*02:06, HLA-B\*54:01) correlate negatively with CFR. Public databases (GISAID, Worldometer, AFND) are cited, though custom analysis scripts and GISAID acknowledgment tables are not provided.

While the descriptive characterization of linkage disequilibrium between ORF1ab P4715L, Spike D614G, and N R203K/G204R across early pandemic clades is accurate, the epidemiological and immunological conclusions rest on severe ecological fallacy and unadjusted spatial/temporal confounding. By May 2020, the B.1 lineage (carrying D614G + P4715L) dominated Europe and eastern North America—regions that simultaneously experienced overwhelming early hospital surges, lower testing denominators (inflating crude CFR), older population age structures, and absence of universal BCG policies—whereas ancestral Wuhan-like lineages predominated in East Asia, where aggressive testing, younger contact-traced cohorts, Universal BCG vaccination, and high frequencies of HLA-A\*11:01 / B\*54:01 co-occurred. Indeed, the authors' own multiple regression shows that the HLA associations with CFR vanish once adjusted for D614G frequency ($P = 0.13$ to $0.73$). Because crude country-level CFR is heavily distorted by testing rates and age demographics, and no multivariable model controls for these confounders or for multiple hypothesis testing, the manuscript's biological claims regarding immune escape from BCG and HLA protection are unsupported. Addressing these issues requires multivariable regression controlling for testing per capita, median age, and epidemic timing, alongside patient-level or age-standardized mortality outcomes.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **ORF1ab P4715L and Spike D614G are in near-complete linkage disequilibrium ($r^2 = 0.98, D' = 1.00$), with N R203K/G204R forming a nested sub-haplotype ($D' = 0.99$): [Well Supported].**  
  The haplotype analysis across 12,343 genomes accurately captures the clonal phylogenetic structure of the B.1 (D614G + P4715L) and B.1.1 (+ N R203K/G204R) lineages during the spring 2020 pandemic wave (Results line 45, Supplementary Fig. 3).

* **Country- and state-level frequencies of ORF1ab 4715L and Spike 614G positively correlate with COVID-19 case fatality rates ($r = 0.41–0.49$): [Fragile].**  
  The bivariate correlations ($P = 0.022–0.047$ across 28 countries and 17 U.S. states; Figs. 2 and 3) do not survive basic epidemiological or statistical scrutiny:
  1. *Crude CFR ascertainment bias (Pillar 2):* Defining fatality rate as crude confirmed deaths divided by confirmed cases on Worldometer (Methods line 35) conflates viral virulence with national testing capacity. In May 2020, Western European countries restricted RT-PCR testing largely to hospitalized patients (yielding crude CFRs of 10–15%), whereas East Asian countries and Western U.S. states tested broadly.
  2. *Time-lag and spatial confounding (Pillar 2 & 3):* The authors downloaded U.S. case/death counts on 3 July 2020 but used viral sequences deposited up to 7 May 2020 (Methods lines 25, 35), creating a two-month mismatch between viral genotype sampling and clinical outcome measurement. Furthermore, combining 17 U.S. states with 27 countries in a single Pearson correlation (Results line 49, Supplementary Fig. 5) violates observation independence by treating sub-national units on par with sovereign countries.
  3. *Lack of multiple-testing correction (Pillar 4):* Testing 16 common mutations (or 131 mutations $>10\%$ frequency) against CFR without false discovery rate (FDR) or Bonferroni adjustment renders nominal $P \approx 0.022–0.047$ statistically indistinguishable from chance.

* **BCG vaccination protects against SARS-CoV-2 infection, while 4715L / 614G variants escape BCG-potentiated innate immunity: [Overstated].**  
  In Results (line 51), the authors observe a non-significant correlation between 614G and CFR in 11 BCG-vaccinated countries ($r = 0.54, P = 0.090$) and no correlation in 17 non-BCG countries ($r = 0.19, P = 0.47$), and conclude that "BCG-vaccination may protect from SARS-CoV-2 infection by potentiation of innate immune response; however, ORF1ab 4715L-type and S protein 614G-type SARS-CoV-2 variants may escape from the immune response." Inferring viral escape from trained innate immunity based on a non-significant ecological correlation ($P = 0.090$, $N = 11$) is both statistically invalid (Pillar 4) and biologically implausible (Pillar 6), as BCG-induced non-specific innate training does not exert sequence-specific selective pressure on Spike residue 614 or Nsp12 residue 4715.

* **Population frequencies of HLA-A\*11:01, HLA-A\*02:06, and HLA-B\*54:01 explain country-level susceptibility and mortality differences: [Methodologically Flawed].**  
  1. *Population stratification / East Asian confounding (Pillar 2 & 3):* HLA-A\*11:01, HLA-A\*02:06, and HLA-B\*54:01 are classic East Asian-enriched alleles. Because East Asian countries had both low early COVID-19 mortality and low D614G frequency in May 2020, any East Asian genetic marker will correlate negatively with crude CFR in an unadjusted ecological regression. The authors themselves show that adjusting for S 614G frequency in multiple regression abolishes the HLA-CFR association ($P = 0.13, 0.73$, and $0.45$; Results line 53).
  2. *Internal contradiction in epitope binding predictions (Pillar 3 & 6):* In Results (line 53), the authors state that wild-type and mutated epitopes bind HLA molecules "at similar affinities." In Discussion (line 62), however, they report that the mutated 4715L peptides have *stronger* predicted binding affinities (11, 12, and 23 nM) than the wild-type P4715 peptides (44, 41, and 45 nM) to HLA-B\*07:02, HLA-B\*54:01, and HLA-A\*11:01. If the 4715L mutation *improves* MHC Class I presentation (lower $\text{IC}_{50}$), it would enhance rather than evade CD8+ T-cell recognition, contradicting the narrative that 4715L increases fatality.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Fit Multivariable Regression Models Controlling for Demographic, Testing, and Temporal Confounders
* **WHY:** Unadjusted bivariate Pearson correlations ($N = 15$ to $28$ countries) between viral clade frequencies, BCG status, HLA frequencies, and crude CFR are severely confounded by testing capacity, population age structure, and epidemic arrival time.
* **WHAT:** Replace unadjusted bivariate inferences with a multivariable regression framework that includes key country-level epidemiological covariates.
* **HOW:** Extract tests per million population, percentage of population aged $\ge 65$ years, and days since the 100th confirmed case (as of 7 May 2020) from Worldometer / UN demographic tables. In R, fit a generalized linear model (e.g., quasi-binomial or beta regression for CFR, and negative binomial regression for cases per million):
  $$\text{CFR}_i \sim \beta_0 + \beta_1 \text{Freq(614G)}_i + \beta_2 \text{BCG}_i + \beta_3 \text{HLA}_i + \beta_4 \text{Age65}_i + \beta_5 \log(\text{TestsPerMillion}_i) + \beta_6 \text{DaysSinceOnset}_i$$
  Report the partial regression coefficients, variance inflation factors (VIF), and adjusted $P$-values.

#### 2. Apply Multiple Hypothesis Testing Corrections and Non-Parametric Rank Tests
* **WHY:** Country-level CFR and case counts per million are right-skewed (violating the normality assumptions of Student's $t$-test and Pearson's $r$), and screening 16 mutations across multiple geographic partitions and HLA alleles inflates Type I error.
* **WHAT:** Re-evaluate all pairwise comparisons and correlations using non-parametric statistics and Benjamini-Hochberg FDR correction.
* **HOW:** In R (`stats`), compute Spearman's rank correlation ($\rho$) and Wilcoxon rank-sum tests alongside Pearson's $r$ and $t$-tests, and apply `p.adjust(p_values, method = "BH")` across all 16 tested mutations and all tested HLA alleles. Remove Supplementary Fig. 5's pooled regression of 17 U.S. states + 27 countries, as states are nested within the U.S. and violate independence.

#### 3. Synchronize the Temporal Window for U.S. State Sequence and Mortality Data
* **WHY:** Comparing viral mutation frequencies from GISAID as of 7 May 2020 against U.S. state mortality data from 3 July 2020 (Methods lines 25 and 35) introduces a 57-day mismatch during which D614G swept to near-fixation across all U.S. states.
* **WHAT:** Align the U.S. state epidemiological cutoff date with the GISAID sequence cutoff date (7 May 2020, or allowing a fixed 14-day lag to 21 May 2020 for case-to-death progression).
* **HOW:** Retrieve historical U.S. state case and death counts for 7 May 2020 (and 21 May 2020) and recompute Figure 3a–c.

#### 4. Correct the Ecological Overreach and Epitope Contradiction in the Abstract and Discussion
* **WHY:** The data do not support the claim that D614G/4715L escapes BCG-mediated innate immunity ($P = 0.090$), nor that HLA alleles independently affect national CFR (since $P > 0.13$ after adjusting for viral clade). Moreover, the Discussion contradicts the Results on whether 4715L alters HLA binding affinity.
* **WHAT:** Reframe the manuscript as an exploratory ecological description of co-varying viral clades and host population characteristics, and reconcile the epitope binding text.
* **HOW:** 
  1. Delete the claim in Results (line 51) that "ORF1ab 4715L-type and S protein 614G-type SARS-CoV-2 variants may escape from the [BCG] immune response."
  2. Explicitly state in the Abstract and Discussion that the negative correlation between East Asian HLA alleles (HLA-A\*11:01, A\*02:06, B\*54:01) and crude CFR is confounded by the geographic distribution of viral clades (East Asia vs. Europe/North America) and is not statistically significant in multivariable analysis.
  3. Reconcile Results line 53 ("bind to HLA molecules at similar affinities") with Discussion line 62 ("mutated peptides show higher binding affinities of 11, 12, and 23 nM" vs. 44, 41, and 45 nM) by clarifying that a 2- to 4-fold change in predicted $\text{IC}_{50}$ within the $<50\text{ nM}$ strong-binder regime does not constitute immune escape.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Several haplotype notations and structural descriptions in the text are inaccurate.
* **WHAT & HOW:**
  * **Haplotype typo in Results (line 47):** The text states "we also examined the correlations of this variant or S 614G-N 203R/204G haplotype with fatality rates" (citing Supplementary Fig. 4A, B), whereas line 45 defines the cluster 2 mutant haplotype as "S protein 614G-N protein 203K/204R" (since 203R/204G is the Wuhan-Hu-1 wild-type). Clarify whether Supplementary Fig. 4B tests the mutant 203K/204R or wild-type 203R/204G background.
  * **Structural description of D614G (Discussion line 60):** The statement "S protein having a D614G substitution is located on the surface of the virus and interacts with ACE2" is imprecise: while the S glycoprotein interacts with ACE2 via its receptor-binding domain (RBD, residues 319–541), residue 614 is located at the C-terminal region of S1 near the S1/S2 protomer interface, outside the direct ACE2 contact footprint. Revise to state that D614G alters S1/S2 inter-protomer interactions and RBD up/down conformational dynamics.
