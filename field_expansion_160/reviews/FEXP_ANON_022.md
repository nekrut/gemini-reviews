# Review of FEXP_ANON_022

**Overall Score:** **5.0 / 10.0** (Mixed / Salvageable) | **Scientific Core Score:** **3.7 / 8.0**  
* **Score Breakdown:** Rigor: 1.3/3.5 | Claims: 1.1/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.3/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_022`
* **Perceived Research Domain:** Invertebrate molecular systematics, mitogenomics, and molecular evolution (Caenogastropoda: Cerithioidea).
* **Study Design:** De novo sequencing and comparative mitogenomic analysis of 6 South Korean cerithioidean gastropod species (2 Batillariidae: *Batillaria attramentaria*, *B. multiformis*; 4 Potamididae: *Cerithidea tonkiniana*, *C. rhizophorarum*, *Cerithideopsis largillierti*, *Pirenella cingulata*) integrated with 27 published cerithioidean mitogenomes and 2 outgroups ($N = 35$ taxa total).
* **Primary Methods:** Mitogenome assembly and annotation (`NOVOPlasty` v4.3.1, `MITOS`, `tRNAscan-SE`, `ARWEN`), RSCU hierarchical clustering (`CAIcal`, `pheatmap`, `pvclust`), partitioned ML and Bayesian phylogenetics (`ModelFinder` v2.2.0, `IQ-TREE`, `MrBayes` v3.2.7a), selection testing (`PAML` v4.8 `yn00` and `codeml` site/branch-site models; `HyPhy` `FUBAR`, `MEME`, `aBSREL`; `AlphaFold` structure prediction), and fossil-calibrated molecular dating (`BEAST` v2.6.0).

---

## 2. Executive Summary & Editorial Verdict

This study reports complete mitochondrial genomes for six euryhaline/intertidal gastropod species in the superfamily Cerithioidea from South Korea (deposited in GenBank under `PV619093–PV619098`), characterizes their gene organization and tRNA rearrangements, reconstructs superfamily phylogenies across 33 cerithioidean taxa using Maximum Likelihood and Bayesian Inference, tests for positive selection across the 13 mitochondrial protein-coding genes (PCGs), and estimates divergence times in BEAST v2.6.0. The authors confirm the monophyly of Cerithioidea and its division into two main clades (corroborated by shared `trnQ`/`trnR` tRNA rearrangements), note persistent ambiguity in family-level relationships depending on dataset composition (PCGs+rRNAs vs. PCGs vs. amino acids), propose `nad6` as a hotspot of episodic and pervasive positive selection within disordered C-terminal regions, and link cerithioidean divergence times to the Cretaceous Thermal Maximum (CTM, ~90 Ma) and Paleocene–Eocene Thermal Maximum (PETM, ~56 Ma).

The six newly assembled mitogenomes (`PV619093–PV619098`) and the comparative analysis of tRNA gene order rearrangements across Cerithioidea represent solid empirical contributions to caenogastropod systematics. However, the evolutionary selection and divergence-dating analyses suffer from serious methodological, mathematical, and reporting flaws. First, the `CodeML` analysis uses equal codon frequencies (`1/61`) on strongly A+T-biased ($62.3\%\text{–}66.6\%$) mitochondrial genes, misinterprets `CodeML` M8 Bayes Empirical Bayes (BEB) posterior mean $\omega > 1.0$ estimates as *"posterior probability values exceeding 1.0"* (footnote to Table 2), reports impossible probability values (`p > 1` in line 69), and lists nucleotide coordinates for "codons" within single genes in Table 2 that violate modulo-3 reading frame phase. Second, the branch-site selection analysis engages in circular double-dipping (selecting foreground branches with `aBSREL` $p < 0.05$ and re-testing them in `CodeML` without multiple-testing correction), and the text contradicts Table 2 regarding both FUBAR site counts (2 vs. 3) and Branch `#2` vs. `#1` site assignments. Third, associating BEAST node age estimates that have 35–150 Myr 95% HPD intervals with brief hyperthermal events like the ~200-kyr PETM without any formal diversification rate-shift modeling overstates the precision of saturated mitochondrial clocks. All of these analytical and textual defects can be corrected through rigorous re-analysis and editorial revision.

### Specific Assessment of Core Claims

* **Mitogenome organization of six Korean cerithioidean species and phylogenetic division of Cerithioidea into two major clades supported by shared tRNA rearrangements (`trnQ`, `trnR`):** **[Well Supported].**  
  The six mitogenome assemblies (`PV619093–PV619098`) follow standard molluscan validation criteria, and the concordance between the deep basal split in ML/BI phylogenies and the synapomorphic tRNA translocations (`trnQ` between `trnR`/`trnK` vs. `trnS2`/`nad4l`) provides strong, independent structural corroboration.

* **Codon usage (RSCU) hierarchical clustering separates freshwater and marine/brackish cerithioidean species:** **[Fragile].**  
  While the dendrogram in Figure 2 clusters species by RSCU similarity, the Figure 2 legend states *"Data are based on six Cerithioidea mitochondrial genomes"*, whereas the Results and Discussion (lines 46, 127) discuss clustering of freshwater vs. marine species and explicitly mention *Turritella sarasinorum* (which is not one of the six newly sequenced intertidal/brackish species). Furthermore, because all freshwater species in the dataset belong to one major clade (Semisulcospiridae, Pleuroceridae, Thiaridae, Hemisinidae, Paludomidae), hierarchical clustering of RSCU without phylogenetic generalized least squares (PGLS) cannot distinguish habitat-driven selection from shared phylogenetic ancestry and A+T compositional drift.

* **`nad6` is a hotspot of positive selection, particularly within C-terminal disordered regions:** **[Methodologically Flawed].**  
  The selection analysis contains multiple technical failures:
  1. In `CodeML`, the authors used equal codon frequencies (`CodonFreq = 0`; line 170) despite severe A+T bias ($62\text{–}67\%$) and strong T-skew (`AT skew = -0.22`), which is well known to induce spurious $\omega > 1$ inferences.
  2. In line 69 and Table 2, the authors report impossible statistics (`p > 1` for M1a vs. M2a and BEB) and claim in the Table 2 footnote that *"Codons with posterior probability values exceeding 1.0 in the BEB analysis under the site model (M8), which are considered unreliable estimates, were excluded"*—confusing the PAML BEB posterior mean $\hat{\omega}$ column ($>1.0$) with the posterior probability column ($\text{PP} \in [0, 1]$).
  3. The three `nad6` codons (`9236`, `9242`, `9260`) highlighted by both FUBAR and MEME lie near the **5' (N-terminal) start** of `nad6` (nucleotide positions 9,236–9,260 in `B. attramentaria`), whereas the structural narrative in Results line 111 and Figure 5 attributes adaptation to the **C-terminal** disordered region.
  4. In `nad6`, Potamididae species vary in length (`507`, `543`, and `552` bp) and share a 1 to 47 bp overlap with `cytb` on the opposite or adjacent frame (line 26, 137); local frame shifts or indel alignment errors in the overlapping/variable terminus of `nad6` readily generate false-positive `MEME`/`FUBAR`/`aBSREL` signals.

* **Divergence of major cerithioidean lineages was driven by the Cretaceous Thermal Maximum (~90 Ma) and accelerated during the Paleocene–Eocene Thermal Maximum (~56 Ma):** **[Overstated].**  
  The BEAST divergence time estimates have wide 95% HPD intervals (e.g., root divergence 351–198 Ma; Semisulcospiridae 95.2–60.1 Ma) driven by mitochondrial substitution saturation at Paleozoic/Mesozoic depths. Attributing cladogenesis to the PETM (~56 Ma, an event lasting $\sim 0.2\text{ Myr}$) when node 95% HPD intervals span 15–35 Myr—and without conducting any lineage-through-time (LTT) or birth–death shift tests—is speculative correlation.

---

## 3. Forensic Defect Inventory

### Defect 1: Misinterpretation of PAML `CodeML` Output (`PP > 1.0` and `p > 1`), Equal Codon Frequency Misspecification, and Circular Branch-Site Testing (Pillar 3 & Pillar 4)
* **Location:** Section "Adaptive evolution in mitochondrial protein-coding genes" (lines 69–109, Table 2) and Section "Selection analyses" (line 170).
* **Diagnostic Finding:**
  1. **Impossible probability values:** Line 69 reports *"not for M1a vs. M2a ( p > 1)"* and *"no individual codon met the BEB significance threshold ( p > 1)"*, while the Table 2 footnote states *"Codons with posterior probability values exceeding 1.0 in the BEB analysis under the site model (M8), which are considered unreliable estimates, were excluded"*. Neither $p$-values nor posterior probabilities can exceed $1.0$. In PAML `codeml` M8 output, each site line prints `site | amino_acid | post_prob | post_mean_w +- SE`; values $>1.0$ are the estimated $\omega$ ($d_N/d_S$) values, not posterior probabilities.
  2. **Codon frequency model misspecification:** Line 170 states that `CodeML` site models were run *"using equal codon frequencies"*. In mitogenomes with $\sim 65\%$ A+T content, assuming equal $1/61$ codon frequencies distorts transition/transversion and synonymous rate estimation. Standard practice requires `F3x4` or `F61` empirical frequencies.
  3. **Data dredging in branch-site tests:** Selecting branches with `aBSREL` $p < 0.05$ (`Branches #1–#3`) and testing those same branches as foreground hypotheses in `CodeML` branch-site Model A on the exact same dataset violates statistical independence.
* **Remediation:** Re-run `CodeML` site and branch-site models using `CodonFreq = 2` (`F3x4`), extract the actual BEB posterior probabilities ($\text{PP} \in [0, 1]$) rather than the post-mean $\omega$ column for Model M8, correct the `p > 1` typos, and apply a Holm–Bonferroni correction across tested branches.

### Defect 2: Frame-Inconsistent Codon Coordinates and Text-vs.-Table Contradictions in Table 2 (Pillar 7)
* **Location:** Results lines 69 and 109, Table 2 (lines 72–108).
* **Diagnostic Finding:**
  1. **Modulo-3 phase impossibility in Table 2:** The Table 2 footnote states that *"Codon positions refer to the nucleotide position (start codon numbers) in the B. attramentaria mitochondrial genome assembled in this study (PV619093)."* Within any single intronless mitochondrial gene, the first nucleotide of every codon must have the exact same remainder modulo 3 ($x \pmod 3$). Yet in Table 2:
     - Within `nad4`, listed start positions include `2871` ($\equiv 0 \pmod 3$), `3528` ($\equiv 0 \pmod 3$), and `3671` ($\equiv 2 \pmod 3$).
     - Within `nad6`, listed start positions include `9236` ($\equiv 2 \pmod 3$), `9402` ($\equiv 0 \pmod 3$), and `9437` ($\equiv 2 \pmod 3$).
     - Within `nad1`, listed start positions include `10,013` ($\equiv 2 \pmod 3$), `10,044` ($\equiv 0 \pmod 3$), and `10,503` ($\equiv 0 \pmod 3$).
     - Within `nad2`, listed start positions include `13,662` ($\equiv 0 \pmod 3$), `13,858` ($\equiv 1 \pmod 3$), and `14,410` ($\equiv 0 \pmod 3$).
     It is impossible for codons within the same intronless reading frame to start at different phases modulo 3.
  2. **Contradiction in FUBAR count (2 vs. 3):** Line 69 states *"although two codons in nad6 suggested possible positive selection [in FUBAR]. MEME identified six codons under episodic positive selection, including three also highlighted by FUBAR (Table 2)."* Table 2 lists **three** FUBAR codons in `nad6` (`9236`, `9242`, `9260`).
  3. **Misaligned columns and contradicting branch counts in Table 2:** Line 109 states that *"Branch #2... exhibited one positively selected codon in cytb"*, whereas in Table 2 the `cytb` sites (`8146`, `9058`) are placed under `Branch #1 (PP)` and the `Branch #2 (PP)` column is completely blank across all genes.
* **Remediation:** Report standard 1-indexed **amino acid / codon positions** within each individual gene (e.g., codon $1\text{ to }181$ of `ND6`) alongside the verified nucleotide triplet coordinates in `PV619093`, reconcile the 2 vs. 3 FUBAR count in line 69, and fix the column alignment for Branches `#1`, `#2`, and `#3` in Table 2.

### Defect 3: Arithmetic and Reporting Errors in Table 1, Figure 2, and Geological Time Intervals (Pillar 6 & Pillar 7)
* **Location:** Results line 26, Table 1 (lines 36–45), Figure 2 caption (line 49), Results line 119, Discussion line 139.
* **Diagnostic Finding:**
  1. **Base composition sum $= 103.00\%$ in Table 1:** In Table 1 (line 44), the PCG nucleotide composition of *Ce. largillierti* is reported as `A + T (%) = 66.61` and `G + C (%) = 36.39`, which sums to **$103.00\%$** instead of $100.00\%$ (likely `63.61%` misprinted as `66.61%`, or `33.39%` misprinted as `36.39%`).
  2. **Genome length discrepancy for *Pirenella cingulata*:** Reported as **`15,632 bp`** in Results text (line 26) and Figure 1, but **`15,629 bp`** in Table 1 (line 45).
  3. **Figure 2 sample size contradiction:** The Figure 2 caption states *"Data are based on six Cerithioidea mitochondrial genomes"*, but the figure and text (lines 46, 127) cluster freshwater vs. marine/brackish species across the 33-species dataset (including *T. sarasinorum*).
  4. **Divergence age contradiction and geological period error:** Results line 119 reports the root split as `346.23–194.88 Ma`, whereas Discussion line 139 reports the origin of Cerithioidea as `274.29 million years ago (351.07–197.51 Ma)` and describes `351–198 Ma` as *"the Cambrian and Early Jurassic intervals"*. In the International Chronostratigraphic Chart, $351\text{ Ma}$ is in the **Carboniferous (Mississippian)**, nearly $135\text{ Myr}$ after the end of the Cambrian ($485.4\text{ Ma}$).
* **Remediation:** Fix the `A+T%` / `G+C%` typo for *Ce. largillierti* PCGs and the genome length of *P. cingulata* in Table 1, update the Figure 2 caption to state that RSCU clustering was performed across all 33 cerithioidean species, reconcile the 95% HPD numbers between lines 119 and 139, and replace *"Cambrian"* with *"Carboniferous"* in line 139.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.3** | **3.5** | Phylogenetics (`IQ-TREE`/`MrBayes` with partitioned `ModelFinder`) is sound, but selection analyses are compromised by equal codon frequencies (`1/61`) on A+T-rich mitogenomes, misreading PAML BEB $\hat{\omega} > 1$ as $\text{PP} > 1.0$, reporting `p > 1`, and circular `aBSREL` $\to$ `CodeML` branch selection. |
| **2. Claim-to-Evidence Alignment** | **1.1** | **2.5** | Core phylogenetic and tRNA rearrangement claims are well grounded, but claims of C-terminal disordered-region adaptation in `ND6` (when shared FUBAR/MEME sites are N-terminal), habitat-driven RSCU clustering without phylogenetic control, and PETM/CTM-driven diversification overreach the evidence. |
| **3. Data Integrity & Biological Plausibility** | **1.3** | **2.0** | The six new mitogenome assemblies (`PV619093–PV619098`) and tRNA structural annotations are biologically solid, but undermined by frame-inconsistent codon coordinates in Table 2 and misidentifying 351 Ma as the Cambrian Period. |
| **4. Reproducibility & Data Integrity** | **1.3** | **2.0** | All six newly sequenced mitogenomes are deposited in GenBank (`PV619093–PV619098`), but the manuscript contains multiple numerical inconsistencies (`103.00%` base sum and `15,632` vs. `15,629` bp in Table 1; 2 vs. 3 FUBAR codons; misaligned `Branch #2` column in Table 2; `6` vs. `33` species in Fig. 2 caption). |
| **Total Composite Score** | **5.0** | **10.0** | **Mixed / Salvageable** (Scientific Core Score: **3.7 / 8.0**) |
