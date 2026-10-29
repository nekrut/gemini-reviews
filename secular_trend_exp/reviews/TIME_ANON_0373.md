<Blinded Review: TIME_ANON_0373>
**Composite Score:** 8.1 / 10.0 (Rigor: 2.8/3.5 | Claims: 2.1/2.5 | Biology: 1.7/2.0 | Reproducibility: 1.5/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Wet-Lab Primary Experimental
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

---

### 1. Executive Summary
This study experimentally determines the RNA secondary structure downstream of the slippery heptanucleotide (`U UUA AAC`, nt 1634–1640) that directs $-1$ programmed ribosomal frameshifting ($-1\text{ PRF}$) between overlapping open reading frames `ORF2a` (protease/VPg) and `ORF2b` (RNA-dependent RNA polymerase, `RdRp`) in Cocksfoot mottle sobemovirus (`CfMV`). Using solution chemical probing (`DMS`, `CMCT`, and `kethoxal`) mapped by primer extension, the authors demonstrate that the stimulatory element starting 7 nt downstream of the slip site (`nt 1648–1676`) folds into a 12-bp stem-loop hairpins structure (`stem 1` of six G–C/C–G pairs + an intrahelical `G1654–U1670` wobble pair and `A–U` pair, separated from a 4-bp `stem 2` by a single bulged `C1667` and capped by a fully solvent-exposed `5'-UACG-3'` tetraloop) rather than an RNA pseudoknot. Through site-directed mutagenesis assayed quantitatively in coupled wheat germ extract (`WGE`, $n = 5$ independent translations per mutant) and *in vivo* via biolistic inoculation of oat plants (`cv. Jaak`, 16 plants per construct across $\ge 2$ independent experiments), they show that disrupting or replacing the second G–C pair of stem 1 (`G1649U`, `C1675A`, or `G1649U/C1675A`) reduces *in vitro* $-1\text{ PRF}$ by ~55% (from $11.1 \pm 1.3\%$ to $4.5\text{–}5.1\%$) and abolishes viral infectivity, whereas expanding the tetraloop to 7 nt (`+UUU`) preserves both $-1\text{ PRF}$ ($13.1 \pm 1.5\%$) and systemic plant infection. The experimental design is thorough and convincing, with a minor caveat regarding coding-sequence pleiotropy in the *in vivo* viral mutants.

### 2. Methodological & Statistical Audit
- **Orthogonal Chemical Probing and Quantitative *In Vitro* Translation:**
  - Chemical modification of `pRF2` transcripts combines three base-specific single-strand probes (`DMS` for N3-C and N1-A, `CMCT` for N3-U and N1-G, and `kethoxal` for N1/N2-G) alongside unmodified control RNA (`UM`) to control for natural reverse-transcriptase pause sites (`Figure 2A`). Strong protection across stems 1 and 2 and complete modification of all four tetraloop bases (`U1660`, `A1661`, `C1662`, `G1663`) and bulged `C1667` provide unambiguous structural evidence against loop-spacer pseudoknot base pairing.
  - *In vitro* frameshifting efficiencies in `WGE` (`Figure 3C`) were quantified by phosphorimaging across $n = 5$ independent translation reactions, properly corrected for background and differential methionine content between `P2a` and `P2a-2b`.
- **Confounding of RNA Structure vs. Amino Acid Coding Changes in *In Vivo* Infectivity Assays (`Figure 4`):**
  - Because the $-1\text{ PRF}$ stimulatory stem-loop lies inside the dual-coding overlap of `ORF2a` ($0\text{ frame}$) and `ORF2b` ($-1\text{ frame}$), mutations introduced into the full-length infectious clone (`CfMV icDNA`) simultaneously alter the encoded polyprotein sequences (`Figure 4A`):
    1. `CfMV mRF(C->A)` (`C1675A`) substitutes Proline to Histidine in `P2a` (`0 frame`) while leaving the `-1 frame` unchanged.
    2. `CfMV mRF(ΔC,+C)` (`ΔC1667, +C1677` to restore reading frame) alters three consecutive amino acids in *both* `P2a` (`Ala-Ala-Cys` $\to$ `Arg-Pro-Val`) and `RdRp` (`Gly-Arg-Leu` $\to$ `Ala-Gly-Cys`).
  - While the authors appropriately acknowledge in the Discussion (lines 102 and 106) that these amino acid substitutions in `P2a` and `RdRp` might independently impair protein function *in vivo*, this ambiguity could have been reduced by testing `pAB(+G)` (or a synonymous/compensatory `G1649C/C1675G` base-pair flip that maintains the high thermodynamic stability of the 6-GC basal stem) in the infectious clone.
- **Compensatory Base-Pair Substitution (`G1649U, C1675A`):**
  - In `Figure 3`, replacing the second `G–C` pair with a weaker `U–A` pair (`G1649U, C1675A`, $5.1 \pm 0.6\%$) did not restore wild-type frameshifting ($11.1 \pm 1.3\%$) relative to the single mismatches (`G1649U` $4.7 \pm 0.8\%$, `C1675A` $4.5 \pm 0.9\%$). The authors correctly interpret this as showing that thermodynamic stability (`G–C` vs. `U–A` hydrogen bonding/stacking at the base of stem 1) is critical for ribosome stalling; however, a `G1649C, C1675G` inversion would have provided a true iso-energetic compensatory control to prove base-pairing restoration.

### 3. Biological / Experimental Grounding & Claim Proportionality
- **`[Well Supported]` The `CfMV` $-1\text{ PRF}$ stimulatory element is a 12-bp bulged stem-loop rather than a pseudoknot:** Chemical probing (`Figure 2`), loop expansion mutagenesis (`+UUU`, `Figure 3`), and preservation of systemic infectivity in `CfMV mRF(+UUU)` (`Figure 4B`) rule out pseudoknot interactions involving the apical loop.
- **`[Well Supported]` Basal stem-1 thermodynamic stability and stem length govern *in vitro* $-1\text{ PRF}$ efficiency, whereas the bulged `C1667` hinge and downstream conserved `CUU` triplet are dispensable:** Converting the `C1667` bulge into a regular base pair (`pAB(+G)`, $10.4 \pm 0.9\%$) or deleting `CUU` (`pAB(ΔCUU)`, $10.4 \pm 1.1\%$) leaves $-1\text{ PRF}$ intact, whereas shortening stem 2 (`pAB(ΔC)`, $7.4 \pm 0.8\%$) or weakening stem 1 (`G1649U`, `C1675A`, `G1649U/C1675A`, $4.5\text{–}5.1\%$) significantly reduces frameshifting.
- **`[Moderately Supported]` Shortening or destabilizing stem 1 abolishes `CfMV` replication *in planta* specifically via reduced $-1\text{ PRF}$:** A ~2-fold drop in `RdRp` synthesis ($11.1\% \to 4.5\%$) or a 33% drop ($11.1\% \to 7.4\%$ in `ΔC`) completely eliminated detectable viral RNA in bombarded oat leaves (`Figure 4B`), which is plausible given tight stoichiometric requirements for viral replicase, but remains partially confounded by the concomitant missense mutations in `P2a` and `RdRp`.

### 4. Reproducibility & Data Completeness
- **Strengths:** Nucleotide coordinates relative to the `CfMV` Norwegian isolate, exact site-directed mutagenesis positions, chemical probing conditions, primer coordinates (`nt 1777–1757`), `WGE` replicate counts ($n = 5$), and biolistic bombardment cohort sizes ($16\text{ plants} \times \ge 2\text{ replicates}$) are clearly specified.
- **Minor Additions:** Reporting the exact oligonucleotide primer sequences used for site-directed mutagenesis and RT-PCR sequencing would facilitate direct replication.
</Blinded Review: TIME_ANON_0373>
