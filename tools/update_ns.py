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

"""
Sync OPC UA companion NodeSets from the deps/UA-Nodeset submodule into
o6/_nodesets/ and regenerate o6/_ns.py.

Usage:
    python tools/update_ns.py        # copy changed XMLs, regen __init__.py
    python tools/update_ns.py --list # show status of all nodesets, no changes
"""

from __future__ import annotations

import argparse
import hashlib
import pprint
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

_TOOLS_DIR = Path(__file__).parent.resolve()
_ROOT = _TOOLS_DIR.parent
_O6_DIR = _ROOT / "o6"
_NODESETS_DIR = _O6_DIR / "_nodesets"
_BUILTIN_PY = _O6_DIR / "_ns.py"
_SUBMODULE_DIR = _ROOT / "deps" / "UA-Nodeset"


# ---------------------------------------------------------------------------
# Whitelist
# ---------------------------------------------------------------------------


@dataclass
class NodeSetSpec:
    # Path inside the repo, e.g. "DI" or "Glass/Flat".
    folder: str
    # Python identifier used for the generated module
    # (o6/namespaces/_nodesets/{short_name}.py).
    short_name: str
    # If True, exclude from the auto-generated _builtin.py (e.g. known segfault).
    skip_builtin: bool = False
    # When non-empty, use this exact filename instead of globbing for *NodeSet2.xml.
    xml_filename: str = ""
    # When True, clear type descriptions before serialization (avoids conflicts
    # with types already registered in the C extension, e.g. ns0).
    skip_types: bool = False
    # Populated at runtime by _resolve_xml_deps:
    depends_on: list[str] = field(default_factory=list)
    model_uri: str = ""


# Dependencies are extracted from XML <RequiredModel> elements at runtime
# by _resolve_xml_deps — no need to maintain them manually here.
NODESETS: list[NodeSetSpec] = [
    # ── Base UA namespace (ns=0) ────────────────────────────────────────────
    NodeSetSpec(
        "Schema",
        "ns0",
        xml_filename="Opc.Ua.NodeSet2.xml",
        skip_types=True,  # ns0 types are built into the C extension
    ),
    # ── Foundation ──────────────────────────────────────────────────────────
    NodeSetSpec("DI", "di"),
    NodeSetSpec("IA", "ia"),
    # ── Machinery ecosystem ─────────────────────────────────────────────────
    NodeSetSpec("Machinery", "machinery"),
    NodeSetSpec("MachineTool", "machine_tool", skip_builtin=True),  # missing ISA95-JOBCONTROL_V2, Machinery/Jobs
    NodeSetSpec("CNC", "cnc"),
    NodeSetSpec("CuttingTool", "cutting_tool", skip_builtin=True),  # missing Machinery/Result, ISA95-JOBCONTROL_V2, Machinery/Jobs, GMS
    NodeSetSpec("LADS", "lads"),
    NodeSetSpec("MachineVision", "machine_vision"),
    NodeSetSpec("Robotics", "robotics"),
    NodeSetSpec("Pumps", "pumps"),
    NodeSetSpec("Weihenstephan", "weihenstephan"),
    NodeSetSpec("Woodworking", "woodworking", skip_builtin=True),  # segfaults C type builder
    NodeSetSpec("MetalForming", "metal_forming", skip_builtin=True),  # missing Dictionary/IRDI, Machinery/ProcessValues
    NodeSetSpec("CommercialKitchenEquipment", "commercial_kitchen"),
    NodeSetSpec("CranesHoists", "cranes_hoists"),
    NodeSetSpec("PlasticsRubber", "plastics_rubber"),
    NodeSetSpec("Powertrain", "powertrain", skip_builtin=True),  # missing FX/Data, FX/AC, Dictionary/IRDI
    NodeSetSpec("Shotblasting", "shotblasting", skip_builtin=True),  # missing ISA95-JOBCONTROL_V2, Machinery/Jobs
    NodeSetSpec("WMTP", "wmtp"),
    # ── Fieldbus / network ──────────────────────────────────────────────────
    NodeSetSpec("PNDRV", "pndrv"),
    NodeSetSpec("PNEM", "pnem"),
    NodeSetSpec("PNENC", "pnenc"),
    NodeSetSpec("PNGSDGM", "pngsdgm"),
    NodeSetSpec("PNRIO", "pnrio"),
    NodeSetSpec("POWERLINK", "powerlink"),
    NodeSetSpec("PROFINET", "profinet"),
    NodeSetSpec("Sercos", "sercos"),
    NodeSetSpec("IOLink", "io_link"),
    # ── Process / industry vertical ─────────────────────────────────────────
    NodeSetSpec("ADI", "adi"),
    NodeSetSpec("PADIM", "padim", skip_builtin=True),  # missing Dictionary/IRDI
    NodeSetSpec("PAEFS", "paefs", skip_builtin=True),  # missing Dictionary/IRDI, Machinery/ProcessValues
    NodeSetSpec("FDI", "fdi"),
    NodeSetSpec("FDT", "fdt"),
    NodeSetSpec("MDIS", "mdis"),
    NodeSetSpec("PLCopen", "plcopen"),
    NodeSetSpec("PackML", "pack_ml"),
    NodeSetSpec("AutoID", "auto_id"),
    NodeSetSpec("CAS", "cas"),
    NodeSetSpec("DEXPI", "dexpi"),
    NodeSetSpec("ECM", "ecm"),
    NodeSetSpec("GMS", "gms"),
    NodeSetSpec("GPOS", "gpos"),
    NodeSetSpec("IJT", "ijt"),
    NodeSetSpec("IREDES", "iredes"),
    NodeSetSpec("ISA-95", "isa95"),
    NodeSetSpec("ISA95-JOBCONTROL", "isa95_jobcontrol"),
    NodeSetSpec("LaserSystems", "laser_systems", skip_builtin=True),  # depends on machine_tool (skipped)
    NodeSetSpec("Mining", "mining"),
    NodeSetSpec("MTConnect", "mt_connect"),
    NodeSetSpec("Onboarding", "onboarding"),
    NodeSetSpec("OpenSCS", "open_scs"),
    NodeSetSpec("RSL", "rsl"),
    NodeSetSpec("Safety", "safety"),
    NodeSetSpec("Scales", "scales"),
    NodeSetSpec("Scheduler", "scheduler"),
    NodeSetSpec("SurfaceTechnology", "surface_technology"),
    NodeSetSpec("TMC", "tmc", skip_builtin=True),  # segfaults C type builder
    NodeSetSpec("TTD", "ttd"),
    NodeSetSpec("WireHarness", "wire_harness"),
    NodeSetSpec("WoT", "wot"),
    # ── Standards / cross-domain ────────────────────────────────────────────
    NodeSetSpec("AMB", "amb"),
    NodeSetSpec("AML", "aml"),
    NodeSetSpec("BACnet", "bacnet"),
    NodeSetSpec("CSPPlusForMachine", "csp_plus"),
    NodeSetSpec("GDS", "gds"),
    NodeSetSpec("I4AAS", "i4aas"),
    NodeSetSpec("IEC61850", "iec61850"),
    NodeSetSpec("UAFX", "uafx"),
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _find_source_xml(folder: str, xml_filename: str = "") -> Optional[Path]:
    source_dir = _SUBMODULE_DIR / folder
    if not source_dir.is_dir():
        return None
    if xml_filename:
        p = source_dir / xml_filename
        return p if p.is_file() else None
    candidates = sorted(source_dir.glob("*NodeSet2.xml"))
    if not candidates:
        return None
    base = folder.split("/")[-1].lower()
    preferred = [c for c in candidates if base in c.name.lower()]
    # Exclude example/test files when a non-example variant exists.
    non_example = [
        c for c in (preferred or candidates)
        if "example" not in c.name.lower()
    ]
    if non_example:
        return non_example[0]
    return preferred[0] if preferred else candidates[0]


def _spec_status(spec: NodeSetSpec) -> str:
    """Return 'ok', 'changed', 'new', or 'missing'."""
    src = _find_source_xml(spec.folder, spec.xml_filename)
    if src is None:
        return "missing"
    ns_path = _NODESETS_DIR / f"{spec.short_name}.py"
    if not ns_path.exists():
        return "new"
    src_hash = _sha256(src)
    for line in ns_path.read_text(encoding="utf-8").splitlines()[:4]:
        if line.startswith("# source-sha256: "):
            stored = line.split(": ", 1)[1].strip()
            return "ok" if stored == src_hash else "changed"
    return "ok"  # no hash stored (old file), assume ok


# ---------------------------------------------------------------------------
# XML dependency extraction
# ---------------------------------------------------------------------------

def _resolve_xml_deps(available: list[NodeSetSpec]) -> list[NodeSetSpec]:
    """Populate depends_on and model_uri on each spec from actual XML RequiredModel declarations."""
    sys.path.insert(0, str(_ROOT))
    from o6._nodeset_parser import extract_model_info

    # Build URI → short_name mapping from all available nodesets
    uri_to_short: dict[str, str] = {}
    for spec in available:
        xml_path = _find_source_xml(spec.folder, spec.xml_filename)
        if xml_path is not None:
            model_uri, _ = extract_model_info(str(xml_path))
            if model_uri:
                uri_to_short[model_uri] = spec.short_name
                spec.model_uri = model_uri

    short_names = {s.short_name for s in available}

    for spec in available:
        xml_path = _find_source_xml(spec.folder, spec.xml_filename)
        if xml_path is None:
            continue
        _, required = extract_model_info(str(xml_path))
        spec.depends_on = [
            uri_to_short[uri]
            for uri, _ver in required
            if uri in uri_to_short and uri_to_short[uri] in short_names
        ]

    return available


# ---------------------------------------------------------------------------
# Code generation
# ---------------------------------------------------------------------------

# Short type codes for serialized node hierarchy.
_NS_NODE_TYPE_CODES: dict[str, str] = {
    "NamespaceObjectNode": "O",
    "NamespaceVariableNode": "V",
    "NamespaceMethodNode": "M",
    "NamespaceObjectTypeNode": "OT",
    "NamespaceDataTypeNode": "D",
    "NamespaceReferenceTypeNode": "RT",
    "NamespaceVariableTypeNode": "VT",
    "NamespaceViewNode": "W",
}


def _serialize_ns_node(ns_node: Any) -> tuple[str, str, dict[str, Any]]:
    """Recursively serialize a NamespaceNode to (type_code, nodeid, {children})."""
    type_code = _NS_NODE_TYPE_CODES.get(type(ns_node).__name__, "O")
    children: dict[str, Any] = {}
    for name, val in vars(ns_node).items():
        if not name.startswith("_"):
            children[name] = _serialize_ns_node(val)
    return (type_code, str(ns_node._nodeid), children)


def _serialize_node_containers(descriptor: Any) -> dict[str, Any]:
    """Serialize all populated node hierarchy containers from a Namespace."""
    result: dict[str, Any] = {}
    for container_name in (
        "objects", "datatypes", "eventtypes", "ifacetypes",
        "objtypes", "reftypes", "vartypes", "views",
    ):
        container = getattr(descriptor, container_name)
        nodes: dict[str, Any] = {
            name: _serialize_ns_node(val)
            for name, val in vars(container).items()
        }
        if nodes:
            result[container_name] = nodes
    return result


def _serialize_namespace_types(descriptor: Any, xml_sha256: str) -> str:
    """Render a Namespace's type descriptions as a Python source module.

    The generated file contains module-level variables that allow
    Namespaces._parse_nodeset_prebuilt() to reconstruct the descriptor
    without parsing any XML.
    """
    # --- structs ---
    structs: list[tuple[str, str, str | None, dict[str, Any]]] = []
    for sd in descriptor._structure_descriptions:
        defn = sd.structure_definition
        enc_id: str | None = (
            str(defn.default_encoding_id) if defn and defn.default_encoding_id else None
        )
        fields_list: list[dict[str, Any]] = []
        if defn:
            for f in defn.fields:
                fd: dict[str, Any] = {
                    "name": f.name,
                    "data_type": str(f.data_type),
                    "value_rank": f.value_rank,
                }
                if f.is_optional:
                    fd["is_optional"] = True
                if f.array_dimensions:
                    fd["array_dimensions"] = list(f.array_dimensions)
                if f.max_string_length:
                    fd["max_string_length"] = f.max_string_length
                fields_list.append(fd)
        struct_dict: dict[str, Any] = {
            "structure_type": defn.structure_type.value if defn else 0,
            "fields": fields_list,
        }
        structs.append((str(sd.data_type_id), str(sd.name), enc_id, struct_dict))

    # --- enums ---
    enums: list[tuple[str, str, dict[str, Any]]] = []
    for ed in descriptor._enum_descriptions:
        enum_fields: list[dict[str, Any]] = []
        for ef in ed.enum_definition.fields:
            efd: dict[str, Any] = {"name": ef.name, "value": int(ef.value)}
            dn_text = ef.display_name.text
            if dn_text:
                efd["display_name"] = dn_text
            desc_text = ef.description.text
            if desc_text:
                efd["description"] = desc_text
            enum_fields.append(efd)
        enums.append((str(ed.data_type_id), str(ed.name), {"fields": enum_fields}))

    # --- original nodeids (same format as _save_original_nodeids) ---
    orig_structs: list[tuple[str, str | None, list[str]]] = []
    for sd in descriptor._structure_descriptions:
        defn = sd.structure_definition
        orig_structs.append((
            str(sd.data_type_id),
            str(defn.default_encoding_id) if defn and defn.default_encoding_id else None,
            [str(f.data_type) for f in defn.fields] if defn else [],
        ))
    orig_enums = [str(ed.data_type_id) for ed in descriptor._enum_descriptions]
    original_nodeids = (orig_structs, orig_enums)

    nodes_data = _serialize_node_containers(descriptor)

    lines = [
        "# AUTO-GENERATED — DO NOT EDIT",
        f"# source-sha256: {xml_sha256}",
        "# Run tools/update_ns.py to regenerate.",
        "from __future__ import annotations",
        "",
        f"_URI: str = {descriptor.metadata.uri!r}",
        f"_VERSION: str = {descriptor.metadata.version!r}",
        f"_REQUIRED: list = {descriptor._required_namespaces!r}",
        f"_STRUCTURES: list = {structs!r}",
        f"_ENUMS: list = {enums!r}",
        f"_ORIGINAL_NODEIDS: tuple = {original_nodeids!r}",
        f"_NODES: dict = {pprint.pformat(nodes_data, indent=1, width=120)}",
        "",
    ]
    return "\n".join(lines)


def _black_format(source: str) -> str:
    """Format *source* with black, returning the original string on failure."""
    import black

    mode = black.Mode()
    try:
        return black.format_str(source, mode=mode)
    except Exception:
        return source


def _generate_nodeset_files(ordered: list[NodeSetSpec]) -> None:
    """Parse each nodeset in dependency order and write *.py files.

    These pre-generated files let Namespaces._parse_nodeset_prebuilt() bypass
    XML parsing entirely at import time.
    """
    # Import here so that update_ns.py can still be imported without o6
    # (e.g. just for --list).
    sys.path.insert(0, str(_ROOT))
    from o6.namespaces import Namespaces

    ns_tmp = Namespaces()
    print("  Generating nodeset .py files...")
    count = 0
    for spec in ordered:
        xml_path = _find_source_xml(spec.folder, spec.xml_filename)
        if xml_path is None:
            continue
        try:
            descriptor = ns_tmp._parse_nodeset(str(xml_path))
            if spec.skip_types:
                descriptor._structure_descriptions = []
                descriptor._enum_descriptions = []
            ns_tmp.append(descriptor, short_name=spec.short_name)
            sha = _sha256(xml_path)
            source = _black_format(_serialize_namespace_types(descriptor, sha))
            ns_path = _NODESETS_DIR / f"{spec.short_name}.py"
            ns_path.write_text(source, encoding="utf-8")
            count += 1
        except Exception as exc:
            print(f"    ✗  {spec.short_name}: {exc}", file=sys.stderr)
            continue
    print(f"    wrote {count} nodeset file(s)")


def _generate_builtin(ordered: list[NodeSetSpec]) -> str:
    lines = [
        "# AUTO-GENERATED — DO NOT EDIT",
        "# Run tools/update_ns.py to regenerate.",
        "",
        "import importlib",
        "import logging",
        "from concurrent.futures import ThreadPoolExecutor",
        "from typing import Optional, Tuple",
        "",
        "from .namespace import Namespace as _Namespace",
        "from .namespaces import Namespaces",
        "",
        "_logger = logging.getLogger(__name__)",
        "",
        "ns = Namespaces()",
        "",
        "# dependency-ordered by update_ns.py",
        "_NODESETS_LIST: list[str] = [",
    ]
    for spec in ordered:
        lines.append(f'    "{spec.short_name}",')
    lines += [
        "]",
        "",
        "",
        "def _parse_one(",
        "    short_name: str,",
        ") -> Tuple[Optional[_Namespace], str, Optional[str]]:",
        "    try:",
        "        _mod = importlib.import_module(f'o6._nodesets.{short_name}')",
        "        return ns._parse_nodeset_prebuilt(_mod), short_name, None",
        "    except Exception as _e:",
        "        return None, short_name, str(_e)",
        "",
        "",
        "with ThreadPoolExecutor() as _pool:",
        "    _parsed_results: list[Tuple[Optional[_Namespace], str, Optional[str]]] = list(",
        "        _pool.map(_parse_one, _NODESETS_LIST)",
        "    )",
        "",
        "# Append in dependency order (sequential — _build_types needs prior types linked)",
        "for _desc, _short_name, _parse_error in _parsed_results:",
        "    if _parse_error is not None:",
        '        _logger.warning("Could not load nodeset %r: %s", _short_name, _parse_error)',
        "        continue",
        "    try:",
        "        ns.append(_desc, short_name=_short_name)",
        "    except Exception as _e:",
        '        _logger.warning("Could not load nodeset %r: %s", _short_name, _e)',
        "",
    ]
    return "\n".join(lines)


def _update_nodesets_init() -> None:
    content = "# AUTO-GENERATED — DO NOT EDIT\n# Run tools/update_ns.py to regenerate.\n"
    (_NODESETS_DIR / "__init__.py").write_text(content)


# ---------------------------------------------------------------------------
# Topological sort
# ---------------------------------------------------------------------------


def _toposort(specs: list[NodeSetSpec]) -> list[NodeSetSpec]:
    """Return *specs* in dependency order (dependencies before dependents)."""
    by_name = {s.short_name: s for s in specs}
    visited: set[str] = set()
    result: list[NodeSetSpec] = []

    def visit(name: str, stack: list[str]) -> None:
        if name in visited:
            return
        if name in stack:
            cycle = " -> ".join(stack[stack.index(name) :] + [name])
            raise ValueError(f"Dependency cycle detected: {cycle}")
        if name not in by_name:
            return
        stack.append(name)
        for dep in by_name[name].depends_on:
            visit(dep, stack)
        stack.pop()
        visited.add(name)
        result.append(by_name[name])

    for spec in specs:
        visit(spec.short_name, [])

    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Show status of all nodesets without making changes.",
    )
    args = parser.parse_args()

    if not _SUBMODULE_DIR.is_dir():
        print(
            f"[error] Submodule not found at {_SUBMODULE_DIR}.\n"
            "Run: git submodule add -b latest "
            "https://github.com/OPCFoundation/UA-Nodeset.git deps/UA-Nodeset",
            file=sys.stderr,
        )
        return 1

    if args.list:
        symbols = {"ok": "✓", "changed": "↑", "new": "+", "missing": "✗"}
        max_folder = max(len(s.folder) for s in NODESETS)
        print(f"     {'folder':<{max_folder}}  short_name")
        print("  " + "-" * (max_folder + 30))
        for spec in NODESETS:
            st = _spec_status(spec)
            sym = symbols[st]
            skip = "  [skip_builtin]" if spec.skip_builtin else ""
            print(f"  {sym}  {spec.folder:<{max_folder}}  {spec.short_name}{skip}")
        return 0

    _NODESETS_DIR.mkdir(parents=True, exist_ok=True)

    # Remove any XML files previously copied into _nodesets/
    for stale_xml in _NODESETS_DIR.glob("*.xml"):
        stale_xml.unlink()
        print(f"  removed {stale_xml.name}")

    failed: list[str] = []
    for spec in NODESETS:
        src = _find_source_xml(spec.folder, spec.xml_filename)
        if src is None:
            print(f"  ✗  {spec.short_name}: not found in {spec.folder!r}", file=sys.stderr)
            failed.append(spec.short_name)
        else:
            print(f"  ✓  {spec.short_name}")

    available = [
        s
        for s in NODESETS
        if _find_source_xml(s.folder, s.xml_filename) is not None and not s.skip_builtin
    ]
    _resolve_xml_deps(available)
    ordered = _toposort(available)

    # Generate nodeset .py files for each nodeset (eliminates XML
    # parse work from the import-time hot path).
    _generate_nodeset_files(ordered)

    _BUILTIN_PY.write_text(_black_format(_generate_builtin(ordered)), encoding="utf-8")
    _update_nodesets_init()
    print(f"\nRegenerated {_BUILTIN_PY.relative_to(_ROOT)} ({len(ordered)} nodeset(s))")

    if failed:
        print(
            f"\n[warn] {len(failed)} nodeset(s) not found in submodule: {', '.join(failed)}",
            file=sys.stderr,
        )
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
