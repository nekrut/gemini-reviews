# Review of PMID:36029839 / PMC9404229 (10.1016/j.envres.2022.113979)

**Manuscript Title:** Molecular evidence for SARS-CoV-2 in samples collected from patients with morbilliform eruptions since late 2019 in Lombardy, northern Italy  
**Authors:** Antonella Amendola, Marta Canuti, Silvia Bianchi, Sudhir Kumar, Clara Fappani, Maria Gori, Daniela Colzani, Sergei L. Kosakovsky Pond, Sayaka Miura, Melissa Baggieri, Antonella Marchi, Elisa Borghi, Gianvincenzo Zuccotti, Mario C. Raviglione, Fabio Magurano, Elisabetta Tanzi  
**Journal / Preprint:** *Environmental Research* (2022, Vol. 215, Pt 1, 113979; `PMID:36029839` / `PMC9404229` / `10.1016/j.envres.2022.113979`)  
**Overall Score:** **4.1 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.2/3.5 | Claims: 0.8/2.5 | Biology: 0.7/2.0 | Reproducibility: 1.4/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

Amendola et al. test 435 archival clinical specimens (148 oropharyngeal swabs, 141 urine samples, and 146 sera) from 156 measles/rubella-negative morbilliform rash patients in Lombardy, Italy across three sampling periods: a pre-pandemic control cohort (August 2018 – July 2019, $N=100$), a late pre-pandemic cohort (August 2019 – February 2020, $N=44$), and a pandemic cohort (March 2020 – March 2021, $N=12$). Using four two-round hemi-nested RT-PCR assays targeting `NsP3` (263 bp, spanning C3037T), `RdRp` (335 bp, spanning C14408T), `Spike A` (421 bp, spanning A23403G / D614G), and `Spike B` (470 bp, RBD), alongside CDC real-time RT-qPCR, Euroimmun IgG/IgM/IgA ELISA, and plaque-reduction neutralization tests ($\text{PRNT}_{80}$), the authors report SARS-CoV-2 RNA in 11/44 (25%) pre-pandemic cases (earliest September 12, 2019) and 2/12 (16.7%) pandemic cases. Mapping Sanger amplicons (GenBank `MZ223385`–`MZ223398`) and re-analyzed Brazilian sewage reads (`PRJNA679821`) onto the Mutation Order Approach (MOA) graph of Kumar et al. (2021), the authors find that all pre-pandemic amplicons covering positions 3037, 14408, or 23403 carry derived B.1 ($\alpha\beta$) alleles, and extrapolate a `proCoV2` origin in late June to late July 2019.

Screening biobanked surveillance specimens with pre-August 2019 negative controls ($N=183$ swabs/urine) and depositing the resulting Sanger sequences in GenBank (`MZ223385`–`MZ223398`) are positive aspects of the study design. However, the core evolutionary and epidemiological conclusions are undermined by severe methodological, contamination-control, and biological flaws: (1) 0 of 13 cases tested positive by standard CDC real-time RT-qPCR and 9 of 11 pre-pandemic cases amplified in only 1 of 4 hemi-nested assays, yet every amplified October–December 2019 fragment carries the derived B.1 haplotype (`C3037T`, `C14408T`, `A23403G`) matching the dominant 2020 European strain and likely laboratory positive control; (2) asymmetric serological interpretation dismisses 12 ELISA-positive control sera (including 4 with 50–59% plaque reduction at 1:10) as background noise while treating non-neutralizing ($\text{PRNT}_{80}$-negative) ELISA hits in late-2019 cases as confirmatory; (3) backward linear extrapolation of $k=6$ mutations from single-locus amplicons without whole genomes or a phylogenetic clock model is invalid; and (4) 4.5 months of cryptic B.1 (Spike D614G) transmission at 25% positivity in rash patients without triggering an epidemic wave in autumn 2019 contradicts SARS-CoV-2 transmission dynamics. Resolving these issues requires disclosing the positive-control sequence, applying symmetric statistical tests across cohorts, and removing the uncalibrated molecular clock claims.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Circulation of Derived B.1 ($\alpha\beta$) Strains (`C3037T`, `C14408T`, `A23403G`) in Italy in October 2019: Fragile / High Risk of Amplicon Carryover.**  
  In Table 3 and Figure 2, every pre-pandemic specimen yielding an `NsP3` (Patients #5, #7), `RdRp` (Patients #3, #4, #6, #9), or `Spike A` (Patient #9) sequence between October 17 and December 15, 2019 carries the derived B.1 alleles (`3037T`, `14408T`, `23403G`), with zero ancestral lineage A or `Wuhan-Hu-1` (lineage B) alleles observed at those positions. Detecting exclusively 2020-derived B.1 alleles in October 2019—only after two rounds of hemi-nested PCR, in specimens 100% negative by CDC RT-qPCR, where 9/11 pre-pandemic cases failed to amplify 3 of 4 target loci, and where a SARS-CoV-2 positive control was included in every amplification round (Section 2.2)—strongly points to trace positive-control or post-PCR carryover rather than pre-Wuhan circulation of B.1.

* **Extrapolation of a Late June – Late July 2019 `proCoV2` Emergence Date: Methodologically Flawed.**  
  In Section 3.2, the authors assume that because single 263–335 bp amplicons from October 17–22, 2019 carry `C14408T` or `C3037T`, the unsequenced remainder of those genomes must carry all three $\beta$ and all three $\alpha$ mutations ($k=6$ substitutions from `proCoV2`), and linearly subtract $11.6\text{--}16.2$ weeks from October 17, 2019. No patient in the study was ever shown to carry all three $\beta$ mutations together (let alone $\alpha_1\text{--}\alpha_3$, which were never targeted). Extrapolating a multi-locus root age by deterministic subtraction from single-amplicon fragments without whole genomes, phylogenetic topology, or Poisson variance propagation is statistically invalid.

* **Serological Confirmation of Pre-Pandemic Cases (ELISA & $\text{PRNT}_{80}$): Overstated / Asymmetric Hypothesis Testing.**  
  In Table 3, 0 of the 9 tested pre-pandemic RNA-positive cases met the standard $\text{PRNT}_{80}$ neutralization threshold (only Patient #5 showed 62% plaque reduction at 1:10 dilution), whereas pandemic cases (#12, #14) neutralized at 1:60 and 1:160. In the pre-September 2019 control cohort ($N=98$ sera), 12 samples (12.2%) were ELISA-positive (IgM/IgA/IgG) and 4 showed 50–59% plaque reduction at 1:10 (Section 3.1). Dismissing 12/98 ELISA-positive / partially neutralizing control sera as inconclusive background while citing 4/9 non-neutralizing ($\text{PRNT}_{80}$-negative) ELISA positives in the pre-pandemic cases as corroborating evidence violates symmetric hypothesis testing.

* **Undetected Circulation of High-Fitness B.1 ($\alpha\beta$) Virus in Lombardy from September 2019 to February 2020: Overstated / Biologically Implausible.**  
  In Section 4.2, the authors argue that an $\alpha\beta$ strain "capable of efficient human-to-human transmission" circulated in northern Italy from September 2019. The $\alpha\beta$ (B.1 / D614G) lineage has a basic reproduction number $R_0 \approx 2.5\text{--}3.5$ and doubling time of 3–5 days, which drove a >60% excess mortality surge within weeks of February 2020. Continuous community circulation infecting 25% (11/44) of non-measles rash patients across Milan and Brescia starting in September–October 2019 cannot be reconciled with the complete absence of hospital/ICU surges or positive influenza-surveillance swabs until late February 2020.

* **Attribution of the 2019 Rise in Measles/Rubella Discard Percentage to SARS-CoV-2: Overstated.**  
  Figure 1 plots the percentage of suspected measles/rubella cases testing negative ("discarded"), which rose from ~30% in 2017–2018 to ~70% in late 2019. Italy experienced a large measles epidemic in 2017–2018 followed by a sharp drop in true measles incidence in 2019 (visible in the grey total-case bars in Figure 1). When true measles cases fall while endemic non-measles rashes (HHV-6, parvovirus B19, enteroviruses, EBV) continue at baseline rates, the fraction of measles-negative cases automatically rises without requiring SARS-CoV-2.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Report the Positive Control Sequence and Audit Carryover Risk
* **WHY:** Every amplification round included "RNA isolated from a SARS-CoV-2-positive patient" (Section 2.2), and all pre-pandemic `NsP3`, `RdRp`, and `Spike A` sequences carry the 2020 B.1 alleles (`3037T`, `14408T`, `23403G`) despite failing single-round RT-qPCR and amplifying only 1 of 4 loci in 9/11 pre-pandemic patients.
* **WHAT:** Disclose the exact genotype of the positive control and evaluate whether amplicon carryover can explain the observed B.1 alleles.
* **HOW:** Report the Pango lineage and full sequence of the positive control RNA in Section 2.2. For the two unique transitions in Patient #5 (`MZ223388`: `T2987C` and `T3012C`), note that non-proofreading `DreamTaq` polymerase across two nested rounds (70+ cycles) from single-copy templates introduces $\sim 10^{-4}$ $\text{T}\to\text{C}$ errors per base per cycle; re-amplify Patient #5 RNA in duplicate with a proofreading polymerase to verify whether `T2987C`/`T3012C` are reproducible template mutations or Taq polymerase errors.

#### 2. Apply Symmetric Statistical Comparisons to Control and Pre-Pandemic Serology
* **WHY:** Treating 12/98 ELISA-positive (and 4/98 with 50–59% plaque reduction at 1:10) control sera as false positives while interpreting 4/9 ELISA-positive (and 1/9 with 62% plaque reduction at 1:10, 0/9 $\text{PRNT}_{80}$-positive) pre-pandemic sera as supportive evidence is an asymmetric double standard.
* **WHAT:** Test formally whether serological reactivity in the pre-pandemic cohort exceeds the false-positive rate of the 2018–2019 control cohort.
* **HOW:** Report Fisher's exact test $p$-values comparing ELISA positivity and $\text{PRNT}_{80}$ positivity across the Control ($N=98$), Pre-pandemic ($N=38$), and Pandemic ($N=10$) serum cohorts in Table 1 or Section 3.1, and apply the strict $\text{PRNT}_{80}$ threshold uniformly to all cohorts.

#### 3. Remove the Uncalibrated June–July 2019 Molecular Clock Extrapolation
* **WHY:** Assuming that a single 335-bp `RdRp` amplicon (`MZ223389`, Oct 17, 2019) belongs to a full genome carrying 6 derived $\alpha\beta$ substitutions and subtracting $11.6\text{--}16.2$ weeks without a tree, whole genome, or Poisson variance model is methodologically invalid.
* **WHAT:** Restrict evolutionary claims to the sequenced amplicon coordinates.
* **HOW:** Delete the "late June – late July 2019" `proCoV2` emergence estimate from the Abstract, Section 3.2 (page 6), and Section 4.2 (page 7), and state that single-locus 263–470 bp amplicons cannot support molecular clock dating.

#### 4. Control for the Post-Epidemic Measles Trough and Differential Exanthema Pathogens
* **WHY:** In Figure 1, the rise in the percentage of discarded measles/rubella cases in 2019 is confounded by the end of the 2017–2018 Italian measles epidemic and the absence of differential viral testing.
* **WHAT:** Separate denominator changes (falling true measles cases) from numerator changes (non-measles rashes) and report differential diagnostics.
* **HOW:** Re-plot Figure 1 showing absolute monthly counts of measles/rubella-positive cases alongside measles/rubella-negative cases, and report differential PCR/serology results for HHV-6, Parvovirus B19, Enterovirus, and EBV among the 44 pre-pandemic cases.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Coordinate mismatches between the main text, Table 2, and GenBank entries create confusion when verifying mutations.
* **WHAT & HOW:**
  * **NsP3 vs. ORF1a codon numbering mismatch (Section 3.2 vs. Table 2):** In Table 2, the `NsP3` amplicon (`nt 2949–3212`) is annotated using mature NsP3 peptide coordinates (`aa 76–164`, with `C3037T` labeled `F106F`). In Section 3.2 (page 5), however, `T2987C` and `T3012C` in the same amplicon (`MZ223388`) are annotated using full `ORF1a` polyprotein coordinates (`F908L` and `L916S`), and with a 1-codon shift: in `NC_045512.2`, nt 2987 is the second position of `ORF1a` codon 908 (`CTT`, Leu, corresponding to NsP3 codon 90), whereas Phe (`TTT`) is at `ORF1a` codon 907 (nt 2984–2986, NsP3 codon 89). Check the alignment of `MZ223388` against `NC_045512.2` and report consistent both `ORF1a` and mature `NsP3` coordinates.
  * **GenBank accession count vs. text count:** Section 2.2 lists 14 GenBank accessions (`MZ223385–MZ223398`), whereas Section 3.2 states `"In total, we obtained 15 sequences, including 12 from pre-pandemic cases"` and Table 3 shows 17 `+` PCR cells across 13 patients. Reconcile the exact mapping between the 14 GenBank accessions, the 15 sequences mentioned in the text, and the 17 positive PCR entries in Table 3.
