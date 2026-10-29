<Blinded Review: TIME_ANON_0963>
**Composite Score:** 5.0 / 10.0 (Rigor: 1.5/3.5 | Claims: 1.3/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.0/2.0)
**Bias Category:** Technical/Assay
**Verdict:** Major Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Commodity/Hype-Cycle Template
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 5.0/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This comparative plant organelle genomics study assembles and annotates the mitochondrial genomes of six *Medicago* species (*M. lupulina*, *M. falcata*, *M. minima*, *M. edgeworthii*, *M. platycarpos*, and diploid *M. sativa*) using PacBio Revio HiFi long-read sequencing (21–42.9 Gb per sample, filtered via `Minimap2` against *M. truncatula* and assembled with `Flye` v2.9.1 / `Bandage`), and compares them alongside two publicly available *Medicago* mitogenomes (*M. truncatula* `NC_029641.1` and *M. arabica* `DQ662798.1`). Across the eight species, mitogenome sizes range from 281,240 to 356,577 bp (`GC` 44.92%–45.58%), exhibiting single circular chromosomes in five species and multipartite circular conformations in three (*M. falcata*, *M. platycarpos*, *M. sativa*). The authors perform a standardized suite of descriptive organelle analyses: repeat identification (`MISA` SSRs, `TRF` tandem repeats, `REPuter` dispersed repeats), relative synonymous codon usage (`RSCU`), in silico RNA editing prediction (`PREPACT`), `BLASTn`/`LINKVIEW2` synteny, pairwise `Ka/Ks` (`KaKs_Calculator` v2.0 across 27 shared PCGs), and concatenated 31-PCG ML (`IQ-TREE`) and Bayesian (`MrBayes`) phylogenetics across 25 Fabaceae species.

While PacBio HiFi long-read assembly is well suited for resolving plant mitochondrial recombination isoforms, forensic audit of the text and methods reveals **severe internal biological and numerical errors—including a swapped rRNA vs. tRNA count in the Results, a false statement in the Conclusions equating total genes (`55 to 74`) with protein-coding genes (`PCGs`), a non-existent mitochondrial GenBank accession (`DQ662798.1`, which is a short chloroplast/nuclear locus or plastome rather than a complete mitogenome) for *M. arabica*, and unedited template text (`evolutioFig. X.`) in Figure 7**.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### Major Technical, Biological, and Editorial Flaws
1. **Biological Inversion of rRNA (`18–24`) and tRNA (`3–5`) Gene Counts (Results Line 39) and Total Gene vs. PCG Confusion (Conclusions Line 165):**
   - In Results line 39, the authors state: *"Functional annotation identified 55–74 genes per genome, including 33–41 protein-coding genes (PCGs), **18–24 rRNA genes, and 3–5 tRNA genes** (Tables S3–S5; Figures S1–S6)."*
   - **Audit:** As the authors themselves wrote in the Background (line 20), angiosperm mitochondrial genomes contain **3 rRNA genes** (`rrn5`, `rrn18`, `rrn26`, occasionally duplicated to 4–5 copies) and **18–24 tRNA genes**! In Results line 39, the authors transposed the counts of **rRNA genes (`3–5`)** and **tRNA genes (`18–24`)**!
   - Even worse, in the Conclusions (line 165), the authors write: *"Genome sizes ranged from 281,240 to 356,577 bp, encompassing **55 to 74 protein-coding genes (PCGs)**"*—contradicting the Abstract and Results (`55–74 functional genes`, of which only `33–41` are PCGs).
2. **Invalid / Mismatched Public GenBank Accession for *Medicago arabica* (`DQ662798.1`) and Outgroup Selection (*Suriana maritima*):**
   - In Materials and Methods (Part 2, line 1), the authors state that the complete mitochondrial genome of *Medicago arabica* was downloaded from NCBI under accession **`DQ662798.1`**. In NCBI GenBank, `DQ662798.1` is a 2006 submission from a phylogenetic marker study, not a 300-kb complete plant mitochondrial genome (complete RefSeq mitogenomes carry `NC_` or recent `OQ`/`OR`/`PP`/`MZ` accessions).
   - In the phylogenetic analysis of 25 Fabaceae species (`Fig. 5`, line 94), the authors select *Suriana maritima* (family **Surianaceae**, order Fabales) as the outgroup, but refer to the dataset throughout lines 92 and 154 as *"25 Fabaceae species"*.
3. **Internal Contradictions in Positively Selected Genes (`Ka/Ks > 1`) Between Results and Discussion:**
   - In Results line 131, the genes exhibiting `Ka/Ks > 1` in pairwise comparisons are listed as **`cox2`, `matR`, and `rpl16`**.
   - Yet in Discussion line 156, the genes exhibiting `Ka/Ks > 1` are listed as **`ccmB`, `ccmFc`, `ccmFn`, `nad3`, `nad9`, and `matR`**—a completely different list of genes (except `matR`)!
   - Moreover, calculating `Ka/Ks` on raw genomic DNA sequences of plant mitochondrial genes (where `nad4`, `ccmB`, etc. undergo 46–89 C-to-U RNA editing events at 1st and 2nd codon positions, `Results` line 85) without accounting for RNA editing conflates genomic T-to-C back-mutations at edited sites with true nonsynonymous substitutions.
4. **In Silico `PREPACT` Prediction Misrepresented as Empirical RNA Editing Identification, Plus Contradictory C-to-U vs. U-to-C Proportions:**
   - No RNA-seq or cDNA sequencing was performed; all "identified" RNA editing sites (`452 to 568` sites) are purely computational homology predictions from `PREPACT` (`Methods` line 27).
   - Furthermore, line 83 states that *"92.53% to 95.35% were cytidine-to-uridine (C-to-U) substitutions"* (implying 4.65%–7.47% U-to-C reverse editing, which is virtually nonexistent in flowering plant mitochondria outside hornworts/lycophytes/ferns), and then immediately states: *"more than 50% of editing events occurred at the second codon position (59.40%–67.77%), followed by the first position (32.23%–40.60%). No editing events were detected at the third codon position."* Notice that $59.40\% + 40.60\% = 100.00\%$ and $67.77\% + 32.23\% = 100.00\%$.
5. **Unedited Template Artifacts in Figure 7 Caption and Missing Accession Numbers for the 6 New Mitogenomes:**
   - Line 124/127 contains raw copy-paste template text: **`during evolutioFig. X. Selection pressure analysis of 27 protein-coding genes...`**
   - Line 69 claims that *"approximately 75% [of all 64 codons] had RSCU values greater than 1 in multiple species"*. Mathematically, because the average RSCU across synonymous codons for every amino acid is identically $1.0$, it is impossible for 75% (48 of 64) of all codons to simultaneously have $\text{RSCU} > 1$! Looking at standard plant mitogenome RSCU tables, ~30–32 codons (nearly all ending in A or U, ~50%) have $\text{RSCU} > 1$.
   - No NCBI GenBank or SRA accession numbers are provided anywhere in the manuscript for the six newly sequenced *Medicago* mitochondrial genomes!

#### Strengths
1. **PacBio Revio HiFi Long-Read Sequencing:** Generating 21–42.9 Gb of PCR-free PacBio HiFi reads per species and inspecting `Flye` assembly graphs in `Bandage` (`Fig. 1A–F`) is the gold-standard approach for resolving multipartite plant mitochondrial conformations.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** Five *Medicago* species assemble as single circular mitogenomes while *M. falcata*, *M. platycarpos*, and *M. sativa* form multipartite circular chromosomes ranging from 281 to 357 kb. `[Moderately Supported]` — Supported by PacBio HiFi assembly graphs, though the raw reads and assemblies are not deposited in public repositories.
- **Claim 2:** *Medicago* mitogenomes contain 18–24 rRNA genes and 3–5 tRNA genes (or 55–74 PCGs), and 75% of codons have $\text{RSCU} > 1$. `[Methodologically Flawed]` — Numerically and biologically impossible statements resulting from careless drafting.
- **Claim 3:** `matR` and other mitochondrial PCGs experienced adaptive positive selection (`Ka/Ks = 3.34`). `[Fragile]` — Pairwise `Ka/Ks` on low-divergence plant mitogenomes (where $K_s$ in the denominator is near zero, e.g., 1 or 2 synonymous changes, and C-to-U RNA editing sites are unmasked) routinely produces artifactual `Ka/Ks > 1` ratios, and the Results and Discussion list contradictory sets of genes.

### 4. Reproducibility & Data Completeness
- **Data Availability:** Poor. No GenBank accessions or SRA BioProject IDs are provided for the six newly sequenced *Medicago* species, and the accession cited for *M. arabica* (`DQ662798.1`) is incorrect.
</Blinded Review: TIME_ANON_0963>
