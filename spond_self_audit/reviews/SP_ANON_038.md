# Blinded Review: SP_ANON_038
**Composite Score:** 6.8 / 10.0 (Rigor: 2.3/3.5 | Claims: 1.7/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.3/2.0)
**Bias Category:** Non-Suppressed Baseline Participants Included in "ART Interruption Rebound" Cohort, Table Negative-Day Data Errors & Paucicellular CSF Template Resampling
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab Functional Validation
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Clinical/Epidemiological Observational

---

### 1. Executive Summary
This longitudinal study investigates whether HIV-1 rebounds independently within the central nervous system (CNS) following antiretroviral therapy (ART) interruption by performing Roche 454 FLX Titanium pyrosequencing of *env* (C2–V3), *pol* (RT), and *gag* (p24) across 38 paired cerebrospinal fluid (CSF) and blood plasma samples from 14 HIV-infected participants (plus paired PBMC and CSF cellular pellet HIV DNA in a subset of 10 and 9 participants). Using a conservative 4-part statistical definition of compartmentalization (requiring simultaneous significance on Hudson's $F_{ST}$ permutation test with and without read-frequency weights, the phylogeny-based Slatkin-Maddison test, and an aLRT $\ge 0.9$ CSF-only clade comprising $\ge 3$ haplotypes and $\ge 5\%$ read frequency), the authors report CSF/blood compartmentalization at the earliest post-interruption timepoint in 5/14 subjects (and in 9/14 subjects overall across follow-up), alongside CSF-unique clades in 12/14 subjects and genetic segregation between rebounding CSF RNA and CSF cell-pellet DNA in 9/10 cases.

---

### 2. Methodological & Statistical Audit
* **Inclusion of Virologically Unsuppressed Patients in an "ART Interruption Rebound" Study (Group 2, Table 1):** Although the study is framed around viral rebound following structured or unstructured ART interruption, Table 1 reveals that all 4 participants in Group 2 (**24409, 25839, NM487, and 58786**) were **not virologically suppressed prior to ART interruption**—their pre-interruption plasma HIV RNA levels were $2.5$, $5.6$, $4.2$, and $4.2 \log_{10}\text{ copies/mL}$, respectively. Interrupting ART in a patient who already has $5.6 \log_{10}$ ($~400,000\text{ copies/mL}$) of ongoing viremia does not measure reservoir reactivation/rebound from latency; it measures continuation of chronic untreated/failing replication where pre-existing CNS compartmentalization is already well established.
* **Data Entry Errors Producing Negative "Days to Rebound After TI" in Tables 1 and 2:**
  * In **Table 1** (Group 3), under the column *"Time in days to 1st rebound after TI"*, participant **34535** is listed as **`-580` days** and participant **26919** is listed as **`-13` days**!
  * Consequently, in **Table 2**, the summary row *"Days to first viral load >200 after TI"* for Group 3 is reported as a median of **`-196` (range `-580–13`)**, and for All participants as **`28 (-580–136)`**!
  A viral rebound occurring 580 days *before* treatment interruption is chronologically impossible and indicates either that the treatment interruption date and rebound date were inverted in the database or that a prior pre-ART viral load date was erroneously subtracted from the TI date.
* **Low CSF Template Input and 454 Resampling Inflation of "CSF-Only Clades":** The authors estimate the minimum number of viral RNA templates entering the RT-PCR reaction as $0.3\text{ mL} \times \text{CSF viral load}$ (Methods). For CSF samples with low viral loads ($2.3\text{–}3.0 \log_{10}\text{ copies/mL}$, i.e., $200\text{–}1,000\text{ copies/mL}$), this corresponds to only **60 to 300 virion RNA copies before extraction and RT inefficiency** (meaning often $<10\text{–}30$ actual cDNA templates amplified). Without molecular barcoding (Primer IDs), 454 pyrosequencing of 10–30 templates to a depth of thousands of reads resamples the same template hundreds of times; residual 454 homopolymer/PCR errors around a single resampled template can generate $\ge 3$ closely related "haplotypes" summing to $\ge 5\%$ read frequency, mimicking a monophyletic "CSF-only clade." To their credit, the authors require all 4 tests (including frequency-collapsed $F_{ST}$ and Slatkin-Maddison) to call full compartmentalization and candidly discuss low CSF template input in the Discussion.
* **Long Lag Between Rebound and First CSF Sampling in Retrospective Groups:** While Group 1 ($n=5$) was sampled a median of 19 days after rebound, Groups 2 and 3 ($n=9$) were sampled a median of 60 days (up to 227 days) after viral rebound, allowing months of post-rebound diversification.

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim:** *Stringent multi-test bioinformatics criteria demonstrate that rebounding HIV-1 RNA in CSF is frequently compartmentalized from paired blood plasma (9/14 subjects) and contains CSF-specific clades that can persist longitudinally.* **[Moderately Supported]** — Strongest in the 5 prospectively monitored Group 1 participants and the 2 participants (34535, 26919) where pre-ART CSF lineages re-emerged post-interruption; weakened in Group 2 by the lack of pre-TI suppression.
* **Claim:** *Rebounding HIV RNA in the CSF is genetically segregated from HIV DNA in paired CSF cellular pellets (9/10 cases), suggesting CNS rebound originates from deeper brain parenchymal reservoirs (e.g., microglia/macrophages) rather than CSF-trafficking lymphocytes.* **[Moderately Supported]** — Biologically plausible, though as the authors acknowledge, paucicellular CSF cell pellets suffer from severe template undersampling of the DNA reservoir.

---

### 4. Reproducibility & Data Completeness
* **Interactive Trees and Pipeline Transparency:** Interactive haplotype trees are hosted publicly (`http://bit.ly/gianella-pond-ellis-trees`), and the 454 denoising/clustering workflow is described in detail, though raw 454 SRA accession numbers are not listed in the main text.
* **Tabular Data Quality:** The negative rebound times (`-580` days, median `-196` days) in Tables 1 and 2 must be audited and corrected.
