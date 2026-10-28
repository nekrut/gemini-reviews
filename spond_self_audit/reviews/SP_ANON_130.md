# Blinded Review: SP_ANON_130

**Composite Score:** 6.6 / 10.0 (Rigor: 2.1/3.5 | Claims: 1.6/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** Unpropagated Phylogenetic Dating Uncertainty & Cohort Pre-Selection Bias
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

---

## 1. Executive Summary

This study investigates the formation dynamics of the "early" (>1 year prior to antiretroviral therapy initiation) replication-competent/near-full-length HIV-1 proviral DNA reservoir in 7 women from the CAPRISA 002 cohort (sampled after a median of 5.1 years on suppressive ART). Using single-genome PacBio sequencing of the 3' half-genome (~4.6 kb *vif*-to-*nef*, 38–133 unique proviral sequences per participant, totaling 286 early proviruses) paired with longitudinal pre-ART plasma viral RNA *env*/*nef* sequences, the authors assign each provirus an estimated integration date (weighted median of patristic distance, clade support, and phylogenetic placement) and test whether early reservoir seeding follows a discretized uniform continuous formation (`dUCF`) or continuous formation with exponential decay (`dCFD`) multinomial distribution. While the PacBio single-genome dataset is high quality and accounting for pre-ART proviral clearance is well motivated, the statistical rejection of continuous seeding (`dCFD`) is compromised by treating noisy point-estimate phylogenetic dates as exact observations binned into discrete pre-ART sampling visits and by cohort pre-selection for women with unusually large early reservoirs.

---

## 2. Methodological & Statistical Audit

* **Failure to Propagate Phylogenetic Dating Uncertainty into the Multinomial Binning Tests (`dUCF` / `dCFD`):** The core statistical test bins each of the 286 early proviral sequences into a discrete 6-month pre-ART sampling interval $d_k$ based solely on its **point-estimate** creation date (the weighted median of three phylogenetic dating estimators), and then tests whether the observed bin counts deviate from multinomial probabilities via a $\chi^2$ simulation test and a 1-parameter exponential decay likelihood ratio test (`dCFD`). This two-stage "point-estimate then hard-bin" procedure has two serious statistical flaws:
  1. *Artificial clumping at sampled plasma RNA timepoints:* Phylogenetic placement and clade dating can only map a provirus to nodes/branches defined by the discretely sampled pre-ART plasma RNA timepoints. If plasma RNA depth, sequence diversity, or population bottlenecks vary across pre-ART visits, proviral point estimates will mechanically cluster onto well-sampled or bottlenecked nodes even if true integration occurred uniformly in continuous time between visits.
  2. *Ignoring wide confidence intervals on individual proviral dates:* Individual proviral dating intervals typically span $\pm 6$ to $\pm 18$ months. Hard-assigning each sequence to a single bin ignores estimation variance, underestimating the variance of the bin counts and inflating the Type I error rate of both the $\chi^2$ and LRT goodness-of-fit tests. A valid test must integrate over the posterior/bootstrap date distribution of each provirus rather than treating point estimates as exact calendar dates.
* **Typographical Error in the `dCFD` Equation (Methods, line 83):** Under item `2. Discretized continuous formation with decay (dCFD)`, the printed probability equation is:
  $$P(\text{interval} = d) \sim (S_{i,k-1} - S_{i,k+1}) / (T_i - 52)$$
  This is identical to the `dUCF` equation immediately above it (`item 1`, line 79) and completely omits the exponential decay weighting factor $\exp(-t / \tau_i)$ or its integral over $[S_{i,k+1}, S_{i,k-1}]$ as a function of the half-life $\lambda_i$!
* **Cohort Ascertainment / Pre-Selection Bias:** The 7 participants analyzed here were not randomly sampled from ART-treated individuals; they were specifically selected from a prior cohort study (Ref. 16) because they possessed a high proportion ($20\%\text{–}70\%$) of early proviruses after ~5 years on ART. Selecting subjects on the outcome variable (an unusually large surviving early proviral fraction) enriches for rare individuals who experienced an exceptional early clonal expansion or immune-escape burst, making it invalid to generalize rejection of continuous decay (`dCFD`) to typical HIV-1 infections.

---

## 3. Biological / Experimental Grounding & Claim Proportionality

* **`[Well Supported]` Persistence of Genetically Diverse Pre-ART Proviruses Anchored to Early Infection:** The 3' half-genome PacBio single-genome sequences convincingly demonstrate that a subset of unique proviruses persisting after 5 years of ART cluster with plasma variants from the first 1–2 years of untreated infection.
* **`[Fragile]` Rejection of Continuous Exponential Decay (`dCFD`) in Favor of Episodic Early Reservoir Seeding:** Because the `dCFD` test does not propagate phylogenetic dating uncertainty, relies on discrete plasma sampling nodes, and analyzes 7 subjects pre-selected for high early proviral prevalence, the statistical rejection of continuous seeding+decay in 6 of 7 women is fragile.
* **`[Moderately Supported]` Minimal Impact of Faster Acute-Phase Proviral Clearance on Post-First-Year Reservoir Distribution:** The sensitivity analysis showing that faster clearance during the first 52 weeks affects only the boundary bin $[S_{i,K}, 52]$ is mathematically reasonable, though it does not resolve the dating-discretization artifact across earlier bins.

---

## 4. Reproducibility & Data Completeness

* **Code & Data Availability:** Custom R scripts and input data tables for the `dUCF`/`dCFD` tests are publicly archived on GitHub (`github.com/[USER_REDACTED]/reservoir_persistence`), and sequences are linked to the primary CAPRISA 002 accession series, though the typographical error in the printed `dCFD` formula in the Methods text should be corrected.
