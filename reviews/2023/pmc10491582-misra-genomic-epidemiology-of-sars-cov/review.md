# Review of PMC10491582 (PMID:37684328)

**Manuscript Title:** Genomic epidemiology of SARS-CoV-2 from Uttar Pradesh, India  
**Authors:** Misra G, Manzoor A, Chopra M, Upadhyay A, Katiyar A, Bhushan B, Anvikar A.  
**Journal / Preprint:** *Sci Rep* (2023; `PMC10491582` / `PMID:37684328` / `10.1038/s41598-023-42065-6`)  
**Calibration Study Cohort:** Cohort C — Wild Literature Sample (`C31` | Double-Blinded as `ANON_147`)  
**Overall Score:** **3.8 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 0.9/3.5 | Claims: 1.0/2.5 | Biology: 1.0/2.0 | Reproducibility: 0.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript reports targeted amplicon whole-genome sequencing (`QIAseq DIRECT SARS-CoV-2` on an Illumina HiSeqX, 150 bp paired-end reads) of 99 RT-PCR-positive SARS-CoV-2 clinical specimens ($C_t < 30$, selected from 3,485 positive samples out of 20,381 swabs tested between March 2021 and January 2022) collected in Western Uttar Pradesh, India. Using `Pangolin` (v4.1.3), `Nextclade` (v2.9.1), `BWA-MEM`/`GATK HaplotypeCaller`, and `MEGA11` (`GTR+G+I`, 1,000 bootstraps), the authors classify the 99 regional sequences alongside 171 GISAID reference sequences from Eastern Uttar Pradesh, Maharashtra, and Kerala (total $N = 270$) into Nextclade/GISAID clades and Pango lineages. The 99 sequenced specimens consist primarily of Omicron `BA.2`-like (75/99, 75.7%) and Delta `B.1.617.2` / `AY.*` (21/99, 21.2%) lineages. Consensus sequences are deposited in NCBI GenBank/BioProject under PRJNA976493 (SAMN35370730–SAMN35370828).

While regional genomic surveillance from densely populated areas of northern India adds useful sequence records to public repositories, the manuscript is undermined by pervasive numerical contradictions between the Abstract, Results, and Figures, basic factual errors regarding SARS-CoV-2 virology and epidemic history, an inappropriate variant-calling pipeline (`GATK HaplotypeCaller` diploid caller applied to haploid viral amplicon data without primer trimming), and unsubstantiated evolutionary and clinical claims. Specifically: (1) the Abstract reports lineage proportions (`55.55%` BA.2-like and `45.5%` B.1.617.2, which sum to `101.05%`) that completely contradict the Results section (`75.7%` BA.2-like and `21.2%` Delta; lines 44 and 64–73) because the authors confused their 99 sequenced samples with the 270-sequence multi-state GISAID tree (`151/270 = 55.9%` GRA, `113/270 = 41.9%` GK); (2) claims of "convergent evolution", "fourth and fifth waves in India", and "vaccine-breakthrough immune escape in patients who received booster doses" are asserted without any phylogenetic homoplasy test, epidemic wave timeline, or patient vaccination metadata; and (3) `QIAseq` primer sequences were not trimmed after alignment (`Cutadapt` only trims adapter ends on unmapped FASTQ reads), risking reference-primer masking at amplicon boundaries. All quantitative tables, text percentages, and bioinformatic variant calls require thorough correction.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Omicron (BA.2-like) and Delta (B.1.617.2) were the predominant circulating lineages among the 99 sequenced specimens from Western Uttar Pradesh between March 2021 and January 2022: [Moderately Supported].**  
  The `Pangolin` and `Nextclade` assignments confirm that the 99 samples fall predominantly into Omicron BA.2 (75 samples) and Delta B.1.617.2/AY.* (21 samples). However, the manuscript gives two mutually contradictory sets of percentages: the Abstract (line 8) claims `"BA-2-like (55.55%) followed by Delta lineage-B.1.617.2 (45.5%)"` (which impossibly sums to $101.05\%$), whereas the Results (line 44) and Figures 2–5 report `75.7%` (75/99) Omicron `21L`/`BA.2` and `21.2%` (21/99) Delta (`21A` 11.1% + `21J` 10.1%). Furthermore, no temporal breakdown by collection month is provided, so pooling samples across an 11-month window (March 2021–January 2022) merely reflects how many swabs were happens-to-be selected from the January 2022 Omicron wave versus the April–May 2021 Delta wave.

* **Phylogenetic diversification and shared substitutions at S:T19I/R, S:E484A/Q, and S:P681R/H demonstrate convergent evolution during the fourth and fifth waves in India: [Overstated].**  
  First, the manuscript performs no ancestral state reconstruction, $dN/dS$ selection analysis, or phylogenetic homoplasy test; it simply lists lineage-defining mutations present in standard Delta (`T19R`, `P681R`), Kappa (`E484Q`), and Omicron BA.2 (`T19I`, `E484A`, `P681H`) reference clades. Second, the sampling window ended in January 2022 (the initial Omicron BA.1/BA.2 third wave in India); India had not experienced "fourth and fifth waves" during March 2021–January 2022.

* **Most sequenced patients had received booster doses of the vaccine and experienced breakthrough infections driven by immune-escape mutations: [Unsupported / Overstated].**  
  In the Discussion (line 105), the authors assert: `"Patient samples were collected from March 2021 to January 2022 in which most of the patients had received booster doses of the vaccine and were still infected by the virus. This indicated that there was an immunity escape observed in these patients."` No patient clinical or vaccination records are presented anywhere in the Results or Methods, and in India, COVID-19 precautionary/booster doses only began rolling out on January 10, 2022 ( initially restricted to healthcare workers and seniors $\ge 60$ years with comorbidities), making it impossible for "most" patients sampled between March 2021 and January 2022 to have received booster doses.

* **Isolate `OP787530.1` descends directly from the original Wuhan strain with four unique mutations attributable to undisclosed travel history: [Fragile].**  
  In the Results (line 84) and Discussion (line 101), isolate `OP787530.1` is assigned to Nextstrain clade `20A` / Pango lineage `B.1.36` carrying `ORF3a:Q57H` and `N:S194L`. `B.1.36` (`20A` with `D614G`, `Q57H`, `S194L`) was one of the most common endemic lineages circulating across India throughout 2020 and early 2021, not a direct unmutated import from Wuhan (`NC_045512.2` is clade `19A` and lacks `D614G`, `Q57H`, and `S194L`).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Reconcile Contradictory Clade/Lineage Percentages and Mutation Counts Across the Text and Figures
* **WHY:** The manuscript contains numerous arithmetic and reporting errors that confuse the 99 newly sequenced Western UP specimens with the 270-genome combined phylogenetic dataset (99 Western UP + 171 GISAID from other regions):
  1. **Abstract (line 8):** Reports `55.55%` BA.2-like and `45.5%` B.1.617.2 among the 99 specimens (summing to `101.05%`), whereas Results (line 44) reports `75.7%` (75/99) BA.2-like and `19.19% + 1% + 1.01% = 21.2%` (21/99) Delta.
  2. **Results (line 44):** The Nextclade breakdown lists `21L (75.7% = 75/99)`, `21A (11/99)`, `21J (10/99)`, `20A (2/99)`, and `21B (1/99)`—which sums to $75 + 11 + 10 + 2 + 1 = 99$ samples, meaning there are *five* clades, not `"six major clades"` as stated on line 44.
  3. **Results (line 61):** Reports mutation occurrence counts across the dataset as `"D614G (266), S: T478K (261)... while S: T478K (187), P681R (113) and L452R (112) are specifically present in B1.617.2 lineage"`. In a dataset of 99 genomes (or even 270 genomes where only 113 are GK/Delta), `T478K` cannot occur `187` times specifically inside `B.1.617.2`. Moreover, line 61 states `"a total of 50 mutations in BA.2 (Omicron) and 33 in B1.167.2 (Delta)"` and in the very next sentence writes `"Likewise, out of 34, seven were located in the S gene of the Delta variant"` (`33` vs. `34`, and `B1.167.2` typo for `B.1.617.2`).
  4. **Results (line 84):** States that 270 genomes are categorized into four GISAID clades: `GRA (151)`, `GK (113)`, `GH (1)`, and `G (1)`, which sums to $151 + 113 + 1 + 1 = 266$, leaving 4 genomes unaccounted for.
* **WHAT & HOW:** Audit the 99-sample metadata table and the 270-sample GISAID table, correct the Abstract to report the exact counts out of 99 (`75/99 [75.8%] BA.2` and `21/99 [21.2%] Delta`), fix the `33` vs. `34` and `266/270` discrepancies, and clearly separate mutation counts in the 99 local samples from counts in the 270-sequence comparative alignment.

#### 2. Trim Amplicon Primer Sequences and Replace `GATK HaplotypeCaller` with a Viral Amplicon Variant Caller
* **WHY:** In the Methods (lines 127 and 137), libraries were amplified with tiled `QIAseq DIRECT SARS-CoV-2` primers, and reads were adapter-trimmed with `Cutadapt`, mapped with `BWA-MEM`, deduplicated with `GATK MarkDuplicates`, and called with `GATK HaplotypeCaller`. In tiled PCR amplicon sequencing, (a) synthetic primer sequences at the $5'$ ends of mapped reads must be soft-clipped (`iVar trim` or `samtools ampliconclip`) using the QIAseq BED file, otherwise primer-binding-site mutations (common in Omicron BA.2) are overwritten by the reference primer sequence; (b) `MarkDuplicates` erroneously discards valid biological amplicon reads because all reads from the same PCR tile share identical start/end coordinates; and (c) `GATK HaplotypeCaller` assumes a diploid organism rather than a haploid viral population.
* **WHAT:** Re-run variant calling on the 99 BAM files using a dedicated viral amplicon pipeline (`iVar` or `bcftools mpileup/call --ploidy 1` after `iVar trim` without `MarkDuplicates`).
* **HOW:** Run `ivar trim -i aligned.bam -b qiaseq_direct_primers.bed -p trimmed.bam`, followed by `samtools mpileup -aa -A -d 0 -Q 20 trimmed.bam | ivar variants -p variants -q 20 -t 0.7`, and verify whether any dropout sites or false reference calls in Spike (Figure 6) are corrected.

#### 3. Stratify Lineage Frequencies by Collection Month to Show the Delta-to-Omicron Transition
* **WHY:** Pooling 99 samples from March 2021 to January 2022 into a single pie chart (Figures 2–3) obscures the temporal replacement of Delta by Omicron, and the Methods conflict with the Results on selection criteria (`Ct < 30` in Methods line 117 vs. `Ct ranged from 19 to 21` in Results line 39).
* **WHAT:** Add a monthly stacked bar chart (March 2021 through January 2022) showing the number of RT-PCR positive cases, number of sequenced samples, and monthly clade proportions, and clarify the exact $C_t$ distribution of the 99 samples.
* **HOW:** Tabulate collection dates (month/year) and exact $C_t$ values for all 99 samples in Supplementary File 3 and plot monthly lineage counts alongside Figure 2.

#### 4. Correct Factual Errors Regarding SARS-CoV-2 History, Lockdown Dates, and Booster Vaccination
* **WHY:** Several historical and biological statements in the Introduction and Discussion are factually incorrect:
  1. **Introduction (line 19):** States `"In January 2021, WHO classified B.1.617.2 (Delta variant) as a VOC which had a Spike (S) double mutation namely E484Q and L452R."` In reality, WHO classified `B.1.617.2` as a VOC in **May 2021** (not January 2021), and `B.1.617.2` (Delta) **lacks** `E484Q` (`E484Q` + `L452R` was present in `B.1.617.1` Kappa, not `B.1.617.2` Delta).
  2. **Discussion (line 95):** States `"The country-wide lockdown (March 2021 to January 2022) was announced by the Government of India"`. India's nationwide lockdown occurred in March–May **2020**, not a 10-month nationwide lockdown from March 2021 to January 2022.
  3. **Discussion (line 105):** Claims `"most of the patients had received booster doses of the vaccine"` between March 2021 and January 2022 and refers to `"the fourth and fifth waves in India"`—remove these unsupported assertions unless verified patient vaccination dates are tabulated.
* **WHAT & HOW:** Correct the WHO Delta VOC designation date (May 2021), clarify that `E484Q` characterizes `B.1.617.1` (Kappa) rather than `B.1.617.2` (Delta), fix the lockdown dates, and remove the unsubstantiated booster-dose and fourth/fifth-wave claims from the Abstract and Discussion.
