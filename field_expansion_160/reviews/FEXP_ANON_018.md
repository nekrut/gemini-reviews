# Review of FEXP_ANON_018

**Overall Score:** **4.7 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **3.4 / 8.0**  
* **Score Breakdown:** Rigor: 1.2/3.5 | Claims: 1.0/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.3/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_018`
* **Perceived Research Domain:** Viral genomic epidemiology, intra-host viral diversity (iSNV), and host–pathogen metatranscriptomics of SARS-CoV-2.
* **Study Design:** Retrospective cross-sectional and partial longitudinal metatranscriptomic sequencing of $N = 1,067$ nasopharyngeal swabs from RT-qPCR-positive patients in Abu Dhabi, UAE (May–June 2020), yielding 896 high-quality consensus genomes ($<2\%$ gaps) and 637 unique viral sequences.
* **Primary Methods:** Metatranscriptomic read classification (Kraken v0.10.5), reference-guided assembly and variant calling (Pilon v1.23, FreeBayes v1.3.1), intra-host SNV calling (`reditools` v1.0), maximum likelihood phylogenetics (Nextstrain/Augur/IQ-TREE v1.6.12), median-joining networks (PopART v1.7), pairwise $L_1$-norm genetic distance, host exon alignment/quantification (HISAT2, TPM), and homology modeling/molecular dynamics (SWISS-MODEL, GROMACS v5.1).

---

## 2. Executive Summary & Editorial Verdict

This study reports metatranscriptomic sequencing of 1,067 SARS-CoV-2-positive nasopharyngeal swabs collected in Abu Dhabi, UAE, between May and June 2020. From 896 high-quality consensus assemblies ($<2\%$ ambiguous bases), the authors identify 1,245 consensus variants across five Nextstrain clades (19A, 19B, 20A, 20B, 20C) and define five UAE-enriched subclades (19B.1, 20B.1–20B.4) characterized by 11 high-frequency local mutations. Using `reditools` to call intra-host single nucleotide variants (iSNVs $\ge 5\%$ minor allele frequency and $\ge 4$ reads), the authors report that at least 5% of patients ($48/896$) were co-infected by multiple distinct SARS-CoV-2 clades. Finally, by examining mutational spectra ($C \to U$ enrichment) and host gene expression in the metatranscriptomic reads against healthy tissues in GTEx, the authors claim a tissue-specific host innate immune response driven by infection-induced upregulation of `APOBEC4` in the nasopharynx. Consensus genomes (GISAID) and viral-aligned reads (NCBI PRJNA687136) are publicly deposited.

While the 896 consensus SARS-CoV-2 genomes provide a valuable genomic surveillance dataset for the first epidemic wave in the UAE, two of the manuscript's three headline conclusions—widespread multi-clade co-infection ($\ge 5\%$, including single patients allegedly co-infected by four distinct global clades simultaneously) and SARS-CoV-2-induced upregulation of `APOBEC4` mediating viral $C \to U$ RNA editing—rest on flawed experimental controls and invalid statistical comparisons. Specifically, multi-clade co-infection calls rely on a threshold of just 4 minor allele reads in high-throughput 96-well plate sequencing without negative extraction controls, spike-in controls, or batch/flowcell contamination checks to rule out index hopping or well-to-well bleed-through. Similarly, the claim that `APOBEC4` is "upregulated among infected patients" was made without sequencing a single SARS-CoV-2-negative nasopharyngeal swab control, instead comparing infected nasal swabs against healthy lung and salivary gland bulk RNA-seq from GTEx (which lacks ciliated nasal epithelium where `APOBEC4` is constitutively expressed). Additional mathematical and statistical defects—including reporting Fisher's exact test $p$-values as `INF` in Table 1, misdefining the TPM normalization equation, and arithmetic contradictions in longitudinal sample counts—require major reanalysis and removal of unsupported claims.

### Specific Assessment of Core Claims

* **Circulation of five global Nextstrain clades (predominantly 20B at 67.2% and 19B at 22.0%) and five local transmission subclades in Abu Dhabi:** **[Well Supported].**  
  The 896 consensus genomes ($<2\%$ gaps, depth $\ge 10\times$) and phylogenetic placement alongside global GISAID references reliably establish multiple introductions and local expansion of five subclades (19B.1 and 20B.1–20B.4), although the Fisher's exact test $p$-values in Table 1 ($p < 10^{-82}$ to `INF`) treat epidemiologically linked transmission chains as independent observations and confuse odds ratios with $p$-values.

* **Cross-settlement human-to-human transmission and smaller intra-host $L_1$-norm genetic distance in longitudinal samples than between settlements:** **[Moderately Supported].**  
  Median-joining networks and $L_1$-norm distances across 120 geo-tagged samples and longitudinal swabs qualitatively support cross-settlement spread and within-host stability, though sample sizes per settlement are small and the longitudinal sample counts in Section 3 ($n = 24$ samples across $n = 7$ individuals vs. a claimed average of $5.2$ samples per individual) are arithmetically inconsistent.

* **At least 5% of patients ($48/896$) were co-infected by multiple distinct SARS-CoV-2 clades/subclades within the same host:** **[Methodologically Flawed].**  
  Co-infection is called whenever clade-defining alleles co-occur at $\ge 5\%$ MAF and $\ge 4$ minor allele copies (and extended to $0.5\%$ MAF in Figs. S14–S15). In high-throughput metatranscriptomic sequencing (up to 192 samples/day extracted on automated 96-well MGISP-960 plates) spanning extreme viral load differences (Ct $<15$ to $>35$), barcode index hopping and plate cross-contamination routinely generate $\ge 4$ reads of dominant cohort clades (19B, 20A, 20B). Figure 5 purports to show cluster(s) of seven patients simultaneously co-infected with four distinct global clades (19A, 19B, 20A, and 20B). Under an overall infection prevalence where multiple independent exposure events are rare, simultaneous natural co-infection by four distinct global clades in seven patients is biologically implausible and diagnostic of unaddressed cross-contamination or index hopping. Assessing concordance on only two technical replicates does not control for pre-library extraction contamination or flowcell-wide index bleed.

* **Upregulation of `APOBEC4` expression in the nasopharynx of infected patients drives tissue-specific $C \to U$ viral RNA editing:** **[Methodologically Flawed].**  
  First, the study includes **zero uninfected nasopharyngeal control swabs**; comparing `APOBEC4` to `ADAR` within infected swabs ($P = 7.7 \times 10^{-5}$) or against uninfected GTEx lung/salivary gland tissues cannot establish infection-induced upregulation, because `APOBEC4` is constitutively expressed in ciliated respiratory/testicular cells present in nasal swabs. Second, unlike `APOBEC3A` and `APOBEC1`, human `APOBEC4` lacks demonstrated cytidine deaminase catalytic activity on RNA substrates. Third, the comparison of $C \to U$ enrichment against a single 8-patient Wuhan BALF study (Giorgio et al.) is confounded by Consensus/GISAID evolutionary accumulation of $C \to U$ transitions over time (May–June 2020 vs. January 2020).

---

## 3. Forensic Defect Inventory

### Defect 1: Statistical Blunders in Table 1 (`P-value = INF`), Phylogenetic Pseudoreplication, and Misannotated Variants (Pillar 3, Pillar 4 & Pillar 7)
* **Location:** Section "Results" (line 39), Table 1 (lines 42–55), Section "Statistical analysis" (line 163).
* **Diagnostic Finding:**
  1. **Impossible $p$-values (`INF`):** In Table 1, for variants at positions 5924, 7171, and 21775 where the global CNCB allele frequency is `0`, the column `P-value #3` (Fisher's exact test $p$-value) is reported as **`INF`**. A probability $p \in [0, 1]$ cannot be infinite; the authors' script evidently output the odds ratio ($\text{OR} = \infty$ due to zero count in the denominator) or $-\log_{10}(0)$ in place of the Fisher's exact test $p$-value.
  2. **Sample size contradiction (`896` vs. `637`):** Table 1 footnote `#3` states that Fisher's exact test compared allele counts in the **896** high-quality UAE genomes against 23,164 CNCB genomes, whereas the Methods (line 163) states that Fisher's exact tests were applied to the **637** unique genomes.
  3. **Pseudoreplication:** Treating 896 (or 637) genomes from a localized outbreak as independent binomial trials in Fisher's exact test ignores shared phylogenetic ancestry (founder effects), producing artificial $p$-values ($10^{-82}$ to $10^{-248}$).
  4. **Annotation error at position 29742:** Table 1 annotates nt 29,742 as `Downstream | S | c.*4358G>A`. Position 29,742 lies in the 3' UTR near the 3' end of the genome (downstream of ORF10 and N), not immediately downstream of Spike (which ends at nt 25,384).
* **Remediation:** Recompute exact two-sided Fisher's exact test $p$-values (replacing `INF` with actual numerical $p$-values), clarify whether $N = 896$ or $N = 637$ was used, note that these tests measure local founder enrichment rather than independent mutational convergence, and correct the annotation of G29742A to 3' UTR.

### Defect 2: Absence of Contamination and Index-Hopping Controls in Multi-Clade Co-Infection Analysis (Pillar 2, Pillar 5 & Pillar 6)
* **Location:** Section "Prevalent co-infection by multiple SARS-CoV-2 variants in the same host" (lines 70–75, Figure 5) and "Intra-host variation detection" (lines 133–135).
* **Diagnostic Finding:** Calling co-infection based on $\ge 4$ minor allele reads ($\text{MAF} \ge 5\%$, or $\ge 0.5\%$ in Figs. S14–S15) in samples with minimum coverage down to $10\times$–$80\times$ without negative controls is highly vulnerable to cross-contamination during 96-well plate automated extraction (MGISP-960) and index hopping on MGI flowcells. The presence of clusters of samples simultaneously carrying defining alleles of 3 to 4 distinct major clades (19A + 19B + 20A + 20B; line 72) is a hallmark of batch-level contamination from high-titer samples into low-titer samples processed on the same plate.
* **Remediation:** Correlate putative co-infection calls with RT-qPCR Ct values, sequencing depth, 96-well extraction plate coordinates, and sequencing run/flowcell batches. Require substantially higher read-depth thresholds (e.g., $\ge 100\times$–$500\times$ per site), phase nearby variants on the same paired-end reads where possible, and reframe multi-clade mixtures cautiously as putative co-infections pending plate-batch exclusion.

### Defect 3: Uncontrolled Claim of Infection-Induced `APOBEC4` Upregulation and Flawed TPM Formula (Pillar 1, Pillar 3, Pillar 5 & Pillar 6)
* **Location:** Abstract (line 5), Section "Results" (lines 78–89, Figure 6B), Section "Methods" (line 140).
* **Diagnostic Finding:**
  1. **Missing uninfected control group:** The manuscript claims *"a previously unidentified upregulation of APOBEC4 expression in nasopharynx among infected patients"* (Abstract, line 5) without analysing any SARS-CoV-2-negative nasopharyngeal swabs. Comparing `APOBEC4` vs. `ADAR` within infected swabs or against GTEx lung/salivary gland bulk RNA-seq is invalid because GTEx does not profile ciliated nasopharyngeal swabs and uses polyA-selected RNA rather than metatranscriptomic RNA.
  2. **Incorrect definition in TPM equation:** In line 140, the authors write:
     $$\text{TPM}(x) = \frac{C_x \times r \times 10^6}{L_x \times T} = \frac{(C_x / L_x) \times 10^6}{\sum_{i=1}^{NN} (C_i / L_i)}$$
     and define $T$ in the text as *"T indicates the length of the gene (kb) divided by the total length of all the genes (kb)"*. Algebraically, for the two expressions to be equal, $T$ must equal $\sum_{i=1}^{NN} \frac{C_i \times r}{L_i}$ (the sum of length-normalized read coverage across all genes), not the ratio of gene lengths!
* **Remediation:** Remove the claim that `APOBEC4` is "upregulated" upon infection (state simply that `APOBEC4` transcripts were detected at higher abundance than `ADAR` in infected nasopharyngeal swabs), acknowledge that `APOBEC4` lacks proven cytidine deaminase activity, and correct the mathematical definition of $T$ in the TPM equation.

### Defect 4: Internal Contradictions in Longitudinal Sample Numbers and Collection Dates (Pillar 7)
* **Location:** Abstract (line 5), Introduction (line 19), Results (lines 27, 64).
* **Diagnostic Finding:**
  1. **Longitudinal sample arithmetic error:** Line 64 reports *"longitudinal samples (n = 24) defined as, same individuals (n = 7) sampled multiple times (avg = 5.2)"*. However, $7 \text{ individuals} \times 5.2 \text{ samples/individual} = 36.4 \neq 24$ (whereas $24 / 7 = 3.43$).
  2. **Sampling date inconsistency:** The sampling window is stated as *"between May 9th and Jun 29th, 2020"* in the Abstract (line 5), *"during April and July, 2020"* in the Introduction (line 19), and *"between May 7th and June 29th 2020"* in the Results (lines 27, 34).
  3. **Test name spelling:** *"Kruskai–Wallis test"* is repeatedly misspelled (lines 56, 59, 163).
* **Remediation:** Correct the longitudinal sample count and mean per individual, harmonize the collection date range across Abstract, Introduction, and Results, and fix typographical errors.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.2** | **3.5** | Fisher's exact test $p$-values reported as `INF` in Table 1; absence of negative/batch controls for low-read-count ($\ge 4$ reads) iSNV co-infection calls; absence of uninfected nasal swab controls for host differential expression; incorrect variable definition in TPM equation. |
| **2. Claim-to-Evidence Alignment** | **1.0** | **2.5** | Two headline Abstract claims—$\ge 5\%$ multi-clade co-infection (including 4-clade mixtures) and infection-induced upregulation of `APOBEC4` driving $C \to U$ editing—are unsupported by appropriate controls. |
| **3. Data Integrity & Biological Plausibility** | **1.2** | **2.0** | Consensus genome assemblies ($N=896$) and clade assignments are solid, but simultaneous 4-clade co-infection in 7 patients and attributing $C \to U$ deamination to `APOBEC4` (which lacks established catalytic deaminase activity) are biologically implausible. |
| **4. Reproducibility & Data Integrity** | **1.3** | **2.0** | Viral consensus sequences (GISAID) and aligned viral reads (NCBI PRJNA687136) are available with tool parameters documented, but host transcriptomic count tables are not deposited and text contains multiple numerical inconsistencies ($n=24$ vs. $7 \times 5.2$, 896 vs. 637 in Table 1, sampling dates). |
| **Total Composite Score** | **4.7** | **10.0** | **Flawed / Overstated** (Scientific Core Score: **3.4 / 8.0**) |
