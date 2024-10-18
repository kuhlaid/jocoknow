---
sidebar_position: 1
---

# Data management planning

In the following sections we provide resources for helping you manage data more effectively. There are the same resources and processes we use to manage this project.

## DMPonline 

DMPonline is a data management planning guide hosted by the Digital Curation Centre (DCC) at https://dmptool.org/. It has built-in federated login for many major institutions, thus reducing the likelihood that you will need to generate a separate username and password to login if you work with one of these institutions. This guide steps you through questions you should be asking yourself about your data and provides a downloadable guide based on the answers you provide to the questions.

## Formatting data

For our project we will be using text-based files for disseminating most of our data. The encoding we want to enforce in these files is UTF-8, which is backwards-compatibility with ASCII and the most common Unicode format. Scripts and programs should not fail due to encoding problems if we are providing data encoded using UTF-8. We process our data through UTF-8 encoding functions and validators to ensure this encoding. Informing users about your data encoding enhances trust in and accessibility to your data.

## Metadata

Metadata is information that describes a set of data. Data repositories generally define metadata as a small overview subset of descriptive information for a set of data, and do not support more detailed descriptive metadata for working with the data. We dig deeper and present a much richer set of metadata, described under the [README.json](data-dictionary.md#dvdatasetmetadatajson-metadata) section of this guide.

## Schemas and validation

If you follow the links to [schemas](data-dictionary.md#schemas) and [validation](data-dictionary.md#validation) you will learn how these processes relate to our [README.json](data-dictionary.md#dvdatasetmetadatajson-metadata) file.