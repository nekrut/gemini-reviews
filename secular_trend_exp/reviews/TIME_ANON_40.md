# Blinded Review: TIME_ANON_40
**Composite Score:** 7.9 / 10.0 (Rigor: 2.5/3.5 | Claims: 2.0/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.7/2.0)
**Bias Category:** Unadjusted Multiple Hypothesis Testing Across 15+ Genes and Unmodeled Within-Subject Biopsy Pairing
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Epidemiological Observational

---

### 1. Executive Summary

This study profiles the mucosal mRNA expression of 15 Th17 pathway-related and proinflammatory genes—including effector cytokines (`IL17A`, `IL17F`, `IL21`, `IL22`, `IL26`), differentiation/signaling factors (`IL6`, `IL1B`, `TGFB1`, `IL23A`, `STAT3`, `RORC`/`RORC1`), recruitment chemokines/receptors (`CCR6`, `CCL20`), and inflammatory markers (`IL8`, `TNF`)—across 72 macrodissected colonic and ileal endoscopic biopsies collected from 22 healthy controls, 12 patients with ulcerative colitis (UC), and 26 patients with Crohn's disease (CD). Using MIQE-compliant quantitative real-time RT-PCR normalized to the geometric mean of three reference genes (`GAPDH`, `SDHA`, `HPRT` validated by `geNorm`), the authors show that while active colonic inflammation in both UC and CD induces the full Th17 transcriptional program (differentiation factors `IL1B`, `IL6`, `TGFB1`, `IL23A`, `STAT3`; recruitment factors `CCR6`, `CCL20`; and all five effector cytokines), active ileal CD exhibits induction of `IL22` ($p = 0.0015$), `IL1B` ($p = 0.0007$), and `IL8` ($p < 0.0001$) without induction of `TGFB1`, `IL23A`, `STAT3`, `CCR6`, `CCL20`, or `IL21`, alongside reduced expression of the master transcription factor `RORC` ($p = 0.0019$).

The molecular assay execution and MIQE reporting are of high quality, and the central biological contrast between colonic and ileal Th17 pathway regulation is supported by strong effect sizes on the core differentiation and recruitment genes ($p \le 0.001$). The primary methodological limitations are: (1) reliance on unadjusted Mann-Whitney $U$ tests at $p < 0.05$ across more than 60 gene-by-group comparisons, which inflates false-positive risk for the "weakly induced" transcripts ($0.01 < p < 0.05$); (2) treating 72 biopsies from 60 subjects as statistically independent observations when at least 7 healthy controls and 5 CD patients contributed paired colonic and ileal biopsies; and (3) a 20-year mean age gap between healthy controls (51–55 years) and CD patients (30–32 years).

---

### 2. Methodological & Statistical Audit

* **Unadjusted Multiple Hypothesis Testing Across 15 Genes and Multiple Contrasts [Moderately Supported]:**
  The authors evaluate 15 target genes (16 primer sets) across five main pairwise contrasts (healthy ileum vs. healthy colon; UC colon vs. control colon; CD colon vs. control colon; CD ileum vs. control ileum; UC colon vs. CD colon; plus CD colon vs. CD ileum), totaling $>75$ statistical tests, using an unadjusted nominal significance threshold of $p < 0.05$ (line 177). While the primary findings emphasized in the Abstract and Conclusions (such as `TGFB1` $p = 0.0005$ and `CCR6` $p = 0.0008$ in healthy ileum vs. colon; strong induction of `IL8`, `IL17A`, `IL22`, `IL1B`, `IL6`, `TGFB1`, `IL23A`, `CCR6`, and `CCL20` in inflamed UC and CD colon at $p \le 0.001$; and reduced `RORC` in ileal CD at $p = 0.0019$) easily survive Benjamini-Hochberg false discovery rate (FDR) control at $q < 0.05$, several marginal effects highlighted in the Results—such as higher `TNF` in healthy ileum ($p = 0.037$), weak induction of `IL17F` in UC ($p = 0.046$), `IL21` ($p = 0.047$) and `IL26` ($p = 0.048$) in colonic CD, and `IL26` ($p = 0.029$), `IL17F` ($p = 0.019$), and `IL6` ($p = 0.015$) in ileal CD—would not survive formal multiplicity correction and should be interpreted cautiously.

* **Unmodeled Within-Subject Clustering of Colonic and Ileal Biopsies [Fragile]:**
  In the Abstract (line 7) and Methods (line 114), the cohort comprises $22$ healthy controls, $12$ UC patients, and $26$ CD patients ($60$ total individuals), from whom $72$ macrodissected biopsy specimens were analyzed (Table 1: $13$ healthy colonic + $16$ healthy ileal $= 29$ control biopsies from $22$ subjects; $15$ inflamed CD colonic + $16$ inflamed CD ileal $= 31$ CD biopsies from $26$ CD patients; and $12$ UC colonic biopsies from $12$ UC patients). Thus, at least $7$ of the $22$ healthy controls and at least $5$ of the $26$ CD patients contributed both a colonic and an ileal biopsy. Comparing colonic vs. ileal healthy controls ($n=13$ vs. $n=16$) and colonic vs. ileal CD ($n=15$ vs. $n=16$) via an unpaired Mann-Whitney $U$ test violates the independence assumption for the paired subset. Using a linear mixed-effects model with a patient random intercept (or reporting a sensitivity analysis restricted to independent subjects / Wilcoxon signed-rank on the paired subset) is needed.

* **Imputation of Non-Detects (`Cq = 45`) and Demographic Imbalance [Moderately Supported]:**
  In healthy controls, the five Th17 effector cytokines (`IL17A`, `IL17F`, `IL21`, `IL22`, `IL26`) were below the detection limit in a substantial fraction of biopsies (line 39), and flattened melting curves / non-detects were assigned `Cq = 45` (line 147). Because the $2^{-\Delta\Delta C_q}$ transformation is non-linear and sensitive to the reference gene $C_q$ of each sample when `Cq` is fixed at 45, reporting the exact detection frequency (Fisher's exact test on proportion detected) alongside the rank-based comparison would strengthen Figure 1B and 2B. Additionally, Table 1 reveals that healthy controls (recruited from polyp/cancer screening colonoscopies) were ~20 years older than CD patients (mean age 55 vs. 30 years in colon; 51 vs. 32 years in ileum) and predominantly female in the colonic control group (4M/9F vs. 9M/3F in UC and 10M/5F in CD).

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **Tissue-Specific Basal Immune Architecture Explaining Lack of Ileal Fold-Change [Well Supported]:**
  A notable strength of the study is that it does not examine IBD biopsies in isolation, but first establishes baseline differences between normal ileum and normal colon (Figure 1). Because normal terminal ileum already contains Peyer's patches and isolated lymphoid follicles with significantly higher basal expression of `TGFB1` ($p = 0.0005$), `STAT3` ($p = 0.007$), and `CCR6` ($p = 0.0008$) than normal colon (and strong basal correlation between `TGFB1` and `CCR6`, $r = 0.785, p = 0.0003$), the lack of additional fold-induction of `TGFB1`, `STAT3`, and `CCR6` in inflamed ileal CD relative to ileal controls (Figure 2C–D) partly reflects this elevated physiological baseline in the ileum, whereas the drop in `RORC` ($p = 0.0019$, Figure 3B) and absence of `IL23A`/`CCL20` induction indicate genuine divergence from colonic inflammation. The Discussion (lines 92–95) thoughtfully considers innate non-Th17 cellular sources of `IL-17A` and `IL-22` in the ileum (such as Paneth cells, LTi-like cells, and NK/Th22 cells).

---

### 4. Reproducibility & Data Completeness

The qPCR methodology and reporting (lines 140–172, Table 2) are exemplary and adhere strictly to the MIQE guidelines: RNA integrity numbers (`RQI` range $7.4\text{--}10$, mean $8.6$), `WT-Ovation` pre-amplification input ($20\text{ ng}$), robotic liquid handling CVs, intronic gDNA contamination controls, 6-point dilution series PCR efficiencies ($88\%\text{--}112\%$), $R^2$ values ($0.9843\text{--}1.000$), amplicon lengths, RefSeq accessions (noting a minor extra zero typo in `TGFB1` accession `NM_0006600` for `NM_000660` in Table 2), and exon-spanning locations for all 19 primer pairs are fully tabulated. Adding Benjamini-Hochberg FDR-adjusted $q$-values and accounting for within-patient biopsy pairing would bring the statistical analysis up to the same high standard as the wet-lab qPCR execution.
