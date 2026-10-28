# Review of PMC9829393 (PMID:36117410)

**Manuscript Title:** The complex genome and adaptive evolution of polyploid Chinese pepper (Zanthoxylum armatum and Zanthoxylum bungeanum)  
**Authors:** Hu L, Xu Z, Fan R, Wang G, Wang F, Qin X, Yan L, Ji X, Meng M, Sim S, Chen W, Hao C, Wang Q, Zhu H, Zhu S, Xu P, Zhao H, Lindsey K, Daniell H, Wendel JF, Jin S.  
**Journal / Preprint:** *Plant Biotechnol J* (2023; `PMC9829393` / `PMID:36117410` / `10.1111/pbi.13926`)  
**Calibration Study Cohort:** Cohort C — Wild Literature Sample (`C44` | Double-Blinded as `ANON_160`)  
**Overall Score:** **6.5 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 2.0/3.5 | Claims: 1.4/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript reports chromosome-scale genome assemblies for two tetraploid Chinese pepper species ($2n = 4x = 132$), *Zanthoxylum armatum* (4.39 Gb assembled into 66 pseudochromosomes grouped into two homologous sets A1 and A2 of 33 chromosomes; contig N50 = 3.31 Mb) and *Z. bungeanum* (4.63 Gb assembled into 66 pseudochromosomes phased into B and C subgenomes of 33 chromosomes; contig N50 = 10.74 Mb), generated using PacBio long reads (~260×), Illumina short reads, and Hi-C (~106×) scaffolding. Using comparative genomics across 16 plant species, the authors reconstruct a 30-protochromosome Ancestral Rutaceae Karyotype (ARK), identify an ancient core-eudicot triplication (WGT-$\gamma$, $K_s \approx 1.51$, ~123.4 MYA) and a *Zanthoxylum*-specific whole-genome duplication (WGD, $K_s \approx 0.25$, ~20.6 MYA), characterize massive long terminal repeat (LTR) retrotransposon proliferation (~71% of the genome, mostly *Copia* and *Gypsy* bursts within the last 5 MYA), and integrate RNA-seq, Iso-Seq, GC-MS volatile profiling, LC-ESI-MS/MS flavonoid metabolomics, and an insect feeding bioassay (*Helicoverpa armigera*). They link MADS-box gene family changes (*PI* contraction and *AGL11* expansion) to imperfect flowers and apomixis, *TPS* and *BAHD-AT* expansions to terpene allomone and hydroxy-$\alpha$-sanshool biosynthesis, and *DREB* and flavonoid gene expansions/subgenome expression bias in *Z. bungeanum* to cold tolerance.

The chromosome-level genome assemblies and multi-omic datasets (deposited in NCBI SRA and Figshare) represent a major technical improvement (~10–25× higher contig N50) over previous fragmented draft assemblies of *Zanthoxylum*. However, the manuscript suffers from a critical methodological circularity in subgenome phasing and phylogenetic dating, confused ploidy terminology, an unquantified herbivory bioassay, and speculative macroevolutionary storytelling. Specifically: (1) the authors phase the 66 chromosomes of *Z. bungeanum* into subgenomes B and C by assigning the chromosome with smaller genetic distance to *Z. armatum* (A) to subgenome B and the more divergent chromosome to C, which circularly guarantees that `(A, B)` cluster together as sisters relative to C; (2) they then claim that `(A, B)` diverged ~5.9 MYA "well after the allotetraploid formation of *Z. bungeanum* ~7.4 MYA," which is temporally impossible (7.4 MYA is the divergence date of the diploid progenitor lineages `A/B` vs. `C`, whereas the allopolyploid hybridization event combining `B` and `C` must postdate the 5.9 MYA divergence of `B` from `A`); and (3) the insect resistance bioassay (Figure 5f) has no experimental methods, sample sizes, or statistical analysis.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **High-depth PacBio and Hi-C sequencing yield contiguous, chromosome-scale assemblies of 66 pseudochromosomes for both *Z. armatum* (4.39 Gb) and *Z. bungeanum* (4.63 Gb), whose ~6-fold genome expansion relative to *Citrus* is driven by a *Zanthoxylum*-specific WGD (~20.6 MYA) and massive LTR retrotransposon proliferation (~71% of the genome): [Well Supported].**  
  The assemblies achieve 98.1% and 98.5% BUSCO completeness with contig N50s of 3.31 Mb and 10.74 Mb (Table 1). Syntenic $K_s$ distributions clearly resolve the *Zanthoxylum*-specific WGD peak alongside WGT-$\gamma$ (Figure 2d), and EDTA/LTR_retriever annotations confirm that *Ty1-copia* and *Ty3-gypsy* elements amplified within the past 0–5 MYA comprise ~71% of both genomes (Figure 3).

* ***Z. bungeanum* exhibits expanded *CHS*, *UGT*, and *DREB* gene families and higher fruit/leaf glycosylated flavonoid accumulation than *Z. armatum*, consistent with its broader temperate distribution: [Moderately Supported].**  
  CAFE gene family analyses, multi-tissue RNA-seq, and LC-ESI-MS/MS metabolomics across six regional cultivars (Figure 6, Table S21) consistently show elevated flavonoid biosynthetic gene expression and higher levels of cyanidin and delphinidin glycosides in *Z. bungeanum*. While the correlation with cold adaptation is biologically plausible, no cold-stress physiological experiments or genetic perturbation assays were conducted to establish causality.

* **Subgenomes A and B diverged ~5.9 MYA, "well after the allotetraploid formation of *Z. bungeanum* ~7.4 MYA," and subgenomes B and C of *Z. bungeanum* were phased independently of *Z. armatum*: [Methodologically Flawed].**  
  First, in Results line 64, the authors state that they phased the 66 chromosomes of *Z. bungeanum* into subgenomes B and C *"based on the syntenic and genetic distance between chromosomes of A subgenome in Z. armatum and homologous chromosomes in Z. bungeanum."* Assigning the chromosome closer to A to subgenome B and the more distant homeolog to subgenome C for each of the 33 chromosome pairs guarantees by construction that subgenome B is sister to A and forces any chimeric or asymmetrically evolving chromosome pair to sort by distance to A rather than true progenitor ancestry (which should be phased using subgenome-specific LTR signatures, e.g., SubPhaser). Second, in Results line 71 (Figure 2a), the authors equate the stem divergence node between `(A, B)` and `C` (~7.4 MYA) with *"the allotetraploid formation of Z. bungeanum ~7.4 MYA."* An allotetraploid species (`BBCC`) cannot form at 7.4 MYA before its B subgenome diverges from *Z. armatum* (`A`) at 5.9 MYA; 7.4 MYA is the speciation date of the diploid ancestral lineages (`A/B` ancestor vs. `C` ancestor), whereas the hybridization event uniting `B` and `C` must have occurred *after* 5.9 MYA.

* **Contraction of B-class MADS-box *PI* genes and expansion of *AGL11*, *TPS*, and *BAHD-AT* genes confer imperfect flowers, apomixis, and insect resistance against *Helicoverpa armigera*, representing a Cenozoic macroevolutionary shift from Darwin's "Abominable Mystery" to "Neo-darwinism": [Overstated].**  
  While the genomic copy-number patterns (*PI* reduced to 3–4 copies with absent fruit expression; *TPS* and *BAHD-AT* expanded) and GC-MS terpene profiles are informative, the *H. armigera* feeding bioassay (Figure 5f) is presented as a single photograph with zero description in the Methods, no replication metrics, no control for leaf toughness/trichomes, and no statistical test. Furthermore, framing two *Zanthoxylum* genomes as proof of a Cenozoic-wide angiosperm shift away from pollinator co-evolution ("degeneration of reproductive strategy... known as 'Neo-darwinism'", Discussion line 157) is unsupported macroevolutionary speculation.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct the Temporal Interpretation of Allotetraploid Formation and Validate Subgenome Phasing with Subgenome-Specific Repeats
* **WHY:** Phasing B and C strictly by genetic distance to A (`Z. armatum`) is circular when subsequently testing `(A, B)` sisterhood and evolutionary rate asymmetry (Figure 2a,c), and dating allotetraploid formation to 7.4 MYA (prior to the 5.9 MYA divergence of A and B) is a phylogenetic contradiction.
* **WHAT:** Distinguish the divergence time of the diploid progenitor lineages ($T_{\text{progenitor}} \approx 7.4\text{ MYA}$ between the `A/B` ancestor and `C`) from the allopolyploid hybridization event ($T_{\text{hybridization}} < 5.9\text{ MYA}$), and validate the B/C chromosome assignment using differential transposable element ($k$-mer / LTR) signatures.
* **HOW:**
  1. Run `SubPhaser` (or perform hierarchical clustering of 15-mer frequencies and lineage-specific LTR insertion profiles across the 66 chromosomes of *Z. bungeanum* without using *Z. armatum* as a reference) to confirm whether the 33 B and 33 C chromosomes partition cleanly by progenitor-specific repeats.
  2. Revise Results line 71 and Note S4 to state that the diploid progenitor of subgenome C diverged from the common ancestor of A and B ~7.4 MYA, that A and B diverged ~5.9 MYA, and that allotetraploid *Z. bungeanum* (`BBCC`) formed via hybridization between the B and C lineages after 5.9 MYA (further measurable from the divergence of B vs. C specific LTR bursts).

#### 2. Clarify Ploidy, Haploid vs. Monoploid Terminology, and Heterozygosity Contradictions
* **WHY:** Both species have $2n = 4x = 132$, so the monoploid chromosome number is $x = 33$ (~2.2 Gb) and the gametic/haploid chromosome number is $n = 2x = 66$ (~4.4–4.6 Gb). However, Table 1 and Results line 28 label the 66-chromosome (4.39 Gb and 4.63 Gb) assemblies as "Monoploid." In addition, the text repeatedly describes the genomes as having "high heterozygosity" (Introduction line 12, Results lines 28 and 64, Methods line 18), but Methods ("Plant materials", line 11 of the second section) states *"The highly homozygous Z. armatum and Z. bungeanum were cultivated..."*
* **WHAT & HOW:**
  1. In Table 1 and throughout the text, replace "Monoploid" for the 66-chromosome assemblies with "Haploid ($n = 2x = 66$) assembly" (or "Combined subgenome assembly"), and clarify why flow cytometry and 17-mer analysis yielded ~4.4 Gb (the size of two 33-chromosome subgenomes, $2x$) rather than ~8.8 Gb ($4x$) or ~2.2 Gb ($1x$).
  2. Correct "The highly homozygous" in Methods ("Plant materials") and report the exact $k$-mer heterozygosity rates estimated from `kmerFreq` (Figure S4, Table S2) in the main text.

#### 3. Add Complete Experimental Methods and Quantitative Statistics for the *Helicoverpa armigera* Bioassay
* **WHY:** Figure 5f and Results line 126 present a leaf-feeding assay with *H. armigera* larvae, but the Methods section contains no mention of how this experiment was performed, how many biological replicates or larvae were used, what the control plant species were, or how leaf consumption was quantified.
* **WHAT & HOW:** Add a dedicated subsection in the Methods detailing the *H. armigera* larval instar, starvation period, number of larvae per dish, number of independent biological replicate dishes, identity of the comparison plant species shown in Figure 5f, and image-analysis quantification (mean $\pm$ SD percentage of leaf area consumed after 24 h, tested via one-way ANOVA or Kruskal–Wallis test).

#### 4. Temper Speculative Macroevolutionary Narratives in the Discussion
* **WHY:** Generalizing from two *Zanthoxylum* species to claims about Cenozoic-wide angiosperm "degeneration of reproductive strategy" and "Neo-darwinism" (Discussion line 157, Figure 7) overreaches a two-species comparative genomic study.
* **WHAT & HOW:** Condense the Discussion and Figure 7 to focus on the lineage-specific evolution of *Zanthoxylum* within Rutaceae (asymmetric subgenome evolution in *Z. bungeanum* vs. *Z. armatum*, WGD/tandem duplication contributions to secondary metabolism), and frame the links between flavonoid/apomixis pathways and Cenozoic climate as testable ecological hypotheses.

#### 5. Technical and Editorial Cleanup
* **WHY:** Inconsistencies between tables and text reduce clarity.
* **WHAT & HOW:**
  * **Table 1 vs. Table S3 Caption:** Table 1 (line 40) and Methods (line 18 of the second section) state PacBio sequencing was performed on the `PacBio Sequel II` platform, whereas the caption for Table S3 (line 219 of the second section) says `generated from PacBio RSII`. Correct the platform name in Table S3.
  * **Results (Line 66) & Table 1 (Line 57):** Note that for *Z. armatum*, the two subgenomes contain $32,942 + 28,618 = 61,560$ genes (leaving $3,635$ unplaced genes out of $65,195$), and for *Z. bungeanum*, subgenomes B and C contain $31,074 + 28,596 = 59,670$ genes (leaving $8,532$ unplaced genes out of $68,202$). Explicitly mention the unanchored/unphased scaffold gene counts in the text.
