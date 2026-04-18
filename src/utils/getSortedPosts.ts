import type { CollectionEntry } from "astro:content";
import postFilter from "./postFilter";

type SortablePost = CollectionEntry<"blog"> | CollectionEntry<"guides">;

const getSortedPosts = <T extends SortablePost>(posts: T[]): T[] => {
  return posts
    .filter(postFilter)
    .sort(
      (a, b) =>
        Math.floor(
          new Date(b.data.modDatetime ?? b.data.pubDatetime).getTime() / 1000
        ) -
        Math.floor(
          new Date(a.data.modDatetime ?? a.data.pubDatetime).getTime() / 1000
        )
    );
};

export default getSortedPosts;
