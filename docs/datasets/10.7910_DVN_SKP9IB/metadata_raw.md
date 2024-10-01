---
sidebar_position: 2
---

# Metadata.json

This file contains the metadata details (citation, code book, and data dictionary) for the dataset. This metadata can be exported in additional standard formats via the dataset repository.

```json title="data/reference/dvDatasetMetadata.json" showLineNumbers
{
  "about": "This document describes the dataset and mainly focuses on the dataset files and data variables for validation purposes prior to publication. The files within the dataset are described in detail within this document. The `objDATASET_INIT` variable contains the generalized metadata to initialize this dataset in the Dataverse (this is the JSON format expected by the Dataverse API).",
  "objDATASET_INIT": {
    "license": {
      "name": "CC0 1.0",
      "uri": "http://creativecommons.org/publicdomain/zero/1.0"
    },
    "metadataBlocks": {
      "citation": {
        "displayName": "Citation Metadata",
        "fields": [
          {
            "typeName": "title",
            "multiple": false,
            "typeClass": "primitive",
            "value": "Development of an AI/ML-ready knee ultrasound dataset in a population-based cohort"
          },
          {
            "typeName": "alternativeURL",
            "multiple": false,
            "typeClass": "primitive",
            "value": "https://jocoknow.vercel.app/docs/datasets/10.7910_DVN_SKP9IB/"
          },
          {
            "typeName": "author",
            "multiple": true,
            "typeClass": "compound",
            "value": [
              {
                "authorName": {
                  "typeName": "authorName",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "Nelson, Amanda"
                },
                "authorAffiliation": {
                  "typeName": "authorAffiliation",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "University of North Carolina at Chapel Hill"
                },
                "authorIdentifierScheme": {
                  "typeName": "authorIdentifierScheme",
                  "multiple": false,
                  "typeClass": "controlledVocabulary",
                  "value": "ORCID"
                },
                "authorIdentifier": {
                  "typeName": "authorIdentifier",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "0000-0002-9344-7877"
                }
              }
            ]
          },
          {
            "typeName": "datasetContact",
            "multiple": true,
            "typeClass": "compound",
            "value": [
              {
                "datasetContactName": {
                  "typeName": "datasetContactName",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "Gale, William"
                },
                "datasetContactAffiliation": {
                  "typeName": "datasetContactAffiliation",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "University of North Carolina at Chapel Hill"
                },
                "datasetContactEmail": {
                  "typeName": "datasetContactEmail",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "w.patrick.gale@unc.edu"
                }
              }
            ]
          },
          {
            "typeName": "dsDescription",
            "multiple": true,
            "typeClass": "compound",
            "value": [
              {
                "dsDescriptionValue": {
                  "typeName": "dsDescriptionValue",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "<h1>About this data</h1>An ultrasound dataset to use in the discovery of ultrasound features associated with pain and radiographic change in KOA is highly innovative and will be a major step forward for the field. These ultrasound images originate from the diverse and inclusive population-based Johnston County Health Study (JoCoHS). This dataset is designed to adhere to FAIR principles and was funded in part by an Administrative Supplement to Improve the AI/ML-Readiness of NIH-Supported Data (3R01AR077060-03S1)."
                },
                "dsDescriptionDate": {
                  "typeName": "dsDescriptionDate",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "2024-09-16"
                }
              },
              {
                "dsDescriptionValue": {
                  "typeName": "dsDescriptionValue",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "<h2>To begin learning about this dataset, visit our <a href='https://jocoknow.vercel.app/docs/datasets/10.7910_DVN_SKP9IB/overview.mdx' target='_blank'>User Guide</a> for an all-in-one document containing statistics and other details to help you work with the data.</h2>"
                },
                "dsDescriptionDate": {
                  "typeName": "dsDescriptionDate",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "2024-09-16"
                }
              }
            ]
          },
          {
            "typeName": "subject",
            "multiple": true,
            "typeClass": "controlledVocabulary",
            "value": [
              "Medicine, Health and Life Sciences"
            ]
          },
          {
            "typeName": "keyword",
            "multiple": true,
            "typeClass": "compound",
            "value": [
              {
                "keywordValue": {
                  "typeName": "keywordValue",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "Body Part"
                },
                "keywordVocabulary": {
                  "typeName": "keywordVocabulary",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "NCIT"
                },
                "keywordVocabularyURI": {
                  "typeName": "keywordVocabularyURI",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C32221"
                }
              },
              {
                "keywordValue": {
                  "typeName": "keywordValue",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "Electronic File Name"
                },
                "keywordVocabulary": {
                  "typeName": "keywordVocabulary",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "NCIT"
                },
                "keywordVocabularyURI": {
                  "typeName": "keywordVocabularyURI",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C171191"
                }
              },
              {
                "keywordValue": {
                  "typeName": "keywordValue",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "Age"
                },
                "keywordVocabulary": {
                  "typeName": "keywordVocabulary",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "NCIT"
                },
                "keywordVocabularyURI": {
                  "typeName": "keywordVocabularyURI",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C25150"
                }
              },
              {
                "keywordValue": {
                  "typeName": "keywordValue",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "Gender"
                },
                "keywordVocabulary": {
                  "typeName": "keywordVocabulary",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "NCIT"
                },
                "keywordVocabularyURI": {
                  "typeName": "keywordVocabularyURI",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C17357"
                }
              },
              {
                "keywordValue": {
                  "typeName": "keywordValue",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "Side"
                },
                "keywordVocabulary": {
                  "typeName": "keywordVocabulary",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "NCIT"
                },
                "keywordVocabularyURI": {
                  "typeName": "keywordVocabularyURI",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C25306"
                }
              },
              {
                "keywordValue": {
                  "typeName": "keywordValue",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "Study Subject Radiography Report"
                },
                "keywordVocabulary": {
                  "typeName": "keywordVocabulary",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "NCIT"
                },
                "keywordVocabularyURI": {
                  "typeName": "keywordVocabularyURI",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C115514"
                }
              },
              {
                "keywordValue": {
                  "typeName": "keywordValue",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "Knee pain (finding)"
                },
                "keywordVocabulary": {
                  "typeName": "keywordVocabulary",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "SNOMED-CT"
                },
                "keywordVocabularyURI": {
                  "typeName": "keywordVocabularyURI",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "https://phinvads.cdc.gov/vads/ViewCodeSystemConcept.action?oid=2.16.840.1.113883.6.96&code=30989003"
                }
              },
              {
                "keywordValue": {
                  "typeName": "keywordValue",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "Ultrasonography"
                },
                "keywordVocabulary": {
                  "typeName": "keywordVocabulary",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "MeSH"
                },
                "keywordVocabularyURI": {
                  "typeName": "keywordVocabularyURI",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "https://www.ncbi.nlm.nih.gov/mesh/68014463"
                }
              },
              {
                "keywordValue": {
                  "typeName": "keywordValue",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "Artificial Intelligence"
                },
                "keywordVocabulary": {
                  "typeName": "keywordVocabulary",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "MeSH"
                },
                "keywordVocabularyURI": {
                  "typeName": "keywordVocabularyURI",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "https://www.ncbi.nlm.nih.gov/mesh/68001185"
                }
              }
            ]
          },
          {
            "typeName": "publication",
            "multiple": true,
            "typeClass": "compound",
            "value": [
              {
                "publicationCitation": {
                  "typeName": "publicationCitation",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "Yerich NV, Alvarez C, Schwartz TA, Savage-Guin S, Renner JB, Bakewell CJ, Kohler MJ, Lin J, Samuels J, Nelson AE. A Standardized, Pragmatic Approach to Knee Ultrasound for Clinical Research in Osteoarthritis: The Johnston County Osteoarthritis Project. ACR Open Rheumatol. 2020 Jul;2(7):438-448. doi: 10.1002/acr2.11159. PMID: 32597564; PMCID: PMC7368135."
                },
                "publicationIDType": {
                  "typeName": "publicationIDType",
                  "multiple": false,
                  "typeClass": "controlledVocabulary",
                  "value": "pmid"
                },
                "publicationIDNumber": {
                  "typeName": "publicationIDNumber",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "32597564"
                },
                "publicationURL": {
                  "typeName": "publicationURL",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "https://doi.org/10.1002/acr2.11159"
                }
              }
            ]
          },
          {
            "typeName": "language",
            "multiple": true,
            "typeClass": "controlledVocabulary",
            "value": [
              "English"
            ]
          },
          {
            "typeName": "grantNumber",
            "multiple": true,
            "typeClass": "compound",
            "value": [
              {
                "grantNumberAgency": {
                  "typeName": "grantNumberAgency",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "NIAMS"
                },
                "grantNumberValue": {
                  "typeName": "grantNumberValue",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "3R01AR077060-03S1"
                }
              }
            ]
          },
          {
            "typeName": "depositor",
            "multiple": false,
            "typeClass": "primitive",
            "value": "Gale, William"
          },
          {
            "typeName": "dateOfDeposit",
            "multiple": false,
            "typeClass": "primitive",
            "value": "2024-09-16"
          },
          {
            "typeName": "dateOfCollection",
            "multiple": true,
            "typeClass": "compound",
            "value": [
              {
                "dateOfCollectionStart": {
                  "typeName": "dateOfCollectionStart",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "2019-03-14"
                },
                "dateOfCollectionEnd": {
                  "typeName": "dateOfCollectionEnd",
                  "multiple": false,
                  "typeClass": "primitive",
                  "value": "2024-06-01"
                }
              }
            ]
          },
          {
            "typeName": "kindOfData",
            "multiple": true,
            "typeClass": "primitive",
            "value": [
              "survey data",
              "clinic data"
            ]
          },
          {
            "typeName": "otherReferences",
            "multiple": true,
            "typeClass": "primitive",
            "value": [
              "Internal reference project #356-dp"
            ]
          }
        ]
      }
    }
  },
  "softwareUsed": [
    "Qualtrics survey platform",
    "MySQL database",
    "Docker Desktop",
    "Jupyter notebook",
    "Python"
  ],
  "files": [
    {
      "strFileName": "dataTable.SUBJECT.csv",
      "type": "application/octet-stream",
      "format": "comma separated value",
      "strDirectoryLabel": "data/reference",
      "strDataDescription": "This is the first file generated for this dataset and contains the participant/subject reference IDs, basic subject demographics, PA knee KL grades and reported pain in knees.",
      "lstCatgories": [
        "data",
        "reference"
      ],
      "variables": [
        {
          "name": "E03SUBJECTID",
          "label": "A unique identifier for a subject in a study.",
          "value": {
            "format": "Universal Unique Identifier (UUID version 1) generated according to RFC 4122",
            "dataType": "object",
            "unique": "True"
          },
          "identifier": "True",
          "ontology": {
            "source": [
              "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C69256"
            ]
          }
        },
        {
          "name": "E03GENDER",
          "label": "What was your gender at birth?",
          "value": {
            "format": "categorical",
            "dataType": "Int64",
            "unique": "False",
            "category": {
              "1": "Male",
              "2": "Female"
            }
          },
          "ontology": {
            "source": [
              "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C164527"
            ]
          }
        },
        {
          "name": "E03PASKR",
          "surveyQuestion": "On MOST days of ANY ONE MONTH in the LAST 12 MONTHS did you have pain, aching, or stiffness in any of the following? Please rate as none, mild, moderate, or severe. - Right - Knee",
          "label": "Right Knee - pain, aching, or stiffness",
          "source": "Qualtrics survey (1h2J)",
          "value": {
            "format": "categorical",
            "dataType": "Int64",
            "unique": "False",
            "category": {
              "0": "None",
              "1": "Mild",
              "2": "Moderate",
              "3": "Severe",
              "888": "No response"
            }
          },
          "ontology": {
            "source": [
              "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C125625",
              "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C125623",
              "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C105779",
              "https://phinvads.cdc.gov/vads/ViewCodeSystemConcept.action?oid=2.16.840.1.113883.6.96&code=249913002",
              "https://phinvads.cdc.gov/vads/ViewCodeSystemConcept.action?oid=2.16.840.1.113883.6.96&code=30989003"
            ]
          }
        },
        {
          "name": "E03PASKL",
          "surveyQuestion": "On MOST days of ANY ONE MONTH in the LAST 12 MONTHS did you have pain, aching, or stiffness in any of the following? Please rate as none, mild, moderate, or severe. - Left - Knee",
          "label": "Left Knee - pain, aching, or stiffness",
          "source": "Qualtrics survey (1h2J)",
          "value": {
            "format": "categorical",
            "dataType": "Int64",
            "unique": "False",
            "category": {
              "0": "None",
              "1": "Mild",
              "2": "Moderate",
              "3": "Severe",
              "888": "No response"
            }
          },
          "ontology": {
            "source": [
              "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C125625",
              "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C125623",
              "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C105779",
              "https://phinvads.cdc.gov/vads/ViewCodeSystemConcept.action?oid=2.16.840.1.113883.6.96&code=249913002",
              "https://phinvads.cdc.gov/vads/ViewCodeSystemConcept.action?oid=2.16.840.1.113883.6.96&code=30989003"
            ]
          }
        },
        {
          "name": "E03RADRPAKKL",
          "label": "Kellgren-Lawrence (KL) Grade read from right PA knee radiograph",
          "value": {
            "format": "categorical",
            "dataType": "Int64",
            "unique": "False",
            "category": {
              "0": "No OA",
              "1": "Questionable OA",
              "2": "Mild OA",
              "3": "Moderate OA",
              "4": "Severe OA",
              "9": "Non OA",
              "88": "Not read",
              "99": "Total joint replacement"
            }
          },
          "ontology": {
            "source": [
              "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C115514"
            ]
          }
        },
        {
          "name": "E03RADLPAKKL",
          "label": "Kellgren-Lawrence (KL) Grade read from left PA knee radiograph",
          "value": {
            "format": "categorical",
            "dataType": "Int64",
            "unique": "False",
            "category": {
              "0": "No OA",
              "1": "Questionable OA",
              "2": "Mild OA",
              "3": "Moderate OA",
              "4": "Severe OA",
              "9": "Non OA",
              "88": "Not read",
              "99": "Total joint replacement"
            }
          },
          "ontology": {
            "source": [
              "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C115514"
            ]
          }
        },
        {
          "name": "E03AGE",
          "label": "Age range (in years) at time of JoCoHS enrollment",
          "value": {
            "format": "categorical",
            "unitOfMeasure": "year",
            "dataType": "Int64",
            "unique": "False",
            "category": {
              "1": "35-39",
              "2": "40-44",
              "3": "45-49",
              "4": "50-54",
              "5": "55-59",
              "6": "60-64",
              "7": "65-70"
            }
          },
          "ontology": {
            "source": [
              "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C69260"
            ]
          }
        }
      ]
    },
    {
      "strFileName": "dataTable.IMAGE_REF.csv",
      "type": "application/octet-stream",
      "format": "comma separated value",
      "tarcInternalReference": "ds1457",
      "strDataDescription": "This file contains the ultrasound image metadata. Use this file to determine the number of ultrasound image types available, file sizes, and references to the files found in the ancillary image archives.",
      "lstCatgories": [
        "data",
        "reference"
      ],
      "detailedDescription": "",
      "strDirectoryLabel": "data/reference",
      "variables": [
        {
          "name": "E03SUBJECTID",
          "label": "A unique identifier for a subject in a study.",
          "value": {
            "format": "Universal Unique Identifier (UUID version 1) generated according to RFC 4122",
            "dataType": "object",
            "unique": "True"
          },
          "identifier": "True",
          "ontology": {
            "source": [
              "https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C69256"
            ]
          }
        },
        {
          "name": "E03USIMGT",
          "label": "Knee ultrasound image type",
          "value": {
            "format": "categorical",
            "dataType": "Int64",
            "unique": "False",
            "category": {
              "11": "Right SUPRAPAT LONG",
              "12": "Right SUPRAPAT LONG CPD",
              "13": "Right SUPRAPAT TRANS 30",
              "14": "Right MED LONG",
              "15": "Right LAT LONG",
              "16": "Right SUPRAPAT TRANS FLEX",
              "17": "Right POST TRANS",
              "21": "Left SUPRAPAT LONG",
              "22": "Left SUPRAPAT LONG CPD",
              "23": "Left SUPRAPAT TRANS 30",
              "24": "Left MED LONG",
              "25": "Left LAT LONG",
              "26": "Left SUPRAPAT TRANS FLEX",
              "27": "Left POST TRANS"
            }
          },
          "identifier": "False",
          "ontology": {
            "source": [
              "https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C32221"
            ]
          }
        },
        {
          "name": "E03USIMGF",
          "label": "Ultrasound image file name",
          "fileFormat": "PNG",
          "value": {
            "format": "Each filename contains the E03SUBJECTID and E03USIMGT value in the form of E03SUBJECTID+'_'+E03USIMGT+'.png'",
            "dataType": "string (42 character)"
          },
          "identifier": "False",
          "ontology": {
            "source": [
              "https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C171191"
            ]
          }
        },
        {
          "name": "E03USIMGZ",
          "label": "Ultrasound image file size in bytes",
          "value": {
            "format": "Int64",
            "unitOfMeasure": "byte",
            "dataType": "Int64"
          },
          "identifier": "False"
        },
        {
          "name": "E03USIMGD",
          "label": "Knee imaged (left or right knee)",
          "value": {
            "format": "categorical",
            "dataType": "Int64",
            "unique": "False",
            "category": {
              "1": "Right",
              "2": "Left"
            }
          },
          "identifier": "False",
          "ontology": {
            "source": [
              "https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&ns=ncit&code=C25306"
            ]
          }
        }
      ]
    },
    {
      "strFileName": "imageArchive.11.zip",
      "fileCount": 867,
      "strDirectoryLabel": "data/image/ultrasound",
      "strDataDescription": "This file contains an archive of Right SUPRAPAT LONG, ultrasound images (file count: 867). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
      "lstCatgories": [
        "data",
        "image"
      ]
    },
    {
      "strFileName": "imageArchive.12.zip",
      "fileCount": 867,
      "strDirectoryLabel": "data/image/ultrasound",
      "strDataDescription": "This file contains an archive of Right SUPRAPAT LONG CPD, ultrasound images (file count: 867). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
      "lstCatgories": [
        "data",
        "image"
      ]
    },
    {
      "strFileName": "imageArchive.13.zip",
      "fileCount": 866,
      "strDirectoryLabel": "data/image/ultrasound",
      "strDataDescription": "This file contains an archive of Right SUPRAPAT TRANS 30, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
      "lstCatgories": [
        "data",
        "image"
      ]
    },
    {
      "strFileName": "imageArchive.14.zip",
      "fileCount": 867,
      "strDirectoryLabel": "data/image/ultrasound",
      "strDataDescription": "This file contains an archive of Right MED LONG, ultrasound images (file count: 867). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
      "lstCatgories": [
        "data",
        "image"
      ]
    },
    {
      "strFileName": "imageArchive.15.zip",
      "fileCount": 867,
      "strDirectoryLabel": "data/image/ultrasound",
      "strDataDescription": "This file contains an archive of Right LAT LONG, ultrasound images (file count: 867). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
      "lstCatgories": [
        "data",
        "image"
      ]
    },
    {
      "strFileName": "imageArchive.16.zip",
      "fileCount": 865,
      "strDirectoryLabel": "data/image/ultrasound",
      "strDataDescription": "This file contains an archive of Right SUPRAPAT TRANS FLEX, ultrasound images (file count: 865). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
      "lstCatgories": [
        "data",
        "image"
      ]
    },
    {
      "strFileName": "imageArchive.17.zip",
      "fileCount": 835,
      "strDirectoryLabel": "data/image/ultrasound",
      "strDataDescription": "This file contains an archive of Right POST TRANS, ultrasound images (file count: 835). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
      "lstCatgories": [
        "data",
        "image"
      ]
    },
    {
      "strFileName": "imageArchive.21.zip",
      "fileCount": 866,
      "strDirectoryLabel": "data/image/ultrasound",
      "strDataDescription": "This file contains an archive of Left SUPRAPAT LONG, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
      "lstCatgories": [
        "data",
        "image"
      ]
    },
    {
      "strFileName": "imageArchive.22.zip",
      "fileCount": 866,
      "strDirectoryLabel": "data/image/ultrasound",
      "strDataDescription": "This file contains an archive of Left SUPRAPAT LONG CPD, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
      "lstCatgories": [
        "data",
        "image"
      ]
    },
    {
      "strFileName": "imageArchive.23.zip",
      "fileCount": 866,
      "strDirectoryLabel": "data/image/ultrasound",
      "strDataDescription": "This file contains an archive of Left SUPRAPAT TRANS 30, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
      "lstCatgories": [
        "data",
        "image"
      ]
    },
    {
      "strFileName": "imageArchive.24.zip",
      "fileCount": 866,
      "strDirectoryLabel": "data/image/ultrasound",
      "strDataDescription": "This file contains an archive of Left MED LONG, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
      "lstCatgories": [
        "data",
        "image"
      ]
    },
    {
      "strFileName": "imageArchive.25.zip",
      "fileCount": 866,
      "strDirectoryLabel": "data/image/ultrasound",
      "strDataDescription": "This file contains an archive of Left LAT LONG, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
      "lstCatgories": [
        "data",
        "image"
      ]
    },
    {
      "strFileName": "imageArchive.26.zip",
      "fileCount": 865,
      "strDirectoryLabel": "data/image/ultrasound",
      "strDataDescription": "This file contains an archive of Left SUPRAPAT TRANS FLEX, ultrasound images (file count: 865). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
      "lstCatgories": [
        "data",
        "image"
      ]
    },
    {
      "strFileName": "imageArchive.27.zip",
      "fileCount": 834,
      "strDirectoryLabel": "data/image/ultrasound",
      "strDataDescription": "This file contains an archive of Left POST TRANS, ultrasound images (file count: 834). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
      "lstCatgories": [
        "data",
        "image"
      ]
    },
    {
      "strFileName": "dvDatasetMetadata.json",
      "type": "application/octet-stream",
      "format": "JSON",
      "strDirectoryLabel": "data/reference",
      "lstCatgories": [
        "data",
        "reference"
      ],
      "strDataDescription": "This file contains metadata created BEFORE data was uploaded to the repository dataset to help describe the data we EXPECT to have uploaded to the dataset. This is file was created since the repository does not contain built-in tools to describe data files and variables in depth, which is needed to both document the data and perform validation. This file is used to validate and describe categorical variables within the data files."
    },
    {
      "strFileName": "README.notebook.public.ipynb",
      "type": "application/octet-stream",
      "format": "Jupyter notebook",
      "strDirectoryLabel": "code",
      "lstCatgories": [
        "code",
        "Jupyter",
        "notebook"
      ],
      "strDataDescription": "The purpose of this file is to provide documentation and preview of the data as a starting point for learning about the dataset. This notebook also provides instructions for running a virtual computing environment to further analyze the data and related metadata."
    },
    {
      "strFileName": "_notebook_worker.py",
      "type": "text/plain",
      "format": "Main script for the Jupyter notebook",
      "strDirectoryLabel": "code",
      "lstCatgories": [
        "code",
        "Jupyter",
        "notebook",
        "Python script"
      ],
      "strDataDescription": "The purpose of this file is to provide the scripts to help describe the dataset within the Jupyter notebook. This script does most of the work behind the scenes for the Jupyter notebook. This code is kept separate from the notebook to prevent the notebook from looking too bloated with code that some users may not be interested in, since one of the primary purposes of the notebook is to describe the dataset and not describe the code that generates the descriptive information. This script is only useful to those wanting to run the code within the Jupyter notebook."
    },
    {
      "strFileName": "_notebook_installer.py",
      "type": "text/plain",
      "format": "Script for installing packages needed in the Jupyter notebook",
      "strDirectoryLabel": "code",
      "lstCatgories": [
        "code",
        "Jupyter",
        "notebook",
        "Python script"
      ],
      "strDataDescription": "The purpose of this file is to install any Python modules used by the Jupyter notebook that are not included in the Jupyter environment by default. This script is only useful to those wanting to run the code within the Jupyter notebook."
    },
    {
      "strFileName": "_notebook.instructions.md",
      "type": "text/plain",
      "format": "Jupyter notebook usage instructions",
      "strDirectoryLabel": "code",
      "lstCatgories": [
        "code",
        "Jupyter",
        "Markdown"
      ],
      "strDataDescription": "This file is used with the README.notebook.public.ipynb and contains instructions on using the notebook."
    },
    {
      "strFileName": "_notebook.config.template.json",
      "type": "application/octet-stream",
      "format": "JSON",
      "strDirectoryLabel": "code",
      "lstCatgories": [
        "code",
        "json"
      ],
      "strDataDescription": "This file is used with the README.notebook.public.ipynb and contains the notebook variables."
    },
    {
      "strFileName": "example.us.image.png",
      "type": "application/octet-stream",
      "format": "Portable Network Graphics",
      "strDirectoryLabel": "data/image/example",
      "lstCatgories": [
        "data",
        "example"
      ],
      "strDataDescription": "This is an example ultrasound file that represents one of the images from the image archives and should not be used for analysis purposes. Images in this dataset are saved in lossless .png format."
    },
    {
      "strFileName": "curation_log.md",
      "type": "application/octet-stream",
      "format": "Markdown",
      "strDirectoryLabel": "documentation",
      "lstCatgories": [
        "curation"
      ],
      "strDataDescription": "This document contains the dataset curation checklist and notes regarding the considerations and steps taken to curate the data."
    }
  ],
  "objCitationSchema": {
    "title": {
      "properties": {
        "value": ""
      }
    },
    "grantNumber": {
      "properties": [
        {
          "grantNumberAgency": {
            "properties": {
              "value": ""
            }
          },
          "grantNumberValue": {
            "properties": {
              "value": ""
            }
          }
        }
      ]
    },
    "dsDescription": {
      "properties": [
        {
          "dsDescriptionValue": {
            "properties": {
              "value": ""
            }
          },
          "dsDescriptionDate": {
            "properties": {
              "value": ""
            }
          }
        }
      ]
    },
    "publication": {
      "properties": [
        {
          "publicationCitation": {
            "properties": {
              "value": ""
            }
          },
          "publicationIDType": {
            "properties": {
              "value": ""
            }
          },
          "publicationIDNumber": {
            "properties": {
              "value": ""
            }
          },
          "publicationURL": {
            "properties": {
              "value": ""
            }
          }
        }
      ]
    },
    "author": {
      "properties": [
        {
          "authorName": {
            "properties": {
              "value": ""
            }
          },
          "authorAffiliation": {
            "properties": {
              "value": ""
            }
          },
          "authorIdentifierScheme": {
            "properties": {
              "value": ""
            }
          },
          "authorIdentifier": {
            "properties": {
              "value": ""
            }
          }
        }
      ]
    },
    "dateOfCollection": {
      "properties": [
        {
          "dateOfCollectionStart": {
            "properties": {
              "value": ""
            }
          },
          "dateOfCollectionEnd": {
            "properties": {
              "value": ""
            }
          }
        }
      ]
    },
    "subject": {
      "properties": {
        "value": []
      }
    }
  }
}
```