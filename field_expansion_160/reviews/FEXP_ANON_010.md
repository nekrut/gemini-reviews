# Review of FEXP_ANON_010

**Overall Score:** **4.4 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **3.3 / 8.0**  
* **Score Breakdown:** Rigor: 1.1/3.5 | Claims: 1.0/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.1/2.0

---

## 1. Blinded Metadata Perception
* **Anonymized Manuscript ID:** `FEXP_ANON_010`
* **Perceived Domain & Design:** Avian viral surveillance and molecular epidemiology; cloacal swab RT-PCR screening ($n = 28$ wild birds across 4 species in 3 Egyptian Nile Delta governorates), egg CAM isolation ($n = 3$ positives), Sanger sequencing of full-length VP2 (`MT304668–MT304670`), `RAxML` phylogenetic reconstruction, and `SNAP` pairwise $d_N/d_S$ estimation for Infectious Bursal Disease Virus (IBDV).
* **Blinding Integrity:** Double-blind review maintained; evaluated strictly on internal data consistency, methodological rigor, and biological plausibility at $t_0$.

---

## 2. Executive Summary & Editorial Verdict

This short surveillance paper screens 28 cloacal swabs collected in 2019 from free-living wild birds across three Nile Delta governorates in Egypt (Monofiya, Qalyubia, and Sharkia) for Infectious Bursal Disease Virus (IBDV). Three of the 28 swabs tested positive by VP2 RT-PCR, were isolated on the chorioallantoic membrane (CAM) of SPF embryonated chicken eggs (causing embryo mortality at day 5), and underwent full-length VP2 Sanger sequencing (`MT304668–MT304670`). Maximum-likelihood phylogenetic analysis (`RAxML` GTR) and pairwise identity plots (`SDT`) show that one isolate (`IBDV/USC-1/2019` / `Egypt-USC-IBD-1-2019`) clusters with Egyptian commercial poultry very virulent IBDV (vvIBDV) strains (carrying the `326-SWSASGS-332` heptapeptide and mutations `P222A`, `V256I`, `N279D`, `L294I`, `N299S`, plus a novel `G254S`), while the other two isolates (`USC-2` and `USC-3`) cluster with cell-culture-adapted commercial live attenuated vaccine strains. The authors also run `SNAP` to plot cumulative synonymous and nonsynonymous substitutions across VP2.

**Editorial Verdict: Reject / Major Revision Required (Flawed / Overstated).** While detecting a vvIBDV-like strain and two live-vaccine-like IBDV strains in wild birds near Egyptian poultry farms is a plausible field observation, the manuscript exhibits a **severe internal data integrity contradiction between the Abstract and the Methods/Results/Table 1 regarding which bird species were actually sampled**, alongside major methodological and editorial defects:
1. **Direct contradiction in the four wild bird species sampled:** The Abstract (line 5) explicitly states that the 28 cloacal swabs were collected from *"four species of free-living Egyptian wild birds (i.e. mallard duck, bean goose, white-fronted goose and black-billed magpie)."* Yet Table 1 (lines 26–43) and the Results (line 60) state that the 28 swabs came from *Anas crecca* (**green-winged teal**, $n=8$), *Anas platyrhynchos* (**mallard**, $n=7$), *Bubulcus ibis* (**cattle egret**, $n=6$), and *Coturnix coturnix* (**common quail**, $n=7$), with the three positive isolates coming from two cattle egrets (*B. ibis*) and one green-winged teal (*A. crecca*)! Neither bean goose (*Anser fabalis*), white-fronted goose (*Anser albifrons*), nor black-billed magpie (*Pica hudsonia*, a North American species not native to Egypt!) appears anywhere in Table 1 or the Results.
2. **Invalid codon-level selection claims from `SNAP` cumulative $d_N/d_S$ curves:** The authors use `SNAP` (a simple Nei-Gojobori pairwise Jukes-Cantor counting tool from 2000) on 3 sequences + references to claim *"sites under positive or negative selection were mapped"* and *"high selection pressures in peak A and B... decide the magnitude of virulence, pathogenicity and characterization of IBV [sic]"* (line 62), without any statistical test ($p$-value or posterior probability) or site-specific ML/Bayesian selection model (`MEME`, `FEL`, `FUBAR`, `PAML`).

### Assessment of Specific Claims
* **Claim 1 (28 cloacal swabs were collected from mallard duck, bean goose, white-fronted goose, and black-billed magpie [Abstract line 5] vs. green-winged teal, mallard, cattle egret, and common quail [Table 1 & Results line 60]): [Methodologically Flawed].**  
  An irreconcilable factual contradiction in the primary biological metadata of the study. Three of the four species named in the Abstract do not match the species in Table 1 or Results, and the two positive host species in Table 1 (*Bubulcus ibis* and *Anas crecca*) are not even mentioned in the Abstract.
* **Claim 2 (One wild-bird isolate [`Egypt-USC-IBD-1-2019`] is genetically closely related to Egyptian poultry vvIBDV strains, and two isolates [`USC-2`, `USC-3`] are closely related to commercial live-attenuated vaccine strains): [Moderately Supported].**  
  The three VP2 sequences (`MT304668–MT304670`) cluster with Egyptian vvIBDV and vaccine reference clades on the `RAxML` VP2 tree (Figure 1). However, Segment B (encoding the VP1 polymerase, which is essential for pathotype and reassortment classification in birnaviruses) was not sequenced, and passage in SPF embryonated chicken eggs prior to sequencing (line 46) was not controlled against direct swab sequencing to rule out laboratory cross-contamination or egg-passage selection of `G254S`.
* **Claim 3 (`SNAP` analysis demonstrates high positive selection pressures in hydrophilic peaks A and B of VP2): [Methodologically Flawed].**  
  `SNAP` only computes cumulative pairwise Jukes-Cantor-corrected $d_S$ and $d_N$ moving along the sequence (Figure 2c). It does not account for phylogenetic structure, transition/transversion bias, or codon-level rate variation, and provides no site-specific $p$-values. Moreover, Figure 2c clearly shows cumulative $d_S \gg d_N$ across the VP2 gene (purifying selection).
* **Claim 4 ("Since serotype I of IBDV is known to be a pathogenic [sic: apathogenic] in avian species other than chicken, it become clear that IBDV didn't assume a significant role in the bird's deaths" [line 67]): [Methodologically Flawed].**  
  In line 44, the authors stated that the samples were collected from *"live wild birds"* ("Capturing and sampling from live wild birds..."), yet in line 67 they suddenly refer to *"the bird's deaths"*!

---

## 3. Forensic Defect Inventory

1. **Pillar 2, 6 & 7 Violation — Severe Metadata Contradiction on Sampled Host Species and Live vs. Dead Birds (Abstract line 5 vs. Table 1 lines 26–43 vs. Results lines 60, 67):**  
   * **Host species mismatch:** Abstract (line 5) lists *"mallard duck, bean goose, white-fronted goose and black-billed magpie."* Table 1 and Results (line 60) list *Anas crecca* (green-winged teal), *Anas platyrhynchos* (mallard), *Bubulcus ibis* (cattle egret), and *Coturnix coturnix* (common quail). Note that the black-billed magpie (*Pica hudsonia*) is native to western North America, not the Egyptian Nile Delta (and even the Eurasian magpie *Pica pica* does not occur in the Nile Delta), strongly suggesting copy-paste text from another study's abstract.
   * **Live vs. dead birds contradiction:** Methods line 44 states *"Capturing and sampling from live wild birds were carried out..."*, and line 67 states *"wild birds... can shed the virus without developing disease"*, but two sentences later (line 67) states *"it become clear that IBDV didn't assume a significant role in the bird's deaths"*!
2. **Pillar 3 & 4 Violation — Misuse of Pairwise `SNAP` Counts to Claim Site-Specific Positive Selection Without Statistical Support (Methods line 53, Results lines 62, 67):**  
   Pairwise Nei-Gojobori counts in `SNAP` treat all $N(N-1)/2$ sequence pairs as independent, ignoring shared phylogenetic branches, and do not provide site-level hypothesis tests. Claiming "sites under positive or negative selection were mapped" and "high selection pressures in peak A and B" without any site-level $d_N/d_S$ values, $p$-values, or phylogenetic codon models (`FEL`/`MEME`/`FUBAR`/`CodeML`) is statistically invalid.
3. **Pillar 5 & 6 Violation — Segment A (VP2) Only Sequencing and Uncontrolled Egg-Passage Prior to Sequencing (Methods line 46, Results line 72):**  
   Virulence of IBDV requires both Segment A (VP2) and Segment B (VP1), as naturally occurring vvIBDV-VP2 / attenuated-VP1 reassortants circulate widely in Egypt. Furthermore, full-length VP2 sequencing was performed only *after* 5-day passage in SPF embryonated chicken eggs (`CAMs were harvested from dead embryos`, line 46) rather than directly from the original cloacal swab RNA, meaning the single reported unique substitution (`G254S`, line 72) could be an egg-adaptation artifact.
4. **Pillar 7 Violation — Pervasive Nomenclature, Virus Acronym, and Antibiotic Concentration Errors:**  
   * **Wrong virus acronym in Results:** Line 62 writes *"decide the magnitude of virulence, pathogenicity and characterization of **IBV**"* (Infectious Bronchitis Virus, a coronavirus) instead of **IBDV**.
   * **Impossible antibiotic concentration in viral transport medium:** Line 44 states that PBS was supplemented with `200 mg/ml Gentamicin, and 4 mg/ml Amphotericin B` (which is $20\%\text{ w/v}$ gentamicin—$1,000\times$ higher than the standard $200\,\mu\text{g/mL}$ and $4\,\mu\text{g/mL}$!).
   * **Inconsistent isolate naming across text and figures:** The same three isolates are referred to as `IBDV/USC-1/2019`, `IBDV/USC-2/2019`, `IBDV/USC-3/2019` in the Abstract (line 5) and Figure 2d legend (line 67), but as `Egypt-USC-IBD-1-2019`, `Egypt-USC-IBD-2-2019`, `Egypt-USC-IBD-3-2019` in the Results (lines 60, 62, 67, 72) and Figure 2a,b legend.
   * **Figure 1 legend error:** Line 62/65 states *"One of the reported isolates clustered within vvIBDVs... while the other one clustered vaccine strains"* (accounting for only 2 of the 3 isolates).

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **1.1** | **3.5** |Tiny convenience sample ($N=28$ total across 4 species, $n=3$ positives), VP2-only sequencing after egg passage without Segment B, and invalid use of pairwise `SNAP` plots to claim site-specific positive selection without statistical tests. |
| **2. Claim-to-Evidence Alignment** | **1.0** | **2.5** | Claims of positive selection in peaks A/B are unsupported by `SNAP`, and the Abstract's description of the study hosts directly contradicts the data in Table 1. |
| **3. Data Integrity & Biological/Behavioral Plausibility** | **1.2** | **2.0** | Major internal contradiction in sampled bird species (bean goose, white-fronted goose, black-billed magpie in Abstract vs. green-winged teal, cattle egret, common quail in Table 1) and live capture (line 44) vs. "the bird's deaths" (line 67). |
| **4. Reproducibility & Data Integrity** | **1.1** | **2.0** | The 3 VP2 sequences are deposited in GenBank (`MT304668–MT304670`), but the manuscript is marred by severe metadata contradictions, `IBV` vs. `IBDV` confusion (line 62), `200 mg/ml` gentamicin unit error (line 44), and inconsistent strain IDs. |
| **Total Composite Score** | **4.4** | **10.0** | **Flawed / Overstated** (Scientific Core Score: **3.3 / 8.0**) |

---

### Constructive and Doable Suggestions for Improvement

1. **Resolve the Fundamental Contradiction in Sampled Wild Bird Species and Live/Dead Status:**  
   * **WHY:** Listing bean goose, white-fronted goose, and black-billed magpie in the Abstract while presenting green-winged teal, cattle egret, and common quail in Table 1 and Results invalidates the basic provenance of the samples.  
   * **WHAT & HOW:** Verify the original field collection logs and GenBank source modifiers for `MT304668–MT304670`, correct the Abstract (line 5) to match the actual sampled species in Table 1, and clarify whether the birds in line 67 were live-captured or found dead.
2. **Replace `SNAP` Pairwise Plots with Phylogeny-Aware Codon Selection Models (`FEL` / `MEME` / `FUBAR`):**  
   * **WHY:** `SNAP` does not perform statistical hypothesis testing for positive selection at individual codons or account for phylogenetic relatedness.  
   * **WHAT & HOW:** Run `FEL`, `MEME`, and `FUBAR` (via Datamonkey/HyPhy) on the VP2 codon alignment used for Figure 1, and report the actual $d_N/d_S$ ($\omega$) estimates and $p$-values / posterior probabilities for codons in hydrophilic peaks A and B.
3. **Compare Direct Swab VP2 Amplicons Against Egg-Passaged CAM Amplicons and Fix Editorial Errors:**  
   * **WHY:** Passaging field swabs in SPF chicken embryos for 5 days can select for host-adaptation mutations (such as `G254S`) not present in the wild bird.  
   * **WHAT & HOW:** Sequence the 743-bp screening RT-PCR product amplified directly from the original cloacal swab RNA (line 44) to verify that `G254S` was present prior to egg inoculation. Correct `IBV` $\to$ `IBDV` (line 62), `200 mg/ml Gentamicin, and 4 mg/ml Amphotericin B` $\to$ `200 μg/ml Gentamicin, and 4 μg/ml Amphotericin B` (line 44), and standardize isolate names across the text and figures.
