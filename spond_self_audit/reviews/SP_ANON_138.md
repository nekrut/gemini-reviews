# Blinded Review: SP_ANON_138

**Composite Score:** 7.1 / 10.0 (Rigor: 2.3/3.5 | Claims: 1.7/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** Low Effective Phylogenetic Sample Size ($N=4$ Origins) & Overparameterized Time-Dependent Curve Fitting
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mid-Stage High-Throughput
**Epistemic Stage:** Basic/Mechanistic Discovery

---

## 1. Executive Summary

This study investigates the macroevolutionary drivers and convergent molecular basis of endothermy in ray-finned fishes and marine vertebrates. The authors assemble a time-calibrated phylogenomic tree of 1,051 ray-finned fishes across 1,099 nuclear exons (763 newly sequenced via exon capture, encompassing 22 endothermic teleost species across 4 independent evolutionary origins) and a comparative genomic dataset of 894 single-copy orthologs across 205 marine vertebrates (including 69 newly sequenced short-read fish genomes). Combining stochastic character mapping (`SIMMAP`), state-dependent diversification (`HiSSE`), phylogenetic generalized logistic regression (`phyloglm`), a modified time-dependent threshold model correlating trait transitions with paleoclimate and cetacean lineage-through-time (`LTT` / `DTT`) curves, fossil co-occurrence across 12 formations, and codon selection analyses (`HyPhy BUSTED-E`, `BUSTED-PH`, and `RER`), the authors conclude that fish endothermy coevolved with cetacean diversification rather than global cooling alone and shares convergent molecular selection in metabolic/muscular genes (`carnmt1`, `dcaf6`, `pyroxd2`, `elapor1`, `pdlim7`). While the dataset generation and error-corrected `BUSTED-E`/`BUSTED-PH` comparative genomics are impressive, the macroevolutionary inference is constrained by an effective sample size of only **four independent origins of endothermy** in ray-finned fishes ($n = 4$ phylogenetic transitions).

---

## 2. Methodological & Statistical Audit

* **Severe Effective Sample Size Limitation ($n = 4$ Evolutionary Origins) in Macroevolutionary Regressions and Threshold Models:** Across the entire 1,051-species ray-finned fish phylogeny, endothermy evolved independently only **four times** (1: Opahs / *Lampris*; 2: Swordfishes + Billfishes / Xiphioidei; 3: Butterfly mackerel / *Gasterochisma*; 4: Tunas / Thunnini, totaling 22 extant species). As Maddison & FitzJohn (2015) and Rabosky & Goldberg (2015) established for phylogenetic comparative methods on binary traits, the statistical degrees of freedom for testing trait associations or time-dependent transition rates are bounded by the number of independent evolutionary transitions ($n = 4$), not the number of tips ($N = 1,051$).
  1. *Multivariate `phyloglm` overparameterization:* In Table 1, the authors fit multiple phylogenetic logistic regressions predicting a binary trait with only 4 independent origins using combinations of multistate categorical predictors (diet classified into **30 groups** and swimming mode differentiated into **11 types**, plus continuous length and depth). Fitting dozens of categorical levels to 4 evolutionary transitions produces severe separation and parameter inflation (e.g., swimming mode 6 jumps from $\beta = 0.08$ in univariate regression to $\beta = 3.24$ in multiple regression).
  2. *Confounding of monotonic Cenozoic `LTT` curves with node ages:* In the time-dependent threshold model (Table 2), the authors substitute paleoclimatic temperature curves with the Lineage-Through-Time (`LTT`) and Disparity-Through-Time (`DTT`) curves of cetaceans (`Neoceti`, `Mysticeti`, `Odontoceti`) and sharks (`Carcharhiniformes`), concluding from lower AIC scores that cetacean diversification drove fish endothermy. However, because all 4 fish endothermy transitions occurred during the Cenozoic (between ~60 Ma and ~15 Ma), *any* clade whose `LTT` curve rises monotonically from the Eocene through the Miocene will mechanically correlate with the cumulative transition probability of those 4 nodes better than a fluctuating $\delta^{18}\text{O}$ curve! Indeed, when the authors shift the fish transition dates older by 25%–50%, the cetacean threshold model fails to converge simply because the shifted dates precede the root of crown `Neoceti`.
* **Rigorous Error-Filtered Codon Selection Testing (`BUSTED-E` and `BUSTED-PH`):** In contrast to the macroevolutionary curve-fitting, the molecular evolution pipeline on the 205-species Marine Vertebrate Dataset (894 orthologs) is methodologically strong. Using `MACSE v2.05` followed by `BUSTED-E` (which isolates alignment/assembly frame-shift errors into an explicit error-sink $\omega$ category) and `BUSTED-PH` (which tests foreground positive selection, background positive selection, and distribution divergence while placing non-focal taxa into a nuisance partition rather than pruning them) avoids the rampant false positives that plague standard branch-site tests on draft short-read assemblies.

---

## 3. Biological / Experimental Grounding & Claim Proportionality

* **`[Well Supported]` Four Independent Cenozoic Origins of Endothermy in Ray-Finned Fishes Without Speciation Rate Acceleration:** The 1,051-species time-calibrated exon phylogeny and `HiSSE` hidden-state models robustly resolve the timing of the four teleost endothermy origins and show that endothermy did not accelerate net lineage diversification (`HiSSE` 4-hidden-state trait-independent model strongly preferred).
* **`[Well Supported]` Convergent Positive Selection and Accelerated Evolution in Metabolic and Muscle Genes Across Marine Endotherms:** The `BUSTED-PH` and `RER` analyses across 205 marine vertebrates identify biologically coherent candidate genes (`carnmt1` in carnosine synthesis/pH buffering, `pyroxd2` in mitochondrial respiration in regional endotherms, `pdlim7` in cardiac/skeletal muscle actin anchorage in full-body endotherms) while candidly reporting that several classic literature candidate genes (`atp2a1/serca1`, `ryr1`) showed phylogeny-wide rather than endotherm-specific positive selection.
* **`[Fragile]` Claim that Competitive Coevolution with Cetaceans Rather Than Paleoclimate Drove the Evolution of Fish Endothermy:** Because this inference rests on correlating $n = 4$ Cenozoic trait origins with smooth cetacean `LTT`/`DTT` curves and descriptive fossil co-occurrence in 12 formations (without an ectothermic control group for fossil co-occurrence), the causal attribution to cetacean competition over abiotic cooling is statistically fragile.

---

## 4. Reproducibility & Data Completeness

* **Data & Code Availability:** Raw sequencing reads (`BioProject PRJNA1077916`), alignments, trees, `HiSSE`/`SIMMAP`/`phyloglm` outputs, and custom scripts (`Datasets S1–S11`) are archived on Dryad/Zenodo and NCBI SRA, providing comprehensive data access.
