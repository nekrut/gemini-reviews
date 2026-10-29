<Blinded Review: TIME_ANON_0624>
OVERALL_SCORE: 8.7/10
VERDICT: PASS
ESTIMATED_DECADE: 1990s
**Composite Score:** 8.7 / 10.0 (Rigor: 2.9/3.5 | Claims: 2.3/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.6/2.0)
**Scientific Core Score:** 7.1 / 8.0
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary (SUMMARY)
This experimental tumor immunology study identifies the first in vivo biological function for the IFN-$\gamma$- and LPS-inducible CXC ($\alpha$) chemokine `IP-10` (`CXCL10`). By cloning murine `IP-10` cDNA from IFN-$\gamma$-stimulated `RAW 264.7` macrophages into two distinct expression vectors (`MoLTR-IP10` and `Ig-IP10`) and stably transfecting two genetically and histologically distinct murine tumor lines—`J558L` plasmacytoma (`BALB/c` background) and `K485` *c-myc*-driven mammary adenocarcinoma (`FVB` background)—the authors demonstrate that constitutive IP-10 secretion (`~20` and `~150 ng/ml` per `2 \times 10^6` cells / `48 h`) has no effect on in vitro cell doubling time or morphology, but potently abrogates tumorigenicity in vivo in syngeneic immunocompetent mice (`0/14` and `2/16` for `J558L` transfectants vs `21/21` parental and `4/5` `NeoR` control; `0/8` for `K485-MoLTR-IP10` vs `5/6` `K485-NeoR` control). Crucially, this antitumor effect is completely abolished in congenitally athymic `nu/nu` mice (`12/16` and `12/16` tumor formation, matching controls), proving thymus/T-lymphocyte dependence. Furthermore, `1:1` co-injection of `IP-10`-secreting and non-secreting `J558L-NeoR` tumor cells leads to rejection of both populations (`0/5` and `1/5` vs `4/5` control), establishing a non-cell-autonomous host effector mechanism accompanied by perivascular diapedesis and dense infiltration of lymphocytes, monocytes, and neutrophils at the tumor site.

### 2. Methodological & Statistical Audit (STRENGTHS, WEAKNESSES & METHODOLOGICAL AUDIT)
- **Rigorous Biochemical and Genetic Controls:**
  - To rule out promoter/vector artifacts, insertion-site clonal anomalies, or strain-restricted idiosyncrasies, the authors tested two independent transcriptional regulatory elements (`MoLTR` and lymphoid-specific `Ig` heavy-chain enhancer/promoter) across two unrelated tumor histologies (`J558L` plasmacytoma in `BALB/c` mice and `K485` mammary adenocarcinoma in `FVB` mice) alongside both untransfected parental lines and `pSV7Neo` (`NeoR` alone) mock-transfected clones isolated through two rounds of limiting dilution.
  - Because existing anti-human IP-10 antisera did not cross-react with murine IP-10, the authors purified both C-terminally (`IP-10-[His]6`) and N-terminally (`[His]6-IP-10`) tagged recombinant mIP-10 to homogeneity via $\text{Ni}^{2+}$-agarose and Mono-S FPLC / RP-HPLC, immunized rabbits sequentially with both constructs to ensure recognition of native termini, and verified by `[^{35}\text{S}]`methionine metabolic labeling and Tris/Tricine SDS-PAGE immunoprecipitation that tumor-secreted mIP-10 (`6–7 kDa` proteolytically processed doublet) comigrated exactly with endogenous mIP-10 secreted by IFN-$\gamma$-stimulated `RAW 264.7` macrophages (`Figure 1c`).
- **Omission of Formal Contingency-Table $P$-Values in `Tables 2–4`:**
  - While `Tables 2, 3, and 4` report exact tumor incidence fractions (`0/14` and `2/16` vs `21/21` and `4/5` in `Table 2`; `0/8` vs `5/6` in `Table 3`; `0/5` and `1/5` vs `4/5` in `Table 4`), the authors do not print formal Fisher's exact test $p$-values in the text or tables. However, auditing the raw counts via two-tailed Fisher's exact tests confirms overwhelming statistical significance across all primary comparisons: `J558L-MoLTR-IP10` vs `None` ($0/14$ vs $21/21$, $p = 2.4 \times 10^{-10}$) and vs `NeoR` ($0/14$ vs $4/5$, $p = 0.0011$); `J558L-Ig-IP10` vs `None` ($2/16$ vs $21/21$, $p = 3.5 \times 10^{-8}$) and vs `NeoR` ($2/16$ vs $4/5$, $p = 0.011$); `BALB/c` vs `nu/nu` for `MoLTR-IP10` ($0/14$ vs $12/16$, $p = 2.4 \times 10^{-5}$); `K485-MoLTR-IP10` vs `NeoR` ($0/8$ vs $5/6$, $p = 0.0030$); and `1:1 mix MoLTR-IP10 + NeoR` vs `NeoR alone` ($0/5$ vs $4/5$, $p = 0.0476$).
- **Morphological Leukocyte Identification and 14–28 Day Endpoint Window:**
  - Tumor-infiltrating leukocytes (`Figure 3`) were classified morphologically on H&E-stained paraffin sections (`day 1` through `day 14`) rather than by immunohistochemical surface phenotyping (`CD4+`, `CD8+`, `NK`, `Mac-1`, `Gr-1`), and animals in the `1:1` bystander mixing experiment (`Table 4`) were autopsied at `14 days` without long-term survival tracking or systemic contralateral tumor re-challenge to test for durable immunologic memory.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1: Tumor-derived murine IP-10 has no direct autocrine growth-inhibitory effect in vitro but potently suppresses plasmacytoma and mammary adenocarcinoma growth in vivo** — `[Well Supported]`. Demonstrated across two tumor models, two mouse strains, and two expression vectors with matched `NeoR` controls.
- **Claim 2: The in vivo antitumor activity of IP-10 is thymus/T-cell dependent and non-cell-autonomous** — `[Well Supported]`. Proven by complete loss of tumor rejection and inflammatory infiltration in athymic `nu/nu` mice (`Table 2`) and by bystander eradication of co-injected `NeoR` non-producer tumor cells (`Table 4`).
- **Claim 3: Neutrophil recruitment to IP-10-secreting tumors in immunocompetent mice is likely secondary to T-cell recruitment/activation rather than direct CXC neutrophil chemotaxis** — `[Well Supported]`. Insightfully reasoned from the absence of neutrophil infiltration in `nu/nu` mice (despite functional neutrophils in `nu/nu` mice in G-CSF models) and corroborated by in vitro chemotaxis studies cited in the Discussion and Note Added in Proof.

### 4. Reproducibility & Data Completeness
- **Experimental Transparency:** Oligonucleotide primer sequences (`nt 1–17` and `362–379`), vector maps, prokaryotic purification and immunization protocols, ELISA kinetic rates (`mOD/min ± SD`, `Table 1`), cell inoculum doses (`2 \times 10^6` cells), tumor mass thresholds (`>= 0.5 g`), and animal counts across all 7 compiled experiments are documented in exemplary detail.
</Blinded Review: TIME_ANON_0624>
