<Blinded Review: TIME_ANON_0742>
**Composite Score:** 5.8 / 10.0 (Rigor: 1.8/3.5 | Claims: 1.3/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.2/2.0)
**Scientific Core Score:** 4.6 / 8.0
**Bias Category:** Over-Interpretation/Clinical
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 5.8/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary (SUMMARY)
This hybrid experimental and transcriptomic study investigates the role of $N^6$-methyladenosine ($\text{m}^6\text{A}$) RNA methylation in Human T-cell Leukemia Virus Type 1 (`HTLV-1`) gene expression and downstream host target regulation in the HTLV-1-infected T-cell line `C91/PL`. Combining *in silico* `SRAMP` prediction, secondary reanalysis of public `MT-4` MeRIP-seq data, anti-$\text{m}^6\text{A}$ RIP-qPCR, pharmacological METTL3/14 inhibition (`STM2457`, `10–50 µM`), lentiviral `METTL3` shRNA knockdown (`shMETTL3#1/#2`), Actinomycin D RNA decay assays, p19 Gag ELISA, and bulk RNA-seq, the authors show that global METTL3 inhibition or knockdown destabilizes *tax* mRNA, lowers Tax protein and extracellular p19 Gag levels, and reduces expression of Tax-activated host genes (*IL2RA*/CD25 and *TXN*) without altering *IL2RA* mRNA stability. While the concordant inhibitor and shRNA experiments support a role for METTL3 activity in maintaining *tax* mRNA abundance, the manuscript overstates its specificity by claiming "targeted depletion of $\text{m}^6\text{A}$ modification within the viral transactivator HTLV-1 Tax" when only global cellular METTL3 inhibition/knockdown was performed, contains a major bioinformatic contradiction in its MeRIP-seq viral alignment method, omits the differential expression software and all qPCR primer sequences, and fails to deposit raw RNA-seq data publicly.

### 2. Methodological & Statistical Audit (STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT)
**Strengths:**
- **Orthogonal Validation of Chemical Inhibition with Genetic Knockdown:** Key findings obtained with the catalytic METTL3 inhibitor `STM2457` (reduced *tax* mRNA, Tax protein, and downstream *IL2RA*/*TXN* expression) are corroborated using two independent `METTL3` shRNAs (`Figures 2D–E, 3E`).
- **Specificity Controls for Downstream *IL2RA* Regulation:** By demonstrating that `STM2457` downregulates *IL2RA* and *TXN* in HTLV-1-positive `C91/PL` cells but not in HTLV-1-negative `Molt4` cells (`Figure 3D`), and that `STM2457` does not reduce *IL2RA* mRNA half-life (`Figure 4D`), the authors reasonably argue that *IL2RA* suppression is secondary to Tax loss rather than direct $\text{m}^6\text{A}$ destabilization of *IL2RA* mRNA.

**Weaknesses & Methodological Flaws:**
- **False Claim of "Targeted Depletion of $\text{m}^6\text{A}$ Within HTLV-1 Tax" (`Abstract line 7`):** The Abstract claims: *"Moreover, targeted depletion of m6A modification within the viral transactivator HTLV-1 Tax resulted in markedly destabilized Tax mRNA..."* No targeted epitranscriptomic editing (e.g., dCas13-ALKBH5 targeting *tax*) or synonymous mutagenesis of $\text{m}^6\text{A}$ `DRACH` motifs within *tax* was performed anywhere in the study. Both `STM2457` (`10–50 µM` for 72 h) and `shMETTL3` globally inhibit METTL3 across the entire host and viral transcriptome (altering `2,246` host genes in `Figure 3B` and reducing cell viability in `Figure 3F`). Because global METTL3 depletion alters hundreds of host transcription and splicing factors, the experiment does not prove that cis-methylation on *tax* mRNA itself—rather than a METTL3-dependent host factor—stabilizes *tax*.
- **Internal Contradiction in the MeRIP-Seq Viral Mapping Pipeline (`lines 37 vs. 147`):** In Results (`line 37`), the authors state they reanalyzed public MeRIP-seq data from `MT-4` cells (`SRR2648293–297`) and *"identified a peak between bases 7109–7439 of the 8507 bp HTLV-1 genome (`Figure 1B`)."* However, in Experimental Procedures (`line 147`, *MeRIP-Seq Secondary Analysis*), they state: *"The processed reads were mapped to the human reference genome (hg38, obtained from NCBI) using HISAT2 (v2.2.1)."* Standard `hg38` does not contain the `NC_001436.1` HTLV-1 proviral sequence; how viral reads were mapped and how `MACS2` called peaks on an 8.5-kb viral genome are not explained.
- **Incomplete and Inaccurate RNA-Seq Bioinformatic Description (`line 142`):** The RNA-seq methods state that `Trimmomatic v0.30`, `HISAT2 v2.0.1`, and `HTSeq v0.6.1` were used, and claim that *"For differentially expressed gene analysis, HTSeq (v0.6.1) estimated gene and converted read counts to transcripts per million (TPM)."* `HTSeq` only counts mapped reads and neither converts counts to TPM nor computes adjusted $p$-values (`p_adj < 0.05` in `Figure 3B`); the statistical package (`DESeq2`, `edgeR`, or `limma`) and biological replicate count ($n$) used for the RNA-seq experiment (`Figure 3A–B`) are completely omitted.
- **Unadjusted Multiple Comparisons (`line 152`):** Dose-response experiments (`0, 10, 25, 50 µM STM2457` in `Figures 2A, 2F, 3D, 3F, 4B, 4C`) were analyzed by repeated pairwise Student's $t$-tests without ANOVA or Dunnett's post-hoc correction.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *HTLV-1 tax and hbz transcripts carry $\text{m}^6\text{A}$ modifications in C91/PL cells.* `[Well Supported]` — Supported by anti-$\text{m}^6\text{A}$ RIP-qPCR with IgG and `STM2457` pretreatment controls (`Figure 1C`).
- **Claim 2:** *Global METTL3 inhibition (`STM2457`) or knockdown (`shMETTL3`) reduces tax mRNA stability, Tax protein abundance, p19 Gag release, and downstream IL2RA/CD25 expression.* `[Well Supported]` — Supported by concordant inhibitor and shRNA experiments (`Figures 2–4`).
- **Claim 3:** *Targeted depletion of $\text{m}^6\text{A}$ specifically within Tax mRNA destabilizes Tax.* `[Overstated]` — Only global cellular METTL3 inhibition/knockdown was performed; cis-acting $\text{m}^6\text{A}$ sites in *tax* were never mutated or specifically demethylated.

### 4. Reproducibility & Data Completeness
- **Strengths:** Provides shRNA target sequences (`shCtrl`, `shMETTL3#1`, `shMETTL3#2`), antibody catalog numbers, and SRA accessions (`SRR2648293–297`) for the reanalyzed `MT-4` dataset.
- **Weaknesses:**
  1. **Complete Omission of Primer Sequences:** None of the RT-qPCR or RIP-qPCR primer sequences (*tax, hbz, NOTCH1, IL2RA, TXN, VCAM1*, or the unnamed internal reference gene) are provided in the text or supplementary tables.
  2. **Missing Raw RNA-Seq Deposition:** The newly generated `C91/PL` RNA-seq raw reads are not deposited in GEO/SRA/DDBJ ("available from the corresponding author upon reasonable request").
  3. **Scrubbing Artifact in Centrifugation Speed (`line 102`):** Spinoculation speed is printed as `"[YEAR] x g for 2 h at 35°C"` (likely a 4-digit speed such as `1200` or `2000` caught by automated year regex scrubbing, which is a preprocessing artifact rather than an author error).
</Blinded Review: TIME_ANON_0742>
