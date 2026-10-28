# Review of ANON_92

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **6.4 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 2.0/3.5 | Claims: 1.5/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study investigates the spatial and temporal spread of SARS-CoV-2 across Minnesota between March 2020 and March 2022 by generating 21,669 viral consensus genomes from Mayo Clinic Laboratories and combining them with 55,206 Minnesota Department of Health (MDH) sequences and global reference genomes. From this pool, the authors subsample $n = 6,188$ genomes across 10 discrete geographic categories (`international`, `USA`, the five highest-case Minnesota counties individually—Hennepin, Ramsey, Dakota, Anoka, and Washington—and 15 remaining counties grouped into Northern, Central, and Southern Minnesota). Using `BEAST v1.10.5` (`ThorneyTreeLikelihood`, strict molecular clock, and `SkyGrid` coalescent prior) followed by asymmetric discrete-trait ancestral state reconstruction and Markov jump counting on 1,000 posterior trees, the authors estimate that the earliest viral introduction reached Hennepin County around 22 January 2020, that Hennepin County accounted for 45/107 international introductions and 772 in-state exportations, and that monthly within-county spatial diversity (`NormShannon`) showed low-to-intermediate mixing ($0.25\text{--}0.50$) unaffected by statewide policy changes. Sequences, BEAST XMLs, and posterior trees are deposited in GISAID, GenBank, and Figshare.

The dataset is a substantial regional surveillance resource, and the application of `ThorneyTreeLikelihood` with empirical tree distributions is computationally practical for 6,188 genomes. However, several methodological and reporting flaws weaken the specific quantitative conclusions. First, the Abstract contradicts the Importance, Results, and Discussion regarding whether the earliest 22 January 2020 introduction into Hennepin County originated from a "domestic source" (Abstract) or an "international source" (Importance, Results, Figure 4, and Discussion). Second, discrete-trait phylogeography (`Lemey et al.`) is highly sensitive to uneven deme sample sizes; allocating proportional-to-case counts to Hennepin County while collapsing 15 other counties into three multi-county regions and all other US states into a single `USA` state inherently biases ancestral root/trunk reconstruction and Markov jumps toward Hennepin County without downsampling sensitivity controls. Third, the Data Availability Statement notes that sample collection dates were randomly shifted by $\pm 31$ days for privacy protection, which—if present in the deposited XMLs or tip dates—severely compromises sub-monthly phylodynamic timing claims. Finally, claims that statewide policy changes and case counts had no effect on viral diversity rely entirely on visual inspection of `NormShannon` curves rather than formal time-series testing.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Hennepin County was the dominant source of in-state SARS-CoV-2 transmission ($n = 772$ Markov jumps) while other Minnesota counties acted primarily as transmission sinks: [Moderately Supported].**  
  While it is epidemiologically plausible that Minnesota's largest metropolitan center and airport hub (Minneapolis/St. Paul) drove statewide viral dispersal, discrete-trait continuous-time Markov chain (CTMC) models are well known to infer the most heavily sampled deme as the ancestral trunk state. Because the authors sampled at 5 sequences per 1,000 county cases (giving Hennepin County the largest single-county sample size) and did not perform uniform-per-deme downsampling or generalized linear model (GLM) phylogeography adjusting for sample size, the exact magnitude of the source/sink asymmetry (Figure 3) is partially confounded by sampling intensity.

* **The earliest introduction of SARS-CoV-2 into Minnesota occurred in Hennepin County around 22 January 2020, six weeks before the first confirmed case: [Fragile].**  
  First, the manuscript contradicts itself on the geographic origin of this event: the Abstract (line 8) states it was *"to Hennepin County from a domestic source around 22 January 2020"*, whereas the Importance (line 13), Results (line 92), Figure 4 caption (line 98), and Discussion (line 105) state it was from an *"international source"*. Second, timing was point-estimated as *"the middle of the branch between the current node and its parent for any change in location state"* (line 48) on the maximum clade credibility (MCC) tree without reporting the 95% highest posterior density (HPD) interval for the transition time or parent/child node ages. Early 2020 basal SARS-CoV-2 branches carry near-zero substitutions, yielding wide temporal credible intervals under a strict clock.

* **Neither clinical case counts nor major statewide policy changes (the end of lockdown on 18 May 2020 and the end of all restrictions on 28 May 2021) impacted county-level viral spatial diversity: [Overstated].**  
  As the authors acknowledge in the Results (line 87: *"Anecdotally (looking at the trends of each graph), the changes in case counts over time do not appear to have a relationship with county-specific diversity"*), no statistical hypothesis test, correlation analysis, or interrupted time-series regression was performed. Furthermore, the subsampling scheme used `augur filter` *"to distribute (as equally as possible) our heterochronous sequences by month"* (line 39), which artificially flattens temporal variation in lineage sampling across epidemic waves and policy transitions.

* **Deposited genomic metadata and BEAST files allow full reproducibility of the phylodynamic timing and introduction estimates: [Fragile].**  
  In the Data Availability section (line 130), the authors state: *"We randomly shifted the collection day by ±31 days for privacy protection."* A random uniform shift of up to $\pm 1$ month across tip dates destroys the fine-scale temporal calibration required to infer Markov jump timing, monthly sink/source ratios (Figure 3), and the 22 January 2020 introduction date. It is unclear whether the BEAST analyses were run on exact dates and only the public GenBank/GISAID metadata were jittered, or whether the deposited Figshare BEAST XMLs also contain jittered dates.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile the Contradiction on the Origin of the Earliest Introduction and Report 95% HPD Intervals
* **WHY:** Stating that the 22 January 2020 introduction came from a "domestic source" in the Abstract and an "international source" in the rest of the paper confuses a headline conclusion, and taking the midpoint of a branch on an MCC tree omits Bayesian temporal uncertainty.
* **WHAT:** Correct the Abstract or main text so the source location matches the posterior tree inference, and report the 95% HPD interval for the earliest transition date.
* **HOW:** Using the `TreeMarkovJumpHistoryAnalyzer` output across the 1,000 posterior trees (already deposited on Figshare), extract the posterior distribution of the earliest Markov jump into Hennepin County, report its posterior median date and 95% HPD interval (in addition to the parent and child node age 95% HPDs on the MCC tree), and ensure the Abstract and Results report the same source state (`USA` vs. `international`).

#### 2. Perform a Balanced-Subsampling Sensitivity Analysis for Discrete-Trait Phylogeography
* **WHY:** In ancestral state reconstruction, demes with more tips disproportionately occupy internal backbone nodes, inflating inferred exports from Hennepin County relative to less-sampled counties.
* **WHAT:** Run a sensitivity analysis on the empirical posterior trees using equal sequence counts per discrete location (deme) to verify that Hennepin County remains a net source.
* **HOW:** Downsample the 1,000 empirical trees (using `ape::keep.tip` or `Baltic`) to a uniform number of tips per Minnesota location per quarter (matched to the smallest included county/region), re-estimate the 10-state CTMC transition matrix and Markov jumps in BEAST, and compare the resulting source/sink ratios (Figure 3) against the full 6,188-tip analysis.

#### 3. Replace Anecdotal Visual Inspection with Formal Time-Series Testing of Policy and Case-Count Effects
* **WHY:** Concluding in the Abstract that policy changes and case counts had no impact on viral diversity based solely on visual inspection of Figure S5 is unsupported, especially when `augur filter` was used to equalize monthly sample counts.
* **WHAT:** Quantify the association between monthly `NormShannon` diversity, log-transformed county case counts, and policy epochs using mixed-effects regression, and temper the causal phrasing in the Abstract.
* **HOW:** Fit a linear mixed-effects model (`NormShannon ~ log10(monthly_cases) + policy_epoch + (1|location)`) accounting for first-order autocorrelation (`nlme::lme` with `corAR1()`), report the regression coefficients, 95% CIs, and $p$-values in the Results, and rephrase the Abstract to state that no statistically significant shift in county lineage-location diversity was detected following policy transitions.

#### 4. Clarify how the $\pm 31$-Day Tip-Date Shift Affects the Analysis vs. Deposited Files
* **WHY:** Shifting collection dates by $\pm 31$ days alters substitution rate estimates and ancestral node dates by weeks; readers attempting to reproduce the analysis from GenBank/GISAID or Figshare need to know which files have exact vs. jittered dates.
* **WHAT:** Explicitly state in the Materials and Methods and Data Availability sections whether the BEAST analyses and Figshare XMLs used exact collection dates or $\pm 31$-day shifted dates.
* **HOW:** Add a sentence in Materials and Methods ("Phylogenetic analysis of SARS-CoV-2") clarifying that exact collection dates were used for all `TempEst`, `augur`, and `BEAST` analyses, and specify whether the BEAST XMLs deposited at `10.6084/m9.figshare.22679449` retain exact decimal dates or rounded/jittered dates.

#### 5. Technical and Mathematical Cleanup
* **WHY:** Typographical errors in mathematical expressions and inconsistent sequence counts across sections reduce clarity.
* **WHAT & HOW:**
  1. **Asymmetric rate matrix formula (line 48):** Correct `"an asymmetric transmission rate matrix of K ( K *1)"` to `"an asymmetric transmission rate matrix with K(K - 1) off-diagonal rates, where K = 10 is the number of discrete locations"`.
  2. **Sequence total reconciliation (Abstract line 8, Fig 1 caption line 59, Supplemental Fig S3 caption line 148):** Reconcile `"over 22,000 patient samples"` (Abstract), `"N = 21,669 with a known sampling location in a Minnesota county"` (Fig 1A), and `"24,070 full genome SARS-CoV-2 sequences generated for this study"` (Fig S3 caption) by stating the total number of passing genomes sequenced (24,070) and the subset mapping to Minnesota counties (21,669, or ~90%, noting how this relates to the 96% Minnesota residency stated on line 61).
