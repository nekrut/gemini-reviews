# Review of ANON_07

**Manuscript Title:** [REDACTED FOR BLINDED REVIEW]  
**Authors:** [REDACTED FOR BLINDED REVIEW]  
**Journal / Preprint:** [REDACTED FOR BLINDED REVIEW]  
**Overall Score:** **8.1 / 10.0** (Strong / Sound) | **Scientific Core Score:** **6.5 / 8.0**  
**Overall Score:** 8.1 / 10.0  
* **Score Breakdown:** Rigor: 2.6/3.5 | Claims: 2.1/2.5 | Biology: 1.8/2.0 | Reproducibility: 1.6/2.0  
**Score Breakdown:** Methodological Rigor: 2.6/3.5 | Claim-Evidence Alignment: 2.1/2.5 | Biological Plausibility: 1.8/2.0 | Reproducibility: 1.6/2.0  
**Verdict:** Strong / Sound

---

### 1. SUMMARY AND OVERALL IMPACT STATEMENT (Executive Summary)

This manuscript reports the major features and practical usage strategies of MAFFT version 7 for multiple sequence alignment (MSA). It focuses on phylogenetic-aware alignment extension (`--add`, `--addfragments`, and `--addprofile` versus legacy `mafft-profile`), automatic strand orientation adjustment (`--adjustdirection`), multithreaded parallelization (`--thread`), scoring matrix parameterization for closely versus distantly related sequences, and structure-seeded alignment (`--seed` combined with ASH structural equivalences). The authors illustrate these capabilities—and candidly highlight MAFFT's failure modes—across three biological test cases: (1) ~300 full-length fungal rDNA sequences combined with ~5,000 non-overlapping ITS1 or ITS2 pyrosequencing reads, (2) 13,822 bacterial 16S rRNA sequences from the Comparative RNA Website (CRW) extended with up to 138,210 artificial fragments (`16S.B.ALL`), and (3) three highly divergent PIN-domain protein structures (PDB: `3v33`, `2qip`, `1taq`).

The paper is unusually transparent about when standard progressive (`FFT-NS-2`), iterative (`L-INS-i`), and profile (`mafft-profile`) alignments fail due to non-additive distance matrices on non-overlapping fragments or root-placement assumptions. However, the empirical evaluation has three notable limitations: (1) hardware configurations are confounded across rows of Table 2 (mixing a 2.67 GHz Xeon E7-8837 with a 3.47 GHz Xeon X5690) and lack comparisons against external fragment-placement tools (e.g., PaPaRa, PAGAN, SEPP), (2) Test Case 1 relies entirely on visual inspection of an unreleased environmental dataset ("Chen W, personal communication"), and (3) the multithreaded iterative refinement mode is noted as non-deterministic without quantifying run-to-run alignment variance. These limitations can be addressed through standardized benchmarking, public deposition of the test alignments, and minor text/equation fixes.

---

### 2. SPECIFIC CONCLUSIONS AND ASSESSMENT OF SUPPORT (Detailed Rubric Evaluation)

* **`--addfragments` accurately aligns non-overlapping fragmentary sequences to a backbone MSA while avoiding the non-additive guide-tree failure of `L-INS-i` and root-placement bias of `mafft-profile` (Test Cases 1 & 2, Table 2, Figs. 1–2): [Well Supported].**  
  The theoretical explanation—that pairwise distances between disjoint ITS1 and ITS2 fragments are large while both are close to full-length sequences, violating distance additivity and distorting the `L-INS-i` WSP/consistency objective—is mathematically and biologically sound. On the `16S.B.ALL` benchmark (Case 1: 13,822 backbone $\times$ 13,821 fragments), `--multipair --addfragments` and `--6merpair --addfragments` achieve 0.9969 and 0.9949 accuracy against the curated CRW reference in 18.3 h and 36.2 min (10 threads), whereas `mafft-profile` drops to 0.2779 accuracy.

* **`--6merpair --addfragments` scales to >138,000 fragments with minimal accuracy loss on conserved rRNA sequences (Table 2, Cases 2 & 3): [Well Supported].**  
  Adding 138,210 fragments to 1,000 or 13,822 backbone sequences completes in 33.8 min (accuracy 0.9969) and 5.91 h (accuracy 0.9949) on 10 cores, whereas the default dynamic-programming `--multipair --addfragments` cannot scale to this regime. The authors appropriately caveat that `--6merpair` degrades on more divergent sequences based on prior simulations.

* **Multithreaded iterative refinement (`--thread`) provides comparable accuracy to serial execution (Section "Parallelization"): [Moderately Supported].**  
  The authors note that while progressive methods yield identical alignments under multithreading, iterative refinement results are non-deterministic across thread counts. No variance or accuracy numbers are shown in the present manuscript (citing only a 2010 application note), and Table 2 only benchmarks multithreading on `--addfragments`.

* **Seeding MAFFT with ASH structural equivalence scores resolves active-site misalignments in highly divergent PIN domains (Test Case 3, Fig. 4): [Moderately Supported].**  
  Using pairwise ASH structural alignments filtered at $e_{ij} \ge 0.5$ ($d_0 = 4$ Å) via `--seed` successfully aligns the catalytic middle aspartic acid across human regnase-1 (`3v33`), *Vibrio parahaemolyticus* VPA0982 (`2qip`), and *Thermus aquaticus* Pol I nuclease domain (`1taq`) where sequence-only `L-INS-i` fails. However, this is a single 3-taxon illustrative example rather than a systematic benchmark across structural families, and the Gaussian equivalence equation is missing from line 147 of the text.

---

### 3. CONSTRUCTIVE AND DOABLE SUGGESTIONS FOR IMPROVEMENT (Major Issues, Minor Issues, Concrete Recommendations)

#### Major Issues
1. **Confounded Hardware and Missing External Baselines in Table 2:** In Table 2, footnote `b` indicates that `mafft --localpair --add` was run on a slower 2.67 GHz Intel Xeon E7-8837 (256 GB RAM), whereas the other rows were run on a faster 3.47 GHz Intel Xeon X5690 (48 GB RAM), confounding CPU and wall-clock time comparisons. Furthermore, since `16S.B.ALL` was taken directly from the SEPP benchmark (Mirarab et al. 2012), omitting the accuracy and runtime of SEPP, PaPaRa, or PAGAN on the exact same dataset leaves readers unable to judge MAFFT's relative standing.
2. **Unreleased Test Case 1 Dataset and Qualitative-Only Evaluation:** The fungal ITS dataset (~300 full-length + ~5,000 ITS1/ITS2 reads) is cited as "Chen W, personal communication" and evaluated solely via visual inspection of Jalview blocks (Fig. 2).

#### Minor Issues
1. **Missing Equation on Line 147:** In Section "Strategy for Integrating Structural Alignments and MAFFT" (line 147), the displayed equation for the Gaussian equivalence score $e_{ij} = \exp(-d_{ij}^2 / d_0^2)$ (or its exact ASH functional form) is blank, and the inline threshold expression on line 148 ("at 0.5") is missing the $\ge$ symbol (`e_ij >= 0.5`).
2. **Missing Complexity Formula on Line 100:** In Section "Estimating the Direction of DNA Sequences" (line 100), the big-$O$ complexity expression before ", where $n$ is the number of sequences" is blank ($O(n^2)$).
3. **Typo in Abstract Keywords and Table 1:** Line 5 reads "metagemone" instead of "metagenome", and Table 1 (line 21 / line 222) reads `mafft --add mew msa` instead of `mafft --add new msa`.

#### Concrete Recommendations

#### 1. Standardize Hardware and Include External Baselines in Table 2
* **WHY:** Comparing wall-clock runtimes across two different CPU architectures (2.67 GHz E7-8837 vs. 3.47 GHz X5690) distorts the relative computational cost of `--localpair --add`, and omitting published results on `16S.B.ALL` obscures how `--addfragments` compares to dedicated phylogenetic placement aligners.
* **WHAT:** Re-time or normalize the Case 1 runs on a single machine (or report the single-core CPU speed scaling factor), and add reference rows (or discussion metrics) for SEPP/PaPaRa/PAGAN on `16S.B.ALL` Case 1.
* **HOW:** Run a subset timing calibration on both Xeon machines to report normalized CPU hours, and include the published CRW recovery accuracy of SEPP/PaPaRa from Mirarab et al. (2012) alongside MAFFT's 0.9969/0.9949 scores.

#### 2. Deposit or Simulate a Publicly Reproducible ITS1/ITS2 Benchmark for Test Case 1
* **WHY:** Because the fungal ITS dataset is from personal communication and cannot be downloaded, readers cannot reproduce Figure 2 or quantitatively measure alignment accuracy on non-overlapping two-domain fragments.
* **WHAT:** Deposit the anonymized fungal ITS alignment (or a public equivalent extracted from UNITE/GenBank) and report a quantitative accuracy metric (e.g., fraction of ITS1 and ITS2 fragments aligned Exclusively to the 5' and 3' sides of the 5.8S region, respectively).
* **HOW:** Count the exact percentage of ITS1 reads erroneously aligned to the ITS2 locus (and vice versa) under `FFT-NS-2`, `L-INS-i`, `mafft-profile`, and `--addfragments`, and archive the input FASTA files as Supplementary Data.

#### 3. Restore Missing Mathematical Expressions and Fix Typos
* **WHY:** Omitted mathematical formulas in the text prevent readers from implementing or verifying the direction-adjustment complexity and ASH structural equivalence score.
* **WHAT & HOW:**
  1. On line 5 (Keywords), change `metagemone` to `metagenome`.
  2. In Table 1 (lines 21 and 222), change `mafft --add mew msa` to `mafft --add new msa`.
  3. On line 100, insert $O(n^2)$ in "an algorithm with a time complexity of $O(n^2)$, where $n$ is the number of sequences".
  4. On line 147, insert the explicit ASH Gaussian equivalence formula $e_{ij} = \exp(-d_{ij}^2 / d_0^2)$, and on line 148 insert $e_{ij} \ge 0.5$.
