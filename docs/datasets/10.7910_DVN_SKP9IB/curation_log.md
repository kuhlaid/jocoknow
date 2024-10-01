---
sidebar_position: 3
sidebar_label: "Curation log"
---

# CURATE(D): Checklist for Data Curation

:::info[Suggested Citation]

Suggested Citation: Data Curation Network (2022). "CURATE(D) Steps and Checklist for Data Curation, version 2" http://z.umn.edu/curate.

:::

## ToDo items

- [ ] add encoding and encoding checks to datatable files in the metadata.json
- [ ] update the user notebook and instructions.md
- [ ] include the curation log in the User Guide for the dataset
- [ ] in the `Are there missing data?` step, we should add extra steps to consider such as which questions did you ask to help determine if there was missing data; include a way to add questions and answers to those questions within the log similar to a Todo list
- [x] resolve the image count discrepancy (NOTE: there was at least one participant who had US images but no survey data and incomplete clinic)
- [x] write a script that generates a README file for the JoCoKnow User Guide from the public notebook
- [ ] **IMPORTANT** name the public README notebook file so that a script can convert the notebook to a Markdown file and load it into the User Guide and add metadata reference to the Markdown from the dataset (as one of the first items users see with the dataset); it will be easier for users to read the dataset intro from the User Guide instead of the clunky Dataverse GUI
- [ ] include notes from C:\Users\pgale\University of North Carolina at Chapel Hill\TarcStudyDataRepository - Files\DataPull\356-dp\Note2\ProcessDataForDataverse\README.md in this curation log


## **CHECK Step**

- [x] Begin Curator Log to track curation decisions
    > - This curation log is not the format I would prefer but my curation log automation program is being designed, so this will need to suffice.
    > - Since we are using the Dataverse API to upload and update files in our dataset via a Jupyter notebook, I need to write and test the Python scripts to ensure the processes I will use are reproducible. I created a reusable Python package (https://github.com/kuhlaid/DvApiMod5.13) and testing notebook (https://github.com/kuhlaid/dv-api-test) to ensure I could test all API calls. I then integrated the DvApiMod5.13 package into my existing curation notebook from a year ago which required some rewriting of code.
    > - Once the dataset data is processed then the notebook to describe the dataset is written and tested.

- [ ] Open the related article and supporting information if available 
- [x] Inventory the dataset 
  - [x] Identify file formats
    > Images were originally captured in JPEG format and the image copies were processed through automated Photoshop scripts that corrected the image metadata and saved the final images to PNG format.

  - [x] Review file organization, hierarchy, and naming convention(s)
    > See the next step on image organizing. All files have a hierarchy 'tag' defined for them so while there is no explicit hierarching within a Dataverse datset, the tags mimic a hierarchy within a 'tree view'. Images were named using the categorical numbering assigned to the image types and to force the user to refer to the README file for details. The main README file is a Jupyter notebook for displaying not 

  - [x] Extract zip files when possible
    > Since the Dataverse lumps dataset files into flat structure by default, it would have been difficult for users to find the README file in the dataset file list with thousands of images. For this reason I double-zipped image files into archives based on image position (single zipped files would automatically extract all images into the root dataset directory which I did not want). This meant only ~20 files were listed in the dataset instead of 11,000. Archiving the images in the also enables users to only download the types of images they are interested in without the need to download the entire dataset (which is rather large in size).

- [x] Create working copy of files for formal inventory and testing
    > - See the Jupyter notebook for steps used to copy images and process the copies.
    > - Text based data was copied directly from the source where they were collected (database or survey tool) and the processing notebook was designed to retrieve the latest copies of the data in an automated fashion.

- [x] Examine code for obvious errors/missing components, etc.
    > Any code for this dataset is simply for the curation process through the referenced Jupyter notebook
- [ ] Check that metadata quality is rich, accurate, and complete to institutional requirements. 
- [x] Check documentation type 
    > README, Codebook, and Data Dictionary
  - [ ] Complete 
  - [ ] Needs work  
  - [ ] If missing, document for the "Request" step 
- [ ] Check whether human subject data (data about humans regardless of IRB determination) is present. If so, 
  - [ ] Request consent form / participation agreement if not present 
  - [x] If the data are not de-identified, document for the "Request" step.
    > Raw data is not de-identified. Data was de-identified and during the data processing 
- [ ] Check the accessibility of all files 
  - [ ] Ensure there are robust descriptions in plain text of data files and any images.  
- [ ] Check whether any visualization(s) of data are easily accessible 
  - [ ] Review alt-text and visualization descriptions. 
  - [ ] Ensure these describe, but do not interpret, associated visualizations. 
  - [ ] Check data visualizations follow accessible color contrast guidelines 
  - [ ] Recommend graphical representation ______________ 
  - [ ] Recommend web-accessible surrogate ______________
     
## **UNDERSTAND Step**                

### Essential Tasks

- [ ] Examine files, organization, and documentation more thoroughly. 
  - [x] Are there changes that could enhance the dataset? NA
  - [x] Are there missing data?
    > No. This dataset is a subset of the individual data collection instruments and image archives it draws from, which may, by themselves, contain more records that are not specific to this subset.
    > - In this task we asked our own sets of questions to check for missing data.
    > - [x] Do the participants who have US images appear in the final data tables? **Answer**: Yes.
    > - [x] Do the number of participants with KL grades (df_PaKneeKlGrades) match up with the participants with images?  **Answer**: Yes. We compared the subjects with images and KL grades.
- [ ] Are any scripts truncating the data?
    > Not exactly. One of the records was flagged as 'ignore' in Qualtrics pain, aching and stiffness survey that needed to be manually corrected. Also the `dftemp2` dataFrame is missing some participants. This is likely due to mismatches between df_qPrivateSubjectEligibility response IDs and the subject id reference data (which I corrected using the `combineDemographicData` method). There was one participant who had US images but did not participate in any of the online surveys and only partial clinic, and another participant who had everything else except for US images (so our total should be 881 - see SubjectExclusions.xlsx).
  - [ ] Could a user with similar qualifications to the author's understand and reuse these data and reproduce the results?
  - [ ] Are the data, documentation and/or metadata presented in a way that aids in interpretation? (e.g., [README Example](https://deepblue.lib.umich.edu/data/Deep\_Blue\_Data\_Example\_Readme.txt)) 
- [ ] Record all questions and concerns in Curation Log.  

*Tasks vary based on file formats and subject domain. Sample tasks based on format:* 

**Tabular Data (e.g, Microsoft Excel) Questions:**

- [ ] Check the organization of the data–is it well-structured? 
- [ ] Are headers/codes clearly defined? 
- [ ] Is quality control clearly defined? 
- [ ] Is methodology clear and sufficient? 

**Database(s) Questions:**

- [x] Is there documentation on tables, relationships, queries, etc?
    > NA
- [ ] Can the data  be exported (to CSV(s), TXT or other) easily? 
- [ ] Which tables or queries are the relevant ones used in a publication? 

**Code Questions:**

- [ ] Does the provided code execute without errors? 
- [x] Is the code commented, i.e., did the author provide descriptive information on sections of code?
    > Yes
- [ ] Is data for input missing? Are environmental conditions and parameters noted? Is it clear which language(s) and version(s) are used? 
- [x] Does the code use absolute paths or relative paths? If absolute paths, is this documented in the README?
    > Relative
- [ ] Are packages or additional libraries used? Is so, is this noted with clear use instructions?  
- [ ] Are any data organized consistently for access by the code? 
- [ ] Is there an indication of whether the depositor intends users to be able to run the code and reproduce results, or just see the process used?  

## **REQUEST Step**

### Essential Tasks

- [ ] Ask about additional data contributors, beyond publication authors. Consider using the Contributor Roles Taxonomy to communicate this: https://casrai.org/credit/  
- [ ] Summarize conversations / outreach efforts in Curator Log  

## **AUGMENT Step**

### Essential Tasks

- [ ] Review information received from the researcher from initial deposit and all subsequent conversations 
- [ ] Update, as appropriate: 
  - [ ] Metadata 
  - [ ] Documentation (README, Codebook, Data Dictionary, Other) 
  - [ ] Replacement files 
  - [ ] Organization and Arrangement of files 
  - [ ] Documentation of file organization, hierarchy, and naming convention(s)  
- [ ] Facilitate discoverability: 
  - [ ] Add links to related publications, grants, reports, source data, etc. 
  - [ ] Provide additional description of files as appropriate for external indexing or other purposes. 
  - [ ] Add subject terms 
- [ ] Ensure keywords are sufficient and representative 
- [ ] Record all changes in the Curation Log 
- [ ] Provide suggestions to improve accessibility of content (e.g., alt-text or additional descriptions; color contrast; etc.)

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
  - [ ] Ensure software and software version is documented  
- [ ] Convert any data visualization(s) that are not accessible (e.g., R [visualizations](https://github.com/DataCurationNetwork/data-primers/blob/master/R%20Data%20Curation%20Primer/R-data-curation-primer.md#accessibility-considerations), which need to be converted for screen reader use, or visualizations that do not meet color contrast guidelines) Reorganize files as appropriate  
- [ ] Standardize file names  
- [ ] Record any transformations in Curator Log


## **EVALUATE Step**


### Essential Tasks

- [ ] Test that files successfully download 
- [ ] Check that any transformations didn't introduce problems 
- [ ] Review final state of data and record with researcher before publication 
- [ ] Add any final changes to Curator Log  

### FAIR evaluation

Findable:  
- [ ] Metadata exceeds researcher/ title/ date.  
- [ ] There is a unique Persistent ID (DOI, Handle, PURL, etc.).  
- [ ] Data/record is discoverable via web search engines.

Accessible:  
- [ ] Data/ record are retrievable via a standard protocol (e.g., HTTP).  
- [ ] Data/ record are free, open (e.g., via a download link).

Interoperable:
- [ ] Metadata is formatted in a standard schema (e.g., Dublin Core).  Metadata is provided in machine-readable format (OAI feed). 

Reusable:
- [ ] Data include sufficient metadata and supporting documentation about the data characteristics for reuse. 
- [ ] A way to contact the researcher directly for further questions is provided 
- [ ] There are clear indicators of who created, owns, and stewards the data. 
- [ ] Data are released with clear data usage terms (e.g., a CC License).


## **DOCUMENT Step**

### Essential Tasks

- [ ] Ensure the following information is captured in the Curator Log: 
  - [ ] Activities taken during the CURATE process 
  - [ ] Accessioning & deposit records (Names, dates, contact information, submission agreements, etc.) 
    > - Initial deposit to draft state is to test the import and check expected files are imported
    > - The Jupyter notebook is then tested and adjusted to work with the data in the draft state

  - [ ] Repository collection metadata 
  - [ ] Provenance logs (changes by curators in the Transform step) 
  - [ ] Service workflow 
  - [ ] Correspondences and other interactions 
  - [ ] Preservation packaging 
  - [ ] Any additional requirements at your institution