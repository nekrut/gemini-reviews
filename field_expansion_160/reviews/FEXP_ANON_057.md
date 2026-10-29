# Review of FEXP_ANON_057

**Overall Score:** **3.3 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.5 / 8.0**  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.9/2.5 | Biology: 0.7/2.0 | Reproducibility: 0.8/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Field & Subfield:** Maternal–Fetal Medicine / Reproductive Immunology / Fecal Microbiota Transplantation (FMT) in Preeclampsia Models
* **Study Design:** Preclinical murine FMT intervention transferring pooled fecal suspensions from severe preeclampsia patients versus healthy pregnant controls into antibiotic-depleted non-pregnant female C57BL/6J mice.
* **Model System & Sample Size:** Human fecal donors ($N = 3$ severe preeclampsia patients pooled into a single slurry; $N = 3$ healthy pregnant women pooled into a single slurry) transplanted into 6-week-old non-pregnant female C57BL/6J mice ($N = 60$ total across 4 groups, $n = 15$ per group: Control [Con], Antibiotic Negative Control [Neg], Normal Pregnancy FMT [NT], and Preeclampsia FMT [PET]).
* **Perceived Methodological Maturity:** Very low; compromised by donor pooling pseudoreplication ($N = 1$ mixed slurry per group), use of non-pregnant recipient mice without blood pressure measurements to model preeclampsia, ELISA cytokine concentrations falling below the stated kit detection limits, a direct contradiction between the Gram-negative LPS mechanism and the Gram-positive/commensal taxa enriched in PET mice, duplicated paragraphs in the Discussion, and unavailable raw 16S sequencing data.

---

## 2. Executive Summary & Editorial Verdict

This study investigates whether gut microbiota dysbiosis in severe preeclampsia drives systemic inflammation by performing fecal microbiota transplantation (FMT) into antibiotic-treated (ampicillin, neomycin, metronidazole for 14 days) 6-week-old female C57BL/6J mice ($N = 60$ across Con, Neg, NT, and PET groups). Feces from three severe preeclampsia donors (`PE1–PE3`) were physically pooled into a single suspension for the PET group, and feces from three healthy pregnant women (`N1–N3`) were pooled into a single suspension for the NT group, followed by oral gavage for 6 weeks. On day 43, fecal V3–V4 16S rRNA sequencing, serum ELISA for LPS, TNF-$\alpha$, and IL-6, and urinary protein measurements were performed. The authors report significant beta-diversity separation (Bray–Curtis $R^2 = 0.307, p = 0.001$), LEfSe enrichment of *Coprococcus*, *Bacillales*, *Staphylococcus*, *Bifidobacterium*, and *Streptococcus* in PET mice versus *Helicobacter* and *Klebsiella* in NT mice, and elevated serum LPS ($10.26 \pm 3.91\text{ }\mu\text{g/ml}$), TNF-$\alpha$ ($13.34 \pm 1.07\text{ pg/ml}$), IL-6 ($16.48 \pm 5.33\text{ pg/ml}$), and urinary protein ($4456.24 \pm 1509.05\text{ }\mu\text{g/ml}$) in PET mice.

**Editorial Verdict: Reject (Flawed / Overstated).** The manuscript suffers from four fundamental methodological and biological defects that invalidate its central conclusions:
1. **Donor Pooling Pseudoreplication ($N = 1$ Effective Donor Unit per Group):** In Section 2.4 (line 80), stool from the three preeclampsia donors was physically mixed into a single pooled slurry prior to gavaging the PET mice, and the three healthy donor stools were similarly pooled. As established in the microbiome causal inference literature (Walter et al., *Cell*, 2020), pooling donors collapses inter-individual human biological variance to $N = 1$ inoculum per condition; treating 15 recipient mice gavaged with the same homogenate as independent biological replicates of preeclampsia is invalid pseudoreplication.
2. **Reported Serum TNF-$\alpha$ and IL-6 Values Fall Below the Stated ELISA Lower Limit of Detection:** Section 2.7 (line 95) explicitly states that *"the detection limit of IL-6 and TNF-$\alpha$ was 15.6–1000 pg/ml."* Yet Section 3.4 (lines 139–141) reports group mean TNF-$\alpha$ concentrations of $9.99$, $10.96$, $9.88$, and $13.34\text{ pg/ml}$—every single group is **below the $15.6\text{ pg/ml}$ lower limit of detection**! Similarly, three of the four IL-6 group means ($10.04$, $11.38$, and $10.07\text{ pg/ml}$) are below the $15.6\text{ pg/ml}$ detection limit. Statistical differences ($p < 0.001$ and $p = 0.005$) derived from extrapolated background optical densities below an assay's calibration floor are analytically invalid.
3. **Self-Contradictory Biological Mechanism (Gram-Negative LPS vs. Gram-Positive Commensal Enrichment):** The Discussion (lines 156–160) attributes the 5-fold rise in serum LPS in PET mice to overgrowth of Gram-negative LPS-producing bacteria and mischaracterizes *Coprococcus* as a pyogenic/food-poisoning coccus. In reality, *Coprococcus* and *Bifidobacterium* (both enriched in PET mice by LEfSe, line 129) are beneficial Gram-positive obligate anaerobes that do **not** synthesize LPS, whereas the canonical Gram-negative LPS-producing pathobiont *Klebsiella* (along with Gram-negative *Helicobacter*) was enriched in the **healthy control (NT)** group!
4. **Absence of Pregnancy and Blood Pressure Phenotyping:** Preeclampsia is defined by gestational hypertension and placental dysfunction, yet recipient mice were non-pregnant virgin females and neither systolic/diastolic blood pressure nor intestinal barrier markers (ZO-1/Occludin) were measured.

### Specific Conclusions and Assessment of Support

* **FMT from pooled preeclampsia versus healthy pregnant donors produces distinct gut microbial community structures in antibiotic-pretreated mice: [Fragile].**  
  While Bray–Curtis PCoA shows separation among the four groups ($R^2 = 0.307, p = 0.001$, Figure 3), pooling the three human donors into a single slurry per group ($N = 1$ pooled inoculum) confounds human disease status with idiosyncratic donor-pool effects, and the healthy pregnancy (NT) inoculum unexpectedly resulted in dominance of *Helicobacter* and *Klebsiella* (line 129).

* **Preeclampsia FMT significantly elevates mouse serum TNF-$\alpha$ and IL-6 levels: [Methodologically Flawed].**  
  All four group means for TNF-$\alpha$ ($9.88\text{–}13.34\text{ pg/ml}$) and three of four group means for IL-6 ($10.04\text{–}11.38\text{ pg/ml}$, with PET at $16.48 \pm 5.33\text{ pg/ml}$) lie below the $15.6\text{ pg/ml}$ lower limit of detection specified for the ELISA kits in Section 2.7.

* **Overgrowth of harmful bacteria (`Coprococcus`, `Staphylococcus`, `Bifidobacterium`, `Streptococcus`) in PET mice drives Gram-negative LPS translocation and preeclampsia pathogenesis: [Methodologically Flawed].**  
  Gram-positive bacteria (*Coprococcus*, *Bifidobacterium*, *Staphylococcus*, *Streptococcus*) lack an outer membrane and do not produce LPS (endotoxin). Moreover, classifying the butyrate-producing commensal genus *Coprococcus* as a bacterium that *"can cause purulent infections and food poisoning in humans"* (line 156) is microbiologically incorrect, and the Discussion's claim that *Lactobacillus* was reduced in PET mice (lines 156, 162) is not supported by any statistical test in the Results (where phylum/top-genus differences in Figure 1 were non-significant, $p > 0.05$).

* **Preeclampsia FMT induces preeclampsia-like proteinuria in recipient mice: [Fragile].**  
  Although urinary protein concentration was higher in PET mice ($4456.24\text{ }\mu\text{g/ml}$, line 146), the recipients were non-pregnant mice without blood pressure measurements, glomerular histology, or 24-hour urine volume normalization (spot urine protein concentration in mice is heavily confounded by hydration status and normal murine major urinary proteins).

---

## 3. Forensic Defect Inventory

### 1. Donor Pooling Pseudoreplication ($N = 1$ Mixed Slurry per Condition) (Pillars 2, 3, 4)
* **Defect:** Section 2.4 (line 80) states: *"The feces of three patients with severe preeclampsia were mixed to prepare fecal bacterial solution and the fecal bacterial solution of normal pregnant women was prepared in the same way."* Fifteen mice per group were then gavaged with these two pooled slurries and analyzed by one-way ANOVA / Student's $t$-test as $n = 15$ independent biological replicates.
* **WHY:** Mixing stool from three human donors into one tube eliminates donor-to-donor variance and creates a single composite microbial community ($N = 1$). Gavaging 15 mice with the same tube measures technical/cage replication of that single mixture, inflating the Type I error rate of host phenotype comparisons to $> 50\%$ (Walter et al., *Cell*, 2020).
* **WHAT:** Acknowledge in the Abstract, Results, and Limitations that donor stools were pooled ($N = 1$ pool of 3 donors per group), or colonize separate cohorts of mice with individual, unpooled human donor samples ($N \ge 5\text{–}6$ individual human donors per group, with 3–4 recipient mice nested per donor) analyzed via a linear mixed-effects model (`phenotype ~ group + (1 | donor_ID)`).
* **HOW:** Reframe all statistical inferences in Section 3 to state that they reflect differences between the two pooled inocula rather than generalizable population-level effects of preeclampsia microbiota.

### 2. ELISA Measurements Below the Kit Lower Limit of Detection (Pillars 4, 6, 7)
* **Defect:** Section 2.7 (line 95) states: *"The detection limit of LPS was 0.313-20 $\mu$g/ml and the detection limit of IL-6 and TNF-$\alpha$ was 15.6–1000 pg/ml."* In Section 3.4 (lines 139–141), serum TNF-$\alpha$ levels are reported as $9.99 \pm 2.47$, $10.96 \pm 1.05$, $9.88 \pm 2.54$, and $13.34 \pm 1.07\text{ pg/ml}$, and serum IL-6 levels are reported as $10.04 \pm 2.25$, $11.38 \pm 5.82$, $10.07 \pm 2.84$, and $16.48 \pm 5.33\text{ pg/ml}$. Additionally, line 95 states that LPS was measured in plasma from *"anticoagulation tubes"* while the section header, text, and Figure 5 label it *"Serum LPS"*, and the vendor of the IL-6/TNF-$\alpha$ kits is listed as *"Leader in Biomolecular Solutions for Life Science"* (which is the advertising slogan of Proteintech/Abcam, not a company name!).
* **WHY:** Concentrations below the lowest standard of an ELISA calibration curve ($15.6\text{ pg/ml}$) represent unquantifiable background noise.
* **WHAT & HOW:** Verify whether a sample dilution factor (e.g., $2\times$ or $5\times$ dilution prior to assaying) was omitted when calculating the final $\text{pg/ml}$ values in Section 3.4; if the samples were assayed undiluted, re-assay serum TNF-$\alpha$ and IL-6 using a high-sensitivity mouse ELISA kit (sensitivity $< 1\text{ pg/ml}$); clarify whether LPS was measured in serum or anticoagulated plasma (and specify the exact Limulus Amebocyte Lysate [LAL] or competitive ELISA catalog number, as $\mu\text{g/ml}$ concentrations of circulating LPS in surviving mice are 1,000-fold higher than physiological $\text{pg/ml}$–$\text{ng/ml}$ endotoxemia levels); and replace the slogan *"Leader in Biomolecular Solutions for Life Science"* with the actual manufacturer name and catalog numbers.

### 3. Microbiological Mischaracterization of *Coprococcus* and Contradiction with Gram-Negative LPS Narrative (Pillars 3, 6)
* **Defect:** (a) Line 156 states: *"Staphylococcus, Streptococcus and Coprococcus were all gram-positive cocci, which can cause purulent infections and food poisoning in humans."* (b) Lines 156–160 argue that PET microbiota increases serum LPS because Gram-negative bacteria produce LPS, ignoring that LEfSe (line 129, Figure 4) showed Gram-negative *Klebsiella* and *Helicobacter* were enriched in the healthy control **NT** group, whereas Gram-positive *Coprococcus*, *Bifidobacterium*, *Staphylococcus*, and *Streptococcus* were enriched in the **PET** group. (c) Lines 156 and 162 claim that *"our study also have shown that mice transplanted with preeclamptic fecal microbiota suspension show a reduced abundance of Lactobacillus"*, which is never statistically tested or reported in Section 3.
* **WHY:** *Coprococcus* (`Lachnospiraceae`) is a strictly anaerobic, butyrate-producing gut commensal, not a pyogenic or food-poisoning pathogen, and Gram-positive bacteria do not produce LPS.
* **WHAT & HOW:** Remove the false statement that *Coprococcus* causes purulent infections and food poisoning; reconcile how serum LPS increased in PET mice when Gram-negative *Klebsiella* and *Helicobacter* were enriched in NT mice; and either provide the exact Kruskal–Wallis / Wilcoxon $p$-value and FDR-adjusted $q$-value for *Lactobacillus* across the four groups in Section 3.1 or remove the claim of *Lactobacillus* depletion from the Discussion.

### 4. Duplicated Discussion Paragraph, Typographical Errors, and Missing 16S Repository Accession (Pillar 7)
* **Defect:**
  1. **Duplicated Paragraph:** In Section 4 (Discussion), paragraph 5 (line 164: *"Therefore, our study provides a theoretical basis for the supplementation of probiotics..."*) and paragraph 6 (line 166: *"In conclusion, this study offers valuable insights into the supplementation of probiotics..."*) are near-verbatim duplicates of the same 6-sentence paragraph.
  2. **Numerical Typo:** Line 146 reports urinary protein in the Neg group as `3049.8.80 ± 1549.63 µg/ml` (double decimal point).
  3. **Table Reference Typo:** Line 30 cites `(Table A1)` while the table on line 33 is titled `Table 1`, and Appendix A (line 178) is empty.
  4. **Outdated R Version & Missing SRA Accession:** Line 90 states `R packages (v3.2.0)` (from 2015) alongside `QIIME2 (2019.4)`, fail to specify how many mice per group were sequenced by 16S rRNA, and the Data Availability Statement (line 183) provides no NCBI SRA / ENA / GSA accession number for the raw 16S sequencing reads.
* **WHY:** Duplicated paragraphs, malformed numbers (`3049.8.80`), and missing sequence accessions undermine data integrity and reproducibility.
* **WHAT & HOW:** Delete the duplicated paragraph on line 166; fix `3049.8.80` on line 146; reconcile `Table A1` vs. `Table 1`; state the exact $n$ per group in Figures 1–6; and deposit the raw 16S rRNA FASTQ files in NCBI SRA or CNCB GSA.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.9** | **3.5** | Pooling 3 donors into a single slurry ($N=1$ inoculum/group) creates severe FMT pseudoreplication; reported TNF-$\alpha$ and IL-6 concentrations are below the $15.6\text{ pg/ml}$ ELISA detection limit; no FDR correction on LEfSe or multi-group comparisons; unspecified $n$ per group in 16S and ELISA assays. |
| **2. Claim-to-Evidence Alignment** | **0.9** | **2.5** | Claims to establish a causal link between preeclampsia gut microbiota, LPS-driven inflammation, and preeclampsia pathogenesis using non-pregnant mice without blood pressure measurements; claims *Lactobacillus* reduction in Discussion without statistical support in Results. |
| **3. Data Integrity & Biological Plausibility** | **0.7** | **2.0** | Mischaracterizes commensal butyrate-producer *Coprococcus* as a cause of "purulent infections and food poisoning"; attributes LPS elevation to Gram-positive taxa while Gram-negative *Klebsiella* and *Helicobacter* are enriched in the healthy control FMT group; $\mu\text{g/ml}$ serum LPS levels are biologically implausible without explanation. |
| **4. Reproducibility & Data Integrity** | **0.8** | **2.0** | No public repository accession (SRA/GSA) for 16S rRNA data; verbatim duplicated paragraph in Discussion (lines 164 and 166); malformed number `3049.8.80` on line 146; manufacturer slogan (`"Leader in Biomolecular Solutions for Life Science"`) listed instead of company name on line 95. |
| **Scientific Core Score** | **2.5** | **8.0** | Sum of Rigor (0.9) + Claims (0.9) + Biology (0.7). |
| **Overall Composite Score** | **3.3** | **10.0** | **Flawed / Overstated Tier** (Sum of all four dimensions). |
