<Blinded Review: TIME_ANON_0277>
**Composite Score:** 7.1 / 10.0 (Rigor: 2.3/3.5 | Claims: 1.8/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** Algorithmic/Model
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This evolutionary and structural biology study investigates the diversification of the tandemly duplicated primate squamous cell carcinoma antigens *SERPINB3* (*SCCA1*, neutral-protease inhibitor) and *SERPINB4* (*SCCA2*, acidic-protease inhibitor) on human chromosome 18q21.3, alongside six known target cysteine and serine proteases (*CTSS, CTSL1, CTSL2, CTSK, CTSG, CMA1*). Combining wet-lab PCR/Sanger gap-filling of *Gorilla gorilla* *SERPINB3* and *SERPINB4* exons, a 21-tissue human RT-PCR expression screen, maximum-likelihood codon models in PAML v4.6 (`codeml` site models M1a/M2a and M7/M8, plus branch-site models), and homology modeling / flexible protein-protein docking (`MODELLER` + `HADDOCK` Guru interface), the authors identify 17 positively selected sites across the *SERPINB3/B4* gene tree—7 of which map directly into the reactive center loop (RCL, positions P3 `V352F`, P2 `E353G`, P1 `L354S`, P2' `S356P`, P3' `P357T`, P10' `C364H`, and P13' `P367T`)—as well as episodic branch-site positive selection on the Homininae (*Homo, Pan, Gorilla*) *SERPINB3* lineage (`327G, 351G, 352F`) and on the Homininae branch of target protease *CTSS* (`255R`). While the integration of codon evolution, docking energetics, and tissue expression is compelling, applying standard single-tree codon models across tandemly duplicated paralogs without testing for inter-paralog gene conversion or tree discordance introduces an algorithmic caveat.

### 2. Methodological & Statistical Audit
- **Codon Substitution Models on Paralogous Gene Families & Gene Conversion Risk:**
  - *SERPINB3* and *SERPINB4* are 92%-identical tandem duplicates on 18q21.3. In Figure 1B and Table 1, the authors fit site models (M1a vs. M2a, M7 vs. M8) to a single combined tree containing 12 paralogous/orthologous sequences across 9 primate species.
  - Tandemly duplicated multigene families frequently undergo non-allelic homologous recombination / inter-paralog gene conversion (especially across conserved core exons while sparing the hypervariable RCL in exon 8). Gene conversion creates mosaic genealogies across a coding alignment, which is well known to inflate false-positive rates in single-tree `codeml` site and branch-site likelihood ratio tests. Running `GARD` or `GENECONV` to test for recombination breakpoints prior to `codeml` analysis would substantially strengthen the evolutionary inference.
- **Internal Table Inconsistencies & Typographical Errors:**
  - **Table 1 Sequence Count ($N = 9$ vs. 12 Sequences in Tree):** Table 1 lists $N = 9$ for `SERPINB3/B4` (representing 9 primate species), whereas the alignment/tree actually analyzed (Figure 1B and Methods line 50) contains 12 coding sequences (3 *Homininae* `SERPINB3` + 3 *Homininae* `SERPINB4` + 2 *Pongo* + 1 *Macaca* + 1 *Papio* + 1 *Chlorocebus* + 1 *Callithrix*).
  - **Table 3 `CMA1` $p$-value Typo (Line 127):** In Table 3 (Branch-Site test of positive selection on target proteases), row `CMA1` reports `2ΔlnL = 1.14`, `df = 1`, and **`p = 28.58`**. For $\chi^2_1 = 1.14$, the exact tail probability is $p = 0.2857$ (i.e., $28.58\%$). The authors inadvertently entered the percentage `28.58` instead of the probability `0.2858` (or `0.29`).
  - **Gene Symbol Typo (Line 50):** Line 50 lists `CTSLK` instead of `CTSK`.
- **Structural Modeling & HADDOCK Docking:**
  - Using the ovalbumin (`1OVA`) Michaelis complex (`1JTI`) as a template to define ambiguous interaction restraints (AIRs) between the flexible serpin RCL (residues 349–357) and the catalytic triad of each protease in `HADDOCK`, followed by evaluation of `i-RMSD` ($\le 4\text{ \AA}$) and `l-RMSD` ($\le 10\text{ \AA}$) across 200 water-refined models, is a thoughtful computational structural biology workflow.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** Primate *SERPINB3* and *SERPINB4* arose via tandem duplication in the Catarrhini/Hominidae ancestor and experienced strong diversifying selection concentrated in the reactive center loop (RCL) that governs protease target specificity. `[Well Supported]` — Directly supported by both the concentration of non-synonymous substitutions at functional scissile-bond residues (`P3, P2, P1, P2', P3'`) known from prior site-directed mutagenesis and biochemical swapping studies to dictate chymotrypsin/cathepsin G vs. papain-like cysteine protease inhibition, and by the `codeml` BEB posterior probabilities ($>99\%$).
- **Claim 2:** Episodic positive selection acted specifically on the Homininae (*Homo, Pan, Gorilla*) *SERPINB3* lineage (`327G, 351G, 352F`) and coevolved with Homininae *CTSS* (`255R`). `[Moderately Supported]` — The branch-site LRTs are statistically significant ($2\Delta\ln L = 8.40, p = 0.004$ for *SERPINB3*; $2\Delta\ln L = 8.70, p = 0.003$ for *CTSS*), though coevolution with *CTSS* remains correlative and should be tempered by the possibility of inter-paralog gene conversion and the fact that CTSS is exposed to many host and pathogen substrates.
- **Claim 3:** Human *SERPINB3* and *SERPINB4* show distinct tissue expression profiles across 21 normal human tissues, with *SERPINB3* expressed more broadly in esophagus, trachea, lung, prostate, and bladder. `[Well Supported]` — Demonstrated by paralog-specific RT-PCR on a 21-tissue human RNA panel (Figure 4).

### 4. Reproducibility & Data Completeness
- **Strengths:** Complete Ensembl/GenBank accession numbers for all 9 primate species across all 8 genes are provided in Supplemental Table S1; PCR/RT-PCR primer sequences and cycling parameters are provided in Supplemental Table S2; newly sequenced *Gorilla gorilla* *SERPINB3* and *SERPINB4* exons are provided in Supplemental Figure S1; and detailed HADDOCK docking cluster scores and RMSDs are provided in Supplemental Table S3 and Figures S2–S8.
- **Limitations:** Multiple sequence alignments and phylogenetic tree files used as input for PAML are not deposited in an external repository (e.g., Dryad/TreeBASE), though the exact accession numbers allow reconstruction.
</Blinded Review: TIME_ANON_0277>
