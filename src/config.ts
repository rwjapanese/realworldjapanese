import { DEFAULT_LANGUAGE } from "./config/languages";

export const SITE = {
  website: "https://realworldjapanese.com/",
  author: "Real-World Japanese",
  profile: "https://realworldjapanese.com/",
  desc: "Real phrases for real Japanese workplaces. Stop sounding rude at work with our A/B/C politeness framework.",
  title: "Real-World Japanese",
  ogImage: "astropaper-og.jpg",
  lightAndDarkMode: true,
  postPerIndex: 4,
  postPerPage: 10,
  scheduledPostMargin: 15 * 60 * 1000,
  showArchives: true,
  showBackButton: true,
  editPost: {
    enabled: false,
    text: "Edit page",
    url: "https://github.com/rwjapanese/realworldjapanese/edit/main/",
  },
  dynamicOgImage: true,
  dir: "ltr",
  lang: DEFAULT_LANGUAGE,
  timezone: "Asia/Tokyo",
} as const;
