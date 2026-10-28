# Blinded Review: SP_ANON_135

**Composite Score:** 3.8 / 10.0 (Rigor: 1.0/3.5 | Claims: 0.7/2.5 | Biology: 1.0/2.0 | Reproducibility: 1.1/2.0)
**Bias Category:** Base-Rate (False-Positive PPV) Fallacy & Asymmetric Confirmation Bias
**Verdict:** Reject
**Study Modality:** Dry-Lab Secondary Cohort/Database Re-Analysis
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Epidemiological Observational

---

## 1. Executive Summary

This narrative review and perspective piece compiles retrospective serological, wastewater, and clinical swab studies (Tables 1 and 2) to argue that SARS-CoV-2 was circulating in Europe, the Americas, and globally as early as September–November 2019—months before the December 2019 Wuhan outbreak—and proposes an "early precursor attenuation model" wherein low-transmissibility, low-virulence variants spread worldwide via travel hubs before an adapted lineage triggered the recognized pandemic. While compiling both positive (Table 1) and negative (Table 2) retrospective surveillance reports is useful as a bibliography, the manuscript's epidemiological and statistical reasoning commits a textbook **base-rate fallacy** regarding diagnostic assay specificity in zero-/near-zero-prevalence populations, selectively dismisses large-scale negative SARI/ILI PCR cohorts while accepting unconfirmed high-false-positive serology and nested-PCR claims at face value, and advances a global pre-December 2019 circulation model that is incompatible with viral phylodynamics and clinical pneumonia surveillance.

---

## 2. Methodological & Statistical Audit

* **Textbook Base-Rate Fallacy and Misunderstanding of Positive Predictive Value (PPV) (Line 100):** When screening pre-pandemic banked samples where true disease prevalence $p$ is zero or near-zero ($p \to 0$), any serological or nested-PCR assay with specificity $<100\%$ generates false positives at rate $1 - \text{Specificity}$, yielding a Positive Predictive Value $\text{PPV} = \frac{p \cdot \text{Sens}}{p \cdot \text{Sens} + (1-p)(1-\text{Spec})} \approx 0$. In the *Discussion* (line 100), the authors attempt to dismiss false positives with the following probabilistic fallacy:
  > *"As all it would take to establish early circulation is a single confirmed positive case, attributing all results to false positives quickly becomes probabilistically untenable."*
  This statement treats false-positive assay hits across multiple uncalibrated studies as if they were independent tests of the *same* specimen with $100\%$ specificity. In reality, if 20 retrospective studies each screen ratusan or thousands of pre-pandemic sera using ELISA/neutralization assays with 98%–99% specificity (cross-reactive with seasonal human coronaviruses `OC43`, `HKU1`, `229E`, `NL63`) or nested RT-PCR prone to amplicon carryover contamination, it is a mathematical certainty that *most or all* such studies will report raw "positive" hits even when true prevalence is strictly $0\%$.
* **Epidemiological Impossibility of the Cited September–November 2019 Seroprevalence Figures:** The authors uncritically endorse studies in Table 1 reporting **11.6% to 14.0% SARS-CoV-2 seropositivity across Italy in September–October 2019** (Ref. 22: 111/959 positive across all 20 Italian regions, >50% neutralized), **3.3%–3.9% in France in November 2019** (Ref. 10), and **7.7% (3/39) of measles-like rash swabs in Lombardy in Sept–Nov 2019** (Ref. 24). The authors fail to perform a basic quantitative sanity check on these numbers:
  1. If $11.6\%$ of the Italian population (~7 million people!) had already been infected and seroconverted by **September 2019**, then even under a hypothetical 10-fold lower infection fatality rate or hospitalization rate, tens of thousands of viral pneumonia hospitalizations and thousands of RT-PCR positive respiratory swabs would have flooded Italian hospitals in August–November 2019.
  2. Yet Table 2 shows that large-scale, gold-standard clinical RT-PCR screens of actual **respiratory/ILI/SARI patients** in the exact same region and timeframe found **0/1,581** (`0%`, Lombardy SARI, Nov 2019–Jan 2020, Ref. 49), **0/631** (`0%`, Lombardy SARI, Oct–Dec 2019, Ref. 50), **0/1,683** (`0%`, Italy respiratory samples, Oct 2019–Jan 2020, Ref. 48), and **0/5,833** (`0%`, Spain ILI, Nov 2019–Feb 2020, Ref. 51)!
* **Asymmetric Skepticism Between Positive and Negative Studies:** The authors dismiss the thousands of negative respiratory/SARI RT-PCR swabs in Table 2 by speculating that early SARS-CoV-2 may have had "alternate tropism" (causing measles-like skin rashes in children or colorectal/wastewater shedding without respiratory illness!) or failed to match PCR primers, while accepting nested-PCR amplicons from measles swabs and wastewater (where positive controls of Wuhan-Hu-1/2020 SARS-CoV-2 were handled in the same laboratories) as authentic pre-pandemic circulation.
* **Incompatibility with Molecular Clock and Sequence Diversity Data:** Whenever nested-PCR amplicons from Autumn 2019 European samples (e.g., Ref. 24) were sequenced, they carried mutations characteristic of **Spring 2020 European lineages** (such as `B.1` / D614G or Wuhan-Hu-1 consensus) rather than ancestral basal diversity—a classic forensic signature of laboratory PCR carryover contamination from 2020 clinical runs.

---

## 3. Biological / Experimental Grounding & Claim Proportionality

* **`[Well Supported]` Utility of Compiling Positive and Negative Retrospective Surveillance Studies in Tables 1 and 2:** Tabulating the sample sizes, collection windows, assay types, and positivity rates across both positive and negative retrospective studies provides a useful reference summary of the literature.
* **`[Methodologically Flawed]` Claim that Attributing Pre-December 2019 Positive Hits to False Positives is "Probabilistically Untenable":** This claim rests on a fundamental misunderstanding of diagnostic specificity, cross-reactivity, and Positive Predictive Value under near-zero prior prevalence.
* **`[Overstated]` Global Circulation of Attenuated Precursor SARS-CoV-2 Variants Across Europe and the Americas in Autumn 2019:** Claiming that SARS-CoV-2 circulated in Italy, France, the UK, Brazil, and the USA months before December 2019—infecting >10% of screened Italian cohorts while producing 0 positives among >10,000 hospitalized SARI/ILI respiratory swabs—is biologically and epidemiologically untenable.

---

## 4. Reproducibility & Data Completeness

* **Data Completeness:** As a secondary literature review, all underlying data are drawn from the cited publications summarized in Tables 1 and 2. No quantitative meta-analysis, Bayesian specificity-adjusted prevalence estimation, or code is presented.
