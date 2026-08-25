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

"""Thin adapter around the vendored open62541 NodeSet compiler frontend."""

from __future__ import annotations

import importlib.util
import json
import logging
import os
import re
import sys
import tempfile
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType
from typing import Any, Iterable
from xml.etree import ElementTree

_ROOT = Path(__file__).resolve().parents[2]
_UPSTREAM = _ROOT / "deps/open62541/tools/nodeset_compiler"
_PACKAGE = "_o6_open62541_nodeset_compiler"
_DESCRIPTION_CACHE = _ROOT / "tools/nodeset_compiler/link_cache.json"
_URL = re.compile(r"^https?://\S+$", re.IGNORECASE)
_FIRST_PARAGRAPH = re.compile(
    r"<h[1-6][^>]*>.*?</h[1-6]>.*?<p\b[^>]*>(.*?)</p>",
    re.IGNORECASE | re.DOTALL,
)
_LOGGER = logging.getLogger(__name__)


def _upstream_package() -> ModuleType:
    package = sys.modules.get(_PACKAGE)
    if package is not None:
        return package
    spec = importlib.util.spec_from_file_location(
        _PACKAGE,
        _UPSTREAM / "__init__.py",
        submodule_search_locations=[str(_UPSTREAM)],
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load open62541 NodeSet compiler from {_UPSTREAM}")
    package = importlib.util.module_from_spec(spec)
    sys.modules[_PACKAGE] = package
    spec.loader.exec_module(package)
    return package


@dataclass(frozen=True)
class Endpoint:
    """One NodeId known to the combined upstream graph."""

    node: Any
    existing: bool
    creation_rank: int | None


@dataclass(frozen=True)
class ModelInput:
    path: Path
    shortname: str
    module: str | None = None
    supplementary_paths: tuple[Path, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "path", Path(self.path).resolve())
        object.__setattr__(
            self,
            "supplementary_paths",
            tuple(Path(path).resolve() for path in self.supplementary_paths),
        )
        if not self.shortname:
            raise ValueError("a model shortname is required")
        if self.module is None:
            object.__setattr__(self, "module", f"o6.ns.{self.shortname}")

    @property
    def paths(self) -> tuple[Path, ...]:
        return (self.path, *self.supplementary_paths)


@dataclass(frozen=True)
class NamespaceBinding:
    uri: str
    shortname: str
    module: str
    version: str
    publication_date: str
    target: bool


@dataclass(frozen=True)
class UnsupportedFeature:
    node_class: str
    nodeid: str
    feature: str


@dataclass(frozen=True)
class ExternalReference:
    source: str
    reference_type: str
    target: str
    is_forward: bool


@dataclass(frozen=True)
class LoadedNodeSet:
    """Parsed, linked and sorted open62541 graph plus its endpoint index."""

    nodeset: Any
    nodes: tuple[Any, ...]
    generated_nodes: tuple[Any, ...]
    endpoints: dict[str, Endpoint]
    namespace_bindings: tuple[NamespaceBinding, ...]
    xml_namespace_uris: tuple[str, ...]
    version: str
    publication_date: str
    datatype_source_paths: tuple[Path, ...]
    external_references: tuple[ExternalReference, ...]
    unsupported_features: tuple[UnsupportedFeature, ...]

    @property
    def namespace_uris(self) -> tuple[str, ...]:
        return tuple(binding.uri for binding in self.namespace_bindings)

    @property
    def target_binding(self) -> NamespaceBinding:
        return next(binding for binding in self.namespace_bindings if binding.target)

    def endpoint(self, nodeid: Any) -> Endpoint:
        try:
            return self.endpoints[str(nodeid)]
        except KeyError as exc:
            raise ValueError(f"unknown NodeSet endpoint {nodeid}") from exc


def _model_metadata(path: Path) -> tuple[str, str, str]:
    root = ElementTree.parse(path).getroot()
    model = root.find("{*}Models/{*}Model")
    uri = model.get("ModelUri") if model is not None else None
    if uri is None:
        uri_node = root.find("{*}NamespaceUris/{*}Uri")
        uri = uri_node.text if uri_node is not None else "http://opcfoundation.org/UA/"
    return (
        uri,
        model.get("Version", "1.0") if model is not None else "1.0",
        model.get("PublicationDate", "") if model is not None else "",
    )


def _xml_namespace_uris(path: Path) -> tuple[str, ...]:
    root = ElementTree.parse(path).getroot()
    return (
        "http://opcfoundation.org/UA/",
        *(element.text or "" for element in root.findall("{*}NamespaceUris/{*}Uri")),
    )


def _external_references(path: Path) -> tuple[ExternalReference, ...]:
    root = ElementTree.parse(path).getroot()
    aliases = {
        alias.get("Alias", ""): (alias.text or "").strip()
        for alias in root.findall("{*}Aliases/{*}Alias")
    }
    records: list[ExternalReference] = []
    for node in root:
        source = node.get("NodeId")
        if source is None:
            continue
        for reference in node.findall("{*}References/{*}Reference"):
            target = (reference.text or "").strip()
            if not (target.startswith("svr=") or target.startswith("nsu=")):
                continue
            reference_type = reference.get("ReferenceType", "")
            records.append(
                ExternalReference(
                    source=source,
                    reference_type=aliases.get(reference_type, reference_type),
                    target=target,
                    is_forward=reference.get("IsForward", "true").lower() != "false",
                )
            )
    return tuple(records)


def _without_external_references(path: Path) -> Any | None:
    tree = ElementTree.parse(path)
    namespace = tree.getroot().tag.partition("}")[0].removeprefix("{")
    changed = False
    for references in tree.getroot().iterfind(".//{*}References"):
        for reference in list(references):
            target = (reference.text or "").strip()
            if target.startswith("svr=") or target.startswith("nsu="):
                references.remove(reference)
                changed = True
    if not changed:
        return None
    temporary = tempfile.NamedTemporaryFile(suffix=".xml")
    if namespace:
        ElementTree.register_namespace("", namespace)
    tree.write(temporary.name, encoding="utf-8", xml_declaration=True)
    return temporary


def _detach_unresolved_references(graph: Any) -> tuple[ExternalReference, ...]:
    """Preserve open edges outside the closed graph required by upstream."""

    records: list[ExternalReference] = []
    for node in graph.nodes.values():
        retained = type(node.references)()
        for reference in node.references:
            if reference.target in graph.nodes:
                if isinstance(retained, dict):
                    retained[reference] = None
                else:
                    retained.append(reference)
                continue
            records.append(
                ExternalReference(
                    source=str(reference.source),
                    reference_type=str(reference.referenceType),
                    target=str(reference.target),
                    is_forward=reference.isForward,
                )
            )
        node.references = retained
    return tuple(records)


def _load_description_cache() -> dict[str, str]:
    try:
        data = json.loads(_DESCRIPTION_CACHE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return {str(url): str(description) for url, description in data.items() if description}


def _localized_text(element: ElementTree.Element, name: str) -> str:
    candidates = [
        (child.get("Locale", ""), "".join(child.itertext()).strip())
        for child in element.findall(f"{{*}}{name}")
    ]
    candidates = [(locale, text) for locale, text in candidates if text]
    if not candidates:
        return ""
    return min(
        candidates,
        key=lambda item: (
            0 if not item[0] else 1 if item[0].lower().startswith("en") else 2,
            item[0],
            item[1],
        ),
    )[1]


def _description_text(element: ElementTree.Element) -> str:
    return _localized_text(element, "Description")


def _resolved_localized_texts(path: Path, name: str) -> dict[str, str]:
    return {
        nodeid: text
        for element in ElementTree.parse(path).getroot()
        if (nodeid := element.get("NodeId")) is not None
        and (text := _localized_text(element, name))
    }


def _resolved_descriptions(
    path: Path, cache: dict[str, str], *, dictionary: bool = False
) -> tuple[dict[str, str], tuple[UnsupportedFeature, ...]]:
    descriptions: dict[str, str] = {}
    unsupported: list[UnsupportedFeature] = []
    for element in ElementTree.parse(path).getroot():
        nodeid = element.get("NodeId")
        if nodeid is None:
            continue
        description = _description_text(element)
        if not description:
            continue
        if _URL.fullmatch(description):
            # Supplementary dictionary NodeSets use Description for the
            # external dictionary-entry URL itself. It is an identifier, not
            # prose suitable for a server-side Description attribute.
            if dictionary:
                continue
            resolved = cache.get(description)
            if resolved is None:
                unsupported.append(
                    UnsupportedFeature(
                        element.tag.rsplit("}", 1)[-1],
                        nodeid,
                        f"uncached Description URL {description}",
                    )
                )
                continue
            description = resolved
        descriptions[nodeid] = description
    return descriptions, tuple(unsupported)


def _paragraph(html: str) -> str | None:
    match = _FIRST_PARAGRAPH.search(html)
    if match is None:
        return None
    text = re.sub(r"<[^>]+>", "", match.group(1))
    text = (
        text.replace("&nbsp;", " ")
        .replace("&amp;", "&")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&quot;", '"')
        .replace("&#39;", "'")
    )
    return re.sub(r"\s+", " ", text).strip() or None


def refresh_description_cache(paths: Iterable[Path]) -> int:
    """Explicitly fetch uncached Description URLs and atomically update the cache."""
    cache = _load_description_cache()
    urls = sorted(
        {
            description
            for path in paths
            for element in ElementTree.parse(path).getroot()
            if (description := _description_text(element))
            and _URL.fullmatch(description)
            and description not in cache
        }
    )
    for url in urls:
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "o6-nodeset-compiler/2.0"})
            with urllib.request.urlopen(request, timeout=20.0) as response:
                description = _paragraph(response.read(200_000).decode("utf-8", "replace"))
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            _LOGGER.warning("Could not resolve Description URL %s: %s", url, exc)
            continue
        if description:
            cache[url] = description
    temporary = _DESCRIPTION_CACHE.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(cache, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temporary, _DESCRIPTION_CACHE)
    return len(urls)


_NODE_ELEMENTS = {
    "DisplayName",
    "Description",
    "Category",
    "Documentation",
    "References",
    "RolePermissions",
    "Extensions",
}
_NODE_ATTRIBUTES = {
    "NodeId",
    "BrowseName",
    "WriteMask",
    "UserWriteMask",
    "AccessRestrictions",
    "HasNoPermissions",
    "SymbolicName",
    "ReleaseStatus",
}
_CLASS_FEATURES = {
    "UAObject": ({"EventNotifier", "ParentNodeId", "DesignToolOnly"}, set()),
    "UAVariable": (
        {
            "ParentNodeId",
            "DesignToolOnly",
            "DataType",
            "ValueRank",
            "ArrayDimensions",
            "AccessLevel",
            "UserAccessLevel",
            "MinimumSamplingInterval",
            "Historizing",
        },
        {"Value", "Translation"},
    ),
    "UAMethod": (
        {
            "ParentNodeId",
            "DesignToolOnly",
            "Executable",
            "UserExecutable",
            "MethodDeclarationId",
        },
        {"ArgumentDescription"},
    ),
    "UAView": (
        {"ParentNodeId", "DesignToolOnly", "ContainsNoLoops", "EventNotifier"},
        set(),
    ),
    "UAObjectType": ({"IsAbstract"}, set()),
    "UAVariableType": (
        {"IsAbstract", "DataType", "ValueRank", "ArrayDimensions"},
        {"Value"},
    ),
    "UADataType": ({"IsAbstract", "Purpose"}, {"Definition"}),
    "UAReferenceType": ({"IsAbstract", "Symmetric"}, {"InverseName"}),
}
_REJECTED_ELEMENTS = {"Translation", "ArgumentDescription"}
_STRUCTURAL_ATTRIBUTES = {
    "SymbolicName",
    "ReleaseStatus",
    "ParentNodeId",
    "DesignToolOnly",
    "MethodDeclarationId",
    "Purpose",
}


def _unsupported_features(path: Path) -> tuple[UnsupportedFeature, ...]:
    """Account for raw NodeSet2 features discarded by the upstream parser."""

    issues: list[UnsupportedFeature] = []
    root = ElementTree.parse(path).getroot()
    for node in root:
        node_class = node.tag.rsplit("}", 1)[-1]
        if node_class not in _CLASS_FEATURES:
            continue
        nodeid = node.get("NodeId", "<missing NodeId>")
        class_attributes, class_elements = _CLASS_FEATURES[node_class]
        known_attributes = _NODE_ATTRIBUTES | class_attributes
        for attribute in node.attrib:
            if attribute not in known_attributes:
                issues.append(UnsupportedFeature(node_class, nodeid, f"attribute {attribute}"))
            elif attribute == "HasNoPermissions":
                issues.append(UnsupportedFeature(node_class, nodeid, f"attribute {attribute}"))
            elif attribute not in _STRUCTURAL_ATTRIBUTES:
                pass  # Emitted by the NodeClass backend.
        known_elements = _NODE_ELEMENTS | class_elements
        for child in node:
            feature = child.tag.rsplit("}", 1)[-1]
            if feature not in known_elements or feature in _REJECTED_ELEMENTS:
                issues.append(UnsupportedFeature(node_class, nodeid, f"element {feature}"))
            elif feature in {"Category", "Documentation", "Extensions"}:
                pass  # Source metadata, not an AddressSpace attribute.
            elif feature in {"DisplayName", "Description", "InverseName"}:
                pass  # Deterministically collapsed by _resolved_localized_texts.
            elif feature == "References":
                for reference in child:
                    if reference.tag.rsplit("}", 1)[-1] != "Reference":
                        issues.append(
                            UnsupportedFeature(
                                node_class, nodeid, "References non-Reference element"
                            )
                        )
                        continue
                    if "ReferenceType" not in reference.attrib:
                        issues.append(
                            UnsupportedFeature(
                                node_class, nodeid, "Reference without ReferenceType"
                            )
                        )
                    for attribute in reference.attrib:
                        if attribute not in {"ReferenceType", "IsForward"}:
                            issues.append(
                                UnsupportedFeature(
                                    node_class,
                                    nodeid,
                                    f"Reference attribute {attribute}",
                                )
                            )
            elif feature == "Definition":
                issues.extend(_unsupported_definition(node_class, nodeid, child))
    return tuple(issues)


def _role_permissions(path: Path) -> dict[str, dict[str, int]]:
    permissions: dict[str, dict[str, int]] = {}
    for node in ElementTree.parse(path).getroot():
        nodeid = node.get("NodeId")
        role_permissions = node.find("{*}RolePermissions")
        if nodeid is None or role_permissions is None:
            continue
        permissions[nodeid] = {
            (entry.text or "").strip(): int(entry.get("Permissions", "0"))
            for entry in role_permissions.findall("{*}RolePermission")
        }
    return permissions


def _access_restrictions(path: Path) -> dict[str, int]:
    return {
        nodeid: int(value)
        for node in ElementTree.parse(path).getroot()
        if (nodeid := node.get("NodeId")) is not None
        and (value := node.get("AccessRestrictions")) is not None
    }


def _allow_subtypes(path: Path) -> dict[str, set[str]]:
    result: dict[str, set[str]] = {}
    for node in ElementTree.parse(path).getroot():
        nodeid = node.get("NodeId")
        definition = node.find("{*}Definition")
        if nodeid is None or definition is None:
            continue
        fields = {
            field.get("Name", "").casefold()
            for field in definition.findall("{*}Field")
            if field.get("AllowSubTypes", "false").lower() == "true"
        }
        if fields:
            result[nodeid] = fields
    return result


def _datatype_field_array_dimensions(path: Path) -> dict[str, dict[str, list[int]]]:
    result: dict[str, dict[str, list[int]]] = {}
    for node in ElementTree.parse(path).getroot():
        nodeid = node.get("NodeId")
        definition = node.find("{*}Definition")
        if nodeid is None or definition is None:
            continue
        fields = {
            field.get("Name", "").casefold(): [
                int(value) for value in field.get("ArrayDimensions", "").split(",")
            ]
            for field in definition.findall("{*}Field")
            if field.get("ArrayDimensions")
        }
        if fields:
            result[nodeid] = fields
    return result


def _canonical_nodeid(value: Any) -> str:
    text = str(value)
    return text[5:] if text.startswith("ns=0;") else text


def _graph_nodeid(
    nodeid: str, xml_namespace_uris: tuple[str, ...], graph_namespace_uris: list[str]
) -> str:
    match = re.fullmatch(r"(?:ns=(\d+);)?(.+)", nodeid)
    if match is None:
        return nodeid
    local_index = int(match.group(1) or 0)
    uri = xml_namespace_uris[local_index]
    graph_index = graph_namespace_uris.index(uri)
    return match.group(2) if graph_index == 0 else f"ns={graph_index};{match.group(2)}"


def _qualified_graph_nodeid(
    nodeid: str, xml_namespace_uris: tuple[str, ...], graph_namespace_uris: list[str]
) -> str:
    mapped = _graph_nodeid(nodeid, xml_namespace_uris, graph_namespace_uris)
    return f"ns=0;{mapped}" if mapped.startswith(("i=", "s=", "g=", "b=")) else mapped


def _unsupported_definition(
    node_class: str, nodeid: str, definition: ElementTree.Element
) -> list[UnsupportedFeature]:
    issues: list[UnsupportedFeature] = []
    known_definition = {"Name", "SymbolicName", "IsUnion", "IsOptionSet", "BaseType"}
    for attribute in definition.attrib:
        if attribute not in known_definition:
            issues.append(
                UnsupportedFeature(node_class, nodeid, f"Definition attribute {attribute}")
            )
    known_field = {
        "Name",
        "SymbolicName",
        "DataType",
        "ValueRank",
        "ArrayDimensions",
        "MaxStringLength",
        "Value",
        "IsOptional",
        "AllowSubTypes",
    }
    for field in definition:
        if field.tag.rsplit("}", 1)[-1] != "Field":
            issues.append(UnsupportedFeature(node_class, nodeid, "Definition non-Field element"))
            continue
        name = field.get("Name", "<unnamed>")
        for attribute, value in field.attrib.items():
            if attribute not in known_field:
                issues.append(
                    UnsupportedFeature(
                        node_class, nodeid, f"Definition field {name} attribute {attribute}"
                    )
                )
            elif attribute == "MaxStringLength" and int(value):
                issues.append(
                    UnsupportedFeature(
                        node_class, nodeid, f"Definition field {name} attribute {attribute}"
                    )
                )
        for child in field:
            feature = child.tag.rsplit("}", 1)[-1]
            if feature not in {"DisplayName", "Description"}:
                issues.append(
                    UnsupportedFeature(
                        node_class, nodeid, f"Definition field {name} element {feature}"
                    )
                )
    return issues


def load_nodeset(
    target: ModelInput,
    *,
    existing: Iterable[ModelInput] = (),
) -> LoadedNodeSet:
    """Load *target* through the upstream open62541 frontend.

    Dependencies are added as ``existing`` nodes, exactly like ``-e`` in the
    upstream compiler. The returned order is the result of its ``sortNodes``.
    """

    _upstream_package()
    nodeset_module = __import__(f"{_PACKAGE}.nodeset", fromlist=["nodeset"])
    graph = nodeset_module.NodeSet()
    target_input = target
    existing_inputs = tuple(existing)
    target_path = target_input.path
    target_paths = target_input.paths
    external_references = tuple(
        reference for path in target_paths for reference in _external_references(path)
    )
    sanitized_targets = tuple(_without_external_references(path) for path in target_paths)
    inputs = (*existing_inputs, target_input)
    metadata = {model_input: _model_metadata(model_input.path) for model_input in inputs}
    target_uri, version, publication_date = metadata[target_input]
    inputs_by_uri: dict[str, tuple[ModelInput, bool]] = {}
    for model_input in inputs:
        uri, _, _ = metadata[model_input]
        if uri in inputs_by_uri:
            raise ValueError(f"namespace {uri} was supplied more than once")
        inputs_by_uri[uri] = model_input, model_input is target_input
    existing_files = []
    target_files = []
    try:
        for model_input in existing_inputs:
            for path in model_input.paths:
                handle = path.open("rb")
                existing_files.append(handle)
                graph.addNodeSet(handle, True, typesArray="UA_TYPES")
        for path, sanitized in zip(target_paths, sanitized_targets, strict=True):
            handle = open(sanitized.name, "rb") if sanitized else path.open("rb")
            target_files.append(handle)
            graph.addNodeSet(handle, False, typesArray="UA_TYPES")
        unresolved_references = _detach_unresolved_references(graph)
        graph.sanitize()
        graph.addInverseReferences()
        graph.setNodeParent()
        generated_indexes = {int(node.id.ns) for node in graph.nodes.values() if not node.hidden}
        if generated_indexes != {0}:
            graph.sortNodes()
    finally:
        for handle in [*existing_files, *target_files]:
            handle.close()
        for sanitized in sanitized_targets:
            if sanitized is not None:
                sanitized.close()

    nodes = tuple(graph.nodes.values())
    role_permissions: dict[str, dict[str, int]] = {}
    access_restrictions: dict[str, int] = {}
    allow_subtypes: dict[str, set[str]] = {}
    field_array_dimensions: dict[str, dict[str, list[int]]] = {}
    descriptions: dict[str, str] = {}
    display_names: dict[str, str] = {}
    inverse_names: dict[str, str] = {}
    description_issues: tuple[UnsupportedFeature, ...] = ()
    description_cache = _load_description_cache()
    for index, path in enumerate(target_paths):
        role_permissions.update(_role_permissions(path))
        access_restrictions.update(_access_restrictions(path))
        allow_subtypes.update(_allow_subtypes(path))
        field_array_dimensions.update(_datatype_field_array_dimensions(path))
        path_descriptions, path_issues = _resolved_descriptions(
            path,
            description_cache,
            dictionary=index > 0 or "/Dictionary/" in _model_metadata(path)[0],
        )
        descriptions.update(path_descriptions)
        description_issues += path_issues
        display_names.update(_resolved_localized_texts(path, "DisplayName"))
        inverse_names.update(_resolved_localized_texts(path, "InverseName"))
    xml_namespace_uris = _xml_namespace_uris(target_path)
    descriptions = {
        _graph_nodeid(nodeid, xml_namespace_uris, graph.namespaces): description
        for nodeid, description in descriptions.items()
    }
    display_names = {
        _graph_nodeid(nodeid, xml_namespace_uris, graph.namespaces): text
        for nodeid, text in display_names.items()
    }
    inverse_names = {
        _graph_nodeid(nodeid, xml_namespace_uris, graph.namespaces): text
        for nodeid, text in inverse_names.items()
    }
    for node in nodes:
        nodeid = _canonical_nodeid(node.id)
        node.rolePermissions = role_permissions.get(nodeid, {})
        node.accessRestrictions = access_restrictions.get(nodeid, 0)
        node.allowSubTypes = allow_subtypes.get(nodeid, set())
        node.fieldArrayDimensions = field_array_dimensions.get(nodeid, {})
        node.resolvedDescription = descriptions.get(nodeid)
        node.resolvedDisplayName = display_names.get(nodeid)
        node.resolvedInverseName = inverse_names.get(nodeid)
    generated = tuple(node for node in nodes if not node.hidden)
    generated_ids = {str(node.id) for node in generated}
    rank = {str(node.id): index for index, node in enumerate(generated)}
    endpoints = {
        str(node.id): Endpoint(
            node=node,
            existing=bool(node.hidden or str(node.id) not in generated_ids),
            creation_rank=rank.get(str(node.id)),
        )
        for node in nodes
    }
    bindings: list[NamespaceBinding] = []
    for uri in graph.namespaces:
        try:
            model_input, is_target = inputs_by_uri[uri]
        except KeyError as exc:
            raise ValueError(f"namespace {uri} has no supplied model binding") from exc
        bindings.append(
            NamespaceBinding(
                uri=uri,
                shortname=model_input.shortname,
                module=model_input.module,
                version=metadata[model_input][1],
                publication_date=metadata[model_input][2],
                target=is_target,
            )
        )
    return LoadedNodeSet(
        nodeset=graph,
        nodes=nodes,
        generated_nodes=generated,
        endpoints=endpoints,
        namespace_bindings=tuple(bindings),
        xml_namespace_uris=xml_namespace_uris,
        version=version,
        publication_date=publication_date,
        datatype_source_paths=tuple(path for model_input in inputs for path in model_input.paths),
        external_references=tuple(
            ExternalReference(
                source=_graph_nodeid(reference.source, xml_namespace_uris, graph.namespaces),
                reference_type=_qualified_graph_nodeid(
                    reference.reference_type, xml_namespace_uris, graph.namespaces
                ),
                target=reference.target,
                is_forward=reference.is_forward,
            )
            for reference in external_references
        )
        + unresolved_references,
        unsupported_features=(
            *(feature for path in target_paths for feature in _unsupported_features(path)),
            *description_issues,
        ),
    )
