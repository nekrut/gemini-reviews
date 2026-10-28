# Critical Peer Review (`ANON_126`)

## Section 1: Overall Assessment & Quantitative Scorecard

**Overall Score:** **8.6 / 10.0** (Strong / Sound)
* **Score Breakdown:** Rigor: 2.9/3.5 | Claims: 2.2/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.6/2.0

**Executive Verdict:**
This study profiles 4,645 single cells isolated from 19 freshly resected human melanoma tumors using full-length Smart-seq2 single-cell RNA-seq (scRNA-seq), integrating inferred copy-number variations (CNVs) to distinguish malignant from non-malignant cells, characterizing intra- and inter-tumoral heterogeneity across cell cycle (`KDM5B`), spatial microenvironment, and drug-resistance (`MITF`-high vs. `AXL`-high) transcriptional states, deconvolving 471 bulk TCGA melanomas, and dissecting activation-independent CD8+ T-cell exhaustion programs alongside T-cell receptor (TCR) clonality. Key transcriptomic findings are corroborated by orthogonal bulk whole-exome sequencing (WES), quantitative immunofluorescence across primary tumors and tissue microarrays (308 cores), paired pre- and post-RAF/MEK-inhibitor relapse biopsies ($n = 6$ patients), and pharmacological dose-response curves across 10 melanoma cell lines. Primary technical limitations involve the small number of individual tumors supporting certain single-tumor analyses (e.g., spatial Region 1 immediate-early stress signatures in `Mel79` and exhaustion PCA in `Mel75`), potential confounding by overall tumor purity when correlating stromal and immune markers across bulk TCGA samples, and minor cross-reference typos.

---

## Section 2: Audit of Key Claims

1. **Claim 1:** *"Each tumor, though classified predominantly as 'MITF-high' or 'AXL-high' at the bulk tumor level, also contains cells corresponding to the other expression program... Notably, we observed a shift toward the AXL-high program following emergence of drug resistance in5 of the 6 patients (P < 0.05 by binomial test; comparable shifts are obtained with each patient's top-scoring cells, Fig. 3D, or with the explicit resistance program from Hugo et al.)."* (Section: "MITF and AXL expression programs are variation modules within single tumors and shift upon treatment", pp. 4–5; Fig. 3A–G)
   * **Tag:** `[Well Supported]`
   * **Evidence & Audit:** The authors show negative coupling between `MITF` and `AXL` module scores at both the inter-tumoral level ($P = 4 \times 10^{-4}$, Fig. 3A) and within individual tumors ($P < 0.05$, Fig. 3B), confirm mutually exclusive protein expression within the same lesions by dual immunofluorescence (Fig. 3C), verify bimodal single-cell population shifts under trametinib treatment across 10 CCLE cell lines by flow cytometry and viability assays (Fig. 3E–F, Fig. S7), and validate increased `AXL`/`MITF` staining ratios in paired pre-treatment versus post-relapse biopsies from RAF/MEK-inhibitor-treated patients (Fig. 3D,G).

2. **Claim 2:** *"We identified a small subpopulation of noncycling cells with high expression of the Jarid1B (KDM5B) histone demethylase, a putative marker of slow-cycling melanoma stem-like cells (Fig. 2B). In our data, KDM5B expression was inversely correlated with that of cell-cycle genes (P < 10^-4) and enriched in a small cluster of G1/0-phased cells (P < 10^-6). Triple immunofluorescence staining for KDM5B, Ki67, and Mart1 verified the presence of dispersed non-cycling KDM5B-high cells in human melanoma tissue (Fig. 2E)."* (Section: "Intra- and intertumoral malignant heterogeneity: Cell cycle and spatial context", p. 3; Fig. 2A–E)
   * **Tag:** `[Well Supported]`
   * **Evidence & Audit:** Separating G1/S and G2/M phase scores across 1,252 malignant cells classifies tumors into low-cycling ($1\text{--}3\%$) and high-cycling ($20\text{--}30\%$) groups, matching quantitative Ki67 immunofluorescence (Fig. 2C–D), and confirms in human patient samples a slow-cycling `KDM5B`-high state previously observed only in experimental models.

3. **Claim 3:** *"Consistent with our hypothesis, complement C3 levels was among the top genes correlated with inferred T-cell abundance (R = 0.45, P < 10^-20). We validated this relationship by dual-immunofluorescence staining ontwo tissue microarrays (TMAs) totalling 308 core biopsies of human melanoma tumors... (R = 0.86, P < 10^-15; Fig. 4C and table S7)."* (Section: "Non-malignant cells and their interactions within the melanoma microenvironment", p. 6; Fig. 4B–C)
   * **Tag:** `[Moderately Supported]`
   * **Evidence & Audit:** While the dual immunofluorescence validation on 308 TMA cores ($R = 0.86$, Fig. 4C) directly supports spatial co-occurrence of C3 deposition and CD8+ T cells, the bulk TCGA correlation ($R = 0.45$ between CAF-restricted genes like `C3` and T-cell markers across 471 bulk tumors, Fig. 4B) is partially confounded by overall tumor purity: because $\text{Tumor Purity} + \text{Stromal Fraction} + \text{Immune Fraction} = 1$, bulk tumors with lower malignant purity simultaneously exhibit higher stromal (CAF) and higher immune (T-cell) gene expression even if the two non-malignant compartments vary independently within the stroma. Partial correlations controlling for DNA-based tumor purity (e.g., ABSOLUTE or CPE purity in TCGA SKCM) should be reported to isolate specific CAF–T-cell coupling in bulk RNA-seq.

4. **Claim 4:** *"In addition to cell-intrinsic heterogeneity, we identified a spatial expression program in Region 1 of tumor Mel79... This program includes stress-response and immediate-early genes (ATF3, FOS, FOSB, JUN, JUNB, EGR1, EGR2, EGR3, HSPA1B), as well as genes implicated in NF-kappaB signaling, angiogenesis (VEGFA), and cell migration/invasion (PLAU, PLAUR, THBS1)."* (Section: "Intra- and intertumoral malignant heterogeneity: Cell cycle and spatial context", p. 4; Fig. 2F–G)
   * **Tag:** `[Fragile]`
   * **Evidence & Audit:** This spatial claim is derived from a single multiregion tumor (`Mel79`), and the core gene set (`FOS`, `FOSB`, `JUN`, `JUNB`, `EGR1/2/3`, `ATF3`, `HSPA1B`) is the canonical enzymatic collagenase/dispase dissociation and warm-ischemia immediate-early stress signature in solid-tumor scRNA-seq. Although the authors also note that `NFKB1` and `JUNB` showed elevated expression in marginal areas by IHC and in bulk TCGA samples with high stromal content, differences in dissociation kinetics or tissue necrosis between Region 1 and the remaining regions of `Mel79` cannot be excluded without spatial transcriptomics or RNA *in situ* hybridization on undissociated sections of `Mel79`.

---

## Section 3: Technical Critique & Actionable Recommendations

### Major Methodological & Statistical Issues

1. **Confounding by Overall Tumor Purity in Bulk TCGA Cell-Type Co-Variation Analysis (Pillar 3 & Pillar 4):**
   * **Issue:** In Figure 4B and Figure 4D, the authors correlate the expression of CAF-specific genes (such as complement factors `C3`, `C1S`, `C1R`, `CFB`) with inferred T-cell/macrophage abundance across 471 bulk TCGA melanomas, and use the ratio of CAF-to-macrophage markers to classify tumors as "CAF-rich" vs. "Macrophage-rich". In bulk tumor transcriptomes, any two non-malignant cell-type signatures will correlate positively across samples whenever malignant cell purity varies widely ($20\%$ to $>90\%$ in TCGA SKCM).
   * **Remediation:** Re-calculate the TCGA correlations in Figure 4B as partial Pearson/Spearman correlations conditioning on independent DNA-based tumor purity estimates (such as ABSOLUTE purity or leukocyte methylation fraction from TCGA SKCM), or normalize both CAF and T-cell scores to total non-malignant (`PTPRC` + stromal) content.

2. **Uneven Per-Patient Cell Counts and Single-Tumor Dependence of Key Sub-Analyses (Pillar 4 & Pillar 5):**
   * **Issue:** Across the 19 profiled tumors, malignant and immune cell recovery is highly skewed (Fig. 1C; Table S1): only 6 tumors have $>50$ malignant cells (`Mel79` alone contributes roughly a third of all malignant cells), and the activation-independent CD8+ T-cell exhaustion PCA and TCR clonotype expansion analyses (Fig. 5B–G) rely predominantly on a single tumor (`Mel75`, $n = 314$ CD8+ T cells, with 4 additional tumors having $52\text{--}195$ cells examined in Fig. S11). Treating single cells as independent observations in Fisher's exact tests or correlation $P$-values ($P < 10^{-6}$, $P < 10^{-4}$) inflates degrees of freedom via pseudoreplication when cells originate from 1–6 patients.
   * **Remediation:** For multi-patient scRNA-seq comparisons, report patient-level summary statistics or mixed-effects models with patient ID as a random effect alongside pooled cell-level $P$-values, and explicitly state the number of distinct patients contributing to each panel in Figures 2 and 5.

### Minor Presentation & Reproducibility Issues

1. **Broken Figure Cross-Reference in Text (Pillar 7):**
   * On page 9 (final paragraph of Results, discussing `CTLA4`, `PRDM1`, and `IL1R2` upregulation in expanded T-cell clones), the text cites `( Fig. 4H )`. Figure 4 only has panels A–D; the intended reference is `( Fig. 5H )`.
2. **Code Availability (Pillar 7):**
   * While raw and processed expression matrices are deposited in GEO (`GSE72056` and `GSE77940`), the custom scripts implementing the 100-gene moving-average CNV caller, the 20-bin control gene subtraction for signature scoring, and the activation-independent exhaustion residual score are described textually in the Supplement without an archived code repository. Depositing these scripts on GitHub/Zenodo would substantially improve reproducibility.
