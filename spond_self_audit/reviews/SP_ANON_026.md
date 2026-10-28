# Blinded Review: SP_ANON_026
**Composite Score:** 4.8 / 10.0 (Rigor: 1.5/3.5 | Claims: 1.2/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.0/2.0)
**Bias Category:** Table Arithmetic Errors, Text-Table Contradictions & Severe Partner Ascertainment/Missingness Bias
**Verdict:** Major Revision
**Study Modality:** Dry-Lab Secondary Cohort/Database Re-Analysis
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Epidemiological Observational

---

### 1. Executive Summary
This observational cohort study evaluates the yield of partner notification and contact tracing services among 574 individuals diagnosed with acute and early HIV-1 infection (AEH) in the San Diego Primary Infection Resource Consortium (PIRC) between 1996 and 2014. Overall, 107 of 574 (18.6%) AEH index cases recruited 119 sexual partners (128 total partnerships) for HIV testing. Among recruited partners, 68/119 (57.1%) were HIV-positive, including 39 (32.8%) newly diagnosed cases (14 of whom had AEH). Using *pol* sequence genetic distance ($\text{TN93} \le 1.5\%$), 38 of 62 (61.2%) sequenced seroconcordant partnerships were genetically linked, and partner enrollment within 30 days of the index case's screening was significantly associated with new HIV diagnosis ($p=0.01$) and genetic linkage ($p<0.01$). While the public health topic is important, the manuscript suffers from blatant arithmetic errors in Table 1, direct contradictions between the main text and Table 3, $>75\%$ missingness in behavioral risk data, and unaddressed reverse causality in the 30-day enrollment finding.

---

### 2. Methodological & Statistical Audit
* **Internal Arithmetic and Tabulation Errors in Table 1:** In Table 1 ("Number of sexual partners identified per index case"), the column for Index Cases ($N=107$) lists:
  * 1 partner: `90 (84%)`
  * 2 partners: `13 (12%)`
  * 3 partners: `26 (20%)`
  Summing the index cases yields $90 + 13 + 26 = 129 \neq 107$, and the percentages sum to $84\% + 12\% + 20\% = 116\%$. Cross-checking against the Unique Partnerships column ($N=128$, which shows $90 \times 1 = 90$, $13 \times 2 = 26$, and $4 \times 3 = 12$; $90 + 26 + 12 = 128$) reveals that only **4 index cases (3.7%)** identified 3 partners, and the authors erroneously copied `26 (20%)` from the 2-partner Unique Partnerships cell into the 3-partner Index Cases cell.
* **Direct Contradiction Between Main Text and Table 3:** On page 134, the Results text explicitly states: *"there were no significant demographic or behavioral risk differences between HIV infected and uninfected recruited partners except for age (Table 3)."* However, inspection of Table 3 shows that **Condom Use during Receptive Anal Intercourse (RAI)** is statistically significant ($p = 0.031$, Fisher's exact test), where 26.3% of HIV-positive partners vs. 5.0% of HIV-negative partners reported "Always" using condoms (and 68.4% vs. 95.0% reported "Sometimes/Never").
* **Extreme Data Missingness in Clinical and Behavioral Variables:** In Table 2, baseline CD4 counts and viral loads are reported for only $n=23$ of 110 recruited partners (79% missing). In Table 3, substance use variables (methamphetamine, inhaled nitrites, GHB, cocaine, Ketamine) are missing for 89 to 91 of the 119 recruited partners ($>75\%$ missingness), rendering the behavioral comparisons across $n=10$ vs. $n=20$ respondents statistically uninformative and highly vulnerable to non-response bias.
* **Severe Ascertainment Bias and Reverse Causality in the 30-Day Window:** Over 81% (467/574) of AEH index cases failed to recruit any testable partner, and index cases who recruited partners were nearly twice as likely to be in acute (Fiebig I–II) infection (43% vs. 25.1%, $p=0.001$). The finding that partners enrolled within $\le 30$ days of index screening were more likely to be genetically linked ($74\%$ vs. $38\%$, $p<0.01$) is treated as a causal effect of rapid partner services delivery. In reality, it is heavily confounded by partnership type: index cases in ongoing, primary/main partnerships (who have the highest transmission probability) can immediately notify and bring their partner to the clinic within days, whereas anonymous or casual contacts take longer to locate and are less likely to be the transmitting source.

---

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim:** *Recruiting sexual partners of AEH index cases identifies a very high prevalence of undiagnosed HIV (32.8%) and AEH (11.8%).* **[Well Supported]** — Despite low overall index participation (18.6%), the diagnostic yield among the 119 tested partners is high and well documented by clinical staging and serology.
* **Claim:** *Providing partner services within 30 days increases the yield of newly diagnosed and genetically linked partners.* **[Overstated / Confounded]** — The observational association between time-to-referral ($\le 30$ vs. $>30$ days) and genetic linkage reflects partner accessibility and relationship concurrency rather than an intervention effect of rapid contact tracing.

---

### 4. Reproducibility & Data Completeness
* **Data and Sequence Availability:** No GenBank accession numbers, anonymized partner-network edge lists, or statistical analysis scripts are provided.
* **Reporting Quality:** Multiple table-text discrepancies and missing sample denominators across Tables 1–3 require thorough forensic correction before publication.
