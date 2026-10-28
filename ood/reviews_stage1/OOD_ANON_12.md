# Review of OOD_ANON_12

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **3.8 / 10.0** (Flawed / Overstated)  
* **Score Breakdown:** Rigor: 1.0/3.5 | Claims: 0.9/2.5 | Biology: 1.0/2.0 | Reproducibility: 0.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study uses a commercial deep-learning molecular transformer drug–target interaction (MT–DTI) service to screen ~83,000 compounds for putative antagonists of endothelin receptor type B (EDNRB) and agonists of adiponectin receptor 1 (ADIPOR1) for cosmetic skin-radiance formulations. From ~3,000 and ~2,000 predicted hits, the authors manually select cyanocobalamin (Vitamin B12, VitB12) and disodium adenosine triphosphate (ATP), respectively. They evaluate VitB12 in MNT-1 and B16F10 melanoma cells (measuring Fluo-4 $\text{Ca}^{2+}$ fluorescence, melanin content, and *MC1R*/*MITF* mRNA upon endothelin-1 stimulation), ATP in Hs68 fibroblasts (measuring *COL1A1* and *ELN* mRNA and scratch-wound migration with and without the AMPK inhibitor dorsomorphin), and a VitB12 + ATP complex in HaCaT keratinocytes (*HAS2*/*HAS3* mRNA and HAS2 immunofluorescence) as well as in a 4-week, 31-participant split-face clinical study measuring facial gloss, Cutometer R2 elasticity, and Antera 3D roughness. Raw data and model weights/code are not publicly available.

Despite combining computational screening, *in vitro* cellular assays, and a human split-face trial, the study's central mechanistic claims—that VitB12 acts as a direct EDNRB antagonist and extracellular ATP acts as a direct ADIPOR1 agonist—are biologically implausible and experimentally unsubstantiated. No direct receptor binding, radioligand displacement, surface plasmon resonance, or receptor knockdown experiments are performed; instead, the authors rely on non-specific downstream readouts ($\text{Ca}^{2+}$ flux, melanin synthesis, and dorsomorphin inhibition) that are confounded by well-established alternative pathways (purinergic P2X/P2Y receptor signaling for extracellular ATP and non-specific kinase inhibition by dorsomorphin) and optical absorbance artifacts (cyanocobalamin's intense red chromophore and inner-filter effect). In addition, the statistical analyses apply uncorrected unpaired $t$-tests to multi-group designs, omit sample sizes ($n$) for nearly all *in vitro* experiments, and fail to document randomization, blinding, or vehicle excipient matching in the clinical trial.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **MT–DTI deep-learning model accurately identifies Vitamin B12 as an EDNRB antagonist and ATP as an ADIPOR1 agonist: [Methodologically Flawed].**  
  Drug–target interaction (DTI) sequence/SMILES transformers predict scalar binding affinity ($K_d$/$K_i$/$\text{IC}_{50}$) and cannot inherently distinguish receptor *agonists* from *antagonists* without functional training labels. More critically, the authors state (Section 2.1) that they trained/adapted the model using only *four* known EDNRB antagonists (bosentan, A-192621, BQ-788, IRL-2500) and *five* ADIPOR1 agonists (AdipoRon, gramine, zeaxanthin dipalmitate [misspelled "depalmitate"], arctiin). Training or fine-tuning a deep transformer on 4–5 positive ligands without negative decoys or cross-validation metrics is statistically degenerate, and selecting VitB12 ($1,355\text{ Da}$ cobalt corrinoid) and ATP (a ubiquitous intracellular nucleotide and canonical P2X/P2Y purinergic agonist) from 5,000 hits based on cosmetic availability provides no evidence of target engagement.

* **Vitamin B12 directly antagonizes EDNRB to inhibit ET-1-induced $\text{Ca}^{2+}$ mobilization and melanogenesis: [Overstated].**  
  No direct binding assay between VitB12 and EDNRB is presented. In Section 3.2, the text states *"We investigated the inhibitory effect of VitB12 on EDNRB expression in MNT-1 cells"*, yet no EDNRB expression data are shown. The reduction in Fluo-4 fluorescence ($\lambda_{\text{ex}} \approx 494\text{ nm}, \lambda_{\text{em}} \approx 516\text{ nm}$) and 400 nm melanin absorbance in the presence of cyanocobalamin is confounded by optical inner-filter quenching and baseline absorbance shifts, as cyanocobalamin has strong absorption bands at 361 nm and 500–550 nm. Furthermore, in Figure 2, multiple concentrations of VitB12 (0.5, 1, and 2 $\mu\text{g/mL}$) and controls are compared using uncorrected unpaired Student's $t$-tests alongside one-way ANOVA without reporting the number of biological replicates ($n$).

* **Extracellular ATP promotes *COL1A1*/*ELN* expression and fibroblast wound healing specifically via the ADIPOR1 pathway: [Methodologically Flawed].**  
  Extracellular ATP is the canonical endogenous ligand for purinergic P2Y (G-protein coupled) and P2X (ionotropic) receptors on dermal fibroblasts, which directly activate $\text{Ca}^{2+}$/CaMKK$\beta$-dependent AMPK phosphorylation, collagen synthesis, and cell migration. To claim that ATP acts via ADIPOR1, the authors rely solely on reversal by $3\ \mu\text{M}$ dorsomorphin (Compound C; Figure 3). However, dorsomorphin blocks *downstream* AMPK (as well as BMP type I receptors ALK2/3/6 and数十 other kinases) regardless of whether AMPK was activated by ADIPOR1, P2Y receptors, or cellular uptake of ATP/adenosine. Without *ADIPOR1* knockdown/knockout or competitive binding against adiponectin, attributing extracellular ATP activity to ADIPOR1 is invalid.

* **The VitB12 + ATP complex synergistically increases *HAS2* and *HAS3* expression in HaCaT keratinocytes: [Fragile].**  
  Section 3.4 (Figure 4) compares only untreated control cells against the combined VitB12 + ATP complex using unpaired $t$-tests. Because neither VitB12 alone nor ATP alone was tested in the *HAS2*/*HAS3* assays, it is impossible to determine whether both ingredients contribute to hyaluronan synthase induction or whether the effect is driven entirely by extracellular ATP signaling.

* **Topical application of the VitB12 + ATP complex improves human facial radiance, elasticity, and texture over placebo: [Fragile].**  
  While the 4-week split-face study ($N = 31$) uses objective instrumentation (Multi Gloss, Cutometer R2, Antera 3D Ra), two major design flaws undermine the attribution of efficacy to the VitB12 + ATP complex: (1) Section 3.5 reveals that *"The VitB12 and ATP complex is blended into the active toner with dexpanthenol and glycerin to improve viscosity and stabilization"*, without clarifying whether dexpanthenol and glycerin—both well-known humectants that directly increase skin hydration, gloss, elasticity, and smoothness—were present at identical concentrations in the placebo toner; and (2) Vitamin B12 imparts a distinct pink/red color to aqueous solutions, compromising participant and examiner blinding unless the placebo toner was color-matched. Additionally, exact RM-ANOVA $F$-statistics, degrees of freedom, and group-by-time interaction $p$-values are not reported in the text or tables.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Perform Direct Receptor Engagement or Genetic Knockdown Controls for EDNRB and ADIPOR1
* **WHY:** Downstream changes in Fluo-4 fluorescence, *MITF*/*MC1R* transcription, and dorsomorphin-sensitive fibroblast migration do not establish direct interaction of VitB12 with EDNRB or ATP with ADIPOR1, particularly given ATP's established role as a purinergic P2 receptor agonist.
* **WHAT:** Test direct ligand–receptor binding (e.g., radioligand/fluorescent ET-1 competition assay on EDNRB and surface plasmon resonance or cellular thermal shift assay [CETSA] on ADIPOR1) or repeat the *COL1A1*/migration assays under siRNA-mediated *ADIPOR1* knockdown versus purinergic receptor blockade (e.g., suramin or PPADS).
* **HOW:** Transfect Hs68 fibroblasts with *ADIPOR1*-targeting siRNA vs. non-targeting control siRNA (or co-treat with $100\ \mu\text{M}$ suramin), stimulate with $10\ \mu\text{g/mL}$ ATP vs. $25\ \mu\text{M}$ AdipoRon/gramine for 24 h, and quantify *COL1A1* and *ELN* mRNA via RT-qPCR.

#### 2. Control for Cyanocobalamin Optical Interference and Single-Agent Effects in Cellular Assays
* **WHY:** Cyanocobalamin absorbs strongly between 350–550 nm, overlapping the excitation/emission spectra of Fluo-4 (494/516 nm) and the 400 nm melanin absorbance readout. Moreover, Figure 4 tests only the combined VitB12 + ATP mixture.
* **WHAT:** Include cell-free/dye-only optical quenching controls for VitB12 at $0.5\text{--}2\ \mu\text{g/mL}$ in the Fluo-4 assay, confirm thorough washing of residual VitB12 prior to NaOH lysis in the 400 nm melanin assay, and include single-agent VitB12 and ATP arms in the HaCaT *HAS2*/*HAS3* experiments.
* **HOW:** Measure Fluo-4 fluorescence in buffer containing fixed $\text{Ca}^{2+}$ across $0\text{--}2\ \mu\text{g/mL}$ VitB12 to quantify inner-filter attenuation, and run a 4-group one-way ANOVA (Control, VitB12 alone, ATP alone, VitB12 + ATP) for *HAS2* and *HAS3* qPCR in HaCaT cells.

#### 3. Clarify Split-Face Clinical Trial Blinding, Excipient Matching, and RM-ANOVA Interaction Statistics
* **WHY:** Adding glycerin and dexpanthenol to the active toner (Section 3.5) and failing to color-match the pink hue of VitB12 would confound all hydration-dependent biophysical metrics (gloss, Cutometer R2, and Antera Ra). Furthermore, high-molecular-weight hydrophilic cyanocobalamin ($1,355\text{ Da}$) and charged disodium ATP ($551\text{ Da}$, $\log P < -3$) face severe stratum corneum penetration barriers despite the authors claiming in Section 3.1 that they *"excluded high molecular weight compounds that may have difficulty penetrating skin."*
* **WHAT:** Provide the complete qualitative and quantitative (w/w %) formulation table for both the Active and Placebo toners, state whether color-matching and double-blinding were implemented, and report the complete two-way RM-ANOVA table (Treatment $\times$ Time interaction $F$, $df$, and exact $p$-values).
* **HOW:** Add a formulation table to Section 2.9 confirming that glycerin and dexpanthenol concentrations were identical in both toners, and tabulate the mean $\pm$ SD (or SEM) raw values for Gloss (G.U.), R2 (%), and Ra (A.U.) at Weeks 0, 1, 2, and 4 alongside the RM-ANOVA group $\times$ time interaction statistics.

#### 4. Correct Statistical Testing and Report Sample Sizes Across All Figures
* **WHY:** Figures 1–3 have no sample sizes ($n$) reported in the legends or text, and Figures 2 and 3 apply uncorrected two-sample Student's $t$-tests across multi-group dose-response and inhibitor experiments, inflating the family-wise Type I error rate.
* **WHAT:** Replace all pairwise $t$-tests in multi-group experiments (Figures 2a–c and 3a,b,d) with one-way ANOVA followed by Tukey's or Dunnett's post-hoc test, and explicitly state the number of independent biological replicates ($n$) in every figure legend.
* **HOW:** Re-analyze the raw replicate data for Figures 2 and 3 using one-way ANOVA with Tukey's HSD post-hoc correction and update the significance markers and figure legends accordingly.

#### 5. Document the MT–DTI Screening Protocol and Correct Textual/Citation Errors
* **WHY:** Section 2.1 provides insufficient detail to understand or reproduce how a pre-trained DTI model was adapted with 4–5 compounds, and the text contains chemical naming and typographical errors.
* **WHAT & HOW:**
  1. In Section 2.1 (line 29), clarify whether the 4 EDNRB antagonists and 5 ADIPOR1 agonists were used for similarity filtering, fine-tuning, or pharmacophore post-filtering of the Deargen MT–DTI predictions, and report the predicted affinity scores ($\text{p}K_d$ or $\text{pIC}_{50}$) for VitB12 and ATP from Tables S1/S2 in the main text.
  2. Correct *"zeaxanthin, depalmitate"* (line 29) to *"zeaxanthin dipalmitate"*, *"EDRNB"* (line 21) to *"EDNRB"*, *"Republic of Koreas"* (line 69) to *"Republic of Korea"*, and *"sould"* (line 157) to *"should"*.
