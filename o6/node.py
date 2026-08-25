# Copyright 2026 (c) o6 Automation GmbH
"""Node-style API for browsing the OPC UA address space."""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any, Optional, overload

import o6
from o6 import _o6
from o6 import MaybeAwaitable, HasNodeId, NodeIdLike
from o6._declarations import NODE_ID_DESCRIPTOR as _NODE_ID_DESCRIPTOR
from o6._node_backend import _without_traceback

if TYPE_CHECKING:
    from o6.client import Client
    from o6.ns import ns0
    from o6.ns.ns0.datatypes import NodeClass as _NodeClassType
    from o6.server import NodePermissions, Server
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
    raise Exception("Unknown NodeClass")


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

    Instances (Objects, Variables, Methods, Views) follow the lowerCamelCase
    convention used for model members, so a `ServerStatus` Variable is reached as
    `serverStatus` -- the exact inverse of the member-to-BrowseName mapping in
    dev_docs/naming_conventions.md. Type nodes (ObjectType, VariableType,
    ReferenceType and DataType, which covers enumerations) keep the PascalCase
    spelling that types and classes use.
    """
    if isinstance(child, list):
        return _child_python_name(child[0])
    if isinstance(child, Node):
        python_name = child.__dict__.get("_python_name")
        if python_name:
            return python_name
        name = child._browse_name.name
    else:
        name = child.browseName.name
    if _is_type_node(child):
        return name
    return name[:1].lower() + name[1:]


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
    raise Exception("Not a Node")


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

    A node handle is a live view of one node in an address space, obtained from a
    client, a server, or by browsing from another handle. It is not a snapshot:
    every access goes to the server.

    Three syntaxes cover the whole API. Attribute access browses one level
    (`server.objectsNode.deviceSet`), the call operator reads or writes an
    attribute (`node()`, `node(23.5)`, `node(attr="browseName")`), and the index
    operator resolves a browse path when a name is ambiguous or relative.

    Public helpers on this class carry a leading underscore, because ordinary
    names would collide with OPC UA child lookup. Subclasses may still keep
    application state under ordinary Python names.

    See the [Node API](../manual/node-api.md).
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

    # Call Syntax
    def __call__(
        self, value: Any = _UNSET, attr: Optional[o6.AttributeId | str] = None
    ) -> MaybeAwaitable[Any]:
        """Read or write one attribute of this node.

        Called without a value it reads, and with a value it writes. The
        attribute defaults to `Value`.

        Args:
            value: The value to write. Omit it to read instead.
            attr: The attribute to address, as an
                [`o6.AttributeId`][o6.common.AttributeId] or a case-insensitive
                attribute name such as `"browseName"`.

        Returns:
            The attribute value when reading, `None` when writing; awaitable when
            the owning client or server runs on an external event loop.

        Raises:
            Exception: The write returned a bad StatusCode.
            StatusCodeError: The service call itself failed.
        """
        _check_attached(self)

        async def call():
            if isinstance(attr, str):
                attribute_id = _str2attributeid(attr)
            else:
                attribute_id = attr

            if attribute_id is None:
                attribute_id = o6.AttributeId.VALUE

            if self._is_native_attached():
                if value is not _UNSET:
                    res = await self._write_native_attribute(int(attribute_id), value)
                    if hasattr(res, "code") and res.code != 0:
                        raise Exception(f"Write failed with status {res}")
                    return
                return await self._read_native_attribute(int(attribute_id))

            if value is not _UNSET:
                res = await self._backend.node_write(self._nodeid, value=value, attr=attribute_id)
                if hasattr(res, "code") and res.code != 0:
                    raise Exception(f"Write failed with status {res}")
                return
            if attribute_id == o6.AttributeId.NODE_ID:
                return self._nodeid
            if attribute_id == o6.AttributeId.NODE_CLASS:
                return _type2nodeclass(type(self))
            if attribute_id == o6.AttributeId.BROWSE_NAME:
                return self._browse_name
            return await self._backend.node_read(self._nodeid, attr=attribute_id)

        try:
            return self._backend.dispatch(call())
        except Exception as exc:
            raise _without_traceback(exc) from None

    @staticmethod
    def _group_children(children: list[Any]) -> dict[str, Any]:
        grouped: dict[str, Any] = {}
        for child in children:
            key = (
                child.__dict__.get("_python_name") or child._browse_name.name
                if isinstance(child, Node)
                else child.browseName.name
            )
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

    async def _resolve_child(self, name: str, node_type: type[Node] | None = None) -> Node:
        children = await self._children_by_name()

        def flatten(values: Any) -> list[Any]:
            return values if isinstance(values, list) else [values]

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

        # Prefer an exact BrowseName match,
        # only when there is no exact match fall back to a case-insensitive lookup
        key = name
        child = children.get(name, None)
        if child is None:
            name_lower = name.lower()
            matches = [(k, v) for k, v in children.items() if k.lower() == name_lower]
            if len(matches) == 1:
                key, child = matches[0]
            elif len(matches) > 1:
                raise ambiguous([candidate for _, value in matches for candidate in flatten(value)])
        if child is None:
            raise AttributeError(f"Child-node {name} not found")
        if isinstance(child, list):
            raise ambiguous(child)
        if isinstance(child, Node):
            return _bind_method(self, child)

        nodeClassType = node_type or _nodeclass2type(child.nodeClass)
        if self._is_native_attached():
            node_child = await self._backend.node_get(str(child.nodeId), nodeClassType)
        else:
            node_child = nodeClassType(self._backend, child.nodeId, child.browseName)
            children[key] = node_child
        return _bind_method(self, node_child)

    def __dir__(self) -> list[str]:
        browse_children_sync = getattr(self._backend, "browse_children_sync", None)
        if callable(browse_children_sync):
            children = self._group_children(browse_children_sync(self))
            return sorted(
                {
                    name
                    for child in children.values()
                    if (name := _child_python_name(child)).isidentifier()
                }
            )

        async def _dir():
            children = await self._children_by_name()

            return sorted(
                {
                    name
                    for child in children.values()
                    if (name := _child_python_name(child)).isidentifier()
                }
            )

        # ``__dir__`` must return synchronously, so resolve the children coroutine to completion here.
        # if server started post to a running loop and block, else drive the loop inline.
        loop = self._backend.loop
        if loop.is_running():
            fut = asyncio.run_coroutine_threadsafe(_dir(), loop)
            return fut.result()
        return loop.run_until_complete(_dir())

    def __getattr__(self, name: str) -> Node | AwaitableNode:
        if name.startswith("_"):
            raise AttributeError(name)
        try:
            r = self._backend.dispatch(self._resolve_child(name))
        except Exception as exc:
            raise _without_traceback(exc) from None
        if isinstance(r, Node):
            return r
        return AwaitableNode(self._backend, r)

    # Index Syntax
    def __getitem__(self, key: str | "ns0.datatypes.RelativePath") -> MaybeAwaitable[list[Any]]:
        """Resolve a browse path relative to this node.

        Use this where attribute access cannot reach: a BrowseName that is not a
        Python identifier, an ambiguous name, or a multi-step relative path.

        Args:
            key: A relative-path string such as `"1:DeviceSet/1:Motor"`, or a
                `ns0.datatypes.RelativePath`.

        Returns:
            Every node the path resolves to, as a list; awaitable when the owning
            client or server runs on an external event loop.

        Raises:
            KeyError: The path matches no node.
        """
        # ns0-typed browse-path plumbing lives behind the backend seam so this
        # module stays free of any ns0 import (see o6._node_paths).
        _check_attached(self)
        try:
            return self._backend.dispatch(self._backend.node_resolve_path(self, key))
        except Exception as exc:
            raise _without_traceback(exc) from None


class AwaitableNode:
    """A node lookup that has not been resolved yet.

    Returned by attribute access on an asynchronous client, so that a chain such
    as `await client.objectsNode.server.serverStatus` performs one browse per
    step without awaiting in between. Awaiting it yields the resolved
    [`Node`][o6.node.Node]; attribute access and calls extend the chain instead.
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

        Takes the same arguments as [`Node.__call__`][o6.node.Node], and defers them
        until the chain is awaited.
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

    The keyword form of the constructor shown below creates a node in a server's
    address space. It is available on the generated ObjectTypes in `o6.ns` and on
    `@o6.objecttype` classes, which is where instances are normally created;
    calling this base class with those keywords raises `TypeError`, because a bare
    Object has no type definition to instantiate.
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


class VariableNode(Node):
    """Node representing an OPC UA Variable.

    The call operator defaults to the `Value` attribute, so `node()` reads the
    value and `node(23.5)` writes it.

    The keyword form of the constructor shown below creates a node in a server's
    address space. It is available on the generated VariableTypes in `o6.ns` and
    on `@o6.variabletype` classes, which is where instances are normally created;
    calling this base class with those keywords raises `TypeError`, because a bare
    Variable has no type definition to instantiate.
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
    [`VariableNode`][o6.node.VariableNode], because a VariableType can carry a default
    value for its instances.
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

    A server Method normally retains its construction Object. Methods without
    one, and Methods reached through an additional reference, use a lightweight
    bound value for that browse edge.
    """

    def __call__(
        self,
        *args: Any,
        object: Optional[NodeIdLike] = None,
        attr: Optional[o6.AttributeId | str] = None,
        value: Any = _UNSET,
    ) -> MaybeAwaitable[Any]:
        """Call this Method, or read and write one of its attributes.

        Method-call syntax and attribute syntax do not mix: passing `attr` or
        `value` together with positional arguments raises.

        Args:
            args: The Method's InputArguments, in declaration order. Node handles
                are cast to NodeIds automatically.
            object: The Object to call the Method on. Needed only for a Method
                reached directly by NodeId, since dot lookup carries its Object.
            attr: Read or write this attribute instead of calling the Method.
            value: The value to write, for attribute syntax.

        Returns:
            The Method's OutputArguments, or the attribute value.

        Raises:
            Exception: Both syntaxes were mixed, or the Object for the call is
                unknown.
            StatusCodeError: The Call service failed, or the Method returned a bad
                StatusCode.
        """
        _check_attached(self)
        if attr is not None or value is not _UNSET:
            if len(args) != 0:
                raise Exception("Method-call syntax and attribute-access syntax do not mix")
            if attr is None:
                attr = o6.AttributeId.VALUE
            try:
                return super().__call__(attr=attr, value=value)
            except Exception as exc:
                raise _without_traceback(exc) from None
        if object is None:
            object = self._construction_owner
            if object is None:
                raise Exception(
                    "the Object for this Method call is unknown; pass object=<node or NodeId>"
                )
        try:
            return self._backend.dispatch(
                self._backend.node_call(
                    object, self._nodeid, [_normalize_nodeids(arg) for arg in args]
                )
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

    Browsing it walks the type's own instance declarations, so it shows what an
    instance of the type will contain rather than any one instance's children.
    """


class ReferenceTypeNode(Node):
    """Node representing an OPC UA ReferenceType."""


class DataTypeNode(Node):
    """Node representing an OPC UA DataType, including enumerations."""


class ViewNode(Node):
    """Node representing an OPC UA View.

    Created by [`o6.view`][o6.view], which also documents what a View contains.
    """


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
