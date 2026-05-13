#!/usr/bin/env python3
"""
add_faqs.py — Extract FAQ Q/A pairs from MDX article bodies and inject them
into the frontmatter as a `faqs:` YAML array, used by Layout.astro to emit
FAQPage JSON-LD structured data.

Usage:
    python3 scripts/add_faqs.py src/data/guides/ja/<slug>.mdx \\
                                src/data/guides/en/<slug>.mdx

What it does:
    1. Locates the FAQ section H2 — accepts `## よくある質問` (JA),
       `## Frequently asked questions` (EN long form), or `## FAQ` (short).
    2. Pairs every `###` question with its following paragraph(s) as the
       answer.
    3. Strips Markdown formatting (`**bold**`, `<strong>`, `[link](href)`,
       inline `code`, etc.) so the JSON-LD output is plain prose — required
       for clean FAQPage rich-result rendering.
    4. Skips blockquote callouts (`>`) and horizontal rules (`---`).
    5. Injects (or replaces) the `faqs:` block in frontmatter — idempotent.

Run after writing a new article. Pair with one of the supported FAQ H2
headings so the script can find the section reliably.
"""
import re
import sys
import pathlib

FAQ_H2_PATTERNS = [
    r'^## よくある質問',
    r'^## Frequently asked questions',
    r'^## FAQ\s*$',
]


def strip_md(text: str) -> str:
    """Strip Markdown formatting for plain prose used in JSON-LD."""
    # <strong>...</strong> / <em>...</em>
    text = re.sub(r'</?strong>', '', text)
    text = re.sub(r'</?em>', '', text)
    # **bold** / __bold__
    text = re.sub(r'\*\*([^\*]+?)\*\*', r'\1', text)
    text = re.sub(r'__([^_]+?)__', r'\1', text)
    # *italic* / _italic_ — be careful not to match ** which is already handled
    text = re.sub(r'(?<!\*)\*([^\*\n]+?)\*(?!\*)', r'\1', text)
    text = re.sub(r'(?<!_)_([^_\n]+?)_(?!_)', r'\1', text)
    # [text](link) → text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # `inline code` → inline code
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # Collapse multiple whitespace into single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def extract_faqs(content: str) -> list[tuple[str, str]]:
    """Walk lines and pair H3 questions with their following paragraph(s)."""
    faq_h2_re = re.compile('|'.join(FAQ_H2_PATTERNS))
    lines = content.split('\n')
    in_faq = False
    faqs: list[tuple[str, str]] = []
    current_q: str | None = None
    current_a: list[str] = []

    for line in lines:
        if faq_h2_re.match(line):
            in_faq = True
            continue
        if not in_faq:
            continue
        # End of FAQ block: next H2 or horizontal rule + new section
        if line.startswith('## ') and not faq_h2_re.match(line):
            break
        if line.startswith('### '):
            # commit previous Q/A
            if current_q is not None:
                faqs.append((current_q, ' '.join(current_a).strip()))
            current_q = line[4:].strip()
            current_a = []
        elif line.strip() and current_q is not None:
            stripped = line.strip()
            # Skip blockquote callouts
            if stripped.startswith('>'):
                continue
            # Skip horizontal rules (---, ***, ___)
            if re.fullmatch(r'[-*_]{3,}', stripped):
                continue
            current_a.append(strip_md(stripped))

    if current_q is not None:
        faqs.append((current_q, ' '.join(current_a).strip()))

    # Filter out empty answers
    return [(q, a) for (q, a) in faqs if a]


def build_yaml(faqs: list[tuple[str, str]]) -> str:
    """Build a YAML `faqs:` block using literal block scalars (>-) so we
    don't have to escape quotes or special chars."""
    out = ['faqs:']
    for q, a in faqs:
        # Use double-quoted strings; escape backslashes and double-quotes.
        q_esc = q.replace('\\', '\\\\').replace('"', '\\"')
        a_esc = a.replace('\\', '\\\\').replace('"', '\\"')
        out.append(f'  - q: "{q_esc}"')
        out.append(f'    a: "{a_esc}"')
    return '\n'.join(out) + '\n'


def inject_faqs(content: str, faqs_yaml: str) -> str:
    """Insert/replace `faqs:` block in frontmatter (between leading --- and
    next ---). Idempotent."""
    fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not fm_match:
        raise ValueError("No frontmatter found")
    frontmatter = fm_match.group(1)
    rest = content[fm_match.end():]

    # Normalize: ensure frontmatter ends with \n so the existing-faqs regex
    # can match the trailing indented line even when the original
    # frontmatter's last byte was the closing `\n` consumed by the \n---\n
    # separator above.
    if not frontmatter.endswith('\n'):
        frontmatter += '\n'

    # Remove existing faqs: block if present (multi-line YAML block).
    # Match `faqs:\n` followed by lines that begin with two or more spaces
    # (the YAML array body), until a non-indented line or EOF.
    existing_re = re.compile(
        r'\nfaqs:\n(?:[ \t]+.*\n)+',
        re.MULTILINE,
    )
    # Also handle the case where faqs: is at the very top with no preceding \n.
    frontmatter = re.sub(existing_re, '\n', '\n' + frontmatter).lstrip('\n')

    # Append the new faqs block at the end of frontmatter.
    if not frontmatter.endswith('\n'):
        frontmatter += '\n'
    frontmatter += faqs_yaml.rstrip('\n')

    return f'---\n{frontmatter}\n---\n{rest}'


def main(paths: list[str]) -> int:
    for p in paths:
        path = pathlib.Path(p)
        content = path.read_text(encoding='utf-8')
        faqs = extract_faqs(content)
        if not faqs:
            print(f'[skip] {p} — no FAQ section found', file=sys.stderr)
            continue
        yaml_block = build_yaml(faqs)
        new_content = inject_faqs(content, yaml_block)
        if new_content == content:
            print(f'[ok-noop] {p} — already up to date')
            continue
        path.write_text(new_content, encoding='utf-8')
        print(f'[updated] {p} — {len(faqs)} FAQs')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
