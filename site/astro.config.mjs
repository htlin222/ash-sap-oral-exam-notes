// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://htlin222.github.io',
	base: '/ash-sap-oral-exam-notes',
	integrations: [
		starlight({
			title: 'ASH-SAP 血液科口試問答筆記',
			description: '依 ASH-SAP 9th Edition (2025) 改寫的血液科專科口試問答重點整理',
			favicon: '/favicon.svg',
			customCss: ['./src/styles/custom.css'],
			social: [],
			editLink: {
				baseUrl: 'https://github.com/htlin222/ash-sap-oral-exam-notes/edit/main/site/',
			},
			sidebar: [
				{
					label: '全部章節',
					items: [{ autogenerate: { directory: 'chapters' } }],
				},
			],
			head: [
				{
					tag: 'meta',
					attrs: { property: 'og:image', content: 'https://htlin222.github.io/ash-sap-oral-exam-notes/og-image.png' },
				},
				{
					tag: 'meta',
					attrs: { name: 'twitter:card', content: 'summary_large_image' },
				},
			],
		}),
	],
});
