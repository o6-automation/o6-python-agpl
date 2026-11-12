#!/usr/bin/env python3
### This Source Code Form is subject to the terms of the Mozilla Public
### License, v. 2.0. If a copy of the MPL was not distributed with this
### file, You can obtain one at http://mozilla.org/MPL/2.0/.

###    Copyright 2026 (c) o6-Automation GmbH (Author: Daniel Opitz)

"""Build and publish docs to https://docs.o6-automation.com/o6-python/.

Run with the Python environment containing requirements.txt dependencies::

    .venv/bin/python tools/deploy_docs.py --build-only
    .venv/bin/python tools/deploy_docs.py --version 1.2.3

Publishing requires SSH access to the shared docs repository. The optional
version labels the commit only; the site is always published at /o6-python/.
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
DOCS_PATH = "o6-python"
PAGES_REPO = "git@github.com:o6-automation/o6-automation.github.io.git"


def run(*args: str, cwd: Path = ROOT) -> None:
    subprocess.run(args, cwd=cwd, check=True)


def build() -> None:
    run(sys.executable, "tools/stage_docs_theme.py")
    run(sys.executable, "docs/gen_tutorial_server.py")
    run(sys.executable, "-m", "zensical", "build", "-f", "zensical.toml", "--clean")
    run(sys.executable, "docs/gen_examples.py", "--copy-markdown-downloads", str(SITE))


def publish(version: str = "") -> None:
    if not (SITE / "index.html").is_file():
        raise RuntimeError("Build the docs before publishing: site/index.html is missing")
    with TemporaryDirectory(prefix="o6-python-docs-") as directory:
        checkout = Path(directory) / "site"
        run("git", "clone", "--depth", "1", "--branch", "main", PAGES_REPO, str(checkout))
        destination = checkout / DOCS_PATH
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(SITE, destination)
        (checkout / ".nojekyll").touch()

        # Preserve the old landing-page URL, as the GitHub Actions deploy does.
        latest = destination / "latest"
        latest.mkdir(exist_ok=True)
        (latest / "index.html").write_text(
            '<meta http-equiv="refresh" content="0; url=../">\n', encoding="utf-8",
        )

        run("git", "add", "-A", "--", DOCS_PATH, ".nojekyll", cwd=checkout)
        changes = subprocess.check_output(
            ["git", "diff", "--cached", "--name-only"], cwd=checkout,
        )
        if not changes:
            print("Docs are already up to date.")
            return
        run("git", "config", "user.name", "o6 Automation GmbH", cwd=checkout)
        run("git", "config", "user.email", "contact@o6-automation.com", cwd=checkout)
        message = f"Update {DOCS_PATH} docs" + (f" for {version}" if version else "")
        run("git", "-c", "commit.gpgsign=false", "commit", "-m", message, cwd=checkout)
        run("git", "push", "origin", "main", cwd=checkout)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-only", action="store_true", help="build without pushing")
    parser.add_argument("--version", default="", help="release label for the commit message")
    args = parser.parse_args()
    build()
    if not args.build_only:
        publish(args.version)


if __name__ == "__main__":
    main()
