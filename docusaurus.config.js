// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'JoCoKnow',
  tagline: 'The User Guide to JoCo data',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  // trying https://github.com/cmfcmf/docusaurus-search-local
  // plugins: ["@cmfcmf/docusaurus-search-local"],

  // waiting on fix for https://github.com/askorama/orama/issues/728 before adding search capabilities
  // plugins: ["@orama/plugin-docusaurus-v3"],

  // (does not work as of Aug. 2 due to .docusaurus/orama-search-index-current.json.gz file not existing)trying orama cloud search index
  // plugins: [
  //   [
  //     "@orama/plugin-docusaurus-v3",
  //     {
  //       cloud: {
  //         indexId: "https://cloud.orama.run/v1/indexes/go-unc-edu-bogqoa",
  //         oramaCloudAPIKey: process.env.ORAMA_CLOUD_API_KEY, // Env variable suggested
  //         deploy: "default" // Enables deploy while building/starting
  //       },
  //     },
  //   ],
  // ],
  plugins: [
    require.resolve('@cmfcmf/docusaurus-search-local')
  ],
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          breadcrumbs: true,
          sidebarPath: './sidebars.js',
          showLastUpdateTime: true, // show date on documents
          showLastUpdateAuthor: true  // show author who performed update
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
          //   'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
          //   'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'The User Guide to JoCo data',
        logo: {
          alt: 'The User Guide Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Support',
          },
          {to: '/blog', label: 'Blog', position: 'left'},
          {
            href: 'https://github.com/kuhlaid/jocoknow',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Tutorial',
                to: '/docs/intro',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'FAQ',
                to: '/blog',
              }
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} JoCoKnow Project. Site built with the open Docusaurus site generation framework.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
