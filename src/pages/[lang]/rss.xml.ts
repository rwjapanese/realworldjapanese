import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import { getPath } from "@/utils/getPath";
import getSortedPosts from "@/utils/getSortedPosts";
import { SITE } from "@/config";
import { ACTIVE_LANGUAGES, isValidLanguage } from "@/config/languages";
import { filterByLang } from "@/utils/i18n";

export async function getStaticPaths() {
  return ACTIVE_LANGUAGES.map(l => ({ params: { lang: l.code } }));
}

export async function GET({ params }: { params: { lang: string } }) {
  const lang = isValidLanguage(params.lang) ? params.lang : "en";
  const posts = await getCollection("blog");
  const langPosts = filterByLang(posts, lang);
  const sortedPosts = getSortedPosts(langPosts);
  return rss({
    title: SITE.title,
    description: SITE.desc,
    site: SITE.website,
    items: sortedPosts.map(({ data, id, filePath }) => ({
      link: getPath(id, filePath),
      title: data.title,
      description: data.description,
      pubDate: new Date(data.modDatetime ?? data.pubDatetime),
    })),
  });
}
