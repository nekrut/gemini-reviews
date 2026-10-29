# Decision Letter 0


### Mark Alber


### Lun Hu


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

HMFGraph: Novel Bayesian approach for recovering biological networks

PLOS Computational Biology

Thank you for submitting your manuscript to PLOS Computational Biology. After careful consideration, we feel that it has merit but does not fully meet PLOS Computational Biology's publication criteria as it currently stands. Therefore, we invite you to submit a revised version of the manuscript that addresses the points raised during the review process.

​Please submit your revised manuscript within 60 days Aug 25 2025 11:59PM. If you will need more time than this to complete your revisions, please reply to this message or contact the journal office at ploscompbiol@plos.org . When you're ready to submit your revision, log on to https://www.editorialmanager.com/pcompbiol/ and select the 'Submissions Needing Revision' folder to locate your manuscript file.

Please include the following items when submitting your revised manuscript:

* A rebuttal letter that responds to each point raised by the editor and reviewer(s). You should upload this letter as a separate file labeled 'Response to Reviewers'. This file does not need to include responses to formatting updates and technical items listed in the 'Journal Requirements' section below.

* A marked-up copy of your manuscript that highlights changes made to the original version. You should upload this as a separate file labeled 'Revised Manuscript with Track Changes'.

* An unmarked version of your revised paper without tracked changes. You should upload this as a separate file labeled 'Manuscript'.

If you would like to make changes to your financial disclosure, competing interests statement, or data availability statement, please make these updates within the submission form at the time of resubmission. Guidelines for resubmitting your figure files are available below the reviewer comments at the end of this letter

We look forward to receiving your revised manuscript.

PLOS Computational Biology

PLOS Computational Biology

Journal Requirements:

1) We ask that a manuscript source file is provided at Revision. Please upload your manuscript file as a .doc, .docx, .rtf or .tex. If you are providing a .tex file, please upload it under the item type u2018LaTeX Source Fileu2019 and leave your .pdf version as the item type u2018Manuscriptu2019.

2) Your manuscript is missing the following section: Results. Please ensure all required sections are present and in the correct order. Make sure section heading levels are clearly indicated in the manuscript text, and limit sub-sections to 3 heading levels. An outline of the required sections can be consulted in our submission guidelines here:

https://journals.plos.org/ploscompbiol/s/submission-guidelines#loc-parts-of-a-submission

3) Please upload all main figures as separate Figure files in .tif or .eps format. For more information about how to convert and format your figure files please see our guidelines:

https://journals.plos.org/ploscompbiol/s/figures

4) Please provide a completed 'Competing Interests' statement, including any COIs declared by your co-authors. If you have no competing interests to declare, please state "The authors have declared that no competing interests exist".

Reviewer's Responses to Questions

Reviewer #1: The manuscript introduces a fast Bayesian Gaussian Graphical Model using a hierarchical matrix-F prior, offering competitive network recovery and efficient hyperparameter tuning via condition number constraints. It further proposes a novel edge selection method based on credible intervals optimized by F1-score, with superior computational performance over MCMC-based approaches.

The authors have conducted substantial work in the field of recovering biological networks. However, my main concerns are as follows:

1.The abstract should clearly articulate the current limitations in existing approaches in order to highlight the novelty and contributions of this work.

2.The introduction is recommended to be enriched with more background on real-world biological applications of network recovery, such as cancer pathway inference or metabolic network reconstruction, in order to better demonstrate the practical relevance and appeal of the method.

3.While the proposed hierarchical Matrix-F prior is theoretically innovative, a more systematic and quantitative comparison with existing Matrix-F-based models is needed—particularly regarding stability and inference performance in high-dimensional settings.

4.The section on Gaussian graphical models reads more like a preliminaries/background section than a direct part of the model description. It might be clearer if repositioned or retitled accordingly.

5.The methodological presentation requires a major revision. Rather than listing only what modifications were made to the model, I would prefer a more structured exposition that traces the complete modeling pipeline—from input to output—with the innovations clearly embedded within that logical flow.

6.A high-level schematic or workflow diagram summarizing the modeling procedure and its innovations would significantly improve clarity and accessibility.

7.The manuscript should more clearly explain the differences between the generalized expectation-maximization (GEM) algorithm and the standard EM algorithm, and elaborate on why GEM is particularly effective in the context of this model.

8.The performance comparisons across methods rely on fixed α and CI strategies for the proposed model. To ensure fairness, I suggest applying a consistent criterion (e.g., a fixed FDR threshold such as 0.2) across all methods.

9.Although real biological datasets are analyzed, the interpretations remain largely qualitative. Incorporating more biological validation—such as comparison with known gene interactions or pathway annotations—would greatly strengthen the biological significance of the recovered networks.

10.Given the large number of mathematical symbols (e.g., α, β, ν, δ), I recommend including a notation table in the methods section to improve readability and reduce potential confusion.

Reviewer #2: This paper proposes a new way to construct biological networks from biological data using Bayesian Gaussian graphical models. Its contributions include incorporating a matrix-F prior, developing a fast generalized EM algorithm, and designing a scheme to select hyperparameters. The methodology part of this paper is statistically sound. However, I have some comments that need more explanations by the authors.

1. The introduction section of this paper is too statistically technical. As this paper is motivated by constructing biological networks, it would be more interesting to general audiences if the authors can make clear which kind of biological network you want to recover, protein network, gene network, or gut network, and introduce some neccessary biological backgrounds.

2. My second question is about the validity of the Gaussian assumption. Many biological data do not fully follow the Gaussian assumption and also exhibit heterogeneity, such as the single cell gene expressions. In the real applications, the paper analyzes gene expression data and gut data. Therefore, it is important to verify the Gaussian assumption in this data. In my opinion, one important statistical paper to address single cell gene expression data is “Estimating heterogeneous gene regulatory networks from zero-inflated single-cell expression data”, The Annals of Applied Statistics, 2022. The authors may emphasize the difference between the proposed method HMFGraph and this AOAS paper, and I believe this AOAS paper can further motivate the improvement of HMFGraph when applied to zero-inflated and heterogeneous biological data.

3. Regarding the edge selection in section 2.5, why do not the authors apply a variable selection prior to the edges, such spike-slab prior or horseshoe prior? The authors should provide some explanations.

4. About the hyperparameter selection, users should calculate Cond(\hat{\Omega}_{\alpha}) for each alpha. What is the computational time for one single alpha? Is it practically applicable? Moreover, could the authors implement some sensitivity analyses for these hyperparameters? In this way, we can largely reduce the selection range of the hyperparameters.

5. The explations for the results in real datasets are shallow. Could the authors provide more biological insights from the results by HMFGraph? More biological findings rather than simulation results are more interesting to Plos computational biology readers.

Reviewer #3: The authors introduce HMFGraph, a Bayesian GGM method that employs a hierarchical matrix-F prior, which computationally outperforms existing Bayesian GGM approaches in handling high-dimensional biological data. The use of this prior enhances flexibility and adaptability to different network structures. The manuscript was well-written and easy to read. My concerns are as follows.

1.Justification of the introduced new parameter \beta :

Figure 3 showed the curves of FDR with varying \alpha, however, the role and selection process for \beta require further explanation or empirical validation to ensure readers understand its impact on network recovery.

2.Sensitivity/Specificity Analysis:

The authors reported the FDR of varying \alpha. Reporting sensitivity/specificity for both \alpha and \beta would help guide users in parameter selection.

3. Biological Interpretation:

The biological significance of the results, particularly in the gut microbiome study, could be strengthened with a comparison to results in the literature.

4.page 5/23, line 135, \beta \in [0,1[should be changed to \beta \in [0,1]

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

[NOTE: If reviewer comments were submitted as an attachment file, they will be attached to this email and accessible via the submission site. Please log into your account, locate the manuscript record, and check for the action link "View Attachments". If this link does not appear, there are no attachment files.]

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com/ . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Registration is free. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email PLOS at figures@plos.org . Please note that Supporting Information files do not need this step. If there are other versions of figure files still present in your submission file inventory at resubmission, please replace them with the PACE-processed versions.

To enhance the reproducibility of your results, we recommend that authors of applicable studies deposit laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols


# Author response to Decision Letter 1

Collection date 2025 Oct.

Submitted filename: Response_to_Reviewers.pdf


# Decision Letter 1


### Marc R Birtwistle


### Lun Hu


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PCOMPBIOL-D-25-00977R1

HMFGraph: Novel Bayesian approach for recovering biological networks

PLOS Computational Biology

Thank you for submitting your manuscript to PLOS Computational Biology. After careful consideration, we feel that it has merit but does not fully meet PLOS Computational Biology's publication criteria as it currently stands. Therefore, we invite you to submit a revised version of the manuscript that addresses the points raised during the review process.

Please submit your revised manuscript within 30 days Dec 01 2025 11:59PM. If you will need more time than this to complete your revisions, please reply to this message or contact the journal office at ploscompbiol@plos.org . When you're ready to submit your revision, log on to https://www.editorialmanager.com/pcompbiol/ and select the 'Submissions Needing Revision' folder to locate your manuscript file.

Please include the following items when submitting your revised manuscript:

* A rebuttal letter that responds to each point raised by the editor and reviewer(s). You should upload this letter as a separate file labeled 'Response to Reviewers'. This file does not need to include responses to formatting updates and technical items listed in the 'Journal Requirements' section below.

* A marked-up copy of your manuscript that highlights changes made to the original version. You should upload this as a separate file labeled 'Revised Manuscript with Track Changes'.

* An unmarked version of your revised paper without tracked changes. You should upload this as a separate file labeled 'Manuscript'.

If you would like to make changes to your financial disclosure, competing interests statement, or data availability statement, please make these updates within the submission form at the time of resubmission. Guidelines for resubmitting your figure files are available below the reviewer comments at the end of this letter.

We look forward to receiving your revised manuscript.

PLOS Computational Biology

PLOS Computational Biology

Additional Editor Comments :

One of our reviewers still has some minor concerns regarding this work, and authors are suggested to carefully address these issues.

Note: If the reviewer comments include a recommendation to cite specific previously published works, please review and evaluate these publications to determine whether they are relevant and should be cited. There is no requirement to cite these works unless the editor has indicated otherwise.

Reviewer's Responses to Questions

Reviewer #1: The authors have addressed most of the issues; however, I still have two minor comments that I would like them to revise:

1.The flowchart is rather simplistic. Please enhance it with more relevant illustrations for better visualization and also further optimize the layout and spacing of the figures.

2.In light of the authors’ contributions to biological networks, I suggest that the authors consider citing the following article at appropriate places in the manuscript.

DOI:10.1038/s41551-024-01312-5

DOI: 10.1109/JBHI.2025.3585290

Reviewer #2: I thank the authors for addressing my concerns well.

Reviewer #3: The authors have addressed all my concerns, I have no further comments.

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

Collection date 2025 Oct.

Submitted filename: Response_to_Reviewers_auresp_2.pdf


# Decision Letter 2


### Marc R Birtwistle


### Lun Hu


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

We are pleased to inform you that your manuscript 'HMFGraph: Novel Bayesian approach for recovering biological networks' has been provisionally accepted for publication in PLOS Computational Biology.

Before your manuscript can be formally accepted you will need to complete some formatting changes, which you will receive in a follow up email. A member of our team will be in touch with a set of requests.

Please note that your manuscript will not be scheduled for publication until you have made the required changes, so a swift response is appreciated.

IMPORTANT: The editorial review process is now complete. PLOS will only permit corrections to spelling, formatting or significant scientific errors from this point onwards. Requests for major changes, or any which affect the scientific understanding of your work, will cause delays to the publication date of your manuscript.

Should you, your institution's press office or the journal office choose to press release your paper, you will automatically be opted out of early publication. We ask that you notify us now if you or your institution is planning to press release the article. All press must be co-ordinated with PLOS.

Thank you again for supporting Open Access publishing; we are looking forward to publishing your work in PLOS Computational Biology.

PLOS Computational Biology

PLOS Computational Biology

***********************************************************

All reviewers were satisfied with the changes made in this revision, and they have no further comments.

Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #1: The author answered my opinion very well. I have no more opinions.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .


# Acceptance letter


### Marc R Birtwistle


### Lun Hu


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PCOMPBIOL-D-25-00977R2

HMFGraph: Novel Bayesian approach for recovering biological networks

I am pleased to inform you that your manuscript has been formally accepted for publication in PLOS Computational Biology. Your manuscript is now with our production department and you will be notified of the publication date in due course.

The corresponding author will soon be receiving a typeset proof for review, to ensure errors have not been introduced during production. Please review the PDF proof of your manuscript carefully, as this is the last chance to correct any errors. Please note that major changes, or those which affect the scientific understanding of the work, will likely cause delays to the publication date of your manuscript.

Soon after your final files are uploaded, unless you have opted out, the early version of your manuscript will be published online. The date of the early version will be your article's publication date. The final article will be published to the same URL, and all versions of the paper will be accessible to readers.

For Research, Software, and Methods articles, you will receive an invoice from PLOS for your publication fee after your manuscript has reached the completed accept phase. If you receive an email requesting payment before acceptance or for any other service, this may be a phishing scheme. Learn how to identify phishing emails and protect your accounts at https://explore.plos.org/phishing .

Thank you again for supporting PLOS Computational Biology and open-access publishing. We are looking forward to publishing your work!

PLOS Computational Biology | Carlyle House, Carlyle Road, Cambridge CB4 3DN | United Kingdom ploscompbiol@plos.org | Phone +44 (0) 1223-442824 | ploscompbiol.org | @PLOSCompBiol

This section collects any data citations, data availability statements, or supplementary materials included in this article.


## Supplementary Materials

Includes all supporting information materials.

Submitted filename: Response_to_Reviewers.pdf

Submitted filename: Response_to_Reviewers_auresp_2.pdf


## Data Availability Statement

All codes for reproducing the results are publicly available at https://github.com/AapoKorhonen/HMFGraph-Supplementary . The showcased method can be tested with our R package HMFGraph, also publicly available at Github: https://github.com/AapoKorhonen/HMFGraph .

Articles from PLOS Computational Biology are provided here courtesy of PLOS
