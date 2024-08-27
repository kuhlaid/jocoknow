# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.2] - future

- [ ] add Algolia search once the site is production ready
- [ ] `cmfcmf/docusaurus-search-local` search plugin needs better configuration
- [ ] local search linking to pages such as `https://jocoknow.vercel.app/docs/jocoknow-extras/translate-your-site/docs/jocoknow-extras/translate-your-site#translate-a-doc` which do not exist
- [ ] add resources for developing data management plan (https://dmponline.dcc.ac.uk/) and data curation logs
- [ ] add a template for logging data curation steps
- [ ] need to add 'levels' to the docs/intro document and make it more user-friendly
- [ ] update `intro` document with links and more information
- [ ] create python packages for handling basic API functions 
- [x] added cheerio resolutions to the package.json file to correct an issue with local search
- [x] adding additional documentation for a data curation checklist and steps to help automate a curation log

## [0.0.1] - Aug. 13, 2024

- [x] adding some starter documents on data curation
- [x] adding dates and authors to blogs on docs
- [x] updated Docusaurus to version 3.5.2
- [x] testing orama search plugin, but both the local and cloud version have an error needing to be fixed in https://github.com/askorama/orama/issues/728
- [x] testing DocSearch crawler https://docsearch.algolia.com/docs/legacy/run-your-own/#run-the-crawl-from-the-docker-image and setting up an .env.prod set of environment variables, but it keeps throwing `Unreachable hosts` error
- [x] adding a basic `cmfcmf/docusaurus-search-local` search plugin (needs configuration changes but is a good starter)