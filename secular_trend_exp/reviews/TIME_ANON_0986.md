<Blinded Review: TIME_ANON_0986>
**Composite Score:** 7.7 / 10.0 (Rigor: 2.6/3.5 | Claims: 2.1/2.5 | Biology: 1.6/2.0 | Reproducibility: 1.4/2.0)
**Bias Category:** None (Methodologically Sound)
**Verdict:** Minor Revision
**Study Modality:** Hybrid Computational + Wet-Lab
**Technology Maturity:** Mature/Classical
**Epistemic Stage:** Basic/Mechanistic Discovery

OVERALL_SCORE: 7.7/10
VERDICT: PASS
ESTIMATED_DECADE: 2010s

---

### 1. Executive Summary / SUMMARY
This molecular systematics, biogeography, and character-evolution study investigates the willow subgenus *Salix* s.l. (Salicaceae) by sequencing $4,688\ \text{bp}$ across four plastid regions (*rbcL*, *matK*, *trnD–T*, *atpB–rbcL*; $3,683\ \text{bp}$ combined) and two nuclear ribosomal DNA spacers (nrDNA ETS, $304\ \text{bp}$; ITS, $682\ \text{bp}$) for 55 specimens representing 51 *Salix* species (41 from subgenus *Salix* s.l. covering all recognized sections, plus 9 from subgenera *Chamaetia* and *Vetrix*) and outgroups (*Populus*, *Dovyalis*). Using maximum parsimony (`PAUP* v4.0b10`), maximum likelihood (`RAxML v7.2.8`), partition homogeneity (`ILD`) tests, galled phylogenetic network reconstruction (`Dendroscope v3.2.8`), fossil-calibrated relaxed molecular clock dating (`BEAST v1.5.4`), and maximum-likelihood ancestral character state reconstruction (`Mesquite v2.75` Mk1 model) for stamen number ($>2$ vs. $2$) and bud-scale morphology (free vs. connate margins), the authors demonstrate that: (1) subgenus *Salix* s.l. is poly-/paraphyletic; (2) section *Triandrae* is non-monophyletic (*S. songarica* groups with *Chamaetia*/*Vetrix* along with *S. bangongensis*, *S. qinghaiensis*, and *S. sericocarpa*, while *S. triandra* + *S. triandroides* form a distinct lineage); (3) extensive cytonuclear and ETS–ITS incongruence ($P \le 0.002$) reflects ancient and ongoing hybridization within the warm-temperate main clade of subgenus *Salix* s.l.; (4) Old World and New World clades of subgenus *Salix* s.l. diverged around the Eocene–Oligocene transition ($33.99\ \text{Ma}$, $95\%$ HPD: $24.77\text{--}44.06\ \text{Ma}$); and (5) multiple stamens and free bud scales are plesiomorphic in *Salix*, with repeated homoplasious transitions to 2 stamens and connate bud scales. The taxonomic sampling, reluctance to concatenate incongruent nuclear/plastid partitions, and open Dryad/GenBank data deposition are strong, with minor methodological caveats regarding direct PCR sequencing of multi-copy nrDNA in polyploid/hybrid willows and overly tight prior parameterization on the root calibration.

### 2. Methodological & Statistical Audit / STRENGTHS & WEAKNESSES

#### STRENGTHS
- **Comprehensive taxonomic coverage of all sections of subgenus *Salix* s.l.:** Sampling 41 species across all Old World and New World sections of subgenus *Salix* s.l. resolves long-standing taxonomic ambiguities (such as demonstrating that *S. songarica* does not group with *S. triandra*/*S. triandroides* despite having 3 stamens).
- **Appropriate handling of topological conflict:** Rather than blindly concatenating plastid and nuclear markers, the authors test partition congruence both via `ILD` and well-supported clade comparisons ($\text{BS} \ge 70\%$), keep ETS, ITS, and combined plastid trees separate when significant conflict is found ($P = 0.002$ between ETS and ITS; $P < 0.001$ between nrDNA and cpDNA), and represent the discordance using galled consensus networks (`Dendroscope`).
- **Exemplary data availability:** Sequence alignments are deposited in Dryad (`doi:10.5061/dryad.qr2vv`) and sequences in GenBank, with complete summary statistics in Table 1.

#### WEAKNESSES & METHODOLOGICAL AUDIT
- **Direct Sanger sequencing of PCR products for multi-copy nrDNA (ITS/ETS) without molecular cloning in a hybridizing/polyploid genus:** Willows (*Salix*) are notorious for frequent allopolyploidy and interspecific hybridization, and nrDNA arrays undergo incomplete concerted evolution (which the authors themselves note as a contributor to the ETS vs. ITS conflict, $P = 0.002$). Directly sequencing PCR amplicons of ITS and ETS without cloning recovers chimeric consensus reads or preferentially amplifies one parental ribotype/pseudogene, which likely contributes to the conflict between linked ETS and ITS spacers (which physically reside in the same 18S–26S rDNA cistron and should share the same genealogical history unless chimeric PCR/paralogy occurs).
- **Overly narrow normal prior ($\text{SD} = 0.3\ \text{Myr}$) on the *Salix*–*Populus* root calibration in `BEAST`:** In Section "Divergence time estimation" (line 182), the root split between *Salix* and *Populus* (based on the 48 Ma stem fossil *Populus tidwellii*) was assigned a normal prior with $\text{mean} = 48\ \text{Ma}$ and **$\text{SD} = 0.3\ \text{Ma}$** ($95\%$ prior interval $47.4\text{--}48.6\ \text{Ma}$), and the *Chamaetia*–*Vetrix* split was given an exponential prior with offset $23\ \text{Ma}$ and $\text{mean} = 1\ \text{Ma}$. Constraining two uncertain fossil calibrations with sub-million-year prior standard deviations artificially narrows the downstream $95\%$ HPD intervals on internal nodes (e.g., *Salix* crown age $43.87\ \text{Ma}$, $95\%$ HPD $37.15\text{--}48.42\ \text{Ma}$).
- **Minor inconsistency in taxon count between Table 1 and Methods:** Methods (line 156) states *"We sampled 55 specimens representing 51 Salix species... Populus and Dovyalis were used as outgroups"* ($55 + 2 = 57$ taxa), which matches `57` taxa for ETS and ITS in Table 1, whereas the plastid columns in Table 1 list `56` taxa without noting which specimen lacked plastid data; also line 37 contains a minor typo (*"plasmid chloroplast DNA"* for *"plastid chloroplast DNA"*).

### 3. Biological / Experimental Grounding & Claim Proportionality
- **Claim that subgenus *Salix* s.l. and section *Triandrae* are non-monophyletic, requiring exclusion of *Pleuradenia*, *S. triandra*/*S. triandroides*, and four Asian species (*S. bangongensis*, *S. qinghaiensis*, *S. sericocarpa*, *S. songarica*):** `[Well Supported]` — Consistently supported by plastid and nuclear phylogenies and morphological reassessment.
- **Claim that multiple stamens and free bud scales are plesiomorphic in *Salix* but evolutionarily labile via convergent reductions/fusions:** `[Well Supported]` — Clearly demonstrated by maximum-likelihood ancestral state reconstructions (Fig. 5).
- **Claim that New World and Old World clades of subgenus *Salix* s.l. are reciprocally monophyletic in plastid DNA due to mid-Tertiary cooling closing high-latitude land bridges, whereas cold-adapted *Chamaetia*/*Vetrix* maintained Holarctic gene flow:** `[Moderately Supported]` — Ecologically coherent and supported by plastid monophyly, though point divergence dates depend heavily on the tightly constrained $48 \pm 0.3\ \text{Ma}$ root prior.

### 4. Reproducibility & Data Completeness
All alignments are publicly archived in Dryad (`http://dx.doi.org/10.5061/dryad.qr2vv`), sequences are in GenBank, voucher specimens are listed in Additional File 1, and all software versions (`Geneious v5.4`, `MEGA v5.2`, `DnaSP v5`, `PAUP* v4.0b10`, `RAxML v7.2.8`, `Dendroscope v3.2.8`, `BEAST v1.5.4`, `Tracer v1.6`, `Mesquite v2.75`) are fully documented.
</Blinded Review: TIME_ANON_0986>
