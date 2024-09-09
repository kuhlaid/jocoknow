---
sidebar_position: 5
---

# Jupyter notebooks

This is likely the best tool to have in your data curation toolbox. A Jupyter notebook is not only the visual eye candy for representing your metadata, but it provides you with the tools to download and work with much of the data. This is significant because we can run data analyses from within the notebook and save the results and notes from those analyses within a single file. The best thing about these notebooks is they are JSON formatted (you will notice we talk at great lengths about JSON in this guide). In this user guide we will provide you with examples and demonstrate the power of these notebooks.

## Best practices

For beginners to Jupyter notebooks, there are few guides on best practices on how to format a notebook. There are simply markdown cells and scripting cells that you fill with your notes and code. Keeping all of your information embedded within the notebook however can present problems. From the coding side it does not provide you with a method of 'script reuse'. It also can cause a notebook to become overly bloated with long blocks of scripts that distract from the overall notebook function which is usually to present results or describe something.

In our notebooks, we elevate the coding experience with a 'script once and use many times' approach which separates the core notebook code from the notebook itself. The approach reduces the scrolling required to navigate a notebook.

## Use cases for a notebook

### Data curation log

The DCN provided a useful curation checklist, but we wanted to use the list in a more dynamic way. What if we converted the checklist to a JSON object and used that as a template that can be read into a Jupyter notebook and used to create a curation logging application. No fancy databases or web servers needed, simply a notebook and a JSON curation checklist file. This process would feed into the next use case we will explain.

This process will take the DCN curation checklist to the next level for researchers to make better use of the resource.

### Data deposit and retrieval

Once our data curation steps have reached the deposit stage, we will use a Juptyer notebook to import the data into the repository.
Since our metadata schema and notebook scripts are reusable across datasets, the notebook provides an easy way to transfer and validate files in a consistent process. Once data is published to the repository, the end-users will have their own Jupyter notebook provided to them to retrieve and review the dataset quickly and easily.

### Documentation export

Many times a Jupyter notebook is useful in a static state for documentation purposes after the scripts have been run and the output (charts, tables, etc.) have been generated in the notebook. Using JupyterLab (or other Jupyter editor) a notebook can be exported to plain Markdown. This allows for easy cloning of a notebook into a document to add into a Docusaurus user guide for instance.