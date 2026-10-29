<Blinded Review: TIME_ANON_0647>
**Composite Score:** 7.8 / 10.0 (Rigor: 2.7/3.5 | Claims: 2.1/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Clinical/Observational

OVERALL_SCORE: 7.8/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This study investigates whether the common 29.5-kb human *APOBEC3B* (`A3B`) germline deletion polymorphism—which fuses the 5' UTR of `A3B` to the 3' UTR of `APOBEC3A` (`A3A`), completely ablating the `A3B` coding sequence—affects HIV-1 acquisition, clinical disease progression, or in vitro viral replication. Prior studies had yielded conflicting conclusions: an earlier US cohort study reported increased HIV-1 acquisition and faster progression in `D/D` homozygotes (despite low `D` allele frequency in European/African Americans), whereas smaller Japanese and Indian studies found no association. Recognizing that East Asians have a high frequency (~30%) of the deleted `D` allele and that prior Asian studies lacked transmission-route matching, the authors enrolled 248 HIV-1-positive Japanese men who have sex with men (MSM) and 207 HIV-1-negative Japanese MSM controls. Using duplex PCR genotyping, longitudinal linear regression of pre-ART $\text{CD4}^+$ T-cell and plasma viral load (VL) trajectories ($n=202$), Cox proportional hazards for time to ART initiation ($n=246$), Illumina MiSeq deep-sequencing of proviral `GG->AG` and `GA->AA` hypermutation ($n=4$ per genotype), qRT-PCR profiling of `A3A–A3H` in primary $\text{CD4}^+$ T cells and IFN-$\alpha$-treated monocyte-derived macrophages (MDMs), and multi-cycle $\text{HIV-1}_{\text{NL4-3}}$ replication assays in primary cells ($n=5$ `I/I` vs. $n=5$ `D/D`), the authors demonstrate that `A3B` genotype has no impact on HIV-1 susceptibility, clinical progression, proviral hypermutation, or in vitro viral replication. The combination of an ethnically and behaviorally matched high-allele-frequency cohort with comprehensive primary-cell virological validation makes this a rigorous, convincing negative study.

### 2. Methodological & Statistical Audit / STRENGTHS, WEAKNESSES & METHODOLOGICAL AUDIT

#### Key Strengths
- **Well-powered population & exposure matching:** By restricting cases ($n=248$) and controls ($n=207$) to Japanese MSM—a population where the `A3B` deletion allele frequency is ~29% (`D/D` homozygotes ~8%)—the study achieves substantially higher statistical power to evaluate recessive (`D/D`) and additive (`I/D`, `D/D`) genetic effects without confounding by ethnicity or heterosexual/parenteral exposure route. Hardy-Weinberg equilibrium is verified in both cases ($p=0.69$) and controls ($p=0.80$).
- **Multi-layered mechanistic corroboration:** Rather than relying solely on case-control odds ratios, the study tests:
  1. Longitudinal clinical progression ($\text{CD4}^+$ and VL slopes via least-squares linear regression over $\ge 2$ pre-ART visits in $n=202$ patients, plus Kaplan-Meier/log-rank and Cox proportional hazards for time from diagnosis to ART in $n=246$ patients);
  2. Ex vivo proviral DNA `G->A` hypermutation spectra in patient PBMCs via Illumina MiSeq (`52,933` to `86,675` reads per patient after `>Q30` filtering) distinguishing dinucleotide context (`GG->AG` vs. `GA->AA`);
  3. Endogenous expression of all seven `APOBEC3` paralogs (`A3A–A3H`) in PHA/IL-2-activated primary $\text{CD4}^+$ T cells and resting vs. IFN-$\alpha$-stimulated MDMs across `I/I`, `I/D`, and `D/D` donors, showing extremely low `A3B` transcription (`<10^-3` relative to `GAPDH`) and no compensatory upregulation of `A3A` or `A3G`;
  4. In vitro replication kinetics (`p24` ELISA over 11 days) and virion infectivity (`TZM-bl` luciferase assay) of WT `NL4-3` and `NL4-3 deltaVif` in primary cells from 5 `I/I` and 5 `D/D` donors.

#### Methodological Weaknesses & Audit Findings
1. **Internal Reporting Discrepancy in Table 3 Regarding Pre-ART Status at Entry:**
   - In the Results section (line 94), the authors state that to analyze untreated disease progression, they used data from *"202 HIV-1-infected participants who had dataset of at least two time points [after first hospital visit and before ART]"*, noting that only *"forty-six patients started ART before the second measurement"*.
   - However, Table 3 (line 105) lists `"ART naïve at entry, n (%): 20 (8%)"` and `"Median VL at entry (IQR), copies/mL: 61 (<40–410)"` across the 248 infected patients (`D/D`: 2 [11%], `I/D`: 7 [6%], `I/I`: 11 [9%]). If 202 of the 248 patients had at least two pre-ART measurements after their first hospital visit, then at least 202 (>81%)—not 20 (8%)—must have been ART-naïve at cohort entry! It appears Table 3 inadvertently labeled "patients who remained ART-naïve at last follow-up" (or VL at last follow-up on ART) as "at entry."
2. **Age Imbalance and Recruitment Venue Differences Between Cases and Controls:**
   - Infected MSM were recruited at a single tertiary referral hospital in Tokyo (median age 40 years, IQR 34–45) with DNA extracted from whole blood, whereas uninfected MSM controls were recruited at a gay festival venue in Tokyo (median age 33 years, IQR 27–39) with DNA extracted from buccal swabs and HIV-1 status determined by follow-up postal dried blood spot (`DBS`) testing in 70% of respondents (lines 28–31, Table 3). While germline genotype is invariant with age, the 7-year younger median age of controls means some younger controls had shorter cumulative window of sexual exposure, and 30% of festival controls lacked confirmatory postal DBS HIV-1 testing.
3. **Minor Terminology Inconsistency (`CD4+ T cells` vs. `PBMCs`):**
   - Methods (line 44) state that primary $\text{CD4}^+$ T cells were purified from PBMCs via negative magnetic selection (`Miltenyi`) and infected with $\text{HIV-1}_{\text{NL4-3}}$, whereas Results (line 136) and the Figure 3 legend (line 141) describe these exact assays as replication kinetics in `"PBMCs"`.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** The *APOBEC3B* deletion polymorphism (`I/I`, `I/D`, `D/D`) is not associated with HIV-1 acquisition susceptibility or co-infection rates (HBV, HCV, syphilis) in Japanese MSM. `[Well Supported]`
- **Claim 2:** *APOBEC3B* genotype does not significantly alter pre-ART $\text{CD4}^+$ T-cell decline ($p=0.054$), plasma viral load trajectory ($p=0.96$), or time from diagnosis to ART initiation ($p=0.96$). `[Well Supported]` — The authors appropriately note the borderline $p=0.054$ in $\text{CD4}^+$ slope and verify that it does not translate into any difference in time to $\text{CD4}^+ < 350/\mu\text{L}$ or ART initiation.
- **Claim 3:** Endogenous `A3B` is expressed at negligible levels in primary human $\text{CD4}^+$ T cells and MDMs compared to `A3A`, `A3F`, and `A3G`, and loss of `A3B` (`D/D`) neither alters `A3A–A3H` expression nor affects proviral `G->A` hypermutation or $\text{HIV-1}_{\text{NL4-3}}$ replication in primary cells. `[Well Supported]`

### 4. Reproducibility & Data Completeness
- **Strengths:** All primer and TaqMan probe sequences for `A3B` genotyping (`I` and `D` alleles) and `A3A–A3H` qRT-PCR (`Table 1`), full cohort contingency tables (`Table 2`, `Table 3`), and deep-sequencing read filtering criteria (`>Q30`, `52,933–86,675` reads) are fully reported.
- **Deficiencies:** Raw Illumina MiSeq fastq files for the proviral deep-sequencing experiment ($n=12$ patients) are not linked to a public sequence read archive (SRA/DRA) accession.
</Blinded Review: TIME_ANON_0647>
