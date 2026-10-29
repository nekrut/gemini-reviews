# Review of FEXP_ANON_023

**Overall Score:** **5.1 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **3.8 / 8.0**  
* **Score Breakdown:** Rigor: 1.4/3.5 | Claims: 1.1/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.3/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_023`
* **Perceived Research Domain:** Invertebrate mitogenomics, bivalve phylogenetics, and molecular evolution (Bivalvia: Mytilidae).
* **Study Design:** In silico assembly of three complete mussel mitochondrial genomes (*Xenostrobus securis*, *Bathymodiolus puteoserpentis*, and *Gigantidas vrijenhoeki*) from public NCBI SRA read archives, re-annotation of the divergent `atp8` gene across 13 Mytilidae mitogenomes, and comparative phylogenetics/selection scanning across 44 Mytilidae mitogenomes plus 2 outgroups.
* **Primary Methods:** Mitogenome assembly from SRA reads (`Trimmomatic` v0.36, `NOVOPlasty`), annotation (`MITOS2`, `ARWEN` v1.2.3, `ORFfinder`, `TMHMM` v2.0, `ExPASy PROTSCALE`, `HHblits` v3.30 HMM-HMM alignment), phylogenetics (`MUSCLE`, `Gblocks` v0.91b, `ModelTest-NG`, `MrBayes` v3.2.7, `RAxML-NG`), divergence dating (`MCMCtree` in `PAML` v4.9), selection tests (`CODEML` branch and branch-site models in `PAML` v4.9), and homology modeling (`Phyre2`).

---

## 2. Executive Summary & Editorial Verdict

This study assembles complete mitochondrial genomes for three mytilid mussel species (*Xenostrobus securis* `ON128254`, *Bathymodiolus puteoserpentis* `ON128252`, and *Gigantidas vrijenhoeki* `ON128253`) from public NCBI SRA data, searches intergenic regions via manual ORF scanning and `HHblits` HMM-HMM homology to annotate the short, fast-evolving `atp8` gene in 13 mytilid species previously reported to lack it, reconstructs a 12-PCG phylogeny and `MCMCtree` timetree across Mytilidae, and applies `PAML` `CODEML` branch and branch-site models to test for relaxed purifying selection in deep-sea Bathymodiolinae and positive selection in the freshwater golden mussel *Limnoperna fortunei*. The three newly assembled mitogenomes are deposited in GenBank (`ON128252–ON128254`).

Assembling three public SRA datasets into complete mitogenomes and identifying candidate `atp8` ORFs in 6 species supported by `HHblits` HMM homology (`M & HMM` in Table 3) are useful contributions to bivalve mitogenomics. However, the manuscript's broader claims and quantitative analyses suffer from several methodological and factual defects: (1) for 7 of the 13 species in Table 3 (including *L. fortunei*, *X. securis*, and all five *Modiolus* species), `HHblits` failed to detect any sequence/profile homology to ATP8, leaving those annotations solely as unvalidated manual ORFs—and in *Crenomytilus grayanus*, the reported `atp8` gene length in Table 3 (`251 bp` with complete `ATG` start and `TAA` stop codons) is not even divisible by 3 ($251 = 83 \times 3 + 2$, an arithmetic miscalculation of $17,571 - 17,320 + 1 = 252\text{ bp}$); (2) the text in Section "Positive selection analyses" directly contradicts Table 4 regarding the $\omega$ value of `atp6` in freshwater vs. deep-sea branches (claiming freshwater $\omega$ is lower than deep-sea $\omega$, whereas Table 4 reports freshwater $\omega = 0.1179$ vs. deep-sea $\omega = 0.0227$); (3) testing "freshwater adaptation" on a single terminal branch ($n = 1$ species, *L. fortunei*, with an unadjusted boundary estimate $\omega_2 = 209.31$ in `nad4`) confounds species-specific substitutions with ecological adaptation and lacks multiple-testing correction across 24 branch-site tests; and (4) Table 1 omits 10 of the 44 Mytilidae species included in the phylogeny (e.g., all Brachidontinae taxa). These issues can be addressed by revising the text/tables, validating or qualifying manual-only `atp8` ORFs, and correcting the statistical interpretation.

### Specific Assessment of Core Claims

* **Assembly of complete mitogenomes for *X. securis* (14,972 bp), *B. puteoserpentis* (20,482 bp), and *G. vrijenhoeki* (17,786 bp) from SRA data:** **[Well Supported].**  
  The assemblies (`ON128252–ON128254`) match known reference fragments ($99.42\%\text{–}100\%$ identity) and display expected gene complements and strand asymmetry, including four tandem `trnH` duplications expanding the *B. puteoserpentis* genome. However, as the authors note in line 92, whether the *X. securis* assembly (`SRR7751554`) represents an F-type or M-type (Doubly Uniparental Inheritance) mitogenome was not verified.

* **`atp8` is not missing across Mytilidae and is present in all 13 re-examined species:** **[Moderately Supported].**  
  In 6 of the 13 species (*Mytilisepta keenae*, *Lithophaga curta*, *B. puteoserpentis*, *G. vrijenhoeki*, *C. grayanus*, and *Mytilaster solisianus*), candidate ORFs were supported by both manual features and `HHblits` HMM-HMM homology (`M & HMM`, Table 3). However, in the remaining 7 species (*Modiolus* spp., *X. securis*, and *L. fortunei*), `HHblits` found no significant homology to known ATP8 profiles (`M` only, Table 3), and in *M. solisianus* the candidate ORF is abnormally long ($420\text{ bp} = 139\text{ aa}$). Because any A+T-rich intergenic region can harbor short 37–60 aa ORFs containing hydrophobic stretches by chance, claiming functional `atp8` retention in the 7 HMM-negative species without transcriptomic (RNA-seq) read mapping is premature.

* **Phylogenetic division of Mytilidae into two primary clades diverging at 399.37 Mya (95% HPD: 392.74–407.65 Mya) and misidentification of GenBank `KM655841.1` (*"Perna perna"*) as *Mytilaster solisianus*:** **[Moderately Supported].**  
  The two-clade topology and the demonstration that `KM655841.1` shares $99.83\%$ `cox1` identity and gene order with *M. solisianus* rather than *Perna* are well supported. However, claiming that the `MCMCtree` posterior root age (`399.37 Mya`, 95% HPD `392.74–407.65 Mya`; line 141) independently corroborates previous divergence estimates is circular because that node was directly constrained with a `393–408 Mya` fossil calibration prior (line 77).

* **Deep-sea Bathymodiolinae experienced relaxed purifying selection across mitochondrial genes (`atp6`, `cob`, `nad2`, `nad5`):** **[Moderately Supported].**  
  In the `CODEML` Three-ratios branch model (Table 4), deep-sea Bathymodiolinae branches show modestly higher $\omega$ ($0.0227\text{–}0.0591$) than shallow-sea branches ($0.0051\text{–}0.0366$) with significant LRT $p \le 0.001$ in four genes, consistent with lower effective population sizes ($N_e$) or altered metabolic constraints in deep-sea vent/seep habitats. However, the text misstates the `atp6` result for the freshwater branch.

* **Episodic positive selection in `nad4` ($p = 0.002, \omega_2 = 209.31$) contributed to the freshwater adaptation of *Limnoperna fortunei*:** **[Fragile].**  
  First, the "freshwater" foreground in the `CODEML` branch-site test consists of a single terminal branch ($n = 1$ species, *L. fortunei*). Testing a single terminal branch cannot separate adaptive evolution driven by freshwater osmoregulation from lineage-specific neutral drift, relaxed selection, or sequencing artifacts in `KP756905`. Second, $\omega_2 = 209.31$ reflects a boundary estimate caused by near-zero synonymous divergence estimates at the foreground sites. Third, across 12 PCGs tested in both deep-sea and freshwater foregrounds ($24$ branch-site LRTs), an unadjusted $p = 0.002$ ($2\Delta\ln L = 9.38$) is borderline (`p_Bonferroni = 0.048`).

---

## 3. Forensic Defect Inventory

### Defect 1: Direct Contradiction Between Text and Table 4 Regarding Freshwater vs. Deep-Sea $\omega$ for `atp6` (Pillar 4, Pillar 5 & Pillar 7)
* **Location:** Section "Positive selection analyses" (line 156) and Table 4 (line 162).
* **Diagnostic Finding:** In line 156, the authors write: *"In freshwater branches, only the $\omega$ value of atp6 was higher than that of shallow-sea branches, **but still lower than the $\omega$ value of deep-sea branches**."* However, Table 4 (line 162) reports for `atp6`:
  - `Shallow sea (ω) = 0.0051`
  - `Deep-sea (ω) = 0.0227`
  - **`Freshwater (ω) = 0.1179`**
  Thus, the freshwater $\omega$ for `atp6` (`0.1179`) is more than **fivefold higher** than the deep-sea $\omega$ (`0.0227`), directly contradicting the main text. (Additionally, in `cox2`, Freshwater $\omega = 0.0175$ also exceeds Shallow sea $\omega = 0.0025$ and Deep-sea $\omega = 0.0019$, although its LRT is non-significant at $p = 0.756$).
* **Remediation:** Correct line 156 to accurately state that in `atp6`, the freshwater branch $\omega$ (`0.1179`) was substantially higher than both the shallow-sea (`0.0051`) and deep-sea (`0.0227`) branches.

### Defect 2: Non-Triplet Nucleotide Length (`251 bp`) and Count Discrepancy (`12` vs. `13`) in Table 3 `atp8` Annotations (Pillar 6 & Pillar 7)
* **Location:** Section "ATP8 annotation" (line 109) and Table 3 (lines 112–127).
* **Diagnostic Finding:**
  1. **Arithmetic & reading-frame error in Table 3:** For *Crenomytilus grayanus* (`MK721543`, line 126), Table 3 reports `Position (bp): 17,320–17,571`, `Size (bp): 251`, `Start codon: ATG`, `Stop codon: TAA`. First, $17,571 - 17,320 + 1 = 252\text{ bp}$, not $251\text{ bp}$ (the authors forgot to add $1$ when subtracting inclusive 1-based genomic coordinates!). Second, a complete coding sequence with a full start codon (`ATG`) and full stop codon (`TAA`) must be an exact multiple of 3 nucleotides ($252 = 84 \times 3$ codons), whereas $251\text{ bp}$ is not divisible by 3!
  2. **Species count discrepancy (`12` vs. `13`):** Line 109 states *"Twelve atp 8 sequences were manually annotated in the intergenic region (Table 3)"*, whereas Table 3 actually lists **13** species.
* **Remediation:** Correct the `Size (bp)` of *Crenomytilus grayanus* `atp8` in Table 3 from `251` to `252`, and update the text in line 109 from *"Twelve"* to *"Thirteen"*.

### Defect 3: Missing Species in Table 1 (`34` Listed vs. `44` Mytilidae + `2` Outgroups Analyzed) (Pillar 7)
* **Location:** Section "Phylogenetic analyses" (line 37), Table 1 (lines 40–76), Figure 1 caption (line 104).
* **Diagnostic Finding:** Line 37 states that *"The 12 protein-coding genes of 46 sequences were used to reconstruct the phylogenetic relationships [39]. The Crassostrea gigas (AF177226.1) and Atrina pectinata (KC153059.1) served as outgroups (Table 1)."* (44 Mytilidae + 2 outgroups = 46 sequences). However, Table 1 contains only **34** Mytilidae species rows and omits all 10 sequences from the subfamily Brachidontinae (*Geukensia*, *Brachidontes*, *Mytilisepta*, *Perumytilus*, *Semimytilus*) and *"Perna perna"* (`KM655841.1`) that are analyzed in Figures 1, 4, and 5 and discussed in line 151.
* **Remediation:** Add the missing 10 Mytilidae mitogenome accessions and the 2 outgroup accessions to Table 1 so that all 46 analyzed sequences are documented.

### Defect 4: Unverified F-Type vs. M-Type Status for *Xenostrobus securis* and Pervasive Editorial/Taxonomic Typos (Pillar 2 & Pillar 7)
* **Location:** Lines 30, 37, 45, 61, 77, 92, 109, 147, 202.
* **Diagnostic Finding:**
  1. Line 37 states *"In this article, only F-type was included in the analyses"*, but line 92 states *"we cannot rule out the possibility that the mitochondrial genome of X. securis may belong to the M-type"*. Because DUI male (M-type) mitogenomes evolve much faster and under relaxed selection compared to female (F-type) mitogenomes, including an unverified M-type genome in a selection scan can bias background $\omega$ estimates.
  2. In Authors' Contributions (line 202), seven authors are credited as having *"performed the experiments"*, even though no wet-lab experiments were conducted in this study (all assemblies used public NCBI SRA reads).
  3. Frequent taxonomic and technical misspellings appear throughout the text: *"X. secures"* (lines 30, 92, 109), *"Bathmodiolus septemdierm"* (for *Bathymodiolus septemdierum*, line 45), *"B. themophilus"* (line 77), *"B. puteoserpents"* (line 92), *"Brachiodontes"* (line 151), *"16.210"* (period instead of comma for *Modiolus kurilensis* size in Table 1, line 61), *"fossil recode"* (line 77), and *"95% highest posterior density (PHD)"* (line 147).
* **Remediation:** Check the tissue/sex metadata of `SRR7751554` or compare `cox1` against known F-type and M-type *X. securis* sequences to confirm mitotype status, revise the Authors' Contributions statement to reflect computational analysis rather than wet-lab experiments, and correct all taxonomic and typographical errors.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.4** | **3.5** | Standard mitogenome assembly (`NOVOPlasty`) and phylogenetics (`RAxML-NG`/`MrBayes`), but compromised by single-branch ($n=1$) freshwater selection inference with boundary $\omega_2 = 209.31$, circular `MCMCtree` root age validation against the input prior, and unvalidated HMM-negative `atp8` ORFs in 7 species. |
| **2. Claim-to-Evidence Alignment** | **1.1** | **2.5** | Main text directly contradicts Table 4 on `atp6` freshwater vs. deep-sea $\omega$ (`0.1179` vs. `0.0227`); single-species `nad4` branch-site result is overinterpreted as freshwater osmoregulatory adaptation; manual-only `atp8` ORFs lacking HMM homology or RNA-seq support are presented as definitive annotations. |
| **3. Data Integrity & Biological Plausibility** | **1.3** | **2.0** | Three newly assembled mitogenomes (`ON128252–ON128254`) and identification of the mislabeled `KM655841.1` GenBank record are biologically sound, but Table 3 reports a biologically impossible `251 bp` (non-multiple of 3) complete CDS for *C. grayanus* `atp8`, and M-type vs. F-type status of *X. securis* is unresolved. |
| **4. Reproducibility & Data Integrity** | **1.3** | **2.0** | GenBank (`ON128252–ON128254`) and SRA (`SRR7751554`, `ERR3959529`, `SRR10802050`) accessions are provided, but Table 1 omits 10 of the 44 analyzed Mytilidae species, line 109 says 12 species while Table 3 has 13, and numerous taxonomic/numerical typos appear throughout. |
| **Total Composite Score** | **5.1** | **10.0** | **Mixed / Salvageable** (Scientific Core Score: **3.8 / 8.0**) |
