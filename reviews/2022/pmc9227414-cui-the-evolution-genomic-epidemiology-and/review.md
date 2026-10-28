# Review of PMC9227414 (PMID:35746707)

**Manuscript Title:** The Evolution, Genomic Epidemiology, and Transmission Dynamics of Tembusu Virus  
**Authors:** Cui Y, Pan Y, Guo J, Wang D, Tong X, Wang Y, Li J, Zhao J, Ji Y, Wu Z, Zeng P, Zhou J, Feng X, Hou L, Liu J.  
**Journal / Preprint:** *Viruses* (2022; `PMC9227414` / `PMID:35746707` / `10.3390/v14061236`)  
**Calibration Study Cohort:** Cohort C — Wild Literature Sample (`C34` | Double-Blinded as `ANON_158`)  
**Overall Score:** **4.2 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.1/3.5 | Claims: 1.0/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.0/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents a bioinformatic analysis of 110 Tembusu virus (TMUV) complete genome and envelope (E) gene sequences downloaded from NCBI GenBank (up to May 2022) alongside reference sequences from Zika virus, West Nile virus (WNV), dengue virus, Quang Binh virus, and mosquito flaviviruses. Using RDP4/SplitsTree for recombination screening, BEAST v1.10.4 for molecular clock dating, Bayesian Skyline demographic reconstruction, and discrete-trait phylogeography (BSSVS/SpreaD3), RAxML and MrBayes for phylogenetic reconstruction, AlphaFold2 for E-protein homology modeling, and Datamonkey (`FEL`, `SLAC`, `FUBAR`, `MEME`) for codon selection analysis, the authors estimate a whole-genome TMUV tMRCA of 1924 (95% HPD: 1850–1983) and a substitution rate of $9.66 \times 10^{-4}$ subs/site/year. They classify TMUV into clusters 1, 2 (2.1 and 2.2), and 3, identify Malaysia and Shandong Province as the primary international and domestic geographic sources, and report two positively selected codons (`NS3-591` and `NS5-883`).

While compiling 110 TMUV genomes for phylodynamic tracking is a useful descriptive exercise, several of the manuscript's primary conclusions are directly contradicted by its own tables or rest on fundamental phylogenetic misconceptions. Specifically: (1) Table 1 directly refutes the claim in the Abstract and Section 3.5 that `NS3-591` and `NS5-883` are confirmed as positively selected by at least two methods under the authors' own significance criteria (`NS3-591` fails *all four* tests in Table 1: FEL $p = 0.072$, SLAC $p = 0.304$, FUBAR $\text{PP} = 0.825$, MEME $p = 0.09$); (2) the authors misinterpret an unrooted/outgroup-rooted flavivirus phylogeny (Figure 6) as showing that TMUV, WNV, and Zika virus literally evolved from extant insect-specific flaviviruses ("originated from mosquito flavivirus and Quang Binh virus"); (3) no root-to-tip regression (TempEst) is performed to verify temporal clock signal before BEAST dating, yielding a 133-year 95% HPD interval (1850–1983) that encompasses the previously published 1934 estimate; and (4) BSSVS discrete phylogeography is interpreted without accounting for extreme spatial and temporal sampling bias (almost all post-2010 poultry sequences come from Chinese duck-farming provinces, whereas early pre-2000 sequences are from Malaysian mosquitoes).

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Codons 591 of NS3 and 883 of NS5 are under positive selection, confirmed by at least two of the four Datamonkey methods (FEL, FUBAR, SLAC, MEME): [Methodologically Flawed].**  
  In Section 2.3 (line 45), the authors define their significance thresholds: *"Positive selection sites were confirmed by at least two methods, with p-values for both FEL and MEME of less than 0.05, p < 0.1 by SLAC, and a posterior probability > 0.9 by FUBAR."* In Table 1 (lines 134–135), the reported values for `NS3-591` are FEL $p = 0.072$, SLAC $p = 0.304$, FUBAR $\text{Post. Pro} = 0.825$, and MEME $p = 0.09$—meaning **zero of the four methods** meet the significance thresholds defined in the Methods! Even if the FEL and MEME thresholds are relaxed to $p < 0.10$ as written in the Table 1 footnote (contradicting Section 2.3), `NS5-883` has FEL $p = 0.11$ and SLAC $p = 0.226$, leaving only FUBAR ($\text{PP} = 0.991$) and borderline MEME ($p = 0.05$). Moreover, Table 1 incorrectly reports the `FEL`, `SLAC`, and `FUBAR` test statistics for `NS3-591` ($3.279, 2.42, 19.058$) and `NS5-883` ($1.302, 3.16, 2.394$) as positive `dN-dS` values while listing `W+` for MEME.

* **TMUV, West Nile virus, and Zika virus originated from mosquito flavivirus and Quang Binh virus: [Methodologically Flawed].**  
  In Section 3.4 (line 111) and the Discussion (lines 153, 155), the authors state: *"Based on phylogenetic analysis, we found that they originated from mosquito flavivirus and Quang Binh virus (Figure 5)"* and *"confirmed that avian TMUV is formed after multiple spills of the mosquito flavivirus."* Quang Binh virus and insect-specific mosquito flaviviruses are divergent, insect-restricted *Flavivirus* species that form the basal outgroup clade in the 6-species tree (Figure 6). Concluding that crown mosquito-borne vertebrate flaviviruses (TMUV, WNV, ZIKV, DENV) descended from extant insect-specific flaviviruses confuses a basal sister clade on a tree with a direct ancestor. In addition, Section 3.4 (line 111) reports `bootstrap = 100%` and `bootstrap = 79.8%` for Figure 6, whereas Section 2.2 (line 40) and the Figure 6 caption state the tree was reconstructed by Bayesian Inference in MrBayes (which outputs posterior probabilities, not bootstrap percentages).

* **The tMRCA of TMUV is 1924, earlier than the previously reported 1934, and its substitution rate ($9.66 \times 10^{-4}$ subs/site/year) is faster due to vaccine-driven immune escape and host expansion: [Overstated].**  
  First, the 95% HPD interval for the whole-genome tMRCA is 1850–1983 (spanning 133 years), and the individual gene tMRCAs range from 1932 to 1982 (Section 3.1, line 58). Because 1934 falls squarely near the center of the 1850–1983 HPD interval, the claim that 1924 is meaningfully earlier than 1934 is statistically unsupported. Second, the authors did not perform a root-to-tip regression (e.g., TempEst) or date-randomization test to verify whether the 109 non-recombinant genomes possess sufficient temporal signal to calibrate a relaxed clock. Third, attributing the higher substitution rate point estimate to TMUV vaccination and mammalian host jumps (Discussion, line 147) is speculative and untested (no branch-specific clock rates comparing pre- vs. post-vaccine lineages or duck vs. non-duck hosts were estimated).

* **TMUV divides into Clusters 1, 2 (2.1 and 2.2), and 3, experienced a population expansion between 2008/2010 and 2013, and spread from Malaysia to Shandong Province and then to other Chinese provinces: [Moderately Supported].**  
  The E-gene clustering into Clusters 1, 2.1, 2.2, and 3 (Figure 3) and the 2010–2013 expansion in the Bayesian Skyline Plot (Figure 2) match the documented emergence of duck egg-drop syndrome in China in 2010. However, the discrete phylogeographic inference (BSSVS, Figure 5) does not control for severe ascertainment skew: because historical pre-2000 isolates were collected in Malaysia and intensive sampling after 2010 occurred in Shandong (which produces one-third of China's commercial ducks), BSSVS transition rates inevitably place the root in Malaysia and the domestic hub in Shandong regardless of whether unobserved circulation occurred in intermediate Southeast Asian or southern Chinese regions.

* **Mutations P73S, S83P, and N277S in the E protein alter virulence, infectivity, and cross-species transmissibility: [Overstated].**  
  These three amino acid substitutions are clade-defining synapomorphies on the E-protein phylogeny (Figure 4), none of which were detected as positively selected in the selection scan (Section 3.5). Mapping clade-diagnostic neutral substitutions onto an AlphaFold2 structure does not demonstrate that they alter virulence or transmissibility without reverse-genetics or functional assays.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile Selection Criteria in Section 2.3 with Table 1 and Remove Unsupported Positive Selection Claims
* **WHY:** Section 2.3 states that positive selection requires $p < 0.05$ for FEL and MEME, $p < 0.1$ for SLAC, and $\text{PP} > 0.9$ for FUBAR across at least two methods, yet `NS3-591` fails every single threshold in Table 1 ($p = 0.072, 0.304, 0.09$; $\text{PP} = 0.825$) and `NS5-883` passes only FUBAR ($\text{PP} = 0.991$) and borderline MEME ($p = 0.05$).
* **WHAT & HOW:** Correct the text in the Abstract, Section 3.5, and Discussion to state accurately that `NS3-591` showed only weak/marginal evidence of episodic/pervasive selection at the relaxed $p < 0.10$ level (FEL $p = 0.072$, MEME $p = 0.09$) and did not pass the $p < 0.05$ or $\text{PP} > 0.90$ criteria, while `NS5-883` was supported by FUBAR ($\text{PP} = 0.991$) and MEME ($p = 0.05$). Also verify the column headers in Table 1 (`dN-dS` vs. $\beta/\alpha$ or $\omega^+$).

#### 2. Assess Temporal Clock Signal and Properly Report tMRCA Uncertainty
* **WHY:** Running BEAST without verifying linear root-to-tip divergence over sampling time can produce spurious tMRCA and rate estimates, and claiming that 1924 (95% HPD: 1850–1983) is significantly earlier than 1934 ignores the 133-year credible interval.
* **WHAT:** Perform a root-to-tip regression in TempEst and revise the Abstract and Discussion to reflect the wide overlap between the 1850–1983 HPD interval and previous estimates.
* **HOW:** Input the RAxML E-gene and whole-genome ML trees alongside tip collection dates into TempEst to report the $R^2$ and slope of root-to-tip divergence vs. time. In the Abstract and Section 4, report the 95% HPD interval (`1850–1983`) alongside the 1924 point estimate and note that it is statistically compatible with the previously reported 1934 tMRCA.

#### 3. Correct the Phylogenetic Interpretation of Outgroup Flaviviruses in Section 3.4 and Discussion
* **WHY:** Insect-specific mosquito flaviviruses and Quang Binh virus are extant outgroup taxa, not the literal ancestors from which TMUV, WNV, and ZIKV evolved through "multiple spills."
* **WHAT & HOW:** Revise Section 3.4 (line 111) and the Discussion (lines 153, 155) to state that TMUV clusters within the mosquito-borne vertebrate flavivirus clade (closely related to WNV and ZIKV) while insect-specific flaviviruses (such as Quang Binh virus) form a basal sister lineage. Also clarify in Section 3.4 (line 111) whether the support values (`100%` and `79.8%`) are MrBayes posterior probabilities (`1.00` and `0.80`) or RAxML bootstrap percentages.

#### 4. Control for Geographic Sampling Skew in BSSVS Phylogeography
* **WHY:** Discrete-trait BSSVS migration rates are sensitive to unequal sample sizes across locations (e.g., heavy sampling in Shandong vs. sparse sampling in Southeast Asia).
* **WHAT & HOW:** Report the number of sequences per country and Chinese province in the main text, perform a tip-location randomization or downsampling sensitivity analysis (subsampling Shandong and other over-represented provinces to matched sample sizes), and temper the phylogeographic claims in the Discussion to acknowledge sampling bias.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Broken cross-references and missing public data deposition hinder verification.
* **WHAT & HOW:**
  * **Section 3.1 (Line 66) vs. Abstract (Line 8):** The Abstract states the effective population size increased rapidly "from 2010 to 2013," whereas Section 3.1 (line 66) says "until approximately 15 years ago (2008), when a sharp increase in population size was observed, lasting for approximately five years (2013)." Harmonize the exact start year (`2008` vs. `2010`) with the x-axis of Figure 2.
  * **Discussion (Line 151):** Fix `Figure 5 a, Table 1` to `Figure 5 a, Supplementary Table S2` (Table 1 is NS3/NS5 selection, not BSSVS BF/PP values).
  * **Discussion (Line 153):** Fix `(Figure 5)` to `(Figure 6)` when referring to the Flaviviridae multi-species phylogeny.
  * **Data Availability (Line 177):** Deposit the aligned FASTA files, BEAST XML configuration files, and output MCC trees in a public repository (e.g., Zenodo or Dryad) rather than "available upon request."
