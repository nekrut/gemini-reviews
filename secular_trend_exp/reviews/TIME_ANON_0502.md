<Blinded Review: TIME_ANON_0502>
**Composite Score:** 5.8 / 10.0 (Rigor: 1.7/3.5 | Claims: 1.6/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.1/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

OVERALL_SCORE: 5.8/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2010s

### 1. Executive Summary / SUMMARY
This quantitative genetics study maps non-*Prnp* modifiers of transmissible spongiform encephalopathy (TSE) incubation time across four factorial combinations of prion strain and inoculation route—natural bovine spongiform encephalopathy (`BSE`) vs mouse-adapted scrapie (`Me7`), administered intracranially (`ic`) vs intraperitoneally (`ip`)—using both a discovery panel of 16–19 `BXD` recombinant inbred (RI) mouse strains and a follow-up cohort of 123–480 `F2` intercross mice derived from the same `C57BL/6J` $\times$ `DBA/2J` progenitors (both homozygous for the short-incubating *Prnp*$^{\text{a}}$ / *s7* allele). From the `BXD` panel, the authors estimate narrow-sense heritabilities of $0.30$ (`Me7 ic`) to $0.59$ (`BSE ic`), compute inter-trait genetic correlations ($r = 0.29$ to $0.70$), and perform simple and composite interval mapping (IM/CIM), nominating 7 candidate QTL regions on chromosomes 4, 6, 10, 11, and 18 (plus Chr 2). Genotyping 27 microsatellite markers around these candidate regions in the `F2` mice fails to replicate 6 of the 7 `BXD` CIM peaks (replicating only Chr 2 for `BSE ic`), after which the authors apply a random-effects meta-analysis across `BXD` and `F2` datasets, concluding that a locus on Chromosome 11 (`40–65 cM`, accounting for ~3% of variance) exerts a general effect across all four agent/route models while other QTLs are route- or agent-specific. While the biological question (whether *ic*-derived prion QTLs generalize to peripheral *ip* routes and across natural vs host-adapted strains) is important and the multi-year BSL-3 mouse bioassay dataset is substantial, the statistical execution suffers from severe overfitting of CIM models in $N = 16\text{–}19$ BXD lines, internal numerical contradictions between Table 6 and Table 7, an impossible Pearson correlation / $p$-value pair ($r = 0.813, P = 0.049$) for the 4 trait means in Table 5, and completely missing mathematical equations throughout the Methods section.

### 2. Methodological & Statistical Audit / WEAKNESSES & METHODOLOGICAL AUDIT
- **Severe Overfitting of Composite Interval Mapping (CIM) in $N = 16\text{–}19$ BXD Strains and High F2 Non-Replication Rate:**
  - The BXD discovery screen uses only $N = 16$ (`Me7 ip`), $17$ (`Me7 ic`), $18$ (`BSE ip`), and $19$ (`BSE ic`) RI strains (Table 1, Table 11; note that in Table 1 `BXD2` is missing its `Me7 ic` value, leaving 17 strains). Performing forward stepwise Composite Interval Mapping (CIM) that conditions on multiple background markers selected from 3,795 markers in a sample of only $N = 16\text{–}19$ lines exhausts the residual degrees of freedom and causes severe overfitting.
  - This overfitting is directly visible in Table 4 (`Interval mapping results for the BXDs`, lines 124–135): weak simple interval mapping (IM) peaks jump to extreme CIM likelihood ratio statistics (e.g., `D6Mit29` in `Me7 ip` jumps from $\text{IM LRS} = 8.1$ to $\text{CIM LRS} = 46.2$; `D6Mit67` in `Me7 ic` jumps from $13.2$ to $41.1$; `D18Mit19` jumps from $15.2$ to $43.8$), and for `D4Mit204` (`Me7 ic`, line 129) conditioning on background markers actually **flips the allelic direction of the QTL** from `C57` in IM to `DBA` in CIM!
  - Unsurprisingly, when these 7 BXD CIM candidate intervals were tested in the much larger, well-powered F2 cohorts ($N = 123\text{–}480$ mice, Table 7), **6 of the 7 loci failed to replicate**, and 4 of the 7 intervals (`Chr 4 BSE ic`, `Chr 4 Me7 ic`, `Chr 6 Me7 ic`, `Chr 18 Me7 ip`) exhibited the **opposite allelic direction** between BXD and F2 (Table 7, lines 217–228).
- **Direct Numerical Contradiction Between Table 6 and Table 7 for the Sole "Replicated" QTL (`Chr 2 BSE ic`):**
  - The authors highlight `Chromosome 2 (1.0–27.3 cM)` for `BSE ic` as the *only* locus out of 7 that successfully replicated between BXD and F2 (line 209). However, comparing `Table 6` (`QTL mapping data for F2s`, lines 188–189) and `Table 7` (`BXD and F2 mapping data`, lines 215–216) reveals a glaring contradiction in the F2 LRS statistics for this exact locus:
    - In **Table 6** (lines 188–189), the `F2 LRS Statistics` for `Chr 2 BSE ic` (`1.0–25.3 cM`) are **`5.6` (Simple)** and **`7.5 *` (Composite)**.
    - In **Table 7** (lines 215–216), `5.6` and `7.5 *` are listed as the **`Peak BXD LRS`**, whereas the `F2 LRS Statistics` are listed as **`2.6` (Simple)** and **`20.1 *` (Composite)**! Thus, either Table 6 accidentally copied the BXD LRS values (`5.6` and `7.5`) into the F2 table, or Table 7 fabricated/mismapped the F2 LRS values (`2.6` and `20.1`).
- **Mathematical Error in the Reported Correlation of BXD and F2 Means (Line 156 & Table 5):**
  - Referring to the 4 pairs of BXD and F2 experiment means in Table 5 (`BSE ic`: $386$ vs $345$; `BSE ip`: $364$ vs $337$; `Me7 ic`: $152$ vs $129$; `Me7 ip`: $326$ vs $292$), line 156 states: *"To help qualify this statement, the calculated Pearson's r between BXD and F2 trait means is 0.813 (P = 0.049)."*
  - Both numbers are mathematically wrong: (1) the actual Pearson correlation between `[386, 364, 152, 326]` and `[345, 337, 129, 292]` is **$r = 0.9987$** ($P = 0.0013$), not $0.813$; and (2) for $N = 4$ data points ($df = N - 2 = 2$), a Pearson correlation of $r = 0.813$ yields $t = 0.813\sqrt{2 / (1 - 0.813^2)} = 1.976$, which corresponds to a two-tailed $P = 0.187$ (or one-tailed $P = 0.093$), never $P = 0.049$.
  - Notice also that the BXD experiment means reported in Table 5 (`386`, `364`, `152`, `326`) do not match the `Expt Mean` row at the bottom of Table 1 (`385`, `368`, `153`, `332`, line 69) because Table 1 included the two progenitor strains (`C57BL/6J` and `DBA/2J`) in the mean.
- **Unadjusted Between-Strain Variance Used in Narrow-Sense Heritability (Table 2) and Missing Equations in Methods:**
  - In Table 2 (lines 85–88), narrow-sense heritability is calculated as $h^2_n = \frac{0.5 V_{\text{Between}}}{0.5 V_{\text{Between}} + V_{\text{Within}}}$ (e.g., for `BSE ic`, $\frac{0.5 \times 13371}{0.5 \times 13371 + 4697} = 0.587 \approx 0.59$). However, in an ANOVA of RI lines with $n \approx 12$ replicates per strain, the observed variance of strain means ($s^2_{\bar{Y}} = 13,371$) estimates $V_G + V_E / \bar{n}$ rather than pure genetic variance $V_G$; failing to subtract $V_E / \bar{n}$ biases heritability upward (especially for `Me7 ic`, where $V_{\text{Between}} = 123$ is smaller than $V_{\text{Within}} = 142$).
  - In the Methods section (Offset 46080, lines 65, 112, 120, 122, 128, 132, 139, 141), **all eight mathematical equations (`Equations 1–9`) and inline symbols ($\tau^2$, $Q$, $\bar{Z}_r$, $w^*$) are completely missing/blank** in the manuscript text.
  - In Results lines 260–264, the negative signs on the meta-analytic effect sizes (`-0.30`, `-0.23`, `-0.22` in Table 8, indicating DBA alleles lengthen incubation time) are omitted (`r 0.30±0.06`, `r 0.23±0.05`, `r 0.22±0.05`).

### 3. Biological / Experimental Grounding & Claim Proportionality / STRENGTHS
- **Strengths:**
  - **Valuable Factorial Experimental Design Across Prion Strains and Inoculation Routes:** Testing both a primary cross-species isolate (`BSE`) and a mouse-adapted strain (`Me7`) across both central (`ic`) and peripheral (`ip`) routes in a *Prnp*-uniform background directly addresses whether peripheral lymphoreticular replication invokes distinct host genetic modifiers compared to direct intracerebral challenge.
  - **Candid Reporting of F2 Replication Failures:** Despite over-relying on CIM in the small BXD panel, the authors transparently present Table 7 showing that 6 of 7 BXD CIM loci failed direct F2 replication before turning to random-effects meta-analysis.
- **Claim Proportionality:**
  - `[Well Supported]` Non-*Prnp* polygenic modifiers account for a substantial fraction ($30\%\text{–}55\%$) of phenotypic variance in prion incubation period across *ic* and *ip* routes in `C57BL/6J` $\times$ `DBA/2J` crosses, and genetic overlap across routes/strains is partial ($r \approx 0.3\text{–}0.7$).
  - `[Moderately Supported]` A modifier locus on Chromosome 11 (`40–65 cM`) shows a consistent small-effect direction (`DBA/2J` allele prolonging incubation time, explaining ~3% of variance) across the combined transmission experiments (Table 9).
  - `[Fragile]` Specific BXD Composite Interval Mapping (CIM) peaks on Chromosomes 4, 6, 10, and 18 (Table 4), which were severely overfitted on $N = 16\text{–}19$ RI strains and failed individual F2 replication or reversed allelic sign in Table 7.

### 4. Reproducibility & Data Completeness
- Strain-by-strain BXD means, SDs, and sample sizes ($n$) for all four experiments are provided in full in Table 1, allowing independent re-calculation of strain-mean correlations, ANOVA variance components, and simple interval mapping against public BXD genotypes on GeneNetwork.
- However, the specific list of 27 microsatellite markers genotyped in the F2 cohorts, the individual F2 genotype-phenotype data, and the 8 missing equation blocks in the Methods section are absent from the main text.
</Blinded Review: TIME_ANON_0502>
