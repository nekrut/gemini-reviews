# Review of PMC7428442 (PMID:32835962)

**Manuscript Title:** SARS-CoV-2 has been circulating in northern Italy since December 2019: Evidence from environmental monitoring  
**Authors:** La Rosa G, Mancini P, Bonanno Ferraro G, Veneri C, Iaconelli M, Bonadonna L, Lucentini L, Suffredini E.  
**Journal / Preprint:** *Sci Total Environ* (2021; `PMC7428442` / `PMID:32835962` / `10.1016/j.scitotenv.2020.141711`)  
**Calibration Study Cohort:** Cohort A — Known Invalid / Refuted (`A08` | Double-Blinded as `ANON_05`)  
**Overall Score:** **5.5 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.8/3.5 | Claims: 1.4/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.1/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript investigates whether SARS-CoV-2 was circulating in northern Italy prior to the first officially diagnosed autochthonous case (21 February 2020) by testing 40 archival 24-hour composite raw sewage samples collected between 9 October 2019 and 28 February 2020 from five wastewater treatment plants (WWTPs) in Milan, Turin, and Bologna, alongside 24 pre-pandemic "blank" sewage samples from September 2018 to June 2019. Using a modified WHO PEG-dextran two-phase concentration with chloroform extraction, followed by an in-house nested RT-PCR (332 bp inner amplicon in ORF1ab/nsp14), a newly designed probe-based RT-qPCR targeting the same nsp14 region (positions 18,600–18,699), and two Corman et al. (2020) assays (E and RdRp), the authors find 0/40 positives with the Corman E and RdRp assays, 18/40 positives by nested RT-PCR, 26/40 positives by nsp14 RT-qPCR, and 15/40 confirmed by both nsp14 assays—including samples dated 18 December 2019 in both Milan and Turin. Twelve Sanger sequences were deposited in GenBank (MT843229–MT843240).

While the inclusion of 24 historical negative sewage controls (2018–2019), quadruplicate HCoV-229E recovery spiking ($2.04 \pm 0.70\%$), inhibition testing, and Sanger confirmation of nested amplicons are substantial strengths, the study's central claim of simultaneous multi-city community circulation in mid-December 2019 is undermined by several unresolved analytical and Contamination/Target-Overlap vulnerabilities: (1) both the nested RT-PCR and the "confirming" RT-qPCR target the exact same short region of ORF1ab (nsp14), meaning that any trace laboratory amplicon or synthetic positive-control DNA (BioFab Research) from the nested RT-PCR target region can cross-react with the RT-qPCR assay, whereas two independent genomic targets (E and RdRp) were 100% negative (0/40) across all samples; (2) only 12 GenBank accessions (MT843229–MT843240) are deposited for 18 nested-PCR-positive samples, and no sequence alignment or SNV comparison is presented to rule out identity with the synthetic positive control; and (3) quantitative back-calculations show that detecting $1.2\times 10^3\text{ to }4.1\times 10^3\text{ g.c./L}$ in raw sewage from catchment populations of hundreds of thousands of inhabitants on 18 December 2019 implies widespread community shedding that flatly contradicts flat (non-increasing) sewage viral loads over the subsequent two months (December 18 to late February) and molecular clock estimates. Addressing these limitations requires amplifying a second, non-overlapping genomic locus (e.g., CDC N1/N2), reporting whether the synthetic positive control carries a distinguishable marker mutation, and performing a quantitative mass-balance shedding calculation.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **The modified PEG-dextran + chloroform protocol and nsp14 assays achieve a $\text{LOD}_{50}$ of $1.46\text{ g.c./}\mu\text{L}$ RNA and $\text{LOQ}$ of $7.35\text{ g.c./}\mu\text{L}$ in spiked sewage, with $0/24$ false positives in 2018–2019 blank samples: [Well Supported].**  
  The analytical validation using the EVAg coronavirus panel, 32 enteric viruses, 15 bacterial species, quadruplicate HCoV-229E recovery controls, and 24 archival sewage blanks (Methods lines 71–73, Results lines 78–82) is clearly documented. However, it is unclear from the text whether the 24 historical blank samples were extracted and amplified interleaved in the exact same batches and plates as the December 2019–February 2020 samples or processed in separate runs.

* **Fifteen sewage samples are independently confirmed positive by two orthogonal molecular methods: [Fragile].**  
  In Results (line 84), the authors require positivity by both the nested RT-PCR and the newly developed real-time RT-qPCR to classify a sample as "confirmed positive" ($15/40$ samples), while noting that **0/40 samples tested positive using the Corman et al. E gene and RdRp assays** (even with the Vogels et al. modified reverse primer). Crucially, Table 1 reveals that both the nested RT-PCR (`2274-CO-FW1`/`2275-CO-REV1` and `2276-CO-FW2`/`2277-CO-REV2`) and the new real-time RT-qPCR (`2297-CoV-2-F`/`2298-CoV-2-R`/`2299-CoV-2-P`) target the **same ORF1ab (nsp14) region**! Furthermore, Methods (line 51) states that a *"synthetic DNA fragment (Biofab Research, Italy) including the PCR target region was used as positive control"* alongside high-copy synthetic standards ($10^1\text{--}10^5\text{ copies/}\mu\text{L}$) for the nsp14 RT-qPCR (line 58b). Because nested PCR involves opening first-round 35-cycle reaction tubes to transfer $2\ \mu\text{L}$ into a second 35-cycle reaction (70 cycles total), and the RT-qPCR amplifies inside the same nsp14 locus, the two assays are not independent with respect to amplicon or synthetic-control cross-contamination, and the absence of any amplification in the E or RdRp genes leaves single-locus dependency unresolved.

* **SARS-CoV-2 was circulating simultaneously in Milan and Turin by 18 December 2019, and in Bologna by 29 January 2020 (or 10 December 2019 by qPCR): [Fragile].**  
  Several internal inconsistencies in Table 2 and epidemiological mass-balance constraints weaken this conclusion (Pillars 3, 5, and 6):
  1. *Lack of exponential growth over 10 weeks:* In Milan, the concentration measured on 18 December 2019 in Plant A ($4.1\times 10^3\text{ g.c./L}$, sample 3289) is *higher* than in every subsequent Milan sample through 28 February 2020 ($4.8\times 10^2\text{ to }3.7\times 10^3\text{ g.c./L}$). Similarly, in Bologna (Plant E), sample 3375 on 10 December 2019 has an unconfirmed qPCR reading of $2.9\times 10^4\text{ g.c./L}$ (nearly 5-fold *above* the LOQ of $5.9\times 10^3\text{ g.c./L}$, yet negative by nested RT-PCR!), followed by $3.3\times 10^4\text{ g.c./L}$ on 29 January 2020 and complete negativity by qPCR on 19 February 2020 (sample 3377). For an respiratory/enteric pandemic virus with $R_0 \approx 2.5\text{--}3.5$ and a doubling time of 3–5 days, maintaining a flat sewage concentration of $\sim 10^3\text{ g.c./L}$ across three cities from mid-December 2019 to late February 2020 without triggering hospital surges until late February is epidemiologically anomalous.
  2. *Missing sequence data and alignment results:* In Methods (line 53), the authors state that all nested PCR amplicons were sequenced, aligned with 134 Italian GISAID genomes in MEGA X, and deposited under GenBank accessions MT843229–MT843240. However, MT843229–MT843240 represents only **12 sequences**, whereas Table 2 reports **18 nested RT-PCR positive samples** (and 15 dual-positive samples). Moreover, the Results section never reports the outcome of the MEGA X alignment (e.g., whether the 332-bp sequences had any SNVs or were 100% identical to the synthetic control).

* **Unit conversion consistency between $\text{g.c./}\mu\text{L}$ RNA and $\text{g.c./L}$ sewage at the LOQ: [Moderately Supported].**  
  In Results (line 78), the authors report $\text{LOD}_{50} = 1.46\text{ g.c./}\mu\text{L}$ RNA and $\text{LOQ} = 7.35\text{ g.c./}\mu\text{L}$ RNA, and in Table 2 / line 86 they state the sewage $\text{LOQ}$ is $5.9\times 10^3\text{ g.c./L}$ (meaning $1\ \mu\text{L}$ of extracted RNA corresponds to $1.25\text{ mL}$ of original sewage, i.e., $125\text{ mL}$ concentrated half-volume eluted into $100\ \mu\text{L}$ RNA, since $7.35 / 0.00125 = 5,880 \approx 5.9\times 10^3\text{ g.c./L}$). However, this elution volume ($100\ \mu\text{L}$) and whether concentrations in Table 2 are uncorrected or corrected for the $2.04\%$ HCoV-229E recovery efficiency are never explicitly stated in the Methods.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Confirm Positive Samples Using an Independent Non-Overlapping Genomic Target (e.g., CDC N1/N2)
* **WHY:** Both positive assays (nested RT-PCR and nsp14 RT-qPCR) amplify within the same ORF1ab (nsp14) region, whereas both non-overlapping Corman assays (E and RdRp) were 0/40 negative. Confirming the stored $-80\ ^\circ\text{C}$ RNA/concentrate aliquots (Methods line 34) with an independent target that never shared a synthetic positive control or nested-PCR amplicon in the laboratory is essential to rule out single-locus carryover.
* **WHAT:** Test the 15 confirmed positive RNA extracts (or the unextracted half-concentrates stored at $-80\ ^\circ\text{C}$) using the high-sensitivity US CDC 2019-nCoV_N1 and N2 RT-qPCR assays targeting the Nucleocapsid (N) gene.
* **HOW:** Run the CDC N1 and N2 TaqMan assays in duplicate on the stored RNA aliquots alongside the 24 archival blanks and report Cq values in Table 2.

#### 2. Document Amplicon Coordinates, Synthetic Control Distinguishability, and All 18 Nested-PCR Sequences
* **WHY:** If the BioFab synthetic positive-control DNA (line 51) has the exact wild-type Wuhan-Hu-1 sequence spanning primers `2274-CO-FW1` to `2275-CO-REV1` and `2297-CoV-2-F` to `2298-CoV-2-R`, Sanger sequencing of the 332-bp nested PCR product cannot distinguish authentic viral cDNA from trace positive-control DNA contamination. Furthermore, 18 samples are listed as nested-PCR positive in Table 2, but only 12 GenBank accessions (MT843229–MT843240) are provided.
* **WHAT:** Specify the exact nucleotide coordinates of the nested primers vs. the RT-qPCR primers and synthetic controls, report the results of the MEGA X alignment (mentioned in Methods line 53 but omitted from Results), and account for all 18 sequenced amplicons.
* **HOW:** 
  1. Add exact NC_045512.2 genomic coordinates for all primers in Table 1 and state whether the BioFab synthetic positive control contained an engineered marker mutation or restriction site to distinguish it from wild-type SARS-CoV-2.
  2. Explain in the Results which 12 of the 18 nested-PCR-positive samples correspond to MT843229–MT843240, why the remaining 6 positive amplicons were not deposited, and describe the sequence identity/SNVs found in the alignment with the 134 Italian GISAID genomes.
  3. Clarify whether the 24 pre-pandemic blank sewage samples were extracted and run on the exact same plates alongside the October 2019–February 2020 samples.

#### 3. Provide the Explicit Formula Converting $\text{g.c./}\mu\text{L}$ RNA to $\text{g.c./L}$ Sewage and Perform a Shedding Mass-Balance Check
* **WHY:** Readers cannot verify how $\text{LOQ} = 7.35\text{ g.c./}\mu\text{L}$ RNA maps to $5.9\times 10^3\text{ g.c./L}$ in wastewater without the final NucliSENS elution volume ($V_{\text{eluate}} = 100\ \mu\text{L}$) and the explicit formula, nor whether Table 2 values are raw or recovery-adjusted ($2.04\%$).
* **WHAT:** Add the concentration conversion equation to the Methods and include a brief quantitative mass-balance calculation in the Discussion estimating how many shedding individuals are required to yield $10^3\text{--}10^4\text{ g.c./L}$ in these WWTPs.
* **HOW:** State the formula:
  $$C_{\text{sewage}}\ (\text{g.c./L}) = \frac{C_{\text{RNA}}\ (\text{g.c./}\mu\text{L}) \times V_{\text{eluate}}\ (\mu\text{L})}{V_{\text{sewage processed}}\ (0.125\text{ L})}$$
  and discuss the epidemiological implications of detecting $4.1\times 10^3\text{ g.c./L}$ (uncorrected) or $\sim 2\times 10^5\text{ g.c./L}$ (corrected for $2.04\%$ recovery) in a catchment serving hundreds of thousands of residents on 18 December 2019.

#### 4. Address High-Copy Unconfirmed RT-qPCR Signals Above LOQ (Sample 3375)
* **WHY:** In Table 2, sample 3375 (Bologna, 10/12/2019) has a real-time RT-qPCR value of $2.9\times 10^4\text{ g.c./L}$—the third highest concentration in the entire study and 5-fold above the LOQ ($5.9\times 10^3\text{ g.c./L}$)—yet it tested negative by the sensitive nested RT-PCR ($3.71\text{ g.c./}\mu\text{L}$ limit), and is plotted in Figure 2.
* **WHAT:** Explain in the Results and Discussion why a sample at $2.9\times 10^4\text{ g.c./L}$ failed nested RT-PCR amplification, and avoid plotting unconfirmed single-assay positives as SARS-CoV-2 trend points in Figure 2 without clear visual distinction.
* **HOW:** Use distinct symbols/colors in Figure 2 to separate the 15 dual-confirmed samples from the 11 unconfirmed qPCR-only detections.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** The manuscript contains several numerical/date typos and duplicated text blocks that should be corrected.
* **WHAT & HOW:**
  * **Duplicated paragraphs in Methods (lines 58–62):** Paragraphs `a)` and `b)` in line 58 are duplicated word-for-word in lines 60 and 62, and Table 1/2 captions are duplicated in lines 30–32, 43–49, and 148–218. Remove the redundant blocks.
  * **Death count typo in Discussion (line 93):** Line 93 writes *"with 35.6441 deaths"* whereas the Introduction (line 16) correctly states *"35.644 deaths"* (i.e., 35,644). Fix to 35,644.
  * **Date typo in Discussion (line 99):** Referring to Deslandes et al. (2020), line 99 states the French patient *"had been hospitalised on December 27, 2020"*—change *"2020"* to *"2019"*.
  * **Spelling and unit typos:** Abstract line 7: *"real-rime RT-PCR"* $\rightarrow$ *"real-time RT-PCR"*; Figure 1 caption (lines 30, 32, 223): *"inhibitants"* $\rightarrow$ *"inhabitants"* and *"WTPs"* $\rightarrow$ *"WWTPs"*; Figure 2 caption (lines 86, 224): *"quatitative"* $\rightarrow$ *"quantitative"*; Table 2 header (lines 84, 170): *"c.g./L"* $\rightarrow$ *"g.c./L"*.
