<Blinded Review: TIME_ANON_0670>
**Composite Score:** 3.9 / 10.0 (Rigor: 1.1/3.5 | Claims: 1.0/2.5 | Biology: 1.0/2.0 | Reproducibility: 0.8/2.0)
**Bias Category:** Algorithmic/Model
**Verdict:** Reject (Fundamental Flaws)
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Translational/Preclinical/Biomarker

OVERALL_SCORE: 3.9/10
VERDICT: FAILED
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This bioinformatics study presents `ViralCellDetector`, a two-part computational workflow for detecting viral contamination in cell line RNA-seq data: (1) a read-mapping pipeline that aligns reads to the host reference using STAR, maps unmapped reads to the NCBI viral genome database using BWA, and applies heuristic filtering criteria; and (2) a Random Forest (RF) classifier trained on 12 host gene expression features selected from 300 differentially expressed genes (derived from HCoV-OC43-infected Vero E6 cells and SARS-CoV-2-infected Calu-3 cells) to classify 1,021 public MCF7 RNA-seq datasets (`110` labeled "infected" vs. `911` "control"). While the general goal of screening public RNA-seq repositories for occult viral contamination is useful, the study suffers from severe methodological, bioinformatic, and machine-learning flaws: it misidentifies well-known reference/sequencing artifacts (`BeAn 58058 virus`, `Human endogenous retrovirus K113`, and intentionally lentiviral-transduced `HIV-1` vectors) as active MCF7 viral contaminations, uses an internally contradictory read-mapping threshold (`at least 20% reads should be mapped to the viral genome`), performs cross-species DE comparison without accounting for Vero E6 being *Chlorocebus sabaeus* (African green monkey), and suffers from circular pseudo-labeling and severe class-imbalance distortion in its Random Forest evaluation.

### 2. Methodological & Statistical Audit / WEAKNESSES & METHODOLOGICAL AUDIT
- **Misidentification of Reference Artifacts, Endogenous Retroviruses, and Lentiviral Vectors as "Viral Contamination" in MCF7:**
  - The authors claim to detect six contaminating viruses in MCF7 cells (Figure 3b, Line 75 & Line 107): `BeAn 58058 virus`, `Human endogenous retrovirus K113 (HERV-K113)`, `HIV-1`, `Woodchuck hepatitis virus (WHV)`, `Encephalomyocarditis virus (EMCV)`, and `Eptesicus fuscus gammaherpesvirus`.
  - In standard human RNA-seq bioinformatics, **`BeAn 58058 virus`** (Cotia poxvirus) is a notorious false-positive database artifact because its NCBI RefSeq genome contains host-derived poly(A)/low-complexity and homopolymer sequences that attract unmapped human reads!
  - **`HERV-K113`** is an *endogenous* human retrovirus integrated in the human genome (which the authors' own Methods on Line 42 state should be removed: *"the endogenous retroviruses may be removed before indexing"*), not an exogenous viral contamination!
  - **`HIV-1`** and **`Woodchuck hepatitis virus` (WPRE, Woodchuck Hepatitis Virus Posttranscriptional Regulatory Element)** are standard components of **lentiviral shRNA/CRISPR/overexpression vectors** routinely used to transduce MCF7 cells in functional genomics studies! Indeed, the authors admit on Line 80 that ~50% of the 110 "infected" MCF7 samples came from studies where viral vectors were intentionally transfected/transduced, yet they still retain all 110 samples as the positive "infected" class (`110 infected vs. 911 control`) to train and test their host-response Random Forest classifier!
- **Arbitrary Upper-Quartile Labeling Circularity:** To define the 110 "infected" MCF7 samples out of 1,021 ARCHS4 samples, the authors did not use their stated pipeline criteria (>20% reads, >50% genome coverage); instead, they simply took the expression counts of the 6 putative viruses across 1,021 samples and applied an arbitrary percentile/quartile threshold to label the top ~10% (110 samples) as "infected" (Line 80). Training an RF classifier on pseudo-labels defined by lentiviral vector elements (HIV-1/WPRE) and HERV-K expression measures vector-transduction / batch effects rather than true viral infection.
- **Misleading Reporting of Sensitivity vs. Specificity Under 90:10 Class Imbalance:** On Line 98 (and Figure 5e), the authors report `accuracy = 0.93, sensitivity = 0.99, and specificity = 0.60` on the MCF7 test set (`911 control` [89.2%] vs. `110 infected` [10.8%]). Mathematically, for `accuracy = 0.892 * Sens + 0.108 * Spec` to equal `0.93` when `Sens = 0.99` and `Spec = 0.60` (`0.892 * 0.99 + 0.108 * 0.60 = 0.883 + 0.065 = 0.948`), the authors have **inverted the positive and negative classes** (`911 controls` treated as the positive class with 99% recall, and `110 infected` treated as the negative class with only 60% recall)! A trivial majority-class classifier predicting "control" for every sample achieves 89.2% accuracy.
- **Feature Selection Leakage & Cross-Species Mapping Flaw:**
  - In Line 47 & 85, the authors state that all sequencing reads from `GSE198398` (Vero E6 cells) and `GSE187420` (Calu-3 cells) were mapped to the human `Hg38` transcriptome (`ENSEMBL GRCh38.p3`). However, **Vero E6 cells are African green monkey (*Chlorocebus sabaeus*) kidney cells, not human cells!** Mapping monkey reads directly to human GRCh38 without orthologous transcriptome handling introduces severe mapping bias.
  - Furthermore, in Line 52 & Figure 5a–b, recursive feature elimination (RFE) and filtering of the top 12 features (`ZNF614`, `ZNF613`, `ZNF595`, `ZNF433`, `ZNF627`, `ZNF333`—6 of the 12 "viral biomarkers" are Krüppel-associated box [KRAB] zinc finger proteins that regulate endogenous retroelements like HERV-K!) appear to have been evaluated across CV folds before reporting test metrics.

### 3. Biological / Experimental Grounding & Claim Proportionality / STRENGTHS
- **STRENGTHS:**
  - Addressing occult viral contamination in public cell-line RNA-seq repositories is an important quality-control problem.
  - Testing the mapping pipeline on true positive control datasets (`GSE65485` HBV and `GSE187420` SARS-CoV-2) with genome coverage visualization (IGV tracks in Figure 1e) is a sensible starting validation.
- **Claim Evaluation:**
  - *Claim that ~10% (110/1,021) of MCF7 RNA-seq datasets are contaminated with 6 viruses including BeAn 58058, HERV-K113, WHV, and HIV-1:* `[Methodologically Flawed]` — Confounds `BeAn 58058` alignment artifacts, endogenous human retroviruses (`HERV-K113`), and lentiviral vector backbone sequences (`HIV-1` / `WPRE` from `WHV`) with exogenous viral contamination.
  - *Claim that the 12-gene RF biomarker panel accurately detects viral infection across cell lines:* `[Overstated]` — Dominated by KRAB-ZNF genes correlating with HERV-K / lentiviral transduction pseudo-labels, with only 60% specificity (true-infected recall when majority/minority labels are untangled).

### 4. Reproducibility & Data Completeness
- Public GEO/SRA accessions (`GSE65485`, `GSE187420`, `GSE198398`, `SRP065220`, `SRP142602`, `SRP163132`) are provided, but no GitHub/code repository URL for `ViralCellDetector` is included in the manuscript text (Footnotes 1–4 are stripped/unlinked).
</Blinded Review: TIME_ANON_0670>
