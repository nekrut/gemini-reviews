# Decision Letter 0


### Jean Fan


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

A graph neural network-based spatial multi-omics data integration method for deciphering spatial domains

PLOS Computational Biology

Thank you for submitting your manuscript to PLOS Computational Biology. After careful consideration, we feel that it has merit but does not fully meet PLOS Computational Biology's publication criteria as it currently stands. Therefore, we invite you to submit a revised version of the manuscript that addresses the points raised during the review process.

Please submit your revised manuscript within 60 days Jun 20 2025 11:59PM. If you will need more time than this to complete your revisions, please reply to this message or contact the journal office at ploscompbiol@plos.org. When you're ready to submit your revision, log on to https://www.editorialmanager.com/pcompbiol/ and select the 'Submissions Needing Revision' folder to locate your manuscript file.

Please include the following items when submitting your revised manuscript:

* A rebuttal letter that responds to each point raised by the editor and reviewer(s). You should upload this letter as a separate file labeled 'Response to Reviewers'. This file does not need to include responses to formatting updates and technical items listed in the 'Journal Requirements' section below.

* A marked-up copy of your manuscript that highlights changes made to the original version. You should upload this as a separate file labeled 'Revised Manuscript with Track Changes'.

* An unmarked version of your revised paper without tracked changes. You should upload this as a separate file labeled 'Manuscript'.

If you would like to make changes to your financial disclosure, competing interests statement, or data availability statement, please make these updates within the submission form at the time of resubmission. Guidelines for resubmitting your figure files are available below the reviewer comments at the end of this letter

We look forward to receiving your revised manuscript.

PLOS Computational Biology

PLOS Computational Biology

Additional Editor Comments :

While the editors do not view the concern about novelty raised by Reviewer #3 as a major issue, the authors are encouraged to clarify their contribution by differentiating more clearly from earlier work via descriptive explanation in addition to comparative evaluation/analysis.

Journal Requirements:

1) Please provide an Author Summary. This should appear in your manuscript between the Abstract (if applicable) and the Introduction, and should be 150-200 words long. The aim should be to make your findings accessible to a wide audience that includes both scientists and non-scientists. Sample summaries can be found on our website under Submission Guidelines:

https://journals.plos.org/ploscompbiol/s/submission-guidelines#loc-parts-of-a-submission

2) Please upload all main figures as separate Figure files in .tif or .eps format. For more information about how to convert and format your figure files please see our guidelines:

https://journals.plos.org/ploscompbiol/s/figures

3) We have noticed that you have uploaded Supporting Information files, but you have not included a list of legends. Please add a full list of legends for your Supporting Information files after the references list.

4) Some material included in your submission may be copyrighted. According to PLOSu2019s copyright policy, authors who use figures or other material (e.g., graphics, clipart, maps) from another author or copyright holder must demonstrate or obtain permission to publish this material under the Creative Commons Attribution 4.0 International (CC BY 4.0) License used by PLOS journals. Please closely review the details of PLOSu2019s copyright requirements here: PLOS Licenses and Copyright. If you need to request permissions from a copyright holder, you may use PLOS's Copyright Content Permission form.

Please respond directly to this email and provide any known details concerning your material's license terms and permissions required for reuse, even if you have not yet obtained copyright permissions or are unsure of your material's copyright compatibility. Once you have responded and addressed all other outstanding technical requirements, you may resubmit your manuscript within Editorial Manager.

Potential Copyright Issues:

i) Figure 1. Please confirm whether you drew the images / clip-art within the figure panels by hand. If you did not draw the images, please provide (a) a link to the source of the images or icons and their license / terms of use; or (b) written permission from the copyright holder to publish the images or icons under our CC BY 4.0 license. Alternatively, you may replace the images with open source alternatives. See these open source resources you may use to replace images / clip-art:

- https://commons.wikimedia.org

- https://openclipart.org/ .

5) Please amend your detailed Financial Disclosure statement. This is published with the article. It must therefore be completed in full sentences and contain the exact wording you wish to be published.

1) Please clarify all sources of financial support for your study. List the grants, grant numbers, and organizations that funded your study, including funding received from your institution. Please note that suppliers of material support, including research materials, should be recognized in the Acknowledgements section rather than in the Financial Disclosure

2) State the initials, alongside each funding source, of each author to receive each grant. For example: "This work was supported by the National Institutes of Health (####### to AM; ###### to CJ) and the National Science Foundation (###### to AM)."

3) State what role the funders took in the study. If the funders had no role in your study, please state: "The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript."

4) If any authors received a salary from any of your funders, please state which authors and which funders.

6) Your current Financial Disclosure states, "The author(s) received no specific funding for this work."

However, your funding information on the submission form indicates receiving funds. Please ensure that the funders match between the Financial Disclosure field and the Funding Information tab in the online submission form. Both locations should list the same funders, grant numbers, and recipients in the same order.

Reviewer's Responses to Questions

Reviewer #1: The paper proposes SpaMI, a graph neural network-based method for integrating spatial multi-omics data to identify spatial domains. It combines contrastive learning and attention mechanisms to improve integration accuracy and denoising. However, several key issues need to be addressed:

1. It would be beneficial to briefly discuss the specific biological problems your study aims to address and their potential biological significance in the introduction. This would enhance the relevance and impact of your research.

2. The literature review section should be further enriched with a more detailed discussion of existing methods, particularly those directly related to the methods proposed in this paper.

3. As a computational model, the article does not provide detailed information on the computational resource requirements of the SpaMI model, including runtime and memory consumption.

4. For datasets without annotations, the authors used only Moran's I as the evaluation metric. Additional metrics should be employed to more comprehensively validate the performance of SpaMI.

5. The manuscript contains some textual errors, such as "import" on page 9. Please review the entire manuscript carefully.

6. Concerns remain about the experimental design. While the authors reported external clustering metrics (e.g., ARI, NMI) for simulated datasets, they only used internal metrics for real datasets. Given the significant differences between simulated and real data, the validation should be strengthened by including more annotated real datasets.

Reviewer #2: This manuscript introduces SpaMI, an innovative graph neural network (GNN)-based framework for integrating spatial multi-omics data. By leveraging contrastive learning, attention mechanisms, and joint optimization of reconstruction and correspondence losses, SpaMI effectively addresses the challenges of spatial heterogeneity and noise in multi-omics datasets. The authors validate SpaMI on both simulated and real-world datasets (e.g., mouse brain and thymus), demonstrating its superior performance in spatial domain identification, denoising, and cross-platform compatibility compared to existing methods. The work is timely, methodologically rigorous, and provides a valuable tool for spatial multi-omics research. The code and data availability further enhance its reproducibility and potential impact. I have the following suggestions.

1. Benchmarking on Public Datasets:

The authors mention multiple spatial multi-omics technologies (Refs. 7–16). Given the growing availability of public datasets, could SpaMI be tested on additional datasets (e.g., tumor tissues or human samples) to further validate its generalizability?

2. Estimation of Spatial Domain Number:

How is the number of spatial domains determined? Could automated methods (e.g., ASTER, scCCESS) be integrated to estimate domain numbers, similar to cell-type quantification in single-cell analysis?

3. Prior-Based Learning:

Public databases (e.g., 10x Visium, Allen Brain Atlas) host vast prior data. Can SpaMI leverage such resources to enhance integration via transfer learning or guided training (10.1101/gr.277891.123)?

4. Scalability via Metacell Strategies:

With increasing data scale, could metacell-based approaches (e.g., EpiCarousel) be adopted to improve computational efficiency while preserving spatial resolution?

5. Computational Efficiency:

The manuscript critiques spaMultiVAE’s complexity. Could the authors quantify SpaMI’s runtime, memory usage, and scalability on larger datasets?

6. Tool Packaging for Accessibility:

While the GitHub repository is valuable, packaging SpaMI into a Python library (e.g., via PyPi) with standardized APIs and tutorials would greatly enhance its usability and adoption.

Reviewer #3: This paper proposed a graph neural network-based model named SpaMI for spatial multi-omics data integration. SpaMI used contrastive learning strategy to extract features within each omics and introduced an attention mechanism to integrate omics-specific representations, which then are utilized for various downstream tasks. The model was validated on both simulated data and real spatial multi-omics datasets. Spatial multi-omics is cutting-edge technique, and while some methods have been developed for spatial multi-omics data integration, further development is still needed. Overall, this paper is well-written. However, the novelty is somewhat limited, as the SpaMI framework closely resembles that of a previous study (Long et al., 2024). There are some major concerns as below:

1. Insufficient novelty. SpaMI combines graph neural networks (GNN) with attention mechanism, which is quite similar to the approach in Long et al., 2024. Although contrastive learning is incorporated in SpaMI, the difference between the two methods is minimal

2. Weak results. The authors evaluated the performance of the proposed method using simulated and three real spatial multi-omics data. However, SpaMI appears comparable to the baseline, SpatialGlue, across most datasets. For example,

� Visually, the spatial distribution and UMAP results for the simulation show that SpaMI and SpatialGlue are comparable. Both methods accurately identify the four factors and background.

� In the mouse thymus results, it is difficult to discern any significant advantage of SpaMI over SpatialGlue, as both methods identify main tissue regions with high accuracy.

3. Inaccurate or unclear descriptions:

� The author claim that single cell multi-omics integration methods might not be applicable for spatial multi-omics data as spatial information is not considered. However, these methods can still be applied to spatial multi-omics data, as one can choose not to use spatial information.

� The author state, “However, the model adopts single-layer GCN as encoder, making the network structure too simple to effectively capture complex structures”. Are there any supporting evidence or results for this claim?

4. Missing labels. Some figures lack labels, such as Fig.3 C, E, Fig. 4 C, E, Fig. 6 C, F. The authors provide labels for SpaMI, but not for other methods.

5. How about the robustness of the proposed method? Most parameters vary across different datasets, which might weaken the generalizability of the proposed method when applied to new datasets.

6. Some typos can be found in the manuscript, such as “is decrease”.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

[NOTE: If reviewer comments were submitted as an attachment file, they will be attached to this email and accessible via the submission site. Please log into your account, locate the manuscript record, and check for the action link "View Attachments". If this link does not appear, there are no attachment files.]

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com/ . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Registration is free. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email PLOS at figures@plos.org. Please note that Supporting Information files do not need this step. If there are other versions of figure files still present in your submission file inventory at resubmission, please replace them with the PACE-processed versions.

To enhance the reproducibility of your results, we recommend that authors of applicable studies deposit laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols


# Author response to Decision Letter 1

Collection date 2025 Sep.

Submitted filename: Response to Reviewers_revised.docx


# Decision Letter 1


### Shaun Mahony


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PCOMPBIOL-D-25-00362R1

A graph neural network-based spatial multi-omics data integration method for deciphering spatial domains

PLOS Computational Biology

Thank you for submitting your manuscript to PLOS Computational Biology. After careful consideration, we feel that it has merit but does not fully meet PLOS Computational Biology's publication criteria as it currently stands. Therefore, we invite you to submit a revised version of the manuscript that addresses the points raised during the review process.

Please submit your revised manuscript within 30 days Oct 15 2025 11:59PM. If you will need more time than this to complete your revisions, please reply to this message or contact the journal office at ploscompbiol@plos.org. When you're ready to submit your revision, log on to https://www.editorialmanager.com/pcompbiol/ and select the 'Submissions Needing Revision' folder to locate your manuscript file.

Please include the following items when submitting your revised manuscript:

* A rebuttal letter that responds to each point raised by the editor and reviewer(s). You should upload this letter as a separate file labeled 'Response to Reviewers'. This file does not need to include responses to formatting updates and technical items listed in the 'Journal Requirements' section below.

* A marked-up copy of your manuscript that highlights changes made to the original version. You should upload this as a separate file labeled 'Revised Manuscript with Track Changes'.

* An unmarked version of your revised paper without tracked changes. You should upload this as a separate file labeled 'Manuscript'.

If you would like to make changes to your financial disclosure, competing interests statement, or data availability statement, please make these updates within the submission form at the time of resubmission. Guidelines for resubmitting your figure files are available below the reviewer comments at the end of this letter.

We look forward to receiving your revised manuscript.

PLOS Computational Biology

PLOS Computational Biology

Additional Editor Comments:

Thank you for sending your revised manuscript back to PLOS Computational Biology. As you will see, one of the reviewers has remaining concerns. These issues will need to be addressed before we can consider publication.

Journal Requirements:

1) Please provide an Author Summary. This should appear in your manuscript between the Abstract (if applicable) and the Introduction, and should be 150-200 words long. The aim should be to make your findings accessible to a wide audience that includes both scientists and non-scientists. Sample summaries can be found on our website under Submission Guidelines:

https://journals.plos.org/ploscompbiol/s/submission-guidelines#loc-parts-of-a-submission

2) We have noticed that you have uploaded Supporting Information files, but you have not included a list of legends. Please add a full list of legends for your Supporting Information files after the references list.

3) Please ensure that the funders and grant numbers match between the Financial Disclosure field and the Funding Information tab in your submission form. Note that the funders must be provided in the same order in both places as well.

State what role the funders took in the study. If the funders had no role in your study, please state: "The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.".

If you did not receive any funding for this study, please simply state: u201cThe authors received no specific funding for this work.u201d

Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #2: My concerns have been addressed.

Reviewer #3: The authors have carefully addressed most of my comments. However, the manuscript still requires further improvement before it can be considered for publication.

1. While the authors have quantitatively demonstrated the contributions of each components using simulated data, these results are insufficient. First, no visualization results are provided. Quantitative evaluation alone may not objectively reflect model performance. Visual evaluation should be also included to support the findings. Second, the ablation study is limited to simulated data, which is overly simplistic and may not accurately capture the complexity of real-world scenarios. Therefore, the inclusion of real-world datasets in the ablation study is necessary to more rigorously validate the model’s effectiveness.

2. In their response, the authors noted that prior information such as annotations was used in the extended model. However, this detail appears to be missing from the manuscript. If such supervision was indeed employed, the comparisons with baseline methods may be biased, as many of the baselines are unsupervised. This discrepancy should be clarified to ensure a fair evaluation.

3. The figures should be improved. For example, the labels are provided only for the proposed methods, such as Fig. 2A, Fig. 3C. The labels for other methods should be also provided.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .

Reviewer #2: Yes: Shengquan Chen

[NOTE: If reviewer comments were submitted as an attachment file, they will be attached to this email and accessible via the submission site. Please log into your account, locate the manuscript record, and check for the action link "View Attachments". If this link does not appear, there are no attachment files.]

While revising your submission, please upload your figure files to the Preflight Analysis and Conversion Engine (PACE) digital diagnostic tool, https://pacev2.apexcovantage.com/ . PACE helps ensure that figures meet PLOS requirements. To use PACE, you must first register as a user. Registration is free. Then, login and navigate to the UPLOAD tab, where you will find detailed instructions on how to use the tool. If you encounter any issues or have any questions when using PACE, please email PLOS at figures@plos.org. Please note that Supporting Information files do not need this step. If there are other versions of figure files still present in your submission file inventory at resubmission, please replace them with the PACE-processed versions.

To enhance the reproducibility of your results, we recommend that authors of applicable studies deposit laboratory protocols in protocols.io, where a protocol can be assigned its own identifier (DOI) such that it can be cited independently in the future. Additionally, PLOS ONE offers an option to publish peer-reviewed clinical study protocols. Read more information on sharing protocols at https://plos.org/protocols?utm_medium=editorial-email&utm_source=authorletters&utm_campaign=protocols


# Author response to Decision Letter 2

Collection date 2025 Sep.

Submitted filename: Response to Reviewers.pdf


# Decision Letter 2


### Shaun Mahony


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

We are pleased to inform you that your manuscript 'A graph neural network-based spatial multi-omics data integration method for deciphering spatial domains' has been provisionally accepted for publication in PLOS Computational Biology.

Before your manuscript can be formally accepted you will need to complete some formatting changes, which you will receive in a follow up email. A member of our team will be in touch with a set of requests.

Please note that your manuscript will not be scheduled for publication until you have made the required changes, so a swift response is appreciated.

IMPORTANT: The editorial review process is now complete. PLOS will only permit corrections to spelling, formatting or significant scientific errors from this point onwards. Requests for major changes, or any which affect the scientific understanding of your work, will cause delays to the publication date of your manuscript.

Should you, your institution's press office or the journal office choose to press release your paper, you will automatically be opted out of early publication. We ask that you notify us now if you or your institution is planning to press release the article. All press must be co-ordinated with PLOS.

Thank you again for supporting Open Access publishing; we are looking forward to publishing your work in PLOS Computational Biology.

PLOS Computational Biology

***********************************************************

Reviewer's Responses to Questions

Comments to the Authors:

Please note here if the review is uploaded as an attachment.

Reviewer #2: I have no further concerns.

Reviewer #3: The authors have carefully addressed the comments. I recommend the publication of this paper.

Have the authors made all data and (if applicable) computational code underlying the findings in their manuscript fully available?

The PLOS Data policy requires authors to make all data and code underlying the findings described in their manuscript fully available without restriction, with rare exception (please refer to the Data Availability Statement in the manuscript PDF file). The data and code should be provided as part of the manuscript or its supporting information, or deposited to a public repository. For example, in addition to summary statistics, the data points behind means, medians and variance measures should be available. If there are restrictions on publicly sharing data or code —e.g. participant privacy or use of data from a third party—those must be specified.

PLOS authors have the option to publish the peer review history of their article ( what does this mean? ). If published, this will include your full peer review and any attached files.

If you choose “no”, your identity will remain anonymous but your review may still be made public.

Do you want your identity to be public for this peer review? For information about this choice, including consent withdrawal, please see our Privacy Policy .


# Acceptance letter


### Shaun Mahony


#### Roles

This is an open access article distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

PCOMPBIOL-D-25-00362R2

A graph neural network-based spatial multi-omics data integration method for deciphering spatial domains

I am pleased to inform you that your manuscript has been formally accepted for publication in PLOS Computational Biology. Your manuscript is now with our production department and you will be notified of the publication date in due course.

The corresponding author will soon be receiving a typeset proof for review, to ensure errors have not been introduced during production. Please review the PDF proof of your manuscript carefully, as this is the last chance to correct any errors. Please note that major changes, or those which affect the scientific understanding of the work, will likely cause delays to the publication date of your manuscript.

Soon after your final files are uploaded, unless you have opted out, the early version of your manuscript will be published online. The date of the early version will be your article's publication date. The final article will be published to the same URL, and all versions of the paper will be accessible to readers.

You will receive an invoice from PLOS for your publication fee after your manuscript has reached the completed accept phase. If you receive an email requesting payment before acceptance or for any other service, this may be a phishing scheme. Learn how to identify phishing emails and protect your accounts at https://explore.plos.org/phishing .

Thank you again for supporting PLOS Computational Biology and open-access publishing. We are looking forward to publishing your work!

PLOS Computational Biology | Carlyle House, Carlyle Road, Cambridge CB4 3DN | United Kingdom ploscompbiol@plos.org | Phone +44 (0) 1223-442824 | ploscompbiol.org | @PLOSCompBiol

This section collects any data citations, data availability statements, or supplementary materials included in this article.


## Supplementary Materials

Submitted filename: Response to Reviewers_revised.docx

Submitted filename: Response to Reviewers.pdf


## Data Availability Statement

An open-source Python implementation of the SpaMI toolkit is accessible at [GITHUB_REPO_REDACTED] .

Articles from PLOS Computational Biology are provided here courtesy of PLOS
