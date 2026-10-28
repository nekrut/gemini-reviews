# Review of PMC7077245 (PMID:31991541)

**Manuscript Title:** Return of the Coronavirus: 2019-nCoV  
**Authors:** Gralinski LE, Menachery VD.  
**Journal / Preprint:** *Viruses* (2020; `PMC7077245` / `PMID:31991541` / `10.3390/v12020135`)  
**Calibration Study Cohort:** Cohort A — Known Invalid / Refuted (`A36` | Double-Blinded as `ANON_195`)  
**Overall Score:** **6.7 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 2.1/3.5 | Claims: 1.7/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.3/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript is an early-outbreak perspective and rapid synthesis written as of January 24, 2020, examining the emergence of the novel group 2B betacoronavirus (2019-nCoV / SARS-CoV-2) in Wuhan, China. Drawing on initial public health dispatches, GISAID genome releases (through mid-January 2020), and comparative coronavirus biology from SARS-CoV and MERS-CoV, the authors summarize the clinical timeline (870 confirmed cases and 26 deaths across 25 Chinese provinces plus 19 exported cases in 10 countries as of January 24, 2020), zoonotic wet-market origins versus human-to-human transmission, age and comorbidity risk factors, whole-genome and protein-level sequence identity (~80% nucleotide identity to SARS-CoV; ~90% amino acid identity in Nucleocapsid; ~75% in Spike and 73% in the receptor-binding domain [RBD] with 8 of 14 human ACE2 contact residues conserved), requirements to fulfill Rivers' modified Koch's postulates in small animal and non-human primate models, healthcare worker and superspreading risks, and the role of rapid open sequence sharing.

As a real-time virological commentary written within three weeks of pathogen identification, the manuscript provides a well-informed comparative synthesis of group 2B coronavirus receptor usage (human, bat, civet, and swine ACE2 vs. non-permissive mouse Ace2), serology caveats, and animal modeling challenges. However, it contains several quantitative, factual, and editorial errors that require correction: (1) misstating both the name and nucleotide sequence identity of the closest bat coronavirus relative reported by Zhou et al. [ref. 30] as *"RaTG3, with 92% sequence identity"* instead of **RaTG13** with **96.2%** identity; (2) inferring that 2019-nCoV *"appears to be less virulent at this point"* than SARS-CoV (10% CFR) based on a crude division of cumulative deaths by confirmed cases (26/870 = 3.0%) during exponential epidemic growth without accounting for right-censoring (onset-to-death lag) or under-ascertainment; (3) omitting accession numbers or methods for the sequence identity numbers reported in Section 4; and (4) multiple typographical errors in database names (`"GSAID"` instead of `"GISAID"`) and prose.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Structural modeling, pseudotyping, and receptor-usage data indicate that 2019-nCoV utilizes human ACE2 (as well as bat, civet, and swine ACE2, but not mouse Ace2) via conserved Spike RBD residues (Section 4–5): [Well Supported].**  
  The authors synthesize sequence conservation across the SARS-CoV RBD (73% identity across residues 318–518, falling between non-ACE2-binding HKU3-4 [62.7%] and ACE2-binding rSHC014 [80.8%], with 8/14 direct contact residues conserved) alongside early functional preprints (refs. 30, 35, 36). Their prediction that non-permissive mouse Ace2 will necessitate transgenic human ACE2 mice or mouse-adapted viral passaging to fulfill Koch's postulates is biologically sound.

* **Epidemiological expansion beyond the Huanan Seafood Market and healthcare worker infections indicate active human-to-human transmission and potential superspreading (Sections 1, 2, 6): [Well Supported].**  
  The synthesis of exported travel cases lacking market exposure, family clusters, and healthcare worker infections accurately distinguishes primary zoonotic spillover from secondary human-to-human transmission.

* **2019-nCoV shares "92% sequence identity" with bat coronavirus "RaTG3" (Section 4, line 42): [Methodologically Flawed].**  
  Line 42 states: *"A recent report has subsequently identified a bat CoV sequence, RaTG3, with 92% sequence identity with the novel virus which argues for bat origins for the 2019-nCoV [ 30 ]."* In reference 30 (Zhou et al., 2020), the bat coronavirus strain is **RaTG13** (not RaTG3) and shares **96.2%** whole-genome nucleotide identity (not 92%) with 2019-nCoV.

* **Compared to SARS-CoV (10% mortality) and MERS-CoV (35% mortality), 2019-nCoV appears to be less virulent except in the elderly and comorbid (Section 1, line 23): [Fragile].**  
  Comparing a mid-outbreak crude case fatality ratio (26 deaths / 870 cases = 3.0% on January 24, when 736 of the 870 cases had been diagnosed within the preceding 5 days and 44 of 170 hospitalized Wuhan patients were still in serious or critical condition) against the final post-epidemic CFR of SARS-CoV (10%) ignores right-censoring due to the 2–4 week lag from symptom onset to death, as well as evolving testing denominators.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct the Bat Coronavirus Strain Name (RaTG13) and Sequence Identity (96.2%)
* **WHY:** Reporting the closest known relative of 2019-nCoV as `"RaTG3"` with `"92% sequence identity"` (line 42) misstates a primary virological fact from the cited study [ref. 30].
* **WHAT & HOW:** In Section 4 (line 42), change *"identified a bat CoV sequence, RaTG3, with 92% sequence identity"* to *"identified a bat CoV sequence, RaTG13 (isolated from Rhinolophus affinis), with 96.2% whole-genome nucleotide sequence identity"*.

#### 2. Qualify Early Case Fatality Comparisons for Right-Censoring and Ascertainment Bias
* **WHY:** During rapid exponential growth (cases jumping from 62 on Jan 17 to 198 on Jan 19 and 870 on Jan 24), most active cases have not yet resolved to recovery or death. Dividing current deaths by current cases underestimates the closed-cohort case fatality risk, while under-detection of mild/asymptomatic infections biases it upward.
* **WHAT & HOW:** In Section 1 (line 23), revise *"the 2019-nCoV appears to be less virulent at this point"* to note that while the crude ratio of reported deaths to confirmed cases (~3%) is lower than the final case fatality rates of SARS-CoV (~10%) and MERS-CoV (~35%), accurate virulence estimation requires accounting for the clinical lag between symptom onset and death among currently hospitalized patients as well as the denominator of mild/asymptomatic infections.

#### 3. Provide Accession Numbers and Alignment Boundaries for the Comparative Sequence Analysis
* **WHY:** In Section 4 (lines 42–46), the authors report original sequence comparisons (e.g., ~90% N protein amino acid identity, ~75% whole-Spike identity, 73% RBD identity across SARS-CoV residues 318–518, and 8/14 conserved contact residues), but do not list the exact GISAID/GenBank accession numbers or alignment tool used.
* **WHAT & HOW:** Add the GenBank/GISAID accession numbers for the compared reference genomes (e.g., 2019-nCoV `Wuhan-Hu-1` `MN908947.3` / `EPI_ISL_402125`, SARS-CoV `Urbani` `AY278741`, `ZC45` `MG772933`, `ZXC21` `MG772934`, `WIV1` `KF367457`, `SHC014` `KC881005`, `HKU3-4` `GQ153543`) in Section 4 so readers can reproduce the exact residue mappings.

#### 4. Technical and Editorial Cleanup
* **WHY:** Several typographical errors and incomplete sentences appear across the text.
* **WHAT & HOW:**
  * **Line 23 (twice):** Change `"GSAID database"` to `"GISAID database"`.
  * **Line 23:** Change `"another exported cases to South Korea"` to `"another exported case in South Korea"`.
  * **Line 44:** Change `"insights about susceptibly"` to `"insights about susceptibility"`.
  * **Line 46:** Change `"although its affinity m be reduced"` to `"although its affinity may be reduced"`, and change `"another rapid report links demonstrates"` to `"another rapid report demonstrates"`.
  * **Line 53:** Add a period after *"mouse Ace2 was not permissive for 2019-nCoV infection."* before *"Dissemination"*.
  * **Line 58:** Change `"infection of health care works"` to `"infection of health care workers"`.
  * **Line 67:** Change `"entioned on ProMED Mail"` to `"mentioned on ProMED Mail"`.
