
# README

This document aims to present the dataset in a format that is easily understandable for you, helping you gain insight into the dataset's contents.

## Citation metadata

### DOI - https://doi.org/10.7910/DVN/SKP9IB




### title



> Development of an AI/ML-ready knee ultrasound dataset in a population-based cohort



### grantNumber



> **grantNumberAgency:** NIAMS



> **grantNumberValue:** 3R01AR077060-03S1



### dsDescription



> **dsDescriptionValue:** <h1>About this data</h1>An ultrasound dataset to use in the discovery of ultrasound features associated with pain and radiographic change in KOA is highly innovative and will be a major step forward for the field. These ultrasound images originate from the diverse and inclusive population-based Johnston County Health Study (JoCoHS). This dataset is designed to adhere to FAIR principles and was funded in part by an Administrative Supplement to Improve the AI/ML-Readiness of NIH-Supported Data (3R01AR077060-03S1).



> **dsDescriptionDate:** 2024-09-16



> **dsDescriptionValue:** <h2>To begin learning about this dataset, visit our <a href='https://jocoknow.vercel.app/docs/datasets/10.7910_DVN_SKP9IB/' target='_blank'>User Guide</a> for an all-in-one document containing statistics and other details to help you work with the data.</h2>



> **dsDescriptionDate:** 2024-09-16



### publication



> **publicationCitation:** Yerich NV, Alvarez C, Schwartz TA, Savage-Guin S, Renner JB, Bakewell CJ, Kohler MJ, Lin J, Samuels J, Nelson AE. A Standardized, Pragmatic Approach to Knee Ultrasound for Clinical Research in Osteoarthritis: The Johnston County Osteoarthritis Project. ACR Open Rheumatol. 2020 Jul;2(7):438-448. doi: 10.1002/acr2.11159. PMID: 32597564; PMCID: PMC7368135.



> **publicationIDType:** pmid



> **publicationIDNumber:** 32597564



> **publicationURL:** https://doi.org/10.1002/acr2.11159



### author



> **authorName:** Nelson, Amanda



> **authorAffiliation:** University of North Carolina at Chapel Hill



> **authorIdentifierScheme:** ORCID



> **authorIdentifier:** 0000-0002-9344-7877



### dateOfCollection



> **dateOfCollectionStart:** 2019-03-14



> **dateOfCollectionEnd:** 2024-06-01



### subject



> Medicine, Health and Life Sciences



## Dataset files


    24 files currently in this dataset



|    | filename                       | directory             | categories                                       | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---:|:-------------------------------|:----------------------|:-------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | README.notebook.public.ipynb   | code                  | ['code', 'Jupyter', 'notebook']                  | The purpose of this file is to provide documentation and preview of the data as a starting point for learning about the dataset. This notebook also provides instructions for running a virtual computing environment to further analyze the data and related metadata.                                                                                                                                                                                                                                                                                                                  |
|  6 | _notebook.config.template.json | code                  | ['code', 'json']                                 | This file is used with the README.notebook.public.ipynb and contains the notebook variables.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|  3 | _notebook.instructions.md      | code                  | ['code', 'Jupyter', 'Markdown']                  | This file is used with the README.notebook.public.ipynb and contains instructions on using the notebook.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 22 | _notebook_installer.py         | code                  | ['code', 'Jupyter', 'notebook', 'Python script'] | The purpose of this file is to install any Python modules used by the Jupyter notebook that are not included in the Jupyter environment by default. This script is only useful to those wanting to run the code within the Jupyter notebook.                                                                                                                                                                                                                                                                                                                                             |
| 21 | _notebook_worker.py            | code                  | ['code', 'Jupyter', 'notebook', 'Python script'] | The purpose of this file is to provide the scripts to help describe the dataset within the Jupyter notebook. This script does most of the work behind the scenes for the Jupyter notebook. This code is kept separate from the notebook to prevent the notebook from looking too bloated with code that some users may not be interested in, since one of the primary purposes of the notebook is to describe the dataset and not describe the code that generates the descriptive information. This script is only useful to those wanting to run the code within the Jupyter notebook. |
|  1 | example.us.image.png           | data/image/example    | ['data', 'example']                              | This is an example ultrasound file that represents one of the images from the image archives and should not be used for analysis purposes. Images in this dataset are saved in lossless .png format.                                                                                                                                                                                                                                                                                                                                                                                     |
|  2 | imageArchive.11.zip            | data/image/ultrasound | ['data', 'image']                                | This file contains an archive of Right SUPRAPAT LONG, ultrasound images (file count: 867). There should only be one image per subject in this archive. Images are saved in lossless .png format.                                                                                                                                                                                                                                                                                                                                                                                         |
|  7 | imageArchive.12.zip            | data/image/ultrasound | ['data', 'image']                                | This file contains an archive of Right SUPRAPAT LONG CPD, ultrasound images (file count: 867). There should only be one image per subject in this archive. Images are saved in lossless .png format.                                                                                                                                                                                                                                                                                                                                                                                     |
|  8 | imageArchive.13.zip            | data/image/ultrasound | ['data', 'image']                                | This file contains an archive of Right SUPRAPAT TRANS 30, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.                                                                                                                                                                                                                                                                                                                                                                                     |
|  9 | imageArchive.14.zip            | data/image/ultrasound | ['data', 'image']                                | This file contains an archive of Right MED LONG, ultrasound images (file count: 867). There should only be one image per subject in this archive. Images are saved in lossless .png format.                                                                                                                                                                                                                                                                                                                                                                                              |
| 10 | imageArchive.15.zip            | data/image/ultrasound | ['data', 'image']                                | This file contains an archive of Right LAT LONG, ultrasound images (file count: 867). There should only be one image per subject in this archive. Images are saved in lossless .png format.                                                                                                                                                                                                                                                                                                                                                                                              |
| 13 | imageArchive.16.zip            | data/image/ultrasound | ['data', 'image']                                | This file contains an archive of Right SUPRAPAT TRANS FLEX, ultrasound images (file count: 865). There should only be one image per subject in this archive. Images are saved in lossless .png format.                                                                                                                                                                                                                                                                                                                                                                                   |
| 14 | imageArchive.17.zip            | data/image/ultrasound | ['data', 'image']                                | This file contains an archive of Right POST TRANS, ultrasound images (file count: 835). There should only be one image per subject in this archive. Images are saved in lossless .png format.                                                                                                                                                                                                                                                                                                                                                                                            |
| 11 | imageArchive.21.zip            | data/image/ultrasound | ['data', 'image']                                | This file contains an archive of Left SUPRAPAT LONG, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.                                                                                                                                                                                                                                                                                                                                                                                          |
| 16 | imageArchive.22.zip            | data/image/ultrasound | ['data', 'image']                                | This file contains an archive of Left SUPRAPAT LONG CPD, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.                                                                                                                                                                                                                                                                                                                                                                                      |
| 12 | imageArchive.23.zip            | data/image/ultrasound | ['data', 'image']                                | This file contains an archive of Left SUPRAPAT TRANS 30, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.                                                                                                                                                                                                                                                                                                                                                                                      |
| 17 | imageArchive.24.zip            | data/image/ultrasound | ['data', 'image']                                | This file contains an archive of Left MED LONG, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.                                                                                                                                                                                                                                                                                                                                                                                               |
| 18 | imageArchive.25.zip            | data/image/ultrasound | ['data', 'image']                                | This file contains an archive of Left LAT LONG, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.                                                                                                                                                                                                                                                                                                                                                                                               |
| 19 | imageArchive.26.zip            | data/image/ultrasound | ['data', 'image']                                | This file contains an archive of Left SUPRAPAT TRANS FLEX, ultrasound images (file count: 865). There should only be one image per subject in this archive. Images are saved in lossless .png format.                                                                                                                                                                                                                                                                                                                                                                                    |
| 15 | imageArchive.27.zip            | data/image/ultrasound | ['data', 'image']                                | This file contains an archive of Left POST TRANS, ultrasound images (file count: 834). There should only be one image per subject in this archive. Images are saved in lossless .png format.                                                                                                                                                                                                                                                                                                                                                                                             |
|  5 | dataTable.IMAGE_REF.tab        | data/reference        | ['data', 'reference']                            | This file contains the ultrasound image metadata. Use this file to determine the number of ultrasound image types available, file sizes, and references to the files found in the ancillary image archives.                                                                                                                                                                                                                                                                                                                                                                              |
|  4 | dataTable.SUBJECT.tab          | data/reference        | ['data', 'reference']                            | This is the first file generated for this dataset and contains the participant/subject reference IDs, basic subject demographics, PA knee KL grades and reported pain in knees.                                                                                                                                                                                                                                                                                                                                                                                                          |
| 20 | dvDatasetMetadata.json         | data/reference        | ['data', 'reference']                            | This file contains metadata created BEFORE data was uploaded to the repository dataset to help describe the data we EXPECT to have uploaded to the dataset. This is file was created since the repository does not contain built-in tools to describe data files and variables in depth, which is needed to both document the data and perform validation. This file is used to validate and describe categorical variables within the data files.                                                                                                                                       |
| 23 | curation_log.md                | documentation         | ['curation']                                     | This document contains the dataset curation checklist and notes regarding the considerations and steps taken to curate the data.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |


    24 files EXPECTED in this dataset



## Datatable preview for dataTable.SUBJECT.csv



|    | E03SUBJECTID                         | E03GENDER   | E03PASKR   | E03PASKL   | E03RADRPAKKL    | E03RADLPAKKL    | E03AGE   |
|---:|:-------------------------------------|:------------|:-----------|:-----------|:----------------|:----------------|:---------|
|  0 | 72bb0a51-f020-11ed-b527-0a580a5f736a | Female      | Moderate   | None       | Moderate OA     | Moderate OA     | 50-54    |
|  1 | 72bb0a76-f020-11ed-b527-0a580a5f736a | Female      | Severe     | None       | Mild OA         | nan             | 60-64    |
|  2 | 72bb0a8a-f020-11ed-b527-0a580a5f736a | Female      | Moderate   | Moderate   | Questionable OA | Mild OA         | 65-70    |
|  3 | 72bb0a99-f020-11ed-b527-0a580a5f736a | Female      | None       | Mild       | No OA           | Questionable OA | 45-49    |
|  4 | 72bb0ab5-f020-11ed-b527-0a580a5f736a | Male        | None       | None       | Questionable OA | Mild OA         | 40-44    |



## General statistics for file dataTable.SUBJECT.csv



### E03GENDER



|    | category   |   counts |
|---:|:-----------|---------:|
|  0 | Female     |      587 |
|  1 | Male       |      294 |



### E03PASKR



|    | category    |   counts |
|---:|:------------|---------:|
|  0 | None        |      399 |
|  1 | Mild        |      196 |
|  2 | Moderate    |      181 |
|  3 | Severe      |      103 |
|  4 | No response |        2 |



### E03PASKL



|    | category    |   counts |
|---:|:------------|---------:|
|  0 | None        |      448 |
|  1 | Moderate    |      168 |
|  2 | Mild        |      168 |
|  3 | Severe      |       95 |
|  4 | No response |        2 |



### E03RADRPAKKL



|    | category                |   counts |
|---:|:------------------------|---------:|
|  0 | No OA                   |      303 |
|  1 | Questionable OA         |      290 |
|  2 | Mild OA                 |      119 |
|  3 | Moderate OA             |       89 |
|  4 | Severe OA               |       63 |
|  5 | Total joint replacement |        2 |



### E03RADLPAKKL



|    | category                |   counts |
|---:|:------------------------|---------:|
|  0 | No OA                   |      339 |
|  1 | Questionable OA         |      262 |
|  2 | Mild OA                 |      120 |
|  3 | Moderate OA             |       87 |
|  4 | Severe OA               |       55 |
|  5 | Total joint replacement |        3 |



### E03AGE



|    | category   |   counts |
|---:|:-----------|---------:|
|  0 | 65-70      |      171 |
|  1 | 60-64      |      153 |
|  2 | 55-59      |      149 |
|  3 | 50-54      |      144 |
|  4 | 40-44      |      104 |
|  5 | 45-49      |      102 |
|  6 | 35-39      |       58 |



## Datatable preview for dataTable.IMAGE_REF.csv



|    | E03SUBJECTID                         | E03USIMGT              | E03USIMGF                                   |   E03USIMGZ | E03USIMGD   |
|---:|:-------------------------------------|:-----------------------|:--------------------------------------------|------------:|:------------|
|  0 | 72bb0a51-f020-11ed-b527-0a580a5f736a | Left SUPRAPAT LONG     | 72bb0a51-f020-11ed-b527-0a580a5f736a_21.png |      132460 | Left        |
|  1 | 72bb0a51-f020-11ed-b527-0a580a5f736a | Left SUPRAPAT LONG CPD | 72bb0a51-f020-11ed-b527-0a580a5f736a_22.png |      154179 | Left        |
|  2 | 72bb0a51-f020-11ed-b527-0a580a5f736a | Left SUPRAPAT TRANS 30 | 72bb0a51-f020-11ed-b527-0a580a5f736a_23.png |      133222 | Left        |
|  3 | 72bb0a51-f020-11ed-b527-0a580a5f736a | Left MED LONG          | 72bb0a51-f020-11ed-b527-0a580a5f736a_24.png |      121758 | Left        |
|  4 | 72bb0a51-f020-11ed-b527-0a580a5f736a | Left LAT LONG          | 72bb0a51-f020-11ed-b527-0a580a5f736a_25.png |      108043 | Left        |



## General statistics for file dataTable.IMAGE_REF.csv



### E03USIMGT



|    | category                  |   counts |
|---:|:--------------------------|---------:|
|  0 | Right SUPRAPAT LONG       |      867 |
|  1 | Right SUPRAPAT LONG CPD   |      867 |
|  2 | Right LAT LONG            |      867 |
|  3 | Right MED LONG            |      867 |
|  4 | Left SUPRAPAT LONG        |      866 |
|  5 | Left SUPRAPAT LONG CPD    |      866 |
|  6 | Left SUPRAPAT TRANS 30    |      866 |
|  7 | Left MED LONG             |      866 |
|  8 | Left LAT LONG             |      866 |
|  9 | Right SUPRAPAT TRANS 30   |      866 |
| 10 | Left SUPRAPAT TRANS FLEX  |      865 |
| 11 | Right SUPRAPAT TRANS FLEX |      865 |
| 12 | Right POST TRANS          |      835 |
| 13 | Left POST TRANS           |      834 |



### E03USIMGD



|    | category   |   counts |
|---:|:-----------|---------:|
|  0 | Right      |     6034 |
|  1 | Left       |     6029 |
