<Blinded Review: TIME_ANON_0823>
**Composite Score:** 5.6 / 10.0 (Rigor: 1.8/3.5 | Claims: 1.4/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.2/2.0)
**Bias Category:** Technical/Assay
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 5.6/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary / SUMMARY
This virology study investigates the establishment of persistent SARS-CoV (strain Frankfurt 1) infection in Vero E6 monkey kidney cells that survive acute lytic/apoptotic infection (48 h.p.i.) and grow out as colonies by 4–10 d.p.i., producing $1.26 \times 10^5\ \text{PFU/ml}$ at passage 7. Using Northern blotting with a DIG-labeled mRNA9 probe, Western blotting for ACE2 and phospho-Akt ($\text{Ser}^{473}$), limiting virus dilution ($2 \times 10^{-1}$ to $2 \times 10^2\ \text{PFU}$), clonal isolation of 91 G418-selected parental Vero E6 subclones prior to infection, and pharmacological kinase inhibitors (`SB203580` for p38, `PD98059` for MEK1/2, `SP600125` for JNK, `LY294002` for PI3K), the authors report that: (1) defective interfering (DI) RNAs are not detected by Northern blot, while subgenomic mRNAs 4–5 are reduced to 12.29% of acute levels; (2) ACE2 protein is completely lost in persistently infected cells (passage 7) and downregulated by 24 h.p.i. in acute infection; (3) even 2 PFU of seed virus suffices to generate lytic death followed by surviving persistent colonies, whereas only 16/91 (17.6%) pre-cloned Vero E6 subclones can establish persistence upon infection at MOI 10; and (4) pre-treatment with JNK (`SP600125`) or PI3K (`LY294002`) inhibitors prevents outgrowth of surviving colonies at 20 d.p.i., and persistent-competent Vero E6 subclones (55, 58, 65) phosphorylate Akt at 20 h.p.i. whereas non-persistent subclones (43, 48, 80) do not.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### STRENGTHS
- **Clever host vs virus fluctuation/cloning experiments:** Combining limiting viral dilution ($0.2, 2, 20, 200\ \text{PFU}$, Fig. 4) with pre-infection single-cell cloning of 91 parental Vero E6 subclones (Fig. 5) and subsequent biochemical comparison of 3 persistence-competent (55, 58, 65) vs 3 persistence-incompetent (43, 48, 80) clones (Fig. 7B) provides direct evidence that host-cell heterogeneity in Vero E6 drives survival and persistence.
- **Investigation of multiple classical persistence mechanisms:** Tests for DI RNA species by Northern blot (Fig. 2) and receptor downregulation by ACE2 immunoblot (Fig. 3).

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Confusing and self-contradictory phrasing in Abstract and text regarding limiting dilution:** The Abstract states: *"SARS-CoV diluted to 2 PFU failed to establish persistence, suggesting that some particular viruses in the seed virus did not induce persistent infection."* That sentence in the Abstract is the exact **opposite** of what Figure 4 and page 63 of the Results actually show! In the Results (line 63), the authors write: *"However, all flasks other than those infected at $2 \times 10^{-1}$ PFU [i.e. including $2 \times 10^0 = 2$ PFU!] showed death of almost all cells at 4 d.p.i. and surviving colonies at 7 d.p.i. These colonies became larger at 13 d.p.i. From these results, it seems most likely that some particular viruses in the seed virus did not induce persistent infection."* What the authors *meant* in their English translation was "a particular mutant virus subpopulation in the seed stock is *not* responsible for inducing persistence (because even 2 PFU of wild-type lytic virus establishes persistence)", but the Abstract mistranslated this into *"SARS-CoV diluted to 2 PFU failed to establish persistence"*!
- **Unsubstantiated claim that 100% of cells in passage-7 persistent cultures remain infected despite complete loss of ACE2:** In Fig. 1, indirect immunofluorescence at 10 d.p.i. is claimed to show viral antigen in "all the cells", and at passage 7 the culture yields $1.26 \times 10^5\ \text{PFU/ml}$ while Western blot (Fig. 3) shows zero detectable ACE2 receptor. In classical coronavirus "carrier cultures", receptor-negative or low-ACE2 surviving cells divide while a small fraction of susceptible revertants undergo lytic infection. No negative/mock IF control is described in Fig. 1, no single-cell cloning of the persistently infected culture was performed to distinguish true intracellular persistence from a carrier culture equilibrium, and in Fig. 7B no total-Akt or $\beta$-actin loading control is mentioned for the 6 Vero E6 subclones.
- **Pharmacological inhibitor toxicity over 20 days not controlled:** In Fig. 6, cells were pre-treated with 10–50 $\mu\text{M}$ `SP600125` (JNK inhibitor) or `LY294002` (PI3K inhibitor), infected at MOI 2, and stained with crystal violet 20 days later. High concentrations (25–50 $\mu\text{M}$) of `LY294002` and `SP600125` are cytostatic/cytotoxic to sparse surviving cells over multi-day culture even in the absence of virus; no uninfected inhibitor-treated colony-formation control is reported.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** SARS-CoV infection of Vero E6 cells selects for surviving cells with downregulated ACE2 expression that continue to shed infectious virus ($1.26 \times 10^5\ \text{PFU/ml}$ at passage 7) without detectable major DI RNAs. `[Well Supported]`
- **Claim 2:** Pre-existing clonal heterogeneity within the parental Vero E6 population (16/91 subclones capable of survival/persistence) rather than a pre-existing non-cytopathic viral variant in the seed stock determines persistence establishment. `[Well Supported]` (Despite the severe wording contradiction in the Abstract).
- **Claim 3:** Activation of JNK and PI3K/Akt signaling specifically mediates establishment of SARS-CoV persistence. `[Moderately Supported]` — Supported by differential Akt $\text{Ser}^{473}$ phosphorylation at 20 h.p.i. between persistence-competent (clones 55, 58, 65) and incompetent (clones 43, 48, 80) clones (Fig. 7B), though the inhibitor experiment (Fig. 6) lacks uninfected clonal outgrowth toxicity controls and total-Akt loading controls.

### 4. Reproducibility & Data Completeness
- **Reagents and primers:** Exact Northern blot primer sequences (`28,751–28,777` and `29,687–29,721` of `NC_004718`), viral strain (`Frankfurt 1`), inhibitor catalog sources, and antibody dilutions are clearly stated.
- **Quantitative replication:** All experiments (Northern, Western, crystal violet plates) are presented as qualitative single-experiment gels/plates without biological replicate counts or statistical tests.
</Blinded Review: TIME_ANON_0823>
