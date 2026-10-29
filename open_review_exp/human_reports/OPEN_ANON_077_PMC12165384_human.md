# Decision Letter 0


### Tobias Bollenbach


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Spatiotemporal dynamics of tumor - CAR T-cell interaction following local administration in solid cancers

PLOS Computational Biology

Thank you for submitting your manuscript to PLOS Computational Biology. After careful consideration, we feel that it has merit but does not fully meet PLOS Computational Biology's publication criteria as it currently stands. Therefore, we invite you to submit a revised version of the manuscript that addresses the points raised during the review process. One of the reviewers suggests moving the Methods section before Results. As this is an option that the journal permits, we leave this choice up to your discretion but please provide a rationale for whatever changes you decide to make.

Please submit your revised manuscript within 30 days Mar 21 2025 11:59PM. If you will need more time than this to complete your revisions, please reply to this message or contact the journal office at ploscompbiol@plos.org . When you're ready to submit your revision, log on to https://www.editorialmanager.com/pcompbiol/ and select the 'Submissions Needing Revision' folder to locate your manuscript file.

Please include the following items when submitting your revised manuscript:

* A rebuttal letter that responds to each point raised by the editor and reviewer(s). You should upload this letter as a separate file labeled 'Response to Reviewers'. This file does not need to include responses to formatting updates and technical items listed in the 'Journal Requirements' section below.

* A marked-up copy of your manuscript that highlights changes made to the original version. You should upload this as a separate file labeled 'Revised Manuscript with Track Changes'.

* An unmarked version of your revised paper without tracked changes. You should upload this as a separate file labeled 'Manuscript'.

If you would like to make changes to your financial disclosure, competing interests statement, or data availability statement, please make these updates within the submission form at the time of resubmission. Guidelines for resubmitting your figure files are available below the reviewer comments at the end of this letter.

We look forward to receiving your revised manuscript.

PLOS Computational Biology

PLOS Computational Biology

Journal Requirements:

1) We ask that a manuscript source file is provided at Revision. Please upload your manuscript file as a .doc, .docx, .rtf or .tex. If you are providing a .tex file, please upload it under the item type u2018LaTeX Source Fileu2019 and leave your .pdf version as the item type u2018Manuscriptu2019.

2) Please upload all main figures as separate Figure files in .tif or .eps format. For more information about how to convert and format your figure files please see our guidelines:

https://journals.plos.org/ploscompbiol/s/figures

3) We have noticed that you have a list of Supporting Information legends (S2 File. Dataset 1) in your manuscript. However, there are no corresponding files uploaded to the submission . Please upload them as separate files with the item type 'Supporting Information'.

4) We noted that subfigures S5 (E-H) are labeled as Figure S6. Please check the labels of the supplementary figures.

5) Some material included in your submission may be copyrighted. According to PLOSu2019s copyright policy, authors who use figures or other material (e.g., graphics, clipart, maps) from another author or copyright holder must demonstrate or obtain permission to publish this material under the Creative Commons Attribution 4.0 International (CC BY 4.0) License used by PLOS journals. Please closely review the details of PLOSu2019s copyright requirements here: PLOS Licenses and Copyright. If you need to request permissions from a copyright holder, you may use PLOS's Copyright Content Permission form.

Please respond directly to this email and provide any known details concerning your material's license terms and permissions required for reuse, even if you have not yet obtained copyright permissions or are unsure of your material's copyright compatibility. Once you have responded and addressed all other outstanding technical requirements, you may resubmit your manuscript within Editorial Manager.

Potential Copyright Issues:

i) Figures 1B, 1C. Please confirm whether you drew the images / clip-art within the figure panels by hand. If you did not draw the images, please provide (a) a link to the source of the images or icons and their license / terms of use; or (b) written permission from the copyright holder to publish the images or icons under our CC BY 4.0 license. Alternatively, you may replace the images with open source alternatives. See these open source resources you may use to replace images / clip-art:

- https://commons.wikimedia.org

- https://openclipart.org/ .

Reviewer's Responses to Questions

Comments to the Authors:

Please note that one of the reviews is uploaded as an attachment.

Reviewer #1: PCOMPBIOL-D-24-01849

Spatiotemporal dynamics of tumor - CAR T-cell interaction following local administration in solid cancers

In this article by Owens, Rahman, and Bozic, the authors present a mathematical model to study two different routes of administration of CAR T cells in solid tumors. They use previously published preclinical data and prior literature to ground their model in data and to study different possible therapeutic outcomes. The manuscript is well written, well motivated, and is likely to be of interest to a wide audience in the fields of mathematical biology, cancer research, and CAR T cells.

The authors principal conclusion is that “We demonstrate that the model can recapitulate tumor and CAR T-cell data from small imaging studies of local administration of CAR T cells in mouse models.”, and that “locally administered CAR T cells will be most successful against slowly proliferating, highly diffusive tumors.” I have concerns about both of these conclusions, namely 1) their model is fit to imaging data, and therefore does not recapitulate the dynamics per say as much as reproduce them, and 2) the efficacy against highly diffusive tumors may be an artifact of the diffusion thresholding in their model. However, there are plenty of insights from their model that can be well justified and supported as conclusions.

I have a few significant concerns regarding the modeling:

Why do the authors threshold diffusion? This is a major assumption in the model that is not consistent with previous PDE modeling in this area, and is explained or justified at all.

The authors glaze over the exhausted cell compartment, and provide no rationale for its inclusion or the key parameter (q) in determining the fraction. Also, exhausted cells are not graphed or discussed in detail. So why include them?

Similarly, the D function (after equation 3b) is complex and not motivated at all. F2 appears to be a very interesting and complex term. Please explain to the reader.

I think the assumption of uniform CAR T cell density on the tumor surface (even in spherical symmetry) is far too simplified, but I do not insist it be changed. Consider providing much more justification for this.

Why do the authors present 4 tumor growth archetypes but present only 3 in figures 3,4? Confusing.

I think the manuscript would benefit greatly from a discussion about the parameters and their meanings, particularly the CAR parameters. Can the tumor growth/diffusion and CAR dynamics reveal more specific/quantitative relationships between the parameters? Also, the 20% reduction in parameters to model ‘reduced efficacy in solid tumors’ is important and not studied or motivated.

Check carefully for typos and latex issues. There are more than a few. (ex. T-cells vs. T cells).

Numerical values in caption of Figure 2 are cumbersome to read. They would be better as a table.

I find figure 1A to be more confusing than helpful. Difficult to interpret the 4 arrows and dots, and the complex term at the top (jD(u,v)^2v/, …) is not explained in the caption or main text in sufficient detail to understand.

Can the variance across mice be shown in Figure 5? Authors state the model was fit to the mean value.

In vitro and ex vivo used to mean the same thing. Consider using a single term.

The \cdot notation used in place of \nabla is unconventional and also not introduced or explained (equations 1,2).

Reviewer #2: Uploaded as an attachment

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

[NOTE: If reviewer comments were submitted as an attachment file, they will be attached to this email and accessible via the submission site. Please log into your account, locate the manuscript record, and check for the action link "View Attachments". If this link does not appear, there are no attachment files.]

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com/ . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Registration is free. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email PLOS at figures@plos.org . Please note that Supporting Information files do not need this step. If there are other versions of figure files still present in your submission file inventory at resubmission, please replace them with the PACE-processed versions.

To enhance the reproducibility of your results, we recommend that authors of applicable studies deposit laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols

Submitted filename: Review of PCOMPBIOL-D-24-01849.docx


# Author response to Decision Letter 1

Collection date 2025 Jun.

Submitted filename: ResponseToReviewers.docx


# Decision Letter 1


### James Faeder


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

We are pleased to inform you that your manuscript 'Spatiotemporal dynamics of tumor - CAR T-cell interaction following local administration in solid cancers' has been provisionally accepted for publication in PLOS Computational Biology.

Before your manuscript can be formally accepted you will need to complete some formatting changes, which you will receive in a follow up email. A member of our team will be in touch with a set of requests.

Please note that your manuscript will not be scheduled for publication until you have made the required changes, so a swift response is appreciated.

IMPORTANT: The editorial review process is now complete. PLOS will only permit corrections to spelling, formatting or significant scientific errors from this point onwards. Requests for major changes, or any which affect the scientific understanding of your work, will cause delays to the publication date of your manuscript.

Should you, your institution's press office or the journal office choose to press release your paper, you will automatically be opted out of early publication. We ask that you notify us now if you or your institution is planning to press release the article. All press must be co-ordinated with PLOS.

Thank you again for supporting Open Access publishing; we are looking forward to publishing your work in PLOS Computational Biology.

PLOS Computational Biology

PLOS Computational Biology

***********************************************************

Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #1: Thank you for thoroughly addressing all reviewer concerns. My only remaining comment is that the model schematic in figure 1 would be helpful to include, provided that it is consistently annotated (or not). In the original version, not all interactions were labeled, and the labels that were provided were not described. I think a schematic of the model, even a simplified one, would benefit the paper and reader.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

This section collects any data citations, data availability statements, or supplementary materials included in this article.


## Supplementary Materials

Data digitized from pre-clinical mouse studies and used for model fitting.

Submitted filename: Review of PCOMPBIOL-D-24-01849.docx

Submitted filename: ResponseToReviewers.docx


## Data Availability Statement

The murine data values used for model parameter estimation are available in the supporting data file. This file was created by digitizing data from images previously published by Skovgard et al ., DOI: 10.1016/j.omto.2021.06.006 and Zhao et al ., DOI: 10.1158/0008-5472.CAN-10-2880. MATLAB code used to produce the results included in this work is available on github at https://github.com/lacyk3/RadiallySymmetricCART .

Articles from PLOS Computational Biology are provided here courtesy of PLOS
