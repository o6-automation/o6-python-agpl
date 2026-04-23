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
from __future__ import annotations

import logging
import re
import weakref
from . import _o6
from .namespace import Namespace

from typing import Any, List

_logger = logging.getLogger(__name__)


class RemoteNamespaces:
    """Discovered server-side namespaces accessible after :meth:`discover`.

    Call :meth:`discover` on a connected client to browse and build types
    for every namespace on the remote server that is not already loaded
    locally.  Each discovered :class:`Namespace` is then stored as an
    attribute keyed by its *short_name*.
    """

    def __init__(self, namespaces: Namespaces) -> None:
        self._namespaces = namespaces
        self._descriptors: dict[str, Namespace] = {}

    def __repr__(self) -> str:
        if not self._descriptors:
            return "RemoteNamespaces()"
        names = ", ".join(sorted(self._descriptors))
        return f"RemoteNamespaces({names})"

    def __getitem__(self, key: str | int) -> Namespace:
        if isinstance(key, int):
            for d in self._descriptors.values():
                if d.metadata.index == key:
                    return d
            raise KeyError(key)
        if key in self._descriptors:
            return self._descriptors[key]
        for d in self._descriptors.values():
            if d.metadata.uri == key:
                return d
        raise KeyError(key)

    def discover(self) -> list[Namespace]:
        import o6

        ns = self._namespaces
        owner = ns._owner
        if owner is None or not isinstance(owner, o6.Client):
            raise RuntimeError("discover() requires a connected Client as owner")

        async def _browse_subtypes(root: o6.NodeId) -> list[o6.NodeId]:
            found: list[o6.NodeId] = []
            to_visit = [root]
            while to_visit:
                current = to_visit.pop()
                bd = o6.BrowseDescription()
                bd.nodeid = current
                bd.browse_direction = o6.BrowseDirection.FORWARD
                bd.reference_type_id = o6.NodeId(45)
                bd.node_class_mask = 64  # DataType
                req = o6.BrowseRequest()
                req.nodes_to_browse = [bd]
                resp = await owner.service_browse(req)  # type: ignore[misc]
                if not resp.results or resp.results[0].status_code.code != 0:
                    continue
                for rd in resp.results[0].references:
                    child = o6.NodeId(f"ns={rd.nodeid.ns};i={rd.nodeid.id}")
                    found.append(child)
                    to_visit.append(child)
            return found

        async def _call() -> list[Namespace]:
            # Read the server namespace array (ns=0;i=2255)
            read_req = o6.ReadRequest()
            rvi = o6.ReadValueId()
            rvi.nodeid = o6.NodeId("i=2255")
            rvi.attribute_id = o6.AttributeId.VALUE
            read_req.nodes_to_read = [rvi]
            resp = await owner.service_read(read_req)  # type: ignore[misc]
            ns_val = resp.results[0].value
            server_ns_array: list[str] = list(ns_val) if ns_val is not None else []

            # Build URI → server-index map for new namespaces only
            new_uris: dict[int, str] = {}
            for idx, uri in enumerate(server_ns_array):
                if idx == 0:
                    continue
                if uri and uri not in ns._linked_uris:
                    new_uris[idx] = uri

            if not new_uris:
                return []

            # Browse DataType subtrees: Structure (i=22) and Enumeration (i=29)
            struct_nodes = await _browse_subtypes(o6.NodeId(22))
            enum_nodes = await _browse_subtypes(o6.NodeId(29))

            # Filter to types in new namespaces
            new_struct_nodes = [n for n in struct_nodes if n.ns in new_uris]
            new_enum_nodes = [n for n in enum_nodes if n.ns in new_uris]
            all_new = new_struct_nodes + new_enum_nodes
            if not all_new:
                return []

            # Read DataTypeDefinition + BrowseName for all discovered types
            read_req2 = o6.ReadRequest()
            rvis: list[Any] = []
            for nid in all_new:
                rv = o6.ReadValueId()
                rv.nodeid = nid
                rv.attribute_id = o6.AttributeId.DATATYPEDEFINITION
                rvis.append(rv)
            for nid in all_new:
                rv = o6.ReadValueId()
                rv.nodeid = nid
                rv.attribute_id = o6.AttributeId.BROWSENAME
                rvis.append(rv)
            read_req2.nodes_to_read = rvis
            resp2 = await owner.service_read(read_req2)  # type: ignore[misc]

            n_total = len(all_new)
            n_structs = len(new_struct_nodes)

            # Group by namespace URI
            uri_structs: dict[
                str, list[tuple[o6.NodeId, o6.StructureDefinition, o6.QualifiedName]]
            ] = {}
            uri_enums: dict[
                str, list[tuple[o6.NodeId, o6.EnumDefinition, o6.QualifiedName]]
            ] = {}

            for i, nid in enumerate(all_new):
                defn = resp2.results[i].value
                qn = resp2.results[i + n_total].value
                if not isinstance(qn, o6.QualifiedName):
                    continue
                nid_uri: str | None = new_uris.get(nid.ns)
                if not nid_uri:
                    continue
                if i < n_structs and isinstance(defn, o6.StructureDefinition):
                    uri_structs.setdefault(nid_uri, []).append((nid, defn, qn))
                elif i >= n_structs and isinstance(defn, o6.EnumDefinition):
                    uri_enums.setdefault(nid_uri, []).append((nid, defn, qn))

            # Build one Namespace per namespace
            all_uris = set(uri_structs.keys()) | set(uri_enums.keys())
            descriptors: list[Namespace] = []

            for uri in all_uris:
                desc = Namespace(uri)

                for nid, sdefn, qn in uri_structs.get(uri, []):
                    sd = _o6.types.StructureDescription()
                    sd.data_type_id = o6.NodeId(nid)
                    sd.name = qn
                    sd.structure_definition = sdefn
                    desc._structure_descriptions.append(sd)

                for nid, edefn, qn in uri_enums.get(uri, []):
                    ed = _o6.types.EnumDescription()
                    ed.data_type_id = o6.NodeId(nid)
                    ed.name = qn
                    ed.enum_definition = edefn
                    desc._enum_descriptions.append(ed)

                # Register the namespace URI with the owner and set metadata.index.
                ns_map = ns._resolve_namespace_map(desc, owner)
                ns._remap_namespace(desc, ns_map)
                ns._build_types(desc)
                ns._link_namespace(desc, owner)
                ns._linked_uris.add(uri)
                if not callable(getattr(type(ns), desc.metadata.short_name, None)):
                    setattr(ns, desc.metadata.short_name, desc)
                setattr(self, desc.metadata.short_name, desc)
                ns._descriptors[desc.metadata.short_name] = desc
                self._descriptors[desc.metadata.short_name] = desc
                descriptors.append(desc)

            return descriptors

        return owner._maybe_async(_call())  # type: ignore[return-value]


def _link_datatypes(container: Any, types: Any) -> None:
    """Recursively walk a datatypes node container and set ``_datatype`` on
    each ``NamespaceDataTypeNode`` to the matching built Python class, if one
    exists in *types*."""
    from .namespace import NamespaceDataTypeNode

    for attr_name, node in vars(container).items():
        if isinstance(node, NamespaceDataTypeNode):
            py_class = getattr(types, attr_name, None)
            if py_class is not None:
                node._datatype = py_class
            _link_datatypes(node, types)


class Namespaces:

    def __init__(self, owner: _o6.Client | _o6.Server | None = None):
        # Weak reference to the owner (Client or Server) so that the
        # Namespaces object does not form a strong reference cycle with it.
        # The owner already holds a strong reference to self via
        # self.namespaces, so it stays alive by normal refcounting.
        self._owner_ref: weakref.ref | None = (
            weakref.ref(owner) if owner is not None else None
        )
        self._linked_uris: set[str] = set()
        self._descriptors: dict[str, Namespace] = {}
        self.remote: RemoteNamespaces = RemoteNamespaces(self)
        # Virtual namespace table for ownerless pre-builds.
        # Simulates a fresh server: ns=0 (UA), ns=1 (server URI),
        # so companion specs start at ns=2.
        self._virtual_ns_table: dict[str, int] = {}
        self._next_virtual_idx: int = 2

    @property
    def _owner(self) -> _o6.Client | _o6.Server | None:
        if self._owner_ref is None:
            return None
        return self._owner_ref()

    def _check_duplicate(self, uri: str) -> None:
        if uri in self._linked_uris:
            raise ValueError(f"Namespace '{uri}' is already loaded in this context")

    def __getitem__(self, key: str | int) -> Namespace:
        if isinstance(key, int):
            for d in self._descriptors.values():
                if d.metadata.index == key:
                    return d
            raise KeyError(key)
        if key in self._descriptors:
            return self._descriptors[key]
        for d in self._descriptors.values():
            if d.metadata.uri == key:
                return d
        raise KeyError(key)

    def _apply_short_name(self, descriptor: Namespace, short_name: str | None) -> None:
        effective = (
            short_name if short_name is not None else descriptor.metadata.short_name
        )
        existing = self._descriptors.get(effective)
        if existing is not None and existing.metadata.uri != descriptor.metadata.uri:
            raise ValueError(
                f"Short name '{effective}' is already used by namespace "
                f"'{existing.metadata.uri}'. Pass short_name=... to resolve the conflict."
            )
        descriptor.metadata.short_name = effective

    _BASE_UA_URI = "http://opcfoundation.org/UA/"

    def _warn_missing_dependencies(self, descriptor: Namespace) -> None:
        for dep in descriptor._required_namespaces:
            uri = dep["uri"] if isinstance(dep, dict) else dep
            if uri and uri != self._BASE_UA_URI and uri not in self._linked_uris:
                _logger.warning(
                    "Namespace '%s' requires '%s' which is not loaded yet. "
                    "Load dependencies before dependents to avoid build failures.",
                    descriptor.metadata.uri,
                    uri,
                )

    def _check_client_not_connected(self) -> None:
        owner = self._owner
        if owner is None or isinstance(owner, _o6.Server):
            return
        channel_state, _, _ = owner._get_state()
        if channel_state != 0:  # UA_SECURECHANNELSTATE_CLOSED
            raise RuntimeError(
                "Cannot call ns.append() after the client is connected. "
                "All namespaces must be loaded before connect()."
            )

    def append(
        self,
        ns: Namespace,
        short_name: str | None = None,
    ) -> Namespace:
        self._check_client_not_connected()
        self._check_duplicate(ns.metadata.uri)
        self._apply_short_name(ns, short_name)
        if self._owner is not None:
            ns = ns._copy_for_rebuild()
            if ns._original_nodeids is not None:
                self._restore_original_nodeids(ns)
            ns_map = self._resolve_namespace_map(ns, self._owner)
            self._remap_namespace(ns, ns_map)
        self._build_types(ns)
        if self._owner is not None:
            self._link_namespace(ns, self._owner)
        self._linked_uris.add(ns.metadata.uri)
        setattr(self, ns.metadata.short_name, ns)
        self._descriptors[ns.metadata.short_name] = ns
        return ns

    def _parse_nodeset(
        self,
        nodeset2xml: str,
    ) -> Namespace:
        """Parse a NodeSet2 XML file and return a Namespace without appending it.

        Thread-safe: does not read or write any shared Namespaces state.
        Call append() sequentially in dependency order afterward.
        """
        from ._nodeset_parser import parse_nodeset

        descriptor = parse_nodeset(nodeset2xml, self)
        self._save_original_nodeids(descriptor)
        return descriptor

    def _parse_nodeset_prebuilt(
        self,
        module: Any,
    ) -> Namespace:
        """Reconstruct a Namespace from a pre-generated nodeset module.

        This is the fast path used by the o6-ns package: no XML parsing,
        no nodeset-compiler overhead.  The module must expose the variables
        produced by tools/update_ns.py (_URI, _VERSION, _REQUIRED,
        _STRUCTURES, _ENUMS, _ORIGINAL_NODEIDS, _NODES).

        Thread-safe: does not read or write any shared Namespaces state.
        Call append() sequentially in dependency order afterward.
        """
        from .namespace import (
            NamespaceObjectNode,
            NamespaceVariableNode,
            NamespaceMethodNode,
            NamespaceObjectTypeNode,
            NamespaceDataTypeNode,
            NamespaceReferenceTypeNode,
            NamespaceVariableTypeNode,
            NamespaceViewNode,
        )

        _node_classes: dict[str, Any] = {
            "O": NamespaceObjectNode,
            "V": NamespaceVariableNode,
            "M": NamespaceMethodNode,
            "OT": NamespaceObjectTypeNode,
            "D": NamespaceDataTypeNode,
            "RT": NamespaceReferenceTypeNode,
            "VT": NamespaceVariableTypeNode,
            "W": NamespaceViewNode,
        }

        def _load_node(data: tuple) -> Any:
            type_code, nodeid, children = data
            cls = _node_classes.get(type_code, NamespaceObjectNode)
            node = cls(nodeid, None) if cls is NamespaceDataTypeNode else cls(nodeid)
            for child_name, child_data in children.items():
                setattr(node, child_name, _load_node(child_data))
            return node

        descriptor = Namespace(uri=module._URI, version=module._VERSION)
        descriptor._required_namespaces = list(module._REQUIRED)
        for nodeid, browse_name, enc_id, struct_dict in module._STRUCTURES:
            descriptor._add_structure_description(
                nodeid, browse_name, struct_dict, enc_id
            )
        for nodeid, browse_name, enum_dict in module._ENUMS:
            descriptor._add_enum_description(nodeid, browse_name, enum_dict)
        descriptor._original_nodeids = module._ORIGINAL_NODEIDS
        for container_name, nodes_dict in module._NODES.items():
            container = getattr(descriptor, container_name)
            for name, node_data in nodes_dict.items():
                setattr(container, name, _load_node(node_data))
        return descriptor

    def load(
        self,
        nodeset2xml: str,
        short_name: str | None = None,
    ) -> Namespace:
        self._check_client_not_connected()
        descriptor = self._parse_nodeset(nodeset2xml)
        self._check_duplicate(descriptor.metadata.uri)
        self._warn_missing_dependencies(descriptor)
        return self.append(ns=descriptor, short_name=short_name)

    def _build_types(self, descriptor: Namespace) -> None:
        """Convert all descriptions to ``UA_DataType`` arrays and create
        Python type objects.  Stores all capsules on
        ``descriptor._capsule`` (a list) so the C arrays remain alive as
        long as the Namespace does.  Populates ``descriptor._types`` with
        the created classes."""

        descriptions = list(descriptor._structure_descriptions) + list(
            descriptor._enum_descriptions
        )
        if not descriptions:
            return

        remaining = list(descriptions)
        # The latest successfully-built capsule; passed as lookup_capsule to
        # the next build so intra-batch type dependencies can be resolved.
        accumulated_capsule: object | None = None
        all_capsules: list[object] = []

        max_passes = len(remaining) + 1
        for _ in range(max_passes):
            if not remaining:
                break

            failed = []
            for desc in remaining:
                try:
                    capsule, result = _o6.build_custom_data_types(
                        [desc], descriptor.metadata.short_name, accumulated_capsule
                    )
                    for nodeid, py_class in result:
                        name = py_class.__name__
                        if hasattr(descriptor._types, name):
                            _logger.warning(
                                "Malformed nodeset '%s': duplicate type name '%s' — "
                                "overwriting earlier definition",
                                descriptor.metadata.uri,
                                name,
                            )
                        setattr(descriptor._types, name, py_class)
                    all_capsules.append(capsule)
                    accumulated_capsule = capsule
                except (RuntimeError, TypeError):
                    failed.append(desc)

            if len(failed) == len(remaining):
                names = [str(getattr(d, "name", "?")) for d in failed]
                missing = [
                    dep["uri"] if isinstance(dep, dict) else dep
                    for dep in descriptor._required_namespaces
                    if (dep["uri"] if isinstance(dep, dict) else dep)
                    not in self._linked_uris
                ]
                hint = (
                    f" (missing dependencies: {', '.join(missing)})"
                    if missing
                    else " (check that all required namespaces are loaded first)"
                )
                raise RuntimeError(
                    f"Could not build {len(failed)} type(s): {', '.join(names)}{hint}"
                )
            remaining = failed

        # Keep every capsule alive — each one owns a standalone UA_DataTypeArray
        # whose UA_DataType* pointers are baked into the Python type objects.
        descriptor._capsule = all_capsules

        # Link built Python classes back into the datatypes node hierarchy.
        _link_datatypes(descriptor.datatypes, descriptor._types)

    def _resolve_namespace_map(
        self,
        descriptor: Namespace,
        owner: _o6.Client | _o6.Server | None = None,
    ) -> dict[int, int]:
        if owner is None:
            owner = self._owner
        ns_map: dict[int, int] = {}
        # OPC UA nodesets always use ns=1 for the primary (target) namespace.
        uri = descriptor.metadata.uri
        xml_idx = 1
        if owner is not None:
            if isinstance(owner, _o6.Server):
                runtime_idx = owner.add_namespace(uri)
            else:
                try:
                    runtime_idx = owner.get_namespace_index(uri)
                except (KeyError, Exception):
                    runtime_idx = _o6.Client.add_namespace(owner, uri)  # type: ignore[attr-defined]
        else:
            if uri in self._virtual_ns_table:
                runtime_idx = self._virtual_ns_table[uri]
            else:
                runtime_idx = self._next_virtual_idx
                self._virtual_ns_table[uri] = runtime_idx
                self._next_virtual_idx += 1
        if runtime_idx != xml_idx:
            ns_map[xml_idx] = runtime_idx
        descriptor.metadata.index = runtime_idx
        if owner is None:
            descriptor._canonical_ns_table = dict(self._virtual_ns_table)
        return ns_map

    @staticmethod
    def _remap_nodeid_str(nodeid_str: str, ns_map: dict[int, int]) -> str:
        def _replace(m: re.Match[str]) -> str:
            old_idx = int(m.group(1))
            new_idx = ns_map.get(old_idx, old_idx)
            return f"ns={new_idx}"

        return re.sub(r"ns=(\d+)", _replace, nodeid_str)

    @classmethod
    def _remap_namespace(cls, descriptor: Namespace, ns_map: dict[int, int]) -> None:
        if not ns_map:
            return
        for sd in descriptor._structure_descriptions:
            sd.data_type_id = cls._remap_nodeid_str(str(sd.data_type_id), ns_map)
            defn = sd.structure_definition
            if defn is not None:
                if defn.default_encoding_id:
                    defn.default_encoding_id = cls._remap_nodeid_str(
                        str(defn.default_encoding_id), ns_map
                    )
                for field in defn.fields:
                    dt = str(field.data_type)
                    remapped = cls._remap_nodeid_str(dt, ns_map)
                    if remapped != dt:
                        field.data_type = remapped
        for ed in descriptor._enum_descriptions:
            ed.data_type_id = cls._remap_nodeid_str(str(ed.data_type_id), ns_map)

    @staticmethod
    def _save_original_nodeids(descriptor: Namespace) -> None:
        if descriptor._original_nodeids is not None:
            return
        structs = []
        for sd in descriptor._structure_descriptions:
            defn = sd.structure_definition
            structs.append(
                (
                    str(sd.data_type_id),
                    (
                        str(defn.default_encoding_id)
                        if defn and defn.default_encoding_id
                        else None
                    ),
                    [str(f.data_type) for f in defn.fields] if defn else [],
                )
            )
        enums = [str(ed.data_type_id) for ed in descriptor._enum_descriptions]
        descriptor._original_nodeids = (structs, enums)

    @staticmethod
    def _restore_original_nodeids(descriptor: Namespace) -> None:
        if descriptor._original_nodeids is None:
            return
        structs, enums = descriptor._original_nodeids
        for sd, (dtid, enc_id, field_dts) in zip(
            descriptor._structure_descriptions, structs
        ):
            sd.data_type_id = dtid
            defn = sd.structure_definition
            if defn is not None:
                if enc_id is not None:
                    defn.default_encoding_id = enc_id
                for f, dt in zip(defn.fields, field_dts):
                    f.data_type = dt
        for ed, dtid in zip(descriptor._enum_descriptions, enums):
            ed.data_type_id = dtid

    @staticmethod
    def _link_namespace(
        descriptor: Namespace,
        owner: _o6.Client | _o6.Server,
    ) -> None:
        """Link all pre-built capsules of a Namespace into the given owner."""
        if not descriptor._capsule:
            raise RuntimeError(
                "Namespace has no built capsules; call _build_types() first"
            )
        for capsule in descriptor._capsule:
            owner.link_custom_data_types(capsule)

        if isinstance(owner, _o6.Server):
            Namespaces._create_data_type_nodes(descriptor, owner)

    @staticmethod
    def _create_data_type_nodes(descriptor: Namespace, owner: _o6.Server) -> None:
        import o6

        HASSUBTYPE = o6.NodeId("i=45")
        STRUCTURE_NODE = o6.NodeId("i=22")
        ENUMERATION_NODE = o6.NodeId("i=29")

        for sd in descriptor._structure_descriptions:
            attr = o6.DataTypeAttributes()
            name = sd.name if isinstance(sd.name, str) else sd.name.name
            attr.display_name = o6.LocalizedText(name)
            try:
                owner.add_data_type_node(
                    o6.NodeId(str(sd.data_type_id)),
                    STRUCTURE_NODE,
                    HASSUBTYPE,
                    (
                        sd.name
                        if isinstance(sd.name, o6.QualifiedName)
                        else o6.QualifiedName(str(sd.name))
                    ),
                    attr,
                )
            except Exception:
                pass

        for ed in descriptor._enum_descriptions:
            attr = o6.DataTypeAttributes()
            name = ed.name if isinstance(ed.name, str) else ed.name.name
            attr.display_name = o6.LocalizedText(name)
            try:
                owner.add_data_type_node(
                    o6.NodeId(str(ed.data_type_id)),
                    ENUMERATION_NODE,
                    HASSUBTYPE,
                    (
                        ed.name
                        if isinstance(ed.name, o6.QualifiedName)
                        else o6.QualifiedName(str(ed.name))
                    ),
                    attr,
                )
            except Exception:
                pass
