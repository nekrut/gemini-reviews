<Blinded Review: TIME_ANON_0580>
**Composite Score:** 8.8 / 10.0 (Rigor: 3.1/3.5 | Claims: 2.2/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.6/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 8.8/10
VERDICT: PASS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary (SUMMARY)
This primary experimental yeast genetics and chromosome biology study systematically characterizes the five-subunit condensin complex in *Saccharomyces cerevisiae* (`SMC2`, `SMC4`, `BRN1`, `YCS4` [`YLR272c`], and `YCS5` [`YDR325w`]). The authors demonstrate by gene disruption and tetrad dissection that all five subunits are essential for viability, even in strains lacking the chromosomal rDNA tandem array (`rdn1-\Delta\Delta` supported by a plasmid-borne rDNA repeat), and show via epitope tagging, quantitative immunodepletion, and peptide-eluted immunoaffinity purification that the five proteins assemble into a stoichiometric 1:1:1:1:1 complex throughout the cell cycle (Fig. 1). Using newly generated temperature-sensitive alleles (`smc2-8` and `smc4-1`), LacO/LacI-GFP chromosome tagging, multiprobe FISH area segmentation on chromosome VIII and rDNA (Fig. 3), live-cell `Smc4p-GFP` imaging (Fig. 4), half-sector chromosome loss assays on a chimeric chromosome III carrying a translocated rDNA array controlled against 200-kb and 900-kb YACs (Fig. 5), and 21-probe chromatin immunoprecipitation (ChIP) across the 9.1-kb rDNA repeat (Fig. 6), the authors establish that budding yeast condensin concentrates in the nucleolus at G2/M, binds specific sites within the rDNA repeat, and is specifically required to condense and segregate the tandem rDNA array during anaphase. The study is a model of orthogonal genetic, cytological, and biochemical validation; minor limitations are restricted to the absence of replicate error bars on the semi-quantitative ChIP densitometry profiles and reliance on "data not shown" for several secondary controls.

### 2. Methodological & Statistical Audit (WEAKNESSES & METHODOLOGICAL AUDIT)
* **Absence of Replicate Dispersion Metrics in ChIP Densitometry (Figure 6D–E) and FISH Area Bar Graphs (Figure 3B, D):** In Figure 6D–E, ChIP PCR signals across the 21 rDNA probes for `Smc2p-HA` and `Ycs5p-HA` in $\alpha$-factor (G1) and nocodazole (G2/M) arrested cells were quantified by ImageQuant volume scans normalized to probe 12 and input DNA. However, the plots present single point profiles without error bars, biological replicate counts, or quantitative real-time PCR (qPCR) linear-range verification (though the authors note a 1:50 template dilution was used for rDNA PCR relative to single-copy loci). Similarly, the sample sizes ($n$ of nuclei) and statistical test $p$-values for the normalized FISH area measurements in Figure 3B and 3D are not stated in the main text.
* **Reliance on "Data Not Shown" / "Unpublished Observations" for Secondary Claims:** Several supporting statements—including negative Western blots of condensin immunoprecipitates for Hmo1p, Smc1p, Mcd1p, and Top2p (Fig. 1B legend), normal sister chromatid cohesion in `smc2-8` and `smc4-1` (line 133), ChIP binding of condensin to pericentromeric and peritelomeric non-rDNA sites (line 10 of chunk 2), and lack of effect of `sir2` and `net1` mutations on condensin targeting (Discussion)—are cited as "data not shown" or "unpublished observations."

### 3. Biological / Experimental Grounding & Claim Proportionality (STRENGTHS)
* **Identification and 1:1:1:1:1 Stoichiometric Purification of the Budding Yeast Condensin Complex: `[Well Supported]`**  
  Complete codepletion of Smc4p upon saturating Smc2p-HA immunoprecipitation (Fig. 1C), proportional co-precipitation of Smc2p/Smc4p across HA-tagged Brn1p, Ycs4p, and Ycs5p (Fig. 1D), and silver-stained peptide elution of the five-subunit complex from 10 g of Ycs5p-HA cells alongside an untagged mock control (Fig. 1E) rigorously establish complex composition.
* **Requirement of `SMC2` and `SMC4` for Establishment of Mitotic Chromosome Condensation: `[Well Supported]`**  
  Synchronous release from G1 ($\alpha$-factor at 23°C) into nocodazole at 37°C followed by normalized FISH area segmentation of both the rDNA array and a 230-kb painted region of chromosome VIII (Fig. 3A–D) demonstrates a clear defect in establishing mitotic compaction in `smc2-8` and `smc4-1` mutants.
* **G2/M Nucleolar Relocalization of Condensin Dependent on the Chromosomal rDNA Array: `[Well Supported]`**  
  Live-cell imaging of endogenously integrated, fully functional `Smc4p-GFP` reveals cell-cycle-regulated concentration into a peripheral subnuclear crescent at G2/M that colocalizes with `Net1p-MYC` and `Sir2p-GFP` and disappears completely into a diffuse nuclear pattern in strain `NOY891` (`rdn1-\Delta\Delta`) lacking chromosomal rDNA repeats (Fig. 4A–E).
* **Specific Requirement of Condensin for Mitotic Segregation and Stability of rDNA-Bearing Chromosomes: `[Well Supported]`**  
  The combination of live `Sir2p-GFP` vs. `LacO/LacI-GFP` (`ura3` and `ade8`) segregation assays (showing stalled rDNA separation while chromosome IV and V arms separate, Fig. 5A–C) and the half-sector chromosome loss assay on chromosome III carrying a translocated rDNA array ($4.6 \times 10^{-2}$ and $2.4 \times 10^{-2}$ loss per division in `smc2-8` and `smc4-1` vs. $<3.4 \times 10^{-5}$ in wild type, Fig. 5D–F), alongside the 200-kb vs. 900-kb YAC length control (Fig. 5G), provides an exceptionally tight genetic proof that rDNA repeat architecture—rather than chromosome length alone—renders chromosomes sensitive to condensin loss.

### 4. Reproducibility & Data Completeness
* **Comprehensive Strain, Plasmid, and Primer Documentation:** Table 1 lists all 33 yeast strains with complete genotypes, and the Materials and Methods section provides full oligonucleotide sequences for gene disruptions (`brn1-\Delta`, `ycs4-\Delta`, `ycs5-\Delta`), `12His-3HA` epitope tagging, and `ADE2` chromosome III marking, as well as ATCC cosmid clone numbers (`C9315`, `C8179`, `C9666`, `C9925`, `C8025`, `C8082`, `C9205`).
* **Missing ChIP Primer Sequences:** While Figure 6C maps the 21 rDNA ChIP PCR probes graphically, the exact primer sequences for the 21 rDNA amplicons are not listed in Materials and Methods and should be included in a supplementary table.
</Blinded Review: TIME_ANON_0580>
