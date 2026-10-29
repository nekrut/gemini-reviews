<Blinded Review: TIME_ANON_0306>
**Composite Score:** 9.1 / 10.0 (Rigor: 3.3/3.5 | Claims: 2.3/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.6/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This study presents an exceptionally thorough evolutionary and mechanistic dissection of `UhpU`, a 3'-UTR–derived small RNA (sRNA) originating from the hexose-6-phosphate transporter gene `uhpT` in *Enterobacteriaceae*. Combining comparative genomics and ancestral state reconstruction (`FastML`) across *Escherichia*, *Salmonella*, *Klebsiella*, and *Citrobacter* with experimental transcriptomics and biochemistry, the authors reconstruct how `UhpU` evolved from a strictly metabolism-coupled, RNase E–processed 3'-UTR fragment into a dual-regulated sRNA possessing its own intragenic $\sigma^{28}$ (`FliA`) promoter.

Specifically, the authors demonstrate that:
1. **Ancestral biogenesis and core regulon:** Across *E. coli*, *S. enterica*, *K. pneumoniae*, and *C. koseri*, growth on glucose-6-phosphate (G6P) strongly induces transcription from the UhpA-dependent `uhpT` promoter (`P_uhpT`), followed by RNase E cleavage (`rne-3071` thermosensitive mutant validation and 5'-monophosphate sensitivity to Terminator 5'-Phosphate-Dependent Exonuclease [`TEX`]) to generate mature `UhpU-S` (`~60 nt`) and `UhpU-L`. Pulse-expression RNA-seq (`GSE298437`), `sfGFP` translational fusions, chromosomal `3xFLAG` Western blots, and $\alpha$-MG sugar-phosphate toxicity assays show that ancestral `UhpU` represses phosphotransferase system (PTS) carbohydrate uptake (`ptsH` in *E. coli*/*K. pneumoniae*/*C. koseri*; `manXYZ` in *S. enterica* where two nucleotide substitutions in `ptsH` disrupted base-pairing), providing protective negative feedback against toxic sugar-phosphate accumulation.
2. **Co-option of horizontally transferred targets (`ygaH'-mprA`):** Following horizontal acquisition of the `ygaZH` efflux operon upstream of `mprAB` in the *Escherichia* ancestor, a variable seed region (`S1`) of `UhpU` established base-pairing (`-17.87 kcal/mol`) within the `ygaH` coding sequence to repress downstream `MprA` translation (`Kd ≈ 250 nM` by EMSA in the presence of `Hfq`), verified by compensatory mutations (`M1`, `M2`, `M3`) and `AlphaFold3` ternary complex modeling (`UhpU–ygaH'mprA–Hfq`).
3. **De novo evolution of an intragenic `FliA` ($\sigma^{28}$) promoter:** After the divergence of *E. coli*/*E. fergusonii*/*Shigella* from *E. albertii*, synonymous mutations within the 3' coding region of `uhpT` created a functional `FliA` `-10` promoter element (`GCCGATAA` vs. ancestral `GCCGGTGA` / *Salmonella* `GCCGGTTA`). Engineering two synonymous point mutations in *E. albertii* (`G1245A`, `G1248A`) or *S. enterica* (`G1245A`, `T1247A`) is sufficient to confer de novo `FliA`-dependent primary transcription (`5'-PPP` resistant to `TEX`, sensitive to 5' polyphosphatase in 5'-RACE) without altering the UhpT amino acid sequence.

### 2. Methodological & Statistical Audit
- **Multi-Layered Orthogonal Experimental Validation:**
  - Every step of the proposed evolutionary trajectory is tested with direct, orthogonal molecular assays:
    - **5'-end phosphorylation state & processing:** Treated vs. untreated `TEX` Northern blots and 5' polyphosphatase–coupled 5'-RACE (`SI Appendix, Fig. S2B`) cleanly distinguish primary transcripts (`5'-PPP`, initiated from `P_fliA` during LB growth) from endonucleolytically processed fragments (`5'-P`, cleaved by RNase E from `P_uhpT` polycistronic transcripts during G6P growth), corroborated by temperature shift in `rne-3071` (`Fig. 1H`) and `Term-seq` 3'-end mapping (`GSE310329`).
    - **Direct sRNA–mRNA base-pairing:** Validated by single and multi-nucleotide point mutations and reciprocal compensatory restores (`UhpU-M1/M2/M3` paired with `ygaH'-mprA-M1/M2/M3` and `ptsH-M`), native EMSAs with purified `Hfq` (`Fig. 3D`, $K_d \approx 250\text{ nM}$), and chromosomal `3xFLAG` Western blots of endogenous `MprA`, `PtsH`, and `ManX` across four bacterial species.
    - **Synthetic evolutionary reconstruction ("gain-of-promoter" experiment):** Mutating just two synonymous nucleotides in *E. albertii* (`P_uhpU-M`: `GCCGGTGA` $\rightarrow$ `GCCGATAA`) and *S. enterica* (`P_uhpU-M`: `GCCGGTTA` $\rightarrow$ `GCCGATAA`) switches on `FliA`-dependent `UhpU-L` transcription (`Fig. 2D, 2E`), directly proving sufficiency of the synonymous substitutions.
- **Statistical Analysis:**
  - Reporter fluorescence (`sfGFP`), qRT-PCR, and motility halo diameters are analyzed across $n = 3$ independent biological replicates using two-tailed unpaired Student's $t$-tests with exact $p$-values reported on figures (`Fig. 2F`, `Fig. 3C, 3E`, `Fig. 4F, 4I`, `Fig. 5E`).
  - RNA-seq differential expression (`DESeq2` on duplicate biological replicates, `|FC| >= 2` for pulse-overexpression and `|FC| >= 1.5` for $\Delta uhpTU$) is appropriately treated as a candidate-generating screen and followed up by Northern blots, Western blots, and translational reporters.
- **Minor Point for Revision:**
  - Detailed wet-lab and bioinformatic protocols (e.g., `FastML` evolutionary model parameters, `DESeq2` version/filtering, `AlphaFold3` confidence metrics such as ipTM/pLDDT for the Hfq-RNA complex) are placed entirely in `SI Appendix` rather than summarized in the main text Materials and Methods (`lines 6–9`). Adding a concise summary of key computational and experimental parameters to the main Methods section would improve standalone readability.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *"UhpU originally evolved as a metabolism-associated sRNA derived from the uhpT 3' UTR via RNase E cleavage, coordinating carbon utilization during hexose phosphate metabolism."* `[Well Supported]`
  - Demonstrated across four *Enterobacteriaceae* genera by G6P-inducible Northern blots, `TEX` susceptibility, `rne-3071` inactivation, and conserved repression of PTS components (`ptsH` / `manXYZ`) protecting against $\alpha$-MG toxicity.
- **Claim 2:** *"As UhpU diversified, its variable seed region co-opted new targets, including horizontally acquired ygaH'mprA, and interacted with flagellar regulator lrhA."* `[Well Supported]`
  - Synteny comparison across 8 species (`Fig. 4A`), compensatory mutagenesis (`Fig. 3C`), Hfq-dependent EMSA (`Fig. 3D`), and endogenous `MprA-FLAG` Westerns (`Fig. 3B, 4C`) conclusively establish co-option of the `ygaH` coding sequence following `ygaZH` insertion.
- **Claim 3:** *"Following divergence from Escherichia albertii, the Escherichia lineage gained an internal FliA promoter, enabling UhpU transcription independently of uhpT."* `[Well Supported]`
  - Ancestral sequence reconstruction (`FastML`), 5'-RACE `TEX`/polyphosphatase assays, and synonymous gain-of-function mutagenesis in *E. albertii* and *S. enterica* (`Fig. 2D, 2E`) provide textbook proof of de novo promoter birth within a coding sequence.

### 4. Reproducibility & Data Completeness
- **Data Availability:** All high-throughput sequencing datasets (pulse-expression RNA-seq, $\Delta uhpTU$ RNA-seq, and Term-seq) are publicly deposited in NCBI GEO under accessions `GSE298437` and `GSE310329`.
- **Reagents & Sequences:** Complete lists of bacterial strains (`Table S3`), plasmids (`Table S4`), and oligonucleotides (`Table S5`) are provided in the `SI Appendix`.
</Blinded Review: TIME_ANON_0306>
