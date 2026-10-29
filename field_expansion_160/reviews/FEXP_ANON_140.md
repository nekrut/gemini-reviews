# Review of FEXP_ANON_140

**Overall Score:** **7.9 / 10.0** (Strong / Sound)
* **Score Breakdown:** Rigor: 2.5/3.5 | Claims: 2.0/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.6/2.0
* **Scientific Core Score:** **6.3 / 8.0**

---

## 1. Blinded Metadata Perception

* **Manuscript ID:** `FEXP_ANON_140`
* **Perceived Study Type:** Methodological and biophysical neuroimaging study using the Midnight Scan Club (MSC) precision-mapping dataset (OpenNeuro `ds000224`; $N = 10$ healthy participants $\times 12$ sessions each = 120 resting-state fMRI runs [30 min each, $4\text{ mm}$ isotropic] paired with 12 time-of-flight [TOF] 2D MR angiograms/venograms per subject).
* **Domain & Focus:** fMRI biophysics and physiological noise modeling (intravascular and distance-dependent perivascular contributions of cerebral macrovasculature—separated into arteries and veins—to whole-gray-matter resting-state functional connectivity degree [$D$], strength [$S$], and spatial variance [$\sigma^2$]).

---

## 2. Executive Summary & Editorial Verdict

This study investigates how signals originating from large cerebral arteries and veins—segmented per participant from multi-orientation 2D time-of-flight (TOF) angiograms and venograms in the Midnight Scan Club (MSC) dataset ($N = 10$ subjects $\times 12$ sessions)—contribute to resting-state gradient-echo BOLD functional connectivity (rs-fcMRI) within the macrovasculature itself, across whole-brain gray matter (GM), and in dilated perivascular shells ($1, 2,\text{ and }3$ voxels $= 4, 8,\text{ and }12\text{ mm}$ from vessels). By quantifying connectivity degree ($D$, at $|r| > 0.15$ and sensitivity-tested up to $0.50$), mean correlation strength ($S$), and spatial correlation variance ($\sigma^2$), the authors demonstrate that (1) venous–venous correlations are predominantly positive whereas arterial–venous correlations are predominantly negative (consistent with diamagnetic oxygenated arterial vs. paramagnetic deoxygenated venous blood susceptibility at 3 T), (2) macrovascular voxels account for up to $\sim 32.5\%$ (venous) and $\sim 6.0\%$ (arterial) of GM connectivity degree and exhibit disproportionately high spatial variance, and (3) venous connectivity effects extend up to 3 voxels ($12\text{ mm}$) into perivascular GM tissue, meaning simple vessel masking cannot eliminate macrovascular bias.

**Editorial Verdict:** **Accept with Minor Revisions.** This is a well-conceived, biophysically grounded methodological study that leverages repeated-session within-subject data ($10 \times 12$ sessions) and subject-specific TOF vascular segmentations to quantify an important and underappreciated confound in rs-fMRI. The primary methodological limitation—which can be addressed directly through a straightforward computational control—is that the fMRI data ($4\text{ mm}$ isotropic voxels) were spatially smoothed with a **6 mm FWHM Gaussian kernel** (`Methods`, line 46) *prior* to evaluating the perivascular distance shells ($1, 2,\text{ and }3$ voxels away). Because a 6 mm FWHM Gaussian filter algebraically smears intravascular signal into adjacent voxels (retaining $\sim 29\%$ weight at 1 voxel [$4\text{ mm}$] distance), the reported perivascular decay over 1–3 voxels conflates true biophysical extravascular dipolar blooming ($T_2^*$ susceptibility field offsets) with post-acquisition spatial smoothing. Recomputing the perivascular distance curves on **unsmoothed** fMRI data alongside the 6-mm smoothed data will cleanly separate physical susceptibility blooming from preprocessing filter smearing. Additionally, several subscript/symbol typos in the `Results` and `Discussion` text should be cleaned up.

### Assessment of Specific Conclusions & Support

* **Macrovascular BOLD signals exhibit strong intra-venous and intra-arterial positive connectivity alongside arterial–venous anti-correlations at 3 T: [Well Supported].**  
  Replicated consistently across 120 scan sessions in 10 participants (`Figures 4–7`), and grounded in the magnetic susceptibility difference between diamagnetic oxygenated arterial blood ($\chi \approx -9.05\text{ ppm}$) and paramagnetic deoxygenated venous blood ($\chi \approx -7.9\text{ ppm}$) relative to brain parenchyma.

* **Macrovasculature contributes substantially to whole-GM connectivity degree (higher from veins than arteries) and exhibits disproportionately high spatial connectivity variance: [Well Supported].**  
  Degree ratios ($D_{V,V}:D_{V,\text{GM}}$ up to $32.51\%$, $D_{A,A}:D_{A,\text{GM}}$ up to $6.01\%$) and variance ratios ($\sigma^2_{\text{vascular}}:\sigma^2_{\text{GM}} \in [0.75, 3.5]$) persisted across correlation thresholds ($r > 0.15$ to $r > 0.50$, `Supplementary Fig. S1`), demonstrating that unmasked large vessels substantially inflate and distort GM functional connectivity hubs (particularly in anterior cingulate, primary visual, and insular networks, `Table 1`).

* **Macrovascular contributions to rs-fcMRI extend up to 3 voxels (12 mm) into perivascular GM tissue, rendering simple vessel masking insufficient: [Moderately Supported].**  
  While extravascular dipolar $T_2^*$ susceptibility fields around large veins genuinely extend beyond voxel boundaries, the fMRI preprocessing pipeline (`line 46`) applied a **6 mm FWHM Gaussian spatial smoothing kernel** to $4\text{ mm}$ isotropic voxels before extracting the 1-, 2-, and 3-voxel perivascular shells. Consequently, part of the perivascular connectivity observed at 1–2 voxels ($4\text{--}8\text{ mm}$) is artificially induced by Gaussian spatial smoothing and downsampling partial-volume effects rather than purely extravascular magnetic field offsets.

---

## 3. Forensic Defect Inventory

### 1. Confounding of Perivascular Distance Decay by Pre-Analysis 6 mm FWHM Gaussian Spatial Smoothing (Pillar 3 & Pillar 5)
* **Defect:** In `fMRI processing and FC analysis` (line 46, step g), the $4\text{ mm}$ isotropic fMRI volumes were spatially smoothed with a $6\text{ mm}$ FWHM ($\sigma = 2.55\text{ mm}$) Gaussian kernel before computing the perivascular shell metrics (`Figure 10` and `Figure 11`). When a $6\text{ mm}$ FWHM Gaussian kernel is convolved with a $4\text{ mm}$ voxel grid, signal from the central vascular voxel (`distance = 0`) is mathematically mixed into the 1-voxel (`4 mm`) and 2-voxel (`8 mm`) dilated shells. Thus, the observed perivascular degree ratio ($D_{V(\text{ex}),V}:D_{V(\text{ex}),\text{GM}}$) conflates biophysical extravascular susceptibility blooming with preprocessing filter smearing.
* **Actionable Fix:** Re-run the perivascular shell analysis (`Figures 10 and 11`, distances of 0, 1, 2, and 3 voxels) on the **unsmoothed** preprocessed fMRI data (omitting step g) and plot the unsmoothed vs. 6-mm smoothed distance decay curves side by side. This will quantify how much of the 1–3 voxel perivascular effect is physical ($T_2^*$ dipolar blooming + unsegmented medium vessels) versus smoothing-induced.

### 2. Subscript and Metric Notation Typos in `Results` and `Discussion` (Pillar 7)
* **Defect:**
  1. `Results` (line 160): *"According to the histogram (Fig. 9e), the $\mu(\sigma^2_{V,V}:\sigma^2_{v,GM})$ and $\mu(\sigma^2_{V,V}:\sigma^2_{v,GM})$ had slightly different maxima, with $\mu(\sigma^2_{V,V}:\sigma^2_{v,GM})$ higher than the $\mu(\sigma^2_{V,V}:\sigma^2_{v,GM})$."* Here, the exact same symbol ($\mu(\sigma^2_{V,V}:\sigma^2_{v,\text{GM}})$) is compared to itself because the second term's subscript (presumably $\sigma^2_{A,V}:\sigma^2_{A,\text{GM}}$ or $\sigma^2_{V,A}:\sigma^2_{V,\text{GM}}$) was mis-typed!
  2. `Results` (line 168): *"The perivascular contribution of the macrovasculature to tissue connectivity is given by degree ratios ($D_{A(ex),A}:D_{A(ex),GM}$ and $D_{A(ex),A}:D_{A(ex),GM}$) (Fig. 10)"*—the arterial ratio is listed twice instead of listing venous ($D_{V(\text{ex}),V}:D_{V(\text{ex}),\text{GM}}$) and arterial ($D_{A(\text{ex}),A}:D_{A(\text{ex}),\text{GM}}$).
  3. `Figure 11` caption (line 174): Prints $\sigma^2_{a(ex),s}:\sigma^2_{a(ex),GM}$ (`s` instead of `a`).
  4. `Discussion` (line 224): States *"our results show that $\mu(\sigma^2_{A(ex),A}:\sigma^2_{A(ex),GM})$ values are much higher than the mean of other variance ratios... (Fig. 9)"*, when `Figure 9` shows the *intravascular* ratio $\sigma^2_{A,A}:\sigma^2_{A,\text{GM}}$ (and in the perivascular `Figure 11`, the arterial ratio $\sigma^2_{A(\text{ex}),A}:\sigma^2_{A(\text{ex}),\text{GM}} \approx 0.14\text{--}0.20$ is actually much *lower* than the venous ratio $\sigma^2_{V(\text{ex}),V}:\sigma^2_{V(\text{ex}),\text{GM}} \approx 0.88\text{--}1.04$).
  5. `Study limitations` (offset line 19): States *"the spatial resolution of rs-fMRI is **higher** than that used in most rs-fMRI studies"*, when $4\text{ mm}$ isotropic voxel size is actually **lower** (coarser) spatial resolution than standard modern $2\text{--}3\text{ mm}$ rs-fMRI (as correctly noted earlier on offset line 1: *"At such a low spatial resolution"*).
* **Actionable Fix:** Correct all five notation/terminology typos in lines 160, 168, 174, 224, and offset line 19.

---

## 4. Quantitative Rubric Scoring

| Rubric Dimension | Score | Max | Forensic Justification |
| :--- | :---: :---: | :---: | :--- |
| **1. Methodological & Statistical Rigor** | **2.5** | **3.5** | Systematic within-subject analysis across 120 sessions ($10 \times 12$) with subject-specific TOF segmentations and threshold sensitivity checks; deduction for applying 6 mm FWHM smoothing prior to the 1–3 voxel perivascular distance analysis. |
| **2. Claim-to-Evidence Alignment** | **2.0** | **2.5** | Claims are well bounded, physically reasoned, and accompanied by a thoughtful discussion of susceptibility vs. unsegmented vessel mechanisms and analytical modeling remedies. |
| **3. Data Integrity & Biological Plausibility** | **1.8** | **2.0** | Biophysically sound treatment of diamagnetic arterial vs. paramagnetic venous BOLD susceptibility and orientation effects relative to $B_0$. |
| **4. Reproducibility & Data Integrity** | **1.6** | **2.0** | Uses open Midnight Scan Club data (`OpenNeuro ds000224`) and named open-source tools (`Brain Charter`, `FSL`, `AFNI`, `FreeSurfer`), with minor deductions for subscript typos in `Results`/`Discussion` and code available upon request. |
| **Scientific Core Score** | **6.3** | **8.0** | Sum of Rigor + Claims + Biology (`2.5 + 2.0 + 1.8`). |
| **Overall Composite Score** | **7.9** | **10.0** | **Strong / Sound** (`2.5 + 2.0 + 1.8 + 1.6`). |
