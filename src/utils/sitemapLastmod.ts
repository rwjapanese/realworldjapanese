import { readdirSync, readFileSync, statSync } from "node:fs";
import { join, extname, basename } from "node:path";
import { fileURLToPath } from "node:url";

/**
 * Config-time sitemap lastmod support.
 *
 * This runs at astro.config evaluation (Node context, not the content layer),
 * so it cannot use `getCollection`. Instead it walks `src/data/**​/*.{md,mdx}`
 * with node:fs, parses just enough frontmatter to reconstruct each article's
 * public URL and its last-modified date, and returns a `url → lastmod` map.
 *
 * The sitemap `serialize` hook looks each URL up in this map and stamps
 * `item.lastmod`. URLs absent from the map (index, tags, about, archives) are
 * left without a lastmod on purpose. We NEVER fall back to build time: Google
 * treats lastmod trust as binary, so stamping every URL on every deploy would
 * forfeit the signal entirely.
 */

const DATA_ROOT = fileURLToPath(new URL("../data", import.meta.url));

/**
 * Maps a data subdirectory to the URL base segment used in routes. Mirrors the
 * COLLECTIONS table in src/utils/getPath.ts (the `blog` collection is served
 * under `/posts/`). Keep these in sync.
 */
const COLLECTION_URL_BASE: Record<string, string> = {
  blog: "posts",
  guides: "guides",
  products: "products",
};

type ParsedFrontmatter = {
  pubDatetime?: string;
  modDatetime?: string;
  slug?: string;
  draft?: boolean;
};

/**
 * Extract the leading `---` fenced YAML frontmatter block. Returns the raw
 * block text (without the fences), or an empty string when none is present.
 */
function extractFrontmatterBlock(raw: string): string {
  const match = raw.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  return match ? match[1] : "";
}

/** Strip surrounding single/double quotes from a scalar YAML value. */
function unquote(value: string): string {
  const trimmed = value.trim();
  if (
    (trimmed.startsWith('"') && trimmed.endsWith('"')) ||
    (trimmed.startsWith("'") && trimmed.endsWith("'"))
  ) {
    return trimmed.slice(1, -1);
  }
  return trimmed;
}

/**
 * Minimal, tolerant frontmatter parser for the four top-level keys we need.
 * Only reads top-level `key: value` lines and ignores nested structures
 * (e.g. faqs), so it never misreads a nested `slug:`/`draft:` under a list.
 */
function parseFrontmatter(block: string): ParsedFrontmatter {
  const result: ParsedFrontmatter = {};
  for (const line of block.split(/\r?\n/)) {
    // Only top-level keys: no leading whitespace (nested/list items indented).
    const m = line.match(/^([A-Za-z][A-Za-z0-9_]*):\s*(.*)$/);
    if (!m) continue;
    const key = m[1];
    const value = unquote(m[2]);
    switch (key) {
      case "pubDatetime":
        result.pubDatetime = value;
        break;
      case "modDatetime":
        result.modDatetime = value;
        break;
      case "slug":
        result.slug = value;
        break;
      case "draft":
        result.draft = value === "true";
        break;
      default:
        break;
    }
  }
  return result;
}

/** Recursively collect .md/.mdx files under a directory. */
function walkMarkdown(dir: string): string[] {
  const out: string[] = [];
  let entries: string[];
  try {
    entries = readdirSync(dir);
  } catch {
    return out;
  }
  for (const name of entries) {
    if (name.startsWith("_")) continue; // glob loader excludes `_`-prefixed
    const full = join(dir, name);
    const stats = statSync(full);
    if (stats.isDirectory()) {
      out.push(...walkMarkdown(full));
    } else if (extname(name) === ".md" || extname(name) === ".mdx") {
      out.push(full);
    }
  }
  return out;
}

/**
 * Turn a valid date-ish frontmatter string into an ISO 8601 string. Returns
 * undefined for missing/invalid values so callers can skip them.
 */
function toIso(value: string | undefined): string | undefined {
  if (!value) return undefined;
  const d = new Date(value);
  if (Number.isNaN(d.getTime())) return undefined;
  return d.toISOString();
}

/**
 * Build a `{ absoluteUrl → lastmod(ISO) }` map for every published article,
 * with the URL constructed exactly as the site emits it (leading + trailing
 * slash, directory format). `site` should be `SITE.website` (may or may not end
 * in a slash).
 */
export function buildLastmodMap(site: string): Record<string, string> {
  const base = site.replace(/\/+$/, "");
  const map: Record<string, string> = {};

  for (const collectionDir of Object.keys(COLLECTION_URL_BASE)) {
    const urlBase = COLLECTION_URL_BASE[collectionDir];
    const root = join(DATA_ROOT, collectionDir);

    for (const file of walkMarkdown(root)) {
      const raw = readFileSync(file, "utf8");
      const fm = parseFrontmatter(extractFrontmatterBlock(raw));
      if (fm.draft) continue;

      const lastmod = toIso(fm.modDatetime) ?? toIso(fm.pubDatetime);
      if (!lastmod) continue;

      // Language = first path segment under the collection dir.
      const rel = file.slice(root.length).replace(/^[\\/]+/, "");
      const parts = rel.split(/[\\/]/);
      const lang = parts[0];
      const fileBase = basename(file, extname(file));
      // Nested subfolders between lang and file become URL path segments.
      const nested = parts.slice(1, -1);
      const slug = fm.slug ?? [...nested, fileBase].join("/");

      const url = `${base}/${lang}/${urlBase}/${slug}/`;
      map[url] = lastmod;
    }
  }

  return map;
}
