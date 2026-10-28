# Review of OOD_ANON_31

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **2.8 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.8/3.5 | Claims: 0.7/2.5 | Biology: 0.6/2.0 | Reproducibility: 0.7/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This study uses an 18-channel portable functional near-infrared spectroscopy (fNIRS) system to measure oxygenated hemoglobin (HbO) fractional amplitude of low-frequency fluctuations (fALFF) and inter-channel Pearson correlations in $n = 15$ chronic pain patients across a 5-minute pre-stimulation period ("Pre-T") and a 5-minute active 150 Hz transcutaneous electrical nerve stimulation period ("During-T"). The authors report significant reductions in Visual Analogue Scale (VAS) and Pittsburgh Sleep Quality Index (PSQI) scores following the 11-minute experiment, decreased fALFF in channels assigned to BA46 and BA45, and increased functional connectivity across prefrontal channels (particularly between BA10 and BA44/45). Raw data and analysis scripts are not publicly available ("available from the corresponding author upon reasonable request").

The manuscript suffers from multiple foundational clinical, methodological, anatomical, and statistical flaws that invalidate its core conclusions. First, the authors administer the PSQI—an instrument that measures 1-month retrospective sleep quality—immediately before and after an 11-minute awake sitting TENS session and claim a highly significant treatment effect ($8.6 \pm 3.6$ to $6.5 \pm 3.2$, $p < 0.001$), which is clinically and temporally impossible. Second, the "During-T" scan is acquired during active 150 Hz peripheral electrical stimulation without a sham control or short-separation channels, confounding "resting-state" connectivity with stimulus-evoked somatosensory processing, order effects, and systemic scalp hemodynamics. Third, Table 1 contains impossible MNI coordinate assignments (e.g., identical anterior prefrontal coordinates $[32.2, 64.13, 41.15]$ assigned to both BA6 premotor/SMA channel 3 and BA9 DLPFC channel 6), and the reported fALFF test statistics violate mathematical monotonicity ($t = 3.335$ reported with $p = 0.0025$ vs. $t = 3.551$ reported with $p = 0.0056$ at the same degrees of freedom). Because the experimental design lacks a sham control and short-separation channels, the primary causal claims cannot be salvaged by computational re-analysis alone.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Short-term (5-minute) TENS significantly reduces pain intensity (VAS) and improves sleep quality (PSQI) ($p < 0.001$): [Methodologically Flawed].**  
  The PSQI assesses sleep quality, latency, and disturbances over the preceding month; administering it before and after an 11-minute awake laboratory session (lines 47, 119–137, 145) and attributing a 2.1-point reduction ($t = 6.254, p < 0.001$) to 5 minutes of TENS is biologically impossible. Moreover, line 145 and the Fig. 2 caption mischaracterize PSQI as a measure of "pain intensity scores." For VAS, the 1.0-point unblinded pre–post reduction ($4.2 \pm 0.9$ to $3.2 \pm 0.8$) lacks a sham-TENS control group, making it impossible to separate specific TENS analgesia from placebo expectation or sitting rest.

* **Spontaneous resting-state brain activity (fALFF) decreases in BA46 (ch1) and BA45 (ch16) during TENS: [Methodologically Flawed].**  
  First, the "During-T" scan is recorded under active 150 Hz electrical stimulation (lines 8, 47) and therefore reflects stimulus-modulated rather than spontaneous resting-state activity. Second, the reported FDR-corrected statistics in line 156—ch1 ($t = 3.335, p = 0.0025$) and ch16 ($t = 3.551, p = 0.0056$)—are mathematically inconsistent: for $df = 14$, a smaller $|t|$-statistic ($3.335$, raw two-tailed $p = 0.0049$) cannot yield a smaller FDR-adjusted $p$-value than a larger $|t|$-statistic ($3.551$, raw two-tailed $p = 0.0032$). Third, lines 87 and 92 state that signals were band-pass filtered to $0.01\text{--}0.08\text{ Hz}$ during preprocessing and then fALFF was computed as the ratio of $0.01\text{--}0.08\text{ Hz}$ power to $0.01\text{--}0.25\text{ Hz}$ power; if band-pass filtering preceded fALFF calculation, denominator power above $0.08\text{ Hz}$ was artificially removed.

* **Resting-state functional connectivity (rsFC) between BA10 and BA44/45 increases significantly during TENS and serves as an objective biomarker of analgesia: [Overstated].**  
  Without short-distance fNIRS channels (acknowledged in line 236), global extracerebral blood flow and autonomic arousal induced by electrical stimulation inflate zero-lag Pearson correlations across all HbO channels simultaneously. Furthermore, the anatomical localization in Table 1 is internally inconsistent: channels 14 ($-73.22, 28.17, -18$) and 16 ($-77.27, 11.81, -13.9$) lie in inferior temporal / temporal polar space ($Z < -13\text{ mm}$) rather than Broca's area (BA44/45), and the study never tests whether connectivity changes correlate with individual VAS reductions ($\Delta\text{VAS}$).

* **Anatomical registration of the 18 fNIRS channels to AAL and Brodmann areas (Table 1): [Methodologically Flawed].**  
  Table 1 assigns the exact same MNI coordinates $(X = 32.2, Y = 64.13, Z = 41.15)$ to both Channel 3 (labeled "Premotor cortex and Supplementary Motor Cortex, PMA and SMA, Brodmann 6") and Channel 6 (labeled "Dorsolateral prefrontal cortex, DLPFC, Brodmann 9"). In MNI space, $Y = +64.13$ is at the anterior prefrontal pole, roughly $60\text{ mm}$ anterior to BA6. Similarly, Channel 11 ($-51.09, 59.41, 22.02$) is in the lateral prefrontal cortex but is mislabeled as "Middle temporal gyrus, MTG, Brodmann 21."

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Remove Invalid Immediate Post-TENS PSQI Claims and Correct Clinical Reporting
* **WHY:** A 1-month sleep quality questionnaire (PSQI) cannot measure immediate changes across an 11-minute awake session, nor is PSQI a pain intensity scale.
* **WHAT:** Remove post-TENS PSQI comparisons from the Abstract, Results (Table 2, Fig. 2B, line 145), and Conclusions, retaining baseline PSQI solely as a demographic descriptor of baseline sleep disturbance.
* **HOW:** Update Table 2 to report only baseline PSQI ($8.60 \pm 3.62$) and recalculate the Table 2 BMI summary row, which is currently miscalculated as $21.7 \pm 2.2$ instead of the true mean $\pm$ SD of the 15 listed values ($22.19 \pm 2.98$).

#### 2. Audit and Correct MNI Optode Registration in Table 1
* **WHY:** Duplicated coordinates between BA6 (ch3) and BA9 (ch6) and swapped prefrontal/temporal labels (ch11 vs. ch14/ch16) invalidate all region-specific neuroanatomical interpretations.
* **WHAT:** Re-export the 3D digitizer or template registration coordinates from `NIRS_KIT` for all 18 channels and verify each channel's MNI projection against the AAL and Brodmann atlases.
* **HOW:** Check the source-detector channel mapping matrix in the `NIRS_KIT` project file, replace the duplicated coordinates for ch3 and the misassigned labels for ch11, ch14, and ch16 in Table 1, and update all region labels in the text and Figures 3–6 accordingly.

#### 3. Recompute fALFF on Unfiltered (Detrended/Motion-Corrected) Data and Fix $t$/$p$-Value Reporting
* **WHY:** Computing fALFF after $0.01\text{--}0.08\text{ Hz}$ band-pass filtering corrupts the $0.01\text{--}0.25\text{ Hz}$ denominator, and reporting $p_{\text{FDR}} = 0.0025$ for $t = 3.335$ alongside $p_{\text{FDR}} = 0.0056$ for $t = 3.551$ ($df = 14$) is mathematically impossible.
* **WHAT:** Compute fALFF prior to narrow-band filtering and report exact raw and Benjamini-Hochberg FDR-adjusted $p$-values across all 18 channels.
* **HOW:** In `NIRS_KIT`, run TDDR motion correction and detrending, compute the power spectrum ratio $\text{RMS}(0.01\text{--}0.08\text{ Hz}) / \text{RMS}(0.01\text{--}0.25\text{ Hz})$, apply paired $t$-tests across the $N = 15$ subjects for all 18 channels, and apply `mafdr(p, 'BHFDR', true)` in MATLAB.

#### 4. Control for Global Systemic Hemodynamics Using HbR and Global Signal Regression
* **WHY:** Without short-separation channels, TENS-induced systemic blood pressure and scalp blood flow fluctuations globally inflate HbO channel-pair correlations.
* **WHAT:** Re-analyze functional connectivity using global signal regression (or principal component removal) on HbO and replicate all connectivity tests on the deoxygenated hemoglobin (HbR) signal, which is far less contaminated by superficial scalp Mayer waves.
* **HOW:** Regress out the mean time series across all 18 channels from each channel's band-pass filtered time series before computing the $18 \times 18$ Pearson correlation matrix, apply Fisher's $r$-to-$z$ transformation prior to paired $t$-tests across the $153$ unique channel pairs, and report whether any edges survive FDR correction across all $153$ pairs in both HbO and HbR.

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Contradictory consent statements, inclusion criteria mismatches, and grammatical errors reduce transparency.
* **WHAT & HOW:**
  1. **Lines 29 vs. 268:** Reconcile the contradiction between "All participants provided written informed consent" (line 29) and "Verbal informed consent was obtained from patients" (line 268).
  2. **Line 29:** Clarify the ethics approval number vs. clinical trial registration number (`ChiCTR2200056394` is a Chinese Clinical Trial Registry identifier, not an institutional ethics committee approval number).
  3. **Lines 12, 29, and Table 2:** Reconcile the inclusion criterion "diagnosed with non-neuropathic pain" (line 29) with the keyword "Neuropathic pain" (line 12) and Subject 10 ("fibromyalgia") in Table 2.
  4. **Line 52:** Change "18 optodes (eight light sources and ten detectors)" vs. "18 channels" so that optodes and measurement channels are clearly distinguished.
  5. **Line 145 & 241:** Correct the spelling of "PQSI" to "PSQI".
