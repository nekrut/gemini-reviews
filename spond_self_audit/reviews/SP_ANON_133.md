# Blinded Review: SP_ANON_133

**Composite Score:** 7.8 / 10.0 (Rigor: 2.7/3.5 | Claims: 2.0/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** Unadjusted Confounding by Earlier Diagnosis Over Time in Trend Regressions
**Verdict:** Minor Revision
**Study Modality:** Dry-Lab Secondary Cohort/Database Re-Analysis
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Epidemiological Observational

---

## 1. Executive Summary

This retrospective clinical cohort study analyzes temporal trends, phylogenetic transmission clustering, and codon-level natural selection of transmitted HIV-1 drug resistance (TDR) across 4,253 ART-naive patients (and 3,155 ART-experienced patients for phylogenetic context) in an integrated Northern California healthcare system between 2003 and 2016. Combining Stanford HIVdb surveillance drug resistance mutation (`SDRM`) annotations with maximum-likelihood/Bayesian phylogenetic cluster detection (`IQ-TREE`, `ClusterPicker`, `BEAST`) and internal/terminal branch selection testing (`HyPhy FEL` on 1,680 sequences), the authors show that most TDR in ART-naive patients arises from Naive-to-Naive (`N-to-N`) transmission chains and that 40 of 43 SDRM positions experience purifying selection (`dN/dS < 1`) in untreated hosts. The integration of large-scale clinical epidemiology with evolutionary selection modeling is strong, though the logistic regression analyses of temporal TDR trends omit multivariable adjustment for the marked secular shift toward earlier HIV diagnosis over the 14-year study window.

---

## 2. Methodological & Statistical Audit

* **Unadjusted Confounding by Secular Shifts Toward Earlier HIV Diagnosis in Temporal Trend Regressions (Results lines 30–34):** The authors document two highly significant secular trends in their ART-naive cohort between 2003 and 2016:
  1. Mean CD4 count at genotyping increased from $259\text{ cells}/\mu\text{L}$ in 2003 to $419\text{ cells}/\mu\text{L}$ in 2016 ($p < 0.001$).
  2. The proportion of sequences with $<0.5\%$ mixed bases (an established molecular proxy for recent infection) increased from $29.8\%$ in 2003 to $52.3\%$ in 2016 ($p < 0.001$).
  Because fitness-impairing TDR mutations (and even some NNRTI/NRTI mutations) revert to wild-type or decay below bulk Sanger detection over years of untreated chronic infection, testing patients earlier after seroconversion mechanically increases the probability of detecting TDR. However, when the authors fit logistic regression models to estimate the annual change in TDR prevalence (`OR = 1.05` per year overall, $p = 0.004$; `OR = 1.11` per year for NNRTIs, $p < 0.001$), they fit **univariate** models with sample year as the sole predictor! Failing to adjust the yearly trend models for baseline CD4 count and nucleotide mixture percentage (`<0.5%`) leaves the upward temporal trend confounded by earlier clinical presentation and baseline genotyping.
* **Principled Use of `HyPhy FEL` to Quantify Reversion/Purifying Selection on ART-Naive Branches:** Restricting `FEL` codon selection inference to the 1,680 subtype B sequences belonging to clusters of $\ge 3$ ART-naive individuals (plus outgroups) and masking branches leading to ART-experienced individuals is a clean, well-designed evolutionary test. Demonstrating that 40 of 43 SDRM positions are under significant purifying selection (`dN/dS < 1`) while `K103N` (`RT 103`), `V179D` (`RT 179`), and `L90M` (`PR 90`) escape strong negative selection directly explains why `K103N` and `L90M` dominate multi-person `N-to-N` transmission clusters.
* **Minor Numerical Typo in Figure 3A Legend (Line 101):** The legend to Figure 3A states *"the complete antiretroviral therapy–naive dataset of 4235 virus sequences"*, transposing the last two digits of $4,253$ (which is reported consistently throughout the Abstract, Results, and Table 1).

---

## 3. Biological / Experimental Grounding & Claim Proportionality

* **`[Well Supported]` Dominance of ART-Naive-to-Naive (`N-to-N`) Transmission Chains in Propagating Common SDRMs (`K103N`, `L90M`, `T215` Revertants):** The phylogenetic cluster analysis (showing 61.3% of clustering TDR sequences link exclusively to other ART-naive patients, including large multi-year clusters of `K103N` and `L90M`) paired with `FEL` selection estimates provides a cohesive mechanistic explanation for persistent TDR despite declining acquired resistance in treated patients.
* **`[Moderately Supported]` Secular Increase in Overall and NNRTI TDR Prevalence (2003–2016):** While raw prevalence clearly rose over time, the extent to which this represents an increase in incident resistant transmissions versus earlier genotyping prior to in-host reversion remains unquantified without a CD4/mixture-adjusted multivariable regression.

---

## 4. Reproducibility & Data Completeness

* **Data & Privacy Constraints:** Clinical demographic tables, SDRM tallies, and `FEL` site-level selection tables are thoroughly reported in the text and supplementary tables. However, the underlying HIV-1 *pol* nucleotide sequences are not deposited in GenBank (a common institutional/IRB constraint in dense regional healthcare cohorts to prevent patient re-identification via transmission network reconstruction, though an explicit data-availability statement explaining access procedures should be included).
