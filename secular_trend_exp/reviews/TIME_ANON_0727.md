<Blinded Review: TIME_ANON_0727>
**Composite Score:** 8.6 / 10.0 (Rigor: 2.9/3.5 | Claims: 2.2/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.6/2.0)
**Scientific Core Score:** 7.0 / 8.0
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 8.6/10
VERDICT: PASS
ESTIMATED_DECADE: 1990s

---

### 1. Executive Summary (SUMMARY)
This study identifies and functionally characterizes the cellular receptor (`CPE-R`, later designated claudin-4 / *CLDN4*) for *Clostridium perfringens* enterotoxin (CPE). Because full-length CPE lyses receptor-bearing cells, the authors engineered a non-cytotoxic $\text{His}_{10}$-tagged C-terminal receptor-binding fragment of CPE (`H10PER`, residues 184–319), biotinylated it, and used FACS-based expression cloning to screen a Vero cell cDNA library transfected into CPE-resistant mouse L929 cells stably expressing polyoma large T antigen (`L929pyT18`). After three rounds of FACS sorting and plasmid rescue, they isolated clone 706 (`CPE-R`), encoding a 209-amino-acid, $22,029\text{ Da}$ four-transmembrane protein sharing sequence similarity with rat RVP1 and mouse oligodendrocyte-specific protein (OSP). Northern blot and FACS analyses across five primate cell lines showed strict concordance between `CPE-R` expression, `H10PER` binding, and CPE sensitivity (present in Vero, Hep3B, and Intestine 407; absent in K562 and JY). Stable expression of `CPE-R` (or C-terminally FLAG-tagged `CPE-R`) in CPE-resistant L929 cells conferred high-affinity $^{125}\text{I-CPE}$ binding ($K_a = 1.49 \times 10^8\text{ M}^{-1}$ by Scatchard analysis), direct $22\text{ kDa}$ recognition in ligand overlay blots (competable by 100-fold cold CPE), morphological bleb-balloon sensitivity to $100\text{ ng/mL}$ CPE, and temperature-dependent ($37^\circ\text{C}$) assembly of CPE and `CPE-R` into the SDS-resistant high-molecular-weight pore complex.

This is a rigorous, classic receptor-identification study supported by orthogonal biochemical and gain-of-function lines of evidence. Only minor improvements in quantitative cytotoxicity readouts and database accession reporting for the newly cloned Vero cDNA are needed.

### 2. Methodological & Statistical Audit (STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT)

#### Strengths
* **Clever non-lytic probe strategy for expression cloning:** Using the non-cytotoxic C-terminal receptor-binding domain (`H10PER`, aa 184–319) as a biotinylated FACS probe avoided killing positive transfectants during library sorting while preserving receptor specificity (competable by unlabeled `H10PER`).
* **Complete gain-of-function and biochemical validation chain:** The authors establish sufficiency in resistant L929 cells (`Neo706` and `706FLAG`) via four independent assays: (1) flow cytometric surface binding; (2) equilibrium $^{125}\text{I-CPE}$ Scatchard binding ($K_a = 1.49 \times 10^8\text{ M}^{-1}$, matching native Vero receptor affinity); (3) direct in vitro ligand overlay on renatured SDS-PAGE blots with 100-fold cold competition; and (4) co-immunoprecipitation of FLAG-tagged `CPE-R` and intact CPE within the SDS-resistant high-MW complex at $37^\circ\text{C}$.
* **Domain and temperature specificity controls for pore complex assembly:** Showing that `H10PER` (lacking the N-terminal cytotoxic domain) coprecipitates with monomeric `CPE-R` but fails to form the high-MW SDS-resistant complex, and that complex formation with intact CPE is strongly promoted at $37^\circ\text{C}$ vs. $4^\circ\text{C}$ (Fig. 7A–B), directly links receptor-mediated complex assembly to cytotoxic pore formation.

#### Weaknesses & Methodological Audit
* **Qualitative rather than quantitative cytotoxicity endpoint:** Cytotoxic sensitivity in `Neo706` (`100 ng/mL` CPE) vs. parental L929 (`5 µg/mL` CPE) is demonstrated via phase-contrast micrographs of membrane blebbing (Fig. 5B) rather than a quantitative dose-response curve (e.g., $^{51}\text{Cr}$ release, LDH release, or vital dye exclusion across serial toxin dilutions with $\text{EC}_{50}$ and error bars).
* **Stoichiometry and additional host components of the high-MW complex remain unresolved:** As noted by the authors in the Discussion, while Figure 7B proves that both CPE and the $22\text{ kDa}$ `CPE-R` are present in the high-MW complex, SDS-PAGE co-immunoprecipitation does not resolve the exact oligomer stoichiometry or whether the previously reported $50$–$70\text{ kDa}$ cellular proteins are co-assembled or represent SDS-resistant `CPE`/`CPE-R` multimers.

### 3. Biological / Experimental Grounding & Claim Proportionality
* **Clone 706 (`CPE-R`) encodes a functional 209-aa, 22-kDa four-transmembrane receptor that binds CPE directly with high affinity ($K_a = 1.49 \times 10^8\text{ M}^{-1}$) and confers CPE sensitivity to resistant L929 cells:** `[Well Supported]` — Unambiguously demonstrated by cDNA sequencing, Northern blot correlation across 5 cell lines, Scatchard analysis, ligand overlay competition, and gain-of-function cytotoxicity in L929 cells.
* **Interaction of intact CPE (requiring its N-terminal domain) with `CPE-R` at $37^\circ\text{C}$ drives assembly of the SDS-resistant high-molecular-weight membrane complex:** `[Well Supported]` — Directly supported by `[35S]`methionine and anti-FLAG/anti-CPE co-immunoprecipitation comparing intact CPE vs. `H10PER` at $4^\circ\text{C}$ and $37^\circ\text{C}$ in `706FLAG` and parental L929 cells (Fig. 7A–B).
* **`CPE-R`, RVP1, and oligodendrocyte-specific protein (OSP) constitute a structurally conserved multigene family:** `[Well Supported]` — Supported by sequence alignment (67.8% identity / 95.6% similarity to rat RVP1; 28.7% identity / 63.8% similarity to mouse OSP) and hydropathy profiles showing four conserved transmembrane helices (later recognized as the claudin tight-junction protein family).

### 4. Reproducibility & Data Completeness
Cloning primers, restriction sites, vector backbones (`pETH10PER`, `pMEPyori18Sf(-)`, `pMEneo-CPE-R`, `pMEEB-CPE-R-FLAG`), expression/purification buffers, and immunoprecipitation conditions are thoroughly documented. Although the complete nucleotide and deduced amino acid sequences of `CPE-R` are printed in Figure 3B, the authors should also provide the GenBank/EMBL/DDBJ accession number for the newly sequenced monkey `CPE-R` cDNA (only the mouse OSP accession `U19582` is listed on line 154).
</Blinded Review: TIME_ANON_0727>
