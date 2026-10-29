<Blinded Review: TIME_ANON_0706>
OVERALL_SCORE: 8.4/10
VERDICT: PASS
ESTIMATED_DECADE: 2000s
**Composite Score:** 8.4 / 10.0 (Rigor: 2.9/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.7/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### SUMMARY
### 1. Executive Summary
This evolutionary genomics and molecular microbiology study investigates positive selection and geographic differentiation across the *Helicobacter pylori* Sel1-like repeat (`slr` / `hcp`, COG0790) secreted protein family (`hp0160`, `hp0211`, `hp0235`, `hp0519`, `hp0628`, and `hp1117`). Prompted by subtractive hybridization and PCR genotyping of 162 strains (87 Japanese, 28 Korean, 47 Spanish) showing an abrupt frequency inversion of two in-frame indels (`Δ24 15+` vs. `24+ Δ15`) in `hp0519` between Japanese (70/87 `Δ24 15+`) and Korean (24/28 `24+ Δ15`) isolates, the authors sequence internal (`n = 78`) and full-length (`n = 27`) `hp0519` alleles alongside five additional `slr` genes (`n >= 32` strains from East Asia, Europe, and Africa), flanking genes `hp0518` and `hp0520`, and six housekeeping genes (288 sequences total, GenBank `EF372636`–`EF372923`). Using McDonald-Kreitman tests, PAML 3.14 codon site, branch, and branch-site models (including star-phylogeny and Datamonkey `SLAC`/`FEL` controls for recombination), homology modeling on crystal structures `1KLX` (`HcpB`) and `1OUV` (`HcpC`), and *E. coli* signal-peptide secretion assays, they demonstrate that (1) `slr` paralog expansion in *Helicobacter* involved episodic positive selection, (2) five of six `slr` genes (all except `hp0628`) exhibit surface-localized positively selected residues, and (3) `hp0519` underwent a dramatic, locus-specific adaptive divergence between Japanese and Korean populations whereas housekeeping genes, flanking genes (`hp0518`, `hp0520`), and all other `slr` genes remain intermingled between Japan and Korea.

### STRENGTHS
- **Flanking-Gene and Housekeeping-Gene Controls Rule Out Demographic Confusion and Hitchhiking:** Showing that Japanese and Korean isolates are intermingled in six concatenated housekeeping genes (`Fig. S2B`) and in five other `slr` genes (`Figs. S4–S8`), AND that the immediately adjacent genes `hp0518` and `hp0520` (`Fig. S2A`) show no Japanese-Korean split, provides compelling proof that the `hp0519` divergence reflects locus-specific selection rather than genome-wide population structure or hitchhiking on a neighboring locus.
- **Orthogonal Tests of Positive Selection and Recombination Sensitivity:** Because high homologous recombination in *H. pylori* can inflate false positives in tree-based codon models, the authors corroborate PAML site/branch-site models (`M2/M3/M7/M8`, `M2JM2/M2JM3`) with tree-independent McDonald-Kreitman tests (48/8 fixed vs. 68/42 polymorphic between Japan and Korea, $p < 0.001$), star-phylogeny re-estimation (`Table S6C`), and `SLAC`/`FEL`.
- **Structural Mapping and Wet-Lab Secretion Verification:** Positively selected residues are mapped onto homology models anchored on empirical crystal structures of paralogs `Hp0336` (`1KLX`) and `Hp1098` (`1OUV`), and N-terminal signal peptide-dependent secretion of `Hp0519-FLAG` is verified experimentally (`Fig. S3`).

### WEAKNESSES & METHODOLOGICAL AUDIT
### 2. Methodological & Statistical Audit
- **Infinite / Extreme $\omega$ Point Estimates ($\omega_J > 25$, $\omega = \infty$) on Short Branches with $d_S \approx 0$:** On the ancestral Japanese `hp0519` branch and several terminal/internal branches in the free-ratio (`FR`) trees (`Fig. 1B`, `Fig. 3A`), $d_S$ is zero or near-zero, causing the maximum-likelihood point estimate of $\omega = d_N / d_S$ to blow up ($\omega_J > 20$ or $\omega = \infty$). Additionally, the early PAML 3.14 branch-site tests (`M2JM2` vs. `M1` and `M2JM3` vs. `M3`, following Yang & Nielsen 2002) compare against null models that assume homogeneous selection across branches and were later shown by Zhang, Nielsen & Yang (2005) to be susceptible to false positives under relaxed constraint or branch rate heterogeneity. Fortunately, the two-ratio branch test (`M2J` vs. `M0`, $\omega_J = 1.6$, $p < 0.0001$) and the non-parametric McDonald-Kreitman test ($p < 0.001$) independently confirm positive selection on the Japanese `hp0519` lineage.
- **Minor LRT Arithmetic Typo:** In line 44, comparing `-lnL(FR) = 11286.639` and `-lnL(M0) = 11356.182` gives $2 \Delta \ln L = 2 \times (11356.182 - 11286.639) = 139.086$, which is slightly misstated as `χ² = 140.062` (with $df = 47$, both yield $p < 0.00001$).
- **Secretion Tested in Heterologous *E. coli* Rather Than *H. pylori*:** The `Hp0519-FLAG` C1/C2 constructs (`Fig. S3`) demonstrate Sec-dependent export across the *E. coli* envelope into culture supernatant, which confirms a functional signal peptide (transport to the periplasm) plus outer-membrane leakage in *E. coli* BL21(DE3), though native extracellular secretion vs. periplasmic localization in *H. pylori* was not directly assayed.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1 (Five of six widely conserved *H. pylori* `slr` genes evolve under positive selection at surface-exposed loop residues, whereas `hp0628` is under purifying selection): `[Well Supported]`** — Consistently supported across `M7/M8` site models, star-tree controls, and structural homology models.
- **Claim 2 (`hp0519` alleles underwent strong, locus-specific adaptive divergence between Japanese and Korean *H. pylori* populations): `[Well Supported]`** — Strongly supported by PCR indel typing ($n = 162$), internal SNP sequencing ($n = 78$), full-length sequencing ($n = 27$), McDonald-Kreitman test ($p < 0.001$), and negative controls at flanking (`hp0518`/`hp0520`) and housekeeping loci.
- **Claim 3 (Geographic `slr` divergence is driven by local differences in human gastric physiology, diet, or co-infecting parasites): `[Moderately Supported]`** — Framed appropriately as a plausible evolutionary hypothesis requiring future identification of host binding partners.

### 4. Reproducibility & Data Completeness
- **Exemplary Sequence & Parameter Archiving:** All 288 newly generated gene sequences are deposited in GenBank (`EF372636`–`EF372923`), and exact substitution models, rate matrices, $\alpha$ shape parameters, and primer sets (`Table S13`) are thoroughly documented.
</Blinded Review: TIME_ANON_0706>
