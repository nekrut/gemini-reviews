# Blinded Review: TIME_ANON_38
**Composite Score:** 3.7 / 10.0 (Rigor: 1.1/3.5 | Claims: 0.9/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.9/2.0)
**Bias Category:** Template Bioinformatics Pipeline Overreach, HeLa-Contaminated Cell Line (BGC823), and Pervasive Gene/Count Inconsistencies
**Verdict:** Reject
**Study Modality:** Hybrid Computational + Wet-Lab Functional Validation
**Technology Maturity:** Commodity/Hype-Cycle Template
**Epistemic Stage:** Translational/Preclinical/Biomarker

---

### 1. Executive Summary

This manuscript combines secondary bioinformatic mining of public gastric cancer (GC) transcriptomic datasets (`GSE79973`, $n = 10$ tumor/normal pairs; and `TCGA-STAD`, $n = 375$ tumors and $32$ normal tissues) with *in vitro* siRNA knockdown experiments in cultured cells. By intersecting differentially expressed genes (DEGs) across `GSE79973` and `TCGA`, constructing a STRING/MCODE protein-protein interaction (PPI) module, and intersecting KEGG pathways (`ECM-receptor interaction` and `Protein digestion and absorption`), the authors select a 7-gene extracellular matrix (ECM) signature (`COL1A1`, `COL3A1`, `COL10A1`, `COL11A1`, `COMP`, `SPP1`, `THBS2`). They then scan promoter regions with `CiiiDER` to predict `CTCF` binding motifs, display public `ENCODE` ChIP-seq tracks (`H3K27ac`, `H3K4me3`), correlate `CTCF` with Wnt pathway transcripts in `GEPIA`, and perform siRNA knockdown of `CTCF`, `COL1A1`, and `COL3A1` in `BGC823` cells to measure cell viability (MTT) and migration (wound healing).

This study follows a formulaic bioinformatic template and exhibits severe methodological, biological, and editorial flaws: (1) all functional wet-lab knockdown, proliferation, and migration assays (Figure 7) were conducted exclusively in `BGC823`, a cell line notoriously cross-contaminated by HeLa (cervical adenocarcinoma) rather than authentic gastric cancer; (2) the manuscript repeatedly confuses `COL3A1` (collagen type III alpha 1) with non-existent human gene symbols `COL1A3` and `COLA31`, and repeatedly contradicts itself on whether there are 6 or 7 hub genes and which cell lines were tested; (3) the claimed "ECM molecular subtype" of GC is merely bulk-tissue differential expression of canonical cancer-associated fibroblast (CAF) stromal collagens without adjustment for tumor purity, TNM stage, or multiple testing; and (4) the claimed `CTCF`–Wnt–ECM regulatory axis rests on unspecific motif scanning and non-gastric `ENCODE` tracks rather than direct chromatin binding or epistatic rescue in GC cells.

---

### 2. Methodological & Statistical Audit

* **Pervasive Arithmetic, Gene-Count, and Gene-Nomenclature Contradictions [Methodologically Flawed]:**
  1. **DEG intersection arithmetic error (line 104):** The text states: *"A total of 221 DEGs were present in both the GSE79973 and TCGA GC datasets, including 95 upregulated genes and 116 downregulated genes (Figure 2A)."* However, $95 + 116 = 211 \neq 221$.
  2. **Six vs. Seven hub genes (lines 96 & 130):** On line 96, the text states: *"Seven genes (COMP, COL10A1, COL11A1, COL3A1, THBS2, and COL1A1) that were shared by both pathways were defined as hub genes"*—listing only **6** genes in parentheses (`SPP1` is omitted). Conversely, on line 130, the text lists all 7 genes (`COL1A1`, `COL3A1`, `COL10A1`, `COL11A1`, `COMP`, `SPP1`, `THBS2`) and in the very next sentence refers to them as *"these six key genes"*.
  3. **Non-existent collagen gene symbols (`COL1A3` and `COLA31` vs. `COL3A1`):** Throughout the Abstract (line 7), Introduction (line 18), Results (line 146), and Discussion (lines 154, 164, 169), the authors refer to `COL1A3` and `COLA31` (*"CTCF regulated COL1A1 and COLA31 expression in vitro. Silencing CTCF or COL1A1/COL1A3 markedly inhibited cell growth..."*), whereas the Methods (line 68), Figure 5, and Figure 7 label the gene `COL3A1`. There is no `COL1A3` gene in the human genome (Type I collagen consists of `COL1A1` and `COL1A2`; `COL3A1` encodes Type III collagen).
  4. **Contradictory cell line lists between text and Figure 4E (lines 68, 122, 125):** Line 68 lists `HGC27` twice in the same sentence. Line 122 states that expression was measured in seven cell lines (`HGC27`, `TGBC11TKB`, `LMSU`, `NCC-StC-K140`, `FU97`, `MKN45`, `AGS`), identifying the four aggressive lines as `TGBC11TKB`, `LMSU`, `NCC-StC-K140`, and `HGC27`. Yet the Figure 4E legend (line 125) states the four aggressive lines are `BGC823, HGC27, LMSU, and NCCStCK140` (`BGC823` replacing `TGBC11TKB`).

* **Confounding by Stromal Admixture and Unadjusted Survival Analysis [Methodologically Flawed]:**
  The seven selected genes (`COL1A1`, `COL3A1`, `COL10A1`, `COL11A1`, `COMP`, `SPP1`, `THBS2`) are classic mesenchymal/desmoplastic stroma markers predominantly secreted by cancer-associated fibroblasts (CAFs) rather than gastric epithelial carcinoma cells. In `TCGA-STAD`, advanced T-stage (invasion into muscularis propria/serosa, T2–T4 vs. T1) is strongly associated with lower tumor purity and higher stromal fraction. The authors' own Figure 3B–C confirms that expression of these genes correlates exclusively with T stage (depth of invasion) and not with N stage, M stage, or histological grade. Dichotomizing `TCGA-STAD` at the median signature score yields a marginal univariable log-rank $p = 0.028$ (Figure 3A) without specifying how the 7 genes were weighted or combined, and without multivariable Cox adjustment for age or TNM stage.

* **Asymmetric DEG Thresholds and Uninformative Motif Scanning [Fragile]:**
  DEGs were called using $|\log_2\text{FC}| \ge 1$ in `GSE79973` (microarray) and $|\log_2\text{FC}| \ge 2$ in `TCGA` (RNA-seq) without justification for the asymmetric fold-change cutoffs. In Figure 5A, scanning $2.5\text{ kb}$ windows ($-2000$ to $+500\text{ bp}$ around the TSS) with `CiiiDER` at a permissive deficit threshold of $0.15$ without background permutation enrichment testing will trivially identify putative `CTCF` and general TF motifs in almost any set of GC-rich human promoters. Furthermore, the Abstract claims that putative `CTCF` elements *"were confirmed by chromatin immunoprecipitation sequencing (ChIP-Seq)"*, when in reality the authors neither performed ChIP-Seq nor analyzed gastric cancer ChIP-Seq data, but merely viewed a single public `ENCODE` track (`ENCBS630AAA`, line 53).

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **Reliance on a Known HeLa-Contaminated Cell Line (`BGC823`) for All Functional Assays [Methodologically Flawed]:**
  Every functional perturbation in the paper—`CTCF` siRNA downregulating `COL1A1`/`COL3A1` mRNA (Figure 7B), MTT cell viability reduction (Figure 7C), and scratch wound-healing inhibition (Figure 7D)—was performed in a single cell line, `BGC823`. `BGC823` is documented in the International Cell Line Authentication Committee (ICLAC) register and `Cellosaurus` (`CVCL_3360`) as a contaminated HeLa derivative (human papillomavirus-positive cervical adenocarcinoma) rather than a valid human gastric cancer model. No short tandem repeat (STR) authentication is reported, and the intended second cell line mentioned in the Methods (`HGC27`, line 68) is never shown in the functional knockdown assays of Figure 7B–D.

* **Unsupported Causal Claims Linking `CTCF`, Wnt Signaling, and ECM Remodeling [Overstated]:**
  In the Discussion (line 162), the authors conclude: *"Our results have identified a CTCF/WNT axis that controls GC migration through ECM regulation via the canonical Wnt/β-catenin signaling"*, and cite a `Supplementary Figure 3` claiming `WNT5` and `WNT3` changes that are never mentioned anywhere in the Results section. In the main text (Figure 6E), the evidence linking `CTCF` to Wnt consists solely of bulk RNA-seq housekeeping co-expression correlations in `GEPIA` between `CTCF` and general chromatin/signaling regulators (`SMAD4`, `APC`, `GSK3B`, `TCF7L2`), which routinely correlate across bulk TCGA datasets due to global transcriptional and proliferation/purity gradients.

---

### 4. Reproducibility & Data Completeness

Reproducibility is poor. Aside from the `COL3A1`/`COL1A3`/`COLA31` nomenclature confusion and the `BGC823`/`TGBC11TKB` cell-line discrepancy, the RT-qPCR Methods section (line 73) contains a contradictory kit description, stating that mRNA was reverse-transcribed with `PrimeScript RT Master Mix` and in the immediately following sentence stating that total RNA was transcribed with the `Mir-X™ RNA first-strand synthesis kit` (which is a microRNA poly(A)-tailing kit). None of the eight supplementary tables (`Supplementary Tables 1–8`, containing the siRNA sequences, qPCR primer sequences, and DEG lists) are included in the manuscript text.
