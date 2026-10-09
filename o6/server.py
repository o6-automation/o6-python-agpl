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
import logging
import threading
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
from o6._creation import variable_attributes
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
)
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
    _WorkerLoop,
)
from o6.util import _load_cert_or_bytes, _load_cert_list

from o6._declarations import TypeDeclaration, VariableTypeSpec, _CallbackKind
from o6._history import History, HistoryBackend, as_history as _as_history

_NodeT = TypeVar("_NodeT", bound=Node)


def _normalize_event_fields(
    fields: Mapping[o6.QualifiedName | str, Any] | None,
) -> dict[o6.QualifiedName | str, Any]:
    return {key: _normalize_nodeids(value) for key, value in (fields or {}).items()}


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

    Construct with `o6.Event(server, ...)` and trigger as often as needed.
    Construction does not access the address space or emit an event.
    As a mutable mapping of event fields, it supports `dict(event)`,
    `len(event)`, `del event[key]`, and iteration. The attributes below can be
    reassigned between triggers.

    Field keys are event-filter path strings such as `"/BatchId"`, or
    [`QualifiedName`][o6.QualifiedName] values when a namespace matters.

    When `eventType` is `None`, each `trigger()` resolves it from
    `eventInstance`'s type if supplied, otherwise from `source`'s declared
    `GeneratesEvent` target. The draft itself keeps `eventType=None`.

    See [Events](manual/server/events-and-timers.md#events).
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
        return tuple(self._server.roles[name] for name in self._server._get_session_roles(self.id))

    @roles.setter
    def roles(self, roles: Iterable[Role | o6.NodeId]) -> None:
        self._server._set_session_roles(self.id, [_role_id(self._server, role) for role in roles])
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
        return self._server._get_session_attribute(self.id, _qualified_name(key))

    def set(self, key: o6.QualifiedName | str, value: Any) -> None:
        """Set one session attribute.

        Args:
            key: Attribute name. A plain string is read as namespace 0.
            value: Any value of a registered OPC UA type.

        Raises:
            StatusCodeError: The session is gone.
        """
        self._server._set_session_attribute(self.id, _qualified_name(key), value)

    def delete(self, key: o6.QualifiedName | str) -> None:
        """Remove one session attribute.

        Args:
            key: Attribute name. A plain string is read as namespace 0.

        Raises:
            StatusCodeError: The session is gone, or the attribute is not set.
        """
        self._server._delete_session_attribute(self.id, _qualified_name(key))

    def close(self) -> None:
        """Close this session, cancelling its subscriptions.

        Raises:
            StatusCodeError: The session is already gone.
        """
        self._server._close_session(self.id)


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
        role_id = self._server._add_role(*self._args(role))
        return self[role_id]

    def update(self, role: Role) -> Role:
        self._server._update_role(*self._args(role))
        return self[role.id if role.id is not None else role.name]

    def remove(self, role: Role | o6.QualifiedName | str) -> None:
        name = role.name if isinstance(role, Role) else role
        self._server._remove_role(_qualified_name(name))

    def __getitem__(self, key: o6.NodeId | o6.QualifiedName | str) -> Role:
        by_id = isinstance(key, o6.NodeId)
        return self._from_native(
            self._server._get_role(key if by_id else _qualified_name(key), by_id)
        )

    def __iter__(self) -> Iterator[Role]:
        for name in self._server._get_roles():
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

    The leading underscore is part of the name: unprefixed attribute access on a
    node handle browses to child nodes, so `node.permissions = ...` would
    silently create an ordinary Python attribute and change nothing.

    Assigning a mapping to `node._permissions` is shorthand for
    [`set`][o6.server.NodePermissions.set]. Every operation here takes
    `recursive=True` to apply to the whole subtree, and each raises
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

    def get(self) -> dict[Role, ns0.datatypes.PermissionType]:
        """Return the permissions set explicitly on this node.

        Namespace defaults are not included, so an empty result means the node
        falls back to its namespace default.
        """
        return {
            self._server.roles[role_id]: ns0.datatypes.PermissionType(value)
            for role_id, value in self._server._get_node_role_permissions(self._node_id).items()
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
        self._server._set_node_role_permissions(
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
        self._server._add_role_permissions(
            self._node_id, _role_id(self._server, role), int(permissions), overwrite, recursive
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
        self._server._remove_role_permissions(
            self._node_id, _role_id(self._server, role), int(permissions), recursive
        )

    def clear(self, *, recursive: bool = False) -> None:
        """Remove every explicit permission, so the namespace default applies.

        Args:
            recursive: Apply to this node's whole subtree.
        """
        self._server._remove_node_role_permissions(self._node_id, recursive)


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


class AccessControl:
    """Python implementation of the open62541 `UA_AccessControl` plugin.

    Subclass it, override `activateSession` for authentication, and override the
    authorization hooks that matter. The base authorization policy is permissive
    and the base authentication policy accepts anonymous sessions only, so an
    unmodified instance behaves like an open server.

    Only overridden hooks cost anything: the server installs a callback
    trampoline for the methods a subclass actually replaces, and leaves the rest
    to open62541.

    Every hook is called on the server's event loop with a
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
                `AnonymousIdentityToken` or `UserNameIdentityToken`.

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

        The base implementation grants every bit. See
        [`AttributeWriteMask`][o6.ns.ns0.datatypes.AttributeWriteMask] for the bit layout.
        """
        return 0xFFFFFFFF

    def getUserAccessLevel(self, session: Session, nodeId: o6.NodeId) -> int:
        """Return the session's UserAccessLevel for one Variable.

        The base implementation grants every bit. See
        [`AccessLevelType`][o6.ns.ns0.datatypes.AccessLevelType] for the bit layout.
        """
        return 0xFF

    def getUserExecutable(self, session: Session, methodId: o6.NodeId) -> bool:
        """Return whether the session may execute a Method at all.

        The base implementation allows it.
        """
        return True

    def getUserExecutableOnObject(
        self,
        session: Session,
        methodId: o6.NodeId,
        objectId: o6.NodeId,
    ) -> bool:
        """Return whether the session may execute a Method on one Object.

        The base implementation allows it. This is the hook to use when the
        answer depends on which instance is being addressed.
        """
        return True

    def allowAddNode(self, session: Session, item: Any) -> bool:
        """Return whether the session may add a node.

        The base implementation allows it.

        Args:
            session: The requesting session.
            item: The requested `AddNodesItem`.
        """
        return True

    def allowAddReference(self, session: Session, item: Any) -> bool:
        """Return whether the session may add a reference.

        The base implementation allows it.

        Args:
            session: The requesting session.
            item: The requested `AddReferencesItem`.
        """
        return True

    def allowDeleteNode(self, session: Session, item: Any) -> bool:
        """Return whether the session may delete a node.

        The base implementation allows it.

        Args:
            session: The requesting session.
            item: The requested `DeleteNodesItem`.
        """
        return True

    def allowDeleteReference(self, session: Session, item: Any) -> bool:
        """Return whether the session may delete a reference.

        The base implementation allows it.

        Args:
            session: The requesting session.
            item: The requested `DeleteReferencesItem`.
        """
        return True

    def allowBrowseNode(self, session: Session, nodeId: o6.NodeId) -> bool:
        """Return whether the session may browse one node.

        The base implementation allows it. This hook runs for every browsed node,
        so keep it cheap.
        """
        return True

    def allowTransferSubscription(
        self,
        oldSession: Session,
        newSession: Session,
    ) -> bool:
        """Return whether subscriptions may move between two sessions.

        The base implementation allows the transfer when both sessions carry an
        equal context, which is what keeps a reconnecting client's subscriptions
        alive while refusing another user's.
        """
        return oldSession.context == newSession.context

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

        The base implementation allows it.

        Args:
            session: The requesting session.
            nodeId: The node whose history is being updated.
            performUpdateType: The requested `PerformUpdateType`.
            value: The [`DataValue`][o6.DataValue] being written.
        """
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

        The base implementation allows it.

        Args:
            session: The requesting session.
            nodeId: The node whose history is being deleted.
            startTimestamp: Start of the range to delete.
            endTimestamp: End of the range to delete.
            isDeleteModified: Delete modified values rather than raw ones.
        """
        return True


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
        index = (
            namespace
            if isinstance(namespace, int)
            else self._server._get_namespace_index(namespace)
        )
        self._server._set_namespace_role_permissions(
            index, {_role_id(self._server, role): int(value) for role, value in permissions.items()}
        )

    def get_default_permissions(
        self, namespace: int | str
    ) -> dict[Role, ns0.datatypes.PermissionType]:
        index = (
            namespace
            if isinstance(namespace, int)
            else self._server._get_namespace_index(namespace)
        )
        return {
            self._server.roles[role_id]: ns0.datatypes.PermissionType(value)
            for role_id, value in self._server._get_namespace_role_permissions(index).items()
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
            self._server._on_event_loop(
                partial(self._server._add_namespace, info.uri, global_index)
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
        publisher.publish()


_server_name_counter = 0
_live_servers: weakref.WeakSet["Server"] = weakref.WeakSet()
_live_servers_lock = threading.Lock()


def _register_live_server(server: "Server") -> None:
    with _live_servers_lock:
        _live_servers.add(server)


def _unregister_live_server(server: "Server") -> None:
    with _live_servers_lock:
        _live_servers.discard(server)


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

    Return behavior depends on the operation and caller loop. Node creation
    returns handles directly except for async tasks calling a running worker
    from another loop, which receive awaitables; see
    [`MaybeAwaitable`][o6.MaybeAwaitable].

    See the [Server guide](manual/server/index.md) for the whole picture, and
    [Server callbacks](manual/server/callbacks.md) for behaviour implementation.
    """

    ns: _ServerNamespaces
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
        acceptAllCertificates: bool = False,
        applicationUri: str | None = None,
        accessControl: AccessControl | None = None,
        allowNonePolicyPassword: bool = False,
        rbacForAnonymous: bool = False,
    ) -> None:
        """Create a server. It is not listening until `start()` is called.

        Args:
            port: TCP port to bind.
            logger: Logger for server output. Defaults to the `o6.server` logger.
            loop: Event loop to schedule non-blocking iterations on. When given,
                or when a running loop is detected, the server does not spawn a
                background thread; otherwise it creates its own loop and drives it
                from a daemon thread.
            certificate: Server certificate, as a path or raw DER or PEM bytes.
                Must be provided together with a nonempty private key.
            privateKey: Matching private key, as a path or raw bytes. Both
                credential files or byte strings must be nonempty.
            trustList: Client certificates the server trusts.
            issuerList: Issuer certificates for chain validation.
            revocationList: Certificate revocation lists.
            secureOnly: Refuse unencrypted connections. Requires a certificate
                and private key.
            acceptAllCertificates: Trust every client certificate. For
                development only.
            applicationUri: Override the advertised application URI. It must match
                the URI inside the server certificate on secured endpoints.
            accessControl: An [`AccessControl`][o6.server.AccessControl] subclass
                instance that authenticates and authorizes sessions.
            allowNonePolicyPassword: Permit username/password tokens on an
                unencrypted channel.
            rbacForAnonymous: Enforce role permissions for anonymous sessions.
                Off by default, which leaves anonymous sessions permissive.

        Raises:
            TypeError: `accessControl` is not an `o6.AccessControl` instance.
            ValueError: Credentials are incomplete or empty, or `secureOnly`
                is requested without a certificate and private key.
            PermissionError: This build has no `server` feature entitlement.
        """
        _requireServer()
        if (certificate is None) != (privateKey is None):
            raise ValueError("certificate and privateKey must be provided together")
        if secureOnly and certificate is None:
            raise ValueError("secureOnly requires certificate and privateKey")
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

        if logger is None:
            logger = logging.getLogger(__name__)

        kwargs: dict = {"port": port, "loop": self._loop, "logger": logger}
        super().__init__(**kwargs)
        self._listener_startup: asyncio.Future | None = None
        self._shutdown_task: asyncio.Task[None] | None = None
        self._shutdown_thread: threading.Thread | None = None
        self._node_backend = _ServerBackend(self)
        self._pending_history: list[tuple[o6.NodeId, History]] = []
        for marker in _server_materialization._collect_variabletype_markers(ns0):
            self._attach_instance_type(marker, VariableNode)
        self.roles = _RoleRegistry(self)
        self._notification_categories: dict[int, NotificationHandlers] = {
            dispatch_key(t): NotificationHandlers(self._sync_notification_trampoline)
            for t in _NOTIFICATION_PROPERTIES.values()
        }
        self._set_all_permissions_for_anonymous(not rbacForAnonymous)

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
            )

        if acceptAllCertificates:
            self.config.setAcceptAllCertificates()

        # Security-policy configuration rebuilds the underlying open62541
        # config, so apply the application identity and access control last.
        if applicationUri is not None:
            self.config.applicationUri = applicationUri
        self.config.allowNonePolicyPassword = allowNonePolicyPassword
        if accessControl is not None:
            if not isinstance(accessControl, AccessControl):
                raise TypeError("access_control must be an o6.AccessControl instance")
            self.config.setAccessControl(accessControl)

        global _server_name_counter
        self._name = "server" + str(_server_name_counter)
        _server_name_counter += 1

        self._port = port
        self._worker: _WorkerLoop | None = None
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
        """Install server-local Python behaviour on a UA type or concrete node.

        `implement(DeclarationType, ImplementationType)` binds an undecorated
        Python behaviour subclass to an existing ObjectType or VariableType on
        this server alone. Future instances created through native APIs or an
        AddNodes request receive that implementation, without modifying or
        subclassing the UA information model. Their implementation-selected
        children are created before the native Mandatory children, and their
        ordinary Python initializer runs once, after the complete subtree exists.
        Because AddNodes supplies no Python arguments, that initializer must be
        callable without required arguments. Passing `None` restores the
        declaration's own Python type for future instances.

        Passing `None` positionally for a concrete Method or Variable restores the
        callback resolution performed during construction. A concrete value
        positionally supplied for a Variable removes both callbacks and installs
        that value in native storage.

        `call=`, `read=`, and `write=` replace or clear one callback slot on a
        Method, Variable, or VariableType. Existing concrete instances are never
        changed by a type-level update.

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

        See [Implementing behaviour](manual/server/behaviour.md#implementing-behaviour) and
        [Server callbacks](manual/server/callbacks.md).
        """
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
                self._on_event_loop(
                    lambda: super(Server, self)._set_local_value(target_node, value)
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
        """Emit an event and return its generated EventId.

        Matches C's `UA_Server_createEvent`: this emits immediately. Construct
        `o6.Event(server, ...)` for a reusable draft. `emitEvent` is an alias.

        An explicit `eventType` wins; otherwise use `eventInstance`'s type when
        supplied, then `source`'s declared `GeneratesEvent` target. Without an
        instance, no declared target falls back to `BaseEventType`; ambiguous
        targets or a source without a type definition raise `ValueError`.

        `eventInstance` optionally supplies fields from an existing Object
        instance of `BaseEventType` or a subtype. Node handles must belong to
        this server; NodeIds are resolved locally. Explicit `fields` take
        precedence over instance properties, then standard defaults apply.
        Stored `EventType` and `SourceNode` properties also override emission
        arguments, including when their values are null NodeIds, matching C.
        The instance is read without being updated or deleted.

        Returns the EventId directly for synchronous callers, or an awaitable
        for asynchronous callers on another event loop.
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
            return super(Server, self)._emit_event(
                source_id,
                resolved_type,
                severity,
                localized_message,
                normalized_fields,
                instance_id,
            )

        return self._maybe_async(_do())

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

    def _maybe_async_coro(self, coro: Any) -> MaybeAwaitable:
        return self._maybe_async(coro)

    T = TypeVar("T")

    def _maybe_async(self, aw: Awaitable[T]) -> MaybeAwaitable[T]:
        if self._worker is not None and not self._worker.running:
            if asyncio.iscoroutine(aw):
                aw.close()
            raise RuntimeError("Server event loop is not running")

        try:
            loop = asyncio.get_running_loop()
            if loop == self._loop:
                return aw  # type: ignore[return-value]
        except RuntimeError:
            loop = None

        async def _await(f):
            return await f

        # Before startup there is no worker to service a foreign loop. Native
        # address-space operations can execute on the configuring caller loop.
        if loop is not None and self._worker is None and not self._loop.is_running():
            return aw

        # Sync caller, but our loop is not running yet (pre-start configuration
        # phase).  Drive the awaitable to completion inline.
        if loop is None and not self._loop.is_running():
            if asyncio.iscoroutine(aw) or inspect.iscoroutine(aw):
                return self._loop.run_until_complete(aw)
            return self._loop.run_until_complete(_await(aw))

        try:
            if asyncio.iscoroutine(aw) or inspect.iscoroutine(aw):
                fut = asyncio.run_coroutine_threadsafe(aw, self._loop)
            else:
                fut = asyncio.run_coroutine_threadsafe(_await(aw), self._loop)
        except RuntimeError:
            if asyncio.iscoroutine(aw):
                aw.close()
            raise RuntimeError("Server event loop is not running")

        if loop is None or asyncio.current_task() is None:
            # Sync caller: no running loop, or running on a foreign loop as a
            # scheduled callback (not inside an async task).  Block until done.
            return fut.result()
        else:
            # Async task on a foreign loop — return an awaitable the caller can
            # ``await`` on their own loop.
            return asyncio.wrap_future(fut)

    def _wrap_future(
        self,
        fut: concurrent.futures.Future,
        caller_loop: asyncio.AbstractEventLoop,
    ) -> asyncio.Future:
        afut = asyncio.wrap_future(fut, loop=caller_loop)
        afut._concurrent_future = fut  # type: ignore[attr-defined]
        return afut

    def _on_event_loop(self, fn: Callable[[], Any]) -> Any:
        # No worker thread yet, or already on it — call directly
        if self._worker is None or not self._worker.running or self._worker.on_loop_thread:
            out = invoke_sync(fn, ())
            # Synchronous async-server calls resolve their future inline.
            # Unwrap to keep the public API sync-friendly.
            if asyncio.isfuture(out) and out.done():
                return out.result()
            return out

        # Detect whether the caller is itself inside an event loop
        try:
            caller_loop = asyncio.get_running_loop()
        except RuntimeError:
            caller_loop = None

        async def _call() -> Any:
            out = invoke_sync(fn, ())
            return await out if inspect.isawaitable(out) else out

        coro = _call()
        try:
            fut = asyncio.run_coroutine_threadsafe(coro, self._loop)
        except RuntimeError:
            coro.close()
            raise

        # Sync caller (no running loop) or same loop — block until done
        if caller_loop is None or caller_loop is self._loop or asyncio.current_task() is None:
            return fut.result()

        # Async task on a different running loop — return an awaitable.
        return self._wrap_future(fut, caller_loop)

    # -- Well-known nodes (convenience properties) ---------------------------

    def __getitem__(self, key: NodeIdLike) -> MaybeAwaitable[Node]:
        """Resolve a node ID to its canonical typed [Node][o6.Node] handle.

        Repeated lookup returns the same server-owned Python object, preserving
        its modeled type and application state. Deleted nodes cannot be looked
        up; reusing their ID resolves to the replacement object.

        Args:
            key: A NodeId-like value accepted by [NodeId][o6.NodeId], including
                a string, numeric namespace-zero ID, NodeId, or node handle.

        Returns:
            The matching Node subclass synchronously, or an awaitable in async
            tasks, before startup and on either the server or a foreign loop.
            The `root`, `objects`, `types`, and `views` handles are available
            immediately in every mode and support normal child/path navigation.

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
        return self._maybe_async(self._node_backend.node_get(o6.NodeId(key)))

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
        """The server's owning asyncio loop, fixed at construction time.

        Supplied or detected running loops remain caller-owned. Otherwise the
        server creates and manages its loop; callers must not close it directly.
        `waitReady()` must be awaited on this loop.
        """
        return self._loop

    @property
    def endpointUrl(self) -> str:
        """The local endpoint URL, built from the configured port."""
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

        Fires around every individual service request the server processes,
        so a handler here is on the hot path.

        See [Service](manual/server/notification-handler.md#service).
        """
        return self._notification_categories[dispatch_key(NotificationType.SERVICE_BEGIN)]

    @onServiceNotification.setter
    def onServiceNotification(self, value: Any) -> None:
        self.onServiceNotification.replace(value)

    @property
    def onSubscriptionNotification(self) -> NotificationHandlers:
        """Registry of subscription created/modified/publishing-mode/transferred/deleted
        notification handlers.

        See [Subscription](manual/server/notification-handler.md#subscription).
        """
        return self._notification_categories[dispatch_key(NotificationType.SUBSCRIPTION_CREATED)]

    @onSubscriptionNotification.setter
    def onSubscriptionNotification(self, value: Any) -> None:
        self.onSubscriptionNotification.replace(value)

    @property
    def onMonitoredItemNotification(self) -> NotificationHandlers:
        """Registry of monitored-item created/modified/monitoring-mode-changed/deleted
        notification handlers.

        See [MonitoredItem](manual/server/notification-handler.md#monitoreditem).
        """
        return self._notification_categories[dispatch_key(NotificationType.MONITOREDITEM_CREATED)]

    @onMonitoredItemNotification.setter
    def onMonitoredItemNotification(self, value: Any) -> None:
        self.onMonitoredItemNotification.replace(value)

    @property
    def onDiscoveryRegisterServerNotification(self) -> NotificationHandlers:
        """Registry of discovery RegisterServer notification handlers.

        A separate category from `onDiscoveryServerOnNetworkNotification`;
        the two payloads are disjoint.

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

        A separate category from `onDiscoveryRegisterServerNotification`;
        the two payloads are disjoint.

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

        Opt-in: open62541 drops audit notifications unless
        `server.config.auditingEnabled` is `True`.
        `notification.auditEventType` names the specific standardized
        `AuditEventType` subtype.

        See [Audit](manual/server/notification-handler.md#audit).
        """
        return self._notification_categories[dispatch_key(NotificationType.AUDIT)]

    @onAuditNotification.setter
    def onAuditNotification(self, value: Any) -> None:
        self.onAuditNotification.replace(value)

    def _sync_notification_trampoline(self) -> None:
        # The C-side flip is a single pointer write and idempotent; no
        # Python-side guard needed.
        self._set_notification_trampoline(any(self._notification_categories.values()))

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

    # -- Lifecycle -----------------------------------------------------------

    def start(self) -> None:
        """Start the server networking layer.

        Synchronous callers wait until the listeners are ready, using a
        background thread to drive I/O. On the server's running asyncio loop,
        await `waitReady()` afterwards, or use `async with server`.
        Listener creation failures are raised by the readiness wait.
        """
        if (
            self._shutdown_thread is not None
            and self._shutdown_thread is not threading.current_thread()
        ):
            self._shutdown_thread.join(timeout=10.0)
        if self._shutdown_task is not None and self._worker is not None:
            if not self._shutdown_task.done() or self._worker.on_loop_thread:
                raise RuntimeError("Server shutdown is still in progress")
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
            begin()
            return

        started_worker = not self._loop.is_running()
        if started_worker:
            self._worker = _WorkerLoop(self._loop)
            self._worker.start()

        async def start_and_wait():
            begin()
            await self.waitReady()

        pending = asyncio.run_coroutine_threadsafe(start_and_wait(), self._loop)
        try:
            pending.result()
        except BaseException:
            pending.cancel()
            _unregister_live_server(self)
            if started_worker and self._worker is not None:
                self._worker.stop(close=False)
                self._worker = None
            raise

    async def waitReady(self) -> None:
        """Wait for a started server's listeners, raising any bind failure.

        Call on `server.loop` after `start()`. Cancelling this
        wait shuts down startup and closes any listeners already opened.
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
            raise

    def stop(self) -> asyncio.Task[None] | None:
        """Shut down the server.

        Calls from a background server's own loop initiate shutdown and return
        a Task that can be awaited. Other callers block until shutdown finishes.
        The server's worker is stopped after the shutdown task completes.
        """
        _unregister_live_server(self)
        if (
            self._shutdown_thread is not None
            and self._shutdown_thread is not threading.current_thread()
        ):
            self._shutdown_thread.join(timeout=10.0)
        worker = self._worker
        if worker is not None and worker.running:
            worker_thread = worker._thread

            async def shutdown_and_drain() -> None:
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

            def begin_shutdown() -> asyncio.Task[None]:
                if self._shutdown_task is None:
                    self._shutdown_task = self._loop.create_task(shutdown_and_drain())
                return self._shutdown_task

            def retire_worker() -> None:
                # WorkerLoop.stop clears its thread handle even when called
                # on that thread. Retain it so external callers can join it.
                self._shutdown_thread = worker_thread
                worker.stop(close=False)
                if worker_thread is not None and worker_thread is not threading.current_thread():
                    worker_thread.join(timeout=10.0)
                if self._worker is worker:
                    self._worker = None

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

            async def shutdown_and_wait() -> None:
                await begin_shutdown()

            future = asyncio.run_coroutine_threadsafe(shutdown_and_wait(), self._loop)
            future.result(timeout=10.0)
            retire_worker()
        elif self.running:
            self._run_shutdown()
            self._stop_event_loop()
        return None

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

    def __del__(self):
        try:
            if self.running:
                self.stop()
        except Exception:
            pass
        try:
            self._cleanup()
        except Exception:
            pass
        try:
            if self._owns_loop and not self._loop.is_closed():
                self._loop.close()
        except Exception:
            pass

    # -- Reverse connect ------------------------------------------------------

    @public_result
    def addReverseConnect(
        self,
        url: str,
        callback: Callable[[int, int], None] | None = None,
    ) -> MaybeAwaitable[int]:
        """Register a reverse connect to a client listening at *url*.

        The server will periodically attempt to establish a connection
        to the given client endpoint (e.g. `opc.tcp://localhost:4841`).

        Args:
            url: The OPC UA endpoint URL of the listening client.
            callback: Called with `(handle, state)` on every state change.

        Returns:
            A handle that can be passed to `removeReverseConnect`.
        """
        return self._on_event_loop(
            lambda: super(Server, self)._add_reverse_connect(
                url, synchronous(callback) if callback is not None else None
            )
        )

    @public_result
    def removeReverseConnect(self, handle: int) -> MaybeAwaitable[None]:
        """Remove a reverse connect registration.

        Args:
            handle: The handle returned by `addReverseConnect`.
        """
        return self._on_event_loop(lambda: super(Server, self)._remove_reverse_connect(handle))

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

        return self._on_event_loop(create)

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
        historizing: bool | History = False,
        ns: int = 1,
        parentReference: NodeIdLike = ns0.reftypes.Organizes,
    ) -> MaybeAwaitable[VariableNode]:
        """Add a variable node to the address space.

        Args:
            name: BrowseName, and DisplayName, of the Variable.
            parent: Parent node, typically `server.objectsNode`.
            value: Initial value. Its OPC UA DataType is inferred unless
                `dataType` is given explicitly. Empty NumPy arrays retain their
                datatype and ValueRank; empty Python sequences require `dataType`.
                Empty values are read back as flat arrays because OPC UA Binary
                omits dimension sizes for them.
            nodeId: Requested NodeId. The server assigns one when omitted.
            dataType: Explicit DataType. Inferred from `value` when omitted.
            typeDefinition: VariableType of the new node.
            writable: Whether clients may write the Variable.
            historizing: Whether to record this Variable's history. Registers
                immediately on a running server, which requires a configured
                history database. Before startup, registration is deferred to
                `start()` so the database can be configured after creation.
            ns: Namespace index for the BrowseName.
            parentReference: Reference linking the parent to the new node.
                Defaults to Organizes, matching the client convenience.

        Returns:
            A handle to the new Variable node, or an awaitable resolving to it
            for every async task, including before startup and on the owning
            loop. Ordinary synchronous callers receive the handle directly.
            Cancellation does not roll back a native creation already completed.

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
            attr, initial_value, empty_shape = variable_attributes(name, value, dataType, writable)
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
            attr.userAccessLevel = access
            # Local array initialization writes the value after attaching the node.
            if isinstance(initial_value, np.ndarray):
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
                # The native initializer already supplies a typed empty array.
                # A zero-length value has no dimensions on the wire and cannot
                # pass the backend's multidimensional Write rank check.
                if initial_value is not None and empty_shape is None:
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

        return self._on_event_loop(create)

    def historize(
        self,
        target: NodeIdLike,
        *,
        capacity: int | None = 0,
        strategy: str = "on-write",
        interval: float = 1.0,
    ) -> MaybeAwaitable[None]:
        """Record the history of an existing Variable.

        `addVariable(..., historizing=...)` covers Variables this server
        creates. This is for the ones it does not: nodes loaded from a nodeset,
        declared instances, or nodes a client added. It sets the `Historizing`
        attribute and the history access bits as well as registering the node,
        so a Variable that was not marked historizing becomes one.

        This takes effect immediately and needs a history database already
        configured. Variables created with `historizing=` register immediately
        when running, or during `start()` when created before startup.
        Await this method from async code; synchronous callers block until it
        completes. Failed registration restores the original node attributes.

        ```python
        server.config.setHistoryDatabase(capacity=5000)
        server.historize("ns=1;s=Level")
        server.historize(sensorNode, strategy="poll", interval=0.2)
        ```

        Args:
            target: The Variable to historize.
            capacity: Samples kept for this node; 0 takes the database default,
                `None` grows the store instead of evicting.
            strategy: `"on-write"` or `"poll"`.
            interval: Seconds between samples, for `"poll"` only.

        Raises:
            RuntimeError: No history database is configured.
            ValueError: The strategy or the interval is not usable.
            StatusCodeError: The node's store could not be allocated.
        """
        config = History(capacity=capacity, strategy=strategy, interval=interval)
        return self._maybe_async(self._change_history(o6.NodeId(target), config))

    def unhistorize(self, target: NodeIdLike) -> MaybeAwaitable[None]:
        """Stop recording a Variable's history and release its store.

        The inverse of `historize`: it clears the `Historizing` attribute and
        the history access bits, drops the registration, and frees the samples.
        Nothing is kept — registering the node again
        starts from an empty store. Await this method from async code;
        synchronous callers block until it completes.

        ```python
        server.unhistorize("ns=1;s=Level")
        ```

        Args:
            target: The Variable to stop historizing.

        Raises:
            RuntimeError: No history database is configured.
            StatusCodeError: The node does not exist.
        """
        return self._maybe_async(self._change_history(o6.NodeId(target), None))

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
        """Add an object node to the address space.

        Args:
            name: BrowseName, and DisplayName, of the Object.
            parent: Parent node.
            nodeId: Requested NodeId. The server assigns one when omitted.
            typeDefinition: ObjectType of the new node. Defaults to
                `BaseObjectType` (`i=58`).
            ns: Namespace index for the BrowseName.
            parentReference: Reference linking the parent to the new node.
                Defaults to Organizes, matching the client convenience.

        Returns:
            A handle to the new Object node, or an awaitable resolving to it
            for every async task, including before startup and on the owning
            loop. Ordinary synchronous callers receive the handle directly.
            Cancellation does not roll back a native creation already completed.

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
        """Add an object type node.

        Args:
            name: BrowseName, and DisplayName, of the ObjectType.
            parent: The `HasSubtype` parent. Defaults to `BaseObjectType`
                (`i=58`).
            nodeId: Requested NodeId. The server assigns one when omitted.
            ns: Namespace index for the BrowseName.

        Returns:
            A handle to the new ObjectType node, or an awaitable resolving to it
            for every async task, including before startup and on the owning
            loop. Ordinary synchronous callers receive the handle directly.
            Cancellation does not roll back a native creation already completed.

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
        """Add a variable type node.

        Args:
            name: BrowseName, and DisplayName, of the VariableType.
            parent: The `HasSubtype` parent. Defaults to `BaseVariableType`
                (`i=62`).
            dataType: DataType of the value. Defaults to `Double` (`i=11`).
            valueRank: ValueRank of the value. Defaults to `-1`, a scalar.
            nodeId: Requested NodeId. The server assigns one when omitted.
            ns: Namespace index for the BrowseName.

        Returns:
            A handle to the new VariableType node, or an awaitable resolving to it
            for every async task, including before startup and on the owning
            loop. Ordinary synchronous callers receive the handle directly.
            Cancellation does not roll back a native creation already completed.

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
            inverseName: InverseName attribute, the name of the reverse
                direction. OPC UA requires it for a non-symmetric, non-abstract
                ReferenceType.
            symmetric: Declare the reference symmetric, so it reads the same in
                both directions and needs no InverseName.
            abstract: Declare the ReferenceType abstract, so only its subtypes may
                be used in references.
            nodeId: NodeId of the node. The server allocates one when omitted.
            ns: Namespace index for the BrowseName.

        Returns:
            A handle to the new ReferenceType node, or an awaitable resolving to it
            for every async task, including before startup and on the owning
            loop. Ordinary synchronous callers receive the handle directly.
            Cancellation does not roll back a native creation already completed.

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

        The View starts out empty; add its members with `addReference`. For the
        declarative route, use [`o6.view`][o6.view] instead.

        Args:
            name: DisplayName of the node, also used as its BrowseName.
            parent: Node that organizes the View. Defaults to the standard
                ViewsFolder.
            eventNotifier: EventNotifier attribute of the node.
            containsNoLoops: ContainsNoLoops attribute, asserting that browsing
                the View cannot revisit a node.
            nodeId: NodeId of the node. The server allocates one when omitted.
            ns: Namespace index for the BrowseName.

        Returns:
            A handle to the new View node, or an awaitable resolving to it
            for every async task, including before startup and on the owning
            loop. Ordinary synchronous callers receive the handle directly.
            Cancellation does not roll back a native creation already completed.

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
        """Add a method node to the address space.

        Args:
            name: BrowseName, and DisplayName, of the Method.
            parent: Parent node, typically an Object.
            callback: Called when a client invokes the Method. See
                [`MethodCallback`][o6.server.MethodCallback] for the signature.
            inputArgs: InputArguments descriptors.
            outputArgs: OutputArguments descriptors.
            nodeId: Requested NodeId. The server assigns one when omitted.
            ns: Namespace index for the BrowseName.

        Returns:
            The unbound server Method node. Invoke it with `object=parent`, or
            reach it through the parent Object's dot syntax to obtain a bound
            call. Every async task receives an awaitable resolving to the
            configured handle, including before startup and on the owning loop.
            Ordinary synchronous callers receive the handle directly. Cancellation does not roll back
            a native creation that has already completed.

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

        return self._on_event_loop(create)

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
            node_class = self._on_event_loop(
                lambda: super(Server, self)._read_attribute(
                    target_id, int(o6.AttributeId.NODE_CLASS)
                )
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
        self._on_event_loop(
            lambda: super(Server, self)._set_callback_slot(
                target, _NATIVE_CALLBACK_KIND[kind], callback, receiver
            )
        )

    def _node_callback(self, target: Node, kind: _CallbackKind) -> Callable[..., Any] | None:
        callback = self._on_event_loop(
            lambda: super(Server, self)._get_callback(target, _NATIVE_CALLBACK_KIND[kind])
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
        """Add a reference using the legacy server argument order.

        Args:
            source: Source node id.
            target: Target node id, including an expanded target.
            referenceType: Reference type id.
            forward: Whether the reference points forward.

        Returns:
            None for synchronous callers; awaitable in async tasks.

        Raises:
            StatusCodeError: The individual mutation failed.
        """
        src_id, ref_id = o6.NodeId(source), o6.NodeId(referenceType)
        tgt_id = (
            target
            if isinstance(target, o6.ExpandedNodeId)
            else o6.ExpandedNodeId(o6.NodeId(target))
        )

        def add() -> None:
            super(Server, self)._add_reference(src_id, ref_id, tgt_id, forward).check()

        return self._on_event_loop(add)

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
        """Delete a reference using legacy server arguments and errors.

        Args:
            source: Source node id.
            target: Target node id, including an expanded target.
            referenceType: Reference type id.
            forward: Whether to delete the forward reference.
            bidirectional: Whether to also delete the reverse reference.

        Returns:
            None for synchronous callers; awaitable in async tasks.

        Raises:
            StatusCodeError: The individual mutation failed.
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

        return self._on_event_loop(delete)

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
            source: Source node id.
            reftype: Reference type id.
            target: Target node id or expanded id, including remote metadata.
            forward: Whether to create a forward reference.
            targetNodeClass: Local creation supports only UNSPECIFIED; other
                values return BAD_NOT_SUPPORTED.
            targetServerUri: Nonempty URIs return BAD_NOT_IMPLEMENTED. Use an
                expanded target to identify a remote node.

        Returns:
            The individual StatusCode, or an awaitable resolving to it.
            Rejected mutations, including duplicate local edges, return bad statuses.

        Raises:
            TypeError: An argument has an invalid Python type.
            ValueError: An argument cannot be converted to a node id or enum.

        Use addReferenceLegacy for the old server positional order and errors.
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

        return self._maybe_async(add())

    def _add_reference_once(
        self,
        source: NodeIdLike,
        target: NodeIdLike,
        reference_type: NodeIdLike,
        *,
        forward: bool = True,
    ) -> MaybeAwaitable[None]:
        """Add an exact edge, accepting one already materialized by open62541."""

        def add() -> None:
            try:
                self.addReferenceLegacy(source, target, reference_type, forward=forward)
            except o6.StatusCodeError as exc:
                if exc.code != o6.StatusCode.BAD_DUPLICATE_REFERENCE_NOT_ALLOWED:
                    raise

        return self._on_event_loop(add)

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
            source: Source node id.
            reftype: Reference type id.
            target: Target node id or expanded id, including remote metadata.
            forward: Whether to delete the forward reference.
            deleteBidirectional: Whether to also delete the reverse reference.

        Returns:
            The individual StatusCode, or an awaitable resolving to it.
            Rejected deletions return non-Good statuses, including
            UNCERTAIN_REFERENCE_NOT_DELETED for an absent edge.

        Raises:
            TypeError: An argument has an invalid Python type.
            ValueError: An argument cannot be converted to a node id.

        Use deleteReferenceLegacy for the old order and bidirectional flag.
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

        return self._maybe_async(delete())

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
            nodeId: A node, node id, or list of these targets.
            deleteTargetReferences: If True (default), remove incoming
                references from remaining nodes. False leaves dangling references.

        Returns:
            One StatusCode for a scalar target, otherwise a list in input order,
            including one-element batches. All targets are attempted despite
            per-target failures. An empty list returns [] without a deletion.
            Async callers must await the result.

        Raises:
            TypeError: An argument has an invalid Python type.
            ValueError: A target cannot be converted to a node id.

        Migrate deleteReferences to deleteTargetReferences. Individual failures
        return statuses; call status.check() to retain exception handling.
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

        return self._maybe_async(delete())

    # -- Method call ----------------------------------------------------------

    def call(  # type: ignore[override]
        self,
        objectId: NodeIdLike,
        methodId: NodeIdLike,
        inputArgs: list[Any] = [],
    ) -> MaybeAwaitable[tuple[o6.StatusCode, *tuple[Any, ...]]]:
        """Call a method node server-side with admin privileges.

        Matches `client.call()` — returns `(StatusCode, *output_arguments)`.

        Args:
            objectId: The Object that owns the Method.
            methodId: The Method to invoke.
            inputArgs: InputArguments values, in declaration order.

        Returns:
            `(statusCode, output1, output2, ...)`, including bad method statuses
            and any available outputs. Invalid method selection and argument
            validation also produce method results. A zero-output result is
            `(statusCode,)`.

        Raises:
            StatusCodeError: Submission failed; `code` retains the original
                status. Method-result failures do not raise.
            TypeError: An argument cannot be converted to an OPC UA value.
        """
        obj_id = o6.NodeId(objectId)
        mth_id = o6.NodeId(methodId)
        args = [_normalize_nodeids(arg) for arg in inputArgs]

        async def _do() -> tuple[o6.StatusCode, *tuple[Any, ...]]:
            return await super(Server, self)._call(obj_id, mth_id, args, 0, True)

        return self._maybe_async(_do())

    @public_result
    def addPublishedDataSet(
        self,
        configuration: ns0.datatypes.PublishedDataSetDataType,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Create published items with their complete metadata and source mapping.

        Field count, data types and ranks must match the source variables.
        Folder paths and event datasets are currently unsupported. Await this
        operation in async tasks, including on the owning loop.
        """
        return self._on_event_loop(
            lambda: super(Server, self)._add_published_dataset(_normalize_nodeids(configuration))
        )

    @public_result
    def addSubscribedDataSet(
        self,
        name: str,
        metadata: ns0.datatypes.DataSetMetaDataType,
        targets: ns0.datatypes.TargetVariablesDataType,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Create a native standalone subscribed DataSet in SubscribedDataSets.

        Field metadata and target mappings must have the same order and count.
        This defines the dataset without creating or enabling a DataSetReader.
        Await this operation in async tasks, including on the owning loop.
        """
        return self._on_event_loop(
            lambda: super(Server, self)._add_subscribed_dataset(name, metadata, targets)
        )

    @public_result
    def removeSubscribedDataSet(self, dataSetId: NodeIdLike) -> MaybeAwaitable[None]:
        """Remove a native standalone subscribed DataSet and its representation."""
        node_id = o6.NodeId(dataSetId)
        return self._on_event_loop(lambda: super(Server, self)._remove_subscribed_dataset(node_id))

    def _pubSubConfiguration(self, componentId: NodeIdLike):
        """Read an owned configuration snapshot; child arrays are read separately.

        Connection Enabled is configured intent. Read Status.State for its live state.
        """
        node_id = o6.NodeId(componentId)
        return self._on_event_loop(lambda: super(Server, self)._pubsub_configuration(node_id))

    def _setPubSubConnectionEnabled(self, connectionId: NodeIdLike, enabled: bool) -> None:
        """Set native PubSub connection state (internal component bridge)."""
        node_id = o6.NodeId(connectionId)
        return self._on_event_loop(
            lambda: super(Server, self)._set_pubsub_connection_enabled(node_id, enabled)
        )

    def _setPubSubComponentEnabled(self, componentId: NodeIdLike, enabled: bool) -> None:
        """Set one native PubSub component state."""
        node_id = o6.NodeId(componentId)
        return self._on_event_loop(
            lambda: super(Server, self)._set_pubsub_component_enabled(node_id, enabled)
        )

    def _removePubSubConnection(self, connectionId: NodeIdLike) -> None:
        """Remove a native PubSub connection and all child components."""
        node_id = o6.NodeId(connectionId)
        return self._on_event_loop(lambda: super(Server, self)._remove_pubsub_connection(node_id))

    def _setAllPubSubComponentsEnabled(self, enabled: bool) -> None:
        """Enable or disable the complete native PubSub component tree."""
        return self._on_event_loop(
            lambda: super(Server, self)._set_all_pubsub_components_enabled(enabled)
        )

    # -- Read / write ---------------------------------------------------------

    def _sync_result(self, result: Any) -> Any:
        if asyncio.isfuture(result):
            if hasattr(result, "_concurrent_future"):
                return result._concurrent_future.result()  # type: ignore[attr-defined]
            return result.result()
        return result

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

        Args:
            target: One NodeId-like target (including a Node) or a list of targets.
            attr: AttributeId or case-insensitive attribute name; keyword-only.
            timestampsToReturn: SOURCE (the default), SERVER, BOTH, or NEITHER.
            valueOnly: Return values for all Good-severity statuses when True,
                discarding status and timestamps. False returns DataValues for
                the caller to interpret, including Uncertain and Bad statuses.
            range: Inclusive OPC UA range string, stop-exclusive slice or tuple
                of slices, or one range per target. A scalar range broadcasts.
                None or an empty string reads the entire attribute.

        Returns:
            A scalar for one target, or a list in input order. An empty target
            list returns []. Raw DataValues retain per-target statuses and
            supported timestamp metadata, including failed reads.

        Raises:
            o6.StatusCodeError: A service failure or an Uncertain/Bad value-only status.
                The code property preserves the status; batch errors include
                the failed index in an exception note. Nonempty ranges on
                non-Value attributes return BAD_INDEX_RANGE_NO_DATA.
            TypeError: An argument has an unsupported Python type.
            ValueError: An attribute name, slice, or range-list length is invalid.

        Local reads run with administrative privileges. Remote client permissions
        still apply to Client.read. Use attr= for the attribute argument.
        """
        is_scalar, request = _read_request(target, attr, timestampsToReturn, valueOnly, range)

        async def _read() -> Any:
            results = [
                await super(Server, self)._read_data_value(item, int(request.timestampsToReturn))
                for item in request.nodesToRead
            ]
            return _read_results(results, is_scalar, valueOnly)

        return self._maybe_async(_read())

    def write(
        self,
        target: NodeIdLike | list[NodeIdLike] | Mapping[NodeIdLike, Any],
        value: Any = _WRITE_UNSET,
        *,
        attr: o6.AttributeId | str = o6.AttributeId.VALUE,
        range: o6.IndexRange | list[o6.IndexRange] = None,
    ) -> MaybeAwaitable[o6.StatusCode | list[o6.StatusCode]]:
        """Write one attribute using a scalar, parallel lists, or a mapping.

        Args:
            target: One NodeId-like target (including a Node), a list of targets,
                or a target-to-value mapping.
            value: Value for one target, or an equal-length list for target lists.
                Omit for mappings. A list for a scalar target is an array value.
                Explicit None writes a null value where the target permits it;
                omitting a scalar value raises ValueError.
                DataValues retain supported status and timestamp metadata.
            attr: AttributeId or case-insensitive attribute name; keyword-only.
            range: Inclusive OPC UA range string, stop-exclusive slice or tuple
                of slices, or one range per target. A scalar range broadcasts.
                None or an empty string writes the entire attribute. Nonempty
                ranges require Value; mappings do not accept ranges.

        Returns:
            One StatusCode for a scalar target, otherwise a list in input order,
            including one-element batches. Empty lists/mappings return []. Every
            target is attempted despite per-target status failures; check results.

        Raises:
            o6.StatusCodeError: A service-level failure; code preserves its status.
            TypeError: An argument has an unsupported Python type.
            ValueError: Input shapes, attribute names, or ranges are invalid.
                Shapes and ranges are validated before any writes.

        Local writes use administrative privileges and execute sequentially,
        without rollback. DataValue payloads honor attr; non-Value status and
        timestamp metadata is unsupported. Non-Value payloads must have the
        attribute's expected datatype; no attribute-specific coercion is applied.
        Replace broadcast calls with parallel values
        or a mapping, and check statuses to retain exception-based handling.
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

        return self._maybe_async(_write())

    def translateBrowsePaths(  # type: ignore[override]
        self,
        request: Any,
    ) -> MaybeAwaitable[Any]:
        """Server-side translate browse paths to node ids.

        Args:
            request: A `TranslateBrowsePathsToNodeIdsRequest` instance.

        Returns:
            The corresponding response."""

        async def _do() -> Any:
            r = super(Server, self)._translate_browse_paths(request)
            return (await r) if inspect.isawaitable(r) else r

        return self._maybe_async(_do())

    def serviceTranslateBrowsePathsToNodeIds(
        self, request: ns0.datatypes.TranslateBrowsePathsToNodeIdsRequest
    ) -> MaybeAwaitable[ns0.datatypes.TranslateBrowsePathsToNodeIdsResponse]:
        """Execute a raw path-translation request, preserving the response status.

        This matches the client service method. `translateBrowsePaths` remains
        an alias with its existing request/response contract.
        """
        return self.translateBrowsePaths(request)

    def findDataType(  # type: ignore[override]
        self,
        nodeId: NodeIdLike,
    ) -> MaybeAwaitable[Any]:
        """Look up a DataType by NodeId and return the Python type or metadata.

        Args:
            nodeId: The DataType node id to look up.

        Returns:
            Python type or DataType metadata for the requested NodeId."""
        nid = o6.NodeId(nodeId)

        async def _do() -> Any:
            r = super(Server, self)._find_data_type(nid)
            return (await r) if inspect.isawaitable(r) else r

        return self._maybe_async(_do())

    # -- View Service Set Methods  ------------------------------------------------------------

    def browse(
        self,
        target: NodeIdLike,
        *,
        direction: ns0.datatypes.BrowseDirection = ns0.datatypes.BrowseDirection.FORWARD,
        reftype: NodeIdLike = ns0.reftypes.HierarchicalReferences,
        refsubtypes: bool = True,
        nodeClassMask: int = ns0.datatypes.NodeClass.UNSPECIFIED,
        resultMask: int = ns0.datatypes.BrowseResultMask.NONE,
    ) -> MaybeAwaitable[list[ns0.datatypes.ReferenceDescription]]:
        """Collect all references from one node.

        Args:
            target: The node to browse from.
            direction: `FORWARD`, `INVERSE`, or `BOTH`.
            reftype: Only follow this ReferenceType. Defaults to
                `HierarchicalReferences`.
            refsubtypes: Also follow subtypes of `reftype`.
            nodeClassMask: Only return nodes of these NodeClasses, as the
                `UInt32` the service takes. Compose the `NodeClass` members you
                want with `|`. `UNSPECIFIED` returns all.
            resultMask: Which reference fields to fill in, as the `UInt32` the
                service takes. Compose the `BrowseResultMask` members you want
                with `|`. `NONE` returns only the target NodeIds.

        Returns:
            A complete flat list of `ReferenceDescription` objects, following
            continuation points until exhausted. Synchronous callers receive it
            directly. Async tasks must await the call, on either the server's
            loop or another loop. This applies to both Node and NodeId targets.

        Raises:
            StatusCodeError: Browse or BrowseNext failed. Outstanding continuation
                points are released on failure where the backend permits release.
        """
        bd = _browse_description(target, direction, reftype, refsubtypes, nodeClassMask, resultMask)

        async def _do() -> list[ns0.datatypes.ReferenceDescription]:
            return self._browse_references(target, bd)

        return self._maybe_async(_do())

    def browsePage(
        self,
        target: NodeIdLike,
        *,
        maxReferences: int = 0,
        direction: ns0.datatypes.BrowseDirection = ns0.datatypes.BrowseDirection.FORWARD,
        reftype: NodeIdLike = ns0.reftypes.HierarchicalReferences,
        refsubtypes: bool = True,
        nodeClassMask: int = ns0.datatypes.NodeClass.UNSPECIFIED,
        resultMask: int = ns0.datatypes.BrowseResultMask.NONE,
    ) -> MaybeAwaitable[ns0.datatypes.BrowseResult]:
        """Fetch one page of references.

        Args:
            target: The node to browse from.
            maxReferences: Cap on returned references. `0` means no cap, and any
                cap can leave a continuation point for `browseNext`.
            direction: `FORWARD`, `INVERSE`, or `BOTH`.
            reftype: Only follow this ReferenceType. Defaults to
                `HierarchicalReferences`.
            refsubtypes: Also follow subtypes of `reftype`.
            nodeClassMask: Only return nodes of these NodeClasses, as the
                `UInt32` the service takes. Compose the `NodeClass` members you
                want with `|`. `UNSPECIFIED` returns all.
            resultMask: Which reference fields to fill in, as the `UInt32` the
                service takes. Compose the `BrowseResultMask` members you want
                with `|`. `NONE` returns only the target NodeIds.

        Returns:
            The `BrowseResult`, holding the references and a continuation point
            when the result was truncated. Synchronous callers receive it
            directly. Async tasks must await the call, on either the server's
            loop or another loop. This applies to both Node and NodeId targets.

        Raises:
            StatusCodeError: The Browse call failed.
        """
        bd = _browse_description(target, direction, reftype, refsubtypes, nodeClassMask, resultMask)

        async def _do() -> ns0.datatypes.BrowseResult:
            result = self._browse_node(target, int(maxReferences), bd)
            result.statusCode.check()
            return result

        return self._maybe_async(_do())

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
            continuationPoint: One token or a list/tuple of tokens from previous
                pages. Tokens belong to this server and must be released when
                paging is abandoned.

        Returns:
            A list of `BrowseResult` pages, one per token, including when only
            one token was supplied. A release returns empty pages. Sync callers
            receive the list directly; async tasks must await it.

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

        return self._maybe_async(_do())

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

        The arguments match [`browse`][o6.server.Server.browse], and the
        traversal is depth-unbounded, so scope it with
        `reftype` and `nodeClassMask` on a large address space.

        Returns:
            Every reachable node as a flat list of `ExpandedNodeId` values.

        Raises:
            StatusCodeError: The traversal failed.
        """
        bd = _browse_description(target, direction, reftype, refsubtypes, nodeClassMask, resultMask)

        async def _do() -> Any:
            r = super(Server, self)._browse_recursive(bd)
            return (await r) if inspect.isawaitable(r) else r

        return self._maybe_async(_do())

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
            One BrowsePathResult for a scalar input, or a list in input order.
            Each result retains its status, including partial/unresolved paths;
            an empty list returns an empty list. Await in async code.

        Raises:
            StatusCodeError: The service failed. Use
                `serviceTranslateBrowsePathsToNodeIds` for raw requests/responses.
        """
        return self._maybe_async(_translate_paths(self.translateBrowsePaths, browsePath))

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
            origin: Node at which the path starts.
            browsePath: One QualifiedName/string or a list/tuple forming one path.

        Returns:
            One BrowsePathResult, retaining unresolved-path status. Await in
            async code. Unlike `browseRecursive`, this follows a specified path.
        """
        return self.translateBrowsePathsToNodeIds(_simplified_browse_path(origin, browsePath))

    def forEachChildNode(  # type: ignore[override]
        self,
        nodeId: NodeIdLike,
        callback: Callable[[o6.NodeId, bool, o6.NodeId], Any],
    ) -> MaybeAwaitable[None]:
        """Visit every reference of one node without building a result list.

        The cheapest way to walk a node's references, because nothing is
        allocated per reference. The callback runs on the server's event loop
        while the node is locked, so it must not block or call back into the
        server.

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

        return self._maybe_async(_do())

    # -- Discovery Server ----------------------------------------------------------------

    @public_result
    def registerDiscovery(
        self,
        url: str,
        semaphoreFilePath: str | Path | None = None,
    ) -> MaybeAwaitable[None]:
        """Register this server at a Discovery Server (LDS).

        Args:
            url: The LDS endpoint URL, e.g. `"opc.tcp://localhost:4840"`.
            semaphoreFilePath: Path to a semaphore file used to coordinate
                shutdown across several instances. `None` sends an empty path.

        Raises:
            StatusCodeError: The registration failed.
        """
        path_arg = str(semaphoreFilePath) if semaphoreFilePath is not None else None
        return self._on_event_loop(lambda: super(Server, self)._register_discovery(url, path_arg))

    @public_result
    def deregisterDiscovery(self, url: str) -> MaybeAwaitable[None]:
        """Deregister this server from a Discovery Server (LDS).

        Should be called once during server shutdown.

        Args:
            url: The LDS endpoint URL that was passed to `registerDiscovery`.

        Raises:
            StatusCodeError: The deregistration failed.
        """
        return self._on_event_loop(lambda: super(Server, self)._deregister_discovery(url))

    def setRegisterServerCallback(
        self,
        callback: Callable[[dict], None] | None,
    ) -> None:
        """Install / remove the callback invoked when another server
        registers with this LDS.

        The callback receives a single `dict` argument with keys:
        `server_uri`, `product_uri`, `discovery_urls` (list of str),
        `last_discovery_timestamp`.

        Pass `None` to remove the callback."""
        return self._on_event_loop(
            lambda: super(Server, self)._set_register_server_callback(
                synchronous(callback) if callable(callback) else callback
            )
        )

    def setServerOnNetworkCallback(
        self,
        callback: Callable[[dict], None] | None,
    ) -> None:
        """Install / remove the callback invoked when another server is
        detected on the network (via mDNS).

        The callback receives a single `dict` argument with keys:
        `record_id`, `server_name`, `discovery_url`,
        `server_capabilities` (list of str), `last_announce_time`,
        `next_announce_time`, `last_online_time`,
        `is_server_announce` (bool), `is_txt_received` (bool).

        Pass `None` to remove the callback.  Requires
        `UA_ENABLE_DISCOVERY_MULTICAST` in the open62541 build."""
        if not _HAS_SERVER_ON_NETWORK_CALLBACK:
            raise NotImplementedError(
                "set_server_on_network_callback requires "
                "UA_ENABLE_DISCOVERY_MULTICAST in the open62541 build"
            )
        return self._on_event_loop(
            lambda: super(Server, self)._set_server_on_network_callback(
                synchronous(callback) if callback is not None else None
            )
        )

    def _register_server_locally(self, registeredServer: "ns0.datatypes.RegisteredServer") -> None:
        """Local API for the RegisterServer2 service — test-only trigger for
        `onDiscoveryRegisterServerNotification`; not part of the public API.
        Requires `config.applicationType = ApplicationType.DISCOVERYSERVER`,
        or open62541 answers `BadServiceUnsupported`."""
        return self._on_event_loop(lambda: super(Server, self)._register_server(registeredServer))

    def _deregister_server_locally(self, serverUri: str, discoveryUrls: Iterable[str] = ()) -> None:
        """Remove a server record added via `_register_server_locally` —
        test-only, not part of the public API."""
        return self._on_event_loop(
            lambda: super(Server, self)._deregister_server(serverUri, list(discoveryUrls))
        )

    def _register_server_on_network_locally(
        self,
        serverOnNetwork: "ns0.datatypes.ServerOnNetwork",
        remoteAddress: str | None = None,
        ttl: int | None = None,
    ) -> None:
        """Local API for adding/updating a ServerOnNetwork entry —
        test-only trigger for `onDiscoveryServerOnNetworkNotification`; not
        part of the public API. Requires `config.serversOnNetworkEnabled`,
        or open62541 answers `BadNotImplemented`."""
        return self._on_event_loop(
            lambda: super(Server, self)._register_server_on_network(
                serverOnNetwork, remoteAddress, ttl
            )
        )

    def _deregister_server_on_network_locally(self, serverName: str) -> None:
        """Remove a ServerOnNetwork entry by server name — test-only, not
        part of the public API. Requires `config.serversOnNetworkEnabled`,
        or open62541 answers `BadNotImplemented`."""
        return self._on_event_loop(
            lambda: super(Server, self)._deregister_server_on_network(serverName)
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
        """Create a local DataChange o6.subscription.MonitoredItem.

        `callback` is called as::

            callback(monitoredItemId, nodeId, attributeId, data_value, context)

        It may be a regular function or an `async def`. The returned handle
        exposes the Value target, initial mode, `requestedParams`, and backend
        revisions in `params`. Local items support deletion; `modify`,
        `setMonitoringMode`, and `setTriggering` raise `NotImplementedError`.
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
            out = self._on_event_loop(
                lambda: super(Server, self)._create_data_change_monitored_item(
                    mir, ttr, context, synchronous(callback)
                )
            )
            result = await out if inspect.isawaitable(out) else out
            return o6.subscription.MonitoredItem._from_server(self, mir, result)

        return self._maybe_async(_create())

    def deleteMonitoredItem(
        self, monitoredItemId: int | o6.subscription.MonitoredItem
    ) -> MaybeAwaitable[None]:
        """Delete a local monitored item by ID or handle.

        Repeated deletion of a handle is a no-op. Async callers must await
        every call, including repeated deletion.
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
            out = self._on_event_loop(lambda: super(Server, self)._delete_monitored_item(mid))
            if inspect.isawaitable(out):
                await out
            if isinstance(monitoredItemId, o6.subscription.MonitoredItem):
                monitoredItemId._monitored_item_id = None

        return self._maybe_async(_delete())

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
        """Create a local Event o6.subscription.MonitoredItem on *nodeId*.

        Build the filter either piecemeal with `selectClauses=`/`whereClause=`,
        or pass a complete `eventFilter=` — not both. `monitoringMode=`,
        `queueSize=` and `discardOldest=` control the local notification queue.
        `clientHandle=` is retained but is not used to route local callbacks.
        Events are driven by emission, so `samplingInterval=` does not set an
        event polling period. The handle exposes the EventNotifier target,
        filter, initial mode, `requestedParams`, and backend revisions in
        `params`. Local items support deletion; `modify`, `setMonitoringMode`,
        and `setTriggering` raise `NotImplementedError`.

        `callback(monitoredItemId, event_fields, context)` where
        `event_fields` is a `dict[str, Any]` keyed by selected event-filter paths,
        such as `"/Message"` or `"/ConditionName/Id"`.

        Raises:
            TypeError: Both `eventFilter` and `selectClauses`/`whereClause`
                were given.
            ValueError: The effective filter has no select clauses. The
                server would otherwise reject an empty `EventFilter` with
                `BadEventFilterInvalid`.
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
            out = self._on_event_loop(
                lambda: super(Server, self)._create_event_monitored_item(
                    mir, context, synchronous(callback)
                )
            )
            result = await out if inspect.isawaitable(out) else out
            return o6.subscription.MonitoredItem._from_server(self, mir, result)

        return self._maybe_async(_create())

    # -- Server Callbacks ---------------------------------------------------------

    def addRepeatedCallback(self, callback: Callable, intervalMs: float) -> int:
        """Register *callback* to be called every *intervalMs* milliseconds.

        Returns an opaque integer callback ID that can be passed to
        `changeRepeatedCallbackInterval` or `removeCallback`."""
        return self._sync_result(
            self._on_event_loop(
                lambda: super(Server, self)._add_repeated_callback(
                    synchronous(callback), float(intervalMs)
                )
            )
        )

    def changeRepeatedCallbackInterval(self, callbackId: int, intervalMs: float) -> None:
        """Change the interval of an existing repeated callback."""
        cid = int(callbackId)
        return self._sync_result(
            self._on_event_loop(
                lambda: super(Server, self)._change_repeated_callback_interval(
                    cid, float(intervalMs)
                )
            )
        )

    def removeCallback(self, callbackId: int) -> None:
        """Remove a repeated callback by ID."""
        cid = int(callbackId)
        return self._on_event_loop(lambda: super(Server, self)._remove_callback(cid))


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
