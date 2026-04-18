# specs/

Planning documents for SEO articles. **Not included in the site build** (lives outside `src/`).

> **Start here when resuming:** [`ROADMAP.md`](./ROADMAP.md) — project-wide TODO tracker with "How to resume" instructions at the top.

## Structure

```
specs/
├── README.md                              ← This file
├── ROADMAP.md                             ← Cross-article TODOs + session handoff (READ FIRST when resuming)
├── articleSpec.template.md                ← Base spec template (per-article)
├── articleSpecLanguageDiff.template.md    ← Language-diff spec template (per-language, added lazily)
└── articles/
    ├── <slug>.spec.md                     ← Base spec for an article (one per article)
    └── <slug>.<lang>.spec.md              ← Language diff spec (added only if target-language SERP diverges materially)
```

## Lifecycle

1. **Plan**: `~/.claude/skills/seo-article-outline` generates `articles/<slug>.spec.md`.
2. **Write**: Use the spec to author `src/data/<collection>/<lang>/<slug>.mdx` (set `draft: true` while writing).
3. **Publish**: Flip `draft: false`. Spec file stays — it's the source of truth for future updates.
4. **Localize (Phase 2+)**: `~/.claude/skills/seo-article-localize` runs target-language SERP analysis. If divergence is material, it generates `<slug>.<lang>.spec.md`; otherwise writer uses the base spec directly.
5. **Audit**: Periodically re-run outline skill to detect SERP drift. Update `last_serp_audit` and delta-integrate findings.

## Rules

- **One base spec per `slug`.** Slug matches the MDX filename.
- **Diff specs are lazy.** Only create when the target-language SERP truly diverges from the base.
- **Never delete a spec after publishing.** Archive with `status: archived` if the article is deprecated.
- **Update the change log** in each spec when editing.
