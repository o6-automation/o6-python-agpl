"""Generate the public API reference from the reviewed API inventory."""

from __future__ import annotations

import argparse
import shutil
import sys
import unicodedata
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT = BASE_DIR.parent
sys.path.insert(0, str(ROOT))

from tools.api_manifest import CANONICAL_PATHS, PUBLIC_MODULES  # noqa: E402

MODULE_PATHS = frozenset(f"o6.{name}" for name in PUBLIC_MODULES)
DOCUMENTED_PATHS = tuple(path for path in CANONICAL_PATHS if path not in MODULE_PATHS)
MANUAL_PATHS = frozenset(("o6.ns.filter", "o6.ns.register"))


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


def _render_page(path: str) -> str:
    name = path.rsplit(".", 1)[-1]
    if path.count(".") == 1 or path in MANUAL_PATHS:
        return "\n".join(
            (
                f"# {name}",
                "",
                f"Canonical path: `{path}`",
                "",
                "This symbol is part of the root convenience API. Its behavior is "
                "documented in the relevant client, server, node, namespace, or "
                "authoring guide.",
                "",
            )
        )
    show_signature = not path.startswith("o6.node.")
    return "\n".join(
        (
            f"# {name}",
            "",
            f"Canonical path: `{path}`",
            "",
            f"::: {path}",
            "    options:",
            "      show_root_heading: false",
            "      show_source: false",
            "      show_category_heading: true",
            "      members_order: source",
            "      inherited_members: true",
            f"      show_signature: {str(show_signature).lower()}",
            "      separate_signature: true",
            "      show_symbol_type_heading: true",
            "",
        )
    )


def _render_index(paths: tuple[str, ...]) -> str:
    lines = [
        "# API Reference",
        "",
        "The supported API, grouped by canonical module. Root shortcuts are "
        "documented on the canonical module entry.",
        "",
    ]
    current_module = ""
    for path in sorted(paths, key=lambda value: (value.rpartition(".")[0], value.lower())):
        module, _, name = path.rpartition(".")
        if module != current_module:
            lines.extend((f"## `{module}`", ""))
            current_module = module
        lines.append(f"- [`{name}`]({_slug(path)}.md) — `{path}` ({_kind(path)})")
    lines.append("")
    return "\n".join(lines)


def generate(output_dir_name: str = "api_reference") -> None:
    output_dir = BASE_DIR / output_dir_name
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    slugs: dict[str, str] = {}
    for path in DOCUMENTED_PATHS:
        slug = _slug(path)
        if previous := slugs.get(slug):
            raise SystemExit(f"[gen-api] URL collision: {previous} and {path}")
        slugs[slug] = path
        (output_dir / f"{slug}.md").write_text(_render_page(path), encoding="utf-8")

    (output_dir / "index.md").write_text(_render_index(DOCUMENTED_PATHS), encoding="utf-8")
    print(f"[gen-api] wrote {len(DOCUMENTED_PATHS)} canonical pages + index → {output_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-o", "--output-dir", default="api_reference")
    args = parser.parse_args()
    generate(args.output_dir)


if __name__ == "__main__":
    main()
