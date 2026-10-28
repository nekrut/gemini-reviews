# Blinded Review: TIME_ANON_43
**Composite Score:** 6.4 / 10.0 (Rigor: 2.0/3.5 | Claims: 1.8/2.5 | Biology: 1.4/2.0 | Reproducibility: 1.2/2.0)
**Bias Category:** In Silico Extrapolation Without Experimental Neutralization Validation
**Verdict:** Minor Revision
**Study Modality:** Dry-Lab Secondary Cohort/Database Re-Analysis
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Translational/Preclinical/Biomarker

---

### 1. Executive Summary

This short bioinformatics communication evaluates the sequence and structural conservation of 10 experimentally defined protective monoclonal antibody (mAb) epitopes on the Ebolavirus glycoprotein (GP)—specifically focusing on the 6 mAbs comprising the therapeutic cocktails ZMab, ZMapp, and MB-003—across 42 non-redundant full-length Ebolavirus GP sequences spanning the five *Ebolavirus* species (`Zaire`, `Bundibugyo`, `Tai Forest`, `Reston`, `Sudan`) and the contemporary Zaire EBOV outbreak lineage. Using sequence alignments (MAFFT), surface conservation mapping (ConSurf), and structure-based free-energy perturbation (FoldX on PDB `2QHR`), the author reports that epitope sequence identity within Zaire EBOV is $>98\%$ for 5 of the 6 cocktail mAbs, with only the linear mucin-like domain epitope recognized by mAb `13F6-1-2` (404-VEQHHRRTDND-414, part of MB-003) acquiring two fixed substitutions (`E405G` and `T411A`) in the outbreak lineage. FoldX modeling predicts that `T411A` eliminates a $2.7\ \text{\AA}$ side-chain hydrogen bond with heavy-chain Asp33, destabilizing the peptide–antibody complex by $\Delta\Delta G = +1.24\ \text{kcal/mol}$.

The study addresses a timely, practical question with a straightforward and transparent computational workflow. However, its quantitative rigor is limited by several methodological simplifications: (1) sequence conservation percentages for discontinuous conformational epitopes (such as `2G4`, `4G7`, `1H3`, and `13C6`) are computed from coarse Escape/ELISA region definitions rather than atomic contact interfaces, (2) the FoldX $\Delta\Delta G$ estimate for `T411A` is reported as a single point number without standard deviation across the 5 runs and does not simultaneously model the adjacent `E405G` double mutant or solvent-mediated water bridges, and (3) no *in vitro* ELISA or pseudovirus neutralization assays are performed to verify whether `E405G/T411A` or `A503V` actually alters mAb binding affinity ($K_d$) or $\text{IC}_{50}$.

---

### 2. Methodological & Statistical Audit

* **Coarse Definition of Conformational Epitopes for Percent Identity Calculations:**
  In the Methods and Results (Figs. 1–3), the author retrieves 10 "functional epitopes" from IEDB, of which only two (`13F6-1-2` in PDB `2QHR` and `KZ52` in PDB `3CSY`, plus Sudan virus `16F6` in `3VE0`) had high-resolution X-ray crystal structures defining exact atomic contact residues. For cocktail antibodies `1H3`, `2G4`, `4G7`, and `13C6`, the epitope positions in IEDB were derived from single escape mutants or gross GP truncation/deletion constructs. Calculating "average percent sequence identity" across an inferred region or a single escape residue treats non-contact framework residues and critical energetic hot-spot residues with equal weight, which can either mask critical escape mutations or overstate divergence in non-contacting loop residues.

* **Incomplete Reporting of FoldX Energetic Uncertainty and Double-Mutant Epistasis:**
  In the Methods, the author states that *"FoldX 14 was used with 5 repetitions to calculate the change of the free energy, ΔΔG, upon the T411A mutation in [PDB: 2QHR] after energy minimization."* In the Results, only the point value ($1.24\ \text{kcal/mol}$) is reported without the standard deviation across the 5 runs. Moreover, the author dismisses `E405G` qualitatively (*"while the E405G mutation would unlikely have an effect on the antibody binding"*) without reporting the FoldX $\Delta\Delta G$ for `E405G` alone or for the actual circulating double mutant `E405G + T411A`. In peptide–antibody complexes, replacing glutamate with glycine (`E405G`) substantially increases backbone conformational entropy in the unbound peptide state, which can entropically penalize binding even when the side chain does not form a direct salt bridge with the Fab.

* **Unweighted Redundancy Filtering Across Outbreak vs Historical Lineages:**
  By collapsing all identical GP sequences into 42 non-identical sequences prior to computing group-level mean percent conservation and ConSurf scores, high-frequency circulating haplotypes are weighted identically to singletons or sequencing errors. While acceptable for a broad cross-species overview, conservation metrics within the outbreak group (`Z14`) should explicitly distinguish fixed lineage-defining substitutions from singleton polymorphisms.

---

### 3. Biological / Experimental Grounding & Claim Proportionality

* **Claim that 5 of 6 Cocktail mAb Epitopes Are Highly Conserved Within Zaire EBOV Whereas `13F6-1-2` Acquires `E405G` and `T411A`: `[Well Supported]`**
  Direct alignment of the 11-mer linear epitope `404-VEQHHRRTDND-414` across historical and contemporary Zaire EBOV sequences clearly demonstrates complete conservation from 1976 until the emergence of `E405G` and `T411A` in the outbreak clade, and inspection of the $2.0\ \text{\AA}$ co-crystal structure (`2QHR`) confirms the loss of the $\text{Thr411 O}\gamma\text{--Asp33 O}\delta 1$ hydrogen bond upon alanine substitution.

* **Claim that `T411A` Potentially Alters `13F6-1-2` Specificity and Neutralization Activity: `[Moderately Supported]`**
  A predicted destabilization of $\Delta\Delta G = +1.24\ \text{kcal/mol}$ corresponds to an roughly 8-fold increase in the equilibrium dissociation constant ($K_d \propto \exp(\Delta\Delta G / RT)$ at $300\ \text{K}$). Because `13F6-1-2` is a non-neutralizing protective antibody that functions via Fc-mediated effector mechanisms and binds a linear peptide with high avidity as an IgG bivalent molecule, an 8-fold monovalent affinity reduction may or may not abolish *in vivo* protection. The author appropriately uses cautious language (*"might potentially change"*), matching the computational scope of the study.

* **Claim that Low Cross-Species Conservancy Implies These Epitopes Are Dispensable for Viral Fitness: `[Overstated]`**
  In the Abstract, the author concludes: *"Low conservancy of Zaire EBOV mAb epitopes to other EBOV lineages suggests that these epitopes are not indispensable for viral fitness."* Sequence divergence between distinct *Ebolavirus* species (which diverge by $35\text{--}45\%$ across GP as a whole, particularly in the mucin-like domain) reflects long-term evolutionary divergence and host/immune adaptation, not lack of functional constraint within a given species or freedom from epistatic fitness costs at the GP1/GP2 fusion interface (`KZ52`/`2G4`/`4G7`).

---

### 4. Reproducibility & Data Completeness

* **Strengths:** All PDB identifiers (`2QHR`, `3CSY`, `3VE0`, `3S88`), IEDB epitope identifiers, and NCBI GenInfo (GI) numbers for the 42 non-redundant sequences are embedded in the figures and text. Software tools (`MAFFT L-INS-i`, `Jalview`, `ConSurf`, `YASARA`, `FoldX`) are clearly named.
* **Deficiencies:**
  1. Table 1 is cited in the Methods (*"For the data considered herein (Table 1 and Figure 1)..."*), but there is no Table 1 in the manuscript—only Figures 1–4.
  2. In Figure 4B's caption, `16F6` is misspelled as `16FG`.
  3. Exact FoldX command-line parameters (temperature, pH, ionic strength, `RepairPDB` vs `BuildModel` protocol) and the $\Delta\Delta G$ values for `E405G`, `E405G/T411A`, and `A503V` should be reported in a tabular summary.
