#!/usr/bin/env python3
# Copyright (c) 2026 o6 Automation GmbH
#
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

"""Stage the shared o6 Zensical theme into the documentation source tree.

The theme lives in the private ``o6-zensical-theme`` submodule and owns
presentation only: the corporate palette, ABC Diatype typography, header,
navigation, and footer styling. Zensical resolves ``extra_css`` relative to
its ``docs_dir``, and the stylesheet references its fonts as
``../fonts/abc-diatype/...``, so both have to sit inside ``docs/`` before a
build.

Run this before ``zensical build`` or ``zensical serve``::

    python tools/stage_docs_theme.py

The staged copies are build artifacts and are ignored by git; the submodule
commit is the theme version.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
THEME_ROOT = REPO_ROOT / "external" / "o6-zensical-theme"
DOCS_DIR = REPO_ROOT / "docs"

STYLESHEET = "o6-zensical-theme.css"
FONT_DIR = "abc-diatype"


def stage(theme_root: Path, docs_dir: Path) -> None:
    """Copy the theme stylesheet and fonts into ``docs_dir``."""
    css_src = theme_root / "theme" / STYLESHEET
    fonts_src = theme_root / "fonts" / FONT_DIR
    if not css_src.is_file() or not fonts_src.is_dir():
        raise SystemExit(
            f"Theme not found under {theme_root}.\n"
            "Initialize the submodule first:\n"
            "  git submodule update --init external/o6-zensical-theme"
        )

    css_dest = docs_dir / "stylesheets" / STYLESHEET
    fonts_dest = docs_dir / "fonts" / FONT_DIR

    css_dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(css_src, css_dest)
    shutil.copytree(fonts_src, fonts_dest, dirs_exist_ok=True)

    print(f"Staged {css_dest.relative_to(REPO_ROOT)}")
    print(f"Staged {fonts_dest.relative_to(REPO_ROOT)}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--theme-root",
        type=Path,
        default=THEME_ROOT,
        help="path to the o6-zensical-theme checkout (default: the submodule)",
    )
    parser.add_argument(
        "--docs-dir",
        type=Path,
        default=DOCS_DIR,
        help="Zensical docs_dir to stage into (default: docs/)",
    )
    args = parser.parse_args(argv)

    stage(args.theme_root.resolve(), args.docs_dir.resolve())
    return 0


if __name__ == "__main__":
    sys.exit(main())
