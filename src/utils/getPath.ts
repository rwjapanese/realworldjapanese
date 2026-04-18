import { BLOG_PATH, GUIDES_PATH, PRODUCTS_PATH } from "@/content.config";
import { slugifyStr } from "./slugify";
import { ACTIVE_LANGUAGES } from "@/config/languages";
import { getEntryLang, withLang } from "./i18n";

const ACTIVE_LANG_CODES = ACTIVE_LANGUAGES.map(l => l.code);

type CollectionPaths = {
  sourcePath: string;
  urlBase: string;
};

const COLLECTIONS: CollectionPaths[] = [
  { sourcePath: BLOG_PATH, urlBase: "posts" },
  { sourcePath: GUIDES_PATH, urlBase: "guides" },
  { sourcePath: PRODUCTS_PATH, urlBase: "products" },
];

function resolveCollection(filePath: string | undefined): CollectionPaths {
  if (!filePath) return COLLECTIONS[0];
  return (
    COLLECTIONS.find(c => filePath.includes(c.sourcePath)) ?? COLLECTIONS[0]
  );
}

/**
 * Get the full language-aware path of a content entry.
 *
 * Examples:
 *   id = "en/welcome", filePath = "src/data/blog/en/welcome.md"
 *     → "/en/posts/welcome/"
 *   id = "ja/keigo-guide", filePath = "src/data/guides/ja/keigo-guide.mdx"
 *     → "/ja/guides/keigo-guide/"
 *
 * @param id - content entry id (language-prefixed)
 * @param filePath - absolute filepath from glob loader
 * @param includeBase - whether to include the collection url base (e.g. `posts`)
 */
export function getPath(
  id: string,
  filePath: string | undefined,
  includeBase = true
) {
  const lang = getEntryLang(id);
  const { sourcePath, urlBase } = resolveCollection(filePath);

  const pathSegments = filePath
    ?.replace(sourcePath, "")
    .split("/")
    .filter(path => path !== "")
    .filter(path => !path.startsWith("_"))
    .filter(
      path =>
        !ACTIVE_LANG_CODES.includes(path as (typeof ACTIVE_LANG_CODES)[number])
    )
    .slice(0, -1)
    .map(segment => slugifyStr(segment));

  const basePath = includeBase ? urlBase : "";

  const entryIdSegments = id.split("/");
  const slug =
    entryIdSegments.length > 0 ? entryIdSegments.slice(-1) : entryIdSegments;

  const tail =
    !pathSegments || pathSegments.length < 1
      ? [basePath, ...slug]
      : [basePath, ...pathSegments, ...slug];

  const joined = tail.filter(Boolean).join("/");

  if (!includeBase) {
    return joined;
  }

  return withLang(lang, joined);
}
