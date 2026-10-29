<Blinded Review: TIME_ANON_0906>
**Composite Score:** 8.9 / 10.0 (Rigor: 3.2/3.5 | Claims: 2.3/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Translational/Preclinical/Biomarker

OVERALL_SCORE: 8.9/10
VERDICT: PASS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary / SUMMARY
`TIME_ANON_0906` is a landmark human transplant immunology and statistical genetics study that identifies the first autosomal HLA class II–restricted minor histocompatibility antigen (`mHag`) selectively expressed on normal and malignant B-lineage cells—encoded by a nonsynonymous SNP (`rs2904880`, `c.571G>C`, `Val174Leu`, designated `CD19^L`) in the B-cell co-receptor gene *CD19*—and introduces a generalizable statistical genetics framework ("zygosity-genotype correlation" implemented in `ssSNPer`) for genome-wide fine-mapping of T-cell epitopes using International HapMap CEPH pedigrees. Specifically:
1. **Isolation and HLA restriction of $\text{CD4}^+$ T-cell clone 21:** Isolated from a multiple myeloma (`MM`) patient who achieved sustained complete remission after relapsing post-allo-SCT and receiving donor lymphocyte infusions (`DLI`) plus $\alpha\text{-IFN}$, $\text{CD4}^+$ T-cell clone 21 specifically recognizes recipient `EBV-LCL` (`IFN-`\gamma ELISA and `CFSE` proliferation) restricted by `HLA-DQA1*05/B1*02` (`Fig. 1`).
2. **Two-point linkage + `ssSNPer` zygosity-genotype fine-mapping (`Fig. 2`):** Phenotyping `HLA-DQA1*05/B1*02`–transduced `EBV-LCLs` from 4 large three-generation CEPH pedigrees (`n = 48` individuals) followed by `Merlin` two-point linkage (`LOD = 6.968` at `D16S401`/`D16S3113`) localized the mHag to a `16.3-Mbp` region on `16p11.2-p12.3`. To avoid testing 119 genes, the authors inferred exact mHag genotypes (`+/+`, `+/-`, `-/-`) for 29 CEPH family members from Mendelian segregation and correlated those inferred zygosities (`r^2`) against all HapMap Phase II SNPs (`~4 x 10^6`) via `ssSNPer`, identifying a single `14.5-kb` LD block (`r^2 = 1.0`, `p = 7.45 x 10^{-9}`) spanning the B-cell–specific gene *CD19* (`Fig. 2 B–C`).
3. **Epitope proof (`CD19^L`, `WEGEPPCLP`):** Genotyping `rs2904880` across 51 HLA-matched donors confirmed `100%` concordance (`19/19` `CC`/`GC` positive vs. `0/32` `GG` negative), retroviral transduction of `CD19^L` (`pLZRS-CD19^L`) into `CD19^V` donor `EBV-LCL` conferred recognition (`Fig. 3A`), and overlapping peptide mapping localized the minimal 9-mer core epitope to `WEGEPPCLP` (`aa 167–175`, with `Leu174` at the C-terminal P9 anchor; `Fig. 3B`).
4. **Functional helper and direct cytolytic anti-leukemia activity (`Figs. 4–5`) + clinical in vivo correlation (`Fig. 6`):** Clone 21 licenses immature DCs to secrete `IL-12` (`Fig. 4B`), amplifies expansion of `LRH-1`–specific $\text{CD8}^+$ CTLs (`Fig. 4C`), directly lyses primary `CD19^L+` chronic lymphocytic leukemia (`B-CLL`) blasts (`60–65%` lysis) via `granzyme B` (`Fig. 5`), and expands dynamically (`4.2 x 10^{-2}`) in vivo following `DLI` coincident with `>90%` drop in serum paraprotein (`Fig. 6`).
5. **Genome-wide retrospective validation and power simulation (`Fig. 7`, `Table I`, `Fig. S2`):** The authors retrospectively map 6 previously known mHags (`HA-1`, `HA-2`, `HA-8`, `HB-1`, `ACC-1`, `ACC-2`) genome-wide using only 10–14 CEPH trios (`p = 3.9 x 10^{-8}` to `7.7 x 10^{-12}`) and simulate 149 random HapMap SNPs across varying allele frequencies (`MAF 0.05–0.90`) and `10%` phenotyping error rates to establish sample-size thresholds (`15–30` trios).

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES

#### STRENGTHS
- **Mathematical elegance of `ssSNPer` zygosity-genotype correlation:** Standard binary association on a dominant T-cell recognition phenotype (`mHag+` vs. `mHag-`) confuses heterozygotes (`+/-`) with homozygotes (`+/+`), losing substantial information when the minor allele frequency is moderate (`p ~ 0.3–0.6`). By deducing exact three-state zygosities (`+/+`, `+/-`, `-/-`) in CEPH parent-offspring trios before computing Pearson's $r^2$ against HapMap genotypes, the authors gain massive statistical power, reducing the required sample size from $>50$ unrelated individuals to `10–20` CEPH trios (`Fig. 7`).
- **Rigorous simulation of real-world experimental phenotyping errors (`Fig. S2`):** Rather than assuming error-free cellular assays, the authors explicitly simulate a `10%` false-negative/false-positive phenotyping error rate across 149 HapMap SNPs, demonstrating how false-negative errors in parents (`+/-` misclassified as `-/-`) vs. offspring impact the genome-wide discovery rate (`>85%` for `AF <= 0.50` in 30 trios).
- **Complete chain of immunological proof:** From clinical T-cell isolation, linkage + HapMap fine-mapping, cDNA transduction, and minimal peptide truncation (`WEGEPPCLP`) to DC licensing, $\text{CD8}^+$ CTL help, granzyme B–mediated primary `B-CLL` tumor lysis, and longitudinal patient TaqMan PCR tracking (`Fig. 6`), every link is experimentally verified.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Paradox of `CD19^L` T-cell expansion in a `CD19-` multiple myeloma patient:** As the authors candidly discuss on page 2033, malignant plasma cells in multiple myeloma (`MM`) typically lose surface `CD19` expression. While the authors hypothesize that `CD19^L`-specific $\text{CD4}^+$ T cells targeted either a putative `CD19+` clonogenic MM stem/progenitor population or provided bystander help via host `CD19+` B cells/APCs to class I–restricted CTLs (`LRH-1`), primary `MM` bone marrow plasma cells from the index patient were unavailable to test direct `CD19^L` expression or lysis.
- **No explicit multiple-testing threshold adjustment reported for the 4-million-SNP genome-wide scan in `Table I`:** While the observed p-values in `Table I` (`7.7 x 10^{-12}` to `3.9 x 10^{-8}`) all pass the canonical Bonferroni genome-wide significance threshold ($p < 0.05 / 10^6 = 5 \times 10^{-8}$), the text sets an arbitrary operational cutoff of $r^2 > 0.75$ rather than deriving an explicit family-wise error rate (`FWER`) threshold.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim that `rs2904880` (`Val174Leu`) in *CD19* encodes the `HLA-DQA1*05/B1*02`–restricted mHag `CD19^L` (`WEGEPPCLP`)** `[Well Supported]`: Unambiguously proved by linkage (`LOD = 6.97`), `ssSNPer` (`r^2 = 1.0`), 51-donor genotyping (`100%` concordance), retroviral `CD19^L` transduction, and synthetic peptide titration (`EC50 ~ 150 nM`).
- **Claim that `CD19^L`-specific $\text{CD4}^+$ T cells provide both DC-mediated helper activity and direct granzyme B–dependent cytolysis of `CD19^L+` B-cell malignancies (`B-CLL`)** `[Well Supported]`: Directly demonstrated by `IL-12` ELISA, `LRH-1` $\text{CD8}^+$ T-cell co-culture, `CFSE` cytotoxicity assays on primary `B-CLL`, and `EGTA`/`z-VAD-fmk`/`concanamycin A` inhibitor dissection (`Figs. 4–5`).
- **Claim that `ssSNPer` zygosity-genotype correlation enables genome-wide mHag identification using 15–30 CEPH trios** `[Well Supported]`: Proved retrospectively on 6 known mHags (`Table I`) and across 149 simulated HapMap loci (`Fig. 7`, `Fig. S2`).

### 4. Reproducibility & Data Completeness
- **Reproducibility and Tool Availability:** Exceptional (`1.5/2.0`). The authors deployed a public web tool (`www.ssSNPer.org`) with GNU GPL source code, reported exact CEPH family IDs (`1331`, `1347`, `1362`, `1416`), SNP rsIDs (`rs2904880` and all correlated SNPs in `Table I`), primer/probe sequences for `Clonotypic` `TCRBV7S3` TaqMan PCR (`Forward`, `Reverse`, `Probe`), and retroviral cloning primers.
</Blinded Review: TIME_ANON_0906>
