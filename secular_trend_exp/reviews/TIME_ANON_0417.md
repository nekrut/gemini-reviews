<Blinded Review: TIME_ANON_0417>
**Composite Score:** 7.6 / 10.0 (Rigor: 2.6/3.5 | Claims: 2.1/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 7.6/10
VERDICT: PASS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary (SUMMARY)
This methodological study adapts Multiple Displacement Amplification (MDA, using $\Phi29$ DNA polymerase and exonuclease-resistant random hexamers) to whole-genome amplification (WGA) of single human sperm cells for fine-scale recombination mapping and experimental haplotyping. By optimizing alkaline Dithiothreitol (DTT)/KOH lysis at $65^\circ\text{C}$ rather than on ice, the authors amplify single-sperm dilutions ($0.8\text{ cells}/3\ \mu\text{L}$) in $50\ \mu\text{L}$ reactions, achieving $\ge 2500$-fold amplification at 76% of 12 tested chromosomal loci and $\ge 250$-fold amplification at 93% of loci, with second-round MDA (`S16MDA2`) providing an additional average 236-fold amplification. They validate the resulting single-sperm WGA products across Sanger resequencing (~3.3 kb per sample, estimating an error rate of $3.65 \times 10^{-5}$), 5 microsatellite (STR) markers (showing zero polymerase slippage), and 7 TaqMan SNP assays, demonstrating direct experimental phasing of multi-SNP haplotypes.

### 2. Methodological & Statistical Audit (WEAKNESSES & METHODOLOGICAL AUDIT)
- **Limiting Dilution vs. Micromanipulation/FACS Isolation:** Single sperm cells were isolated by limiting dilution ($0.8\text{ cells}/3\ \mu\text{L}$) rather than visual micromanipulation or flow sorting. Under a Poisson distribution with $\lambda = 0.8$, the probability of $\ge 1$ cell is $1 - e^{-0.8} = 55.1\%$ (matching the observed 9/16 positive aliquots = 56.3%), and the conditional probability that a positive aliquot contains $\ge 2$ cells is $\frac{1 - e^{-0.8}(1 + 0.8)}{1 - e^{-0.8}} = \frac{0.191}{0.551} = 34.7\%$. Indeed, the authors detect heterozygosity in 2 of the 9 positive aliquots (`S06` and `S14`, or 22.2%), leaving only $n=7$ confirmed single-sperm aliquots (`S01`, `S04`, `S05`, `S08`, `S13`, `S15`, `S16`, with `S01` subsequently lost before STR/TaqMan typing). While Poisson expectations are correctly noted, a sample size of $n=6\text{–}7$ single sperm from a single donor is modest for estimating genome-wide coverage and dropout distributions.
- **Table 2 Caption vs. Row Count Discrepancy:** The caption of Table 2 states: `"Total copy number for nine genes (TOP1, P53, CYP1A1, C6orf195, ADCYAP1, PTEN, PMS2 and CAT)..."`—listing only 8 gene names in parentheses while the table itself contains 9 gene rows (it omitted `PIK3CA` from the parenthetical list in the title).
- **Table 3 Calculation Check:** In Table 3, `S16MDA` input copy number is derived from $1\ \mu\text{L}$ of a $1/10\text{ C}_0$ dilution of the $50\ \mu\text{L}$ `S16` reaction (i.e., $1/500\text{th}$ of the total copies in Table 2). Checking the math: for `CYP1A1`, Table 2 reports $3.4 \times 10^7$, and $3.4 \times 10^7 / 500 = 68,000$ (Table 3 reports $68,995$, from unrounded qPCR values); for `C6orf195`, $4.2 \times 10^5 / 500 = 840$ (exact match); for `ADCYAP1`, $6.1 \times 10^5 / 500 = 1220$ (Table 3 reports $1225$); for `PTEN`, $5.8 \times 10^5 / 500 = 1160$ ($1155$). The internal arithmetic across Tables 2 and 3 is fully consistent.
- **High Non-Specific Background Synthesis:** The authors candidly report that negative control aliquots without sperm yield $15\text{–}35\ \mu\text{g}$ of total DNA (identical to the $13\text{–}35\ \mu\text{g}$ yield of sperm-containing tubes) due to hexamer-primed artifactual synthesis, and that locus-specific representation varies by several orders of magnitude across single cells (leading them to appropriately caution against using single-cell MDA for CGH copy-number analysis).

### 3. Biological / Experimental Grounding & Claim Proportionality (STRENGTHS)
- `[Well Supported]` Alkaline DTT/KOH lysis at $65^\circ\text{C}$ markedly outperforms lysis on ice for decondensing protamine-packed human sperm chromatin prior to $\Phi29$ MDA (7/8 vs. 2/8 aliquots amplifying all 3 test genes).
- `[Well Supported]` High fidelity of $\Phi29$ MDA on single-sperm templates (1 mutation in 27.4 kb sequenced = $3.65 \times 10^{-5}$) and absence of microsatellite repeat slippage across 5 STR loci compared to thermophilic Taq/PEP-based WGA.
- `[Well Supported]` Demonstration that single-sperm MDA products allow direct physical phasing of heterozygous SNPs into haplotypes (`AAA`/`CCG` on `NT_011362.9`, `CG`/`TA` on `NT_010194.16`, and `ACE`, `EDN1`, `ELF5` haplotypes).

### 4. Reproducibility & Data Completeness
All 19 PCR primer pairs (Sets A, B, C) are provided in full in Table 1, along with dbSNP rsIDs, GenBank contig accessions (`NT_011362.9`, `NT_010194.16`) with exact nucleotide coordinates, STR marker IDs, reagent concentrations, and thermal cycling parameters.
</Blinded Review: TIME_ANON_0417>
