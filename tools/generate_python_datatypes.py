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
Generate Python type stubs (.pyi) for OPC UA datatypes using the o6 module conventions.

Two input modes (can be combined):
  BSD/CSV mode  (-t/-c/-x): uses open62541's nodeset_compiler type_parser to load
                            type definitions from BSD + optional NodeIds CSV.
                            The -x flag provides a NodeSet2 XML for symbolic name
                            resolution only (not type definitions).
  NodeSet2 mode (-n):       reads UADataType Definition elements directly from a
                            NodeSet2 XML file. Works standalone or alongside BSD mode.

Usage:
    # BSD + CSV (NS0 types)
    python3 tools/generate_python_datatypes.py \\
        -t deps/open62541/build/install/share/open62541/schema/Opc.Ua.Types.bsd \\
        -c deps/open62541/build/install/share/open62541/schema/NodeIds.csv \\
        -o o6/types_gen.pyi

    # NodeSet2 XML directly (companion specs or standalone)
    python3 tools/generate_python_datatypes.py \\
        -n path/to/MyCompanion.NodeSet2.xml \\
        -o o6/my_types_gen.pyi

    # Both combined (NodeSet2 companion + NS0 base for type resolution)
    python3 tools/generate_python_datatypes.py \\
        -t deps/open62541/build/install/share/open62541/schema/Opc.Ua.Types.bsd \\
        -c deps/open62541/build/install/share/open62541/schema/NodeIds.csv \\
        -n path/to/MyCompanion.NodeSet2.xml \\
        -o o6/my_types_gen.pyi
"""

import sys
import os
import argparse
import csv
import keyword
import re
import xml.etree.ElementTree as ET
from collections import OrderedDict

# Use the local deps install of open62541's nodeset compiler
_OPEN62541_SHARE = os.path.join(
    os.path.dirname(__file__),
    '..', 'deps', 'open62541', 'build', 'install', 'share', 'open62541'
)
_OPEN62541_SHARE = os.path.normpath(_OPEN62541_SHARE)
sys.path.insert(0, _OPEN62541_SHARE)

# Also check system-installed locations
for _share_candidate in [
    os.path.join('/usr', 'local', 'share', 'open62541'),
    os.path.join('/usr', 'share', 'open62541'),
]:
    if os.path.isdir(os.path.join(_share_candidate, 'nodeset_compiler')):
        sys.path.insert(0, _share_candidate)
        break

from nodeset_compiler.type_parser import CSVBSDTypeParser, BuiltinType, EnumerationType, StructType, OpaqueType

# NS0 numeric NodeId → type name, for resolving DataType attributes in NodeSet2 XML.
# Based on the standard OPC UA NodeIds (Opc.Ua.NodeSet2 namespace 0).
_NS0_NODEID_NAMES: dict[int, str] = {
    1: 'Boolean', 2: 'SByte', 3: 'Byte', 4: 'Int16', 5: 'UInt16',
    6: 'Int32', 7: 'UInt32', 8: 'Int64', 9: 'UInt64',
    10: 'Float', 11: 'Double', 12: 'String', 13: 'DateTime',
    14: 'Guid', 15: 'ByteString', 16: 'XmlElement',
    17: 'NodeId', 18: 'ExpandedNodeId', 19: 'StatusCode',
    20: 'QualifiedName', 21: 'LocalizedText', 23: 'DataValue',
    24: 'BaseDataType', 25: 'DiagnosticInfo',
}


# Mapping from OPC UA builtin type names to Python type annotation strings.
# Primitive OPC UA types map to Python primitives; complex builtins map to
# stub classes that are emitted at the top of the generated file.
BUILTIN_MAP = {
    'Boolean':        'bool',
    'SByte':          'int',
    'Byte':           'int',
    'Int16':          'int',
    'UInt16':         'int',
    'Int32':          'int',
    'UInt32':         'int',
    'Int64':          'int',
    'UInt64':         'int',
    'Float':          'float',
    'Double':         'float',
    'String':         'str',
    'DateTime':       'DateTime',
    'Guid':           'UUID',
    'ByteString':     'bytes',
    'XmlElement':     'str',
    'NodeId':         'NodeId',
    'ExpandedNodeId': 'ExpandedNodeId',
    'StatusCode':     'StatusCode',
    'QualifiedName':  'QualifiedName',
    'LocalizedText':  'LocalizedText',
    'ExtensionObject':'Any',
    'DataValue':      'DataValue',
    'Variant':        'Any',
    'DiagnosticInfo': 'Any',
}

# OPC UA builtin types that need a stub class emitted in the generated file.
# (Excludes primitives that map directly to Python builtins and opaque Any types.)
_BUILTIN_STUB_CLASSES = [
    'StatusCode',
    'DateTime',
    'Guid',
    'NodeId',
    'ExpandedNodeId',
    'QualifiedName',
    'LocalizedText',
    'DataValue',
]


# OPC UA builtin types that need a stub class emitted in the generated file.
# (Excludes primitives that map directly to Python builtins and opaque Any types.)
_BUILTIN_STUB_CLASSES = [
    'StatusCode',
    'DateTime',
    'Guid',
    'NodeId',
    'ExpandedNodeId',
    'QualifiedName',
    'LocalizedText',
    'DataValue',
]


def is_builtin(t) -> bool:
    return isinstance(t, BuiltinType) or t.name in BUILTIN_MAP


def py_type(member_type, is_array: bool, is_optional: bool) -> str:
    """Return the Python type annotation string for a struct member."""
    if is_builtin(member_type):
        base = BUILTIN_MAP.get(member_type.name, 'Any')
    elif isinstance(member_type, EnumerationType):
        base = member_type.name
    elif isinstance(member_type, OpaqueType):
        base = BUILTIN_MAP.get(member_type.name, 'bytes')
    else:
        base = member_type.name

    if is_array:
        base = f'list[{base}]'
    if is_optional:
        base = f'{base} | None'
    return base


def make_snake_name(caml: str) -> str:
    """Convert camelCase to snake_case, matching the C makeSnakeName() in types_convert.c."""
    if not caml:
        return caml
    # Pre-process: treat "NodeId"/"nodeId" as a single word atom
    caml = caml.replace('NodeId', 'Nodeid').replace('nodeId', 'nodeid')
    out = [caml[0].lower()]
    for c in caml[1:]:
        if c.isupper():
            out.append('_')
            out.append(c.lower())
        else:
            out.append(c)
    return ''.join(out)


def safe_name(name: str) -> str:
    """Append underscore to Python keywords so stubs remain valid syntax."""
    return name + '_' if keyword.iskeyword(name) or keyword.issoftkeyword(name) else name


def safe_class_name(name: str) -> str:
    """Ensure a class name is a valid Python identifier (prefix '_' if starts with a digit)."""
    name = safe_name(name)
    if name and name[0].isdigit():
        name = '_' + name
    return name


def setter_ann(ann: str) -> str:
    """Widen some setter signatures (e.g. the C layer converts str to NodeId)."""
    ann = re.sub(r'\bNodeId\b', 'NodeIdLike', ann)
    ann = re.sub(r'\bLocalizedText\b', 'LocalizedText | str', ann)
    ann = re.sub(r'\bQualifiedName\b', 'QualifiedName | str', ann)
    return ann


def generate_enum(t: EnumerationType) -> list[str]:
    lines = []
    lines.append(f'class {safe_class_name(t.name)}(enum.IntEnum):')
    if not t.elements:
        return []  # skip abstract zero-member enums
    else:
        for name, value in t.elements.items():
            lines.append(f'    {safe_name(name).upper()} = ...')
    lines.append('')
    return lines


def generate_struct(t: StructType) -> list[str]:
    lines = []
    lines.append(f'class {safe_class_name(t.name)}:')
    lines.append('    def __init__(self) -> None: ...')
    if not t.members:
        lines.append('    ...')
    else:
        for m in t.members:
            ann = py_type(m.member_type, m.is_array, m.is_optional)
            mname = safe_name(make_snake_name(m.name))
            lines.append(f'    @property')
            lines.append(f'    def {mname}(self) -> {ann}: ...')
            lines.append(f'    @{mname}.setter')
            lines.append(f'    def {mname}(self, val: {setter_ann(ann)}, /) -> None: ...')
    lines.append('')
    return lines


# ---------------------------------------------------------------------------
# NodeSet2 XML direct parser
# ---------------------------------------------------------------------------

class _NS2Member:
    """Lightweight stand-in for StructMember used by the NodeSet2 path."""
    def __init__(self, name: str, type_annotation: str, is_array: bool, is_optional: bool) -> None:
        self.name = name
        self._annotation = type_annotation
        self.is_array = is_array
        self.is_optional = is_optional


class _NS2Enum:
    """Lightweight stand-in for EnumerationType used by the NodeSet2 path."""
    def __init__(self, name: str, elements: dict[str, int]) -> None:
        self.name = name
        self.elements = elements


class _NS2Struct:
    """Lightweight stand-in for StructType used by the NodeSet2 path."""
    def __init__(self, name: str, members: list[_NS2Member]) -> None:
        self.name = name
        self.members = members


def _build_nodeid_map(extra_nodeids_csv: list) -> dict[str, str]:
    """
    Build a mapping of "ns=X;i=Y" / "i=Y" → type name.
    Seeded with NS0 builtins; extended from any -c NodeIds.csv files.
    """
    nodeid_map: dict[str, str] = {f'i={k}': v for k, v in _NS0_NODEID_NAMES.items()}
    for f in extra_nodeids_csv:
        # rewind in case it was already consumed by CSVBSDTypeParser
        try:
            f.seek(0)
        except Exception:
            pass
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 3:
                continue
            name, nid, kind = row[0].strip(), row[1].strip(), row[2].strip()
            if kind == 'DataType':
                nodeid_map[f'i={nid}'] = name
    return nodeid_map


def _resolve_datatype(dt_attr: str | None, nodeid_map: dict[str, str],
                      known_names: set[str]) -> str:
    """Resolve a DataType attribute (e.g. 'i=11', 'ns=2;i=42') to a Python annotation."""
    if not dt_attr:
        return 'Any'
    # Prefer exact key lookup
    name = nodeid_map.get(dt_attr)
    if name is None:
        # strip leading namespace if present: 'ns=X;i=Y' → 'i=Y'
        stripped = dt_attr.split(';')[-1]
        name = nodeid_map.get(stripped)
    if name is None:
        return 'Any'
    # Return o6 annotation if builtin, otherwise the type name as-is
    return BUILTIN_MAP.get(name, name if name in known_names else 'Any')


def parse_nodeset2_xml(files: list, nodeid_map: dict[str, str]) -> tuple[list[_NS2Enum], list[_NS2Struct]]:
    """
    Parse UADataType Definition sections from NodeSet2 XML files.
    Returns (enums, structs) lists of lightweight descriptors.
    """
    enums: list[_NS2Enum] = []
    structs: list[_NS2Struct] = []

    # First pass: collect all defined type names so we can resolve cross-refs
    all_names: set[str] = set()
    parsed_trees: list[tuple] = []  # (root, ns_map)
    for f in files:
        try:
            f.seek(0)
        except Exception:
            pass
        tree = ET.parse(f)
        root = tree.getroot()
        tag_ns = root.tag.split('}')[0].strip('{') if '}' in root.tag else ''
        ns_map = {'ua': tag_ns} if tag_ns else {}
        for dt in root.findall('.//ua:UADataType', ns_map) if ns_map else root.findall('.//UADataType'):
            browse = dt.get('BrowseName', '')
            name = browse.split(':')[-1] if ':' in browse else browse
            if name:
                all_names.add(name)
        parsed_trees.append((root, ns_map))

    # Second pass: extract enum/struct definitions
    for root, ns_map in parsed_trees:
        find = lambda tag: root.findall(f'.//ua:{tag}', ns_map) if ns_map else root.findall(f'.//{tag}')
        for dt in find('UADataType'):
            browse = dt.get('BrowseName', '')
            name = browse.split(':')[-1] if ':' in browse else browse
            if not name:
                continue
            defn = (
                dt.find('ua:Definition', ns_map) if ns_map else dt.find('Definition')
            )
            if defn is None:
                continue
            fields = (
                defn.findall('ua:Field', ns_map) if ns_map else defn.findall('Field')
            )
            if not fields:
                continue

            # Enum: all fields have a Value attribute
            if all(f.get('Value') is not None for f in fields):
                elements: dict[str, int] = {}
                for field in fields:
                    fname = field.get('Name', '')
                    fval = field.get('Value', '0')
                    elements[fname] = int(fval)
                enums.append(_NS2Enum(name, elements))
            else:
                # Struct
                members: list[_NS2Member] = []
                for field in fields:
                    fname = field.get('Name', '')
                    if not fname:
                        continue
                    is_array = field.get('ValueRank', '-1') not in ('-1', '')
                    is_optional = field.get('IsOptional', 'false').lower() == 'true'
                    dt_attr = field.get('DataType')
                    ann = _resolve_datatype(dt_attr, nodeid_map, all_names)
                    if is_array:
                        ann = f'list[{ann}]'
                    if is_optional:
                        ann = f'{ann} | None'
                    mname = make_snake_name(fname)
                    members.append(_NS2Member(mname, ann, is_array=False, is_optional=False))
                structs.append(_NS2Struct(name, members))

    return enums, structs


def generate_ns2_enum(t: _NS2Enum) -> list[str]:
    lines = [f'class {safe_class_name(t.name)}(enum.IntEnum):']
    if not t.elements:
        return []  # skip abstract zero-member enums
    else:
        for name in t.elements:
            lines.append(f'    {safe_name(name).upper()} = ...')
    lines.append('')
    return lines


def generate_ns2_struct(t: _NS2Struct) -> list[str]:
    lines = [f'class {safe_class_name(t.name)}:']
    lines.append('    def __init__(self) -> None: ...')
    if not t.members:
        lines.append('    ...')
    else:
        for m in t.members:
            ann = m._annotation
            mname = safe_name(m.name)
            lines.append('    @property')
            lines.append(f'    def {mname}(self) -> {ann}: ...')
            lines.append(f'    @{mname}.setter')
            lines.append(f'    def {mname}(self, val: {setter_ann(ann)}, /) -> None: ...')
    lines.append('')
    return lines


def inject_builtins(parser_obj) -> None:
    """Inject BuiltinType stubs so member references resolve during parsing."""
    builtins = [
        'Boolean', 'SByte', 'Byte', 'Int16', 'UInt16', 'Int32', 'UInt32',
        'Int64', 'UInt64', 'Float', 'Double', 'String', 'DateTime', 'Guid',
        'ByteString', 'XmlElement', 'NodeId', 'ExpandedNodeId', 'StatusCode',
        'QualifiedName', 'LocalizedText', 'ExtensionObject', 'DataValue',
        'Variant', 'DiagnosticInfo', 'Char', 'Int8', 'UInt8', 'CharArray', 'Bit',
    ]
    ns = 'http://opcfoundation.org/UA/'
    if ns not in parser_obj.types:
        parser_obj.types[ns] = OrderedDict()
    for b in builtins:
        if b not in parser_obj.types[ns]:
            parser_obj.types[ns][b] = BuiltinType(b)


def collect_used_builtins(types: dict,
                          ns2_structs: list | None = None) -> set:
    """Determine which builtin type names are referenced in generated types."""
    used = set()
    for ns in types.values():
        for t in ns.values():
            if is_builtin(t):
                continue
            if isinstance(t, StructType):
                for m in t.members:
                    if is_builtin(m.member_type):
                        used.add(m.member_type.name)
    # Also check NodeSet2 structs for Guid usage
    if ns2_structs:
        for t in ns2_structs:
            for m in t.members:
                if 'UUID' in m._annotation:
                    used.add('Guid')
    return used


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Generate a .pyi stub with OPC UA struct and enum types for the o6 module.'
    )
    parser.add_argument('-c', '--type-csv',  type=argparse.FileType('r'),  action='append', default=[],
                        help='NodeIds CSV file (used for BSD mode and NodeSet2 DataType resolution)')
    parser.add_argument('-x', '--xml',       type=argparse.FileType('rb'), action='append', default=[],
                        help='NodeSet2 XML for symbolic name resolution in BSD mode (not type definitions)')
    parser.add_argument('-t', '--type-bsd',  type=argparse.FileType('r'),  action='append', default=[],
                        help='Binary Schema Definition file with type definitions')
    parser.add_argument('-n', '--nodeset2',  type=argparse.FileType('r'),  action='append', default=[],
                        help='NodeSet2 XML file to extract type definitions from directly')
    parser.add_argument('--import', dest='import_bsd', type=str, action='append', default=[],
                        help='TYPE_ARRAY#filepath.bsd definitions to load but not emit')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()

    # --- BSD/CSV mode ---
    bsd_types: dict = {}
    if args.type_bsd or args.import_bsd:
        parser_obj = CSVBSDTypeParser(
            opaque_map=[],
            selected_types=[],
            no_builtin=False,
            outname='types',
            existing_bsd=args.import_bsd,
            type_bsd=args.type_bsd,
            type_csv=args.type_csv,
            type_xml=args.xml,
            namespaceIndexMap={}
        )
        inject_builtins(parser_obj)
        parser_obj.parse_types()
        bsd_types = parser_obj.types

    # --- NodeSet2 direct mode ---
    ns2_enums: list[_NS2Enum] = []
    ns2_structs: list[_NS2Struct] = []
    if args.nodeset2:
        nodeid_map = _build_nodeid_map(args.type_csv)
        ns2_enums, ns2_structs = parse_nodeset2_xml(args.nodeset2, nodeid_map)

    used_builtins = collect_used_builtins(bsd_types, ns2_structs)

    out = args.output

    # Header
    out.write('# AUTO-GENERATED by tools/generate_python_datatypes.py — DO NOT EDIT\n')
    out.write('from __future__ import annotations\n')
    out.write('from typing import Any\n')
    out.write('import enum\n')
    if 'Guid' in used_builtins:
        out.write('from uuid import UUID\n')
    # Import complex OPC UA types from types_builtin so struct member annotations resolve
    out.write('from o6._o6.types_builtin import (\n')
    out.write('    DateTime, NodeId, NodeIdLike, ExpandedNodeId, StatusCode,\n')
    out.write('    QualifiedName, LocalizedText, DataValue,\n')
    out.write(')\n')
    out.write('\n')

    # Emit BSD-mode types
    bsd_enum_lines = []
    bsd_struct_lines = []
    for ns in bsd_types.values():
        for t in ns.values():
            if is_builtin(t):
                continue
            if isinstance(t, EnumerationType):
                bsd_enum_lines.extend(generate_enum(t))
            elif isinstance(t, StructType):
                bsd_struct_lines.extend(generate_struct(t))
            # OpaqueType: skip (mapped to bytes via BUILTIN_MAP or ignored)

    if bsd_enum_lines:
        out.write('# --- Enumerations ---\n\n')
        out.writelines(line + '\n' for line in bsd_enum_lines)

    if bsd_struct_lines:
        out.write('# --- Structured Types ---\n\n')
        out.writelines(line + '\n' for line in bsd_struct_lines)

    # Collect names already emitted in BSD mode so NodeSet2 doesn't redefine them
    bsd_emitted: set[str] = set()
    for ns in bsd_types.values():
        for t in ns.values():
            if not is_builtin(t):
                bsd_emitted.add(safe_class_name(t.name))

    # Emit NodeSet2-mode types (skip any already emitted from BSD)
    ns2_enums_new = [t for t in ns2_enums if safe_class_name(t.name) not in bsd_emitted]
    ns2_structs_new = [t for t in ns2_structs if safe_class_name(t.name) not in bsd_emitted]

    if ns2_enums_new:
        out.write('# --- Enumerations (NodeSet2) ---\n\n')
        for t in ns2_enums_new:
            out.writelines(line + '\n' for line in generate_ns2_enum(t))

    if ns2_structs_new:
        out.write('# --- Structured Types (NodeSet2) ---\n\n')
        for t in ns2_structs_new:
            out.writelines(line + '\n' for line in generate_ns2_struct(t))

    # Emit __all__ omitting types that are overridden in o6/__init__.pyi or o6/_o6/types.pyi.
    # This prevents `from o6._o6.types_gen import *` from clobbering those names.
    _TYPES_PYI_OVERRIDES = {'EventFilter', 'DataChangeFilter', 'SimpleAttributeOperand', 'RelativePath', 'ReadValueId'}

    all_names: list[str] = []
    for ns in bsd_types.values():
        for t in ns.values():
            if not is_builtin(t):
                cname = safe_class_name(t.name)
                if cname not in _TYPES_PYI_OVERRIDES:
                    all_names.append(cname)
    for t in ns2_enums_new:
        cname = safe_class_name(t.name)
        if cname not in _TYPES_PYI_OVERRIDES:
            all_names.append(cname)
    for t in ns2_structs_new:
        cname = safe_class_name(t.name)
        if cname not in _TYPES_PYI_OVERRIDES:
            all_names.append(cname)

    out.write('\n__all__ = [\n')
    for name in all_names:
        out.write(f'    {name!r},\n')
    out.write(']\n')

    if out is not sys.stdout:
        import subprocess
        out.flush()
        try:
            subprocess.run([sys.executable, '-m', 'black', '--fast', '-q', out.name], check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass  # black is optional


if __name__ == '__main__':
    main()
