# Review of ANON_102

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **3.2 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 0.7/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates whether the serotonin–norepinephrine reuptake inhibitor (SNRI) Duloxetine directly targets signal transducer and activator of transcription 3 (STAT3/pSTAT3) to mediate its analgesic effects. The authors combine AutoDock 4.2 molecular docking, 10 ns GROMACS molecular dynamics (MD) simulations, and MM-PBSA free-energy calculations on STAT3 (PDB: 6NJS) and pSTAT3 (PDB: 6QHD) with *in vitro* assays in IL-6–stimulated C2C12 murine myoblasts (MTT viability, Western blotting of STAT3 and pSTAT3, and bulk RNA-seq analyzed via DESeq2, `gffcompare`, and rMATS). They report that Duloxetine docks to pSTAT3 ($-5.83\text{ kcal/mol}$; MM-PBSA $\Delta G = -15.17\text{ kJ/mol}$), reduces IL-6–induced STAT3 and pSTAT3 protein expression at 6.4 and $12.8\ \mu\text{M}$, enriches mitochondrial and synaptic transcriptomic pathways, and alters alternative splicing of novel class "j" *Stat3* isoforms. No public repository accession numbers are provided for the raw RNA-seq reads or MD trajectories.

While exploring off-target immunomodulatory mechanisms of SNRIs is of pharmacological interest, the study's central conclusions are undermined by severe methodological, structural, and statistical flaws. First, Ruxolitinib—an ATP-competitive JAK1/JAK2 kinase inhibitor that inhibits STAT3 phosphorylation upstream rather than by binding STAT3 directly—is used throughout the *in silico* pipeline as a positive-control reference ligand for direct STAT3/pSTAT3 binding. Second, docking to pSTAT3 (6QHD) was performed in the coiled-coil domain (residues 176–207), whereas docking to unphosphorylated STAT3 (6NJS) was performed in the SH2 domain (residues 591–639), confounding phosphorylation state with completely different protein domains. Third, no direct biophysical binding assay (e.g., SPR, ITC, or thermal shift) was conducted, and all cellular experiments were performed in murine skeletal myoblasts (C2C12) rather than neuronal or glial cells. Resolving these issues requires redocking to matched structural pockets with a validated direct STAT3 SH2 inhibitor, extending MD simulations to standard timescales ($\ge 100\text{ ns}$ across replicates), re-analyzing the Western blot and RNA-seq datasets with valid statistical thresholds, and reframing claims to match indirect cellular observations.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Duloxetine directly binds pSTAT3 with higher affinity than STAT3 and more favorable MM-PBSA free energy than Ruxolitinib ($\Delta G = -15.17$ vs. $-12.98\text{ kJ/mol}$): [Methodologically Flawed].**  
  In Table 1 and Sections 2.1–2.2, pSTAT3 (PDB: 6QHD) was docked at the coiled-coil domain (TYR176, LEU179, LYS180, MET200, GLU204), whereas unphosphorylated STAT3 (PDB: 6NJS) was docked at the SH2 domain (LYS591, ARG609, SER636, GLU638). Comparing MM-PBSA energies across two distinct structural domains cannot establish selectivity for phosphorylated over unphosphorylated STAT3. Furthermore, Ruxolitinib is a selective JAK1/2 kinase inhibitor, not a direct STAT3 ligand, making it an invalid structural benchmark. In Section 2.4 (line 115), the text misreports Duloxetine's electrostatic energy $\Delta E_{\text{EL}}$ as $-19.16\text{ kJ/mol}$ (which is actually $\Delta G_{\text{GAS}}$ in Table 3; $\Delta E_{\text{EL}}$ is $+1.14\text{ kJ/mol}$, unfavorable), and a single 10 ns MD trajectory without conformational entropy estimation cannot resolve a $2.19\text{ kJ/mol}$ ($0.52\text{ kcal/mol}$) difference.

* **Duloxetine dose-dependently suppresses IL-6–induced pSTAT3 and total STAT3 protein levels in C2C12 cells ($p < 0.0001$): [Fragile].**  
  Western blots in Figure 8 show reduced band intensities for both pSTAT3 and total STAT3 after a 40-minute treatment (Section 4.4.3), while RNA-seq at 24 hours shows unchanged *Stat3* mRNA levels (Section 2.6). Because total STAT3 protein drops steeply alongside pSTAT3, the authors have not calculated the pSTAT3/total STAT3 ratio to demonstrate specific inhibition of phosphorylation rather than rapid protein degradation or precipitation. Moreover, pairwise Student's $t$-tests were applied across multi-group dose–response comparisons without ANOVA or multiple-testing correction, and sample size ($n$) is omitted from Figure 8.

* **Duloxetine and Ruxolitinib induce distinct transcriptomic programs, with Duloxetine enriching mitochondrial, oxidative phosphorylation, and synaptic pathways: [Fragile].**  
  Section 4.4.4 (line 288) states that genes with "$-\log_{10}(\text{p-value}) < 0.05$ and a $\log_2\text{ fold change} \ge |1|$ were considered significantly differentially expressed." Mathematically, $-\log_{10}(p) < 0.05$ selects genes with $p > 0.891$; even if intended as $p < 0.05$ ($-\log_{10}(p) > 1.30$), filtering DESeq2 output by unadjusted $p$-values without Benjamini–Hochberg false discovery rate (FDR) correction inflates false positives in genome-wide GO/KEGG enrichment. In addition, attributing "synaptic regulatory mechanisms" and neuroenergetic remodeling to an undifferentiated mouse skeletal muscle myoblast line (C2C12) overstates its neurobiological relevance.

* **Duloxetine and Ruxolitinib dose-dependently modulate alternative splicing and novel class "j" isoforms of *Stat3*: [Overstated].**  
  The Methods reveal an annotation assembly mismatch: Section 4.4.4 aligns reads to mouse genome build `mm39` (RefSeq), whereas Section 4.4.5 runs rMATS v4.3.0 using an `Ensembl GRCm38/mm10` GTF annotation (and Table 4 lists `mm10` coordinates `chr11:100777632–100830447`). Neither the number of biological replicates per condition, junction read coverage, nor rMATS FDR values are reported. In Section 2.8 (line 182), the text claims that Ruxolitinib at $12.8\ \mu\text{M}$ "reduced inclusion to 0.94" from a control IncLevel of 0.90 (and Figure 6D reports $0.85 \to 0.94$), which is an increase rather than a reduction.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Correct Structural Docking Controls and Domain Matching
* **WHY:** Comparing docking poses in the coiled-coil domain of 6QHD against the SH2 domain of 6NJS confounds phosphorylation state with domain identity, and Ruxolitinib is a JAK1/2 kinase inhibitor rather than a direct STAT3 binder.
* **WHAT:** Redock Duloxetine against the same canonical binding pocket (the SH2 domain around ARG609/LYS591, or a validated allosteric pocket) in both STAT3 and pSTAT3, using a known direct STAT3 SH2 inhibitor (such as Stattic, S3I-201, or C188-9) as the positive control.
* **HOW:** Define identical grid box coordinates centered on the SH2 phosphotyrosine-binding pocket across the aligned crystal structures in AutoDock 4.2, run triplicate MD trajectories of at least 100 ns per complex in GROMACS, and report mean $\pm$ SD MM-PBSA energies across independent trajectories.

#### 2. Normalize pSTAT3 to Total STAT3 and Apply Multi-Group Statistical Testing
* **WHY:** Both total STAT3 and pSTAT3 decrease in Figure 8 after 40 minutes of treatment; without normalizing pSTAT3 to total STAT3, one cannot distinguish specific inhibition of Tyr705 phosphorylation from general protein loss. Pairwise $t$-tests across six conditions also inflate Type I error.
* **WHAT:** Report the densitometric ratio of $\text{pSTAT3}/\text{total STAT3}$ alongside $\text{pSTAT3}/\text{loading control}$ and $\text{STAT3}/\text{loading control}$, state the exact number of independent biological replicates ($n$), and re-analyze using one-way ANOVA with Dunnett's or Tukey's post-hoc test.
* **HOW:** Re-quantify the raw Western blot membranes from the Supplementary File, compute per-lane $\text{pSTAT3}/\text{STAT3}$ ratios, and update Figure 8B–C and Section 2.10 with ANOVA $F$-statistics and multiplicity-adjusted $p$-values.

#### 3. Fix Differential Expression Filtering and Genome Build Consistency in RNA-Seq
* **WHY:** The stated threshold $-\log_{10}(p) < 0.05$ is mathematically inverted ($p > 0.89$), unadjusted $p$-values are inappropriate for transcriptome-wide testing, and mixing `mm39` BAM alignments (Section 4.4.4) with `mm10` GTF coordinates (Section 4.4.5) corrupts splice-junction quantification.
* **WHAT:** Ensure a single consistent genome assembly (`mm10` or `mm39`) is used across HISAT2, `featureCounts`, `gffcompare`, and rMATS, filter DESeq2 results at Benjamini–Hochberg $\text{FDR} < 0.05$ and $|\log_2\text{FC}| \ge 1$, and report rMATS junction counts and FDR values for all claimed *Stat3* splicing events.
* **HOW:** Re-run DESeq2 and rMATS on the aligned BAM files with the matched reference GTF, state the replicate count per group in Section 4.4.4, and provide a table of rMATS inclusion levels, junction read counts, and FDR values for the events in Figure 6.

#### 4. Temper Direct-Binding and Neurobiological Claims
* **WHY:** Neither direct physical binding of Duloxetine to STAT3 nor activity in neural or glial cells was experimentally tested.
* **WHAT:** Reframe the Title, Abstract, and Discussion to state that Duloxetine *attenuates IL-6–induced STAT3 signaling in C2C12 myoblasts* and exhibits *putative in silico affinity for STAT3*, rather than claiming established direct target engagement or neuroinflammatory mechanisms.
* **HOW:** Revise Abstract lines 8–9 ("directly targeting phosphorylated STAT3... establish Duloxetine as a dual-action therapeutic") and Section 5 Conclusions to explicitly note that direct target engagement requires biophysical confirmation (e.g., SPR/CETSA) and validation in microglial or neuronal models.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Internal contradictions between tables and text, dosage typos, and missing data accessions impede verification.
* **WHAT & HOW:**
  * **Section 2.4 (line 115) & Table 3:** Fix the misquoted $\Delta E_{\text{EL}}$ value for pSTAT3–Duloxetine (text states $-19.16\text{ kJ/mol}$, which is $\Delta G_{\text{GAS}}$; Table 3 gives $\Delta E_{\text{EL}} = +1.14\text{ kJ/mol}$).
  * **Section 2.8 (line 182) & Figure 6D:** Reconcile the control IncLevel (0.90 in text vs. 0.85 in caption) and correct the statement that changing from $0.90$ (or $0.85$) to $0.94$ represents "reduced inclusion" / "suppression of exon incorporation."
  * **Section 4.4.3 (line 279):** Correct the Duloxetine/Ruxolitinib concentration typo from "$12.6\ \mu\text{M}$" to "$12.8\ \mu\text{M}$".
  * **Data Availability:** Deposit the raw FASTQ files and processed count matrices in NCBI GEO/SRA and provide the accession number.
