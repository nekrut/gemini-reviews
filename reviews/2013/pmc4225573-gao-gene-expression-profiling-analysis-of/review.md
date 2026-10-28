# Review of PMC4225573 (PMID:24256571)

**Manuscript Title:** Gene expression profiling analysis of the putamen for the investigation of compensatory mechanisms in Parkinson's disease  
**Authors:** Gao L, Gao H, Zhou H, Xu Y.  
**Journal / Preprint:** *BMC Neurol* (2013; `PMC4225573` / `PMID:24256571` / `10.1186/1471-2377-13-181`)  
**Calibration Study Cohort:** Cohort A — Known Invalid / Refuted (`A46` | Double-Blinded as `ANON_77`)  
**Overall Score:** **2.6 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.6/3.5 | Claims: 0.5/2.5 | Biology: 0.7/2.0 | Reproducibility: 0.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript re-analyzes a publicly available microarray dataset (GEO: GSE20291) comprising postmortem putamen tissue from 15 Parkinson's disease (PD) patients and 15 pathologically normal controls profiled on the Affymetrix Human Genome U133A array (12,688 Entrez genes). Using an unadjusted two-sample Student's $t$-test ($p < 0.05$), the authors report 715 differentially expressed genes (DEGs; 268 upregulated and 447 downregulated). They perform Gene Ontology (GO) and KEGG pathway enrichment using DAVID (Benjamini–Hochberg adjusted $p < 0.10$), select 40 DEGs from 9 neuron-related GO categories, map those 40 genes onto the Human Protein Reference Database (HPRD) protein–protein interaction (PPI) network, and apply the Clique Percolation Method (CFinder, $k=3$) to identify a subnetwork containing *PRKCA*, *BCL2*, and *CDC42*. Based on these analyses, the authors conclude that altered expression of *OPHN1*, *PAX6*, connexin 43, *CAMK2*, *PRKCA*, *CDC42*, and *BCL2* promotes the growth of intrinsic striatal tyrosine hydroxylase (TH) interneurons and reduces functional excitatory synapses in PD.

The study is undermined by a foundational statistical failure: screening 12,688 genes with an unadjusted Student's $t$-test at $p < 0.05$ and no fold-change threshold yields an expected $12,688 \times 0.05 \approx 634$ false-positive genes under a completely null hypothesis. Thus, approximately 89% of the 715 reported DEGs are expected to be random statistical noise. All downstream GO/KEGG enrichments, HPRD hub rankings (which reflect literature curation density for well-studied cancer/signaling proteins rather than PD-specific regulation), and mechanistic claims regarding rare intrinsic striatal TH interneurons (which make up $<0.1\%$ of cells in bulk putamen tissue) rest on this uncalibrated gene list. In addition, the Methods section contains internal contradictions regarding sample size (30 vs. 35 samples) and misattributes ethical approval of a public US cohort (GSE20291) to the authors' home institution. Complete statistical re-analysis with empirical Bayes moderation, false discovery rate (FDR) control, proper background specification, and substantial reframing of the biological claims are required.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **715 genes (268 upregulated, 447 downregulated) are differentially expressed in the putamen of PD patients compared to controls (Abstract, Results line 74): [Methodologically Flawed].**  
  DEGs were selected solely on the basis of an unadjusted Student's $t$-test $p < 0.05$ across 12,688 genes with no multiple-testing correction and no minimum fold-change requirement (Methods, line 52). Under the global null hypothesis, $12,688 \times 0.05 = 634.4$ genes will pass $p < 0.05$ by chance alone. Observing 715 nominal hits provides negligible evidence of true differential expression for individual genes, and no table of log-fold changes, $t$-statistics, or FDR $q$-values is provided anywhere in the manuscript.

* **DEGs in the PD putamen are significantly enriched for neuron projection morphogenesis, gap junction, and calcium signaling pathways (Results lines 79–130, Tables 1 and 2): [Fragile].**  
  Feeding 715 mostly noise genes into DAVID without specifying the 12,688 genes present on the Affymetrix HG-U133A array as the custom background population (rather than the default whole human genome) inflates enrichment significance for well-annotated neural and signaling genes overrepresented on the U133A chip. Moreover, 4 of the 9 neuron-related GO terms used to build the 40-gene set did not even reach an adjusted $p < 0.05$ (passing only a relaxed $p < 0.1$ cutoff, line 79).

* ***PRKCA*, *RXRA*, *CDC42*, and *BCL2* act as central hub regulators and functional modules driving striatal neuron remodeling in PD (Results lines 135–145, Figures 1 and 2): [Methodologically Flawed].**  
  The authors projected the 40 neuron-annotated candidate genes onto the entire HPRD database (7,670 chip-overlapped genes and 31,041 literature-curated interactions) and ranked them by their global degree in HPRD (*PRKCA* degree = 166, *RXRA* = 81, *CDC42* = 70, *BCL2* = 69). In literature-curated PPI databases, global connectivity is heavily confounded by historical research volume—ubiquitous signaling proteins like PKC$\alpha$, Bcl-2, and Cdc42 have hundreds of cataloged interactions regardless of the tissue or disease studied. No permutation test against random sets of 40 neuron-annotated genes was performed.

* **Altered expression of *OPHN1*, *PAX6*, connexin 43, *CAMK2*, *PRKCA*, *CDC42*, and *BCL2* promotes intrinsic striatal TH interneuron growth and reduces functional excitatory synapses (Abstract Conclusion, Discussion lines 156–171): [Overstated].**  
  Bulk putamen RNA comprises predominantly medium spiny projection neurons, astrocytes, oligodendrocytes, and microglia; intrinsic striatal TH-immunoreactive interneurons are an extremely rare population whose proliferation or survival cannot be inferred from unvalidated bulk microarray signals. Furthermore, the Discussion (line 160) contradicts the Abstract conclusion: the authors note that *downregulation* of CaMKII reduces functional excitatory synapses, state that CaMKII was *upregulated* in their study, yet conclude in the Abstract (line 26) that the observed gene changes "reduce the functional excitatory synapses."

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Replace Unadjusted Student's $t$-Tests with Moderated $t$-Statistics and False Discovery Rate Control
* **WHY:** Testing 12,688 genes with an unadjusted $t$-test at $p < 0.05$ yields ~634 false positives by chance, rendering the 715-gene list statistically indistinguishable from noise.
* **WHAT:** Re-compute differential expression in GSE20291 using `limma` (empirical Bayes moderated $t$-statistics) with Benjamini–Hochberg FDR adjustment, and report a complete table of test statistics.
* **HOW:** In R/Bioconductor, fit a linear model (`lmFit` followed by `eBayes`) across the RMA-normalized expression matrix of the 15 PD and 15 control samples. Report the number of genes passing $\text{FDR} < 0.05$ (or $\text{FDR} < 0.10$ with $|\log_2\text{FC}| > 0.5$). If few individual genes survive genome-wide FDR correction due to the modest sample size ($n=15$ per group), use rank-based Gene Set Enrichment Analysis (GSEA) across the entire ranked list of 12,688 genes rather than hard-thresholding at unadjusted $p < 0.05$.

#### 2. Use the Exact Microarray Platform Background and Degree-Preserving Null Permutations for Network Analysis
* **WHY:** Default whole-genome backgrounds in DAVID artificially inflate neuronal GO terms for older expression arrays, and ranking genes by total HPRD degree selects ubiquitous literature hubs (*PRKCA*, *BCL2*) irrespective of PD biology.
* **WHAT:** Specify the exact 12,688 Entrez genes present on the Affymetrix HG-U133A array as the background list in enrichment tests, and normalize PPI hub/module analyses against degree-matched null networks.
* **HOW:** Upload the list of 12,688 array Entrez IDs as the custom background in DAVID (or `clusterProfiler::enrichGO` / `enrichKEGG`). For PPI analysis, construct the induced subgraph among differentially expressed genes (or co-expression modules via WGCNA on the putamen expression matrix) and test whether observed node degrees and CFinder clique modules exceed those obtained from 1,000 degree-preserving random rewirings (or 1,000 random draws of 40 neuronal genes from the array).

#### 3. Account for Bulk Tissue Cellular Composition and Remove Unsupported Claims About Rare TH Interneurons
* **WHY:** Bulk putamen microarray profiles cannot isolate gene expression changes within rare striatal TH+ interneurons or measure synapse density, and the CaMKII directionality argument in the Discussion (line 160) contradicts the Abstract (line 26).
* **WHAT:** Remove claims that the microarray data demonstrate intrinsic striatal TH interneuron growth or reduced excitatory synapses, fix the CaMKII contradiction, and assess cell-type marker expression.
* **HOW:** Check and report the actual $\log_2\text{FC}$, $t$-statistic, and adjusted $p$-value for *TH* (tyrosine hydroxylase) and canonical striatal cell-type markers (e.g., *PPP1R1B*/DARPP-32, *DRD1*, *DRD2*, *GFAP*, *MBP*) in GSE20291. Rewrite the Abstract Conclusion and Discussion (lines 26, 156–171) to state that the observed transcriptomic signals reflect bulk putamen tissue remodeling and require cell-type-resolved validation.

#### 4. Resolve Data Provenance Misattribution and Sample Size Contradictions in Methods
* **WHY:** Line 45 states that the 15 PD samples in GSE20291 were "approved by the ethic committee of the Fourth Affiliated Hospital of China Medical University," whereas GSE20291 is a public dataset generated at the University of Washington / Oregon Health & Science University (ref. [16], Zhang et al. 2005). In addition, line 45 reports "30 samples" (15 PD, 15 control), whereas line 47 reports "35 samples."
* **WHAT & HOW:** Correct line 45 to accurately state that GSE20291 is a de-identified public dataset downloaded from NCBI GEO ( originally collected under the institutional review board of the originating study [16]) requiring no new human subjects approval. Correct the sample count discrepancy between lines 45 and 47 (confirming whether 30 or 35 CEL files were normalized), and fix typos such as `"Total715 DEGs"` (line 21), `"interneuronsas"` (line 35), and `"inhibitIP3-mediated"` (line 166).
