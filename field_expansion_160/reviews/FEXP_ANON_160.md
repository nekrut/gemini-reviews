# Forensic Peer Review: FEXP_ANON_160

**Overall Score:** **3.8 / 10.0** (Flawed / Overstated) | **Scientific Core Score:** **2.9 / 8.0**
* **Score Breakdown:** Rigor: 1.0/3.5 | Claims: 0.8/2.5 | Biology: 1.1/2.0 | Reproducibility: 0.9/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Tier:** Mid-Tier Pharmacology / Chemical Biology Journal
* **Perceived Impact Factor Range:** 4.0 – 6.5
* **Subfield:** Phenotypic Drug Discovery / High-Content Imaging & Anti-Fibrotic Natural Products
* **Rationale:** The manuscript presents a broad experimental scope—combining high-content Digital Phase Contrast (DPC) imaging, an Inception V4 classifier (`deep-DPC`), a 1,400-compound natural product screen, *in vitro* primary neonatal rat cardiac fibroblast (NRCF) assays, an 8-week Ang II mouse cardiac fibrosis model with echocardiography/histology, Biacore T200 SPR, and RNA-seq. However, a forensic audit exposes severe internal contradictions between the Methods and Results on how the deep learning dataset was labeled and sized, data augmentation leakage prior to train/validation splitting, direct self-contradictions on whether RhoA/ROCK1/Cofilin and cardiac hypertrophy are affected, and multiple corrupted methods descriptions.

---

## 2. Executive Summary & Editorial Verdict

This study introduces `deep-DPC`, a phenotypic screening workflow combining Harmony 4.9 morphological feature extraction (31 parameters) and an Inception V4 convolutional neural network trained on time-series Digital Phase Contrast (DPC) images of TGF-$\beta$ I-stimulated NIH-3T3 fibroblasts to classify cells into six fibrotic progression states (`types 0–5`). Applying `deep-DPC` to screen 1,400 traditional Chinese medicine (TCM) natural products identifies 105 initial hits and 29 refined hits, from which **Neo-Przewaquinone A (NPA)** (a tanshinone dimer from *Salvia miltiorrhiza*) is selected for validation in TGF-$\beta$ I-stimulated primary neonatal rat cardiac fibroblasts (NRCFs), an 8-week Angiotensin II (Ang II) osmotic minipump mouse model of cardiac fibrosis, surface plasmon resonance (SPR) binding to TGF-$\beta$ receptor I (ALK5, $K_D = 5.38 \times 10^{-8}\text{ M}$), and bulk RNA-seq/immunoblotting.

Despite the substantial amount of *in vitro* and *in vivo* experimental work, a forensic audit uncovers major methodological flaws and direct self-contradictions across the manuscript:

1. **Direct Contradiction Between Methods and Results on `deep-DPC` Ground-Truth Labeling, TGF-$\beta$ I Concentrations, and Dataset Size, Compounded by Augmentation/Time-Series Data Leakage (First half, line 46 vs. line 119):**
   * **Methods (line 46):** States that images of NIH-3T3 cells treated with vehicle were labeled `type 0`, while cells treated with **`0.01, 0.10, 1, 5, 10 or 20 ng/mL`** of TGF-$\beta$ I (six nonzero concentrations!) were labeled `type 1–5` (five classes!), creating a dataset of **`24,000` labeled images** ($4,000$ per type) randomly split $4:1$ into **`19,200` training** and **`4,800` validation** images.
   * **Results (line 119):** States that NIH-3T3 cells were imaged under **`200, 100, 50, 25, 10, 5, 2.5 and 1.25 ng/mL`** TGF-$\beta$ I (line 117), that low-concentration TGF-$\beta$ I (**`1.25 and 2.5 ng/mL`** at $12\text{ h}$) was classified as `type-1, 2, or 3` (without explaining how two concentrations at one time point map to three distinct ground-truth classes!), and that high-concentration TGF-$\beta$ I (**`25 ng/mL and 50 ng/mL`** after $20\text{ h}$) was classified as `type-4 and type-5`. It then states that **`2,000` images were labeled for each type** ($12,000$ images total, matching line 14) and **data augmentation (image rotation) was applied to create a final dataset of `48,000` images** before fine-tuning Inception V4!
   * **Data Leakage:** Applying $4\times$ rotation augmentation ($12,000 \to 48,000$) *prior* to a random $4:1$ train/validation split places rotated copies of the exact same microscope field—as well as consecutive 30-minute time-lapse frames of the exact same physical well—into both the training and validation sets, inflating the reported $95\%$ validation accuracy.
2. **Self-Contradiction on RhoA/ROCK1/Cofilin Cytoskeletal Signaling (First half, line 126 vs. Second half, lines 28 & 35):**
   * In the first half (line 126), the authors report: *"Furthermore, the levels of RhoA/ROCK1/Cofilin proteins, which regulate cytoskeleton formation and cellular morphology, were **unchanged** between the Tgfbr1 knockdown and 10 ng/mL TGF-$\beta$ I stimulated groups (Fig. S1 f–i)."*
   * Yet in the second half (line 28), they claim: *"Additionally, NPA treatment decreased levels of RhoA/ROCK1/Cofilin proteins, which are key regulators of cytoskeleton formation [51], **consistent with our previous findings in NIH-3T3 cells using the deep-DPC screening method** (Fig. 5a and b)"*!
3. **Self-Contradiction on Cardiac Hypertrophy in Ang II Mice (Second half, line 8 & 10 vs. line 12):**
   * Line 8 states: *"Ang II also induced significant cardiac hypertrophy, as indicated by an increased heart weight to the tibia length ratio (HW/TL) compared to the control group... Treatment with different concentrations of NPA **significantly reversed** Ang II-induced changes in HW/TL (Fig. 3g)."* Line 10 adds that NPA improved left ventricular mass (`LV mass, Fig. 3i`).
   * Four sentences later, line 12 states: *"NPA **did not significantly affect** Ang-II-induced myocardial hypertrophy (Fig. S12d, Supporting Information)."*
4. **Section Title Contradicting Results on PI3K/AKT Signaling and Multiple Corrupted Protocol Descriptions:**
   * The section header at second half line 17 reads: *"NPA as a novel inhibitor: **Activation** of the PI3K/AKT pathway via TGF-$\beta$ receptor I..."*, whereas the text and Western blots (lines 26–28, Fig. 4h) show that TGF-$\beta$ I activates PI3K/AKT and NPA **inhibits/downregulates** PI3K/AKT phosphorylation!
   * In the Methods, the CCK-8 viability assay (first half, line 71) is described using an LDH cell-lysis formula (*"subtracting the spontaneous release control (PBS-treated) from the lysis buffer-treated samples"*); the RNA-seq section (line 95) states *"Single-end sequencing of the amplified flow cytometer on a HiSeq4000 platform"*; the cell-cycle section (line 102) states *"DNA histograms, generated without gating, were used"* (which fails to exclude cell doublets); the SPR concentrations are reported as `0.01–10 µM` in text line 21 vs. `48–780 nM` in Figure 4a/b; and multi-group comparisons across 4–6 groups (Control, Model, and 3 doses of NPA) are described as using a *"two-sided t-test"* in Statistics (line 107) vs. *"one-way ANOVA"* in Figure 3 caption (line 146).

**Editorial Verdict:** **Major Revision.** The biological discovery of NPA as an ALK5-binding anti-fibrotic tanshinone dimer is promising, but the manuscript cannot be published until the authors resolve the contradictions regarding `deep-DPC` training data construction, eliminate rotation/time-series data leakage between training and validation sets, reconcile the contradictory statements on RhoA/ROCK1/Cofilin and cardiac hypertrophy, and fix the corrupted Methods sections.

### Specific Conclusions and Assessment of Support
* **Claim 1:** The `deep-DPC` Inception V4 classifier trained on 6 categories of TGF-$\beta$ I-treated NIH-3T3 DPC images achieves $95\%$ validation accuracy and $92.3\%$ independent test accuracy. `[Methodologically Flawed]` — The TGF-$\beta$ I concentrations (`0.01–20 ng/mL` vs. `1.25–50 ng/mL`), how 2 low concentrations map to 3 classes (`type 1–3`), and total dataset size (`12,000` vs. `24,000` vs. `48,000`) directly contradict between Methods (line 46) and Results (line 119), and performing $4\times$ rotation augmentation and random frame splitting before train/validation partitioning introduces severe data leakage.
* **Claim 2:** Thirteen DPC morphological parameters correlate ($r^2 > 0.3$) with $\alpha$-SMA expression across TGF-$\beta$ I concentrations, time points, and SD-208 inhibition, and `deep-DPC` screening of 1,400 natural products ($Z' > 0.5$) identifies 29 anti-fibrotic hits including Neo-Przewaquinone A (NPA). `[Moderately Supported]` — The linear correlation intersections (`Fig. 1m`, `Table S3`), $Z'$-factor quality control (`Fig. 2d`), and $\alpha$-SMA immunofluorescence validation of the 29 hits (`Fig. 2f–h`) support the phenotypic screen, though the text mislabels `Fig. 2g` as `Fig. 2e` and `Fig. 2h` in line 144.
* **Claim 3:** NPA directly binds TGF-$\beta$ receptor I ($K_D = 5.38 \times 10^{-8}\text{ M}$ by SPR), attenuates $\alpha$-SMA, Collagen I, and Collagen III expression in NRCFs, and reduces myocardial collagen deposition and cardiac dysfunction in Ang II-infused mice without hepatorenal toxicity. `[Moderately Supported]` — Supported by Biacore T200 sensorgrams (`Fig. 4a,b`), Western blots (`Fig. 3b–e, s, t`), Masson's trichrome (`Fig. 3q,r`), and echocardiography (`Fig. 3h–p`), although the text contradicts itself on whether myocardial hypertrophy is reversed (line 8 vs. line 12) and reports conflicting SPR concentration ranges (`0.01–10 µM` vs. `48–780 nM`).
* **Claim 4:** NPA inhibits fibroblast proliferation and preserves cell morphology by downregulating the PI3K/AKT–CDK2 and RhoA/ROCK1/Cofilin pathways. `[Fragile]` — While RNA-seq and Western blots in NRCFs (`Fig. 4c–j`, `Fig. 5a–c`) show reduced p-PI3K, p-AKT, CDK2, and RhoA/ROCK1/Cofilin after NPA treatment, the claim that RhoA/ROCK1/Cofilin modulation is *"consistent with our previous findings in NIH-3T3 cells"* directly contradicts line 126 (*"the levels of RhoA/ROCK1/Cofilin proteins... were unchanged between the Tgfbr1 knockdown and 10 ng/mL TGF-$\beta$ I stimulated groups"*), and cell-cycle flow cytometry was performed *"without gating"* (line 102).

---

## 3. Forensic Defect Inventory

### 3.1 Major Methodological and Statistical Defects

* **Defect 1: Incompatible Descriptions of `deep-DPC` Training Dataset, Class Labeling Rules, and Pre-Split Augmentation Leakage.**
  * *Location:* Introduction (first half, line 14), Section "The architecture of deep-DPC" (first half, line 46), and Section "DPC image data Acquisition and processing" (first half, lines 117–119).
  * *Forensic Evidence:*
    1. **Concentration & Class Mapping Contradiction:** Line 46 states that `types 1–5` correspond to **`0.01, 0.10, 1, 5, 10 or 20 ng/mL`** TGF-$\beta$ I (6 concentrations mapped to 5 classes without specifying which two concentrations are merged or how time points are handled). Line 119 instead states that `type-1, 2, or 3` came from **`1.25 and 2.5 ng/mL`** at $12\text{ h}$ (2 concentrations mapped to 3 classes!) and `type-4 and type-5` came from **`25 ng/mL and 50 ng/mL`** after $20\text{ h}$.
    2. **Dataset Size Contradiction & Rotation Leakage:** Line 14 states the system was validated using `12,000 images`; line 46 states a dataset of `24,000 labeled images` was split $4:1$ into `19,200` training and `4,800` validation images; line 119 states `2,000` images were labeled per type ($12,000$ total) and rotated to create `48,000` images, and later in the same paragraph states `12,000 images` were divided into 5 folds of `2,400 images` for 5-fold CV. Rotating images before random train/validation/CV splitting leaks identical cells across splits.

* **Defect 2: Direct Self-Contradictions on RhoA/ROCK1/Cofilin and Ang II Cardiac Hypertrophy.**
  * *Location:* First half, line 126 vs. Second half, line 28 (RhoA/ROCK1/Cofilin); Second half, lines 8 and 10 vs. line 12 (Cardiac hypertrophy); Second half, line 17 vs. lines 26–28 (PI3K/AKT activation vs. inhibition).
  * *Forensic Evidence:*
    1. Line 126 (first half) reports that RhoA, ROCK1, and Cofilin protein levels are unchanged by TGF-$\beta$ I stimulation or *Tgfbr1* siRNA knockdown (`Fig. S1f–i`), whereas line 28 (second half) claims that NPA's reduction of RhoA/ROCK1/Cofilin in NRCFs is *"consistent with our previous findings in NIH-3T3 cells."*
    2. Line 8 (second half) states that NPA *"significantly reversed Ang II-induced changes in HW/TL (Fig. 3g)"* (and reduced LV mass in `Fig. 3i`), whereas line 12 states *"NPA did not significantly affect Ang-II-induced myocardial hypertrophy (Fig. S12d)."*
    3. Section header at line 17 (second half) states *"Activation of the PI3K/AKT pathway via TGF-$\beta$ receptor I"*, opposite to the actual finding that NPA inhibits PI3K/AKT activation.

* **Defect 3: Corrupted Experimental Protocol Descriptions in Materials and Methods.**
  * *Location:* First half, lines 41, 71, 95, 97, 102, 107; Second half, lines 21–24.
  * *Forensic Evidence:*
    1. **$Z'$-factor equation (first half, line 41):** Defines $\mu_c$ twice, writing *"and $\mu_c$ is the standard deviation of each plate in the control group"* instead of $\sigma_c$.
    2. **CCK-8 vs. LDH cytotoxicity formula (first half, line 71):** States cytotoxicity was measured using a `CCK-8 assay kit` (which measures dehydrogenase reduction of WST-8 in viable cells), but describes an LDH membrane-lysis calculation (*"subtracting the spontaneous release control (PBS-treated) from the lysis buffer-treated samples"*).
    3. **RNA-seq methods (first half, lines 95–97):** Writes *"Single-end sequencing of the amplified flow cytometer on a HiSeq4000 platform"* ("flow cell" mistranslated as "flow cytometer") and states both `DESeq2 (Q value <= 0.05)` and `Bonferroni correction (Q <= 0.05)` without specifying fold-change thresholds or sample sizes ($n$).
    4. **Ungated flow cytometry (first half, line 102):** States *"DNA histograms, generated without gating, were used to determine the percentages of cells with different DNA content"*, omitting debris and doublet discrimination.
    5. **SPR buffer pH vs. "isoelectric point" and concentration mismatch (second half, lines 21–24):** Line 21 calls the sodium acetate immobilization buffer pH scout (`pH 4.5`) *"The optimal isoelectric point for TGF-$\beta$ receptor I"*, and reports NPA concentrations of `0.01–10 µM` in text vs. `48–780 nM` in Figure 4a/b.

### 3.2 Minor Presentation, Structural, and Editorial Issues
* **Missing Abstract in Scrubbed Manuscript Text (First half, lines 3–5):** The `## Abstract` section is blank.
* **Duplicate Sentences and Typos:** First half line 130 repeats the same sentence on the 13 common DPC parameters twice consecutively; line 128 writes `Cell Eadial Mean` and `DPC SER Rright 0 px`; line 146 writes `Salvanic acid B` (for Salvianolic acid B); second half line 8 writes `Ang II II`.

---

## 4. Quantitative Rubric Scoring

* **Methodological & Statistical Rigor (1.0 / 3.5):** While the *in vitro*/*in vivo* pharmacological assays and SPR kinetic measurements are extensive, the computational `deep-DPC` pipeline suffers from pre-split rotation augmentation leakage and contradictory class-labeling definitions, the flow cytometry is ungated, and multiple Methods paragraphs contain garbled protocols (CCK-8 vs. LDH lysis, "amplified flow cytometer").
* **Claim-Evidence Alignment (0.8 / 2.5):** Several mechanistic and *in vivo* claims directly contradict each other within the text (RhoA/ROCK1/Cofilin unchanged in NIH-3T3 vs. "consistent with our previous findings"; cardiac hypertrophy reversed in `Fig. 3g` vs. unaffected in `Fig. S12d`; PI3K/AKT "Activation" in header vs. downregulation in data).
* **Biological & Domain Validity (1.1 / 2.0):** Identifying Neo-Przewaquinone A as a nanomolar ALK5 binder ($K_D = 53.8\text{ nM}$) with lower H9c2 cardiomyocyte toxicity than Tanshinone IIA and demonstrating *in vivo* anti-fibrotic efficacy in an 8-week Ang II model is biologically compelling.
* **Reproducibility & Transparency (0.9 / 2.0):** Antibody catalog numbers, animal ethics approval (`022-12-055`), and instrument models are well documented, but no source code or image dataset repository is provided for `deep-DPC`, and the contradictory training set specifications prevent independent reproduction of the neural network.
* **Scientific Core Score:** **2.9 / 8.0** (`1.0 + 0.8 + 1.1`)
* **Overall Score:** **3.8 / 10.0** (`1.0 + 0.8 + 1.1 + 0.9`)
