<Blinded Review: TIME_ANON_0397>
**Composite Score:** 6.0 / 10.0 (Rigor: 1.8/3.5 | Claims: 1.7/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.2/2.0)
**Bias Category:** Algorithmic/Model
**Verdict:** Major Revision
**Study Modality:** Dry-Lab Secondary Cohort/Database
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This comparative plant genomics study identifies and characterizes the phospholipase D (PLD) gene family in two woody dicots—Poplar (*Populus trichocarpa*, 18 genes including 1 pseudogene `PtPLD18`) and Grape (*Vitis vinifera*, 11 genes)—and compares them against *Arabidopsis thaliana* (12 genes) and rice (*Oryza sativa*, 16 functional genes). Using Neighbor-Joining (NJ) phylogenetics, exon-intron architecture, MEME/MAST motif discovery (30 motifs across N-terminal C2/PXPH, central HKD1/HKD2, and C-terminal regions), flanking-gene microsynteny ($K_s$ dating), DIVERGE Type-I functional divergence ($\theta_I = 0.64, P < 0.01$), and PAML 4.0 `codeml` site models, the authors classify higher-plant PLDs into 6 subgroups ($\alpha, \beta/\gamma, \delta, \varepsilon, \zeta, \varphi$) across three domain subfamilies (C2-PLDs, PXPH-PLDs, and signal-peptide SP-PLDs). They show that Poplar experienced a recent segmental duplication expansion ($K_s = 0.21–0.25$, dated to 11.3–13.8 Ma). However, the study contains a major table-vs-text swap in the $K_s$ molecular clock calculations for Grape and *Arabidopsis*, and over-interprets non-significant PAML site-model parameters ($\omega = 1.34$ and $\omega = 8.14$) as evidence of positive selection on PXPH- and SP-PLDs.

### 2. Methodological & Statistical Audit
* **Swapped Molecular Clock Rates ($\lambda$) and Duplication Dates Between Grape and *Arabidopsis* (Table 3 vs. Text):**
  * In the Methods (offset line 11), the synonymous substitution rates ($\lambda$) are stated as $1.5 \times 10^{-8}$ for *Arabidopsis*, $6.5 \times 10^{-9}$ for rice, $9.1 \times 10^{-9}$ for Poplar, and $6.5 \times 10^{-9}$ for Grape, with duplication date $T = K_s / (2\lambda)$.
  * In Table 3 (lines 113–114), the Grape paralog pair `VvPLD10`/`VvPLD1` has Mean $K_s = 1.1491$ and Date $= 88.39\text{ Ma}$ ($1.1491 / (2 \times 6.5 \times 10^{-9}) = 88.39\text{ Ma}$), while the *Arabidopsis* pair `AtPLD\alpha1`/`AtPLD\alpha2` has Mean $K_s = 0.7527$ and Date $= 25.09\text{ Ma}$ ($0.7527 / (2 \times 1.5 \times 10^{-8}) = 25.09\text{ Ma}$).
  * Yet in the Results prose (lines 119–121), the authors swap the two rows from Table 3: *"The PLD gene segmental duplication in Grape was estimated to have occurred about 25.09 Ma (mean Ks = 0.7527)... The earliest observed segmental duplication event occurred in the PLD genes of Arabidopsis around 88.39 Ma."* This inversion leads the authors to build an erroneous evolutionary narrative claiming Grape duplicated at 25.09 Ma and *Arabidopsis* at 88.39 Ma, directly contradicting their own Table 3.
* **Inconsistent Gene Counts in Abstract vs. Conclusion:** The Abstract (line 9) and Results (line 92) state that "76.5%, 13/17" of Poplar PLD genes clustered closely with Grape, whereas the Conclusion (line 167) states "82.8%, 14/17" (note also that $14/17 = 82.4\%$, not $82.8\%$).
* **Unsupported Positive Selection Claims for PXPH-PLDs and SP-PLDs:** In the Abstract (line 9), Results (line 132), and Conclusion (line 167), the authors claim that "positive selection contributed to the evolution of the PXPH- and SP-PLDs" based on PAML `codeml` site models estimating $\omega = 1.34$ (PXPH-PLD) and $\omega = 8.14$ (SP-PLD). However, line 132 admits that the Bayes Empirical Bayes (BEB) posterior probabilities did *not* reach significance ($P < 0.90$), and the SP-PLD alignment consists of only 3 sequences across all 4 species (`PtPLD11`, `VvPLD3`, `OsPLD\varphi`, as *Arabidopsis* lacks SP-PLD). Fitting PAML site models (M2a/M8) to an alignment of just 3 highly diverged sequences across monocots and dicots has virtually zero statistical power and extreme parameter instability ($\omega = 8.14$).
* **Phylogenetic Tree Construction Using Uncorrected $p$-Distance:** Constructing the multi-species superfamily tree across divergent subfamilies (C2, PXPH, and SP-PLDs, which do not even share N-terminal domain homology) using Neighbor-Joining with uncorrected $p$-distance and complete deletion (line 184) ignores multiple hits and rate heterogeneity across sites ($\Gamma$), and complete deletion discards all alignment columns outside the shared catalytic core when SP-PLDs (~516 aa) are aligned with PXPH-PLDs (~1,100 aa).

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Classification of Poplar (18) and Grape (11) PLDs into C2, PXPH, and SP subfamilies and 6 subgroups:** `[Well Supported]` — Domain architecture (PFAM/SMART) and exon-intron conservation clearly support the assignment of Poplar and Grape PLDs into the established $\alpha, \beta/\gamma, \delta, \varepsilon, \zeta, \varphi$ subgroups.
* **Recent segmental duplication of 5 PLD gene pairs in Poplar (~11.3–13.8 Ma):** `[Well Supported]` — Microsynteny of flanking protein-coding genes (2 to 12 conserved flanking genes in Table 3) and tightly clustered $K_s$ values ($0.206–0.251$) align well with the known salicoid whole-genome duplication in *Populus*.
* **Positive selection driving PXPH-PLD and SP-PLD evolution:** `[Overstated]` — Based on tiny sample sizes (3 SP-PLD sequences, 6 PXPH-PLD sequences), non-significant BEB site support, and deep divergence ($K_s$ saturation between monocots and dicots).

### 4. Reproducibility & Data Completeness
* **Gene Catalogs and Motif Alignments:** Tables 1–3 provide NCBI Gene IDs, JGI/Genoscope locus IDs, genomic coordinates, protein lengths, and EST counts for all Poplar and Grape PLDs, and Additional Files 1–14 document the MEME motifs and domain alignments.
* **Typo in URL and Text/Table Mismatch:** Line 189 contains a typo in the JGI Poplar URL (`.../Poptr1_1/optr1_1.home.html`), and the swapped Grape/*Arabidopsis* $K_s$ values between Table 3 and lines 119–121 require correction.
</Blinded Review: TIME_ANON_0397>
