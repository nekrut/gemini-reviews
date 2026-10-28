# Review of PMC6697540 (PMID:31367035)

**Manuscript Title:** Human placenta has no microbiome but can contain potential pathogens  
**Authors:** de Goffau MC, Lager S, Sovio U, Gaccioli F, Cook E, Peacock SJ, Parkhill J, Charnock-Jones DS, Smith GCS.  
**Journal / Preprint:** *Nature* (2019; `PMC6697540` / `PMID:31367035` / `10.1038/s41586-019-1451-5`)  
**Calibration Study Cohort:** Cohort B — Validated Control (`B31` | Double-Blinded as `ANON_199`)  
**Overall Score:** **9.8 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.4/3.5 | Claims: 2.5/2.5 | Biology: 2.0/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents a large-scale, forensically designed investigation of whether the human placenta harbors a resident microbiome or whether bacterial DNA in the placenta is associated with preeclampsia (PE), delivery of a small for gestational age (SGA) infant, or spontaneous preterm birth (PTB). Analysing placental terminal villi biopsies from 537 nulliparous women enrolled in the prospective Pregnancy Outcome Prediction (POP) study, the authors examine two cohorts: Cohort 1 ($n = 80$ pre-labor Caesarean sections: 20 PE, 20 SGA, 40 matched controls), spiked prior to DNA extraction with ~1,100 CFU of *Salmonella bongori* as an internal quantitative positive control and profiled by both deep shotgun metagenomics (average 424 million reads/sample) and V1–V2 16S rRNA amplicon sequencing; and Cohort 2 ($n = 498$: 100 PE, 100 SGA, 100 PTB, and 198 matched controls), extracted in duplicate using two distinct kits (Qiagen and MP Biomedical) and profiled by duplicate 16S rRNA sequencing alongside 47 reagent extraction blanks, followed by targeted nested PCR/qPCR for the *Streptococcus agalactiae* (Group B *Streptococcus*, GBS) *sip* gene in 276 samples. The authors demonstrate that the human placenta does not possess a resident microbiome and that bacterial infection is not a common cause of PE, SGA, or PTB. Almost all detected bacterial sequences trace to five rigorously documented contamination pathways (acquisition of vaginal/fecal bacteria during labor and delivery, PBS wash buffer batch contamination in 2012–2013, kit-specific DNA extraction contaminants, PCR polymerase/buffer lot contaminants, and sequencing facility cross-contamination/index-hopping), with the sole exception of *S. agalactiae*, which is verified across all three orthogonal methods in ~5% of pre-labor placentas without batch or delivery-mode dependence. All 16S data (ENA ERP109246 / PRJEB27192), human-filtered/managed-access metagenomes (EGA EGAD00001004198), oligotype abundance matrices, and custom bioinformatic scripts are available.

This study is a benchmark of experimental, bioinformatic, and statistical rigor in low-biomass metagenomics. By incorporating a quantitative cellular spike-in (*S. bongori* at 1,100 CFU) to empirically calibrate sensitivity (~6 CFU per metagenomic read pair and ~0.1–0.2% of 16S reads per CFU), extracting 498 placentas twice with orthogonal kits, tracking reagent lot numbers and collection dates, and performing strain-level assembly of metagenomic reads to prove cross-contamination from concurrent facility sequencing projects (*Vibrio cholerae*, *S. pneumoniae*, *Leishmania infantum*, *Danio rerio*, *Sarcophilus harrisii*) and single-strain *E. coli* reagent contamination, the authors leave no ambiguity in their conclusions. Only minor statistical presentation refinements are suggested.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The human placenta lacks a resident microbiome, and virtually all widespread bacterial signals derive from reagent, buffer, sequencing-facility, or intrapartum contamination (Fig. 1, Fig. 2, Fig. 4, Tables 1–2): [Well Supported].**  
  In Cohort 1, 98% of metagenomic variance (PC1 80%, PC2 18%) is explained by sequencing run batch rather than clinical phenotype (Fig. 1a–b), and strain-level mapping proves that pervasive *E. coli* reads across 80 samples derive from a single clonal reagent strain (`WG5`, Extended Data Fig. 3), while *V. cholerae* and *S. pneumoniae* reads match specific isolates sequenced concurrently at the Sanger Institute. In Cohort 2, duplicate extractions across 498 samples show that putative placental taxa (*Burkholderia*, *Bradyrhizobium*, *Thiohalocapsa halophila*, *Deinococcus geothermalis*) segregate strictly by extraction kit (MPBio vs. Qiagen), PCR master-mix lot (Q5 buffer lot #11408 / Taq lot #51405), or PBS wash date (2012–2013), whereas vaginal *Lactobacillus* and vaginosis taxa correlate strongly with vaginal and intrapartum CS delivery versus pre-labor CS ($P < 0.001$; Fig. 2b–c).

* **Quantitative sensitivity of both 16S amplicon sequencing and deep metagenomics is sufficient to detect ~6 CFU of bacteria in 25 mg of placental tissue (Extended Data Fig. 2, Online Methods): [Well Supported].**  
  The 1,100 CFU *S. bongori* spike-in was detected in 80/80 metagenomic samples (mean $180 \pm 90$ read pairs) and 79/79 16S samples (mean $54 \pm 13\%$ of reads, ~33,000 reads), directly refuting any claim that failure to detect a resident placental microbiome is due to low assay sensitivity or PCR inhibition by host DNA.

* ***Streptococcus agalactiae* (GBS) is genuinely present prior to labor onset in ~5% of placentas, verified across 16S (both kits), shotgun metagenomics, and nested *sip* PCR/qPCR (Tables 1–2, Results): [Well Supported].**  
  *S. agalactiae* is absent from all 47 negative controls, independent of DNA extraction kit, sequencing run, year of collection, and mode of delivery (present in pre-labor CS samples), and exhibits highly significant concordance between 16S and shotgun metagenomics ($\kappa = 0.58, P < 0.0001$ / $P = 1.5 \times 10^{-8}$) and between 16S and nested *sip* PCR/qPCR in 276 samples ($\kappa = 0.48, P = 9.7 \times 10^{-21}$, with 7/7 *sip*-positive samples exceeding 1% 16S reads).

* **Placental bacterial presence is not a common cause of preeclampsia, SGA, or spontaneous preterm birth, though delivery-associated *Ureaplasma* and *S. anginosus* associate with PTB (Fig. 3, Supplementary Table 5): [Well Supported].**  
  Powered at 82% to detect $\text{OR} = 5$ at 5% control prevalence in 100 matched case-control pairs, *S. agalactiae* showed no significant association with PE, PTB, or SGA (a non-significant trend of $P = 0.06$ for SGA is transparently reported), while *Ureaplasma* spp. and *S. anginosus* associated with PTB in vaginally delivered placentas, consistent with ascending intrapartum infection.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Account for the Two Re-Used Control Subjects in Pooled Cohort 2 Analyses
* **WHY:** In Experimental Approach (line 17) and Methods (line 197), the authors note that Cohort 2 included 100 PE, 100 SGA, 100 PTB, and *"198 matched controls (two controls were used twice)"* (yielding 498 total sample records from 496 unique women). While conditional logistic regression for PE (100 pairs) and SGA (100 pairs) handles each matched set separately, pooled analyses across all 498 records (such as Fig. 2b–c and Extended Data Figs. 6–8) include the two duplicated control subjects twice.
* **WHAT & HOW:** Clarify in the Methods (*Patient selection*, line 197, and *Statistics*, line 16 of page 2) whether the two controls matched to both a PE and an SGA case were sequenced twice or had their sequencing record duplicated in the 498-sample table, and ensure that pooled Mann-Whitney $U$ tests and Spearman correlations across Cohort 2 deduplicate those two subjects ($n = 496$ unique women).

#### 2. Report Continuous Read-Count / Relative-Abundance Concordance Alongside Thresholded Kappa Statistics
* **WHY:** In Table 1 and Supplementary Table 4, inter-method concordance ($\kappa$) is computed after dichotomizing 16S relative abundance at $>1\%$ (and $>0.1\%$ in Supplementary Table 3). When a true low-level signal sits near the $1\%$ boundary (e.g., $0.8\%$ in one kit and $1.2\%$ in the other, or 1–2 reads in metagenomics), hard thresholding can underestimate concordance or lose quantitative information.
* **WHAT & HOW:** Alongside the thresholded $\kappa$ statistics in Table 1, report the quantitative Spearman rank correlation ($\rho$) and Lin's concordance correlation coefficient between metagenomic read counts (normalized to *S. bongori* spike-in reads) and 16S relative abundances (normalized to *S. bongori* 16S reads) in Cohort 1.

#### 3. Technical and Editorial Cleanup
* **WHY:** A few minor typographical errors appear in the tables and methods.
* **WHAT & HOW:**
  * **Table 1 header (line 37):** Fix typo `"Absent/Weak/Strong (n=5)t §"` to `"(n=5) §"`.
  * **Line 238 (Bioinformatic analysis of metagenomics data):** Fix `"Streptococcus pneumonia"` to `"Streptococcus pneumoniae"`.
  * **Fig. 4 caption (line 180):** Fix `"V. cholera"` to `"V. cholerae"`.
