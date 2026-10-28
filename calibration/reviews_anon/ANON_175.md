# Peer Review: ANON_175

**Overall Score:** **6.4 / 10.0** (Mixed / Salvageable)
* **Score Breakdown:** Rigor: 1.9/3.5 | Claims: 1.5/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.5/2.0

---

## 1. Executive Summary & Synthesis

This manuscript presents a chromosome-scale reference genome assembly for Masson pine (*Pinus massoniana*, $2n = 24$, assembled genome size $21.91\text{ Gb}$, contig $\text{N50} = 4\text{ Mb}$, scaffold $\text{N50} = 1.5\text{ Gb}$, $95.3\%$ BUSCO completeness) generated from 968.84 Gb of PacBio long reads, 1,419 Gb of BGI short reads, 2,018.88 Gb of Hi-C reads, and 183.79 Gb of PacBio Iso-Seq full-length transcripts, complemented by 156 tissue/treatment RNA-seq libraries and 204 population transcriptomes. Using these genomic resources, the authors investigate repetitive element proliferation, intron expansion, whole-genome duplication ($K_s$) history, horizontal gene transfer (HGT), and the transcriptional regulation of oleoresin biosynthesis (`PmPGK`, `PmTPS4/12/21`, `PmMYB4`, `PmbZIP2`).

The primary asset of this work is the high-contiguity 21.91 Gb conifer reference assembly and multi-tissue/population transcriptomic resource (deposited under `PRJNA1240911` and GigaDB), which represents a major advance for gymnosperm genomics. However, several downstream evolutionary and functional analyses suffer from internal numerical contradictions, questionable statistical thresholds, and discrepancies between the Methods and Figure legends:
1. **Self-contradictory gene structure statistics:** Line 210 states that the average intron length is **12,680.84 bp** (and reports average CDS length = `1,007 bp` alongside average exon length = `1,005 bp`), whereas Line 229 states that the average intron length is **11.56 kb**.
2. **Flawed GWAS/TWAS significance thresholding:** While the Methods (`line 133`) specify a GWAS threshold of $P \le 1.0 \times 10^{-5}$ across 503,296 SNPs, the Results (`offset 46080, line 12`) re-label this analysis a "Transcriptome-Wide Association Study (TWAS)" and call 6,064 SNPs significant at an unadjusted $P \le 0.01$—where $503,296 \times 0.01 \approx 5,033$ false positives are expected under the global null alone.
3. **Experimental inconsistencies between Methods and Figure 4:** Methods describe `His-tagged PmMYB4` for EMSA (`line 177`) and `35S:PmMYB4-GFP` / `35S:PmbZIP2-GFP` in tobacco protoplasts (`line 182`), whereas the Figure 4C–D caption (`offset 46080, line 1`) reports `GSTMYB4` and `cYFP-bZIP4` / `nYFP-MYB4` BiFC in tobacco leaves. Even more concerning, Methods (`line 167`) states that RT-qPCR of transgenic **poplar 84K** lines used *"pine 18S rRNA as an endogenous control."*

---

## 2. Claim-by-Claim Evaluation

* **Claim 1:** *The 21.91 Gb chromosome-scale assembly of Pinus massoniana achieves a contig N50 of 4 Mb, scaffold N50 of 1.5 Gb across 12 pseudochromosomes (97.31% anchored), and 95.3% complete Embryophyta BUSCOs, capturing 80,366 protein-coding genes and 86.25% repetitive sequences.* — **[Well Supported]**
  * **Evidence & Critique:** The sequencing depth (~44$\times$ PacBio, ~65$\times$ short reads, ~92$\times$ Hi-C), Hi-C contact map (Fig. S3), short-read mapping rate (99.13%), transcript mapping rate (97.70%), and BUSCO completeness (95.3%, the highest among compared conifers in Fig. S4) provide strong support for assembly quality and contiguity. However, the basic gene structure metrics reported in `Evolution of the P. massoniana genome` contain internal contradictions that require correction: Line 210 reports *"the average lengths of coding sequences, exons, and introns were 1,007 bp, 1,005 bp, and 12,680.84 bp, respectively"*, whereas Line 229 reports *"with an average intron length of 11.56 kb"*. Moreover, if multi-exon genes have an average CDS length of 1,007 bp, the average *individual exon* length cannot simultaneously be 1,005 bp unless genes average ~1.002 exons (likely confusing mean single-exon length with mean total exonic/transcript length per gene).

* **Claim 2:** *Ks distributions of paralogous gene pairs reveal two whole-genome duplication (WGD) events in Pinaceae at ~320 MYA and ~260 MYA (Fig. 2D).* — **[Fragile]**
  * **Evidence & Critique:** Whether conifers experienced one or more ancestral WGDs remains fiercely debated because ancient $K_s$ peaks ($K_s > 1.5\text{–}2.5$) are confounded by synonymous substitution saturation and continuous retrotransposon-mediated dispersed gene duplication. Indeed, in the authors' own `DupGen_finder` classification (`line 212`, Fig. S9B), only **410 gene pairs (`0.79%`)** out of 51,898 duplicated genes were classified as WGD/segmental pairs, whereas **75.95%** (`39,418`) were dispersed duplications (`DSD`) and **12.56%** (`6,518`) were tandem duplications (`TD`). Inferring two distinct WGD events at 320 MYA and 260 MYA when $<0.8\%$ of duplicates reside in syntenic collinear blocks is weakly supported without explicit Ks saturation correction and syntenic depth validation.

* **Claim 3:** *Horizontal gene transfer (HGT) transferred 62 genes into the P. massoniana genome, including genes involved in terpenoid biosynthesis (`FDPS`, `TPS`, `MVD`, `HMGS`).* — **[Fragile]**
  * **Evidence & Critique:** Identifying true HGT of core eukaryotic mevalonate pathway enzymes (`HMGS`, `MVD`, `FDPS`)—which are ancestral, universally conserved eukaryotic enzymes present across all land plants—requires ruling out bacterial/fungal endophyte contamination in sequencing reads, retrotransposon capture, and phylogenetic reconstruction artifacts (long-branch attraction or uneven taxonomic sampling in nr). While the authors state that candidate HGT loci were checked for physical linkage to native genes and PacBio read spanning (`line 111`), claiming that core mevalonate enzymes (`HMGS`, `MVD`, `FDPS`) were horizontally acquired in *P. massoniana* (`line 238`, Fig. 3C) is extraordinary and requires explicit maximum-likelihood gene trees with bootstrap support and donor-lineage identification.

* **Claim 4:** *Association mapping across 204 P. massoniana accessions and functional validation demonstrate that `PmPGK` and the `PmMYB4–PmbZIP2` module regulate `PmTPS` genes and oleoresin production (Fig. 4).* — **[Moderately Supported]**
  * **Evidence & Critique:** The biochemical and transgenic assays—dual-luciferase reporter assays (Fig. 4E), EMSA binding (Fig. 4C), RNA in situ hybridization showing epithelial cell localization in resin canals (Fig. 4F), and heterologous overexpression of `PmPGK` in poplar 84K elevating terpene levels (Fig. S22)—provide converging functional evidence. However, the statistical association analysis (`line 133` vs. `offset 46080, line 12`) is undermined by switching from a genome-wide $P \le 1.0 \times 10^{-5}$ threshold in Methods to an unadjusted $P \le 0.01$ threshold in Results (yielding 6,064 SNPs, roughly equal to the 5,033 false positives expected by chance across 503,296 SNPs), and by multiple discrepancies between Methods and Figure 4 captions regarding protein tags and gene names (`His-PmMYB4` vs. `GSTMYB4`; `PmbZIP2-GFP` vs. `cYFP-bZIP4`).

---

## 3. Technical & Methodological Critique

### Major Flaws & Inconsistencies

1. **GWAS/TWAS Statistical Thresholding and MAF Filtering Contradictions:**
   * **MAF filter typo (`line 133`):** Under `Genome-wide association study`, Line 133 states *"SNPs with an MAF below 5% were subjected to GWAS using the mixed linear model in GEMMA"*, directly contradicting Line 128 (*"retaining SNPs with a minor allele frequency (MAF) greater than 0.05"*).
   * **Unadjusted $P \le 0.01$ threshold in Results (`offset 46080, line 12`):** Methods (`line 133`) states *"Associations were deemed significant at a P value threshold of $\le 1.0\text{E}-5$, corresponding to $-\log_{10}(P) \ge 5$."* Yet in Results (`Discovery of vital regulatory genes in oleoresin synthesis`, offset 46080, line 12), the authors refer to this same 204-accession RNA-seq SNP analysis as a *"Transcriptome-Wide Association Study (TWAS)"* (even though testing SNP genotypes called from RNA-seq against a phenotype is an exome/transcriptome-SNP GWAS, whereas TWAS tests genetically regulated gene expression levels) and report *"6,064 key genetic markers (SNPs) significantly associated with oleoresin synthesis and production ($P \le 0.01$)"*! Testing 503,296 SNPs at $P \le 0.01$ without multiple-testing correction guarantees ~5,033 false-positive SNPs under the null hypothesis.

2. **Experimental Mismatches Between Methods and Figure 4 Legends:**
   * **EMSA fusion tag (`line 177` vs. `offset 46080, line 1`):** Methods (`line 177`) states that `PmMYB4` was cloned into `pET32a` to express a **His-tagged** protein purified on `Ni-NTA Agarose`. However, the Figure 4C caption (`offset 46080, line 1`) states: *"Electrophoretic mobility shift assay (EMSA) was conducted to investigate the interactions between **GSTMYB4** protein and the promoter gene."*
   * **Subcellular localization vs. BiFC (`line 182` vs. `offset 46080, line 1`):** Methods (`line 182`) describes cloning `PmMYB4` and `PmbZIP2` into `pBI121-GFP` (`35S:PmMYB4-GFP` and `35S:PmbZIP2-GFP`) for transformation into tobacco protoplasts. Yet the Figure 4D caption (`offset 46080, line 1`) describes bimolecular fluorescence complementation (BiFC) constructs with a different bZIP gene number: *"Subcellular localization of **cYFP-bZIP4** and **nYFP-MYB4** in transiently expressed tobacco leaves."*
   * **Endogenous RT-qPCR control in transgenic poplar (`line 167`):** Under `Genetic transformation`, Line 167 states that `35S:PmPGK-GFP` was transformed into **poplar 84K** (*Populus alba $\times$ P. glandulosa*), and then states: *"The expression level of PmPGK across different transgenic lines was quantified via RT-qPCR, using **pine 18S rRNA** as an endogenous control."* Pine (*Pinus*) 18S rRNA cannot be an endogenous reference gene inside a transgenic poplar (*Populus*) plant unless the primers cross-react with poplar 18S rRNA.

3. **Contradictory Intron and Exon Summary Statistics:**
   * Line 210 reports average CDS length = `1,007 bp`, average exon length = `1,005 bp`, and average intron length = `12,680.84 bp`.
   * Line 229 reports average intron length = `11.56 kb` (`11,560 bp`).
   * These two numbers for average intron length (`12.68 kb` vs. `11.56 kb`) and the impossible ratio of mean CDS length (`1,007 bp`) to mean exon length (`1,005 bp`) need to be audited directly against the GFF3 annotation file.

---

## 4. Constructive Recommendations

1. **Reconcile Gene Annotation Summary Statistics:** Recompute mean and median gene, CDS, single-exon, and intron lengths directly from the final 80,366-gene GFF3 annotation and resolve the discrepancy between `12,680.84 bp` (line 210) and `11.56 kb` (line 229), as well as the `1,007 bp` CDS vs. `1,005 bp` exon length.
2. **Enforce Genome-Wide Multiple Testing Correction in Association Mapping:** Report only loci passing the genome-wide significance threshold ($P \le 1.0 \times 10^{-5}$ or Benjamini-Hochberg $\text{FDR} < 0.05$ across the 503,296 SNPs) rather than unadjusted $P \le 0.01$, correct the typo `"MAF below 5%"` to `"MAF above 5%"` in Line 133, and accurately term the analysis a transcriptome-SNP GWAS rather than a TWAS.
3. **Harmonize Experimental Methods and Figure 4 Captions:** Clarify whether `PmMYB4` was His-tagged or GST-tagged in EMSA (Fig. 4C), whether Fig. 4D shows GFP fusions or split-YFP (`nYFP/cYFP`) BiFC and whether the partner is `PmbZIP2` or `PmbZIP4`, and specify the actual *Populus* reference gene used for RT-qPCR in transgenic 84K poplar.
4. **Provide Phylogenetic Trees and Read-Level Evidence for Putative HGT Genes:** Supply maximum-likelihood phylogenetic trees with bootstrap support and flanking synteny plots for all 62 putative HGT candidates, and re-evaluate whether conserved eukaryotic mevalonate pathway genes (`HMGS`, `MVD`, `FDPS`) represent true HGT or aberrant BLAST/nr taxonomic hits.
