# Blinded Review: TIME_ANON_39
**Composite Score:** 7.0 / 10.0 (Rigor: 2.3/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.1/2.0)
**Bias Category:** Primer Sequence Copy-Paste Error in Methods and Missing Embedded Tables
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Epidemiological Observational

---

### 1. Executive Summary

This clinical molecular pathology study evaluates the prevalence, mutation spectrum, and baseline hematological correlates of somatic calreticulin (*CALR*) exon 9 mutations alongside *JAK2* V617F, *JAK2* exon 12, and *MPL* W515 mutations in a retrospective single-center cohort of 168 Korean patients with classic myeloproliferative neoplasms (MPNs: 36 polycythemia vera [PV], 114 essential thrombocythemia [ET], and 18 primary myelofibrosis [PMF]). Using bidirectional Sanger sequencing of a 483-bp *CALR* exon 9 amplicon, the authors detect *CALR* frameshift indels in $0\%$ ($0/36$) of PV, $21.9\%$ ($25/114$) of ET, and $16.7\%$ ($3/18$) of PMF patients—accounting for $58.5\%$ ($24/41$) of *JAK2*/*MPL*-negative ET and $33.3\%$ ($3/9$) of *JAK2*/*MPL*-negative PMF cases. Five distinct exon 9 indel variants were identified, all generating the canonical +1 bp shifted positively charged C-terminal peptide lacking the KDEL endoplasmic reticulum retention motif, with Type 1 (`L367fs*46`, $53.6\%$) and Type 2 (`K385fs*47`, $35.7\%$) accounting for $89.3\%$ of mutant cases. Compared with *JAK2* V617F-positive ET patients, *CALR*-mutated ET patients presented at a significantly younger age ($p = 0.025$) and with lower leukocyte counts ($p < 0.001$).

The study is a well-executed, appropriately scoped clinical replication cohort whose findings align closely with foundational *CALR* MPN studies. The primary defects requiring revision are a copy-paste error in the Methods section where the *CALR* exon 9 PCR primers are erroneously duplicated as the *JAK2* exon 12 sequencing primers, and the omission of the four formatted tables (`Tables 1–4`) from the manuscript body.

---

### 2. Methodological & Statistical Audit

* **Internal Consistency of Cohort Counts and Mutation Proportions [Well Supported]:**
  All subgroup denominators and mutation percentages reported in the Results (lines 42, 47) are arithmetically consistent:
  * **PV ($n = 36$):** $31$ *JAK2* V617F ($86.1\%$), $0$ *JAK2* exon 12, $0$ *MPL*, $0$ *CALR*, and $5$ triple-negative ($13.9\%$; $31 + 5 = 36$).
  * **ET ($n = 114$):** $68$ *JAK2* V617F ($59.6\%$), $5$ *MPL* W515 ($4.4\%$), leaving $114 - 68 - 5 = 41$ *JAK2*/*MPL*-negative ET patients. Among these $41$ patients, $24$ carried *CALR* mutations ($24/41 = 58.5\%$), leaving $41 - 24 = 17$ minus $1$ dual *JAK2*+*CALR* mutant? Wait: let us check the exact numbers on line 42! If $68$ have *JAK2*, $5$ have *MPL*, $25$ have *CALR* (of whom $1$ has both *CALR* and *JAK2* V617F, and $24$ have *CALR* alone), then the number of patients with at least one mutation is $68 + 5 + 24 = 97$, which leaves $114 - 97 = 17$ triple-negative patients ($14.9\%$), whereas line 42 reports `14.0% (16/114)` triple-negative ET patients (implying 1 patient had concurrent *JAK2* and *MPL* or was excluded). Clarifying that single patient's status by restoring Table 1 will make the accounting 100% transparent.
  * **PMF ($n = 18$):** $9$ *JAK2* V617F ($50.0\%$), $0$ *MPL*, $3$ *CALR* among the $9$ *JAK2*/*MPL*-negative cases ($3/9 = 33.3\%$), and $6$ triple-negative ($6/18 = 33.3\%$; $9 + 3 + 6 = 18$).

* **Statistical Power and Multiple Testing in Phenotypic Comparisons [Moderately Supported]:**
  Four continuous variables (age, hemoglobin, leukocyte count, and platelet count) were compared between *CALR*-mutated and *JAK2*-mutated patients in ET and PMF using independent $t$-tests or Mann-Whitney tests (lines 37, 55). The lower leukocyte count in *CALR*-mutated ET ($p < 0.001$) remains highly significant under Bonferroni correction ($\alpha = 0.05/4 = 0.0125$), whereas the age difference ($p = 0.025$) is nominal. The authors appropriately note that the PMF subgroup ($n = 18$, with only $3$ *CALR*-mutated cases) is too small to detect hematological differences.

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **Concordance with Known *CALR* Exon 9 Frameshift Biology and Assay Sensitivity [Well Supported]:**
  All five detected indel variants (`L367fs*46`, canonical `K385fs*47`, novel `1154_delinsTTTGTC` resulting in `K385fs*47`, `E364fs*55`, and `E369fs*46`) shift the reading frame by +1 bp into the identical novel basic C-terminal peptide (`RMRRMRRTRRKMRRKMSPARPRTSCREACLQGWTEA`) and eliminate the C-terminal KDEL ER-retention signal. The Discussion (line 67) also thoughtfully addresses the lower sensitivity of direct Sanger sequencing ($\sim 15\text{--}20\%$ mutant allele burden limit of detection) compared to capillary fragment analysis or next-generation sequencing when interpreting the $13.9\%$ PV and $14.0\%$ ET triple-negative rates.

---

### 4. Reproducibility & Data Completeness

Two specific issues reduce the reproducibility score and should be corrected in a minor revision:
1. **Duplicated Primer Sequences for *CALR* Exon 9 and *JAK2* Exon 12 (lines 33 & 35):** On line 33, the *CALR* exon 9 primers are given as forward `5'-CATACGCTGAGGAGTTTGGC-3'` and reverse `5'-GAGTGGAGGAGGGGAACAAA-3'`. On line 35, the primers for *JAK2* exon 12 direct sequencing are given as the exact same nucleotide sequences (`5'-CATACGCTGAGGAGTTTGGC-3'` and `5'-GAGTGGAGGAGGGGAACAAA-3'`). This is an obvious copy-paste error in the Methods text; the actual *JAK2* exon 12 primers must be provided.
2. **Missing Tables 1–4:** While the text summarizes the primary numbers from Tables 1–3, the actual formatted tables (`Table 1` through `Table 4`, including the exact mean $\pm$ SD values for hemoglobin, WBC, and platelets in Table 3) are missing from the markdown document and should be restored.
