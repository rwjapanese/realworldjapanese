import type { APIRoute } from "astro";
import { getCollection, type CollectionEntry } from "astro:content";
import { generateOgImageForPost } from "@/utils/generateOgImages";
import { getEntryLang, getEntrySlug } from "@/utils/i18n";
import { SITE } from "@/config";

export async function getStaticPaths() {
  if (!SITE.dynamicOgImage) {
    return [];
  }

  const guides = await getCollection("guides").then(g =>
    g.filter(({ data }) => !data.draft && !data.ogImage)
  );

  return guides.map(guide => ({
    params: {
      lang: getEntryLang(guide.id),
      slug: guide.data.slug ?? getEntrySlug(guide.id),
    },
    props: guide,
  }));
}

export const GET: APIRoute = async ({ props }) => {
  if (!SITE.dynamicOgImage) {
    return new Response(null, {
      status: 404,
      statusText: "Not found",
    });
  }

  const buffer = await generateOgImageForPost(
    props as CollectionEntry<"guides">
  );
  return new Response(new Uint8Array(buffer), {
    headers: { "Content-Type": "image/png" },
  });
};
