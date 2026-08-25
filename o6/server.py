# Copyright 2026 (c) o6 Automation GmbH

import asyncio
import builtins
import concurrent.futures
from dataclasses import dataclass, field
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

import o6
import o6.subscription
from o6 import _server_construction, _server_materialization, _server_types
from o6._node_backend import _ServerBackend, _attribute_id, _server_node, _targets_and_ranges
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
    _infer_data_type,
    _WorkerLoop,
)
from o6.util import _load_cert_or_bytes, _load_cert_list

from o6._declarations import TypeDeclaration, VariableTypeSpec, _CallbackKind

_NodeT = TypeVar("_NodeT", bound=Node)


def _normalize_event_fields(
    fields: Mapping[o6.QualifiedName | str, Any] | None,
) -> dict[o6.QualifiedName | str, Any]:
    return {key: _normalize_nodeids(value) for key, value in (fields or {}).items()}


def _server_proxy(server: "Server") -> "Server":
    """Return a non-owning server reference with the transparent proxy contract."""
    return cast("Server", weakref.proxy(server))


@dataclass
class Event(MutableMapping[o6.QualifiedName | str, Any]):
    """Reusable server-side event draft."""

    _server: "Server" = field(repr=False)
    eventType: NodeIdLike = field(default_factory=lambda: o6.NodeId(ns0.objtypes.BaseEventType))
    source: NodeIdLike = field(default_factory=lambda: ns0.instances.server)
    message: LocalizedTextLike = ""
    severity: int = 1
    fields: dict[o6.QualifiedName | str, Any] = field(default_factory=dict)
    payloadSource: NodeIdLike | None = None

    def __getitem__(self, key: o6.QualifiedName | str) -> Any:
        return self.fields[key]

    def __setitem__(self, key: o6.QualifiedName | str, value: Any) -> None:
        self.fields[key] = value

    def __delitem__(self, key: o6.QualifiedName | str) -> None:
        del self.fields[key]

    def __iter__(self) -> Iterator[o6.QualifiedName | str]:
        return iter(self.fields)

    def __len__(self) -> int:
        return len(self.fields)

    def trigger(self) -> MaybeAwaitable[bytes]:
        return self._server.emitEvent(
            self.eventType,
            source=self.source,
            message=self.message,
            severity=self.severity,
            fields=self.fields,
            payloadSource=self.payloadSource,
        )


@dataclass(frozen=True, eq=False)
class Role:
    name: o6.QualifiedName | str
    id: o6.NodeId | None = None
    identities: tuple[ns0.datatypes.IdentityMappingRuleType, ...] = ()
    applications: tuple[str, ...] = ()
    applicationsExclude: bool = False
    endpoints: tuple[ns0.datatypes.EndpointType, ...] = ()
    endpointsExclude: bool = False

    def __post_init__(self) -> None:
        if isinstance(self.name, str):
            object.__setattr__(self, "name", o6.QualifiedName(0, self.name))
        if self.id is not None and not isinstance(self.id, o6.NodeId):
            object.__setattr__(self, "id", o6.NodeId(self.id))

    def __hash__(self) -> int:
        return hash(self.id if self.id is not None else str(self.name))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Role):
            return NotImplemented
        if self.id is not None and other.id is not None:
            return self.id == other.id
        return str(self.name) == str(other.name)


@dataclass(frozen=True)
class SessionActivation:
    context: Any = None
    roles: tuple[Role | o6.NodeId, ...] = ()


class Session:
    """A safe proxy for a server session, resolved by NodeId on every use."""

    def __init__(self, server: "Server", sessionId: o6.NodeId, context: Any = None) -> None:
        self._server = _server_proxy(server)
        self.id = o6.NodeId(sessionId)
        self.context = context
        self._pending_roles: tuple[Role | o6.NodeId, ...] | None = None

    @property
    def roles(self) -> tuple[Role, ...]:
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
        return self._server._get_session_attribute(self.id, _qualified_name(key))

    def set(self, key: o6.QualifiedName | str, value: Any) -> None:
        self._server._set_session_attribute(self.id, _qualified_name(key), value)

    def delete(self, key: o6.QualifiedName | str) -> None:
        self._server._delete_session_attribute(self.id, _qualified_name(key))

    def close(self) -> None:
        self._server._close_session(self.id)


@dataclass(frozen=True)
class MethodCallback(Protocol):
    def __call__(
        self,
        node: ObjectNode,
        *inputs: Any,
    ) -> tuple[Any, ...] | Awaitable[tuple[Any, ...]]: ...


_CALLBACK_UNSET = object()

_NATIVE_CALLBACK_KIND: dict[_CallbackKind, int] = {"call": 0, "read": 1, "write": 2}


def _is_async_callable(callback: Callable[..., Any]) -> bool:
    return inspect.iscoroutinefunction(callback) or inspect.iscoroutinefunction(
        getattr(callback, "__call__", None)
    )


class VariableReadCallback(Protocol):
    def __call__(
        self,
        node: VariableNode,
        *,
        range: tuple[slice, ...] | None,
        session: Session | None,
        includeSourceTimestamp: bool,
    ) -> tuple[Any, ...]: ...


class VariableWriteCallback(Protocol):
    def __call__(
        self,
        node: VariableNode,
        value: o6.DataValue,
        *,
        range: tuple[slice, ...] | None,
        session: Session | None,
    ) -> tuple[o6.StatusCode]: ...


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


class NodePermissions:
    def __init__(self, server: "Server", nodeId: o6.NodeId) -> None:
        self._server = _server_proxy(server)
        self._node_id = o6.NodeId(nodeId)

    def get(self) -> dict[Role, o6.Permission]:
        return {
            self._server.roles[role_id]: o6.Permission(value)
            for role_id, value in self._server._get_node_role_permissions(self._node_id).items()
        }

    def set(
        self, permissions: Mapping[Role | o6.NodeId, o6.Permission], *, recursive: bool = False
    ) -> None:
        self._server._set_node_role_permissions(
            self._node_id,
            {_role_id(self._server, role): int(value) for role, value in permissions.items()},
            recursive,
        )

    def grant(
        self,
        role: Role | o6.NodeId,
        permissions: o6.Permission,
        *,
        overwrite: bool = False,
        recursive: bool = False,
    ) -> None:
        self._server._add_role_permissions(
            self._node_id, _role_id(self._server, role), int(permissions), overwrite, recursive
        )

    def revoke(
        self, role: Role | o6.NodeId, permissions: o6.Permission, *, recursive: bool = False
    ) -> None:
        self._server._remove_role_permissions(
            self._node_id, _role_id(self._server, role), int(permissions), recursive
        )

    def clear(self, *, recursive: bool = False) -> None:
        self._server._remove_node_role_permissions(self._node_id, recursive)


class AccessControl:
    """Python implementation of the open62541 ``UA_AccessControl`` plugin.

    Subclasses normally override :meth:`activateSession` for authentication
    and optionally override the authorization hooks.  The base authorization
    policy is permissive; the base authentication policy accepts anonymous
    sessions only.
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
        """Authenticate a session and return its context or activation result."""
        if isinstance(userIdentityToken, ns0.datatypes.AnonymousIdentityToken):
            return None
        raise o6.StatusCodeError(o6.StatusCode.BAD_IDENTITY_TOKEN_REJECTED)

    def closeSession(self, session: Session) -> None:
        """Release a context returned by :meth:`activateSession`."""

    def getUserRightsMask(self, session: Session, nodeId: o6.NodeId) -> int:
        return 0xFFFFFFFF

    def getUserAccessLevel(self, session: Session, nodeId: o6.NodeId) -> int:
        return 0xFF

    def getUserExecutable(self, session: Session, methodId: o6.NodeId) -> bool:
        return True

    def getUserExecutableOnObject(
        self,
        session: Session,
        methodId: o6.NodeId,
        objectId: o6.NodeId,
    ) -> bool:
        return True

    def allowAddNode(self, session: Session, item: Any) -> bool:
        return True

    def allowAddReference(self, session: Session, item: Any) -> bool:
        return True

    def allowDeleteNode(self, session: Session, item: Any) -> bool:
        return True

    def allowDeleteReference(self, session: Session, item: Any) -> bool:
        return True

    def allowBrowseNode(self, session: Session, nodeId: o6.NodeId) -> bool:
        return True

    def allowTransferSubscription(
        self,
        oldSession: Session,
        newSession: Session,
    ) -> bool:
        return oldSession.context == newSession.context

    def allowCreateSubscription(self, session: Session) -> bool:
        return True

    def allowHistoryUpdate(
        self,
        session: Session,
        nodeId: o6.NodeId,
        performUpdateType: int,
        value: o6.DataValue,
    ) -> bool:
        return True

    def allowHistoryDelete(
        self,
        session: Session,
        nodeId: o6.NodeId,
        startTimestamp: Any,
        endTimestamp: Any,
        isDeleteModified: bool,
    ) -> bool:
        return True


# =============================================================================
# Server – high-level OPC UA server
# =============================================================================


class _ServerNamespaces:
    """The server-side namespace host: publishes decorator-authored nodeset
    modules into the address space via :meth:`append`.

    It carries no per-instance Python node tree — namespace registration lives
    in the process-wide ``o6.ns`` registry and the OPC UA server's own
    namespace array."""

    def __init__(self, server: "Server") -> None:
        # Avoid keeping the server alive solely through server.ns -> server.
        # This lets the weak live-server registry forget local servers as soon
        # as user code releases them.
        self._server = _server_proxy(server)
        self._nodeset_modules: list[ModuleType] = []

    def set_default_permissions(
        self, namespace: int | str, permissions: Mapping[Role | o6.NodeId, o6.Permission]
    ) -> None:
        index = (
            namespace
            if isinstance(namespace, int)
            else self._server._get_namespace_index(namespace)
        )
        self._server._set_namespace_role_permissions(
            index, {_role_id(self._server, role): int(value) for role, value in permissions.items()}
        )

    def get_default_permissions(self, namespace: int | str) -> dict[Role, o6.Permission]:
        index = (
            namespace
            if isinstance(namespace, int)
            else self._server._get_namespace_index(namespace)
        )
        return {
            self._server.roles[role_id]: o6.Permission(value)
            for role_id, value in self._server._get_namespace_role_permissions(index).items()
        }

    def append(self, ns: ModuleType) -> None:
        """Publish a nodeset module authored with the ``@o6`` decorators.

        The module must have called :func:`o6.ns.namespace` (one or more
        times) at import time; every namespace module recorded in its
        ``__NAMESPACES__`` set is registered with this server, then the
        module's decorated nodes are injected into the address space."""
        ns_infos = getattr(ns, "__NAMESPACES__", None)
        if ns_infos is None:
            raise ValueError(f"Module {ns.__name__} has no __NAMESPACES__ metadata")

        if ns in self._nodeset_modules:
            return

        published_uris = {
            info.uri
            for module in self._nodeset_modules
            for info in getattr(module, "__NAMESPACES__", ())
        }
        module_uris = {info.uri for info in ns_infos}
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
        self._nodeset_modules.append(ns)

        self._inject_nodes(ns)

    def _inject_nodes(self, ns: ModuleType) -> None:
        _server_materialization._publish_namespace(self._server, ns, self._nodeset_modules)


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
    """High-level OPC UA Server.

    Parameters
    ----------
    port : int, optional
        TCP port number (default 4840).
    logger : logging.Logger, optional
        Custom logger object.
    loop : asyncio.AbstractEventLoop, optional
        Event loop used for cooperative scheduling.
        When provided (or when a running loop is detected), the server
        avoids spawning a background thread and instead schedules
        non-blocking iterations on the loop.  If *None* and no running
        loop exists, a daemon thread is used as a fallback.
    certificate : str, Path, or bytes, optional
        Server certificate (file path or raw bytes).
    privateKey : str, Path, or bytes, optional
        Server private key (file path or raw bytes).
    trustList : list, optional
        Trusted certificates for client verification.
    issuerList : list, optional
        Issuer certificates.
    revocationList : list, optional
        Certificate revocation lists.
    secureOnly : bool
        If True, reject unencrypted connections (default False).
    acceptAllCertificates : bool
        If True, trust all client certificates (default False).
    applicationUri : str, optional
        Override the default application URI.

    Example
    -------
    >>> server = Server(port=4840)
    >>> with server:
    ...     temp = server.addVariable("Temperature",
    ...                                server.objectsNode, 22.5)
    ...     print(temp())
    22.5"""

    ns: _ServerNamespaces
    _loop: asyncio.AbstractEventLoop

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
        _requireServer()
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
        self._node_backend = _ServerBackend(self)
        for marker in _server_materialization._collect_variabletype_markers(ns0):
            self._attach_instance_type(marker, VariableNode)
        self.roles = _RoleRegistry(self)
        self._set_all_permissions_for_anonymous(not rbacForAnonymous)

        if applicationUri is not None:
            self.config.applicationUri = applicationUri

        # Apply encryption if certificate and key are provided
        cert_bytes = _load_cert_or_bytes(certificate)
        key_bytes = _load_cert_or_bytes(privateKey)
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
        # config, so install transport authentication and access control last.
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
        """Install server-local Python behavior on a UA type or concrete node.

        A declaration plus an undecorated implementation class selects how
        future instances of that UA type are constructed. Passing ``None``
        restores the declaration's own Python type for future instances.

        Passing ``None`` positionally for a concrete Method or Variable
        restores the callback resolution performed during construction. A
        concrete value positionally supplied for a Variable removes both
        callbacks and installs that value in native storage.

        ``call=``, ``read=``, and ``write=`` replace or clear callback slots on
        a Method, Variable, or VariableType. Existing concrete instances are
        never changed by a type-level update.
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
        eventType: NodeIdLike = ns0.objtypes.BaseEventType,
        *,
        source: NodeIdLike = ns0.instances.server,
        message: LocalizedTextLike = "",
        severity: int = 1,
        fields: Mapping[o6.QualifiedName | str, Any] | None = None,
        payloadSource: NodeIdLike | None = None,
    ) -> Event:
        """Create a reusable event draft without emitting it."""
        if not 1 <= severity <= 1000:
            raise ValueError("event severity must be between 1 and 1000")
        return Event(
            self,
            eventType=o6.NodeId(eventType),
            source=o6.NodeId(source),
            message=message,
            severity=severity,
            fields=_normalize_event_fields(fields),
            payloadSource=(o6.NodeId(payloadSource) if payloadSource is not None else None),
        )

    def emitEvent(
        self,
        eventType: NodeIdLike = ns0.objtypes.BaseEventType,
        *,
        source: NodeIdLike = ns0.instances.server,
        message: LocalizedTextLike = "",
        severity: int = 1,
        fields: Mapping[o6.QualifiedName | str, Any] | None = None,
        payloadSource: NodeIdLike | None = None,
    ) -> MaybeAwaitable[bytes]:
        """Emit an event and return its generated EventId."""
        if not 1 <= severity <= 1000:
            raise ValueError("event severity must be between 1 and 1000")
        localized_message = (
            message if isinstance(message, o6.LocalizedText) else o6.LocalizedText(message)
        )
        return self._on_event_loop(
            lambda: super(Server, self)._emit_event(
                o6.NodeId(source),
                o6.NodeId(eventType),
                severity,
                localized_message,
                _normalize_event_fields(fields),
                o6.NodeId(payloadSource) if payloadSource is not None else None,
            )
        )

    # -- Thread-safe dispatch ------------------------------------------------

    def _maybe_async_coro(self, coro: Any) -> MaybeAwaitable:
        try:
            caller_loop = asyncio.get_running_loop()
        except RuntimeError:
            caller_loop = None

        if caller_loop is None:
            if self._loop.is_running():
                # Worker thread owns the loop — post from outside and block.
                fut: concurrent.futures.Future = concurrent.futures.Future()

                async def _run():
                    try:
                        fut.set_result(await coro)
                    except Exception as exc:
                        fut.set_exception(exc)

                self._loop.call_soon_threadsafe(lambda: self._loop.create_task(_run()))
                return fut.result()
            else:
                return self._loop.run_until_complete(coro)

        # Caller is on a different loop — return an awaitable.
        cfut = asyncio.run_coroutine_threadsafe(coro, self._loop)
        return asyncio.wrap_future(cfut)

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

        if loop is None or asyncio.current_task() is None or hasattr(builtins, "__IPYTHON__"):
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
        afut = asyncio.wrap_future(fut)
        afut._concurrent_future = fut  # type: ignore[attr-defined]
        original_result = cast(Callable[[float | None], Any], afut.result)

        def result(timeout: float | None = None) -> Any:
            if not afut.done():
                return fut.result(timeout)
            return original_result(timeout)

        afut.result = result  # type: ignore[assignment]
        return afut

    def _on_event_loop(self, fn: Callable[[], Any]) -> Any:
        # No worker thread yet, or already on it — call directly
        if self._worker is None or not self._worker.running or self._worker.on_loop_thread:
            out = fn()
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

        # Schedule fn() on the worker loop and collect the result via a
        # thread-safe concurrent.futures.Future
        fut: concurrent.futures.Future = concurrent.futures.Future()

        def _call() -> None:
            try:
                out = fn()
                if asyncio.isfuture(out) or inspect.isawaitable(out):
                    task = asyncio.ensure_future(out, loop=self._loop)

                    def _complete(task: asyncio.Future) -> None:
                        try:
                            fut.set_result(task.result())
                        except BaseException as exc:
                            fut.set_exception(exc)

                    task.add_done_callback(_complete)
                else:
                    fut.set_result(out)
            except BaseException as exc:
                fut.set_exception(exc)

        try:
            self._loop.call_soon_threadsafe(_call)
        except RuntimeError as exc:
            fut.set_exception(exc)

        # Sync caller (no running loop) or same loop — block until done
        if caller_loop is None or caller_loop is self._loop or asyncio.current_task() is None:
            return fut.result()

        # Async task on a different running loop — return an awaitable.
        return self._wrap_future(fut, caller_loop)

    # -- Well-known nodes (convenience properties) ---------------------------

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
    def endpointUrl(self) -> str:
        return f"opc.tcp://localhost:{self._port}"

    # -- Lifecycle -----------------------------------------------------------

    def start(self) -> None:
        """Start the server networking layer.

        The asyncio event loop handles all I/O, timers, and callbacks.
        When no running loop is detected (synchronous callers), a
        lightweight background daemon thread drives the loop instead."""
        _register_live_server(self)
        if self.running:
            return

        if self._loop.is_running():
            # Async context: the loop is already running, startup directly.
            self._run_startup()
        else:
            # Sync fallback: start the event loop in a background thread
            # first, then call run_startup from the loop thread so that
            # create_server() tasks execute immediately.
            self._worker = _WorkerLoop(self._loop)
            self._worker.start()
            fut: concurrent.futures.Future = concurrent.futures.Future()

            def _do_startup():
                try:
                    self._run_startup()
                    fut.set_result(None)
                except Exception as e:
                    fut.set_exception(e)

            self._loop.call_soon_threadsafe(_do_startup)
            fut.result(timeout=5.0)

    def stop(self) -> None:
        """Shut down the server."""
        _unregister_live_server(self)
        if not self.running:
            return
        if self._worker is not None and self._worker.running:
            # Sync fallback: run_shutdown from the loop thread, then
            # keep the loop alive until the server reaches STOPPED so
            # that asyncio transport close events (connection_lost) and
            # subscription timers can complete the teardown.
            fut: concurrent.futures.Future = concurrent.futures.Future()

            async def _shutdown_and_drain():
                try:
                    self._run_shutdown()
                    # Give asyncio a few cycles so transport close events
                    # (connection_lost) and pending timer callbacks can fire
                    # before we tear down the event loop.
                    for i in range(10):  # up to ~0.5 s
                        if self._is_fully_stopped:
                            break
                        await asyncio.sleep(0.05)
                    # A couple of extra iterations so asyncio fully processes
                    # the pending transport.close() / server.close() calls
                    # that the C event source stop scheduled.  The selector
                    # may need more than one pass to unregister the listening
                    # socket, so a single sleep(0) is not always sufficient.
                    for _ in range(10):
                        await asyncio.sleep(0)
                    # Stop the C event loop while asyncio is still live so
                    # that listener/connection cleanup can safely use Python
                    # APIs.  Without this, pyServer_clear (tp_dealloc) would
                    # call el->stop during GC, where PyObject_CallMethod on
                    # transport.close() can segfault.
                    self._stop_event_loop()
                    fut.set_result(None)
                except Exception as e:
                    fut.set_exception(e)

            self._loop.call_soon_threadsafe(lambda: self._loop.create_task(_shutdown_and_drain()))
            fut.result(timeout=10.0)

            # Stop the worker thread but keep the asyncio loop alive so
            # subsequent sync configuration / calls can still drive it via
            # ``run_until_complete``.  The loop is closed in ``__del__``.
            self._worker.stop(close=False)
            self._worker = None
        else:
            self._run_shutdown()
            self._stop_event_loop()

    def __enter__(self) -> "Server":
        self.start()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.stop()

    async def __aenter__(self) -> "Server":
        self.start()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.stop()

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

    def addReverseConnect(
        self,
        url: str,
        callback: Callable[[int, int], None] | None = None,
    ) -> int:
        """Register a reverse connect to a client listening at *url*.

        The server will periodically attempt to establish a connection
        to the given client endpoint (e.g. ``opc.tcp://localhost:4841``).

        Parameters
        ----------
        url : str
            The OPC UA endpoint URL of the listening client.
        callback : callable, optional
            Called with ``(handle, state)`` on every state change.

        Returns
        -------
        int
            A handle that can be passed to :meth:`removeReverseConnect`."""
        return self._on_event_loop(lambda: super(Server, self)._add_reverse_connect(url, callback))

    def removeReverseConnect(self, handle: int) -> None:
        """Remove a reverse connect registration.

        Parameters
        ----------
        handle : int
            The handle returned by :meth:`addReverseConnect`."""
        self._on_event_loop(lambda: super(Server, self)._remove_reverse_connect(handle))

    # -- Add nodes (high-level) -----------------------------------------------

    def _create_node(
        self,
        add_thunk: Callable[[], Any],
        browse_name: o6.QualifiedName,
        node_cls: type[_NodeT],
    ) -> _NodeT:
        """Run a low-level ``add_*_node`` call on the event loop and wrap the
        returned NodeId in the given high-level Node subclass."""
        out_id = self._on_event_loop(add_thunk)
        return super()._get_node(out_id, node_cls, self._node_backend)

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
        historizing: bool = False,
        ns: int = 1,
    ) -> VariableNode:
        """Add a variable node to the address space.

        Parameters
        ----------
        name : str or LocalizedText
            Browse name (and display name) of the variable.
        parent : NodeIdLike
            Parent node (typically ``server.objectsNode``).
        value : any, optional
            Initial value. The OPC UA data-type is inferred automatically
            unless *dataType* is given explicitly.
        nodeId : NodeIdLike, optional
            Requested node id.  ``None`` -> server assigns one.
        dataType : NodeIdLike, optional
            Explicit data type.  If ``None``, inferred from *value*.
        typeDefinition : NodeIdLike, optional
            VariableType used for the new node.
        writable : bool
            Whether the variable is writable by clients (default ``True``).
        historizing : bool
            Whether the variable supports historical data access (default ``False``).
        ns : int
            Namespace index for the browse name (default 1).
        Returns
        -------
        VariableNode"""
        parent_id = o6.NodeId(parent)
        requested_id = o6.NodeId(nodeId)

        # Infer data type
        if dataType is not None:
            dt_id = o6.NodeId(dataType)
            # Still derive value_rank from the value so arrays work correctly
            # when data_type is given explicitly.
            if value is not None:
                _, value_rank = _infer_data_type(value)
            else:
                value_rank = -1
        elif value is not None:
            dt_id, value_rank = _infer_data_type(value)
        else:
            dt_id = o6.NodeId(o6.Int32)
            value_rank = -1

        # Build attributes
        attr = ns0.datatypes.VariableAttributes()
        attr.displayName = o6.LocalizedText(name)
        attr.dataType = dt_id
        attr.valueRank = value_rank
        if value_rank >= 1:
            # OPC UA spec requires array_dimensions to have exactly value_rank
            # elements. Use 0 for each dimension to mean "any length".
            attr.arrayDimensions = [o6.UInt32(0)] * value_rank

        access = 0
        if writable:
            access = 3  # Read | Write
        else:
            access = 1  # Read only
        if historizing:
            access |= 4 | 8  # HistoryRead | HistoryWrite
            attr.historizing = True
        attr.accessLevel = access
        attr.userAccessLevel = access

        if value is not None:
            # numpy arrays must not be embedded in VariableAttributes.value —
            # open62541 rejects array variants during add_variable_node type-check.
            # Scalars are safe to embed; arrays are written via write_value below.
            try:
                import numpy as _np

                _is_array = isinstance(value, _np.ndarray)
            except ImportError:
                _is_array = False
            if not _is_array:
                attr.value = o6.Double(value) if isinstance(value, float) else value

        browse_name = o6.QualifiedName(f"{ns}:{name}")
        type_def = o6.NodeId(typeDefinition)

        out_id = self._on_event_loop(
            lambda: self._add_variable_node(
                requested_id,
                parent_id,
                o6.NodeId(ns0.reftypes.Organizes),
                browse_name,
                type_def,
                attr,
            )
        )

        # Write the value separately if provided – ensures variant wrapper is correct
        if value is not None:
            v = o6.Double(value) if isinstance(value, float) else value
            self._on_event_loop(lambda: super(Server, self)._write_value(out_id, v))

        node_type = self._variable_instance_type(type_def)
        return super()._get_node(out_id, node_type, self._node_backend)

    def addObject(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike,
        *,
        nodeId: NodeIdLike | None = None,
        typeDefinition: NodeIdLike = o6.NodeId(ns0.objtypes.BaseObjectType),
        ns: int = 1,
    ) -> ObjectNode:
        """Add an object node to the address space.

        Parameters
        ----------
        name : str or LocalizedText
            Browse name / display name.
        parent : NodeIdLike
            Parent node.
        nodeId : NodeIdLike, optional
            Requested node id.
        typeDefinition : NodeIdLike, optional
            Type definition node (default: BaseObjectType i=58).
        ns : int
            Namespace index for the browse name.
        Returns
        -------
        ObjectNode"""
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
                o6.NodeId(ns0.reftypes.Organizes),
                browse_name,
                type_def,
                attr,
            ),
            browse_name,
            ObjectNode,
        )

    def addObjectType(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike = o6.NodeId(ns0.objtypes.BaseObjectType),
        *,
        nodeId: NodeIdLike | None = None,
        ns: int = 1,
    ) -> ObjectTypeNode:
        """Add an object type node.

        Parameters
        ----------
        name : str or LocalizedText
            Browse name / display name.
        parent : NodeIdLike, optional
            Parent type node (default: BaseObjectType i=58).
        nodeId : NodeIdLike, optional
            Requested node id.
        ns : int
            Namespace index for the browse name.
        Returns
        -------
        ObjectTypeNode"""
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
            browse_name,
            ObjectTypeNode,
        )

    def addVariableType(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike = o6.NodeId(ns0.vartypes.BaseVariableType),
        *,
        dataType: NodeIdLike = o6.NodeId(o6.Double),
        valueRank: int = -1,
        nodeId: NodeIdLike | None = None,
        ns: int = 1,
    ) -> VariableTypeNode:
        """Add a variable type node.

        Parameters
        ----------
        name : str or LocalizedText
            Browse name / display name.
        parent : NodeIdLike, optional
            Parent type (default: BaseVariableType i=62).
        dataType : NodeIdLike, optional
            Data type (default: Double i=11).
        valueRank : int
            Value rank (default: -1 = scalar).
        nodeId : NodeIdLike, optional
            Requested node id.
        ns : int
            Namespace index for the browse name.
        Returns
        -------
        VariableTypeNode"""
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
            browse_name,
            VariableTypeNode,
        )

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
    ) -> ReferenceTypeNode:
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
            browse_name,
            ReferenceTypeNode,
        )

    def addView(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike = ns0.instances.views,
        *,
        eventNotifier: int = 0,
        containsNoLoops: bool = True,
        nodeId: NodeIdLike | None = None,
        ns: int = 1,
    ) -> ViewNode:
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
            browse_name,
            ViewNode,
        )

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
    ) -> MethodNode:
        """Add a method node to the address space.

        Parameters
        ----------
        name : str or LocalizedText
            Browse name / display name.
        parent : NodeIdLike
            Parent node (typically an object node).
        callback : callable
            Python function called when a client invokes the method.
            Signature: ``callback(node, *inputs) -> (StatusCode, *outputs)``.
        inputArgs : list of Argument, optional
            Input argument descriptors.
        outputArgs : list of Argument, optional
            Output argument descriptors.
        nodeId : NodeId, optional
            Requested node id.
        ns : int
            Namespace index for the browse name.
        Returns
        -------
        MethodNode
            The unbound server Method node. Invoke it with ``object=parent``,
            or reach it through the parent Object's dot syntax to obtain a
            bound call.
        """
        parent_id = o6.NodeId(parent)
        requested_id = o6.NodeId(nodeId)

        attr = ns0.datatypes.MethodAttributes()
        attr.displayName = o6.LocalizedText(name)
        attr.executable = True
        attr.userExecutable = True

        browse_name = o6.QualifiedName(f"{ns}:{name}")
        out_id = self._on_event_loop(
            lambda: self._add_method_node(
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
        )
        node = super()._get_node(out_id, MethodNode, self._node_backend)
        parent_node = _server_node(self, parent_id, ObjectNode)
        node._construction_owner = parent_node
        self.implement(node, call=callback)
        return node

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
                if _is_async_callable(cast(Callable[..., Any], value)):
                    raise TypeError("Variable callbacks cannot be async")

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

    def addReference(  # type: ignore[override]
        self,
        source: NodeIdLike,
        target: NodeIdLike,
        referenceType: NodeIdLike,
        *,
        forward: bool = True,
    ) -> None:
        """Add a reference between two nodes.

        Args:
            source: Source node id.
            target: Target NodeId or ExpandedNodeId. An ExpandedNodeId may name
                a node on another server.
            referenceType: Reference type NodeId.
            forward: ``True`` for a forward reference, ``False`` for inverse."""
        src_id = o6.NodeId(source)
        tgt_id = (
            target
            if isinstance(target, o6.ExpandedNodeId)
            else o6.ExpandedNodeId(o6.NodeId(target))
        )
        ref_id = o6.NodeId(referenceType)
        self._on_event_loop(
            lambda: super(Server, self)._add_reference(src_id, ref_id, tgt_id, forward)
        )

    def _add_reference_once(
        self,
        source: NodeIdLike,
        target: NodeIdLike,
        reference_type: NodeIdLike,
        *,
        forward: bool = True,
    ) -> None:
        """Add an exact edge, accepting one already materialized by open62541."""
        try:
            self.addReference(source, target, reference_type, forward=forward)
        except o6.StatusCodeError as exc:
            if exc.code != o6.StatusCode.BAD_DUPLICATE_REFERENCE_NOT_ALLOWED:
                raise

    def deleteReference(
        self,
        source: NodeIdLike,
        target: NodeIdLike,
        referenceType: NodeIdLike,
        *,
        forward: bool = True,
        bidirectional: bool = True,
    ) -> None:
        """Delete a reference between two nodes."""
        src_id = o6.NodeId(source)
        tgt_id = (
            target
            if isinstance(target, o6.ExpandedNodeId)
            else o6.ExpandedNodeId(o6.NodeId(target))
        )
        ref_id = o6.NodeId(referenceType)
        self._on_event_loop(
            lambda: super(Server, self)._delete_reference(
                src_id, ref_id, tgt_id, forward, bidirectional
            )
        )

    def deleteNode(  # type: ignore[override]
        self,
        nodeId: NodeIdLike,
        *,
        deleteReferences: bool = True,
    ) -> None:
        """Delete a node from the address space.

        Args:
            nodeId: The node id to delete.
            deleteReferences: If ``True`` (default), also delete references
                pointing to the node."""
        nid = o6.NodeId(nodeId)
        self._on_event_loop(lambda: super(Server, self)._delete_node(nid, deleteReferences))

    # -- Method call ----------------------------------------------------------

    def call(  # type: ignore[override]
        self,
        objectId: NodeIdLike,
        methodId: NodeIdLike,
        inputArgs: list[Any] = [],
    ) -> MaybeAwaitable[tuple]:
        """Call a method node server-side with admin privileges.

        Matches ``client.call()`` — returns ``(StatusCode, *output_arguments)``.

        Parameters
        ----------
        objectId : NodeIdLike
            The object node that owns the method.
        methodId : NodeIdLike
            The method node to invoke.
        inputArgs : list, optional
            Input argument values.

        Returns
        -------
        tuple
            ``(status_code, output1, output2, ...)``"""
        obj_id = o6.NodeId(objectId)
        mth_id = o6.NodeId(methodId)
        args = [_normalize_nodeids(arg) for arg in inputArgs] if inputArgs else []

        async def _do() -> tuple:
            return await super(Server, self)._call(obj_id, mth_id, args)

        return self._maybe_async(_do())

    def _setPubSubConnectionEnabled(self, connectionId: NodeIdLike, enabled: bool) -> None:
        """Set native PubSub connection state (internal component bridge)."""
        node_id = o6.NodeId(connectionId)
        self._on_event_loop(
            lambda: super(Server, self)._set_pubsub_connection_enabled(node_id, enabled)
        )

    def _setPubSubComponentEnabled(self, componentId: NodeIdLike, enabled: bool) -> None:
        """Set one native PubSub component state."""
        node_id = o6.NodeId(componentId)
        self._on_event_loop(
            lambda: super(Server, self)._set_pubsub_component_enabled(node_id, enabled)
        )

    def _removePubSubConnection(self, connectionId: NodeIdLike) -> None:
        """Remove a native PubSub connection and all child components."""
        node_id = o6.NodeId(connectionId)
        self._on_event_loop(lambda: super(Server, self)._remove_pubsub_connection(node_id))

    def _setAllPubSubComponentsEnabled(self, enabled: bool) -> None:
        """Enable or disable the complete native PubSub component tree."""
        self._on_event_loop(lambda: super(Server, self)._set_all_pubsub_components_enabled(enabled))

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
        attr: o6.AttributeId | str = o6.AttributeId.VALUE,
        *,
        range: o6.IndexRange | list[o6.IndexRange] = None,
    ) -> MaybeAwaitable[Any]:
        """Read one or more node attributes from the server.

        Args:
            target: A single node id or a list of node ids.
            attr: The attribute to read; defaults to ``o6.AttributeId.VALUE``.
                Can also be an attribute name string.
            range: An OPC UA range string, a Python slice, or a tuple of
                slices. A list supplies one range per target.

        Returns:
            The attribute value (or list of values when ``target`` is a list)."""
        attr = _attribute_id(attr)
        if range is not None and attr != o6.AttributeId.VALUE:
            raise ValueError("range is only supported for the Value attribute")

        is_scalar, targets, ranges = _targets_and_ranges(target, range)
        if not is_scalar:

            async def _do_list() -> list:
                results = []
                for item, index_range in zip(targets, ranges):
                    nid = o6.NodeId(item)
                    if attr == o6.AttributeId.VALUE:
                        results.append(await super(Server, self)._read_value(nid, index_range))
                    else:
                        results.append(await super(Server, self)._read_attribute(nid, int(attr)))
                return results

            return self._maybe_async(_do_list())

        nid = o6.NodeId(targets[0])
        attr_id = int(attr)

        async def _do() -> Any:
            if attr == o6.AttributeId.VALUE:
                return await super(Server, self)._read_value(nid, ranges[0])
            return await super(Server, self)._read_attribute(nid, attr_id)

        return self._maybe_async(_do())

    def write(
        self,
        target: NodeIdLike | list[NodeIdLike],
        value: Any,
        attr: o6.AttributeId | str = o6.AttributeId.VALUE,
        *,
        range: o6.IndexRange | list[o6.IndexRange] = None,
    ) -> MaybeAwaitable[None]:
        """Write one or more node attributes on the server.

        If ``value`` is a :class:`o6.DataValue`, it is written directly via
        ``UA_Server_writeDataValue`` — preserving any explicit status code
        and timestamps stored in the object.  Otherwise the value is wrapped
        in a DataValue before writing.

        Args:
            target: A single node id or a list of node ids.
            value: Value (or DataValue) to write.
            attr: The attribute to write; defaults to ``o6.AttributeId.VALUE``.
            range: An OPC UA range string, a Python slice, or a tuple of
                slices. A list supplies one range per target.
        """
        attr = _attribute_id(attr)
        if range is not None and attr != o6.AttributeId.VALUE:
            raise ValueError("range is only supported for the Value attribute")

        is_scalar, targets, ranges = _targets_and_ranges(target, range)
        if not is_scalar:

            async def _do_list() -> None:
                for item, index_range in zip(targets, ranges):
                    nid = o6.NodeId(item)
                    if isinstance(value, o6.DataValue):
                        await super(Server, self)._write_data_value(nid, value, index_range)
                    elif attr == o6.AttributeId.VALUE:
                        v = o6.Double(value) if isinstance(value, float) else value
                        await super(Server, self)._write_value(nid, v, index_range)
                    else:
                        await super(Server, self)._write_attribute(nid, int(attr), value)

            return self._maybe_async(_do_list())

        nid = o6.NodeId(targets[0])
        attr_id = int(attr)

        async def _do() -> None:
            index_range = ranges[0]
            if isinstance(value, o6.DataValue):
                await super(Server, self)._write_data_value(nid, value, index_range)
                return
            if attr == o6.AttributeId.VALUE:
                v = o6.Double(value) if isinstance(value, float) else value
                await super(Server, self)._write_value(nid, v, index_range)
                return
            await super(Server, self)._write_attribute(nid, attr_id, value)

        return self._maybe_async(_do())

    def translateBrowsePaths(  # type: ignore[override]
        self,
        request: Any,
    ) -> MaybeAwaitable[Any]:
        """Server-side translate browse paths to node ids.

        Args:
            request: A ``TranslateBrowsePathsToNodeIdsRequest`` instance.

        Returns:
            The corresponding response."""

        async def _do() -> Any:
            r = super(Server, self)._translate_browse_paths(request)
            return (await r) if inspect.isawaitable(r) else r

        return self._maybe_async(_do())

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
        maxReferences: int = 0,
        direction: ns0.datatypes.BrowseDirection = ns0.datatypes.BrowseDirection.FORWARD,
        reftype: NodeIdLike = ns0.reftypes.HierarchicalReferences,
        refsubtypes: bool = True,
        nodeClassMask: ns0.datatypes.NodeClass = ns0.datatypes.NodeClass.UNSPECIFIED,
        resultMask: ns0.datatypes.BrowseResultMask = ns0.datatypes.BrowseResultMask(0),
    ):
        bd = ns0.datatypes.BrowseDescription()
        bd.nodeId = o6.NodeId(target)
        bd.browseDirection = direction
        bd.referenceTypeId = o6.NodeId(reftype)
        bd.includeSubtypes = refsubtypes
        bd.nodeClassMask = nodeClassMask
        bd.resultMask = resultMask

        if (
            isinstance(target, Node)
            and target._backend is self._node_backend
            and target._is_native_attached()
        ):
            return super()._browse(int(maxReferences), bd, target)

        async def _do() -> Any:
            r = super(Server, self)._browse(int(maxReferences), bd)
            return (await r) if inspect.isawaitable(r) else r

        return self._maybe_async(_do())

    def browseNext(
        self,
        releaseContinuationPoint: bool,
        continuationPoint,
    ):
        async def _do() -> Any:
            r = super(Server, self)._browse_next(bool(releaseContinuationPoint), continuationPoint)
            return (await r) if inspect.isawaitable(r) else r

        return self._maybe_async(_do())

    def browseRecursive(
        self,
        target: NodeIdLike,
        *,
        direction: ns0.datatypes.BrowseDirection = ns0.datatypes.BrowseDirection.FORWARD,
        reftype: NodeIdLike = ns0.reftypes.HierarchicalReferences,
        refsubtypes: bool = True,
        nodeClassMask: ns0.datatypes.NodeClass = ns0.datatypes.NodeClass.UNSPECIFIED,
        resultMask: ns0.datatypes.BrowseResultMask = ns0.datatypes.BrowseResultMask(0),
    ):
        bd = ns0.datatypes.BrowseDescription()
        bd.nodeId = o6.NodeId(target)
        bd.browseDirection = direction
        bd.referenceTypeId = o6.NodeId(reftype)
        bd.includeSubtypes = refsubtypes
        bd.nodeClassMask = nodeClassMask
        bd.resultMask = resultMask

        async def _do() -> Any:
            r = super(Server, self)._browse_recursive(bd)
            return (await r) if inspect.isawaitable(r) else r

        return self._maybe_async(_do())

    def translateBrowsePathsToNodeIds(
        self,
        browsePath,
    ):
        async def _do() -> Any:
            r = super(Server, self)._translate_browse_paths_to_nodeids(browsePath)
            return (await r) if inspect.isawaitable(r) else r

        return self._maybe_async(_do())

    def browseSimplifiedBrowsePaths(
        self,
        origin: NodeIdLike,
        browsePath,
    ):
        nid = o6.NodeId(origin)

        async def _do() -> Any:
            r = super(Server, self)._browse_simplified_browse_paths(nid, browsePath)
            return (await r) if inspect.isawaitable(r) else r

        return self._maybe_async(_do())

    def forEachChildNode(  # type: ignore[override]
        self,
        nodeId: NodeIdLike,
        callback: Callable[[o6.NodeId, bool, o6.NodeId], Any],
    ) -> MaybeAwaitable[None]:
        nid = o6.NodeId(nodeId)

        async def _do() -> None:
            r = super(Server, self)._for_each_child_node(nid, callback)
            if inspect.isawaitable(r):
                await r

        return self._maybe_async(_do())

    # -- Discovery Server ----------------------------------------------------------------

    def registerDiscovery(
        self,
        url: str,
        semaphoreFilePath: str | Path | None = None,
    ) -> None:
        """Register this server at a Discovery Server (LDS).

        Parameters
        ----------
        url : str
            The LDS endpoint URL, e.g. ``"opc.tcp://localhost:4840"``.
        semaphoreFilePath : str, optional
            Path to a semaphore file used to coordinate shutdown across
            multiple instances.  ``None`` uses an empty path."""
        path_arg = str(semaphoreFilePath) if semaphoreFilePath is not None else None
        return self._on_event_loop(lambda: super(Server, self)._register_discovery(url, path_arg))

    def deregisterDiscovery(self, url: str) -> None:
        """Deregister this server from a Discovery Server (LDS).

        Should be called once during server shutdown.

        Parameters
        ----------
        url : str
            The LDS endpoint URL that was passed to
            :meth:`registerDiscovery`."""
        return self._on_event_loop(lambda: super(Server, self)._deregister_discovery(url))

    def setRegisterServerCallback(
        self,
        callback: Callable[[dict], None] | None,
    ) -> None:
        """Install / remove the callback invoked when another server
        registers with this LDS.

        The callback receives a single ``dict`` argument with keys:
        ``server_uri``, ``product_uri``, ``discovery_urls`` (list of str),
        ``last_discovery_timestamp``.

        Pass ``None`` to remove the callback."""
        return self._on_event_loop(
            lambda: super(Server, self)._set_register_server_callback(callback)
        )

    def setServerOnNetworkCallback(
        self,
        callback: Callable[[dict], None] | None,
    ) -> None:
        """Install / remove the callback invoked when another server is
        detected on the network (via mDNS).

        The callback receives a single ``dict`` argument with keys:
        ``record_id``, ``server_name``, ``discovery_url``,
        ``server_capabilities`` (list of str), ``last_announce_time``,
        ``next_announce_time``, ``last_online_time``,
        ``is_server_announce`` (bool), ``is_txt_received`` (bool).

        Pass ``None`` to remove the callback.  Requires
        ``UA_ENABLE_DISCOVERY_MULTICAST`` in the open62541 build."""
        if not _HAS_SERVER_ON_NETWORK_CALLBACK:
            raise NotImplementedError(
                "set_server_on_network_callback requires "
                "UA_ENABLE_DISCOVERY_MULTICAST in the open62541 build"
            )
        return self._on_event_loop(
            lambda: super(Server, self)._set_server_on_network_callback(callback)
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

        ``callback`` is called as::

            callback(monitoredItemId, nodeId, attributeId, data_value, context)

        It may be a regular function or an ``async def``."""
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
                    mir, ttr, context, callback
                )
            )
            monitored_item_id = await out if inspect.isawaitable(out) else out
            return o6.subscription.MonitoredItem._from_server(self, int(monitored_item_id))

        return self._maybe_async(_create())

    def deleteMonitoredItem(
        self, monitoredItemId: int | o6.subscription.MonitoredItem
    ) -> MaybeAwaitable[None]:
        """Delete a local o6.subscription.MonitoredItem by its numeric ID."""
        if isinstance(monitoredItemId, o6.subscription.MonitoredItem):
            if monitoredItemId.id is None:
                return None
            mid = int(monitoredItemId.id)
            monitoredItemId._monitored_item_id = None
        else:
            mid = int(monitoredItemId)

        async def _delete() -> None:
            out = self._on_event_loop(lambda: super(Server, self)._delete_monitored_item(mid))
            if inspect.isawaitable(out):
                await out

        return self._maybe_async(_delete())

    def createEventMonitoredItem(
        self,
        nodeId: NodeIdLike,
        callback: Callable,
        *,
        context: object = None,
        selectClauses: "list[ns0.datatypes.SimpleAttributeOperand] | None" = None,
        whereClause: "ns0.datatypes.ContentFilter | None" = None,
    ) -> MaybeAwaitable[o6.subscription.MonitoredItem]:
        """Create a local Event o6.subscription.MonitoredItem on *nodeId*.

        ``callback(monitoredItemId, event_fields, context)`` where
        ``event_fields`` is a dict ``{QualifiedName: value}``."""
        nid = o6.NodeId(nodeId)
        ef = ns0.datatypes.EventFilter()
        if selectClauses is not None:
            ef.selectClauses = selectClauses
        if whereClause is not None:
            ef.whereClause = whereClause

        async def _create() -> o6.subscription.MonitoredItem:
            out = self._on_event_loop(
                lambda: super(Server, self)._create_event_monitored_item(nid, ef, context, callback)
            )
            monitored_item_id = await out if inspect.isawaitable(out) else out
            return o6.subscription.MonitoredItem._from_server(self, int(monitored_item_id))

        return self._maybe_async(_create())

    def createEventMonitoredItemEx(
        self,
        nodeId: NodeIdLike,
        callback: Callable,
        *,
        monitoringMode: "ns0.datatypes.MonitoringMode | None" = None,
        clientHandle: int = 0,
        samplingInterval: float = 0.0,
        eventFilter: "ns0.datatypes.EventFilter | None" = None,
        queueSize: int = 0,
        discardOldest: bool = True,
        context: object = None,
    ) -> MaybeAwaitable[o6.subscription.MonitoredItem]:
        """Extended version of createEventMonitoredItem with full control.

        Uses a ``MonitoredItemCreateRequest`` (attributeId = EventNotifier).
        Returns the monitoredItemId."""
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
        if eventFilter is not None:
            mir.requestedParameters.filter = eventFilter

        async def _create() -> o6.subscription.MonitoredItem:
            out = self._on_event_loop(
                lambda: super(Server, self)._create_event_monitored_item_ex(mir, context, callback)
            )
            monitored_item_id = await out if inspect.isawaitable(out) else out
            return o6.subscription.MonitoredItem._from_server(self, int(monitored_item_id))

        return self._maybe_async(_create())

    # -- Server Callbacks ---------------------------------------------------------

    def addRepeatedCallback(self, callback: Callable, intervalMs: float) -> int:
        """Register *callback* to be called every *intervalMs* milliseconds.

        Returns an opaque integer callback ID that can be passed to
        :meth:`changeRepeatedCallbackInterval` or :meth:`removeCallback`."""
        return self._sync_result(
            self._on_event_loop(
                lambda: super(Server, self)._add_repeated_callback(callback, float(intervalMs))
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
