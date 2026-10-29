# Review of FEXP_ANON_027

**Overall Score:** **2.8 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.9 / 8.0**  
* **Score Breakdown:** Rigor: 0.6/3.5 | Claims: 0.6/2.5 | Biology: 0.7/2.0 | Reproducibility: 0.9/2.0

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_027`
* **Perceived Research Domain:** Plant plastome genomics and synonymous codon usage bias analysis (*Bupleurum falcatum* L., family Apiaceae).
* **Study Design:** Reference-guided assembly and annotation of a single chloroplast genome of *Bupleurum falcatum* (`MT797174`), Neighbor-Joining phylogenetic placement in Apiaceae, and descriptive synonymous codon usage analysis across plastid protein-coding sequences.
* **Primary Methods:** Reference-guided plastome assembly (`MITObim` v1.8 using *B. chinense* `MN337347`), annotation (`CPGAVAS2`, `OGDRAW` v1.3.1), Neighbor-Joining phylogenetics (`MEGA X`), codon usage parameter calculation (`CodonW`, `EMBOSS cusp`, custom Python script), and Spearman correlation / chi-square tests (`SPSS` 20.0).

---

## 2. Executive Summary & Editorial Verdict

This manuscript reports the complete chloroplast genome assembly of the medicinal plant *Bupleurum falcatum* (`MT797174`, reported length 155,851 bp, 132 annotated genes including 80 protein-coding genes [PCGs]), places it within Apiaceae via a Neighbor-Joining tree of 77 PCGs, and evaluates synonymous codon usage bias (neutrality plot, ENC-plot, PR2-bias plot, Spearman rank correlations, and optimal codon identification) across 78 coding sequences. The plastome sequence is deposited in GenBank under accession `MT797174`.

Although the chloroplast genome sequence (`MT797174`) itself is deposited in GenBank, the manuscript's quantitative, statistical, and biological analyses are pervasive failures that invalidate its core codon-usage conclusions. Specifically: (1) the reported lengths of the four quadripartite chloroplast regions ($\text{LSC} = 85,763\text{ bp}$, $\text{SSC} = 17,528\text{ bp}$, $2 \times \text{IR} = 2 \times 26,305\text{ bp}$) sum to $155,901\text{ bp}$, contradicting the reported total genome length of $155,851\text{ bp}$ by $50\text{ bp}$; (2) the authors claim to have filtered the 80 annotated PCGs to retain only genes $\ge 100$ codons ($\ge 300\text{ bp}$) and retained 78 of 80 genes, which is biologically impossible in an angiosperm plastome where $\ge 20$ canonical photosynthetic and ribosomal genes (`petG`, `petL`, `petN`, `psbE–N`, `rpl32–36`, etc.) are shorter than 100 codons; (3) Table 1 marks tiny correlation coefficients (`0.05*`, `0.075*`, `0.142**`) as statistically significant ($P < 0.05$ and $P < 0.01$) for $N = 78$ genes (where $P < 0.05$ requires $|r| \ge 0.223$), while leaving larger correlations (`0.276`) unmarked and reporting a near-zero correlation (`0.02`) between `GC3` and `GCall`; and (4) Table 2 ("Optimal codons") is truncated halfway through the genetic code (omitting 7 entire amino acids and several synonymous codons), contains only 3 sequences in the `High` and `Low` groups with tiny total codon counts (e.g., 3 total Proline codons in `High`), and falsely claims $P < 0.01$ chi-square significance for three codons (`UCG*`, `CCU*`, `ACU*`) none of which reach $P < 0.01$ under valid contingency testing.

### Specific Assessment of Core Claims

* **Complete chloroplast genome assembly of *B. falcatum* (`MT797174`) is 155,851 bp with LSC (85,763 bp), SSC (17,528 bp), and paired IRs (26,305 bp each), and places *B. falcatum* within monophyletic *Bupleurum*:** **[Fragile].**  
  While the NJ placement within *Bupleurum* is expected given reference-guided assembly against *B. chinense* (`MN337347`), the reported component lengths in Section 3.1 ($85,763 + 17,528 + 2 \times 26,305 = 155,901\text{ bp}$) do not add up to the reported genome length ($155,851\text{ bp}$). Furthermore, Section 3.1 (line 71) contradicts Figure 2 on the number of analyzed species (`21` in text vs. `20` in Fig. 2 caption) and misidentifies the family as *"Araliaceae"* in line 71 while classifying *Atriplex undulata* (Amaranthaceae) as Apiaceae/Araliaceae in line 156.

* **Filtering the 80 plastid protein-coding genes for length $\ge 100$ codons ($\ge 300\text{ bp}$) and valid start/stop codons yielded 78 genes for codon usage analysis:** **[Methodologically Flawed].**  
  In all standard angiosperm chloroplast genomes (including Apiaceae), at least 20 of the ~80 protein-coding genes encode small subunits of Photosystem I/II, cytochrome $b_6f$, and the ribosome that are 29 to 95 codons long (e.g., `petN` is 29 codons, `psbM` is 34 codons, `psbI` is 36 codons, `rpl36` is 37 codons, `petL` is 31 codons). Retaining 78 out of 80 PCGs after applying a $\ge 100$-codon filter is biologically impossible and indicates that the length filter described in line 33 was never actually applied.

* **Natural selection, mutation pressure, and compositional constraints shape *B. falcatum* codon usage as demonstrated by Spearman correlations (Table 1), neutrality, ENC, and PR2 plots:** **[Methodologically Flawed].**  
  The correlation matrix in Table 1 is statistically invalid: for $N = 78$ genes ($df = 76$), a two-tailed Spearman correlation requires $|r| \ge 0.223$ for $P < 0.05$ and $|r| \ge 0.290$ for $P < 0.01$. Yet Table 1 flags `r = 0.05*` (`GC12` vs `CAI`) and `r = 0.075*` (`GCall` vs `ENC`) at $P < 0.05$, and `r = 0.142**` (`GC12` vs `Axis1`) at $P < 0.01$, while leaving `r = 0.276` (`GC3` vs `Axis1`) unflagged. Furthermore, Table 1 reports `r = 0.001` between `GC12` and `GC3` (whereas line 84 reports $R^2 = 0.0015$, which corresponds to $|r| = \sqrt{0.0015} = 0.039$, not $0.001$).

* **Three optimal codons (`UCG`, `CCU`, `ACU`) are used significantly more frequently in highly expressed genes ($P < 0.01$, Table 2):** **[Methodologically Flawed].**  
  Table 2 is severely defective:
  1. **Unstated grouping and tiny sample counts:** The manuscript never defines how `High` and `Low` expression groups were selected. Adding the stop codon counts (`TER`: `UAA`, `UAG`, `UGA`) in Table 2 reveals that `High` contains only $0 + 1 + 2 = 3$ genes and `Low` contains only $1 + 2 + 0 = 3$ genes, with only **81 total codons** across all listed amino acids in `High` (e.g., only 3 Proline codons and 3 Methionine codons in total!).
  2. **Invalid chi-square significance ($P < 0.01$):** For `CCU*` (Proline), the observed counts are `3 CCU / 0 other Pro` in `High` vs. `1 CCU / 3 other Pro` in `Low` (Fisher's exact $p = 0.143$; $\chi^2 = 3.67, p = 0.055$). For `UCG*` (Serine), counts are `3 UCG / 3 other Ser` in `High` vs. `0 UCG / 11 other Ser` in `Low` (Fisher's exact $p = 0.029$). For `ACU*` (Threonine), counts are `7 ACU / 2 other Thr` in `High` vs. `6 ACU / 12 other Thr` in `Low` (Fisher's exact $p = 0.046$; $\chi^2 p = 0.029$). None of the three codons achieves $P < 0.01$.
  3. **Truncated table:** Table 2 omits 7 of the 20 amino acids (`Gln, Asn, Lys, Asp, Glu, Arg, Gly`) as well as `CAC` (His) and `AGU/AGC` (Ser).

---

## 3. Forensic Defect Inventory

### Defect 1: Truncated Table 2, Implausible Codon Counts, and False $P < 0.01$ Chi-Square Claims for Optimal Codons (Pillar 3, Pillar 4 & Pillar 7)
* **Location:** Section "Identification of optimal codons" (line 122) and Table 2 (lines 125–149).
* **Diagnostic Finding:**
  1. Table 2 stops abruptly after `His (CAU)`, omitting `CAC`, `AGU`, `AGC`, and all codons for `Gln`, `Asn`, `Lys`, `Asp`, `Glu`, `Arg`, and `Gly`.
  2. The parenthetical codon counts `(N)` in Table 2 sum to only 81 amino acid codons and 3 stop codons in the entire `High` group (impossible if `High` comprises even a single gene $\ge 100$ codons, let alone 5–10% of 78 genes).
  3. None of the three asterisked codons (`UCG*`, `CCU*`, `ACU*`) reach $P < 0.01$ under a chi-square or Fisher's exact test on the reported raw counts (`CCU`: $p = 0.143$; `UCG`: $p = 0.029$; `ACU`: $p = 0.046$).
* **Remediation:** Define the exact criterion used to partition genes into `High` and `Low` expression groups (e.g., top/bottom 10% of ENC or CAI, $n = 8$ genes each), recompute total codon counts across all complete CDSs in each group, include all 20 amino acids (61 sense codons) in Table 2, and compute valid $2 \times 2$ contingency tests with multiple-testing correction.

### Defect 2: Statistically Impossible Correlation Significance Flags in Table 1 (Pillar 4 & Pillar 7)
* **Location:** Section "Statistical analysis" (line 58), Section "Nucleotide composition" (line 84), and Table 1 (lines 111–118).
* **Diagnostic Finding:** In Table 1 ($N = 78$ genes), correlations of `0.05*` and `0.075*` are marked significant at $P < 0.05$ (actual two-tailed $p = 0.66$ and $p = 0.51$), and `0.142**` is marked significant at $P < 0.01$ (actual $p = 0.21$), whereas `0.276` (`GC3` vs `Axis1`, actual $p = 0.014$) has no asterisk. Moreover, `GC3` vs `GCall` is reported as `0.02`, and all entries in Table 1 are positive between `0.001` and `0.276`, suggesting that $R^2$ values, $p$-values, or corrupted numbers were pasted into Table 1 in place of Spearman's $r_s$.
* **Remediation:** Recompute the Spearman rank correlation matrix ($r_s$) and exact two-tailed $p$-values across the verified plastid CDS set and replace Table 1 with accurate signed correlation coefficients.

### Defect 3: Chloroplast Genome Length Arithmetic Discrepancy and Impossible $\ge 100$-Codon Gene Count (Pillar 6 & Pillar 7)
* **Location:** Abstract (lines 7, 9), Section "DNA sequencing, genome assembly and annotation" (line 33), Section "Chloroplast genome structure" (lines 66, 71), Discussion (line 156).
* **Diagnostic Finding:**
  1. **Genome length sum error:** Line 66 states that the genome is $155,851\text{ bp}$, composed of $\text{LSC} = 85,763\text{ bp}$, $\text{SSC} = 17,528\text{ bp}$, and two IRs of $26,305\text{ bp}$ each. However, $85,763 + 17,528 + 2(26,305) = 155,901\text{ bp} \neq 155,851\text{ bp}$ (a 50 bp discrepancy).
  2. **Impossible filtered CDS count (`78` of `80` PCGs $\ge 100$ codons):** Line 33 states that out of 80 PCGs, filtering for length $\ge 100$ codons left 78 genes. In any Apiaceae plastome, $\sim 20\text{–}25$ PCGs are $<100$ codons long, leaving only $\sim 52\text{–}56$ genes $\ge 100$ codons.
  3. **Additional factual and editorial contradictions:** DNA input is stated as `2 μg` in Abstract line 7 vs. `5 μg` in Methods line 33; species count in the NJ tree is `21` in line 71 vs. `20` in the Figure 2 caption; line 71 refers to *B. falcatum* as significant for *"Araliaceae species conservation"* instead of Apiaceae; line 156 lists *Atriplex undulata* (Amaranthaceae) as a member of Apiaceae/Araliaceae; and Figure 5 is mislabeled *"Neutrality plot (ENC vs GC3)"* instead of *"ENC-plot"*.
* **Remediation:** Verify the exact coordinates and lengths of LSC, SSC, IRa, and IRb in GenBank record `MT797174` so that $\text{LSC} + \text{SSC} + 2\text{IR}$ equals the total genome length, apply the $\ge 100$-codon filter properly (which will retain $\sim 52\text{–}55$ non-redundant CDSs), and fix all DNA mass, species count, family name, and figure caption errors.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Diagnostic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **0.6** | **3.5** | Pervasive statistical failures: Table 1 flags $r = 0.05$ and $0.075$ as $P < 0.05$ for $N=78$; Table 2 claims $P < 0.01$ chi-square significance on counts of 3 vs. 1 (`p=0.14`) and omits 7 amino acids; the stated $\ge 100$-codon filter was not actually applied. |
| **2. Claim-to-Evidence Alignment** | **0.6** | **2.5** | Claims regarding optimal codons (`UCG`, `CCU`, `ACU`), parameter correlations, and translational selection rest on corrupted or truncated tables. |
| **3. Data Integrity & Biological Plausibility** | **0.7** | **2.0** | Plastome regions ($\text{LSC}+\text{SSC}+2\text{IR} = 155,901\text{ bp}$) do not sum to the reported genome length ($155,851\text{ bp}$); claiming 78 of 80 plastid PCGs are $\ge 100$ codons violates known angiosperm plastome gene lengths; *Atriplex undulata* is misclassified as Apiaceae/Araliaceae. |
| **4. Reproducibility & Data Integrity** | **0.9** | **2.0** | Chloroplast genome is deposited in GenBank (`MT797174`) with voucher specimen `CHAIH-19-0620`, but Table 2 is truncated mid-table, Table 1 values are corrupted, and text contains multiple numerical contradictions (`2 μg` vs. `5 μg`, `21` vs. `20` species). |
| **Total Composite Score** | **2.8** | **10.0** | **Fundamentally Invalid** (Scientific Core Score: **1.9 / 8.0**) |
