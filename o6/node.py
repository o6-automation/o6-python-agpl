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

"""Node-style API for browsing the OPC UA address space."""

from __future__ import annotations

import asyncio
from collections.abc import Iterator, Mapping
from dataclasses import replace
from functools import partial
from typing import TYPE_CHECKING, Any, NoReturn, Optional, cast, overload

import o6
from o6 import _o6
from o6 import MaybeAwaitable, HasNodeId, NodeIdLike
from o6._browse_names import browse_identifier as _browse_identifier
from o6._declarations import NODE_ID_DESCRIPTOR as _NODE_ID_DESCRIPTOR
from o6._node_backend import _ClientBackend, _without_traceback
from o6._write import _write_payload

if TYPE_CHECKING:
    from o6.client import Client
    from o6.ns import ns0
    from o6.ns.ns0.datatypes import NodeClass as _NodeClassType
    from o6.server import Event, NodePermissions, Server
else:
    _NodeClassType = Any

if TYPE_CHECKING:
    from o6.ns.ns0.datatypes import NodeClass as _NodeClass
else:
    from o6._o6 import types as _bootstrap

    # Keep the runtime bootstrap independent of ns0 to avoid a circular import.
    _NodeClass = _bootstrap.NodeClass
    del _bootstrap

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_UNSET = object()


def _str2attributeid(s: str) -> o6.AttributeId:
    """Resolve a case-insensitive OPC UA attribute name."""
    from o6._node_backend import _attribute_id

    return _attribute_id(s)


def _nodeclass2type(nc: _NodeClassType) -> type:
    if nc == _NodeClass.OBJECT:
        return ObjectNode
    elif nc == _NodeClass.VARIABLE:
        return VariableNode
    elif nc == _NodeClass.METHOD:
        return MethodNode
    elif nc == _NodeClass.OBJECT_TYPE:
        return ObjectTypeNode
    elif nc == _NodeClass.VARIABLE_TYPE:
        return VariableTypeNode
    elif nc == _NodeClass.REFERENCE_TYPE:
        return ReferenceTypeNode
    elif nc == _NodeClass.DATA_TYPE:
        return DataTypeNode
    elif nc == _NodeClass.VIEW:
        return ViewNode
    raise ValueError("Unknown NodeClass")


def _is_type_node(child: Any) -> bool:
    """True for a browsed child that models an OPC UA type rather than an instance."""
    if isinstance(child, Node):
        # Live node handles can be generated subclasses, so match by inheritance.
        return isinstance(
            child, (ObjectTypeNode, VariableTypeNode, ReferenceTypeNode, DataTypeNode)
        )
    return child.nodeClass in (
        _NodeClass.OBJECT_TYPE,
        _NodeClass.VARIABLE_TYPE,
        _NodeClass.REFERENCE_TYPE,
        _NodeClass.DATA_TYPE,
    )


def _child_python_name(child: Any) -> str:
    """Python-facing name of a browsed child node.

    Instances use the compiler's lowerCamelCase member spelling; type nodes
    keep its class spelling. Prefix private spellings so dot lookup can reach
    them without exposing the Node implementation's private attributes.
    """
    if isinstance(child, Node):
        python_name = child.__dict__.get("_python_name")
        if python_name:
            return python_name
        name = child._browse_name.name
    else:
        name = child.browseName.name
    return _browse_identifier(name, is_type=_is_type_node(child))


def _child_items(children: dict[str, Any]) -> Iterator[tuple[str, Any]]:
    for key, value in children.items():
        for child in (value if isinstance(value, list) else [value]):
            yield key, child


def _matching_children(children: dict[str, Any], name: str) -> list[tuple[str, Any]]:
    """Prefer an exact original name, then match names and aliases together."""
    if name in children:
        value = children[name]
        return [(name, child) for child in (value if isinstance(value, list) else [value])]
    name_lower = name.lower()
    return [
        (key, child)
        for key, child in _child_items(children)
        if key.lower() == name_lower or _child_python_name(child).lower() == name_lower
    ]


def _type2nodeclass(T: type) -> _NodeClassType:
    if T == ObjectNode:
        return _NodeClass.OBJECT
    elif T == VariableNode:
        return _NodeClass.VARIABLE
    elif T == MethodNode:
        return _NodeClass.METHOD
    elif T == ObjectTypeNode:
        return _NodeClass.OBJECT_TYPE
    elif T == VariableTypeNode:
        return _NodeClass.VARIABLE_TYPE
    elif T == ReferenceTypeNode:
        return _NodeClass.REFERENCE_TYPE
    elif T == DataTypeNode:
        return _NodeClass.DATA_TYPE
    elif T == ViewNode:
        return _NodeClass.VIEW
    raise TypeError("Not a Node")


# ---------------------------------------------------------------------------
# Node classes
# ---------------------------------------------------------------------------


if TYPE_CHECKING:

    class _NativeNodeBase:
        _construction_owner: Any

        def _check_attached(self) -> None: ...
        def _is_native_attached(self) -> bool: ...
        def _pubsub_publish(self) -> None: ...
        def _pubsub_offset_table(
            self,
        ) -> tuple[bytes, tuple[tuple[int, int, o6.NodeId], ...]]: ...
        def _read_native_attribute(self, attr: int) -> Any: ...
        def _set_pubsub_state_machine(self, callback: Any) -> None: ...
        def _write_native_attribute(self, attr: int, value: Any) -> Any: ...

else:
    _NativeNodeBase = getattr(_o6, "_NodeBase", object)


def _check_attached(node: "Node") -> None:
    checker = getattr(_NativeNodeBase, "_check_attached", None)
    if checker is not None:
        checker(node)


def _normalize_nodeids(value: Any) -> Any:
    """Recursively cast Node handles in method arguments to NodeIds."""
    if isinstance(value, Node):
        return o6.NodeId(value)
    if isinstance(value, list):
        normalized = [_normalize_nodeids(item) for item in value]
        if type(value) is list:
            return normalized
        # Typed list subclasses carry native array element metadata. Preserve
        # the container (especially for empty arrays, where type inference is
        # impossible) and only replace members that required NodeId casting.
        if any(after is not before for before, after in zip(value, normalized)):
            value[:] = normalized
        return value
    if isinstance(value, tuple):
        return tuple(_normalize_nodeids(item) for item in value)
    return value


class Node(_NativeNodeBase, HasNodeId):
    """Base class providing dot, index, and call syntax for OPC UA nodes.

    A node handle is a live view of one node, obtained from a client, a server,
    or by browsing from another handle. Attribute reads and writes go to the
    server. Client child navigation uses a refreshable cache.

    Attribute access browses one level (`client.objects.server`). The call
    operator reads or writes an attribute (`node()`, `node(23.5)`,
    `node(attr="browseName")`). The index operator resolves a browse path when a
    name is ambiguous or relative.

    Public helpers on this class start with an underscore so they do not
    collide with child lookup. Subclasses can keep application state under
    ordinary Python names.

    See the [Node API](manual/node-api/index.md).
    """

    # Public helpers defined by the base Node API would collide with OPC UA
    # child dot syntax, so identity, permissions, caches, and similar helpers
    # must keep an underscore prefix. Subclasses may still carry application
    # state under ordinary Python names; __dir__ intentionally lists children.
    _nodeid = _NODE_ID_DESCRIPTOR
    _child_cache: Optional[dict[str, Any]]

    def __init__(
        self,
        backend: Any,
        nodeId: NodeIdLike,
        browseName: o6.QualifiedName,
    ) -> None:
        """Wrap an existing node. Handles come from a client, server, or browsing.

        Args:
            backend: The client or server backend that carries out operations.
            nodeId: NodeId of the node.
            browseName: BrowseName of the node.
        """
        assert isinstance(browseName, o6.QualifiedName)
        self._backend = backend
        # Attached server PyNodes expose these directly from their embedded
        # UA_Node. Client handles and declarations retain the Python
        # identity fields.
        if not self._is_native_attached():
            self._nodeid = o6.NodeId(nodeId)
            self._browse_name = browseName
            # Client and detached nodes cache browse results. Attached server
            # nodes browse directly from their embedded native UA_Node.
            self._child_cache = None
            if isinstance(backend, _ClientBackend):
                backend.add_node(self)

    def __str__(self) -> str:
        return str(self._nodeid)

    def __repr__(self) -> str:
        return f"{self._browse_name}: {type(self).__name__}({self._nodeid})"

    @property
    def _permissions(self) -> NodePermissions:
        """Role permissions assigned explicitly to this node."""
        _check_attached(self)
        server = getattr(self._backend, "_server", None)
        if server is None:
            raise TypeError("role permissions are available only for server nodes")
        from o6.server import NodePermissions

        return NodePermissions(server, self._nodeid)

    @_permissions.setter
    def _permissions(self, value) -> None:
        self._permissions.set(value)

    def __lshift__(self, other: object) -> NoReturn:
        """Reject event emission on any NodeClass but Object and View.

        Overridden by [`ObjectNode`][o6.node.ObjectNode] and
        [`ViewNode`][o6.node.ViewNode] -- the only NodeClasses OPC UA defines
        an `EventNotifier` attribute for -- with the real implementation.
        """
        raise TypeError(
            f"{type(self).__name__} nodes cannot emit events "
            "(EventNotifier is only defined for Object and View nodes)"
        )

    def _do_emit(self, event: "Event | Mapping[str, Any] | ObjectNode") -> MaybeAwaitable[bytes]:
        """Fire `event` sourced at this node. Reached only through `<<`."""
        _check_attached(self)
        server = getattr(self._backend, "_server", None)
        if server is None:
            raise TypeError(
                "local event creation requires a server-side node "
                "(this node handle came from a Client)"
            )
        from o6.server import Event

        if isinstance(event, Node):
            if not isinstance(event, ObjectNode):
                raise TypeError("event instance must be an Object node")
            event = Event(server, eventInstance=event)
        elif not isinstance(event, Event):
            if not isinstance(event, Mapping):
                raise TypeError(
                    "expected an Event draft, an event argument mapping, or an event Object instance"
                )
            event = Event(server, **cast(Mapping[str, Any], event))
        # `replace` copies, so the caller's draft keeps its own `source` and
        # can be fired against a different node next. Going through
        # `trigger()` keeps `Event` the single place that knows which fields
        # an event carries.
        return replace(event, _server=server, source=self._nodeid).trigger()

    # Call Syntax
    def __call__(
        self, value: Any = _UNSET, attr: Optional[o6.AttributeId | str] = None
    ) -> MaybeAwaitable[Any]:
        """Read or write one attribute of this node.

        Reads without a value and writes with one. The attribute defaults to
        `Value`. Reads return the value for Good statuses and raise for
        Uncertain or Bad. For status and timestamps, use the client's or
        server's `read(..., valueOnly=False)`.

        Args:
            value: The value to write. Omit it to read instead.
            attr: The attribute to address, as an
                [`o6.AttributeId`][o6.common.AttributeId] or a case-insensitive
                attribute name such as `"browseName"`.

        Returns:
            The attribute value when reading, `None` when writing. Async tasks
            always receive an awaitable, including for immediate local results.

        Raises:
            StatusCodeError: The read or write operation failed.
        """
        _check_attached(self)

        attribute_id = _str2attributeid(attr) if isinstance(attr, str) else attr
        if attribute_id is None:
            attribute_id = o6.AttributeId.VALUE

        if self._is_native_attached():

            def native_call():
                if value is not _UNSET:
                    return self._backend._server._write_data_value(
                        self._nodeid, _write_payload(value), None, int(attribute_id)
                    )
                return self._read_native_attribute(int(attribute_id))

            try:
                return self._backend.dispatch_native(native_call)
            except Exception as exc:
                raise _without_traceback(exc) from None

        async def call():
            if value is not _UNSET:
                await self._backend.node_write(self._nodeid, value=value, attr=attribute_id)
                return
            if attribute_id == o6.AttributeId.NODE_ID:
                return self._nodeid
            if attribute_id == o6.AttributeId.NODE_CLASS:
                return _type2nodeclass(type(self))
            if attribute_id == o6.AttributeId.BROWSE_NAME:
                return self._browse_name
            return await self._backend.node_read(self._nodeid, attr=attribute_id)

        try:
            return self._backend.dispatch(call)
        except Exception as exc:
            raise _without_traceback(exc) from None

    @staticmethod
    def _group_children(children: list[Any]) -> dict[str, Any]:
        grouped: dict[str, Any] = {}
        for child in children:
            key = child._browse_name.name if isinstance(child, Node) else child.browseName.name
            old = grouped.get(key)
            if old is None:
                grouped[key] = child
            elif isinstance(old, list):
                old.append(child)
            else:
                grouped[key] = [old, child]
        return grouped

    # Dot Syntax
    async def _children_by_name(self) -> dict[str, Any]:
        _check_attached(self)
        if self._is_native_attached():
            return self._group_children(await self._backend.browse_children(self))
        if self._child_cache is None:
            target = (
                self
                if callable(getattr(self._backend, "browse_children_sync", None))
                else self._nodeid
            )
            children = await self._backend.browse_children(target)
            self._child_cache = self._group_children(children)
        return self._child_cache

    def _select_child(self, children: dict[str, Any], name: str) -> tuple[str, Any]:
        def ambiguous(matches: list[Any]) -> AttributeError:
            details = []
            for match in matches:
                if isinstance(match, Node):
                    browse_name = match._browse_name
                    node_id = match._nodeid
                else:
                    browse_name = match.browseName
                    node_id = o6.NodeId(match.nodeId)
                details.append(f"  - QualifiedName={browse_name}, NodeId={node_id}")
            return AttributeError(
                f"Child-node lookup for {name!r} is ambiguous; "
                f"{len(matches)} matching references:\n" + "\n".join(details)
            )

        matches = _matching_children(children, name)
        if not matches:
            raise AttributeError(f"Child-node {name} not found")
        if len(matches) > 1:
            raise ambiguous([child for _, child in matches])
        return matches[0]

    async def _resolve_child(self, name: str, node_type: type[Node] | None = None) -> Node:
        cached = self.__dict__.get("_child_cache") is not None
        children = await self._children_by_name()
        if (
            cached
            and isinstance(self._backend, _ClientBackend)
            and not _matching_children(children, name)
        ):
            self._backend.invalidate_children(self._nodeid)
            children = await self._children_by_name()
        key, child = self._select_child(children, name)
        if isinstance(child, Node):
            return _bind_method(self, child)

        nodeClassType = node_type or _nodeclass2type(child.nodeClass)
        if self._is_native_attached():
            node_child = await self._backend.node_get(str(child.nodeId), nodeClassType)
        else:
            node_child = nodeClassType(self._backend, child.nodeId, child.browseName)
            group = children[key]
            if isinstance(group, list):
                children[key] = [node_child if entry is child else entry for entry in group]
            else:
                children[key] = node_child
        return _bind_method(self, node_child)

    def _resolve_child_native(self, name: str) -> Node:
        children = self._group_children(self._backend.browse_children_native(self))
        _, child = self._select_child(children, name)
        node_child = self._backend.node_get_native(
            str(child.nodeId), _nodeclass2type(child.nodeClass)
        )
        return _bind_method(self, node_child)

    def __dir__(self) -> list[str]:
        """List children without blocking the owning loop on remote discovery.

        Expose valid Python aliases for BrowseNames, including punctuation,
        leading digits, and keywords. Original names remain usable in paths.
        On that loop, remote nodes expose cached names and Python attributes.
        Use the client's asynchronous browse API for fresh remote discovery.
        """
        try:
            running = asyncio.get_running_loop()
        except RuntimeError:
            running = None
        if running is not None and running is getattr(self._backend, "loop", None):
            if self._is_native_attached():
                children = self._group_children(self._backend.browse_children_native(self))
            else:
                children = self.__dict__.get("_child_cache") or {}
            return sorted(
                set(object.__dir__(self))
                | {_child_python_name(child) for _, child in _child_items(children)}
            )
        browse_children_sync = getattr(self._backend, "browse_children_sync", None)
        if callable(browse_children_sync):
            children = self._group_children(browse_children_sync(self))
            return sorted({_child_python_name(child) for _, child in _child_items(children)})

        async def _dir():
            children = await self._children_by_name()

            return sorted({_child_python_name(child) for _, child in _child_items(children)})

        # ``__dir__`` must return synchronously, so block until the children coroutine completes.
        return self._backend.dispatch_wait(_dir)

    def __getattr__(self, name: str) -> Node | AwaitableNode:
        if name.startswith("_"):
            raise AttributeError(name)
        try:
            if self._is_native_attached():
                r = self._backend.dispatch_native(lambda: self._resolve_child_native(name))
            else:
                r = self._backend.dispatch(partial(self._resolve_child, name))
        except Exception as exc:
            raise _without_traceback(exc) from None
        if isinstance(r, Node):
            return r
        return AwaitableNode(self._backend, r)

    # Index Syntax
    def __getitem__(self, key: str | "ns0.datatypes.RelativePath") -> MaybeAwaitable[list[Any]]:
        """Resolve a browse path relative to this node.

        Use it for a BrowseName that is not a Python identifier, an ambiguous
        name, or a multi-step relative path.

        Args:
            key: A relative-path string such as `"1:DeviceSet/1:Motor"`, or a
                `ns0.datatypes.RelativePath`.

        Returns:
            Every node the path resolves to, as a list; awaitable in async tasks.

        Raises:
            KeyError: The path matches no node.
        """
        _check_attached(self)
        try:
            return self._backend.dispatch(partial(self._backend.node_resolve_path, self, key))
        except Exception as exc:
            raise _without_traceback(exc) from None


class AwaitableNode:
    """A node lookup that has not been resolved yet.

    Returned by child lookup in async code, so that
    `await client.objects.server.serverStatus` browses once per step with a
    single `await`. Awaiting it returns the resolved [`Node`][o6.node.Node].
    Attribute access and calls extend the chain.
    """

    def __init__(self, backend: Any, awaitable: Any) -> None:
        """Wrap a pending lookup. Attribute access on a node creates these.

        Args:
            backend: The client or server backend that carries out operations.
            awaitable: The pending node lookup.
        """
        self._backend = backend
        self._awaitable = awaitable

    def __await__(self):
        """Resolve the chain and return the [`Node`][o6.node.Node] it reached."""
        return self._awaitable.__await__()

    def __getattr__(self, name: str) -> AwaitableNode:
        if name.startswith("_"):
            raise AttributeError(name)
        parent = self._awaitable
        backend = self._backend

        async def chain() -> Node:
            node = await parent
            return await node._resolve_child(name)

        return AwaitableNode(backend, chain())

    def __call__(self, *args: Any, **kwargs: Any) -> AwaitableNode:
        """Read or write the resolved node, returning another awaitable step.

        Takes the arguments of [`Node.__call__`][o6.node.Node] and applies them
        when the chain is awaited.
        """
        parent = self._awaitable
        backend = self._backend

        async def chain() -> Any:
            node = await parent
            result = node(*args, **kwargs)
            if hasattr(result, "__await__"):
                return await result
            return result

        return AwaitableNode(backend, chain())


class ObjectNode(Node):
    """Node representing an OPC UA Object.

    The keyword form of the constructor creates a node in a server's address
    space. Use it on the generated ObjectTypes in `o6.ns` and on
    `@o6.objecttype` classes. On this base class it raises `TypeError`, because
    a bare Object has no type definition.
    """

    @overload
    def __init__(self, backend: Any, nodeId: NodeIdLike, browseName: o6.QualifiedName) -> None: ...

    @overload
    def __init__(
        self,
        *,
        server: Optional[Server] = None,
        nodeId: Optional[NodeIdLike] = None,
        parent: Optional[NodeIdLike | Node] = None,
        browseName: Optional[str | o6.QualifiedName] = None,
        referenceType: Optional[NodeIdLike] = None,
        values: Optional[dict[str, Any]] = None,
        references: Optional[list[Any]] = None,
    ) -> None: ...

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def __lshift__(  # type: ignore[override]
        self, event: "Event | Mapping[str, Any] | ObjectNode"
    ) -> MaybeAwaitable[bytes]:
        """Fire `event` sourced at this Object, without an explicit `Server` reference.

        Accepts an [`Event`][o6.server.Event] draft, a mapping of event arguments,
        or an event Object instance on this server. An instance supplies its
        fields and type; mappings and drafts can pass it as `eventInstance`.
        A draft's `source` is not changed, so the draft can be reused for
        another node.

        See [Events](manual/server/events.md#events).
        """
        return self._do_emit(event)


class VariableNode(Node):
    """Node representing an OPC UA Variable.

    The call operator defaults to the `Value` attribute, so `node()` reads the
    value and `node(23.5)` writes it.

    The keyword form of the constructor creates a node in a server's address
    space. Use it on the generated VariableTypes in `o6.ns` and on
    `@o6.variabletype` classes. On this base class it raises `TypeError`,
    because a bare Variable has no type definition.
    """

    @overload
    def __init__(self, backend: Any, nodeId: NodeIdLike, browseName: o6.QualifiedName) -> None: ...

    @overload
    def __init__(
        self,
        *,
        server: Optional[Server] = None,
        nodeId: Optional[NodeIdLike] = None,
        parent: Optional[NodeIdLike | Node] = None,
        browseName: Optional[str | o6.QualifiedName] = None,
        referenceType: Optional[NodeIdLike] = None,
        value: Any = None,
        values: Optional[dict[str, Any]] = None,
        dataType: Any = None,
        valueRank: Optional[int] = None,
        arrayDimensions: Optional[list[int]] = None,
        accessLevel: Optional[int] = None,
        references: Optional[list[Any]] = None,
    ) -> None: ...

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    @property
    def _is_live(self) -> bool:
        """True for a live node bound to a server."""
        return self._backend is not None

    @property
    def _value(self) -> Any:
        return self()

    @_value.setter
    def _value(self, v: Any) -> None:
        self(v)

    def __call__(
        self, value: Any = _UNSET, attr: Optional[o6.AttributeId | str] = None
    ) -> MaybeAwaitable[Any]:
        """Read or write this Variable's value, or another attribute.

        Identical to [`Node.__call__`][o6.node.Node] except that the attribute
        defaults to `Value`.
        """
        if attr is None:
            attr = o6.AttributeId.VALUE
        return super().__call__(attr=attr, value=value)


class VariableTypeNode(Node):
    """Node representing an OPC UA VariableType.

    The call operator defaults to the `Value` attribute, like
    [`VariableNode`][o6.node.VariableNode]. The Value of a VariableType is the
    default value for its instances.
    """

    def __call__(
        self, value: Any = _UNSET, attr: Optional[o6.AttributeId | str] = None
    ) -> MaybeAwaitable[Any]:
        """Read or write this VariableType's default value, or another attribute.

        Identical to [`Node.__call__`][o6.node.Node] except that the attribute
        defaults to `Value`.
        """
        if attr is None:
            attr = o6.AttributeId.VALUE
        return super().__call__(attr=attr, value=value)


class MethodNode(Node):
    """A callable OPC UA Method node.

    A server Method keeps the Object it was created under. A Method without
    one, or reached through an additional reference, is bound to the Object it
    was browsed from.
    """

    def __call__(
        self,
        *args: Any,
        object: Optional[NodeIdLike] = None,
        attr: Optional[o6.AttributeId | str] = None,
        value: Any = _UNSET,
    ) -> MaybeAwaitable[Any]:
        """Call this Method, or read and write one of its attributes.

        Passing `attr` or `value` together with positional arguments raises.

        Args:
            args: The Method's InputArguments, in declaration order. Node handles
                are cast to NodeIds automatically.
            object: The Object to call the Method on. Needed only for a Method
                reached directly by NodeId, since dot lookup carries its Object.
            attr: Read or write this attribute instead of calling the Method.
            value: The value to write, for attribute syntax.

        Returns:
            `(StatusCode, *output_arguments)` after checking the method status,
            or the attribute value.

        Raises:
            ValueError: Both syntaxes were mixed, or the Object for the call is
                unknown.
            StatusCodeError: The Call service failed, or the Method returned a bad
                StatusCode.
        """
        _check_attached(self)
        if attr is not None or value is not _UNSET:
            if len(args) != 0:
                raise ValueError("Method-call syntax and attribute-access syntax do not mix")
            if attr is None:
                attr = o6.AttributeId.VALUE
            try:
                return super().__call__(attr=attr, value=value)
            except Exception as exc:
                raise _without_traceback(exc) from None
        if object is None:
            object = self._construction_owner
            if object is None:
                raise ValueError(
                    "the Object for this Method call is unknown; pass object=<node or NodeId>"
                )
        try:
            arguments = [_normalize_nodeids(arg) for arg in args]
            if self._is_native_attached():
                return self._backend.node_call_native(object, self._nodeid, arguments)
            return self._backend.dispatch(
                partial(self._backend.node_call, object, self._nodeid, arguments)
            )
        except Exception as exc:
            raise _without_traceback(exc) from None


class _BoundMethod(MethodNode):
    """A Method node together with the Object used to reach it."""

    def __init__(self, method: MethodNode, object: Node) -> None:
        # Do not initialize another node handle. The underlying Method remains
        # the sole node representation; this object only represents one browse
        # edge, like Python's own bound-method objects.
        self._method = method
        self._object = object

    @property
    def _nodeid(self) -> o6.NodeId:
        return self._method._nodeid

    @_nodeid.setter
    def _nodeid(self, value: NodeIdLike) -> None:
        self._method._nodeid = o6.NodeId(value)

    @property
    def _permissions(self) -> NodePermissions:
        return self._method._permissions

    @_permissions.setter
    def _permissions(self, value) -> None:
        self._method._permissions = value

    def __call__(
        self,
        *args: Any,
        object: Optional[NodeIdLike] = None,
        attr: Optional[o6.AttributeId | str] = None,
        value: Any = _UNSET,
    ) -> MaybeAwaitable[Any]:
        if object is None and attr is None and value is _UNSET:
            object = self._object
        try:
            return self._method(*args, object=object, attr=attr, value=value)
        except Exception as exc:
            raise _without_traceback(exc) from None

    def __str__(self) -> str:
        return str(self._method)

    def __repr__(self) -> str:
        return repr(self._method)

    def __dir__(self) -> list[str]:
        return dir(self._method)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._method, name)


def _bind_method(parent: Node, child: Node) -> Node:
    if isinstance(parent, (ObjectNode, ObjectTypeNode)) and isinstance(child, MethodNode):
        # A server Method with this construction owner needs no per-edge wrapper.
        # Shared, client and detached Methods still retain the browse edge.
        if child._construction_owner is None and child._is_native_attached():
            try:
                child._construction_owner = parent
            except ValueError:
                pass
        if child._construction_owner is parent:
            return child
        return _BoundMethod(child, parent)
    return child


class ObjectTypeNode(Node):
    """Node representing an OPC UA ObjectType.

    Browsing it lists the type's instance declarations: what an instance of
    the type contains.
    """


class ReferenceTypeNode(Node):
    """Node representing an OPC UA ReferenceType."""


class DataTypeNode(Node):
    """Node representing an OPC UA DataType, including enumerations."""


class ViewNode(Node):
    """Node representing an OPC UA View.

    Created by [`o6.view`][o6.view], which also documents what a View contains.
    """

    def __lshift__(  # type: ignore[override]
        self, event: "Event | Mapping[str, Any] | ObjectNode"
    ) -> MaybeAwaitable[bytes]:
        """Fire `event` sourced at this View, without an explicit `Server` reference.

        Identical to [`ObjectNode.__lshift__`][o6.node.ObjectNode].
        """
        return self._do_emit(event)


__all__ = [
    "AwaitableNode",
    "DataTypeNode",
    "MethodNode",
    "Node",
    "ObjectNode",
    "ObjectTypeNode",
    "ReferenceTypeNode",
    "VariableNode",
    "VariableTypeNode",
    "ViewNode",
]


def __dir__() -> list[str]:
    return sorted(__all__)
