<Blinded Review: TIME_ANON_0877>
**Composite Score:** 7.2 / 10.0 (Rigor: 2.5/3.5 | Claims: 2.0/2.5 | Biology: 1.5/2.0 | Reproducibility: 1.2/2.0)
**Bias Category:** Technical/Assay
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 7.2/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This experimental molecular microbiology manuscript performs a systematic 5' and 3' promoter deletion analysis of two master transcriptional regulators of *Candida albicans* filamentation—*NRG1* (a transcriptional repressor downregulated upon filament induction) and *UME6* (a transcriptional activator with an unusually long 3 kb 5' UTR, upregulated upon filament induction). Using *Streptococcus thermophilus lacZ* reporter constructs integrated at the ectopic *RPS1* locus in strain CAI4 and assayed via qRT-PCR (normalized to *ACT1* via the Pfaffl method), the authors map promoter regions responsive to YEPD + 10% serum at 37°C, Spider medium at 30°C, Lee's medium pH 6.8, and dilution-induced "hyphal shock" (+/- 40 µM farnesol). They localize distinct and overlapping condition-specific positive and negative cis-regulatory regions across the 2.9 kb *NRG1* upstream region and the 7 kb *UME6* upstream region.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

####ENGTHS
- **Systematic 5' and 3' nested deletion series:** Both 5' truncations and internal/3' fragments (cloned upstream of a basal promoter in `placbasal`) are tested across multiple distinct filament-inducing cues (serum + 37°C, Spider medium, neutral pH, and dilution shock).
- **Direct test of the farnesol quorum-sensing hypothesis:** Testing whether 40 µM exogenous farnesol rescues the dilution-induced repression of *NRG1* deletion constructs directly falsifies a plausible cAMP-farnesol transcriptional mechanism for hyphal shock.
- **Candid discussion of limitations:** The authors explicitly acknowledge that their non-inducing control (YEPD at 30°C) differs in temperature from the 37°C + serum condition, and that ectopic integration at *RPS1* fails to recapitulate native *NRG1* chromatin pH-responsiveness.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Minimal biological replication ($n = 2$) and absence of formal hypothesis testing:** In the Materials and Methods (line 45), the authors state: *"All qRT-PCR reactions were performed in biological duplicate and technical duplicate. Values shown indicate mean ± SEM."* Computing SEM on $n=2$ biological replicates provides a noisy error estimate ($s/\sqrt{2}$), and no formal statistical tests (ANOVA, t-tests, or multiple-comparison adjustments) are reported despite describing changes as "significant decline" or "significantly increased" in the text (lines 65, 67, 89).
- **Ectopic reporter and *URA3* position effects in CAI4:** Integrating constructs at *RPS1* via `placbasal` in CAI4 removes the native chromatin context. This is highlighted by the complete failure of the full-length 2.9 kb *NRG1-lacZ* reporter to downregulate in neutral pH (Lee's pH 6.8 or $\alpha$-MEM pH 7.4, line 99), contradicting endogenous *NRG1* behavior.
- **Lack of site-directed mutagenesis of putative TF motifs:** The regulatory regions mapped are broad (hundreds of base pairs to 1 kb, e.g., -883 bp to -1.5 kb in *NRG1*; -4.0 kb to -4.9 kb in *UME6*). TESS in silico motif predictions (using *S. cerevisiae* consensus motifs and default parameters) are overlaid correlatively without point-mutating the putative Efg1, Ndt80, Nrg1, or Brg1 binding sites to prove direct cis-element necessity.
- **Confounding of transcriptional initiation vs. 5' UTR stability in *UME6*:** Because *UME6* has a 3 kb 5' UTR, 3' promoter deletions (such as -3.0 to -6.0 kb vs. -4.0 to -6.0 kb) alter or remove portions of the 5' UTR or native TSS region, potentially confounding transcriptional initiation rates with mRNA stability of the resulting chimeric transcript.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** The *NRG1* promoter contains distinct condition-specific negative response elements for 37°C + serum (-362 to -122 bp, -74 to -50 bp, and -1.5 kb to -883 bp) and Spider medium (-2.1 to -2.5 kb and -2.5 to -2.9 kb). `[Moderately Supported]` — Supported by reporter fold-change profiles, though limited by $n=2$ biological replicates and broad deletion intervals.
- **Claim 2:** Farnesol-mediated inhibition of cAMP signaling does not govern the *NRG1* promoter response to "hyphal shock" upon culture dilution. `[Well Supported]` — Directly supported by the invariance of fold-downregulation in the presence vs. absence of 40 µM farnesol (Fig. 2).
- **Claim 3:** The *UME6* upstream region (-3 kb to -7 kb) contains distinct and overlapping response regions for 37°C + serum and neutral pH (Lee's pH 6.8). `[Moderately Supported]` — The directional switches between serum at 37°C (where -4.0 to -4.9 kb acts negatively) and neutral pH (where -4.0 to -4.9 kb acts positively) are biologically interesting and internally consistent, though broad in resolution.

### 4. Reproducibility & Data Completeness
- **Constructs and Primers:** Cloning restriction sites, base-pair coordinates relative to the start codon, and references to S1 Table (strains) and S2 Table (primers 1–33) are thoroughly documented (line 35).
- **Assay Parameters:** Harvesting time points (30 min serum, 6 hr Spider, 1 hr Lee's pH 6.8), annealing temperatures (57.4°C), and normalization methods (Pfaffl against *ACT1*) are clearly specified. Raw Ct values are not included in the main text.
</Blinded Review: TIME_ANON_0877>
