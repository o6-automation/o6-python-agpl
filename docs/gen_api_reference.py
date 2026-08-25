"""Generate the public API reference from the reviewed API inventory.

Every page in ``docs/api_reference`` is written by this script and holds nothing
but a heading, the canonical import path, and an ``mkdocstrings`` directive.
All prose therefore belongs in the docstring of the documented symbol, never in
the generated Markdown. The narrative guides (``docs/manual/client/``,
``docs/manual/server/``, the tutorials) are separate hand-written pages that this
script neither reads nor overwrites.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import unicodedata
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT = BASE_DIR.parent
sys.path.insert(0, str(ROOT))

from tools.api_manifest import CANONICAL_PATHS, PUBLIC_MODULES, ROOT_ALIASES  # noqa: E402

MODULE_PATHS = frozenset(f"o6.{name}" for name in PUBLIC_MODULES)
DOCUMENTED_PATHS = tuple(path for path in CANONICAL_PATHS if path not in MODULE_PATHS)

# ``o6.ns`` is a module object of a private ModuleType subclass, so its call
# syntax resolves statically only through the class that defines it.
TARGET_OVERRIDES = {
    "o6.ns.filter": "o6.ns._NamespacePackage.filter",
    "o6.ns.register": "o6.ns._NamespacePackage.register",
}

# The root shortcut for each canonical path, e.g. ``o6.Client`` for
# ``o6.client.Client``.
SHORTCUTS = {canonical: f"o6.{name}" for name, canonical in ROOT_ALIASES.items()}


def _slug(path: str) -> str:
    """Return the stable short-name URL used by the API reference."""
    name = path.rsplit(".", 1)[-1]
    normalized = unicodedata.normalize("NFKD", name)
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii")
    slug = "".join(char.lower() if char.isalnum() else "-" for char in ascii_only)
    return "-".join(part for part in slug.split("-") if part) or "symbol"


def _kind(path: str) -> str:
    name = path.rsplit(".", 1)[-1]
    if name == "roles":
        return "object"
    if name[:1].isupper():
        return "class or type"
    return "function"


def _slugs(paths: tuple[str, ...]) -> dict[str, str]:
    """Map every documented path to a unique URL slug.

    Names that differ only in capitalization (``OffsetTable`` and
    ``offsetTable``) would claim the same URL, so every member of such a group
    is qualified by its kind instead of one of them silently winning.
    """
    claims: dict[str, list[str]] = {}
    for path in paths:
        claims.setdefault(_slug(path), []).append(path)
    slugs: dict[str, str] = {}
    for slug, claimants in claims.items():
        if len(claimants) == 1:
            slugs[claimants[0]] = slug
            continue
        for path in claimants:
            slugs[path] = f"{slug}-{_kind(path).split()[0]}"
    return slugs


# Dunders that implement a Python protocol without adding anything to the OPC UA
# API. Behaviour worth knowing about (`__call__`, `__getitem__`, `__await__`, the
# context-manager pair) stays visible and is documented on the member itself.
_UNINTERESTING_DUNDERS = (
    "str",
    "repr",
    "hash",
    "eq",
    "ne",
    "lt",
    "le",
    "gt",
    "ge",
    "bool",
    "int",
    "index",
    "format",
    "dir",
    "getattr",
    "setattr",
    "init_subclass",
    "class_getitem",
    "copy",
    "deepcopy",
    "reduce",
)


def _render_page(path: str) -> str:
    name = path.rsplit(".", 1)[-1]
    target = TARGET_OVERRIDES.get(path, path)
    shortcut = SHORTCUTS.get(path)
    lines = [f"# {name}", "", f"Canonical path: `{path}`"]
    if shortcut and shortcut != path:
        lines += ["", f"Root shortcut: `{shortcut}`"]
    lines += [
        "",
        f"::: {target}",
        "    options:",
        # The signature of the documented symbol itself is part of its heading,
        # so the root heading has to be rendered for the page to show one.
        "      show_root_heading: true",
        "      show_root_full_path: false",
        "      heading_level: 2",
        "      show_source: false",
        "      show_category_heading: true",
        "      members_order: source",
        "      inherited_members: true",
        # Enum members and plain data attributes carry their meaning in their
        # name and value, so the reference lists them even without a docstring.
        "      show_if_no_docstring: true",
        "      filters:",
        # A negative lookahead, rather than mkdocstrings' own ``!^_[^_]``
        # default, because ``[^`` starts a footnote reference in Markdown.
        '        - "!^_(?!_)"',
        f'        - "!^__({"|".join(_UNINTERESTING_DUNDERS)})__$"',
        "      show_signature: true",
        "      separate_signature: true",
        "      show_symbol_type_heading: true",
        "",
    ]
    return "\n".join(lines)


def _render_index(paths: tuple[str, ...], slugs: dict[str, str]) -> str:
    lines = [
        "# API Reference",
        "",
        "The supported API, grouped by canonical module. Every page on this "
        "index is generated from the docstrings in the `o6` package.",
        "",
        "Symbols re-exported at the top level are listed under their canonical "
        "module and name the root shortcut on their own page, so "
        "`o6.client.Client` covers `o6.Client`.",
        "",
    ]
    current_module = ""
    for path in sorted(paths, key=lambda value: (value.rpartition(".")[0], value.lower())):
        module, _, name = path.rpartition(".")
        if module != current_module:
            lines.extend((f"## `{module}`", ""))
            current_module = module
        lines.append(f"- [`{name}`]({slugs[path]}.md) — `{path}` ({_kind(path)})")
    lines.append("")
    return "\n".join(lines)


def generate(output_dir_name: str = "api_reference") -> None:
    output_dir = BASE_DIR / output_dir_name
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    slugs = _slugs(DOCUMENTED_PATHS)
    for path, slug in slugs.items():
        (output_dir / f"{slug}.md").write_text(_render_page(path), encoding="utf-8")

    (output_dir / "index.md").write_text(
        _render_index(DOCUMENTED_PATHS, slugs), encoding="utf-8"
    )
    print(f"[gen-api] wrote {len(DOCUMENTED_PATHS)} canonical pages + index → {output_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-o", "--output-dir", default="api_reference")
    args = parser.parse_args()
    generate(args.output_dir)


if __name__ == "__main__":
    main()
