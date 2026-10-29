# Review of FEXP_ANON_017

**Overall Score:** **5.8 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **4.5 / 8.0**  
* **Score Breakdown:** Rigor: 1.8/3.5 | Claims: 1.3/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.3/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_017`
* **Perceived Research Domain:** Viral genomic epidemiology and phylodynamics of SARS-CoV-2 (first epidemic wave in Italy, January–July 2020).
* **Study Design:** Observational genomic surveillance combining 191 newly sequenced SARS-CoV-2 genomes (primarily from Abruzzo and Lombardy) with 460 publicly available Italian GISAID sequences ($N = 651$ total Italian genomes) and 1,722 global reference sequences ($N = 2,373$ total alignment).
* **Primary Methods:** Multiple sequence alignment (MAFFT L-INS-i), Pango lineage assignment (Pangolin v2.0.7), maximum likelihood phylogenetics (IQ-TREE v1.6.12, HKY+$\Gamma$), molecular clock dating via Least-Squares Dating (LSD, fixed clock rate $8 \times 10^{-4}$ substitutions/site/year), and stated Bayesian coalescent validation on a subset (BEAST v1.10).

---

## 2. Executive Summary & Editorial Verdict

This manuscript presents a genomic epidemiological survey of the first wave of SARS-CoV-2 in Italy (29 January to 20 July 2020), contributing 191 newly generated viral genomes—primarily from the central region of Abruzzo ($n = 102$) and northern region of Lombardy—and integrating them with 460 existing Italian genomes from GISAID alongside 1,722 global sequences. Using maximum likelihood phylogenetics (IQ-TREE) and least-squares molecular clock dating (LSD), the authors classify circulating Pango lineages (predominantly B.1 at 50% and B.1.1 at 40%), identify 124 putative Italian transmission clusters alongside 239 singleton sequences, and estimate cluster times to the most recent common ancestor (tMRCAs) across pre-lockdown, partial-lockdown (22 February–7 March), nationwide-lockdown (8 March–3 June), and post-lockdown periods. Sequences are deposited in GISAID with accession metadata referenced in supplementary tables.

While the 191 newly sequenced genomes provide useful empirical coverage for an undersampled central Italian region during the early pandemic, several methodological and inferential flaws undermine the headline quantitative conclusions regarding importation counts, inter-regional transmission, and lockdown-induced lineage extinction. First, the global background dataset was constructed via BLASTn top-50 matching followed by removing all identical global sequences while retaining identical Italian sequences; this asymmetric deduplication artificially collapses non-Italian clades and inflates the apparent monophyly and singleton count of Italian sequences. Second, defining "transmission clusters" and "cross-region transmission" on a largely polytomous SARS-CoV-2 tree without formal phylogeographic ancestral state reconstruction and using a permissive branch support threshold ($\text{UFBoot} > 70\%$) leads to uncalibrated cluster boundaries; notably, only 54 of 124 clusters (and only 1 of 18 multi-region clusters) had enough support to estimate a tMRCA. Third, the claim that the nationwide lockdown caused a "marked genetic bottleneck and lineage extinction" rests on comparing 11 lineages observed in $n = 442$ lockdown sequences against 3 lineages observed in only $n = 12$ post-lockdown sequences without rarefaction or subsampling controls. These issues can be resolved through computational re-analysis (symmetric subsampling, rarefaction controls, and explicit reporting of the BEAST validation) and substantial tempering of causal claims.

### Specific Assessment of Core Claims

* **Dominance of Pango lineages B.1 (50%) and B.1.1 (40%) among sampled Italian sequences during the first wave:** **[Well Supported].**  
  Lineage assignment via Pangolin v2.0.7 and the canonical marker mutations (C3037T, C14408T, A23403G/D614G for B.1; G28881A/G28882A/G28883C KR motif in N for B.1.1) are consistent with established European genomic surveillance data from spring 2020, though regional proportions remain subject to sampling skew toward Lombardy (62%) and Abruzzo (16%).

* **Identification of at least 124 independent Italian transmission clusters and 239 singletons representing independent introductions:** **[Methodologically Flawed].**  
  In Section 2.5 (line 46), the authors state that *"Identical global sequences were also excluded"* after extracting the top 50 BLASTn hits per Italian sequence, whereas identical Italian sequences were kept (e.g., clusters 52 and 71 containing 34 and 37 mostly identical sequences). Asymmetric removal of identical global sequences eliminates foreign sister taxa on zero-length branches, forcing basal polytomies to resolve as ostensibly "Italian-only" clusters or singletons. Furthermore, 70 of the 124 clusters lacked even modest branch support ($\text{SH-aLRT} > 0.9$ or $\text{UFBoot} > 70\%$), meaning cluster counts reflect arbitrary topological tie-breaking across zero-length branches (`-blmin 1e-10`).

* **Ongoing local transmission during lockdown and 18 instances of inter-regional transmission between North, Central, and South Italy:** **[Fragile].**  
  Persistence of identical or near-identical sequences within North Italy across 29–35 days (clusters 52 and 71) supports local transmission during lockdown. However, the claim of 18 inter-regional transmission clusters is fragile: the authors acknowledge in the Discussion (line 103) that out of the multi-region clusters, *"only one had sufficient support to accurately estimate the tMRCA"*, and no formal discrete-trait phylogeographic model or travel-history conditioning was performed to distinguish direct inter-regional transmission from parallel importations of identical European B.1/B.1.1 basal haplotypes.

* **Overly narrow LSD tMRCA confidence intervals (e.g., B.1 tMRCA 15–30 January 2020; B.1.1 17–24 February 2020) validated by BEAST 1.10:** **[Overstated].**  
  The authors rightly note (Section 3.2, line 75) that the narrow LSD intervals are an artifact of numerous zero-length branches. However, despite claiming in Section 2.5 (line 48) that *"we validated our estimates of node ages by analysing a subset of the data in BEAST 1.10"*, the manuscript never reports a single BEAST posterior tMRCA estimate, 95% HPD interval, or subset sample size in the Results or tables.

* **Nationwide lockdown caused a marked genetic bottleneck and lineage extinction (reducing diversity from 11 lineages during lockdown to 3 lineages post-lockdown):** **[Methodologically Flawed].**  
  Only $n = 12$ sequences were sampled in the post-lockdown period (8 of which came from Abruzzo), compared to $n = 442$ during the nationwide lockdown and $n = 184$ during the partial lockdown (Section 3.2). Observing 3 lineages in 12 draws versus 11 lineages in 442 draws (where 8 of the 11 lockdown lineages were present at $\le 1\%$–$4\%$ frequency, including singletons B.1.35 and B.1.5.5) is an expected statistical consequence of severe sample-size reduction ($n = 12$), not evidence of biological lineage extinction.

---

## 3. Forensic Defect Inventory

### Defect 1: Asymmetric Deduplication of Global vs. Italian Sequences (Pillar 2 & Pillar 3)
* **Location:** Section 2.4 (lines 41) & Section 2.5 (line 46).
* **Diagnostic Finding:** The global background was assembled via BLASTn (top 50 hits per Italian genome + 500 random sequences), after which *"Identical global sequences were also excluded"* while identical Italian sequences were retained. In early-wave SARS-CoV-2 (mean pairwise similarity 99.4% globally and 99.6% within Italy; Section 3.4), widespread basal haplotypes in lineages B.1 and B.1.1 were shared across hundreds of European patients. Deleting duplicate non-Italian genomes strips foreign tips from shared internal nodes and polytomies, directly biasing topological clustering toward grouping Italian sequences together or isolating singletons.
* **Remediation:** Retain representative global duplicates proportional to country/temporal sampling (or perform formal ancestral state reconstruction / BaTS / structured coalescent analysis on time-stratified subsamples) rather than asymmetrically deduplicating only non-Italian sequences.

### Defect 2: Uncalibrated Polytomy Resolution and Missing BEAST Validation Results (Pillar 3 & Pillar 4)
* **Location:** Section 2.5 (line 48), Section 3.2 (line 75), Section 3.3 (line 87).
* **Diagnostic Finding:** 
  1. IQ-TREE was run with `-blmin 1e-10` and ultrafast bootstrap (`UFBoot`), using a support cutoff of $\text{UFBoot} > 70\%$ or $\text{SH-aLRT} > 0.9$ (misspelled as `SH-aLTR`). Because IQ-TREE's UFBoot is only calibrated as an unbiased clade probability at $\ge 95\%$, a $70\%$ UFBoot threshold admits poorly resolved clades. Even under this lenient threshold, 70 of the 124 putative transmission clusters failed to achieve support.
  2. Methods Section 2.5 describes a BEAST 1.10 analysis on a subset of sequences to validate LSD node ages, but zero BEAST results are presented in Section 3.
* **Remediation:** Collapse branches with $\text{UFBoot} < 95\%$ into polytomies prior to cluster enumeration, or report cluster counts across sensitivity thresholds ($\text{UFBoot} \ge 70\%, 90\%, 95\%$). Explicitly report the BEAST 1.10 posterior median tMRCAs and 95% HPD intervals alongside the LSD parametric bootstrap intervals in the main text and Table S3.

### Defect 3: Sample-Size Confounding in Post-Lockdown Lineage Extinction Claim (Pillar 1, Pillar 4 & Pillar 5)
* **Location:** Section 3.2 (lines 68, 75) & Section 4 Discussion (line 101).
* **Diagnostic Finding:** The claim that lockdown caused a genetic bottleneck and lineage extinction is based on observing 11 lineages in $n = 442$ nationwide-lockdown sequences versus 3 lineages in $n = 12$ post-lockdown sequences (and 8 of those 12 are from a single region, Abruzzo). Under a simple hypergeometric/multinomial null model where the lockdown lineage frequency distribution (50% B.1, 40% B.1.1, 4% B.1.5, and 8 rare lineages totaling 6%) remains completely unchanged after lockdown, a random sample of size $n = 12$ yields an expected richness of $\approx 2.6$ lineages ($95\%$ interval: $2\text{–}4$ lineages). Thus, observing 3 lineages in $n = 12$ sequences is completely indistinguishable from the null hypothesis of zero change in lineage diversity.
* **Remediation:** Perform a Monte Carlo rarefaction analysis (e.g., 10,000 random draws of $n = 12$ sequences from the $n = 442$ lockdown pool, stratified by region) to test whether post-lockdown lineage richness is significantly lower than expected by sample size alone, and remove the unsupported claim of lockdown-induced lineage extinction if the null cannot be rejected.

### Defect 4: Numerical and Typographical Errors in Methods and Text (Pillar 7)
* **Location:** Abstract (line 5), Section 2.2 (line 29), Section 2.5 (lines 46, 48), Section 3.1 (line 61).
* **Diagnostic Finding:**
  1. **Sequence count inconsistency:** The Abstract (line 5), Section 2.2 (line 29), and Section 3.1 (line 61) state that **191** new genomes were sequenced in this study, which when added to **460** published GISAID genomes equals **651** Italian sequences. However, Section 2.5 (line 46) states: *"651 sequences from Italy, of which 192 were created in this study here"*.
  2. **MCMC chain length typo:** Section 2.5 (line 48) states: *"We ran a Markov chain Monte Carlo of $5 \times 10^{-8}$ steps sampling every 5000 steps"*, which is a mathematical impossibility (a negative exponent instead of $5 \times 10^{7}$ or $5 \times 10^{8}$).
  3. **Evolutionary rate units and typographical errors:** Line 48 reports the clock rate as *"8 × 10 −4 subs/site"* (missing *"per year"*), misspells *"Whuhan-Hu-1"* (line 46) and *"SH-aLTR"* (line 48), and writes *"the mean rate of to the same value"* (line 48).
* **Remediation:** Reconcile the 191 vs. 192 newly sequenced genome count across Section 2.5 and the rest of the manuscript, correct the BEAST MCMC length exponent to $5 \times 10^{7}$ or $5 \times 10^{8}$, and fix the unit and spelling errors.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.8** | **3.5** | Asymmetric removal of identical global sequences distorts cluster/singleton inference; 70/124 clusters lack branch support; BEAST validation is described in Methods but omitted from Results; no rarefaction control for $n=12$ post-lockdown sample size. |
| **2. Claim-to-Evidence Alignment** | **1.3** | **2.5** | Core claims regarding "at least 124 independent introductions," inter-regional transmission (17/18 clusters unsupported for tMRCA), and lockdown-induced "genetic bottleneck and lineage extinction" overreach the resolution of the polytomous tree and sparse sampling. |
| **3. Data Integrity & Biological Plausibility** | **1.4** | **2.0** | Sequenced genomes (191) and Pango lineage assignments are biologically sound, and masking of artifactual positions 6867–6868 is appropriate, though severe geographic/temporal ascertainment skew (62% Lombardy, 16% Abruzzo, $n=12$ pre/post lockdown) is not controlled in downstream inference. |
| **4. Reproducibility & Data Integrity** | **1.3** | **2.0** | Sequences and GISAID accession tables (Tables S1, S4) are provided alongside standard versioned tools (MAFFT, IQ-TREE, Pangolin, BEAST), but undermined by the 191 vs. 192 sequence count discrepancy, the $5 \times 10^{-8}$ MCMC step typo, and missing BEAST output tables. |
| **Total Composite Score** | **5.8** | **10.0** | **Mixed / Salvageable** (Scientific Core Score: **4.5 / 8.0**) |
