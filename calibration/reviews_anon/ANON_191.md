# Review of ANON_191

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.3 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.2/3.5 | Claims: 2.4/2.5 | Biology: 1.9/2.0 | Reproducibility: 1.8/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript rigorously evaluates whether healthy term human placentas harbor an authentic commensal microbiota distinguishable from background environmental and reagent contamination. The authors collected internal maternal-side (basal plate) and fetal-side placental biopsies, paired maternal saliva and vaginal swabs, clinical laboratory air swabs, unused sterile swabs, and reagent-only extraction blanks from six uncomplicated term deliveries. Crucially, replicate placental biopsies, saliva samples, and negative controls were extracted in parallel using two commercial DNA purification kits (STRATEC PSP and MO BIO PowerSoil) and assayed by V1–V2 16S rRNA quantitative PCR (qPCR) and Illumina MiSeq amplicon sequencing. Both frequentist (Kruskal-Wallis with Dunn's post-test) and Bayesian (`BEST`) analyses of qPCR cycle thresholds ($C_t$) demonstrate that 16S copy numbers in maternal and fetal placental biopsies ($1.24 \times 10^2$ to $5.72 \times 10^2$ copies) are indistinguishable from air swabs, sterile swabs, and reagent blanks ($8.77 \times 10^1$ to $1.93 \times 10^2$ copies), whereas paired oral and vaginal swabs contain $\sim 30,000$-fold higher bacterial DNA ($5.97 \times 10^6$ to $3.69 \times 10^8$ copies). Community profiling (PERMANOVA on Bray-Curtis and weighted/unweighted UniFrac distances) and cross-kit concordance filtering across 5 logs of relative abundance show that placental samples cluster strictly by extraction kit (soil/water taxa in PSP; *Clostridium difficile* reagent/lab background in MO BIO), with zero bacterial OTUs shared between extraction methods at $\ge 1\%$ abundance above negative controls. Raw sequencing data are publicly deposited in NCBI SRA (PRJNA309332) and raw qPCR amplification curves and oligonucleotide sequences are provided in the supplementary files.

This is a methodologically exemplary forensic microbiome study. By pairing absolute quantification (qPCR) with orthogonal kit extractions and contemporaneous environmental/reagent controls from the same patients, the authors provide a definitive template for testing the "contamination-only" null hypothesis in low-biomass tissues. The conclusions are carefully bounded to the sample size ($n=6$ healthy term deliveries), internal parenchymal sampling protocol, and V1–V2 amplicon window. Only minor technical refinements in the qPCR efficiency calibration and exact sequence variant denoising could further strengthen the analysis.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Absolute 16S rRNA gene copy numbers in internal maternal and fetal placental biopsies are indistinguishable from negative contamination controls (Fig. 1a–d; Additional file 3: Figure S2): [Well Supported].**  
  Both non-parametric testing of raw $C_t$ values ($P > 0.05$ for all placenta-vs.-control pairs across both kits) and Bayesian posterior estimation confirm no enrichment of bacterial DNA in placental biopsies over clinical laboratory air swabs (95% credible upper bound $<3.5\times$ in MO BIO and $<0.8\times$ in PSP, with $P = 0.004$ and $P = 0.00004$ for a $\ge 10$-fold excess). Analysing raw $C_t$ values alongside standard-curve copy numbers avoids distortion near the lower limit of detection.

* **Microbial community structure in placental biopsies does not separate from contamination controls and clusters strictly by DNA purification kit (Figs. 2–3; Additional file 4: Figure S3): [Well Supported].**  
  PERMANOVA tests on phylum-level Bray-Curtis and 97%-OTU weighted and unweighted UniFrac distances show no significant difference between placental biopsies and matched air swabs/extraction blanks ($P > 0.05$ in PSP; $P = 0.11$ in MO BIO after accounting for sterile swab outliers). Co-occurrence clustering (Fig. 3) demonstrates that 27/28 MO BIO low-biomass samples and 28/29 PSP low-biomass samples segregate by extraction kit rather than tissue vs. control, whereas paired high-biomass saliva samples cluster by individual patient across kits.

* **No authentic bacterial lineages are reproducibly shared across both DNA extraction methods at $\ge 1\%$ relative abundance above negative controls (Fig. 4; Additional file 5: Table S3): [Well Supported].**  
  Requiring cross-kit concordance (recovery in both PSP and MO BIO from the same patient) and abundance exceeding negative controls recovers 28 abundant OTUs ($\ge 1\%$) and 2,197 total OTUs ($\ge 0.001\%$) in saliva, but 0 OTUs at $\ge 1\%$ in maternal or fetal placenta. Furthermore, the three low-abundance ($\ge 0.001\%$) OTUs shared across multiple placentas were 100% identical to human chromosomal DNA (off-target amplification), and singleton maternal-side outliers (*Prevotella* in subject 67, *Enterobacteriaceae* in subject 61) did not match the OTUs present in the same patient's paired saliva or vaginal swabs.

* **Six methodological recommendations for low-biomass microbiome studies (Discussion, line 148): [Well Supported].**  
  Every recommendation—requiring absolute qPCR quantification, explicitly testing the "all-contamination" null hypothesis, processing contemporaneous matched controls, sequencing low-yield/failed PCR libraries to sample the reagent background, avoiding unvalidated post-hoc subgrouping when omnibus PERMANOVA is null, and enforcing reviewer reporting standards—is directly grounded in the empirical failure modes demonstrated in Results.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Incorporate Empirically Measured Kit-Specific qPCR Amplification Efficiency into the Bayesian Fold-Change Model
* **WHY:** In the caption of Additional file 3: Figure S2 (line 232), the Bayesian `BEST` analysis converts $C_t$ differences into DNA fold-changes assuming that *"Each cycle difference in the cycle of threshold between samples was assumed to represent a 2-fold difference in DNA"* (100% amplification efficiency, $E = 2.0$), whereas low-biomass templates near the limit of detection ($C_t \approx 34\text{–}38$) or containing different kit buffers may exhibit slightly different efficiencies.
* **WHAT:** Propagate the empirical slope/efficiency of the standard curve from each run into the fold-change conversion and clarify why the limit of detection (LOD) differs between the PSP ($C_t = 38.29$) and MO BIO ($C_t = 34.04$) assays in Fig. 1c–d.
* **HOW:** Compute the amplification factor $E = 10^{-1/\text{slope}}$ from the qPCR standard curves used in Fig. 1a–b, transform posterior $\Delta C_t$ distributions via $E^{-\Delta C_t}$, and add a brief sentence in Methods (line 188) explaining how the kit-specific LOD $C_t$ values (38.29 vs. 34.04) were defined (e.g., no-template water controls vs. standard curve dilution limits).

#### 2. Quantify Statistical Power / Minimum Detectable Biomass in a Sample Size of $n = 6$
* **WHY:** In the Discussion (line 146), the authors appropriately note that studying $n = 6$ deliveries leaves open the possibility that a larger cohort could detect a weak signal. Providing a quantitative bound on the minimum bacterial load detectable above the kit background with $n = 6$ makes this limitation concrete.
* **WHAT:** Report the minimum excess 16S copy number (or $\Delta C_t$) that the $n = 6$ paired study design had 80% power to detect at $\alpha = 0.05$, and note that the Bayesian credible intervals already bound the mean placental signal to $<3.5\times$ background ($\lesssim 500$ copies per reaction).
* **HOW:** Using the observed standard deviations of $C_t$ in air swabs and placental biopsies (Fig. 1c–d), report the minimum detectable difference $\Delta C_t$ (and corresponding copy-number excess) in the Discussion paragraph on study limitations (line 146).

#### 3. Deposit Exact Analysis Scripts (R / `qiimer` / `BEST` Pipeline) in a Public Repository
* **WHY:** While the raw sequencing reads are deposited in SRA (PRJNA309332) and the `qiimer` package is referenced on GitHub, the exact R scripts used to generate the PERMANOVA tests, Bayesian `BEST` posterior distributions, and Fig. 4 cross-kit abundance curves are not linked in the Data Availability Statement.
* **WHAT & HOW:** Upload the R markdown or script files reproducing Figs. 1–4 and Additional files 2–5 to a public GitHub repository or Zenodo archive and cite the URL/DOI in the *Availability of data and materials* section (line 213).
