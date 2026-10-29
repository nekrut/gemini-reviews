<Blinded Review: TIME_ANON_0748>
**Composite Score:** 5.5 / 10.0 (Rigor: 1.5/3.5 | Claims: 1.6/2.5 | Biology: 1.5/2.0 | Reproducibility: 0.9/2.0)
**Scientific Core Score:** 4.6 / 8.0
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 5.5/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary (SUMMARY)
This cross-species microarray study profiles endometrial gene expression between the estrogen-dominant proliferative phase (Day 13) and the progesterone-dominant secretory phase / window of implantation (Days 21–23) in artificially cycled Rhesus monkeys using human Affymetrix `HG-U95A` oligonucleotide arrays (~12,686 probe sets). Using `dChip` model-based expression estimates and a mixed-model ANOVA (`SAS PROC MIXED`, `FDR < 5%`, fold change $>2$), the authors report 108 differentially expressed genes (39 up-regulated and 69 down-regulated in the secretory phase), highlight known progesterone-responsive endometrial markers (*SLPI*, uteroglobin, *H2A*, *PLK*, *SAT2*, *MT1G*, *TGFBI*, *MMP11*, *PENK*, *SFRP4*), and confirm temporal induction of *SLPI* and *WFDC2* across cycle days 13–26 by semi-quantitative RT-PCR. While the primate model and the concordance of top hits with human endometrial biology are strengths, the study suffers from a classic microarray pseudoreplication flaw: RNA from the individual monkeys ($n = 3$ at Day 13; $n = 3$ each at Days 21 and 23) was pooled into a single sample per phase prior to cDNA synthesis, and $N = 5$ technical IVT/hybridization replicates of those two pools were analyzed by ANOVA as if they were independent replicates. Furthermore, `Tables 1` and `2` (the actual lists of 39 up-regulated and 69 down-regulated genes) are missing from the manuscript body, and no housekeeping loading control is shown in the RT-PCR validation gel.

### 2. Methodological & Statistical Audit (STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT)
**Strengths:**
- **Controlled Primate Artificial Menstrual Cycle Model:** Timed silastic estradiol and progesterone implants in ovariectomized Rhesus monkeys (`lines 31–37`) provide precisely staged proliferative (Day 13) and receptive secretory (Days 21–23) endometrial tissue free of natural ovulatory timing variance.
- **Temporal Multi-Timepoint RT-PCR Follow-Up (`Figure 2`):** Validates two Whey Acidic Protein (`WAP`) family members (*SLPI* and *WFDC2*) across 6 distinct cycle timepoints (`Days 13, 14, 17, 21, 23, and 26`), demonstrating peak expression during the Day 17–23 implantation window.

**Weaknesses & Methodological Flaws:**
- **Pooling of All Biological Replicates Prior to Labelling (Technical Pseudoreplication in Mixed-Model ANOVA, `lines 42, 47, 56, 73`):** As described in Methods (`lines 42, 47`) and Results (`line 73`), $1\text{ }\mu\text{g}$ of poly(A)+ RNA from each of the 3 animals per timepoint was pooled into a single tube prior to cDNA synthesis (`Day 13 pool` vs. `Days 21+23 pool`). Five separate IVT probe reactions and chip hybridizations (`N = 5`) were then performed from the *same pooled cDNA* for each condition and analyzed by mixed-model ANOVA (`PROC MIXED`) with Benjamini–Hochberg `FDR < 5%`. Because biological variation across individual monkeys was collapsed into a single pool per group ($n_{\text{biological}} = 1$ per group), the residual error term in the ANOVA measures only *technical IVT/hybridization variance*, not animal-to-animal biological variance. Consequently, the reported `FDR < 5%` p-values test only whether the two RNA pools differ technically, not whether the proliferative and secretory populations differ statistically across animals.
- **Cross-Species Hybridization Dropout Caveat (`Rhesus` cRNA on `Human HG-U95A` 25-mer Probes):** While the authors note that cross-species primate hybridization is feasible (`line 24`) and thoughtfully emphasize known positive controls (`line 121`), single-nucleotide mismatches between Rhesus transcripts and human 25-mer oligonucleotide probes systematically depress PM/MM hybridization signals for diverging transcripts.
- **Absence of Internal Loading Control in Semi-Quantitative RT-PCR (`Figure 2`, `lines 61–66`):** `Figure 2` presents ethidium-bromide gels for *SLPI* (30 cycles) and *WFDC2* (25 cycles) across cycle days 13–26 (`40 ng` template cDNA per reaction) without a parallel housekeeping gene control (e.g., *GAPDH* or *ACTB*) to verify uniform cDNA input and reverse-transcription efficiency across the 6 timepoint pools.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *Known progesterone-regulated endometrial markers (such as SLPI, WFDC2, uteroglobin, SAT2, TGFBI, MMP11, PENK, and SFRP4) are strongly differentially expressed between proliferative (Day 13) and secretory (Days 21–23) Rhesus monkey endometrium.* `[Well Supported]` — Concordant with prior human and primate Northern blot, in situ hybridization, and microarray studies, and confirmed across 6 cycle days for *SLPI* and *WFDC2* (`Figure 2`).
- **Claim 2:** *Mixed-model ANOVA identifies 108 statistically significant genes at FDR < 5% between proliferative and secretory phases.* `[Methodologically Flawed]` — The `FDR < 5%` test is based on $N = 5$ technical array replicates of a single pooled RNA sample per condition rather than independent biological replicates.

### 4. Reproducibility & Data Completeness
- **Strengths:** Detailed descriptions of RNA isolation, ENZO IVT labeling, Affymetrix hybridization cocktail composition, `dChip` Li–Wong normalization, and RT-PCR primer sequences (`SLPI` and `WFDC2`) are provided.
- **Weaknesses:**
  1. **Missing `Table 1` and `Table 2` Contents (`lines 130–132`):** Only the stub titles `"Table 1. Genes up-regulated during the secretory phase"` and `"Table 2. Genes down-regulated during the secretory phase"` appear at the end of the text; the actual gene tables are absent from the manuscript file.
  2. **No Public Microarray Data Deposition:** Raw `.CEL` files and normalized expression matrices are not deposited in GEO or ArrayExpress.
</Blinded Review: TIME_ANON_0748>
