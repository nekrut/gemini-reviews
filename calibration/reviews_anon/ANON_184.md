# Review of ANON_184

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **7.4 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.1/3.5 | Claims: 1.8/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript benchmarks six organelle genome assembly pipelines (`GetOrganelle`, `NOVOPlasty`, `Flye + Unicycler`, `PMAT`, `ptGAUL`, and `Oatk`) across sequencing platforms (`DNBseq`/`Illumina`, `ONT`, and `PacBio HiFi`) and reports complete, gap-free mitochondrial and plastid genomes for two *Rhododendron* species from contrasting elevations: the alpine *R. nivale* subsp. *boreale* (4,287.5 m; 510,610 bp mitogenome across two circular and one linear chromosome; 202,882 bp plastome) and the low-elevation *R. vialii* (<1,800 m; 761,073 bp single circular mitogenome; 195,319 bp plastome with an expanded inverted repeat leaving a 73 bp SSC). Using long-read spanning validation (`minimap2`), the authors verify 16 mitochondrial (`R1–R16`) and 6 plastid (`R17–R22`) recombination paths, annotate SSR/tandem/dispersed repeats, predict 358 mitochondrial C-to-U RNA editing sites (`Deepred-Mt`), and quantify plastid-to-mitochondrial DNA transfers and synteny with *Vaccinium macrocarpon*. They then assemble a comparative dataset of 58 angiosperm species from 11 families across high and low altitudes (plus *Oryza sativa* as outgroup) to compare mitogenome (32 PCGs) and plastome (77 PCGs) maximum-likelihood phylogenies (`IQ-TREE`), codon usage bias (`CodonW` and `EMBOSS`), and branch-site positive selection (`HyPhy aBSREL`), identifying `atp4`, `atp9`, `mttB`, and `clpP` as positively selected in multiple high-altitude lineages. Raw sequencing reads (`SRA PRJNA1040959`), annotated genomes (`GenBank PQ537102–PQ537104, PQ537097, PQ536991–PQ536992`), and assemblies/scripts (`Figshare 10.6084/m9.figshare.25909855`) are all publicly available.

The de novo assembly and long-read structural validation of the *Rhododendron* mitogenomes and plastomes represent a solid technical and genomic resource for a genus where repetitive organelle structures have historically resisted assembly. Furthermore, the authors deserve credit for reporting negative results honestly—specifically showing via PCA and `ENc`/`GC3s` distributions that organelle codon usage is governed primarily by phylogenetic lineage rather than altitude. However, the comparative and evolutionary analyses across the 58 angiosperm species have three methodological weaknesses: (1) using a paired Wilcoxon signed-rank test to compare independent high- vs. low-altitude species groups without controlling for phylogenetic non-independence; (2) running exploratory `aBSREL` across all branches without formally testing whether positive selection is statistically enriched on high-altitude branches relative to low-altitude branches; and (3) running `aBSREL` on genomic mitochondrial CDSs without accounting for C-to-U RNA editing, which is particularly dense in `mttB` (Fig. 3) and can create artificial nonsynonymous substitutions at the DNA level that are reverted to conserved amino acids at the mRNA level. These limitations can be resolved through targeted statistical re-analysis.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **PacBio HiFi assembly (`Oatk` and `PMAT`) resolves the complex multi-chromosomal/branched mitogenomes and expanded-IR plastomes of *R. nivale* subsp. *boreale* and *R. vialii*: [Well Supported].**  
  The assemblies are gap-free with uniform HiFi read depth (Figs. S2–S5), and all 22 putative repeat-mediated recombination conformations (`R1–R22`, Fig. 1) are directly supported by individual PacBio HiFi reads spanning $\ge 1,000\text{ bp}$ on both flanks of the repeat junctions (Figs. S7–S10). However, the failure of short-read assemblers (`GetOrganelle`, `NOVOPlasty`) in the benchmark is partly attributable to subsampling short reads to only `10–20x` depth (Methods line 52) while providing `150x` depth to `ptGAUL` and `Oatk`.

* **Mitogenome and plastome phylogenies across the 58 eudicot species strongly support the monophyly of all 11 families and the sister relationship of *Rhododendron* and *Vaccinium*, while exhibiting cytonuclear/organellar topological discordance in Rosids (`Crassulaceae`, `Salicaceae`, `Brassicaceae`, `Rosaceae`) and `Saussurea`: [Well Supported].**  
  Concatenated ML analyses under `GTR+F+R3` (77 plastid PCGs) and `GTR+F+I+R4` (32 mitochondrial PCGs) yield 100% bootstrap support for all 11 families and for `Ericaceae + Primulaceae`, while documenting clear, well-supported topological incongruence between the plastid and mitochondrial trees (Fig. 6, Figs. S12–S13).

* **Organelle codon usage bias across the 58 angiosperm species is primarily structured by evolutionary lineage (family) rather than altitude: [Well Supported].**  
  Both `ENc` and `GC3s` distributions (Fig. 7A–B) and PCA of absolute (`absCUFs`) and synonymous (`synCUFs`) codon usage frequencies (Fig. 7D–G, Fig. S15) show no separation by altitude and clear clustering by plant family (particularly `Ericaceae`, `Convolvulaceae`, and `Salicaceae`). Note, however, that the two-group comparisons in Fig. 7A–C improperly used the *Wilcoxon signed-rank test* (a paired test) instead of the unpaired Wilcoxon rank-sum (Mann–Whitney $U$) test or a phylogenetic ANOVA, and the 8 codons reported as differing in RSCU between altitudes (Fig. 7C) were not adjusted for multiple testing across 61 codons.

* **Positive selection on mitochondrial `atp4`, `atp9`, `mttB` and plastid `clpP` represents convergent molecular adaptation to high-altitude environments: [Fragile].**  
  While `HyPhy aBSREL` detects episodic diversifying selection ($\omega > 1$, adjusted $p < 0.05$) on several high-altitude terminal branches in these four genes (Table S25), two critical controls are missing:
  1. **No symmetric comparison against low-altitude branches:** In an exploratory `aBSREL` scan across all branches of a 59-species tree, finding 2–4 positively selected high-altitude branches does not demonstrate an association with altitude unless the proportion of positively selected branches in high-altitude species is statistically compared against the proportion in low-altitude species (e.g., via Fisher's exact test or a foreground-vs-background branch-site test). Furthermore, plastid `clpP` is well known to undergo rapid, lineage-wide structural acceleration and pseudogenization/intron loss across specific angiosperm clades (e.g., `Ericaceae`, `Primulaceae`, `Caryophyllales`) regardless of elevation.
  2. **Confounding by mitochondrial C-to-U RNA editing:** In plant mitochondria, C-to-U RNA editing frequently converts genomic `C` codons back to ancestral `U` codons to restore conserved amino acid residues. When a plant lineage loses an RNA editing site by genomic `C -> T` substitution (retroprocessing) or gains/shifts editing sites, DNA-based codon models (`aBSREL`) score these as nonsynonymous substitutions even when the translated protein sequence is unchanged. Notably, Fig. 3 shows that `mttB` has one of the highest densities of C-to-U RNA editing sites in the entire mitogenome (~35 sites).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Test Formally for Enrichment of Positive Selection on High-Altitude vs. Low-Altitude Branches
* **WHY:** Listing high-altitude species with significant `aBSREL` $p$-values without reporting how often low-altitude species also show positive selection in the same genes creates an asymmetric confirmation bias.
* **WHAT:** Report the complete list of all branches (both high-altitude and low-altitude) with adjusted $p < 0.05$ in `aBSREL` for all 32 mitochondrial and 77 plastid genes, and perform a formal hypothesis test comparing high-altitude foreground branches against low-altitude background branches.
* **HOW:**
  1. In Table S25, add a column listing all low-altitude branches selected by `aBSREL` alongside the high-altitude branches, and compute a $2 \times 2$ Fisher's exact test for each candidate gene (`atp4`, `atp9`, `mttB`, `clpP`) testing whether high-altitude terminal branches have a higher rate of positive selection than low-altitude terminal branches.
  2. Run `HyPhy RELAX` and `HyPhy BUSTED` (designating all high-altitude terminal branches as the foreground `Test` set and low-altitude branches as the `Reference` set) to test whether selective regime shifts are specifically associated with high elevation.

#### 2. Control for C-to-U RNA Editing in Mitochondrial Positive Selection Analyses (`mttB`, `atp4`, `atp9`)
* **WHY:** Because plant mitochondrial transcripts undergo extensive C-to-U editing prior to translation (especially in `mttB`, Fig. 3), analyzing unedited genomic DNA sequences in `aBSREL` conflates evolutionary changes in C-to-U editing sites (which are often synonymous at the protein level) with genuine amino acid positive selection.
* **WHAT:** Verify whether the positively selected sites/branches inferred in `mttB`, `atp4`, and `atp9` persist when predicted C-to-U RNA editing sites are converted to `T` (`U`) prior to running `aBSREL`.
* **HOW:** Apply `Deepred-Mt` (score $> 0.9$) to the `mttB`, `atp4`, and `atp9` CDSs across the 59 species (or mask known C-to-U editable codon positions), re-run `MACSE` and `HyPhy aBSREL` on the edited coding sequences, and report whether the high-altitude selection signals remain significant.

#### 3. Replace the Paired Wilcoxon Signed-Rank Test with Unpaired and Phylogenetically Controlled Tests for Codon Usage
* **WHY:** In Methods line 82 and the Fig. 7 caption (line 191), the authors state they used the *Wilcoxon Signed-Rank Test* for comparing median `ENc`, `GC3s`, and `RSCU` values between high- and low-altitude groups. Because the 58 species are divided into two independent (unpaired) altitude groups of unequal size and share phylogenetic ancestry, a paired signed-rank test is mathematically inappropriate.
* **WHAT:** Recompute the high- vs. low-altitude comparisons in Fig. 7A–C using an unpaired Wilcoxon rank-sum (Mann–Whitney $U$) test and phylogenetic generalized least squares (`PGLS` / phylogenetic ANOVA), with Benjamini–Hochberg FDR correction across the 61 sense codons in Fig. 7C.
* **HOW:** In R (`v4.3.2`), run `wilcox.test(x ~ altitude, paired = FALSE)` and `phylolm(RSCU ~ altitude, phy = plastome_tree, model = "lambda")` across the 58 species, adjust the resulting $p$-values with `p.adjust(..., method = "BH")`, and update Fig. 7A–C and its caption.

#### 4. Equalize Sequencing Depth in the Organelle Assembler Benchmark or Clarify the Subsampling Strategy
* **WHY:** Methods line 52 states that `10 ~ 20x` short-read datasets were extracted for short-read tools (`GetOrganelle`, `NOVOPlasty`), whereas `ptGAUL` and `Oatk` were run with `coverage set at 150`. Comparing short-read assemblers at 10–20x depth against HiFi assemblers at 150x depth confounds sequencing technology with read depth.
* **WHAT:** Clarify whether `10–20x` refers to nuclear whole-genome coverage (which corresponds to >500x organelle coverage) or organelle coverage, and if the latter, re-test `GetOrganelle` and `NOVOPlasty` at matched 150x organelle coverage (or ~5–10 Gb of total raw short reads).
* **HOW:** Update Table S3 and the Methods section to explicitly report both total sequencing yield (Gb) and estimated organelle coverage depth input to each of the six assembly tools.

#### 5. Minor Editorial and Textual Corrections
* **WHY:** Several minor grammatical and typographical errors appear in the manuscript.
* **WHAT & HOW:**
  1. Fig. 2 caption (line 112): Change `"inverted repeat (IR) regions of the plasmid genome"` to `"plastid genome (plastome)"`.
  2. Methods line 77: Fix duplicate verb `"The IQtree v.2.2.2.6 [42] was used to was used to construct"`.
  3. Methods line 82: Fix typo `"using 'prcomp' fuction"` to `"function"`.
  4. Results line 157: Change `"the mitogenome structure of Rhododendron was highly variability"` to `"highly variable"`.
