# Decision Letter 0


### Vinod Yata


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Thank you for submitting your manuscript to PLOS ONE. After careful consideration, we feel that it has merit but does not fully meet PLOS ONE’s publication criteria as it currently stands. Therefore, we invite you to submit a revised version of the manuscript that addresses the points raised during the review process.

Please submit your revised manuscript by Apr 26 2025 11:59PM. If you will need more time than this to complete your revisions, please reply to this message or contact the journal office at plosone@plos.org . When you're ready to submit your revision, log on to https://www.editorialmanager.com/pone/ and select the 'Submissions Needing Revision' folder to locate your manuscript file.

A rebuttal letter that responds to each point raised by the academic editor and reviewer(s). You should upload this letter as a separate file labeled 'Response to Reviewers'.

A marked-up copy of your manuscript that highlights changes made to the original version. You should upload this as a separate file labeled 'Revised Manuscript with Track Changes'.

An unmarked version of your revised paper without tracked changes. You should upload this as a separate file labeled 'Manuscript'.

If you would like to make changes to your financial disclosure, please include your updated statement in your cover letter. Guidelines for resubmitting your figure files are available below the reviewer comments at the end of this letter.

If applicable, we recommend that you deposit your laboratory protocols in protocols.io to enhance the reproducibility of your results. Protocols.io assigns your protocol its own identifier (DOI) so that it can be cited independently in the future. For instructions see: https://journals.plos.org/plosone/s/submission-guidelines#loc-laboratory-protocols . Additionally, PLOS ONE offers an option for publishing peer-reviewed Lab Protocol articles, which describe protocols hosted on protocols.io. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols .

We look forward to receiving your revised manuscript.

Vinod Kumar Yata, PhD

Journal requirements:

When submitting your revision, we need you to address these additional requirements.

1. Please ensure that your manuscript meets PLOS ONE's style requirements, including those for file naming. The PLOS ONE style templates can be found at

https://journals.plos.org/plosone/s/file?id=wjVg/PLOSOne_formatting_sample_main_body.pdf and

https://journals.plos.org/plosone/s/file?id=ba62/PLOSOne_formatting_sample_title_authors_affiliations.pdf

2. We note that your Data Availability Statement is currently as follows: [All relevant data are within the manuscript and its Supporting Information files.]

Please confirm at this time whether or not your submission contains all raw data required to replicate the results of your study. Authors must share the “minimal data set” for their submission. PLOS defines the minimal data set to consist of the data required to replicate all study findings reported in the article, as well as related metadata and methods ( https://journals.plos.org/plosone/s/data-availability#loc-minimal-data-set-definition ).

For example, authors should submit the following data:

- The values behind the means, standard deviations and other measures reported;

- The values used to build graphs;

- The points extracted from images for analysis.

Authors do not need to submit their entire data set if only a portion of the data was used in the reported study.

If your submission does not contain these data, please either upload them as Supporting Information files or deposit them to a stable, public repository and provide us with the relevant URLs, DOIs, or accession numbers. For a list of recommended repositories, please see https://journals.plos.org/plosone/s/recommended-repositories .

If there are ethical or legal restrictions on sharing a de-identified data set, please explain them in detail (e.g., data contain potentially sensitive information, data are owned by a third-party organization, etc.) and who has imposed them (e.g., an ethics committee). Please also provide contact information for a data access committee, ethics committee, or other institutional body to which data requests may be sent. If data are owned by a third party, please indicate how others may request data access.

3. Please include a separate caption for each figure in your manuscript.

4. We notice that your supplementary figures are included in the manuscript file. Please remove them and upload them with the file type 'Supporting Information'. Please ensure that each Supporting Information file has a legend listed in the manuscript after the references list.

Additional Editor Comments (if provided):

[Note: HTML markup is below. Please do not edit.]

Reviewer's Responses to Questions

Comments to the Author

1. Is the manuscript technically sound, and do the data support the conclusions?

2. Has the statistical analysis been performed appropriately and rigorously? -->?>

3. Have the authors made all data underlying the findings in their manuscript fully available??>

4. Is the manuscript presented in an intelligible fashion and written in standard English??>

Reviewer #1: Matsumoto et al. describe a brief evaluation of the relationship between microbiome composition and urothelial carcinoma in a unique dataset containing data on both the gut and oral microbiota of patients undergoing treatment. While there are minor suggestions that could be made (the abstract does not adequately justify why the oral microbiome would be relevant to the urinary tract, for example, though it is covered in the introduction), I believe there are several major issues that are much more important to address.

Line 36: The abstract mentions using QIIME to generate operational taxonomic units, but OTUs are not mentioned anywhere in the manuscript. It appears all other analyses use web portal-based tools from Illumina; this discrepancy should be clarified.

Line 158: The methods used for assessing compositional differences between groups are insufficiently described and supported here. My primary objection is in using the Student's t-test to evaluate differences in relative abundance—it's unclear whether relative abundance was tested using read counts, percentages, or some kind of transformed count, but figure 2 suggests the test was done on percentages. I am very skeptical that this is an appropriate method to use, as percentages within a sample are not independent: if one taxon grows significantly, the relative abundance of at least one other taxon, and likely many others, will fall. There are dozens of relevant papers debating the appropriate methods for differential abundance testing (e.g. https://doi.org/10.3389/fmicb.2017.02224); if the authors prefer to use the Student's t-test on relative abundances, I strongly believe it necessary that they provide references for why this is appropriate.

160: This test is described in multiple places as the "non-parametric Student's t test"; the only Student's t-test I am aware of is certainly parametric.

163: The manuscript states a significance threshold of 0.05, but does not specify how many tests were performed nor whether multiple test correction was applied. This is critical information: Figure 2 describes four tests covering two taxa, but presumably there were far more tests performed. If all families were tested for between-group differences, I would guess that even a generous approach to multiple test correction would alter most of the described p-values to be far above the set significance threshold. It is impossible for me to estimate any more accurately because this information was not available, but I strongly believe these results are invalid without a consideration of multiple testing and a description of how it was performed. This should be added.

I leave it to the editor to evaluate the authors' adherence to PLOS editorial policies, but I should note that the manuscript does not describe any deposition of sequencing data, and if any other data was submitted as supplementary files, I was unable to see them. As presented, the analysis described is impossible to replicate. I also am surprised to find that dozens of subjects were recruited, then samples were collected, prepped, sequenced and analyzed, without any disclosed funding.

I hesitate to submit a review that sounds this negative: The authors have collected an interesting dataset and describe compelling reasons for evaluating the microbiome in the context of this disease. However, it is vital that the methodology be updated to be more in line with accepted standards, or at least methods supported by literature, to avoid misleading patients and healthcare practitioners who may look to papers like this for clues to treatment.

Reviewer #2: Line 81-83: Please define your specific aim more precisely.

Lines 86-88: The introduction's mention of Veillonellaceae and Prevotellaceae may suggest predetermined conclusions rather than objective investigation. Please reconsider this framing.

Lines 112 & 114: Please correct the sentence structure to eliminate repetition.

Line 350: There is an inconsistency with Line 170. Figure 1 should present alpha diversity (Simpson and Shannon indices). Please correct this discrepancy.

The methodology section lacks information on raw data processing. Please specify:

1) The number of reads per sample after processing

2) Whether samples were sequenced with adequate depth

3) Analysis of overall community differences (beta diversity)

4) Visualization of beta diversity through PCoA plots

what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy

[NOTE: If reviewer comments were submitted as an attachment file, they will be attached to this email and accessible via the submission site. Please log into your account, locate the manuscript record, and check for the action link "View Attachments". If this link does not appear, there are no attachment files.]

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com/ . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Registration is free. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email PLOS at figures@plos.org . Please note that Supporting Information files do not need this step.


# Author response to Decision Letter 1

Collection date 2025.

**Point-by-point responses to the Reviewers’ comments**

Line 36: The abstract mentions using QIIME to generate operational taxonomic units, but OTUs are not mentioned anywhere in the manuscript. It appears all other analyses use web portal-based tools from Illumina; this discrepancy should be clarified.

Thank you for your comment. We did not use QIIME but Illumina’s web portal-based tool. We have corrected the sentence accordingly (lines 38–39 of the revised manuscript).

Line 158: The methods used for assessing compositional differences between groups are insufficiently described and supported here. My primary objection is in using the Student's t-test to evaluate differences in relative abundance—it's unclear whether relative abundance was tested using read counts, percentages, or some kind of transformed count, but figure 2 suggests the test was done on percentages. I am very skeptical that this is an appropriate method to use, as percentages within a sample are not independent: if one taxon grows significantly, the relative abundance of at least one other taxon, and likely many others, will fall. There are dozens of relevant papers debating the appropriate methods for differential abundance testing (e.g. https://doi.org/10.3389/fmicb.2017.02224); if the authors prefer to use the Student's t-test on relative abundances, I strongly believe it necessary that they provide references for why this is appropriate.

Thank you for your comments on the certification. We used the centred log-ratio (CLR) transformation to normalise the count data of saliva and stool from healthy individuals and UC family members. We have clarified this method in lines 177–181 of the revised manuscript.

160: This test is described in multiple places as the "non-parametric Student's t test"; the only Student's t-test I am aware of is certainly parametric.

Thank you for your comment. We have corrected the name of the test as “Mann-Whitney U test” (line 185 of the revised manuscript).

163: The manuscript states a significance threshold of 0.05, but does not specify how many tests were performed nor whether multiple test correction was applied. This is critical information: Figure 2 describes four tests covering two taxa, but presumably there were far more tests performed. If all families were tested for between-group differences, I would guess that even a generous approach to multiple test correction would alter most of the described p-values to be far above the set significance threshold. It is impossible for me to estimate any more accurately because this information was not available, but I strongly believe these results are invalid without a consideration of multiple testing and a description of how it was performed. This should be added.

Thank you for your comments on the certification. We have clarified that we performed multiple test correction using the Benjamini-Hochberg method in lines 181–184 of the revised manuscript.

I leave it to the editor to evaluate the authors' adherence to PLOS editorial policies, but I should note that the manuscript does not describe any deposition of sequencing data, and if any other data was submitted as supplementary files, I was unable to see them. As presented, the analysis described is impossible to replicate. I also am surprised to find that dozens of subjects were recruited, then samples were collected, prepped, sequenced and analyzed, without any disclosed funding.

Thank you for your comments on the certification. As suggested, we have described the deposition of sequencing in lines 187–188 of the revised manuscript. We have added our funding sources.

Lines 81-83: Please define your specific aim more precisely.

Thank you for your comment. We have defined our specific aim more precisely in lines 85–89 of the revised manuscript.

Lines 86-88: The introduction's mention of Veillonellaceae and Prevotellaceae may suggest predetermined conclusions rather than objective investigation. Please reconsider this framing.

Thank you for pointing out the concern about the mention of the Veillonellaceae and Prevotellidae families. We have deleted this text as it lacks objectivity.

Lines 112 & 114: Please correct the sentence structure to eliminate repetition.

As pointed out, we corrected the structure of the sentence and eliminated the duplication.

Line 350: There is an inconsistency with Line 170. Figure 1 should present alpha diversity (Simpson and Shannon indices). Please correct this discrepancy.

Thank you for pointing out the discrepancy. We have corrected the figure number as Figure S1 (line 222 of the revised manuscript).

The methodology section lacks information on raw data processing. Please specify:

1) The number of reads per sample after processing

2) Whether samples were sequenced with adequate depth

3) Analysis of overall community differences (beta diversity)

4) Visualization of beta diversity through PCoA plots.

1) and 2) We have uploaded Excel files (saliva_reads_family.xlsx and stool_reads_family.xlsx) that specified the number of reads per sample and family after processing. These files show that samples were sequenced with adequate depth.

3) and 4) We have analysed the overall community differences and visualized the beta diversity through PCoA plots in Figure S2.

Submitted filename: Cover letter rebuttal-20250411-clear.docx


# Decision Letter 1


### Vinod Yata


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Exploration of predictive factors based on oral and intestinal bacterial flora for treating patients with urothelial carcinoma

We’re pleased to inform you that your manuscript has been judged scientifically suitable for publication and will be formally accepted for publication once it meets all outstanding technical requirements.

Within one week, you’ll receive an e-mail detailing the required amendments. When these have been addressed, you’ll receive a formal acceptance letter and your manuscript will be scheduled for publication.

An invoice will be generated when your article is formally accepted. Please note, if your institution has a publishing partnership with PLOS and your article meets the relevant criteria, all or part of your publication costs will be covered. Please make sure your user information is up-to-date by logging into Editorial Manager at Editorial Manager® and clicking the ‘Update My Information' link at the top of the page. If you have any questions relating to publication charges, please contact our Author Billing department directly at authorbilling@plos.org.

If your institution or institutions have a press office, please notify them about your upcoming paper to help maximize its impact. If they’ll be preparing press materials, please inform our press team as soon as possible -- no later than 48 hours after receiving the formal acceptance. Your manuscript will remain under strict press embargo until 2 pm Eastern Time on the date of publication. For more information, please contact onepress@plos.org.

Vinod Kumar Yata, PhD

Additional Editor Comments (optional):

The authors have carefully and comprehensively addressed the reviewers' concerns raised in the initial round of peer review. Specifically:

The statistical methodology has been significantly improved with clarification of the use of centered log-ratio transformation and appropriate non-parametric tests.

The manuscript now includes detailed information on multiple testing corrections using the Benjamini-Hochberg method.

Corrections have been made to statistical terminology (e.g., replacing the inaccurate use of “non-parametric Student’s t-test” with the appropriate “Mann-Whitney U test”).

Details regarding sequencing data availability have been provided, and deposition to GEO ( GSE293354 ) enhances the transparency and reproducibility of the study.

Additional clarifications and improvements to the introduction, aim, methodology, and discussion sections have strengthened the scientific rigor and readability of the manuscript.

The study presents novel and meaningful insights into the association between microbiota and treatment outcomes in urothelial carcinoma, and it aligns well with the scope and readership of PLOS ONE.

On this basis, I am pleased to recommend acceptance of the manuscript in its current form.


# Acceptance letter


### Vinod Yata


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

I'm pleased to inform you that your manuscript has been deemed suitable for publication in PLOS ONE. Congratulations! Your manuscript is now being handed over to our production team.

At this stage, our production department will prepare your paper for publication. This includes ensuring the following:

* All references, tables, and figures are properly cited

* All relevant supporting information is included in the manuscript submission,

* There are no issues that prevent the paper from being properly typeset

You will receive further instructions from the production team, including instructions on how to review your proof when it is ready. Please keep in mind that we are working through a large volume of accepted articles, so please give us a few days to review your paper and let you know the next and final steps.

Lastly, if your institution or institutions have a press office, please let them know about your upcoming paper now to help maximize its impact. If they'll be preparing press materials, please inform our press team within the next 48 hours. Your manuscript will remain under strict press embargo until 2 pm Eastern Time on the date of publication. For more information, please contact onepress@plos.org.

If we can help with anything else, please email us at customercare@plos.org.

Thank you for submitting your work to PLOS ONE and supporting open access.

PLOS ONE Editorial Office Staff

This section collects any data citations, data availability statements, or supplementary materials included in this article.


## Supplementary Materials

Detailed analysis of microbial composition across additional sample types or conditions. Specific comparisons and statistical comments are provided.

Illumina BaceSpace 16S For the count data of the families analysed by metagenomics, we used the vegan R package to calculate the Bray-Cruits distance and then performed intergroup comparisons and PCoA. For intergroup comparisons, we analysed the whole group using PERMANOVA. We also calculated and plotted the distances between Healthy, UC and Healthy-UC. We used the Wilcoxon test to test for significance in each group.

Submitted filename: Cover letter rebuttal-20250411-clear.docx


## Data Availability Statement

The datasets generated and analyzed during the current study are available in the repository, persistent https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293354 . All original code is available at NCBI GEO under accession number GSE293354.

Articles from PLOS One are provided here courtesy of PLOS
