---
sidebar_position: 2
---

# Metadata.json

This file contains the metadata details (citation, code book, and data dictionary) for the dataset as well as an embedded JSON schema `@DocumentSchema` to describe the JSON properties. This metadata can be exported in additional standard formats via the dataset repository. This is a long document.

```json title="data/reference/dvDatasetMetadata.json" showLineNumbers
{
    "about": "see the @DocumentSchema property for embedded schema information about this file",
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
                                    "value": "<h1>About the data</h1>An ultrasound dataset to use in the discovery of ultrasound features associated with pain and radiographic change in KOA is highly innovative and will be a major step forward for the field. These ultrasound images originate from the diverse and inclusive population-based Johnston County Health Study (JoCoHS). This dataset is designed to adhere to FAIR principles and was funded in part by an Administrative Supplement to Improve the AI/ML-Readiness of NIH-Supported Data (3R01AR077060-03S1)."
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
                                    "value": "<h2>To begin learning about the dataset, visit our <a href='https://jocoknow.vercel.app/docs/datasets/10.7910_DVN_SKP9IB/overview' target='_blank'>User Guide</a> for an all-in-one document containing statistics and other details to help you work with the data.</h2>"
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
                                "grantNumberValue": {
                                    "typeName": "grantNumberValue",
                                    "multiple": false,
                                    "typeClass": "primitive",
                                    "value": "R01AR077060"
                                }
                            },
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
                    "label": "Right Knee - pain, aching, or stiffness on MOST days of ANY ONE MONTH in the LAST 12 MONTHS",
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
                    "label": "Left Knee - pain, aching, or stiffness on MOST days of ANY ONE MONTH in the LAST 12 MONTHS",
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
                    "label": "Age categorized in 5-year increments at time of JoCoHS enrollment",
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
                            "11": "Right Anterior suprapatellar longitudinal",
                            "12": "Right Anterior suprapatellar longitudinal with power Doppler",
                            "13": "Right Anterior suprapatellar transverse in 30 degrees flexion",
                            "14": "Right Medial longitudinal",
                            "15": "Right Lateral longitudinal",
                            "16": "Right Anterior suprapatellar transverse in maximal flexion",
                            "17": "Right Posterior medial transverse",
                            "21": "Left Anterior suprapatellar longitudinal",
                            "22": "Left Anterior suprapatellar longitudinal with power Doppler",
                            "23": "Left Anterior suprapatellar transverse in 30 degrees flexion",
                            "24": "Left Medial longitudinal",
                            "25": "Left Lateral longitudinal",
                            "26": "Left Anterior suprapatellar transverse in maximal flexion",
                            "27": "Left Posterior medial transverse"
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
                    "label": "Knee imaged - left or right knee",
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
            "strDataDescription": "This file contains an archive of Right Anterior suprapatellar longitudinal, ultrasound images (file count: 867). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
            "lstCatgories": [
                "data",
                "image"
            ]
        },
        {
            "strFileName": "imageArchive.12.zip",
            "fileCount": 867,
            "strDirectoryLabel": "data/image/ultrasound",
            "strDataDescription": "This file contains an archive of Right Anterior suprapatellar longitudinal with power Doppler, ultrasound images (file count: 867). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
            "lstCatgories": [
                "data",
                "image"
            ]
        },
        {
            "strFileName": "imageArchive.13.zip",
            "fileCount": 866,
            "strDirectoryLabel": "data/image/ultrasound",
            "strDataDescription": "This file contains an archive of Right Anterior suprapatellar transverse in 30 degrees flexion, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
            "lstCatgories": [
                "data",
                "image"
            ]
        },
        {
            "strFileName": "imageArchive.14.zip",
            "fileCount": 867,
            "strDirectoryLabel": "data/image/ultrasound",
            "strDataDescription": "This file contains an archive of Right Medial longitudinal, ultrasound images (file count: 867). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
            "lstCatgories": [
                "data",
                "image"
            ]
        },
        {
            "strFileName": "imageArchive.15.zip",
            "fileCount": 867,
            "strDirectoryLabel": "data/image/ultrasound",
            "strDataDescription": "This file contains an archive of Right Lateral longitudinal, ultrasound images (file count: 867). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
            "lstCatgories": [
                "data",
                "image"
            ]
        },
        {
            "strFileName": "imageArchive.16.zip",
            "fileCount": 865,
            "strDirectoryLabel": "data/image/ultrasound",
            "strDataDescription": "This file contains an archive of Right Anterior suprapatellar transverse in maximal flexion, ultrasound images (file count: 865). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
            "lstCatgories": [
                "data",
                "image"
            ]
        },
        {
            "strFileName": "imageArchive.17.zip",
            "fileCount": 835,
            "strDirectoryLabel": "data/image/ultrasound",
            "strDataDescription": "This file contains an archive of Right Posterior medial transverse, ultrasound images (file count: 835). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
            "lstCatgories": [
                "data",
                "image"
            ]
        },
        {
            "strFileName": "imageArchive.21.zip",
            "fileCount": 866,
            "strDirectoryLabel": "data/image/ultrasound",
            "strDataDescription": "This file contains an archive of Left Anterior suprapatellar longitudinal, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
            "lstCatgories": [
                "data",
                "image"
            ]
        },
        {
            "strFileName": "imageArchive.22.zip",
            "fileCount": 866,
            "strDirectoryLabel": "data/image/ultrasound",
            "strDataDescription": "This file contains an archive of Left Anterior suprapatellar longitudinal with power Doppler, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
            "lstCatgories": [
                "data",
                "image"
            ]
        },
        {
            "strFileName": "imageArchive.23.zip",
            "fileCount": 866,
            "strDirectoryLabel": "data/image/ultrasound",
            "strDataDescription": "This file contains an archive of Left Anterior suprapatellar transverse in 30 degrees flexion, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
            "lstCatgories": [
                "data",
                "image"
            ]
        },
        {
            "strFileName": "imageArchive.24.zip",
            "fileCount": 866,
            "strDirectoryLabel": "data/image/ultrasound",
            "strDataDescription": "This file contains an archive of Left Medial longitudinal, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
            "lstCatgories": [
                "data",
                "image"
            ]
        },
        {
            "strFileName": "imageArchive.25.zip",
            "fileCount": 866,
            "strDirectoryLabel": "data/image/ultrasound",
            "strDataDescription": "This file contains an archive of Left Lateral longitudinal, ultrasound images (file count: 866). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
            "lstCatgories": [
                "data",
                "image"
            ]
        },
        {
            "strFileName": "imageArchive.26.zip",
            "fileCount": 865,
            "strDirectoryLabel": "data/image/ultrasound",
            "strDataDescription": "This file contains an archive of Left Anterior suprapatellar transverse in maximal flexion, ultrasound images (file count: 865). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
            "lstCatgories": [
                "data",
                "image"
            ]
        },
        {
            "strFileName": "imageArchive.27.zip",
            "fileCount": 834,
            "strDirectoryLabel": "data/image/ultrasound",
            "strDataDescription": "This file contains an archive of Left Posterior medial transverse, ultrasound images (file count: 834). There should only be one image per subject in this archive. Images are saved in lossless .png format.",
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
            "strDataDescription": "This file contains metadata created BEFORE data was uploaded to the repository dataset to help describe the data we EXPECT to have uploaded to the dataset. This is file was created since the repository does not contain built-in tools to describe data files and variables in depth, which is needed to both document the data and perform validation. This file is used to validate and describe categorical variables within the datatable files."
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
            "strDataDescription": "This file provides documentation describing the dataset and a preview of the data. This notebook also includes code to use as a dataset documenting framework for your own projects."
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
            "strDataDescription": "This file contains the scripts to help describe the dataset within the Jupyter Notebook. This script is ONLY useful to those wanting to run the code within the Jupyter Notebook. This code is kept separate from the Notebook to prevent the Notebook becoming bloated with code."
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
            "strDataDescription": "This file is used with the README.notebook.public.ipynb and contains the notebook variables. It also contains an embedded schema to describe/validate the JSON config."
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
        },
        {
            "strFileName": "README.md",
            "type": "application/octet-stream",
            "format": "Markdown",
            "strDirectoryLabel": "documentation",
            "lstCatgories": [
                "README"
            ],
            "strDataDescription": "This document contains an overview of the dataset and is a good starting point to understanding the data."
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
    },
    "@DocumentSchema": {
        "$schema": "http://json-schema.org/schema#",
        "title": "Dataset Metadata",
        "description": "This object is the schema for this document. This file contains metadata created BEFORE data was uploaded to the repository dataset to help describe the data we EXPECT to have uploaded to the dataset. This document describes the dataset and mainly focuses on the dataset files and data variables for validation purposes prior to publication. The files within the dataset are described in detail within this document.",
        "type": "object",
        "properties": {
            "about": {
                "description": "This property provides a reference to this schema used to validate and describe the document.",
                "type": "string"
            },
            "objDATASET_INIT": {
                "description": "This object contains the generalized metadata to initialize this dataset in the Dataverse (this is the JSON format expected by the Dataverse API).",
                "type": "object",
                "properties": {
                    "license": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "uri": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "name",
                            "uri"
                        ]
                    },
                    "metadataBlocks": {
                        "type": "object",
                        "properties": {
                            "citation": {
                                "type": "object",
                                "properties": {
                                    "displayName": {
                                        "type": "string"
                                    },
                                    "fields": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "typeName": {
                                                    "type": "string"
                                                },
                                                "multiple": {
                                                    "type": "boolean"
                                                },
                                                "typeClass": {
                                                    "type": "string"
                                                },
                                                "value": {
                                                    "anyOf": [
                                                        {
                                                            "type": "string"
                                                        },
                                                        {
                                                            "type": "array",
                                                            "items": {
                                                                "anyOf": [
                                                                    {
                                                                        "type": "string"
                                                                    },
                                                                    {
                                                                        "type": "object",
                                                                        "properties": {
                                                                            "authorName": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "authorAffiliation": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "authorIdentifierScheme": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "authorIdentifier": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "datasetContactName": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "datasetContactAffiliation": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "datasetContactEmail": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "dsDescriptionValue": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "dsDescriptionDate": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "keywordValue": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "keywordVocabulary": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "keywordVocabularyURI": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "publicationCitation": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "publicationIDType": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "publicationIDNumber": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "publicationURL": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "grantNumberAgency": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "grantNumberValue": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "dateOfCollectionStart": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            },
                                                                            "dateOfCollectionEnd": {
                                                                                "type": "object",
                                                                                "properties": {
                                                                                    "typeName": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "multiple": {
                                                                                        "type": "boolean"
                                                                                    },
                                                                                    "typeClass": {
                                                                                        "type": "string"
                                                                                    },
                                                                                    "value": {
                                                                                        "type": "string"
                                                                                    }
                                                                                },
                                                                                "required": [
                                                                                    "multiple",
                                                                                    "typeClass",
                                                                                    "typeName",
                                                                                    "value"
                                                                                ]
                                                                            }
                                                                        }
                                                                    }
                                                                ]
                                                            }
                                                        }
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "multiple",
                                                "typeClass",
                                                "typeName",
                                                "value"
                                            ]
                                        }
                                    }
                                },
                                "required": [
                                    "displayName",
                                    "fields"
                                ]
                            }
                        },
                        "required": [
                            "citation"
                        ]
                    }
                },
                "required": [
                    "license",
                    "metadataBlocks"
                ]
            },
            "softwareUsed": {
                "description": "Contains a simple list of software used for this project.",
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "files": {
                "description": "Listing of the files contained within this dataset.",
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "strFileName": {
                            "description":"The name of the file.",
                            "type": "string"
                        },
                        "type": {
                            "description":"A description of the file type used for HTTP requests.",
                            "type": "string"
                        },
                        "format": {
                            "description":"A description of the file type.",
                            "type": "string"
                        },
                        "strDirectoryLabel": {
                            "description":"This a tag used in the organizing of the file within the Dataverse dataset (can be thought of as both a tag and file directory).",
                            "type": "string"
                        },
                        "strDataDescription": {
                            "description":"A description of the file purpose.",
                            "type": "string"
                        },
                        "lstCatgories": {
                            "description":"Used in tagging or keywords for finding the file within the dataset.",
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "variables": {
                            "description":"Provides the list of variables or columns in a data table and the details about the variable.",
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {
                                        "description":"Variable name.",
                                        "type": "string"
                                    },
                                    "label": {
                                        "description":"A description of the variable.",
                                        "type": "string"
                                    },
                                    "value": {
                                        "description":"A description variable value.",
                                        "type": "object",
                                        "properties": {
                                            "format": {
                                                "description":"Expected format of the variable value (categorical or not).",
                                                "type": "string"
                                            },
                                            "dataType": {
                                                "description":"Python data type.",
                                                "type": "string"
                                            },
                                            "unique": {
                                                "description":"Boolean flag of whether the values are unique for each record or not.",
                                                "type": "string"
                                            },
                                            "category": {
                                                "description":"For categorical variables, this value lists the numeric values and their labels.",
                                                "type": "object",
                                                "patternProperties": {
                                                    "^.*$": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "unitOfMeasure": {
                                                "description":"Specifies the value unit of measure where applicable.",
                                                "type": "string"
                                            }
                                        },
                                        "required": [
                                            "format"
                                        ]
                                    },
                                    "identifier": {
                                        "description":"Specify if the value is an identifying field for the file.",
                                        "type": "string"
                                    },
                                    "ontology": {
                                        "description":"Lists any applicable meta thesaurus entries related to the variable.",
                                        "type": "object",
                                        "properties": {
                                            "source": {
                                                "description": "URI of meta thesaurus entries",
                                                "type": "array",
                                                "items": {
                                                    "type": "string"
                                                }
                                            }
                                        },
                                        "required": [
                                            "source"
                                        ]
                                    },
                                    "surveyQuestion": {
                                        "description":"If the value was derived from a survey question then this provides the question text.",
                                        "type": "string"
                                    },
                                    "source": {
                                        "description":"Specifies where the variable originates.",
                                        "type": "string"
                                    },
                                    "fileFormat": {
                                        "description":"If the variable references a file, specify the format of the file.",
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "label",
                                    "name",
                                    "value"
                                ]
                            }
                        },
                        "tarcInternalReference": {
                            "description":"References private (administrative) resources used by the file.",
                            "type": "string"
                        },
                        "fileCount": {
                            "description":"If the file is an archive of many files, this field specifies the file count of the archive.",
                            "type": "integer"
                        }
                    },
                    "required": [
                        "lstCatgories",
                        "strDataDescription",
                        "strDirectoryLabel",
                        "strFileName"
                    ]
                }
            },
            "objCitationSchema": {
                "description":"This object serves two purposes. First, this object is simply a reference to the Dataverse citation metadata values within the `['objDATASET_INIT']['metadataBlocks']['citation']['fields']` object. It lets our scripts know where the citation values are found for a given field. Secondly, it defines the order and citation fields we are interested in printing to the notebook.",
                "type": "object",
                "properties": {
                    "title": {
                        "type": "object",
                        "properties": {
                            "properties": {
                                "type": "object",
                                "properties": {
                                    "value": {
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "value"
                                ]
                            }
                        },
                        "required": [
                            "properties"
                        ]
                    },
                    "grantNumber": {
                        "type": "object",
                        "properties": {
                            "properties": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "grantNumberAgency": {
                                            "type": "object",
                                            "properties": {
                                                "properties": {
                                                    "type": "object",
                                                    "properties": {
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "value"
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "properties"
                                            ]
                                        },
                                        "grantNumberValue": {
                                            "type": "object",
                                            "properties": {
                                                "properties": {
                                                    "type": "object",
                                                    "properties": {
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "value"
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "properties"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "grantNumberAgency",
                                        "grantNumberValue"
                                    ]
                                }
                            }
                        },
                        "required": [
                            "properties"
                        ]
                    },
                    "dsDescription": {
                        "type": "object",
                        "properties": {
                            "properties": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "dsDescriptionValue": {
                                            "type": "object",
                                            "properties": {
                                                "properties": {
                                                    "type": "object",
                                                    "properties": {
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "value"
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "properties"
                                            ]
                                        },
                                        "dsDescriptionDate": {
                                            "type": "object",
                                            "properties": {
                                                "properties": {
                                                    "type": "object",
                                                    "properties": {
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "value"
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "properties"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "dsDescriptionDate",
                                        "dsDescriptionValue"
                                    ]
                                }
                            }
                        },
                        "required": [
                            "properties"
                        ]
                    },
                    "publication": {
                        "type": "object",
                        "properties": {
                            "properties": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "publicationCitation": {
                                            "type": "object",
                                            "properties": {
                                                "properties": {
                                                    "type": "object",
                                                    "properties": {
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "value"
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "properties"
                                            ]
                                        },
                                        "publicationIDType": {
                                            "type": "object",
                                            "properties": {
                                                "properties": {
                                                    "type": "object",
                                                    "properties": {
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "value"
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "properties"
                                            ]
                                        },
                                        "publicationIDNumber": {
                                            "type": "object",
                                            "properties": {
                                                "properties": {
                                                    "type": "object",
                                                    "properties": {
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "value"
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "properties"
                                            ]
                                        },
                                        "publicationURL": {
                                            "type": "object",
                                            "properties": {
                                                "properties": {
                                                    "type": "object",
                                                    "properties": {
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "value"
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "properties"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "publicationCitation",
                                        "publicationIDNumber",
                                        "publicationIDType",
                                        "publicationURL"
                                    ]
                                }
                            }
                        },
                        "required": [
                            "properties"
                        ]
                    },
                    "author": {
                        "type": "object",
                        "properties": {
                            "properties": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "authorName": {
                                            "type": "object",
                                            "properties": {
                                                "properties": {
                                                    "type": "object",
                                                    "properties": {
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "value"
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "properties"
                                            ]
                                        },
                                        "authorAffiliation": {
                                            "type": "object",
                                            "properties": {
                                                "properties": {
                                                    "type": "object",
                                                    "properties": {
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "value"
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "properties"
                                            ]
                                        },
                                        "authorIdentifierScheme": {
                                            "type": "object",
                                            "properties": {
                                                "properties": {
                                                    "type": "object",
                                                    "properties": {
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "value"
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "properties"
                                            ]
                                        },
                                        "authorIdentifier": {
                                            "type": "object",
                                            "properties": {
                                                "properties": {
                                                    "type": "object",
                                                    "properties": {
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "value"
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "properties"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "authorAffiliation",
                                        "authorIdentifier",
                                        "authorIdentifierScheme",
                                        "authorName"
                                    ]
                                }
                            }
                        },
                        "required": [
                            "properties"
                        ]
                    },
                    "dateOfCollection": {
                        "type": "object",
                        "properties": {
                            "properties": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "dateOfCollectionStart": {
                                            "type": "object",
                                            "properties": {
                                                "properties": {
                                                    "type": "object",
                                                    "properties": {
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "value"
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "properties"
                                            ]
                                        },
                                        "dateOfCollectionEnd": {
                                            "type": "object",
                                            "properties": {
                                                "properties": {
                                                    "type": "object",
                                                    "properties": {
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "value"
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "properties"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "dateOfCollectionEnd",
                                        "dateOfCollectionStart"
                                    ]
                                }
                            }
                        },
                        "required": [
                            "properties"
                        ]
                    },
                    "subject": {
                        "type": "object",
                        "properties": {
                            "properties": {
                                "type": "object",
                                "properties": {
                                    "value": {
                                        "type": "array"
                                    }
                                },
                                "required": [
                                    "value"
                                ]
                            }
                        },
                        "required": [
                            "properties"
                        ]
                    }
                },
                "required": [
                    "author",
                    "dateOfCollection",
                    "dsDescription",
                    "grantNumber",
                    "publication",
                    "subject",
                    "title"
                ]
            }
        },
        "required": [
            "about",
            "files",
            "objCitationSchema",
            "objDATASET_INIT",
            "softwareUsed"
        ]
    }
}
```