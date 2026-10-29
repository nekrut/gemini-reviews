# Decision Letter 0


### Lin Chen


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PGENETICS-D-24-01090The identification of blood-derived Response eQTLs reveal complex effects of regulatory variants on Inflammatory and Infectious Disease riskPLOS Genetics Dear Dr. Liefferinckx, Thank you for submitting your manuscript to PLOS Genetics. After careful consideration, we feel that it has merit but does not fully meet PLOS Genetics's publication criteria as it currently stands. Therefore, we invite you to submit a revised version of the manuscript that addresses the points raised during the review process. Please submit your revised manuscript within 60 days Jan 07 2025 11:59PM. If you will need more time than this to complete your revisions, please reply to this message or contact the journal office at plosgenetics@plos.org. When you're ready to submit your revision, log on to https://www.editorialmanager.com/pgenetics/ and select the 'Submissions Needing Revision' folder to locate your manuscript file. Please include the following items when submitting your revised manuscript:* A rebuttal letter that responds to each point raised by the editor and reviewer(s). You should upload this letter as a separate file labeled ' Response to Reviewers '. This file does not need to include responses to any formatting updates and technical items listed in the 'Journal Requirements' section below.* A marked-up copy of your manuscript that highlights changes made to the original version. You should upload this as a separate file labeled ' Revised Manuscript with Track Changes '.* An unmarked version of your revised paper without tracked changes. You should upload this as a separate file labeled ' Manuscript '. If you would like to make changes to your financial disclosure, competing interests statement, or data availability statement, please make these updates within the submission form at the time of resubmission. Guidelines for resubmitting your figure files are available below the reviewer comments at the end of this letter. We look forward to receiving your revised manuscript. Kind regards, Lin Chen, Ph.D.Academic EditorPLOS Genetics Anne O'Donnell-LuriaSection EditorPLOS Genetics

Journal Requirements: Additional Editor Comments (if provided): [Note: HTML markup is below. Please do not edit.] Reviewers' comments: Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #1: Overview: Lieﬀerinckx et al. performed cis-eQTL mapping using whole blood samples from N=406 healthy participants across four conditions, including three different immune stimulation and baseline resting. Briefly, the authors discovered ~50% of eQTLs were exclusively found after stimulation treatment, i.e., response eQTLs, which highlighted that eQTL can be context-specific and potentially better explain disease risk. The authors performed colocalization analysis between conditions and between genes to identify cis-regulatory modules and characterize condition specificity of eQTLs. Finally, the authors performed colocalization with GWAS immune traits and identified novel genes that are missed by using resting samples alone. This work will be likely of interest to the statistical genetics and human inflammatory disease communities. This manuscript is written well, and results presented clearly. Overall, I suggest providing more details in describing methods. With that said I have several comments.

1. For the results regarding association between rs1801274 and PC1-TCR, can the author provide more details in interpreting this finding? Given the PCs capture linear combinations of gene expression profile between individuals, can we interpret this as “trans-eQTL” effect in TCR condition? What’s interesting is that rs1801274 is missense variant for FCGR2A, but this gene was not found to be correlated with PC1-TCR (Supplemental Table 2). In fact, after running PCA on the gene expression matrix within each condition, the authors can look at the loading matrix output to determine which genes have highest loading (positive or negative) on the top PC, which reflect correlations.

2. It would be helpful for the author provides more explaination on how the eQTL merging method works. How is it different from colocalization analysis described in Wallace C. PLoS Genet. 2021? Does multiple cRM for a given gene means multiple causal eQTL for this gene?

3. In line with above, can the author provide interpretation on multigenic cRM? I am not surprised they are less common than monogenic cRMs given two genes have to be close enough to share the cis-eQTL association pattern. But it’s not clear how to interpret this in the context of reQTLs across conditions.

4. Regarding the three mechanisms to explain condition-specific cRM, can the author provide some mechanistic hypothesis? For example, could the treatment cause epigenetic markers changes such as h3k27ac for enhancers and h3k4me3 for promoters, or chromatin change (open to close or vice versa), such that detection of eQTLs can be specific to certain condition or the sign of eQTL can differ between conditions.

1. Figure 1A shows the separated clusters of four conditions, consistent with the expectation. To rule out the possibility that this may reflect batch effect, can the authors describe how RNA sequencing was done for these samples? Are they randomly assigned to different batches?

2. Are the axis for Supplemental Figure 1c correctly labeled?

3. For Figure 2B, please add units for values shown on the heatmap Figure 2B. Is it 0-100%? Please switch the color scale to 0 as white and 100 as dark blue, it’s very misleading right now. The color code doesn’t match the captions describing this figure. For example, control is in red (stated as green). Please make sure the color code is correctly described.

4. For Figure 3B, please choose 4 other different colors if you want to color it (not the same colors you used for four conditions), although I don’t think it’s necessary to color it as the upset plot is self-evident.

5. For Figure 3cdf, the x-axis looks like the allele count for risk allele, please annotate and describe the x-axis. Please label the units for y-axis.

6. Add label b in Figure 4.

7. The reference number in line 458 for EAP method looks like wrong. Should be (6) not (7).

Reviewer #2: Liefferinckx et al. presented their work on identifying cis-eQTLs that potentially regulate the expression of nearby genes in both resting and stimulated whole blood samples collected from a homogeneous group of healthy individuals. They identified response eQTLs specific to particular conditions and further provided three different scenarios to explain why a response eQTL was observed under stimulation. Lastly, they overlapped the eQTLs with publicly GWAS data on immune related diseases to identify candidate genes.

My main concerns are as follows:

The authors used whole blood samples rather than sorted specific immune cell populations, such as dendritic cells (reference 8) and monocytes (references 8 & 11) for the innate immune response or T cells (reference 9) for adaptive immune response, as in previous work. Given that differences in abundances of specific immune cells and other blood cell traits across individuals have a genetic basis (Vuckovic et al 2020: https://doi.org/10.1016/j.cell.2020.08.008 ), could the eQTL signals that were identified in whole blood be confounded by blood cell traits? How would it potentially affect the identification of response eQTLs? I understand that performing cell sorting is not feasible at this stage, but have the authors considered using gene expression signatures to infer cell type composition, and assess its effects on the identification of (r)eQTLs? In addition, the authors should discuss the specific advantages and constraints of using whole blood in lines 289-290.

Secondly, there is lack of methods for identifying response eQTLs. Are these defined simply as eQTLs that passed multiple testing correction in one condition but not in another, or are more formal statistical tests performed? The former is less ideal since an eQTL that showed suggestive evidence but did not pass multiple testing correction in other conditions (often due to limited power) could still be potentially shared across conditions, and thus not a true reQTL. Also, are directions of effects considered when defining reQTLs? For example, are eQTLs with opposite effect signs considered context specific eQTLs?

Thirdly, the authors proposed three scenarios to explain context specific eQTL signals. It would be helpful to estimate the proportion that can be attributed to each of the three scenarios in this dataset, and to provide some comments on whether it can be generalisable to other cohorts/dataset.

Lastly, it appears that more eQTLs were identified in the resting samples only compared to stimulated samples (more control specific eQTLs as shown in Figure 3b and 3g; please provide specific numbers if it's not the case). Is this unexpected to the authors too? Given that control samples showed a high proportion of genes with low expression levels (figure 2B), one would expect that it leads to fewer eQTLs as expected under the first mechanism proposed by the authors.

Discuss what’s novel from this study compared to previous response eQTL studies.

Line 112: I don’t think I can find how the driven genes were identified in Methods. Are these driven genes enriched in relevant pathways?

Line 458: please confirm if the correct reference is 6 or 7.

Line 424: please provide more details on the processing of the gene expression data. For instance, how the data were normalised, was the normalisation performed within each condition or across conditions, how correction for covariates was performed (before or after normalisation), etc.

Some work is needed to improve the readability:

• Supplementary Figure 1: what does the x-axis represent in panel C? The y-axis indicates PC1 but panel C looks identical to the TCR group in panel A; however, I think the authors calculated PCs in each condition separately for this GWAS. Could the authors please clarify?

• Figure 2B showing expression heatmap: Could the authors explain what the scale from 0 to 100 means? LPS stimulation (TLR4) is green, not plink as stated in the current legend.

• Could the authors make text in Figure 3 (especially b and g) bigger?

• Figure 3E: the legend refers to a red arrow but I can’t see any

Regarding data sharing: would the summary statistics for cis-eQTLs, response eQTLs, the merged cis regulatory module (cRM) that authors defined in this study, and colocalised or matched eQTL – GWAS signals be made publicly available? These data should not involve any sensitive information, and they would be valuable for future research.

Have all data underlying the figures and results presented in the manuscript been provided?

Large-scale datasets should be made available via a public repository as described in the PLOS Genetics data availability policy , and numerical data that underlies graphs or summary statistics should be provided in spreadsheet form as supporting information.

Reviewer #1: No: Raw data not available and made upon request only. Summary statistics data is in supplemental table

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

[NOTE: If reviewer comments were submitted as an attachment file, they will be attached to this email and accessible via the submission site. Please log into your account, locate the manuscript record, and check for the action link "View Attachments". If this link does not appear, there are no attachment files.] Figure resubmission: While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com/ . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Registration is free. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email PLOS at figures@plos.org. Please note that Supporting Information files do not need this step. If there are other versions of figure files still present in your submission file inventory at resubmission, please replace them with the PACE-processed versions. Reproducibility: To enhance the reproducibility of your results, we recommend that authors of applicable studies deposit laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols


# Author response to Decision Letter 1

Collection date 2025 Apr.

Submitted filename: Review - Point by point answers_final.pdf


# Decision Letter 1


### Lin Chen


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Dear Dr Liefferinckx,

We are pleased to inform you that your manuscript entitled "The identification of blood-derived response eQTLs reveals complex effects of regulatory variants on inflammatory and infectious disease risk" has been editorially accepted for publication in PLOS Genetics. Congratulations!

Before your submission can be formally accepted and sent to production you will need to complete our formatting changes, which you will receive in a follow up email. Please be aware that it may take several days for you to receive this email; during this time no action is required by you. Please note: the accept date on your published article will reflect the date of this provisional acceptance, but your manuscript will not be scheduled for publication until the required changes have been made.

Once your paper is formally accepted, an uncorrected proof of your manuscript will be published online ahead of the final version, unless you’ve already opted out via the online submission form. If, for any reason, you do not want an earlier version of your manuscript published online or are unsure if you have already indicated as such, please let the journal staff know immediately at plosgenetics@plos.org.

In the meantime, please log into Editorial Manager at https://www.editorialmanager.com/pgenetics/, click the "Update My Information" link at the top of the page, and update your user information to ensure an efficient production and billing process. Note that PLOS requires an ORCID iD for all corresponding authors. Therefore, please ensure that you have an ORCID iD and that it is validated in Editorial Manager. To do this, go to ‘Update my Information’ (in the upper left-hand corner of the main menu), and click on the Fetch/Validate link next to the ORCID field. This will take you to the ORCID site and allow you to create a new iD or authenticate a pre-existing iD in Editorial Manager.

If you have a press-related query, or would like to know about making your underlying data available (as you will be aware, this is required for publication), please see the end of this email. If your institution or institutions have a press office, please notify them about your upcoming article at this point, to enable them to help maximise its impact. Inform journal staff as soon as possible if you are preparing a press release for your article and need a publication date.

Thank you again for supporting open-access publishing; we are looking forward to publishing your work in PLOS Genetics!

Twitter: @PLOSGenetics

----------------------------------------------------

Comments from the reviewers (if applicable):

Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #1: The authors addressed all my comments.

Reviewer #2: The authors have significantly improved the manuscript.

My remaining comments regarding the responses to my first comment:

The authors showed that the estimated proportions of cell lines are quite similar across four conditions, which is reassuring (only in terms of the robustness of eQTL detection; not saying I definitely expected the results). That said, this does not entirely rule out the possibility that some eQTLs may be tagging the change in cell type composition. I think a more direct test would be accounting for the cell type proportions as a covariate in eQTL mapping and see if this affects the identification of eQTLs, although I doubt it would have a huge impact given what has been shown by the authors.

The fact that the authors found rs1801274 again in their GWAS of changes in cell type proportions suggests to me that PC1 might capture some of the variation in cell type composition and the association between rs1801274 and PC1-TCR could simply reflect this (relevant to the other reviewer’s first comment). I agree with the authors that we won’t have a definitive answer using data from the current study design.

Have all data underlying the figures and results presented in the manuscript been provided?

Large-scale datasets should be made available via a public repository as described in the PLOS Genetics data availability policy , and numerical data that underlies graphs or summary statistics should be provided in spreadsheet form as supporting information.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

----------------------------------------------------

If you have submitted a Research Article or Front Matter that has associated data that are not suitable for deposition in a subject-specific public repository (such as GenBank or ArrayExpress), one way to make that data available is to deposit it in the Dryad Digital Repository . As you may recall, we ask all authors to agree to make data available; this is one way to achieve that. A full list of recommended repositories can be found on our website .

The following link will take you to the Dryad record for your article, so you won't have to re‐enter its bibliographic information, and can upload your files directly:

http://datadryad.org/submit?journalID=pgenetics&manu=PGENETICS-D-24-01090R1

More information about depositing data in Dryad is available at http://www.datadryad.org/depositing . If you experience any difficulties in submitting your data, please contact help@datadryad.org for support.

Additionally, please be aware that our data availability policy requires that all numerical data underlying display items are included with the submission, and you will need to provide this before we can formally accept your manuscript, if not already present.

----------------------------------------------------

If you or your institution will be preparing press materials for this manuscript, or if you need to know your paper's publication date for media purposes, please inform the journal staff as soon as possible so that your submission can be scheduled accordingly. Your manuscript will remain under a strict press embargo until the publication date and time. This means an early version of your manuscript will not be published ahead of your final version. PLOS Genetics may also choose to issue a press release for your article. If there's anything the journal should know or you'd like more information, please get in touch via plosgenetics@plos.org .


# Acceptance letter


### Lin Chen


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PGENETICS-D-24-01090R1

The identification of blood-derived response eQTLs reveals complex effects of regulatory variants on inflammatory and infectious disease risk

Dear Dr Liefferinckx,

We are pleased to inform you that your manuscript entitled "The identification of blood-derived response eQTLs reveals complex effects of regulatory variants on inflammatory and infectious disease risk" has been formally accepted for publication in PLOS Genetics! Your manuscript is now with our production department and you will be notified of the publication date in due course.

The corresponding author will soon be receiving a typeset proof for review, to ensure errors have not been introduced during production. Please review the PDF proof of your manuscript carefully, as this is the last chance to correct any errors. Please note that major changes, or those which affect the scientific understanding of the work, will likely cause delays to the publication date of your manuscript.

Soon after your final files are uploaded, unless you have opted out or your manuscript is a front-matter piece, the early version of your manuscript will be published online. The date of the early version will be your article's publication date. The final article will be published to the same URL, and all versions of the paper will be accessible to readers.

Thank you again for supporting PLOS Genetics and open-access publishing. We are looking forward to publishing your work!

The PLOS Genetics Team

Carlyle House, Carlyle Road, Cambridge CB4 3DN | United Kingdom

plosgenetics@plos.org | +44 (0) 1223-442823

plosgenetics.org | Twitter: @PLOSGenetics

This section collects any data citations, data availability statements, or supplementary materials included in this article.


## Supplementary Materials

A. Principal component analysis (PCA) of the expression of the most variable 500 genes across the four conditions of stimulation (Control (Ctrl), TLR4, TLR7/8 and TCR stimulations). B. Manhattan plot showing significant association of rs1801274 with PC1 phenotype. Principal Components were calculated for expression of genes in each paired condition (control-stimulated condition). By considering PC as new phenotype in GWAS, rs1801274, located on chromosome 1, was significantly associated with PC1-TCR phenotype (p= 4e-45). C. Distribution of rs1801274 genotypes in the TCR group . TCR group observed in panel A has been highlighted by removing others groups and all individuals have been flagged by genotype of variant rs1801274. Individuals with genotype AA segregate from the two others genotypes (AG and GG) and tend to form the continuum with control group as shown panel A.

A. Manhattan plot showing significant association of rs1801274 with IFN Ɣ level phenotype. IFNƔ level was considered as phenotype and associated with genotypic data through GWAS. rs1801274, located on chromosome 1, was significantly associated with the phenotype (p= 7.72e-40). Geocode cohort available for this phenotype (n= 380). B. Manhattan plot showing significant association of rs1801274 with IL-2 level phenotype. IL-2 level was considered as phenotype and associated with genotypic data through GWAS. rs1801274, located on chromosome 1, was significantly associated with the phenotype (p= p=2.63e-15). Only a sub cohort was available for this phenotype (n= 187).

A. Examples of monogenic cRMs. Graphical representation of one cRM modulating UBE2L 3 (Ubiquitin Conjugating Enzyme E2 L3) and C5 (Complement C5) genes. Every node corresponds to a condition-specific EAP linked to the Gene and edges connect pairs illustrates a significant matching of EAPs with θ ≥| 0.6|. B. Examples of multigenic cRMs. Graphical representation of two multigenic cRMs. The first module clusters eQTLs linked to LLGL1 (LLGL Scribble Cell Polarity Complex Component 1) and TOP3A (DNA Topoisomerase III Alpha) genes. The second module clusters eQTLs linked to TRGJP2 (T Cell Receptor Gamma Joining P2) and TRGJP1 (T Cell Receptor Gamma Joining P1) genes. Every node corresponds to a condition-specific EAP linked to the genes and edges connect pairs illustrates a significant matching of EAPs with θ ≥ | 0.6|. The blue line is used in case of positive θ while red line is used in case of negative θ.

Despite the larger catalog, the plot reveals the continued predominance of condition-specific eQTLs, with the majority being reQTLs. Since this graph only considers monogenic cRMs, the maximum number of eQTLs per gene is four, corresponding to the number of conditions in our dataset. The bars indicate the number of modules.

These manually curated examples highlight eQTLs where the gene is either not expressed or expressed at too low level for the eQTL to be detected in the resting condition, but becomes detectable after stimulation. The boxplots display gene expression levels, with the Y-axis representing normalized gene expression and the X-axis indicating different conditions (Control (Ctrl) condition in red, TCR stimulation in purple, TLR4 stimulation in green, TLR7/8 stimulation in blue).

These manually curated examples highlight eQTLs where there is a loss of genotype effect in one specific condition (resting or one condition of stimulation), while the gene remains expressed at sufficiently high levels for the eQTL to be detected if it exists. X-axis shows the different conditions of stimulation (red – Crtl, purple – TCR, green – TLR4, blue- TLR7/8), and Y-axis shows normalized gene expression. The genes are indicated at the top of each panel. The cRM related to the target gene (in uppercase) are labelled 1000, 0100, 0010 and 0001 for the conditions of stimulation: Ctrl-, TCR-, TLR4 - and TLR7/8 -, respectively. The situations are depicted according to these labels.

The plots represent the EAPs for several selected genes under different conditions of stimulation (red – Crtl, purple – TCR, green – TLR4, blue- TLR7/8). The Y-axis shows the distribution of −log(p) values for all variants in the region around the top cis-eQTL. The X-axis represents a genomic region centered on the Transcriptional Start Site (TSS) of the gene. The selected eGenes are modulated by different cRMs. The peak of pattern of the first cRM is highlighted by a red arrow, while the pattern of the second cRM is highlighted by a blue arrow and when three different cRM exist, the pattern of the third cRM is highlighted by a green arrow.

The dashed line represents the transcriptional start site (TSS) of the CTSS (Cathepsin S) gene. The Y-axis shows the distribution of −log(p) values for all the variants in the region around the top cis-eQTL. The X- axis represents a genomic region centered on the TSS of the CTSS gene. The EAP of the different conditions of stimulation are shown in colors (red – Crtl, purple – TCR, green – TLR4, blue- TLR7/8). The EAP in Ctrl condition (in red) is sufficiently different from EAPs in TLR4 and TLR7/8 conditions to be included in a specific cRM (cRM 4515). EAPs related to TLR4 and TLR7/8 conditions were similar and merged in a same cRM (cRM 2090).

A Zoom plot of a locus on Chromosome 2 illustrating the correlation between DAP for IBD (red) and EAP for PLCL1 gene (grey). A p-value was calculated for each association between each neighbouring variants of SNP and the expression of the AJ009632.2 gene within a specifically defined window around this target gene under each condition of stimulation. The EAP, shown on left Y-axis, represents the distribution of association −log(p) values for all the variants in the region in the 1Mb region around the eGene Transcriptional Start Site (TSS), derived from our dataset. Similarly, a p-value was extracted from GWAS summary statistics for each association between neighbouring variants of the top SNP and IBD phenotype. The resulting DAP on right Y-axis, represents the distribution of association −log(p) values for all variants in the ~200 kb region around rs6738825, an IBD risk locus from public dataset (ref 27). In this example, the DAP was not significantly correlated with the EAP linked to the Ctrl (θ = -0.04, p= NS) but was significantly correlated with the EAP linked to the TLR4 condition (θ = 0.75, p=0.005). B Zoom plot of a locus on Chromosome 2 illustrating the correlation between DAP for RA (blue) and EAP for PLCL1 gene (grey). A p-value was calculated for each association between each neighbouring variants of SNPs and the expression of the PLCL1 gene within a specific window around this gene. The EAP on the left Y-axis, represents the distribution of association −log(p) values for all variants in the 1Mb region around the eGene Transcriptional Start Site (TSS), derived from our dataset. Similarly, a p-value was extracted from GWAS summary statistics for each association between neighbouring variants of the top SNP and RA phenotype. The resulting DAP on the right Y-axis, represents the distribution of association −log(p) values for all variants in in the ~200 kb region around rs10497813, a RA risk locus from a public dataset (ref. 25). In this example, the DAP was not significantly correlated with the EAP linked to the Ctrl condition (θ = -0.04, p= NS) but was significantly correlated with the EAP linked to the TLR4 condition (θ = -0.73, p= 0.004). The correlation plots show the correlation of each SNP in EAP and DAP. The add-on plots of correlation show that the correlation is positive for matching DAP-EAP in case of IBD but negative for matching DAP-EAP in case of RA. Images used in the figure have been generated with a Biorender Academic License.

For each neighbouring variant of the SNP, a p-value was computed indicating the association with the expression of the RAB2A gene within a specific genomic window. The EAP, represented on left Y-axis, was defined as the distribution of association −log(p) values for all variants within 1Mb vicinity around the eGene Transcriptional Start Site (TSS), derived from our dataset. Similarly, a p-value was extracted from GWAS summary statistics for each association between neighbouring variants of the top SNP and COVID-19 phenotype. The resulting DAP shown on right Y-axis, represents the distribution of association −log(p) values across all variants within a manually defined region ~200 kb around rs10850094, a COVID-19 risk locus obtained from public dataset (Ref. 26). In this particular example, the DAP exhibited no significant correlation with the EAP associated with Ctrl (θ = 0.34, p= NS), whereas it displayed significant correlations with EAPs linked to TLR7/8 (θ = 0.91, p <0.0001), TCR (θ = 0.85, p=0.0002) and TLR4 conditions (θ = 0.72, p=0.004)). This example underscores that the eQTLs associated with OAS1 gene are r esponsive eQTLs. The add-on correlation plots demonstrate positive correlations between matching DAP-EAPs pairs. Images used in the figure have been generated with a Biorender Academic License.

2023;621(7977):E7-E26).

Submitted filename: Review - Point by point answers_final.pdf


## Data Availability Statement

Data can be found at https://ega-archive.org/datasets/EGAD50000001320 Additionally, we provide an interactive web browser to facilitate user-friendly exploration of our dataset at https://tools.giga.uliege.be/cedar/publiclw .

Articles from PLOS Genetics are provided here courtesy of PLOS
