# Blinded Review: SP_ANON_121

**Composite Score:** 6.8 / 10.0 (Rigor: 2.3/3.5 | Claims: 1.7/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** Linear Sequential Topology Assumption & Internal Text-Result Contradiction
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Epidemiological Observational

---

## 1. Executive Summary

This manuscript characterizes longitudinal intra-host HIV-1 subtype B *pol* substitution rates and codon selection ($dN/dS$) across 93 antiretroviral-naive men who have sex with men (77 mono-infected, 16 dually infected) from a primary infection cohort, utilizing population-based Sanger sequencing (GenBank KC814216–KC814576). The authors compare two treatments of IUPAC nucleotide ambiguities in the Tamura-Nei (TN93) genetic distance framework—resolving ambiguities to minimize distance (`TN93-resolved`) versus averaging across all possible resolutions (`TN93-averaged`)—and fit codon-level Muse-Gaut (MG94) models in HyPhy across whole *pol* and putative HLA-matched cytotoxic T-lymphocyte ($\text{CTL}^+$ vs. $\text{CTL}^-$) epitope partitions. While the empirical dataset is valuable and the authors appropriately caution that elevated apparent substitution rates in dually infected hosts reflect strain replacement or mixing rather than accelerated de novo mutation, the evolutionary rate inference relies on a linear ancestor-descendant topology across sequentially sampled bulk consensus sequences, and the Discussion contains direct internal contradictions with the reported numerical results regarding CTL selection in dual infection.

---

## 2. Methodological & Statistical Audit

* **Chronological Linear Topology Assumption in MG94 Rate Estimation:** In the Methods ("Substitution Rate Analysis"), the joint likelihood of longitudinal sequences is maximized by computing "the probability of evolving from the oldest to the newest sequence (given all the intermediates, if present), along the tissue sample chronology, using a custom written HyPhy script." Treating sequentially sampled bulk population sequences as direct linear ancestors of subsequent timepoints violates coalescent tree structure: longitudinal samples are terminal tips diverging from internal common ancestors, not direct progenitors of later samples. Forcing a linear chain across bulk consensus sequences forces transient polymorphisms and lineage shifts onto a single trunk, systematically inflating branch lengths and substitution rate estimates—particularly in dually infected subjects undergoing lineage turnover.
* **Internal Contradictions Between Results and Discussion on $\text{CTL}^+$ vs. $\text{CTL}^-$ Selection:**
  1. In Results ("Testing for Signal of HLA Mediated Selection"), mono-infected individuals exhibit higher $dN/dS$ in $\text{CTL}^+$ regions ($0.98$, 95% CI $0.68\text{–}1.36$) than in $\text{CTL}^-$ regions ($0.49$, 95% CI $0.45\text{–}0.55$, $p < 0.001$). Conversely, in dually infected individuals, the Results explicitly report that $dN/dS$ is *lower* in $\text{CTL}^+$ regions ($0.15$, 95% CI $0.08\text{–}0.24$) than in $\text{CTL}^-$ regions ($0.31$, 95% CI $0.27\text{–}0.35$, $p < 0.001$). Yet in the Discussion (paragraph 4), the text asserts: *"Significantly higher dN/dS substitutions within CTL epitopes compared to non-CTL regions in the pol gene of dually infected cohort mirrored our findings in mono-infected individuals."* This statement is the exact opposite of the numerical findings reported in the Results.
  2. Two sentences earlier in the same Discussion paragraph, the manuscript states: *"Although we observed insignificantly faster nucleotide substitution and higher dN/dS rates within putative CTL targeted regions..."* despite reporting statistically significant differences ($p = 0.005$ and $p < 0.001$) in the Results.
* **Ambiguity Averaging Inflation and Table 1 Formatting:** The comparison between `TN93-resolved` ($0.06\%$ median distance) and `TN93-averaged` ($0.36\%$ median distance) effectively illustrates how bulk Sanger mixed bases dominate naive distance metrics when overall divergence is low. However, in Table 1, the 5%–95% quantile range for `TN93-resolved` substitution rate in mono-infection is printed as `(-0.0000–0.0012)` with a negative sign artifact on zero. Furthermore, the $R^2 \ge 0.98$ concordance check across substitution models (JC69, F81, K80, HKY85, TN93, GTR, GTR+$\Gamma_4$) is performed on pairwise genetic distances where total divergence is $<2\%$; in this near-zero divergence regime, all continuous-time Markov models are first-order linear in substitution counts, so high $R^2$ is mathematically guaranteed and does not validate model adequacy for codon-level $dN/dS$ inference.

---

## 3. Biological / Experimental Grounding & Claim Proportionality

* **`[Well Supported]` Limited Intra-Host *pol* Sequence Divergence in ART-Naive Mono-Infection:** The finding that longitudinal subtype B *pol* sequences evolve slowly in untreated mono-infection ($7.2 \times 10^{-4}$ substitutions/site/year under MG94, with 75% of pairs remains below the 0.5th percentile of LANL inter-host diversity after 4 years) is well grounded in the cohort data and consistent with purifying constraint on viral enzymes.
* **`[Well Supported]` Confounding of Substitution Rates by Strain Turnover in Dual Infection:** The authors' interpretation that the apparent 10-fold rate elevation in dual infection ($9.7 \times 10^{-3}$ subs/site/year) reflects shifts in dominant co-infecting variants or recombination rather than an intrinsic change in reverse transcriptase fidelity is biologically sound and well supported by the paired UDS data cited for these subjects.
* **`[Methodologically Flawed]` Concordant Positive CTL Selection in Dual and Mono-Infection:** As noted in the methodological audit, the claim in the Discussion that dually infected patients show elevated $dN/dS$ in $\text{CTL}^+$ regions mirroring mono-infected patients is directly refuted by the authors' own MG94 estimates ($\text{CTL}^+ dN/dS = 0.15$ vs. $\text{CTL}^- dN/dS = 0.31$ in dual infection). Moreover, putative $\text{CTL}^+$ partitioning relies solely on static in silico motif scanning (`MHCI_binding` PEPDIST) across the baseline sequence without experimental IFN-$\gamma$ ELISpot verification or accounting for overlapping reading frames and protease/RT structural constraints.

---

## 4. Reproducibility & Data Completeness

* **Data Availability:** All longitudinal *pol* sequences are deposited in GenBank under accession numbers `KC814216–KC814576`, and clinical/cohort metadata are summarized in Table 1 and Table S1.
* **Code & Model Availability:** While standard HyPhy template batch files were used for distance and MG94 estimation, the custom HyPhy script implementing the sequential multi-timepoint likelihood and the exact $\text{CTL}^+/\text{CTL}^-$ partition coordinate definitions per patient HLA genotype are not archived in a public code repository.
