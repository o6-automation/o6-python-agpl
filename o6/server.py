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

import asyncio
import concurrent.futures
import copy
from contextlib import suppress
from dataclasses import dataclass, field
import enum
from functools import partial
import inspect
import itertools
import logging
import re
import threading
import time
import warnings
import weakref
from pathlib import Path
from types import ModuleType, TracebackType
from typing import (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Callable,
    Iterable,
    Iterator,
    Mapping,
    MutableMapping,
    Protocol,
    TypeAlias,
    TypeVar,
    cast,
    overload,
)

import numpy as np

import o6
import o6.subscription
from o6._browse import (
    _BrowseCollection,
    _browse_description,
    _simplified_browse_path,
    _translate_paths,
)
from o6._creation import is_value_envelope, variable_attributes
from o6._delete import _delete_inputs
from o6._dispatch import public_result, synchronous, invoke_sync
from o6._read import _read_request, _read_results
from o6._write import _WRITE_UNSET, _write_inputs, _write_payload
from o6 import _server_construction, _server_materialization, _server_types
from o6._node_backend import _ServerBackend, _attribute_id, _server_node, _targets_and_ranges
from o6._notifications import (
    AUDIT_CATEGORY,
    CATEGORY_MASK,
    Notification,
    NotificationHandlers,
    NotificationType,
    dispatch_key,
    lifecycle_point,
    run_handlers,
    schedule_coroutine,
)
from o6.discovery import MdnsConfig, _announced_url
from o6.ns import ns0

_logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    _NativeServer: TypeAlias = Any
    _requireServer: Callable[[], None]

else:
    from . import _o6

    _NativeServer = getattr(_o6, "Server", None)
    _requireServer = getattr(_o6, "_require_server", None)
    del _o6
from o6.node import (
    Node,
    ObjectNode,
    VariableNode,
    MethodNode,
    ObjectTypeNode,
    VariableTypeNode,
    ReferenceTypeNode,
    ViewNode,
    _nodeclass2type,
    _normalize_nodeids,
)

if _NativeServer is None:
    raise ImportError(
        "Server support is not available. " "The o6 package was built without server support."
    )

_HAS_SERVER_ON_NETWORK_CALLBACK = hasattr(_NativeServer, "set_server_on_network_callback")

from o6 import NodeIdLike, LocalizedTextLike, MaybeAwaitable
from o6.util import (
    _LOOP_ALIVE_POLL,
    _ScheduledFinalizer,
    _WorkerLoop,
    _call_native,
    _idle_loop,
    _ConfigView,
    _finalize_native,
    _run_on_loop,
)
from o6.util import _load_cert_or_bytes, _load_cert_list

from o6._declarations import TypeDeclaration, VariableTypeSpec, _CallbackKind
from o6._history import History, HistoryBackend, as_history as _as_history

_NodeT = TypeVar("_NodeT", bound=Node)


def _normalize_event_fields(
    fields: Mapping[o6.QualifiedName | str, Any] | None,
) -> dict[o6.QualifiedName | str, Any]:
    return {key: _normalize_nodeids(value) for key, value in (fields or {}).items()}


# The optional "#Attribute" and "[IndexRange]" suffixes of an event field path.
_EVENT_PATH_SUFFIX = re.compile(r"(#[A-Za-z]+)?(\[[^\]]*\])?$")


def _event_path_names(
    path: str, default: int
) -> tuple[list[tuple[o6.QualifiedName, bool]], str, str | None] | None:
    """Split an event field path into BrowseNames and its suffix.

    Each segment is `name` or `prefix:name`, where the prefix is a
    process-wide namespace index or a registered namespace shortname. A
    segment without a prefix takes the namespace index `default`. The flag
    tells whether a segment named its namespace. The last item is a prefix
    that looks like a shortname but is not registered. Returns `None` for
    paths that are passed on unchanged: with a TypeDefinitionId, escapes or
    empty segments.
    """
    suffix = _EVENT_PATH_SUFFIX.search(path)
    tail = suffix.group(0) if suffix else ""
    body = path[: len(path) - len(tail)]
    if not body.startswith("/") or any(char in body for char in "&%<>"):
        return None
    names: list[tuple[o6.QualifiedName, bool]] = []
    unknown = None
    for segment in body[1:].split("/"):
        if not segment:
            return None
        prefix, separator, name = segment.partition(":")
        if separator and name and prefix.isdigit() and int(prefix) <= 0xFFFF:
            names.append((o6.QualifiedName(int(prefix), name), True))
        elif separator and name and prefix in o6.ns:
            names.append((o6.QualifiedName(getattr(o6.ns, prefix).index, name), True))
        else:
            if separator and name and prefix.isidentifier():
                unknown = prefix
            names.append((o6.QualifiedName(default, segment), False))
    return names, tail, unknown


def _event_path_string(indexes: list[int], names: list[str], suffix: str) -> str:
    """Print a path the way open62541 prints the SimpleAttributeOperand of a filter."""

    def escape(name: str) -> str:
        return "".join(
            f"%{ord(char):02X}" if char in ";%" or ord(char) <= 32 or ord(char) == 127 else char
            for char in name
        )

    return (
        "".join(
            f"/{index}:{escape(name)}" if index else f"/{escape(name)}"
            for index, name in zip(indexes, names)
        )
        + suffix
    )


def _normalize_event_args(
    eventType: NodeIdLike | None,
    source: NodeIdLike,
    fields: Mapping[o6.QualifiedName | str, Any] | None,
    eventInstance: NodeIdLike | None,
) -> tuple[o6.NodeId | None, o6.NodeId, dict[o6.QualifiedName | str, Any], o6.NodeId | None]:
    return (
        o6.NodeId(eventType) if eventType is not None else None,
        o6.NodeId(source),
        _normalize_event_fields(fields),
        o6.NodeId(eventInstance) if eventInstance is not None else None,
    )


def _server_proxy(server: "Server") -> "Server":
    """Return a non-owning server reference with the transparent proxy contract."""
    return cast("Server", weakref.proxy(server))


def _require_event_select_clauses(eventFilter: "ns0.datatypes.EventFilter") -> None:
    if not eventFilter.selectClauses:
        raise ValueError(
            "EventFilter needs at least one select clause; the server rejects an "
            "empty one with BadEventFilterInvalid. Pass selectClauses=..., or build "
            'one with EventFilter.parse("SELECT /EventId, ...")'
        )


@dataclass
class Event(MutableMapping[o6.QualifiedName | str, Any]):
    """Reusable server-side event draft.

    Construct with `o6.Event(server, ...)` and trigger it any number of times.
    Construction does not access the address space or emit an event.
    The draft is a mutable mapping of event fields: it supports `dict(event)`,
    `len(event)`, `del event[key]` and iteration. The attributes below can be
    reassigned between triggers.

    Field keys are BrowseNames of fields of the event type (`"BatchId"`),
    paths of BrowseNames (`"/plant:BatchId"`), or
    [`QualifiedName`][o6.QualifiedName] values. See
    [Event fields](manual/server/events.md#event-fields).

    When `eventType` is `None`, each `trigger()` resolves it from
    `eventInstance`'s type if supplied, otherwise from `source`'s declared
    `GeneratesEvent` target. The draft itself keeps `eventType=None`.

    See [Events](manual/server/events.md#events).
    """

    _server: "Server" = field(repr=False)
    eventType: NodeIdLike | None = None
    source: NodeIdLike = field(default_factory=lambda: ns0.instances.server)
    message: LocalizedTextLike = ""
    severity: int = 1
    fields: dict[o6.QualifiedName | str, Any] = field(default_factory=dict)
    eventInstance: NodeIdLike | None = None

    def __post_init__(self) -> None:
        if not 1 <= self.severity <= 1000:
            raise ValueError("event severity must be between 1 and 1000")

    def __getitem__(self, key: o6.QualifiedName | str) -> Any:
        """Read one explicit event field."""
        return self.fields[key]

    def __setitem__(self, key: o6.QualifiedName | str, value: Any) -> None:
        """Set one explicit event field."""
        self.fields[key] = value

    def __delitem__(self, key: o6.QualifiedName | str) -> None:
        """Remove one explicit event field."""
        del self.fields[key]

    def __iter__(self) -> Iterator[o6.QualifiedName | str]:
        """Iterate the explicit event field keys."""
        return iter(self.fields)

    def __len__(self) -> int:
        """The number of explicit event fields."""
        return len(self.fields)

    def trigger(self) -> MaybeAwaitable[bytes]:
        """Emit this event once and return its EventId.

        Field values are resolved from `fields` first, then from
        `eventInstance`, then from the `BaseEventType` defaults.

        Returns:
            The generated 16-byte EventId.

        Raises:
            ValueError: `severity` is outside the OPC UA range `1..1000`; or
                neither `eventType` nor `eventInstance` is provided and the
                source has no type definition or more than one `GeneratesEvent`
                target on its declared type.
            TypeError: `eventInstance` is not an event Object instance on this server.
            StatusCodeError: Reading the instance or emitting the event failed.
        """
        return self._server.createEvent(
            self.eventType,
            source=self.source,
            message=self.message,
            severity=self.severity,
            fields=self.fields,
            eventInstance=self.eventInstance,
        )


@dataclass(frozen=True, eq=False)
class Role:
    """One OPC UA role in the server's role set.

    Resolved roles compare and hash by NodeId; name-only roles compare and hash
    by name and are distinct from resolved roles. Permission APIs resolve
    name-only roles through the server registry. The well-known roles are
    available from [`o6.roles`][o6.server.roles], and
    server-specific roles are registered through `server.roles.add(...)`.

    The criteria fields decide which sessions the server grants the role to.

    See [Role-based access control](manual/server/security.md#role-based-access-control).
    """

    name: o6.QualifiedName | str
    """BrowseName of the role. A plain string is read as namespace 0."""
    id: o6.NodeId | None = None
    """NodeId of the role node. `None` until the server assigns one."""

    identities: tuple[ns0.datatypes.IdentityMappingRuleType, ...] = ()
    """Identity mapping rules that grant this role to a session."""

    applications: tuple[str, ...] = ()
    """Application URIs the role applies to. Empty means every application."""

    applicationsExclude: bool = False
    """Treat `applications` as a deny list instead of an allow list."""

    endpoints: tuple[ns0.datatypes.EndpointType, ...] = ()
    """Endpoints the role applies to. Empty means every endpoint."""

    endpointsExclude: bool = False
    """Treat `endpoints` as a deny list instead of an allow list."""

    def __post_init__(self) -> None:
        if isinstance(self.name, str):
            object.__setattr__(self, "name", o6.QualifiedName(0, self.name))
        if self.id is not None and not isinstance(self.id, o6.NodeId):
            object.__setattr__(self, "id", o6.NodeId(self.id))

    def __hash__(self) -> int:
        return hash(self._identity())

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Role):
            return NotImplemented
        return self._identity() == other._identity()

    def _identity(self) -> tuple[bool, o6.NodeId | str]:
        return (True, self.id) if self.id is not None else (False, str(self.name))


@dataclass(frozen=True)
class SessionActivation:
    """Result of an authentication that also assigns roles.

    Return this from `AccessControl.activateSession` instead of a bare context
    when the roles of a session follow from who authenticated. The assignment is
    applied right after activation, once the server has evaluated its own role
    identity mappings.

    See [Role-based access control](manual/server/security.md#role-based-access-control).
    """

    context: Any = None
    """The session context, exactly as a plain `activateSession` return value."""

    roles: tuple[Role | o6.NodeId, ...] = ()
    """Roles to assign to the session, as [`Role`][o6.server.Role] or NodeId values."""


class Session:
    """A safe proxy for a server session, resolved by NodeId on every use.

    Handed to the [`AccessControl`][o6.server.AccessControl] hooks and to server-side
    read and write callbacks. Nothing native is retained, so holding on to a
    `Session` past the session's lifetime is safe: the next operation raises
    `StatusCodeError` with `BAD_SESSION_ID_INVALID` instead of using freed
    memory.

    Session attributes are the OPC UA per-session key/value store, readable by
    the client through the SessionDiagnostics object.

    See [The Session proxy](manual/server/security.md#the-session-proxy).
    """

    def __init__(self, server: "Server", sessionId: o6.NodeId, context: Any = None) -> None:
        """Wrap an existing session id. The server creates these, not users.

        Args:
            server: The server that owns the session.
            sessionId: NodeId of the session.
            context: The context returned by `AccessControl.activateSession`.
        """
        self._server = _server_proxy(server)
        self.id = o6.NodeId(sessionId)
        self.context = context
        self._pending_roles: tuple[Role | o6.NodeId, ...] | None = None

    @property
    def roles(self) -> tuple[Role, ...]:
        """The roles currently granted to this session.

        Assigning replaces the whole set, and accepts [`Role`][o6.server.Role] objects or
        role NodeIds.
        """
        if self._pending_roles is not None:
            return tuple(
                role if isinstance(role, Role) else self._server.roles[role]
                for role in self._pending_roles
            )
        names = self._server._call_native(lambda: self._server._get_session_roles(self.id))
        return tuple(self._server.roles[name] for name in names)

    @roles.setter
    def roles(self, roles: Iterable[Role | o6.NodeId]) -> None:
        role_ids = [_role_id(self._server, role) for role in roles]
        self._server._call_native(lambda: self._server._set_session_roles(self.id, role_ids))
        self._pending_roles = None

    def _apply_activation_roles(self) -> None:
        pending = self._pending_roles
        if pending is not None:
            try:
                self.roles = pending
            except o6.StatusCodeError as exc:
                if exc.code != o6.StatusCode.BAD_SESSION_ID_INVALID:
                    raise
                self._pending_roles = None

    def get(self, key: o6.QualifiedName | str) -> Any:
        """Read one session attribute.

        Args:
            key: Attribute name. A plain string is read as namespace 0.

        Raises:
            StatusCodeError: The session is gone, or the attribute is not set.
        """
        name = _qualified_name(key)
        return self._server._call_native(lambda: self._server._get_session_attribute(self.id, name))

    def set(self, key: o6.QualifiedName | str, value: Any) -> None:
        """Set one session attribute.

        Args:
            key: Attribute name. A plain string is read as namespace 0.
            value: Any value of a registered OPC UA type.

        Raises:
            StatusCodeError: The session is gone.
        """
        name = _qualified_name(key)
        self._server._call_native(lambda: self._server._set_session_attribute(self.id, name, value))

    def delete(self, key: o6.QualifiedName | str) -> None:
        """Remove one session attribute.

        Args:
            key: Attribute name. A plain string is read as namespace 0.

        Raises:
            StatusCodeError: The session is gone, or the attribute is not set.
        """
        name = _qualified_name(key)
        self._server._call_native(lambda: self._server._delete_session_attribute(self.id, name))

    def close(self) -> None:
        """Close this session, cancelling its subscriptions.

        Raises:
            StatusCodeError: The session is already gone.
        """
        self._server._call_native(lambda: self._server._close_session(self.id))

    def effectivePermissions(self, nodeId: NodeIdLike) -> ns0.datatypes.PermissionType:
        """The permissions this session has on one node.

        Combines the permissions that the node, or the default permissions of
        its namespace, grant to the session's roles, as the base
        authorization hooks of [`AccessControl`][o6.server.AccessControl]
        evaluate them. Without any rules for the node, every bit is set when
        the permissive fallback applies (`rbacForAnonymous=False`) and no bit
        otherwise.

        Args:
            nodeId: The NodeId or node handle to check.

        Returns:
            The combined `PermissionType` flags granted to this session.
            Access restrictions and custom authorization overrides are not
            included. Calling this method does not change permissions.

        Raises:
            StatusCodeError: The session is gone, or the node does not exist.
        """
        node_id = o6.NodeId(nodeId)
        return ns0.datatypes.PermissionType(
            self._server._call_native(lambda: self._server._effective_permissions(self.id, node_id))
        )


@dataclass(frozen=True)
class MethodCallback(Protocol):
    """The shape of a Method implementation.

    Registered with [`o6.call`][o6.call], `Server.addMethod`, or
    `Server.implement`. The callback may be a coroutine function, in which case
    the server awaits it on its own event loop.

    See [Methods](manual/server/callbacks.md#methods).
    """

    def __call__(
        self,
        node: ObjectNode,
        *inputs: Any,
    ) -> tuple[Any, ...] | Awaitable[tuple[Any, ...]]:
        """Run the Method.

        Args:
            node: The Object the Method was called on.
            inputs: The decoded InputArguments, in declaration order.

        Returns:
            A tuple of the StatusCode followed by the OutputArguments.
        """


_CALLBACK_UNSET = object()

_NATIVE_CALLBACK_KIND: dict[_CallbackKind, int] = {"call": 0, "read": 1, "write": 2}


class VariableReadCallback(Protocol):
    """The shape of a Variable value-read implementation.

    Registered with [`o6.read`][o6.read] or `Server.addVariable`. The callback
    runs on the server's event loop, so it must not block.

    See [Variables](manual/server/callbacks.md#variables).
    """

    def __call__(
        self,
        node: VariableNode,
        *,
        range: tuple[slice, ...] | None,
        session: Session | None,
        includeSourceTimestamp: bool,
    ) -> tuple[Any, ...] | Awaitable[tuple[Any, ...]]:
        """Produce the value of the Variable.

        Args:
            node: The Variable being read.
            range: The requested index range, or `None` for the whole value.
            session: The reading session, or `None` for an internal read.
            includeSourceTimestamp: Whether the caller wants a SourceTimestamp.

        Returns:
            A tuple of the StatusCode and the value.
        """


class VariableWriteCallback(Protocol):
    """The shape of a Variable value-write implementation.

    Registered with [`o6.write`][o6.write] or `Server.addVariable`. The callback
    runs on the server's event loop, so it must not block.

    See [Variables](manual/server/callbacks.md#variables).
    """

    def __call__(
        self,
        node: VariableNode,
        value: o6.DataValue,
        *,
        range: tuple[slice, ...] | None,
        session: Session | None,
    ) -> tuple[o6.StatusCode] | Awaitable[tuple[o6.StatusCode]]:
        """Accept or reject a write to the Variable.

        Args:
            node: The Variable being written.
            value: The requested [`DataValue`][o6.DataValue].
            range: The requested index range, or `None` for the whole value.
            session: The writing session, or `None` for an internal write.

        Returns:
            A one-tuple holding the StatusCode of the write.
        """


def _qualified_name(value: o6.QualifiedName | str) -> o6.QualifiedName:
    return value if isinstance(value, o6.QualifiedName) else o6.QualifiedName(0, value)


def _role_id(server: "Server", role: Role | o6.NodeId) -> o6.NodeId:
    if isinstance(role, o6.NodeId):
        return role
    if role.id is not None:
        return role.id
    return server.roles[role.name].id  # type: ignore[return-value]


class _RoleRegistry:
    def __init__(self, server: "Server") -> None:
        self._server = _server_proxy(server)

    def _native(self, name: str, *args: Any) -> Any:
        """Call a native server method on the loop thread; see `Server._call_native`."""
        server = self._server
        method = getattr(server, name)
        return server._call_native(lambda: method(*args))

    @staticmethod
    def _from_native(data: dict[str, Any]) -> Role:
        return Role(
            id=data["id"],
            name=data["name"],
            identities=tuple(data["identities"]),
            applications=tuple(data["applications"]),
            applicationsExclude=data["applications_exclude"],
            endpoints=tuple(data["endpoints"]),
            endpointsExclude=data["endpoints_exclude"],
        )

    @staticmethod
    def _args(role: Role) -> tuple[Any, ...]:
        return (
            role.id,
            role.name,
            role.identities,
            role.applications,
            role.applicationsExclude,
            role.endpoints,
            role.endpointsExclude,
        )

    def add(self, role: Role) -> Role:
        role_id = self._native("_add_role", *self._args(role))
        return self[role_id]

    def update(self, role: Role) -> Role:
        self._native("_update_role", *self._args(role))
        return self[role.id if role.id is not None else role.name]

    def remove(self, role: Role | o6.QualifiedName | str) -> None:
        name = role.name if isinstance(role, Role) else role
        self._native("_remove_role", _qualified_name(name))

    def __getitem__(self, key: o6.NodeId | o6.QualifiedName | str) -> Role:
        by_id = isinstance(key, o6.NodeId)
        return self._from_native(
            self._native("_get_role", key if by_id else _qualified_name(key), by_id)
        )

    def __iter__(self) -> Iterator[Role]:
        for name in self._native("_get_roles"):
            yield self[name]


class _WellKnownRoles:
    anonymous = Role("Anonymous", o6.NodeId(o6.ns["i=15644"]))
    authenticated_user = Role("AuthenticatedUser", o6.NodeId(o6.ns["i=15656"]))
    observer = Role("Observer", o6.NodeId(o6.ns["i=15668"]))
    operator = Role("Operator", o6.NodeId(o6.ns["i=15680"]))
    engineer = Role("Engineer", o6.NodeId(o6.ns["i=16036"]))
    supervisor = Role("Supervisor", o6.NodeId(o6.ns["i=15692"]))
    configure_admin = Role("ConfigureAdmin", o6.NodeId(o6.ns["i=15716"]))
    security_admin = Role("SecurityAdmin", o6.NodeId(o6.ns["i=15704"]))


roles = _WellKnownRoles()
"""The well-known OPC UA roles, as [`Role`][o6.server.Role] values.

`anonymous`, `authenticated_user`, `observer`, `operator`, `engineer`,
`supervisor`, `configure_admin`, and `security_admin`. Every server creates these
role nodes itself, so they can be used in permission mappings without being
registered first:

```python
from o6.ns.ns0.datatypes import PermissionType

temperature._permissions = {
    o6.roles.observer: PermissionType.BROWSE | PermissionType.READ,
}
```

Server-specific roles are registered through `server.roles.add(...)` instead.

See [Role-based access control](manual/server/security.md#role-based-access-control).
"""


class NodePermissions:
    """The RolePermissions of one node, reached as `node._permissions`.

    The leading underscore is required. Unprefixed attribute access on a node
    handle browses to child nodes, so `node.permissions = ...` creates a plain
    Python attribute and changes nothing.

    Assigning a mapping to `node._permissions` is shorthand for
    [`set`][o6.server.NodePermissions.set]. Every operation takes
    `recursive=True` to apply to the whole subtree. Every operation raises
    `StatusCodeError` if the node is gone.

    See [Role-based access control](manual/server/security.md#role-based-access-control).
    """

    def __init__(self, server: "Server", nodeId: o6.NodeId) -> None:
        """Bind to one node's permissions. Reach this through `node._permissions`.

        Args:
            server: The server that owns the node.
            nodeId: NodeId of the node.
        """
        self._server = _server_proxy(server)
        self._node_id = o6.NodeId(nodeId)

    def _native(self, name: str, *args: Any) -> Any:
        """Call a native server method on the loop thread; see `Server._call_native`."""
        server = self._server
        method = getattr(server, name)
        return server._call_native(lambda: method(*args))

    def get(self) -> dict[Role, ns0.datatypes.PermissionType]:
        """Return the permissions set explicitly on this node.

        Namespace defaults are not included, so an empty result means the node
        falls back to its namespace default.
        """
        return {
            self._server.roles[role_id]: ns0.datatypes.PermissionType(value)
            for role_id, value in self._native("_get_node_role_permissions", self._node_id).items()
        }

    def set(
        self,
        permissions: Mapping[Role | o6.NodeId, ns0.datatypes.PermissionType],
        *,
        recursive: bool = False,
    ) -> None:
        """Replace this node's permissions with the given mapping.

        Args:
            permissions: Role to [`PermissionType`][o6.ns.ns0.datatypes.PermissionType] mask. Roles may be
                given as [`Role`][o6.server.Role] objects or role NodeIds.
            recursive: Apply to this node's whole subtree.
        """
        self._native(
            "_set_node_role_permissions",
            self._node_id,
            {_role_id(self._server, role): int(value) for role, value in permissions.items()},
            recursive,
        )

    def grant(
        self,
        role: Role | o6.NodeId,
        permissions: ns0.datatypes.PermissionType,
        *,
        overwrite: bool = False,
        recursive: bool = False,
    ) -> None:
        """Add permissions for one role, keeping the other roles' entries.

        Args:
            role: The role to grant to.
            permissions: The [`PermissionType`][o6.ns.ns0.datatypes.PermissionType] bits to add.
            overwrite: Replace the role's existing mask instead of adding to it.
            recursive: Apply to this node's whole subtree.
        """
        self._native(
            "_add_role_permissions",
            self._node_id,
            _role_id(self._server, role),
            int(permissions),
            overwrite,
            recursive,
        )

    def revoke(
        self,
        role: Role | o6.NodeId,
        permissions: ns0.datatypes.PermissionType,
        *,
        recursive: bool = False,
    ) -> None:
        """Remove permissions from one role, keeping its remaining bits.

        Args:
            role: The role to revoke from.
            permissions: The [`PermissionType`][o6.ns.ns0.datatypes.PermissionType] bits to remove.
            recursive: Apply to this node's whole subtree.
        """
        self._native(
            "_remove_role_permissions",
            self._node_id,
            _role_id(self._server, role),
            int(permissions),
            recursive,
        )

    def clear(self, *, recursive: bool = False) -> None:
        """Remove every explicit permission, so the namespace default applies.

        Args:
            recursive: Apply to this node's whole subtree.
        """
        self._native("_remove_node_role_permissions", self._node_id, recursive)


# Mirrors the switch in open62541's `ua_server_auditing.c` (`auditEvent`) that
# resolves an audit notification's standardized AuditEventType. AUDIT_CLIENT
# and AUDIT_CLIENT_UPDATEMETHOD are deliberately absent — upstream's own
# switch has no case for them either (its TODO comment), so there is no
# already-existing type identifier to resolve them to yet.
_AUDIT_EVENT_TYPES: dict[int, type] = {
    NotificationType.AUDIT: ns0.objtypes.AuditEventType,
    NotificationType.AUDIT_SECURITY: ns0.objtypes.AuditSecurityEventType,
    NotificationType.AUDIT_SECURITY_CHANNEL: ns0.objtypes.AuditChannelEventType,
    NotificationType.AUDIT_SECURITY_CHANNEL_OPEN: ns0.objtypes.AuditOpenSecureChannelEventType,
    NotificationType.AUDIT_SECURITY_SESSION: ns0.objtypes.AuditSessionEventType,
    NotificationType.AUDIT_SECURITY_SESSION_CREATE: ns0.objtypes.AuditCreateSessionEventType,
    NotificationType.AUDIT_SECURITY_SESSION_ACTIVATE: ns0.objtypes.AuditActivateSessionEventType,
    NotificationType.AUDIT_SECURITY_SESSION_CANCEL: ns0.objtypes.AuditCancelEventType,
    NotificationType.AUDIT_SECURITY_CERTIFICATE: ns0.objtypes.AuditCertificateEventType,
    NotificationType.AUDIT_SECURITY_CERTIFICATE_DATAMISMATCH: (
        ns0.objtypes.AuditCertificateDataMismatchEventType
    ),
    NotificationType.AUDIT_SECURITY_CERTIFICATE_EXPIRED: (
        ns0.objtypes.AuditCertificateExpiredEventType
    ),
    NotificationType.AUDIT_SECURITY_CERTIFICATE_INVALID: (
        ns0.objtypes.AuditCertificateInvalidEventType
    ),
    NotificationType.AUDIT_SECURITY_CERTIFICATE_UNTRUSTED: (
        ns0.objtypes.AuditCertificateUntrustedEventType
    ),
    NotificationType.AUDIT_SECURITY_CERTIFICATE_REVOKED: (
        ns0.objtypes.AuditCertificateRevokedEventType
    ),
    NotificationType.AUDIT_SECURITY_CERTIFICATE_MISMATCH: (
        ns0.objtypes.AuditCertificateMismatchEventType
    ),
    NotificationType.AUDIT_NODE: ns0.objtypes.AuditNodeManagementEventType,
    NotificationType.AUDIT_NODE_ADD: ns0.objtypes.AuditAddNodesEventType,
    NotificationType.AUDIT_NODE_DELETE: ns0.objtypes.AuditDeleteNodesEventType,
    NotificationType.AUDIT_NODE_ADDREFERENCES: ns0.objtypes.AuditAddReferencesEventType,
    NotificationType.AUDIT_NODE_DELETEREFERENCES: ns0.objtypes.AuditDeleteReferencesEventType,
    NotificationType.AUDIT_UPDATE: ns0.objtypes.AuditUpdateEventType,
    NotificationType.AUDIT_UPDATE_WRITE: ns0.objtypes.AuditWriteUpdateEventType,
    NotificationType.AUDIT_UPDATE_HISTORY: ns0.objtypes.AuditHistoryUpdateEventType,
    NotificationType.AUDIT_UPDATE_METHOD: ns0.objtypes.AuditUpdateMethodEventType,
}

# The categories a Server raises, and the property each is reached by. The
# per-category payloads and worked examples live in the manual; each property
# docstring links to its own section there rather than restating it.
_NOTIFICATION_PROPERTIES: dict[str, NotificationType] = {
    "onLifecycleNotification": NotificationType.LIFECYCLE_STARTED,
    "onSecureChannelNotification": NotificationType.SECURECHANNEL_OPENED,
    "onSessionNotification": NotificationType.SESSION_CREATED,
    "onServiceNotification": NotificationType.SERVICE_BEGIN,
    "onSubscriptionNotification": NotificationType.SUBSCRIPTION_CREATED,
    "onMonitoredItemNotification": NotificationType.MONITOREDITEM_CREATED,
    "onDiscoveryRegisterServerNotification": NotificationType.DISCOVERY_REGISTERSERVER,
    "onDiscoveryServerOnNetworkNotification": NotificationType.DISCOVERY_SERVERONNETWORK,
    "onAuditNotification": NotificationType.AUDIT,
}


# The base authorization hooks of AccessControl, ported from the open62541
# default plugin like the native fallbacks in src/server/server_access_control.c.
# 0xFFFFFFFF means that no RolePermissions apply to the node.
_NO_RULES = 0xFFFFFFFF


def _permissions(session: "Session", nodeId: Any) -> int:
    try:
        return int(session.effectivePermissions(nodeId))
    except o6.StatusCodeError as error:
        if error.code != o6.StatusCode.BAD_NODE_ID_UNKNOWN:
            raise  # the hook fails and denies
        return _NO_RULES  # a missing node is not restricted here


def _permits(session: "Session", nodeId: Any, required: int) -> bool:
    permissions = _permissions(session, nodeId)
    return permissions == _NO_RULES or bool(permissions & required)


class AccessControl:
    """Python implementation of the open62541 `UA_AccessControl` plugin.

    Subclass it, override `activateSession` for authentication, and override
    the authorization hooks you need. The base authorization hooks enforce
    role permissions like the default plugin: each hook checks the
    permissions the session's roles have on the node (see
    [`Session.effectivePermissions`][o6.server.Session.effectivePermissions]).
    Nodes without permission rules stay permissive unless the server uses
    `rbacForAnonymous=True`. An override that calls `super()` keeps these
    checks. The base authentication policy accepts anonymous sessions only.

    The server installs a Python callback only for the hooks a subclass
    overrides. open62541 handles the others without calling into Python.

    Every hook runs on the server's event loop with a
    [`Session`][o6.server.Session] proxy, so hooks must not block.

    See [Access control and authentication](manual/server/security.md#access-control-and-authentication).
    """

    _authorization_hooks = (
        "closeSession",
        "getUserRightsMask",
        "getUserAccessLevel",
        "getUserExecutable",
        "getUserExecutableOnObject",
        "allowAddNode",
        "allowAddReference",
        "allowDeleteNode",
        "allowDeleteReference",
        "allowBrowseNode",
        "allowCreateSubscription",
        "allowTransferSubscription",
        "allowHistoryUpdate",
        "allowHistoryDelete",
    )

    def __init__(self, *, anonymous: bool = True, username: bool = False) -> None:
        """Build the plugin and its advertised user token policies.

        Args:
            anonymous: Advertise the anonymous token policy.
            username: Advertise the username/password token policy.
        """
        self._legacy_callbacks: dict[str, bool] = {}
        self.user_token_policies: list[ns0.datatypes.UserTokenPolicy] = []
        if anonymous:
            self.user_token_policies.append(
                ns0.datatypes.UserTokenPolicy(
                    policyId="anonymous", tokenType=ns0.datatypes.UserTokenType.ANONYMOUS
                )
            )
        if username:
            self.user_token_policies.append(
                ns0.datatypes.UserTokenPolicy(
                    policyId="username", tokenType=ns0.datatypes.UserTokenType.USER_NAME
                )
            )

    def clear(self) -> None:
        """Release plugin-owned resources. Called once by the server config."""

    def _overridden_callbacks(self) -> frozenset[str]:
        """Return hooks that need a C-to-Python callback trampoline."""
        plugin_type = type(self)
        return frozenset(
            name
            for name in self._authorization_hooks
            if getattr(plugin_type, name) is not getattr(AccessControl, name)
        )

    def _make_session(self, server: "Server", session_id: o6.NodeId, context: Any) -> Session:
        return Session(server, session_id, context)

    @synchronous
    def _invoke(self, method_name: str, *args: Any) -> Any:
        """Call a hook, adapting pre-Session callback signatures."""
        method = getattr(self, method_name)
        legacy = self._legacy_callbacks.get(method_name)
        if legacy is None:
            parameters = tuple(inspect.signature(method).parameters.values())
            if method_name == "activateSession":
                legacy = len(parameters) > 2 and parameters[2].name in {
                    "session_id",
                    "sessionId",
                }
            else:
                legacy = bool(args) and len(parameters) == len(args) + 1
            self._legacy_callbacks[method_name] = legacy
        if method_name == "activateSession":
            session = args[2]
            if legacy:
                return method(args[0], args[1], session.id, args[3])
            return method(*args)

        if not args or not isinstance(args[0], Session):
            return method(*args)
        session = args[0]
        remaining = args[1:]
        if legacy:
            return method(session.id, session.context, *remaining)
        return method(*args)

    def _complete_activation(self, session: Session, result: Any) -> Any:
        if not isinstance(result, SessionActivation):
            return result
        if result.roles:
            session._pending_roles = result.roles
            session._server._loop.call_soon(session._apply_activation_roles)
        return result.context

    def activateSession(
        self,
        endpoint: ns0.datatypes.EndpointDescription,
        remoteCertificate: bytes,
        session: Session,
        userIdentityToken: Any,
    ) -> Any | SessionActivation:
        """Authenticate a session and return its context or activation result.

        The base implementation accepts anonymous tokens and rejects everything
        else. Override it to authenticate; raise
        [`StatusCodeError`][o6.StatusCodeError] to reject.

        Args:
            endpoint: The endpoint the session is connecting through.
            remoteCertificate: The client certificate, empty when unsecured.
            session: The session being activated.
            userIdentityToken: The decoded identity token, for example an
                `AnonymousIdentityToken` or `UserNameIdentityToken`. An empty
                token arrives as `AnonymousIdentityToken`.

        Returns:
            Any object to keep as `session.context`, or a
            [`SessionActivation`][o6.server.SessionActivation] to also assign roles.

        Raises:
            StatusCodeError: Authentication failed. `BAD_IDENTITY_TOKEN_REJECTED`
                is the usual choice.
        """
        if isinstance(userIdentityToken, ns0.datatypes.AnonymousIdentityToken):
            return None
        raise o6.StatusCodeError(o6.StatusCode.BAD_IDENTITY_TOKEN_REJECTED)

    def closeSession(self, session: Session) -> None:
        """Release a context returned by `activateSession`.

        Called once per session, when the session ends for any reason. The base
        implementation does nothing.

        Args:
            session: The session that is closing.
        """

    def getUserRightsMask(self, session: Session, nodeId: o6.NodeId) -> int:
        """Return the session's UserWriteMask for one node.

        The base implementation maps the `WRITE_ATTRIBUTE`,
        `WRITE_ROLE_PERMISSIONS` and `WRITE_HISTORIZING` permissions to the
        mask. See [`AttributeWriteMask`][o6.ns.ns0.datatypes.AttributeWriteMask]
        for the bit layout.
        """
        permissions = _permissions(session, nodeId)
        if permissions == _NO_RULES:
            return 0xFFFFFFFF
        write_mask = ns0.datatypes.AttributeWriteMask
        permission = ns0.datatypes.PermissionType
        mask = 0
        if permissions & permission.WRITE_ATTRIBUTE:
            mask = 0xFFFFFFFF & ~(write_mask.ROLE_PERMISSIONS | write_mask.HISTORIZING)
        if permissions & permission.WRITE_ROLE_PERMISSIONS:
            mask |= write_mask.ROLE_PERMISSIONS
        if permissions & permission.WRITE_HISTORIZING:
            mask |= write_mask.HISTORIZING
        return int(mask)

    def getUserAccessLevel(self, session: Session, nodeId: o6.NodeId) -> int:
        """Return the session's UserAccessLevel for one Variable.

        The base implementation maps the `READ`, `WRITE`, `READ_HISTORY` and
        the history-update permissions to the level. `STATUS_WRITE` and
        `TIMESTAMP_WRITE` are granted only for nodes without permission rules.
        See [`AccessLevelType`][o6.ns.ns0.datatypes.AccessLevelType] for the
        bit layout.
        """
        permissions = _permissions(session, nodeId)
        if permissions == _NO_RULES:
            return 0xFF
        access = ns0.datatypes.AccessLevelType
        permission = ns0.datatypes.PermissionType
        history_write = (
            permission.INSERT_HISTORY | permission.MODIFY_HISTORY | permission.DELETE_HISTORY
        )
        level = 0
        if permissions & permission.READ:
            level |= access.CURRENT_READ
        if permissions & permission.WRITE:
            level |= access.CURRENT_WRITE
        if permissions & permission.READ_HISTORY:
            level |= access.HISTORY_READ
        if permissions & history_write:
            level |= access.HISTORY_WRITE
        return int(level)

    def getUserExecutable(self, session: Session, methodId: o6.NodeId) -> bool:
        """Return whether the session may execute a Method at all.

        The base implementation requires the `CALL` permission on the Method.
        """
        return _permits(session, methodId, ns0.datatypes.PermissionType.CALL)

    def getUserExecutableOnObject(
        self,
        session: Session,
        methodId: o6.NodeId,
        objectId: o6.NodeId,
    ) -> bool:
        """Return whether the session may execute a Method on one Object.

        The base implementation requires the `CALL` permission on both the
        Object and the Method. Use this hook when the answer depends on the
        Object instance.
        """
        call = ns0.datatypes.PermissionType.CALL
        return _permits(session, objectId, call) and _permits(session, methodId, call)

    def allowAddNode(self, session: Session, item: Any) -> bool:
        """Return whether the session may add a node.

        The base implementation requires the `ADD_NODE` permission on the
        parent node.

        Args:
            session: The requesting session.
            item: The requested `AddNodesItem`.
        """
        return _permits(session, item.parentNodeId, ns0.datatypes.PermissionType.ADD_NODE)

    def allowAddReference(self, session: Session, item: Any) -> bool:
        """Return whether the session may add a reference.

        The base implementation requires the `ADD_REFERENCE` permission on the
        source node.

        Args:
            session: The requesting session.
            item: The requested `AddReferencesItem`.
        """
        return _permits(session, item.sourceNodeId, ns0.datatypes.PermissionType.ADD_REFERENCE)

    def allowDeleteNode(self, session: Session, item: Any) -> bool:
        """Return whether the session may delete a node.

        The base implementation requires the `DELETE_NODE` permission on the
        node.

        Args:
            session: The requesting session.
            item: The requested `DeleteNodesItem`.
        """
        return _permits(session, item.nodeId, ns0.datatypes.PermissionType.DELETE_NODE)

    def allowDeleteReference(self, session: Session, item: Any) -> bool:
        """Return whether the session may delete a reference.

        The base implementation requires the `REMOVE_REFERENCE` permission on
        the source node.

        Args:
            session: The requesting session.
            item: The requested `DeleteReferencesItem`.
        """
        return _permits(session, item.sourceNodeId, ns0.datatypes.PermissionType.REMOVE_REFERENCE)

    def allowBrowseNode(self, session: Session, nodeId: o6.NodeId) -> bool:
        """Return whether the session may browse one node.

        The base implementation requires the `BROWSE` permission. This hook
        runs for every browsed node, so keep it cheap.
        """
        return _permits(session, nodeId, ns0.datatypes.PermissionType.BROWSE)

    def allowTransferSubscription(
        self,
        oldSession: Session,
        newSession: Session,
    ) -> bool:
        """Return whether subscriptions may move between two sessions.

        The base implementation applies the open62541 default policy. Sessions
        of the same user (the same user name or certificate subject) may take
        over each other's subscriptions; another user cannot. Anonymous
        sessions both need an encrypting SecurityPolicy and the same client
        ApplicationUri. For a subscription whose session is gone
        (`oldSession.id` is null), open62541 verifies the saved owner identity
        before invoking this hook. The base implementation then permits the
        transfer; an override can still reject it.
        """
        server = oldSession._server
        return server._call_native(
            lambda: server._allow_transfer_subscription(oldSession.id, newSession.id)
        )

    def allowCreateSubscription(self, session: Session) -> bool:
        """Return whether the session may create a subscription.

        The base implementation allows it.
        """
        return True

    def allowHistoryUpdate(
        self,
        session: Session,
        nodeId: o6.NodeId,
        performUpdateType: int,
        value: o6.DataValue,
    ) -> bool:
        """Return whether the session may update history for one node.

        The base implementation requires the `INSERT_HISTORY` permission to
        insert and `MODIFY_HISTORY` to replace or update.

        Args:
            session: The requesting session.
            nodeId: The node whose history is being updated.
            performUpdateType: The requested `PerformUpdateType`.
            value: The [`DataValue`][o6.DataValue] being written.
        """
        update = ns0.datatypes.PerformUpdateType
        permission = ns0.datatypes.PermissionType
        if performUpdateType == update.INSERT:
            return _permits(session, nodeId, permission.INSERT_HISTORY)
        if performUpdateType in (update.REPLACE, update.UPDATE):
            return _permits(session, nodeId, permission.MODIFY_HISTORY)
        return True

    def allowHistoryDelete(
        self,
        session: Session,
        nodeId: o6.NodeId,
        startTimestamp: Any,
        endTimestamp: Any,
        isDeleteModified: bool,
    ) -> bool:
        """Return whether the session may delete history for one node.

        The base implementation requires the `DELETE_HISTORY` permission.

        Args:
            session: The requesting session.
            nodeId: The node whose history is being deleted.
            startTimestamp: Start of the range to delete.
            endTimestamp: End of the range to delete.
            isDeleteModified: Delete modified values rather than raw ones.
        """
        return _permits(session, nodeId, ns0.datatypes.PermissionType.DELETE_HISTORY)


# =============================================================================
# Server – high-level OPC UA server
# =============================================================================


class _ServerNamespaces:
    """The server-side namespace host: publishes decorator-authored nodeset
    modules into the address space via `append`.

    It carries no per-instance Python node tree — namespace registration lives
    in the process-wide `o6.ns` registry and the OPC UA server's own
    namespace array."""

    def __init__(self, server: "Server") -> None:
        # Avoid keeping the server alive solely through server.ns -> server.
        # This lets the weak live-server registry forget local servers as soon
        # as user code releases them.
        self._server = _server_proxy(server)
        self._nodeset_modules: list[ModuleType] = []
        self._pending_publications: dict[
            ModuleType, _server_materialization._NamespacePublisher
        ] = {}

    def set_default_permissions(
        self,
        namespace: int | str,
        permissions: Mapping[Role | o6.NodeId, ns0.datatypes.PermissionType],
    ) -> None:
        server = self._server
        values = {_role_id(server, role): int(value) for role, value in permissions.items()}

        def apply() -> None:
            index = (
                namespace if isinstance(namespace, int) else server._get_namespace_index(namespace)
            )
            server._set_namespace_role_permissions(index, values)

        server._call_native(apply)

    def get_default_permissions(
        self, namespace: int | str
    ) -> dict[Role, ns0.datatypes.PermissionType]:
        server = self._server

        def read() -> dict[Any, int]:
            index = (
                namespace if isinstance(namespace, int) else server._get_namespace_index(namespace)
            )
            return dict(server._get_namespace_role_permissions(index))

        return {
            server.roles[role_id]: ns0.datatypes.PermissionType(value)
            for role_id, value in server._call_native(read).items()
        }

    def append(self, ns: ModuleType) -> None:
        """Publish a nodeset module authored with the `@o6` decorators.

        The module must have called `o6.ns.namespace` (one or more
        times) at import time; every namespace module recorded in its
        `__NAMESPACES__` set is registered with this server, then the
        module's decorated nodes are injected into the address space."""
        ns_infos = getattr(ns, "__NAMESPACES__", None)
        if ns_infos is None:
            raise ValueError(f"Module {ns.__name__} has no __NAMESPACES__ metadata")

        if ns in self._nodeset_modules:
            return

        module_uris = {info.uri for info in ns_infos}
        for pending in self._pending_publications:
            if pending is not ns and module_uris & {info.uri for info in pending.__NAMESPACES__}:
                raise RuntimeError(f"Finish publishing {pending.__name__} before {ns.__name__}")

        published_uris = {
            info.uri
            for module in self._nodeset_modules
            for info in getattr(module, "__NAMESPACES__", ())
        }
        overlapping_uris = module_uris & published_uris
        if overlapping_uris and overlapping_uris != module_uris:
            raise ValueError(
                f"Module {ns.__name__} mixes already-published namespace URIs "
                f"({', '.join(sorted(overlapping_uris))}) with new namespace URIs"
            )

        for info in ns_infos:
            global_index = info.index
            assert global_index is not None
            self._server._run_on_loop(
                partial(self._server._add_namespace, info.uri, global_index),
                sync_result=True,
                wait=True,
            )

        # Track the module so ``_all_registered_markers`` can walk reference-type markers
        # declared in companion specs already loaded into this process.
        if overlapping_uris:
            # The NamespaceArray identifies namespaces by URI.  Historical
            # releases of a companion specification can therefore coexist in
            # the Python registry, but not in one server address space.  Keep
            # the first published release and only register this module's
            # global-index aliases above.
            return
        self._inject_nodes(ns)
        self._nodeset_modules.append(ns)
        self._pending_publications.pop(ns)

    def _inject_nodes(self, ns: ModuleType) -> None:
        publisher = self._pending_publications.get(ns)
        if publisher is None:
            publisher = _server_materialization._NamespacePublisher(
                self._server, self._nodeset_modules, _server_materialization._NamespaceInventory(ns)
            )
            self._pending_publications[ns] = publisher
        # A NodeSet Variable without a Value stays empty instead of getting a default.
        previous = self._server._run_on_loop(
            partial(self._server._set_allow_empty_variables, True), sync_result=True, wait=True
        )
        try:
            publisher.publish()
        finally:
            self._server._run_on_loop(
                partial(self._server._set_allow_empty_variables, previous),
                sync_result=True,
                wait=True,
            )


# `next()` on a count is atomic, so concurrent servers get distinct auto-names
_server_name_counter = itertools.count()
_live_servers: weakref.WeakSet["Server"] = weakref.WeakSet()
# Reentrant: a garbage collection inside the lock can run Server.__del__
_live_servers_lock = threading.RLock()


def _register_live_server(server: "Server") -> None:
    with _live_servers_lock:
        _live_servers.add(server)


def _unregister_live_server(server: "Server") -> None:
    with _live_servers_lock:
        _live_servers.discard(server)


def _release_owned_loop(loop: asyncio.AbstractEventLoop) -> None:
    """Drop the hold on a server's owned loop once the server is collected.

    The `weakref.finalize` registry keeps the loop reachable from outside the
    server's reference cycle. Without that hold, a GC pass that collects the
    cycle can finalize the loop's self-pipe sockets before `Server.__del__`
    closes the loop, as the free-threaded GC does. `close()` then fails, and the
    loop warns that it is unclosed. `__del__` still closes the loop.
    """


def _get_live_servers() -> tuple["Server", ...]:
    """Return the currently usable server objects in this process."""
    with _live_servers_lock:
        return tuple(_live_servers)


class Server(_NativeServer):
    """High-level OPC UA server.

    ```python
    server = o6.Server(port=4840)
    with server:
        temperature = server.addVariable("Temperature", server.objectsNode, 22.5)
        print(temperature())
    ```

    Whether a call returns a value or an awaitable depends on the operation and
    the caller's loop. Node creation returns handles directly, except to an
    async task on another loop while the worker runs, which receives an
    awaitable. See [`MaybeAwaitable`][o6.MaybeAwaitable].

    See the [Server guide](manual/server/index.md) and
    [Server callbacks](manual/server/callbacks.md).

    `config` exposes native quotas, interval and queue ranges, and listener URLs.
    Its getters return synchronous detached values; these settings require a
    fully stopped server for assignment. Configure encryption before custom
    settings because `config.setEncryption()` resets native defaults. See
    [Configuration](manual/server/lifecycle.md#quotas-intervals-and-listening-addresses)
    for properties, units, defaults, and validation rules.
    """

    ns: _ServerNamespaces

    def enablePushManagement(self) -> None:
        """Enable remote certificate and trust-list management before startup.

        Call once on a fully stopped server after configuring its certificate,
        private key, encrypted security policies and authentication. This method
        is synchronous, including in asyncio applications. Encryption and filestore
        configuration cannot be reset afterwards. Starting the same instance
        again retains management support.

        Enables the standard `ServerConfiguration` methods with SecurityAdmin
        permissions and preserves the anonymous permission fallback. Configure
        session security modes and method authorization through `AccessControl`.
        See [GDS PushManagement](manual/server/security.md#gds-pushmanagement)
        for access control, certificate storage and transaction lifecycle.

        Returns:
            None.

        Raises:
            StatusCodeError: PushManagement is already enabled or the server is
                starting, running or stopping.
            RuntimeError: The certificate, private key or encrypted security
                policy configuration is missing.
            NotImplementedError: The platform or build lacks PushManagement support.
            MemoryError: Not enough memory to enable PushManagement.
        """
        self._enable_push_management()

    _loop: asyncio.AbstractEventLoop

    root: ObjectNode
    """Canonical handle for the Root folder (`i=84`), available without awaiting."""

    objects: ObjectNode
    """Canonical handle for the Objects folder (`i=85`), available without awaiting."""

    types: ObjectNode
    """Canonical handle for the Types folder (`i=86`), available without awaiting."""

    views: ObjectNode
    """Canonical handle for the Views folder (`i=87`), available without awaiting."""

    def __init__(
        self,
        port: int = 4840,
        logger: logging.Logger | None = None,
        loop: asyncio.AbstractEventLoop | None = None,
        *,
        certificate: str | Path | bytes | None = None,
        privateKey: str | Path | bytes | None = None,
        trustList: list[str | Path | bytes] | None = None,
        issuerList: list[str | Path | bytes] | None = None,
        revocationList: list[str | Path | bytes] | None = None,
        secureOnly: bool = False,
        securityPolicies: Iterable[str] | None = None,
        acceptAllCertificates: bool = False,
        applicationUri: str | None = None,
        applicationName: str | o6.LocalizedText | None = None,
        productUri: str | None = None,
        accessControl: AccessControl | None = None,
        allowNonePolicyPassword: bool = False,
        rbacForAnonymous: bool = False,
    ) -> None:
        """Create a server. It is not listening until `start()` is called.

        Args:
            port: TCP port to bind.
            logger: Logger for server output. Defaults to the `o6.server` logger.
            loop: Event loop that runs the server iterations. If a loop is
                given or one is running, the server uses it and starts no
                thread. Otherwise it creates its own loop and runs it on a
                daemon thread.
            certificate: Server certificate, as a path or raw DER or PEM bytes.
                Requires `privateKey`. Must not be empty.
            privateKey: Matching private key, as a path or raw bytes. Requires
                `certificate`. Must not be empty.
            trustList: Client certificates, or the CA certificates of their
                issuers, that the server trusts. The same list checks X.509
                user tokens. With a certificate but without a trust list, the
                server rejects every client certificate.
            issuerList: CA certificates that complete the chain of a trusted
                certificate. They are not trusted themselves.
            revocationList: Certificate revocation lists of the trusted and
                issuer CAs.
            secureOnly: Refuse unencrypted connections. Requires a certificate
                and private key.
            securityPolicies: The SecurityPolicies to offer, by name:
                `"None"`, `"Basic128Rsa15"`, `"Basic256"`, `"Basic256Sha256"`,
                `"Aes128_Sha256_RsaOaep"` and `"Aes256_Sha256_RsaPss"`. The
                full policy URI is accepted too. The server offers exactly
                these policies, with a Sign and a SignAndEncrypt endpoint
                for each one except `"None"`. The deprecated `"Basic128Rsa15"`
                and `"Basic256"` get a low, non-zero SecurityLevel, below
                the other policies. `None` selects the default: the three
                SHA-256 policies, plus `"None"` unless `secureOnly` is set.
                Requires a certificate and private key, and excludes
                `secureOnly`. A policy that cannot be set up with the
                certificate fails the constructor.
            acceptAllCertificates: Trust every client certificate and ignore
                the trust list. Defaults to `False`. For development only.
            applicationUri: Override the advertised application URI. It must match
                the URI inside the server certificate on secured endpoints.
            applicationName: ApplicationName advertised in GetEndpoints,
                FindServers and LDS registrations. A `str` is published with
                locale `"en"`. Defaults to `"o6-python Server"`.
            productUri: ProductUri of the ApplicationDescription and of
                `Server/ServerStatus/BuildInfo`. Defaults to
                `"https://o6-automation.com/o6-python"`. BuildInfo's
                SoftwareVersion defaults to `o6.__version__`. Set the other
                BuildInfo fields with `config.buildInfo`.
            accessControl: An [`AccessControl`][o6.server.AccessControl] subclass
                instance that authenticates and authorizes sessions.
            allowNonePolicyPassword: Permit username/password tokens on an
                unencrypted channel.
            rbacForAnonymous: Deny operations on nodes that have neither node
                nor namespace role permissions. Defaults to `False`. The fallback
                affects all session roles. To support client connection setup,
                namespace 0 gets
                default permissions that grant Browse and Read to the
                Anonymous and AuthenticatedUser roles; change them with
                `server.ns.set_default_permissions(0, ...)`. The inherited
                authorization hooks of a custom `AccessControl` apply the same
                rules. See [Access Control & Roles](manual/server/security.md).

        Raises:
            TypeError: `accessControl` is not an `o6.AccessControl` instance.
            ValueError: Credentials are incomplete or empty, `secureOnly` or
                `securityPolicies` is requested without a certificate and
                private key, or `securityPolicies` is empty, names an unknown
                policy or is combined with `secureOnly`.
            PermissionError: This build has no `server` feature entitlement.
        """
        _requireServer()
        if (certificate is None) != (privateKey is None):
            raise ValueError("certificate and privateKey must be provided together")
        if secureOnly and certificate is None:
            raise ValueError("secureOnly requires certificate and privateKey")
        if securityPolicies is not None and certificate is None:
            raise ValueError("securityPolicies requires certificate and privateKey")
        cert_bytes = _load_cert_or_bytes(certificate)
        key_bytes = _load_cert_or_bytes(privateKey)
        if certificate is not None and (not cert_bytes or not key_bytes):
            raise ValueError("certificate and privateKey must not be empty")

        if loop is not None:
            self._loop: asyncio.AbstractEventLoop = loop
            self._owns_loop = False
        else:
            try:
                self._loop = asyncio.get_running_loop()
                self._owns_loop = False
            except RuntimeError:
                self._loop = asyncio.new_event_loop()
                self._owns_loop = True
                weakref.finalize(self, _release_owned_loop, self._loop)
        # start() creates the worker; native helpers read it from here on
        self._worker: _WorkerLoop | None = None

        if logger is None:
            logger = logging.getLogger(__name__)

        kwargs: dict = {"port": port, "loop": self._loop, "logger": logger}
        super().__init__(**kwargs)
        self._mdns_config: MdnsConfig | None = None
        self._listener_startup: asyncio.Future | None = None
        self._shutdown_task: asyncio.Task[None] | None = None
        self._shutdown_thread: threading.Thread | None = None
        self._node_backend = _ServerBackend(self)
        self._pending_history: list[tuple[o6.NodeId, History]] = []
        self._warned_event_fields: set[tuple[o6.NodeId, o6.QualifiedName | str]] = set()
        for marker in _server_materialization._collect_variabletype_markers(ns0):
            self._attach_instance_type(marker, VariableNode)
        self.roles = _RoleRegistry(self)
        self._certificate_rejected_callback: Callable[[bytes, o6.StatusCode], Any] | None = None
        self._notification_sync_lock = threading.Lock()
        self._notification_categories: dict[int, NotificationHandlers] = {
            dispatch_key(t): NotificationHandlers(self._sync_notification_trampoline)
            for t in _NOTIFICATION_PROPERTIES.values()
        }
        self._set_all_permissions_for_anonymous(not rbacForAnonymous)
        if rbacForAnonymous:
            # Deny-by-default would also deny the NamespaceArray and
            # ServerStatus reads every client needs to connect.
            browse_read = int(
                ns0.datatypes.PermissionType.BROWSE | ns0.datatypes.PermissionType.READ
            )
            self._set_namespace_role_permissions(
                0,
                {
                    _role_id(self, roles.anonymous): browse_read,
                    _role_id(self, roles.authenticated_user): browse_read,
                },
            )

        # Apply encryption if certificate and key are provided
        if cert_bytes and key_bytes:
            tl = _load_cert_list(trustList)
            il = _load_cert_list(issuerList)
            rl = _load_cert_list(revocationList)
            self.config.setEncryption(
                cert_bytes,
                key_bytes,
                port,
                tl,
                il,
                rl,
                secureOnly,
                securityPolicies,
            )

        if acceptAllCertificates:
            self.config.setAcceptAllCertificates()

        # Security-policy configuration rebuilds the underlying open62541
        # config, so apply the application identity and access control last.
        if applicationUri is not None:
            self.config.applicationUri = applicationUri
        if applicationName is not None or productUri is not None:
            description = self.config.applicationDescription
            if isinstance(applicationName, str):
                # The shorthand splits at the first colon only
                applicationName = o6.LocalizedText(f"en:{applicationName}")
            if applicationName is not None:
                description.applicationName = applicationName
            if productUri is not None:
                description.productUri = productUri
                buildInfo = self.config.buildInfo
                buildInfo.productUri = productUri
                self.config.buildInfo = buildInfo
            self.config.applicationDescription = description
        # Report the o6 version, not open62541's, as SoftwareVersion
        buildInfo = self.config.buildInfo
        buildInfo.softwareVersion = o6.__version__
        self.config.buildInfo = buildInfo
        self.config.allowNonePolicyPassword = allowNonePolicyPassword
        if accessControl is not None:
            if not isinstance(accessControl, AccessControl):
                raise TypeError("access_control must be an o6.AccessControl instance")
            self.config.setAccessControl(accessControl)

        self._name = f"server{next(_server_name_counter)}"

        self._port = port
        self.ns = _ServerNamespaces(self)
        self.root = cast(ObjectNode, _server_node(self, "i=84", ObjectNode))
        self.objects = cast(ObjectNode, _server_node(self, "i=85", ObjectNode))
        self.types = cast(ObjectNode, _server_node(self, "i=86", ObjectNode))
        self.views = cast(ObjectNode, _server_node(self, "i=87", ObjectNode))
        _register_live_server(self)

    def _attach_instance_type(self, marker: type, node_type: type[Node]) -> None:
        _server_types._attach_instance_type(self, marker, node_type)

    @overload
    def implement(self, declaration: type, implementation: type | None, /) -> None: ...

    @overload
    def implement(self, target: MethodNode, behavior: None, /) -> None: ...

    @overload
    def implement(self, target: VariableNode, behavior: Any, /) -> None: ...

    @overload
    def implement(
        self,
        target: MethodNode | NodeIdLike,
        /,
        *,
        call: Callable[..., Any] | None,
    ) -> None: ...

    @overload
    def implement(
        self,
        target: VariableNode | VariableTypeNode | type | NodeIdLike,
        /,
        *,
        read: VariableReadCallback | None | object = _CALLBACK_UNSET,
        write: VariableWriteCallback | None | object = _CALLBACK_UNSET,
    ) -> None: ...

    def implement(
        self,
        target: MethodNode | VariableNode | VariableTypeNode | NodeIdLike | type,
        implementation: Any = _CALLBACK_UNSET,
        /,
        *,
        call: Callable[..., Any] | None | object = _CALLBACK_UNSET,
        read: VariableReadCallback | None | object = _CALLBACK_UNSET,
        write: VariableWriteCallback | None | object = _CALLBACK_UNSET,
    ) -> None:
        """Install Python behaviour on a UA type or a concrete node of this server.

        - `implement(DeclarationType, ImplementationType)` binds an undecorated
          Python subclass to an existing ObjectType or VariableType. Future
          instances created natively or by AddNodes use that class. The
          information model is not changed. Children selected by the
          implementation are created before the native Mandatory children. The
          Python initializer runs once, after the whole subtree exists, and
          must be callable without required arguments. `None` restores the
          declaration's own Python type for future instances.
        - `implement(node, None)` on a Method or Variable repeats the callback
          resolution done at construction.
        - `implement(variable, value)` removes both callbacks and stores
          `value` in native storage.
        - `call=`, `read=` and `write=` replace or clear one callback slot on a
          Method, Variable or VariableType.

        A type-level change never alters existing instances.

        Args:
            target: The declared type to implement, or a concrete Method,
                Variable, VariableType, or NodeId-like value.
            implementation: An implementation class for a type target, `None` to
                reset, or a value to store for a Variable target. Cannot be
                combined with the keyword slots.
            call: Method implementation, or `None` to clear the slot.
            read: Variable value-read implementation, or `None` to clear the slot.
            write: Variable value-write implementation, or `None` to clear the
                slot.

        Raises:
            TypeError: An implementation class is combined with `call=`, `read=`,
                or `write=`; a Method is given a positional value other than
                `None`; or a positional value targets something that is neither a
                Method nor a Variable.

        See [Implementing behaviour](manual/information-model-authoring/implementing-types.md) and
        [Server callbacks](manual/server/callbacks.md).
        """
        self._run_on_loop(
            partial(self._implement, target, implementation, call=call, read=read, write=write),
            sync_result=True,
            wait=True,
        )

    def _implement(
        self,
        target: MethodNode | VariableNode | VariableTypeNode | NodeIdLike | type,
        implementation: Any,
        *,
        call: Callable[..., Any] | None | object,
        read: VariableReadCallback | None | object,
        write: VariableWriteCallback | None | object,
    ) -> None:
        """Run `implement` on the loop thread, where it resolves and reads nodes."""
        if implementation is not _CALLBACK_UNSET:
            if (
                call is not _CALLBACK_UNSET
                or read is not _CALLBACK_UNSET
                or write is not _CALLBACK_UNSET
            ):
                raise TypeError(
                    "implementation class cannot be combined with call=, read=, or write="
                )
            if isinstance(target, type):
                _server_types._implement(
                    self,
                    target,
                    cast(type | None, implementation),
                )
                return
            target_node = self._callback_target(target)
            if isinstance(target_node, MethodNode):
                if implementation is not None:
                    raise TypeError("a Method can only be reset with positional None")
                _server_construction._restore_construction_callbacks(self, target_node)
                return
            if not isinstance(target_node, VariableNode):
                raise TypeError("positional behavior requires a concrete Method or Variable")
            if implementation is None:
                _server_construction._restore_construction_callbacks(self, target_node)
            else:
                value = (
                    o6.Double(implementation)
                    if isinstance(implementation, float)
                    else implementation
                )
                self._run_on_loop(
                    lambda: super(Server, self)._set_local_value(target_node, value),
                    sync_result=True,
                    wait=True,
                )
            return
        self._implement_callbacks(target, call=call, read=read, write=write)

    def _variable_instance_type(self, type_id: o6.NodeIdLike) -> type[VariableNode]:
        return cast(type[VariableNode], _server_types._variable_instance_type(self, type_id))

    def createEvent(
        self,
        eventType: NodeIdLike | None = None,
        *,
        source: NodeIdLike = ns0.instances.server,
        message: LocalizedTextLike = "",
        severity: int = 1,
        fields: Mapping[o6.QualifiedName | str, Any] | None = None,
        eventInstance: NodeIdLike | None = None,
    ) -> MaybeAwaitable[bytes]:
        """Emit an event immediately and return its EventId.

        Matches C's `UA_Server_createEvent`. `emitEvent` is an alias. Use
        `o6.Event(server, ...)` for a reusable draft.

        The event type is `eventType`, else the type of `eventInstance`, else
        the `GeneratesEvent` target of the type of `source`, else
        `BaseEventType`. Field values come from `fields`, then from
        `eventInstance`, then from the defaults. The stored `EventType` and
        `SourceNode` of the instance override the arguments, even when null.
        The instance is only read. See
        [Events](manual/server/events.md#events).

        Args:
            eventType: The event type, or `None` to infer it.
            source: The SourceNode of the event. Defaults to the Server Object.
            message: The event message.
            severity: The event severity, `1..1000`.
            fields: Explicit field values. A key is the BrowseName of a field
                of the event type (`"BatchId"`), a path of BrowseNames with
                registered shortnames or process-wide namespace indexes
                (`"/plant:BatchId"`), or a [`QualifiedName`][o6.QualifiedName].
                A key that is likely a mistake warns once. See
                [Event fields](manual/server/events.md#event-fields).
            eventInstance: An Object of `BaseEventType` or a subtype that
                supplies field values. A node handle must belong to this
                server. A NodeId is resolved on this server.

        Returns:
            The EventId, or an awaitable of it for an async caller on another
            event loop.

        Raises:
            ValueError: `severity` is out of range, or the type cannot be
                inferred because `source` has no type definition or its type
                declares more than one `GeneratesEvent` target.
            TypeError: `eventInstance` belongs to another server or is not an
                event Object instance.
        """
        if not 1 <= severity <= 1000:
            raise ValueError("event severity must be between 1 and 1000")
        localized_message = (
            message if isinstance(message, o6.LocalizedText) else o6.LocalizedText(message)
        )
        if isinstance(eventInstance, Node):
            if eventInstance._backend is not self._node_backend:
                raise TypeError("eventInstance must belong to the same server")
            eventInstance._check_attached()
        type_id, source_id, normalized_fields, instance_id = _normalize_event_args(
            eventType, source, fields, eventInstance
        )

        async def _do() -> bytes:
            resolved_type = type_id
            if instance_id is not None:
                instance_type = await self._event_instance_type(instance_id)
                if resolved_type is None:
                    resolved_type = instance_type
            if resolved_type is None:
                resolved_type = await self._resolve_generates_event_type(source_id)
            event_fields = await self._resolve_event_fields(resolved_type, normalized_fields)
            return super(Server, self)._emit_event(
                source_id,
                resolved_type,
                severity,
                localized_message,
                event_fields,
                instance_id,
            )

        return self._run_on_loop(_do)

    emitEvent = createEvent

    async def _event_instance_type(self, instance_id: o6.NodeId) -> o6.NodeId:
        node_class = self._read_attribute(instance_id, int(o6.AttributeId.NODE_CLASS))
        if inspect.isawaitable(node_class):
            node_class = await node_class
        if node_class != ns0.datatypes.NodeClass.OBJECT:
            raise TypeError(
                "eventInstance must be an Object instance of BaseEventType or a subtype"
            )
        try:
            type_id = self._get_node_type(instance_id)
        except o6.StatusCodeError as exc:
            if exc.code != o6.StatusCode.BAD_NOT_FOUND:
                raise
            raise TypeError(
                "eventInstance must have a BaseEventType-derived type definition"
            ) from exc
        base_type = o6.NodeId(ns0.objtypes.BaseEventType)
        if type_id != base_type:
            ancestors = self.browseRecursive(
                type_id,
                direction=ns0.datatypes.BrowseDirection.INVERSE,
                reftype=ns0.reftypes.HasSubtype,
            )
            ancestors = await ancestors if inspect.isawaitable(ancestors) else ancestors
            if not any(o6.NodeId(ancestor) == base_type for ancestor in ancestors):
                raise TypeError(
                    "eventInstance must be an Object instance of BaseEventType or a subtype"
                )
        return type_id

    async def _resolve_event_fields(
        self, event_type: o6.NodeId, fields: dict[o6.QualifiedName | str, Any]
    ) -> dict[o6.QualifiedName | str, Any]:
        """Key the fields with the paths open62541 compares with event filters.

        A filter selects a field by a path of server-side BrowseNames, such as
        `/2:Counter`. The keys use process-wide namespace indexes or
        shortnames, or name a field of the event type without a path. Resolve
        against the current model on every emission: fields and namespaces
        can be added or changed after an earlier emission.
        """
        resolved: dict[o6.QualifiedName | str, Any] = {}
        for key, value in fields.items():
            path, problem = await self._resolve_event_field(event_type, key)
            warning_key = (event_type, key)
            if problem is not None and warning_key not in self._warned_event_fields:
                warnings.warn(
                    f"Event field {key!r} of event type {event_type}: {problem}. "
                    f"The event is emitted with the key {path!r}, which event filters "
                    "may not select",
                    UserWarning,
                    stacklevel=2,
                )
                if len(self._warned_event_fields) >= 4096:
                    self._warned_event_fields.clear()
                self._warned_event_fields.add(warning_key)
            resolved[path] = value
        return resolved

    async def _resolve_event_field(
        self, event_type: o6.NodeId, key: o6.QualifiedName | str
    ) -> tuple[o6.QualifiedName | str, str | None]:
        """Return the open62541 key of one event field and why it is suspect.

        A path is translated as given, also when the event type does not
        declare it, since a field can travel without a declaration. The
        problems are the likely mistakes: an unknown namespace, a BrowseName
        that names no field, and a path in the wrong namespace.
        """
        if isinstance(key, o6.QualifiedName):
            # A QualifiedName is a path whose namespace is the default of its
            # segments, as in open62541, or just the BrowseName of a field.
            path = key.name if key.name.startswith("/") else f"/{key.name}"
            default = key.ns if isinstance(key.ns, int) else key.ns.index
            bare = False
        elif key.startswith("/"):
            path, default, bare = key, 0, False
        elif "/" in key:
            return key, None  # A path with a TypeDefinitionId is passed on.
        else:
            path, default, bare = f"/{key}", 0, True
        parsed = _event_path_names(path, default)
        if parsed is None:
            return key, None
        names, suffix, unknown = parsed
        if unknown is not None:
            return key, f"{unknown!r} is not a registered namespace shortname"
        types = await self._event_type_chain(event_type)
        problem = None
        if bare and not names[0][1]:
            matches = await self._event_field_names(types, names[0][0].name)
            if len(matches) == 1:
                names = [(matches[0], True)]
            elif matches:
                listed = ", ".join(sorted(repr(str(match)) for match in matches))
                return key, f"the name matches several fields ({listed}); use a path"
            else:
                problem = "the event type has no field with this BrowseName"
        browse_names = [name for name, _ in names]
        indexes = [self._event_namespace_index(name) for name in browse_names]
        if any(index is None for index in indexes):
            return key, "its namespace is not published on this server"
        resolved = _event_path_string(
            cast(list[int], indexes), [name.name for name in browse_names], suffix
        )
        if problem is None and len(browse_names) == 1:
            name = browse_names[0]
            if not await self._event_path_exists(types, browse_names):
                others = [
                    match
                    for match in await self._event_field_names(types, name.name)
                    if match != name
                ]
                if others:
                    listed = ", ".join(sorted(repr(str(match)) for match in others))
                    problem = f"the event type has no such field, but has {listed}"
        return resolved, problem

    def _event_namespace_index(self, name: o6.QualifiedName) -> int | None:
        namespace = name.ns
        if isinstance(namespace, int):
            # Index 1 is the alias of the server's application namespace.
            return namespace if namespace in (0, 1) else None
        try:
            return int(self._get_namespace_index(namespace.uri))
        except KeyError:
            return None

    async def _event_type_chain(self, event_type: o6.NodeId) -> list[o6.NodeId]:
        """The event type and its supertypes, which declare its fields."""
        ancestors = self.browseRecursive(
            event_type,
            direction=ns0.datatypes.BrowseDirection.INVERSE,
            reftype=ns0.reftypes.HasSubtype,
        )
        ancestors = await ancestors if inspect.isawaitable(ancestors) else ancestors
        chain = [event_type]
        chain.extend(o6.NodeId(ancestor) for ancestor in ancestors)
        return list(dict.fromkeys(chain))

    async def _event_field_names(self, types: list[o6.NodeId], name: str) -> list[o6.QualifiedName]:
        found: list[o6.QualifiedName] = []
        for type_id in types:
            query = _browse_description(
                type_id,
                ns0.datatypes.BrowseDirection.FORWARD,
                ns0.reftypes.HierarchicalReferences,
                True,
                ns0.datatypes.NodeClass.VARIABLE,
                ns0.datatypes.BrowseResultMask.BROWSE_NAME,
            )
            for reference in self._browse_references(type_id, query):
                if reference.browseName.name == name and reference.browseName not in found:
                    found.append(reference.browseName)
        return found

    async def _event_path_exists(
        self, types: list[o6.NodeId], names: list[o6.QualifiedName]
    ) -> bool:
        request = ns0.datatypes.TranslateBrowsePathsToNodeIdsRequest(
            browsePaths=[_simplified_browse_path(type_id, names) for type_id in types]
        )
        response = super(Server, self)._translate_browse_paths(request)
        response = await response if inspect.isawaitable(response) else response
        return any(
            int(result.statusCode) & 0xC0000000 == 0 and result.targets
            for result in response.results
        )

    async def _resolve_generates_event_type(self, source_id: o6.NodeId) -> o6.NodeId:
        """Infer eventType from source's declared type's GeneratesEvent reference.

        Browses fresh on every call rather than caching by type: the
        information model can change at runtime (references added or
        removed), and a cached answer would silently go stale.
        """
        try:
            type_id = self._get_node_type(source_id)
        except o6.StatusCodeError as exc:
            if exc.code != o6.StatusCode.BAD_NOT_FOUND:
                raise
            raise ValueError(
                f"cannot infer eventType: source {source_id} has no type definition; "
                "pass eventType= explicitly"
            ) from exc

        browsed = self.browse(type_id, reftype=ns0.reftypes.GeneratesEvent)
        result = await browsed if inspect.isawaitable(browsed) else browsed
        targets = [o6.NodeId(ref.nodeId) for ref in result]
        if not targets:
            return o6.NodeId(ns0.objtypes.BaseEventType)
        if len(targets) == 1:
            return targets[0]
        raise ValueError(
            f"cannot infer eventType: type {type_id} declares more than one "
            "GeneratesEvent target; pass eventType= explicitly"
        )

    # -- Thread-safe dispatch ------------------------------------------------

    def _run_on_loop(
        self, fn: Callable[[], Any], *, sync_result: bool = False, wait: bool = False
    ) -> Any:
        """Run a native operation on this server's loop thread; see `o6.util._run_on_loop`."""
        return _run_on_loop(
            self._loop,
            lambda: self._worker,
            fn,
            sync_result=sync_result,
            wait=wait,
            owner="Server",
        )

    @property
    def config(self) -> o6.ServerConfig:
        """This server's [`ServerConfig`][o6.ServerConfig].

        Readable from any thread. It can be changed only while the server is
        fully stopped.
        """
        return cast("o6.ServerConfig", _ConfigView(self, super().config))

    def _call_native(self, fn: Callable[[], Any]) -> Any:
        """Return a synchronous native operation's result from any thread; see `o6.util._call_native`."""
        return _call_native(self._loop, lambda: self._worker, fn, owner="Server")

    # -- Well-known nodes (convenience properties) ---------------------------

    def __getitem__(self, key: NodeIdLike) -> MaybeAwaitable[Node]:
        """Return the canonical typed [Node][o6.Node] handle for a NodeId.

        Every lookup of a node returns the same Python object, with its modeled
        type and application state. A deleted node cannot be looked up. A new
        node that reuses the NodeId resolves to the new object.

        Args:
            key: Any value accepted by [NodeId][o6.NodeId]: a string, a numeric
                namespace-0 id, a NodeId or a node handle.

        Returns:
            The matching Node subclass. In any async task (before startup, on
            the server loop or on another loop) an awaitable of it. The
            `root`, `objects`, `types` and `views` handles need no lookup and
            are available without awaiting.

        Raises:
            StatusCodeError: Lookup failed; an unknown or deleted ID has code
                `StatusCode.BAD_NODE_ID_UNKNOWN`.
            RuntimeError: The server has been cleaned up or its worker loop
                is no longer running.

        ```python
        node = server["ns=1;s=Temperature"]        # sync
        node = await server["ns=1;s=Temperature"]  # async
        ```
        """
        return self._run_on_loop(partial(self._node_backend.node_get, o6.NodeId(key)))

    @property
    def objectsNode(self) -> o6.NodeId:
        """The Objects folder (i=85)."""
        return o6.NodeId(ns0.instances.objects)

    @property
    def typesNode(self) -> o6.NodeId:
        """The Types folder (i=86)."""
        return o6.NodeId(ns0.instances.types)

    @property
    def serverNode(self) -> o6.NodeId:
        """The Server object (i=2253)."""
        return o6.NodeId(ns0.instances.server)

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        """The asyncio loop the server runs on, fixed at construction.

        A loop passed in or detected at construction stays owned by the
        caller. A loop the server created is managed by the server; do not
        close it. Await `waitReady()` on this loop.
        """
        return self._loop

    @property
    def endpointUrl(self) -> str:
        """A localhost URL built from the constructor's port.

        With custom `config.serverUrls`, choose a client URL explicitly; this
        convenience property does not track configured or discovered listeners.
        """
        return f"opc.tcp://localhost:{self._port}"

    # -- Notifications -------------------------------------------------------

    @property
    def onLifecycleNotification(self) -> NotificationHandlers:
        """Registry of server-lifecycle notification handlers.

        See [Lifecycle](manual/server/notification-handler.md#lifecycle).
        """
        return self._notification_categories[dispatch_key(NotificationType.LIFECYCLE_STARTED)]

    @onLifecycleNotification.setter
    def onLifecycleNotification(self, value: Any) -> None:
        self.onLifecycleNotification.replace(value)

    @property
    def onSecureChannelNotification(self) -> NotificationHandlers:
        """Registry of secure-channel opened/closed notification handlers.

        See [Secure Channel](manual/server/notification-handler.md#secure-channel).
        """
        return self._notification_categories[dispatch_key(NotificationType.SECURECHANNEL_OPENED)]

    @onSecureChannelNotification.setter
    def onSecureChannelNotification(self, value: Any) -> None:
        self.onSecureChannelNotification.replace(value)

    @property
    def onSessionNotification(self) -> NotificationHandlers:
        """Registry of session created/activated/deactivated/closed notification handlers.

        See [Session](manual/server/notification-handler.md#session).
        """
        return self._notification_categories[dispatch_key(NotificationType.SESSION_CREATED)]

    @onSessionNotification.setter
    def onSessionNotification(self, value: Any) -> None:
        self.onSessionNotification.replace(value)

    @property
    def onServiceNotification(self) -> NotificationHandlers:
        """Registry of service-call begin/end notification handlers.

        Fires around every service request, so handlers here must be fast.

        See [Service](manual/server/notification-handler.md#service).
        """
        return self._notification_categories[dispatch_key(NotificationType.SERVICE_BEGIN)]

    @onServiceNotification.setter
    def onServiceNotification(self, value: Any) -> None:
        self.onServiceNotification.replace(value)

    @property
    def onSubscriptionNotification(self) -> NotificationHandlers:
        """Registry of subscription lifecycle notification handlers.

        Covers created, modified, publishing mode, transferred and deleted.

        See [Subscription](manual/server/notification-handler.md#subscription).
        """
        return self._notification_categories[dispatch_key(NotificationType.SUBSCRIPTION_CREATED)]

    @onSubscriptionNotification.setter
    def onSubscriptionNotification(self, value: Any) -> None:
        self.onSubscriptionNotification.replace(value)

    @property
    def onMonitoredItemNotification(self) -> NotificationHandlers:
        """Registry of MonitoredItem lifecycle notification handlers.

        Covers created, modified, monitoring mode changed and deleted.

        See [MonitoredItem](manual/server/notification-handler.md#monitoreditem).
        """
        return self._notification_categories[dispatch_key(NotificationType.MONITOREDITEM_CREATED)]

    @onMonitoredItemNotification.setter
    def onMonitoredItemNotification(self, value: Any) -> None:
        self.onMonitoredItemNotification.replace(value)

    @property
    def onDiscoveryRegisterServerNotification(self) -> NotificationHandlers:
        """Registry of discovery RegisterServer notification handlers.

        Separate from `onDiscoveryServerOnNetworkNotification`, with a
        different payload.

        See [Discovery: RegisterServer](manual/server/notification-handler.md#discovery-registerserver).
        """
        return self._notification_categories[
            dispatch_key(NotificationType.DISCOVERY_REGISTERSERVER)
        ]

    @onDiscoveryRegisterServerNotification.setter
    def onDiscoveryRegisterServerNotification(self, value: Any) -> None:
        self.onDiscoveryRegisterServerNotification.replace(value)

    @property
    def onDiscoveryServerOnNetworkNotification(self) -> NotificationHandlers:
        """Registry of discovery ServerOnNetwork notification handlers.

        Separate from `onDiscoveryRegisterServerNotification`, with a
        different payload.

        See [Discovery: ServerOnNetwork](manual/server/notification-handler.md#discovery-serveronnetwork).
        """
        return self._notification_categories[
            dispatch_key(NotificationType.DISCOVERY_SERVERONNETWORK)
        ]

    @onDiscoveryServerOnNetworkNotification.setter
    def onDiscoveryServerOnNetworkNotification(self, value: Any) -> None:
        self.onDiscoveryServerOnNetworkNotification.replace(value)

    @property
    def onAuditNotification(self) -> NotificationHandlers:
        """Registry of audit notification handlers.

        open62541 raises audit notifications only when
        `server.config.auditingEnabled` is `True`. `notification.auditEventType`
        names the standardized `AuditEventType` subtype.

        See [Audit](manual/server/notification-handler.md#audit).
        """
        return self._notification_categories[dispatch_key(NotificationType.AUDIT)]

    @onAuditNotification.setter
    def onAuditNotification(self, value: Any) -> None:
        self.onAuditNotification.replace(value)

    # -- Certificates ----------------------------------------------------------

    @property
    def rejectedCertificates(self) -> list[bytes]:
        """Client application certificates the server rejected, as DER bytes.

        Returns a snapshot of rejected SecureChannel certificates, oldest
        first, without duplicates. After 100 distinct certificates, the next
        distinct rejection clears the list and becomes its first entry.
        It lives in memory and is empty after `config.setEncryption()`,
        with `acceptAllCertificates=True`, and without a certificate. Add a
        certificate to `trustList` to trust it.

        See [Rejected certificates](manual/server/lifecycle.md#rejected-certificates).
        """
        return self._call_native(self._rejected_certificates)

    def onCertificateRejected(
        self, callback: Callable[[bytes, o6.StatusCode], Any] | None
    ) -> Callable[[bytes, o6.StatusCode], Any] | None:
        """Call `callback(certificate, statusCode)` for every rejected certificate.

        Covers client application certificates and X.509 user-token
        certificates. `certificate` is the DER certificate (or chain) the
        client sent, `statusCode` the reason, for example
        `BAD_CERTIFICATE_UNTRUSTED`. The callback runs on the server's event
        loop while the server processes the request, so it must not block; a
        coroutine function is scheduled on the loop. Exceptions are logged.
        The server also logs the subject, ApplicationUri and thumbprint of
        every rejected certificate.

        Args:
            callback: The callable, or `None` to remove it. Replaces the
                previously registered callback.

        Returns:
            `callback`, so that the method can be used as a decorator.

        Raises:
            TypeError: `callback` is neither callable nor `None`.
        """
        if callback is not None and not callable(callback):
            raise TypeError("callback must be callable or None")
        self._certificate_rejected_callback = callback
        return callback

    def _certificate_rejected(self, certificate: bytes, status: int) -> None:
        callback = self._certificate_rejected_callback
        if callback is None:
            return
        try:
            result = invoke_sync(callback, (certificate, o6.StatusCode(status)))
        except Exception:
            _logger.exception("Certificate rejection callback %r raised", callback)
            return
        if inspect.isawaitable(result):
            schedule_coroutine(result, self._loop, _logger)

    def _sync_notification_trampoline(self) -> None:
        def install() -> None:
            # Reads the handlers and installs under one lock, so a concurrent
            # add or remove cannot leave the trampoline off while handlers
            # exist. Runs on the loop thread, or inline while none runs the
            # loop, so the lock is never held while marshalling.
            with self._notification_sync_lock:
                self._set_notification_trampoline(any(self._notification_categories.values()))

        self._call_native(install)

    def _dispatch_notification(self, type: int, payload: Mapping[str, Any]) -> None:
        category = self._notification_categories.get(dispatch_key(type))
        if category is None:
            return
        handlers = category.snapshot()
        if not handlers:
            return
        audit_event_type: o6.NodeId | None = None
        if (type & CATEGORY_MASK) >> 32 == AUDIT_CATEGORY:
            audit_type_cls = _AUDIT_EVENT_TYPES.get(type)
            if audit_type_cls is not None:
                audit_event_type = o6.NodeId(audit_type_cls)
        notification = Notification(
            type=type,
            payload=payload,
            lifecycle=lifecycle_point(type),
            auditEventType=audit_event_type,
        )
        run_handlers(handlers, notification, self._loop, _logger)

    @property
    def mdnsConfig(self) -> MdnsConfig | None:
        """Immutable configured mDNS snapshot, or `None` when disabled."""
        return self._mdns_config

    def setMdns(self, config: MdnsConfig | None) -> None:
        """Install, replace or disable mDNS before startup.

        Enabling mDNS also enables the network table and keeps the application
        type. Disabling leaves the table enabled. Disabling is a no-op on
        builds without mDNS.

        Args:
            config: The mDNS configuration, or `None` to disable mDNS.

        Raises:
            TypeError: `config` is not `MdnsConfig` or `None`.
            RuntimeError: The server is running or still stopping.
            ValueError: Registration announcements require a discovery server.
            NotImplementedError: mDNS is unavailable.
            StatusCodeError: Native driver attachment failed.
        """
        if config is not None and not isinstance(config, MdnsConfig):
            raise TypeError("config must be MdnsConfig or None")
        if self.running or not self._is_fully_stopped:
            raise RuntimeError("mDNS configuration requires a stopped server")
        if (
            config is not None
            and config.announceRegisteredServers
            and self.config.applicationType != ns0.datatypes.ApplicationType.DISCOVERY_SERVER
        ):
            raise ValueError("announceRegisteredServers requires ApplicationType.DISCOVERY_SERVER")
        self._set_mdns(config)
        self._mdns_config = config
        self._sync_notification_trampoline()

    @classmethod
    def newFromFile(
        cls,
        file_path: str | Path,
        port: int = 4840,
        logger: logging.Logger | None = None,
        loop: asyncio.AbstractEventLoop | None = None,
        *,
        applicationUri: str | None = None,
        applicationName: str | o6.LocalizedText | None = None,
        productUri: str | None = None,
        accessControl: AccessControl | None = None,
        rbacForAnonymous: bool = False,
    ) -> "Server":
        """Create a server from a JSON5 configuration file.

        Every setting in the file is used. Everything the file leaves out gets
        the o6 default, which includes `port` and the identity arguments below.
        The security configuration comes from the file: without
        `securityPolicies` the server is unencrypted. See
        [`ServerConfig.loadFromFile`][o6.ServerConfig.loadFromFile] for the
        file format.

        ```python
        server = o6.Server.newFromFile("server.json5")
        ```

        Args:
            file_path: JSON5 configuration file.
            port: TCP port to bind when the file has no `serverUrls`.
            logger: Logger for server output. Defaults to the `o6.server` logger.
            loop: Event loop that runs the server iterations, as for `Server()`.
            applicationUri: ApplicationUri when the file sets none.
            applicationName: ApplicationName when the file sets none.
            productUri: ProductUri when the file sets none.
            accessControl: An [`AccessControl`][o6.server.AccessControl]
                subclass instance that authenticates and authorizes sessions.
            rbacForAnonymous: Deny operations on nodes without role
                permissions, as for `Server()`.

        Returns:
            The configured server. It is not listening until `start()` is called.

        Raises:
            FileNotFoundError: The file does not exist.
            ValueError: The file is not a JSON5 object.
            StatusCodeError: A setting of the file is invalid.
            PermissionError: This build has no `server` feature entitlement.
        """
        server = cls(
            port,
            logger,
            loop,
            applicationUri=applicationUri,
            applicationName=applicationName,
            productUri=productUri,
            accessControl=accessControl,
            rbacForAnonymous=rbacForAnonymous,
        )
        server.config.loadFromFile(file_path)
        return server

    @public_result
    def registerServerOnNetwork(
        self,
        serverName: str,
        discoveryUrl: str,
        serverCapabilities: Iterable[str] | None = None,
    ) -> o6.MaybeAwaitable[None]:
        """Add or replace a ServerOnNetwork record by name.

        Enable `config.serversOnNetworkEnabled` or mDNS first. A record with
        the same name is replaced, including a remotely discovered one, but not
        the entry of a registered server (`BadNotWritable`). An attached mDNS
        configuration with `announce=True` announces the record while the
        server runs, also when it was added before startup, and announces it
        again after each restart. Records added while no such configuration is
        attached are not announced.

        When `mdnsConfig.announce` is true, the URL host must be a bare hostname
        (`myhost`) or one qualified with `.local` (`myhost.local`), which is
        stored and announced as `myhost`. Listeners discover both as
        `myhost.local`. The hostname must be one label of up to 63 letters,
        digits and hyphens, so IP addresses and multi-label names such as
        `plc.example.com` or `a.b.local` are rejected. Without announcing mDNS,
        the URL is stored unchanged.

        Args:
            serverName: Record name. Must be unique across publishers.
            discoveryUrl: Discovery URL of the server.
            serverCapabilities: Capability identifiers of the server.

        Returns:
            `None`, or an awaitable of it for an async caller.

        Raises:
            TypeError: An argument is not a string or an iterable of strings.
            ValueError: mDNS announces records and the URL host is not a
                hostname it can announce.
            StatusCodeError: open62541 rejected the record.
        """
        if not isinstance(serverName, str) or not isinstance(discoveryUrl, str):
            raise TypeError("serverName and discoveryUrl must be strings")
        if isinstance(serverCapabilities, (str, bytes)):
            raise TypeError("serverCapabilities must be an iterable of strings")
        capabilities = list(serverCapabilities) if serverCapabilities is not None else []
        if any(not isinstance(value, str) for value in capabilities):
            raise TypeError("serverCapabilities must contain strings")
        mdns = self._mdns_config
        if mdns is not None and mdns.announce:
            discoveryUrl = _announced_url(discoveryUrl)
        record = ns0.datatypes.ServerOnNetwork(
            serverName=serverName, discoveryUrl=discoveryUrl, serverCapabilities=capabilities
        )
        return self._run_on_loop(
            lambda: super(Server, self)._register_server_on_network(record), sync_result=True
        )

    @public_result
    def deregisterServerOnNetwork(self, serverName: str) -> o6.MaybeAwaitable[None]:
        """Remove a ServerOnNetwork record by name.

        An unknown name is not an error.

        Args:
            serverName: Name of the record.

        Returns:
            `None`, or an awaitable of it for an async caller.

        Raises:
            TypeError: `serverName` is not a string.
            StatusCodeError: open62541 failed to remove the record.
        """
        if not isinstance(serverName, str):
            raise TypeError("serverName must be a string")
        return self._run_on_loop(
            lambda: super(Server, self)._deregister_server_on_network(serverName), sync_result=True
        )

    # -- Lifecycle -----------------------------------------------------------

    def start(self) -> None:
        """Start the server networking layer.

        A synchronous caller blocks until the listeners are ready, and a
        background thread drives I/O. On the server's running loop, `start()`
        returns at once: await `waitReady()` afterwards, or use
        `async with server`. Listener creation failures are raised by the
        readiness wait.
        """
        if (
            self._shutdown_thread is not None
            and self._shutdown_thread is not threading.current_thread()
        ):
            self._shutdown_thread.join(timeout=10.0)
        if self._shutdown_task is not None and self._worker is not None:
            if not self._shutdown_task.done() or self._worker.on_loop_thread:
                raise RuntimeError("Server shutdown is still in progress")
        self._configuration_locked = True
        _register_live_server(self)
        try:
            caller_loop = asyncio.get_running_loop()
        except RuntimeError:
            caller_loop = None

        def begin():
            if not self.running:
                if self._shutdown_task is not None and not self._shutdown_task.done():
                    raise RuntimeError("Server shutdown is still in progress")
                self._shutdown_task = None
                self._register_pending_history()
                self._listener_startup = asyncio.gather(*self._run_startup())

        if caller_loop is self._loop:
            try:
                begin()
            except BaseException:
                _unregister_live_server(self)
                self._configuration_locked = not self._is_fully_stopped
                raise
            return

        async def start_and_wait():
            begin()
            await self.waitReady()

        started_worker = False
        pending = None
        try:
            # Threads that use the idle loop inline check for the worker under
            # the same lock, so none of them runs the loop once it exists.
            with _idle_loop(self._loop).lock:
                if not self._loop.is_running():
                    worker = _WorkerLoop(self._loop)
                    worker.start()
                    # Published running, so that callers never see it stopped
                    self._worker = worker
                    started_worker = True
            pending = asyncio.run_coroutine_threadsafe(start_and_wait(), self._loop)
            pending.result()
        except BaseException:
            if pending is not None:
                pending.cancel()
            _unregister_live_server(self)
            if started_worker and self._worker is not None:
                self._worker.stop()
                self._worker = None
            self._configuration_locked = not self._is_fully_stopped
            raise

    async def waitReady(self) -> None:
        """Wait for a started server's listeners, raising any bind failure.

        Call on `server.loop` after `start()`. Cancelling the wait aborts
        startup and closes listeners already opened.

        Raises:
            RuntimeError: Not called on `server.loop`, the server was not
                started, or it was stopped during startup.
        """
        if asyncio.get_running_loop() is not self._loop:
            raise RuntimeError("waitReady() must run on the server's event loop")
        if self._listener_startup is None:
            raise RuntimeError("Server has not been started")
        startup = self._listener_startup
        try:
            await startup
            if startup is not self._listener_startup or not self.running:
                raise RuntimeError("Server was stopped during startup")
        except BaseException:
            if startup is self._listener_startup:
                if self.running:
                    self._run_shutdown()
                    self._stop_event_loop()
                _unregister_live_server(self)
                self._configuration_locked = not self._is_fully_stopped
            raise

    def stop(self) -> asyncio.Task[None] | None:
        """Shut down the server.

        Called on the loop of a background server, it starts the shutdown and
        returns an awaitable Task. Other callers block until shutdown finishes
        and get `None`. The worker stops after the shutdown task completes.

        With `config.shutdownDelay > 0` a background server keeps serving for
        that long first, reporting `ServerStatus/State` as Shutdown with
        `SecondsTillShutdown` counting down, so connected clients can notice.
        """
        _unregister_live_server(self)
        # Time the shutdown may take on top of the delay served first
        delay_s = self.config.shutdownDelay / 1000.0 if self.running else 0.0
        if (
            self._shutdown_thread is not None
            and self._shutdown_thread is not threading.current_thread()
        ):
            self._shutdown_thread.join(timeout=10.0 + delay_s)
        worker = self._worker
        if worker is not None and worker.running:
            worker_thread = worker._thread

            def begin_shutdown() -> asyncio.Task[None]:
                if self._shutdown_task is None:
                    self._shutdown_task = self._loop.create_task(self._shutdown_and_drain())
                return self._shutdown_task

            def retire_worker() -> None:
                # WorkerLoop.stop clears its thread handle even when called
                # on that thread. Retain it so external callers can join it.
                self._shutdown_thread = worker_thread
                worker.stop()
                if worker_thread is not None and worker_thread is not threading.current_thread():
                    worker_thread.join(timeout=10.0)
                if self._worker is worker:
                    self._worker = None
                self._configuration_locked = not self._is_fully_stopped

            if worker.on_loop_thread:
                if self._shutdown_task is not None and not self._shutdown_task.done():
                    return self._shutdown_task
                task = begin_shutdown()

                def finished(task: asyncio.Task[None]) -> None:
                    if not task.cancelled() and task.exception() is not None:
                        _logger.error("Server shutdown failed", exc_info=task.exception())
                    # Let callbacks awaiting this task resume before retiring
                    # the loop that drives them.
                    self._loop.call_soon(retire_worker)

                task.add_done_callback(finished)
                return task

            completed: concurrent.futures.Future[None] = concurrent.futures.Future()

            def attach() -> None:
                # A plain callback, so nothing is left unawaited if the loop
                # stops before it runs.
                def settle(task: asyncio.Task[None]) -> None:
                    if task.cancelled():
                        completed.cancel()
                    elif task.exception() is not None:
                        completed.set_exception(task.exception())  # type: ignore[arg-type]
                    else:
                        completed.set_result(None)

                try:
                    begin_shutdown().add_done_callback(settle)
                except BaseException as exc:
                    completed.set_exception(exc)

            self._loop.call_soon_threadsafe(attach)
            self._wait_for_shutdown(completed, worker_thread, 10.0 + delay_s)
            retire_worker()
        elif self.running:

            def shut_down() -> bool:
                self._run_shutdown()
                self._stop_event_loop()
                return self._is_fully_stopped

            # On the thread of an application loop that runs elsewhere
            self._configuration_locked = not self._call_native(shut_down)
        return None

    def _wait_for_shutdown(
        self,
        completed: concurrent.futures.Future[None],
        worker_thread: threading.Thread | None,
        timeout: float,
    ) -> None:
        """Block until the shutdown task completes, for a caller off the loop thread.

        A `stop()` on the loop thread retires the worker once the task is done,
        which stops the loop. A request queued after that never runs, so the
        end of the worker thread also ends the wait.

        Raises:
            TimeoutError: The shutdown did not complete within `timeout` seconds.
            RuntimeError: The loop stopped before the shutdown completed.
        """
        deadline = time.monotonic() + timeout
        while not completed.done():
            if worker_thread is not None and not worker_thread.is_alive():
                task = self._shutdown_task
                if task is not None and task.done():
                    return
                raise RuntimeError("Server event loop stopped before the shutdown completed")
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError("Server shutdown did not complete in time")
            concurrent.futures.wait((completed,), timeout=min(_LOOP_ALIVE_POLL, remaining))
        completed.result()

    async def _shutdown_and_drain(self) -> None:
        """Shut down on the loop thread, serving `config.shutdownDelay` first."""
        if self.running:
            delay_ms = self._begin_shutdown_delay()
            if delay_ms > 0.0:
                await asyncio.sleep(delay_ms / 1000.0)
        if self.running:
            self._run_shutdown()
        for _ in range(10):
            if self._is_fully_stopped:
                break
            await asyncio.sleep(0.05)
        # Drain transport close callbacks before stopping the native
        # event loop; its cleanup still calls into asyncio transports.
        for _ in range(10):
            await asyncio.sleep(0)
        self._stop_event_loop()

    def __enter__(self) -> "Server":
        """Start the server and return it."""
        self.start()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Stop the server on leaving the block, including on an exception."""
        self.stop()

    async def __aenter__(self) -> "Server":
        """Start the server and return it."""
        self.start()
        if asyncio.get_running_loop() is self._loop:
            await self.waitReady()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Stop the server on leaving the block, including on an exception."""
        result = self.stop()
        if result is not None:
            await result

    def __del__(self) -> None:
        # Never blocks: while a thread runs the loop, teardown is scheduled on
        # it (see `o6.util._finalize_native`). The C deallocator is the fallback.
        loop = getattr(self, "_loop", None)
        if loop is None:
            return
        _unregister_live_server(self)

        def cleanup() -> None:
            try:
                if self.running:
                    self.stop()
            finally:
                self._cleanup()
                if self._owns_loop and not loop.is_closed():
                    loop.close()

        _finalize_native(
            self,
            loop,
            getattr(self, "_worker", None),
            live=lambda: self.running,
            finalize=self._finalize,
            cleanup=cleanup,
        )

    def _finalize(self) -> None:
        """Shut down and release a collected server; runs on its loop at top level."""

        def release() -> None:
            self._cleanup()
            worker, self._worker = self._worker, None
            if worker is not None:
                worker.retire(close=self._owns_loop)

        task = self._shutdown_task
        if task is not None and not task.done():
            task.add_done_callback(lambda _task: release())
        elif self.running:
            # Releases even if the task is cancelled, or destroyed by a closing loop
            released = _ScheduledFinalizer(self._loop, release, release)

            async def shut_down() -> None:
                try:
                    await self._shutdown_and_drain()
                except Exception:
                    _logger.error("Server shutdown failed", exc_info=True)
                finally:
                    released()

            # A task cancelled before its first step skips `finally`
            self._shutdown_task = self._loop.create_task(shut_down())
            self._shutdown_task.add_done_callback(lambda _task: released())
        else:
            release()

    # -- Reverse connect ------------------------------------------------------

    @public_result
    def addReverseConnect(
        self,
        url: str,
        callback: Callable[[int, int], None] | None = None,
    ) -> MaybeAwaitable[int]:
        """Register a reverse connection to a client listening at `url`.

        The server retries the connection to the client endpoint periodically.

        Args:
            url: Endpoint URL of the listening client, for example
                `opc.tcp://localhost:4841`.
            callback: Called with `(handle, state)` on every state change.

        Returns:
            A handle that can be passed to `removeReverseConnect`.
        """
        return self._run_on_loop(
            lambda: super(Server, self)._add_reverse_connect(
                url, synchronous(callback) if callback is not None else None
            ),
            sync_result=True,
        )

    @public_result
    def removeReverseConnect(self, handle: int) -> MaybeAwaitable[None]:
        """Remove a reverse connect registration.

        Args:
            handle: The handle returned by `addReverseConnect`.
        """
        return self._run_on_loop(
            lambda: super(Server, self)._remove_reverse_connect(handle), sync_result=True
        )

    # -- Add nodes (high-level) -----------------------------------------------

    def _create_node(
        self,
        add_thunk: Callable[[], Any],
        node_cls: type[_NodeT],
    ) -> MaybeAwaitable[_NodeT]:
        """Create and resolve the canonical node together on the server loop."""

        def create() -> _NodeT:
            out_id = add_thunk()
            return super(Server, self)._get_node(out_id, node_cls, self._node_backend)

        return self._run_on_loop(create, sync_result=True)

    @public_result
    def addVariable(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike,
        value: Any = None,
        *,
        nodeId: NodeIdLike | None = None,
        dataType: NodeIdLike | None = None,
        typeDefinition: NodeIdLike = o6.NodeId(ns0.vartypes.BaseDataVariableType),
        writable: bool = True,
        accessLevel: int | None = None,
        userAccessLevel: int | None = None,
        historizing: bool | History = False,
        ns: int = 1,
        parentReference: NodeIdLike = ns0.reftypes.Organizes,
    ) -> MaybeAwaitable[VariableNode]:
        """Add a Variable node to the address space.

        Args:
            name: BrowseName and DisplayName of the Variable.
            parent: Parent node, typically `server.objectsNode`.
            value: Initial value. Its DataType is inferred unless `dataType`
                is given. An empty NumPy array keeps its DataType and
                ValueRank. An empty Python sequence requires `dataType`. Empty
                values read back as flat arrays, because OPC UA Binary omits
                their dimensions. A `DataValue` sets the value from its
                `value`, and keeps its status and timestamps. With
                `dataType=o6.DataValue`, the DataValue is the value itself.
            nodeId: Requested NodeId. When omitted, the server assigns a
                numeric NodeId in its application namespace, index 1.
            dataType: DataType of the Variable. Inferred from `value` when
                omitted.
            typeDefinition: VariableType of the new node.
            writable: Whether clients may write the Variable.
            accessLevel: The AccessLevel attribute as `AccessLevelType`
                flags. Replaces the level derived from `writable`, for
                example to add `STATUS_WRITE | TIMESTAMP_WRITE` for clients
                that write DataValues with status or timestamps.
                `historizing` still adds the history bits.
            userAccessLevel: The UserAccessLevel attribute. Defaults to the
                AccessLevel. o6 servers derive UserAccessLevel from the
                AccessLevel and the session's permissions and ignore it.
            historizing: Whether to record the Variable's history, or a
                `History` configuration. On a running server the Variable is
                registered at once and a history database must be configured.
                Before startup, registration waits for `start()`, so the
                database can be configured later.
            ns: Namespace index of the BrowseName.
            parentReference: ReferenceType from the parent to the new node.
                Defaults to Organizes, as on the client.

        Returns:
            The new Variable node. In any async task (before startup, on the
            server loop or on another loop) an awaitable of it. Cancelling
            the awaitable does not roll back a completed creation.

        Raises:
            StatusCodeError: Node creation or history registration failed.
            RuntimeError: Runtime historizing was requested without a database.
            TypeError: An empty value has no usable datatype.
        """
        parent_id = o6.NodeId(parent)
        requested_id = o6.NodeId(nodeId)

        explicit_type = o6.NodeId(dataType) if dataType is not None else None
        history = _as_history(historizing)
        browse_name = o6.QualifiedName(f"{ns}:{name}")
        type_def = o6.NodeId(typeDefinition)

        def create() -> VariableNode:
            if history is not None and self.running and not self.config.historyEnabled:
                raise RuntimeError(
                    "No history database configured. Call config.setHistoryDatabase() first."
                )
            attr, initial_value, empty_shape = variable_attributes(
                name, value, dataType, writable, accessLevel, userAccessLevel
            )
            if explicit_type is not None and empty_shape is not None:
                element_type = super(Server, self)._find_data_type(explicit_type)
                if not isinstance(element_type, type):
                    raise TypeError(f"No registered Python datatype for {explicit_type}")
            access = attr.accessLevel
            if history is not None:
                access |= int(
                    ns0.datatypes.AccessLevelType.HISTORY_READ
                    | ns0.datatypes.AccessLevelType.HISTORY_WRITE
                )
                attr.historizing = True
            attr.accessLevel = access
            attr.userAccessLevel = access if userAccessLevel is None else int(userAccessLevel)
            envelope = initial_value if is_value_envelope(initial_value, dataType) else None
            # Local array initialization writes the value after attaching the node.
            if isinstance(envelope.value if envelope is not None else initial_value, np.ndarray):
                attr.value = None

            out_id = self._add_variable_node(
                requested_id,
                parent_id,
                o6.NodeId(parentReference),
                browse_name,
                type_def,
                attr,
            )
            try:
                if envelope is not None:
                    # Local DataValue conversion retains empty-array dimensions,
                    # so its status and timestamps can be written with the value.
                    written = super(Server, self)._write_data_value(
                        out_id, envelope, None, int(o6.AttributeId.VALUE)
                    )
                    if written.done():
                        written.result()
                elif initial_value is not None and empty_shape is None:
                    written = super(Server, self)._write_value(out_id, initial_value)
                    if written.done():
                        written.result()
                node_type = self._variable_instance_type(type_def)
                node = super(Server, self)._get_node(out_id, node_type, self._node_backend)
                if history is not None and self.running:
                    self._register_history(out_id, history)
            except BaseException as exc:
                try:
                    super(Server, self)._delete_node(out_id, True).check()
                except Exception as rollback_error:
                    exc.add_note(f"Could not remove the incomplete variable: {rollback_error}")
                raise
            if history is not None and not self.running:
                self._pending_history.append((out_id, history))
            return node

        return self._run_on_loop(create, sync_result=True)

    def historize(
        self,
        target: NodeIdLike,
        *,
        capacity: int | None = 0,
        strategy: str = "on-write",
        interval: float = 1.0,
    ) -> MaybeAwaitable[None]:
        """Record the history of an existing Variable.

        Use it for Variables not created with `addVariable(historizing=...)`,
        such as nodes loaded from a nodeset, declared instances or nodes a
        client added. It sets the `Historizing` attribute and the history
        access bits, and registers the node.

        Takes effect immediately and requires a configured history database.
        Await it from async code. Synchronous callers block until it
        completes. If registration fails, the node attributes are restored.

        ```python
        server.config.setHistoryDatabase(capacity=5000)
        server.historize("ns=1;s=Level")
        server.historize(sensorNode, strategy="poll", interval=0.2)
        ```

        Args:
            target: The Variable to historize.
            capacity: Samples kept for this node; 0 takes the database default,
                `None` grows the store instead of evicting.
            strategy: `"on-write"`, `"poll"`, or `"manual"` (explicit insertion).
            interval: Seconds between samples, for `"poll"` only.

        Raises:
            RuntimeError: No history database is configured.
            ValueError: The strategy or the interval is not usable.
            StatusCodeError: The node's store could not be allocated.
        """
        config = History(capacity=capacity, strategy=strategy, interval=interval)
        return self._run_on_loop(partial(self._change_history, o6.NodeId(target), config))

    def unhistorize(self, target: NodeIdLike) -> MaybeAwaitable[None]:
        """Stop recording a Variable's history and release its store.

        Clears the `Historizing` attribute and the history access bits, drops
        the registration and frees the samples. Registering the node again
        starts from an empty store. Await it from async code. Synchronous
        callers block until it completes.

        ```python
        server.unhistorize("ns=1;s=Level")
        ```

        Args:
            target: The Variable to stop historizing.

        Raises:
            RuntimeError: No history database is configured.
            StatusCodeError: The node does not exist.
        """
        return self._run_on_loop(partial(self._change_history, o6.NodeId(target), None))

    async def _change_history(self, node_id: o6.NodeId, config: History | None) -> None:
        """Change attributes and native registration together on the server loop."""
        if not self.config.historyEnabled:
            raise RuntimeError(
                "No history database configured. Call config.setHistoryDatabase() first."
            )
        historizing = await self.read(node_id, attr=o6.AttributeId.HISTORIZING)
        access = int(await self.read(node_id, attr=o6.AttributeId.ACCESS_LEVEL))
        history_bits = int(ns0.datatypes.AccessLevelType.HISTORY_READ) | int(
            ns0.datatypes.AccessLevelType.HISTORY_WRITE
        )
        new_access = access | history_bits if config is not None else access & ~history_bits

        async def attributes(enabled: bool, level: int) -> None:
            (await self.write(node_id, enabled, attr=o6.AttributeId.HISTORIZING)).check()
            (await self.write(node_id, o6.Byte(level), attr=o6.AttributeId.ACCESS_LEVEL)).check()

        try:
            await attributes(config is not None, new_access)
            if config is not None:
                self._register_history(node_id, config)
            else:
                try:
                    self._history_remove(node_id)
                except o6.StatusCodeError as exc:
                    if exc.symbol != "BadNodeIdUnknown":
                        raise
        except BaseException as exc:
            try:
                await attributes(historizing, access)
            except Exception as rollback_error:
                exc.add_note(f"Could not restore history attributes: {rollback_error}")
            raise
        if config is None:
            self._pending_history = [
                entry for entry in self._pending_history if entry[0] != node_id
            ]

    def _register_history(self, node_id: o6.NodeId, config: History) -> None:
        try:
            self._history_add(
                node_id,
                capacity=config.capacity,
                strategy=config.strategy,
                interval=config.interval,
            )
        except o6.StatusCodeError as exc:
            if exc.symbol != "BadNodeIdExists":
                raise

    def _register_pending_history(self) -> None:
        """Register everything `historizing=` collected during construction."""
        if not self._pending_history:
            return
        if not self.config.historyEnabled:
            raise RuntimeError(
                "No history database configured. Call config.setHistoryDatabase() first."
            )
        while self._pending_history:
            node_id, config = self._pending_history[0]
            self._register_history(node_id, config)
            del self._pending_history[0]

    @public_result
    def addObject(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike,
        *,
        nodeId: NodeIdLike | None = None,
        typeDefinition: NodeIdLike = o6.NodeId(ns0.objtypes.BaseObjectType),
        ns: int = 1,
        parentReference: NodeIdLike = ns0.reftypes.Organizes,
    ) -> MaybeAwaitable[ObjectNode]:
        """Add an Object node to the address space.

        Args:
            name: BrowseName and DisplayName of the Object.
            parent: Parent node.
            nodeId: Requested NodeId. When omitted, the server assigns a
                numeric NodeId in its application namespace, index 1.
            typeDefinition: ObjectType of the new node. Defaults to
                `BaseObjectType` (`i=58`).
            ns: Namespace index for the BrowseName.
            parentReference: ReferenceType from the parent to the new node.
                Defaults to Organizes, as on the client.

        Returns:
            The new Object node. In any async task (before startup, on the
            server loop or on another loop) an awaitable of it. Cancelling
            the awaitable does not roll back a completed creation.

        Raises:
            StatusCodeError: The AddNodes call failed.
        """
        parent_id = o6.NodeId(parent)
        requested_id = o6.NodeId(nodeId)
        type_def = o6.NodeId(typeDefinition)

        attr = ns0.datatypes.ObjectAttributes()
        attr.displayName = o6.LocalizedText(name)

        browse_name = o6.QualifiedName(f"{ns}:{name}")

        return self._create_node(
            lambda: self._add_object_node(
                requested_id,
                parent_id,
                o6.NodeId(parentReference),
                browse_name,
                type_def,
                attr,
            ),
            ObjectNode,
        )

    @public_result
    def addObjectType(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike = o6.NodeId(ns0.objtypes.BaseObjectType),
        *,
        nodeId: NodeIdLike | None = None,
        ns: int = 1,
    ) -> MaybeAwaitable[ObjectTypeNode]:
        """Add an ObjectType node to the address space.

        Args:
            name: BrowseName and DisplayName of the ObjectType.
            parent: The `HasSubtype` parent. Defaults to `BaseObjectType`
                (`i=58`).
            nodeId: Requested NodeId. When omitted, the server assigns a
                numeric NodeId in its application namespace, index 1.
            ns: Namespace index for the BrowseName.

        Returns:
            The new ObjectType node. In any async task (before startup, on the
            server loop or on another loop) an awaitable of it. Cancelling
            the awaitable does not roll back a completed creation.

        Raises:
            StatusCodeError: The AddNodes call failed.
        """
        parent_id = o6.NodeId(parent)
        requested_id = o6.NodeId(nodeId)

        attr = ns0.datatypes.ObjectTypeAttributes()
        attr.displayName = o6.LocalizedText(name)

        browse_name = o6.QualifiedName(f"{ns}:{name}")

        return self._create_node(
            lambda: self._add_object_type_node(
                requested_id,
                parent_id,
                o6.NodeId(ns0.reftypes.HasSubtype),
                browse_name,
                attr,
            ),
            ObjectTypeNode,
        )

    @public_result
    def addVariableType(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike = o6.NodeId(ns0.vartypes.BaseVariableType),
        *,
        dataType: NodeIdLike = o6.NodeId(o6.Double),
        valueRank: int = -1,
        nodeId: NodeIdLike | None = None,
        ns: int = 1,
    ) -> MaybeAwaitable[VariableTypeNode]:
        """Add a VariableType node to the address space.

        Args:
            name: BrowseName and DisplayName of the VariableType.
            parent: The `HasSubtype` parent. Defaults to `BaseVariableType`
                (`i=62`).
            dataType: DataType of the value. Defaults to `Double` (`i=11`).
            valueRank: ValueRank of the value. Defaults to `-1`, a scalar.
            nodeId: Requested NodeId. When omitted, the server assigns a
                numeric NodeId in its application namespace, index 1.
            ns: Namespace index for the BrowseName.

        Returns:
            The new VariableType node. In any async task (before startup, on the
            server loop or on another loop) an awaitable of it. Cancelling
            the awaitable does not roll back a completed creation.

        Raises:
            StatusCodeError: The AddNodes call failed.
        """
        parent_id = o6.NodeId(parent)
        requested_id = o6.NodeId(nodeId)
        dt_id = o6.NodeId(dataType)

        attr = ns0.datatypes.VariableTypeAttributes()
        attr.displayName = o6.LocalizedText(name)
        attr.dataType = dt_id
        attr.valueRank = valueRank

        browse_name = o6.QualifiedName(f"{ns}:{name}")

        return self._create_node(
            lambda: self._add_variable_type_node(
                requested_id,
                parent_id,
                o6.NodeId(ns0.reftypes.HasSubtype),
                browse_name,
                dt_id,
                attr,
            ),
            VariableTypeNode,
        )

    @public_result
    def addReferenceType(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike = ns0.reftypes.NonHierarchicalReferences,
        *,
        inverseName: LocalizedTextLike | None = None,
        symmetric: bool = False,
        abstract: bool = False,
        nodeId: NodeIdLike | None = None,
        ns: int = 1,
    ) -> MaybeAwaitable[ReferenceTypeNode]:
        """Add a ReferenceType node to the address space.

        Args:
            name: DisplayName of the node, also used as its BrowseName.
            parent: The `HasSubtype` parent. Defaults to
                `NonHierarchicalReferences`.
            inverseName: InverseName attribute, the name of the inverse
                direction. OPC UA requires it for a non-symmetric, non-abstract
                ReferenceType.
            symmetric: Make the reference symmetric. A symmetric reference
                reads the same in both directions and needs no InverseName.
            abstract: Make the ReferenceType abstract. Only its subtypes can
                be used in references.
            nodeId: NodeId of the node. When omitted, the server assigns a
                numeric NodeId in its application namespace, index 1.
            ns: Namespace index for the BrowseName.

        Returns:
            The new ReferenceType node. In any async task (before startup, on the
            server loop or on another loop) an awaitable of it. Cancelling
            the awaitable does not roll back a completed creation.

        Raises:
            StatusCodeError: The AddNodes call failed, for example because the
                NodeId is taken or the parent does not exist.
        """
        parent_id = o6.NodeId(parent)
        requested_id = o6.NodeId(nodeId)

        attr = ns0.datatypes.ReferenceTypeAttributes()
        attr.displayName = o6.LocalizedText(name)
        attr.isAbstract = abstract
        attr.symmetric = symmetric
        if inverseName is not None:
            attr.inverseName = o6.LocalizedText(inverseName)

        browse_name = o6.QualifiedName(f"{ns}:{name}")

        return self._create_node(
            lambda: self._add_reference_type_node(
                requested_id,
                parent_id,
                o6.NodeId(ns0.reftypes.HasSubtype),
                browse_name,
                attr,
            ),
            ReferenceTypeNode,
        )

    @public_result
    def addView(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike = ns0.instances.views,
        *,
        eventNotifier: int = 0,
        containsNoLoops: bool = True,
        nodeId: NodeIdLike | None = None,
        ns: int = 1,
    ) -> MaybeAwaitable[ViewNode]:
        """Add a View node to the address space.

        The View starts empty. Add its members with `addReference`. To declare
        a View, use [`o6.view`][o6.view].

        Args:
            name: DisplayName of the node, also used as its BrowseName.
            parent: Node that organizes the View. Defaults to the standard
                ViewsFolder.
            eventNotifier: EventNotifier attribute of the node.
            containsNoLoops: ContainsNoLoops attribute. `True` asserts that
                browsing the View never revisits a node.
            nodeId: NodeId of the node. When omitted, the server assigns a
                numeric NodeId in its application namespace, index 1.
            ns: Namespace index for the BrowseName.

        Returns:
            The new View node. In any async task (before startup, on the
            server loop or on another loop) an awaitable of it. Cancelling
            the awaitable does not roll back a completed creation.

        Raises:
            StatusCodeError: The AddNodes call failed.
        """
        parent_id = o6.NodeId(parent)
        requested_id = o6.NodeId(nodeId)

        attr = ns0.datatypes.ViewAttributes()
        attr.displayName = o6.LocalizedText(name)
        attr.eventNotifier = eventNotifier
        attr.containsNoLoops = containsNoLoops

        browse_name = o6.QualifiedName(f"{ns}:{name}")

        return self._create_node(
            lambda: self._add_view_node(
                requested_id,
                parent_id,
                o6.NodeId(ns0.reftypes.Organizes),
                browse_name,
                attr,
            ),
            ViewNode,
        )

    @public_result
    def addMethod(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike,
        callback: MethodCallback,
        *,
        inputArgs: list[ns0.datatypes.Argument] | None = None,
        outputArgs: list[ns0.datatypes.Argument] | None = None,
        nodeId: o6.NodeId | None = None,
        ns: int = 1,
    ) -> MaybeAwaitable[MethodNode]:
        """Add a Method node to the address space.

        Args:
            name: BrowseName and DisplayName of the Method.
            parent: Parent node, typically an Object.
            callback: Called when a client invokes the Method. See
                [`MethodCallback`][o6.server.MethodCallback] for the signature.
            inputArgs: InputArguments descriptors.
            outputArgs: OutputArguments descriptors.
            nodeId: Requested NodeId. When omitted, the server assigns a
                numeric NodeId in its application namespace, index 1.
            ns: Namespace index for the BrowseName.

        Returns:
            The unbound Method node. Call it with `object=parent`, or reach it
            as an attribute of the parent Object for a bound call. In any
            async task (before startup, on the server loop or on another loop)
            an awaitable of it. Cancelling the awaitable does not roll back a
            completed creation.

        Raises:
            StatusCodeError: The AddNodes call failed.
        """
        parent_id = o6.NodeId(parent)
        requested_id = o6.NodeId(nodeId)

        attr = ns0.datatypes.MethodAttributes()
        attr.displayName = o6.LocalizedText(name)
        attr.executable = True
        attr.userExecutable = True

        browse_name = o6.QualifiedName(f"{ns}:{name}")

        def create() -> MethodNode:
            out_id = self._add_method_node(
                requested_id,
                parent_id,
                o6.NodeId(ns0.reftypes.HasComponent),
                browse_name,
                attr,
                inputArgs if inputArgs is not None else [],
                outputArgs if outputArgs is not None else [],
                o6.NodeId(),
                o6.NodeId(),
            )
            node = super(Server, self)._get_node(out_id, MethodNode, self._node_backend)
            parent_node = _server_node(self, parent_id, ObjectNode)
            node._construction_owner = parent_node
            self.implement(node, call=callback)
            return node

        return self._run_on_loop(create, sync_result=True)

    def _callback_target(
        self, target: MethodNode | VariableNode | VariableTypeNode | NodeIdLike | type
    ) -> Node:
        """Return the concrete server node addressed by a callback API target."""
        bound_method = getattr(target, "_method", None)
        if isinstance(target, MethodNode) and isinstance(bound_method, MethodNode):
            target = bound_method
        type_declaration = (
            vars(target).get("__o6_declaration__") if isinstance(target, type) else None
        )
        if isinstance(type_declaration, TypeDeclaration) and isinstance(
            type_declaration.attributes, VariableTypeSpec
        ):
            target_id = type_declaration.nodeid
            target_node: Node = cast(Node, _server_node(self, target_id, VariableTypeNode))
        elif isinstance(target, Node):
            target_id = o6.NodeId(target)
            target_node = target
        else:
            target_id = o6.NodeId(target)
            node_class = self._run_on_loop(
                lambda: super(Server, self)._read_attribute(
                    target_id, int(o6.AttributeId.NODE_CLASS)
                ),
                sync_result=True,
                wait=True,
            )
            return _server_node(
                self,
                target_id,
                _nodeclass2type(ns0.datatypes.NodeClass(node_class)),
            )
        return target_node

    def _implement_callbacks(
        self,
        target: MethodNode | VariableNode | VariableTypeNode | NodeIdLike | type,
        *,
        call: Callable[..., Any] | None | object = _CALLBACK_UNSET,
        read: VariableReadCallback | None | object = _CALLBACK_UNSET,
        write: VariableWriteCallback | None | object = _CALLBACK_UNSET,
    ) -> None:
        """Replace individual callback slots on an existing node."""
        target_node = self._callback_target(target)
        target_id = o6.NodeId(target_node)

        if isinstance(target_node, (VariableNode, VariableTypeNode)):
            if call is not _CALLBACK_UNSET:
                raise TypeError("Variable callbacks use read= and write= keyword arguments")
            if read is _CALLBACK_UNSET and write is _CALLBACK_UNSET:
                raise TypeError("implement requires read= or write= for a Variable")
            for kind, value in (("read", read), ("write", write)):
                if value is _CALLBACK_UNSET or value is None:
                    continue
                if not callable(value):
                    raise TypeError(f"Variable {kind} callback must be callable or None")
            current_read = self._node_callback(target_node, "read")
            current_write = self._node_callback(target_node, "write")
            proposed_read = (
                current_read if read is _CALLBACK_UNSET else cast(Callable[..., Any] | None, read)
            )
            proposed_write = (
                current_write
                if write is _CALLBACK_UNSET
                else cast(Callable[..., Any] | None, write)
            )
            if isinstance(target_node, VariableTypeNode):
                _server_types._variable_callbacks(
                    self,
                    target_id,
                    override_node=target_node,
                    override_read=proposed_read,
                    override_write=proposed_write,
                )
            elif proposed_write is not None and proposed_read is None:
                raise TypeError("a callback-backed Variable requires a read callback")
            updates = [
                (kind, value)
                for kind, value in (("read", read), ("write", write))
                if value is not _CALLBACK_UNSET
            ]
            if proposed_read is None:
                updates.reverse()
            for update_kind, value in updates:
                self._set_node_callback(
                    target_node, update_kind, cast(Callable[..., Any] | None, value)
                )
            return

        if not isinstance(target_node, MethodNode):
            raise TypeError("callbacks can only be bound to Method, Variable or VariableType nodes")
        if read is not _CALLBACK_UNSET or write is not _CALLBACK_UNSET:
            raise TypeError("Method callbacks do not take read= or write=")
        if call is _CALLBACK_UNSET:
            raise TypeError("implement requires call= for a Method")
        if call is not None and not callable(call):
            raise TypeError("Method callback must be callable or None")
        self._set_node_callback(target_node, "call", cast(Callable[..., Any] | None, call))

    def _set_node_callback(
        self,
        target: Node,
        kind: _CallbackKind,
        callback: Callable[..., Any] | None,
        receiver: Node | None = None,
    ) -> None:
        self._run_on_loop(
            lambda: super(Server, self)._set_callback_slot(
                target, _NATIVE_CALLBACK_KIND[kind], callback, receiver
            ),
            sync_result=True,
            wait=True,
        )

    def _node_callback(self, target: Node, kind: _CallbackKind) -> Callable[..., Any] | None:
        callback = self._run_on_loop(
            lambda: super(Server, self)._get_callback(target, _NATIVE_CALLBACK_KIND[kind]),
            sync_result=True,
            wait=True,
        )
        return cast(Callable[..., Any] | None, callback)

    @synchronous
    def _python_node_lifecycle(
        self,
        node_id: o6.NodeIdLike,
        type_id: o6.NodeIdLike,
        native_node: Node | None,
        node_class: int,
        early: bool,
    ) -> None:
        _server_construction._python_node_lifecycle(
            self, node_id, type_id, native_node, node_class, early
        )

    # -- References / deletion ------------------------------------------------

    @public_result
    def addReferenceLegacy(
        self,
        source: NodeIdLike,
        target: NodeIdLike | o6.ExpandedNodeId,
        referenceType: NodeIdLike,
        *,
        forward: bool = True,
    ) -> MaybeAwaitable[None]:
        """Add a reference, given as `(source, target, referenceType)`.

        Args:
            source: Source NodeId.
            target: Target NodeId or ExpandedNodeId.
            referenceType: ReferenceType NodeId.
            forward: Whether the reference is forward.

        Returns:
            `None`, or an awaitable of it in an async task.

        Raises:
            StatusCodeError: The reference could not be added.
        """
        src_id, ref_id = o6.NodeId(source), o6.NodeId(referenceType)
        tgt_id = (
            target
            if isinstance(target, o6.ExpandedNodeId)
            else o6.ExpandedNodeId(o6.NodeId(target))
        )

        def add() -> None:
            super(Server, self)._add_reference(src_id, ref_id, tgt_id, forward).check()

        return self._run_on_loop(add, sync_result=True)

    @public_result
    def deleteReferenceLegacy(
        self,
        source: NodeIdLike,
        target: NodeIdLike | o6.ExpandedNodeId,
        referenceType: NodeIdLike,
        *,
        forward: bool = True,
        bidirectional: bool = True,
    ) -> MaybeAwaitable[None]:
        """Delete a reference, given as `(source, target, referenceType)`.

        Args:
            source: Source NodeId.
            target: Target NodeId or ExpandedNodeId.
            referenceType: ReferenceType NodeId.
            forward: Whether to delete the forward reference.
            bidirectional: Whether to also delete the inverse reference.

        Returns:
            `None`, or an awaitable of it in an async task.

        Raises:
            StatusCodeError: The reference could not be deleted.
        """
        src_id, ref_id = o6.NodeId(source), o6.NodeId(referenceType)
        tgt_id = (
            target
            if isinstance(target, o6.ExpandedNodeId)
            else o6.ExpandedNodeId(o6.NodeId(target))
        )

        def delete() -> None:
            super(Server, self)._delete_reference(
                src_id, ref_id, tgt_id, forward, bidirectional
            ).check()

        return self._run_on_loop(delete, sync_result=True)

    @public_result
    def addReference(
        self,
        source: NodeIdLike,
        reftype: NodeIdLike,
        target: NodeIdLike | o6.ExpandedNodeId,
        forward: bool = True,
        targetNodeClass: ns0.datatypes.NodeClass = ns0.datatypes.NodeClass.UNSPECIFIED,
        targetServerUri: str = "",
    ) -> MaybeAwaitable[o6.StatusCode]:
        """Add a reference with administrative privileges.

        Args:
            source: Source NodeId.
            reftype: ReferenceType NodeId.
            target: Target NodeId, or an ExpandedNodeId for a remote node.
            forward: Whether to create a forward reference.
            targetNodeClass: Only `UNSPECIFIED` is supported. Other values
                return `BAD_NOT_SUPPORTED`.
            targetServerUri: A nonempty URI returns `BAD_NOT_IMPLEMENTED`.
                Identify a remote node with an ExpandedNodeId `target`.

        Returns:
            The StatusCode, or an awaitable of it. A rejected reference,
            including a duplicate local one, returns a bad status.

        Raises:
            TypeError: An argument has an invalid Python type.
            ValueError: An argument cannot be converted to a NodeId or enum.
        """
        src_id = o6.NodeId(source)
        ref_id = o6.NodeId(reftype)
        tgt_id = (
            target
            if isinstance(target, o6.ExpandedNodeId)
            else o6.ExpandedNodeId(o6.NodeId(target))
        )
        node_class = ns0.datatypes.NodeClass(targetNodeClass)
        if not isinstance(targetServerUri, str):
            raise TypeError("targetServerUri must be a string")

        async def add() -> o6.StatusCode:
            if targetServerUri:
                return o6.StatusCode.BAD_NOT_IMPLEMENTED
            if node_class != ns0.datatypes.NodeClass.UNSPECIFIED:
                return o6.StatusCode.BAD_NOT_SUPPORTED
            return super(Server, self)._add_reference(src_id, ref_id, tgt_id, forward)

        return self._run_on_loop(add)

    def _add_reference_once(
        self,
        source: NodeIdLike,
        target: NodeIdLike,
        reference_type: NodeIdLike,
        *,
        forward: bool = True,
    ) -> None:
        """Add an exact edge, accepting one already materialized by open62541."""

        def add() -> None:
            try:
                self.addReferenceLegacy(source, target, reference_type, forward=forward)
            except o6.StatusCodeError as exc:
                if exc.code != o6.StatusCode.BAD_DUPLICATE_REFERENCE_NOT_ALLOWED:
                    raise

        return self._run_on_loop(add, sync_result=True, wait=True)

    def deleteReference(
        self,
        source: NodeIdLike,
        reftype: NodeIdLike,
        target: NodeIdLike | o6.ExpandedNodeId,
        forward: bool = True,
        deleteBidirectional: bool = True,
    ) -> MaybeAwaitable[o6.StatusCode]:
        """Delete a reference with administrative privileges.

        Args:
            source: Source NodeId.
            reftype: ReferenceType NodeId.
            target: Target NodeId, or an ExpandedNodeId for a remote node.
            forward: Whether to delete the forward reference.
            deleteBidirectional: Whether to also delete the inverse reference.

        Returns:
            The StatusCode, or an awaitable of it. A rejected deletion returns
            a non-Good status, `UNCERTAIN_REFERENCE_NOT_DELETED` for a missing
            reference.

        Raises:
            TypeError: An argument has an invalid Python type.
            ValueError: An argument cannot be converted to a NodeId.
        """
        src_id = o6.NodeId(source)
        ref_id = o6.NodeId(reftype)
        tgt_id = (
            target
            if isinstance(target, o6.ExpandedNodeId)
            else o6.ExpandedNodeId(o6.NodeId(target))
        )

        async def delete() -> o6.StatusCode:
            return super(Server, self)._delete_reference(
                src_id, ref_id, tgt_id, forward, deleteBidirectional
            )

        return self._run_on_loop(delete)

    @overload
    def deleteNode(
        self, nodeId: list[NodeIdLike], deleteTargetReferences: bool = True
    ) -> MaybeAwaitable[list[o6.StatusCode]]: ...

    @overload
    def deleteNode(
        self, nodeId: NodeIdLike, deleteTargetReferences: bool = True
    ) -> MaybeAwaitable[o6.StatusCode]: ...

    def deleteNode(
        self,
        nodeId: NodeIdLike | list[NodeIdLike],
        deleteTargetReferences: bool = True,
    ) -> MaybeAwaitable[o6.StatusCode | list[o6.StatusCode]]:
        """Delete one or more nodes with administrative privileges.

        Args:
            nodeId: A node or NodeId, or a list of them.
            deleteTargetReferences: Remove references from remaining nodes
                to the deleted nodes. `False` leaves dangling references.

        Returns:
            One StatusCode for a single target, otherwise a list in input
            order, also for a one-element list. Every target is attempted,
            even after a failure. An empty list returns `[]`. Async callers
            must await the result.

        Raises:
            TypeError: An argument has an invalid Python type.
            ValueError: A target cannot be converted to a NodeId.

        Failures are returned as statuses. Call `status.check()` to raise
        them.
        """
        is_scalar, ids = _delete_inputs(nodeId, deleteTargetReferences)

        async def delete() -> o6.StatusCode | list[o6.StatusCode]:
            results = []
            for nid in ids:
                status = super(Server, self)._delete_node(nid, deleteTargetReferences)
                if status == o6.StatusCode.GOOD:
                    self._pending_history = [
                        entry for entry in self._pending_history if entry[0] != nid
                    ]
                results.append(status)
            return results[0] if is_scalar else results

        return self._run_on_loop(delete)

    # -- Method call ----------------------------------------------------------

    def call(  # type: ignore[override]
        self,
        objectId: NodeIdLike,
        methodId: NodeIdLike,
        inputArgs: list[Any] = [],
    ) -> MaybeAwaitable[tuple[o6.StatusCode, *tuple[Any, ...]]]:
        """Call a Method on the server with administrative privileges.

        Same result shape as `client.call()`.

        Args:
            objectId: The Object that owns the Method.
            methodId: The Method to invoke.
            inputArgs: InputArguments values, in declaration order.

        Returns:
            `(statusCode, output1, output2, ...)`, or `(statusCode,)` without
            outputs. Bad method statuses, including an invalid Method or
            invalid arguments, are returned with any available outputs.

        Raises:
            StatusCodeError: The call could not be submitted. `code` holds the
                status. Bad method results do not raise.
            TypeError: An argument cannot be converted to an OPC UA value.
        """
        obj_id = o6.NodeId(objectId)
        mth_id = o6.NodeId(methodId)
        args = [_normalize_nodeids(arg) for arg in inputArgs]

        async def _do() -> tuple[o6.StatusCode, *tuple[Any, ...]]:
            return await super(Server, self)._call(obj_id, mth_id, args, 0, True)

        return self._run_on_loop(_do)

    @public_result
    def addPublishedDataSet(
        self,
        configuration: ns0.datatypes.PublishedDataSetDataType,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Create a PublishedDataSet with its metadata and source mapping.

        Field count, DataTypes and ValueRanks must match the source Variables.
        Folder paths and event DataSets are not supported. Await it in any
        async task, including on the server loop.

        Args:
            configuration: The PublishedDataSet configuration.

        Returns:
            The NodeId of the PublishedDataSet.
        """
        return self._run_on_loop(
            lambda: super(Server, self)._add_published_dataset(_normalize_nodeids(configuration)),
            sync_result=True,
        )

    @public_result
    def addSubscribedDataSet(
        self,
        name: str,
        metadata: ns0.datatypes.DataSetMetaDataType,
        targets: ns0.datatypes.TargetVariablesDataType,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Create a standalone SubscribedDataSet under SubscribedDataSets.

        Defines the DataSet only. No DataSetReader is created or enabled.
        Await it in any async task, including on the server loop.

        Args:
            name: Name of the DataSet.
            metadata: Field metadata, in the same order and count as `targets`.
            targets: Target Variable mappings.

        Returns:
            The NodeId of the SubscribedDataSet.
        """
        return self._run_on_loop(
            lambda: super(Server, self)._add_subscribed_dataset(name, metadata, targets),
            sync_result=True,
        )

    @public_result
    def removeSubscribedDataSet(self, dataSetId: NodeIdLike) -> MaybeAwaitable[None]:
        """Remove a standalone SubscribedDataSet and its nodes."""
        node_id = o6.NodeId(dataSetId)
        return self._run_on_loop(
            lambda: super(Server, self)._remove_subscribed_dataset(node_id), sync_result=True
        )

    def _pubSubConfiguration(self, componentId: NodeIdLike):
        """Read an owned configuration snapshot; child arrays are read separately.

        Connection Enabled is configured intent. Read Status.State for its live state.
        """
        node_id = o6.NodeId(componentId)
        return self._run_on_loop(
            lambda: super(Server, self)._pubsub_configuration(node_id), sync_result=True, wait=True
        )

    def _setPubSubConnectionEnabled(self, connectionId: NodeIdLike, enabled: bool) -> None:
        """Set native PubSub connection state (internal component bridge)."""
        node_id = o6.NodeId(connectionId)
        return self._run_on_loop(
            lambda: super(Server, self)._set_pubsub_connection_enabled(node_id, enabled),
            sync_result=True,
            wait=True,
        )

    def _setPubSubComponentEnabled(self, componentId: NodeIdLike, enabled: bool) -> None:
        """Set one native PubSub component state."""
        node_id = o6.NodeId(componentId)
        return self._run_on_loop(
            lambda: super(Server, self)._set_pubsub_component_enabled(node_id, enabled),
            sync_result=True,
            wait=True,
        )

    def _removePubSubConnection(self, connectionId: NodeIdLike) -> None:
        """Remove a native PubSub connection and all child components."""
        node_id = o6.NodeId(connectionId)
        return self._run_on_loop(
            lambda: super(Server, self)._remove_pubsub_connection(node_id),
            sync_result=True,
            wait=True,
        )

    def _setAllPubSubComponentsEnabled(self, enabled: bool) -> None:
        """Enable or disable the complete native PubSub component tree."""
        return self._run_on_loop(
            lambda: super(Server, self)._set_all_pubsub_components_enabled(enabled),
            sync_result=True,
            wait=True,
        )

    # -- Read / write ---------------------------------------------------------

    def read(
        self,
        target: NodeIdLike | list[NodeIdLike],
        *,
        attr: o6.AttributeId | str = o6.AttributeId.VALUE,
        timestampsToReturn: ns0.datatypes.TimestampsToReturn | None = None,
        valueOnly: bool = True,
        range: o6.IndexRange | list[o6.IndexRange] = None,
    ) -> MaybeAwaitable[Any]:
        """Read one attribute from a node or a list of nodes.

        Reads run with administrative privileges.

        Args:
            target: A NodeId-like value or Node, or a list of them.
            attr: AttributeId or attribute name, matched case-insensitively.
            timestampsToReturn: `SOURCE` (default when `None`), `SERVER`,
                `BOTH` or `NEITHER`.
            valueOnly: `True` returns the value for any Good-severity status
                and drops status and timestamps. `False` returns DataValues,
                including Uncertain and Bad ones.
            range: OPC UA range string (inclusive), a slice or tuple of slices
                (stop-exclusive), or a list with one range per target. A single
                range applies to every target. `None` or `""` reads the whole
                attribute. A nonempty range on an attribute other than Value
                gives `BAD_INDEX_RANGE_NO_DATA`.

        Returns:
            A result for one target, or a list in input order. An empty list
            returns `[]`. DataValues keep the per-target status and supported
            timestamps, also for failed reads.

        Raises:
            o6.StatusCodeError: The service failed, or a `valueOnly` read got an
                Uncertain or Bad status. `code` holds the status. For a list,
                an exception note names the failed index.
            TypeError: An argument has an unsupported Python type.
            ValueError: An attribute name, slice or range-list length is
                invalid.
        """
        is_scalar, request = _read_request(target, attr, timestampsToReturn, valueOnly, range)

        async def _read() -> Any:
            results = [
                await super(Server, self)._read_data_value(item, int(request.timestampsToReturn))
                for item in request.nodesToRead
            ]
            return _read_results(results, is_scalar, valueOnly)

        return self._run_on_loop(_read)

    def write(
        self,
        target: NodeIdLike | list[NodeIdLike] | Mapping[NodeIdLike, Any],
        value: Any = _WRITE_UNSET,
        *,
        attr: o6.AttributeId | str = o6.AttributeId.VALUE,
        range: o6.IndexRange | list[o6.IndexRange] = None,
    ) -> MaybeAwaitable[o6.StatusCode | list[o6.StatusCode]]:
        """Write one attribute of one node, a list of nodes or a mapping.

        Writes run with administrative privileges, one after another, without
        rollback. A payload for an attribute other than Value must have that
        attribute's DataType; it is not coerced.

        Args:
            target: A NodeId-like value or Node, a list of them, or a mapping
                from target to value.
            value: The value for one target, or a list of equal length for a
                list of targets. Omit it for a mapping. A list for a single
                target is an array value. `None` writes a null value where the
                target allows it. Omitting the value for a single target
                raises `ValueError`. A DataValue keeps its supported status and
                timestamps; for attributes other than Value they are not
                supported.
            attr: AttributeId or attribute name, matched case-insensitively.
            range: OPC UA range string (inclusive), a slice or tuple of slices
                (stop-exclusive), or a list with one range per target. A single
                range applies to every target. `None` or `""` writes the whole
                attribute. A nonempty range requires the Value attribute.
                Mappings take no range.

        Returns:
            One StatusCode for a single target, otherwise a list in input
            order, also for a one-element list. An empty list or mapping
            returns `[]`. Every target is attempted, even after a failure;
            check the statuses.

        Raises:
            o6.StatusCodeError: The service failed. `code` holds the status.
            TypeError: An argument has an unsupported Python type.
            ValueError: Input shapes, attribute names or ranges are invalid.
                They are checked before anything is written.
        """
        is_scalar, attribute, nodeids, values, ranges = _write_inputs(target, value, attr, range)

        async def _write() -> o6.StatusCode | list[o6.StatusCode]:
            results = []
            for nodeid, val, index_range in zip(nodeids, values, ranges):
                result = await super(Server, self)._write_data_value(
                    nodeid, _write_payload(val), index_range or None, int(attribute), True
                )
                results.append(o6.StatusCode(result))
            return results[0] if is_scalar else results

        return self._run_on_loop(_write)

    def translateBrowsePaths(  # type: ignore[override]
        self,
        request: Any,
    ) -> MaybeAwaitable[Any]:
        """Translate BrowsePaths to NodeIds on the server.

        Args:
            request: A `TranslateBrowsePathsToNodeIdsRequest`.

        Returns:
            The `TranslateBrowsePathsToNodeIdsResponse`."""

        async def _do() -> Any:
            r = super(Server, self)._translate_browse_paths(request)
            return (await r) if inspect.isawaitable(r) else r

        return self._run_on_loop(_do)

    def serviceTranslateBrowsePathsToNodeIds(
        self, request: ns0.datatypes.TranslateBrowsePathsToNodeIdsRequest
    ) -> MaybeAwaitable[ns0.datatypes.TranslateBrowsePathsToNodeIdsResponse]:
        """Run a raw TranslateBrowsePathsToNodeIds request.

        Matches the client service method. The response status is returned,
        not raised. `translateBrowsePaths` is an alias.
        """
        return self.translateBrowsePaths(request)

    def findDataType(  # type: ignore[override]
        self,
        nodeId: NodeIdLike,
    ) -> MaybeAwaitable[Any]:
        """Look up a DataType by NodeId and return the Python type or metadata.

        Args:
            nodeId: NodeId of the DataType.

        Returns:
            The Python type or DataType metadata."""
        nid = o6.NodeId(nodeId)

        async def _do() -> Any:
            r = super(Server, self)._find_data_type(nid)
            return (await r) if inspect.isawaitable(r) else r

        return self._run_on_loop(_do)

    # -- View Service Set Methods  ------------------------------------------------------------

    def browse(
        self,
        target: NodeIdLike,
        *,
        direction: ns0.datatypes.BrowseDirection = ns0.datatypes.BrowseDirection.FORWARD,
        reftype: NodeIdLike = ns0.reftypes.HierarchicalReferences,
        refsubtypes: bool = True,
        nodeClassMask: int = ns0.datatypes.NodeClass.UNSPECIFIED,
        resultMask: int = ns0.datatypes.BrowseResultMask.ALL,
    ) -> MaybeAwaitable[list[ns0.datatypes.ReferenceDescription]]:
        """Collect all references from one node.

        Args:
            target: The node to browse from.
            direction: `FORWARD`, `INVERSE`, or `BOTH`.
            reftype: Only follow this ReferenceType. Defaults to
                `HierarchicalReferences`.
            refsubtypes: Also follow subtypes of `reftype`.
            nodeClassMask: `NodeClass` members combined with `|`. Only nodes
                of these NodeClasses are returned. `UNSPECIFIED` returns all.
            resultMask: `BrowseResultMask` members combined with `|`, selecting
                the reference fields to fill in. Defaults to `ALL`. `NONE`
                returns only the target NodeIds.

        Returns:
            A flat list of every `ReferenceDescription`. Continuation points
            are followed until exhausted. Async tasks must await the call, on
            any loop.

        Raises:
            StatusCodeError: Browse or BrowseNext failed. Open continuation
                points are released where possible.
        """
        bd = _browse_description(target, direction, reftype, refsubtypes, nodeClassMask, resultMask)

        async def _do() -> list[ns0.datatypes.ReferenceDescription]:
            return self._browse_references(target, bd)

        return self._run_on_loop(_do)

    def browsePage(
        self,
        target: NodeIdLike,
        *,
        maxReferences: int = 0,
        direction: ns0.datatypes.BrowseDirection = ns0.datatypes.BrowseDirection.FORWARD,
        reftype: NodeIdLike = ns0.reftypes.HierarchicalReferences,
        refsubtypes: bool = True,
        nodeClassMask: int = ns0.datatypes.NodeClass.UNSPECIFIED,
        resultMask: int = ns0.datatypes.BrowseResultMask.ALL,
    ) -> MaybeAwaitable[ns0.datatypes.BrowseResult]:
        """Fetch one page of references.

        Args:
            target: The node to browse from.
            maxReferences: Maximum number of references to return. `0` means
                no limit. Any limit can leave a continuation point for
                `browseNext`.
            direction: `FORWARD`, `INVERSE`, or `BOTH`.
            reftype: Only follow this ReferenceType. Defaults to
                `HierarchicalReferences`.
            refsubtypes: Also follow subtypes of `reftype`.
            nodeClassMask: `NodeClass` members combined with `|`. Only nodes
                of these NodeClasses are returned. `UNSPECIFIED` returns all.
            resultMask: `BrowseResultMask` members combined with `|`, selecting
                the reference fields to fill in. Defaults to `ALL`. `NONE`
                returns only the target NodeIds.

        Returns:
            The `BrowseResult` with the references, and a continuation point
            if the result was truncated. Async tasks must await the call, on
            any loop.

        Raises:
            StatusCodeError: The Browse call failed.
        """
        bd = _browse_description(target, direction, reftype, refsubtypes, nodeClassMask, resultMask)

        async def _do() -> ns0.datatypes.BrowseResult:
            result = self._browse_node(target, int(maxReferences), bd)
            result.statusCode.check()
            return result

        return self._run_on_loop(_do)

    def _browse_node(
        self,
        target: NodeIdLike,
        max_references: int,
        description: ns0.datatypes.BrowseDescription,
    ) -> ns0.datatypes.BrowseResult:
        """Execute native browse immediately, including during node navigation."""
        if (
            isinstance(target, Node)
            and target._backend is self._node_backend
            and target._is_native_attached()
        ):
            return cast(
                ns0.datatypes.BrowseResult, super()._browse(max_references, description, target)
            )
        return cast(ns0.datatypes.BrowseResult, super()._browse(max_references, description))

    def _browse_references(
        self, target: NodeIdLike, description: ns0.datatypes.BrowseDescription
    ) -> list[ns0.datatypes.ReferenceDescription]:
        """Collect native pages immediately, including during node navigation."""
        collection = _BrowseCollection()
        try:
            collection.append(self._browse_node(target, 0, description))
            while collection.continuation_point:
                pages = self._browse_next(False, collection.continuation_point)
                collection.append(pages[0])
            return collection.references
        finally:
            if collection.continuation_point:
                with suppress(Exception):
                    self._browse_next(True, collection.continuation_point)

    def browseNext(
        self,
        releaseContinuationPoint: bool,
        continuationPoint: bytes | list[bytes] | tuple[bytes, ...],
    ) -> MaybeAwaitable[list[ns0.datatypes.BrowseResult]]:
        """Continue or release pages obtained from `browsePage`.

        Args:
            releaseContinuationPoint: Discard the continuation point instead of
                fetching the next batch.
            continuationPoint: One token, or a list or tuple of tokens, from
                earlier pages. Release tokens you stop paging through.

        Returns:
            A list of `BrowseResult` pages, one per token, also for a single
            token. A release returns empty pages. Async tasks must await the
            call.

        Raises:
            StatusCodeError: The BrowseNext call failed, for example because the
                continuation point expired.
        """

        async def _do() -> list[ns0.datatypes.BrowseResult]:
            pages = self._browse_next(bool(releaseContinuationPoint), continuationPoint)
            try:
                for page in pages:
                    page.statusCode.check()
            except BaseException:
                tokens = [page.continuationPoint for page in pages if page.continuationPoint]
                if tokens:
                    with suppress(Exception):
                        self._browse_next(True, tokens)
                raise
            return cast(list[ns0.datatypes.BrowseResult], pages)

        return self._run_on_loop(_do)

    def browseRecursive(
        self,
        target: NodeIdLike,
        *,
        direction: ns0.datatypes.BrowseDirection = ns0.datatypes.BrowseDirection.FORWARD,
        reftype: NodeIdLike = ns0.reftypes.HierarchicalReferences,
        refsubtypes: bool = True,
        nodeClassMask: int = ns0.datatypes.NodeClass.UNSPECIFIED,
        resultMask: int = ns0.datatypes.BrowseResultMask.NONE,
    ) -> MaybeAwaitable[Any]:
        """Browse a whole subtree in one native traversal.

        The arguments match [`browse`][o6.server.Server.browse]. Depth is
        unlimited; on a large address space, narrow it with `reftype` and
        `nodeClassMask`.

        Returns:
            Every reachable node as a flat list of `ExpandedNodeId` values.

        Raises:
            StatusCodeError: The traversal failed.
        """
        bd = _browse_description(target, direction, reftype, refsubtypes, nodeClassMask, resultMask)

        async def _do() -> Any:
            r = super(Server, self)._browse_recursive(bd)
            return (await r) if inspect.isawaitable(r) else r

        return self._run_on_loop(_do)

    @overload
    def translateBrowsePathsToNodeIds(
        self, browsePath: list[ns0.datatypes.BrowsePath]
    ) -> MaybeAwaitable[list[ns0.datatypes.BrowsePathResult]]: ...

    @overload
    def translateBrowsePathsToNodeIds(
        self, browsePath: ns0.datatypes.BrowsePath
    ) -> MaybeAwaitable[ns0.datatypes.BrowsePathResult]: ...

    def translateBrowsePathsToNodeIds(
        self, browsePath: ns0.datatypes.BrowsePath | list[ns0.datatypes.BrowsePath]
    ) -> MaybeAwaitable[ns0.datatypes.BrowsePathResult | list[ns0.datatypes.BrowsePathResult]]:
        """Resolve one BrowsePath or a list of paths.

        Args:
            browsePath: A BrowsePath or list of BrowsePaths to resolve.

        Returns:
            One BrowsePathResult for a single path, or a list in input order.
            Each result keeps its status, also for partly or not resolved
            paths. An empty list returns `[]`. Await it in async code.

        Raises:
            StatusCodeError: The service failed. For raw requests and
                responses, use `serviceTranslateBrowsePathsToNodeIds`.
        """
        return self._run_on_loop(partial(_translate_paths, self.translateBrowsePaths, browsePath))

    def browseSimplifiedBrowsePaths(
        self,
        origin: NodeIdLike,
        browsePath: (
            o6.QualifiedName
            | str
            | list[o6.QualifiedName | str]
            | tuple[o6.QualifiedName | str, ...]
        ),
    ) -> MaybeAwaitable[ns0.datatypes.BrowsePathResult]:
        """Resolve a BrowseName chain through forward hierarchical references.

        Args:
            origin: Node where the path starts.
            browsePath: One BrowseName, or a list or tuple of BrowseNames
                forming one path. Strings are accepted.

        Returns:
            One BrowsePathResult. An unresolved path keeps its status. Await it
            in async code.
        """
        return self.translateBrowsePathsToNodeIds(_simplified_browse_path(origin, browsePath))

    def forEachChildNode(  # type: ignore[override]
        self,
        nodeId: NodeIdLike,
        callback: Callable[[o6.NodeId, bool, o6.NodeId], Any],
    ) -> MaybeAwaitable[None]:
        """Visit every reference of one node without building a result list.

        Nothing is allocated per reference, so this is the cheapest way to
        walk references. The callback runs on the server's event loop while
        the node is locked. It must not block or call into the server.

        Args:
            nodeId: The node whose references are visited.
            callback: Called as `(childId, isInverse, referenceTypeId)` for each
                reference.
        """
        nid = o6.NodeId(nodeId)

        async def _do() -> None:
            r = super(Server, self)._for_each_child_node(nid, synchronous(callback))
            if inspect.isawaitable(r):
                await r

        return self._run_on_loop(_do)

    # -- Discovery Server ----------------------------------------------------------------

    @public_result
    def registerDiscovery(
        self,
        url: str,
        semaphoreFilePath: str | Path | None = None,
        *,
        securityMode: int | None = None,
        securityPolicy: str | None = None,
    ) -> MaybeAwaitable[None]:
        """Register this server at a Discovery Server (LDS).

        The server must be running. It registers its ApplicationDescription
        with the DiscoveryUrls of its listeners. The call only starts the
        registration: the answer of the LDS is logged, not returned or
        raised. Check the result with `Client.findServers()` at the LDS, and
        repeat the call to renew the registration before the LDS expires it.

        With a certificate configured on the server, the
        registration uses SignAndEncrypt with Basic256Sha256 by default. The
        LDS must trust the server certificate, and the server verifies the LDS
        certificate like a client certificate: with its `trustList`, or with
        `acceptAllCertificates`. The ApplicationUri of the certificate must be
        the application URI of the server: an LDS refuses a registration over
        a channel without a client certificate, or with one for another URI
        (`BadSecurityModeInsufficient`, `BadCertificateUriInvalid`). Without a
        certificate, the server uses SecurityPolicy#None, which such an LDS
        refuses. A registration that does not complete within the
        client timeout of 5 seconds is cancelled.

        Args:
            url: Endpoint URL of the LDS, for example
                `"opc.tcp://localhost:4840"`.
            semaphoreFilePath: Semaphore file that coordinates shutdown across
                several instances. `None` sends an empty path.
            securityMode: `o6.SecurityMode.SIGN_AND_ENCRYPT` or `NONE`.
                Defaults to `SIGN_AND_ENCRYPT` with a certificate and `NONE`
                without.
            securityPolicy: URI, `o6.SecurityPolicy` member or short name of
                the policy for `SIGN_AND_ENCRYPT`. Defaults to
                `"Basic256Sha256"`.

        Raises:
            ValueError: `securityMode` is `SIGN`, or `SIGN_AND_ENCRYPT` is
                requested without a server certificate, or the mode and the
                policy do not match.
            StatusCodeError: The registration could not be started, for
                example because the server is not running, or
                `BadTooManyOperations` if a (de)registration is still pending.
        """
        path_arg = str(semaphoreFilePath) if semaphoreFilePath is not None else None
        mode = 0 if securityMode is None else int(securityMode)
        return self._run_on_loop(
            lambda: super(Server, self)._register_discovery(url, path_arg, mode, securityPolicy),
            sync_result=True,
        )

    @public_result
    def deregisterDiscovery(
        self,
        url: str,
        *,
        securityMode: int | None = None,
        securityPolicy: str | None = None,
    ) -> MaybeAwaitable[None]:
        """Deregister this server from a Discovery Server (LDS).

        Call it once during server shutdown, with the security used for
        `registerDiscovery`. Like the registration, the call only starts the
        deregistration and logs the answer of the LDS.

        Args:
            url: The LDS endpoint URL passed to `registerDiscovery`.
            securityMode: As for `registerDiscovery`.
            securityPolicy: As for `registerDiscovery`.

        Raises:
            ValueError: As for `registerDiscovery`.
            StatusCodeError: The deregistration could not be started, or
                `BadTooManyOperations` if a (de)registration is still pending.
        """
        mode = 0 if securityMode is None else int(securityMode)
        return self._run_on_loop(
            lambda: super(Server, self)._deregister_discovery(url, mode, securityPolicy),
            sync_result=True,
        )

    def setRegisterServerCallback(
        self,
        callback: Callable[[dict], None] | None,
    ) -> None:
        """Set the callback run when another server registers with this LDS.

        The callback receives one `dict` with the keys `server_uri`,
        `product_uri`, `discovery_urls` (list of str) and
        `last_discovery_timestamp`.

        Args:
            callback: The callback, or `None` to remove it.
        """
        return self._run_on_loop(
            lambda: super(Server, self)._set_register_server_callback(
                synchronous(callback) if callable(callback) else callback
            ),
            sync_result=True,
            wait=True,
        )

    def setServerOnNetworkCallback(
        self,
        callback: Callable[[dict], None] | None,
    ) -> None:
        """Set the callback run when mDNS detects another server on the network.

        The callback receives one `dict` with the keys `record_id`,
        `server_name`, `discovery_url`, `server_capabilities` (list of str),
        `last_announce_time`, `next_announce_time`, `last_online_time`,
        `is_server_announce` (bool) and `is_txt_received` (bool).

        Args:
            callback: The callback, or `None` to remove it.

        Raises:
            NotImplementedError: Not available with the current open62541
                discovery API.
        """
        if not _HAS_SERVER_ON_NETWORK_CALLBACK:
            raise NotImplementedError(
                "server-on-network callbacks are not available with the "
                "current open62541 discovery API"
            )
        return self._run_on_loop(
            lambda: super(Server, self)._set_server_on_network_callback(
                synchronous(callback) if callback is not None else None
            ),
            sync_result=True,
            wait=True,
        )

    # -- o6.subscription.MonitoredItem Service Set ------------------------------------------------

    def createDataChangeMonitoredItem(
        self,
        nodeId: NodeIdLike,
        callback: Callable,
        *,
        timestamps: "ns0.datatypes.TimestampsToReturn | None" = None,
        context: object = None,
        samplingInterval: float = 0.0,
        monitoringMode: "ns0.datatypes.MonitoringMode | None" = None,
    ) -> MaybeAwaitable[o6.subscription.MonitoredItem]:
        """Create a local DataChange MonitoredItem on the Value of a node.

        The callback is called as
        `callback(monitoredItemId, nodeId, attributeId, data_value, context)`
        and may be a function or a coroutine function.

        The returned handle exposes the Value target, the initial mode,
        `requestedParams`, and the revised values in `params`. Local items can
        be deleted. `modify`, `setMonitoringMode` and `setTriggering` raise
        `NotImplementedError`.
        """
        mir = ns0.datatypes.MonitoredItemCreateRequest()
        mir.itemToMonitor.nodeId = o6.NodeId(nodeId)
        mir.itemToMonitor.attributeId = o6.AttributeId.VALUE
        mir.monitoringMode = (
            monitoringMode if monitoringMode is not None else ns0.datatypes.MonitoringMode.REPORTING
        )
        mir.requestedParameters.samplingInterval = samplingInterval

        ttr = timestamps if timestamps is not None else ns0.datatypes.TimestampsToReturn.SOURCE

        async def _create() -> o6.subscription.MonitoredItem:
            out = self._run_on_loop(
                lambda: super(Server, self)._create_data_change_monitored_item(
                    mir, ttr, context, synchronous(callback)
                ),
                sync_result=True,
                wait=True,
            )
            result = await out if inspect.isawaitable(out) else out
            return o6.subscription.MonitoredItem._from_server(self, mir, result)

        return self._run_on_loop(_create)

    def deleteMonitoredItem(
        self, monitoredItemId: int | o6.subscription.MonitoredItem
    ) -> MaybeAwaitable[None]:
        """Delete a local monitored item by ID or handle.

        Deleting a handle again is a no-op. Async callers must await every
        call, including a repeated one.

        Raises:
            ValueError: The handle belongs to another server.
        """
        if isinstance(monitoredItemId, o6.subscription.MonitoredItem):
            if monitoredItemId._server_ref is None or monitoredItemId._server_ref() is not self:
                raise ValueError("MonitoredItem belongs to a different server or subscription")

        async def _delete() -> None:
            if isinstance(monitoredItemId, o6.subscription.MonitoredItem):
                if monitoredItemId.id is None:
                    return
                mid = int(monitoredItemId.id)
            else:
                mid = int(monitoredItemId)
            out = self._run_on_loop(
                lambda: super(Server, self)._delete_monitored_item(mid), sync_result=True, wait=True
            )
            if inspect.isawaitable(out):
                await out
            if isinstance(monitoredItemId, o6.subscription.MonitoredItem):
                monitoredItemId._monitored_item_id = None

        return self._run_on_loop(_delete)

    def createEventMonitoredItem(
        self,
        nodeId: NodeIdLike,
        callback: Callable[[int, dict[str, Any], Any], MaybeAwaitable[None]],
        *,
        context: object = None,
        selectClauses: "list[ns0.datatypes.SimpleAttributeOperand] | None" = None,
        whereClause: "ns0.datatypes.ContentFilter | None" = None,
        eventFilter: "ns0.datatypes.EventFilter | None" = None,
        monitoringMode: "ns0.datatypes.MonitoringMode | None" = None,
        clientHandle: int = 0,
        samplingInterval: float = 0.0,
        queueSize: int = 0,
        discardOldest: bool = True,
    ) -> MaybeAwaitable[o6.subscription.MonitoredItem]:
        """Create a local Event MonitoredItem on `nodeId`.

        Pass the filter as `selectClauses=` and `whereClause=`, or as a
        complete `eventFilter=`, not both. `monitoringMode=`, `queueSize=` and
        `discardOldest=` control the local notification queue. `clientHandle=`
        is stored but does not route local callbacks. Events are pushed on
        emission, so `samplingInterval=` sets no polling period.

        The callback is called as
        `callback(monitoredItemId, event_fields, context)`. `event_fields` is
        a `dict[str, Any]` keyed by the selected event-filter paths, such as
        `"/Message"` or `"/ConditionName/Id"`.

        The returned handle exposes the EventNotifier target, the filter, the
        initial mode, `requestedParams`, and the revised values in `params`.
        Local items can be deleted. `modify`, `setMonitoringMode` and
        `setTriggering` raise `NotImplementedError`.

        Raises:
            TypeError: Both `eventFilter` and `selectClauses`/`whereClause`
                were given.
            ValueError: The filter has no select clauses. The server would
                reject it with `BadEventFilterInvalid`.
        """
        if eventFilter is not None and (selectClauses is not None or whereClause is not None):
            raise TypeError("Pass either eventFilter=, or selectClauses=/whereClause=, not both")

        if eventFilter is not None:
            resolved_filter = eventFilter
        else:
            resolved_filter = ns0.datatypes.EventFilter()
            if selectClauses is not None:
                resolved_filter.selectClauses = selectClauses
            if whereClause is not None:
                resolved_filter.whereClause = whereClause
        _require_event_select_clauses(resolved_filter)

        mir = ns0.datatypes.MonitoredItemCreateRequest()
        mir.itemToMonitor.nodeId = o6.NodeId(nodeId)
        mir.itemToMonitor.attributeId = o6.AttributeId.EVENT_NOTIFIER
        mir.monitoringMode = (
            monitoringMode if monitoringMode is not None else ns0.datatypes.MonitoringMode.REPORTING
        )
        mir.requestedParameters.clientHandle = int(clientHandle)
        mir.requestedParameters.queueSize = int(queueSize)
        mir.requestedParameters.discardOldest = bool(discardOldest)
        mir.requestedParameters.samplingInterval = samplingInterval
        mir.requestedParameters.filter = copy.deepcopy(resolved_filter)

        async def _create() -> o6.subscription.MonitoredItem:
            out = self._run_on_loop(
                lambda: super(Server, self)._create_event_monitored_item(
                    mir, context, synchronous(callback)
                ),
                sync_result=True,
                wait=True,
            )
            result = await out if inspect.isawaitable(out) else out
            return o6.subscription.MonitoredItem._from_server(self, mir, result)

        return self._run_on_loop(_create)

    # -- Server Callbacks ---------------------------------------------------------

    def addRepeatedCallback(self, callback: Callable, intervalMs: float) -> int:
        """Run `callback` every `intervalMs` milliseconds.

        Returns:
            A callback ID for `changeRepeatedCallbackInterval` and
            `removeCallback`.
        """
        return self._run_on_loop(
            lambda: super(Server, self)._add_repeated_callback(
                synchronous(callback), float(intervalMs)
            ),
            sync_result=True,
            wait=True,
        )

    def changeRepeatedCallbackInterval(self, callbackId: int, intervalMs: float) -> None:
        """Change the interval of an existing repeated callback."""
        cid = int(callbackId)
        return self._run_on_loop(
            lambda: super(Server, self)._change_repeated_callback_interval(cid, float(intervalMs)),
            sync_result=True,
            wait=True,
        )

    def removeCallback(self, callbackId: int) -> None:
        """Remove a repeated callback by ID."""
        cid = int(callbackId)
        return self._run_on_loop(
            lambda: super(Server, self)._remove_callback(cid), sync_result=True, wait=True
        )


__all__ = [
    "AccessControl",
    "Event",
    "History",
    "HistoryBackend",
    "MethodCallback",
    "NodePermissions",
    "Role",
    "Server",
    "Session",
    "SessionActivation",
    "VariableReadCallback",
    "VariableWriteCallback",
    "roles",
]


def __dir__() -> list[str]:
    return sorted(__all__)


del _NativeServer
