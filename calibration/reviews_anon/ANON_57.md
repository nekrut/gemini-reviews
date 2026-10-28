# Review of ANON_57

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **5.9 / 10.0** (Mixed / Salvageable)  
* **Score Breakdown:** Rigor: 1.7/3.5 | Claims: 1.3/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.5/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

This manuscript applies supervised machine learning (XGBoost, Random Forest, and Support Vector Machine) and Shapley Additive Explanations (SHAP) to classify colorectal cancer (CRC; $n = 191$) versus healthy controls ($n = 251$) by pooling three public 16S rRNA (V4 region) fecal microbiome datasets (Baxter et al. 2016, Zackular et al. 2014, and Zeller et al. 2014; total $N = 442$). After filtering out taxa present in $<10\%$ of samples (retaining 164 of 462 microbial features), applying a centered log-ratio (CLR) transformation, and appending four demographic variables (Age, Gender, BMI, and Country), the authors evaluate models across 20 repetitions of nested 5-fold stratified cross-validation (3-fold inner `RandomizedSearchCV`). Random Forest achieves the highest area under the precision–recall curve ($\text{AUPRC} = 0.668 \pm 0.016$, $\text{ROC-AUC} = 0.699 \pm 0.011$, $\text{Accuracy} = 0.673 \pm 0.015$, $\text{Precision} = 0.729 \pm 0.038$, $\text{F1} = 0.507 \pm 0.030$). SHAP analysis highlights oral-origin pathobionts (*Fusobacterium, Porphyromonas, Peptostreptococcus, Parvimonas*) alongside Age, Gender, and BMI as positively associated with CRC predictions, while *Lachnospira*, *Anaerostipes*, and *Eubacterium* spp. are negatively associated. Processed data and Python scripts are publicly available via Zenodo and GitHub.

While the nested cross-validation design, compositional CLR normalization, and open code repository are positive technical features, the study has three significant analytical and interpretive limitations. First, the CRC and control groups are strongly confounded by Age ($p \le 0.0001$), BMI ($p \le 0.01$), and Gender ($p < 0.01$; 59.7% male in CRC vs. 40.2% in controls), and all three demographic variables rank among the top 20 SHAP predictors; however, the authors never evaluate a demographics-only baseline model or a microbiome-only model to quantify how much of the modest $\text{ROC-AUC} = 0.699$ actually comes from the gut microbiota. Second, although Recall (sensitivity) is defined in Section 3.3 as a primary evaluation metric, it is omitted from Table 3; algebraically inverting $\text{F1} = 0.507$ and $\text{Precision} = 0.729$ reveals that the Random Forest model has a **Recall of only ~38.9%**, missing $>61\%$ of CRC patients and contradicting the Discussion's claim of *"a highly dependable prediction of CRC outcomes."* Third, pooling three multi-country studies into a random 5-fold CV without Leave-One-Dataset-Out (LODO) validation leaves cross-study generalizability untested. Adding demographic/microbiome ablation baselines, reporting Recall in Table 3, and tempering clinical performance claims are straightforward revisions using the authors' existing GitHub pipeline.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Random Forest provides a "highly dependable" diagnostic classification of CRC versus controls ($\text{Precision} = 0.729$, $\text{AUPRC} = 0.668$, $\text{ROC-AUC} = 0.699$) (Abstract, Section 4.2, Table 3, Discussion line 251): [Overstated].**  
  While Section 3.3 (line 136) defines Recall as a key evaluation metric, Table 3 omits the Recall column. From the harmonic mean formula $\text{F1} = \frac{2 \cdot \text{PREC} \cdot \text{REC}}{\text{PREC} + \text{REC}}$, a Precision of $0.729$ and an F1 score of $0.507$ imply $\text{Recall} = \frac{0.507 \times 0.729}{2(0.729) - 0.507} \approx \mathbf{0.389}$ (and similarly $\text{Recall} \approx 0.392$ for SVM and $0.527$ for XGBoost). A screening classifier that misses 61.1% of true CRC cases and achieves $67.3\%$ accuracy (only 10.5 percentage points above the $56.8\%$ majority-class baseline of $251/442$) has modest discriminative power and cannot be characterized as "highly dependable" for clinical diagnosis. Additionally, Section 3.3 (line 148) incorrectly states that AUPRC is suited for datasets *"where the number of positive cases is greater than the number of negative cases"*; in fact, positives are the minority here ($191 < 251$), and AUPRC is specifically informative when positives are rare relative to negatives.

* **Gut microbiome features drive the classifier's discriminative performance beyond host demographic confounders (Sections 2, 4.2–4.3, Table 2, Figures 1, 4): [Fragile].**  
  Figure 1 and Table 2 show highly significant baseline imbalances between CRC and control subjects in Age ($p \le 0.0001$), BMI ($p \le 0.01$), and Gender ($p < 0.01$). Because Age, Gender, and BMI were included as input features and rank among the top 20 SHAP variables (Figure 4B, line 223), and because no ablation comparing (i) Demographics only (`Age + Gender + BMI + Country`), (ii) Microbiome only (`164 CLR taxa`), and (iii) Combined (`Demographics + Microbiome`) was performed, it is unknown how much of the $0.699$ ROC-AUC exceeds a simple logistic regression or Random Forest on Age, Gender, and BMI alone.

* **SHAP analysis consistently identifies oral pathobionts (*Fusobacterium, Porphyromonas, Peptostreptococcus, Parvimonas*) as positively associated with CRC and butyrate-producing Clostridiales (*Lachnospira, Anaerostipes*) as protective across models (Sections 4.3, 5, Figures 4–5, Table 4): [Well Supported].**  
  The directionality of the top microbial genera in the TreeExplainer interventional SHAP summary and dependence plots (Figures 4B, 5) is consistent across RF and XGBoost (overlap coefficient 0.75, Table 4) and aligns well with established metagenomic literature on oral-fecal translocation in CRC. However, a taxonomic discrepancy appears in Section 5 (line 261) and Figure 4B: the authors report species-level taxa (*Eubacterium eligens* and *Eubacterium ventriosum*), whereas Sections 2 (line 35) and 4.1 (line 173) state that the dataset consists exclusively of **genus-level** 16S V4 abundance tables.

* **The preprocessing and nested cross-validation pipeline is free of data leakage and generalizes across cohorts (Sections 3.1, 3.3, 4.1): [Moderately Supported].**  
  Using nested 3-fold inner CV inside 5-fold outer CV across 20 repeats prevents hyperparameter tuning leakage. However, two pipeline details require correction: (1) prevalence filtering (dropping taxa present in $<10\%$ of samples, line 89) was performed across all 442 samples before cross-validation splitting rather than inside each training fold, and (2) the manuscript does not state how zero counts were replaced (e.g., pseudocount or multiplicative replacement) prior to computing the logarithm in the CLR transformation. Moreover, because the 442 samples pool three cohorts (Baxter, Zackular, Zeller), random 5-fold CV mixes samples from the same study across train and test splits rather than testing cross-cohort generalization.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Add Ablation Baselines Decoupling Microbiome Signal from Demographic Confounders (Age, Sex, BMI)
* **WHY:** Age, Gender, and BMI differ significantly between CRC and control subjects (Figure 1, Table 2) and appear among the top 20 SHAP features (Figure 4B). Without a demographics-only baseline, the diagnostic contribution of the 16S microbiome cannot be isolated.
* **WHAT:** Run the exact same 20-repeat nested 5-fold CV pipeline for three feature sets: (1) Demographics only (`Age, Gender, BMI, Country`), (2) Microbiome only (`164 CLR taxa`), and (3) Combined (`Microbiome + Demographics`), and test whether adding microbiome features significantly improves ROC-AUC and AUPRC over demographics alone.
* **HOW:** Subset the input DataFrame in the GitHub pipeline to run RF, XGBoost, and SVM on each of the three feature sets. Add the resulting metrics to Table 3 and report a paired Wilcoxon signed-rank test across the 20 repetitions comparing the AUPRC and ROC-AUC of `Microbiome + Demographics` versus `Demographics only`.

#### 2. Report Recall in Table 3, Evaluate Leave-One-Dataset-Out (LODO) Generalization, and Temper Diagnostic Claims
* **WHY:** Omitting Recall ($\approx 0.389$ for RF) from Table 3 conceals the high false-negative rate ($>61\%$) of the classifier at the default 0.5 probability threshold, and random 5-fold CV does not test transferability across the three source studies (Baxter $n = 291$, Zeller $n = 91$, Zackular $n = 60$).
* **WHAT & HOW:**
  1. Add the `REC` (Recall / Sensitivity) and `Spec` (Specificity) columns to **Table 3** for XGBoost, RF, and SVM.
  2. Add a Leave-One-Dataset-Out (LODO) evaluation (training on two studies and testing on the held-out third study) to assess cross-cohort generalizability.
  3. Revise **Section 5 (line 251)** to replace *"offering a highly dependable prediction of CRC outcomes"* with a balanced assessment acknowledging that 16S V4 genus/OTU profiles with demographics achieve moderate discrimination ($\text{ROC-AUC} = 0.699$, $\text{Recall} = 0.389$ at the default threshold) and would require threshold tuning or shotgun metagenomics/FIT integration for clinical screening.

#### 3. Document Zero-Count Handling in CLR Transformation and Move Prevalence Filtering Inside CV Folds
* **WHY:** The centered log-ratio transformation $\text{CLR}(x_i) = \ln(x_i) - \frac{1}{D}\sum_{k=1}^D \ln(x_k)$ is mathematically undefined when $x_i = 0$, which occurs pervasive in sparse microbiome count tables.
* **WHAT & HOW:** In **Section 3.1 (line 89)**, explicitly state the zero-replacement strategy or pseudocount value (e.g., adding a pseudocount of $1$ or $0.5$, or multiplicative replacement via `scikit-bio`) applied before CLR transformation. Move the $<10\%$ prevalence filter inside the cross-validation loop (`sklearn.pipeline.Pipeline`) so that taxa are filtered using only the 4 training folds in each split. Also specify the kernel type, cost parameter $C$, and SHAP explainer (`KernelExplainer` vs. `LinearExplainer`) used for the SVM model in Sections 3.2.3 and 3.4.

#### 4. Technical, Mathematical, and Editorial Corrections
* **WHY:** Equation typos, taxonomic inconsistencies, and misstated statistical definitions reduce clarity.
* **WHAT & HOW:**
  1. **Section 3.3 (line 148):** Correct *"where the number of positive cases is greater than the number of negative cases"* to *"where the number of positive cases is smaller than the number of negative cases (here, 191 CRC vs. 251 controls)."*
  2. **Section 3.4, Equation 1 (lines 157–161):** Replace the slash notation `/ F / ! ( / S / - / F / - 1 ) ! / S / !` with standard vertical cardinality bars $\frac{|F|!(|S| - |F| - 1)!}{|S|!}$, change $f_x(F \cup j)$ to $f_x(F \cup \{j\})$, and fix line 161 from $S - (F \subseteq \{j\})$ to $S \setminus (F \cup \{j\})$.
  3. **Sections 2, 4.1, and 5 (Taxonomic Resolution):** Clarify how species-level assignments (*Eubacterium eligens, Eubacterium ventriosum* in line 261 and Figure 4B) were obtained when Sections 2 (line 35) and 4.1 (line 173) state that features were aggregated at the **genus level**.
  4. **Section 4 (line 168):** Change *"the prevalence of bacteroides that exerts the most significant influence"* to *"the prevalence of bacterial taxa that exert the most significant influence"* (*Bacteroides* is a specific genus, not a general term for bacteria).
  5. **Section 4.3 (line 223):** Fix the spelling of *"Porphiromonas"* to *"Porphyromonas"*.
  6. **Section 5 (line 259):** Remove the word *"spurious"* in *"This spurious association has been observed in previous works"*, as the authors are describing a reproducible, biologically plausible negative association of *Lachnospiraceae* with CRC rather than a statistical artifact.
