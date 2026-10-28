# Review of OOD_ANON_41

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.1 / 10.0** (Exemplary)  
* **Score Breakdown:** Rigor: 3.2/3.5 | Claims: 2.3/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.9/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript benchmarks whole-brain task-modulated functional connectivity (TMFC) estimation methods across block and event-related fMRI designs using both empirical datasets (Human Connectome Project, $N = 100$; Consortium for Neuropsychiatric Phenomics, $N = 115$) and biophysically grounded simulations. The authors couple a 100-node Wilson-Cowan neural mass model oscillating in the gamma band ($\approx 40\text{ Hz}$) with a Balloon-Windkessel haemodynamic model, controlling ground-truth TMFC via context-dependent short-term synaptic weight modulations alongside independent boxcar co-activations. They systematically evaluate direct correlation difference (CorrDiff), standard, generalised, and correlational psychophysiological interaction (sPPI, gPPI, cPPI) with and without deconvolution, and beta-series correlations using least-squares all (BSC-LSA), least-squares separate (BSC-LSS), and fractional ridge regression (BSC-FRR) across varying signal-to-noise ratios (SNR), sample sizes, event durations, interstimulus intervals (ISIs), repetition times (TRs), and haemodynamic response function (HRF) variability. All simulated time series, analysis scripts, Jupyter notebooks, a Python simulation package (`TMFC_simulator`), an SPM12 GUI toolbox (`TMFC_toolbox`), and standalone ridge-regression deconvolution code (`BOLD_deconvolution`) are publicly released.

This is a thorough, well-controlled methodological benchmark that resolves several persistent ambiguities in the fMRI connectivity literature. It demonstrates that cPPI estimates the sum of task-related and intrinsic background connectivity rather than differential task modulation, that finite impulse response (FIR) task regression is required to prevent co-activation false positives in sPPI and non-deconvolved gPPI, that deconvolution substantially improves PPI sensitivity even in block designs, and that region- and subject-level HRF variability severely degrades time-series correlation methods (gPPI, CorrDiff) while sparing trial-wise amplitude correlation methods (BSC-LSS, BSC-FRR) when design matrix upsampling is omitted. Minor limitations include the assumption of constant per-scan SNR across fast and slow TRs (neglecting T1 recovery trade-offs), the additive injection of boxcar co-activations directly into the haemodynamic model rather than via driving inputs to the Wilson-Cowan populations, and homogeneous local circuit parameters across all 100 cortical nodes. All of these can be addressed via targeted simulation extensions and textual clarifications.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Correlational PPI (cPPI) fails to isolate task-modulated connectivity and instead reflects intrinsic background and task-state connectivity (`Cond A + B` rather than `Cond A - B`): [Well Supported].**  
  Both empirical matrices (Figs. 2–3, $r = 0.69\text{--}0.99$ with RSFC/BGFC/TSFC) and ground-truth simulations (Fig. 5h, Supplementary Fig. S6) demonstrate that partial correlation of two PPI terms conditioned on seed physiological time series and psychological regressors retains shared intrinsic variance rather than contrasting condition-specific connectivity.

* **Co-activations spuriously inflate TMFC estimates unless removed via FIR task regression, and sPPI /gPPI with deconvolution are the most sensitive methods for block and rapid event-related ($\text{ISI} \le 4\text{ s}$) designs under canonical HRFs: [Well Supported].**  
  Simulations with explicit co-activations (Fig. 6) show that sPPI specificity drops near zero without FIR regression and non-deconvolved gPPI specificity drops to 24% in event-related designs, whereas FIR regression restores specificity to $\ge 95\%$. Across SNR and sample size sweeps (Figs. 7–8, Supplementary Tables S3–S8), deconvolution nearly doubles PPI sensitivity in both block and event-related designs, and Bayesian $t$-tests confirm equivalence between symmetrised sPPI and gPPI once co-activations are removed.

* **Cross-region and cross-subject HRF variability sharply reduces TMFC sensitivity, with non-upsampled BSC-LSS and BSC-FRR outperforming gPPI: [Well Supported].**  
  Simulating Balloon-Windkessel parameters with time-to-peak varying between 3 and 7 s (Fig. 9) reduces block-design gPPI sensitivity at $\text{SNR} = 0.4$ from 78% to 5% and event-related gPPI sensitivity from 93% to 14%, whereas BSC-LSS without microtime design-matrix upsampling retains 45% sensitivity (and 83% vs. 51% for gPPI in matched 24–27 min scan comparisons at $\text{SNR} = 0.5$). The comparison with model-free CorrDiff confirms that HRF phase dispersion directly attenuates cross-regional time-series correlations more severely than trial-by-trial beta-amplitude correlations.

* **Rapid (100 ms) gamma-band synchronisation modulations can be recovered from slow BOLD signals ($\text{TR} = 2\text{ s}$), and fast acquisition ($\text{TR} < 1\text{ s}$) improves per-event sensitivity beyond sample-count gains: [Moderately Supported].**  
  While the fixed-scan-count experiment ($N_{\text{scans}} = 1238$, Fig. 8e) demonstrates higher normalised sensitivity per event ($\text{TPR}/N_e$) at $\text{TR} = 500\text{ ms}$ than at $\text{TR} = 1000\text{ ms}$, the simulation holds per-volume white noise constant ($\text{SNR} = 0.4$) across TRs and assumes purely white Gaussian measurement noise, omitting both the physical reduction in steady-state longitudinal magnetisation at short TRs and temporally autocorrelated physiological noise ($1/f$, cardiac, and respiratory aliasing).

* **gPPI with deconvolution can recover the causal direction of information flow (asymmetric effective connectivity) only under unrealistically high SNR, long scan duration, and canonical HRF: [Well Supported].**  
  Under directed ground-truth synaptic matrices (Fig. 10, Supplementary Fig. S10), deconvolved gPPI matches regression DCM ($r = 0.93$, correct sign rate $\text{CSR} = 100\%$ at $\text{SNR} = 5$, double duration), whereas non-deconvolved gPPI yields $\text{CSR} \approx 50\%$ ($|r| < 0.05$). However, none of the asymmetric gPPI differences survive $\text{FDR} < 0.001$, and realistic $\text{SNR} = 0.5$ or HRF variability collapses directional recovery to chance while generating spurious matrix asymmetry in noisy empirical designs (Supplementary Figs. S7–S9).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Incorporate TR-Dependent Thermal SNR Scaling and Autocorrelated Noise in Fast-TR Simulations
* **WHY:** Holding $\text{SNR} = \sigma_{\text{signal}}/\sigma_{\text{noise}} = 0.4$ constant when reducing TR from 2000 ms to 500 ms overstates the practical sensitivity advantage of fast multiband EPI, because shorter repetition times reduce Ernst-angle signal recovery and increase thermal noise per unit time while altering physiological noise aliasing.
* **WHAT:** Add a sensitivity check in the fast-TR simulation (Fig. 8d, e) that scales per-volume noise with $\text{TR}$ according to steady-state T1 recovery ($S \propto \sqrt{\frac{1 - E_1}{1 + E_1}}$ with $E_1 = \exp(-\text{TR}/T_1)$, $T_1 \approx 1.3\text{ s}$ at 3T) and AR(1) noise.
* **HOW:** Using the existing simulated BOLD time series in `TMFC_simulations`, regenerate noisy downsampled series at $\text{TR} \in \{500, 700, 1000, 2000, 3000\}\text{ ms}$ with T1-adjusted SNR and AR(1) coefficient $\phi = 0.3$, and report the resulting TPR curves alongside Fig. 8d–e.

#### 2. Test Neuronal-Level Driving Inputs vs. Haemodynamic-Level Boxcar Addition for Co-Activations
* **WHY:** In the current pipeline (Methods, "BOLD signal generation"), co-activations are simulated by feeding independent boxcar functions into a separate Balloon-Windkessel model and summing the resulting BOLD signal with the oscillatory Wilson-Cowan BOLD signal ($\text{SF} = 1$). Because the Wilson-Cowan equations are nonlinear, injecting task driving inputs ($I_E(t)$) directly into the excitatory subpopulations can interact with ongoing gamma oscillations and alter phase-locking values, whereas post-hoc BOLD addition forces co-activations and synaptic modulations to be strictly linear and separable.
* **WHAT:** Verify that FIR task regression still achieves $\ge 95\%$ specificity when co-activations are generated by step changes in external input $I_E(t)$ to the co-activated Wilson-Cowan modules.
* **HOW:** Run a control simulation in `TMFC_simulator` for the default block and event-related designs where Modules 1 & 3 (Cond A) and Modules 2 & 4 (Cond B) receive an additive excitatory drive $\Delta I_E$ during task periods instead of separate boxcar BOLD addition, and report TPR/TNR in a supplementary figure.

#### 3. Quantify False Positive Rates Under a Complete Null Synaptic Modulation ($\Delta w_{ji} = 0$) with HRF Variability
* **WHY:** The manuscript states that specificity never fell below 95% after FIR regression (line 104), but those specificity estimates were evaluated under fixed canonical HRFs (Fig. 6). When regions have mismatched HRF time-to-peak (3–7 s) and co-activations are present, a fixed-window FIR basis set or canonical GLM regressor can leave residual activation variance or induce differential phase shifts that leak into PPI or BSC estimates.
* **WHAT:** Report the empirical specificity (TNR) and false discovery rate across methods under variable HRFs (time-to-peak 3–7 s) in the presence of co-activations ($\text{SF} = 1$).
* **HOW:** Compute and plot TNR alongside TPR in Fig. 9a, b using the existing variable-HRF simulation outputs.

#### 4. Clarify Mathematical Notation and Editorial Typos
* **WHY:** Minor typographical errors in the text and figure captions slightly obscure technical details.
* **WHAT & HOW:**
  1. Fig. 1a caption (line 23): Fix duplicated phrase *"was introduced first introduced by Di et al."* to *"was first introduced by Di et al."*
  2. Results (line 169): Fix *"BSC-FFR method"* to *"BSC-FRR method"*.
  3. Discussion (line 36, offset 46080): Fix *"This task can be spitted into three 10-minute sessions"* to *"This task can be split into three 10-minute sessions"*.
  4. Discussion (line 40, offset 46080): Fix *"heamodynamic variability"* (twice) to *"haemodynamic variability"*.
  5. Discussion (line 110, offset 46080): Fix *"oxygen concertation"* to *"oxygen concentration"*.
