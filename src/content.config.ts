import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";
import { SITE } from "@/config";

export const BLOG_PATH = "src/data/blog";
export const GUIDES_PATH = "src/data/guides";
export const PRODUCTS_PATH = "src/data/products";

const commonSchema = z.object({
  author: z.string().default(SITE.author),
  pubDatetime: z.date(),
  modDatetime: z.date().optional().nullable(),
  title: z.string(),
  description: z.string(),
  featured: z.boolean().optional(),
  draft: z.boolean().optional(),
  tags: z.array(z.string()).default(["others"]),
  canonicalURL: z.string().optional(),
  hideEditPost: z.boolean().optional(),
  timezone: z.string().optional(),
  cluster: z.string().optional(),
  pillar: z.string().optional(),
  leadMagnet: z.string().optional(),
  productCTA: z.string().optional(),
  targetKeyword: z.string().optional(),
  slug: z.string().optional(),
  isIndexable: z.boolean().default(true),
});

const blog = defineCollection({
  loader: glob({ pattern: "**/[^_]*.{md,mdx}", base: `./${BLOG_PATH}` }),
  schema: ({ image }) =>
    commonSchema.extend({
      ogImage: image().or(z.string()).optional(),
    }),
});

const guides = defineCollection({
  loader: glob({ pattern: "**/[^_]*.{md,mdx}", base: `./${GUIDES_PATH}` }),
  schema: ({ image }) =>
    commonSchema.extend({
      ogImage: image().or(z.string()).optional(),
    }),
});

const products = defineCollection({
  loader: glob({ pattern: "**/[^_]*.{md,mdx}", base: `./${PRODUCTS_PATH}` }),
  schema: ({ image }) =>
    commonSchema.extend({
      ogImage: image().or(z.string()).optional(),
      price: z.number().optional(),
      gumroadUrl: z.string().url().optional(),
    }),
});

export const collections = { blog, guides, products };
