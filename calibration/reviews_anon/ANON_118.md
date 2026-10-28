# Review of ANON_118

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.8 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.8/3.5 | Claims: 1.5/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.3/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript presents a comparative pangenome and phylogenomic analysis of *Enterococcus faecium* and *Enterococcus lactis* using publicly available GenBank assemblies as of early 2023. Starting from 2,727 *E. faecium* and 111 *E. lactis* genomes, the authors filtered for CheckM quality ($\ge 90\%$ completeness, $\le 10\%$ contamination) and dereplicated 2,825 assemblies at $99.5\%$ nucleotide identity across 92 concatenated UBCG2 housekeeping genes, yielding 192 representative genomes (128 *E. faecium* and 64 *E. lactis*). Using Average Nucleotide Identity (ANI), 16S rRNA vs. core-gene maximum-likelihood phylogenies, Roary/PANINI accessory genome clustering, KEGG metabolic reconstruction, and BLAST searches against CARD, VFDB, BAGEL4/BACTIBASE, and mobileOG-db, the authors demonstrate that 16S rRNA and carbohydrate metabolism cannot separate the two species (explaining widespread GenBank misannotation of *E. lactis* as *E. faecium*), whereas core and accessory genomes divide them into *E. lactis*, *E. faecium* subclade I (mixed human/animal/food origins), and *E. faecium* subclade II (exclusively human clinical isolates with larger genomes, lower GC content, and enriched mobile antibiotic resistance, virulence, and bacteriocin genes). Only generic NCBI taxon links are provided in the Data Availability statement, with assembly accessions listed in Table S1.

The core taxonomic and genomic findings—that historical "clade B" / non-pathogenic *E. faecium* strains in GenBank are frequently misclassified *E. lactis* and that hospital-adapted *E. faecium* (subclade II, corresponding to the well-established clade A1) undergoes genome expansion via horizontal transfer of low-GC mobile elements—are solid and consistent with prior literature. However, the manuscript is weakened by four preventable issues: (1) severe gene-annotation errors in Figure 6 where bacterial resistance genes (`fosB`, `vatE`, `aad(6)`, `mel`, `eatAv`) are misidentified as eukaryotic transcription factors, vacuolar ATPases, and proteases, alongside a direct contradiction regarding the exotoxin gene `speB`; (2) phylogenetic overinterpretation claiming that extant *E. faecium* evolved from extant *E. lactis*; (3) invalid statistical testing in Figures 2 and 5 where a composite group (`EF`) is compared against its own subsets (`EF-I` and `EF-II`) using uncorrected Student's $t$-tests; and (4) unexamined dereplication bias when collapsing 2,825 genomes to 192 representatives. All of these flaws can be resolved through careful re-annotation, appropriate non-parametric/phylogenetic statistics, and textual revision.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **16S rRNA sequences and core carbon metabolic pathways fail to distinguish *E. faecium* from *E. lactis*, whereas whole-genome ANI ($>97.8\%$) and 92 core genes cleanly separate them and reveal extensive GenBank misclassification: [Well Supported].**  
  The contrast between the polyphyletic 16S rRNA tree (Fig. S2) and the reciprocally monophyletic 92-gene UBCG2 phylogeny (Fig. 1) and ANI heatmap (Fig. S1) convincingly demonstrates why routine 16S-based identification has resulted in numerous *E. lactis* assemblies being deposited in GenBank as *E. faecium*.

* ***E. faecium* subclade II (human-derived) possesses significantly larger genomes, lower GC content, and higher abundances of antibiotic resistance, virulence, bacteriocin, and mobile element genes than subclade I and *E. lactis*: [Moderately Supported].**  
  The empirical separation in genome size ($2.98 \pm 0.20\text{ Mb}$ vs. $2.67 \pm 0.18\text{ Mb}$ in subclade I), GC content ($37.82\%$ vs. $38.03\%$), PANINI accessory clustering (Fig. 3), and PERMANOVA of resistance/virulence profiles ($R^2 = 0.5525, P = 0.001$; Fig. 7) is clear. However, the statistical testing in Figures 2 and 5 applies pairwise Student's $t$-tests across four groups (`EF`, `EF-I`, `EF-II`, and `EL`) without multiple-testing correction, normality verification for discrete gene counts, or accounting for phylogenetic non-independence—and crucially, `EF` is the union of `EF-I` and `EF-II`, violating the two-sample independence assumption of Student's $t$-test whenever `EF` is tested against `EF-I` or `EF-II`.

* ***E. faecium* evolved from *E. lactis*, and *E. faecium* subclade II evolved from subclade I: [Overstated].**  
  In the Discussion (Paragraphs 2 and 3), the authors state that *"Our phylogenetic analyses suggest E. faecium, primarily from humans and animals, may have evolved from E. lactis"* and *"E. faecium subclade II strains... may have evolved from E. faecium subclade I strains."* In Figure 1, *E. faecium* and *E. lactis* form reciprocally monophyletic sister clades rooted by *E. hirae*; a sister-group relationship on a phylogenetic tree indicates divergence from a shared common ancestor, not that one extant species is the ancestor of the other.

* **Specific antibiotic resistance and virulence factor gene profiles distinguish the clades, and no exotoxin genes were detected in any genome: [Methodologically Flawed].**  
  Section "Abundance and distribution..." (Paragraph 4) states: *"Notably, no genes classified as exotoxins, indicating a direct virulence for hosts, were detected."* Yet Figure 6B and its caption (Category 10: exoenzyme) explicitly plot and list `speB`, defined as *"pyrogenic exotoxin"*! Furthermore, the Figure 6 caption contains multiple severe gene-symbol expansion errors caused by mapping bacterial AMR/virulence gene symbols to unrelated eukaryotic or heterologous homonyms:
  1. `fosB` (fosfomycin resistance bacillithiol transferase) is mislabeled as *"transcription factor AP-1 subunit"* (the mammalian oncogene FosB).
  2. `vatE` (streptogramin A $O$-acetyltransferase) is mislabeled as *"vacuolar H+-ATPase E subunit"* (eukaryotic V-ATPase subunit E).
  3. `aad(6)` (aminoglycoside 6-adenylyltransferase) is mislabeled as *"putative aryl-alcohol dehydrogenase"*.
  4. `mel` (macrolide efflux genetic assembly protein) is mislabeled as *"$\alpha$-galactosidase"* (melibiase).
  5. `eatAv` (ABC-F type ribosomal protection protein in Enterococci) is mislabeled in the caption (Category 5) as *"serine protease"* (confusing it with the *E. coli* autotransporter protease EatA), while `msrC` is misspelled as `mcrC` in the main text.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct the Gene Annotations in Figure 6 and Resolve the `speB` Exotoxin Contradiction
* **WHY:** Mislabelling canonical bacterial antibiotic resistance genes (`fosB`, `vatE`, `aad(6)`, `mel`, `eatAv`) as mammalian transcription factors, vacuolar ATPases, and proteases in Figure 6 introduces serious biological errors, and plotting `speB` (pyrogenic exotoxin) in Figure 6B directly contradicts the main-text claim that no exotoxins were detected.
* **WHAT:** Audit all BLASTX hits in Figure 6 against official CARD and VFDB ontology definitions and reconcile the presence/absence of `speB`.
* **HOW:** Replace the erroneous expansions in the Figure 6 caption with their true CARD definitions (`fosB`: fosfomycin thiol transferase; `vatE`: streptogramin A acetyltransferase; `aad(6)`: aminoglycoside 6-adenylyltransferase; `mel`: macrolide efflux protein; `eatAv`: ABC-F ribosomal protection protein), fix the typo `mcrC` $\to$ `msrC` in the Results, and inspect the `speB` BLASTX alignments ($>60\%$ identity threshold) to determine whether they are genuine streptococcal pyrogenic exotoxin homologs or false-positive matches to a housekeeping peptidase.

#### 2. Fix Non-Independent Group Comparisons and Apply Non-Parametric / Phylogenetic Tests
* **WHY:** Comparing the pooled species group `EF` ($N = 128$) against its own constituent subclades `EF-I` and `EF-II` in Figures 2 and 5 violates sample independence, and discrete counts of resistance/virulence/mobile genes are skewed and phylogenetically structured.
* **WHAT:** Remove statistical significance bars comparing `EF` against `EF-I` or `EF-II`, and replace uncorrected Student's $t$-tests among the three mutually exclusive clades (`EF-I`, `EF-II`, `EL`) with Kruskal–Wallis and Dunn's post-hoc tests (with Benjamini–Hochberg adjustment) as well as phylogenetic generalized least squares (PGLS) / phylogenetic ANOVA.
* **HOW:** In R, run `kruskal.test()` followed by `FSA::dunnTest(..., method="bh")` across the three disjoint groups (`EF-I`, `EF-II`, `EL`), and use `phytools::phylANOVA()` on the 92-gene maximum-likelihood tree to verify that differences in genome size, GC content, and mobile element abundance remain significant after controlling for shared ancestry.

#### 3. Quantify Dereplication Representation and Map Clades to Established *E. faecium* Nomenclature
* **WHY:** Dereplicating 2,825 GenBank genomes at $99.5\%$ UBCG2 identity down to 192 representatives treats a singleton environmental isolate and a 500-genome hospital VRE outbreak cluster as equally weighted single data points ($N = 1$), and introducing "subclade I" and "subclade II" without mapping them to the standard *E. faecium* Clade A1 / A2 / B nomenclature obscures comparisons with existing literature.
* **WHAT:** Report the cluster size (number of raw GenBank genomes represented by each of the 192 dereplicated genomes) in Table S1 and Figure 1, and explicitly map subclade I and subclade II to Clades A1 and A2.
* **HOW:** Add a bar track to the outer ring of Figure 1 showing $\log_{10}(\text{cluster size})$ for each representative genome, and test whether the proportion of human vs. animal isolates in subclade I and II changes when weighted by total pre-dereplication genome counts.

#### 4. Reframe Evolutionary Directionality Claims in the Discussion
* **WHY:** A bifurcating tree where *E. faecium* and *E. lactis* are reciprocally monophyletic sister clades does not show that *E. faecium* evolved from extant *E. lactis*.
* **WHAT:** Revise the Discussion to state that *E. faecium* and *E. lactis* diverged from a common ancestor that likely resembled *E. lactis* and *E. faecium* subclade I in having a smaller genome and fewer mobile resistance elements, followed by derived genome expansion and HGT acquisition in the human-adapted *E. faecium* subclade II lineage.
* **HOW:** Replace *"E. faecium... may have evolved from E. lactis"* and *"E. faecium subclade II strains... may have evolved from E. faecium subclade I strains"* in Paragraphs 2–3 of the Discussion with ancestor-descendant language grounded in parsimony/outgroup polarity relative to *E. hirae*.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Inconsistent date stamps, typos, and missing archival files hinder reproducibility.
* **WHAT & HOW:**
  1. **Results vs. Methods Retrieval Date:** Reconcile *"as of January 2023"* (Results, paragraph 1) with *"As of February 2023"* (Methods, paragraph 1).
  2. **Results — PCA Section:** Fix the typo *"PREMANOVA R 2 = 0.5943"* to *"PERMANOVA"*, and *"subclade I countparts"* to *"counterparts"*.
  3. **Data Availability:** Deposit the Newick tree files (Fig. 1 and Fig. 8), the Roary `gene_presence_absence.csv` matrix, and the CARD/VFDB annotation tables in Zenodo or Figshare rather than providing only generic NCBI taxon query URLs.
