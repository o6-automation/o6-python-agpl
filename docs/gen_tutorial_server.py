#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""Publish the tutorial example server into the docs.

The runnable source of truth is ``examples/tutorial-server/`` -- ``server.py``
plus the ``sim.py`` it imports. That is what ``tests/check_tutorials.py`` starts
the client tutorials against, so it cannot silently rot. This script publishes
those two files two ways:

* copies each one to ``docs/tutorials/``, which the site serves so the page can
  link them as downloads, and
* injects each one as a fenced ``python`` block into ``docs/tutorials/setup.md``,
  between its ``BEGIN GENERATED`` / ``END GENERATED`` markers.

Both outputs go through :func:`strip_markers`, which drops the
``BEGIN``/``END CODE``/``MD`` comments that only ``docs/gen_examples.py`` cares
about, so what readers download has no build scaffolding in it. Download and
listing are therefore identical to each other, and differ from the repository
files by those comment lines alone.

The prose around the markers is hand-written; only the code blocks are replaced.

Usage::

    .venv/bin/python3 docs/gen_tutorial_server.py            # write the outputs
    .venv/bin/python3 docs/gen_tutorial_server.py --check     # exit 1 if stale

Run from the repository root.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# ``docs/gen_examples.py`` uses these comments to slice an example into prose and
# code. They are noise in a file someone is about to download and run.
LITERATE_MARKER_RE = re.compile(r"^#\s*(?:BEGIN|END)\s+(?:CODE|MD)\s*$")

# ``__file__`` lives in ``docs/``, so its parent's parent is the repo root.
REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO_ROOT / "examples" / "tutorial-server"
DOCS_DIR = REPO_ROOT / "docs" / "tutorials"
PAGE = DOCS_DIR / "setup.md"

# The files readers can download, in the order the page presents them. Linking
# them from the site rather than from a repository keeps the links working
# regardless of how the repository is laid out or mirrored.
PUBLISHED = ("server.py", "sim.py", "ui.py")

# Of those, the ones the page shows in full. ``ui.py`` is an optional extra, so
# it is offered as a download without a listing.
LISTED = ("server.py", "sim.py")


def markers(name: str) -> tuple[str, str]:
    """Return the begin/end marker pair delimiting ``name``'s code block."""
    return f"<!-- BEGIN GENERATED: {name} -->", f"<!-- END GENERATED: {name} -->"


def strip_markers(source: str) -> str:
    """Return ``source`` without the literate-programming marker comments.

    A marker sitting on its own between two blank lines would leave a doubled
    blank behind, so one of the two goes with it. That keeps the result formatted
    the way the source was: two blank lines between top-level definitions, one
    elsewhere.
    """
    lines = source.splitlines()
    kept: list[str] = []
    for index, line in enumerate(lines):
        if LITERATE_MARKER_RE.match(line.strip()):
            blank_before = bool(kept) and not kept[-1].strip()
            blank_after = index + 1 < len(lines) and not lines[index + 1].strip()
            if blank_before and blank_after:
                kept.pop()
            continue
        kept.append(line)
    return re.sub(r"\n{4,}", "\n\n\n", "\n".join(kept)).rstrip("\n") + "\n"


def render_block(name: str, source: str) -> str:
    """Wrap a file's source in a fenced, titled ``python`` block."""
    return f'```python title="{name}"\n{source.rstrip()}\n```'


def reindent(block: str, indent: str) -> str:
    """Indent every non-empty line of ``block`` by ``indent``.

    The markers sit inside collapsible ``???`` blocks on the page, whose content
    has to be indented to belong to them.
    """
    return "\n".join(indent + line if line.strip() else "" for line in block.splitlines())


def build() -> dict[Path, str]:
    """Return the desired content of every generated file."""
    generated: dict[Path, str] = {}
    page = PAGE.read_text()

    for name in PUBLISHED:
        source = strip_markers((SOURCE_DIR / name).read_text())
        generated[DOCS_DIR / name] = source

        if name not in LISTED:
            continue

        begin, end = markers(name)
        if begin not in page or end not in page:
            sys.exit(f"{PAGE.relative_to(REPO_ROOT)} is missing the markers for {name}")
        head, _, rest = page.partition(begin)
        _, _, tail = rest.partition(end)
        # Whatever whitespace precedes the marker also indents the block.
        indent = head[head.rfind("\n") + 1 :]
        body = reindent(render_block(name, source), indent)
        page = f"{head}{begin}\n{body}\n{indent}{end}{tail}"

    generated[PAGE] = page
    return generated


def read_or_none(path: Path) -> str | None:
    """Return the file's text, or None if it does not exist yet."""
    try:
        return path.read_text()
    except FileNotFoundError:
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit non-zero if any generated file is out of date",
    )
    args = parser.parse_args()

    generated = build()

    if args.check:
        stale = [path for path, content in generated.items() if read_or_none(path) != content]
        for path in stale:
            print(f"stale: {path.relative_to(REPO_ROOT)}")
        if stale:
            print("\nRun: .venv/bin/python3 docs/gen_tutorial_server.py")
            return 1
        print("tutorial server docs are up to date")
        return 0

    for path, content in generated.items():
        path.write_text(content)
        print(f"wrote {path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
