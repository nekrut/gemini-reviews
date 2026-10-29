# Forensic Peer Review: FEXP_ANON_153

**Overall Score:** **1.7 / 10.0** (Fundamentally Invalid) | **Scientific Core Score:** **1.2 / 8.0**
* **Score Breakdown:** Rigor: 0.3/3.5 | Claims: 0.3/2.5 | Biology: 0.6/2.0 | Reproducibility: 0.5/2.0

---

## 1. Blinded Metadata Perception
* **Perceived Tier:** Low Tier (Predatory/Megajournal)
* **Perceived Impact Factor Range:** < 2.0
* **Subfield:** Bioinformatics / Machine Learning for Protein-Binding Peptide Prediction
* **Rationale:** The manuscript contains corrupted mathematical equations (missing factorials in the Shapley value formula, writing the logistic sigmoid equation while calling it the hyperbolic tangent function, writing a continuous wavelet integral for discrete wavelet decomposition), performs supervised feature selection across the entire dataset prior to cross-validation, and reports independent test set metrics in Tables 3 and 4 that are arithmetically impossible for the stated 200-positive / 800-negative test set size and internally inconsistent between tables.

---

## 2. Executive Summary & Editorial Verdict

This manuscript proposes Deep-ProBind, a deep neural network (DNN) classifier trained on a 125-dimensional BorutaSHAP-selected subset of a 1,244-dimensional hybrid feature vector (conjoint triad, pseudo amino acid composition, and discrete wavelet transform of physicochemical indices) to predict protein-binding peptides. A forensic audit reveals that the mathematical definitions, validation pipeline, and reported performance tables are invalid:

1. **Arithmetically Impossible Independent Test Set Metrics & Inter-Table Contradictions (Tables 3, 4, and 5):** The Benchmark Dataset section specifies that the independent test set is unbalanced, containing exactly $N_+ = 200$ positive (binding) peptides and $N_- = 800$ negative (non-binding) peptides ($N = 1,000$). Because the number of true positives ($\text{TP}$) out of 200 positive peptides must be an integer, sensitivity ($\text{SN} = \text{TP}/200 \times 100\%$) can only terminate in `.00%` or `.50%`. Yet Tables 3 and 4 report non-integer sensitivities across every model on the independent dataset, including `SN = 94.36%` ($\text{TP} = 188.72$), `94.06%`, `93.79%`, `92.86%`, `92.57%`, and `92.22%`. Furthermore, for $N_+ = 200$ and $N_- = 800$, if $\text{SN} = 94.36\%$ ($\text{TP} \approx 188.72$) and $\text{SP} = 92.82\%$ ($\text{TN} \approx 742.56, \text{FP} \approx 57.44$), overall accuracy must be $\text{ACC} = 0.2\,\text{SN} + 0.8\,\text{SP} = 93.13\%$ (not `93.62%`), precision is $\text{TP}/(\text{TP}+\text{FP}) = 76.67\%$, the $\text{F1}$ score is $84.60\%$ (not `94.35%` in Table 3 or `94.90%` in Table 4), and $\text{MCC}$ is $0.799$ (not `0.872`). Even on a balanced $1:1$ dataset, $\text{SN} = 94.36\%$ and $\text{SP} = 92.82\%$ yield $\text{F1} = 93.64\%$, contradicting both `94.35%` (Table 3) and `94.90%` (Table 4). By contrast, the literature baseline `PepBind-SVM` in Table 5 (`SN = 86.00%`, `SP = 93.60%`, `ACC = 92.10%`, `MCC = 0.765`) obeys the exact $200/800$ unbalanced relation $0.2(86.00) + 0.8(93.60) = 92.08\% \approx 92.10\%$ and integer sensitivity $\text{TP} = 172/200 = 86.00\%$.
2. **Global Feature Selection Data Leakage:** BorutaSHAP feature selection (reducing 1,244 features to 125 features) is applied to the dataset prior to 10-fold cross-validation and model comparisons, leaking label information into the cross-validation folds.
3. **Corrupted Mathematical Equations (Equations 5, 6, 8, and 10):** Equation 10 defines the hyperbolic tangent (`Tanh`) activation function as $f(i) = \frac{e^i}{1+e^i}$, which is the logistic sigmoid function $\sigma(i) \in (0,1)$, not $\tanh(i) = \frac{e^i - e^{-i}}{e^i + e^{-i}} \in (-1,1)$. Equation 8 (SHAP value formula) omits all three factorial operators, writing $\frac{|S|(|N|-|S|-1)}{|N|}$ instead of $\frac{|S|!(|N|-|S|-1)!}{|N|!}$. Equation 5 (PAAC sequence-order correlation factor) divides by $L - \varepsilon$ while summing to $L - \tau$. Equation 6 defines the Discrete Wavelet Transform (DWT) using a continuous integral $\frac{1}{\sqrt{c}}\int y(i)\Psi(\frac{i-d}{c})\,di$ with undefined mixture of discrete and continuous indices.

**Editorial Verdict:** **Reject.** The manuscript's performance metrics are mathematically irreconcilable with the stated test set composition and internally inconsistent across tables.

### Specific Conclusions and Assessment of Support
* **Claim 1:** Deep-ProBind achieves 93.62% accuracy, 94.36% sensitivity, 92.82% specificity, 94.35% (or 94.90%) F1 score, and 0.872 MCC on the independent test set of 200 positive and 800 negative peptides. `[Methodologically Flawed]` — A positive sample size of $N_+ = 200$ cannot yield $\text{SN} = 94.36\%$ ($\text{TP} = 188.72$), and on a $1:4$ unbalanced dataset $\text{SN} = 94.36\%$ and $\text{SP} = 92.82\%$ yield $\text{F1} = 84.60\%$ and $\text{MCC} = 0.799$, not `94.35%`/`94.90%` and `0.872`. Moreover, the F1 score for the identical model on the identical independent test set is reported as `94.35%` in Table 3 and `94.90%` in Table 4.
* **Claim 2:** BorutaSHAP feature selection reduces the 1,244-dimensional hybrid feature space to 125 optimal features, boosting 10-fold CV accuracy from 85.46% to 92.67%. `[Methodologically Flawed]` — Performing supervised BorutaSHAP feature selection before splitting into 10-fold cross-validation folds leaks validation labels into the feature selection step; additionally, in Table 3 (`Hybrid features without feature selection`, Independent dataset), `SN = 87.34%` and `SP = 84.22%` yield $\text{ACC} = (87.34+84.22)/2 = 85.78\%$ on a $1:1$ set or $84.84\%$ on a $1:4$ set, yet Table 3 reports `ACC = 87.73%` (which exceeds both sensitivity and specificity, an arithmetic impossibility for any weighted average of $\text{SN}$ and $\text{SP}$).
* **Claim 3:** The proposed 4-hidden-layer DNN architecture using hyperbolic tangent (`Tanh`) activation outperforms SVM, RF, KNN, NB, and LR. `[Overstated]` — Equation 10 defines `Tanh` as the logistic sigmoid function $\frac{e^i}{1+e^i}$, and the text in Section "Performance comparison with different classifiers" contradicts its own architecture description by stating that *"The DNN model outperformed the SVM algorithm and other traditional ML because it uses a single processing layer."*

---

## 3. Forensic Defect Inventory

### 3.1 Major Methodological and Statistical Defects

* **Defect 1: Arithmetically Impossible Metrics on the Unbalanced Independent Dataset and Impossible Weighted Averages (Tables 3, 4, and 5).**
  * *Location:* Section "Benchmark dataset" (first half, line 29); Table 3 (first half, lines 163–170); Table 4 (second half, lines 15–29); Table 5 (second half, lines 40–46).
  * *Forensic Evidence:*
    1. Line 29 states: *"The independent dataset is unbalanced and includes 200 binding peptides and 800 non-binding peptides, as adapted from the study by Li et al. [24]."*
    2. For $N_+ = 200$, $\text{SN} = \text{TP}/200 \times 100\%$ must be a multiple of $0.50\%$. In Table 5, the literature baseline `PepBind-SVM [24]` reports `SN = 86.00%` ($\text{TP} = 172/200$) and `SP = 93.60%` ($\text{TN} = 749/800 = 93.625\%$), with $\text{ACC} = (172+749)/1000 = 92.10\%$ and $\text{MCC} = 0.765$, which is arithmetically exact for $N_+ = 200, N_- = 800$.
    3. By contrast, every row reported by the authors for the Independent dataset in Tables 3 and 4 violates integer sample counts and $200/800$ class weighting:
       * In Table 3, `Hybrid features (without feature selection)` on the Independent dataset reports `SN = 87.34%`, `SP = 84.22%`, `ACC = 87.73%`, `F1 = 87.22%`, `MCC = 0.742`. Since $\text{ACC} = \frac{N_+ \text{SN} + N_- \text{SP}}{N_+ + N_-}$ is a convex combination of $\text{SN}$ and $\text{SP}$, $\text{ACC}$ **must** lie strictly between $\min(\text{SN},\text{SP}) = 84.22\%$ and $\max(\text{SN},\text{SP}) = 87.34\%$ for any positive sample sizes $N_+, N_-$. Reporting `ACC = 87.73%` $> \max(87.34\%, 84.22\%)$ is mathematically impossible.
       * In Table 3, `DWT` on the Training dataset reports `SN = 79.31%`, `SP = 75.56%`, `ACC = 77.26%`, `F1 = 79.23%`, `MCC = 0.728`. For $\text{SN} = 79.31\%$ and $\text{SP} = 75.56\%$ on the balanced training set ($N_+ = N_- = 1,192$), true $\text{ACC} = (79.31+75.56)/2 = 77.44\%$ and true $\text{MCC} = \frac{0.7931 \times 0.7556 - 0.2069 \times 0.2444}{\sqrt{0.7931 \times 0.2444 + \dots}} \approx 0.549$, whereas Table 3 reports `MCC = 0.728` (inflated by $+0.179$).
       * In Table 3 vs. Table 4, for `Deep-ProBind` / `Hybrid features (with feature selection)` on the Independent dataset, `F1` is reported as `94.35%` in Table 3 (first half, line 168) and `94.90%` in Table 4 (second half, line 29), while `SN = 94.36%`, `SP = 92.82%`, `ACC = 93.62%`, and `MCC = 0.872` remain unchanged. Neither `94.35%` nor `94.90%` is consistent with $\text{SN} = 94.36\%$ and $\text{SP} = 92.82\%$ under $1:4$ balance ($\text{F1} = 84.60\%$) or $1:1$ balance ($\text{F1} = 93.64\%$).

* **Defect 2: Supervised Feature Selection Leakage Prior to Cross-Validation.**
  * *Location:* Section "Shapley additive explanations (SHAP)" (first half, lines 63–74) and Figure 1.
  * *Forensic Evidence:* The 1,244-dimensional hybrid feature matrix is reduced to 125 features using BorutaSHAP prior to the 10-fold cross-validation evaluation and classifier comparison (Tables 3 and 4). Selecting features using the target labels of the entire dataset before cross-validation introduces supervised lookahead bias.

* **Defect 3: Corrupted Mathematical Definitions Across Feature Extraction, SHAP, and DNN Sections.**
  * *Location:* Equations 5, 6, 8, and 10 (first half, lines 46, 51, 69, and 89).
  * *Forensic Evidence:*
    1. **Equation 5 (PAAC correlation factor $\theta_\tau$):** Written as $\theta_\tau = \frac{1}{L-\varepsilon}\sum_{i=1}^{L-\tau} \theta(R_i, R_{i+\tau}), (\varepsilon < L)$. The denominator index $\varepsilon$ does not match the lag variable $\tau$ in the upper summation limit $L - \tau$.
    2. **Equation 6 (DWT):** Written as $X(c,d) = \frac{1}{\sqrt{c}}\int_{i=1}^{N} y(i)\Psi\left(\frac{i-d}{c}\right)di$, followed by $X_j^{\text{low}}[k] = \sum_{n=1}^{N} y(i)h[2k-i]$ and $X_j^{\text{high}}[k] = \sum_{i=1}^{N} y(i)d_j[2k-i]$, mixing continuous integration from $i=1$ to $N$ with discrete summation indices ($n=1$ while summing over $i$).
    3. **Equation 8 (Shapley values):** Written as $\phi_i = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|(|N|-|S|-1)}{|N|}[v(S \cup \{i\}) - v(S)]$, omitting all three factorial symbols (`!`) in the combinatorial weight $\frac{|S|!(|N|-|S|-1)!}{|N|!}$.
    4. **Equation 10 (Tanh activation function):** Lines 88–89 state *"the dynamic hyperbolic Tangent (Tanh) serves as the activation function... The Tanh function is given by the Eq. 10: $f(i) = \frac{e^i}{1+e^i}$."* That formula is the standard logistic sigmoid function, not the hyperbolic tangent $\tanh(i) = \frac{e^i - e^{-i}}{e^i + e^{-i}}$.

### 3.2 Minor Presentation, Structural, and Editorial Issues
* **Self-Contradictory Architecture Description (Second half, line 32):** After defining a 4-hidden-layer DNN in Table 1 (`128-64-32-16` neurons), line 32 claims: *"The DNN model outperformed the SVM algorithm and other traditional ML because it uses a single processing layer."*
* **Mismatched Reference Citation for Baseline Model (Second half, line 37 vs. line 44):** Line 37 cites `PepBind-SVM [1]` (where Ref. 1 is a general protein-protein interaction paper), whereas Table 5 cites `PepBind-SVM [24]`.

---

## 4. Quantitative Rubric Scoring

* **Methodological & Statistical Rigor (0.3 / 3.5):** Supervised feature selection is performed outside the CV loop, four core mathematical equations are algebraically wrong, and the confusion-matrix-derived metrics in Tables 3 and 4 violate fundamental arithmetic bounds (e.g., $\text{ACC} > \max(\text{SN}, \text{SP})$ and non-integer $\text{TP}$ on $N_+ = 200$).
* **Claim-Evidence Alignment (0.3 / 2.5):** The central claim of superior generalization on the unbalanced independent test set is invalidated by the arithmetic impossibility of the reported sensitivity, F1, accuracy, and MCC figures.
* **Biological & Domain Validity (0.6 / 2.0):** The problem formulation (predicting protein-binding peptides from sequence-derived physicochemical descriptors) is biologically motivated, but no biological case studies, motif analyses, or structural validations are performed.
* **Reproducibility & Transparency (0.5 / 2.0):** A GitHub URL (`[GITHUB_REPO_REDACTED]`) is provided, but the manuscript's equations and evaluation tables contain severe internal contradictions that prevent reproduction of the reported numbers.
* **Scientific Core Score:** **1.2 / 8.0** (`0.3 + 0.3 + 0.6`)
* **Overall Score:** **1.7 / 10.0** (`0.3 + 0.3 + 0.6 + 0.5`)
