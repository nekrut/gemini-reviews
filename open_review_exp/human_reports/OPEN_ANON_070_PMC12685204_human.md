# Decision Letter 0


### Roger Dimitri Kouyos


### Katharina Kusejko


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

T-shaped alignments integrating HIV-1 near full-length genome and partial pol sequences can improve phylodynamic inference of transmission clusters

PLOS Computational Biology

Thank you for submitting your manuscript to PLOS Computational Biology. After careful consideration, we feel that it has merit but does not fully meet PLOS Computational Biology's publication criteria as it currently stands. Therefore, we invite you to submit a revised version of the manuscript that addresses the points raised during the review process.

​Please submit your revised manuscript within 60 days. If you will need more time than this to complete your revisions, please reply to this message or contact the journal office at ploscompbiol@plos.org . When you're ready to submit your revision, log on to https://www.editorialmanager.com/pcompbiol/ and select the 'Submissions Needing Revision' folder to locate your manuscript file.

Please include the following items when submitting your revised manuscript:

* A rebuttal letter that responds to each point raised by the editor and reviewer(s). You should upload this letter as a separate file labeled 'Response to Reviewers'. This file does not need to include responses to formatting updates and technical items listed in the 'Journal Requirements' section below.

* A marked-up copy of your manuscript that highlights changes made to the original version. You should upload this as a separate file labeled 'Revised Manuscript with Track Changes'.

* An unmarked version of your revised paper without tracked changes. You should upload this as a separate file labeled 'Manuscript'.

If you would like to make changes to your financial disclosure, competing interests statement, or data availability statement, please make these updates within the submission form at the time of resubmission. Guidelines for resubmitting your figure files are available below the reviewer comments at the end of this letter

We look forward to receiving your revised manuscript.

PLOS Computational Biology

PLOS Computational Biology

Additional Editor Comments (if provided):

The two reviewers have raised several important points that should be addressed. In addition, I have the following comments:

1) In the "Author Summary", the authors write that a novel approach for analyzing the spread of HIV-1 is explored. This is somewhat misleading, as this manuscript does not look into HIV-1 transmission, but clustering results in a convenience samples. No conclusions about any HIV transmission dynamics can be drawn here. Similar, the lines 226-229 in the Discussion concerning public health go in my opinion far beyond what was done here, a recommendation concerning cluster certainty should be avoided.

2) For this manuscript, as this describes mainly the workflow for exploring the impact of different fractions of full-length genomes, having the "Methods" section before the "Results" section would improve the reading flow.

3) Methods: To me it is not clear - also Reviewer 1 pointed this out - what was shuffled 1000 times randomly. This is a crucial point: Did you shuffle the order of sequences every time, and thus different sequences were "cropped" to consist of pol only? I am worried that if this was not shuffled properly, and thus always the same sequences were cropped, this might lead to artificial clustering due to sequences in the Los Alamos Database being more similar. Please clarify this aspect in the discussion. You might also think about a "methods" Figure clearly explaining the algorithm and different measures you applied to assess the impact of the fraction of full-genomes.

4) Selection of all available Los Alamos sequences: As these sequences stem from different studies and techniques (as Reviewer 2 pointed out), it would be interesting to see a sensitivity analysis looking into a subset of the sequences stemming from one study only (i.e., you could take the largest sub-study with available wgs). In my opinion, with this quite biased selection of available sequences, it is not clear which phylogenetic patterns would be expected at all - the current selection of sequences do not belong to one sub-epidemic in a country/region/time-frame/sub-population/etc. Thus the results are also hard to interpret.

5) Cluster Definition: You defined clusters as matching only if all members were the same. This is a very strict definition, and in my opinion might be too strict. E.g., if you have a cluster with 10 members, even if this cluster is still there with only one member difference, this would lead to a "non-match". I suggest to at least run a sensitivity analysis applying other cluster definition, e.g. more than 50%, or more than 2/3 of the members being the same. The result presented in Figure 4 might be a consequence of this strict definition: It is concerning that already when comparing all wgs to wgs90, the AMI is only between 0.3 to 0.5. If the AMI is anyway quite low, does the difference between the lower wgs values (wgs90, wgs80, wgs70,...) matter so much? It seems that even 10% missing wgs is leading to a much worse result. To understand this better: could you include results of wgs99, wgs95 or other intermediate values as well to understand this "jump" at the beginning? This also questions the whole "take-home message" that at least 50% wgs is beneficial: the actual changes in AMI are minimal.

6) Discussion: please do not use the term "phylodynamic" here, as no dynamic aspect (e.g. cluster growth) was investigated

Journal Requirements:

1) We ask that a manuscript source file is provided at Revision. Please upload your manuscript file as a .doc, .docx, .rtf or .tex. If you are providing a .tex file, please upload it under the item type u2018LaTeX Source Fileu2019 and leave your .pdf version as the item type u2018Manuscriptu2019.

2) We noticed that you used the phrase 'data not shown' in the manuscript. We do not allow these references, as the PLOS data access policy requires that all data be either published with the manuscript or made available in a publicly accessible database. Please amend the supplementary material to include the referenced data or remove the references.

3) Please ensure that the funders and grant numbers match between the Financial Disclosure field and the Funding Information tab in your submission form. Note that the funders must be provided in the same order in both places as well.

- State the initials, alongside each funding source, of each author to receive each grant. For example: "This work was supported by the National Institutes of Health (####### to AM; ###### to CJ) and the National Science Foundation (###### to AM)."

- State what role the funders took in the study. If the funders had no role in your study, please state: "The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.".

If you did not receive any funding for this study, please simply state: u201cThe authors received no specific funding for this work.u201d

Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #1: The study by Guang et al assessed the impact of having sequences with varying length on clustering analysis, or more specific how much improvement including full-length sequences can have on the overall clustering outputs. This is an important aspect of clustering, particularly when it is used for public health use in HIV, where information on clusters may be used to inform policies. Thus, accuracy is important. Overall, it is a neat study looking at a common problem in sequence analysis. The study design seems sound, though I am not familiar with the Robinson-Foulds distance and the adjusted mutual index. Thus, I cannot comment on the results for these.

Though, this is a computational journal I struggled to fully understand the study and believe the manuscript could benefit from more detail and clarifications. Also, how does the IQTree algorithm deal with missing data, for example does it ignore positions with incomplete coverage? I may have missed it but some explanations on that would be helpful. Apologies if I missed this, but did including wgs improve bootstrapping support overall?

Lines 74 to 79 could be re-written to clarify the outcomes. I didn’t understand fully what the distance along y-axis represents and what the distance. I understand how the points move along the axis from wgs20 to wgs90 but not why pol and wgs10 are ‘off’ the line, as in wgs10 is worse than pol?

Lines 253 to 260 not very clear

Line 144. Replace ‘developed’ with ‘assessed’ or similar as per my understanding the study did not ‘develop’ the approach, rather compared outputs.

Line 244. While sampling dates are important, I don’t think we can stay bootstrap and genetic distances are ‘arbitrary’. I would rephrase this.

Line 245. Unclear what exactly was repeated 1000 times? The clustering? The generation of mixed length datasets?

Figure 1. It seems the more ‘wgs’ sequences are present the more variation is in the distance comparison (larger confidence intervals), why is that?

Figure 3 is a bit chaos. Can you separate by bootstrap? Make each panel small, I think that should be sufficient.

Reviewer #2: See attachment.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

[NOTE: If reviewer comments were submitted as an attachment file, they will be attached to this email and accessible via the submission site. Please log into your account, locate the manuscript record, and check for the action link "View Attachments". If this link does not appear, there are no attachment files.]

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com/ . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Registration is free. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email PLOS at figures@plos.org . Please note that Supporting Information files do not need this step. If there are other versions of figure files still present in your submission file inventory at resubmission, please replace them with the PACE-processed versions.

To enhance the reproducibility of your results, we recommend that authors of applicable studies deposit laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols

Submitted filename: Reviewer_comments.docx


# Author response to Decision Letter 1

Collection date 2025 Nov.

Submitted filename: reviewer_response_v3.docx


# Decision Letter 1


### Roger Dimitri Kouyos


### Katharina Kusejko


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PCOMPBIOL-D-25-00292R1

T-shaped alignments integrating HIV-1 near full-length genome and partial pol sequences can improve phylogenetic inference of transmission clusters

PLOS Computational Biology

Thank you for submitting your manuscript to PLOS Computational Biology. After careful consideration, we feel that it has merit but does not fully meet PLOS Computational Biology's publication criteria as it currently stands. Therefore, we invite you to submit a revised version of the manuscript that addresses the points raised during the review process.

Please submit your revised manuscript within 30 days Dec 09 2025 11:59PM. If you will need more time than this to complete your revisions, please reply to this message or contact the journal office at ploscompbiol@plos.org . When you're ready to submit your revision, log on to https://www.editorialmanager.com/pcompbiol/ and select the 'Submissions Needing Revision' folder to locate your manuscript file.

Please include the following items when submitting your revised manuscript:

* A rebuttal letter that responds to each point raised by the editor and reviewer(s). You should upload this letter as a separate file labeled 'Response to Reviewers'. This file does not need to include responses to formatting updates and technical items listed in the 'Journal Requirements' section below.

* A marked-up copy of your manuscript that highlights changes made to the original version. You should upload this as a separate file labeled 'Revised Manuscript with Track Changes'.

* An unmarked version of your revised paper without tracked changes. You should upload this as a separate file labeled 'Manuscript'.

If you would like to make changes to your financial disclosure, competing interests statement, or data availability statement, please make these updates within the submission form at the time of resubmission. Guidelines for resubmitting your figure files are available below the reviewer comments at the end of this letter.

We look forward to receiving your revised manuscript.

PLOS Computational Biology

PLOS Computational Biology

Journal Requirements:

1) Thank you for stating "Publicly available data at https://www.hiv.lanl.gov/content/sequence/HIV/mainpage.html was used for the analysis." Please confirm whether all data needed to replicate the study's findings are at this link? If so, please update your Data Availability statement to "All data required to replicate the study's findings can be found here https://www.hiv.lanl.gov/content/sequence/HIV/mainpage.html

Note: If the reviewer comments include a recommendation to cite specific previously published works, please review and evaluate these publications to determine whether they are relevant and should be cited. There is no requirement to cite these works unless the editor has indicated otherwise.

Reviewer's Responses to Questions

Reviewer #2: This manuscript has improved significantly through all additional analyses and points discussed. Although the study is very thoroughly conducted and has gained improvements, the setup reflects a highly experimental scenario with many uncertainties. Thus, I would suggest to position the attitude towards public health implementations and recommendations for incorporating such nFL genomes even more neutral (e.g. L278-287).

Minor points to address:

- L 106/107: You have two unfinished sentences regarding the overlap coefficient.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

[NOTE: If reviewer comments were submitted as an attachment file, they will be attached to this email and accessible via the submission site. Please log into your account, locate the manuscript record, and check for the action link "View Attachments". If this link does not appear, there are no attachment files.]

While revising your submission, we strongly recommend that you use PLOS’s NAAS tool ( https://ngplosjournals.pagemajik.ai/artanalysis ) to test your figure files. NAAS can convert your figure files to the TIFF file type and meet basic requirements (such as print size, resolution), or provide you with a report on issues that do not meet our requirements and that NAAS cannot fix.

After uploading your figures to PLOS’s NAAS tool - https://ngplosjournals.pagemajik.ai/artanalysis , NAAS will process the files provided and display the results in the "Uploaded Files" section of the page as the processing is complete. If the uploaded figures meet our requirements (or NAAS is able to fix the files to meet our requirements), the figure will be marked as "fixed" above. If NAAS is unable to fix the files, a red "failed" label will appear above. When NAAS has confirmed that the figure files meet our requirements, please download the file via the download option, and include these NAAS processed figure files when submitting your revised manuscript.

To enhance the reproducibility of your results, we recommend that authors of applicable studies deposit laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols


# Author response to Decision Letter 2

Collection date 2025 Nov.

Submitted filename: response_to_reviewers.docx


# Decision Letter 2


### Roger Dimitri Kouyos


### Katharina Kusejko


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

We are pleased to inform you that your manuscript 'T-shaped alignments integrating HIV-1 near full-length genome and partial pol sequences can improve phylogenetic inference of transmission clusters' has been provisionally accepted for publication in PLOS Computational Biology.

Before your manuscript can be formally accepted you will need to complete some formatting changes, which you will receive in a follow up email. A member of our team will be in touch with a set of requests.

Please note that your manuscript will not be scheduled for publication until you have made the required changes, so a swift response is appreciated.

IMPORTANT: The editorial review process is now complete. PLOS will only permit corrections to spelling, formatting or significant scientific errors from this point onwards. Requests for major changes, or any which affect the scientific understanding of your work, will cause delays to the publication date of your manuscript.

Should you, your institution's press office or the journal office choose to press release your paper, you will automatically be opted out of early publication. We ask that you notify us now if you or your institution is planning to press release the article. All press must be co-ordinated with PLOS.

Thank you again for supporting Open Access publishing; we are looking forward to publishing your work in PLOS Computational Biology.

PLOS Computational Biology

PLOS Computational Biology

***********************************************************


# Acceptance letter


### Roger Dimitri Kouyos


### Katharina Kusejko


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PCOMPBIOL-D-25-00292R2

T-shaped alignments integrating HIV-1 near full-length genome and partial pol sequences can improve phylogenetic inference of transmission clusters

I am pleased to inform you that your manuscript has been formally accepted for publication in PLOS Computational Biology. Your manuscript is now with our production department and you will be notified of the publication date in due course.

The corresponding author will soon be receiving a typeset proof for review, to ensure errors have not been introduced during production. Please review the PDF proof of your manuscript carefully, as this is the last chance to correct any errors. Please note that major changes, or those which affect the scientific understanding of the work, will likely cause delays to the publication date of your manuscript.

Soon after your final files are uploaded, unless you have opted out, the early version of your manuscript will be published online. The date of the early version will be your article's publication date. The final article will be published to the same URL, and all versions of the paper will be accessible to readers.

For Research, Software, and Methods articles, you will receive an invoice from PLOS for your publication fee after your manuscript has reached the completed accept phase. If you receive an email requesting payment before acceptance or for any other service, this may be a phishing scheme. Learn how to identify phishing emails and protect your accounts at https://explore.plos.org/phishing .

Thank you again for supporting PLOS Computational Biology and open-access publishing. We are looking forward to publishing your work!

PLOS Computational Biology | Carlyle House, Carlyle Road, Cambridge CB4 3DN | United Kingdom ploscompbiol@plos.org | Phone +44 (0) 1223-442824 | ploscompbiol.org | @PLOSCompBiol

This section collects any data citations, data availability statements, or supplementary materials included in this article.


## Supplementary Materials

Each row represents a different mixture of wgs and pol sequences, going from 100% pol to 100% wgs. Each column represents a bootstrap threshold for clustering, with the subcolumns indicating the mean number of clusters and mean cluster size found at that bootstrap. Cluster number was averaged over all samples for a given mixture, and cluster size was averaged over both all cluster sizes in a given sample, and over all samples.

Each row represents a different mixture of wgs and pol sequences, going from 100% pol to 100% wgs. Each column represents a bootstrap threshold for clustering, with the subcolumns indicating the mean number of clusters and mean cluster size found at that bootstrap. Cluster number was averaged over all samples for a given mixture, and cluster size was averaged over both all cluster sizes in a given sample, and over all samples.

The figure explores the impact of the 4 different base frequency proportions (pi(A), pi(C), pi(G), pi(T), gray bar on top of each panel) in our choice of substitution model for IQTree (GTR+F+I+G4). Proportion is on the Y-axis, and the different mixture datasets are ordered from pol to wgs100 on the X axis. Boxes in panels indicate the central 50% (top and bottom of boxes) and the median (thicker black line in boxes) of the proportions, whiskers indicate the range, and dots indicate outliers. There is a monotonic relationship between relative rate values and wgs proportion beginning with wgs10, when wgs sequences are introduced.

The figure explores the impact of the 4 different gamma rate categories (gray bar on top of each panel) in our choice of substitution model for IQTree (GTR+F+I+G4). Rate is on the Y-axis, and the different mixture datasets are ordered from pol to wgs100 on the X axis. Boxes in panels indicate the central 50% (top and bottom of boxes) and the median (thicker black line in boxes) of the proportions, whiskers indicate the range, and dots indicate outliers. There is a monotonic relationship between relative rate values and wgs proportion beginning with wgs10, when wgs sequences are introduced.

Submitted filename: Reviewer_comments.docx

Submitted filename: reviewer_response_v3.docx

Submitted filename: response_to_reviewers.docx


## Data Availability Statement

All data required to replicate the study’s findings can be found here https://www.hiv.lanl.gov/content/sequence/HIV/mainpage.html . All analysis source code is available at [GITHUB_REPO_REDACTED] .

Articles from PLOS Computational Biology are provided here courtesy of PLOS
