# Review of FEXP_ANON_028

**Overall Score:** **2.6 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.8 / 8.0**  
* **Score Breakdown:** Rigor: 0.5/3.5 | Claims: 0.5/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.8/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_028`
* **Perceived Research Domain:** Plant plastome comparative genomics and synonymous codon usage analysis (*Caragana* spp., family Fabaceae/Leguminosae).
* **Study Design:** Comparative analysis of synonymous codon usage bias and phylogenetic relationships across 52 protein-coding sequences ($\ge 300\text{ bp}$) from five *Caragana* chloroplast genomes (*C. arborescens* `MT211962`, *C. jubata* `MT211963`, *C. opulens* `OQ656872`, *C. tibetica* `OQ942026`, and *C. turkestanica* `OQ942027`).
* **Primary Methods:** Plastome assembly and annotation (`SPAdes` v3.10.1, `BLAST` v2.2.25, `HMMER` v3.1b2, `ARAGORN` v1.2.38), codon usage metrics (`EMBOSS cusp` for `GC1, GC2, GC3, GCall`; `CodonW` v1.4.2 for `GC3s, ENC, CAI, CBI, Fop, RSCU`), correlation heatmaps (`SPSS`), neutrality/ENC/PR2 plots (`ggplot2` in R), and RSCU hierarchical clustering vs. Bayesian phylogenetics (`PhyloSuite`).

---

## 2. Executive Summary & Editorial Verdict

This manuscript analyzes synonymous codon usage across 52 filtered protein-coding genes ($\ge 300\text{ bp}$) in the chloroplast genomes of five *Caragana* species (*C. arborescens*, *C. jubata*, *C. opulens*, *C. tibetica*, and *C. turkestanica*; GenBank accessions `MT211962`, `MT211963`, `OQ656872`, `OQ942026`, `OQ942027`). Using `EMBOSS cusp` and `CodonW` v1.4.2, the authors compute codon position GC contents (`GC1, GC2, GC3, GCall, GC3s`), `ENC`, `CAI`, `CBI`, `Fop`, and `RSCU`, construct neutrality, ENC, and PR2 plots, define 9–12 optimal codons per species ($\text{RSCU} > 1$ and $\Delta\text{RSCU} \ge 0.08$ between top and bottom 10% ENC genes), and compare RSCU clustering with plastome phylogenies.

While the five *Caragana* plastome sequences are publicly available in GenBank with documented herbarium vouchers, the manuscript's analytical pipeline and text contain severe computational, mathematical, and biological errors that invalidate its primary comparative claims. Most critically, a forensic audit of the correlation analysis (Section "Analysis of codon bias-related parameters", line 153, and Figure 2) reveals a **spreadsheet row-alignment bug between `EMBOSS-cusp` and `CodonW`** in three of the five species: whereas `GC3` (calculated in `EMBOSS-cusp`) and `GC3s` (calculated in `CodonW`) measure almost identical quantities and must correlate at $r > 0.92$ across plastid genes (as seen in *C. arborescens* $r = 0.928$ and *C. jubata* $r = 0.938$), their correlation drops to random noise in *C. opulens* ($r = 0.158$), *C. tibetica* ($r = 0.177$), and *C. turkestanica* ($r = 0.198$), while the sign of `ENC` vs. `GC1` simultaneously flips. Because the 52 orthologous plastid genes are $>98\%$ identical across all five species (Table 4 shows species-wide `GC3` differs by $\le 0.30\%$), this collapse of `GC3`-vs.-`GC3s` correlation proves that gene rows were mismatched when merging `EMBOSS-cusp` and `CodonW` outputs in Excel for the three `OQ` genomes—and this data-merging artifact is the sole basis for the Abstract's headline claim of *"two potential groups among the five species"*! In addition, the Results and Discussion directly contradict one another on whether the ENC-plot supports mutation or natural selection, the Background states that there are 61 total codons in the genetic code (3 stop + 58 sense codons), the mathematical formulas in the Methods were left blank, and the Conclusion asserts that *"Caragana arborescens forms a sister group with itself"*.

### Specific Assessment of Core Claims

* **Chloroplast coding sequences of the five *Caragana* species have conserved GC content (`36.91%–37.05%`), follow $\text{GC}_1 > \text{GC}_2 > \text{GC}_3$, and prefer A/U-ending codons with weak overall codon usage bias ($\text{ENC} = 35.82\text{–}56.77$):** **[Well Supported].**  
  Table 4 and the 29 shared high-frequency codons ($\text{RSCU} > 1$, 96.6% ending in A or U) accurately reflect the standard A+T-rich compositional structure of IRLC legume plastomes.

* **Correlation and parameter analyses divide the five *Caragana* species into two distinct groups (*C. arborescens* + *C. jubata* vs. *C. opulens* + *C. tibetica* + *C. turkestanica*):** **[Methodologically Flawed].**  
  In line 153 (and Fig. 2), the authors report that `GC3` (from `EMBOSS-cusp`) and `GC3s` (from `CodonW`) correlate at $r = 0.928$ and $0.938$ in *C. arborescens* (`MT211962`) and *C. jubata* (`MT211963`), but only at $r = 0.158, 0.177,$ and $0.198$ in *C. opulens* (`OQ656872`), *C. tibetica* (`OQ942026`), and *C. turkestanica* (`OQ942027`), accompanied by a reversal in the correlation between `ENC` (`CodonW`) and `GC1` (`EMBOSS-cusp`). Mathematically, for any set of 52 protein-coding genes, `GC3` (all 3rd codon positions) and `GC3s` (synonymous 3rd codon positions, i.e., excluding only `AUG` Met and `UGG` Trp) are nearly identical variables ($r > 0.92$). A correlation of $r = 0.158\text{–}0.198$ between `GC3` and `GC3s` in three species whose plastid CDSs are nearly identical in sequence to the other two species is physically impossible unless the 52 gene rows from `EMBOSS-cusp` and `CodonW` were sorted in different orders when combined in Excel (Methods line 97). Thus, the two-group division reported in the Abstract is a spreadsheet row-misalignment artifact.

* **ENC-plot and PR2-plot analyses demonstrate that natural selection predominantly shapes codon usage in *Caragana* while mutation has no significant influence:** **[Methodologically Flawed].**  
  The manuscript's own sections flatly contradict each other:
  1. In **Results line 174** (ENC-plot analysis), the authors conclude: *"The narrow range of ENC deviations suggests that **the codon bias in these species is mainly caused by mutations**."*
  2. In **Discussion line 212**, the authors write the exact opposite: *"ENC plot analysis revealed that **natural selection predominantly influences most genes, whereas a smaller proportion is influenced by mutation effects**. Further PR2 plot analysis revealed that **mutation pressure has no influence on codon bias**... with gene mutations having no significant influence."*
  Furthermore, the neutrality plot regression slopes of $\text{GC}_{12}$ on $\text{GC}_3$ (`0.35` to `0.43`, line 161) are actually steep for plastid genomes (indicating $35\%\text{–}43\%$ direct mutational contribution across codon positions), and PR2 asymmetry ($\text{G}_3 > \text{C}_3, \text{T}_3 > \text{A}_3$) in plastomes reflects strand-specific replication/transcription deamination bias as well as selection, not a complete absence of mutation pressure.

* **Phylogenetic analysis shows *C. tibetica* and *C. jubata* are sister species grouped with *C. opulens*, while *C. arborescens* and *C. turkestanica* cluster together:** **[Moderately Supported].**  
  The phylogenetic relationships in Figure 8B–C are consistent with section/series classifications in *Caragana*, although the phylogenetic methods (line 125) omit all details of alignment software, substitution model selection, MCMC chain length, burn-in, and outgroup taxa, and the Conclusion (line 239) nonsensical states that *"Caragana arborescens forms a sister group with itself"*.

---

## 3. Forensic Defect Inventory

### Defect 1: Spreadsheet Row Misalignment Between `EMBOSS-cusp` and `CodonW` Outputs in Three Species (Pillar 2, Pillar 3 & Pillar 4)
* **Location:** Abstract (line 7), Methods (lines 92, 97), Results (line 153, Figure 2), Conclusion (line 239).
* **Diagnostic Finding:** `GC1, GC2, GC3, GCall` were computed in `EMBOSS-cusp`, whereas `GC3s, ENC, CAI, CBI, Fop` were computed in `CodonW 1.4.2` and merged in Excel. For *C. opulens*, *C. tibetica*, and *C. turkestanica*, the correlation between `GC3` and `GC3s` collapses from $\sim 0.93$ to $0.158\text{–}0.198$ and cross-program correlations (`ENC` vs. `GC1`, `CAI` vs. `GC1`) invert compared to *C. arborescens* and *C. jubata*. Because `GC3` and `GC3s` differ only by `AUG` and `UGG` codons within the exact same gene, $r(\text{GC3}, \text{GC3s}) < 0.20$ proves that the 52 gene rows from the two software programs were not matched by gene name in those three species.
* **Remediation:** Re-join the `EMBOSS-cusp` and `CodonW` tables strictly by gene identifier (`gene_id`) across all five species, recompute the correlation matrices (Figure 2) and neutrality/ENC plots, and remove the artifactual claim that the five species split into two correlation groups.

### Defect 2: Direct Self-Contradiction Between Results and Discussion on ENC-Plot Interpretation (Pillar 3 & Pillar 5)
* **Location:** Results line 174 vs. Discussion line 212.
* **Diagnostic Finding:** Results line 174 states that the narrow ENC ratio distribution (`(-0.10, 0.10]`) *"suggests that the codon bias in these species is mainly caused by mutations"*, whereas Discussion line 212 claims that *"ENC plot analysis revealed that natural selection predominantly influences most genes"* and that *"mutation pressure has no influence on codon bias"*.
* **Remediation:** Reconcile the Results and Discussion to consistently state that both mutational composition bias (explaining $35\%\text{–}43\%$ of variance in neutrality plots and the clustering of ENC ratios near $0$) and natural selection contribute to codon usage bias.

### Defect 3: Elementary Genetic Code Error (`61 = 3 + 58` Codons) and Omitted Mathematical Equations (Pillar 6 & Pillar 7)
* **Location:** Background (line 24) and Methods (lines 104, 108, 174).
* **Diagnostic Finding:**
  1. **Genetic code count error:** Line 24 states: *"Of the 61 codons, three are stop codons, while the remaining 58 encode the 20 amino acids."* The standard genetic code has **64** codons: 3 stop codons and **61** sense codons encoding the 20 amino acids.
  2. **Missing equations:** Line 104 (*"The formula for calculating the standard curve is as follows [23]:"*) and line 108 (*"The calculation formula of ENC ratio is as follows [26]:"*) are followed by blank lines where equations ① and ② (referenced in line 174) were completely omitted.
* **Remediation:** Correct line 24 to state *"Of the 64 codons, three are stop codons, while the remaining 61 encode the 20 amino acids"*, and insert Wright's expected ENC equation $\text{ENC}_{\text{exp}} = 2 + s + \frac{29}{s^2 + (1-s)^2}$ and the ENC ratio equation $\frac{\text{ENC}_{\text{exp}} - \text{ENC}_{\text{obs}}}{\text{ENC}_{\text{exp}}}$ at lines 104 and 108.

### Defect 4: Pervasive Factual, Geographic, and Editorial Errors Across Text, Tables, and Figures (Pillar 7)
* **Location:** Abstract (line 7), Background (line 28), Table 1 (lines 41–48), Methods (line 49, 125), Table 3 (lines 73–80), Figure 4 caption (line 172), Conclusion (line 239).
* **Diagnostic Finding:**
  1. **Conclusion biological absurdity:** Line 239 states *"while Caragana arborescens forms a sister group with itself"* (instead of with *Caragana turkestanica*).
  2. **Duplicate Figure 4 caption:** Figure 4 (the ENC-plot) is mislabeled *"Fig. 4: Neutrality plot analysis of five Caragana species"* (duplicating the caption of Figure 3).
  3. **Identical GPS coordinates for different regions in Table 1:** *C. jubata* (labeled `Haibei Tibetan Autonomous Prefecture`) and *C. opulens* (labeled `Xining City`) are given the exact same GPS coordinates (`N37°36′53.34′′, E101°19′18.63′′`).
  4. **GC content contradiction:** Abstract line 7 reports the GC content of the five species as `36.00% to 37.10%`, Background line 28 reports whole-plastome GC content as `34.30% to 34.71%`, and Table 4 reports CDS `GCall` as `36.91% to 37.05%`.
  5. **Wrong tool URL and incomplete phylogenetic methods:** Line 49 gives the URL for `SSPACE` (`baseclear.com/.../sspace-standard/`) as the URL for `SPAdes v3.10.1`. Line 125 states that Bayesian trees were built in `PhyloSuite` without reporting the sequence aligner, evolutionary substitution model, MCMC generations, sampling frequency, burn-in, or outgroup species shown in Figure 8B–C.
  6. **Typos:** Line 38 ends with a stray word *"sent."*; Table 1 title writes *"satistical table"*; Table 3 writes *"photosesten I"*, *"photosesten II"*, and *"Acetyl-CoA-Carboxyase"*.
* **Remediation:** Fix the sister-group statement in line 239, correct the Figure 4 caption to *"ENC-plot analysis of five Caragana species"*, verify and correct the GPS coordinates in Table 1, clarify whole-genome vs. CDS GC content in the Abstract, provide complete `PhyloSuite`/`MrBayes` parameters in line 125, and fix all typographical errors.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.5** | **3.5** | Fatal row-misalignment bug between `EMBOSS-cusp` (`GC3`) and `CodonW` (`GC3s`) in 3 of 5 species ($r = 0.158\text{–}0.198$ instead of $>0.92$) invalidates the correlation heatmaps; missing mathematical formulas in Methods; undocumented Bayesian phylogenetic parameters. |
| **2. Claim-to-Evidence Alignment** | **0.5** | **2.5** | Headline Abstract claim of two species groups in parameter correlations is an artifact of misaligned gene rows; Discussion directly contradicts Results on the ENC-plot conclusion and falsely claims mutation has zero influence on codon bias. |
| **3. Data Integrity & Biological Plausibility** | **0.8** | **2.0** | Five plastome assemblies in GenBank are valid IRLC legume plastomes, but undermined by the elementary genetic code error (`61 = 3 + 58` codons), identical GPS coordinates assigned to different prefectures in Table 1, and claiming a species *"forms a sister group with itself"*. |
| **4. Reproducibility & Data Integrity** | **0.8** | **2.0** | GenBank accessions (`MT211962`, `MT211963`, `OQ656872`, `OQ942026`, `OQ942027`) and herbarium voucher IDs (`QhST20190077–0081`) are provided, but equations ① and ② are missing, Figure 4 has the wrong caption, and Table 1/3 contain numerous typos. |
| **Total Composite Score** | **2.6** | **10.0** | **Fundamentally Invalid** (Scientific Core Score: **1.8 / 8.0**) |
