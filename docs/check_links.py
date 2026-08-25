#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""Check every internal link in the built docs site.

``zensical build`` reports "No issues found" for pages that link to a heading
that does not exist, or to a page in a repository that has since been
reorganised. This script walks the generated HTML instead of the Markdown, so it
sees exactly what a reader's browser would follow:

* **paths** -- every ``href``/``src`` that stays on the site has to resolve to a
  file (or to a directory holding an ``index.html``),
* **fragments** -- ``#anchor`` has to match an ``id``/``name`` in the target
  page, including for same-page links.

Links to other sites are left alone; use ``--report-external`` to list them
without fetching anything.

Usage::

    .venv/bin/zensical build                       # the site has to exist first
    .venv/bin/python3 docs/check_links.py          # exits 1 on any broken link
    .venv/bin/python3 docs/check_links.py --all     # don't truncate the report
    .venv/bin/python3 docs/check_links.py --site out --base-path /docs/

Run from the repository root.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.parse
from collections import defaultdict
from pathlib import Path

# ``__file__`` lives in ``docs/``, so its parent's parent is the repo root.
REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SITE = REPO_ROOT / "site"
ZENSICAL_TOML = REPO_ROOT / "zensical.toml"

# Schemes that never point at a file in the built site.
EXTERNAL_PREFIXES = ("http://", "https://", "//", "mailto:", "tel:", "data:", "javascript:")

# Fragments the theme emits itself. "__skip" is the "skip to content" link, and
# the theme only emits the matching target on some pages -- a real dangling link,
# but not one the docs can fix, so it is reported separately from authored links.
# Pass --strict to have it count as a failure.
THEME_FRAGMENTS = frozenset({"__skip"})

LINK_RE = re.compile(r'(?:href|src)="([^"]+)"')
ANCHOR_RE = re.compile(r'\s(?:id|name)="([^"]+)"')
SITE_URL_RE = re.compile(r'^\s*site_url\s*=\s*"([^"]+)"', re.MULTILINE)

# How many findings of each kind to print before truncating.
REPORT_LIMIT = 25


def site_base_path() -> str:
    """Return the URL path the site is deployed under, e.g. ``/o6-python/``.

    Pages contain a few root-absolute links (the 404 page's assets, for
    instance). They resolve against the deployment root, not the filesystem
    root, so the prefix has to come off before they can be looked up.
    """
    try:
        match = SITE_URL_RE.search(ZENSICAL_TOML.read_text())
    except FileNotFoundError:
        return "/"
    if not match:
        return "/"
    path = urllib.parse.urlsplit(match.group(1)).path
    return path if path.endswith("/") else path + "/"


class LinkChecker:
    """Resolves the links of a built site against the files it contains."""

    def __init__(self, site: Path, base_path: str) -> None:
        self.site = site
        self.base_path = base_path
        self.anchors: dict[Path, set[str]] = {}
        self.broken_paths: list[tuple[Path, str]] = []
        self.broken_anchors: list[tuple[Path, str]] = []
        self.theme_anchors: list[tuple[Path, str]] = []
        self.external: set[str] = set()
        self.pages = sorted(site.rglob("*.html"))
        self.checked = 0

    def anchors_of(self, page: Path) -> set[str]:
        """Return the anchor names a page defines, reading it at most once."""
        if page not in self.anchors:
            self.anchors[page] = set(ANCHOR_RE.findall(page.read_text(errors="ignore")))
        return self.anchors[page]

    def resolve(self, page: Path, path_part: str) -> Path:
        """Return the file a link's path component points at."""
        if path_part.startswith(self.base_path):
            target = self.site / path_part[len(self.base_path) :]
        elif path_part.startswith("/"):
            # A root-absolute link outside the deployment prefix: still worth
            # resolving against the site root rather than silently passing.
            target = self.site / path_part.lstrip("/")
        else:
            target = page.parent / path_part
        target = Path(urllib.parse.unquote(str(target)))
        return target / "index.html" if target.is_dir() else target

    def check_page(self, page: Path) -> None:
        """Check every link on one page."""
        for link in LINK_RE.findall(page.read_text(errors="ignore")):
            if link.startswith(EXTERNAL_PREFIXES):
                self.external.add(link)
                continue

            path_part, _, fragment = link.partition("#")
            path_part = path_part.partition("?")[0]
            self.checked += 1

            # A bare "#fragment" points into the page that contains it.
            target = page if not path_part else self.resolve(page, path_part)

            if not target.exists():
                self.broken_paths.append((page, link))
            elif fragment and target.suffix == ".html" and fragment not in self.anchors_of(target):
                bucket = self.theme_anchors if fragment in THEME_FRAGMENTS else self.broken_anchors
                bucket.append((page, link))

    def run(self) -> None:
        """Check every page in the site."""
        for page in self.pages:
            self.check_page(page)


def report(checker: LinkChecker, limit: int | None) -> None:
    """Print the findings, grouped by the page they were found on."""
    for label, findings in (
        ("broken paths", checker.broken_paths),
        ("broken anchors", checker.broken_anchors),
    ):
        print(f"\n{len(findings)} {label}:")
        by_page: dict[Path, list[str]] = defaultdict(list)
        for page, link in findings:
            by_page[page].append(link)

        shown = 0
        for page, links in sorted(by_page.items()):
            for link in links:
                if limit is not None and shown >= limit:
                    print(f"  ... and {len(findings) - shown} more (pass --all to see them)")
                    break
                print(f"  {page.relative_to(checker.site)} -> {link}")
                shown += 1
            else:
                continue
            break


def main() -> int:
    parser = argparse.ArgumentParser(description="Check internal links in the built docs site")
    parser.add_argument(
        "--site",
        type=Path,
        default=DEFAULT_SITE,
        help=f"the built site to check (default {DEFAULT_SITE.name}/)",
    )
    parser.add_argument(
        "--base-path",
        help="URL path the site is deployed under (default: read from zensical.toml)",
    )
    parser.add_argument("--all", action="store_true", help="print every finding, untruncated")
    parser.add_argument(
        "--strict",
        action="store_true",
        help=f"also fail on theme-emitted fragments ({', '.join(sorted(THEME_FRAGMENTS))})",
    )
    parser.add_argument(
        "--report-external",
        action="store_true",
        help="also list the external links found, without fetching them",
    )
    args = parser.parse_args()

    if not args.site.is_dir():
        print(f"{args.site} does not exist -- run 'zensical build' first", file=sys.stderr)
        return 2

    checker = LinkChecker(args.site, args.base_path or site_base_path())
    checker.run()

    print(
        f"checked {checker.checked} internal links across {len(checker.pages)} pages "
        f"(base path {checker.base_path})"
    )

    if args.report_external:
        print(f"\n{len(checker.external)} external links (not fetched):")
        for link in sorted(checker.external):
            print(f"  {link}")

    if args.strict:
        checker.broken_anchors.extend(checker.theme_anchors)
        checker.theme_anchors.clear()
    elif checker.theme_anchors:
        print(
            f"ignoring {len(checker.theme_anchors)} theme-emitted dangling "
            "fragment(s); pass --strict to include them"
        )

    if not checker.broken_paths and not checker.broken_anchors:
        print("no broken internal links")
        return 0

    report(checker, None if args.all else REPORT_LIMIT)
    return 1


if __name__ == "__main__":
    sys.exit(main())
