<Blinded Review: TIME_ANON_0462>
**Composite Score:** 3.9 / 10.0 (Rigor: 1.1/3.5 | Claims: 1.0/2.5 | Biology: 0.9/2.0 | Reproducibility: 0.9/2.0)
**Bias Category:** Algorithmic/Model
**Verdict:** Reject (Fundamental Flaws)
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Commodity/Hype-Cycle Template
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 3.9/10
VERDICT: FAILED
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This manuscript presents a formulaic, template-driven *in silico* genome-wide catalog of the Small Ubiquitin-related Modifier (*SUMO*) gene family in bread wheat (*Triticum aestivum* L.), reporting 31 *TaSUMO* genes distributed across the A, B, and D subgenomes, followed by automated web-server outputs for phylogenetic trees (MEGA7), MEME motifs, GSDS exon-intron structures, PlantCARE promoter *cis*-elements, psRNATarget miRNA predictions, STRING protein interaction networks, Ka/Ks duplication ratios, public RNA-seq heatmaps ( Wheat Expression Browser), and a minimally described qRT-PCR experiment (`Fig. S12`). Forensic audit reveals severe internal contradictions, biological misconceptions (referring to SUMO post-translational modifiers as *"SUMO transporter proteins"*), contradictory duplication pair counts (`11` pairs in the Abstract vs. `8` pairs in the Results and Conclusion), evolutionary misinterpretations (claiming that monocot-specific and dicot-specific phylogenetic clusters prove gene amplification occurred *before* the monocot-dicot split in the Results, while stating the exact opposite in the Discussion), and complete omission of statistical testing or cultivar-level reporting for the qRT-PCR experiment across five wheat cultivars (`KSU-L`, `KSU-K`, `KSU-Y`, `KSU-105`, `KSU-115`).

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES

#### STRENGTHS
- **Subgenome-Wide Compilation of Wheat *TaSUMO* Loci:** The authors compile chromosomal coordinates, CDS lengths, exon counts, and predicted physicochemical parameters (`Table 1`) for 31 *TaSUMO* candidates in hexaploid wheat (`IWGSC` Ensembl Plants).

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Direct Numerical Contradiction in Duplicated Gene Pair Counts (`Abstract` vs. `Results` and `Conclusion`):**
  - In the `Abstract` (`line 9`), the authors state: *"The **eleven pairs** of duplicated gene were identified across different wheat chromosomes. Ka/Ks ratio revealed that **8** duplicated TaSUMO genes went through **purifying purification**..."*
  - In the `Results` (`lines 83–85`) and `Conclusion` (`line 185`), the authors state: *"Through synteny analysis, we identified **eight pairs** of duplicated genes (`TaSUMO2:TaSUMO4`, `TaSUMO3:TaSUMO5`, `TaSUMO9:TaSUMO10`, `TaSUMO11:TaSUMO17`, `TaSUMO12:TaSUMO14`, `TaSUMO13:TaSUMO15`, `TaSUMO20:TaSUMO27`, and `TaSUMO26:TaSUMO31`)... The Ka/Ks values of **all the 8 gene pairs** was less than 1 (`Table S4`)."* Thus, the `11 pairs` claim in the Abstract is directly contradicted by the body text and `Table S4`.
- **Fundamental Mischaracterization of SUMO Biology (`line 30`):** In `Materials and methods` (`line 30`), the authors write: *"Each sequence has been stripped of redundancy and manually scrutinized, yielding a distinctive collection of potential **SUMO transporter proteins**."* SUMO (Small Ubiquitin-related Modifier) is a ~100-amino-acid ubiquitin-like covalent post-translational modifier conjugated to target lysines via E1/E2/E3 enzymes—it is **not** a membrane transporter protein. Calling *TaSUMO* genes "SUMO transporter proteins" suggests a copy-paste artifact from an unrelated transporter gene-family template paper.
- **Self-Contradictory Evolutionary Inference Regarding the Monocot-Dicot Split (`line 73` vs. `line 154`):**
  - In `Results` (`line 73`), the authors write: *"However, the cluster I, VIII, IX, X, XI, XII and XIII were monocot specific while the cluster II, and III were dicot specific suggesting gene amplification occurred **before** the split between monocot and dicot (`Fig. 1A` and `Table S2`)."*
  - In `Discussion` (`line 154`), they state the exact opposite (and biologically correct) interpretation: *"While cluster II and III exclusively comprised dicot species, clusters I, VIII, IX, X, XI, XII, and XIII were specific to monocots, suggesting a divergence in the evolutionary path of the SUMO gene **subsequent to** the split between monocots and dicots."* Lineage-specific clades indicate gene duplication/expansion *after* lineage divergence, not before.
- **Contradictory Motif Counts and Mis-Cited Figures (`line 99` vs. `line 156`):**
  - In `Results` (`line 99`), the authors state: *"With the exception of a few instances, the majority of TaSUMO proteins exhibited **three to six motifs**, highlighting a notable structural conservation (`Fig. S8A`)."*
  - In `Discussion` (`line 156`), they write: *"A collective count of **4 motifs** was recognized in each SUMO protein (`Fig. 8A, B`)."* Not only does the main text only have 7 figures (`Fig. 1` to `Fig. 7`, so `Fig. 8A, B` does not exist in the main text), `Fig. S8A` only searched for a maximum of 4 motifs (`Motif 1` to `Motif 4`).
- **Disconnect Between Elaborate qRT-PCR Methods (`lines 57–59`) and Virtually Non-Existent qRT-PCR Results (`lines 136–138`):**
  - In `Materials and methods` (`lines 57–59`), the authors describe growing **five distinct wheat cultivars** (`KSU-L`, `KSU-K`, `KSU-Y`, `KSU-105`, and `KSU-115`) in three replicates, subjecting them to cold ($5^\circ\text{C}$), heat ($37^\circ\text{C}$), and drought (PEG-6000) across 0, 24, 48, and 72 h, and harvesting roots, leaves, and stems.
  - Yet in `Results` (`lines 136–138`), the entire qRT-PCR experiment is summarized in two generic sentences referring to `Fig. S12` without mentioning a single cultivar name (`KSU-L`, `KSU-K`, etc.), tissue comparison, fold-change value, error bar definition, $p$-value, or statistical test (ANOVA / $t$-test).
- **Garbled Prose and Typographical Errors Throughout:** Examples include *"went through **purifying purification**"* and *"significant **conversation** in their gene structure"* (`Abstract, line 9`), *"Ka/Ks **ration**"* (`line 36`), and *"200 µl of **triazole** reagent"* (`line 59`, for TRIzol).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *Bread wheat contains 31 TaSUMO genes distributed across subgenomes A, B, and D.* `[Moderately Supported]` — Supported by BLASTP/HMMER searches against Ensembl Plants, though several candidates (`TaSUMO2` at 294 aa, `TaSUMO18` at 285 aa, `TaSUMO30` at 282 aa) are nearly triple the length of canonical ~100 aa SUMO proteins and likely represent di-/tri-SUMO concatemers or misannotated fusion genes that were not distinguished from canonical mono-SUMOs.
- **Claim 2:** *11 (or 8) duplicated TaSUMO gene pairs evolved under purifying selection and amplified before (or after) the monocot-dicot split.* `[Methodologically Flawed]` — Internally contradictory between the Abstract (`11 pairs`), Results (`8 pairs`), and Discussion (`before` vs. `subsequent to` the monocot-dicot split).
- **Claim 3:** *qRT-PCR validates stress-responsive expression of TaSUMO genes across five wheat cultivars enabling resilient wheat breeding.* `[Overstated]` — The Results section fails to report cultivar-specific data, quantitative fold changes, or any statistical hypothesis tests for the qRT-PCR experiment.

### 4. Reproducibility & Data Completeness
- **Data Availability:** Sequence IDs (`TraesCS...`) are listed in `Table 1`, and primer sequences are referred to in `Table S1`, but no raw qRT-PCR $C_t$ values or statistical analysis scripts are provided. Moreover, the promoter length parameter in `line 45` was accidentally scrubbed by automated year-redaction (`"[YEAR] bp"` instead of `1500 bp` or `2000 bp`).
</Blinded Review: TIME_ANON_0462>
