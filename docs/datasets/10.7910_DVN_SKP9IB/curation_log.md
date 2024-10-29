---
sidebar_position: 3
sidebar_label: "Curation log"
---

# CURATE(D): Checklist for Data Curation

:::info[Suggested Citation]

Suggested Citation: Data Curation Network (2022). "CURATE(D) Steps and Checklist for Data Curation, version 2" http://z.umn.edu/curate.

:::

## About

The following information pertains to the curation of this dataset, meaning it references and describes internal processes and procedures to prepare the data and documentation for importing into a public repository. This document is meant only for those who want to understand the curation process and is not particularly useful for those simply wishing to analyze the data within this repository.

## ToDo items

- [x] add N values and file size to the dataset files list of the README (just under the file name)
- [x] add a blurb about the total JoCoHS participation and why this subset is smaller
- [x] added a method to check that categorical values listed in the metadata are not being used so we can remove them and conserve space
- [x] change the empty values to -99 and include in the metadata
- [x] update the user notebook and instructions.md
- [x] include the curation log in the User Guide for the dataset
- [x] in the `Are there missing data?` step, we should add extra steps to consider such as which questions did you ask to help determine if there was missing data; include a way to add questions and answers to those questions within the log similar to a Todo list
- [x] resolve the image count discrepancy (NOTE: there was at least one participant who had US images but no survey data and incomplete clinic)
- [x] write a script that generates a README file for the JoCoKnow User Guide from the public notebook
- [x] **IMPORTANT** name the public README notebook file so that a script can convert the notebook to a Markdown file and load it into the User Guide and add metadata reference to the Markdown from the dataset (as one of the first items users see with the dataset); it will be easier for users to read the dataset intro from the User Guide instead of the clunky Dataverse GUI
- [x] include notes from private curation CHANGELOG


## **CHECK Step**

- [x] Begin Curator Log to track curation decisions
    > - This curation log is not the format I would prefer but my curation log automation program is being designed.
    > - Since we are using the Dataverse API to upload and update files in our dataset via a Jupyter notebook, I need to write and test the Python scripts to ensure the processes I will use are reproducible. I created a reusable Python package (https://github.com/kuhlaid/DvApiMod5.13) and testing notebook (https://github.com/kuhlaid/dv-api-test) to ensure I could test all API calls. I then integrated the DvApiMod5.13 package into my existing curation notebook from a year ago which required some rewriting of code.
    > - The process for publishing the dataset is a bit convoluted since we have one process to upload files to the dataset and another to verify the upload was successful. The reason we do it this way is because we can rely on reproducible automation scripts to update our dataset consistently more so than relying on manually updating the dataset repository. We have a 'private' Notebook that processes identifying data and anonymizes it, then uploads the data files to the repository. We then use a secondary 'public' Notebook which is provided with the dataset to generate a README file that describes the dataset files and data table properties using the data uploaded to the repository to check that our data exists in the repository as we expect it to be. Finally we return back to the 'private' Notebook to remove the dataset draft and upload the final copy which contains the latest generated README Notebook and our final curation log. Then we push copies of the README, curation log, and metadata for the dataset to a Docusarus documentation site. At this point we review and publish the dataset or rerun this whole process as needed.

- [x] Open the related article and supporting information if available 
- [x] Inventory the dataset 
  - [x] Identify file formats
    > Images were originally captured in JPEG format and the image copies were processed through automated Photoshop scripts that corrected the image metadata, anonymized the images, and saved the final images to PNG format.
    > Data-tables are saved to CSV file format so they can be easily parsed through scripts.

  - [x] Review file organization, hierarchy, and naming convention(s)
    > See the next step on image organizing. All files have a hierarchy 'tag' defined for them so while there is no explicit hierarchy within a Dataverse dataset, the tags mimic a hierarchy within a 'tree view'. Images were named using the categorical numbering assigned to the image types and to force the user to refer to the README file for details. The main README file is a Jupyter notebook for displaying not 

  - [x] Extract zip files when possible
    > Since the Dataverse lumps dataset files into flat structure by default, it would have been difficult for users to find the README file in the dataset file list with thousands of images. For this reason I double-zipped image files into archives based on image position (single zipped files would automatically extract all images into the root dataset directory which I did not want). This meant only ~20 files were listed in the dataset instead of 11,000. Archiving the images in the also enables users to only download the types of images they are interested in without the need to download the entire dataset (which is rather large in size).

- [x] Create working copy of files for formal inventory and testing
    > - See the Jupyter notebook for steps used to copy images and process the copies.
    > - Text based data was copied directly from the source where they were collected (database or survey tool) and the processing notebook was designed to retrieve the latest copies of the data in an automated fashion.

- [x] Examine code for obvious errors/missing components, etc.
    > Any code for this dataset is simply for the curation and documentation process through Jupyter notebooks
- [x] Check that metadata quality is rich, accurate, and complete to institutional requirements. 
- [x] Check documentation type 
    > README, Codebook, Metadata, and Data Dictionary
  - [x] Complete
- [x] Check whether human subject data (data about humans regardless of IRB determination) is present. If so, 
  - [x] Request consent form / participation agreement if not present 
  - [x] If the data are not de-identified, document for the "Request" step.
    > Raw data is not de-identified. Data was de-identified and during the data processing 
- [x] Check the accessibility of all files 
  - [x] Ensure there are robust descriptions in plain text of data files and any images.  
- [x] Check whether any visualization(s) of data are easily accessible 
    > NA
     
## **UNDERSTAND Step**                

### Essential Tasks

- [x] Examine files, organization, and documentation more thoroughly.
    > This was an iterative process that cycled between writing code to generate dataset documentation and the files and metadata needed to create it. The main driver was the metadata JSON file which contains the data to initialize a dataset, determines the files to be imported into the repository, defines the data-table variables and categorical values, and other dataset descriptive information. As scripts were modified to parse the metadata and generate new documentation files, the generated files were imported into the repository and documentation website to ensure optimal accessibility and organization.
    > Discussed empty data table cells with the team and a value of -99, instead of NULL, was decided since that would keep numeric columns treated as numeric and not string (if NULL were used)
  - [x] Are there changes that could enhance the dataset? NA
  - [x] Are there missing data?
    > No. This dataset is a subset of the individual data collection instruments and image archives it draws from, which may, by themselves, contain more records that are not specific to this subset.
    > - In this task we asked our own sets of questions to check for missing data.
    > - [x] Do the participants who have US images appear in the final data tables? **Answer**: Yes.
    > - [x] Do the number of participants with KL grades (df_PaKneeKlGrades) match up with the participants with images?  **Answer**: Yes. Scripts compared the subjects with images and KL grades.
- [x] Are any scripts truncating the data?
    > Not exactly. One of the records was flagged as 'ignore' in Qualtrics pain, aching and stiffness survey that needed to be manually corrected. Also the `dftemp2` dataFrame is missing some participants. This is likely due to mismatches between df_qPrivateSubjectEligibility response IDs and the subject id reference data (which I corrected using the `combineDemographicData` method). There was one participant who had US images but did not participate in any of the online surveys and only partial clinic, and another participant who had everything else except for US images (so our total should be 881 - see SubjectExclusions.xlsx).
  - [x] Could a user with similar qualifications to the author's understand and reuse these data and reproduce the results?
  > NA (no analysis data provided)
  - [x] Are the data, documentation and/or metadata presented in a way that aids in interpretation? (e.g., [README Example](https://deepblue.lib.umich.edu/data/Deep\_Blue\_Data\_Example\_Readme.txt)) 
    > Providing both machine readable data and human readable documentation
- [x] Record all questions and concerns in Curation Log.
  > Was concerned about data encoding checks but using VSCode with UTF-8 default encoding and Jupyter notebook processing via Python ensured the encoding of UTF-8 for text files
  > Researchers were concerned about dataset citation versions with the Dataverse, but this is out of scope for us to handle since the Dataverse controls the versioning

*Tasks vary based on file formats and subject domain. Sample tasks based on format:* 

**Tabular Data (e.g, Microsoft Excel) Questions:**

- [x] Check the organization of the data–is it well-structured?
- [x] Are headers/codes clearly defined?
  > The metadata file fully describes the data and variables 
- [x] Is quality control clearly defined? 
- [x] Is methodology clear and sufficient? 

**Database(s) Questions:**

- [x] Is there documentation on tables, relationships, queries, etc?
    > NA
- [x] Can the data be exported (to CSV(s), TXT or other) easily?
  > Yes via API or web interface 
- [x] Which tables or queries are the relevant ones used in a publication?
  > NA

**Code Questions:**

- [x] Does the provided code execute without errors?
  > The code was tested for errors and no errors were thrown at the time of publication (code can become deprecated over time and could throw errors in the future but the code is only important to the generation of the documentation) 
- [x] Is the code commented, i.e., did the author provide descriptive information on sections of code?
    > Yes
- [x] Is data for input missing? Are environmental conditions and parameters noted? Is it clear which language(s) and version(s) are used? 
  > NA
- [x] Does the code use absolute paths or relative paths? If absolute paths, is this documented in the README?
    > Relative
- [x] Are packages or additional libraries used? Is so, is this noted with clear use instructions?
  > Code only provided to better describe the data, but contains clear instructions  
- [x] Are any data organized consistently for access by the code? 
  > NA
- [x] Is there an indication of whether the depositor intends users to be able to run the code and reproduce results, or just see the process used? 
  > Code only provided for advanced users wishing to use in their own projects and is not essential to the use of the 

## **REQUEST Step**

### Essential Tasks

- [x] Ask about additional data contributors, beyond publication authors. Consider using the Contributor Roles Taxonomy to communicate this: https://casrai.org/credit/  
- [x] Summarize conversations / outreach efforts in Curator Log
  > Reaching out to PIs to review the dataset before final publication
  > Received PI and researcher suggestions for metadata updates, so updating the metadata file, removing the dataset draft from the repository and uploading the revisions to the repository. Adding scripts to include the variable labels in the statistics for the README. Once the new dataset draft is uploaded I regenerate the README file based on the latest metadata pushed to the repository.

## **AUGMENT Step**

### Essential Tasks

- [x] Review information received from the researcher from initial deposit and all subsequent conversations 
- [x] Update, as appropriate: 
  - [x] Metadata 
  > Robust metadata with embedded schemas
  - [x] Documentation (README, Codebook, Data Dictionary, Other) 
  - [x] Replacement files 
  - [x] Organization and Arrangement of files 
  > Added directory labels for files so files can be organized using a hierarchy or table views 
  - [x] Documentation of file organization, hierarchy, and naming convention(s) 
  > Defined in Metadata file 
- [x] Facilitate dataset discovery: 
  - [x] Add links to related publications, grants, reports, source data, etc. 
  - [x] Provide additional description of files as appropriate for external indexing or other purposes. 
  - [x] Add subject terms 
- [x] Ensure keywords are sufficient and representative 
- [x] Record all changes in the Curation Log 
- [x] Provide suggestions to improve accessibility of content (e.g., alt-text or additional descriptions; color contrast; etc.)

## **TRANSFORM Step**

### Essential Tasks

- [x] Check whether preferred file formats are in use 
  > - Yes, using FAIR file formats.
  - [x] Retain original formats 
    > - Preserving original data this dataset is derived from as part of the project data curation
- [x] Check whether software needed is readily available
  > - Dataset files may be analyzed using open Python or other popular tools
  - [x] Suggest open source options, if applicable and appropriate
  > - Jupyter notebooks and Python are useful for analyzing the data as there is a strong user community for Python and Jupyter provides you with an environment to both run code and document your steps
  - [x] Ensure software and software version is documented
    > NA
- [x] Convert any data visualization(s) that are not accessible (e.g., R [visualizations](https://github.com/DataCurationNetwork/data-primers/blob/master/R%20Data%20Curation%20Primer/R-data-curation-primer.md#accessibility-considerations), which need to be converted for screen reader use, or visualizations that do not meet color contrast guidelines) Reorganize files as appropriate  
- [x] Standardize file names  
- [x] Record any transformations in Curator Log


## **EVALUATE Step**


### Essential Tasks

- [x] Test that files successfully download 
- [x] Check that any transformations didn't introduce problems 
- [x] Review final state of data and record with researcher before publication 
- [x] Add any final changes to Curator Log  

### FAIR evaluation

Findable:  
- [x] Metadata exceeds researcher/ title/ date.  
- [x] There is a unique Persistent ID (DOI, Handle, PURL, etc.).  
- [x] Data/record is discoverable via web search engines.

Accessible:  
- [x] Data/ record are retrievable via a standard protocol (e.g., HTTP).  
- [x] Data/ record are free, open (e.g., via a download link).

Interoperable:
- [x] Metadata is formatted in a standard schema (e.g., Dublin Core).  Metadata is provided in machine-readable format (OAI feed).
  > Metadata requested from the Dataverse repository is available in a variety of formats. The main dataset metadata file also includes an embedded schema that describes the JSON metadata.

Reusable:
- [x] Data include sufficient metadata and supporting documentation about the data characteristics for reuse.
  > Embedded JSON schemas into the JSON metadata files
- [x] A way to contact the researcher directly for further questions is provided
  > Contact form provided in the Dataverse dataset as well as the User Guide
- [x] There are clear indicators of who created, owns, and stewards the data. 
- [x] Data are released with clear data usage terms (e.g., a CC License).


## **DOCUMENT Step**

### Essential Tasks

- [x] Ensure the following information is captured in the Curator Log: 
  - [x] Activities taken during the CURATE process 
  - [x] Accessioning & deposit records (Names, dates, contact information, submission agreements, etc.) 
    > - Initial deposit to draft state is to test the import and check expected files are imported
    > - The Jupyter notebook is then tested and adjusted to work with the data in the draft state
  - [x] Repository collection metadata 
  - [x] Provenance logs (changes by curators in the Transform step) 
  - [x] Service workflow 
  - [x] Correspondences and other interactions 
  - [x] Preservation packaging 
  - [x] Any additional requirements at your institution