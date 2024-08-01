# About this code

This repository was started in August of 2024 and uses [Docusaurus 3](https://docusaurus.io), a modern static website generator. The idea behind the repository is to provide an knowledgebase guide into understanding and working with the JoCo publicly available data.

## Why Docusaurus

The reason for Docusaurus is it is a CMS framework with integrations for things such as site search and the ability to easily prop up a test environment on [Vercel](https://vercel.com) or similar cloud virtual hosting solutions such as [StackBlitz](https://stackblitz.com/) without the need to create a coding environment locally (which can be pain for developers who simply wish to help with documentation and not have to worry about installing software dependencies which might not work with their computer setup).

Other benefits are:

- The Docusaurus framework automatically checks for broken links in your documents when you build the code (whether you are building locally or letting Vercel build for you). This is great for quality assurance.
- Looking good from the start, means a framework that has been designed by professional graphic artists for accessibility and out-of-the-box visual appeal. So you can simply focus on content and not building a site from scratch.

## Using this code on Vercel

The easiest way use this code (for your own project or to help contribute to this documentation) is to fork this repository in GitHub then log into Vercel.com and create a new project using your forked repo. Vercel can be used as a cloud testing environment, to help you avoid the need to setup NodeJs and NPM on your local computer (but you could do that as well). Vercel will build from your GitHub code repository and setup a test site so you could simply make changes to your forked repository code in GitHub.com, and see the changes in Vercel as you make code updates. 

Note, some of the application settings are set as environment variables. The `.env.example` file contains place-holder values for the environment. These variables will need to be added to your Vercel project since you do not want sensitive environment API keys or passwords published/embedded in your repository code. Once you have the code deployed to Vercel from GitHub, a link to your test site on Vercel will added to your main repository page on GitHub.

## Using the code locally

See Docusaurus documentation for this. It is not recommended. Try using StackBlitz or some other virtual service first, to save you the headache of installing dependencies on your computer.
