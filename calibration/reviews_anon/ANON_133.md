# Review of ANON_133

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.5 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.4/3.5 | Claims: 2.0/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.5/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This short report investigates how a minimal synthetic bacterial cell, `JCVI-syn3A` (543 kbp genome encoding 489 protein-coding genes), adapts during ~400 generations of automated serial batch culture in rich medium (SP4-KO) across 10 parallel lineages. All 10 evolved lineages achieved an ~15% increase in exponential growth rate relative to the ancestral strain. Whole-genome resequencing (`breseq`) of endpoint and midpoint clones identified an average of 8 mutations per isolate (range 2–10), characterized by a strong $\text{G/C} \to \text{A/T}$ substitution bias (36/38 SNPs), deletion-biased indels (1–175 bp), and convergent mutations in 8 genes—most notably an uncharacterized ABC efflux permease (`JCVISYN3A_0399`, mutated in 8/10 lineages), fatty acid kinase `fakA`, an upstream $(\text{TA})_{13}$ phase-variable simple sequence repeat regulating lipoprotein `JCVISYN3A_0481`, the tetracycline resistance marker `tetM` (6 distinct downregulating or inactivating mutations), and the uncharacterized gene `JCVISYN3A_0601` (inactivated by start-codon loss and a premature stop codon). RNA-seq profiling of 12 isolates (`GSE205017`) revealed widespread upregulation of ribosomal proteins and downregulation of DNA replication/repair genes. All genome resequencing and transcriptomic datasets are publicly available on NCBI GEO/SRA (`GSE205017`) and `aledb.org` (Project 52).

This is a concise, biologically informative study that demonstrates three practical results for synthetic genomics: (1) `JCVI-syn3A` is not hypermutable despite lacking mismatch repair genes, making causal genotype–phenotype mapping tractable; (2) selection markers retained from genome engineering (`tetM`) impose a measurable fitness cost in antibiotic-free media; and (3) at least one gene retained in `JCVI-syn3A` (`JCVISYN3A_0601`) is dispensable for rapid axenic growth. The primary methodological limitations are the lack of explicit accounting for pre-existing standing variation (`rpoC` and reference diffs) in the mutational spectrum counts, the absence of gene-length/target-size normalization for functional category mutation proportions, and growth-phase confounding in the unadjusted `log(TPM)` RNA-seq clustering. All of these can be resolved through straightforward computational re-analysis of the deposited data.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Repeated independent mutations target specific rate-limiting and non-essential loci in `JCVI-syn3A`, including `JCVISYN3A_0399`, `fakA`, `JCVISYN3A_0481`, `tetM`, and `JCVISYN3A_0601`: [Well Supported].**  
  The observation of 5 distinct amino acid substitutions in the ABC efflux permease `JCVISYN3A_0399` across 8/10 lineages, 4 distinct mutations in `fakA`, 6 distinct promoter/coding loss-of-function mutations in `tetM`, and independent start-loss and nonsense mutations in `JCVISYN3A_0601` provides strong genetic evidence of positive selection acting on membrane transport, lipid salvage, removal of costly engineering cassettes, and further genome streamlining.

* **`JCVI-syn3A` exhibits a non-hypermutable rate (~8 mutations per 400 generations) with a strong $\text{X} \to \text{A/T}$ SNP bias (36/38 SNPs) and deletion bias: [Moderately Supported].**  
  While the overall low mutation count and AT-biased spectrum are clear (Figure 1C), the text notes that *"Certain mutations, such as `rpoC` were found across nearly all strains, which are likely the result of culturing of syn3A before the independent lineages"* and that several other mutations were *"found across all sequenced strains, likely reflective of mutations that were missed in the original GenBank reference genome sequence or that arose during culturing of syn3A."* It is unclear from the text and Figure 1C–D whether these pre-existing standing variants and reference discrepancies were counted once, excluded, or counted multiple times (up to 9–10 times each) when tallying the 38 SNPs and the functional category proportions in Figure 1D.

* **Transporter, translation, metabolism, and transcription genes are disproportionately targeted by adaptive mutations (Figure 1D): [Fragile].**  
  Figure 1D plots the raw proportion of total observed mutations falling into six broad functional categories without normalizing for the fraction of the `JCVI-syn3A` coding genome occupied by each category. In a minimal cell of 489 genes where translation, metabolism, and membrane transport constitute the bulk of the genome, raw mutation counts do not distinguish true mutational enrichment from mutational target size (total base pairs per category).

* **Evolved strains bifurcate into two distinct transcriptional regulatory states (`ALE1–ALE3` vs. `ALE4–ALE7`) driven by a global "greed vs. fear" trade-off and `rpoC` mutations: [Fragile].**  
  First, as the authors candidly note in the Results, the `ALE1–ALE3` cluster closely resembles the stationary-phase wild-type control (`wt.stationary` in Figure 3), indicating that `ALE1–ALE3` cultures were likely harvested during late-exponential/early-stationary transition rather than reflecting a distinct evolved regulatory strategy. Second, if the `rpoC` mutation was inherited from the pre-culture by 9 of the 10 lineages, it cannot explain why `ALE1–ALE3` and `ALE4–ALE7` diverge transcriptionally, nor can its effect be separated from independent adaptive mutations without assaying an `rpoC`-only ancestor clone. Third, differential expression in Figure 3 relies on centered `log(TPM)` values from $n = 2$ biological replicates without formal negative-binomial differential expression testing (`DESeq2`/`edgeR` FDR adjustment) or correction for compositional closure when abundant transcripts (such as `tetM` and ribosomal proteins) shift substantially.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Separate Pre-Existing Standing Variation from *De Novo* Parallel Mutations
* **WHY:** Mutations that were already fixed in the founding culture (diff vs. GenBank `CP016816.2`) or segregating at high frequency prior to lineage splitting (such as the shared `rpoC` allele present in 9/10 lineages) represent single ancestral mutational events rather than independent parallel evolution across replicate flasks.
* **WHAT:** Explicitly partition Table S1 and Figure 1C–D into (a) baseline reference diffs present in all strains, (b) pre-existing founder variants shared identically across multiple lineages (e.g., `rpoC`), and (c) unique *de novo* mutations that arose independently during the 400-generation ALE.
* **HOW:** Re-tabulate the SNP spectrum (Figure 1C) and functional category distribution (Figure 1D) counting each unique mutational event exactly once, and report the exact nucleotide/amino acid coordinates of the shared `rpoC` mutation and whether it was present in the sequenced `wt` ancestral control used in Figure 1A and Figure 3.

#### 2. Normalize Functional Category Mutation Counts by Genomic Target Size
* **WHY:** Plotting the raw percentage of mutations per functional category (Figure 1D) is confounded by how many kilobases of sequence belong to each category in `JCVI-syn3A`.
* **WHAT:** Test for statistically significant mutational enrichment per category (and per gene) after normalizing by coding length (mutations per kbp).
* **HOW:** For each of the six functional categories in Figure 1D, divide the number of independent *de novo* mutations by the total coding base pairs assigned to that category in `CP016816.2`, and compute a two-sided binomial or Poisson enrichment $p$-value (with Benjamini–Hochberg FDR correction) comparing observed vs. expected mutation counts under uniform random mutagenesis.

#### 3. Control for Growth-Phase Harvesting and Compositional Bias in the RNA-Seq Analysis
* **WHY:** Because `ALE1–ALE3` cluster with `wt.stationary` in Figure 3, harvesting density differences confound the comparison of evolved transcriptional states, and raw `TPM` normalization in a tiny 489-gene transcriptome is sensitive to compositional skew from high-abundance ribosomal transcripts.
* **WHAT:** Perform formal differential expression analysis (`DESeq2`) on the HTSeq count matrices (`GSE205017`) and regress out or stratify by the stationary-phase signature.
* **HOW:** (1) Apply `DESeq2` median-of-ratios size factor normalization (which is robust to extreme upregulation of ribosomal genes and downregulation of `tetM`) to the `HTSeq` counts from `GSE205017` and report log2 fold changes and Benjamini–Hochberg adjusted $p$-values ($p_{\text{adj}} < 0.05$) for `ALE4–ALE7` vs. `wt.log`. (2) Project each sample onto the `wt.stationary - wt.log` vector to quantify its growth-phase index, and plot the growth-phase-adjusted residuals in Figure 3.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Minor inconsistencies between the main text, Figure 3 caption, and STAR Methods should be reconciled for clarity.
* **WHAT & HOW:**
  * **Figure 3 Caption vs. Main Text:** The Figure 3 caption refers to *"those most upregulated/downregulated in ALE4-ALE8"*, whereas the main text refers to *"ALE4-ALE7"*. Reconcile the strain numbering and explicitly list in the Figure 3 caption all 12 sequenced RNA-seq samples (including which two lineages provided the small and large colony isolates).
  * **STAR Methods ("Whole genome sequencing" vs. "Data and code availability"):** The Methods state that *"The lack of genome amplifications was determined with a custom script that identified discontinuities in read depth"*, whereas the Data and Code Availability section states *"No additional custom code was created or used for this project."* Either archive the read-depth discontinuity script on GitHub/Zenodo or clarify how coverage discontinuities were inspected using standard `breseq` output.
  * **Key Resources Table:** Fix the truncated entry *"Kapa HyperPlus Library Prep Ki"* to *"Kapa HyperPlus Library Prep Kit"*.
