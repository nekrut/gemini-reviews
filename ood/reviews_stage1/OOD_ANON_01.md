# Review of OOD_ANON_01

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **2.3 / 10.0** (Fundamentally Invalid)  
* **Score Breakdown:** Rigor: 0.4/3.5 | Claims: 0.6/2.5 | Biology: 0.8/2.0 | Reproducibility: 0.5/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript proposes a multimodal data fusion pipeline to relate time-varying resting-state functional MRI (rs-fMRI) spatial network dynamics with concurrently recorded EEG spectral band power across $N = 90$ participants pooled from four heterogeneous datasets (three public cohorts and one in-house sample). Using group independent component analysis (ICA) followed by sliding-window multivariate-objective optimization ICA with reference (MOO-ICAR), the authors extract 14 intrinsic connectivity networks (ICNs) and correlate either their supra-threshold voxel counts ("network volumes") or the first principal component of their voxel time courses against sliding-window EEG power in four frequency bands (delta, theta, alpha, beta) recorded from three midline electrodes (Fz, Cz, Pz). They report strong associations ($|r| > 0.4$) between primary visual network volume and alpha power, and between motor/cerebellar networks and beta/theta/delta bands.

Despite the scientific value of characterizing spatial-temporal coupling in simultaneous EEG-fMRI, the study's statistical and signal-processing pipeline is invalidated by multiple fundamental methodological errors. First, network volume thresholds ($V_{TH}$) are selected via post-hoc circular testing (double-dipping) on the same subject correlations subsequently evaluated for significance, and the thresholds stated as selected in Section 3.2 contradict the values highlighted in Tables 2–4. Second, group-level correlation maps (Figures 7 and 8) are computed by applying Principal Component Analysis (PCA) across the subject dimension ($14 \times 4 \times Z$) and interpreting the unscaled first principal component as a group correlation coefficient thresholded at $|r| > 0.4$ via a sample-size-$N=90$ $t$-distribution calculation; PCA across subjects removes the mean group effect and yields component loadings or scores that do not follow a correlation distribution. Third, the sliding-window correlation analysis uses a 2-second step size on 60-second tapered windows without accounting for extreme temporal autocorrelation ($>96\%$ window overlap) or the hemodynamic response function (HRF) delay between electrical and BOLD signals, and pools datasets with incompatible TRs (2.0 s vs. 2.1 s) and scan durations (420 s vs. 600 s) without harmonization. Substantial re-analysis from raw preprocessed time courses is required to salvage any valid empirical conclusions.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Selection of network-specific z-score thresholds ($V_{TH}$) via group $t$-tests on EEG-fMRI correlations (Section 3.2, Tables 2–4): [Methodologically Flawed].**  
  The authors select $V_{TH} \in \{0.5, 1.0, \dots, 3.5\}$ for each network by correlating network volume with average EEG band power across all $N=90$ subjects and picking the threshold that yields the lowest $p < 0.05$ in a one-sample $t$-test, then use those exact thresholded volumes to claim significant band-specific EEG-fMRI coupling in Section 3.4. This is textbook circular analysis (double-dipping) that inflates Type I error. Furthermore, the text in Section 3.2 contradicts Tables 2–4: the text states that "VIS-P/S, SUB, MTR-P/S, CER, ATN, FPN-R, and DMN-A networks are less than 0.05 at $V_{TH} = 2.5, 2.0, 3.0, 2.5, 2.0, 2.0, 1.5$, respectively," whereas in Table 2 (Cz), SUB is $p = 0.6299$ at $V_{TH} = 2.0$, MTR-P is $p = 0.0714$ at $V_{TH} = 3.0$, MTR-S is $>0.12$ at all thresholds, and FPN-R is $>0.35$ at all thresholds (and $>0.44$ at all thresholds in Table 3). Even the captions of Tables 2–4 contradict the main text (e.g., Table 4 caption states $V_{TH} = 1.0$ was selected for CER, whereas the text says $2.5$).

* **Group-level volume-based and voxel-wise correlations with EEG spectral power ($|r| > 0.4$, Figures 7 and 8): [Methodologically Flawed].**  
  In Section 2.3.2, the authors compute subject-specific correlation matrices of size $14 \times 4$ for $Z=90$ subjects ($14 \times 4 \times Z$), and then state: "PCA was then applied across Z to further reduce the data. The first principal component of dimension ($14 \times 4$) was obtained and interpreted for our analysis." In Section 3.4, they threshold this PCA output at $|0.4|$ because "with our sample size of 90, it corresponds to an uncorrected $p$-value of 0.0001." This procedure is mathematically invalid on three counts: (1) within-subject correlations are computed across $w$ sliding windows with $96.7\%$ overlap (width $30 \times \text{TR} \approx 60\text{ s}$, step $2\text{ s}$), not across $N=90$ independent observations; (2) applying PCA across the subject dimension $Z$ centers the data across subjects (destroying the group mean correlation) and extracts the axis of maximum inter-subject variance, which has arbitrary sign and scale; and (3) treating PC1 scores/loadings as Pearson correlation coefficients with $df = 88$ is statistically meaningless.

* **Voxel-wise fusion via within-network PCA correlation with EEG band power (Section 2.3.1, Equation 1, Figure 8): [Methodologically Flawed].**  
  To correlate voxel-level spatial maps ($68,235 \text{ voxels} \times w$) with EEG band power ($1 \times w$), the authors extract the first principal component of the spatial map across windows ($\text{PCA}(SM_{Nnets}(t))$) for each subject independently. Because PCA eigenvectors have an arbitrary sign ($\pm 1$) in each subject and window decomposition, correlating subject-specific PC1 time courses with EEG band power produces correlation coefficients whose signs are arbitrary across subjects, rendering group aggregation invalid unless sign-alignment against a reference template is performed.

* **Neurobiological localization of alpha, beta, theta, and delta rhythms to expanding/shrinking fMRI resting-state networks (Sections 3.3–3.5, Discussion): [Overstated].**  
  The pipeline computes zero-lag correlations between EEG spectral power in window $w$ and fMRI spatial maps in the same window $w$ without convolving EEG power with a canonical hemodynamic response function (HRF) or accounting for the 4–6 s hemodynamic lag. In addition, the four pooled datasets have different repetition times ($\text{TR} = 2.1\text{ s}$ in Telesford and Gu vs. $\text{TR} = 2.0\text{ s}$ in Wu and Inhouse; Table 1), meaning the window width of "$30 \times \text{TR}$ seconds" is 63 seconds in two datasets and 60 seconds in the other two, while the step size is fixed at 2 seconds (a non-integer multiple of TR = 2.1 s). Finally, EEG was bandpass-filtered to 1–30 Hz (Section 2.5), truncating the stated delta band (0.5–4 Hz) below 1 Hz.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Replace Cross-Subject PCA with Valid Second-Level Random-Effects Inference
* **WHY:** Applying PCA across the subject dimension ($14 \times 4 \times Z$) captures inter-subject variance rather than the group mean correlation, has arbitrary sign/scaling, and cannot be tested against a Pearson $r$ threshold of $|0.4|$ for $N=90$.
* **WHAT:** Compute standard second-level group statistics on Fisher $z$-transformed within-subject correlation coefficients.
* **HOW:** For each subject $s \in \{1,\dots,90\}$, network $n$, electrode $e$, and band $M$, compute the within-subject correlation $r_{s,n,e,M}$ across time windows, apply Fisher's transform $z_{s,n,e,M} = \text{atanh}(r_{s,n,e,M})$, and perform a one-sample $t$-test across the $N=90$ subjects against $H_0: \mu_z = 0$ (controlling for dataset batch effects as covariates in a linear model), followed by Benjamini-Hochberg FDR or Bonferroni correction across all $14 \times 4 \times 3 = 168$ tests.

#### 2. Eliminate Circular Threshold Selection ($V_{TH}$) and Reconcile Tables 2–4
* **WHY:** Selecting $V_{TH}$ by minimizing the $p$-value of the correlation between network volume and EEG power in the same dataset biases subsequent correlation tests, and half of the networks have no significant threshold in Tables 2–4 anyway.
* **WHAT:** Define $V_{TH}$ a priori (independent of EEG data) or integrate across all thresholds using an area-under-the-curve (AUC) summary metric.
* **HOW:** Either fix $V_{TH}$ at a standard statistical threshold (e.g., $Z = 2.5$, as used for visualization in Figures 4 and 6) prior to computing EEG correlations, or compute the integrated volume across thresholds $V_{\text{AUC}}(w) = \sum_{k} \text{Vol}_{V_{TH,k}}(w) \Delta V_{TH}$ for each time window $w$. Correct the text in Section 3.2 so that reported $p$-values match Tables 2–4.

#### 3. Account for Hemodynamic Lag, Window Autocorrelation, and Sign Ambiguity in Voxel PCA
* **WHY:** Convolving a 60 s window with a 2 s step creates $>96\%$ overlap between adjacent windows, and unaligned subject-specific PCA components have arbitrary polarity.
* **WHAT:** Convolve EEG band power time courses with a canonical HRF before windowing, align subject PCA spatial loadings to the group ICN template to fix sign ambiguity, and account for effective degrees of freedom.
* **HOW:** Convolve the 1 Hz-sampled EEG band power envelope with the SPM12 canonical HRF prior to sliding-window averaging. For the voxel-wise analysis (Section 2.3.1), orient the sign of each subject's first principal component so that its spatial eigenvector correlates positively with the group ICN map from GIFT.

#### 4. Harmonize Sliding-Window Parameters Across the Four Pooled Datasets
* **WHY:** Table 1 shows that two datasets have $\text{TR} = 2100\text{ ms}$ (duration 600 s) and two have $\text{TR} = 2000\text{ ms}$ (duration 420 s). A window of $30 \times \text{TR}$ with a 2 s step is inconsistent in physical time (63 s vs. 60 s) and does not align with volume acquisition times when $\text{TR} = 2.1\text{ s}$.
* **WHAT:** Resample all fMRI time series and EEG power envelopes to a common temporal grid or define windows in fixed seconds (e.g., 60 s window, 1 TR step) and test for dataset/scanner site effects.
* **HOW:** Interpolate the fMRI spatial map time series to a uniform 2.0 s grid before windowing, include dataset indicator variables (3 dummy covariates for the 4 cohorts) in the second-level regression, and replace the Google Image Search elements in Figure 1 with original or properly licensed schematics.
