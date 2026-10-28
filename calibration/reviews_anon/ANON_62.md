# Review of ANON_62

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **4.5 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.2/3.5 | Claims: 1.1/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.1/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This retrospective surveillance study screens 546 cats (376 household cats and 170 shelter cats) across 10 provinces in South Korea between April 2021 and March 2022 for SARS-CoV-2 infection using RT-qPCR on nasopharyngeal/oropharyngeal swabs and an anti-nucleocapsid (N) double-antigen ELISA on sera. The authors report a seroprevalence of 3.48% (`19/546`; `16/376 [4.26%]` in household cats and `3/170 [1.76%]` in shelter cats) and detect viral RNA in a single symptomatic household cat in Jeonbuk (`1/546 [0.18%]`, Case 17, `JBNU-cat`, sampled in February 2022 with Ct values of 25.32 for `ORF3a` and 25.18 for `N`). The virus from `JBNU-cat` was isolated in Vero E6 cells, sequenced on an Illumina iSeq 100 (`29,841 nt`, mean depth $14,783\times$), classified within Omicron sublineage `BA.1.1`, and deposited in GISAID (`EPI_ISL_16577826`).

While documenting a reverse-zoonotic SARS-CoV-2 Omicron `BA.1.1` infection and estimating baseline feline seroprevalence in South Korea provides useful One Health surveillance data, the manuscript contains substantial methodological omissions, internal contradictions, and biological misinterpretations. First, the study design is internally contradictory: the Introduction and Methods state that the 546 cats were "randomly selected from local animal hospitals and animal shelters," whereas the Discussion states that *all* 546 cats exhibited at least one COVID-19-related clinical sign such as fever ($>39.5\,^\circ\text{C}$) or cough. Second, Table 2 presents Plaque Reduction Neutralization Test (`PRNT`) titers for all 19 cats, but no PRNT protocol, virus strain, or neutralization threshold is described anywhere in the Materials and Methods. Third, the Discussion claims that spike mutations in `JBNU-cat` reflect "selective pressures exerted by the feline host environment" without distinguishing standard human `BA.1.1` lineage-defining mutations or Vero E6 passage adaptations from feline-specific changes, and erroneously states that Vero E6 (African green monkey) cells express the human ACE2 receptor and demonstrate the permissiveness of feline cells. These issues can be resolved through careful reanalysis of the sequence alignment against local human `BA.1.1` genomes, addition of the missing PRNT and qPCR standard-curve methods, and correction of the sampling and biological descriptions.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **SARS-CoV-2 seroprevalence was 3.48% (19/546) and active RT-qPCR prevalence was 0.18% (1/546) among randomly selected cats in South Korea between April 2021 and March 2022: [Fragile].**  
  Although the laboratory screening of 546 feline swabs and sera is straightforward, the epidemiological denominator is unclear because Section 2.1 states that the 546 cats were "randomly selected from local animal hospitals and animal shelters," whereas Section 4 states that *"Of the 546 cats included in the study, all exhibited at least one COVID-19-related clinical sign, such as fever (body temperature above 39.5 °C) and cough."* If inclusion required respiratory signs or fever, the cohort represents a symptomatic clinical convenience sample rather than a random sample, and prevalence estimates cannot be generalized to the general feline population. In addition, Table 2 reports raw `OD450` values (`0.5824` to `1.8163`) rather than the `S/P` percentages required by the IDvet ELISA kit cutoff ($\text{S/P} > 60\%$, Section 2.3), and the three seropositive animal-shelter cats (Cases 7, 13, and 14, two of unknown age) are inexplicably listed as having a "COVID-19 Patient Owner = Yes."

* **Isolation and genomic confirmation of an infectious SARS-CoV-2 Omicron `BA.1.1` strain (`JBNU-cat`) from a symptomatic household cat whose owner had COVID-19: [Well Supported].**  
  The primary swab from Case 17 had clear RT-qPCR amplification (`ORF3a` Ct = 25.321, `N` Ct = 25.182), yielded cytopathic effect and spike immunofluorescence across serial passages in Vero E6 cells (Figure 1, Table 3), and produced a high-coverage whole-genome sequence (`EPI_ISL_16577826`) clustering within Omicron `BA.1.1` alongside contemporary South Korean human isolates from early 2022 (Figure 2).

* **Spike protein mutations in the `JBNU-cat` isolate suggest selective pressures and viral adaptation within the feline host environment: [Overstated].**  
  Figure 3 compares the `JBNU-cat` spike NTD and RBD against generic `Hu-1`, `Delta`, and `Omicron` reference sequences without identifying any amino acid substitution that is unique to `JBNU-cat` relative to contemporaneous human `BA.1.1` genomes in South Korea. Furthermore, Section 2.5 states that viral RNA for sequencing was extracted from the *Vero E6 culture isolate* rather than directly from the primary clinical swab; Vero E6 propagation is well known to select for cell-culture adaptations in the spike protein. Without sequencing the primary feline swab or the owner's SARS-CoV-2 specimen, standard `BA.1.1` lineage mutations cannot be attributed to feline host adaptation.

* **Robust replication of `JBNU-cat` in Vero E6 cells demonstrates human ACE2 binding and underscores the permissive nature of feline cells for SARS-CoV-2: [Methodologically Flawed].**  
  In the Discussion, the authors state that they demonstrated *"the successful isolation and propagation of the Omicron variant in Vero E6 cells, a cell line known to express the human ACE2 receptor. The observed robust replication competence... further underscores the permissive nature of feline cells for SARS-CoV-2 infection."* Vero E6 cells are African green monkey (*Chlorocebus sabaeus*) kidney epithelial cells—as noted in Section 2.4—and express simian ACE2, not human or feline ACE2. Viral growth in Vero E6 cells provides no experimental evidence regarding replication kinetics in feline cells.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Add the Missing PRNT Methodology and Complete Serological Reporting in Table 2
* **WHY:** Table 2 reports specific Plaque Reduction Neutralization Test (`PRNT`) titers (`1/24`, `1/33`, `1/45`, `>1/5`) for all 19 cats, but PRNT is never mentioned in the Materials and Methods. Moreover, Table 2 lists raw `OD450` values without the control optical densities (`ODNC`, `ODPC`) or calculated `S/P%` values needed to verify the 60% positivity threshold (especially for Case 17, which has the lowest `OD450` of `0.5824`).
* **WHAT:** Add a dedicated subsection in Section 2 detailing the PRNT protocol and update Table 2 to include both `OD450` and calculated `S/P (%)` values.
* **HOW:** Specify the challenge virus strain (e.g., ancestral vs. Omicron BA.1), cell line, serial dilution series, incubation period, plaque/focus readout ($50\%$ or $90\%$ neutralization endpoint), and the mathematical interpolation formula (e.g., Reed–Muench or Spearman–Kärber) that produced non-twofold titers such as `1/24`, `1/33`, and `1/45`. Check whether Cat #8's titer of `>1/5` is a typographical error for `<1/5` (or `<1:10`), and clarify whether Case 17 (`OD450 = 0.5824`) met the $\text{S/P} > 60\%$ ELISA criterion or was seronegative/ambiguous during acute infection.

#### 2. Distinguish Lineage-Defining Human `BA.1.1` Mutations from Feline-Specific or Culture-Induced Substitutions
* **WHY:** Comparing `JBNU-cat` only against Wuhan-Hu-1, Delta, and a generic Omicron reference conflates the ~30 canonical Omicron `BA.1.1` spike mutations (which evolved in humans) with feline host adaptation, and sequencing the Vero E6 isolate rather than the primary swab introduces potential cell-culture artifacts.
* **WHAT:** Tabulate all nucleotide and amino acid differences between `EPI_ISL_16577826` (`JBNU-cat`) and the consensus of the 121 contemporary South Korean human `BA.1.1` genomes used in Figure 2, and temper the Discussion claims regarding feline-specific selective pressure.
* **HOW:** Inspect the multiple sequence alignment from MAFFT v7 used to build Figure 2. List every genome-wide substitution present in `JBNU-cat` that is absent from (or rare in) the 121 South Korean human `BA.1.1` sequences. If `JBNU-cat` carries no private spike mutations relative to local human `BA.1.1` strains, revise Section 3.2 and Section 4 to state that the spike protein is conserved relative to circulating human `BA.1.1` viruses without evidence of feline-specific adaptive mutations.

#### 3. Reconcile Cohort Inclusion Criteria and Shelter Metadata
* **WHY:** The manuscript contradicts itself on whether all 546 cats were randomly selected or whether all 546 cats had clinical signs (fever $>39.5\,^\circ\text{C}$ or cough), and lists three shelter cats as having COVID-19-positive owners.
* **WHAT:** Clarify the exact inclusion criteria and symptom distribution across the 546 cats, and explain the owner status of the shelter cats in Table 2.
* **HOW:** Report in Section 3.1 (and Table 1) the exact number and percentage of the 546 cats that presented with respiratory signs/fever versus asymptomatic routine/shelter visits. For Cases 7, 13, and 14 in Table 2 (`Source: Animal shelter`, `COVID-19 Patient Owner: Yes`), clarify whether these cats were surrendered to or quarantined at a shelter directly from a COVID-19-positive owner's household, or correct the table entries if mislabeled.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Inconsistencies in PCR target names, Pango lineage nomenclature, and cell-line biology detract from the technical reliability of the report.
* **WHAT & HOW:**
  1. **qPCR Target Gene Discrepancy (Section 2.2 vs. Figure 1A & Table 3):** Section 2.2 and Table 2 state that the qRT-PCR assay targets the `ORF3a` and `N` genes, whereas the Figure 1A caption refers to *"The copy number of N and RdRp gene of JBNU-cat measured by qRT-PCR"* and Table 3 reports a single `Copy Number (log10)` and `Cq` column. Specify which PCR kit and target gene are plotted in Figure 1A and reported in Table 3, provide the standard-curve equation used to convert `Cq` to $\log_{10}\text{ copy number}$, and explain why the negative control in Table 3 (`Cq = 40`) is assigned a non-zero copy number of `1.285 log10` ($\approx 19.3$ copies).
  2. **Pango Lineage Nomenclature Error (Section 3.2):** Correct the sentence *"This lineage falls within the GRA clade, a grouping within GISAID based on shared ancestry that corresponds to the B.1.1.529.2 lineage within the Pangolin classification system."* GISAID clade `GRA` corresponds to the entire Omicron clade (`B.1.1.529` and its descendants), and `BA.1.1` is an alias of `B.1.1.529.1.1` (whereas `B.1.1.529.2` is `BA.2`).
  3. **Vero E6 Species and ACE2 Receptor Correction (Section 4):** Remove the erroneous statement that Vero E6 cells express the human ACE2 receptor and demonstrate the permissiveness of feline cells; state accurately that Vero E6 is an African green monkey kidney line used for standard viral isolation.
  4. **Typographical Fix in Table 2:** Correct `Unkown` to `Unknown` in Row 14 of Table 2.
