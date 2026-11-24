# Copyright 2026 (c) o6 Automation GmbH
# SPDX-License-Identifier: AGPL-3.0-or-later
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

"""Registers a server's custom DataTypes with the client decoder.

`_DataTypeLoader` registers the structures of an `_InformationModel` from the
definitions and encodings already read. `exportInformationModel` gives it the
crawled model; `loadRemoteDataTypes` gives it the DataType hierarchy that
`_RemoteDataTypes` browses on its own.
"""

from __future__ import annotations

import asyncio
import logging
from collections import deque
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Iterable, cast

import numpy as np

import o6
from o6._browse import _browse_description, _finish_request
from o6._datatype_registration import _INT_ENUM_FACTORY, add_datatype, add_enum
from o6._registration_lock import REGISTRATION_LOCK
from o6._information_model import (
    _BASE_DATA_TYPE,
    _ENUMERATION,
    _HAS_ENCODING,
    _HAS_SUBTYPE,
    NS0_URI,
    NamespaceInfo,
    NodeRef,
    QualifiedNameRef,
    TypeInfo,
    _InformationModel,
    _ns0,
)
from o6.ns import _GLOBAL_SCOPE, NamespaceModule, _module_for_index, ns0

if TYPE_CHECKING:
    from o6.client import Client

_logger = logging.getLogger("o6.informationmodel")

_NodeClass = ns0.datatypes.NodeClass
_Direction = ns0.datatypes.BrowseDirection
_ALL_RESULTS = int(ns0.datatypes.BrowseResultMask.ALL)

_STRUCTURE = _ns0(22)
_MAX_NODES_PER_READ = _ns0(11705)
_MAX_NODES_PER_BROWSE = _ns0(11710)

# Operations per request, lowered to the server's operation limits.
_BATCH_SIZE = 500

_NULL_NODE_ID = o6.NodeId(0)
_DEFAULT_BINARY = QualifiedNameRef(NS0_URI, "Default Binary")
# The ns0 DataTypes of the builtin types a simple DataType can derive from:
# Boolean (1) to DiagnosticInfo (25), but Structure (22) and BaseDataType (24).
_BUILTIN_TYPE_IDS = frozenset(range(1, 26)) - {22, 24}


def _bad(status: o6.StatusCode | None) -> bool:
    return status is not None and o6.StatusCode.BAD in status


def _isNull(nodeId: o6.NodeId | None) -> bool:
    return nodeId is None or nodeId == _NULL_NODE_ID


def _ns0NodeId(node_id: NodeRef) -> o6.NodeId:
    """The client NodeId of one of the numeric ns0 constants."""
    return o6.NodeId(cast(int, node_id.identifier))


def _read_id(nodeId: o6.NodeId, attribute: o6.AttributeId) -> ns0.datatypes.ReadValueId:
    item = ns0.datatypes.ReadValueId()
    item.nodeId = nodeId
    item.attributeId = attribute
    return item


def _emptyModel(client: Client) -> _InformationModel:
    """A model without nodes, with the namespaces of the client's last mapping refresh."""
    index_uris = {0: NS0_URI}
    for uri, global_index, _wire_index in getattr(client, "_namespace_snapshot", ()):
        index_uris.setdefault(global_index, uri)
    uris = getattr(client, "_namespace_snapshot_uris", None) or [NS0_URI]
    return _InformationModel({uri: NamespaceInfo(uri) for uri in uris if uri}, index_uris)


def _unpackagedNamespaces(client: Client) -> set[str]:
    """The server namespace URIs the client maps to a registration without a package.

    These are the client-scoped registrations of `updateRemoteNamespaces` and
    of the server's namespace 1. A namespace mapped to a global registration,
    whether bundled or declared by the application, has its own declarations.
    """
    uris = set()
    for uri, global_index, wire_index in getattr(client, "_namespace_snapshot", ()):
        namespace = _module_for_index(global_index)
        if (
            wire_index > 0
            and isinstance(namespace, NamespaceModule)
            and namespace.scope != _GLOBAL_SCOPE
            and "_o6_source" not in vars(namespace)
        ):
            uris.add(uri)
    return uris


class _Services:
    """Browse and Read in batches within the server's operation limits."""

    # Completes the message of a failed service call.
    _activity = "while crawling the information model"

    def __init__(self, client: Client) -> None:
        self.client = client
        self.batchSizes = {"Read": _BATCH_SIZE, "Browse": _BATCH_SIZE}

    async def _inBatches(
        self,
        service: str,
        items: list[Any],
        send: Callable[[list[Any]], Awaitable[tuple[o6.StatusCode, list[Any]]]],
    ) -> list[Any]:
        """Send `items` in batches, halving the batch on BadTooManyOperations."""
        results: list[Any] = []
        while len(results) < len(items):
            size = self.batchSizes[service]
            chunk = items[len(results) : len(results) + size]
            status, chunk_results = await send(chunk)
            if status == o6.StatusCode.BAD_TOO_MANY_OPERATIONS and size > 1:
                self.batchSizes[service] = size // 2
                continue
            status.check(message=f"{service} {self._activity}")
            if len(chunk_results) != len(chunk):
                raise RuntimeError(f"{service} result count does not match the request")
            results.extend(chunk_results)
        return results

    async def _read(self, items: list[ns0.datatypes.ReadValueId]) -> list[o6.DataValue]:
        async def send(chunk: list[Any]) -> tuple[o6.StatusCode, list[Any]]:
            request = ns0.datatypes.ReadRequest()
            request.timestampsToReturn = ns0.datatypes.TimestampsToReturn.NEITHER
            request.nodesToRead = chunk
            response = await self.client._service_read(request)
            return response.responseHeader.serviceResult, list(response.results)

        return await self._inBatches("Read", items, send)

    async def _browse(
        self, descriptions: list[ns0.datatypes.BrowseDescription]
    ) -> list[tuple[o6.StatusCode, list[ns0.datatypes.ReferenceDescription]]]:
        """Browse in batches and follow every continuation point."""

        async def send(chunk: list[Any]) -> tuple[o6.StatusCode, list[Any]]:
            request = ns0.datatypes.BrowseRequest()
            request.nodesToBrowse = chunk
            response = await self.client._service_browse(request)
            status = response.responseHeader.serviceResult
            if _bad(status):
                return status, []
            statuses = [o6.StatusCode(result.statusCode) for result in response.results]
            collected = [list(result.references) for result in response.results]
            pending = {
                index: result.continuationPoint
                for index, result in enumerate(response.results)
                if result.continuationPoint
            }
            try:
                while pending:
                    next_response = await self._browseNext(list(pending.values()), False)
                    indices, pending = list(pending), {}
                    for index, page in zip(indices, next_response.results):
                        collected[index].extend(page.references)
                        if _bad(page.statusCode):
                            statuses[index] = o6.StatusCode(page.statusCode)
                        elif page.continuationPoint:
                            pending[index] = page.continuationPoint
            except BaseException:
                if pending:  # free the server's continuation points
                    await _finish_request(self._browseNext(list(pending.values()), True))
                raise
            return status, list(zip(statuses, collected))

        return await self._inBatches("Browse", descriptions, send)

    async def _browseNext(self, points: list[bytes], release: bool) -> Any:
        request = ns0.datatypes.BrowseNextRequest()
        request.releaseContinuationPoints = release
        request.continuationPoints = points
        response = await self.client._service_browseNext(request)
        response.responseHeader.serviceResult.check(message=f"BrowseNext {self._activity}")
        if len(response.results) != len(points):
            raise RuntimeError("BrowseNext result count does not match the request")
        return response

    async def _readOperationLimits(self) -> None:
        limits = [
            _read_id(_ns0NodeId(limit), o6.AttributeId.VALUE)
            for limit in (_MAX_NODES_PER_READ, _MAX_NODES_PER_BROWSE)
        ]
        try:
            per_read, per_browse = await self._read(limits)
        except o6.StatusCodeError:
            return
        for service, limit in (("Read", per_read), ("Browse", per_browse)):
            if not _bad(limit.status) and limit.value:
                self.batchSizes[service] = min(self.batchSizes[service], int(limit.value))


class _DataTypeLoader:
    """Registers the structures of a model the client cannot decode yet.

    Uses the definitions and encodings already read, without service calls.
    Enumerations are registered as field types of a structure; a field of a
    simple DataType, such as an OptionSet of UInt32, is declared as its builtin,
    encoded the same.
    """

    def __init__(
        self,
        client: Client,
        model: _InformationModel,
        clientIds: dict[NodeRef, o6.NodeId],
        binaryEncoding: Callable[[NodeRef], NodeRef | None],
        namespaces: Iterable[str] | None = None,
    ) -> None:
        """
        Args:
            client: The client whose decoder gets the DataTypes.
            model: The DataTypes in `model.types`, with their supertypes.
            clientIds: The client NodeIds of the browsed nodes.
            binaryEncoding: The Default Binary encoding of a structure, for
                definitions without a `defaultEncodingId`.
            namespaces: The namespace URIs to register structures of; `None`
                for all but ns0.
        """
        self.client = client
        self.model = model
        self.clientIds = clientIds
        self.binaryEncoding = binaryEncoding
        self.namespaces = None if namespaces is None else set(namespaces)
        self.decodable: dict[NodeRef, bool] = {}
        self.pendingTypes: dict[NodeRef, TypeInfo] = {}
        self.loadedTypes: set[NodeRef] = set()
        self.failedTypes: dict[NodeRef, str] = {}
        self.registered: list[type] = []

    def _wanted(self, type_id: NodeRef) -> bool:
        if self.namespaces is None:
            return not type_id.isNs0
        return type_id.namespaceUri in self.namespaces

    def load(
        self, failed: dict[NodeRef, str] | None = None, reported: set[NodeRef] | None = None
    ) -> list[type]:
        """Register the structures and their field types, and apply them to the client's decoder.

        Args:
            failed: DataTypes known to be unloadable, by reason. They are
                warned about with the rest.
            reported: DataTypes already warned about, which are not warned
                about again. The newly warned ones are added.

        Returns:
            The registered Python classes, in registration order.
        """
        with REGISTRATION_LOCK:
            return self._load(failed, reported)

    def _load(self, failed: dict[NodeRef, str] | None, reported: set[NodeRef] | None) -> list[type]:
        self.failedTypes.update(failed or {})
        pending = self.pendingTypes
        pending.update(
            (type_id, info)
            for type_id, info in self.model.types.items()
            if self._wanted(type_id)
            and type_id not in self.failedTypes
            and isinstance(info.definition, ns0.datatypes.StructureDefinition)
            and not self._decodable(type_id)
        )
        # A structure needs its field types first.
        progress = True
        while pending and progress:
            progress = False
            for type_id, info in list(pending.items()):
                fields = self._fields(info.definition)
                if fields is None:
                    continue
                del pending[type_id]
                progress |= self._register(
                    type_id,
                    add_datatype,
                    {"structure_type": info.definition.structureType, "fields": fields},
                    self._binaryEncoding(type_id, info.definition),
                )
        for type_id in pending:
            self.failedTypes.setdefault(type_id, "a field type cannot be loaded")
        for type_id, reason in self.failedTypes.items():
            if reported is not None:
                if type_id in reported:
                    continue
                reported.add(type_id)
            _logger.warning(f"DataType {type_id} cannot be loaded to decode values: {reason}")
        if self.loadedTypes:
            # Copy the registered types into the client's decoder.
            client = cast(Any, self.client)
            client._apply_namespace_snapshot(
                client._namespace_snapshot_uris, list(client._namespace_snapshot)
            )
        return self.registered

    def _clientNodeId(self, node_id: NodeRef) -> o6.NodeId:
        index = self.model.globalIndex(node_id.namespaceUri)
        return o6.NodeId(f"ns={index};{node_id.identifierText}")

    def _decodable(self, type_id: NodeRef) -> bool:
        if type_id not in self.decodable:
            node_id = self.clientIds.get(type_id) or self._clientNodeId(type_id)
            found = cast(Any, self.client)._find_data_type(node_id)
            self.decodable[type_id] = found is not None
        return self.decodable[type_id]

    def _register(
        self, type_id: NodeRef, register: Callable[..., Any], *args: Any, **kwargs: Any
    ) -> bool:
        """Register a DataType of the model with `add_datatype` or `add_enum`."""
        try:
            python_type, _description = register(
                self.model.shortname(type_id.namespaceUri),
                str(self._clientNodeId(type_id)),
                self.model.types[type_id].browseName.name,
                *args,
                **kwargs,
            )
        except (RuntimeError, TypeError, ValueError, o6.StatusCodeError) as error:
            self.failedTypes[type_id] = str(error)
            return False
        self.loadedTypes.add(type_id)
        self.registered.append(python_type)
        return True

    def _fields(self, definition: ns0.datatypes.StructureDefinition) -> list[dict[str, Any]] | None:
        """The fields to register a structure with; `None` until all field types are loaded."""
        fields = []
        for item in definition.fields or ():
            data_type = self._fieldType(self.model.ref(item.dataType))
            if data_type is None:
                return None
            fields.append(
                {
                    "name": str(item.name),
                    "description": item.description,
                    "is_optional": bool(item.isOptional),
                    "value_rank": int(item.valueRank),
                    "data_type": str(data_type),
                    "array_dimensions": item.arrayDimensions,
                    "max_string_length": item.maxStringLength,
                }
            )
        return fields

    def _fieldType(self, type_id: NodeRef) -> o6.NodeId | None:
        """The client NodeId a field is registered with; `None` while it cannot be decoded."""
        if type_id in self.loadedTypes or (
            type_id not in self.pendingTypes and self._decodable(type_id)
        ):
            return self._clientNodeId(type_id)
        info = self.model.types.get(type_id)
        if info is None or type_id in self.pendingTypes or type_id in self.failedTypes:
            return None
        definition = info.definition
        if isinstance(definition, ns0.datatypes.EnumDefinition) and self.model.isSubtypeOf(
            type_id, _ENUMERATION
        ):
            entries = [
                {"name": str(entry.name), "value": int(entry.value)}
                for entry in definition.fields or ()
            ]
            if not self._register(
                type_id, add_enum, {"fields": entries}, enum_factory=_INT_ENUM_FACTORY
            ):
                return None
            return self._clientNodeId(type_id)
        builtin = next((a for a in self.model._ancestors(type_id) if a.isNs0), None)
        if builtin is not None and builtin.identifier in _BUILTIN_TYPE_IDS:
            return _ns0NodeId(builtin)
        return None

    def _binaryEncoding(
        self, type_id: NodeRef, definition: ns0.datatypes.StructureDefinition
    ) -> str | None:
        """The structure's binary encoding; servers may leave it out of the definition."""
        if not _isNull(definition.defaultEncodingId):
            return str(definition.defaultEncodingId)
        binary = self.binaryEncoding(type_id)
        return None if binary is None else str(self._clientNodeId(binary))


class _RemoteDataTypes(_Services):
    """Loads the DataTypes of the server's unpackaged namespaces, without crawling the address space.

    Browses the DataType hierarchy below BaseDataType and reads only what
    `_DataTypeLoader` needs: the DataTypeDefinition and IsAbstract of the
    DataTypes in unpackaged namespaces, and the encodings of structures whose
    definition names none.
    """

    _activity = "while loading the server's DataTypes"

    def __init__(self, client: Client) -> None:
        super().__init__(client)
        self.clientIds: dict[NodeRef, o6.NodeId] = {}
        self.encodings: dict[NodeRef, NodeRef] = {}
        self.failedTypes: dict[NodeRef, str] = {}

    async def run(self) -> list[type]:
        if not self.client.connected:
            raise RuntimeError("Client is not connected")
        await cast(Awaitable[None], self.client.updateRemoteNamespaces())
        self.model = _emptyModel(self.client)
        namespaces = _unpackagedNamespaces(self.client)
        if not namespaces:
            return []
        await self._readOperationLimits()
        await self._browseHierarchy()
        candidates = [t for t in self.model.types if t.namespaceUri in namespaces]
        await self._readDefinitions(candidates)
        await self._browseEncodings(candidates)
        loader = _DataTypeLoader(
            self.client, self.model, self.clientIds, self.encodings.get, namespaces
        )
        return loader.load(self.failedTypes, cast(Any, self.client)._reportedDataTypes)

    async def _browseHierarchy(self) -> None:
        """Collect every DataType below BaseDataType, with its BrowseName and supertype."""
        model = self.model
        self.clientIds[_BASE_DATA_TYPE] = _ns0NodeId(_BASE_DATA_TYPE)
        model.types[_BASE_DATA_TYPE] = TypeInfo(
            _BASE_DATA_TYPE, QualifiedNameRef(NS0_URI, "BaseDataType")
        )
        queue = deque([_BASE_DATA_TYPE])
        while queue:
            batch = [queue.popleft() for _ in range(min(len(queue), self.batchSizes["Browse"]))]
            browsed = await self._browse(
                [
                    _browse_description(
                        self.clientIds[type_id],
                        _Direction.FORWARD,
                        _ns0NodeId(_HAS_SUBTYPE),
                        False,
                        int(_NodeClass.DATA_TYPE),
                        _ALL_RESULTS,
                    )
                    for type_id in batch
                ]
            )
            for supertype, (status, subtypes) in zip(batch, browsed):
                if _bad(status):
                    if not supertype.isNs0:
                        _logger.warning(f"Browse of {supertype} failed: {status.name}")
                    continue
                for description in subtypes:
                    if description.nodeId.svr:
                        continue  # on another server
                    try:
                        type_id = model.ref(description.nodeId)
                        client_id = o6.NodeId(description.nodeId)
                        browse_name = model.qualifiedName(description.browseName)
                    except (KeyError, TypeError, ValueError):
                        continue  # in a namespace the client has not mapped
                    if type_id in model.types:
                        continue
                    self.clientIds[type_id] = client_id
                    model.types[type_id] = TypeInfo(type_id, browse_name, supertype)
                    queue.append(type_id)

    async def _readDefinitions(self, candidates: list[NodeRef]) -> None:
        """Read the DataTypeDefinition of the candidates; note the structures without one."""
        attributes = (o6.AttributeId.DATA_TYPE_DEFINITION, o6.AttributeId.IS_ABSTRACT)
        reads = await self._read(
            [_read_id(self.clientIds[t], a) for t in candidates for a in attributes]
        )
        for index, type_id in enumerate(candidates):
            definition, is_abstract = reads[2 * index : 2 * index + 2]
            self._setDefinition(type_id, definition, is_abstract)

    def _setDefinition(
        self, type_id: NodeRef, definition: o6.DataValue, is_abstract: o6.DataValue
    ) -> None:
        """Keep a DataTypeDefinition read; note a structure without one.

        Needs the supertypes of `type_id` in the model.
        """
        info = self.model.types[type_id]
        if not _bad(definition.status):
            info.definition = definition.value
        if not self.model.isSubtypeOf(type_id, _STRUCTURE) or isinstance(
            info.definition, ns0.datatypes.StructureDefinition
        ):
            return
        if not _bad(is_abstract.status) and is_abstract.value:
            return  # never encoded
        if definition.status == o6.StatusCode.BAD_ATTRIBUTE_ID_INVALID:
            # Servers before OPC UA 1.04 describe structures in DataTypeDictionaries.
            reason = "the server provides no DataTypeDefinition attribute"
        elif _bad(definition.status):
            reason = f"its DataTypeDefinition is not readable: {definition.status!r}"
        else:
            reason = "its DataTypeDefinition is not a StructureDefinition"
        self.failedTypes[type_id] = reason

    async def _browseEncodings(self, candidates: list[NodeRef]) -> None:
        """Find the Default Binary encoding of the structures whose definition names none."""
        wanted = [
            type_id
            for type_id in candidates
            if isinstance(
                definition := self.model.types[type_id].definition,
                ns0.datatypes.StructureDefinition,
            )
            and _isNull(definition.defaultEncodingId)
        ]
        browsed = await self._browse(
            [
                _browse_description(
                    self.clientIds[type_id],
                    _Direction.FORWARD,
                    _ns0NodeId(_HAS_ENCODING),
                    False,
                    int(_NodeClass.OBJECT),
                    _ALL_RESULTS,
                )
                for type_id in wanted
            ]
        )
        for type_id, (status, encodings) in zip(wanted, browsed):
            if _bad(status):
                continue
            for encoding in encodings:
                if encoding.nodeId.svr:
                    continue
                try:
                    name = self.model.qualifiedName(encoding.browseName)
                    if name == _DEFAULT_BINARY:
                        self.encodings[type_id] = self.model.ref(encoding.nodeId)
                except KeyError:
                    continue


# The ns0 DataTypes a supertype chain ends at for the loader: Structure,
# Enumeration, BaseDataType and the builtins.
_ROOT_TYPE_IDS = _BUILTIN_TYPE_IDS | {22, 24, 29}
# Leaves of a result that never hold an ExtensionObject.
_PLAIN_VALUES = (type(None), bool, int, float, str, bytes)


class _DataTypeLookup(_RemoteDataTypes):
    """Loads the DataTypes of binary encodings the client cannot decode.

    Browses from each encoding to its DataType, then level by level to the
    supertypes and the field types the DataTypes need, with one Browse and one
    Read per level, and registers them with `_DataTypeLoader`.
    """

    _activity = "while loading the DataType of a received value"

    async def load(self, encodings: list[o6.NodeId]) -> None:
        """Load the DataTypes of `encodings`; warn about the ones without a DataType."""
        self.model = model = _emptyModel(self.client)
        namespaces = _unpackagedNamespaces(self.client)
        browsed = await self._browse(
            [
                _browse_description(
                    encoding,
                    _Direction.INVERSE,
                    _ns0NodeId(_HAS_ENCODING),
                    False,
                    int(_NodeClass.DATA_TYPE),
                    _ALL_RESULTS,
                )
                for encoding in encodings
            ]
        )
        roots = []
        for encoding, (status, references) in zip(encodings, browsed):
            reference = next((r for r in references if not r.nodeId.svr), None)
            if _bad(status) or reference is None:
                reason = status.name if _bad(status) else "no DataType has this encoding"
                _logger.warning(
                    f"Values with encoding {model.ref(encoding)} cannot be decoded: {reason}"
                )
                continue
            type_id = model.ref(reference.nodeId)
            self.encodings[type_id] = model.ref(encoding)
            if type_id not in model.types:
                browse_name = model.qualifiedName(reference.browseName)
                model.types[type_id] = TypeInfo(type_id, browse_name)
                self.clientIds[type_id] = o6.NodeId(reference.nodeId)
                roots.append(type_id)
        candidates = await self._browseTypes(roots)
        await self._browseEncodings([t for t in candidates if t not in self.encodings])
        loader = _DataTypeLoader(self.client, model, self.clientIds, self.encodings.get, namespaces)
        loader.load(self.failedTypes, cast(Any, self.client)._reportedDataTypes)

    async def _browseTypes(self, roots: list[NodeRef]) -> list[NodeRef]:
        """Add the DataTypes with their supertypes and undecodable field types to the model.

        Returns:
            The DataTypes outside ns0 whose definition was read.
        """
        model = self.model
        reads: dict[NodeRef, tuple[o6.DataValue, o6.DataValue]] = {}
        level = roots
        while level:
            found: list[NodeRef] = []

            def visit(type_id: NodeRef, client_id: o6.NodeId, name: QualifiedNameRef) -> None:
                if type_id not in model.types:
                    model.types[type_id] = TypeInfo(type_id, name)
                    self.clientIds[type_id] = client_id
                    found.append(type_id)

            supertypes = await self._browse(
                [
                    _browse_description(
                        self.clientIds[type_id],
                        _Direction.INVERSE,
                        _ns0NodeId(_HAS_SUBTYPE),
                        False,
                        int(_NodeClass.DATA_TYPE),
                        _ALL_RESULTS,
                    )
                    for type_id in level
                ]
            )
            for type_id, (status, references) in zip(level, supertypes):
                reference = next((r for r in references if not r.nodeId.svr), None)
                if _bad(status) or reference is None:
                    continue
                try:
                    supertype = model.ref(reference.nodeId)
                except KeyError:
                    continue  # in a namespace the client has not mapped
                model.types[type_id].supertype = supertype
                if not supertype.isNs0 or supertype.identifier not in _ROOT_TYPE_IDS:
                    name = model.qualifiedName(reference.browseName)
                    visit(supertype, o6.NodeId(reference.nodeId), name)

            remote = [type_id for type_id in level if not type_id.isNs0]
            attributes = (
                o6.AttributeId.BROWSE_NAME,
                o6.AttributeId.DATA_TYPE_DEFINITION,
                o6.AttributeId.IS_ABSTRACT,
            )
            values = await self._read(
                [_read_id(self.clientIds[t], a) for t in remote for a in attributes]
            )
            for index, type_id in enumerate(remote):
                browse_name, definition, is_abstract = values[3 * index : 3 * index + 3]
                if not _bad(browse_name.status):
                    model.types[type_id].browseName = model.qualifiedName(browse_name.value)
                reads[type_id] = (definition, is_abstract)
                if _bad(definition.status) or not isinstance(
                    definition.value, ns0.datatypes.StructureDefinition
                ):
                    continue
                for field in definition.value.fields or ():
                    try:
                        field_id = model.ref(field.dataType)
                    except KeyError:
                        continue  # the loader fails the structure

                    client_id = o6.NodeId(field.dataType)
                    if cast(Any, self.client)._find_data_type(client_id) is None:
                        visit(field_id, client_id, QualifiedNameRef(field_id.namespaceUri, ""))
            level = found

        # The definitions need the supertype chains, complete only now.
        for type_id, (definition, is_abstract) in reads.items():
            self._setDefinition(type_id, definition, is_abstract)
        return list(reads)


class _UnknownDataTypes:
    """Decodes values of DataTypes a client does not know, loading the DataTypes on demand.

    Only binary bodies of unpackaged namespaces are loaded. Each encoding is
    looked up at most once per client, whether the lookup succeeds or not.
    """

    def __init__(self, client: Client) -> None:
        self.client = client
        # Encodings not to look up again: looked up, skipped or warned about.
        self.settled: set[o6.NodeId] = set()
        self.pending: dict[o6.NodeId, asyncio.Task[None]] = {}

    @property
    def enabled(self) -> bool:
        return bool(self.client.config.loadUnknownDataTypes)

    async def decode(self, value: Any) -> Any:
        """Decode the unknown values in a result, loading their DataTypes first.

        Lists, NumPy object arrays and dicts in `value` are updated in place.
        """
        if not self.enabled:
            return value
        value, unknown = self._redecode(value)
        tried: set[o6.NodeId] = set()
        # A loaded structure can hold another unknown one in a Variant field.
        # Each encoding is waited for once, so this ends, also when a lookup
        # is abandoned on a lost connection.
        while lookups := self._lookUp([e for e in unknown if e not in tried]):
            tried.update(unknown)
            # Unlike gather, wait leaves the shared lookups running if the caller is cancelled.
            await asyncio.wait(lookups)
            value, unknown = self._redecode(value)
        return value

    def decodeNotification(self, value: Any) -> Any:
        """Decode a notification with the DataTypes known now; load unknown ones in the background.

        The notification is not held back, so delivery keeps its order.
        """
        if not self.enabled:
            return value
        value, unknown = self._redecode(value)
        self._lookUp(unknown)
        return value

    def cancel(self) -> None:
        """Stop the running lookups; their encodings are looked up again later."""
        for task in set(self.pending.values()):
            task.cancel()

    def _redecode(self, value: Any) -> tuple[Any, list[o6.NodeId]]:
        """Decode the encoded ExtensionObjects in `value` with the DataTypes the client has now.

        Returns:
            The value, and the binary encodings that stay undecoded.
        """
        unknown: list[o6.NodeId] = []
        redecode = cast(Any, self.client)._redecode

        def walk(item: Any) -> Any:
            if isinstance(item, _PLAIN_VALUES):
                return item
            if isinstance(item, list):
                item[:] = [walk(element) for element in item]
            elif isinstance(item, tuple):
                return tuple(walk(element) for element in item)
            elif isinstance(item, np.ndarray):
                if item.dtype == object:
                    for index, cell in np.ndenumerate(cast(Any, item)):
                        item[index] = walk(cell)
            elif isinstance(item, dict):
                for key, element in item.items():
                    item[key] = walk(element)
            elif isinstance(item, o6.DataValue):
                if not isinstance(item.value, _PLAIN_VALUES):
                    item.value = walk(item.value)
            else:
                item, binary, xml = redecode(item)
                unknown.extend(binary)
                for encoding in xml:
                    self._settle(encoding, "only binary bodies are decoded")
            return item

        return walk(value), unknown

    def _settle(self, encoding: o6.NodeId, reason: str) -> None:
        """Never look `encoding` up; warn the first time."""
        if encoding not in self.settled:
            self.settled.add(encoding)
            _logger.warning(
                f"Values with encoding {self._describe(encoding)} cannot be decoded: {reason}"
            )

    def _describe(self, encoding: o6.NodeId) -> str:
        try:
            return str(_emptyModel(self.client).ref(encoding))
        except KeyError:
            return str(encoding)

    def _lookUp(self, encodings: list[o6.NodeId]) -> set[asyncio.Task[None]]:
        """Start loading the DataTypes of new encodings.

        Returns:
            The lookups `encodings` wait for, also ones already running.
        """
        new = []
        unpackaged: set[str] | None = None
        for encoding in dict.fromkeys(encodings):
            if encoding in self.settled or encoding in self.pending:
                continue
            if unpackaged is None:
                unpackaged = _unpackagedNamespaces(self.client)
            try:
                uri = _emptyModel(self.client).ref(encoding).namespaceUri
            except KeyError:
                uri = None
            if uri in unpackaged:
                new.append(encoding)
            else:
                # The namespace's own package defines its types; never extend it.
                self.settled.add(encoding)
        if new:
            task = self.client._loop.create_task(self._load(new))
            self.pending.update((encoding, task) for encoding in new)
        return {self.pending[e] for e in encodings if e in self.pending}

    async def _load(self, encodings: list[o6.NodeId]) -> None:
        try:
            await _DataTypeLookup(self.client).load(encodings)
        except asyncio.CancelledError:
            for encoding in encodings:
                self.pending.pop(encoding, None)
            raise
        except Exception as error:
            if not self.client.connected:
                # The connection was lost; look the encodings up again later.
                for encoding in encodings:
                    self.pending.pop(encoding, None)
                return
            for encoding in encodings:
                self._settle(encoding, f"loading its DataType failed: {error}")
        self.settled.update(encodings)
        for encoding in encodings:
            self.pending.pop(encoding, None)
