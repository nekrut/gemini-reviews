# Review of ANON_71

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **2.5 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.6/3.5 | Claims: 0.5/2.5 | Biology: 0.6/2.0 | Reproducibility: 0.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript re-analyzes 13 publicly available 16S rRNA (V4 region) amplicon sequencing samples of Atlantic cod (*Gadus morhua*) gut microbiota drawn from two previously published studies: seven wild-caught fish from northern Norway (`PRJEB22384`, Riiser et al. [50]; 4 from Lofoten and 3 from Sørøya) and six laboratory-maintained fish originally caught in southern Norway (`PRJEB21667`, Bagi et al. [11]; 3 laboratory control fish and 3 fish experimentally exposed to $0.01\text{ ppm}$ dispersed crude oil). Using both DADA2 amplicon sequence variants (ASVs, Silva v132) and QIIME 1.8 operational taxonomic units (OTUs, 97% identity, Silva v119), the authors compare alpha/beta diversity (PERMANOVA $R^2 = 0.467, p < 0.002$) and run `DESeq2` differential abundance tests to argue that differences between the two groups—and the presence of genera such as *Novosphingobium*, *Sphingomonas*, *Alcanivorax*, *Cycloclasticus*, and *Deferribacteraceae* in the southern dataset—reflect environmental polycyclic aromatic hydrocarbon (PAH) pollution in southern Norwegian waters.

The study's experimental design and statistical inferences are fundamentally invalid. First, the comparison between "pristine northern Norway" and "anthropogenically impacted southern Norway" is completely confounded by study batch (`PRJEB22384` vs. `PRJEB21667`), housing and diet (wild-caught marine fish vs. captive laboratory-held fish fed in tanks), and direct experimental manipulation (three of the six "southern Norway" fish were deliberately dosed with $0.01\text{ ppm}$ crude oil in the laboratory). Second, no environmental or tissue PAH concentrations were measured in either region. Third, the authors acknowledge in the Discussion (line 69) that **no genus remained statistically significant after Benjamini–Hochberg false discovery rate (FDR) correction**, yet proceed to interpret unadjusted $p$-values ($p = 0.01\text{--}0.05$) as biological evidence. Fourth, when the DADA2 ASV pipeline failed to detect putative PAH-degrading genera as differentially abundant, the authors switched to a legacy QIIME 1.8 OTU pipeline (Section 3.3) to highlight low-count taxa. Because the study design completely conflates study batch, captivity, and laboratory oil dosing with geography, its conclusions cannot be salvaged through computational re-analysis of these 13 samples alone.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Differences in Atlantic cod gut microbiota between the northern ($n = 7$) and southern ($n = 6$) datasets reflect environmental anthropogenic PAH contamination in southern Norway: [Methodologically Flawed].**  
  The seven northern samples (`PRJEB22384`) were collected directly from wild fish at sea, whereas the six southern samples (`PRJEB21667`) came from fish maintained in laboratory tanks (and half were experimentally exposed to $0.01\text{ ppm}$ dispersed crude oil). In cross-study 16S rRNA comparisons, differences in DNA extraction protocols, PCR reagents, sequencing runs, laboratory tank water, and commercial feed overwhelm biological geographic variation. Notably, the dominance of *Firmicutes* (*Lactobacillus*, *Ruminococcus*, *Tyzzerella*) and *Bacteroidetes* (*Alistipes*, *Parabacteroides*, *Rikenella*) in the southern cohort versus marine *Vibrionales* (*Photobacterium*) and *Fusobacteria* in the wild northern cohort is a classic signature of commercial aquaculture/laboratory diet versus wild piscivorous diet, not marine oil pollution.

* **Sixteen bacterial genera (ASVs) and ten putative biomarker genera (OTUs) are significantly differentially abundant between northern and southern Norway cod guts: [Methodologically Flawed].**  
  In Section 4 (line 69), the authors state that *"results analyzed for false discovery rate by Benjamini–Hochberg tests were all above the corrected p value"* and that they chose *"to interpret the results beyond the traditional p value."* Reporting unadjusted `DESeq2` Wald test $p$-values ($p = 0.01\text{--}0.05$) across dozens of tested genera when 100% of taxa fail FDR correction equates random false positives (and batch effects across $N = 13$ samples) with biological signal.

* **Exclusive presence of *Novosphingobium*, *Sphingobium*, *Sphingomonas*, *Rhodococcus*, *Microbacterium*, *Alcanivorax*, and *Cycloclasticus* in southern Norway cod indicates environmental exposure to oil-related compounds: [Methodologically Flawed].**  
  First, the text contradicts itself on exclusivity: line 69 states that *Alcanivorax* and *Cycloclasticus* *"were present only in the southern Norway fish gut microbiomes,"* and in the very next sentence admits *"For the last two genera, few reads (1–3) were found in some samples from northern Norway."* Second, these genera did not differ significantly in the DADA2 ASV analysis (line 62), prompting an ad hoc switch to QIIME 1.8 OTUs. Third, *Sphingomonas*, *Novosphingobium*, *Sphingobium*, *Rhodococcus*, *Microbacterium*, and *Pedobacter* are well-documented reagent and DNA extraction kit contaminants ("kitome") in 16S sequencing studies, which naturally segregate by study batch (`PRJEB21667` vs. `PRJEB22384`). Finally, three of the six southern samples were experimentally dosed with crude oil in the laboratory.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Separate Wild Field Surveys from Laboratory Tank Experiments and Remove Oil-Dosed Fish from Baseline Comparisons
* **WHY:** Pooling 3 laboratory control fish and 3 laboratory crude-oil-exposed ($0.01\text{ ppm}$) fish from `PRJEB21667` and comparing them against 7 wild-caught fish from `PRJEB22384` confounds geography with laboratory captivity, diet, sequencing batch, and intentional oil dosing.
* **WHAT:** Never pool laboratory oil-dosed fish with unexposed controls when testing for wild environmental contamination. Restrict any baseline comparison in `PRJEB21667` to the $n = 3$ unexposed controls, and explicitly model `Study/Captivity` as a primary confounding factor.
* **HOW:** Re-run the ordination and `DESeq2` analyses splitting the samples into four explicit groups: `Northern_Wild_Lofoten` ($n=4$), `Northern_Wild_Soroya` ($n=3$), `Southern_Lab_Control` ($n=3$), and `Southern_Lab_Oil_0.01ppm` ($n=3$), or acquire wild-caught, unmanipulated cod gut samples from southern and northern Norway processed within a single extraction and sequencing batch alongside water/bile PAH chemical measurements.

#### 2. Enforce Benjamini–Hochberg FDR Correction and Eliminate Pipeline Switching Between ASVs and OTUs
* **WHY:** Reporting unadjusted $p \le 0.05$ after all taxa fail Benjamini–Hochberg FDR correction (line 69) violates basic multiple-testing standards. Similarly, switching from DADA2 ASVs (Silva v132) in Section 3.2 to QIIME 1.8 OTUs (Silva v119) in Section 3.3 because the ASV pipeline did not yield significant differences for target genera is post-hoc selective reporting.
* **WHAT:** Use a single, modern denoising pipeline (DADA2 ASVs with Silva v132/v138) throughout the entire manuscript, and report only taxa passing Benjamini–Hochberg FDR $q < 0.05$ (or $q < 0.10$) as differentially abundant.
* **HOW:** Remove the legacy QIIME 1.8 / Silva v119 OTU workflow (lines 38, 60–62), include a table of exact ASV counts, log2 fold changes, raw $p$-values, and BH-adjusted $q$-values for all tested genera, and state in the Abstract and Results that no individual genus reached statistical significance after multiple-testing correction.

#### 3. Screen Putative Hydrocarbon-Degrading Genera Against Known Sequencing Reagent ("Kitome") Contaminants
* **WHY:** Genera highlighted as southern Norway oil indicators (*Sphingomonas*, *Novosphingobium*, *Sphingobium*, *Rhodococcus*, *Microbacterium*, *Pedobacter*) are ubiquitous contaminants of commercial DNA extraction kits and PCR master mixes that routinely appear as batch-specific artifacts when comparing two independent BioProjects (`PRJEB22384` vs. `PRJEB21667`).
* **WHAT:** Audit the low-abundance genera against published contaminant lists (e.g., Salter et al., 2014) and extraction blank controls from the original studies.
* **HOW:** Cross-reference all 65 candidate genera in Table S1 against standard reagent contaminant catalogs, flag kitome-associated Alphaproteobacteria and Actinobacteria in the Results and Discussion, and filter out ASVs supported by only 1–3 reads across samples.

#### 4. Reconcile Contradictory Clustering and Ordination Descriptions Across Methods, Results, and Figure Captions
* **WHY:** The manuscript gives mutually contradictory descriptions of how Figure 2a and Figure 2c were generated:
  - For Figure 2a, Methods line 36 states *"Ward's hierarchical clustering method based on Euclidean distance was applied to interpret the distance matrix using average linkages"* (mixing two incompatible linkage methods—Ward's and average linkage—on Euclidean distance), whereas the Figure 2a caption (line 95) states *"generated through Bray–Curtis distance metric and Ward's linkage method."*
  - For Figure 2c, Results line 52 describes it as a *"weighted UniFrac distance metric-based PCoA plot [that] explained 69.4% of the taxonomic variation,"* whereas the Figure 2c caption (line 95) calls it *"Nonmetric multidimensional scaling (NMDS) beta diversity ordination"* (NMDS axes do not have percent variance explained).
* **WHAT & HOW:** Inspect the exact R / `MicrobiomeAnalyst` calls used to generate Figure 2a and 2c, and correct lines 36, 52, and 95 so the distance metric (Bray–Curtis vs. Euclidean), linkage rule (Ward's vs. average), and ordination method (PCoA vs. NMDS) match the plotted figures.

#### 5. Technical, Tabular, and Citation Cleanup
* **WHY:** Misaligned tables, self-contradictory sentences, and broken citations undermine technical accuracy.
* **WHAT & HOW:**
  1. **Table 1 (lines 84–90):** The table header has 4 columns (`Area | Latitude | Longitude | Samples`), but the first row has 5 entries (`Northern Norway | Lofoten | 68°10′19″ N | 13°45′00″ E | 4`), shifting all subsequent entries into the wrong columns. Add a `Location` column so all 5 fields align properly.
  2. **Line 62:** Reference `[12]` (an OSPAR Commission oil/gas production report) is incorrectly cited as the source of the *"65 bacterial genera... that had been previously identified as PAH degraders [12]."* Cite the actual microbiological reference.
  3. **Line 48 & Line 57:** Fix typos `"OUT-based results"` $\to$ `"OTU-based results"` (line 48), `"Fusabacterium"` $\to$ `"Fusobacterium"`, and `"Mucispirilum"` $\to$ `"Mucispirillum"` (line 57).
