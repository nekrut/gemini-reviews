# Review of FEXP_ANON_050

**Overall Score:** **5.1 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **4.2 / 8.0**  
* **Score Breakdown:** Rigor: 1.7/3.5 | Claims: 1.3/2.5 | Biology: 1.2/2.0 | Reproducibility: 0.9/2.0

---

## 1. Blinded Metadata Perception

* **Perceived Field & Subfield:** Ethnopharmacology / Gastroenterology / Host–Microbiome Interactions in Precancerous Gastric Lesions
* **Study Design:** Preclinical rat intervention evaluating dose-dependent effects of the herbal formulation Weifuchun (WFC) on N-methyl-N'-nitro-N-nitrosoguanidine (MNNG)-induced precancerous lesions of gastric cancer (PLGC), combining UPLC-Q-TOF-MS chemical profiling, histopathology, ELISA, Western blotting, and 16S rRNA sequencing of gastric contents and feces.
* **Model System & Sample Size:** Male Sprague–Dawley (SD) rats ($N = 34$ initial: $n = 8$ Normal Control [NC], $n = 26$ MNNG model; after sacrificing 2 NC and 2 Model rats at week 10 for model confirmation, $n = 6$ per group in NC, PLGC, PLGC+L-WFC [0.3 g/kg/d], PLGC+M-WFC [0.6 g/kg/d], and PLGC+H-WFC [1.2 g/kg/d]; 16S rRNA sequencing conducted on $n = 6$ rats/group in NC, PLGC, and PLGC+H-WFC).
* **Perceived Methodological Maturity:** Moderate experimental execution in the animal pharmacology arm, but weakened by causal overinterpretation of pooled cross-group Spearman correlations, self-contradictory discussion of *Coprococcus* literature, omission of a prominent pathobiont (*Desulfovibrio*) bloom in the treated group, incomplete sentences in the Results, and absence of public repository accession numbers for the 16S sequencing data.

---

## 2. Executive Summary & Editorial Verdict

This manuscript investigates the therapeutic effects of Weifuchun (WFC) in an 18-week rat model of MNNG-induced precancerous lesions of gastric cancer (PLGC; 10 weeks modeling followed by 8 weeks concurrent MNNG + WFC administration at 0.3, 0.6, and 1.2 g/kg/day; $n = 6$ per group). Using UPLC-Q-TOF-MS, the authors qualitatively annotate 78 positive-ion and 77 negative-ion compounds in WFC. In vivo, WFC dose-dependently attenuates gastric mucosal atrophy, intestinal metaplasia, and PCNA-positive proliferation (AOD reduced by 13.84% and 20.78% in M-WFC and H-WFC), lowers serum pro-inflammatory cytokines (TNF-$\alpha$, IL-6, IL-1$\beta$, IL-8), restores serum PGI/PGII and gastrin, and inhibits gastric mucosal IL-6, p-JAK1/JAK1, and p-STAT3/STAT3 protein levels (by 50.30%, 74.20%, and 64.93% in H-WFC). 16S rRNA V3–V4 sequencing of gastric contents and fecal samples in the NC, PLGC, and PLGC+H-WFC groups ($n = 6$ each) shows partial restoration of community structure and enrichment of the genus *Coprococcus*, which correlates negatively with IL-6 and PCNA across samples.

**Editorial Verdict: Major Revision (Mixed / Salvageable).** The dose-dependent histological, biochemical, and Western blot data demonstrating that WFC mitigates MNNG-induced gastric mucosal injury and suppresses IL-6/JAK1/STAT3 phosphorylation are consistent and well-presented. However, the manuscript overreaches by claiming a causal chain in which WFC alleviates PLGC *by* restoring *Coprococcus* homeostasis to inhibit the IL-6/JAK1/STAT3 pathway. In reality, the link between *Coprococcus* and IL-6/PCNA rests entirely on unadjusted Spearman correlations pooled across treatment groups (Figure 11), which automatically produces significant correlations between any variable altered by MNNG/WFC without establishing within-group covariance or causal mediation. Furthermore, the Discussion contradicts itself by citing a study in which ginseng *decreases* *Coprococcus* to explain why WFC *increases* *Coprococcus*, completely ignores its own LEfSe finding that high-dose WFC significantly enriches the sulfate-reducing pathobiont *Desulfovibrio* in the gut (Figure 9), leaves a truncated sentence in the Results, and fails to deposit the raw 16S rRNA reads in a public sequence archive. These issues can be resolved through statistical re-analysis, deposition of raw sequencing reads, and careful reframing of the causal claims.

### Specific Conclusions and Assessment of Support

* **WFC dose-dependently ameliorates MNNG-induced gastric mucosal pathology, reduces PCNA proliferation, lowers serum inflammatory cytokines, and inhibits gastric IL-6/JAK1/STAT3 phosphorylation: [Well Supported].**  
  Histopathology (Figure 3), PCNA immunohistochemistry (Figure 4), serum ELISA for TNF-$\alpha$, IL-6, IL-1$\beta$, IL-8, PGI/PGII, and gastrin (Figure 5A–F), and gastric mucosal Western blots for IL-6, p-JAK1, and p-STAT3 (Figure 5G–J) show consistent, monotonic dose–response trends across the 0.3, 0.6, and 1.2 g/kg/day WFC groups ($n = 6$ per group).

* **High-dose WFC shifts gastric and fecal microbial community structure toward the normal control state and increases the relative abundance of *Coprococcus*: [Moderately Supported].**  
  16S rRNA profiles of gastric contents (Figure 6) and feces (Figure 8) show higher *Coprococcus* abundance in NC and PLGC+H-WFC rats compared to untreated PLGC rats. However, only the high-dose group was sequenced ($n = 6$/group), preventing dose–response verification of the microbiome changes, and the bioinformatic methods (lines 91, 156, 171) ambiguously mix "OTU clustering" with "ASV/OTU" terminology.

* **WFC alleviates PLGC by maintaining *Coprococcus* homeostasis, which in turn lowers IL-6 levels and inhibits the JAK1/STAT3 pathway: [Overstated].**  
  The abstract and conclusion present a directional causal mediation model (WFC $\rightarrow$ *Coprococcus* $\rightarrow$ $\downarrow$ IL-6/JAK1/STAT3 $\rightarrow$ $\downarrow$ PCNA), but no microbiota manipulation (e.g., antibiotic depletion, fecal microbiota transplantation, or *Coprococcus* supplementation) was performed. The Spearman correlations in Figure 11 pool rats across distinct experimental groups (NC, PLGC, and PLGC+H-WFC), confounding treatment-group separation with biological microbe–host coupling.

* **WFC comprehensively restores beneficial intestinal microbiota homeostasis in PLGC rats: [Fragile].**  
  While WFC restores overall alpha diversity and *Coprococcus* in feces, LEfSe analysis of the intestinal microbiota (Figure 9, line 175) reveals that the PLGC+H-WFC group is specifically enriched for `g_Desulfovibrio`, `f_Desulfovibrionaceae`, `o_Desulfovibrionales`, and `c_Deltaproteobacteria`. *Desulfovibrio* is a sulfate-reducing pathobiont that generates cytotoxic hydrogen sulfide ($\text{H}_2\text{S}$) and lipopolysaccharide (LPS), which is completely unaddressed in the text.

---

## 3. Forensic Defect Inventory

### 1. Ecological Confounding in Pooled Cross-Group Spearman Correlations (Pillars 1, 3, 4)
* **Defect:** In Figure 10 and Figure 11, Spearman correlations are computed between bacterial genera (*Coprococcus*, *Ruminococcus*, *Allobaculum*, *Bifidobacterium*) and host markers (IL-6, PCNA) across the pooled experimental groups, and the caption to Figure 11 states simply `n = 6` without clarifying whether $N = 18$ rats (3 groups $\times$ $n = 6$) or only 6 rats were included.
* **WHY:** When two variables (e.g., *Coprococcus* and IL-6) both differ strongly between untreated PLGC rats and NC/H-WFC rats in opposite directions, pooling the groups guarantees a negative correlation due to group-mean separation (an instance of Simpson's paradox / group-induced confounding), even if within-group correlation is zero.
* **WHAT:** Report the exact total sample size ($N$) in Figures 10–11, compute within-group (or group-adjusted partial) Spearman correlations, and apply Benjamini–Hochberg FDR correction across all tested taxon–marker pairs.
* **HOW:** Calculate partial Spearman correlations between each genus and IL-6 / PCNA controlling for treatment group indicator variables (or within the PLGC+H-WFC group alone), report the FDR-adjusted $q$-values, and temper the Abstract and Conclusion to describe these associations as correlative rather than causal.

### 2. Self-Contradictory Literature Citation on *Coprococcus* and Unaddressed *Desulfovibrio* Bloom (Pillars 3, 5, 6)
* **Defect:** (a) In the Discussion (line 206), to support the claim that WFC acts by increasing *Coprococcus*, the authors write: *"Research suggests that the active ingredient Renshen in WFC can effectively mitigate colitis by reducing cell infiltration and lowering levels of inflammatory markers such as IL-6 and TNF-$\alpha$ [67]. Additionally, it regulates gut microbiota diversity and composition, decreases the relative abundance of Coprococcus, and supports the recovery of both gut microbiota and the intestinal mucosal barrier [68]."* Citing a study where ginseng *decreases* *Coprococcus* directly contradicts the authors' mechanism where WFC *increases* *Coprococcus*. (b) In Section "16S rRNA sequencing analysis of rat intestinal microbiota" (line 175, Figure 9), LEfSe shows that the top biomarker enriched in the PLGC+H-WFC fecal microbiota is `g_Desulfovibrio` (`f_Desulfovibrionaceae`, `c_Deltaproteobacteria`), whereas the untreated PLGC group is enriched for `g_Lactobacillus`. The Discussion ignores the *Desulfovibrio* enrichment entirely.
* **WHY:** Selective reporting of favorable taxa (*Coprococcus*) while ignoring a treatment-induced bloom of a known $\text{H}_2\text{S}$- and LPS-producing pathobiont (*Desulfovibrio*) creates an asymmetric, biased interpretation of microbiome remodeling.
* **WHAT:** Resolve the contradiction regarding reference [68] and explicitly discuss the biological implications of *Desulfovibrio* enrichment in the PLGC+H-WFC group and *Lactobacillus* enrichment in the PLGC group.
* **HOW:** Add a paragraph in the Discussion addressing why *Lactobacillus* is elevated in MNNG-damaged stomachs/intestines (consistent with acid/nitrosamine tolerance reported in gastric cancer cohorts) and why high-dose WFC enriched *Desulfovibrio*, noting that WFC's microbial effects are not uniformly probiotic.

### 3. Missing Public Sequence Repository Accession for 16S rRNA Data (Pillar 7)
* **Defect:** The Data Availability Statement reads: *"All relevant data are within the manuscript and its Supporting Information files."* However, raw 16S rRNA amplicon sequencing FASTQ files for the 18 gastric content samples and 18 fecal samples are not deposited in NCBI SRA, ENA, or CNCB/GSA.
* **WHY:** Without raw sequencing reads and metadata mapping files, the 16S diversity, taxonomic classification, and LEfSe results cannot be independently verified or re-analyzed.
* **WHAT & HOW:** Deposit the 36 raw 16S rRNA FASTQ files into a public archive (e.g., NCBI BioProject/SRA or GSA) and add the accession number to the Data Availability Statement.

### 4. Textual Truncation, Typographical Errors, and Methodological Ambiguities (Pillar 7)
* **Defect:**
  1. Line 140 ends with a truncated, incomplete sentence: *"Specifically, relative to the PLGC group, PLGC+L-WFC group."*
  2. Line 100 contains an incomplete clause: *"For multiple comparison correction across, the FDR was controlled using the Benjamini-Hochberg method."*
  3. Line 37 states that dried WFC extract was *"reconstituted in a 0.1% (v/v) formaldehyde solution and analyzed utilizing a UPLC-Q-TOF-MS"*—this is almost certainly a mistranslation of **formic acid** (`HCOOH`, the standard LC-MS mobile phase modifier), as formaldehyde (`HCHO`) chemically cross-links analytes and is never used for UPLC-Q-TOF-MS reconstitution.
  4. Lines 158 and 173 misspell *"Venn diagram"* as *"Veen graph"* / *"Veen diagram"*, line 9 mispells *"Coprococcus"* as *"Coprocuccus"*, and lines 160 and 175 misspell `PLGC + H-WFC` as `LGC + H-WFC`.
* **WHY:** Truncated sentences omit quantitative results for the low-dose WFC group, and reporting "0.1% formaldehyde" instead of "0.1% formic acid" corrupts the analytical chemistry protocol.
* **WHAT & HOW:** Complete the truncated sentence on line 140 with the exact percentage changes and $p$-values for the `PLGC+L-WFC` group; replace *"0.1% (v/v) formaldehyde solution"* on line 37 with *"0.1% (v/v) formic acid solution"*; clarify in Section "16S rRNA sequencing" (line 91) whether QIIME2 DADA2 (ASVs) or OTU clustering (97% identity) was used; and fix the typographical errors (`Venn`, `Coprococcus`, `PLGC + H-WFC`).

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.7** | **3.5** | Solid dose–response pharmacology (histology, ELISA, Western blot), but microbiome–host integration relies on group-confounded Spearman correlations without within-group or partial correlation controls; ambiguity between ASV denoising and OTU clustering. |
| **2. Claim-to-Evidence Alignment** | **1.3** | **2.5** | Overstates correlative 16S findings as a directional causal mechanism (*Coprococcus* mediating IL-6/JAK1/STAT3 inhibition); selectively omits the *Desulfovibrio* bloom in the H-WFC group. |
| **3. Data Integrity & Biological Plausibility** | **1.2** | **2.0** | Self-contradictory discussion citing Renshen *decreasing* *Coprococcus* to explain WFC *increasing* *Coprococcus*; unaddressed enrichment of sulfate-reducing *Desulfovibrio* in H-WFC; mistranslation of formic acid as formaldehyde in UPLC-Q-TOF-MS. |
| **4. Reproducibility & Data Integrity** | **0.9** | **2.0** | No public repository accession (SRA/ENA/GSA) for the 36 16S rRNA sequencing libraries; truncated sentence omitting L-WFC cytokine results on line 140; unclear sample size ($n=6$ vs $N=18$) in Figure 11 caption. |
| **Scientific Core Score** | **4.2** | **8.0** | Sum of Rigor (1.7) + Claims (1.3) + Biology (1.2). |
| **Overall Composite Score** | **5.1** | **10.0** | **Mixed / Salvageable Tier** (Sum of all four dimensions). |
