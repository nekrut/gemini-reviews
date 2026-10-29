<Blinded Review: TIME_ANON_0844>
**Composite Score:** 7.0 / 10.0 (Rigor: 2.5/3.5 | Claims: 1.7/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** Over-Interpretation/Clinical
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 7.0/10
VERDICT: PASS
ESTIMATED_DECADE: 1990s

---

### 1. Executive Summary / SUMMARY
This tumor immunology and expression-cloning study (`TIME_ANON_0844`) reports the molecular cloning and characterization of the human squamous cell carcinoma (SCC) antigen gene `SART-1` (`GenBank AB006198`, `2,506 bp`, encoding an 800-amino-acid nuclear protein `SART-1_800` of ~125 kDa and a cytosolic 43-kDa protein `SART-1_259`), identified by screening a `KE4` esophageal SCC cDNA library in `VA13` (`SV40`-transformed fibroblast) recipient cells co-transfected with `HLA-A2601` using HLA-A2601-restricted CTLs (`KE4 CTL`). Through progressive exonuclease III deletion mutants (`D1–D6`), COS-7/VA13 co-transfection IFN-$\gamma$ ELISAs, Northern blotting across normal human tissues and cancer panels, rabbit polyclonal anti-`SART-1_800` and anti-`SART-1_259`/GST Western blotting of nuclear and cytosolic fractions across 54 cell lines/tissues, and screening of 26 synthetic nonapeptides followed by cold-target inhibition and $5\text{ }\mu\text{g/ml}$ peptide-pulsed PBMC CTL induction from HLA-A26 (`A2601`, `A2602`, `A2603`) cancer patients, the authors map three immunogenic HLA-A26-restricted nonapeptide epitopes (`SART-1_736-744` `KGSGKMKTE`, `SART-1_749-757` `KATPSSKKE`, and `SART-1_785-793` `VKLKQEKEA`). While the immunological cloning, deletion mapping, and CTL induction experiments are thorough and well controlled, the authors' molecular biological explanation for how the cytosolic 43-kDa `SART-1_259` protein is translated—invoking a prokaryotic **Shine-Dalgarno (`AGGAGG`) sequence** to drive $-1$ ribosomal frameshifting in human eukaryotic cells—is mechanistically erroneous.

### 2. Methodological & Statistical Audit / WEAKNESSES & METHODOLOGICAL AUDIT
- **Erroneous Invocation of a Prokaryotic Shine-Dalgarno (`AGGAGG`) Ribosomal Frameshifting Mechanism in Human Cells (Lines 52–53, 79, 89):**
  - When the authors expressed the `6C2` cDNA fragment in *Escherichia coli* (`pGEX`), they observed a 43-kDa protein (`SART-1_259` fused to GST) terminated at an out-of-frame stop codon at position `940` following an `AGGAGG` hexamer at positions `359–364` (`70 bp` downstream of the first `ATG` at `291`), and confirmed by Edman N-terminal microsequencing that the bacterially expressed protein began at the first `ATG` (`line 53`).
  - However, the authors then claim (lines 52, 79, 89) that human squamous cell carcinomas translate this 43-kDa cytosolic `SART-1_259` protein via **Shine-Dalgarno (`AGGAGG`)-mediated $-1$ ribosomal frameshifting**: *"The mechanism involved in generating the 43-kD SART-1_259 was suspected to be -1 frameshifting between the Shine-Dalgarno sequence (AGGAGG at base positions 359–364) and a premature stop codon at position 940"* (`line 79`).
  - In molecular biology, the Shine-Dalgarno (`AGGAGG`) sequence base-pairs with the 3' end of **prokaryotic 16S rRNA** (`CCUCCU`); **eukaryotic 18S rRNA lacks the anti-Shine-Dalgarno sequence**, and Shine-Dalgarno-driven frameshifting is an *E. coli* expression artifact (`pGEX` in bacteria) that does not operate in mammalian ribosomes! Furthermore, all three identified CTL epitopes recognized on human tumor cells (`736–744`, `749–757`, and `785–793`) reside in the C-terminal region (`aa 736–793`) of the canonical in-frame **800-aa nuclear `SART-1_800` (125-kDa) protein** (`nt 2496–2669`), NOT in the truncated 259-aa product! Thus, while the anti-`SART-1_259/GST` polyclonal antiserum cross-reacts with a 43-kDa band in human tumor cytosols (likely a proteolytic cleavage product, splice isoform, or cross-reactive band sharing the N-terminal 24 aa of `SART-1_800`), attributing it to eukaryotic Shine-Dalgarno frameshifting is a confusion of bacterial *E. coli* `pGEX` expression with human translation.
- **Statistical Testing:** Two-tailed Student's $t$-tests ($P < 0.05$, asterisks in Figures 1, 2, 5, 6, 7) are appropriately applied to triplicate IFN-$\gamma$ ELISA determinations (`pg/ml` and `% specific lysis`), though multiple-comparison corrections across the 26 screened nonapeptides (`Figure 5B`) are not applied.

### 3. Biological / Experimental Grounding & Claim Proportionality / STRENGTHS
- **Expression Cloning and Exonuclease Deletion Mapping of `SART-1` (`AB006198`) `[Well Supported]`:** Screening $2 \times 10^5$ cDNA clones in HLA-A2601-transfected `VA13` cells (`Figure 1`), demonstrating ubiquitous 2.6-kb mRNA expression paired with tumor/testis-preferential protein translation (`Figures 2–3`), and narrowing the antigenic region to `nt 2122–2692` (`aa 611–799`) via deletion mutants `D1–D6` (`Figure 5A`) are rigorously executed.
- **Identification and Functional Validation of `SART-1_736-744` (`KGSGKMKTE`) Across HLA-A26 Subtypes `[Well Supported]`:** Demonstrating dose-dependent peptide recognition down to $1\text{ nM}$ (`Figure 6A`), cold-target inhibition of `KE4` tumor lysis by peptide-pulsed `VA13` cells (`Figure 6B`), and in vitro priming of HLA-A2601, HLA-A2602, and HLA-A2603 patient PBMCs to lyse `HLA-A26+` SCC targets (`Figure 7`) provides solid preclinical immunology evidence.
- **Claim of Shine-Dalgarno `-1` Frameshifting in Human Tumor Cells `[Methodologically Flawed]`:** As detailed above, the Shine-Dalgarno mechanism only explains the recombinant `pGEX` artifact in *E. coli*, not mammalian translation.

### 4. Reproducibility & Data Completeness
- **Good Sequence and Reagent Reporting:** The full 2,506-bp sequence is deposited in GenBank (`AB006198`), all 26 synthetic nonapeptide sequences (`724–732` through `785–793`) are listed in Figure 5B, and HLA class I typing alleles and cell line origins are fully specified (`Reproducibility: 1.4/2.0`).
</Blinded Review: TIME_ANON_0844>
