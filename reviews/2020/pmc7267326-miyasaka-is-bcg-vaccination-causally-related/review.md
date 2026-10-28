# Review of PMC7267326 (PMID:32379923)

**Manuscript Title:** Is BCG vaccination causally related to reduced COVID-19 mortality?  
**Authors:** Miyasaka M.  
**Journal / Preprint:** *EMBO Mol Med* (2020; `PMC7267326` / `PMID:32379923` / `10.15252/emmm.202012661`)  
**Calibration Study Cohort:** Cohort A — Known Invalid / Refuted (`A43` | Double-Blinded as `ANON_140`)  
* **Overall Score:** **4.2 / 10.0** (Flawed / Overstated)
* **Score Breakdown:** Rigor: 1.1/3.5 | Claims: 1.0/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.0/2.0
* **Synthesis:** This commentary/opinion piece examines cross-national differences in cumulative COVID-19 deaths per million (as of May 6, 2020 from Worldometer across 17 selected countries in Table 1) and proposes the hypothesis that "early" Bacillus Calmette-Guérin (BCG) vaccine substrains (such as BCG Japan, BCG Russia, and BCG Brazil/Moreau, which retain MPB64/MPB70/MPB83 antigens, cell-wall methoxymycolate, and higher viable bacterial counts per dose) confer stronger non-specific trained immunity against SARS-CoV-2 than "late" BCG substrains (such as BCG Denmark, Pasteur, and Glaxo). While the review of known biochemical, genomic (RD1/RD2 deletion), and viable-colony differences between early and late BCG substrains is informative and the author appropriately acknowledges counterexamples (e.g., Finland and Australia discontinued universal BCG decades ago yet had very low May 2020 COVID-19 mortality), the empirical argument rests on a severely cherry-picked 17-country table without statistical testing or confounding control, mischaracterizes an *in silico* sequence-similarity preprint as a "laboratory analysis" showing specific anti-SARS-CoV-2 envelope immunity, and makes a flawed clinical-trial sample-size calculation containing factual date errors (`March 4, 2020` instead of `May 2020`).

---

## 2. Claim-by-Claim Evaluation & Empirical Audit

* **Claim 1:** Early BCG vaccine substrains (BCG Japan, Russia, Moreau/Brazil, Sweden) differ biochemically and genetically from late substrains (BCG Denmark, Pasteur, Glaxo)—retaining region-of-difference 2 (RD2) proteins MPB64, MPB70, and MPB83, producing cell-wall $\alpha$-, keto-, and methoxymycolates, containing higher viable colony counts per ampoule (`27.5 × 10^6/mL` for BCG Japan vs. `3.0–6.2 × 10^6/mL` for Denmark/Pasteur/Glaxo in 1979 WHO data), and inducing stronger Th1 cytokine responses (IFN-$\gamma$, TNF-$\alpha$, IL-2) in human neonates.
  * **Support Level:** **[Well Supported]**
  * **Audit Trail:** Discussion of BCG substrain genealogy and microbiology (pages 3–6, citing references 6–12).
  * **Assessment:** The microbiological, biochemical, and neonatal immunogenicity differences between pre-1927 ("early") and post-1931 ("late") BCG substrains are well-established in the mycobacterial vaccine literature and accurately summarized here.

* **Claim 2:** Cross-national COVID-19 mortality data as of May 6, 2020 (Table 1) suggest that countries administering "early" BCG strains (Japan, South Korea, Taiwan, China, Russia, India, Iraq, Turkey) have lower COVID-19 mortality than countries administering "late" BCG strains (Spain, France, UK, Germany, Iran) or no universal BCG (Italy, USA), supporting a hypothesis that early BCG strains protect against COVID-19 mortality.
  * **Support Level:** **[Methodologically Flawed]**
  * **Audit Trail:** Table 1 (17 selected countries as of May 6, 2020 from Worldometer) and text on pages 3–5.
  * **Assessment:** Table 1 suffers from severe selection bias (cherry-picking 17 countries out of >180 countries worldwide), absence of any statistical hypothesis test, and unadjusted ecological confounding:
    1. **Omission of High-Mortality Countries Using "Early" BCG Strains:** In the text (page 4), the author explicitly classifies **BCG Brazil (Moreau)**, **BCG Japan**, and **BCG Russia** as the quintessential "early" BCG strains (`"early strains include BCG Japan, BCG Russia, BCG Brazil, and BCG Sweden"`). Yet Table 1 completely omits Brazil, Peru, Ecuador, Mexico, and Colombia—countries with long-standing mandatory universal neonatal vaccination using BCG Moreau or BCG Japan/Russia that were already experiencing severe COVID-19 mortality in May 2020 (and went on to suffer among the highest per-capita COVID-19 death tolls in the world). Even within Table 1, Russia and India were simply at an earlier phase of their epidemic curves on May 6, 2020 (`9` and `1` deaths/million, respectively) before experiencing massive subsequent mortality waves.
    2. **Confounding by Epidemic Arrival Time, Testing/Death Ascertainment, and Border Measures:** Comparing raw Worldometer deaths per million on May 6, 2020 between East Asian countries that implemented strict quarantine/contact tracing in January–February 2020 (Taiwan, South Korea, Japan, China), conflict-affected or resource-limited states with severe death under-ascertainment (Iraq at `2/million`), and Western European epicenters (Spain, Italy, UK, France) confounds epidemic timing, surveillance completeness, age demographics, and non-pharmaceutical interventions with historical vaccine procurement.
    3. **Internal Contradictions:** As the author acknowledges on page 5, Finland (`44/million`) and Australia (`4/million`) discontinued universal BCG vaccination (`2006` and `mid-1980s`), meaning individuals under 14 or under 35 were unvaccinated and older cohorts received Glaxo/Copenhagen strains, yet both had far lower mortality than neighboring Sweden or Western Europe.

* **Claim 3:** *"In 2020, laboratory analyses found that BCG vaccination induces specific immunity against the envelope protein of SARS CoV-2 [4]."*
  * **Support Level:** **[Overstated]**
  * **Audit Trail:** Page 3, line 31, citing reference 4 (`Lyons-Weiler J, 2020, Preprint, ResearchGate`).
  * **Assessment:** Reference 4 was an unrefereed *in silico* sequence-alignment note looking for short amino-acid homologies (`BLAST`) between *Mycobacterium* proteins and the SARS-CoV-2 envelope protein; it contained **zero** wet-laboratory experiments, serological assays, T-cell assays, or immunological measurements showing that BCG vaccination induces specific immunity against the SARS-CoV-2 envelope protein. Describing an unvalidated *in silico* homology preprint as *"laboratory analyses found that BCG vaccination induces specific immunity"* is factually inaccurate.

* **Claim 4:** Ongoing randomized clinical trials (RCTs) of BCG vaccination in $>10,000$ healthcare workers cannot provide a clear answer because *"<10 of 1,000 individuals are expected to become infected with SARS-CoV-2 even in endemic countries such as Spain, Italy, and France (with incidence of 5,285, 3,485, and 2,584 cases per million population, respectively, as of March 4, 2020)."*
  * **Support Level:** **[Methodologically Flawed]**
  * **Audit Trail:** Concluding paragraph (page 6, lines 124–132).
  * **Assessment:** This argument contains three major epidemiological and factual errors:
    1. **Factual Date Error (`March 4, 2020` vs. `May 2020`):** On March 4, 2020, Spain had ~200 total confirmed cases (~4 per million) and France had ~285 total confirmed cases (~4 per million). The cumulative incidence figures cited by the author (`5,285`, `3,485`, and `2,584` cases per million for Spain, Italy, and France) are the Worldometer figures from **May 2020** (matching the May 6, 2020 date of Table 1), not March 4, 2020.
    2. **Conflation of Early-2020 General-Population Confirmed PCR Cases with True Infection Attack Rates:** In spring 2020 in Spain, Italy, and France, PCR testing was largely restricted to hospitalized patients; seroprevalence surveys (`ENE-COVID` in Spain) showed that true SARS-CoV-2 infection prevalence by May 2020 was ~5% (`50 per 1,000`), roughly 10-fold higher than PCR-confirmed case counts.
    3. **Healthcare Worker vs. General Population Risk:** Front-line healthcare workers enrolled in prospective RCTs over 6–12 months of follow-up experienced substantially higher cumulative SARS-CoV-2 exposure and frequent PCR/serological testing compared to a 2-month general-population snapshot, making $N = 10,000$ healthcare-worker RCTs well powered to detect clinically meaningful reductions in COVID-19 incidence or severity.

---

## 3. Technical & Methodological Deep-Dive

### 1. Eliminating Selection Bias in Cross-Country BCG Substrain Comparisons
When evaluating whether early vs. late BCG substrains correlate with national COVID-19 mortality, assembling an ad hoc 17-country table creates severe confirmation bias. A methodologically valid ecological test requires:
1. **Complete Global Inclusion:** Including all countries in the BCG World Atlas with documented substrain histories (especially Latin American nations using BCG Moreau/Brazil and BCG Japan, Eastern European nations using BCG Russia/Bulgaria, and African/Asian nations) rather than selecting 17 illustrative countries.
2. **Alignment by Epidemic Time and Multivariable Adjustment:** Aligning countries by time since a threshold death rate (e.g., 1 death per million) and adjusting in a multivariable regression for median population age, fraction of population $\ge 65$ years, GDP per capita, excess mortality / testing rate, and timing of border/lockdown interventions. When these factors and subsequent 2020–2021 waves in Russia, Brazil, Peru, India, and Eastern Europe are included, the apparent advantage of early-substrain countries disappears.

### 2. Specific Corrections Required in the Text
* **Page 3, Line 31:** Remove or correct the statement that *"laboratory analyses found that BCG vaccination induces specific immunity against the envelope protein of SARS CoV-2 [4]"*, as Reference 4 is a purely computational sequence comparison preprint with no laboratory immunology data.
* **Page 6, Line 130:** Correct *"as of March 4, 2020"* to *"as of May 6, 2020"*, and revise the clinical trial power calculation to account for cumulative prospective attack rates among healthcare workers rather than 2-month general-population PCR-confirmed case counts.
