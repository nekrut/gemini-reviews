# Review of FEXP_ANON_024

**Overall Score:** **7.4 / 10.0** (Strong / Sound) | **Scientific Core Score:** **5.6 / 8.0**  
* **Score Breakdown:** Rigor: 2.3/3.5 | Claims: 1.7/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.8/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_024`
* **Perceived Research Domain:** Microbial metagenomics, phylogenomics, and comparative metabolic evolution (uncultured marine and sponge-associated Actinobacteria, class *Acidimicrobiia*, order `UBA5794`).
* **Study Design:** Oligotrophic culture enrichment, full-length PacBio 16S rRNA amplicon sequencing, and Illumina HiSeq-2500 shotgun metagenomic assembly/binning of deep-sea hydrothermal sediment (`N04`, 2,986 m depth, Carlsberg Ridge), combined with comparative phylogenomic and metabolic analysis of 134 high-quality `UBA5794` MAGs (dereplicated at $99\%$ ANI to $N = 98$ non-redundant genomes).
* **Primary Methods:** Full-length 16S rRNA analysis (`lima`, `UPARSE`, `Mothur`/SILVA 138.1, `MAFFT` v7.505, `Gblocks` v0.91b, `MEGA11`, `FastTree` v2.1.3), metagenomic assembly and binning (`metaSPAdes` v3.9.0, `Megahit` v1.2.9, `SPAdes` v3.13.1, `MetaWRAP` [`CONCOCT`, `MetaBAT2`, `MaxBin2`], `CheckM` v1.0.9, `GTDB-Tk` v2.0.0), phylogenomics (`OrthoFinder`, `IQ-TREE` v2.1.2 on 120 GTDB markers and 291 single-copy OGs), metabolic profiling (`Prokka`, `Kofamscan`/KEGG, `PfamA`, `METABOLIC` v2.0, `HydDB`), habitat association testing (`vegan` Bray–Curtis PCoA, `Scoary` Fisher's exact test with BH FDR), HGT detection (`HGTector2`), and ancestral state reconstruction (`Mesquite` v3.31 Mk1 and Asymm.2 models).

---

## 2. Executive Summary & Editorial Verdict

This study resolves the taxonomic identity and metabolic repertoire of the uncultured actinobacterial lineage `UBA5794` (class *Acidimicrobiia*), which is frequently misassigned to *"Candidatus* Actinomarinales" (or the OM1 clade) in standard 16S rRNA gene surveys. By combining full-length PacBio 16S rRNA amplicon sequencing and shotgun metagenomic binning of an oligotrophic enrichment from deep-sea hydrothermal sediment on the Carlsberg Ridge (recovering 3 high-quality MAGs containing full-length 16S rRNA genes identical to dominant amplicon OTUs) with 131 public `UBA5794` genomes ($N = 98$ non-redundant MAGs at $<99\%$ ANI), the authors demonstrate that `UBA5794` forms a distinct order sister to *Ca.* Actinomarinales. Unlike the streamlined, low-GC ($\sim 32.5\%$), photic-zone planktonic *Ca.* Actinomarinales ($\sim 1.1\text{ Mb}$), `UBA5794` possesses larger ($1.39\text{–}5.38\text{ Mb}$, median $2.79\text{ Mb}$), high-GC ($59.1\%\text{–}72.5\%$, median $64.2\%$) genomes with versatile heterotrophic and chemolithotrophic pathways (polyP glucokinase, glyoxylate shunt, oxygen-labile 2-oxoglutarate ferredoxin oxidoreductase `KOR`, CO dehydrogenase `CoxLMS`, group 3b `[NiFe]` sulfhydrogenases, sulfide-quinone reductase `SQR`, and `ars`/`mer`/`ygfKMN` metalloid detoxification). Furthermore, phylogenomic and functional ordination separates `UBA5794` into a sponge-associated clade (`Cluster 1` plus a smaller subclade in `Cluster 2`) enriched in CRISPR/R-M/toxin–antitoxin defense systems, cobalamin (`VB12`), and squalene (`hpnCDE`) biosynthesis, and free-living lineages enriched in Type IV pili, heliorhodopsins (`HeR`), and inorganic sulfur/nitrogen energy metabolism. Raw reads and MAGs are publicly deposited under NCBI BioProject `PRJNA1141458`.

This is a well-executed and biologically informative comparative metagenomic study. Linking full-length 16S rRNA sequences assembled directly inside `UBA5794` MAGs (`metabat2_bin.28` and `bin.29`) to the `"Actinomarinales; uncultured"` clade in SILVA 138.1 decisively resolves a longstanding taxonomic confusion in marine microbial ecology. The primary methodological limitations lie in the statistical treatment of evolutionary non-independence and MAG incompleteness: (1) because nearly all sponge-associated genomes belong to a single monophyletic clade (`Cluster 1`), testing habitat associations via uncorrected Fisher's exact tests in `Scoary` and two-sample $t$/Wilcoxon tests treats phylogenetically related genomes as independent replicates rather than using `Scoary`'s phylogenetic permutation test; (2) inferring obligate anaerobic specialization from the absence of `coxABCD`/`cydAB` and catalase/SOD in $12.24\%$ of MAGs does not control for MAG completeness (which extends down to $70\%$); and (3) `HGTector2` comparisons between sponge and free-living MAGs do not control for potential unbinned foreign contigs (up to $10\%$ CheckM contamination) in complex sponge metagenomes. These caveats can be addressed through straightforward sensitivity analyses on the existing dataset.

### Specific Assessment of Core Claims

* **`UBA5794` represents an independent order sister to *Ca.* Actinomarinales within *Acidimicrobiia*, resolving the misannotation of `"Actinomarinales; uncultured"` 16S rRNA sequences in SILVA 138.1:** **[Well Supported].**  
  The recovery of full-length 16S rRNA genes inside `UBA5794` MAGs matching dominant amplicon OTUs at $100\%$ identity (Fig. S2), combined with $<88.4\%$ 16S rRNA sequence identity to *Ca.* Actinomarinaceae (below the $89.2\%$ order-level threshold) and robust monophyly in both 120-marker GTDB-Tk and 291-orthogroup IQ-TREE phylogenies, provides definitive support.

* **`UBA5794` possesses flexible carbon, energy, and heavy metal(loid) detoxification pathways distinct from streamlined *Ca.* Actinomarinales:** **[Well Supported].**  
  Pathway reconstructions across the 98 non-redundant MAGs (`Kofamscan`, `PfamA`, `METABOLIC` v2.0, `HydDB`) consistently document widespread polyP glucokinase ($80.6\%$), glyoxylate shunt ($57\%\text{–}63\%$), `korAB` ($83\%\text{–}86\%$), `CoxLMS` ($>70\%$), `SQR` ($56.1\%$), `arsC`/`arsM` ($72.5\%$/$58.2\%$), and `ygfK` ($53.1\%$).

* **Complete absence of terminal oxidases (`coxABCD` and `cydAB`) in $12.24\%$ of MAGs indicates physiological specialization for strictly anaerobic habitats:** **[Fragile].**  
  The inclusion criteria admit MAGs with CheckM completeness down to $>70\%$ (line 52). In a MAG with $70\%\text{–}80\%$ completeness, multi-gene operons such as `coxABCD` or `cydAB` have a substantial probability of falling in unassembled or unbinned genomic regions. Without demonstrating that the 12 oxidase-lacking MAGs have near-complete ($>95\%$) genome recovery or form a cohesive phylogenetic clade with verified anaerobic markers, operon absence in draft MAGs is fragile evidence of obligate anaerobiosis.

* **Sponge-associated and free-living `UBA5794` lineages exhibit statistically significant enrichment of habitat-specific genes (defense systems, `VB12`, squalene vs. Type IV pili, `HeR`, inorganic respiration) and higher HGT rates in sponges:** **[Moderately Supported].**  
  The functional separation in PCoA (Fig. 4) and presence of complete `hpnCDE` squalene and `cob` vitamin $B_{12}$ clusters in sponge symbionts vs. `HeR` and `pil` clusters in free-living MAGs are biologically compelling and consistent with known sponge microbiome biology. However, because almost all sponge MAGs reside in a single clade (`Cluster 1`, plus a small subclade in `f_ZC4RG35`; Fig. 3), running standard Fisher's exact tests in `Scoary` (without `Scoary`'s pairwise phylogenetic comparison filter) and standard Wilcoxon/$t$-tests (Figs. S4, S8) conflates clade-level phylogenetic inertia with independent habitat convergence. Additionally, higher `HGTector2` counts in sponge MAGs could be partially inflated if sponge-derived MAGs have higher CheckM contamination (up to $10\%$) from co-assembled sponge symbiont contigs.

* **Ancestral state reconstruction indicates a free-living origin (`Mk1 = 0.973`, `Asymm.2 = 0.938`) with subsequent transition to sponge symbiosis, and plate tectonics isolated terrestrial `"others"` lineages from marine sediments:** **[Moderately Supported].**  
  The Mesquite ML ancestral state reconstruction supporting a free-living ancestor for `UBA5794` is consistent with the basal branching of free-living marine sediment lineages in `Cluster 2` and outgroup *Acidimicrobiia*. However, the speculation in line 168 that terrestrial/cave/fossil MAGs (`"others"`, $n=12$) were isolated from marine sediment ancestors *"under the strong external force of plate tectonics"* is an untested conjecture (`Overstated` as a specific geological mechanism).

---

## 3. Forensic Defect Inventory

### Defect 1: Uncontrolled Phylogenetic Non-Independence in `Scoary` Enrichment and Group Wilcoxon/$t$-Tests (Pillar 3 & Pillar 4)
* **Location:** Section "Identification of habitat-associated genes/domains" (line 64), Section "Separation between sponge-associated and free-living UBA5794 groups" (lines 129–147), Section "Lifestyle and HGT shaping habitat adaptation" (lines 156–158).
* **Diagnostic Finding:** In line 64, the authors state that gene clusters were called habitat-associated in `Scoary` based solely on Fisher's exact test $p < 0.05$ and BH FDR $q < 0.05$. Because sponge-associated `UBA5794` genomes are nearly monophyletic (concentrated in `Cluster 1` and one subclade of `f_ZC4RG35`), standard Fisher's exact tests and two-sample Wilcoxon/$t$-tests treat all 27 (de-replicated) sponge MAGs as independent evolutionary trials. A single ancestral gene acquisition or loss on the stem branch of `Cluster 1` will produce an extreme Fisher's exact test $q$-value even if it represents only $1\text{–}2$ independent evolutionary transitions.
* **Remediation:** Re-run `Scoary` enabling the phylogenetic tree correction (`-t` / pairwise comparisons permutation $p < 0.05$) using the 291-OG IQ-TREE phylogeny, or highlight which sponge-enriched features (e.g., CRISPR/R-M, `cob` operon, `hpnCDE` squalene cluster, loss of `SCO1` and Type IVa pili) are convergently shared across both independent sponge lineages (`Cluster 1` AND the sponge-associated members of family `f_ZC4RG35` in `Cluster 2`). For continuous traits (genome size, coding density, sigma factors, normalized HGT counts), supplement the Wilcoxon/$t$-tests with phylogenetic generalized least squares (`phylolm` / `PGLS`).

### Defect 2: Uncontrolled MAG Completeness ($>70\%$) in Gene-Absence Inferences and Contamination Check for `HGTector2` (Pillar 2 & Pillar 3)
* **Location:** Section "Phylogenetic analysis" (line 52), Section "Energy metabolism and element cycle" (line 113), Section "Lifestyle and HGT" (line 158).
* **Diagnostic Finding:**
  1. **Completeness confounding of gene absence:** Line 113 infers that $12.24\%$ ($12/98$) of `UBA5794` genomes are specialized for strictly anaerobic habitats because they lack `coxABCD`, `cydAB`, catalase, and SOD. Because the dataset includes MAGs down to $70\%$ completeness (line 52), false-negative gene absence due to incomplete assembly can easily account for missing operons in lower-completeness bins.
  2. **Contamination confounding of HGT counts:** Sponge metagenomes contain dense microbial consortia, and MAGs with up to $10\%$ CheckM contamination (line 52) can harbor unbinned foreign contigs carrying mobile defense islands (R-M, toxin–antitoxin, CRISPR), which `HGTector2` will score as HGT events.
* **Remediation:** Report the CheckM completeness and phylogenetic clustering of the 12 oxidase-negative MAGs (e.g., verify that the inference holds when restricted to $\ge 90\%$ complete MAGs), and verify in `HGTector2` that the elevated HGT rate in sponge MAGs persists after controlling for CheckM contamination percentage (e.g., via partial correlation or restricting to contigs $\ge 10\text{ kb}$ that also carry native `Acidimicrobiia` core genes).

### Defect 3: Minor Technical and Typographical Corrections (Pillar 7)
* **Location:** Lines 45, 108, 158, 168.
* **Diagnostic Finding:**
  1. Line 45 lists the second SPAdes k-mer configuration as `(21, 33, 55, 77, 99127)`—missing a comma and space between `99` and `127`.
  2. Line 108 describes GH109 enzymes as utilizing an `NAD - dependent hydrolysis` mechanism instead of `NAD+ -dependent` (or $\text{NAD}^+$-dependent).
  3. Line 158 annotates `bcrB` as *"benzoyl-CoA 2,3-epoxidase subunit B (bcrB)"* whereas line 151 correctly identifies benzoyl-CoA 2,3-epoxidase as `boxBC` and benzoyl-CoA reductase as `bcrBC`.
  4. Line 168 misspells `Movile Cave` as `Moville Cave` (spelled correctly on line 20).
* **Remediation:** Insert the missing comma in the SPAdes k-mer list (`99, 127`), correct `NAD+ -dependent`, harmonize the gene symbol `boxB` vs. `bcrB` on line 158, and fix the spelling of `Movile Cave`.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.3** | **3.5** | Strong multi-assembler binning, subsampling refinement, full-length 16S-to-MAG linkage, and 120-marker/291-OG phylogenomics; deductions for lack of phylogenetic control (`PGLS` / `Scoary` tree permutations) when testing sponge vs. free-living clades and not conditioning on MAG completeness/contamination for gene-absence and HGT tests. |
| **2. Claim-to-Evidence Alignment** | **1.7** | **2.5** | Primary taxonomic, metabolic, and ecological claims are well supported by the data; minor overstatements regarding obligate anaerobiosis from gene absence in $>70\%$-complete MAGs and speculative plate-tectonic vicariance. |
| **3. Data Integrity & Biological Plausibility** | **1.6** | **2.0** | High biological plausibility and thorough metabolic cross-checking (e.g., `GH109` NR validation, `HydDB` classification, synteny of `HeR` and `hpnCDE` operons); oligotrophic enrichment bias is appropriately restricted to N04 recovery while comparative analyses leverage 98 dereplicated genomes. |
| **4. Reproducibility & Data Integrity** | **1.8** | **2.0** | Raw metagenomic reads and all recovered MAGs are openly deposited under NCBI BioProject `PRJNA1141458` (`SAMN43058488`, `SAMN42893693–SAMN42893736`), and all software versions, thresholds, and 15 supplementary tables are comprehensively documented. |
| **Total Composite Score** | **7.4** | **10.0** | **Strong / Sound** (Scientific Core Score: **5.6 / 8.0**) |
