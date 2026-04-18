import type { CollectionEntry } from "astro:content";
import {
  DEFAULT_LANGUAGE,
  isValidLanguage,
  type LanguageCode,
  ACTIVE_LANGUAGES,
} from "@/config/languages";

/**
 * Extract language code from a content entry ID.
 * Entries live under `src/data/<collection>/<lang>/...`, so the first path
 * segment of the id is the language code.
 *
 * Example: "en/keigo-guide" → "en"
 */
export function getEntryLang(id: string): LanguageCode {
  const firstSegment = id.split("/")[0];
  return isValidLanguage(firstSegment) ? firstSegment : DEFAULT_LANGUAGE;
}

/**
 * Get the slug portion of an entry id (after the language prefix).
 * Example: "en/posts/keigo-guide" → "posts/keigo-guide"
 */
export function getEntrySlug(id: string): string {
  const segments = id.split("/");
  if (segments.length > 0 && isValidLanguage(segments[0])) {
    return segments.slice(1).join("/");
  }
  return id;
}

/**
 * Filter a collection by language. Entries whose path starts with `<lang>/`
 * are kept. Returns the same element type the caller passed in.
 */
export function filterByLang<T extends { id: string }>(
  entries: T[],
  lang: LanguageCode
): T[] {
  return entries.filter(entry => getEntryLang(entry.id) === lang);
}

/**
 * Build a language-prefixed URL path.
 * Example: withLang("en", "/posts/keigo") → "/en/posts/keigo/"
 */
export function withLang(lang: LanguageCode, path: string = "/"): string {
  const trimmed = path.replace(/^\/+/, "").replace(/\/+$/, "");
  if (trimmed === "") return `/${lang}/`;
  return `/${lang}/${trimmed}/`;
}

/**
 * Build a blog post URL for a given entry.
 * Respects an optional `slug` override in frontmatter (for language-specific URLs).
 */
export function getPostUrl(
  entry: CollectionEntry<"blog"> | CollectionEntry<"guides"> | CollectionEntry<"products">,
  basePath: string
): string {
  const lang = getEntryLang(entry.id);
  const overrideSlug = entry.data.slug;
  const slug = overrideSlug ?? getEntrySlug(entry.id);
  return withLang(lang, `${basePath}/${slug}`);
}

/**
 * Get the language code for the current Astro request, falling back to the
 * default language when the URL has no language prefix.
 */
export function getCurrentLang(pathname: string): LanguageCode {
  const firstSegment = pathname.replace(/^\/+/, "").split("/")[0];
  return isValidLanguage(firstSegment) ? firstSegment : DEFAULT_LANGUAGE;
}

/** Strip the language prefix from a pathname. */
export function stripLangPrefix(pathname: string): string {
  const langCodes = ACTIVE_LANGUAGES.map(l => l.code).join("|");
  const regex = new RegExp(`^/(${langCodes})(/|$)`);
  const stripped = pathname.replace(regex, "/");
  return stripped === "" ? "/" : stripped;
}

/**
 * Active-language paths used by `getStaticPaths` to generate routes for each
 * active language.
 */
export function getLangStaticPaths() {
  return ACTIVE_LANGUAGES.map(l => ({ params: { lang: l.code } }));
}
