"""Generate the companion-specification reference from the generated namespaces.

The pages under ``docs/ns_reference`` are produced from the ``.pyi`` stubs that
the NodeSet compiler writes next to each generated namespace module. Those stubs
carry the ``Description`` text of the companion specification itself as Python
docstrings, so every word on these pages comes from the specification, never
from this repository.

Only namespaces whose stub actually carries a description get a page, and within
a page only the documented types are listed. A namespace the compiler could not
describe is skipped rather than published empty.

This reference is deliberately separate from ``docs/api_reference``, which
documents the ``o6`` package itself.
"""

from __future__ import annotations

import argparse
import ast
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT = BASE_DIR.parent
NS_DIR = ROOT / "o6" / "ns"
sys.path.insert(0, str(ROOT))


@dataclass(frozen=True)
class Namespace:
    """One generated namespace and the types its stub describes."""

    shortname: str
    uri: str
    version: str
    publicationDate: str
    documented: tuple[str, ...]


def _metadata(package: Path) -> dict[str, str]:
    """Read the ``_initialize_namespace`` call of a generated namespace."""
    init = package / "__init__.py"
    if not init.is_file():
        return {}
    tree = ast.parse(init.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        function = node.func
        name = function.attr if isinstance(function, ast.Attribute) else getattr(function, "id", "")
        if name != "_initialize_namespace":
            continue
        return {
            keyword.arg: keyword.value.value
            for keyword in node.keywords
            if keyword.arg and isinstance(keyword.value, ast.Constant)
            if isinstance(keyword.value.value, str)
        }
    return {}


def _documented_types(stub: Path) -> tuple[str, ...]:
    """Return the classes in a stub that carry a specification description."""
    tree = ast.parse(stub.read_text(encoding="utf-8"))
    return tuple(
        node.name
        for node in tree.body
        if isinstance(node, ast.ClassDef) and ast.get_docstring(node)
    )


def collect() -> tuple[Namespace, ...]:
    """Find every generated namespace whose stub describes at least one type."""
    namespaces = []
    for stub in sorted(NS_DIR.glob("*/datatypes.pyi")):
        documented = _documented_types(stub)
        if not documented:
            continue
        package = stub.parent
        metadata = _metadata(package)
        namespaces.append(
            Namespace(
                shortname=metadata.get("shortname", package.name),
                uri=metadata.get("uri", ""),
                version=metadata.get("version", ""),
                publicationDate=metadata.get("publication_date", ""),
                documented=documented,
            )
        )
    return tuple(namespaces)


def _render_page(namespace: Namespace) -> str:
    lines = [
        f"# {namespace.shortname}",
        "",
        f"Import as `o6.ns.{namespace.shortname}`.",
        "",
        "| | |",
        "|---|---|",
    ]
    if namespace.uri:
        lines.append(f"| Namespace URI | `{namespace.uri}` |")
    if namespace.version:
        lines.append(f"| Version | {namespace.version} |")
    if namespace.publicationDate:
        lines.append(f"| Publication date | {namespace.publicationDate[:10]} |")
    lines += [
        f"| Described DataTypes | {len(namespace.documented)} |",
        "",
        "The descriptions below are the companion specification's own, as "
        "compiled into the generated namespace module.",
        "",
    ]
    for name in namespace.documented:
        lines += [
            f"::: o6.ns.{namespace.shortname}.datatypes.{name}",
            "    options:",
            "      show_root_heading: true",
            "      show_root_full_path: false",
            "      heading_level: 2",
            "      show_source: false",
            "      show_category_heading: false",
            "      show_symbol_type_heading: true",
            "      members_order: source",
            "      inherited_members: false",
            "      separate_signature: true",
            "      show_signature_annotations: true",
            # Members of a described type are listed with their declared OPC UA
            # type even though the compiler emits no per-member description.
            "      show_if_no_docstring: true",
            "      filters:",
            '        - "!^_(?!_)"',
            "",
        ]
    return "\n".join(lines)


def _render_index(namespaces: tuple[Namespace, ...]) -> str:
    lines = [
        "# Companion Spec Reference",
        "",
        "The OPC UA companion specifications packaged with o6\\\\Python, as "
        "compiled by the NodeSet compiler. Every description on these pages is "
        "the specification's own `Description` text, carried through into the "
        "generated namespace modules.",
        "",
        "This reference covers the DataTypes the compiler describes. A "
        "specification whose NodeSet supplies no descriptions has no page here, "
        "even though its namespace is still packaged and importable — "
        "`o6.ns` lists everything that ships, described or not.",
        "",
        "For the `o6` package itself, see the "
        "[API Reference](../api_reference/index.md).",
        "",
        "| Namespace | Version | Described DataTypes | URI |",
        "|---|---|---|---|",
    ]
    for namespace in sorted(namespaces, key=lambda item: item.shortname):
        lines.append(
            f"| [`{namespace.shortname}`]({namespace.shortname}.md) "
            f"| {namespace.version} | {len(namespace.documented)} "
            f"| `{namespace.uri}` |"
        )
    lines.append("")
    return "\n".join(lines)


def generate(output_dir_name: str = "ns_reference") -> None:
    namespaces = collect()
    output_dir = BASE_DIR / output_dir_name
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    for namespace in namespaces:
        (output_dir / f"{namespace.shortname}.md").write_text(
            _render_page(namespace), encoding="utf-8"
        )
    (output_dir / "index.md").write_text(_render_index(namespaces), encoding="utf-8")

    described = sum(len(namespace.documented) for namespace in namespaces)
    print(
        f"[gen-ns] wrote {len(namespaces)} namespace pages + index "
        f"({described} described types) → {output_dir}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-o", "--output-dir", default="ns_reference")
    args = parser.parse_args()
    generate(args.output_dir)


if __name__ == "__main__":
    main()
