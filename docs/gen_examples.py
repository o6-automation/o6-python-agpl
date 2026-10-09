#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
# SPDX-License-Identifier: AGPL-3.0-or-later
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
Generate example documentation pages from annotated example scripts.

Each example ``.py`` file can be tagged with two kinds of inline markers:

* ``# BEGIN MD`` … ``# END MD`` — descriptive markdown text. Lines are
  emitted verbatim after stripping the leading ``# `` (or ``#``) marker.
  Indentation after the marker is preserved.
* ``# BEGIN CODE`` … ``# END CODE`` — a self-contained code snippet
  shown to readers as a fenced ``python`` block.

Outside any marker the file is treated as ordinary script content — the
markers themselves are also valid Python comments and do not affect
runtime. Each example's own file(s), with markers stripped, are written
next to the generated page as downloadable ``.py`` files and linked from
a ``## Source Code`` section, instead of being dumped into the page as a
second, huge copy of code the walkthrough above has already shown
step by step.

A multi-file example (manifest entry with ``doc_files`` set) renders every
listed file into the same doc page, one after another in ``doc_files``
order, each under its own ``## <filename>`` heading with its own docstring,
marker blocks, and source listing.

Usage::

    .venv/bin/python3 docs/gen_examples.py

Run from the repository root. The generator writes ``docs/examples/<slug>.md``
plus a sibling ``docs/examples/<slug>/`` directory holding its downloadable
``.py`` file(s), and rewrites the ``Examples`` nav block between the
``# BEGIN EXAMPLES`` / ``# END EXAMPLES`` markers in ``zensical.toml``.
"""

from __future__ import annotations

import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Sequence

# ``__file__`` lives in ``docs/``, so its grandparent is the repo root.
REPO_ROOT = Path(__file__).resolve().parent.parent
# A stale ``examples`` package may exist in site-packages; make sure the
# repo tree wins before importing the manifest.
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from examples.manifest import ALL_EXAMPLES, ExampleSpec, script_path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
DOCS_ROOT = REPO_ROOT / "docs"
OUTPUT_DIR = DOCS_ROOT / "examples"
ZENSICAL_TOML = REPO_ROOT / "zensical.toml"

# Markers in zensical.toml delimiting the generated "Examples" nav entry.
_TOML_BEGIN_RE = re.compile(r"^(?P<indent>[ \t]*)# BEGIN EXAMPLES\s*$", re.MULTILINE)
_TOML_END_RE = re.compile(r"^[ \t]*# END EXAMPLES\s*$", re.MULTILINE)


# ---------------------------------------------------------------------------
# Nav sections
# ---------------------------------------------------------------------------
# Top-level role folder → nav section label.  ``advanced_applications`` is
# excluded: its entries are standalone applications, not a graduated series,
# and are not published as a nav section.
SECTION_LABELS: dict[str, str] = {
    "client": "Client",
    "server": "Server",
    "type_authoring": "Type Authoring",
}


def _display_title(section: str, title: str) -> str:
    """Strip a leading repeat of ``section`` from an example's manifest
    ``title``, for use as both the page's H1 and its nav-sidebar label.

    The nav sidebar already groups pages under their section (``Client``,
    ``Server``, ``Type Authoring``), so a title of "Client Browsing" reads
    as "Client > Client Browsing" — the section name said twice. Stripped
    down to "Browsing", the same string works as both the sidebar entry and
    the page's own heading without repeating itself. Titles that don't
    start with the section name (everything under "Type Authoring") pass
    through unchanged.
    """
    if title == section:
        rest = ""
    elif title.startswith(section + " "):
        rest = title[len(section) + 1 :]
    else:
        return title
    rest = rest.strip()
    if rest.startswith("(") and rest.endswith(")"):
        rest = rest[1:-1].strip()
    return rest or title


def _slug(example_id: str) -> str:
    """Docs slug for a manifest id: ``client/C02_firststeps`` →
    ``client-c02-firststeps``."""
    return example_id.replace("/", "-")


def _sort_key(item: tuple[str, ExampleSpec]) -> tuple:
    """Order pages within a section by numeric prefix (``C01_`` < ``C02_``);
    un-prefixed entries (``advanced_applications``) sort alphabetically."""
    example_id, _spec = item
    stem = example_id.rsplit("/", 1)[-1]
    prefix = stem.split("_", 1)[0]
    if len(prefix) == 3 and prefix[0] in "CST" and prefix[1:].isdigit():
        return (0, prefix, example_id)
    return (1, example_id, "")


def _published() -> list[tuple[str, ExampleSpec]]:
    """Manifest entries with ``doc=True``, grouped into nav sections and
    ordered by numeric prefix within each section."""
    by_section: dict[str, list[tuple[str, ExampleSpec]]] = {}
    for example_id, spec in ALL_EXAMPLES.items():
        if not spec.doc:
            continue
        role = example_id.split("/", 1)[0]
        if role not in SECTION_LABELS:
            continue
        by_section.setdefault(role, []).append((example_id, spec))

    published: list[tuple[str, ExampleSpec]] = []
    for role in SECTION_LABELS:
        published.extend(sorted(by_section.get(role, []), key=_sort_key))
    return published


# ---------------------------------------------------------------------------
# Marker parsing
# ---------------------------------------------------------------------------
# Recognise "# BEGIN MD", "# BEGIN CODE" (with optional trailing whitespace
# and any amount of leading whitespace) and the matching "# END MD" /
# "# END CODE".  Capture the marker keyword so we can decide whether the
# block is markdown or code.
_MARKER_RE = re.compile(r"^(?P<indent>\s*)#\s*BEGIN\s+(?P<kind>MD|CODE)\s*$")
_END_RE = re.compile(r"^(?P<indent>\s*)#\s*END\s+(?P<kind>MD|CODE)\s*$")


@dataclass
class Block:
    """A single marker-delimited block from a .py file."""

    kind: str  # "MD" or "CODE"
    lines: list[str] = field(default_factory=list)


@dataclass
class ParsedExample:
    """Result of scanning one example script."""

    title: str
    docstring: str | None
    blocks: list[Block]
    raw_source: str  # original .py contents, used for the "Full source" block


_SETEXT_UNDERLINE_RE = re.compile(r"^=+$")


def _strip_leading_setext_title(docstring: str) -> str:
    """Drop a leading RST-style ``Title\\n=====`` line pair from ``docstring``.

    Several example scripts open their module docstring with their own
    hand-written title, underlined Setext-style. Markdown treats that same
    pattern as a heading, so left in place it renders as a second, often
    differently-worded H1 underneath the page's real title (see
    :func:`generate_pages`) — the "Server Tutorial: Variables" duplicate
    heading this strips. Docstrings that open with an ordinary sentence
    instead (no underline) are left untouched.
    """
    lines = docstring.splitlines()
    if len(lines) >= 2 and _SETEXT_UNDERLINE_RE.match(lines[1].strip()):
        lines = lines[2:]
        if lines and not lines[0].strip():
            lines = lines[1:]
        return "\n".join(lines).strip()
    return docstring


def _extract_docstring(source: str) -> str | None:
    """Return the module docstring, or ``None`` if there isn't one."""
    # Match the first triple-quoted string after optional shebang / encoding.
    m = re.search(
        r'^\s*[rR]?(?:"""|\'\'\')(?P<body>.*?)(?:"""|\'\'\')',
        source,
        flags=re.DOTALL | re.MULTILINE,
    )
    if not m:
        return None
    return _strip_leading_setext_title(m.group("body").strip())


def parse_example(path: Path, title: str) -> ParsedExample:
    """Scan ``path`` and return its docstring, marker blocks, and raw source."""
    raw = path.read_text(encoding="utf-8")
    docstring = _extract_docstring(raw)

    blocks: list[Block] = []
    current: Block | None = None

    for line in raw.splitlines():
        m_open = _MARKER_RE.match(line)
        m_end = _END_RE.match(line)
        if m_open:
            current = Block(kind=m_open.group("kind"))
            continue
        if m_end:
            if current is not None and m_end.group("kind") == current.kind:
                blocks.append(current)
                current = None
            else:
                raise ValueError(f"{path}: mismatched marker: {line!r}")
            continue
        if current is not None:
            current.lines.append(line)

    if current is not None:
        raise ValueError(f"{path}: unterminated marker: BEGIN {current.kind}")

    return ParsedExample(title=title, docstring=docstring, blocks=blocks, raw_source=raw)


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------
def _strip_markers(source: str) -> str:
    """Strip marker regions from ``source`` for the downloadable ``.py`` file.

    * ``# BEGIN MD`` … ``# END MD`` — the whole block (both marker lines
      and every line between them) is removed; the descriptive text
      belongs in the prose, not the file a reader downloads.
    * ``# BEGIN CODE`` … ``# END CODE`` — only the marker lines are
      removed; the code in between is preserved verbatim.

    Lines outside any marker pass through untouched.
    """
    md_open = re.compile(r"^\s*#\s*BEGIN\s+MD\s*$")
    md_close = re.compile(r"^\s*#\s*END\s+MD\s*$")
    code_marker = re.compile(r"^\s*#\s*(?:BEGIN|END)\s+CODE\s*$")

    out: list[str] = []
    in_md = False
    for line in source.splitlines():
        if not in_md and md_open.match(line):
            in_md = True
            continue
        if in_md:
            if md_close.match(line):
                in_md = False
            # Drop every line (markers and content) while inside the block.
            continue
        if code_marker.match(line):
            continue
        out.append(line)
    return "\n".join(out)


def _strip_hash_prefix(line: str) -> str:
    """Strip the leading ``# `` from a markdown-marker line.

    Handles ``# foo``, ``## foo`` (deeper headings inside MD), and bare ``#``.
    All whitespace to the left of the first ``#`` is dropped so that
    comments nested inside ``if``/``with``/function bodies still render
    as flush-left markdown.
    """
    stripped = line.lstrip()
    if not stripped.startswith("#"):
        # Blank inside a marker (just "#"); preserve as empty line.
        return ""
    # Strip one or more leading "#" plus optional single space.
    body = stripped.lstrip("#")
    if body.startswith(" "):
        body = body[1:]
    return body


def _render_md_block(block: Block) -> str:
    """Render a ``# BEGIN MD`` block as raw markdown."""
    out: list[str] = []
    for line in block.lines:
        if line.strip().startswith("#"):
            out.append(_strip_hash_prefix(line))
        else:
            # Lines that didn't start with "#" — rare, but render as-is.
            out.append(line.rstrip())
    # Trim trailing blank lines but keep at least one trailing newline.
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out)


def _render_code_block(block: Block) -> str:
    """Render a ``# BEGIN CODE`` block as a fenced ``python`` code block."""
    # Drop the marker lines themselves (already excluded by parser) and
    # dedent by the smallest common indentation so the snippet is flush-left.
    body = "\n".join(block.lines).strip("\n")
    lines = body.split("\n") if body else []
    indents = [len(l) - len(l.lstrip()) for l in lines if l.strip()]
    if indents:
        common = min(indents)
        lines = [l[common:] if len(l) >= common else l for l in lines]
    return "```python\n" + "\n".join(lines) + "\n```"


_ATX_HEADING_RE = re.compile(r"^#{1,6}(\s+\S.*)?$")


def _bump_headings(text: str) -> str:
    """Deepen every ATX heading in ``text`` by one level (``## `` → ``### ``).

    A file's MD blocks are authored against the classic single-file layout,
    where they sit at the document's top level. Nested under a multi-file
    page's own ``## <filename>`` heading, they need to drop one level to
    stay properly nested instead of reading as siblings of the file heading.
    """
    return "\n".join("#" + line if _ATX_HEADING_RE.match(line) else line for line in text.split("\n"))


def _requires_server_notice(spec: ExampleSpec) -> str | None:
    """Standard "start the other example's server first" admonition, built
    from the spec's ``requires_server`` manifest id.

    Examples get read out of order, so every page that needs another
    example's server states it the same way instead of each script writing
    its own reminder in slightly different words.
    """
    if spec.requires_server is None:
        return None
    other_id = spec.requires_server
    other_spec = ALL_EXAMPLES[other_id]
    other_script = script_path(other_id, other_spec).relative_to(REPO_ROOT).as_posix()
    other_ref = (
        f"[{other_spec.title}]({_safe_filename(_slug(other_id))}.md)"
        if other_id in dict(_published())
        else f"`{other_spec.title}`"
    )
    return (
        f'!!! info "This example needs a running server"\n'
        f"    Start {other_ref} first:\n"
        f"\n"
        f"    ```\n"
        f"    python {other_script}\n"
        f"    ```"
    )


def _render_docs_section(parsed: ParsedExample, heading: str | None, notice: str | None = None) -> str:
    """Render one file's docstring and marker blocks (no source).

    ``heading`` is the filename to title this section with, for a
    multi-file page; ``None`` renders the classic single-file layout,
    where the docstring/blocks sit at the top of the page with no
    filename heading of their own. ``notice``, when given, is a
    pre-rendered admonition block (see :func:`_requires_server_notice`)
    inserted right after the docstring.
    """
    parts: list[str] = []

    if heading is not None:
        parts.append(f"## {heading}")
        parts.append("")

    # Module docstring becomes the lead paragraph.
    if parsed.docstring:
        parts.append(parsed.docstring)
        parts.append("")

    if notice is not None:
        parts.append(notice)
        parts.append("")

    # First MD block (if any) is treated as a "Source layout / import"
    # intro. Subsequent blocks alternate MD explanation + CODE snippet
    # in the order they appear.
    for block in parsed.blocks:
        if block.kind == "MD":
            rendered = _render_md_block(block)
            parts.append(_bump_headings(rendered) if heading is not None else rendered)
        else:
            parts.append(_render_code_block(block))
        parts.append("")

    return "\n".join(parts)


def _render_source_links_section(folder: str, filenames: Sequence[str]) -> str:
    """Render a "## Source Code" section linking to the downloadable copies
    of ``filenames`` inside ``folder`` (a page-specific directory sitting
    next to the ``.md`` file — see :func:`write_pages`).

    The full source used to be dumped verbatim into the page as a giant
    fenced block, on top of the step-by-step walkthrough above that already
    quotes every snippet. Linking a real, downloadable ``.py`` file instead
    keeps the page focused on the explanation and gives readers something
    they can actually run.
    """
    parts = ["## Source Code", ""]
    if len(filenames) == 1:
        filename = filenames[0]
        parts.append(f"Download [`{filename}`]({folder}/{filename}) to run it locally.")
    else:
        parts.append("Download these files into the same folder to run the example:")
        parts.append("")
        parts.extend(f"- [`{filename}`]({folder}/{filename})" for filename in filenames)
    parts.append("")
    return "\n".join(parts)


def render_markdown(
    title: str,
    parsed_files: Sequence[tuple[ParsedExample, str | None, str | None]],
    folder: str,
    filenames: Sequence[str],
) -> str:
    """Build the full markdown page for one example, which may span
    several ``(parsed, heading, notice)`` files.

    The page opens with a single ``# title`` heading (see
    :func:`_display_title` — the one place a page's H1 is written, so it
    can never drift from what the nav sidebar shows). Every file's docs
    section (docstring + marker blocks) follows in the order given, then a
    "Source Code" section linking the downloadable copies of ``filenames``
    (see :func:`_render_source_links_section`).
    """
    docs = [_render_docs_section(parsed, heading, notice) for parsed, heading, notice in parsed_files]
    return "\n".join([f"# {title}", "", *docs, _render_source_links_section(folder, filenames)])


# ---------------------------------------------------------------------------
# Generation
# ---------------------------------------------------------------------------
@dataclass
class GeneratedPage:
    slug: str
    title: str
    section: str
    path: Path
    body: str
    source_dir: Path
    sources: list[tuple[str, str]]  # (filename, downloadable content)


def _safe_filename(slug: str) -> str:
    """Ensure the slug is filesystem-safe."""
    return slug.replace("/", "_")


def generate_pages() -> list[GeneratedPage]:
    """Build (but don't write) the pages for every documented example.

    Single-file examples render one section with their own docstring and
    marker blocks. Multi-file examples (``doc_files`` set on the spec)
    render every listed file into the same page, in ``doc_files`` order,
    each under its own ``## `` heading. Every page ends with a "Source
    Code" section linking downloadable copies of its file(s), written by
    :func:`write_pages` into a page-specific directory next to the ``.md``
    file.
    """
    pages: list[GeneratedPage] = []
    for example_id, spec in _published():
        entry_src = script_path(example_id, spec)
        if not entry_src.exists():
            raise FileNotFoundError(f"manifest entry not found: {entry_src}")
        safe_slug = _safe_filename(_slug(example_id))
        out_path = OUTPUT_DIR / f"{safe_slug}.md"
        section = SECTION_LABELS[example_id.split("/", 1)[0]]
        display_title = _display_title(section, spec.title)

        notice = _requires_server_notice(spec)
        if spec.doc_files is None:
            parsed = parse_example(entry_src, title=spec.title)
            sections: list[tuple[ParsedExample, str | None, str | None]] = [(parsed, None, notice)]
            sources = [(entry_src.name, _strip_markers(parsed.raw_source))]
        else:
            folder = entry_src.parent
            sections = []
            sources = []
            for filename in spec.doc_files:
                src = folder / filename
                if not src.exists():
                    raise FileNotFoundError(
                        f"manifest entry {example_id!r} lists {filename!r} in "
                        f"doc_files, but the file is missing: {src}"
                    )
                # The entry script owns the page title; supporting files
                # just contribute their own section under their filename.
                title = spec.title if filename == spec.entry else filename
                # The notice belongs on the entry file's section — that's
                # the one that actually needs the other server running.
                parsed = parse_example(src, title=title)
                sections.append((parsed, filename, notice if filename == spec.entry else None))
                sources.append((filename, _strip_markers(parsed.raw_source)))

        body = render_markdown(
            display_title, sections, folder=safe_slug, filenames=[filename for filename, _ in sources]
        )

        pages.append(
            GeneratedPage(
                slug=_slug(example_id),
                title=display_title,
                section=section,
                path=out_path,
                body=body,
                source_dir=OUTPUT_DIR / safe_slug,
                sources=sources,
            )
        )
    return pages


def write_pages(pages: Iterable[GeneratedPage]) -> None:
    """Write all generated pages, and their downloadable source files, to
    ``docs/examples/``, removing any file or directory that is not part of
    the current generation (orphan purge)."""
    pages = list(pages)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    current_paths = {page.path for page in pages}
    for existing in OUTPUT_DIR.glob("*.md"):
        if existing not in current_paths:
            existing.unlink()

    current_dirs = {page.source_dir for page in pages}
    for existing in OUTPUT_DIR.iterdir():
        if existing.is_dir() and existing not in current_dirs:
            shutil.rmtree(existing)

    for page in pages:
        page.path.write_text(page.body, encoding="utf-8")
        page.source_dir.mkdir(parents=True, exist_ok=True)
        current_files = {page.source_dir / filename for filename, _content in page.sources}
        for existing in page.source_dir.glob("*.py"):
            if existing not in current_files:
                existing.unlink()
        for filename, content in page.sources:
            (page.source_dir / filename).write_text(content, encoding="utf-8")


def _toml_escape(label: str) -> str:
    """Quote a label for the zensical.toml nav format."""
    # The format requires the literal value on the right of '=' with
    # surrounding double quotes — escape any embedded double quotes.
    return label.replace("\\", "\\\\").replace('"', '\\"')


def _render_toml_entries(pages: Sequence[GeneratedPage]) -> list[str]:
    """Render the ``{ "Examples" = [ ... ] }`` nav entry as TOML lines,
    relative to a zero indent. Paths are written relative to zensical's
    ``docs_dir`` (defaults to ``docs/``), so the leading ``docs/`` segment
    is stripped.  Pages are grouped under their nav section label,
    preserving section insertion order (already prefix-sorted by
    :func:`_published`).
    """
    lines = ['{ "Examples" = [', '    "examples.md",']

    by_section: dict[str, list[GeneratedPage]] = {}
    section_order: list[str] = []
    for page in pages:
        if page.section not in by_section:
            by_section[page.section] = []
            section_order.append(page.section)
        by_section[page.section].append(page)

    for section in section_order:
        lines.append(f'    {{ "{_toml_escape(section)}" = [')
        for page in by_section[section]:
            rel = Path("examples", f"{_safe_filename(page.slug)}.md").as_posix()
            lines.append(f'        {{ "{_toml_escape(page.title)}" = "{rel}" }},')
        lines.append("    ]},")

    lines.append("]},")
    return lines


def _marked_block(indent: str, pages: Sequence[GeneratedPage]) -> str:
    """The full ``# BEGIN EXAMPLES`` … ``# END EXAMPLES`` block, indented
    to match the surrounding nav array."""
    body = [f"{indent}{line}" for line in _render_toml_entries(pages)]
    return "\n".join([f"{indent}# BEGIN EXAMPLES", *body, f"{indent}# END EXAMPLES"])


def render_zensical_toml(pages: Sequence[GeneratedPage], current_text: str) -> str:
    """Return ``current_text`` with the region between the ``# BEGIN
    EXAMPLES`` / ``# END EXAMPLES`` markers replaced by the nav entry for
    ``pages``. Raises if the markers are missing."""
    m_begin = _TOML_BEGIN_RE.search(current_text)
    m_end = _TOML_END_RE.search(current_text)
    if not m_begin or not m_end or m_end.start() < m_begin.start():
        raise RuntimeError(
            f"{ZENSICAL_TOML}: could not find '# BEGIN EXAMPLES' / '# END EXAMPLES' markers"
        )
    new_block = _marked_block(indent=m_begin.group("indent"), pages=pages)
    return current_text[: m_begin.start()] + new_block + current_text[m_end.end() :]


def update_zensical_toml(pages: Sequence[GeneratedPage]) -> bool:
    """Rewrite the Examples nav block in zensical.toml in place. Returns
    ``True`` if the file changed."""
    current_text = ZENSICAL_TOML.read_text(encoding="utf-8")
    new_text = render_zensical_toml(pages, current_text)
    if new_text == current_text:
        return False
    ZENSICAL_TOML.write_text(new_text, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main() -> int:
    pages = generate_pages()
    write_pages(pages)
    print(f"Wrote {len(pages)} page(s) to " f"{OUTPUT_DIR.relative_to(REPO_ROOT)}/")
    changed = update_zensical_toml(pages)
    print(f"zensical.toml Examples nav block {'updated' if changed else 'already up to date'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
