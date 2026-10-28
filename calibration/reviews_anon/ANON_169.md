# Review of ANON_169

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.3 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.4/3.5 | Claims: 1.4/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.2/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript performs a genome-wide survey of the sodium-coupled (`SLC5` / `ScSMCT`, 16 genes) and proton-coupled (`SLC16` / `ScMCT`, 54 genes) monocarboxylate transporter families in the razor clam (*Sinonovacula constricta*). Using the published *S. constricta* genome assembly (`PRJNA559038`), the authors characterize gene copy numbers across 21 metazoan species, map the 70 razor-clam genes onto 15 chromosomes, perform MCScanX synteny analysis with three other bivalves (*Meretrix meretrix*, *Cyclina sinensis*, and *Crassostrea gigas*), reconstruct Maximum Likelihood and Bayesian phylogenies, run codon site-model selection tests (`EasyCodeML`), examine gill RNA-seq expression across salinity, ammonia nitrogen, and thermal stress datasets, and profile seven upregulated genes over a 72-hour time course via qRT-PCR.

The comparative genomic catalog confirming lineage-specific expansion of `SLC5` and `SLC16` paralogs in bivalves (particularly `ScMCT14` with 22 copies and 35.7% tandem duplication) is a useful resource for mollusk genomics. However, the study's evolutionary and physiological conclusions are weakened by three major methodological and interpretive flaws: (1) running PAML codon site models across an alignment of all 54 deeply divergent `ScMCT` paralogs (spanning subfamilies MCT1 through MCT14), where the stringent M1a vs. M2a test is completely non-significant ($p = 1.0000$) and the three M8 sites (`2V`, `13I`, `14A`) sit in the poorly aligned hypervariable N-terminus; (2) attributing anaerobic glycolysis and lactate efflux functions to `ScMCT12`, `ScMCT13`, and `ScMCT14` paralogs under stress, despite the Introduction correctly noting that only MCT1–MCT4 are established proton-coupled lactate/pyruvate transporters whereas MCT12–MCT14 transport creatine or unknown non-lactate substrates; and (3) analyzing the 72-hour qRT-PCR stress time course by comparing all timepoints solely against 0 h rather than against the time-matched control groups described in the Methods, while reporting inconsistent biological replicate counts ($n = 3$ vs. $n = 6$) and an unreleased SRA submission placeholder (`SUB14268245`).

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Lineage-specific expansion of `ScSMCT` (16 genes) and `ScMCT` (54 genes) in *S. constricta* and other bivalves driven partly by tandem duplication: [Well Supported].**  
  The homology, conserved domain (CD-search/SMART), chromosome mapping (Fig. 1B), and phylogenetic analyses (Fig. 2, Fig. S1) consistently support a major expansion of SLC16 and SLC5 paralogs in bivalves (36–78 copies vs. $\le 2$ copies per subfamily in most vertebrates), with highest syntenic conservation between *S. constricta* and fellow venerid clam *M. meretrix* (6 collinear pairs).

* **Positive selection at three codon sites (`2V`, `13I`, `14A`) drove the adaptive evolution of `ScMCT` proteins in *S. constricta*: [Methodologically Flawed].**  
  In Section 2.4 and Table 2, the authors fitted `EasyCodeML` site models to a single alignment of all 54 `ScMCT` paralogs and a single alignment of all 16 `ScSMCT` paralogs. Aligning 54 paralogs from 14 distinct `SLC16` subfamilies violates the PAML assumption of moderate divergence, introducing synonymous substitution saturation ($d_S \gg 1$) and alignment errors in terminal/loop regions. Critically, the conservative positive-selection likelihood ratio test (M1a vs. M2a) yielded $p = 1.0000$ with 0 sites for both `SMCT` and `MCT` (Table 2); only the M7 vs. M8 test—which is prone to false positives when $\omega$ distributions deviate from a single beta distribution across divergent subfamilies—flagged three N-terminal residues (`2V`, `13I`, `14A`). Furthermore, the Discussion (page 7, line 171) contradicts the Results by stating that *"three sites of ScMCTs were under purification selection... indicating that positive selection may play an important role."*

* **Upregulation of `ScMCT12_5`, `ScMCT14_16`, and `ScMCT13_1` under ammonia and thermal stress mediates lactate efflux from anaerobic glycolysis: [Overstated].**  
  As the authors state in the Introduction (line 15), within the 14-member SLC16 family, *"only four members (MCT1, MCT2, MCT3, MCT4) transport monocarboxylate with a proton across the plasma membrane"*, whereas other members transport thyroid hormones (MCT8), aromatic amino acids (MCT10), or creatine (MCT12), or remain orphan transporters (MCT13, MCT14). While `ScMCT1_2` and `ScMCT2_3` (which respond to salinity in Fig. 4B) are genuine orthologs of lactate-transporting MCT1/MCT2, extrapolating lactate efflux and intracellular pH buffering to `ScMCT12_5` and `ScMCT14_16` under ammonia stress (or `ScMCT13_1` under heat stress) is not supported without substrate transport assays or tissue lactate measurements.

* **Temporal qRT-PCR expression profiles of seven `ScMCT`/`ScSMCT` genes across 72 hours of salinity, ammonia, and heat stress: [Moderately Supported].**  
  Although the qRT-PCR time courses (Fig. 4) broadly corroborate the RNA-seq trends, the statistical design has three weaknesses: (1) despite allocating clams into normal seawater (25 ppt) and control temperature (25 °C) groups (Section 2.6, line 54), Figure 4 compares post-challenge timepoints (3–72 h) against the 0 h baseline via one-way ANOVA rather than against time-matched unchallenged controls via two-way ANOVA; (2) the ammonia concentration used in qRT-PCR (46 mg/L, line 54) is nearly fourfold lower than in the RNA-seq dataset (180 mg/L, Fig. 3B caption, line 145) without explanation; and (3) the number of biological replicates is inconsistently reported as *"three biological replicates"* (line 54), *"six biological parallels"* (line 56), and *"n = 3"* (Fig. 4 caption, line 162).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Restrict PAML Codon Selection Analyses to Orthologous Clades or Recently Expanded Subfamily Paralogs
* **WHY:** Running `CodeML` site models on a simultaneous alignment of 54 `ScMCT` genes spanning all SLC16 subfamilies produces synonymous saturation and N-terminal alignment artifacts, and M1a vs. M2a yielded $p = 1.0000$.
* **WHAT:** Run `CodeML` (or `HyPhy` MEME/BUSTED) separately within well-aligned, recently expanded subfamily clades (e.g., the 22 `ScMCT14` paralogs, or the bivalve `MCT1`/`MCT2` orthogroups) after trimming gapped N/C-termini, and require concordance between M1a/M2a and M7/M8 before claiming positive selection.
* **HOW:** Extract coding sequences for each monophyletic subfamily from Figure 2, align codons with `PRANK` or `MACSE`, mask columns with $>20\%$ gaps, re-run `EasyCodeML` M1a vs. M2a and M7 vs. M8 per subfamily, and correct the self-contradictory sentence on page 7, line 171 (*"under purification selection... indicating that positive selection"*).

#### 2. Re-Analyze qRT-PCR Time-Course Data Using Two-Way ANOVA with Time-Matched Controls and Clarify Replicate Counts
* **WHY:** Comparing 3–72 h treatment samples only against 0 h confounds tank-handling and circadian effects with stress responses, and the text contradicts itself on whether $n = 3$ or $n = 6$ biological replicates were analyzed.
* **WHAT:** Clarify whether the six sampled clams per timepoint were pooled in pairs into $n = 3$ biological replicates, and include the parallel control group (25 ppt seawater / 25 °C) across timepoints in a two-way ANOVA (`Treatment × Time`) or explicitly note if only 0 h controls were assayed for ammonia stress.
* **HOW:** Update Section 2.6 (lines 54–56) and the Figure 4 caption to state unambiguously how the 6 sampled gills map to the $n = 3$ error bars, and discuss the difference between the 46 mg/L qRT-PCR ammonia challenge and the 180 mg/L RNA-seq ammonia dataset.

#### 3. Distinguish Canonical Lactate Transporters (`ScMCT1–4`) from Non-Canonical/Orphan `SLC16` Subfamilies (`ScMCT12–14`)
* **WHY:** Only SLC16A1–A4 (MCT1–4) are validated proton-coupled lactate/pyruvate transporters, whereas the ammonia- and heat-induced genes (`ScMCT12_5`, `ScMCT13_1`, `ScMCT14_16`) belong to subfamilies with distinct or uncharacterized substrates.
* **WHAT:** Revise the Abstract, Results (Section 3.3–3.4), and Discussion (page 7) to distinguish between canonical lactate transporters (`ScMCT1_2`, `ScMCT2_3`, `ScSMCT1_1`, `ScSMCT1_2`) and non-canonical `SLC16` members (`ScMCT12_5`, `ScMCT13_1`, `ScMCT14_16`).
* **HOW:** Frame the upregulation of `ScMCT12_5` and `ScMCT14_16` under ammonia stress as transport of creatine, amino-acid derivatives, or uncharacterized organic osmolytes/metabolites rather than assuming they export glycolytic lactate.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Several biophysical inconsistencies, missing methodological details, and typographical errors appear in the manuscript.
* **WHAT & HOW:**
  1. **Section 3.1 (page 3, line 93):** Re-check the minimum protein length and molecular weight in *"the amino acids residues of ScSMCT and ScMCT proteins are from 371 to 788, with the putative molecular weights from 18.280 kDa to 85.476 kDa."* A 371-amino-acid polypeptide has a molecular weight of $\sim 40\text{ kDa}$, not $18.280\text{ kDa}$ (which corresponds to $\sim 165\text{ aa}$); correct either the minimum residue count or the minimum kDa in the text and Table S1.
  2. **Section 2.1 vs. Section 3.1 (line 93) & Discussion (line 169):** State which software tool (e.g., WoLF PSORT or Cell-PLoc) was used to predict subcellular localization in Section 2.1, and reconcile whether `ScSMCT2_7` was predicted in the *"nucleus"* (line 93) or *"nuclear membrane"* (line 169).
  3. **Section 2.5 (page 2, line 49):** Replace the temporary NCBI submission ID `SUB14268245` with the permanent public BioProject (`PRJNA...`) or SRA (`SRR...`) accession numbers, and clarify how `DESeq2` (which operates on raw read counts, not TPM) was used alongside TPM heatmap visualization, including whether Benjamini–Hochberg adjusted $p$-values (`padj < 0.05`) were used.
  4. **Table 1 (page 3, line 68) & Section 3.1 (line 95):** Correct primer name `ScMCT_2R` to `ScMCT1_2R`, and fix the typo `"up to 6siz"` in line 95 to `"up to six"`.
