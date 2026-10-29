<Blinded Review: TIME_ANON_0987>
**Composite Score:** 5.8 / 10.0 (Rigor: 1.8/3.5 | Claims: 1.5/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.2/2.0)
**Bias Category:** Technical/Assay
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 5.8/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This plant molecular biology study clones the 5' flanking regulatory sequence of the peanut (*Arachis hypogaea* L. cv. 'Luhua 14') NF-YB transcription factor gene *AhLEC1B* (an ortholog of *Arabidopsis LEC1-LIKE* [*AtL1L* / *NF-YB6*]) via genome walking, maps its transcription start site (TSS, $83\ \text{bp}$ upstream of the ATG start codon) by 5' RACE, predicts putative *cis*-regulatory motifs using `PLACE` and `PlantCARE`, and evaluates six 5'- and/or 3'-deletion promoter fragments (`Q1`–`Q6`) fused to the $\beta$-glucuronidase (*GUS*) reporter in stably transformed heterologous *Arabidopsis thaliana* (Col-0, $\ge 6$ independent $T_2$ lines per construct). Histochemical GUS staining indicates that the longest fragment (`Q1`, $1,281\ \text{bp}$: $1,229\ \text{bp}$ upstream promoter + $52\ \text{bp}$ 5' UTR) restricts expression preferentially to developing embryos, 5'-deleted fragments (`Q4`, `Q5`, `Q6`, down to $66\ \text{bp}$ upstream promoter + $52\ \text{bp}$ 5' UTR) drive constitutive GUS staining across vegetative and reproductive tissues, and 3'-deleted fragments lacking the proximal $351\ \text{bp}$ (`Q2`, `Q3`) lose all promoter activity. While the 5' RACE TSS mapping and basic 5'/3' deletion series in transgenic *Arabidopsis* establish the core promoter region and suggest upstream vegetative repression analogous to *AtLEC1*, the study relies exclusively on qualitative histochemical X-Gluc staining without quantitative fluorometric MUG or qRT-PCR assays, over-interprets short 4-bp `PLACE`/`PlantCARE` sequence matches, and contains internal base-pair length discrepancies across sections.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES

#### STRENGTHS
- **Empirical TSS determination via 5' RACE prior to promoter deletion design:** Using decapped full-length mRNA ligation (`GeneRacer`) from developing peanut seeds (10–70 DAP) accurately anchors the TSS (+1) $83\ \text{bp}$ upstream of the translation initiation codon before interpreting core promoter elements (TATA box at $-36\ \text{bp}$).
- **Replication across $\ge 6$ independent single-copy $T_2$ transgenic lines per construct:** Testing at least six independent *Arabidopsis* transformants per deletion construct (`Q1`–`Q6`) alongside wild-type negative (`CK-N`) and `35S:GUS` positive (`CK-P`) controls mitigates T-DNA integration position artifacts.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Exclusively qualitative histochemical X-Gluc staining without quantitative MUG fluorometry or *GUS* transcript quantification:** All functional conclusions regarding promoter strength and tissue specificity across `Q1`–`Q6` rest solely on visual inspection of overnight/24 h X-Gluc histochemical staining photographs (Fig. 6). Extended (24 h) X-Gluc incubation saturates strong signals and can produce oxidative diffusion artifacts in small tissues; no quantitative 4-methylumbelliferyl-$\beta$-D-glucuronide (MUG) fluorometric enzymatic assays or *GUS* qRT-PCR measurements with statistical error bars were performed.
- **Internal inconsistencies in reported sequence lengths across Abstract, Results, and Discussion:**
  - In Results line 91, the GenomeWalker fragment is described as *"1289 bp in length including the promoter region (1235bp) and 5'UTR sequences (54bp)"* ($1235 + 54 = 1289\ \text{bp}$).
  - In Results line 107, the sequence submitted to `PLACE`/`PlantCARE` is *"1318 bp sequences containing 1235 bp promoter region and 83 bp 5'UTR"* ($1235 + 83 = 1318\ \text{bp}$).
  - In Results line 114, `Q1` is *"1281bp containing 1229bp promoter region and 52bp 5' UTR"* ($1229 + 52 = 1281\ \text{bp}$), and `Q6` is *"118bp including 66bp promoter region and 52bp 5' UTR"* ($66 + 52 = 118\ \text{bp}$).
  - However, the Abstract (line 7) and Discussion (lines 157, 159) repeatedly refer to the `Q6` proximal promoter region as **"65bp"** (*"65bp proximal promoter region and the 52bp 5' UTR"*), contradicting the `66bp` reported in Results line 114 ($65 + 52 = 117 \ne 118$).
- **Over-interpretation of 4-bp `PLACE` motif matches and speculative "co-regulation by binding of upstream genes":**
  - Table 2 and Results/Discussion catalog 4-bp and 5-bp degenerate sequences from `PLACE`—such as `AAAG` (`DOF CORE`, 17 copies), `YACT` (`CACTFT`, 22 copies), `GATA` (`GATA BOX`, 12 copies), `TGAC` (`WRKY71OS`, 4 copies), and `ATATT` (`ROOT MOTIF`, 15 copies). A 4-bp motif (`AAAG` or `GATA`) occurs by pure chance once every $256\ \text{bp}$ on each strand ($\sim 10$ times in $1,318\ \text{bp}$), and `YACT` occurs once every $128\ \text{bp}$ ($\sim 20$ times in $1,318\ \text{bp}$).
  - No electrophoretic mobility shift assay (EMSA), yeast one-hybrid (Y1H), ChIP, or site-directed mutagenesis of the putative `-1149 bp` `RY REPEAT` (`CATGCA`) was performed, yet the Abstract claims as a result that *"AhLEC1B is preferentially expressed in the embryo and is co-regulated by binding of its upstream genes with both positive and negative corresponding cis-regulatory elements."*
- **Minor typos in Methods:** Line 83 refers to *"MAGE 4.0"* instead of *"MEGA 4.0"*, and line 73 refers to *"0.1% (v/v) HgCl"* instead of *"0.1% (w/v) $\text{HgCl}_2$"* (mercuric chloride is a solid salt, and mercurous chloride $\text{HgCl}$ is insoluble).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim that the full-length $1,281\ \text{bp}$ *AhLEC1B* 5' region (`Q1`) drives embryo-preferential GUS expression in transgenic *Arabidopsis*, whereas 5' deletions (`Q4`–`Q6`) derepress vegetative expression:** `[Well Supported]` — Clearly demonstrated by the qualitative shift from embryo-restricted staining in `Q1` to constitutive whole-plant staining in `Q4`–`Q6` (Fig. 6), paralleling the known *turnip* (*tnp*) distal promoter deletion phenotype of *Arabidopsis LEC1*.
- **Claim that the proximal $66\ \text{bp}$ promoter + $52\ \text{bp}$ 5' UTR (`Q6`) is sufficient for basal constitutive promoter activity, and deleting the proximal $351\ \text{bp}$ (`Q2`, `Q3`) abolishes activity:** `[Well Supported]` — Directly supported by comparing `Q6` (active) vs. `Q2`/`Q3` (inactive, lacking the TATA box and TSS).
- **Claim that *AhLEC1B* is regulated by physical binding of VAL, WRKY71, and AGL15 to predicted motifs:** `[Overstated]` — Based purely on in silico `PLACE`/`PlantCARE` string matching without protein–DNA binding or point-mutation assays.

### 4. Reproducibility & Data Completeness
All 17 oligonucleotide primer sequences (`BD GenomeWalker`, `GeneRacer`, and deletion primers `BF1`–`BF5`, `BR1`–`BR2`) are provided in Table 1, and the full annotated sequence is included in Figure 4 and Supporting Information (`S1 Fig`).
</Blinded Review: TIME_ANON_0987>
