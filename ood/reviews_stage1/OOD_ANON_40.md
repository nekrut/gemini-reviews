# Review of OOD_ANON_40

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.0 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.4/3.5 | Claims: 1.2/2.5 | Biology: 1.2/2.0 | Reproducibility: 1.2/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This systematic review and coordinate-based Functional Connectivity Network Mapping (FCNM) study aggregates peak coordinates of gray matter (GM) alterations from 26 whole-brain voxel-based morphometry (VBM) studies comparing 667 individuals with anorexia nervosa (AN) and 659 healthy controls (HC). Using resting-state fMRI connectomes from $n = 1,093$ healthy adults in the Human Connectome Project (HCP S1200), the authors generate 4-mm (and sensitivity 1-mm and 7-mm) spherical seed masks for each contrast, threshold group-level one-sample $t$-maps at positive $p_{\text{FDR}} < 0.05$, and define the AN dysfunctional network as voxels present in $\ge 50\%$ of contrasts. They report primary overlap with the canonical auditory network (70.5%), sensorimotor network (SMN, 20.6%), ventral default mode network (DMN, 19.2%), and dorsal DMN (13.1%), along with female-only, adolescent, and adult subgroup analyses. Study-level metadata are tabulated in the article, though extracted coordinate tables and analysis scripts are not deposited in an external repository.

While applying network localization to reconcile heterogeneous VBM findings in AN is a reasonable objective, the current analysis is weakened by four major methodological issues. First, thresholding voxel-wise one-sample $t$-tests across $N = 1,093$ HCP subjects solely by statistical significance ($p_{\text{FDR}} < 0.05$) without a minimum effect-size threshold ($r$ or $t$) or a spatial permutation null model means that tiny correlations ($r \approx 0.065$, explaining $< 0.5\%$ of variance) are binarized as "connected," preferentially nominating high-degree cortical hubs (superior temporal gyrus, precuneus, ACC, precentral gyrus) regardless of seed location. Second, the subgroup analyses in Table 1 and line 171 misclassify multiple adult samples with mean ages of $20.0\text{--}22.8\text{ years}$ (Amianto 2013, D'Agata 2015, Björnsdotter 2018, Phillipou 2018) as "Adolescents," and exhibit an unexplained mathematical discrepancy where the 24-study female-only subset drops Auditory overlap from $70.5\%$ to $22\%$. Third, acute underweight AN (which reflects reversible starvation-induced pseudoatrophy) is pooled with weight-recovered AN and GM increases are pooled with GM decreases. These limitations can be resolved by computational re-analysis using the authors' existing coordinate database and HCP pipeline.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Heterogeneous GM alterations across 26 VBM studies in AN specifically converge onto the canonical auditory network (70.5% overlap), SMN (20.6%), ventral DMN (19.2%), and dorsal DMN (13.1%): [Fragile].**  
  In a sample of $N = 1,093$ HCP participants, the standard error of Fisher's $z$ is $1/\sqrt{1090} = 0.0303$, so a one-sample $t$-test reaches $p_{\text{FDR}} < 0.05$ at $t \approx 2.1$, corresponding to a trivial correlation of $r \approx 0.064$. Without an effect-size cutoff (e.g., $t > 7$ or $r > 0.20$, standard in lesion/coordinate network mapping) and without a spatial null control (comparing the 26 AN contrast seeds against 1,000 sets of random gray-matter seeds matched for sphere count and spatial clustering), it is unclear how much of the $\ge 50\%$ overlap in the superior temporal gyrus, Rolandic operculum, precuneus, ACC, and precentral gyrus reflects true AN specificity versus the baseline global connectivity of cortical hubs in the HCP dataset.

* **Adolescent and adult AN subgroups exhibit distinct network profiles (e.g., 79% LECN, 92% ventral DMN, 93% SMN, and 90% precuneus overlap in adolescents vs. 60% posterior salience and 32% basal ganglia in adults; line 171): [Methodologically Flawed].**  
  Inspection of Table 1 reveals that four studies classified in the "Adolescent" subgroup actually enrolled adult cohorts: Phillipou et al. (2018) had a mean age of $22.8 \pm 6.7\text{ years}$, D'Agata et al. (2015) had a mean age of $21.0 \pm 5.0\text{ years}$, Björnsdotter et al. (2018) had a mean age of $20.3 \pm 2.2\text{ years}$, and Amianto et al. (2013) had a mean age of $20.0 \pm 4.0\text{ years}$ (whereas Van Opstal et al. 2015, mean age $22.1 \pm 3.3\text{ years}$, was classified as "Adult"). Because nearly half of the "Adolescent" subgroup sample ($89/215$ AN patients) comes from studies with mean age $\ge 20\text{ years}$, the developmental interpretations in the Results and Discussion (line 206) are invalid.

* **The female-only subgroup (24 of the 26 studies) shows markedly lower auditory (22% vs. 70.5%) and SMN ($<10\%$ vs. 20.6%) network overlap than the overall sample (lines 131, 171, 204): [Methodologically Flawed].**  
  In Table 1, 23 of the 26 studies are 100% female, two are $\sim 90\%$ female (Castro-Fornieles 2009: 91.6%; Bär 2015: 88.4%), and one is listed as NA (Fonville 2014). Removing at most 2–3 studies out of 26 cannot mathematically reduce the proportion of studies exceeding threshold from $\ge 13/26$ ($50\%$) down to $< 12/24$ ($50\%$) across 70% of the auditory network when both the 10-study adolescent subset (77%) and 16-study adult subset (92%) exceeded 50% across the entire auditory network. Furthermore, Discussion line 204 contradicts itself by first stating that the female-only group had "comparatively lesser involvement observed for the SMN" and then arguing that "female patients may experience more significant impairments in [SMN] network functionality."

* **Identified GM network disruptions represent enduring neurobiological substrates of distorted body image and eating pathology: [Overstated].**  
  The main analysis pools acute underweight AN (10 studies), chronic AN, weight-recovered AN (5 studies), and unspecified state (10 studies), and combines GM decreases with GM increases (acknowledged in line 211). Because acute malnutrition and dehydration produce widespread, reversible cortical GM volume reductions ("pseudoatrophy") that normalize upon weight restoration, pooling acute and recovered patients conflates state-dependent starvation effects with trait-level neurobiological vulnerability.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Add a Spatial Permutation Null Model and a Minimum Effect-Size Threshold ($t$ or $r$)
* **WHY:** With $N = 1,093$ HCP subjects, $p_{\text{FDR}} < 0.05$ binarizes correlations as small as $r \approx 0.064$, inflating overlap in high-degree hub networks even for random coordinates.
* **WHAT:** Apply a standard FCNM effect-size threshold (e.g., $|t| \ge 7$ or Fisher $z \ge 0.20$) and perform a 1,000-iteration spatial permutation test (rotating or randomly relocating the 26 contrast seed masks within the gray matter mask while preserving sphere number and cluster size) to identify regions where AN overlap significantly exceeds null expectation ($p_{\text{perm}} < 0.05$).
* **HOW:** Using the 1,093 preprocessed HCP FC maps, recompute the network probability map at $z \ge 0.20$, generate 1,000 null seed sets matched for coordinate count per study, and test whether canonical network overlap for AN exceeds the 95th percentile of the null distribution.

#### 2. Correct the Adolescent vs. Adult Age-Group Classifications in Table 1 and Audit the Female-Only Subgroup Calculation
* **WHY:** Classifying studies with mean ages of $20.0, 20.3, 21.0,$ and $22.8\text{ years}$ as "Adolescent" invalidates the age subgroup analysis, and the drop in Auditory overlap from $70.5\%$ (26 studies) to $22\%$ (24 female-only studies) indicates a denominator or thresholding bug.
* **WHAT:** Reclassify Amianto et al. (2013), D'Agata et al. (2015), Björnsdotter et al. (2018), and Phillipou et al. (2018) into the Adult (or young adult $\ge 18\text{ years}$) subgroup, restricting the Adolescent subgroup to the 6 true adolescent cohorts with mean age $13.6\text{--}16.5\text{ years}$ (`Castro-Fornieles 2009`, `Gaudio 2011`, `Mainz 2012`, `Bomba 2015`, `Fujisawa 2015`, `Martin Monzon 2017`, `Lenhart 2022`), and audit the script that produced Supplementary Figure S6 (female-only).
* **HOW:** Re-run the subgroup FCNM overlap scripts after correcting the age-group labels and verify the exact number of contrast seeds $K$ and threshold $\lceil 0.5 K \rceil$ used in each subgroup.

#### 3. Stratify Analyses by Illness State (Acute Underweight vs. Weight-Recovered) and Direction of GM Change
* **WHY:** Mixing acute starvation-induced GM reductions with weight-recovered cohorts and GM increases obscures whether network convergence reflects acute malnutrition or persistent trait abnormalities.
* **WHAT:** Run separate FCNM analyses for (a) GM decreases only ($n = 25$ studies), (b) acute AN vs. HC, and (c) weight-recovered AN vs. HC (`Muhlau 2007`, `Boghi 2011 recovered`, `Joos 2011`, `Friederich 2012 recovered`, `Mainz 2012`, `Oliva 2020`).
* **HOW:** Partition the contrast seed masks by clinical state and sign of GM change ($\text{AN} < \text{HC}$ vs. $\text{AN} > \text{HC}$) and report the resulting network overlap polar plots in the main text.

#### 4. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Table 1 contains systematic decimal-point errors in statistical thresholds and garbled sample-size entries, and raw peak coordinates are not provided for reproducibility.
* **WHAT & HOW:**
  1. **Table 1, `Threshold` column (lines 99–122):** Correct the 14 occurrences of `"p < 0.5 FWE"`, `"P < 0.5 FDR"`, and `"P < 0.5 corrected"` to `"p < 0.05 FWE/FDR/corrected"`.
  2. **Table 1, `AN/HC` column (lines 101, 104, 105, 116):** Clarify the multi-line subgroup counts in `Boghi et al. (2011)` (`21/27` is the sum of `10/13` acute and `11/14` chronic—ensure these were not double-counted as 42 AN patients), and fix the truncated/missing HC counts in `Joos et al. (2011)` (`5/18 12`), `Friederich et al. (2012)` (`12/14 13`), and `Kohmura et al. (2017)` (`23/29 23`).
  3. **Supplementary Data:** Add a supplementary table listing all extracted MNI coordinates $(X, Y, Z)$ and contrast directions for the 26 included studies.
  4. **Line 211:** Change the duplicate `"Fourth,"` enumeration to `"Fifth,"`.
