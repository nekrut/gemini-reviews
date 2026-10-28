# Intra-Agent Test–Retest Repeatability Study ($N = 30 \times K = 3$ Blinded Runs)

## 1. Experimental Design
To quantify how much of an agentic forensic peer review's quantitative score ($S \in [1, 10]$), binary failure classification ($S < 6.0$), and specific technical defect discovery is deterministic signal versus stochastic LLM decoding/path variance, we conducted a 3-wave test–retest repeatability experiment (`90` total blinded reviews):

1. **Stratified Sample ($N = 30$ Manuscripts):**
   * **Cohort A (Known Flawed / Retracted / Critiqued, $n = 10$):** 2 manuscripts randomly sampled from each of the 5 benchmark domains (`Viral Evolution`, `Statistical Genetics`, `Cancer & Microbiome`, `Molecular Evolution`, `Transcriptomics & CompBio`).
   * **Cohort B (Validated Benchmark Controls, $n = 10$):** 2 manuscripts randomly sampled from each of the 5 domains.
   * **Cohort C (Random Wild Literature, $n = 10$):** 2 manuscripts randomly sampled from each of the 5 domains.
2. **Independent Re-Anonymization & Context Isolation ($K = 3$ Replicates per Manuscript):**
   * **Run 1 (`ANON_XX`):** Original blinded audit from the 200-paper study.
   * **Run 2 (`REP2_01`–`REP2_30`):** Freshly shuffled manuscript IDs (`seed = 1002`), audited by 3 isolated `anon-reviewer` subagents with zero access to Run 1 or external metadata.
   * **Run 3 (`REP3_01`–`REP3_30`):** Independently re-shuffled manuscript IDs (`seed = 1003`), audited by 3 new isolated `anon-reviewer` subagents.

---

## 2. Quantitative Repeatability Metrics ($\text{ICC}$, Pairwise $r$, and Deviation)

| Metric | Single-Run $\text{ICC}(2,1)$ (Absolute Agreement) | Single-Run $\text{ICC}(3,1)$ (Consistency) | 3-Run Ensemble $\text{ICC}(2,3)$ | Residual $\text{SD}_w = \sqrt{\text{MS}_E}$ | Mean Pairwise $\|\Delta S\|$ | Pairwise Pearson $r_{12} / r_{13} / r_{23}$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Overall Score (`/10.0`)** | **0.9671** | **0.9691** | **0.9888** | **0.46 pts** | **0.49 pts** | `0.979 / 0.968 / 0.964` |
| **Rigor (`/3.5`)** | **0.9692** | **0.9727** | **0.9895** | **0.17 pts** | **0.18 pts** | `0.986 / 0.973 / 0.965` |
| **Claims (`/2.5`)** | **0.9585** | **0.9616** | **0.9858** | **0.14 pts** | **0.15 pts** | `0.975 / 0.959 / 0.964` |
| **Biology (`/2.0`)** | **0.9544** | **0.9538** | **0.9843** | **0.11 pts** | **0.10 pts** | `0.962 / 0.946 / 0.957` |
| **Reproducibility (`/2.0`)** | **0.9139** | **0.9221** | **0.9696** | **0.11 pts** | **0.13 pts** | `0.934 / 0.937 / 0.897` |

### Key Takeaways on Continuous Scores
* **High Single-Run Reliability ($\text{ICC}(2,1) = 0.967$):** By comparison, human peer review inter-rater reliability in biomedical and computer science venues (e.g., NeurIPS consistency experiments, NIH study section audits, and *BMJ*/*JAMA* multi-reviewer studies) typically ranges from $\text{ICC} = 0.20$ to $0.45$. A single blinded `anon-reviewer` pass achieves $\text{ICC}(2,1) = 0.967$ with a within-paper standard deviation of **$0.46$ points** on a 10-point scale.
* **Sub-Score Stability:** `Methodological & Statistical Rigor` ($\text{ICC}(2,1) = 0.969$) and `Claim-to-Evidence Alignment` ($\text{ICC}(2,1) = 0.959$) are the most repeatable sub-scores.

---

## 3. Cohort-Stratified Stability & Binary Classification Concordance (`< 6.0` Threshold)

| Cohort | $n$ | Run 1 Mean | Run 2 Mean | Run 3 Mean | Mean Pairwise $\|\Delta S\|$ | Mean of Per-Paper SDs | `< 6.0` Count (Run 1 / Run 2 / Run 3 / 3-Run Mean) | Unanimous 3/3 Binary Agreement |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Cohort A (Known Invalids)** | 10 | `3.61` | `3.69` | `4.06` | `0.49` | `0.38` | `9/10` \| `9/10` \| `9/10` \| `9/10` (`90%` sens.) | **10 / 10 (`100%`)** |
| **Cohort B (Validated Controls)** | 10 | `8.72` | `9.02` | `9.02` | `0.32` | `0.25` | `0/10` \| `0/10` \| `0/10` \| `0/10` (`100%` spec.) | **10 / 10 (`100%`)** |
| **Cohort C (Wild Literature)** | 10 | `4.98` | `4.84` | `5.08` | `0.66` | `0.52` | `7/10` \| `7/10` \| `8/10` \| `7/10` (`70%` fail) | **8 / 10 (`80%`)** |
| **All Stratified Papers** | **30** | **`5.77`** | **`5.85`** | **`6.05`** | **`0.49`** | **`0.38`** | **`16/30` \| `16/30` \| `17/30` \| `16/30`** | **28 / 30 (`93.3%`)** |

*Note: Residual SD_w = sqrt(MSE from two-way ANOVA) = 0.46; mean of per-paper sample SDs = 0.385; RMS within-paper SD = 0.476.*

* **Fleiss' Kappa ($\kappa$) Across the 3 Blinded Runs:** **$\kappa = 0.9104$** (Pairwise binary agreement $\bar{P} = 95.6\%$).
* **100% Unanimity on Ground-Truth Cohorts A & B (`20 / 20`):** Every single Cohort A and Cohort B manuscript received the exact same binary classification across all 3 runs (`90%` sensitivity and `100%` specificity in Run 1, Run 2, and Run 3). Notably, the single Cohort A false negative (`A30`, Bakewell et al. *PNAS* 2007) was consistently scored above threshold (`7.4`/`7.7`/`8.4`; SD `0.51`), plausibly reflecting $t_0$ information isolation (the manuscript's internal $Q20$ filtering description appears sound without external re-alignment of the draft `panTro1` assembly).
* **Disagreements Are Strictly Confined to the `6.0` Boundary (`5.2 – 7.1`):** The only 2 manuscripts out of 30 (`6.7%`) that crossed the `6.0` cutoff across runs were two Cohort C papers whose 3-run mean scores sit right on the `6.0` decision boundary:
  1. `C45` (*Enterococcus faecium / E. lactis* pangenome): Run 1 = `5.8`, Run 2 = `7.1`, Run 3 = `5.2` (**Mean = `6.03`**).
  2. `C98` (*Cho et al.*, bladder cancer scRNA/bulk signature): Run 1 = `6.4`, Run 2 = `5.6`, Run 3 = `5.5` (**Mean = `5.83`**).

---

## 4. Paper-by-Paper Score & Defect Concordance Table ($N = 30 \times 3$ Runs)

| ID | Cohort | Domain | Run 1 | Run 2 | Run 3 | **3-Run Mean ± SD** | Binary Agreement (`<6.0`) | Core Technical Flaw / Strength Rediscovered Across Runs |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **`A03`** | A | Viral Evol | 2.4 | 2.4 | 2.6 | **2.47 ± 0.12** | 3/3 Fail | Outgroup rooting of median-joining network with ~1,150-mutation distant `RaTG13` (`C->U` homoplasy) + travel ascertainment bias (`Forster et al. PNAS`). |
| **`A26`** | A | Viral Evol | 3.3 | 4.1 | 5.3 | **4.23 ± 1.01** | 3/3 Fail | Applying tumor single-cell ordering (`SCITE`) to SARS-CoV-2 + `C18060U` outgroup homoplasy misplacing derived `WA1` clade at pandemic root (`Kumar et al. MBE`). |
| **`A45`** | A | Stat Gen | 2.8 | 3.2 | 3.0 | **3.00 ± 0.20** | 3/3 Fail | All 3 runs caught European COVID-19 GWAS vs. Japanese (`bbj-a-123`) Graves outcome mismatch AND impossible Table 2 MR-Egger 95% CI $4\times$ narrower than IVW. |
| **`A20`** | A | Stat Gen | 4.4 | 4.3 | 4.7 | **4.47 ± 0.21** | 3/3 Fail | All 3 runs caught that re-identification ($m_{10}=83\%$) is driven by demographic ancestry/sex/pigmentation PCs (facial SNPs add zero $R^2$) + telomere age batch artifact (`Lippert et al. PNAS`). |
| **`A28`** | A | Microbiome | 4.0 | 4.3 | 4.4 | **4.23 ± 0.21** | 3/3 Fail | All 3 runs caught vaginal prostaglandin delivery contaminating fetal organs (*Gardnerella/Lactobacillus*) + kitome (*Bradyrhizobium*) + superantigen T-cell confounding (`Mishra et al. Cell`). |
| **`A27`** | A | Microbiome | 4.0 | 2.6 | 3.8 | **3.47 ± 0.76** | 3/3 Fail | All 3 runs caught unsequenced reagent blanks in low-biomass placenta + marine extremophile/kitome artifacts (*Thioalkalivibrio*, *Burkholderia*) + `MG-RAST` vs `MetaPhlAn` pipeline mismatch (`Aagaard et al. STM`). |
| **`A30`** | A | Mol Evol | 7.4 | 7.7 | 8.4 | **7.83 ± 0.51** | 3/3 Pass (FN) | Deterministic $t_0$ false negative: all 3 runs noted $Q20$ filtering and $N_e$ interpretation while flagging nominal $P=0.049$ OMIM enrichment (`Bakewell et al. PNAS`). |
| **`A05`** | A | Mol Evol | 2.2 | 2.0 | 2.2 | **2.13 ± 0.12** | 3/3 Fail | All 3 runs caught partial GenBank CDS count bias (10–64 snake/bat CDSs vs >28,000 mammal CDSs) + `bat-SL-CoVZC45` clustering with snakes (`Ji et al. JMV`). |
| **`A47`** | A | CompBio | 3.0 | 3.8 | 3.2 | **3.33 ± 0.42** | 3/3 Fail | All 3 runs caught CGGA validation leakage into pre-LASSO screening, feeding `limma::removeBatchEffect` outputs into `DESeq2`, and self-contradictory ICI response claims. |
| **`A46`** | A | CompBio | 2.6 | 2.5 | 3.0 | **2.70 ± 0.26** | 3/3 Fail | All 3 runs caught 12,688 unadjusted Student's $t$-tests at $p<0.05$ yielding ~634 expected false positives out of 715 DEGs (`FDR ~89%`). |
| **`B03`** | B | Viral Evol | 8.4 | 9.0 | 9.3 | **8.90 ± 0.46** | 3/3 Pass | Recombination-partitioned `BUSTED[S]` with 3-rate synonymous HMM + `SDUc` CpG trait evolution showing bat-lineage adaptation (`MacLean et al. PLoS Biol`). |
| **`B05`** | B | Viral Evol | 9.0 | 9.5 | 9.2 | **9.23 ± 0.25** | 3/3 Pass | All 3 runs highlighted `FAVITES` contact-network simulations, forensic identification of the `C17747T` `ARTIC` primer artifact, and unsampled-lineage BEAST GLM (`Worobey et al. Science`). |
| **`B39`** | B | Stat Gen | 9.4 | 9.4 | 9.1 | **9.30 ± 0.17** | 3/3 Pass | Rigorous derivation, block-jackknife SEs, and simulation calibration of LD Score Regression (`Bulik-Sullivan et al. Nat Genet`). |
| **`B38`** | B | Stat Gen | 8.5 | 8.9 | 8.8 | **8.73 ± 0.21** | 3/3 Pass | Strict 3-way split (GWAS discovery, $N=120\text{k}$ validation, $N=289\text{k}$ testing) for `LDpred` GPSs; all 3 runs noted covariate-inclusive AUCs in Table 1 (`Khera et al. Nat Genet`). |
| **`B33`** | B | Microbiome | 9.1 | 9.2 | 9.2 | **9.17 ± 0.06** | 3/3 Pass | Multi-center *S. bongori* serial dilutions across 4 kits proving reagent kitome ($\sim 500$ copies/$\mu$L) dominates low-biomass samples (`Salter et al. BMC Biol`). |
| **`B30`** | B | Microbiome | 6.5 | 6.8 | 7.5 | **6.93 ± 0.51** | 3/3 Pass | Valuable human anti-PD-1 gut microbiome cohort, tempered in all 3 runs by small murine FMT ($n=2$ vs $n=3$, $p=0.20$) and HPF pseudoreplication (`Gopalakrishnan et al. Science`). |
| **`B19`** | B | Mol Evol | 9.1 | 9.5 | 9.5 | **9.37 ± 0.23** | 3/3 Pass | Exact $O(B)$ Felsenstein pruning mixture over branch-specific $\omega$ (`MEME`), boundary LRT calibration, and EB uncertainty principle (`Murrell et al. PLoS Genet`). |
| **`B20`** | B | Mol Evol | 8.6 | 9.1 | 9.1 | **8.93 ± 0.29** | 3/3 Pass | Gene-wide random-effects codon model (`BUSTED`) with conservative $\chi^2_2$ null bound outperforming covarion `fitmodel` (`Murrell et al. MBE`). |
| **`B43`** | B | CompBio | 9.1 | 9.4 | 8.9 | **9.13 ± 0.25** | 3/3 Pass | 48-replicate-per-group yeast RNA-seq benchmark establishing empirical null FPs and power curves across 11 tools (`Schurch et al. RNA`). |
| **`B44`** | B | CompBio | 9.5 | 9.4 | 9.6 | **9.50 ± 0.10** | 3/3 Pass | 18 ground-truth bulk/scRNA datasets + `RNAscope` validation proving cell-level DE pseudoreplication and pseudobulk restoration (`Squair et al. Nat Commun`). |
| **`C38`** | C | Viral Evol | 3.2 | 3.3 | 2.6 | **3.03 ± 0.38** | 3/3 Fail | All 3 runs caught that this 4-paragraph H5N1 piece contains zero original data, makes Highlights claims (milk RNA, ruminant-human transmission) absent from body text, and contradicts itself on cattle susceptibility. |
| **`C32`** | C | Viral Evol | 6.3 | 6.3 | 7.6 | **6.73 ± 0.75** | 3/3 Pass | All 3 runs noted solid 34,106-swab / 297-genome Wave 5 H7N9 surveillance while catching embryonated egg-passage adaptation confounding and the `46 (104.5%)` Table 2 typo. |
| **`C81`** | C | Stat Gen | 5.2 | 4.2 | 4.5 | **4.63 ± 0.51** | 3/3 Fail | All 3 runs caught tautological inclusion of baseline non-fasting plasma glucose as a mediator of incident T2DM, reversed logistic regression with PRS as outcome, and contradictory mediator lists. |
| **`C85`** | C | Stat Gen | 6.2 | 6.7 | 7.4 | **6.77 ± 0.60** | 3/3 Pass | All 3 runs noted well-powered UKB prospective AAA cohort ($N=271,068$) while catching omitted statin/BMI adjustment and impossible Table 1 `PLR` $t$-test $P$-value (`t=7.27, P=0.559`). |
| **`C61`** | C | Microbiome | 4.8 | 4.4 | 4.8 | **4.67 ± 0.23** | 3/3 Fail | All 3 runs caught unadjusted smoking (`53.5%` vs `28.6%`) and BMI confounding in 374 inpatients vs 105 controls, internal contradiction on 3 vs 4 enterotypes, and unvalidated Random Forest AUC. |
| **`C13`** | C | Microbiome | 2.1 | 1.8 | 2.1 | **2.00 ± 0.17** | 3/3 Fail | All 3 runs caught physical pooling of 300 mg stool across patients within each TB group ($N=1$ composite pool per group) analyzed via pseudoreplicated ANOVA + uncomputed mRNA correlations. |
| **`C53`** | C | Mol Evol | 5.4 | 5.5 | 5.5 | **5.47 ± 0.06** | 3/3 Fail | All 3 runs caught treating 1,484 Proteobacterial genomes as independent in non-phylogenetic tests (confounding `tsaB`/`gluQ` loss with endosymbiont AT bias) and using raw codon counts instead of RSCU. |
| **`C45`** | C | Mol Evol | 5.8 | 7.1 | 5.2 | **6.03 ± 0.97** | **2/3 Fail (Split)** | Borderline (`mean 6.03`): all 3 runs caught misinterpreting sister clades as *E. faecium* evolving from *E. lactis* and mislabeling eukaryotic/housekeeping gene names (`fosB`, `vatE`, `tufA`, `groEL`) in AMR lists. |
| **`C98`** | C | CompBio | 6.4 | 5.6 | 5.5 | **5.83 ± 0.49** | **2/3 Fail (Split)** | Borderline (`mean 5.83`): all 3 runs caught cross-cohort feature selection leakage in the 10-gene `Scissor` bladder cancer signature and unadjusted univariate survival claims. |
| **`C86`** | C | CompBio | 4.4 | 3.5 | 5.6 | **4.50 ± 1.05** | 3/3 Fail | All 3 runs caught test-set selection leakage (picking `CoxBoost + plsRcox` by maximizing C-index across the 6 GEO validation sets) and omitting the model's gene weights. |
