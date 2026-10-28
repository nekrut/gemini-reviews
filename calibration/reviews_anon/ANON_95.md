# Review of ANON_95

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.9 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.8/3.5 | Claims: 1.4/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.2/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This short report describes a retrospective SARS-CoV-2 RT-PCR investigation of archived nasopharyngeal swabs stored at $-80^\circ\text{C}$ from intensive care unit (ICU) patients admitted for influenza-like illness (ILI) between 2 December 2019 and 16 January 2020 at a hospital north of Paris, France. Out of 58 ICU admissions for ILI during this window, 14 patients met the inclusion criteria of fever/respiratory symptoms, bilateral pulmonary ground-glass opacities on chest CT, and a negative admission multiplex respiratory PCR. Retrospective testing performed between 6 and 9 April 2020 using the Charité E-gene RT-PCR assay and confirmed with the GeneFinder COVID-19 Plus RealAmp Kit (`RdRp`, `E`, `N`, and cellular `RNase P`) identified one positive sample from a 42-year-old male admitted on 27 December 2019 (symptom onset 23 December 2019) with no travel history since August 2019. Clinical metadata for all 14 tested patients are tabulated in Table 1.

Retrospectively screening banked ICU respiratory specimens from December 2019–January 2020 is a direct and practical approach to investigating early cryptic SARS-CoV-2 circulation in Europe. However, because the entire claim of December 2019 community transmission in France rests on a single retrospective PCR positive ($1/14$) assayed in early April 2020—at the peak of the first Paris COVID-19 wave, when clinical laboratories were handling large volumes of high-titer SARS-CoV-2 specimens—extraordinary contamination controls and genomic verification are required. The manuscript does not report the quantitative cycle threshold ($C_t$) values for any target gene (`E`, `RdRp`, `N`, `RNase P`), does not clarify whether confirmation was performed via independent RNA re-extraction from an untouched primary sample tube, does not include viral genome sequencing or paired acute/convalescent serology to rule out laboratory cross-contamination, and overreaches in claiming that this single ICU case "strongly supports" specific population-level modeling assumptions about asymptomatic transmission rates. Providing exact $C_t$ values, independent re-extraction/sequencing data, or serological confirmation from the patient would substantially strengthen the report.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **A banked nasopharyngeal swab collected in late December 2019 from a 42-year-old ICU patient with haemoptysis, fever, lymphopenia, and bilateral ground-glass opacities tested positive on two SARS-CoV-2 RT-PCR assays: [Moderately Supported].**  
  The patient's clinical presentation (5 days of fever, cough, headache, haemoptysis, bilateral lower-lobe ground-glass opacities on CT, normal procalcitonin $0.21\ \mu\text{g/L}$, lymphopenia $0.89 \times 10^9\text{/L}$) and amplification on both the Charité E-gene assay (Figure 2) and the three-target GeneFinder assay (`RdRp`, `E`, `N`) are consistent with COVID-19. However, the retrospective RT-PCR runs were performed on 6–9 April 2020 during the height of the Paris epidemic surge. The manuscript omits the numerical $C_t$ values for both assays, does not specify whether the confirmatory GeneFinder test was run on the same RNA eluate or a fresh RNA extraction from a separate primary aliquot, and lacks viral sequencing or follow-up patient serology to definitively exclude amplicon or specimen cross-contamination during RNA extraction in April 2020.

* **SARS-CoV-2 was already spreading in the French population at the end of December 2019, and official statistics underestimate the true burden: [Fragile].**  
  While a confirmed autochthonous case on 27 December 2019 would imply local exposure in mid-December 2019, generalizing from $n = 1$ unsequenced positive specimen (out of 14 selected ICU patients at a single center) to broad population-wide community spread in December 2019 is fragile without phylogenetic placement or convalescent serology from the patient and his household contact (the child with prior ILI mentioned in Section 3, line 43).

* **The identification of this single ICU case "strongly supports" published estimates that 18–23% of SARS-CoV-2 infections are asymptomatic and 55% of infections are caused by undocumented cases: [Overstated].**  
  In the Discussion (line 87), the authors state: *"Two recent studies suggested that ~18–23% of patients infected with SARS-CoV-2 were asymptomatic [12] and that ~55% of infections were caused by unidentified infected persons [13]. The current results strongly support these two assumptions..."* Observing a single symptomatic ICU patient provides zero statistical information regarding the population asymptomatic fraction or the exact proportion of transmission attributable to undocumented infections.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Report Exact Quantitative $C_t$ Values and Clarify RNA Re-Extraction Procedures
* **WHY:** In Figure 2, only an unlabeled amplification curve (without y-axis fluorescence scale or numerical $C_t$ threshold line) is shown for the Charité E-gene assay, and no curves or $C_t$ values are shown for the confirmatory GeneFinder assay (`RdRp`, `E`, `N`, and `RNase P`). Evaluating whether the signal represents a robust viral load vs. a late-cycle ($C_t > 37$) trace contaminant requires exact $C_t$ values and knowledge of the extraction workflow.
* **WHAT:** Report the exact $C_t$ values for the patient sample and positive/negative controls across all targets in both assays, and detail the physical separation and extraction protocol.
* **HOW:** Add the numerical $C_t$ values for Charité `E` and GeneFinder `RdRp`, `E`, `N`, and `RNase P` to Section 3 and the Figure 2 legend. Explicitly state in Section 2.2 whether the confirmatory GeneFinder RT-PCR was performed on a second independent RNA extraction from the original frozen primary nasopharyngeal swab tube, how many negative extraction controls (blanks) were processed alongside the 14 banked samples on 6–9 April 2020, and whether the banked samples were extracted in a batch separate from acute April 2020 clinical specimens.

#### 2. Perform Viral Amplicon Sequencing or Convalescent Serological Confirmation
* **WHY:** Because RT-PCR was performed in April 2020, two independent lines of evidence available from the existing specimen and discharged patient can definitively rule out April 2020 laboratory contamination: (a) viral genome sequencing (showing an early basal clade A or B sequence rather than a derived March/April 2020 European B.1 lineage) and (b) convalescent anti-SARS-CoV-2 serology from Patient #5 (and his family).
* **WHAT:** Attempt targeted amplicon sequencing on the stored RNA/specimen and/or report follow-up SARS-CoV-2 IgG/neutralizing serology from Patient #5.
* **HOW:** Sequence the stored RNA eluate (or even the Sanger-sequenced RT-PCR amplicons if full-genome coverage is low due tohigh $C_t$) to verify viral sequence identity, and if patient consent permits, report a follow-up serological test from Patient #5. If neither is possible due to sample exhaustion or loss to follow-up, explicitly state this as a key limitation in the Discussion.

#### 3. Clarify the Admission Multiplex PCR Panel and Selection Criteria in Methods
* **WHY:** Section 2.1 (line 21) states that patients had *"a negative reverse transcription PCR (RT-PCR) performed at admission"*, and Table 1 lists Patient #5 as admitted on 27 December 2019 with symptom onset 5 days earlier (22 December 2019), yet line 43 states symptoms evolved "for 4 days." Readers need to know which respiratory viruses and bacteria were excluded at admission.
* **WHAT:** Specify the exact commercial multiplex respiratory PCR panel used at admission and reconcile the symptom duration (4 days in text vs. 5 days in Table 1).
* **HOW:** In Section 2.1, list the commercial name and viral/bacterial targets (e.g., Influenza A/B, RSV, rhinovirus, seasonal human coronaviruses OC43/229E/NL63/HKU1, *Mycoplasma pneumoniae*) of the admission multiplex PCR, and clarify in Section 3 and Table 1 whether the nasopharyngeal swab for Patient #5 was collected on 27 December 2019 (day 4 or day 5 of symptoms).

#### 4. Temper Population-Level Extrapolations in the Abstract and Discussion
* **WHY:** A single retrospective positive case cannot validate specific quantitative parameters (18–23% asymptomatic rate; 55% undocumented transmission share) from epidemiological compartmental models.
* **WHAT:** Revise the Abstract and Discussion to frame the finding as a single probable early case warranting broader multi-center biobank and serological verification.
* **HOW:** Replace *"The current results strongly support these two assumptions"* in the Discussion (line 87) with *"If confirmed across broader cohorts, early unrecognized circulation would be consistent with studies highlighting the role of undocumented infections in early viral spread [12, 13]."*

#### 5. Technical and Citation Fixes
* **WHY:** Figure 2 cites the wrong reference for the Charité RT-PCR protocol, and Figure 2's axes lack numerical labels.
* **WHAT & HOW:**
  1. **Citation mismatch in Figure 2 caption (line 38):** Change `"Result of Charité protocol RT-PCR assay [11]"` to `"[7]"` (Corman et al.; reference `[11]` is the French April 2020 case/death count).
  2. **Figure 2 axis labels:** Add cycle number (`0–45`) on the x-axis and $\Delta R_n$ fluorescence units plus the threshold line on the y-axis of Figure 2.
