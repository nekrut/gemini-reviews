# Review of PMC7523107 (10.1101/2020.09.24.311845)

**Manuscript Title:** An evolutionary portrait of the progenitor SARS-CoV-2 and its dominant offshoots in COVID-19 pandemic  
**Authors:** Sudhir Kumar, Qiqing Tao, Steven Weaver, Maxwell Sanderford, Marcos A. Caraballo-Ortiz, Sudip Sharma, Sergei L. K. Pond, Sayaka Miura  
**Journal / Preprint:** *bioRxiv* (`PMC7523107` / `10.1101/2020.09.24.311845`; subsequently published in *Molecular Biology and Evolution*, 2021)  
**Overall Score:** **7.5 / 10.0** (Strong / Sound)  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 1.9/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.6/2.0

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT

Kumar et al. apply a maximum-likelihood Mutation Order Approach (MOA; implemented in SCITE) to reconstruct the early mutational history and most recent common ancestor (`proCoV2`) of human SARS-CoV-2 without inferring a full bifurcating phylogeny. Analyzing three sequential GISAID snapshots—29,681 genomes through July 7, 2020 (`29KG`, 49 SNVs with variant frequency $>1\%$), 68,057 genomes through October 12, 2020 (`68KG`, 84 SNVs), and 172,480 genomes through December 30, 2020 (`172KG`)—the authors orient variant polarity using a three-sarbecovirus outgroup consensus (`RaTG13`, `RmYN02`, and pangolin `MT121216.1`) modified by co-occurrence index (COI) maximization. They infer that `proCoV2` precedes `Wuhan-Hu-1` (`NC_045512`) by three sequential $\alpha$ mutations ($\alpha_1$: C18060U, $\alpha_2$: U8782C, $\alpha_3$: C28144U) plus a basal layer of synonymous U$\to$C $\mu$ variants, and group downstream mutations into a Greek-letter barcode system ($\mu, \nu, \alpha, \beta, \gamma, \delta, \varepsilon, \zeta, \eta$). Codon-aware alignments (`HyPhy` `codon-msa` + `MAFFT`), the inferred `proCoV2` FASTA sequence, and a client-side `minimap2` sequence classifier are provided at `http://sars2evo.datamonkey.org/`.

The haplotype-ordering framework scales well to tens of thousands of low-diversity genomes and avoids arbitrary polytomy resolution in early pandemic trees. However, four methodological and technical issues weaken the main conclusions: (1) SCITE assumes a clonal infinite-sites process where high allele frequency implies early origin and deviations represent sequencing error, which conflicts with APOBEC-driven $\text{C}\to\text{U}$ homoplasy and selective sweeps in SARS-CoV-2; (2) flipping outgroup-derived mutation polarity whenever $\text{COI} < 70\%$ (positions 3037 and 28657) introduces post-hoc circularity; (3) the emergence timeline (late October to mid-November 2019) is computed by dividing an integer point count of $k=3$ substitutions by an average clock rate without propagating Poisson mutational variance; and (4) Extended Data Tables 1 and 2 contain unresolved temporal inversions and extensive typesetting/OCR corruptions. All four issues can be resolved through targeted sensitivity analyses, formal uncertainty bounds, and table corrections using the existing data.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT

* **Ancestral Status of `proCoV2` Relative to `Wuhan-Hu-1` via $\alpha_1\text{--}\alpha_3$ (Positions 18060, 8782, 28144): Moderately Supported.**  
  Outgroup sarbecoviruses match Pango lineage A states at positions 8782 (U), 28144 (C), and 18060 (C), whereas `Wuhan-Hu-1` (lineage B) carries derived alleles, with 896 intermediate genomes in `29KG` supporting the stepwise path (bootstrap confidence level $\text{BCL} = 100\%$). However, equating the 49-SNV barcode root with the single human index case overstates what frequency-weighted MOA can resolve: position 18060 ($\text{U}\to\text{C}$ / $\text{C}\to\text{U}$) is a known homoplasic site, and rooting via a ~1,200-nt divergent sarbecovirus outgroup without modeling early Wuhan ascertainment bias or recombinant outgroup histories leaves alternative basal rootings statistically viable.

* **Pre-December 2019 Emergence Dating (5.8–8.1 Weeks Prior to December 24, 2019): Fragile.**  
  In "The progenitor genome" (page 4) and Methods (page 11), the authors divide 3 base differences by a substitution rate interval ($6.64\times 10^{-4}$ to $9.27\times 10^{-4}$ subs/site/year) to place `proCoV2` in late October to mid-November 2019. Treating $k=3$ substitutions as a deterministic distance ignores Poisson variance on short branches and conflates the coalescent tMRCA with the index human infection. In addition, citing a 409-bp Italian Spike fragment (page 5) as confirming `proCoV2` before December 2019 is uninformative because that amplicon spans 0 of the 49 diagnostic MOA positions.

* **Infinite-Sites Model Specification & COI-Driven Polarity Reversal (Positions 3037, 28657, 28854): Methodologically Flawed.**  
  SCITE absorbs all departures from a single-origin infinite-sites tree into global false-positive ($\text{FPR} = 0.00295$) and false-negative ($\text{FNR} = 0.00418$) error parameters (page 10). In consensus genomes filtered to variants at $>1\%$ global frequency, actual sequencing error is far below $0.3\%$; these parameters are instead fitting recurrent homoplasies (primarily $\text{C}\to\text{U}$ transitions such as C28854U, $\beta_{3b}$). Reversing the outgroup-assigned ancestral state at position 3037 because $\text{U}\to\text{C}$ yielded $\text{COI} = 60\%$ while $\text{C}\to\text{U}$ yielded $\text{COI} = 100\%$ (page 10) circularly conditions the input data on the infinite-sites assumption being tested.

* **Episodic Accumulation of Multi-Variant Groups ($\beta, \varepsilon, \zeta, \eta$): Moderately Supported.**  
  Co-occurrence of multi-mutation haplotypes ($\beta_1\text{--}\beta_3$ in 22,739 genomes vs. 201 intermediates; $\varepsilon_1\text{--}\varepsilon_3$ in 7,624 genomes vs. 42 intermediates) is clear in the data. However, the Wald-Wolfowitz runs test for episodic clustering ($P \ll 0.01$ in `29KG`, $P < 10^{-8}$ in `68KG`, pages 6 and 12) treats $\varepsilon_1$ (G28881A), $\varepsilon_2$ (G28882A), and $\varepsilon_3$ (G28883C) as three independent point mutations. In SARS-CoV-2, `GGG` $\to$ `AAC` at 28881–28883 is a single complex trinucleotide substitution event, which artificially inflates temporal clustering when entered as three separate loci.

* **Consistency of Backbone Structure Across Sample Expansion (`29KG` to `68KG` to `172KG`): Well Supported.**  
  Doubling the sample size from 29,681 to 68,057 genomes preserves the primary mutational hierarchy ($\mu \to \alpha \to \beta \to \{\gamma\delta, \varepsilon, \zeta, \eta\}$) with $\text{COI} > 96.7\%$, and 74 of 80 Pango lineages (v2.0.3) map with $>90\%$ concordance to a single MOA fingerprint (Extended Data Figure 1).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT

#### 1. Separate Homoplasy from Sequencing Error in SCITE and Remove Circular COI Polarity Flipping
* **WHY:** SCITE treats all parallel mutations and back-mutations as sequencing errors ($\text{FPR}/\text{FNR}$), and flipping ancestral/derived states whenever $\text{COI} < 70\%$ (positions 3037 and 28657, page 10) forces the data to conform to a single-origin tree.
* **WHAT:** Quantify site-by-site homoplasy rates and justify root polarity at positions 3037 and 28657 without conditioning on COI maximization.
* **HOW:** Tabulate the mismatch rate between observed genotypes and the SCITE tree separately for each of the 49 (and 84) sites to show which specific loci (e.g., 28854, 11083, 14805) drive the inferred $\text{FPR} = 0.00295$ and $\text{FNR} = 0.00418$. For position 3037, report the parsimony/likelihood support for outgroup homoplasy (`U` in `RaTG13`/`RmYN02`/pangolin vs. `C` in basal human lineages A and B) independently of SCITE's COI metric.

#### 2. Propagate Poisson Mutational Uncertainty in the `proCoV2` Emergence Time Estimate
* **WHY:** Dividing an integer difference of $k=3$ mutations by the substitution rate range ($6.64\times 10^{-4}$ to $9.27\times 10^{-4}$ subs/site/year) ignores the wide variance of a Poisson process at $k=3$ and understates the credible interval around the tMRCA.
* **WHAT:** Replace the point-subtraction window (5.8–8.1 weeks) with a formal probability interval integrating both rate uncertainty and Poisson count variance.
* **HOW:** Model the waiting time $t$ for $k=3$ substitutions across $L = 29,115$ sites under $k \sim \text{Poisson}(\mu L t)$ with $\mu \sim \text{Uniform}(6.64\times 10^{-4}, 9.27\times 10^{-4})$ (or Gamma prior), report the 95% credible interval for $t$, and remove the claim on page 5 that the 409-bp Italian Spike fragment (which covers 0 of the 49 MOA sites) confirms `proCoV2`.

#### 3. Collapse the Linked `N:28881–28883` Trinucleotide Substitution in the Wald-Wolfowitz Runs Test
* **WHY:** Treating simultaneous multi-nucleotide mutations ($\varepsilon_1\text{--}\varepsilon_3$ at 28881–28883) as three independent sequential events violates the independence assumption of the Wald-Wolfowitz runs test (page 12).
* **WHAT:** Re-compute the runs test for episodic variant appearance using strictly independent mutational events.
* **HOW:** Merge positions 28881–28883 into a single locus (`ε1–3`) in the `29KG` (47 loci) and `68KG` (82 loci) first-appearance time vectors ($t_f$) and report the updated runs-test $Z$-scores and $p$-values.

#### 4. Resolve Temporal Ordering Inversions in Extended Data Table 2 and Clarify the $\mu_1\text{--}\mu_7$ Root Definition
* **WHY:** For `29KG`, the authors validate MOA by noting that $t_f(\text{child}) \ge t_f(\text{parent})$ for 47/49 variants (page 3). In Extended Data Table 2 (`68KG`), however, parent mutation $\zeta_1$ (pos 445) has $t_f = 179$ days while its descendants $\zeta_2\text{--}\zeta_7$ have $t_f = 78\text{--}96$ days, and parent $\eta_1$ (pos 1163) has $t_f = 86$ days while $\eta_2$ has $t_f = 51$ days and offshoots $\eta_{1e}, \eta_{1g}, \eta_{1i}$ have $t_f = 55\text{--}73$ days. Moreover, the text states `proCoV2` differs from `Wuhan-Hu-1` at 3 positions ($\alpha_1\text{--}\alpha_3$), whereas Figure 1 and Tables 1–2 place three (`29KG`) or seven (`68KG`) synonymous $\mu$ mutations above $\alpha_1$.
* **WHAT:** Audit the `68KG` first-appearance timestamps and state explicitly whether the `proCoV2` FASTA sequence carries `U` or `C` at $\mu_1\text{--}\mu_7$.
* **HOW:** Report the exact $t_f(\text{child}) \ge t_f(\text{parent})$ concordance fraction for all 84 variants in `68KG`, explain the $\zeta_1$ Day 179 and $\eta_2$ Day 51 inversions, and specify on page 4 whether `proCoV2` is defined at the root above $\mu_1$ (6 or 10 nt differences from `Wuhan-Hu-1`) or at the $\mu_3/\mu_7$ node (3 nt differences).

#### 5. Technical, Mathematical, and Editorial Cleanup
* **WHY:** Numerical mismatches between the text and figures/tables, along with extensive symbol corruptions in Extended Data Tables 1 and 2, detract from reproducibility.
* **WHAT & HOW:**
  * **Main text vs. Methods sample-size mismatch:** Fix `"29,861 genomes"` in Methods (pages 10–11, four occurrences) to match `"29,681 genomes"` reported in Results (page 3) and Methods (page 8).
  * **Dataset label typo:** In Methods ("Testing episodic spread of variants", page 12), change `"64KG"` (twice) to `"68KG"`.
  * **Variant count discrepancy:** On page 12, `68KG` is described as having 72 variants ($>1\%$) plus 12 retained from `29KG` (= 84 total), whereas the Figure 3b caption states `"The 68KG dataset contains 12 additional variants"` (which would imply $49 + 12 = 61$, not 84).
  * **Exponent formatting & lineage typo:** On page 6, change `"P < 1−8"` to `"P < 10^{-8}"`; on page 7, change `"B.1.350"` to `"B.1.351"`.
  * **Extended Data Tables 1 & 2 symbol corruptions:**
    * Replace leading-zero `"0RF3a"` and `"0RF8"` with `"ORF3a"` and `"ORF8"` throughout both tables.
    * Replace capital `"V1"` and `"V2"` (positions 17858 and 17747 at the bottom of Tables 1 and 2) with Greek `"ν1"` and `"ν2"`.
    * In Table 1, two distinct mutations (positions 13862 and 10798) are both labeled `"β3f"` (position 10798 should be `"β3g"`).
    * In Table 2, fix `"5,"` at position 1059 to `"δ1"`, realign shifted labels `"γ1"` (currently on the `β3d` row, pos 25429) and `"δ1"` (currently on the `γ1` row, pos 25563), and replace lowercase `"l"` in `"T>l"` and `"M>l"` (positions 13862, 1059, 4002, 19542, 19718, 26060) with capital `"I"` (`"T>I"`, `"M>I"`).
    * In Table 1, standardize comma decimals (`"2,0%"`, `"2,7%"`, `"2,5%"`, `"1,2%"`) to periods.
