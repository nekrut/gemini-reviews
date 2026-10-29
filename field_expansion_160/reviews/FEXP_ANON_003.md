# Review of FEXP_ANON_003

**Overall Score:** **7.8 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.0 / 8.0**  
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 1.9/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.8/2.0

---

## 1. Blinded Metadata Perception
* **Anonymized Manuscript ID:** `FEXP_ANON_003`
* **Perceived Domain & Design:** Viral phylodynamics and molecular epidemiology; retrospective Bayesian coalescent skyline (BSP), birth-death skyline serial (BDSKY), and discrete-trait phylogeographic analysis of $n = 1,144$ HIV-1 CRF01_AE and $n = 192$ Subtype B partial *pol* (PR/RT) sequences collected in the Philippines between 2008 and 2020.
* **Blinding Integrity:** Double-blind review maintained; evaluated strictly on internal phylogenetic, phylodynamic, and statistical merits at $t_0$.

---

## 2. Executive Summary & Editorial Verdict

This study reconstructs the phylodynamic and phylogeographic history of HIV-1 CRF01_AE (and compares it against Subtype B) in the Philippines using archived drug resistance genotyping (DRG) partial *pol* sequences (HXB2 coordinates 2253–3233, with a 129-bp amplicon gap at 2538–2666 and drug-resistance codons stripped) from the Research Institute for Tropical Medicine (RITM). Maximum-likelihood reconstruction (IQ-TREE 2) identifies a dominant Philippine CRF01_AE clade containing 97% ($1,144/1,179$) of domestic sequences. Using BEAST 2 (uncorrelated lognormal relaxed clock, `bModelTest`, BSP, and BDSKY), the authors estimate a clade tMRCA of June 1996 ($95\%\text{ HPD}$: Dec 1991 – Oct 1999), exponential expansion of effective population size ($N_e$) until ~2014, and two peaks in the effective reproductive number ($R_e = 2.46$ in 2007 and $R_e = 2.52$ in 2015) separated by a dip to $R_e = 1.43$ ($95\%\text{ HPD } [1.06, 1.90]$) in 2011. Discrete-trait phylogeography (`BEAST` v1.10.4 with BSSVS) places the root in Luzon ($\text{PP} = 1.0$) with seeding into Visayas and Mindanao in 2001–2006. Crucially, the authors perform spatiotemporal uniform subsampling ($n = 256$ and $n = 151$) for BDSKY/BSP and 10 balanced island-group subsamples ($n = 34 \times 3 = 102$) for phylogeography, plus a parallel analysis of the major Philippine Subtype B clade ($n = 192$).

**Editorial Verdict: Minor Revision (Strong / Sound).** This is a well-executed, transparent, and methodologically conscientious phylodynamic study that adheres to best practices in data curation (stripping convergent drug-resistance codons, checking root-to-tip temporal signal, running multiple MCMC chains to 300M steps, and deposited GenBank accessions + GitHub BEAST XMLs) and sensitivity testing (spatiotemporal and balanced deme subsampling). The primary technical limitations that prevent an Exemplary score are: (1) an unmodeled 2-year diagnostic shutdown at RITM in 2012–2013 (due to reagent stockouts) that falls right inside the coarse 2-slice BDSKY sampling-proportion parameterization (2008–2013 and 2013–2018), creating a known phylodynamic artifact where a drop in sampling intensity in 2012–2013 can induce an apparent dip in $R_e$ in 2009–2011 followed by an artificial rebound in 2014–2015; (2) asymmetric temporal sampling windows between CRF01_AE (2008–2018) and Subtype B (routine RITM sampling restricted to Feb 2014 – Feb 2020, with only a few pre-2014 LANL sequences); and (3) a tree-prior mismatch in the BEAST 1.10.4 discrete phylogeographic analysis, where `bPopSizes` dimension was set to 3 instead of the standard 5 or 10 used in the main BSP analysis.

### Assessment of Specific Claims
* **Claim 1 (97% of Philippine CRF01_AE sequences form a single monophyletic clade introduced around June 1996 [95% HPD: Dec 1991 – Oct 1999]): [Well Supported].**  
  Supported by high ultrafast bootstrap/SH-aLRT support (97.5 / 99), positive root-to-tip temporal signal ($r = 0.37$, $R^2 = 0.137$), and concordance across the full $n=1,144$ dataset and uniform subsamples, as well as prior full-genome estimates.
* **Claim 2 (Luzon was the geographic origin [root PP = 1.0] and primary exporter of the CRF01_AE epidemic to Visayas and Mindanao): [Well Supported].**  
  Recognizing that raw sample counts are heavily skewed toward Luzon ($933$ vs. $34$ Visayas and $75$ Mindanao), the authors appropriately conducted Befi-BaTS tip-association tests and 10 balanced subsamples ($n = 34$ per island group). The Luzon root state and Luzon-to-Visayas/Mindanao export pattern remained consistent across the balanced subsamples, and the authors appropriately note that pairwise relative migration rate 95% HPDs overlap 1.0.
* **Claim 3 (CRF01_AE $R_e$ peaked in 2007 [2.46], dipped in 2011 [1.43], and rebounded in 2015 [2.52], potentially reflecting the 4th/5th Philippine AIDS Medium Term Plans): [Fragile].**  
  While the dip-and-rebound persists in the $n=256$ and $n=151$ subsamples, the authors disclose in the Discussion (line 113) that RITM performed *zero* drug resistance genotyping in 2012–2013 due to reagent stockouts, relying only on a small number of GenBank sequences during those two years. In BDSKY, the sampling proportion $s$ was held piecewise-constant across only two broad intervals (Jan 2008 – June 2013 and June 2013 – Nov 2018). When actual sampling drops sharply to near-zero in 2012–2013 within a piecewise-constant $s$ interval, BDSKY attributes the sudden deficit of sampled lineages and coalescent/branching events immediately prior to 2012–2013 to a decrease in the birth rate ($\lambda$, and hence $R_e$), followed by a sharp rebound in $R_e$ when routine RITM sequencing resumes in 2014.
* **Claim 4 (Subtype B exhibited a synchronous rise, dip, and rebound in $R_e$ comparable to CRF01_AE): [Fragile].**  
  The Subtype B $R_e$ 95% HPD intervals in Figure 4B span almost two orders of magnitude (e.g., $2.61$ [$95\%\text{ HPD } 0.050\text{–}5.03$] in 2009 and $0.75$ [$95\%\text{ HPD } 0.058\text{–}2.089$] in 2015), encompassing both rapid growth ($R_e = 5$) and near-extinction ($R_e = 0.05$). Moreover, RITM Subtype B samples were only collated from Feb 2014 to Feb 2020 (line 28), meaning pre-2014 Subtype B sampling was extremely sparse.

---

## 3. Forensic Defect Inventory

1. **Pillar 2 & 3 Violation — Unmodeled 2012–2013 Diagnostic Hiatus in Piecewise-Constant BDSKY Sampling Proportion (Methods line 50; Discussion line 113):**  
   The BDSKY serial model jointly estimates $R_e(t)$, the becoming-uninfectious rate $\delta$, and the sampling proportion $s(t)$. Because the authors specified only two active sampling intervals (`2008-01-15 to 2013-06-17` and `2013-06-17 to 2018-11-18`), the model assumes constant sampling effort from 2008 to mid-2013. However, RITM halted DRG sequencing entirely during 2012–2013 due to lack of reagents (line 113). Uniform subsampling ($n=256, 151$) cannot fully fix this if the 2012–2013 GenBank sequences are sparse or drawn from a narrow outbreak cluster. To verify that the 2011 dip in $R_e$ is not a sampling-rate misspecification artifact, $s(t)$ must include a dedicated changepoint interval for the 2012–2013 reagent hiatus (or skygrid/BDSKY with yearly sampling proportion intervals).
2. **Pillar 2 Violation — Asymmetric Sampling Timeframes Between CRF01_AE (2008–2018) and Subtype B (2014–2020) (Methods line 28):**  
   Line 28 states that RITM CRF01_AE sequences were collated from January 2008 to November 2018, whereas RITM Subtype B sequences were collated from February 2014 to February 2020 (with pre-2014 Subtype B tips coming only from sporadic LANL entries back to July 2008). Comparing $R_e$ trajectories in 2008–2014 between a densely sampled clade (CRF01_AE) and a clade with almost no domestic sampling before May 2014 explains why the Subtype B $R_e$ HPD spans $[0.05, 5.03]$ prior to 2014.
3. **Pillar 3 Violation — Clock Rate Prior vs. Posterior Shift and Single-Chain MCMC for Subtype B (Methods lines 48, 54; Results line 71):**  
   The normal clock-rate prior was centered at $M = 1.5 \times 10^{-3}$ ($\text{SD} = 4.9 \times 10^{-4}$) subst/site/year, whereas the CRF01_AE posterior median was $3.27 \times 10^{-3}$ ($95\%\text{ HPD } [2.93, 3.59] \times 10^{-3}$)—more than $3.6\text{ SD}$ above the prior mean. While the data clearly overwhelmed the prior in the large CRF01_AE dataset, in the smaller Subtype B dataset ($n=192$, run with only a *single* MCMC chain rather than multiple independent chains, line 54) the posterior clock rate is pulled downward toward the prior ($2.54 \times 10^{-3}$), which directly shifts the relative timing of historical $R_e$ peaks.
4. **Pillar 7 Violation — Minor Text/Formatting Omissions:**  
   * Line 48 has an incomplete citation placeholder: `following the prior set in ), and the best-fitting molecular clock model`.
   * Line 62 has an empty citation parenthesis: `over a map of the Philippines ()`.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.5** | **3.5** | Rigorous sequence curation (DRM stripping, recombinant filtering), model selection (stepping-stone/path-sampling), and subsampling sensitivity analyses; penalized for piecewise-constant BDSKY sampling slices across the 2012–2013 sequencing hiatus and single-chain MCMC for Subtype B. |
| **2. Claim-to-Evidence Alignment** | **1.9** | **2.5** | Origin, monophyly, and phylogeographic seeding claims are well-calibrated and appropriately caveated; claims of synchronous $R_e$ dips between CRF01_AE and Subtype B over-interpret HPDs spanning $[0.05, 5.03]$. |
| **3. Data Integrity & Biological/Behavioral Plausibility** | **1.6** | **2.0** | Careful handling of amplicon gaps and DRM convergence; however, the 2012–2013 RITM reagent stockout and 2014–2020 vs. 2008–2018 Subtype B collection window create temporal ascertainment skew. |
| **4. Reproducibility & Data Integrity** | **1.8** | **2.0** | Exemplary open science: all 1,404 sequences deposited in GenBank (`OQ428277–OQ428541`, `OQ710464–OQ711602`) and all BEAST XML files shared on GitHub (`[GITHUB_REPO_REDACTED]`). Minor deduction for two missing citation placeholders on lines 48 and 62. |
| **Total Composite Score** | **7.8** | **10.0** | **Strong / Sound** (Scientific Core Score: **6.0 / 8.0**) |

---

### Constructive and Doable Suggestions for Improvement

1. **Add a Dedicated 2012–2013 Sampling-Proportion Interval in BDSKY:**  
   * **WHY:** Assuming a constant sampling proportion from Jan 2008 to June 2013 when RITM stopped genotyping in 2012–2013 forces the birth-death prior to depress $R_e$ prior to the gap and spike $R_e$ when sampling resumes in 2014.  
   * **WHAT & HOW:** Modify the `TreeSlicer` configuration in the GitHub BEAST2 XML to partition $s(t)$ into four intervals (`Origin–2008`, `2008–2011`, `2012–2013` with a tighter lower-mean Beta prior reflecting the RITM stockout, and `2014–2018`) and check whether the 2011 $R_e$ dip persists.
2. **Verify Clock-Rate Prior Sensitivity and Multi-Chain Convergence for Subtype B:**  
   * **WHY:** The CRF01_AE posterior evolutionary rate ($3.27 \times 10^{-3}$) lies $>3.6\text{ SD}$ above the normal prior mean ($1.5 \times 10^{-3}$), whereas the smaller Subtype B dataset ($n=192$, 1 chain) is pulled toward the prior ($2.54 \times 10^{-3}$), which can create the apparent 2–4 year lag between Subtype B and CRF01_AE trajectories.  
   * **WHAT & HOW:** Run 3–4 independent MCMC chains for Subtype B using a broader lognormal or uniform clock rate prior spanning $[1.0 \times 10^{-3}, 5.0 \times 10^{-3}]$ subst/site/year.
3. **Fix Missing Citation Placeholders:**  
   * **WHAT & HOW:** Fill in the missing references at line 48 (`following the prior set in [REF])`) and line 62 (`over a map of the Philippines ([REF])`).
