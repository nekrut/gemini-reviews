<Blinded Review: TIME_ANON_0679>
**Composite Score:** 4.5 / 10.0 (Rigor: 1.5/3.5 | Claims: 0.9/2.5 | Biology: 1.1/2.0 | Reproducibility: 1.0/2.0)
**Bias Category:** Over-Interpretation/Clinical
**Verdict:** Major Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Translational/Preclinical/Biomarker

OVERALL_SCORE: 4.5/10
VERDICT: CAVEATS
ESTIMATED_DECADE: 2020s

---

### 1. Executive Summary / SUMMARY
This study describes the construction, rescue, and *in vitro* characterization of a recombinant avian orthoavulavirus 1 (`rAOaV-1`, formerly Newcastle disease virus, avirulent strain compressed under accession `MN905722`) engineered to express the full-length codon-optimized spike (S) glycoprotein of SARS-CoV-2 (`rAOaV-1-SARS-CoV-2`) inserted as an independent transcription unit between the phosphoprotein (P) and matrix (M) genes. The authors rescue the chimeric virus in Vero cells and embryonated chicken eggs, verify expression of the S and HN proteins in infected Vero cells by Western blot and double-label confocal immunofluorescence, show that `rAOaV-1-SARS-CoV-2` replicates more slowly than wild-type `wtAOaV-1` in Vero cells without exogenous trypsin, evaluate neutralization of the recombinant virus by convalescent mouse anti-SARS-CoV-2 serum ($\sim 40\%$ spot reduction) versus chicken anti-AOaV-1 serum ($\sim 90\%$ reduction), and assess genetic stability across 5 serial passages in embryonated eggs. While the reverse genetics rescue and basic *in vitro* antigen expression are straightforward, the manuscript suffers from severe clinical/translational over-claiming (asserting safety, primate attenuation, and vaccine efficacy with **zero animal or immunogenicity experiments**), internal contradictions regarding ribozyme architecture (`HHRz + HdvRz` vs. dual `HHRz`), and unedited copy-paste duplication in the Materials and Methods section.

### 2. Methodological & Statistical Audit / WEAKNESSES & METHODOLOGICAL AUDIT
- **Severe Translational Over-Claiming Without Any *In Vivo* or Immunogenicity Data:**
  - The Abstract (Line 17) concludes: *"Taken together, the presented respiratory vaccine candidate is highly attenuated in primates per se, safe and lacking pre-existing immunity in human."* Similarly, the Discussion (Line 128) states that *"Here, we applied the reverse genetics inline with multiple morphological and biochemical assays to establish vaccine capability, physiological sustainability and simplicity in culturing tools for tuning single vaccine cytotoxicity."*
  - In reality, **not a single animal experiment** (no mice, hamsters, chickens, or non-human primates), **no immunogenicity assay** (no vaccination or measurement of induced anti-S binding or neutralizing antibodies or T-cell responses), and **no standard avian pathogenicity/safety test** (such as intracerebral pathogenicity index [ICPI] in 1-day-old chicks or mean death time [MDT] in eggs) was performed in this study! Claiming that this specific chimeric construct (which expresses a functional heterologous coronavirus Spike protein capable of mediating trypsin-independent entry on its surface) is "safe" and "attenuated in primates" without any *in vivo* safety or tropism testing is scientifically unfounded—especially since incorporating functional SARS-CoV-2 S onto the surface of an enveloped paramyxovirus could alter cellular tropism toward ACE2-expressing human respiratory or endothelial cells.
- **Unedited Copy-Paste Duplication and Contradiction in the Western Blot Protocol (Line 51):**
  - Under *"Western Blot Analysis"* (Line 51), the paragraph reads:
    > *"The virus or control-treated hypertonic lysates were boiled in SDS-PAGE buffer so that loads with constant amounts could be unnaturalized at 98°C for 8 min... Following the electrophoretic protein extraction, proteins shifted to **nitrocellulose** membranes... Subsequently, the cell lysates were centrifuged at 14,000 rpm for 10 min after maximum incubation for 30 min on ice. Next, the collected supernatants were mixed with equivalent 2x loading buffer and boiled to denature the protein at 98°C for 5 min. Alongside, the constant amounts of proteins were loaded onto 10% SDS-PAGE to separate different size protein, shifted onto **PVDF** membrane."*
  - This paragraph stitches together two conflicting Western blot protocols back-to-back (boiling 8 min + transfer to nitrocellulose, immediately followed by centrifuging lysates again + boiling 5 min + transfer to PVDF)!
- **Internal Contradiction in Antigenome Ribozyme Design (Line 37 vs. Line 79 & Figure 1A):**
  - In Materials and Methods (Line 37), the rescue plasmid is described as containing *"the hammerhead ribozyme (HHRz) introduced at 5'-end and rotated symmetry ribozyme from hepatitis delta virus (HdvRz) placed at the 3'-end of the antigenome."*
  - However, in Results (Line 79) and the caption to Figure 1A (Line 83), the authors state the exact opposite: *"whereas a hammerhead ribozyme sequence was introduced in **both 5' and 3'-ends** of the antigenome to ensure tight adherence to the 'rule of six'."*
- **Inadequate Quantification of Virion Incorporation and Genetic Stability:**
  - Although the authors claim that SARS-CoV-2 S is incorporated into the surface of `rAOaV-1-SARS-CoV-2` virions (inferred indirectly from a $\sim 40\%$ reduction in fluorescent spots by mouse anti-SARS-CoV-2 serum in Figure 2E and trypsin-independent multi-cycle spread in Vero cells), Western blotting was performed only on **whole-cell lysates** (Figure 1B, loaded with $\beta$-actin control) rather than purified sucrose-gradient virions, and no immunogold electron microscopy was performed.
  - Furthermore, in Figure 3B (genetic stability across passages P1–P5), no loading control ($\beta$-actin or viral NP/HN) is included alongside the S protein Western blot, and no Sanger/NGS sequencing of P5 viral RNA was performed to verify the absence of nonsense or frameshift mutations in the S transgene.

### 3. Biological / Experimental Grounding & Claim Proportionality / STRENGTHS
- **[Well Supported] Successful Rescue and Co-Expression of SARS-CoV-2 Spike and AOaV-1 HN in Infected Vero Cells:** Reverse genetics rescue, double-label confocal immunofluorescence (Figure 1C), and Western blot of infected cell lysates (Figure 1B) demonstrate that full-length S protein ($\sim 180\text{ kDa}$ uncleaved and $\sim 90\text{ kDa}$ cleaved S1/S2) is expressed alongside viral HN.
- **[Moderately Supported] Functional Contribution of S Protein to Trypsin-Independent Entry and Partial Neutralization Sensitivity:** The ability of `rAOaV-1-SARS-CoV-2` (and `wtAOaV-1`) to replicate in Vero cells without exogenous trypsin and the partial ($\sim 40\%$) reduction in infection by mouse anti-SARS-CoV-2 serum suggest that S protein is present on virions and partially contributes to entry alongside HN/F, though purified virion immunoblotting is needed.
- **[Overstated] Claims of Vaccine Efficacy, Primate Attenuation, and Safety:** Completely unsupported by experimental data in this manuscript, as no animal immunogenicity, challenge, or safety studies were conducted.

### 4. Reproducibility & Data Completeness
- **Reproducibility Assessment:** The parental viral genome accession (`MN905722`) and SARS-CoV-2 S gene accession (`MN908947`) are provided, along with the gene-start (`ACAGAGAATGCG`) and gene-end (`TTAGAAAAAA`) transcriptional signals and PmeI cloning site (`GTTTAAAC`). However, the conflicting Western blot and ribozyme descriptions in the Methods section and the lack of exact antibody catalog numbers/dilutions detract from reproducibility.
</Blinded Review: TIME_ANON_0679>
