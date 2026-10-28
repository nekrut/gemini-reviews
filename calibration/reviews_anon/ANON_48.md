# Review of ANON_48

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.6 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.9/3.5 | Claims: 2.1/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript introduces BUSTED (Branch-Site Unrestricted Statistical Test for Episodic Diversification), a maximum-likelihood random-effects codon model implemented in HyPhy and Datamonkey designed to test for gene-wide episodic positive selection across an entire phylogeny or a pre-specified subset of foreground branches. BUSTED models site-to-site and branch-to-branch variation in $\omega = d_N/d_S$ using a three-category discrete distribution ($\omega_1 \le \omega_2 \le 1 \le \omega_3$) estimated independently on foreground and background branch partitions, testing the null constraint $\omega_3^{\text{FG}} = 1$ via a conservative $\chi^2_2$ likelihood ratio test. It also defines a zero-cost exploratory site-level metric, the constrained Evidence Ratio ($\text{ER}_s = 2 \log [P(D_s | M) / P(D_s | M_s)]$). The authors validate BUSTED on simulated alignments from Lu and Guindon (2014), parametric power simulations based on sperm lysin, an empirical HIV-1 reverse transcriptase (RT) drug-resistance dataset, and 10,779 vertebrate gene alignments from Selectome v06.

BUSTED is a well-formulated statistical advance over classic Nielsen–Yang branch-site models and fixed-switching covarion models (`fitmodel`), particularly because it allows unconstrained episodic selection ($\omega_3^{\text{BG}} \ge 1$) on background branches—preventing background positive selection from inducing false positives on foreground branches—and maintains conservative Type I error control across all simulated null regimes. Two methodological issues warrant refinement: (1) despite explicitly cautioning in the Methods that site-level Evidence Ratios ($\text{ER}_s$) do not obey asymptotic $\chi^2$ sampling properties, the HIV-1 RT analysis applies an uncalibrated asymptotic $\chi^2_1$ ($P < 0.01$) threshold to $\text{ER}_s$ in Table 2 without evaluating site-level false positive rates under the gene-wide alternative model; and (2) the empirical screen finding positive selection in 24.87% of 10,779 Selectome alignments assumes constant synonymous substitution rates ($d_S=1$) and single-nucleotide instantaneous codon changes, both of which can inflate $\omega_3$ (including the plateau at $\hat{\omega}_3 \approx 40$ in Fig. 3D) when multi-nucleotide substitutions or synonymous rate variation occur. Calibrating the site-level $\text{ER}_s$ false discovery behavior under null-site/selected-gene simulations, quantifying the impact of extreme $\hat{\omega}_3$ boundary estimates in Selectome, and fixing a missing footnote in Table 2 will make the manuscript even stronger.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **BUSTED maintains conservative gene-wide Type I error rates across neutral and heterogeneous-branch null simulations while `fitmodel` can be severely anticonservative: [Well Supported].**  
  Across all four neutral/purifying simulation regimes from Lu and Guindon (2014) (Table 1, rows 1–4, 500 replicates each) and the sperm lysin null simulations (Fig. 2B), BUSTED's empirical false positive rate at nominal $\alpha = 0.05$ remains between 0.006 and 0.020, whereas `fitmodel` reaches a 15.0% FPR on 64XX (Table 1) and 23% FPR at $P \le 0.05$ on the lysin-based branch-site null (Fig. 2B).

* **When foreground branches are specified a priori or when a moderate fraction of sites (20%) experience episodic selection, BUSTED achieves higher calibrated power than Nielsen–Yang and `fitmodel`: [Well Supported].**  
  In Table 1 (`BUSTED FG` vs. `NYbs` on 16 B XU and 32 B XU) and the Type-I-error-calibrated power curve (Fig. 2C), BUSTED consistently outperforms both competing methods except on very small trees with sparse foreground branches (Tree 1 $\alpha$ XV and Tree 2 $\delta\gamma$ XV where only 1–2 foreground branches carry signal).

* **BUSTED's site-wise Evidence Ratios ($\text{ER}_s$) thresholded at $\chi^2_1$ ($P < 0.01$) perform comparably to purpose-built directional drug-resistance models (13/15 true positives in HIV-1 RT): [Fragile].**  
  In "Evidence of Selection at Individual Sites," the authors state that $\text{ER}_s = 2 \log[P(D_s | M)/P(D_s | M_s)]$ is computed without re-optimizing model parameters and "we cannot expect it to obey asymptotic sampling properties." However, in the HIV-1 RT benchmark (Table 2), they threshold $\text{ER}_s$ using a $\chi^2_1$ distribution at $P < 0.01$ ($\text{ER}_s > 6.635$) and compare its precision (13/15) directly against calibrated $p$-values from MEDS (13/17) and FEEDS (3/6). Because $\text{ER}_s$ conditions on the gene-wide MLEs ($\hat{\omega}_3^{\text{FG}}, \hat{p}_3^{\text{FG}}$), neutral sites ($\omega=1$) in a gene with strong selection elsewhere can accumulate inflated evidence ratios whenever they happen to have 1–2 nonsynonymous changes and 0 synonymous changes on foreground branches. No simulation results are presented to establish the site-level false positive rate of the $\text{ER}_s > 6.635$ rule.

* **24.87% of 10,779 Euteleostomes genes in Selectome v06 show gene-wide evidence of episodic diversifying selection, with detection rate saturating at $\hat{\omega}_3 \approx 40$: [Moderately Supported].**  
  The large-scale screen demonstrates BUSTED's computational tractability and shows expected positive scaling with alignment length (Fig. 3A). However, because BUSTED fixes the synonymous rate across sites and branches and sets instantaneous rates of double/triple nucleotide substitutions ($\delta(i,j)>1$) to zero, a single multi-nucleotide substitution or a codon with depressed synonymous rate on a short branch forces $\hat{\omega}_3$ to the numerical boundary ("$\approx 40$ is the empirical infinity," Fig. 3D) with a small weight $p_3$, which can trigger gene-wide rejection of $\omega_3=1$ without genuine adaptive diversification.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Evaluate the Site-Level False Positive and True Positive Rates of $\text{ER}_s$ on the Simulated Benchmark Data
* **WHY:** Recommending $\text{ER}_s > 6.635$ ($\chi^2_1, P < 0.01$) as an empirical site-identification rule in Table 2 while stating in the Methods that $\text{ER}_s$ does not follow asymptotic sampling properties leaves readers unsure whether $\text{ER}_s$ controls site-level false positives in genes where BUSTED rejects the gene-wide null.
* **WHAT:** Quantify the empirical distribution and false discovery rate of $\text{ER}_s > 6.635$ at strictly neutral/conserved sites ($\omega \le 1$) inside the already-simulated positive-selection alignments from Table 1 and Fig. 2.
* **HOW:** Using the existing simulation replicates from Table 1 (where $p_s = 0.20$ or $0.40$ of sites have $\omega > 1$ and the remaining $1 - p_s$ of sites have $\omega \le 1$), tabulate the fraction of truly neutral sites ($1 - p_s$) and truly selected sites ($p_s$) that exceed $\text{ER}_s = 6.635$ (or $\text{ER}_s = 3.84$), and report the empirical site-level FPR and TPR in a brief paragraph or supplementary table.

#### 2. Quantify How Many Selectome Detections Rest on Boundary Estimates ($\hat{\omega}_3 \ge 40$, Very Small $\hat{p}_3$)
* **WHY:** In deep vertebrate alignments (Selectome Euteleostomes), single-codon multi-nucleotide hits or zero-synonymous-change branches frequently push $\hat{\omega}_3$ to its upper bound ($\ge 40$) at a tiny proportion of branch-sites ($\hat{p}_3 < 0.005$), which may represent model misspecification (unmodeled multi-hit substitutions or synonymous rate variation) rather than adaptive selection.
* **WHAT:** Stratify the 2,681 significant Selectome alignments by whether $\hat{\omega}_3$ hits the upper boundary ($\ge 40$) and how many sites have $\text{ER}_s > 6.635$.
* **HOW:** From the existing 10,779 Selectome output files, report the percentage of the 2,681 positive detections where $\hat{\omega}_3 \ge 40$ with $\hat{p}_3 < 0.01$ and only a single site drives the likelihood ratio ($>80\%$ of total $\sum \text{ER}_s$), providing users with a practical diagnostic (e.g., requiring $\ge 2$ sites with high $\text{ER}_s$) to filter out single-site multi-nucleotide artifacts.

#### 3. Technical and Editorial Fixes
* **WHY:** Table 2 contains an undefined footnote callout (`a`), and the text has two minor grammatical typos.
* **WHAT & HOW:**
  * **Table 2 (Line 122 & Lines 153–160):** Site 41 has footnote callout `— a` under "BUSTED Evidence Ratio", while the table legend defines footnotes `b`, `c`, and `d` but omits footnote `a`. Add the missing definition for footnote `a` (e.g., explaining that `—` indicates the site did not meet the significance/ER threshold for that method).
  * **Line 104:** Fix *"BUSTED outperform fitmodel"* $\rightarrow$ *"BUSTED outperforms fitmodel"*.
  * **Line 176:** Fix *"along with the those of Lu and Guindon (2014)"* $\rightarrow$ *"along with those of Lu and Guindon (2014)"*.
