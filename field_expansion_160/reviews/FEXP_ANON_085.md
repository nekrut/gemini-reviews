# Review of FEXP_ANON_085

**Overall Score:** **3.6 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **3.2 / 8.0**  
* **Score Breakdown:** Rigor: 1.0/3.5 | Claims: 1.0/2.5 | Biology: 1.2/2.0 | Reproducibility: 0.4/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Role / Domain:** Single-cell transcriptomic and immunohistochemistry (IHC) investigation of human skin aging ($n = 4$ young vs. $n = 4$ elderly donors) with `pySCENIC`, `CellPhoneDB`, and `Drug2Cell` computational drug repurposing.
* **Blinded Document Assessment:** An observational scRNA-seq study undermined by cell-level pseudoreplication with unadjusted $p < 0.05$ cutoffs across all statistical comparisons, complete omission of essential donor metadata (anatomical biopsy site, UV exposure status, donor sex, IRB protocol number, and total sequenced cell count), failed protein-level IHC validation for three of the four tested markers (`MT1`, `LTF`, `JAG1`), biologically hazardous chemotherapy hits (`cisplatin`, `dacarbazine`, `etoposide`) from `Drug2Cell`, and unavailable raw sequencing data.

---

## 2. Executive Summary & Editorial Verdict

This study compares single-cell RNA-seq profiles of human skin from four young donors (14–20 years) and four elderly donors (60–76 years), identifying 10 major skin cell populations and multiple keratinocyte subclusters (including six basal cell subclusters). The authors perform Wilcoxon/Mann–Whitney U tests to identify aging-associated DEGs, `pySCENIC` regulons (`FOSB(+)`, `DDIT3(+)`, `LTF(+)`), `CellPhoneDB` ligand–receptor alterations (`WNT4`, `JAG1`), and `Drug2Cell` compound activity scores, accompanied by IHC staining for `MT1`, `LTF`, `FOSB`, and `JAG1`. They report subcluster-specific `MT1` mRNA changes in basal C11, increased `FOSB` regulon activity and protein staining in aged basal keratinocytes, and prioritize `epinephrine bitartrate`, `becaplermin`, and `retinol` (alongside several cytotoxic chemotherapeutics) as anti-aging candidates.

**Editorial Verdict: Reject (Flawed / Overstated).** The manuscript's statistical and experimental design cannot support its conclusions. First, all differential expression (Wilcoxon rank-sum), regulon activity (`pySCENIC` Mann–Whitney U), and drug response (`Drug2Cell` Mann–Whitney U) comparisons treat individual cells as independent observations across only $n = 4$ vs. $n = 4$ donors and apply an unadjusted $p < 0.05$ threshold without false discovery rate (FDR) correction, resulting in extreme pseudoreplication. Second, critical clinical and technical metadata are missing: the authors never report the anatomical site of the skin biopsies (sun-exposed vs. sun-protected), donor sex distribution, total number of cells passing QC, or human subjects ethics approval / informed consent documentation. Third, of the four targets tested by IHC (`MT1`, `LTF`, `FOSB`, `JAG1`), three (`MT1`, `LTF`, `JAG1`) showed no age-related protein difference, and even for `FOSB`, no statistical test or $p$-value is reported for the ImageJ quantification. Fourth, raw scRNA-seq data are not deposited in any public repository.

### Specific Conclusions and Assessment of Support

* **Subcluster-specific aging DEGs and metallothionein (`MT1G`, `MT1E`, `MT1A`, `MT1X`) dynamics in basal keratinocytes: [Fragile].**  
  DEGs were called using an unadjusted cell-level Wilcoxon test ($p < 0.05, |\text{avg\_log}_2\text{FC}| > 0.5$, line 55) without donor-level pseudobulk aggregation or multiple-testing correction. Furthermore, IHC staining for `MT1` (Figure S2, line 83) showed uniform protein expression across epidermal layers with no difference between young and elderly skin. Because anatomical site and UV exposure history of the 8 biopsies are unreported, stress-gene differences (`MT` family, `HSPA1A/B`, `FOSB`) may reflect site-specific sun exposure or dissociation stress rather than chronological aging.
* **Increased `FOSB(+)` and `DDIT3(+)` regulon activity and decreased `LTF(+)` expression in aged basal keratinocytes: [Moderately Supported].**  
  While `FOSB` upregulation is qualitatively supported by both scRNA-seq and IHC (Figure S9), `pySCENIC` regulons were run on young and elder groups separately (line 107) and compared via unadjusted cell-level Mann–Whitney U tests ($p < 0.05$, line 60). In addition, `FOSB` and `DDIT3` are classic immediate-early / dissociation-stress genes induced by enzymatic digestion at $37^\circ\text{C}$ (`collagenase I/IV + dispase + trypsin`, line 35), and `LTF` showed no protein-level change on IHC (Figure S8, line 112).
* **Loss of `WNT4` and `JAG1–NOTCH3` intercellular communication in aged skin: [Fragile].**  
  `CellPhoneDB` v3 permutations permute cluster labels across cells rather than donor age labels ($n = 4$ vs. $n = 4$), and IHC for `JAG1` failed to detect any age-related difference in protein abundance (Figure S10, line 124).
* **`Drug2Cell` identification of anti-aging drug candidates (`epinephrine bitartrate`, `becaplermin`, `cisplatin`, `dacarbazine`, `etoposide phosphate`): [Overstated].**  
  `Drug2Cell` merely computes target-gene expression enrichment scores and compares them with unadjusted cell-level Mann–Whitney tests ($p < 0.05$, line 75). It does not account for directionality of pharmacological action (agonist vs. antagonist vs. cytotoxic agent), which is why DNA-damaging chemotherapeutics that induce senescence (`cisplatin`, `dacarbazine`, `etoposide phosphate`, line 136) are absurdly flagged alongside topical agents as skin-aging drug candidates.

---

## 3. Forensic Defect Inventory

1. **Cell-Level Pseudoreplication and Absence of Multiple-Testing Correction Across All Comparisons (Pillar 3 & Pillar 4):**
   * **Location:** Materials and Methods ("Differential Gene Expression Analysis", line 55; "Gene Regulatory Network Analysis", line 60; "Drug Response Prediction", line 75).
   * **Defect:** In a two-group comparison of $n = 4$ young vs. $n = 4$ elderly donors, applying two-sample Wilcoxon / Mann–Whitney U tests across thousands of single cells treats cells from the same donor as independent biological replicates, inflating Type I error rates by orders of magnitude. Compounding this flaw, all three analyses use raw $p < 0.05$ without Benjamini–Hochberg FDR correction.
2. **Omission of Essential Clinical Metadata, Cell Counts, and Human Ethics Approval (Pillar 2 & Pillar 7):**
   * **Location:** Materials and Methods ("Skin Sample Collection", line 30; "Data Preprocessing and Integration", line 45).
   * **Defect:**
     * **Missing Ethics / IRB Statement:** Although human skin biopsies were collected from healthy donors (including minors aged 14–20 years, line 30), the manuscript contains no Institutional Review Board (IRB) approval number, hospital name, or informed consent statement.
     * **Missing Anatomical Site & Sex Metadata:** Neither the anatomical location of the skin biopsies (photoexposed vs. photoprotected) nor donor sex is disclosed.
     * **Missing Cell Counts:** The total number of single cells sequenced and retained after QC across the 8 donors (and per cluster/donor) is never reported anywhere in the text or figure legends.
3. **Unexplained Pipeline Anachronism (`HiSeq 2500` + `Cell Ranger 2.2.0` + `hg19` vs. `Seurat 5.0`) (Pillar 2 & Pillar 7):**
   * **Location:** Materials and Methods ("Cell Isolation, Sequencing, and Library Preparation", line 35; "Processing scRNA-Seq Raw Data", line 40; "Data Preprocessing and Integration", line 45).
   * **Defect:** The authors report sequencing on an Illumina HiSeq 2500 and running `Cell Ranger v2.2.0` (a 2018 software release) aligned to legacy reference `hg19`, followed by downstream analysis in `Seurat v5.0` (released in late 2023). If the data were reused or reprocessed from an earlier study, the source accession must be cited; if newly generated, raw data must be deposited publicly.
4. **Unquantified IHC Validation and High Rate of mRNA–Protein Discordance (Pillar 4 & Pillar 5):**
   * **Location:** Materials and Methods ("IHC Staining", line 70) and Results (lines 83, 112, 114, 124; Figures S2, S8, S9, S10).
   * **Defect:** Although line 70 states *"ImageJ quantified five fields/sample,"* no quantitative bar plots, sample sizes ($n$ donors stained), mean $\pm$ SD values, or statistical $p$-values for the IHC staining are reported in the Results text, and all IHC images are relegated to Supplementary Figures S2 and S8–S10. Moreover, 3 of the 4 stained proteins (`MT1`, `LTF`, `JAG1`) show no difference between young and aged skin.
5. **Separate `pySCENIC` Network Inference per Age Group (Pillar 3):**
   * **Location:** Results ("Skin Aging-Related Gene Modules and Regulatory Function Alterations", line 107).
   * **Defect:** Line 107 states that the authors *"predicted the transcription factors (TF) regulons via gene regulatory network analysis on cells from the elder and young groups separately."* When `GRNBoost2` and `cisTarget` are run separately on young and elderly cells, the resulting regulons (`TF(+)`) contain different target gene sets in each age group (as shown in Fig. 3F), making direct Mann–Whitney comparisons of `AUCell` scores between age groups (Fig. 3A) apples-to-oranges because the underlying gene sets being scored are not identical.
6. **Withheld Raw Data and Code (Pillar 7):**
   * **Location:** Data Availability Statement (lines 201, 232).
   * **Defect:** Raw FASTQ files and UMI count matrices are not deposited in GEO/SRA/GSA (*"available from the corresponding author upon reasonable request"*), and no analysis scripts are provided.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.0** | **3.5** | Cell-level Wilcoxon/Mann–Whitney pseudoreplication across $n=4$ vs. $n=4$ donors without FDR adjustment; separate `pySCENIC` regulon definitions across age groups; unquantified IHC statistics. |
| **2. Claim-to-Evidence Alignment** | **1.0** | **2.5** | `MT1`, `LTF`, and `JAG1` transcriptional claims fail IHC protein validation; `Drug2Cell` target-expression correlations are over-interpreted as anti-aging drug repurposing (including cytotoxic chemotherapeutics). |
| **3. Data Integrity & Biological Plausibility** | **1.2** | **2.0** | Missing donor sex, biopsy anatomical site (UV confounding), IRB/consent documentation for human subjects (including 14–20 yr olds), and total cell counts; enzymatic dissociation stress may confound `FOSB`/`DDIT3`/`HSPA1A`. |
| **4. Reproducibility & Data Integrity** | **0.4** | **2.0** | Neither raw/processed scRNA-seq data nor analysis code is publicly available, and key sample/cell counts are omitted from the manuscript. |
| **Scientific Core Score** | **3.2** | **8.0** | Sum of Rigor + Claims + Biology. |
| **Total Composite Score** | **3.6** | **10.0** | **Flawed / Overstated** |

---

### 5. Constructive and Doable Suggestions for Improvement

1. **Replace Cell-Level Tests with Donor-Level Pseudobulk Differential Expression:** Aggregate UMI counts per donor and cell type ($n = 4$ young vs. $n = 4$ elderly) and run `DESeq2` or `edgeR` quasi-likelihood $F$-tests with Benjamini–Hochberg FDR correction ($\text{FDR} < 0.05$). Similarly, average `AUCell` and `Drug2Cell` scores per donor within each cell cluster before comparing age groups.
2. **Compute `pySCENIC` Regulons on the Combined Atlas:** Run `GRNBoost2` and `cisTarget` once on the integrated 8-donor dataset so that each `TF(+)` regulon has a fixed target gene set before comparing `AUCell` activity between young and elderly donors.
3. **Report Complete Donor Metadata, Ethics Approval, and Cell Counts:** Add a table detailing each donor's age, sex, anatomical biopsy site, sun-exposure classification, total cells sequenced, and post-QC cell counts per cluster, and provide the institutional ethics approval number and informed consent statement (especially for adolescent donors aged 14–17).
4. **Provide Statistical Quantification for IHC and Filter Cytotoxic Compounds in `Drug2Cell`:** Report donor-level mean optical density / % positive nuclei $\pm$ SD and two-sample test $p$-values for `MT1`, `LTF`, `FOSB`, and `JAG1` IHC, and filter out genotoxic antineoplastic agents (`cisplatin`, `dacarbazine`, `etoposide`) from anti-aging repurposing claims.
5. **Deposit Raw and Processed Data in a Public Repository:** Upload the UMI count matrices and metadata to NCBI GEO or GSA and provide the analysis scripts on GitHub/Zenodo.
