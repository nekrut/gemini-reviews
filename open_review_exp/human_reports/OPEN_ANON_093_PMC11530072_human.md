# Decision Letter 0


### Jason A Papin


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.


## Transfer Alert

This paper was transferred from another journal. As a result, its full editorial history (including decision letters, peer reviews and author responses) may not be present.

Thank you very much for submitting your manuscript "Simulation of 69 microbial communities indicates sequencing depth and false positives are major drivers of bias in Prokaryotic metagenome-assembled genome recovery" for consideration at PLOS Computational Biology.

As with all papers reviewed by the journal, your manuscript was reviewed by members of the editorial board and by several independent reviewers. In light of the reviews (below this email), we would like to invite the resubmission of a significantly-revised version that takes into account the reviewers' comments.

Please note that while there is enthusiasm from all three reviewers about the focus of this work, there are substantial critiques on methodology and presentation. So, while this is a "major revision" decision, please make note of the expectation for extensive revision for the manuscript to be considered further. Please also note the repeated request for the code to be available per the journal policy.

We cannot make any decision about publication until we have seen the revised manuscript and your response to the reviewers' comments. Your revised manuscript is also likely to be sent to reviewers for further evaluation.

When you are ready to resubmit, please upload the following:

[1] A letter containing a detailed list of your responses to the review comments and a description of the changes you have made in the manuscript. Please note while forming your response, if your article is accepted, you may have the opportunity to make the peer review history publicly available. The record will include editor decision letters (with reviews) and your responses to reviewer comments. If eligible, we will contact you to opt in or out.

[2] Two versions of the revised manuscript: one with either highlights or tracked changes denoting where the text has been changed; the other a clean version (uploaded as the manuscript file).

Important additional instructions are given below your reviewer comments.

Please prepare and submit your revised manuscript within 60 days. If you anticipate any delay, please let us know the expected resubmission date by replying to this email. Please note that revised manuscripts received after the 60-day due date may require evaluation and peer review similar to newly submitted manuscripts.

Thank you again for your submission. We hope that our editorial process has been constructive so far, and we welcome your feedback at any time. Please don't hesitate to contact us if you have any questions or comments.

PLOS Computational Biology

***********************

Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #1: See attached document.

Reviewer #2: The generation of Metagenome-Assembled Genomes (MAGs) from individual microbes within complex samples is a critical step for identifying the community members present and their functional capacity within a metagenomics sample. Previous work has shown that intrinsic parameters of the sample or the sequencing can bias MAG generation, which would significantly alter the interpretation of a metagenomics experiment’s results. The manuscript by da Rocha et al aims to investigate bias in tools used for MAG generation. The authors generated in silico microbial communities, allowing them to test three MAG generation pipelines for the effect of sample evenness, sequencing depth, and taxonomic relatedness on MAG recovery. This work is of significant interest to individuals working with metagenomics data, as it tests the influence of these factors on bias in MAG recovery as well as tests the accuracy of several MAG generation pipelines on simulated data.

Overall, the authors found that the DAS Tool (DT) pipeline had the highest accuracy of MAG generation pipelines tested. The authors also found other associations between the number of MAGs recovered and other parameters, although there were few consistent trends. Of note, the statistical approach used is not suited for the number of comparisons made in this analysis, making it difficult to interpret these results. In addition, the language of the manuscript could be revised to ease interpretation of the results. Comments are listed below.

1. Throughout the paper, the authors use a Student’s t test to test for significant differences between groups. However, a Student’s t test is only valid for comparisons between two groups, and most of these comparisons involve three or more comparisons. Therefore, the statistics should be revised for this study to use an alternative test, such as a One-way ANOVA, instead.

2. While the authors draw many conclusions on the associations between sample evenness, sequencing depth, and taxonomic similarity, most of this data is presented in supplementary figures, with only one figure (Fig. 3) showing significant differences across these parameters. I think some of this data should be presented within the body of the manuscript as main figures to ease interpretation of the work.

3. The text should be revised to more clearly explain the main takeaways of the paper. For example, more detailed explanation of the evenness models investigated should be included within the results section.

1. On line 35, the final sentence of the abstract is incomplete and should be revised.

2. The MAGs generated for this manuscript have been shared publicly on NCBI Bioproject, but no code for this analysis was listed. Are the tools used for this analysis all stand-alone applications, and thus no custom code was required?

Reviewer #3: In this work, de Rocha et al. test three different pipelines for extracting metagenome-assembled genomes (MAGs) from three metagenomic datasets while systematically varying the input parameters for the pipelines. Their aim was to evaluate how sample evenness, sequencing depth, and taxonomic distribution profiles influence the recovery of genomes. To accomplish this, they generated mock microbial communities by dividing 126 bacteria, archaea, and fungi into three groups of 42 each. They then tested three pipelines, 8K, DT, and MM, with sequencing depth, taxonomical distribution, and evenness distribution varied with five different parameters each. The results indicated that the 8Kpipeline recovered the highest number of MAGs but only 25% of the 42 species on average, while the DT pipeline recovered 45% of species on average. The 8K pipeline also recovered the lowest number of true positives and had the highest number of false negatives. Moreover, MAG recovery was was influenced by taxonomic relatedness and sequencing depth but not evenness distribution. Overall, their results suggested that the DT pipeline has the highest accuracy and sequencing depth influences results. The three pipelines also had generally low accuracy in recovering closely related species.

This is a timely study that demonstrates the importance of the choice of reconstruction pipeline and parameter selection. As MAG reconstruction is commonly used by the research community, this is valuable knowledge.

- While the MAGs have been made available, the code used to generate and evaluate the MAGs does not appear to be available. This is also important for the audience to reproduce how the quality and accuracy of the MAGs was determined.

- Line 36: incomplete sentence “Our data indicates the scientific community should their findings from MAG recovery”

- There are a few typos (e.g., “Informtaion” in line 50).

- Line 104: other than in the abstract, this is the first time, the abbreviations for the three pipelines are used before being defined, which is a bit confusing.

- It would be helpful to have the overview on the workflow near the beginning of the manuscript rather than as Figure 6.

- There is a high number of supplementary tables most of which are small. I would suggest condensing them.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

Reviewer #1: No: Data to produce the plots are provided, as well as the sequencing data. However, there is not a code availability statement and no link to the code for bioinformatic workflow, statistical analysis and plot generation.

Reviewer #3: No: While the MAGs have been shared, the code for performing the simulations does not seem to be available.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email us at figures@plos.org .

Please note that, as a condition of publication, PLOS' data policy requires that you make available all data used to draw the conclusions outlined in your manuscript. Data must be deposited in an appropriate repository, included within the body of the manuscript, or uploaded as supporting information. This includes all numerical values that were used to generate graphs, histograms etc.. For an example in PLOS Biology see here: http://www.plosbiology.org/article/info%3Adoi%2F10.1371%2Fjournal.pbio.1001908#s5 .

To enhance the reproducibility of your results, we recommend that you deposit your laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols

Submitted filename: PlosReview.pdf


# Author response to Decision Letter 0

Collection date 2024 Oct.

Submitted filename: 01_PointbyPointReplytoReviewers_v6.pdf


# Decision Letter 1


### Jason A Papin


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Thank you very much for submitting your manuscript "Simulation of 69 microbial communities indicates sequencing depth and false positives are major drivers of bias in Prokaryotic metagenome-assembled genome recovery" for consideration at PLOS Computational Biology. As with all papers reviewed by the journal, your manuscript was reviewed by members of the editorial board and by several independent reviewers. The reviewers appreciated the attention to an important topic but raised important points that need to be further addressed.

Please prepare and submit your revised manuscript within 30 days. If you anticipate any delay, please let us know the expected resubmission date by replying to this email.

When you are ready to resubmit, please upload the following:

[1] A letter containing a detailed list of your responses to all review comments, and a description of the changes you have made in the manuscript. Please note while forming your response, if your article is accepted, you may have the opportunity to make the peer review history publicly available. The record will include editor decision letters (with reviews) and your responses to reviewer comments. If eligible, we will contact you to opt in or out

[2] Two versions of the revised manuscript: one with either highlights or tracked changes denoting where the text has been changed; the other a clean version (uploaded as the manuscript file).

Important additional instructions are given below your reviewer comments.

Thank you again for your submission to our journal. We hope that our editorial process has been constructive so far, and we welcome your feedback at any time. Please don't hesitate to contact us if you have any questions or comments.

PLOS Computational Biology

***********************

A link appears below if there are any accompanying review attachments. If you believe any reviews to be missing, please contact ploscompbiol@plos.org immediately:

Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #2: This manuscript evaluates several Metagenome-Assembled Genome pipelines and the effects of sequence depth, species abundance, and species relatedness on model performance. In this revision, the authors put substantial effort into revising the organization of the manuscript, and I found that the goals of the manuscript and major findings were much clearer and easier to follow. The authors also added a new Figure 1, which highlights the major differences across pipelines. However, the statistical approach used in the manuscript is still a concern, as it underestimates the possibility of Type 1 errors in the results. Comments are listed below:

1. A Student’s t test is used for nearly all of the analyses in the manuscript, despite most of these analyses comparing differences between 3 or more groups (the paper compared outcomes across 3 different MAG pipelines, 5 different sequence depths, and 4 different abundance models). While I understand that the pairwise comparisons between two groups is what you are interested in, using a t test across all comparisons will overestimate the significance of your results. This is because each comparison is associated with a Type 1 error, where you falsely reject the null hypothesis. The probability of a Type 1 error will increase with each comparison, and when you are performing 3 tests (i.e., 8K vs DT, 8K vs MM, DT vs MM) with the same data, using a p value threshold of p < 0.05 will underestimate this error rate. The reported p values are also not corrected for multiple comparisons, which occur when using a univariate test repeatedly across many comparisons. As is, the p values presented overestimate the number of statistical differences and must be adjusted to account for these issues.

A One-way ANOVA with a post hoc test (such as Tukey’s method) will adjust the p value to account for the increased Type 1 error rate, and pairwise comparisons can be performed to identify statistical differences between paired conditions. For example, in Supplemental Table 6, a One-way ANOVA should be used to calculate pairwise comparisons across all Taxonomic Distributions for each Species Abundance. I would recommend this approach to account for the increased Type 1 error rate.

1. The resolution of the figures (particularly Figure 1 and Figure 4) appears low. Please check figure resolution before submission of final figures.

Reviewer #3: The authors have done a good job revising the manuscript and addressing my and the other reviewers' comments. I have no further comments.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email us at figures@plos.org .

Please note that, as a condition of publication, PLOS' data policy requires that you make available all data used to draw the conclusions outlined in your manuscript. Data must be deposited in an appropriate repository, included within the body of the manuscript, or uploaded as supporting information. This includes all numerical values that were used to generate graphs, histograms etc.. For an example in PLOS Biology see here: http://www.plosbiology.org/article/info%3Adoi%2F10.1371%2Fjournal.pbio.1001908#s5 .

To enhance the reproducibility of your results, we recommend that you deposit your laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols

Review your reference list to ensure that it is complete and correct. If you have cited papers that have been retracted, please include the rationale for doing so in the manuscript text, or remove these references and replace them with relevant current references. Any changes to the reference list should be mentioned in the rebuttal letter that accompanies your revised manuscript.

If you need to cite a retracted article, indicate the article’s retracted status in the References list and also include a citation and full reference for the retraction notice.


# Author response to Decision Letter 1

Collection date 2024 Oct.

Submitted filename: 02_Second_PointbyPointReplytoReviewers_v8.pdf


# Decision Letter 2


### Jason A Papin


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

We are pleased to inform you that your manuscript 'Simulation of 69 microbial communities indicates sequencing depth and false positives are major drivers of bias in Prokaryotic metagenome-assembled genome recovery' has been provisionally accepted for publication in PLOS Computational Biology.

Before your manuscript can be formally accepted you will need to complete some formatting changes, which you will receive in a follow up email. A member of our team will be in touch with a set of requests.

Please note that your manuscript will not be scheduled for publication until you have made the required changes, so a swift response is appreciated.

IMPORTANT: The editorial review process is now complete. PLOS will only permit corrections to spelling, formatting or significant scientific errors from this point onwards. Requests for major changes, or any which affect the scientific understanding of your work, will cause delays to the publication date of your manuscript.

Should you, your institution's press office or the journal office choose to press release your paper, you will automatically be opted out of early publication. We ask that you notify us now if you or your institution is planning to press release the article. All press must be co-ordinated with PLOS.

Thank you again for supporting Open Access publishing; we are looking forward to publishing your work in PLOS Computational Biology.

PLOS Computational Biology

***********************************************************


# Acceptance letter


### Jason A Papin


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PCOMPBIOL-D-23-00832R2

Simulation of 69 microbial communities indicates sequencing depth and false positives are major drivers of bias in Prokaryotic metagenome-assembled genome recovery

I am pleased to inform you that your manuscript has been formally accepted for publication in PLOS Computational Biology. Your manuscript is now with our production department and you will be notified of the publication date in due course.

The corresponding author will soon be receiving a typeset proof for review, to ensure errors have not been introduced during production. Please review the PDF proof of your manuscript carefully, as this is the last chance to correct any errors. Please note that major changes, or those which affect the scientific understanding of the work, will likely cause delays to the publication date of your manuscript.

Soon after your final files are uploaded, unless you have opted out, the early version of your manuscript will be published online. The date of the early version will be your article's publication date. The final article will be published to the same URL, and all versions of the paper will be accessible to readers.

Thank you again for supporting PLOS Computational Biology and open-access publishing. We are looking forward to publishing your work!

PLOS Computational Biology | Carlyle House, Carlyle Road, Cambridge CB4 3DN | United Kingdom ploscompbiol@plos.org | Phone +44 (0) 1223-442824 | ploscompbiol.org | @PLOSCompBiol

This section collects any data citations, data availability statements, or supplementary materials included in this article.


## Supplementary Materials

Completeness and contamination percentages of all Metagenome-Assembled Genomes (MAGs) recovered by each binning pipeline (8K DT and MM) (A). The quality MAGs are also color-coded for their respective quality score (B) (Quality score = completeness—5 * contamination). The normalized counts of MAGs are shown according to completeness (C) and contamination (D).

Taxonomic distribution was set to Random. (*P-value < 0.05)

Sequencing depth of the communities was kept at 60 million reads. (*P-value < 0.05)

Species taxonomy was set to Random. (* P-value < 0.05)

Sequencing depth of the communities was kept at 60 million reads. (* P-value < 0.05)

Sequencing depth of the communities was kept at 60 million reads. (*P-value < 0.05)

Sequencing depth of the communities was kept at 60 million reads. (*P-value < 0.05)

Abundance distribution 1: Equal abundance (all species are equally abundant); Species abundance distribution 2: Logarithmic decay; Species abundance distribution 3: Exponential decay; Species abundance distribution 4: Logarithmic decay with plateaus (Some species have equal abundances); Species abundance distribution 5: Exponential decay with plateaus (Some species have equal abundances).

The sequencing depth of the communities was kept at 60 million reads. (*P-value < 0.05).

Features include species group (Community), Species abundance distribution, Taxonomic distribution, Sequencing depth, Pipeline and genomic metrics (number of contigs, N50, L50, average and standard deviation of GC content))

Sequencing depth was kept at 60 million reads. (Ratio FP = total number of FPs/total number of species recovered (*100); Accuracy = (TP/TP+FP)*100)

MAG ID contemplates the community (A, B, C), species abundance distribution (Equal abundance; Logarithmic decay; Exponential decay; Logarithmic decay with abundance plateaus; Exponential decay with abundance plateaus), Taxonomic relatedness (Ordered; Not related; Closely related; Very closely related; Random) and sequencing depth (10, 30, 60, 120 and 1280 million reads). 16S rRNa sequences were recovered using the ssu_finder function from CheckM. Classification of 16S rRNA sequences was determined using the online version of SILVA ( https://www.arb-silva.de/aligner/ ).

Features include Species abundance distribution (Equal abundance; Logarithmic decay; Exponential decay; Logarithmic decay with abundance plateaus; Exponential decay with abundance plateaus), Taxonomic distribution (Ordered; Not related; Closely related; Very closely related; Random), quality metrics (completeness, contamination and strain heterogeneity) and abundance metrics (coverage and relative abundance).

Sequencing depth of the communities was kept at 60 million reads.

Sequencing depth of the communities was kept at 60 million reads.

Sequencing depth of the communities was kept at 60 million reads.

Sequencing depth of the communities was kept at 60 million reads.

Sequencing depth of the communities was kept at 60 million reads.

Taxonomic relatedness was kept random.

Sequencing depth of the communities was kept at 60 million reads.

Sequencing depth of the communities was kept at 60 million reads.

Sequencing depth of the communities was kept at 60 million reads.

Additionally, standard deviation errors are also presented for each category.

Sequencing depth of the communities was kept at 60 million reads.

Sequencing depth of the communities was kept at 60 million reads.

Sequencing depth of the communities was kept at 60 million reads.

Sequencing depth of the communities was kept at 60 million reads.

Sequencing depth of the communities was kept at 60 million reads.

(* Special cases: linear chromosomes or multiple chromosomes; **: Eukaryotes; ü: recovered; x: not recovered,NA: not applicable (i.e., not in the original community)).

Sequencing depth was kept at 60 million end reads.

The "Reference" column is populated with the species to which the species in "Very Closely Related" and "Closely Related" are related at the Genus and Family level, respectively. Additional features include the Domain, Phylum and community set (A,B and C) in which those species were used.

Additional features include the coverage and relative abundance of the species in the original communities. Community species dataset: Original species list. Species abundance distribution (Logarithmic decay; Exponential decay; Logarithmic decay with abundance plateaus; Exponential decay with abundance plateaus). Sequencing depth was kept at 60 million reads.

Additional features include the coverage and relative abundance of the species in the original communities. Community species dataset: Original species list. Species abundance distribution (Logarithmic decay; Exponential decay; Logarithmic decay with abundance plateaus; Exponential decay with abundance plateaus). Sequencing depth was kept at 60 million reads.

Additional features include the coverage and relative abundance of the species in the original communities. Community species dataset: Original species list. Species abundance distribution (Logarithmic decay; Exponential decay; Logarithmic decay with abundance plateaus; Exponential decay with abundance plateaus). Sequencing depth was kept at 60 million reads.

Sequencing depth of the communities was kept at 60 million reads.

Further, the community set in which the species were placed is also shown.

Very closely related: Communities composed of species belonging to the same genus as the reference; Closely related: Communities composed of species belonging to the same family (but not genus) as the reference; Not closely related: Communities not satisfying none of the genus and family conditions in Very closely related and Closely related; Randomly assigned: Communities assembled with randomly organized species; Ordered: no criteria for distribution but the community order itself (only used on equal evenness communities). Letters represent the triplets used (.e.g, A1 (reference genome), A2 (species with the same genus as A1), and A3 (species with the same family but not genus of A1)).

Submitted filename: PlosReview.pdf

Submitted filename: 01_PointbyPointReplytoReviewers_v6.pdf

Submitted filename: 02_Second_PointbyPointReplytoReviewers_v8.pdf


## Data Availability Statement

The true positive metagenome-assembled genomes (MAGs) (4638 out of 5217) obtained in this study are available at the National Center for Biotechnology Information (NCBI) repository with the sample accession numbers SAMN34004744 - SAMN34012094 (BioProject PRJNA950613). The complete set of MAGs (including the false positives) and simulated metagenomic libraries are available on the long-term data archive at the Helmholtz Center for Environmental Research – UFZ data center using the link ( https://www.ufz.de/record/dmp/archive/13476 ). All the code used during data analysis is available at https://github.com/mdsufz/mockc_analysis

Articles from PLOS Computational Biology are provided here courtesy of PLOS
