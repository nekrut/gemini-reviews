<Blinded Review: TIME_ANON_0174>
**Composite Score:** 6.8 / 10.0 (Rigor: 2.2/3.5 | Claims: 1.7/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** Statistical/Design
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Translational/Preclinical/Biomarker

---

### 1. Executive Summary
This preclinical study uses a human rheumatoid arthritis (RA) synovium xenograft model in male C.B-17 SCID mice to evaluate whether repeated local injection of a recombinant E1/E3-deleted type-5 adenovirus expressing Fas ligand (`Ad-FasL`, $10^{11}$ viral particles every 2 weeks for 5 doses) can ablate human inflammatory synovial tissue in situ ("molecular synovectomy"). The authors establish a dose response ($10^9$ to $10^{11}$ particles) using `Ad-LacZ` (showing high transduction of synoviocytes, infiltrating leukocytes, and endothelial cells at $10^{11}$ particles without chondrocyte transduction at day 3), determine transgene mRNA kinetics by RT-PCR (peaking days 2–10 and declining by day 20), and show that `Ad-FasL` increases TUNEL-positive apoptotic synovial cells ~15–20-fold at day 3 and reduces engrafted synovial mass from a mean of $150.0 \pm 41.3\text{ mg}$ (`Ad-LacZ`, $n=10$) to $30.6 \pm 23.2\text{ mg}$ (`Ad-FasL`, $n=10$; Wilcoxon rank-sum $P < 0.005$) after two months. While the in vivo xenograft reduction is striking and the rank-sum arithmetic in Table 1 is exact, the study suffers from pseudoreplication across 6 patient donors, omission of the PBS control group weights from Table 1, and lack of long-term cartilage or hepatic toxicity evaluation.

### 2. Methodological & Statistical Audit
- **Verification of Table 1 Rank-Sum Test Arithmetic:** Auditing the raw graft weights and ranks in Table 1 ($n_1 = 10$ `Ad-LacZ` vs. $n_2 = 10$ `Ad-FasL`):
  - `Ad-LacZ` weights (mg): `162, 122, 171, 159, 203, 184, 98, 177, 156, 68` $\rightarrow$ assigned ranks: `16, 13, 17, 15, 20, 19, 12, 18, 14, 10`, yielding $T_1 = 154$ (mean $= 150.0\text{ mg}$, median $= 160.5\text{ mg}$).
  - `Ad-FasL` weights (mg): `17, 72, 29, 62, 11, 46, 34, 10, 0, 25` $\rightarrow$ assigned ranks: `4, 11, 6, 9, 3, 8, 7, 2, 1, 5`, yielding $T_2 = 56$ (mean $= 30.6\text{ mg}$, median $= 27.0\text{ mg}$).
  - Rank assignment and sums are 100% exact ($T_1 + T_2 = 154 + 56 = 210 = N(N+1)/2$, Mann-Whitney $U = 1$, exact two-sided $P = 0.00018 < 0.005$).
- **Omission of the PBS Control Group in Table 1:** In the Methods (line 50), the authors explicitly state that three treatment groups were run (`Ad-FasL`, `Ad-LacZ`, and `PBS only`), that *"Ten samples from each treatment group were examined,"* and that *"The weight of each sample was measured individually for each group as shown in Table 1."* However, Table 1 only reports the `Ad-LacZ` and `Ad-FasL` groups, completely omitting the 10 `PBS`-treated graft weights. Reporting the uninjected/PBS graft weights at 10 weeks is essential to determine how much of the initial $200\text{ mg}$ graft resorbs spontaneously in SCID mice vs. how much is maintained or inflamed by `Ad-LacZ` viral vector particles.
- **Donor Pseudoreplication (6 Patients into 30 Mice):** Synovial tissue was harvested from 6 RA patients (Methods, line 30 & 50) and subdivided into $200\text{ mg}$ pieces implanted into 10 SCID mice per group. In Table 1, the 10 grafts per group are analyzed as completely independent observations in an unstratified Wilcoxon rank-sum test without tracking which patient donor each graft came from or modeling donor random effects.
- **Unassessed Cartilage and Systemic Hepatic Toxicity of Repeated Ad-FasL:** Chondrocytes in the superficial zone of articular cartilage express Fas and undergo apoptosis upon FasL exposure, and the authors note in the Discussion (line 143) that after 4 weeks of in vitro culture (when matrix is degraded), `Ad-LacZ` infects superficial chondrocytes. However, the 2-month repeated `Ad-FasL` experiment only weighed isolated synovium and did not evaluate chondrocyte apoptosis or cartilage matrix degradation in synovium+cartilage co-grafts, nor did it monitor mouse liver histology or serum transaminases (a critical safety endpoint since systemic leakage of `Ad-FasL` causes fulminant hepatic apoptosis in mice).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** Local injection of $10^{11}$ particles of `Ad-FasL` into human RA synovial xenografts in SCID mice drives transgene expression for ~10 days and induces a 15–20-fold increase in synovial cell apoptosis at day 3 compared to `Ad-LacZ` and PBS controls. `[Well Supported]`
- **Claim 2:** Biweekly intra-graft injection of `Ad-FasL` ($\times 5$ doses over 2 months) reduces human RA synovial xenograft weight by ~80% ($30.6\text{ mg}$ vs. $150.0\text{ mg}$ in `Ad-LacZ`) and depletes infiltrating mononuclear cells and hyperplastic synoviocytes. `[Well Supported]`
- **Claim 3:** Repeated intra-articular `Ad-FasL` gene transfer can serve as a clinical "gene scalpel" for molecular synovectomy in early RA without damaging cartilage. `[Overstated]` — In immunocompetent humans, repeated intra-articular injection of $10^{11}$ first-generation E1/E3-deleted adenovirus particles induces severe neutralizing anti-adenoviral immunity and acute joint inflammation (which SCID mice cannot mount), and long-term chondrocyte safety under repeated `Ad-FasL` dosing was not tested in vivo.

### 4. Reproducibility & Data Completeness
- **Protocol & Primer Completeness:** Exact RT-PCR primer sequences for transgenic `FasL` (`5'-TCAGCTCTTCCACCTGCAG-3'` and vector poly(A) `5'-CACTGCATTCTAGTTGTGG-3'`, 688 bp) and $\beta$-actin (505 bp), cycling parameters, viral particle purification protocols, and individual graft weights for `Ad-LacZ` and `Ad-FasL` (Table 1) are fully reported. Only the raw weights for the `PBS` group and the patient-to-mouse graft mapping are missing.
</Blinded Review: TIME_ANON_0174>
