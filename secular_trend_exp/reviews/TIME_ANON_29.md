# Blinded Review: TIME_ANON_29
**Composite Score:** 3.3 / 10.0 (Rigor: 0.8/3.5 | Claims: 0.7/2.5 | Biology: 0.8/2.0 | Reproducibility: 1.0/2.0)
**Bias Category:** Superfamily/Ortholog Conflation & Uncalibrated Template Phylogenetics
**Verdict:** Reject
**Study Modality:** Hybrid Computational + Wet-Lab Functional Validation
**Technology Maturity:** Commodity/Hype-Cycle Template
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary

This manuscript presents a comparative bioinformatic and expression survey of proteins containing the `Band_7` / SPFH domain (`IPR001107` / `PF01145` / `SM00244`), which the authors collectively refer to as the "Prohibitin (PHB) gene family." Using sequences retrieved from 11 species across Bacteria, Fungi, Plants, and Animals (focusing on 17 genes in *Arabidopsis thaliana*), the authors construct Neighbor-Joining (NJ) trees in `MEGA 4.0`, identify 20 sequence motifs using `MEME 4.3.0`, map intron/exon boundaries (`GSDS`) and chromosomal paralogons in *Arabidopsis*, and cluster public `Genevestigator` microarray profiles alongside a 5-tissue RT-qPCR heatmap. They classify the sequences into five classes, propose horizontal gene transfer (HGT) between *E. coli* and the "amniotic ancestor" of humans, conclude that segmental duplication followed by neofunctionalization drove family expansion in *Arabidopsis*, and suggest that *Arabidopsis* findings can be translated to human breast cancer and aging research.

The manuscript follows a formulaic "gene family survey" template and suffers from a foundational domain-classification error, inadequate phylogenetic methods for inter-kingdom divergences, unnormalized/untested RT-qPCR reporting, and numerous internal contradictions. First, by equating the entire `IPR001107 Band_7` / SPFH domain superfamily (which encompasses stomatins, flotillins, erlins, podocin, plant hypersensitive-induced reaction [HIR] proteins, bacterial HflK/HflC proteases, and true prohibitins) with "Prohibitin (PHB) genes," the authors conflate distinct, non-orthologous protein families—treating humans as having "12 PHB genes" (when humans have only two prohibitins, *PHB1* and *PHB2*, plus stomatins, flotillins, and erlins) and misinterpreting deep endosymbiotic/paralogous SPFH lineages (such as bacterial HflK/C and human stomatin-like protein *STOML2*) as direct horizontal gene transfer between *E. coli* and amniotes. Second, inter-kingdom trees are built with unrooted Neighbor-Joining using Poisson distances and pairwise deletion without rate-variation ($\Gamma$) or model selection. Third, claims of "neofunctionalization" and "evolutionary pressure" are asserted solely from visual inspection of expression heatmaps without $d_N/d_S$ ($\omega$) tests or statistical comparisons.

---

### 2. Methodological & Statistical Audit

1. **Conflation of the SPFH / `Band_7` Domain Superfamily with the Prohibitin (PHB) Gene Family:**
   * In the Background (line 16) and Results (line 30), the authors state that `Band_7` (`IPR001107` / `PF01145`), SPFH (*stomatins, prohibitins, flotillins, and HflK/C*), and prohibitin domains are synonymous, and therefore label all 12 human, 12 *E. coli*, 18 *C. elegans*, and 17 *Arabidopsis* `IPR001107` hits as "PHB (Prohibitin) genes."
   * Biologically, the SPFH / `Band_7` domain is a structural superfamily comprising several ancient, functionally distinct families: true Prohibitins (*PHB1/PHB2*, which form the mitochondrial inner-membrane ring complex discussed in lines 16–18; Class IV in the authors' tree), Stomatins (*STOM, STOML1–3, NPHS2*), Flotillins (*FLOT1/2*, such as the *Arabidopsis* tandem pair `At5g25250`/`At5g25260`), Erlins (*ERLIN1/2*), plant HIR defense proteins, and bacterial *HflK/HflC/QmcA* membrane-protease regulators.
   * Because the authors treat all SPFH domain proteins as a single gene family ("PHB") while attributing the literature on human *PHB1/PHB2* nuclear tumor-suppressor and mitochondrial inner-membrane functions to all 17 *Arabidopsis* and 12 human SPFH proteins (Background lines 16–19, Discussion lines 131–140), their functional and evolutionary inferences confound anciently diverged non-orthologous families.

2. **Inadequate Phylogenetic Methodology & Invalid Claim of Bacteria-to-Amniote Horizontal Gene Transfer:**
   * To infer evolutionary relationships across Bacteria (*E. coli*), Fungi (*S. cerevisiae*), Plants, and Animals (spanning >2 billion years of sequence divergence across heterogeneous SPFH families), the authors align full-length proteins of widely varying lengths and domain architectures with default `ClustalX 1.83` and construct an unrooted Neighbor-Joining (NJ) tree in `MEGA 4.0` using simple **Poisson distances with pairwise deletion** and no among-site rate variation ($\Gamma$) or empirical amino acid substitution matrix (Methods line 162). Under these conditions, deep branches are saturated and highly susceptible to long-branch attraction; indeed, the Figure 1 caption (line 50) notes that *"Several conserved genes could not be included into classes."*
   * Based on *E. coli* and human SPFH genes clustering in the same clade in this 9-species NJ tree (which includes only a single prokaryote and a single vertebrate), the authors claim *"horizontal gene transfer between bacteria and amniotic ancestor"* (Results line 52; repeated in Background line 22, Discussion line 128, and Conclusions line 145). In reality, human mitochondrial stomatin-like protein 2 (*STOML2* / *SLP-2*) and related SPFH proteins share ancestry with bacterial SPFH proteins via the ancient mitochondrial endosymbiosis (or ancient paralogy combined with lineage loss in yeast), not horizontal gene transfer into the amniote stem.

3. **Unsupported Claims of "Neofunctionalization" and Selective Pressure:**
   * The Abstract (line 9) and Discussion (line 128) assert that *"most of the duplicated genes experienced neofunctionalization. The results highlighted that PHB genes might be involved in important functions so that the duplicated genes are under the evolutionary pressure to derive new function."*
   * No evolutionary rate analysis ($d_N/d_S$ or branch-site selection tests) was performed, no ancestral expression state reconstruction was conducted to distinguish neofunctionalization from subfunctionalization (dosage sharing/tissue partitioning), and no quantitative correlation or statistical test was applied to the microarray or qPCR heatmaps (Figs. 7–8).

4. **Internal Contradictions in Species Counts and Gene Locus Identifiers:**
   * **Species counts:** Table 1 (line 33) and Methods (line 155) list **11 species**. However, the Figure 1 caption (line 50) states that *"nine species from four kingdom were analysed"* (omitting *Medicago*, *Sorghum*, or *Populus* without explanation). Then Results line 54 states that *"five higher plant species including Arabidopsis, rice, poplar, medicago and sorghum"* were analyzed in Figure 2, whereas the Figure 2 caption (line 57) states *"PHB protein sequences of four species from higher plants were analysed."*
   * **Corrupted *Arabidopsis* TAIR locus IDs:**
     * Line 82 lists Class IV_A gene **`At5g40700`**, whereas Line 92 lists the same paralog (paired with `At3g27280` and `At5g14300`) as **`At5g40770`** (*ATPHB3*).
     * The Figure 6 caption (line 95) labels the chromosome 5 tandem repeat as **`At5g25259` and `At5g25269`**, whereas Line 97 gives their correct TAIR IDs **`At5g25250` and `At5g25260`**.

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **Classification of *Arabidopsis* SPFH genes by intron/exon structure, `MEME` motifs, and chromosomal paralogons (Figures 3–6):** **Moderately Supported (Descriptive).** Within *Arabidopsis*, showing that segmental duplicate pairs (`At1g03860`/`At5g44140`, `At2g20530`/`At4g28510`, `At3g27280`/`At5g40770`) share conserved exon-intron phases and motif architectures is valid descriptive genomics, though well-known from standard *Arabidopsis* paleopolyploidy maps.
* **Claims of Bacteria-to-Amniote HGT, evolutionary pressure for neofunctionalization, and direct translatability of *Arabidopsis* SPFH surveys to human breast cancer, obesity, and neurodegeneration (Abstract line 11, Results line 52, Discussion lines 138–140):** **Overstated / Methodologically Flawed.**

---

### 4. Reproducibility & Data Completeness

* **Critical RT-qPCR Omissions (Methods line 182, Figure 8):**
  1. The Methods section (line 182) and Figure 8 caption (line 114) never specify what **internal reference/housekeeping gene** (e.g., *ACT2*, *UBQ10*, *EF1α*) was amplified to normalize cDNA loading across the five *Arabidopsis* tissues (root, stem, cauline leaf, rosette leaf, flower) before computing $\log_2$ ratios relative to rosette leaf.
  2. Neither the number of biological and technical replicates nor any measure of variance/error bars is reported for the RT-qPCR experiment in Figure 8.
  3. The accession lists for the non-*Arabidopsis* species (rice, *Medicago*, poplar, sorghum, moss, *Chlamydomonas*, *C. elegans*, *E. coli*, yeast, human) used to build Figures 1–3 are not tabulated in the main text or listed in the Additional Files (which contain only human/*C. elegans* intron structures and *Arabidopsis* qPCR primers).
