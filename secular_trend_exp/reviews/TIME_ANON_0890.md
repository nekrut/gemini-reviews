<Blinded Review: TIME_ANON_0890>
**Composite Score:** 8.6 / 10.0 (Rigor: 3.1/3.5 | Claims: 2.3/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 8.6/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This evolutionary and functional genetics study investigates the molecular basis of the classical canine white spotting locus ($S$: Solid $S$, Irish spotting $s^i$, Piebald $s^p$, and Extreme white $s^w$) at the *MITF* (microphthalmia-associated transcription factor) gene on dog chromosome 20. Building on prior fine-mapping of a 100 kb non-coding region that identified four candidate variants—a `SINEC-Cf` insertion ($\sim 3.1\text{ kb}$ upstream of the *MITF-M* TSS), `SNP#21` ($\sim 1.2\text{ kb}$ upstream), a complex mononucleotide repeat length polymorphism `Lp` ($\text{C}_X\text{A}_Y\text{G}_2\text{A}_Z$, $\sim 100\text{ bp}$ upstream of the *MITF-M* TSS), and a 12-bp deletion in exon 1B (`Exon1B_del`)—the authors screen 60 geographically diverse gray wolves (verified as pure wolves via low *AMY2B* diploid copy number, $\text{CN}=2$) and 206 dogs across 17 breeds, and perform systematic Dual-Luciferase reporter assays in human `624mel` melanoma cells. They demonstrate that: (1) all four white-spotting-associated variants occur in wild wolves, proving that none can act alone as a recent derived mutation sufficient for extreme white spotting, and supporting a multi-site haplotype ("evolution of alleles") model; (2) the `Lp` repeat exhibits high diversity in wolves (15 alleles in 17 wolves) with direct haplotype sharing between wolves and white-spotted dogs (`32B+`, `35A+`, `35B+`, `35D-`), but zero overlap between wolves and solid ($S/S$) dogs (`29A-`, `31A-`, `32A-`), indicating strong selection for short `Lp` alleles to maintain solid coat color during domestication; and (3) `LpWhite` alleles (from Boxer $s^w$, Dalmatian $s^w$, and Bernese Mountain Dog $s^i$) consistently reduce *MITF-M* promoter activity compared to `LpSolid` (and wolf disrupted-repeat `34A`), strictly dependent on an upstream 128-bp enhancer cluster containing four SOX10, one PAX3, and three LEF1 binding sites, whereas site-directed mutagenesis of `SNP#21` has no effect and `SINEC-Cf` acts as an additive weak repressor.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### STRENGTHS
- **Clever evolutionary falsification via ancestral wolf screening with *AMY2B* introgression control:** Screening 60 wolves across Eurasia and North America (and verifying $\text{CN}=2$ at *AMY2B* to rule out recent dog admixture) decisively falsifies the hypothesis that `SINEC-Cf` or individual `Lp` alleles are derived dog-specific loss-of-function mutations.
- **Rigorous handling of mononucleotide repeat PCR stutter:** Because the $\text{C}_X\text{A}_Y\text{G}_2\text{A}_Z$ repeat suffers from polymerase slippage during PCR, the authors amplified with high-fidelity KOD Hot Start polymerase, subcloned into `pCR-Blunt II-TOPO`, sequenced multiple clones per individual, and cross-verified exact insert sizes by capillary fragment analysis (`MegaBACE`) both before and after ligation into the `pGL3-Basic` luciferase vector.
- **Mechanistic promoter dissection and site-directed mutagenesis:** Rather than testing a single promoter fragment, the authors test factorial combinations of `SINE`/`noSINE` $\times$ `LpWhite`/`LpSolid` (Fig. 3B), perform site-directed mutagenesis of `SNP#21` (`A` $\to$ `G`) to eliminate LD confounding between `SNP#21` and `Lp` (Fig. S1), truncate the promoter into three nested constructs (`Promoter 1–3`, Fig. 3C) to prove that `Lp` length only affects transcription when the upstream 128-bp SOX10/PAX3/LEF1 cluster is present (supporting a DNA helical phasing / half-turn cooperativity model between upstream SOX10/PAX3/LEF1 and downstream PAX3/TATA), and test five distinct natural `Lp` alleles from dogs and wolves (Fig. 4).

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Heterologous human melanoma cell line (`624mel`) and absence of `Exon1B_del` functional assay:** Reporter assays were performed in human `624mel` melanoma cells rather than primary canine neural crest melanoblasts, and the 12-bp coding deletion in exon 1B (`Exon1B_del`) was not functionally assayed at the protein/isoform level (though the authors appropriately note this limitation and cite CanFam3.1 RNA-seq evidence confirming exon 1B transcription).
- **Incomplete genomic interval in combined SINE+Lp reporter constructs:** As noted in the Figure 3A legend, the intervening region from $-1400$ to $-2800\text{ bp}$ upstream of the *MITF-M* promoter was omitted when ligating the $-3150\text{ bp}$ `SINEC-Cf` fragment upstream of the *MITF-M* promoter in `pGL3-Basic`, altering the native genomic distance between the SINE and the TSS.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** None of the four candidate polymorphisms (`SINEC-Cf`, `SNP#21`, `Lp`, `Exon1B_del`) is the sole causal mutation for extreme white spotting, as all four occur in wolves or fail to perfectly cosegregate across breeds; instead, canine white spotting alleles represent multi-mutation haplotypes ("evolution of alleles"). `[Well Supported]` — Conclusively established by the wolf and multi-breed genotype tables (Tables 1–2, Table S2).
- **Claim 2:** The `Lp` repeat polymorphism is a primary functional regulator of *MITF-M* promoter activity, likely by altering DNA helical phasing ($\sim 4\text{ bp} \approx 0.4$ helical turns) between the upstream SOX10/PAX3/LEF1 cluster and downstream core promoter elements, and short `LpSolid` alleles were selected during domestication to produce solid-colored dogs. `[Well Supported]` — Compellingly supported by both the median-joining haplotype network (Fig. 2) and the promoter truncation / multi-allele luciferase series (Figs. 3C and 4).
- **Claim 3:** `SNP#21` has no detectable effect on *MITF-M* promoter activity in vitro, while the `SINEC-Cf` region acts additively to reduce reporter activity. `[Well Supported]` — Directly demonstrated by site-directed mutagenesis (Fig. S1) and factorial reporter constructs (Fig. 3B).

### 4. Reproducibility & Data Completeness
- **Genomic Coordinates & Primers:** Exact genomic coordinates, repeat compositions ($\text{C}_X\text{A}_Y\text{G}_2\text{A}_Z$), wolf sample metadata (`Table S1`), breed frequencies (`Table S2`), and cloning/mutagenesis primers (`Table S3`) are thoroughly documented.
</Blinded Review: TIME_ANON_0890>
