import type { SocialLink } from "../types";

export const SOCIALS: SocialLink[] = [
    {
        name: "Github",
        href: "https://github.com/jan-dolezil",
        linkTitle: `Follow Claude Shannon on Github`,
        isActive: true,
    },
    {
        name: "Mail",
        href: "mailto:honza.dolezil@gmail.com",
        linkTitle: `Send an email to Claude`,
        isActive: true,
    },
    {
        name: "Google Scholar",
        href: "https://scholar.google.com/citations?user=shannon",
        linkTitle: `Claude Shannon on Google Scholar`,
        isActive: false,
    },
    {
        name: "ORCID",
        href: "https://orcid.org/0000-0002-1825-0097",
        linkTitle: `Claude Shannon on ORCID`,
        isActive: false,
    },
    {
        name: "LinkedIn",
        href: "https://www.linkedin.com/in/claude-shannon-123456789/",
        linkTitle: `Claude Shannon on LinkedIn`,
        isActive: false, // Assuming Claude doesn't have a LinkedIn profile
    },
];

export const SOCIAL_ICONS: Record<string, string> = {
    Github: "Github",
    Mail: "Mail",
    Linkedin: "LinkedIn",
    "Google Scholar": "GoogleScholar",
    ORCID: "ORCID",
    RSS: "RSS",
};