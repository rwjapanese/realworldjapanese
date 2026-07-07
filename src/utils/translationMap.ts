import { getCollection, type CollectionKey } from "astro:content";
import {
  ACTIVE_LANGUAGE_CODES,
  isValidLanguage,
  type LanguageCode,
} from "@/config/languages";
import { getEntryLang, getEntrySlug } from "./i18n";

/**
 * Collections that generate per-language article pages and therefore
 * participate in hreflang cross-linking.
 */
const ARTICLE_COLLECTIONS: CollectionKey[] = ["blog", "guides", "products"];

/**
 * A translation "key" identifies the same logical article across languages.
 * Two entries are counterparts when they resolve to the same key: either the
 * same slug-less id tail (basename) or, when a language overrides the URL via
 * frontmatter `slug`, the same override slug.
 *
 * We build one key per (collection, language, entry) and group by
 * (collection + tail). This lets a JA article with a `slug` override still be
 * matched to its EN counterpart as long as the *basename* matches — and if a
 * language sets an explicit override to intentionally diverge, it simply won't
 * collide, which is the correct behaviour (no false alternate).
 */
type EntryLike = { id: string; data: { slug?: string; draft?: boolean } };

/**
 * The slug-less tail of an entry id (path after the language prefix), used as
 * the counterpart-matching key. Example: "en/nested/keigo" → "nested/keigo".
 */
function entryTail(id: string): string {
  return getEntrySlug(id);
}

/**
 * For a given collection entry id, return the list of active languages that
 * actually have a published (non-draft) counterpart article — always including
 * the entry's own language.
 *
 * Counterpart matching is by slug-less id tail (basename incl. any nested
 * path). This mirrors how routes are generated: two files at
 * `guides/en/keigo-guide.mdx` and `guides/ja/keigo-guide.mdx` are the same
 * logical guide in two languages.
 */
export async function getAvailableLocales(
  collection: CollectionKey,
  id: string
): Promise<LanguageCode[]> {
  const selfLang = getEntryLang(id);
  const tail = entryTail(id);

  const entries = (await getCollection(
    collection,
    ({ data }: EntryLike) => !data.draft
  )) as unknown as EntryLike[];

  const langs = new Set<LanguageCode>([selfLang]);
  for (const entry of entries) {
    if (entryTail(entry.id) !== tail) continue;
    const lang = getEntryLang(entry.id);
    if (isValidLanguage(lang)) langs.add(lang);
  }

  // Preserve a stable, config-driven ordering.
  return ACTIVE_LANGUAGE_CODES.filter(code => langs.has(code));
}

/**
 * Resolve the URL slug (path tail after the collection base) for the
 * counterpart of `id` in `targetLang`. Honors a per-language `slug` frontmatter
 * override, matching `getStaticPaths` in the [...slug] routes. Returns
 * `undefined` when no counterpart exists in that language.
 */
export async function getCounterpartSlug(
  collection: CollectionKey,
  id: string,
  targetLang: LanguageCode
): Promise<string | undefined> {
  const tail = entryTail(id);
  const entries = (await getCollection(
    collection,
    ({ data }: EntryLike) => !data.draft
  )) as unknown as EntryLike[];

  const match = entries.find(
    entry =>
      getEntryLang(entry.id) === targetLang && entryTail(entry.id) === tail
  );
  if (!match) return undefined;
  return match.data.slug ?? entryTail(match.id);
}

/**
 * Build the full set of per-language slugs for an entry's counterparts, keyed
 * by language code. Only languages with an actual counterpart appear. The
 * result feeds hreflang alternate URL construction so each alternate uses that
 * language's own (possibly overridden) slug rather than the source slug.
 */
export async function getCounterpartSlugs(
  collection: CollectionKey,
  id: string
): Promise<Partial<Record<LanguageCode, string>>> {
  const tail = entryTail(id);
  const entries = (await getCollection(
    collection,
    ({ data }: EntryLike) => !data.draft
  )) as unknown as EntryLike[];

  const map: Partial<Record<LanguageCode, string>> = {};
  for (const entry of entries) {
    if (entryTail(entry.id) !== tail) continue;
    const lang = getEntryLang(entry.id);
    if (!isValidLanguage(lang)) continue;
    map[lang] = entry.data.slug ?? entryTail(entry.id);
  }
  return map;
}

export { ARTICLE_COLLECTIONS };
