<Blinded Review: TIME_ANON_0903>
**Composite Score:** 6.2 / 10.0 (Rigor: 2.0/3.5 | Claims: 1.6/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.2/2.0)
**Bias Category:** Over-Interpretation/Clinical
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Translational/Preclinical/Biomarker

OVERALL_SCORE: 6.2/10
VERDICT: PASS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
`TIME_ANON_0903` conducts quantitative trait locus (`QTL`) mapping and fine-mapping of grain protein content (`GPC`) in bread wheat (*Triticum aestivum*) using a 198-line recombinant inbred line (`RIL`) population derived from a cross between the Canadian elite cultivar `TAA10` (`AABBDD`) and the resynthesized hexaploid wheat `XX329` (`AABBDD`, carrying the D genome of *Aegilops tauschii* subsp. *strangulata* accession `TQ18` and the AB genome of `TAA10`). Evaluating GPC across 6 field environments (`2020–2021` and `2021–2022` across Hebei, Henan, and Beijing) plus best linear unbiased predictions (`BLUPs`), the authors report:
1. **Primary QTL detection on chromosomes 2D, 4D, and 7D (`Table 4`):** Using an 822-marker D-genome genetic map (`2,535.9 cM`) and inclusive composite interval mapping (`ICIM` in `QTL IciMapping v4.2`), the authors detect three multi-environment QTLs: `QGpc.cau-2D` (detected in 4 environments + BLUP, `LOD = 2.66–9.82`, `PVE = 5.47–17.28%`, positive allele from `XX329`), `QGpc.cau-4D` (3 environments + BLUP, `LOD = 3.91–5.59`, `PVE = 8.32–12.65%`, positive allele from `TAA10`), and `Qgpc.cau-7D` (2 environments + BLUP, `LOD = 3.16–3.87`, `PVE = 6.91–8.05%`, positive allele from `TAA10`).
2. **Fine-mapping of `QGpc.cau-2D` via residual heterozygous lines (`RHL-124`):** Using `F8` progeny of `RHL-124` heterozygous across `Xcau-2D531`–`Xcau-2D577` (`13.6–37.6 Mb` on `IWGSC RefSeq v2.1`), the authors develop 5 additional InDel markers (`Xcau-2D778` to `Xcau-2D782`), categorize `1,004` `F8` and `2,592` `F9` plants into 10 homozygous recombinant families (`Fig. 3c–d`), and narrow `QGpc.cau-2D` to a `4.2 Mb` physical interval between `Xcau-2D541` (`16.0 Mb`) and `Xcau-2D781` (`20.2 Mb`).
3. **Candidate gene screening:** Within the `4.2 Mb` interval (`134` high-confidence genes), whole-genome resequencing of `TAA10` and `XX329` identifies coding SNPs/InDels in 11 spike/grain-expressed genes, and qRT-PCR of 22 promoter-polymorphic genes identifies 3 differentially expressed genes (`TraesCS2D03G0077200`, `TraesCS2D03G0086500`, `TraesCS2D03G0087700`).

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES

#### STRENGTHS
- **Clean near-isogenic D-genome genetic background (`TAA10` $\times$ `XX329`):** Because `XX329` shares `98.84%` AB-genome identity with `TAA10`, variation in the 198 RILs predominantly reflects D-genome introgressions from *Ae. tauschii* `TQ18`, increasing power to map D-subgenome QTLs without major AB-subgenome confounding.
- **Multi-environment RHL fine-mapping (`Fig. 3c–d`):** Advancing heterozygous `RHL-124` derivatives into homozygous recombinant `F9` families (`n = 10` recombinant types) and evaluating them with paired homozygous non-recombinant sibling controls across 5 field environments provides robust phenotypic validation that reduces the `24 Mb` primary interval to `4.2 Mb`.
- **Transparent test of pleiotropy with thousand-grain weight (`TGW`) (`Fig. S1`):** Because GPC increases are often passive concentration artifacts of reduced starch/grain weight, the authors explicitly measure `TGW` in the `NIL^{XX329}` vs. `NIL^{TAA10}` pairs across 4 environments (`Fig. S1`), demonstrating that `QGpc.cau-2D` increases GPC by `2.07–4.35%` without significantly reducing `TGW` in 3 of 4 environments.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Text-vs-Table discrepancy for `QGpc.cau-4D` phenotypic variance explained (`PVE`):** On page 5 (Results, *QTL mapping of GPC*), the text states that `QGpc.cau-4D` explained *"7.22%-11.59% of the phenotypic variation"*, whereas `Table 4` directly below reports `PVE` values for `QGpc.cau-4D` of `10.17%`, `12.65%`, `10.97%`, and `8.32%` (`8.32%–12.65%`).
- **Omitted heritability formula and incomplete ANOVA table (`Table 2`):** In the Methods section (*Data analysis*, page 3), the text states *"broad-sense heritability ($H^2$) across environments were calculated using the following formula:"* followed by a completely blank space where the equation was omitted. Furthermore, `Table 2` reports `df` and Mean Squares for `Genotype (G)` (`df = 197`), `Environment (E)` (`df = 5`), and `G x E` (`df = 985`), but omits the residual `Error` row (`MS_e` and `df_e`), preventing verification of the $F$-statistics and how $H^2 = 0.85$ was computed (using $1 - MS_{G\times E}/MS_G = 1 - 0.56/3.94 = 0.858$).
- **Inconsistent recombinant line identifiers between Methods/Text and `Fig. 3d`:** The Methods (page 2) and Results (page 5) list the 10 homozygous recombinant lines as `124-15-9`, `124-61-97`, `124-65-22`, `124-116-59`, `124-137-27`, `124-138-15`, `124-164-181`, `124-185-169`, `124-187-73`, and `124-199-56`, whereas `Fig. 3d` labels two of those lines as `124-61-67` (instead of `124-61-97`) and `124-164-184` (instead of `124-164-181`).
- **Contradictory candidate gene prioritization in Discussion vs. Results:** In the Discussion (page 9), the authors conclude that 4 genes—`TraesCS2D03G0077200`, `TraesCS2D03G0086500`, `TraesCS2D03G0080700`, and `TraesCS2D03G0079200`—are the primary candidates for `QGpc.cau-2D`. However:
  1. In the Results (page 7), `TraesCS2D03G0080700` was explicitly shown to have **no significant expression difference** between `NIL^{TAA10}` and `NIL^{XX329}`, while `TraesCS2D03G0087700` *did* show a significant expression difference (`Fig. 4c`, `p < 0.05` at 15 and 20 DPA)—indicating that the authors confused `TraesCS2D03G0080700` with `TraesCS2D03G0087700` in the Discussion!
  2. `TraesCS2D03G0079200` contains only 2 **synonymous** SNPs (`Table S4`) and no differential expression was demonstrated, making its elevation to a top causal candidate speculative.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim that `QGpc.cau-2D` maps to a `4.2 Mb` physical interval (`16.0–20.2 Mb`) on chromosome 2D where the *Ae. tauschii* allele increases GPC without a consistent TGW penalty** `[Well Supported]`: Strongly supported by multi-environment RIL mapping, `RHL-124` fine-mapping across 10 recombinant classes (`Fig. 3d`), and `TGW` NIL comparisons (`Fig. S1`).
- **Claim that `TraesCS2D03G0077200`, `TraesCS2D03G0086500`, `TraesCS2D03G0080700`, and `TraesCS2D03G0079200` are the primary causal candidates** `[Overstated]`: `134` high-confidence genes reside in the `4.2 Mb` interval, no loss-of-function or transgenic validation was performed, and `TraesCS2D03G0080700` was mistakenly substituted for `TraesCS2D03G0087700` in the Discussion.

### 4. Reproducibility & Data Completeness
- **Data Availability:** Moderate (`1.2/2.0`). Marker positions, LOD scores, PVE, additive effects (`Table 4`), and reference genome coordinates (`IWGSC RefSeq v2.1`) are reported, while primer sequences (`Table S2`), coding variants (`Table S4`), and raw RIL genotypes are referenced in supplementary files; however, no NCBI SRA accession is provided for the parental whole-genome resequencing reads (`10x` coverage of `TAA10` and `XX329`).
</Blinded Review: TIME_ANON_0903>
