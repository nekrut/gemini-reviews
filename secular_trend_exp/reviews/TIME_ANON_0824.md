<Blinded Review: TIME_ANON_0824>
**Composite Score:** 6.4 / 10.0 (Rigor: 2.1/3.5 | Claims: 1.8/2.5 | Biology: 1.3/2.0 | Reproducibility: 1.2/2.0)
**Bias Category:** Algorithmic/Model
**Verdict:** Minor Revision
**Study Modality:** Dry-Lab Secondary Cohort/Database
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 6.4/10
VERDICT: PASS
ESTIMATED_DECADE: 2000s

---

### 1. Executive Summary / SUMMARY
This molecular phylogenetics short report re-evaluates whether Saaremaa virus (SAAV, carried by *Apodemus agrarius*) and Dobrava virus (DOBV, carried by *Apodemus flavicollis*) form reciprocally monophyletic clades on the hantavirus Small (S) genomic segment (nt 37–1232, encoding the nucleocapsid N protein). Adding three newly available S-segment sequences—one SAAV strain from Denmark (`Lolland/Aa1403`, `AJ616854`) and two DOBV strains from southern Russia (`Krasnodar`, `AF442623` and `Goryachiy Klyuch`, `AF442622`)—to yield 7 SAAV and 6 DOBV sequences alongside 14 outgroup hantaviruses (Table 1), the authors infer phylogenies using PHYLIP Maximum Likelihood, Maximum Parsimony, Neighbor-Joining, Fitch-Margoliash, and TreePuzzle (Table 2). Across all 12 method/outgroup combinations, SAAV and DOBV resolve as separate clusters (DOBV bootstrap/puzzle support 79–100%; SAAV support 49–100%, with 10/12 analyses $\ge 70\%$). Using a molecular clock test in TreePuzzle, the DOBV–SAAV divergence time is estimated at 3.0–3.7 MYA.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES & METHODOLOGICAL AUDIT

#### STRENGTHS
- **Sensitivity analysis across multiple phylogenetic algorithms and outgroup choices:** Table 2 systematically compares 5 phylogenetic inference methods (ML, MP, NJ, Fitch-Margoliash, TreePuzzle) across 3 outgroup configurations (Seoul virus `SEOV` only, a 14-taxon hantavirus collection, and unrooted/no-outgroup), transparently reporting where SAAV clade support drops below 70% (e.g., 49% in PHYLIP ML with the full outgroup collection, 58% in Fitch-Margoliash with `SEOV` outgroup).
- **Reproducible dataset specification:** All 27 GenBank accession numbers and the exact alignment region (`nt 37–1232`) are tabulated in Table 1.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Conceptual confusion regarding unrooted ("no outgroup") trees and monophyly:** In Table 2 and the text (line 68), the authors state: *"In fact, a 100% support for SAAV monophyly was reached, when no outgroup sequences were used at all."* In an unrooted tree containing only DOBV and SAAV sequences ("no outgroup"), a single internal bipartition separates the DOBV leaves from the SAAV leaves! However, an unrooted bipartition **cannot** distinguish reciprocal monophyly of both groups from paraphyly of SAAV with respect to a nested monophyletic DOBV clade (or vice versa), because rooting is required to polarize ancestor-descendant directionality! Thus, reporting "100% support for SAAV monophyly" in an unrooted 2-species tree is a fundamental phylogenetic fallacy (it only measures support for the unrooted split, which is identical to the DOBV monophyly split).
- **Dismissal of potential intraspecies/interspecies recombination in `Lolland/Aa1403`:** The authors note that SIMPLOT analysis of `Lolland/Aa1403` (`AJ616854`) showed discordant similarity blocks (nt 200–460 matching Estonian SAAV vs nt 1150–1450 matching Russian/Slovakian SAAV), yet retained it without reporting formal recombination test statistics (e.g., bootscan, Sawyer's test, or GARD/PHI) simply because "the presence of this sequence did not 'break' the molecular clock."
- **Unspecified substitution model and molecular clock calibration:** While the Methods mention that `MODELTEST` and `PAUP` were used to select the best-fit DNA substitution model, the actual model selected (e.g., GTR+I+G, HKY+G) and its parameter estimates (transition/transversion ratio, gamma shape parameter $\alpha$) are never stated in the paper! Furthermore, the calibration point/rate used to convert TreePuzzle branch lengths into "3.0–3.7 MYA" is completely omitted (and hantavirus molecular clock calibrations based on host co-speciation are notoriously ~3–4 orders of magnitude slower than short-term viral substitution rates due to purifying selection and site saturation).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim 1:** Including additional geographic sampling (Danish SAAV and southern Russian DOBV) resolves S-segment phylogenies into separate DOBV and SAAV clusters across distance, parsimony, and likelihood methods. `[Moderately Supported]` — True in rooted trees with moderate support (70–91% in most rooted analyses, though dropping to 49% in full-outgroup ML), whereas the "100% support with no outgroup" is an artifact of unrooted bipartition equivalence.
- **Claim 2:** DOBV and SAAV diverged 3.0–3.7 million years ago. `[Fragile]` — Relies on an unstated deep host-codivergence calibration and a strict clock test on a 1,196-bp coding alignment subject to strong third-codon-position saturation.

### 4. Reproducibility & Data Completeness
- **Accession numbers:** Complete table of 27 GenBank accessions provided (Table 1).
- **Model parameters:** Substitution model name, rate parameters, and clock calibration rate are omitted from the text.
</Blinded Review: TIME_ANON_0824>
