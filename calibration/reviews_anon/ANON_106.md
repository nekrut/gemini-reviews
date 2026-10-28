# Review of ANON_106

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.7 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 2.1/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study protocol describes the Year 1 (2018–2019 season) architecture of the Seattle Flu Study (SFS), a metropolitan-scale multi-armed respiratory pathogen surveillance platform across five counties in Washington State. The design integrates six sampling streams: (1) community cross-sectional kiosks at public venues enrolling individuals with $\ge 2$ acute respiratory illness (ARI) symptoms, (2) clinical cross-sectional residual swabs from four regional hospitals, (3) a prospective inpatient cohort sampled longitudinally for up to 7 days, (4) a prospective weekly childcare cohort, (5) active ambulatory clinical surveillance via the US Influenza Vaccine Effectiveness (VE) Network, and (6) high-touch surface and bioaerosol environmental sampling. Specimens are screened via a TaqMan OpenArray multiplex RT-PCR assay targeting 15 viral and 3 bacterial pathogens, with influenza-positive samples ($C_{RT}$-pooled in batches of 24) undergoing Twist hybrid-capture Illumina whole-genome sequencing, Nextstrain phylodynamic analysis, and generalized additive mixed modeling (GAMM) for geospatial mapping. Aggregate data and code are disseminated via the study website (`www.seattleflu.org`).

The protocol outlines a practical, scalable molecular epidemiology infrastructure that bridges community-dwelling non-care-seekers and hospital populations, and the authors candidly discuss key Year 1 limitations (convenience sampling, demographic under-representation, and exclusion of asymptomatic infections). However, as a formal methodological protocol, it has three notable gaps: (1) the "Sample size" section provides no target sample sizes, expected positivity rates, or statistical power/precision calculations for any study arm or phylogenetic/spatial objective; (2) the Statistical Methods section does not specify how data from arms with radically different inclusion criteria and care-seeking probabilities are stratified or weighted when estimating community prevalence and geospatial incidence maps; and (3) holding clinical residual specimens at $4^\circ\text{C}$ for 3–7 days prior to freezing introduces pre-analytical RNA degradation that confounds viral load ($C_{RT}$) comparisons between clinical and community arms. These protocol specifications and minor citation errors can be addressed directly in the text.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Integrating community kiosk sampling with ambulatory and inpatient residual swabs captures respiratory infections across the care-seeking spectrum for molecular surveillance: [Well Supported].**  
  The multi-arm structure, standardized mid-nasal Copan flocked swabbing, TaqMan OpenArray screening (showing $96\%$ concordance for influenza and $92\%$ for RSV against clinical Cepheid/BioFire assays), and $C_{RT}$-matched hybrid-capture sequencing form a coherent laboratory and epidemiological workflow.

* **Geospatial generalized additive mixed models (GAMMs) and Nextstrain phylogenetics applied across the study arms can map community-wide prevalence and regional transmission dynamics: [Moderately Supported].**  
  In the Statistical Methods (lines 262–264), pathogen prevalence is defined simply as cases detected divided by tested episodes, and geospatial incidence maps are estimated via GAMMs with spatial, temporal, and age effects. However, symptom triggers and sampling denominators differ sharply across arms: community kiosk enrollees require any two symptoms from Table 1 (which permits non-respiratory pairs such as headache plus fatigue, or nausea plus diarrhoea), US Influenza VE enrollees require a cough of $<8$ days' duration, and clinical residual specimens reflect clinician testing discretion. Pooling these arms into spatial GAMMs or phylogeographic reconstructions without arm-specific offsets, symptom-profile adjustment, or census-tract sampling weights risks confounding true viral incidence with kiosk placement and hospital catchment areas.

* **Viral load ($C_{RT}$) and molecular markers of nasal swab efficiency can be compared across clinical disease characteristics and single vs. co-infections (Secondary Outcomes 11–12): [Fragile].**  
  Under Specimen Collection Methods (line 216), residual clinical specimens are held at $4^\circ\text{C}$ at hospital laboratories and transported within 3–7 days before $-80^\circ\text{C}$ storage, whereas prospective community and clinical cohort mid-nasal swabs are collected directly in UTM for research processing. Furthermore, clinical cross-sectional specimens include heterogeneous sample types ("respiratory specimens of all types," line 99, e.g., nasopharyngeal vs. mid-nasal swabs, washes, or BAL). Unadjusted comparisons of $C_{RT}$ values between severe hospitalized patients (residual swabs) and mild community cases are therefore confounded by collection anatomical site and 3–7 day hold-time RNA decay.

* **The Sample Size section establishes adequate statistical power for the primary and secondary outcomes: [Methodologically Flawed].**  
  The "Sample size" section (lines 136–138) consists of two sentences noting that 6,953 positive influenza tests were reported in Washington State in 2017–2018. It provides no target enrollment numbers per arm, no expected influenza positivity rates in community kiosks vs. hospitals, and no minimum detectable risk ratios or phylogenetic sampling fractions.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Add Target Enrollment Numbers and Precision/Power Justifications to the Sample Size Section
* **WHY:** A study protocol requires quantitative sample size targets and precision bounds for its primary and secondary statistical endpoints.
* **WHAT:** Expand the "Sample size" section (lines 136–138) to state the planned (or achieved Year 1) sample sizes across each of the six study arms, expected influenza/ARI positivity rates, and resulting 95% confidence interval widths or minimum detectable risk ratios (RRs).
* **HOW:** Specify target specimen counts for (i) community cross-sectional kiosks, (ii) clinical residual swabs, (iii) prospective inpatient cohort, (iv) childcare cohort, (v) active clinical surveillance, and (vi) environmental samples. Using Poisson/negative binomial regression power formulas at $\alpha = 0.05$ (two-sided), report the minimum detectable RR for key subgroup comparisons (e.g., vaccinated vs. unvaccinated, shelter vs. campus sites) and the expected proportion of Washington State influenza cases captured for Nextstrain phylogenetic reconstruction.

#### 2. Account for Heterogeneous Ascertainment and Denominators in Geospatial GAMMs and Prevalence Estimates
* **WHY:** Combining convenience kiosk samples (triggered by any two symptoms in Table 1, including non-specific pairs like fatigue + headache) with clinician-ordered hospital swabs will bias spatial incidence maps toward hospital catchment areas and high-traffic kiosk locations.
* **WHAT:** Specify in the Statistical Methods (lines 260–266) how study arm, symptom syndrome definition (e.g., CDC Influenza-Like Illness [fever + cough/sore throat] vs. broad $\ge 2$ symptoms), and census-tract sampling effort are parameterized in the GAMMs and prevalence regressions.
* **HOW:** Include study arm and symptom category as fixed covariates (and recruitment site as a structured random effect) in the Poisson/negative binomial and GAMM equations, and describe post-stratification or inverse-probability weighting by home census tract demographics (age, race/ethnicity, income) when generating regional incidence maps.

#### 3. Control for Pre-Analytical Hold Time, Swab Type, and Host RNase P in Viral Load ($C_{RT}$) Analyses
* **WHY:** Clinical residual specimens are held at $4^\circ\text{C}$ for 3–7 days and span diverse specimen types (line 99 and 216), which degrades viral RNA and alters $C_{RT}$ relative to freshly frozen mid-nasal swabs.
* **WHAT:** Adjust all viral load regressions (Secondary Outcomes 11–12, lines 175–177) for specimen collection-to-freezing delay (days at $4^\circ\text{C}$), anatomical swab type, days since symptom onset, and endogenous human housekeeping gene $C_{RT}$ (e.g., RNase P on the OpenArray panel).
* **HOW:** Explicitly name the human cellular control target assayed on the OpenArray platform in the Laboratory Methods (line 229), define normalized viral load as $\Delta C_{RT} = C_{RT,\text{virus}} - C_{RT,\text{host}}$, and include collection-to-freezer time and specimen type as covariates in the viral kinetics and severity models (line 266).

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Discrepancies in the number of study arms and broken reference-manager citations detract from protocol clarity.
* **WHAT & HOW:**
  * **Study Design (line 66) vs. Study Arms (lines 95–108) & Figure 1:** Line 66 lists five study arms, omitting the sixth arm ("The environmental sampling arm," line 107). Update line 66 to list all six arms, and note in the Figure 1 caption that both the active clinical surveillance and environmental sampling arms are omitted from the participant flowchart.
  * **Table 2 Footnote (line 257):** The footnote for `*Enterovirus` cites references `1–3` (which are the 1918 influenza pandemic mortality papers cited in the Introduction, line 41). Replace `1–3` with the correct enterovirus assay/taxonomy reference.
  * **Figure 1 Caption (line 92):** Fix the duplicated, garbled reference-manager text `"For methods, see Prevention USCfDCa. FluView and Prevention USCfDCa. FluView and Fong et al . 13 14"` to `"For methods, see US Centers for Disease Control and Prevention (FluView) and Fong et al. [13, 14]."`
