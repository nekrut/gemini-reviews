# Review of FEXP_ANON_026

**Overall Score:** **7.0 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.3 / 8.0**  
* **Score Breakdown:** Rigor: 2.2/3.5 | Claims: 1.5/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.7/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_026`
* **Perceived Research Domain:** Insect comparative genomics, agricultural vector biology, and evolutionary/epigenetic genomics (*Frankliniella fusca*, order Thysanoptera).
* **Study Design:** De novo hybrid long-read/short-read genome assembly and annotation of an 11th-generation inbred line of the tobacco thrips (*Frankliniella fusca*), followed by comparative orthology, pairwise $d_N/d_S$ divergence, $\text{CpG}_{O/E}$ methylation signature profiling, and re-analysis of developmental/virus-infection RNA-seq datasets (`SRX2788009–SRX2788014`) relative to congener *F. occidentalis*.
* **Primary Methods:** Long-read genome assembly and short-read polishing (`Flye` v2.6, `Minimap2` v2.17, `Pilon` v1.10, `QUAST` v5.0.2, `BUSCO` v4.0.5 Insecta odb10, `JELLYFISH`), 4-round gene annotation (`MAKER` v3.01.02-beta, `SNAP`, `AUGUSTUS` v3.2.3, `RepeatMasker` v4.0.7, `EDTA` v1.9.9, `OmicsBox`, `eggNOG-mapper` v1.0.3, `InterProScan`), phylogenomics and orthology (`OrthoFinder` v2.3.7, `MAFFT`, `RAxML`, `IQ-TREE` v1.6.12, `OrthoVenn2`), pairwise $d_N/d_S$ (`Pal2Nal` v14, `PAML` v4.9), RNA-seq expression and exon usage (`RSEM` v1.3.3, `Bowtie2` v2.4.1, `DESeq2`, `STAR` v2.7.9, `DEXSeq`), and $\text{CpG}_{O/E}$ estimation (`CpG.pl`).

---

## 2. Executive Summary & Editorial Verdict

This manuscript presents the first reference genome assembly for the tobacco thrips, *Frankliniella fusca* (an agricultural pest and vector of *Tomato spotted wilt orthotospovirus* [TSWV]), and only the third genome assembly for the order Thysanoptera. Generated from PacBio Sequel-2 long reads (113$\times$ coverage) polished with Illumina HiSeq 2000 short reads from an 11th-generation inbred line, the 372.45 Mb ungapped assembly (`JAHWGI000000000`) comprises 1,444 contigs with an N50 of 1.18 Mb and achieves 99.0% BUSCO completeness (96.6% in the 26,761 `MAKER`-annotated gene models). The authors compare gene families and xenobiotic/virus-interaction domains with congener *F. occidentalis* (`7,912` 1:1 orthologs), calculate pairwise $d_N/d_S$ across 7,817 orthologs, re-map published stage-specific RNA-seq libraries (`SRX2788009–SRX2788014`) to evaluate differential gene expression (`DESeq2`) and differential exon usage (`DEXSeq`) upon orthotospovirus infection, and examine coding-sequence $\text{CpG}_{O/E}$ depletion alongside 50 fragmented `DNMT3`-like gene models. Raw sequencing reads, the genome assembly, and transcriptome assembly are all publicly deposited under NCBI BioProject `PRJNA742006`.

The primary deliverable—a contiguous, 99.0% BUSCO-complete, PacBio-based reference genome and annotation for *F. fusca*—is a well-validated foundational resource for thysanopteran genomics that substantially improves upon the earlier fragmented short-read assembly of *F. occidentalis* (263.7 Mb ungapped across 6,263 scaffolds). However, the secondary evolutionary and functional analyses contain several methodological caveats and overstatements: (1) positive selection is inferred solely from an unadjusted pairwise point estimate of whole-gene $d_N/d_S > 1$ (`388 / 7,817 = 4.96%` of 1:1 orthologs) without likelihood ratio testing against $d_N/d_S = 1$ or filtering for low-$d_S$ noise and `MAKER`-vs.-`RefSeq` exon boundary mismatches; notably, virus-responsive DEGs actually show no enrichment for $d_N/d_S > 1$ ($4.6\%$ vs. $5.3\%$, $p = 0.1882$) and alternatively spliced genes show a significant depletion ($3.2\%$ vs. $6.9\%$, $p < 0.00001$); (2) the main text (line 35) mistakenly states that the assembly contains *"46 ungapped scaffolds measuring ~ 370 Mb"*, confusing the 46 contigs $\ge 2.5\text{ Mb}$ plotted in Figure 2 with the total of 1,444 contigs in Table 1; and (3) the claim that 50 incomplete `DNMT3`-like fragments (none of which contain a complete set of `DNMT3` domains) reflect sub- or neofunctionalization rather than fragmented pseudogenes or repeat-associated duplications is speculative.

### Specific Assessment of Core Claims

* **High-completeness hybrid genome assembly (372.45 Mb, N50 = 1.18 Mb, 99.0% BUSCO) and proteome annotation (26,761 genes, 96.6% BUSCO) of *Frankliniella fusca*:** **[Well Supported].**  
  The primary genome assembly and four-round `MAKER` annotation are technically sound, well validated by BUSCO Insecta odb10, QUAST, k-mer spectra, and syntenic comparison to *F. occidentalis*, and fully deposited in NCBI (`PRJNA742006`). (Note, however, the text typo on line 35 reporting 46 scaffolds instead of the 1,444 contigs shown in Table 1).

* **Phylogenomic placement of *F. fusca* and conservation/expansion of detoxification (`CYP`, `GST`, `CE`) and virus-interaction gene families relative to *F. occidentalis*:** **[Well Supported].**  
  `OrthoFinder2` species-tree inference across 20 arthropods and `OrthoVenn2` / `InterProScan` domain comparisons reliably establish 7,912 1:1 orthologs and show that domain copy numbers do not significantly differ overall between the two *Frankliniella* species ($t$-test $p = 0.2452$).

* **Substitution patterns consistent with positive selection ($d_N/d_S > 1$) occur in $\sim 5\%$ (`388/7,817`) of 1:1 orthologs, including virus-responsive DEGs and AS genes:** **[Fragile].**  
  Calling positive selection strictly from a whole-gene pairwise point estimate of $d_N/d_S > 1$ in `PAML` without (a) performing a likelihood ratio test against the null hypothesis of neutrality ($d_N/d_S = 1$), (b) filtering out genes with near-zero synonymous divergence ($d_S \to 0$) where a few nonsynonymous differences inflate the ratio, or (c) masking local frame/splice-site discrepancies between de novo `MAKER` gene models in *F. fusca* and `RefSeq` models in *F. occidentalis* inflates the apparent proportion of positively selected genes ($4.96\%$). Furthermore, the authors' own Fisher's exact tests demonstrate that virus-responsive DEGs are not enriched for $d_N/d_S > 1$ ($p = 0.1882$, line 82) and AS genes are significantly depleted of $d_N/d_S > 1$ ($p < 0.00001$, line 84).

* **Genes downregulated and alternatively spliced in response to orthotospovirus infection exhibit lower $\text{CpG}_{O/E}$ (higher historical germline DNA methylation):** **[Moderately Supported].**  
  The bimodal coding-sequence $\text{CpG}_{O/E}$ distribution (mean $0.68$; Fig. 7A) and the lower $\text{CpG}_{O/E}$ of downregulated and alternatively spliced genes (Fig. 8) are statistically clear and consistent with insect gene-body methylation patterns. However, because $\text{CpG}_{O/E}$ is a static evolutionary signature of germline cytosine deamination rather than a direct assay of dynamic somatic methylation during infection (e.g., WGBS), this correlation likely reflects baseline differences between housekeeping/constitutively expressed genes (which typically have low $\text{CpG}_{O/E}$ and high exon counts, increasing statistical power for `DEXSeq` and `DESeq2` detection) and inducible genes, rather than virus-induced de novo methylation.

* **Fifty incomplete `DNMT3`-like sequences are paraphyletic with respect to `DNMT1` and suggest sub- or neofunctionalization:** **[Overstated].**  
  As noted in line 102, **none** of the 50 `DNMT3`-like sequences contain all expected `DNMT3` domains, and many are arrayed in tandem on contigs. Without intact catalytic and targeting domains, fragmented copies are far more parsimoniously explained as partial gene duplications/pseudogenes or transposable element captures than 50 subfunctionalized methyltransferases. Additionally, the apparent paraphyly of `DNMT3` with respect to `DNMT1` in Figure 7C (line 104) is a rooting artifact of an unrooted two-paralog tree lacking an external C5-methyltransferase outgroup (such as `DNMT2`/`TRDMT1`).

---

## 3. Forensic Defect Inventory

### Defect 1: Factual Contradiction Between Main Text (`46 ungapped scaffolds`) and Table 1 (`1,444 contigs`) (Pillar 7)
* **Location:** Section "Genome assembly and annotations" (line 35), Table 1 (line 43), Figure 2 caption (line 49), Methods (line 140).
* **Diagnostic Finding:** Line 35 states: *"The F. fusca genome assembly contained 46 ungapped scaffolds measuring ~ 370 Mb (Table 1)."* However, Table 1 reports `Number of contigs = 1,444`, `Total length = 372,449,807 bp`, and `Scaffold N50 = 1,182,854 bp` (and Methods line 145 states that 5% of the assembly subfiles contained 72 contigs: $72 \times 20 = 1,440$ contigs). The number `46` actually refers only to the subset of contigs $\ge 2.5\text{ Mb}$ extracted via `Seqtk` for Circos visualization in Figure 2 (lines 49, 140).
* **Remediation:** Correct line 35 to state that the *F. fusca* genome assembly contained **1,444 ungapped contigs/scaffolds** measuring 372.45 Mb (with 46 contigs $\ge 2.5\text{ Mb}$ in length).

### Defect 2: Unfiltered Pairwise Whole-Gene $d_N/d_S > 1$ Calls Without Likelihood Ratio Tests or Alignment QC (Pillar 3 & Pillar 4)
* **Location:** Section "Molecular evolution of pest status genes" (lines 78–90) and Section "Protein evolution rate" (line 162).
* **Diagnostic Finding:** Pairwise whole-gene $d_N/d_S$ (`PAML` v4.9) is an exceedingly conservative test when properly calibrated, yet the authors report 388 of 7,817 orthologs ($4.96\%$) having $d_N/d_S > 1$ simply by thresholding the raw point estimate at $1.0$. No likelihood ratio test (comparing freely estimated $\omega$ against fixed $\omega = 1$ with $\chi^2_1$ $p$-values and FDR adjustment) was performed, nor were minimum synonymous substitution filters (e.g., $d_S > 0.01$ and $d_S < 2.0$) applied to remove division-by-near-zero artifacts or non-homologous exon stretches between `MAKER` and `RefSeq` gene models.
* **Remediation:** Filter pairwise `Pal2Nal` alignments to require $0.01 \le d_S \le 2.0$, perform formal `codeml` likelihood ratio tests (`fix_omega = 1, omega = 1` vs. `fix_omega = 0`), and report how many of the 388 genes have statistically significant $d_N/d_S > 1$ ($p < 0.05$ and BH FDR $q < 0.05$).

### Defect 3: Expression Level and Gene Length Confounding in $\text{CpG}_{O/E}$ vs. `DESeq2`/`DEXSeq` Comparisons and `MAKER` Single-Isoform Setting (Pillar 3 & Pillar 5)
* **Location:** Section "Genome wide DNA methylation" (lines 106–109, Figure 8) and Section "Genome annotation" (line 145).
* **Diagnostic Finding:**
  1. In insects, heavily methylated (low $\text{CpG}_{O/E}$) genes are overwhelmingly constitutively expressed housekeeping genes with high baseline read counts and more exons. Because statistical power in `DEXSeq` (differential exon usage) and `DESeq2` scales strongly with baseline read depth and exon number, housekeeping genes are much more likely to reach statistical significance for differential exon usage or downregulation upon stress/infection, creating a baseline-expression confounder when comparing $\text{CpG}_{O/E}$ across `AS` vs. `non-AS` and `DEG` vs. `non-DEG` categories.
  2. Line 145 notes that `MAKER` was run with `alt_splice = 0` (generating only a single canonical transcript per gene). While `DEXSeq` can still test differential exon usage across the constitutive exons of a single transcript model, it misses alternative splice junctions or retained introns not present in the single `MAKER` model.
  3. Line 157 reports using `DESeq2 v3.13`—`3.13` is the Bioconductor release version, whereas the corresponding `DESeq2` package version is `v1.32.x`.
* **Remediation:** Test whether the $\text{CpG}_{O/E}$ differences in Figure 8 remain significant in a multiple regression controlling for baseline log-mean expression (`baseMean`) and exon count, clarify that `DEXSeq` evaluated differential usage of annotated exons within the single-isoform `MAKER` models, and correct the `DESeq2` version number in line 157.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.2** | **3.5** | Primary deliverable (hybrid PacBio + Illumina genome assembly and 4-round `MAKER` annotation, 99.0% BUSCO) is rigorously executed and validated; deductions for thresholding raw pairwise $d_N/d_S > 1$ without LRTs or $d_S$ filtering, unrooted `DNMT` tree interpretation, and unadjusted baseline expression/exon-count confounding in $\text{CpG}_{O/E}$ comparisons. |
| **2. Claim-to-Evidence Alignment** | **1.5** | **2.5** | Resource claims are well supported, but claims of positive selection on virus-responsive genes (where DEGs show no enrichment $p=0.1882$ and AS genes show significant depletion $p<10^{-5}$) and sub-/neofunctionalization of 50 incomplete `DNMT3` fragments are overstated. |
| **3. Data Integrity & Biological Plausibility** | **1.6** | **2.0** | Inbred-line male head DNA extraction, vector contamination screening (`VecScreen`), and BUSCO/QUAST validation ensure high assembly integrity. |
| **4. Reproducibility & Data Integrity** | **1.7** | **2.0** | Complete raw sequencing data (`SRR15147323–SRR15147327`), genome assembly (`JAHWGI000000000`), and transcriptome assembly (`GJHY00000000`) are openly deposited under `PRJNA742006` alongside 20 supplementary tables; 0.3 deduction for the `46 scaffolds` vs. `1,444 contigs` contradiction in line 35 and `DESeq2 v3.13` version typo. |
| **Total Composite Score** | **7.0** | **10.0** | **Strong / Sound** (Scientific Core Score: **5.3 / 8.0**) |
