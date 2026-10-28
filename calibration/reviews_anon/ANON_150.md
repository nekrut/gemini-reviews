# Review of ANON_150

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.1 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.1/3.5 | Claims: 2.4/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript systematically characterizes reagent and DNA extraction kit contamination ("the kitome") in high-throughput 16S rRNA amplicon sequencing and shotgun metagenomics, demonstrating how background bacterial DNA distorts microbial community profiles in low-biomass samples. Using a pure culture of *Salmonella bongori* (strain NCTC-12419) serially diluted ten-fold over five orders of magnitude ($\sim 10^8$ down to $10^3$ cells), the authors (1) perform 16S rRNA V1–V2 Illumina MiSeq sequencing at 20 and 40 PCR cycles across three independent laboratories (WTSI, ICL, UB) using distinct production lots of the FastDNA SPIN Kit for Soil; (2) quantify absolute background 16S rRNA gene copy numbers via V4 qPCR against a *Vibrio natriegens* standard curve; (3) perform Nextera XT Illumina MiSeq shotgun metagenomic sequencing of the dilution series extracted in parallel with four commercial kits (FastDNA SPIN, MoBio UltraClean, QIAamp Stool, and PSP Spin Stool); and (4) re-analyze a longitudinal 454 16S rRNA dataset of 182 infant nasopharyngeal swabs from the Maela cohort in Thailand to show how chronological extraction across four kit lots created a spurious age-associated PCoA clustering artifact. Raw 16S and metagenomic sequencing reads are publicly deposited in ENA under accessions ERP006737 and ERP006808, with sample-level metadata and read counts in Additional file 1.

This is a foundational, rigorously designed methodological study that combines controlled multi-center spike-in titration series, orthogonal qPCR biomass quantification, multi-kit shotgun metagenomics, and an authentic clinical re-extraction validation to establish an essential standard for microbiome research. The experimental evidence is clear and directly supports all primary claims. The only minor limitations are: (1) within each laboratory and extraction kit, each dilution point of the *S. bongori* series was extracted as a single replicate ($n = 1$ per dilution per kit/site), preventing estimation of within-lot extraction variance; (2) the clinical nasopharyngeal 454 dataset was rarefied to a very low depth of 200 reads per sample using unweighted Jaccard PCoA; and (3) while Box 1 provides sound qualitative guidelines, the manuscript stops short of formulating a quantitative dilution/subtraction model relating input biomass and qPCR copy number to expected contaminant proportion. These minor points do not detract from the paper's major contribution and can be easily addressed in the text.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Commercial DNA extraction kits and laboratory reagents harbor ubiquitous, batch- and manufacturer-specific bacterial DNA contamination (~500 16S rRNA gene copies/$\mu$L of eluate in the tested FastDNA kit) that dominates 16S rRNA and shotgun metagenomic profiles below $10^3\text{–}10^4$ input cells: [Well Supported].**  
  Demonstrated across three independent laboratories (Figure 1), four commercial extraction kits in PCR-free Nextera XT shotgun metagenomics (Figure 3), and triplicate V4 16S qPCR showing a linear decrease from $10^8$ to $10^5$ input cells followed by an invariant floor of ~500 copies/$\mu$L below dilution 3 while no-template qPCR water controls remained below the detection limit of 45 copies (Figure 2).

* **Contaminant taxonomic profiles are reproducible within a specific extraction kit batch/laboratory but differ markedly across kit manufacturers and lot numbers: [Well Supported].**  
  In the *S. bongori* dilution series, 63 bacterial taxa were absent from template-free PCR water blanks but consistently present at $>0.1\%$ abundance across serially diluted extractions, with distinct kit-specific signatures in shotgun metagenomics processed concurrently in a single lab (e.g., *Burkholderiaceae*/*Enterobacteriaceae* in FastDNA SPIN vs. *Bradyrhizobiaceae*/*Chitinophagaceae* in PSP vs. diverse *Bacillaceae*/*Microbacteriaceae* in QIAamp; Figure 3b).

* **Non-randomized processing of low-biomass clinical samples across different extraction kit batches can generate false biological associations, as demonstrated in the infant nasopharyngeal cohort: [Well Supported].**  
  In the 182-swab Maela infant nasopharyngeal dataset, chronological extraction across four FastDNA SPIN kit lots produced an apparent early-life vs. late-infancy PCoA separation (Figure 4a) that mapped one-to-one onto extraction kit batch (Figure 4b,d,e), vanished upon removing kit-associated OTUs (Figure 4c), and was definitively falsified when archived aliquots were re-extracted with a clean kit lot and found to lack the putative "founder" OTUs.

* **Simple *in silico* subtraction of all taxa detected in negative controls or contaminant lists is insufficient when genuine sample members overlap with reagent contaminants or cross-contaminate blanks: [Well Supported].**  
  The Discussion (lines 131–136) and Box 1 appropriately caution that blind removal of genera listed in Table 1 (which includes common human skin/mucosal genera such as *Streptococcus*, *Corynebacterium*, *Propionibacterium*, and *Escherichia*) can erase true biological signal, and instead advocate batch randomization, lot tracking, concurrent negative extraction controls, qPCR input thresholding, and strain/oligotype resolution.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Formulate a Quantitative Mixing Model Linking qPCR Input Biomass to Expected Contaminant Read Fraction
* **WHY:** Figure 1 (16S relative abundance) and Figure 2 (qPCR total 16S copy number) measure the exact same *S. bongori* dilution series (FastDNA lot #15447), yet the two datasets are presented qualitatively in separate sections. Because total sequenced reads are a two-component mixture of template biomass ($N_{\text{sample}}$) and constant kit background ($N_{\text{kit}} \approx 500\text{ copies}/\mu\text{L} \times 50\text{ }\mu\text{L} = 2.5 \times 10^4\text{ copies}$), the expected proportion of contaminant reads follows the simple hyperbolic competitive-amplification model:
  $$P_{\text{contam}}(D) = \frac{N_{\text{kit}}}{N_{\text{sample}}(D) + N_{\text{kit}}}$$
* **WHAT:** Overlay or correlate the observed fraction of non-*Salmonella* 16S reads in Figure 1a against the qPCR-predicted contaminant fraction $N_{\text{kit}} / (N_{\text{total}}(D))$ from Figure 2.
* **HOW:** Using the read counts in Additional file 1 (Table S1a) and the triplicate qPCR copy numbers in Figure 2, add a supplementary panel or paragraph showing the quantitative agreement between the qPCR background floor (~500 copies/$\mu$L) and the empirical 50% tipping point between dilutions 3 and 4 ($\sim 10^4\text{–}10^5$ cells).

#### 2. Account for Index-Hopping / Cross-Talk and Input-Volume Differences Across Centres
* **WHY:** In the Methods ("DNA extraction", line 157), UB and WTSI extracted $200\text{ }\mu\text{L}$ of *S. bongori* culture and eluted in $50\text{ }\mu\text{L}$ (a $4\times$ concentration factor), whereas ICL extracted $500\text{ }\mu\text{L}$ and eluted in $100\text{ }\mu\text{L}$ (a $5\times$ concentration factor, and $2.5\times$ more total input cells contacting the column matrix). Additionally, in multiplexed Illumina MiSeq runs, low-biomass samples and negative controls amplified for 40 cycles can acquire a small fraction ($0.1\%\text{–}1\%$) of *S. bongori* reads from high-biomass undiluted libraries via barcode cross-talk or primer contamination.
* **WHAT:** Note the $2.5\times$ difference in absolute cell input at ICL vs. UB/WTSI when comparing the dilution tipping points in Figure 1a, and report the exact percentage of *S. bongori* reads observed in the template-free PCR negative controls (`con` columns in Figure 1a) to quantify baseline sequencing cross-talk.
* **HOW:** Add a brief sentence in the Results ("16S rRNA gene sequencing of a pure *Salmonella bongori* culture", line 73) stating the percentage of *S. bongori* reads found in the `con` lanes of Table S1a and noting the $500\text{ }\mu\text{L}$ vs. $200\text{ }\mu\text{L}$ extraction volume at ICL.

#### 3. Quantify the Variance Explained ($R^2$) by Extraction Kit Batch vs. Infant Age in the Nasopharyngeal PCoA
* **WHY:** In Figure 4a–c, the shift in PCoA clustering before and after removing contaminant OTUs is shown visually, and individual OTUs are tested with `metastats` ($p < 0.01$), but no formal multivariate effect size ($R^2$ from PERMANOVA / `adonis` or ANOSIM in `mothur`) is reported to compare the fraction of community variance explained by `Kit_Batch` vs. `Infant_Age` before and after contaminant filtering.
* **WHAT:** Report the `AMOVA` / `HOMOVA` or PERMANOVA test statistics and $R^2$ values for `Kit_Batch` and `Age_Group` on the Jaccard/Bray-Curtis distance matrices corresponding to Figure 4a, 4b, and 4c.
* **HOW:** Run `amova` in `mothur` (or `vegan::adonis2` in R) on the distance matrices for Figure 4a/b (unfiltered) and Figure 4c (filtered, as well as at a higher subsampling depth such as 1,000 reads if supported by the 454 read distribution) and include the $F$-statistics, $R^2$, and $p$-values in the text on line 114.

#### 4. Technical and Editorial Cleanup
* **WHY:** A few minor typographical errors appear in the text and captions.
* **WHAT & HOW:**
  1. **Figure 2 caption (line 92):** States `"While the copy number initially reduces in tandem with increased dilution, plateauing after four dilutions..."`, whereas the main text (line 86) states `"However, at the third dilution copy number remained stable"`—harmonize the dilution numbering (dilution 3 vs. dilution 4) between line 86 and the Figure 2 caption.
  2. **Results, line 105:** Correct the family spelling `"Comomonadaceae"` to `"Comamonadaceae"`.
  3. **Methods, line 157:** Correct `"spanned a range of sample biomass from approximately 10 8 down to 10 3 cells"`—on the same line, change `"across the five-fold serial dilutions"` to `"across the five ten-fold serial dilutions"`.
