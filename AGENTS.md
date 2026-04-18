# AGENTS.md

Auto-loaded by Cursor, Claude Code, and any OpenAI-compatible coding agent.
Keep this file short; long-form context lives in `specs/ROADMAP.md`.

## First thing in every session

Read [`specs/ROADMAP.md`](./specs/ROADMAP.md) before responding to the user.
It documents:
- Current site state and live articles
- Available skills (`seo-article-outline`, `seo-article-localize`,
  `ja-article-style`, `en-article-style`)
- Prioritized TODOs (P0 → P3)
- Recent decisions log

If the user's request matches an existing ROADMAP.md TODO, announce which item
you're picking up. If it's new, add it to ROADMAP.md before starting.

## After completing any task

Update `specs/ROADMAP.md` in the same response:
1. Tick the TODO checkbox.
2. Add a dated one-liner to §"Recent decisions".
3. If the work revealed new TODOs, add them under the correct priority level.

For article edits, also update `specs/articles/<slug>.spec.md` §11 Change Log.

## Key project files

- `specs/ROADMAP.md` — cross-session TODO tracker (read first)
- `specs/articles/<slug>.spec.md` — per-article SEO planning + Change Log
- `work/AEIOU/marketing/SEO.md` — keyword research + skill operations guide
- `~/.claude/skills/{seo-article-outline, seo-article-localize,
  ja-article-style, en-article-style}/` — skill definitions (symlinked to
  `~/.cursor/skills/`)

## Non-negotiables

- Do not edit the root `CHANGELOG.md` (upstream AstroPaper auto-generated).
- Do not modify article frontmatter (`---` blocks) via style-linter scripts.
- Do not add emoji to article prose unless explicitly requested.
- Respond to the user in Japanese (per user preference).
