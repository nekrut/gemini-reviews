# Blinded Review: TIME_ANON_24
**Composite Score:** 4.1 / 10.0 (Rigor: 1.1/3.5 | Claims: 1.0/2.5 | Biology: 1.0/2.0 | Reproducibility: 1.0/2.0)
**Bias Category:** Control-Group HWE Violation / Heterozygote-Only Association Artifact
**Verdict:** Reject
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Clinical/Epidemiological Observational

---

### 1. Executive Summary

This manuscript investigates the population frequency and infectious-disease associations of a 6-bp promoter indel polymorphism (`-305_-300delAACTTT`) in the human *IFNA2* gene across 1,256 individuals from five cohorts: 586 healthy Vietnamese blood donors, 199 Central African children with malaria (100 mild, 99 severe), 265 Brazilians of European descent (101 chronic HCV patients and 164 healthy controls), 108 Kaingang Amerindians, and 98 Guarani Amerindians. Using PCR and direct Sanger sequencing, the authors report significant allele and genotype frequency differences across populations, deviations from Hardy-Weinberg equilibrium (HWE) in Brazilians and Kaingang, no association with malaria severity ($p = 1.0$) or HCV treatment response, and a statistically significant association with HCV infection in Brazilians ($p = 0.03$ overall; $\text{OR} = 2, p = 0.014$ for heterozygotes).

Closer audit of the contingency tables and Hardy-Weinberg statistics reveals that the paper's sole positive clinical claim—that `-305_-300delAACTTT` is associated with HCV prevalence in Brazilians—is an artifact of severe Hardy-Weinberg disequilibrium specifically within the Brazilian healthy control group ($p = 0.0004$), combined with an incoherent genetic model where heterozygotes (`wt/del`) are elevated in HCV cases ($30\%$ vs. $17\%$) while homozygotes (`del/del`) are *depleted* in HCV cases ($3\%$ vs. $6\%$) and the overall allele frequency does not significantly differ between HCV cases and controls ($17.8\%$ vs. $14.3\%, p = 0.28$). In addition, the paper pools diseased HCV cases with healthy controls when computing "Brazilian" population frequencies and HWE in Tables 1–5, and commits a factor-of-2 arithmetic error when reporting malaria subgroup allele frequencies in the text.

---

### 2. Methodological & Statistical Audit

1. **The Claimed HCV Association Is Driven by HWE Violation in Controls and Fails Under Allelic or Monotonic Genetic Models:**
   * From the counts reported in the Results (line 136):
     * **HCV patients ($n = 101$, $202$ alleles):** `wt/wt` $= 68$ ($67.3\%$), `wt/del` $= 30$ ($29.7\%$), `del/del` $= 3$ ($3.0\%$). Deletion allele count $= 30 + 2(3) = 36 / 202$ ($q_{\text{HCV}} = 17.82\%$).
     * **Healthy Brazilian controls ($n = 164$, $328$ alleles):** `wt/wt` $= 127$ ($77.4\%$), `wt/del` $= 27$ ($16.5\%$), `del/del` $= 10$ ($6.1\%$). Deletion allele count $= 27 + 2(10) = 47 / 328$ ($q_{\text{ctrl}} = 14.33\%$).
   * **Allelic test is null:** Comparing deletion allele counts between HCV cases ($36/202$) and healthy controls ($47/328$) yields $\chi^2 = 1.16, p = 0.28$ (Fisher's exact $p = 0.32$).
   * **Biologically contradictory direction across genotypes:** Whereas `wt/del` heterozygotes are more frequent in HCV patients than controls ($29.7\%$ vs. $16.5\%$), `del/del` homozygotes are *half as frequent* in HCV patients as in controls ($3.0\%$ vs. $6.1\%$). If the deletion reduces *IFNA2* transcription in vitro and impairs antiviral immunity, `del/del` homozygotes should have at least as high risk as `wt/del` heterozygotes, not lower risk.
   * **Severe HWE violation restricted to the healthy control cohort:** Testing HWE separately in the two Brazilian sub-cohorts shows that the 101 HCV cases are in exact Hardy-Weinberg equilibrium (expected counts $68.2, 29.6, 3.2$ vs. observed $68, 30, 3$; $\chi^2 = 0.018, p = 0.89$), whereas the 164 healthy controls exhibit extreme HWE deviation due to a deficit of heterozygotes and excess of homozygotes (expected counts $120.4, 40.3, 3.4$ vs. observed $127, 27, 10$; $\chi^2 = 17.68, p = 2.6 \times 10^{-5}$; exact $p = 0.0004$). Direct Sanger sequencing of PCR products across a 6-bp deletion produces overlapping out-of-frame chromatogram peaks in heterozygotes, which is notorious for causing heterozygote under-calling (scoring noisy traces as homozygous) if sequencing quality varies between batches. Comparing well-calibrated case genotypes against an HWE-violating control batch invalidates the $\text{OR} = 2.0$ ($p = 0.014$) heterozygote comparison.

2. **Confounded Pooling of Diseased Cases and Controls in Population Genetics Tables (Tables 1–5):**
   * In Tables 1–5, the "Brazilians" population ($N = 265$) is formed by pooling the $101$ chronic HCV patients with the $164$ healthy controls ($68+127 = 195$ `wt/wt`, $30+27 = 57$ `wt/del`, $3+10 = 13$ `del/del`), and the "Central Africans" population ($N = 199$) consists entirely of hospitalized malaria patients. Pooling clinical disease cohorts with healthy population cohorts to perform cross-population differentiation tests (Tables 2 and 4) and population HWE tests (Table 5) confounds case-control ascertainment with population structure.
   * Furthermore, the 10 pairwise population comparisons in Table 2 and 10 pairwise comparisons in Table 4 (20 tests total) are interpreted at an unadjusted threshold of $p < 0.05$ without multiple-testing correction.

3. **Arithmetic & Numerical Errors in the Main Text:**
   * **Factor-of-2 error in malaria allele frequencies (line 136):** The text states: *"allelic frequencies of the deletion in mild malaria cases 0.10 (90 individuals without deletion, 9 with the deletion on one chromosome) versus 0.12 in severe cases (89 individuals without deletion, 9 with the deletion on one chromosome, 1 individual with the deletion on both chromosomes, P = 1)."* First, $90 + 9 = 99$ individuals, whereas Methods (line 34) states $n = 100$ mild malaria cases (and in Table 3, total Central African genotypes are $178$ `wt/wt`, $20$ `wt/del`, $1$ `del/del` $= 199$, meaning $2$ `wt/del` individuals and $1$ fewer `wt/wt` individual are missing from the text breakdown $90+89 = 179 \neq 178$ and $9+9 = 18 \neq 20$). Second, $9$ or $11$ deletion alleles out of $\sim 200$ chromosomes correspond to **allelic frequencies of $0.045\text{--}0.055$ ($5\text{--}6\%$)**, matching Table 1's pooled Central African allele frequency of $22/398 = 0.055$ ($0.06$). The authors divided the allele counts by the number of diploid *individuals* ($\sim 100$) instead of the number of *chromosomes* ($\sim 200$), doubling the reported allelic frequencies to $0.10$ and $0.12$.
   * **Control sample size misstated in line 136:** Line 136 states *"In the healthy control group we had in a total of 265 individuals 127 (77%) with no deletion on any chromosome; 27 (17%) with a deletion on one chromosome and 10 (6%) with a deletion on both chromosomes."* Here $127 + 27 + 10 = 164$ healthy controls; $265$ is the combined total of controls plus HCV patients.
   * **Inconsistent variant nomenclature:** The same 6-bp deletion is referred to as `-305_-300delAACTTT` in the Abstract and text (lines 7, 20, 70, 136), `del -301/-306` in Tables 1 and 3, and `Δ-300/-305` in the section heading (line 134).

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **Claim that `-305_-300delAACTTT` plays a disadvantageous role in HCV infection and influences HCV prevalence (Abstract lines 9–11, Conclusion line 152):** **Overstated / Methodologically Flawed.** Because the allelic association is null ($p = 0.28$), `del/del` homozygotes are less frequent in HCV cases than controls ($3\%$ vs. $6\%$), and the control group violates HWE ($p = 0.0004$), the data do not support a biological effect of this polymorphism on HCV susceptibility.
* **Claim that HWE deviation in Brazilians is caused by European migration admixture (Discussion line 147):** **Speculative / Unverified.** Wahlund effects from population substructure produce a deficit of heterozygotes only when sub-populations have drastically different allele frequencies ($\Delta q \gg 0.3$). With minor allele frequencies around $0.06\text{--}0.16$ across global populations, intra-European admixture in Curitiba cannot generate a 3-fold homozygote excess ($10$ observed vs. $3.4$ expected) in healthy controls while HCV patients from the exact same hospital and ethnic group are in exact HWE ($3$ observed vs. $3.2$ expected). Genotyping/base-calling error in the control batch is a far more parsimonious explanation.

---

### 4. Reproducibility & Data Completeness

* **Positives:** PCR primer sequences (`IFN-F` and `IFN-R`), thermal cycling parameters, amplicon size ($480\text{ bp}$), and complete genotype and allele count tables for all five populations are provided in the text and tables.
* **Deficiencies:**
  1. No GenBank reference accession number is given to anchor the promoter nucleotide coordinates (explaining why the authors themselves oscillate between `-305_-300`, `-301/-306`, and `-300/-305`).
  2. Data for the HCV treatment response analysis ("data not shown", line 136) and the three other *IFNA2* promoter mutations mentioned in line 70 ("Of the four mutations in the IFNA2 promoter only the deletion -305_-300delAACTTT was analyzed") are omitted.
