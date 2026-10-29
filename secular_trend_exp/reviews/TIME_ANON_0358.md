<Blinded Review: TIME_ANON_0358>
**Composite Score:** 8.0 / 10.0 (Rigor: 2.8/3.5 | Claims: 2.1/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This evolutionary genetics study tests whether parallel industrial melanism in two classic British geometrid moths—the pale brindled beauty (*Phigalia pilosaria* f. *monacharia*) and the scalloped hazel (*Odontopera bidentata* f. *nigra*)—maps to the same genomic master-switch region (*cortex*) previously shown to control the iconic *carbonaria* morph in the peppered moth (*Biston betularia*, from which they diverged 30–45 Ma). Using backcross mapping families ($n=32$ offspring in *P. pilosaria* segregating 15 *typica* : 17 *monacharia*; $n=74$ offspring in *O. bidentata* segregating 39 *typica* : 35 *nigra*) anchored by orthologous gene markers derived from low-coverage Illumina whole-genome sequencing and 5' RACE of *cortex* exon 1 (`cortE1`), the authors demonstrate that dominant melanism in both species maps cleanly to the conserved *cortex* syntenic block (`rab-ggt`$\beta$ – `HEATR2` – `cortex` – `shuttle craft`).

Second, to test whether *monacharia* and *nigra* arose via recent hard selective sweeps during the nineteenth-century Industrial Revolution (like *B. betularia* *carbonaria*), the authors genotype wild-caught population samples (*P. pilosaria* $n=55$; *O. bidentata* $n=95$; compared against *B. betularia* $n=64$) across six linked markers (`a–e` and `cortE1`) spanning ~700 kb–1.4 Mb. While *B. betularia* displays strong chromosome-wide haplotype–morph linkage disequilibrium across 5 of 6 markers ($p \le 0.05$ to $p \le 0.001$), *O. bidentata* shows zero association at any marker, and *P. pilosaria* shows only a localized association at `cortE1` ($p \le 0.05$ when excluding intermediate morphs). This demonstrates deep developmental parallelism at the *cortex* locus across 30–45 Myr of divergence, paired with markedly different population genetic histories (standing genetic variation / older recombined alleles or soft/poly-allelic sweeps in *P. pilosaria* and *O. bidentata* vs. a single ~1819 *de novo* transposable element sweep in *B. betularia*).

### 2. Methodological & Statistical Audit
* **Comparative Linkage Mapping Resolution:**
  * In *O. bidentata* ($n=74$, 1.35 cM per recombinant), *nigra* co-segregates at 0 cM with `cortE1`, `c`, and `d`, tightly localizing the causal variant to the *cortex* interval.
  * In *P. pilosaria* ($n=32$, 3.125 cM per recombinant), 1 recombinant separates *monacharia* from `cortE1` and 1 recombinant separates *monacharia* from `HEATR2`. The authors transparently explain that 5' RACE on adult RNA captured an alternative first exon (`cortE1`) located between exon 2 and marker `c`, and because lepidopteran *cortex* spans a vast genomic interval with multiple tissue-specific 5' exons (`1A`, `1C`, etc.), a single recombinant relative to `cortE1` still places *monacharia* squarely inside the extended *cortex*–`parn`–`HEATR2` regulatory domain.
* **Population Association & Power Considerations:**
  * Wild-caught samples ($n=55$ *P. pilosaria*: 31 *typica*, 12 *intermediate*, 12 *monacharia*; $n=95$ *O. bidentata*: 73 *typica*, 22 *nigra*) were tested for genic differentiation across morphs via exact $G$-tests in Genepop (Table 2; note a minor species initial typo in Table 2 where *P. pilosaria* is printed as "*A. pilosaria*").
  * Because markers `a–e` and `cortE1` are spaced so that any causal site within the ~700 kb interval lies $<200\text{ kb}$ from a typed marker, a single mutation sweeping from low frequency within the last 200–300 generations (since the Industrial Revolution, given 1 generation/year in these univoltine moths) could not have decayed to linkage equilibrium ($r^2 \approx 0$) via recombination alone. Thus, the null association at flanking markers `a–e` is well-powered to rule out a recent hard sweep from a single nineteenth-century mutation.
  * However, pooling wild individuals across multiple northern England and Scottish localities and collection years introduces potential geographic population structure; while structure typically inflates false-positive associations rather than erasing a hard sweep, explicit geographic stratification (e.g., Cochran–Mantel–Haenszel test by region) would further strengthen the population genetics analysis.

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Claim 1:** *"Comparative linkage mapping using family material supports the hypothesis for both species, indicating a deeply conserved developmental mechanism for melanism involving cortex."* — **[Well Supported]**. Demonstrated by 1:1 Mendelian backcross segregation and syntenic anchoring across `rab-ggt`$\beta$ to `nudC` in Figure 2.
* **Claim 2:** *"In contrast to the strong selective sweep signature seen in British B. betularia, no significant association was detected between cortex-region markers and melanic morphs in wild-caught samples of P. pilosaria and O. bidentata, implying much older, or diverse, origins of melanic morph alleles in these latter species."* — **[Well Supported]**. Grounded in both the marker association contrast (Table 2) and ecological/historical records showing appreciable pre-industrial/rural frequencies and lower dispersal in *P. pilosaria* and *O. bidentata*.

### 4. Reproducibility & Data Completeness
* **Data Availability:** NCBI BioProject accession numbers (`PRJNA566081` and `PRJNA566083`) are provided for the whole-genome sequencing reads, and primers, mini-haplotype contingency tables, collection localities, and recombinant segregation matrices are provided in Electronic Supplementary Material Tables S1–S4.
</Blinded Review: TIME_ANON_0358>
