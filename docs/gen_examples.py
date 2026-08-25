#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
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
runtime. The full source is always appended under a ``## Full source``
section.

Usage::

    .venv/bin/python3 docs/gen_examples.py            # write files + print nav
    .venv/bin/python3 docs/gen_examples.py --dry-run  # only print the nav
    .venv/bin/python3 docs/gen_examples.py --check    # exit non-zero if files are stale

Run from the repository root. The generator writes ``docs/examples2/<slug>.md``
and prints the TOML block that should replace the ``Examples`` section of
``zensical.toml``.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Sequence


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
# ``__file__`` lives in ``docs/``, so its grandparent is the repo root.
REPO_ROOT = Path(__file__).resolve().parent.parent
EXAMPLES_ROOT = REPO_ROOT / "examples"
DOCS_ROOT = REPO_ROOT / "docs"
OUTPUT_DIR = DOCS_ROOT / "examples2"
ZENSICAL_TOML = REPO_ROOT / "zensical.toml"


# ---------------------------------------------------------------------------
# Whitelist of examples to publish.
#
# Each entry is ``(relative_path, slug, title)``:
#
# * ``relative_path`` — path under ``examples/`` to the annotated ``.py``.
# * ``slug``          — basename for the generated ``.md`` (no extension).
# * ``title``         — human-readable title used in the page <h1> and
#                       the zensical nav.
#
# Add new entries here to publish additional examples.
# ---------------------------------------------------------------------------
WHITELIST: dict[str, list[tuple[str, str, str]]] = {
    "low level": [
        # ---- Low-level ----
        ("lowlevel/types.py", "lowlevel-types", "Types"),
        ("lowlevel/client.py", "lowlevel-client", "Client")
    ],
    "high level": [
        # ---- High-level ----
        ("highlevel/client_basic.py", "highlevel-client-basics", "Client Basics"),
        ("highlevel/client_browsing.py", "highlevel-client-browsing", "Client Browsing"),
        ("highlevel/client_configuration.py", "highlevel-client-config", "Client Configuration"),
        ("highlevel/client_modes.py", "highlevel-client-modes", "Client Modes"),
        ("highlevel/client_nodemanagement.py", "highlevel-client-nodemanagement", "Client Node Management"),
        ("highlevel/client_usernamepw.py", "highlevel-client-usernamepw-authentication", "Client Username / Password Authentication"),
        ("highlevel/opcua_browser.py", "highlevel-client-opcua-browser", "Client Interactive Browser"),
        ("highlevel/client/subscription.py", "highlevel-client-subscriptions", "Client Subscriptions"),

        ("highlevel/basic_server.py", "highlevel-server-basics", "Server Basics"),
        ("highlevel/server_minimal.py", "highlevel-server-minimal", "Server Minimal"),
        ("highlevel/server_objects.py", "highlevel-server-objects", "Server Objects"),
        ("highlevel/server_variables.py", "highlevel-server-variables", "Server Variables"),
        ("highlevel/server_methods.py", "highlevel-server-methods", "Server Methods"),
        ("highlevel/implement_objtype.py", "highlevel-server-implement-objtype", "Server ObjectType Implementation"),
        ("highlevel/implement_readwrite.py", "highlevel-server-implement-readwrite", "Server Variable Read/Write Override"),
        ("highlevel/server_async.py", "highlevel-server-async", "Server Async"),

        ("sim_examples/client/basic_sim_client.py", "highlevel-pump-client", "Pump Simulation Example: Client"),
        ("sim_examples/server/basic_sim_server.py", "highlevel-pump-server", "Pump Simulation Example: Server"),
        ("example-server/client.py", "highlevel-distilling-client", "Distilling Simulation Example: Client"),
        ("example-server/server.py", "highlevel-distilling-server", "Distilling Simulation Example: Server"),
        ("highlevel/server_sortingline_vc.py", "highlevel-sorting-line-server", "Sorting Line Example: Server"),
        ("highlevel/controller_sortingline_vc.py", "highlevel-sorting-line-controller", "Sorting Line Example: Controller"),
        ("highlevel/client_sortingline_vc.py", "highlevel-sorting-line-client", "Sorting Line Example: Client")
    ]
}


# ---------------------------------------------------------------------------
# Marker parsing
# ---------------------------------------------------------------------------
# Recognise "# BEGIN MD", "# BEGIN CODE" (with optional trailing whitespace
# and any amount of leading whitespace) and the matching "# END MD" /
# "# END CODE".  Capture the marker keyword so we can decide whether the
# block is markdown or code.
_MARKER_RE = re.compile(
    r"^(?P<indent>\s*)#\s*BEGIN\s+(?P<kind>MD|CODE)\s*$"
)
_END_RE = re.compile(
    r"^(?P<indent>\s*)#\s*END\s+(?P<kind>MD|CODE)\s*$"
)


@dataclass
class Block:
    """A single marker-delimited block from a .py file."""
    kind: str            # "MD" or "CODE"
    lines: list[str] = field(default_factory=list)


@dataclass
class ParsedExample:
    """Result of scanning one example script."""
    title: str
    docstring: str | None
    blocks: list[Block]
    raw_source: str      # original .py contents, used for the "Full source" block


def _extract_docstring(source: str) -> str | None:
    """Return the module docstring, or ``None`` if there isn't one."""
    # Match the first triple-quoted string after optional shebang / encoding.
    m = re.search(r'^\s*(?:"""|\'\'\')(?P<body>.*?)(?:"""|\'\'\')',
                  source, flags=re.DOTALL | re.MULTILINE)
    return m.group("body").strip() if m else None


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
                raise ValueError(
                    f"{path}: mismatched marker: {line!r}"
                )
            continue
        if current is not None:
            current.lines.append(line)

    if current is not None:
        raise ValueError(f"{path}: unterminated marker: BEGIN {current.kind}")

    return ParsedExample(title=title, docstring=docstring,
                         blocks=blocks, raw_source=raw)


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------
def _strip_markers(source: str) -> str:
    """Strip marker regions from ``source`` for the source-code dump.

    * ``# BEGIN MD`` … ``# END MD`` — the whole block (both marker lines
      and every line between them) is removed; the descriptive text
      belongs in the prose, not the source listing.
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


def render_markdown(parsed: ParsedExample) -> str:
    """Build the full markdown page for one example."""
    parts: list[str] = []

    # Module docstring becomes the lead paragraph.
    if parsed.docstring:
        parts.append(parsed.docstring)
        parts.append("")

    # First MD block (if any) is treated as a "Source layout / import"
    # intro. Subsequent blocks alternate MD explanation + CODE snippet
    # in the order they appear.
    for block in parsed.blocks:
        if block.kind == "MD":
            parts.append(_render_md_block(block))
        else:
            parts.append(_render_code_block(block))
        parts.append("")

    # Always append the full source for readers who want to copy-paste.
    # Both marker comments and the descriptive ``# BEGIN MD`` … ``# END MD``
    # blocks are stripped so the listing matches a clean copy of the script.
    parts.append("## Complete Source Code")
    parts.append("")
    parts.append("```python")
    parts.append(_strip_markers(parsed.raw_source).rstrip())
    parts.append("```")
    parts.append("")
    return "\n".join(parts)


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


def _safe_filename(slug: str) -> str:
    """Ensure the slug is filesystem-safe."""
    return slug.replace("/", "_")


def generate_pages(whitelist: dict[str, list[tuple[str, str, str]]]
                   ) -> list[GeneratedPage]:
    """Build (but don't write) the pages for every whitelisted example.

    ``whitelist`` maps a section label to a list of
    ``(relative_path, slug, title)`` tuples.
    """
    pages: list[GeneratedPage] = []
    for section, entries in whitelist.items():
        for rel_path, slug, title in entries:
            src = EXAMPLES_ROOT / rel_path
            if not src.exists():
                raise FileNotFoundError(
                    f"whitelisted example not found: {src}"
                )
            parsed = parse_example(src, title=title)
            body = render_markdown(parsed)
            out_path = OUTPUT_DIR / f"{_safe_filename(slug)}.md"
            pages.append(GeneratedPage(slug=slug, title=title,
                                       section=section,
                                       path=out_path, body=body))
    return pages


def write_pages(pages: Iterable[GeneratedPage]) -> None:
    """Write all generated pages to ``docs/examples2/``."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for page in pages:
        page.path.write_text(page.body, encoding="utf-8")


def _toml_escape(label: str) -> str:
    """Quote a label for the zensical.toml nav format."""
    # The format requires the literal value on the right of '=' with
    # surrounding double quotes — escape any embedded double quotes.
    return label.replace("\\", "\\\\").replace('"', '\\"')


def print_nav_block(pages: Sequence[GeneratedPage]) -> None:
    """Print the TOML block to replace the Examples section of zensical.toml.

    Pages are grouped under their WHITELIST section label.  Paths are
    written relative to zensical's ``docs_dir`` (defaults to ``docs/``),
    so the leading ``docs/`` segment is stripped.
    """
    print("# Replace the \"Examples\" block in zensical.toml with the following:")
    print('{ "Examples" = [')
    print('    "examples.md",')

    # Group pages by section, preserving WHITELIST insertion order.
    by_section: dict[str, list[GeneratedPage]] = {}
    section_order: list[str] = []
    for page in pages:
        section = getattr(page, "section", "")
        if section not in by_section:
            by_section[section] = []
            section_order.append(section)
        by_section[section].append(page)

    for section in section_order:
        section_pages = by_section[section]
        if not section:
            for page in section_pages:
                rel = Path("examples2",
                           f"{_safe_filename(page.slug)}.md").as_posix()
                print(f'    {{ "{_toml_escape(page.title)}" = "{rel}" }},')
            continue
        print(f'    {{ "{_toml_escape(section)}" = [')
        for page in section_pages:
            rel = Path("examples2",
                       f"{_safe_filename(page.slug)}.md").as_posix()
            print(f'        {{ "{_toml_escape(page.title)}" = "{rel}" }},')
        print('    ]},')

    print(']},')
    print()


def _check_staleness(pages: Sequence[GeneratedPage]) -> int:
    """Exit code 1 if any existing file is out of date."""
    stale: list[Path] = []
    for page in pages:
        if not page.path.exists():
            stale.append(page.path)
            continue
        if page.path.read_text(encoding="utf-8") != page.body:
            stale.append(page.path)
    if stale:
        print("Stale generated files (re-run without --check):",
              file=sys.stderr)
        for p in stale:
            print(f"  {p.relative_to(REPO_ROOT)}", file=sys.stderr)
        return 1
    return 0


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true",
                        help="Only print the nav block; do not write files.")
    parser.add_argument("--check", action="store_true",
                        help="Exit non-zero if any generated file is stale.")
    args = parser.parse_args(argv)

    pages = generate_pages(WHITELIST)

    if args.dry_run:
        print_nav_block(pages)
        return 0

    if args.check:
        rc = _check_staleness(pages)
        print_nav_block(pages)
        return rc

    write_pages(pages)
    print(f"Wrote {len(pages)} page(s) to "
          f"{OUTPUT_DIR.relative_to(REPO_ROOT)}/")
    print_nav_block(pages)
    return 0


if __name__ == "__main__":
    sys.exit(main())