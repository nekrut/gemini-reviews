# Review of ANON_41

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **9.3 / 10.0** (Exemplary) | **Scientific Core Score:** **7.4 / 8.0**  
**Overall Score:** 9.3 / 10.0  
* **Score Breakdown:** Rigor: 3.3/3.5 | Claims: 2.3/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.9/2.0  
**Score Breakdown:** Methodological Rigor: 3.3/3.5 | Claim-Evidence Alignment: 2.3/2.5 | Biological Plausibility: 1.8/2.0 | Reproducibility: 1.9/2.0  
**Verdict:** Exemplary

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT (Executive Summary)

This manuscript presents PLINK 1.9, a complete C/C++ algorithmic and systems re-engineering of the PLINK population-genetics and genome-wide association study (GWAS) toolset, alongside the architectural specification for PLINK 2.0. The authors introduce five core computational innovations: (1) bitwise parallel algorithms operating on packed 2-bit genotypes in 960-marker blocks using hardware and SSE2 software `popcount` (`popcount2`) for identity-by-state (IBS) Hamming distances and pairwise linkage disequilibrium ($r$) correlations, (2) $O(n)$-to-$O(n^2 \log n)$ complete-linkage clustering and out-of-core single-variant streaming to eliminate full-matrix RAM bottlenecks, (3) four $2^{15}$-entry partial-sum lookup tables (packing 20 3-bit genotype-pair states per 64-bit word) for double-precision genomic relationship matrix (GRM) computation, (4) $O(\sqrt{n})$-time and $O(1)$-space exact tests for Hardy-Weinberg equilibrium (HWE) and $2 \times 2$ / $2 \times 3$ Fisher's exact tests by terminating tail summation at the IEEE-754 double-precision underflow threshold ($2^{-53}$), and (5) unimodality-bounded early exit for Gabriel et al. $D'$ haplotype block estimation (`--blocks`), plus integration of `PERMORY`, `BOOST`, and coordinate-descent LASSO. Benchmarks across seven 32/64-bit Linux, macOS, and Windows machines on synthetic (`synth1`, `synth2`) and 1000 Genomes Phase 1 (`1000g`, 39.6M variants) datasets demonstrate 1–4 orders of magnitude speedups over PLINK 1.07.

This is an exemplary computational genomics paper: the mathematical derivations, bit-level encodings, and numerical complexity reductions are stated with complete precision, and the software is openly archived under GPLv3 with full benchmark datasets in GigaDB. Only minor technical points warrant clarification: (1) formal upper-bound proofs on the cumulative tail truncation error ($O(n) \cdot 2^{-53} \ell$) for the $O(\sqrt{n})$ Fisher/HWE exact test are deferred to a separate manuscript in preparation, (2) Table 6 omits `Ratio` entries for several rows where `PERMORY 1.1` was benchmarked, and (3) the PLINK 2.0 section describes an unimplemented future specification. None of these detract from the primary deliverable.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT (Detailed Rubric Evaluation)

* **Bit-level parallelism (`popcount` / `popcount2`) and out-of-core streaming accelerate IBS distance, LD pruning (`--indep-pairwise`), and basic I/O by 1–3 orders of magnitude while running in low memory (Tables 1, 2, 4): [Well Supported].**  
  The bitwise derivations for IBS Hamming distance (XOR/AND masks across 960-marker blocks) and pairwise Pearson correlation $r$ (encoding $v_i w_i \in \{-1, 0, 1\}$ into 2-bit `popcount2` partial sums and precomputing marginal moments in $O(mn)$ time when no calls are missing) are mathematically exact. Across 7 hardware configurations, IBS matrix calculation speeds up by $320\times$ to $4,200\times$ (Table 2) and LD pruning speeds up by $360\times$ to $8,700\times$ (Table 4), completing whole-genome LD pruning of 1000 Genomes Phase 1 (39.6M variants) in 14.5k–20.2k seconds on 64-bit machines where PLINK 1.07 runs out of memory.

* **Early-termination exact tests reduce HWE and $2 \times 2$ / $2 \times 3$ Fisher's exact test complexity from $O(n)$ to $O(\sqrt{n})$ time and $O(1)$ space with 10+ digit precision, enabling fast `max(T)` permutation testing (Figs. 1–2, Table 6): [Well Supported].**  
  Because hypergeometric contingency table probabilities decay super-geometrically away from the mode $\ell_{\max}$ with standard deviation scaling as $O(\sqrt{n})$, only $O(\sqrt{n})$ tables in a $2 \times 2$ test (and an $O(\sqrt{n})$-area elliptical annulus in a $2 \times 3$ test, further collapsed by summing rows to $2 \times 2$ marginals) exceed $2^{-53} \ell_{\max}$ or $2^{-53} \ell$. Coupled with `PERMORY`-style bit-parallelism and multithreading, 10,000-permutation `--fisher` case-control runs accelerate by $2,900\times$ to $91,000\times$ over PLINK 1.07 (Table 6).

* **15-bit partial-sum lookup tables enable cross-platform, low-memory, double-precision GRM computation competitive with GCTA (Table 3): [Well Supported].**  
  By packing 5 markers of 3-bit genotype-pair states into four $2^{15}$-entry lookup tables (1 MB total, fitting in L2/L3 cache), PLINK 1.9 computes variance-standardized GRMs in double precision across 32/64-bit Windows, macOS, and Linux where GCTA v1.02/1.24 either runs out of memory or is restricted to 64-bit Linux. The authors transparently report that on the 512-core 64-bit Linux server (`Linux64-512`), GCTA 1.24 (using single-precision arithmetic) is $1.6\times$ to $5\times$ faster than PLINK 1.9 (`Ratio` 0.20–0.64).

* **Unimodality bounds on Hill's cubic diplotype likelihood equation accelerate Gabriel et al. haplotype block identification (`--blocks`) by 3 orders of magnitude (Fig. 3, Table 5): [Well Supported].**  
  Exploiting the fact that the $D'$ log-likelihood on $[0, 1]$ rarely has interior local minima allows immediate classification of "recombination" pairs by checking $L(D' = 0.90) < L(D'_{\text{mode}}) / 220$, skipping 99 of the 101 grid evaluations and pruning windows once recombination pairs exceed the 1:19 ratio threshold. Runtimes on `synth1` drop from 2,323–18,925 s (PLINK 1.07) to 1.3–17.3 s (PLINK 1.90).

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT (Major Issues, Minor Issues, Concrete Recommendations)

#### Major Issues
None that undermine the validity of the methods or results.

#### Minor Issues
1. **Cumulative Tail Bound for Numerator Truncation in $O(\sqrt{n})$ Exact Tests:** In Figure 1, the authors note that tables with relative frequency $< 2^{-53} \ell_{\max}$ have no impact on the denominator due to IEEE-754 double-precision underflow, and state that "A few more tables need to be considered when evaluating the numerator." Specifically, when the observed table itself is in the far tail ($\ell \ll \ell_{\max}$), stopping the numerator sum when subsequent terms drop below $2^{-53} \ell$ omits at most $n$ terms bounded by a geometric series with ratio $r < 1$; stating this geometric-series upper bound explicitly in the text (even briefly) makes the 10-digit accuracy claim self-contained without waiting for the companion paper.
2. **Incomplete `Ratio` Column in Table 6 (`--trend` and `--assoc lin`):** In Table 6, for `--trend (C/C)` on `Linux64-512`, `Win32-2`, and `Win64-2`, timings are reported for all three tools (`PLINK 1.07`, `PERMORY 1.1`, and `PLINK 1.90`), but the `Ratio` column is left blank, whereas for `--assoc lin (QT)` on the same machines, `Ratio` reports the speedup of `PLINK 1.90` over `PERMORY 1.1` (27.2, 0.69, 2.89).
3. **Minor Typographical Duplication (Line 13):** Line 13 reads "However, the five years since the final first-generation update (v1.07), however, have witnessed..." (duplicate "however").

#### Concrete Recommendations

#### 1. State the Geometric Series Tail Bound for the Exact Test Numerator
* **WHY:** In $2 \times 2$ HWE and Fisher's exact tests, readers may wonder whether summing $O(n)$ neglected tail terms each $< 2^{-53} \ell$ could accumulate $O(n \cdot 2^{-53})$ relative error when $n \sim 10^6$ unless the geometric decay ratio is bounded away from 1 in the tail.
* **WHAT:** Add a 1–2 sentence mathematical note in Section "Hardy-Weinberg equilibrium and Fisher's exact tests" bounding the geometric decay ratio $R(k) = \frac{(n_1 - k)(n_2 - k)}{(k+1)(k+2)}$ in the tail outside the observed table.
* **HOW:** Note that for any table strictly more extreme than the mode by at least one standard deviation, the adjacent-table likelihood ratio satisfies $R(k) \le 1 - \Omega(n^{-1/2})$, so the infinite geometric tail sum beyond $2^{-53} \ell$ is bounded by $O(\sqrt{n}) \cdot 2^{-53} \ell \ll 10^{-10} \ell$.

#### 2. Complete the Missing Speedup Ratios in Table 6 and Clarify the Baseline
* **WHY:** Table 6 mixes ratios against `PLINK 1.07` (in the upper sections where `PERMORY` is absent) with ratios against `PERMORY 1.1` (in `--assoc lin`) while leaving the `--trend` rows with `PERMORY` blank.
* **WHAT:** Fill in the six blank `Ratio` cells in the `--trend (C/C)` block of Table 6 and clearly label whether `Ratio` is `PLINK 1.07 / PLINK 1.90` or `PERMORY 1.1 / PLINK 1.90` (or include two ratio columns).
* **HOW:** Compute `285.0 / 2.8 = 102`, `1444.2 / 61.5 = 23.5`, `889.7 / 14.4 = 61.8` (for `synth1`) and `580.9 / 13.7 = 42.4`, `2362.5 / 198.0 = 11.9`, `1423.6 / 34.0 = 41.9` (for `synth2`) vs. `PERMORY 1.1`, alongside the ratios vs. `PLINK 1.07`.

#### 3. Editorial Cleanup
* **WHY:** Removing minor prose typos polishes the presentation.
* **WHAT & HOW:** On line 13 ("Findings", paragraph 1), remove the second "however," from "However, the five years since the final first-generation update (v1.07), however, have witnessed...".
