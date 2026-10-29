<Blinded Review: TIME_ANON_0931>
**Composite Score:** 7.6 / 10.0 (Rigor: 2.7/3.5 | Claims: 2.1/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Dry-Lab Theory/Methods/Simulation
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 7.6/10
VERDICT: PASS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary / SUMMARY
This statistical genetics simulation study evaluates three methodological frameworks—`LAMP` (Li et al. likelihood-based joint modeling of linkage and association), `Li-cpg` (conditional on parental genotypes), and `Sun-cpg` (affected sib-pair IBD sharing conditional on candidate genotypes and parental genotypes)—on the Genetic Analysis Workshop 15 (GAW15) Problem 3 simulated rheumatoid arthritis dataset (100 replicates of 1,500 affected sib pairs [ASPs] on chromosome 6, where susceptibility is governed by three true disease loci: `DRB1`, `C`, and `D`). Testing candidate non-dense SNPs (`152–155`, `162`), dense SNPs (`d3437`, `d3439`, `d3931`, `d3933`), two-SNP haplotypes, multi-SNP sets, and the multi-allelic `DRB1` locus at $\alpha = 0.05$, the authors demonstrate that all three methods have high power (`90–100%`) to reject individual non-dense SNPs as the sole causal variant, but have very low power (`8–9%`) to reject the `d3437–d3439` haplotype (which tags the major `DRB1-C` linkage peak of $\text{LOD} \approx 95$) despite its failure to capture the rarer locus `D` ($\text{LOD} \approx 3.3$). In addition, the authors perform a targeted 1,000-replicate simulation of a single 4-allele causal locus (`1,000` ASPs per replicate) to prove that `LAMP` suffers a 100% false rejection rate when its biallelic risk-class assumption is violated, whereas `Sun-cpg` (`5.3%`) and `Li-cpg` (`4.5%`) maintain valid nominal 5% Type I error.

### STRENGTHS
- **Clear Mechanistic Dissection of Linkage-to-Association Conditioning:** The authors lucidly explain *why* linkage-based conditional tests (`Sun-cpg`, `Li-cpg`) have only `8–9%` power to detect the residual locus `D` effect after conditioning on the `d3437–d3439` haplotype, contrasting the small linkage contribution of a rare high-risk allele at locus `D` ($\text{LOD} \approx 3.3$) with its much stronger detectability via stepwise conditional logistic regression.
- **Targeted 1,000-Replicate Type I Error Simulation for Multi-Allelic Markers:** Rather than accepting the `99–100%` rejection of `DRB1` by `LAMP` and `Li-cpg` at face value, the authors construct a clean 1,000-replicate null simulation with a single 4-allele causal marker (multiplicative allele risk factors `0.1, 0.15, 0.2, 0.3`). This simulation decisively proves that `LAMP` rejects the true sole causal locus in `100%` of replicates because of model misspecification (assuming a single high-risk allele), while `Sun-cpg` (`0.053`) and `Li-cpg` (`0.045`) preserve Type I error control.
- **Proportionate, Self-Critical Interpretation:** Claims are carefully calibrated to the statistical properties and limitations of each method.

### 2. Methodological & Statistical Audit / WEAKNESSES & METHODOLOGICAL AUDIT
- **Data-Driven Selection of Candidate SNPs Using Replicates 1–5 Included in the 100-Replicate Power Summary:**
  - Candidate SNPs (`152–155`, `162`, `d3437`, `d3439`, `d3931`, `d3933`) were selected based on linkage and stepwise conditional logistic regression results in Replicates 1–5, and power was then evaluated across all 100 replicates (including Replicates 1–5). While the effect on 100-replicate power estimates is small (at most 5% of the sample), reporting power strictly on the 95 held-out replicates (`Replicates 6–100`) would eliminate any selection-inducement bias.
- **Omission of Binomial Confidence Intervals and Direct Test on True Causal Trio (`{DRB1, C, D}`):**
  - In Table 1, empirical rejection rates across $N = 100$ replicates are reported as integer percentages without binomial standard errors ($\pm 1.96 \sqrt{p(1-p)/100}$, which is $\pm 9.8\%$ at $p = 50\%$).
  - As noted in Methods, the authors did not run `Sun-cpg` on the exact set of three true simulated disease loci (`{DRB1, C, D}`) across the 100 GAW15 replicates to verify that empirical Type I error on the GAW15 chromosome 6 data equals 5% (though the dense SNP sets `{d3437–d3439, d3931}` and `{d3437–d3439, d3933}` serve as near-complete LD proxies and yield `4%` rejection, matching the nominal 5% level).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** *`LAMP`, `Li-cpg`, and `Sun-cpg` have high power (90–100%) to reject single non-dense SNPs as the sole causal variant in the chromosome 6 HLA region.* `[Well Supported]` — Directly supported by Table 1 across 100 GAW15 replicates.
- **Claim 2:** *Tests of whether a candidate haplotype explains observed linkage (`Sun-cpg`, `Li-cpg`) have low power (8–9%) to detect secondary disease loci (such as locus `D`) that make only a small contribution to the overall linkage peak.* `[Well Supported]` — Supported by Table 1 and quantitative LOD score decomposition ($\text{LOD} \approx 95$ vs. $\text{LOD} \approx 3.3$).
- **Claim 3:** *For multi-allelic candidate markers, `LAMP` cannot be used to test whether the marker is the sole causal variant because violation of its single-risk-allele assumption yields 100% false rejection.* `[Well Supported]` — Proven analytically and via the 1,000-replicate simulation study.

### 4. Reproducibility & Data Completeness
- **Benchmark Dataset & Simulation Parameters:** Uses the standardized GAW15 Problem 3 simulated benchmark dataset (`100` replicates, `1,500` ASPs) and fully specifies all parameters of the 1,000-replicate 4-allele simulation (`allele risk factors 0.1, 0.15, 0.2, 0.3`, multiplicative genotype risks, `1,000` ASPs).
</Blinded Review: TIME_ANON_0931>
