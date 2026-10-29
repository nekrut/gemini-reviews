<Blinded Review: TIME_ANON_0309>
**Composite Score:** 8.1 / 10.0 (Rigor: 2.5/3.5 | Claims: 2.1/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.7/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This study provides a comprehensive molecular characterization of the genomic organization, transcription start site (TSS), promoter architecture, alternative splicing, alternative polyadenylation, and non-AUG translation initiation of the human paternally expressed imprinted retrotransposon-derived gene `PEG10`. Using 5'-RACE in `HepG2` and `SH-SY5Y` cells, the authors map the major TSS (`mTSS`) 24 nt downstream of a conserved TATA-box (`TATAAAT`), refining the 5'-end of exon 1 (`GenBank EF437368`) and identifying an alternative splice site (+11 nt in exon 1b, `EF437369`). Sequencing the 2-kb `PEG10` promoter across 10 unrelated individuals reveals three deletion variants (`PPV1`: 31 bp deletion, `EF450773`; `PPV2`: 37 bp deletion, `EF450774`; `PPV3`: 71 bp deletion, `EF450775`) within a polymorphic `CCCCCN` low-complexity repeat upstream of the `mTSS`. Functional dissection of nested promoter-luciferase constructs (`-1910` to `-220` bp) demonstrates that the proximal 220-bp bidirectional region (shared head-to-head with `SGCE`) is sufficient to drive strong transcription, while ectopic `c-MYC` expression represses these upstream promoter constructs. Most importantly, by cloning C-terminally His-tagged `PEG10` cDNA constructs that include the native 5'-UTR and performing site-directed mutagenesis (`mutATG` and `mutCTG`), the authors prove that human `PEG10` initiates translation not only at the previously assumed canonical `AUG` codon in exon 2 (`50 kDa` RF1 product), but predominantly at an in-frame upstream non-AUG `CUG` start codon located 102 nt (`34 amino acids`) upstream (`55 kDa` RF1 and `115 kDa` RF1/2 frameshift products), as well as at a novel upstream `AUG` codon created in the exon 1b splice variant (`PEG10-RF1b/2`, +76 aa N-terminal extension).

The molecular biology and biochemical experiments—particularly the 5'-RACE mapping, discovery of the exon 1b splice variant, site-directed mutagenesis of the `CUG` and `AUG` initiation sites, and comparative N-terminal alignment across mammals showing conservation of the upstream region and absence of the human exon-2 methionine in orthologs (`Figure 11B`)—are rigorous, well controlled, and biologically insightful. Minor methodological limitations include reliance on endpoint semi-quantitative RT-PCR (`25–30` cycles) rather than real-time qRT-PCR for expression comparisons, normalizing luciferase assays via co-transfected `pEYFP-N1` fluorescence without formal statistical hypothesis tests across promoter constructs, and a missing reverse primer (`SGCE-rev`) in `Table 1`.

### 2. Methodological & Statistical Audit
- **Translation Initiation Site (TIS) Mutagenesis and Endogenous Validation (`Figures 7–10`):**
  - The authors noticed that endogenous `PEG10` in `HEK293` and `HepG2` cells migrates at `~55 kDa` and `~115 kDa`, roughly `5 kDa` larger than proteins expressed from conventional ORF-only constructs starting at the exon-2 `AUG` (`~50 kDa` and `~110 kDa`).
  - Including the native 5'-UTR in C-terminally His-tagged `RF1a` and `RF1a/2` constructs reproduced both the `50 kDa` and `55 kDa` bands (`Figure 8`). Site-directed mutagenesis of the canonical `AUG` (`ATG` $\rightarrow$ `TTG`, `mutATG`) selectively abolished the `50 kDa` band while preserving the `55 kDa` and `115 kDa` bands; conversely, mutating the in-frame `-102 nt` `CUG` codon (`CTG` $\rightarrow$ `TTA`, `mutCTG`) selectively abolished the `55 kDa` band while preserving the `50 kDa` band (`Figure 9`). Double mutation (`mutATG/CTG`) eliminated both bands (revealing only a minor downstream cryptic `~40 kDa` product). This is a textbook, definitive demonstration of dual `CUG`/`AUG` translation initiation.
- **5'-RACE, 3'-RACE, and Splice Variant Characterization:**
  - 5'-RACE in two independent cell lines (`HepG2` and `SH-SY5Y`) consistently identified the exact same `mTSS` at a canonical initiator (`Inr`) pyrimidine-purine dinucleotide (`CA`) 24 bp downstream of the conserved `TATAAAT` box (`Figure 2`).
  - Splice-junction cloning (`ABP-F2`/`ABP-R2`) and isoform-specific PCR (`ABP-F2b`/`ABP-R2`) cleanly validated the +11 nt exon 1b alternative 5' splice donor (`GT`), which shifts the reading frame to bring an upstream exon-1 `AUG` codon into frame with `RF1` (`PEG10-RF1b/2`, `76 aa` longer at the N-terminus).
- **Semi-Quantitative RT-PCR and Luciferase Assay Quantification:**
  - Gene expression comparisons across cell lines (`Figure 1`), retinoic acid differentiation of `SH-SY5Y` cells (`Figure 4`), serum starvation (`Figure 6A`), and `c-MYC` overexpression (`Figure 6C`) rely on endpoint semi-quantitative RT-PCR (`25 or 30 cycles`) visualized on ethidium bromide agarose gels, rather than quantitative real-time RT-PCR.
  - In the `Steady-Glo` promoter luciferase assays (`Figure 5`), transfection efficiency was normalized using co-transfected `pEYFP-N1` (100 ng) rather than a dual-luciferase internal Renilla control, and bar graphs present mean ± SD of triplicate wells without formal ANOVA / post-hoc $p$-values. Notably, as the authors themselves point out on line 7, the `-1007` construct showed opposite responses to 0.2% FCS between `Figure 5B` (decrease) and `Figure 5C` (slight increase).
- **Table 1 Audit:**
  - `Table 1` (`lines 64–100`) provides 34 primer sequences, but the last entry lists `SCGE-fwd` (`5'-ATCACATCGGCCCTAGACAG-3'`, note typo `SCGE` for `SGCE`) without the corresponding `SGCE-rev` primer used in `Figure 7`.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *"Translation of PEG10 starts at a CUG codon upstream of the predicted AUG codon... leading to proteins of about 55 kDa (RF1a) and 115 kDa (RF1a/2), as well as the 50 kDa protein translated from the AUG start site."* `[Well Supported]`
  - Conclusively proven by single and double site-directed mutagenesis (`mutATG`, `mutCTG`, `mutATG/CTG`), anti-His and anti-PEG10 immunoblotting in `COS-1`, `HEK293`, and `HepG2` cells, and evolutionary conservation of the upstream N-terminal extension across mammals (`Figure 11B`).
- **Claim 2:** *"Sequencing led to the identification of a novel PEG10 splice variant [exon 1b, +11 nt] creating a new in-frame AUG codon upstream of the CUG codon."* `[Well Supported]`
  - Directly supported by cDNA cloning (`EF437369`), splice-specific RT-PCR across multiple cell lines (`Figure 1B`), and expression of the higher-molecular-weight `RF1b` and `RF1b/2` protein isoforms (`Figure 8B`).
- **Claim 3:** *"Homozygous and heterozygous deletions of 31 bp (PPV1), 37 bp (PPV2) and 71 bp (PPV3) were detected in the PEG10 promoter... and the proximal 220 bp PPV1 promoter is sufficient to drive PEG10 expression."* `[Well Supported]`
  - Supported by genomic sequencing in 10 unrelated individuals (`EF450773–EF450775`) and nested `pGL2-basic` promoter deletion assays (`Figure 5A`).
- **Claim 4:** *"Ectopic c-MYC expression led to an inhibition of all tested PEG10 promoter constructs... and serum deprivation did not reveal enhanced PEG10 expression."* `[Moderately Supported]`
  - The authors transparently report that their upstream promoter and sqRT-PCR results in `HEK293` and `HepG2` cells differ from a prior study reporting c-MYC activation via an intronic E-box in `L02`/cancer cells, providing a balanced and thoughtful mechanistic explanation (`line 9`).

### 4. Reproducibility & Data Completeness
- **Accession Numbers:** All novel transcript, CDS, and promoter sequences are deposited in GenBank under accessions `EF437368` (`PEG10` transcript variant 1), `EF437369` (variant 2, exon 1b), `EF437370`, `EF437371`, `EF450773` (`PPV1`), `EF450774` (`PPV2`), and `EF450775` (`PPV3`).
- **Protocols & Primers:** Cloning strategies, restriction sites, cell culture conditions, mutagenesis primers, and antibody detection methods (`LI-COR Odyssey`) are thoroughly documented; only the missing `SGCE-rev` primer in `Table 1` needs to be appended.
</Blinded Review: TIME_ANON_0309>
