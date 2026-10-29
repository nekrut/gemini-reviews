<Blinded Review: TIME_ANON_0959>
**Composite Score:** 8.0 / 10.0 (Rigor: 2.8/3.5 | Claims: 2.1/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Translational/Preclinical/Biomarker

OVERALL_SCORE: 8.0/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This antiviral pharmacology and host-dependency study investigates the inhibition of human coronavirus `HCoV-NL63` replication in Caco-2 cells by immunosuppressive immunophilin ligands (cyclosporine A `CsA`, `CsD`, and `FK506`), clinically advanced non-immunosuppressive `CsA` derivatives (`Alisporivir/Debio-025` and `NIM811`), five newly synthesized position-1-modified non-immunosuppressive `CsA` derivatives (`compounds 1–5`), and a novel C-21-modified non-immunosuppressive `FK506` derivative (`compound 6`). Using a high-throughput quantum-dot double-antibody sandwich `N`-protein ELISA (`virospot` assay), plaque reduction assays, and viral RNA qRT-PCR alongside `CellTiter-Glo` / `MTT` cell viability controls, the authors show that all tested compounds potently inhibit `HCoV-NL63` replication in the low micromolar range ($\text{EC}_{50} = 0.8\text{–}8.1\ \mu\text{M}$, with `Alisporivir` and `NIM811` achieving $\text{EC}_{50} = 0.8\ \mu\text{M}$ and `compound 3` achieving $\text{EC}_{50} = 1.1\ \mu\text{M}$).

Crucially, the authors pair antiviral profiling with biochemical and cellular orthogonal assays: (1) chymotrypsin-coupled peptidyl-prolyl *cis-trans* isomerase (`PPIase`) inhibition assays against recombinant human `CypA` and `FKBP12`; (2) ternary calcineurin (`CnA`) phosphatase inhibition assays; (3) PMA/ionomycin-stimulated `NFAT`-luciferase reporter assays in Jurkat T cells; (4) `NFAT3-GFP` nuclear translocation microscopy; and (5) lentiviral shRNA knockdown of `CypA` (`PPIA`, 97% protein knockdown) vs. `CypB` (`PPIB`, 98% protein knockdown) in single-cell-cloned Caco-2 cells. The shRNA experiments definitively demonstrate that `HCoV-NL63` replication requires host `CypA` (`PPIA`)—whose depletion reduces viral titers by >2.5 $\log_{10}$ to near the detection limit—and is completely independent of `CypB` (`PPIB`).

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### Strengths
1. **Orthogonal Biochemical, Cellular, and Genetic Dissection of Mechanism:** Rather than relying solely on pharmacological inhibitors (which can have off-target effects on ABC transporters or membranes at micromolar concentrations), the authors establish the host factor requirement genetically using stable single-cell-cloned Caco-2 lines with near-complete knockdown of `CypA` (`97%` reduction by quantitative Western blot normalized to $\beta$-actin) and `CypB` (`98%` reduction), verified across 5 independent single-cell clones per target.
2. **Comprehensive Decoupling of Antiviral Potency from Calcineurin/NFAT Immunosuppression:** By testing `CsA`, `CsD`, `Alisporivir`, `NIM811`, `compounds 1–5`, `FK506`, and `compound 6` across enzymatic `PPIase` (`CypA`/`FKBP12`), biochemical calcineurin (`CnA`), Jurkat `NFAT`-luciferase, and `NFAT3-GFP` nuclear import assays (`Table 2`), the authors prove that antiviral activity against `HCoV-NL63` tracks with cyclophilin/FKBP binding and is wholly independent of calcineurin inhibition.
3. **Multi-Readout Antiviral Validation (Protein ELISA + Plaque Assay + Viral RNA qRT-PCR + Viability):** Antiviral $\text{EC}_{50}$ values from the `N`-protein quantum-dot ELISA (`Fig. 3A`, `Table 2`) are corroborated by direct infectious virus plaque titration (`Fig. 1A`) and intracellular viral RNA copy number reduction (`Fig. 3B` for `CsA`, `Alisporivir`, `NIM811`, `3`, `FK506`, `6`), paired with ATP (`CellTiter-Glo`) and `MTT` viability curves over the full `0–20 uM` range (`Fig. 3A`, `Fig. S2`).

#### Weaknesses & Internal Table/Text Discrepancies
1. **Unit Error in Table 2 for `CsA` NFAT-Luciferase Reporter $\text{IC}_{50}$ (`nM` vs. `uM`):**
   - In `Table 2`, the fourth column header is labeled **`IC50 [uM] of NFAT reporter gene activity in Jurkat cells`**, and the entry for `CsA` is given as **`1.6 ± 0.0003`**.
   - However, in Results line 105, the text states: *"Only the parental compound CsA (IC50 1.6 nM) and the recursive derivative 1 (IC50 227 nM) exerted pronounced effects on reporter gene expression."* Furthermore, in `Figure 2B`, the `CsA` curve inhibits `NFAT` reporter activity by >50% at $0.0016\ \mu\text{M}$ ($1.6\text{ nM}$) and reaches ~0% activity by $0.01\ \mu\text{M}$. Thus, `CsA`'s $\text{IC}_{50}$ is **$1.6\text{ nM}$** ($0.0016\ \mu\text{M}$), and `compound 1`'s $\text{IC}_{50}$ (`0.23 ± 0.13 uM` = `230 nM`) is correctly in $\mu\text{M}$, meaning the `CsA` entry in `Table 2` was entered in `nM` (`1.6`) under a `[uM]` column header (off by $1,000\times$ relative to the column unit, while its SD `± 0.0003` was in $\mu\text{M}$!).
2. **Inconsistency in Cell Line Name for `NFAT-GFP` Translocation Assay (`HeLa` vs. `HEK-293` vs. `HeLa 93`):**
   - Methods line 50 states: *"HeLa cells stably transfected with NFAT3-GFP... were cultured in DMEM..."* and the `Figure 2C` caption states *"HeLa cells stably expressing NFAT-GFP..."*
   - However, the `Table 2` column header states: **`NFAT-GFP Translocation in HEK-293 cells`**, and Results line 107 refers to them as **`HeLa 93 cells`** (an apparent typographical chimera of `HeLa` and `HEK-293`).
3. **Lack of Genetic Knockdown Rescue or `FKBP` Knockdown Specificity:** While `CypA` (`PPIA`) knockdown reduces `HCoV-NL63` replication by >99%, the authors did not perform an shRNA-resistant `PPIA` cDNA rescue (though testing 5 independent single-cell clones substantially mitigates off-target clonal drift) and did not identify which specific `FKBP` family member mediates the antiviral effect of `FK506` and non-immunosuppressive `compound 6` (noting that `compound 6` has weak affinity for `FKBP12`, $K_i \approx 1,861\text{ nM}$, yet inhibits `HCoV-NL63` with $\text{EC}_{50} = 4.2\ \mu\text{M}$).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** Non-immunosuppressive `CsA` derivatives (`Alisporivir`, `NIM811`, `compounds 1–5`) and the non-immunosuppressive `FK506` derivative (`compound 6`) potently inhibit `HCoV-NL63` replication in Caco-2 cells ($\text{EC}_{50} = 0.8\text{–}8.1\ \mu\text{M}$) without cytotoxicity up to $20\ \mu\text{M}$. `[Well Supported]`
- **Claim 2:** Cyclophilin A (`PPIA`), and not Cyclophilin B (`PPIB`), is an essential host factor for `HCoV-NL63` replication in Caco-2 cells. `[Well Supported]`
- **Claim 3:** The antiviral activity of `compound 6` despite ~70-fold reduced `FKBP12` PPIase inhibition suggests that another `FKBP` isoform (or a non-`FKBP12` target) participates in `HCoV-NL63` replication. `[Moderately Supported]` — Appropriately framed as a hypothesis in the Discussion.

### 4. Reproducibility & Data Completeness
- **Chemical & Experimental Detail:** Full chemical names (`Table 1`), lentiviral `MISSION` shRNA clone IDs (`TRCN0000049228`–`232` for `PPIA`, `TRCN0000049248`–`252` for `PPIB`), qRT-PCR primers/TaqMan probe for `HCoV-NL63` (`NL63F2`, `NL63R2`, `NL63P2`), and enzymatic assay constants are completely reported.
- **Minor Corrections Needed:** Fix the `1.6` (`nM` vs `uM`) unit entry for `CsA` in `Table 2` and harmonize the `HeLa` vs `HEK-293` / `HeLa 93` cell line label.
</Blinded Review: TIME_ANON_0959>
