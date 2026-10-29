# Review of FEXP_ANON_009

**Overall Score:** **6.8 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **5.4 / 8.0**  
* **Score Breakdown:** Rigor: 2.0/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.4/2.0

---

## 1. Blinded Metadata Perception
* **Anonymized Manuscript ID:** `FEXP_ANON_009`
* **Perceived Domain & Design:** Avian viral molecular evolution and genomics; whole-genome sequencing of 10 archival Duck hepatitis A virus type 1 (DHAV-1) isolates from the 2004–2005 Hungarian epizootic (`MT856991–MT857000`), combined with 114 DHAV-1 (58 complete genomes, 56 VP1 sequences) and 24 DHAV-3 complete genomes from GenBank (1993–2020) to analyze recombination (`RDP4`), codon-level selection (`FUBAR`, `FEL`, `MEME`), and evolutionary rates / divergence times (`BEAST` v1.10.4).
* **Blinding Integrity:** Double-blind review maintained; evaluated strictly on internal evolutionary, phylogenetic, and bioinformatic merits at $t_0$.

---

## 2. Executive Summary & Editorial Verdict

This study sequences near-complete coding genomes (7,370–7,386 nt) of 10 archival DHAV-1 isolates collected from Pekin and Muscovy duck flocks during the 2004–2005 outbreak in Bács-Kiskun County, Hungary, and integrates them with 114 DHAV-1 and 24 DHAV-3 GenBank sequences. Using `RDP4` (with Bonferroni-adjusted $p \le 10^{-6}$ for primary events) and split-region neighbor-joining trees, the authors identify three recombination events, notably an inter-genotype recombination in the immunogenic VP0 capsid region between DHAV-1 and DHAV-3 in Chinese strains (`JF828997` vs. `JX235698`). After removing putative recombinants, they run `FUBAR`, `FEL`, and `MEME` on DHAV-1 coding sequences (finding strong purifying selection overall, $dN/dS \le 0.159$, and 4 positively selected codons across VP1 and 3C: aa542, aa676, aa680, and aa1719) and `BEAST` v1.10.4 (lognormal relaxed clock, constant-size coalescent prior, 50M steps) across individual mature protein regions, estimating mean substitution rates of $5.63 \times 10^{-4}$ to $1.11 \times 10^{-3}$ subst/site/year and inferring at least four independent introductions of subgroup SG 1.3 into Hungary from Asian-related lineages.

**Editorial Verdict: Minor to Major Revision (Mixed / Salvageable).** The 10 archival European DHAV-1 complete coding genomes (`MT856991–MT857000`) fill a genuine geographic gap in picornavirus surveillance, and the authors appropriately remove recombinant sequences before performing selection and molecular clock analyses. However, several methodological weaknesses and missing quantitative metrics limit the rigor of the evolutionary inferences: (1) although the Methods state that `TempEst` v1.5.3 was used to check temporal structure (line 43), *no root-to-tip correlation ($r$ or $R^2$) or regression slope is reported anywhere in the paper*, despite acknowledging severe temporal skew (only 3 sequences collected before 2000); (2) using an unrealistic *constant-size coalescent tree prior* for an acute epizootic poultry virus undergoing regional outbreaks and vaccination bottlenecks; (3) reporting mean substitution rates to five significant digits (`5.6286 × 10^-4`) in the text without reporting their 95% HPD intervals (except for VP1) or effective sample sizes (ESS); and (4) inconsistent recombination inclusion criteria (setting a strict $p \le 10^{-6}$ criterion in the Methods, line 39, but then retaining Recombination Event 3 involving the Hungarian strains based on "only two methods of analysis... data not shown" in line 52).

### Assessment of Specific Claims
* **Claim 1 (DHAV undergoes both intra-genotype and inter-genotype [DHAV-1/DHAV-3] recombination, including transfer of an ~800 nt VP0 capsid segment): [Well Supported].**  
  Recombination Events 1 and 2 are supported by multiple `RDP4` algorithms at Bonferroni-corrected $p \le 10^{-6}$ and discordant region-specific phylogenies. By contrast, the putative Recombination Event 3 linking Hungarian strains (`MT856991–MT857000`) as major parents to a 2003 Chinese strain (`EU888310`) over a short 190-nt VP0 segment is only weakly supported by two methods ("data not shown", line 52) and likely reflects shared ancestral polymorphism rather than direct recombination.
* **Claim 2 (DHAV-1 protein-coding regions evolve under strong overall purifying selection [$dN/dS \le 0.159$] with diversifying selection at four specific codons [VP1 S49, Q183, D187; 3C Q104]): [Well Supported].**  
  Recombinants were excluded prior to selection analysis, and the four highlighted sites were concordantly identified across `FEL` ($p < 0.05$), `MEME` ($p < 0.05$), and `FUBAR` ($\text{PP} \ge 0.95$), with VP1 sites 183 and 187 mapping to the known C-terminal hypervariable neutralization loop.
* **Claim 3 (The 2004–2005 Hungarian DHAV-1 outbreak resulted from at least four independent introductions sharing late-1990s ancestors with Chinese SG 1.3 strains): [Fragile].**  
  All 10 Hungarian isolates were collected from duck farms within a *single county* (Bács-Kiskun County) during a single 2004–2005 epizootic and share $99.0\%\text{–}99.4\%$ sequence identity with Chinese reference strains. Inferring "at least four independent introductions" into Hungary simply because the 10 Hungarian sequences form three or four subclusters interspersed with 2000s/2010s Chinese sequences ignores severe geographic undersampling in Europe (zero other European genomes exist in GenBank) and within-epizootic/pre-importation diversity.
* **Claim 4 (DHAV-1 exhibits slightly lower evolutionary rates [$5.63 \times 10^{-4}$ to $1.11 \times 10^{-3}$ subst/site/year] than other picornaviruses): [Fragile].**  
  The VP1 substitution rate ($1.013 \times 10^{-3}$, $95\%\text{ HPD } [6.75 \times 10^{-4}, 1.35 \times 10^{-3}]$) overlaps broadly with typical picornavirus evolutionary rates ($10^{-3}$ to $3 \times 10^{-3}$ subst/site/year), and no formal statistical comparison or 95% HPDs for the other 10 mature proteins are presented in the text.

---

## 3. Forensic Defect Inventory

1. **Pillar 3 & 4 Violation — Unreported `TempEst` Root-to-Tip Regression Statistics and Constant-Population Coalescent Prior (Methods line 43, Results lines 56–58):**  
   Line 43 states that temporal structure was checked with `TempEst` v1.5.3 before running `BEAST` 1.10.4 across all 11 mature protein regions, yet the manuscript never reports the root-to-tip correlation coefficient ($r$), $R^2$, or x-intercept for either the full genome or any individual short gene (several of which, such as 2A1 [60 nt] and 3B [~66 nt], are far too short to have independent molecular clock signal!). Furthermore, imposing a constant-size coalescent tree prior (`constant size coalescent tree prior`, line 43) across 60 years of epizootic outbreaks and vaccine-driven population changes can bias root height and rate estimates when only 3 sequences predate the year 2000 (line 58).
2. **Pillar 3 & 5 Violation — Violation of Prespecified Recombination Threshold for Event 3 and Neighbor-Joining with $p$-Distance (Methods line 39, Results line 52):**  
   Line 39 specifies a strict threshold for accepting recombination events (supported by independent methods with $p \le 10^{-6}$ after Bonferroni correction, confirmed by phylogenetic analysis). Yet in line 52, Recombination Event 3 (~190 nt in VP0 involving Hungarian isolates) is included despite the authors admitting that *"only two methods of analysis supported this event, the sequence and phylogenetic analyses (data not shown) also suggested a historic recombination event."* In addition, breakpoint confirmation trees were built using Neighbor-Joining with uncorrected $p$-distance (`MEGA6`, line 39) rather than maximum likelihood under the best-fit substitution model (`PhyML` SMS, line 43).
3. **Pillar 7 Violation — Missing Tables/Figures in Main Text Representation and False Precision on Substitution Rates:**  
   * **False precision without uncertainty bounds:** Abstract (line 5) and Results (line 56) report mean substitution rates to 5 significant digits (`5.6286 × 10^-4 to 1.1147 × 10^-3`) without providing the 95% HPD intervals for each gene in the text.
   * **Missing tables in the markdown text:** While Tables 1, 2, and 3 and Figures 1–4 are cited in the text, their contents are not embedded in the manuscript body, making it essential that the text itself report the 95% HPDs, `TempEst` $R^2$, and `BEAST` posterior node supports.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.0** | **3.5** | Proper removal of recombinants prior to selection/clock analyses and multi-method selection consensus (`FEL`, `MEME`, `FUBAR`); penalized for unreported `TempEst` temporal signal statistics, constant-size coalescent prior, NJ $p$-distance confirmation trees, and estimating separate clocks on tiny peptides. |
| **2. Claim-to-Evidence Alignment** | **1.8** | **2.5** | Recombination in VP0 (Events 1–2) and VP1 positive selection claims are well supported; claims of "four independent introductions" into a single Hungarian county during a single outbreak and "lower evolutionary rates than other picornaviruses" are overstated given sampling gaps and overlapping HPDs. |
| **3. Data Integrity & Biological/Behavioral Plausibility** | **1.6** | **2.0** | Virus isolation in embryonated Muscovy duck eggs (line 24) prior to sequencing can introduce egg-passage adaptation mutations in VP1; only 3 pre-2000 GenBank sequences exist to anchor the molecular clock. |
| **4. Reproducibility & Data Integrity** | **1.4** | **2.0** | All 10 Hungarian complete coding genomes are publicly deposited in GenBank (`MT856991–MT857000`); however, `TempEst` statistics, `BEAST` XMLs/alignments, and phylogenetic confirmation of Recombination Event 3 ("data not shown") are omitted. |
| **Total Composite Score** | **6.8** | **10.0** | **Mixed / Salvageable** (Scientific Core Score: **5.4 / 8.0**) |

---

### Constructive and Doable Suggestions for Improvement

1. **Report `TempEst` Root-to-Tip $R^2$ Values and Compare Constant Coalescent Against Bayesian Skygrid/Skyline Priors:**  
   * **WHY:** Estimating substitution rates on individual short picornavirus proteins (e.g., 2A, 3A, 3B) when only 3 sequences predate 2000 risks severe prior sensitivity if temporal signal is weak.  
   * **WHAT & HOW:** Report the `TempEst` correlation coefficient ($r$) and $R^2$ for the non-recombinant whole coding alignment and individual gene regions, restrict independent `BEAST` clock rate estimation to genes with positive temporal signal (or partition the whole non-recombinant alignment with linked trees and unlinked rates), and verify robustness under a Bayesian Skyline or Skygrid tree prior.
2. **Enforce the Prespecified Recombination Criterion ($p \le 10^{-6}$ Across $\ge 3$ Methods + ML Bootstrap Support) on Event 3:**  
   * **WHY:** Accepting a 190-nt VP0 putative recombination event supported by only two methods ("data not shown") violates the paper's own Methods threshold (line 39).  
   * **WHAT & HOW:** Replace the NJ $p$-distance trees with maximum-likelihood (`PhyML` / `IQ-TREE`) trees for the 190-nt segment vs. flanking genome, report the bootstrap support values, and downgrade Event 3 to an unconfirmed/putative signal if it fails the $\le 10^{-6}$ threshold.
3. **Temper the "Four Independent Introductions into Hungary" Claim:**  
   * **WHY:** With zero other European DHAV-1 genomes in GenBank, paraphyly of 10 isolates from a single county (`Bács-Kiskun`) relative to Chinese sequences can reflect unsequenced regional diversity in Europe or importation of a genetically diverse flock batch rather than four separate long-distance introduction events.  
   * **WHAT & HOW:** Revise line 58 to note that the four Hungarian sub-clusters within SG 1.3 represent either multiple introductions or previously unsampled European/import diversity, and report the posterior probability and 95% HPD tMRCA for each Hungarian clade.
