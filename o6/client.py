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

from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Awaitable,
    Iterable,
    Literal,
    Mapping,
    TypeAlias,
    overload,
)
from types import TracebackType
from functools import partial

import builtins
from contextlib import suppress
import asyncio
import datetime
import hashlib
import itertools
import logging
import operator
import re
import threading

from typing import Self

from pathlib import Path

import o6
import o6.subscription
from o6._browse import (
    _BrowseCollection,
    _finish_request,
    _browse_description,
    _simplified_browse_path,
    _translate_paths,
)
from o6._datatype_loading import _RemoteDataTypes, _UnknownDataTypes
from o6._creation import is_value_envelope, variable_attributes
from o6._delete import _delete_inputs
from o6._read import _check_read_status, _read_request, _read_results
from o6._write import _WRITE_UNSET, _write_inputs, _write_payload, _write_payload_status
from o6._node_backend import (
    _ClientBackend,
    _attribute_id,
    _child_browse_result_mask,
    _targets_and_ranges,
    _without_traceback,
)
from o6._notifications import (
    Notification,
    NotificationHandlers,
    NotificationType,
    lifecycle_point,
    run_handlers,
)
from o6.node import _normalize_nodeids

if TYPE_CHECKING:
    _NativeClient: TypeAlias = Any
    _requireClient: Callable[[], None]
else:
    from . import _o6

    _NativeClient = _o6.Client
    _requireClient = _o6._require_client
    del _o6
import o6.node as nodes
from o6 import LocalizedTextLike, MaybeAwaitable, NodeIdLike
from o6.util import (
    _call_native,
    _ConfigView,
    _finalize_native,
    _run_on_loop,
    _ScheduledFinalizer,
    _WorkerLoop,
)
from typing import cast

from o6.ns import ns0


def _version_key(value: str) -> tuple[tuple[int, int | str], ...]:
    return tuple(
        (0, int(part)) if part.isdigit() else (1, part.lower())
        for part in re.findall(r"\d+|[A-Za-z]+", value)
    )


def _select_namespace_candidate(hits: list[Any], scope: str, server_version: str = "") -> Any:
    matching = [hit for hit in hits if server_version and hit.version == server_version]
    return max(
        matching or hits,
        key=lambda hit: (hit.scope == scope, _version_key(hit.version)),
    )


def _load_namespace_modules(namespaces: Iterable[Any]) -> None:
    """Load bundled packages that are only registered, so their DataTypes decode.

    The decoder takes the DataTypes defined when the namespace mapping is applied.
    """
    for namespace in namespaces:
        namespace._load()


def _namespace_slug(uri: str) -> str:
    """A snake_case name from the last segment of a namespace URI."""
    path = re.sub(r"^\w+://|^\w+:", "", uri)
    segments = re.findall(r"[^/:]+", path)
    name = next((segment for segment in reversed(segments) if segment), "namespace")
    name = re.sub(r"[.\-\s]+", "_", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    name = re.sub(r"[^a-zA-Z0-9_]", "_", name).lower().strip("_") or "namespace"
    return f"ns_{name}" if name[0].isdigit() else name


def _remote_namespace_shortname(uri: str, scope: str) -> str:
    """Return a stable, client-scoped shortname for a remote namespace URI."""
    base = f"{scope}_{_namespace_slug(uri)}"
    candidate = base
    digest = hashlib.sha256(uri.encode()).hexdigest()[:12]
    collision = 0
    while candidate in o6.ns:
        existing = getattr(o6.ns, candidate)
        if existing.uri == uri and existing.scope == scope:
            return candidate
        collision += 1
        suffix = digest if collision == 1 else f"{digest}_{collision}"
        candidate = f"{base}_{suffix}"
    return candidate


def _history_read_value_id(nodeid: NodeIdLike) -> ns0.datatypes.HistoryReadValueId:
    rvid = ns0.datatypes.HistoryReadValueId()
    rvid.nodeId = o6.NodeId(nodeid)
    return rvid


def _unwrap_history_read(response: Any, is_scalar: bool, indices: list[int] | None = None) -> Any:
    if o6.StatusCode.BAD in response.responseHeader.serviceResult:
        error = o6.StatusCodeError(response.responseHeader.serviceResult)
        error.add_note("HistoryRead service failed")
        raise error
    results = response.results
    if is_scalar and len(results) != 1:
        raise RuntimeError("HistoryRead returned an unexpected number of results")
    for index, result in enumerate(results):
        if o6.StatusCode.BAD in result.statusCode:
            error = o6.StatusCodeError(result.statusCode)
            target_index = indices[index] if indices is not None else index
            error.add_note(f"HistoryRead result at index {target_index} failed")
            raise error
    if is_scalar:
        hd = results[0].historyData
        return hd.body if hasattr(hd, "body") and hd.body is not None else hd
    out = []
    for r in results:
        hd = r.historyData
        if hasattr(hd, "body") and hd.body is not None:
            out.append(hd.body)
        else:
            out.append(hd)
    return out


# `next()` on a count is atomic, so concurrent clients get distinct auto-names
_client_name_counter = itertools.count(1)
# Seconds a collected client waits for its SecureChannel to close
_FINALIZE_CLOSE_TIMEOUT = 1.0


# The notification scopes open62541's client exposes, and the native setter
# that installs each one's callback. `global` observes everything the
# connection produces; the other two observe only their own scope, and fire
# independently of `global` and of each other.
_NOTIFICATION_SCOPES = ("global", "lifecycle", "service")


class Client(_NativeClient):
    """High-level OPC UA client.

    ```python
    with o6.Client("opc.tcp://localhost:4840") as client:
        print(client.read("ns=1;s=Temperature"))
    ```

    Request methods return a plain value when the client drives its own event
    loop, and an awaitable when it runs on an external one. See
    [`MaybeAwaitable`][o6.MaybeAwaitable]. Operations on a disconnected client
    raise.

    See the [Client guide](manual/client/index.md) and the
    [tutorials](tutorials/index.md).
    """

    _loop: asyncio.AbstractEventLoop
    root: nodes.ObjectNode
    """Node handle for the standard Root folder (`i=84`)."""

    objects: nodes.ObjectNode
    """Node handle for the standard Objects folder (`i=85`)."""

    types: nodes.ObjectNode
    """Node handle for the standard Types folder (`i=86`)."""

    views: nodes.ObjectNode
    """Node handle for the standard Views folder (`i=87`)."""

    def __init__(
        self,
        endpointUrl: str = "",
        loop: asyncio.AbstractEventLoop | None = None,
        *,
        logger: logging.Logger | None = None,
        certificate: str | Path | bytes | None = None,
        privateKey: str | Path | bytes | None = None,
        trustList: list[str | Path | bytes] | None = None,
        revocationList: list[str | Path | bytes] | None = None,
        acceptAllCertificates: bool = False,
        loadUnknownDataTypes: bool = True,
        securityMode: int | None = None,
        securityPolicy: str | None = None,
        applicationUri: str | None = None,
        username: str | None = None,
        password: str | None = None,
        allowNonePolicyPassword: bool = False,
        name: str = "",
    ) -> None:
        """Create a client. It does not connect until `connect()` is called.

        Other settings, such as `sessionName`, `requestedSessionTimeout`,
        `sessionLocaleIds` and `endpoint`, are set on `client.config` before
        `connect()`. See [`ClientConfig`][o6.ClientConfig].

        Args:
            endpointUrl: Endpoint to connect to, for example
                `"opc.tcp://localhost:4840"` or, with an IPv6 address in
                brackets, `"opc.tcp://[::1]:4840"`. Can also be set later
                through `client.config.endpointUrl`.
            loop: Event loop to use. Defaults to the running loop, or a new
                loop if none is running.
            logger: Logger for client output. Same as `client.config.logger`.
            certificate: Client certificate, as a path or raw DER or PEM
                bytes. Same as `client.config.certificate`.
            privateKey: Private key for `certificate`, as a path or raw bytes.
                Same as `client.config.privateKey`.
            trustList: Trusted server certificates, or the CA certificates of
                their issuers, as paths or raw bytes. With a client certificate
                but without a trust list, the client rejects every server
                certificate unless `acceptAllCertificates=True`. Same as
                `client.config.trustList`.
            revocationList: Certificate revocation lists, as paths or raw
                bytes. Same as `client.config.revocationList`.
            acceptAllCertificates: Trust every server certificate and ignore
                the trust list. Defaults to `False`. For development only.
                Same as `client.config.acceptAllCertificates`.
            loadUnknownDataTypes: Load the DataType of a received structure
                the client cannot decode from the server, once per encoding,
                and return the value decoded. Defaults to `True`. Applies to
                server namespaces without a package. See
                [Unknown namespaces and structured values](../manual/sdk-fundamentals/namespace/loading-and-using-nodesets.md#unknown-namespaces-and-structured-values).
                Same as `client.config.loadUnknownDataTypes`.
            securityMode: Message security mode, as an integer or
                `o6.ns.ns0.datatypes.MessageSecurityMode`. Same as
                `client.config.securityMode`.
            securityPolicy: URI, `o6.SecurityPolicy` member or short name of
                the security policy, for example `"Basic256Sha256"`. Same as
                `client.config.securityPolicy`.
            applicationUri: Application URI sent in the
                `ApplicationDescription`. Same as `client.config.applicationUri`.
            username: User name for `UserNameIdentityToken` authentication.
                Same as `client.config.setUsernamePassword(username, password)`.
                Password-token encryption does not authenticate the server
                without `certificate`, `privateKey` and `trustList`. See
                [Secured connections](manual/client/lifecycle.md#secured-connections).
            password: Password for `username`.
            allowNonePolicyPassword: Permit sending a username/password token
                without encryption. `False` also when credentials are given.
                Same as `client.config.allowNonePolicyPassword`.
            name: Client name. Must be a valid Python identifier, unique in
                the process, and not `server<digits>`, `global` or `::global`.
                Defaults to a generated `clientN`.

        Raises:
            ValueError: `name` is invalid, reserved or not unique, or
                `securityPolicy` is an unknown short name.
        """
        _requireClient()
        owns_loop = False
        if loop is None:
            try:
                loop = asyncio.get_running_loop()
            except:
                loop = asyncio.new_event_loop()
                owns_loop = True
            else:
                if hasattr(builtins, "__IPYTHON__"):
                    # In IPython, the event loop is already running but we can't
                    # block on it, so we still have to run the worker loop in a
                    # separate thread.
                    loop = asyncio.new_event_loop()
                    owns_loop = True
        if logger is None:
            logger = logging.getLogger(__name__)

        # Initialize Python-side attributes BEFORE super().__init__ so
        # __del__ can access them even if the C init raises.
        self._loop = loop
        self._logger = logger
        self._owns_loop = owns_loop
        self._worker: _WorkerLoop | None = _WorkerLoop(loop) if owns_loop else None
        # The worker starts with the first operation that needs the loop
        self._worker_pending = self._worker is not None
        # Reentrant: an inline native call may start the worker itself
        self._worker_start_lock = threading.RLock()
        self._subscriptions: dict[int, o6.subscription.Subscription] = {}
        self._default_subscription_id: int | None = None
        # The DataTypes `loadRemoteDataTypes` has warned about, once each.
        self._reportedDataTypes: set[Any] = set()
        # Counts the native namespace snapshots applied; see `_apply_namespace_snapshot`.
        self._namespace_applications = 0
        self._notification_sync_lock = threading.Lock()
        self._notification_scopes: dict[str, NotificationHandlers] = {
            scope: NotificationHandlers(partial(self._sync_notification_scope, scope))
            for scope in _NOTIFICATION_SCOPES
        }

        if name:
            if not name.isidentifier():
                raise ValueError(
                    f"name must be a valid Python identifier (letters, digits, underscores, "
                    f"not starting with a digit), got {name!r}"
                )
            import re

            if re.fullmatch(r"server\d+", name):
                raise ValueError(
                    f"Client name is reserverd: {name!r}, matches pattern 'server{{number}}'"
                )
            if name in ["::global", "global"]:
                raise ValueError(f"Client name is reserverd: {name!r}'")
        else:
            name = f"client{next(_client_name_counter)}"

        self._name = name
        if self._name + "_ns1" in o6.ns:
            raise ValueError(f"Client name {self._name} is not unique")

        super().__init__(logger=logger, loop=loop)
        self._unknownDataTypes = _UnknownDataTypes(self)

        def configure() -> None:
            self._set_owns_loop(owns_loop)
            self.config.tcpReuseAddr = True
            if endpointUrl:
                self.config.endpointUrl = endpointUrl

            if certificate is not None:
                self.config.certificate = certificate
            if privateKey is not None:
                self.config.privateKey = privateKey
            if trustList is not None:
                self.config.trustList = trustList
            if revocationList is not None:
                self.config.revocationList = revocationList
            self.config.acceptAllCertificates = bool(acceptAllCertificates)
            self.config.loadUnknownDataTypes = bool(loadUnknownDataTypes)
            # Finalize certificate configuration before selecting the channel policy.
            self.config._finalize_encryption()
            if securityMode is not None:
                self.config.securityMode = int(securityMode)
            if securityPolicy is not None:
                self.config.securityPolicy = securityPolicy
            if applicationUri is not None:
                self.config.applicationUri = applicationUri

            if username is not None:
                self.config.setUsernamePassword(username, password or "")
            self.config.allowNonePolicyPassword = allowNonePolicyPassword

        # Runs on the thread of an application loop that already runs
        self._call_native(configure)

        # Initialize the well-known entry-points into the namespace 0
        self._node_backend = _ClientBackend(self)
        self.root = nodes.ObjectNode(self._node_backend, "i=84", o6.QualifiedName(0, "Root"))
        self.objects = nodes.ObjectNode(self._node_backend, "i=85", o6.QualifiedName(0, "Objects"))
        self.types = nodes.ObjectNode(self._node_backend, "i=86", o6.QualifiedName(0, "Types"))
        self.views = nodes.ObjectNode(self._node_backend, "i=87", o6.QualifiedName(0, "Views"))

    @classmethod
    def newFromFile(
        cls,
        file_path: str | Path,
        endpointUrl: str = "",
        loop: asyncio.AbstractEventLoop | None = None,
        *,
        logger: logging.Logger | None = None,
        applicationUri: str | None = None,
        name: str = "",
    ) -> Self:
        """Create a client from a JSON5 configuration file.

        Every setting in the file is used, including `endpointUrl`,
        `securityMode`, `securityPolicyUri` and `userIdentityToken`.
        Everything the file leaves out gets the o6 default. The security
        configuration comes from the file. See
        [`ClientConfig.loadFromFile`][o6.ClientConfig.loadFromFile] for the
        file format.

        ```python
        client = o6.Client.newFromFile("client.json5")
        client.connect()
        ```

        Args:
            file_path: JSON5 configuration file.
            endpointUrl: Endpoint to connect to when the file sets none.
            loop: Event loop to use, as for `Client()`.
            logger: Logger for client output. Defaults to the `o6.client` logger.
            applicationUri: ApplicationUri when the file sets none.
            name: Client name, as for `Client()`.

        Returns:
            The configured client. It does not connect until `connect()` is called.

        Raises:
            FileNotFoundError: The file does not exist.
            ValueError: The file is not a JSON5 object.
            StatusCodeError: A setting of the file is invalid.
        """
        client = cls(endpointUrl, loop, logger=logger, applicationUri=applicationUri, name=name)
        client.config.loadFromFile(file_path)
        return client

    def __del__(self) -> None:
        # Never blocks: while a thread runs the loop, teardown is scheduled on
        # it (see `o6.util._finalize_native`). The C deallocator is the fallback.
        loop = getattr(self, "_loop", None)
        if loop is None:
            return
        worker = getattr(self, "_worker", None)

        def cleanup() -> None:
            self._cleanup()
            if self._owns_loop and not loop.is_closed():
                loop.close()

        _finalize_native(
            self, loop, worker, live=self._is_live, finalize=self._finalize, cleanup=cleanup
        )

    def _finalize(self) -> None:
        """Close and release a collected client; runs on its loop at top level."""

        def release() -> None:
            self._cleanup()
            if self._worker is not None:
                self._worker.retire(close=True)

        if not self._is_live():
            release()
            return

        # Releases even if the task is cancelled, or destroyed by a closing loop
        released = _ScheduledFinalizer(self._loop, release, release)

        async def close() -> None:
            try:
                self._unknownDataTypes.cancel()
                closing = super(Client, self)._disconnect_secure_channel()  # type: ignore[misc]
                if closing is not None and not closing.done():
                    await asyncio.wait({closing}, timeout=_FINALIZE_CLOSE_TIMEOUT)
                # Let transport close events run before native cleanup
                for _ in range(10):
                    await asyncio.sleep(0)
            except Exception:
                self._logger.debug("Closing a collected client failed", exc_info=True)
            finally:
                released()

        # A task cancelled before its first step skips `finally`
        self._loop.create_task(close()).add_done_callback(lambda _task: released())

    def _run_on_loop(
        self, fn: Callable[[], Any], *, sync_result: bool = False, wait: bool = False
    ) -> Any:
        """Run a native operation on this client's loop thread; see `o6.util._run_on_loop`."""
        self._start_worker()
        worker = self._worker
        return _run_on_loop(
            self._loop, lambda: worker, fn, sync_result=sync_result, wait=wait, owner="Client"
        )

    def _apply_namespace_snapshot(
        self, uris: list[str], entries: list[tuple[str, int, int]]
    ) -> None:
        """Replace the native namespace mapping and custom DataTypes, and count the application.

        `updateRemoteNamespaces` awaits between its provisional and its final
        mapping. The count tells it whether a DataType lookup applied another
        mapping meanwhile, so that the final one must be applied again.
        """
        super()._apply_namespace_snapshot(uris, entries)
        self._namespace_applications += 1

    def _start_worker(self) -> None:
        """Start the owned worker for the first operation that needs the loop.

        Until then no loop runs, so configuration runs inline on any thread.
        A worker stopped by `disconnect()` stays stopped; `connect()` restarts it.
        """
        worker = self._worker
        if worker is None:
            return
        with self._worker_start_lock:
            if self._worker_pending:
                self._worker_pending = False
                worker.start()

    @property
    def config(self) -> o6.ClientConfig:
        """This client's [`ClientConfig`][o6.ClientConfig].

        Readable from any thread. It can be changed only while the client is
        not connected.
        """
        return cast("o6.ClientConfig", _ConfigView(self, super().config))

    def _call_native(self, fn: Callable[[], Any]) -> Any:
        """Return a synchronous native operation's result from any thread; see `o6.util._call_native`."""
        worker = self._worker
        if worker is not None:
            with self._worker_start_lock:
                # The worker starts only under this lock, so a loop that no
                # thread runs stays idle until `fn` returns.
                if not worker.running and not self._loop.is_running():
                    return fn()
        return _call_native(self._loop, lambda: worker, fn, owner="Client")

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        """The asyncio event loop of this client, fixed at construction."""
        return self._loop

    @property
    def state(self) -> tuple[o6.SecureChannelState, o6.SessionState, o6.StatusCode]:
        """The tuple `(channelState, sessionState, connectStatus)`."""
        channel_state, session_state, status_code = self._call_native(self._get_state)
        return (
            o6.SecureChannelState(channel_state),
            o6.SessionState(session_state),
            status_code,
        )

    @property
    def connected(self) -> bool:
        """Whether the Session is activated."""
        _, session_state, _ = self.state
        return session_state == o6.SessionState.ACTIVATED

    @property
    def onGlobalNotification(self) -> NotificationHandlers:
        """Registry of handlers for every notification of this client.

        Covers lifecycle, service and all other notifications. Use it as a
        decorator, a callable or a list, like the
        `Server.on<category>Notification` registries.

        See [Notification handler](manual/client/notification-handler.md).
        """
        return self._notification_scopes["global"]

    @onGlobalNotification.setter
    def onGlobalNotification(self, value: Any) -> None:
        self.onGlobalNotification.replace(value)

    @property
    def onLifecycleNotification(self) -> NotificationHandlers:
        """Registry of handlers for client lifecycle notifications.

        Fires on connection start and stop, independent of
        `onGlobalNotification`.

        See [Notification handler](manual/client/notification-handler.md).
        """
        return self._notification_scopes["lifecycle"]

    @onLifecycleNotification.setter
    def onLifecycleNotification(self, value: Any) -> None:
        self.onLifecycleNotification.replace(value)

    @property
    def onServiceNotification(self) -> NotificationHandlers:
        """Registry of handlers for service begin and end notifications.

        Independent of `onGlobalNotification`.

        See [Notification handler](manual/client/notification-handler.md).
        """
        return self._notification_scopes["service"]

    @onServiceNotification.setter
    def onServiceNotification(self, value: Any) -> None:
        self.onServiceNotification.replace(value)

    def _sync_notification_scope(self, scope: str) -> None:
        """Install or remove the native callback backing one scope.

        The native side stores exactly one callback per scope, so the
        registry installs a single dispatcher that fans out to its handlers,
        and removes it again once the last handler is gone.
        """
        registry = self._notification_scopes[scope]
        setter = getattr(self, f"_set_{scope}_notification_callback")

        def install() -> None:
            # Reads the registry and installs under one lock, so a concurrent
            # add or remove cannot leave a stale callback installed. Runs on
            # the loop thread, or inline while none runs the loop, so the lock
            # is never held while marshalling.
            with self._notification_sync_lock:
                setter(partial(self._dispatch_notification, scope) if registry else None)

        self._call_native(install)

    def _dispatch_notification(self, scope: str, type: int, payload: Mapping[str, Any]) -> None:
        handlers = self._notification_scopes[scope].snapshot()
        if not handlers:
            return
        notification = Notification(type=type, payload=payload, lifecycle=lifecycle_point(type))
        run_handlers(handlers, notification, self._loop, self._logger)

    def _create_default_subscription(self) -> MaybeAwaitable[o6.subscription.Subscription]:
        async def _create() -> o6.subscription.Subscription:
            if self._default_subscription_id is not None:
                existing = self._subscriptions.get(self._default_subscription_id)
                if existing is not None:
                    return existing

            subscription = await self.createSubscription(publishingInterval=100.0)
            self._default_subscription_id = subscription.id
            return subscription

        return self._run_on_loop(_create)

    async def _set_ns1_mapping(self) -> None:
        sup = super()

        async def get_application_uri() -> str:
            request = ns0.datatypes.GetEndpointsRequest()
            request.endpointUrl = self.config.endpointUrl
            response = await self.serviceGetEndpoints(request)  # type: ignore[misc]
            application_uri = response.endpoints[0].server.applicationUri
            return application_uri

        application_uri = await get_application_uri()

        ns = o6.ns.register(
            shortname=self._name + "_ns1",
            uri=application_uri,
            scope=self.config.endpointUrl,
        )
        self._application_namespace_index = ns.index

    def connect(
        self,
        noSession: bool = False,
        *,
        createDefaultSubscription: bool = True,
    ) -> MaybeAwaitable[None]:
        """Connect to the server.

        Opens a SecureChannel and, by default, a Session. Applies the
        certificate and key first. Starts the background worker thread. If
        setup after the Session fails, including creating the default
        subscription, the Session is closed before the error is raised.

        Args:
            noSession: Open only the SecureChannel, for discovery or to
                activate a Session later. The connect completes once the
                channel with the requested security is open.
            createDefaultSubscription: Create the default subscription after
                connecting. Set it to `False` for sessions that do not
                monitor, or that pass their own subscription to the monitoring
                methods. Ignored when `noSession=True`.

        Raises:
            RuntimeError: Temporary credentials for password-token encryption
                could not be created. Configure `certificate` and `privateKey`
                explicitly before retrying.
            StatusCodeError: Certificate validation, channel negotiation,
                session activation or post-connect setup failed. Fails with
                `BadTimeout` and closes the channel when the channel, and the
                Session unless `noSession`, are not open within
                `config.timeout` milliseconds. A timeout of `0` waits without
                limit.
        """
        sup = super()

        if noSession:

            async def _connect() -> None:
                self._node_backend.invalidate_children()
                self.config._finalize_encryption()  # no-op if cert/key not set or already applied
                await sup._connect_secure_channel()  # type: ignore[attr-defined]

        else:

            async def _connect() -> None:
                # sup._connect() creates AND activates the session on the server.
                # Failed post-connect setup must not leave the session open.
                self._node_backend.invalidate_children()
                # Credentials may have been set after construction.
                self.config._finalize_encryption()
                await sup._connect()  # type: ignore[attr-defined]
                try:
                    await self._set_ns1_mapping()
                    await self.updateRemoteNamespaces()  # type: ignore[misc]
                    if createDefaultSubscription:
                        await self._create_default_subscription()
                except BaseException:
                    try:
                        result = sup._disconnect()  # type: ignore[attr-defined]
                        if result is not None:
                            await result
                    except Exception:
                        # Surface the original failure
                        self._logger.warning(
                            "Disconnect after a failed connect failed", exc_info=True
                        )
                    raise

        # Restart a worker that disconnect() stopped
        self._worker_pending = self._worker is not None

        return self._run_on_loop(_connect)

    def disconnect(
        self,
        closeSession: bool = True,
        deleteSubscriptions: bool = True,
    ) -> MaybeAwaitable[None]:
        """Disconnect from the server.

        By default, deletes all subscriptions, closes the Session and the
        SecureChannel, and stops the background worker thread. Calling it on
        a disconnected client or a closed event loop returns `None` without
        raising.

        Args:
            closeSession: Close the Session and the SecureChannel. `False`
                closes only the SecureChannel and keeps the Session, for
                example for session transfer.
            deleteSubscriptions: Delete all subscriptions first. Ignored when
                `closeSession` is `False`.
        """
        sup = super()

        if closeSession:
            if self._loop.is_closed():
                return None

            if self._worker is not None and not self._worker.running:
                return None

            async def _disconnect() -> None:
                self._unknownDataTypes.cancel()
                if deleteSubscriptions:
                    for subscription in list(self._subscriptions.values()):
                        try:
                            await subscription.delete()
                        except Exception:
                            pass  # channel may already be closed; proceed with disconnect
                    self._subscriptions.clear()
                    self._default_subscription_id = None

                try:
                    result = sup._disconnect()  # type: ignore[attr-defined]
                    if result is not None:
                        await result
                except Exception:
                    self._logger.warning("Disconnect failed", exc_info=True)
                # Drain: let asyncio process pending transport close events
                # (connection_lost, etc.) before stopping the event loop.
                for _ in range(10):
                    await asyncio.sleep(0)

            result = self._run_on_loop(_disconnect)

            # In synchronous context _run_on_loop blocks until _disconnect
            # completes, so we can safely tear down the worker thread now.
            if not isinstance(result, asyncio.Future):
                if self._worker is not None:
                    self._worker.stop()
                return result

            # Async context: schedule thread cleanup after the future resolves.
            async def _await_and_stop():
                await result
                if self._worker is not None:
                    self._worker.stop()

            return _await_and_stop()

        else:

            async def _disconnect() -> None:
                await sup._disconnect_secure_channel()  # type: ignore[attr-defined]

            return self._run_on_loop(_disconnect)

    def startReverseConnect(
        self,
        port: int,
        hostnames: list[str] | None = None,
    ) -> MaybeAwaitable[None]:
        """Listen on `port` for a reverse connection opened by the server.

        Close the connection with [disconnect][o6.client.Client.disconnect].

        Args:
            port: TCP port to listen on.
            hostnames: Network interfaces to listen on. `None` or an empty
                list lets open62541 choose, usually all interfaces.
        """
        sup = super()

        async def _connect() -> None:
            await sup._start_reverse_connect(port, hostnames or [])  # type: ignore[attr-defined]

        # Restart a worker that disconnect() stopped
        self._worker_pending = self._worker is not None

        return self._run_on_loop(_connect)

    def activateCurrentSession(self) -> Any:
        """Activate this client's existing Session again, on the current channel.

        Sends ActivateSession with the stored identity token and credentials,
        then creates the default subscription. Use it after the SecureChannel
        was renewed or re-established.
        """
        sup = super()

        async def _call() -> None:
            await sup._activate_current_session()  # type: ignore[attr-defined]
            await self._create_default_subscription()

        return self._run_on_loop(_call)

    def activateSession(
        self,
        authToken: o6.NodeId,
        serverNonce: bytes,
    ) -> Any:
        """Take over a Session created by another client.

        Open a SecureChannel with `connect(noSession=True)` first. Also creates
        the default subscription.

        Args:
            authToken: Authentication token NodeId of the original Session.
            serverNonce: Server nonce of the original Session.
        """
        sup = super()

        async def _call() -> None:
            await sup._activate_session(authToken, serverNonce)  # type: ignore[attr-defined]
            await self._create_default_subscription()

        return self._run_on_loop(_call)

    def __enter__(self) -> Self:
        """Connect if not connected, and return the client."""
        if not self.connected:
            self.connect()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Disconnect, also while connecting or reconnecting. Exceptions are not suppressed."""
        self.disconnect()

    async def __aenter__(self) -> Self:
        """Await `connect()` if not connected, and return the client."""
        if not self.connected:
            await self.connect()  # type: ignore[misc]
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Await `disconnect()`, also while connecting or reconnecting. Exceptions are not suppressed."""
        result = self.disconnect()
        if result is not None:
            await result

    def __getitem__(self, key: NodeIdLike) -> MaybeAwaitable[nodes.Node]:
        """Return a typed [Node][o6.Node] handle for a NodeId.

        Reads the NodeClass and BrowseName from the server and returns the
        matching Node subclass, such as `VariableNode` or `ObjectNode`.

        Args:
            key: Any value accepted by [NodeId][o6.NodeId]: a string such as
                `"ns=1;s=Temperature"`, a numeric namespace-0 id or a NodeId.

        Raises:
            StatusCodeError: The read failed. An unknown NodeId has code
                `BAD_NODE_ID_UNKNOWN`.
            RuntimeError: The client is not connected, or the response is
                malformed.

        ```python
        node = client["ns=1;s=Temperature"]        # sync
        node = await client["ns=1;s=Temperature"]  # async
        ```
        """

        nodeid = o6.NodeId(key)

        async def _get_node() -> nodes.Node:
            if not self.connected:
                raise RuntimeError("Client is not connected")
            # Read NodeClass and BrowseName
            rvi_nc = ns0.datatypes.ReadValueId()
            rvi_nc.nodeId = nodeid
            rvi_nc.attributeId = o6.AttributeId.NODE_CLASS
            rvi_bn = ns0.datatypes.ReadValueId()
            rvi_bn.nodeId = nodeid
            rvi_bn.attributeId = o6.AttributeId.BROWSE_NAME
            read_request = ns0.datatypes.ReadRequest()
            read_request.nodesToRead = [rvi_nc, rvi_bn]
            read_response = await self._service_read(read_request)

            read_response.responseHeader.serviceResult.check(message=f"Lookup {nodeid}")
            if len(read_response.results) != 2:
                raise RuntimeError(f"Lookup {nodeid} returned an unexpected number of results")
            for attribute, result in zip(("NodeClass", "BrowseName"), read_response.results):
                result.status.check(message=f"Lookup {nodeid}: {attribute}")
            node_class_value = read_response.results[0].value
            browse_name = read_response.results[1].value
            try:
                node_class = ns0.datatypes.NodeClass(operator.index(node_class_value))
                node_type = nodes._nodeclass2type(node_class)
            except (TypeError, ValueError):
                raise RuntimeError(f"Lookup {nodeid} returned an invalid NodeClass") from None
            if not isinstance(browse_name, o6.QualifiedName):
                raise RuntimeError(f"Lookup {nodeid} returned an invalid BrowseName")
            return node_type(self._node_backend, nodeid, browse_name)

        try:
            return self._run_on_loop(_get_node)
        except Exception as exc:
            raise _without_traceback(exc) from None

    #
    # Raw Service API
    #
    # These explicit methods preserve a discoverable, typed public API while
    # _run_on_loop provides the shared sync/async dispatch policy.

    # Discovery Service Set

    def serviceFindServers(
        self, request: ns0.datatypes.FindServersRequest
    ) -> MaybeAwaitable[ns0.datatypes.FindServersResponse]:
        """Call the FindServers service to list servers known to a discovery server.

        [OPC UA Part 4 §5.5.2](https://reference.opcfoundation.org/specs/OPC-10000-4/5.5.2)"""
        return self._run_on_loop(partial(self._service_find_servers, request))

    def serviceFindServersOnNetwork(
        self, request: ns0.datatypes.FindServersOnNetworkRequest
    ) -> MaybeAwaitable[ns0.datatypes.FindServersOnNetworkResponse]:
        """Call the FindServersOnNetwork service to list servers found by mDNS or an LDS.

        [OPC UA Part 4 §5.5.3](https://reference.opcfoundation.org/specs/OPC-10000-4/5.5.3)"""
        return self._run_on_loop(partial(self._service_find_servers_on_network, request))

    def serviceGetEndpoints(
        self, request: ns0.datatypes.GetEndpointsRequest
    ) -> MaybeAwaitable[ns0.datatypes.GetEndpointsResponse]:
        """Call the GetEndpoints service to get the endpoint descriptions of a server.

        [OPC UA Part 4 §5.5.4](https://reference.opcfoundation.org/specs/OPC-10000-4/5.5.4)"""
        return self._run_on_loop(partial(self._service_get_endpoints, request))

    def serviceRegisterServer(
        self, request: ns0.datatypes.RegisterServerRequest
    ) -> MaybeAwaitable[ns0.datatypes.RegisterServerResponse]:
        """Call the RegisterServer service to register, update or unregister at an LDS.

        The service result is returned, not raised: check
        `responseHeader.serviceResult`. To unregister, set
        `request.server.isOnline=False` and await the response before
        disconnecting, with the same connection and security settings. A
        registration matches by server URI and at least one shared discovery
        URL.
        """
        return self._run_on_loop(partial(self._service_register_server, request))

    def serviceRegisterServer2(
        self, request: ns0.datatypes.RegisterServer2Request
    ) -> MaybeAwaitable[ns0.datatypes.RegisterServer2Response]:
        """Call the RegisterServer2 service to register with a discovery configuration.

        Non-Good results are returned in the response, not raised. Check
        `responseHeader.serviceResult` and every entry of
        `configurationResults`. There is no automatic fallback. Fall back to
        `serviceRegisterServer` only on `BadServiceUnsupported`. Matching and
        unregistration work as for `serviceRegisterServer`.
        """
        return self._run_on_loop(partial(self._service_register_server2, request))

    def invalidateNodeCache(self, target: NodeIdLike | None = None) -> MaybeAwaitable[None]:
        """Drop the cached children of this client's node handles.

        The next navigation browses again. Call it after the address space
        changed by other means, or after raw service browsing. A complete
        `browse()` invalidates its target. Node and reference changes through
        this client, and namespace refresh, invalidate all handles. A cached
        miss is browsed once more before it raises. Async callers must await
        it.

        Args:
            target: Invalidate the handles of this node only. `None`
                invalidates all handles.
        """
        nodeid = o6.NodeId(target) if target is not None else None

        async def _invalidate() -> None:
            self._node_backend.invalidate_children(nodeid)

        return self._run_on_loop(_invalidate)

    async def _mutate_address_space(self, operation: Awaitable[Any]) -> Any:
        try:
            return await operation
        finally:
            # Partial failures can still change the address space.
            self._node_backend.invalidate_children()

    def exportInformationModel(
        self,
        directory: str | Path,
        *,
        includeInstances: bool = False,
        includeCompleteServer: bool = False,
        includeValues: bool | Literal["types"] = True,
        includeAccessAttributes: bool = False,
    ) -> MaybeAwaitable[list[Path]]:
        """Export the server's information model as NodeSet2 XML, one file per namespace.

        Covers the address space from the Root folder with Browse and Read and
        writes `<shortname>.NodeSet2.xml` files. ns0 and the runtime data below the
        Server object (status, diagnostics, sessions, ...) are skipped. The
        server's own nodes below the Server object are exported.
        A reference to a node of a companion specification that has no file in
        the export, such as a dictionary entry, is kept and makes that
        specification a required model.
        Problems, such as unreadable attributes, are logged as warnings.

        Args:
            directory: Output directory, created when missing.
            includeInstances: Also export instances, such as Variables and Objects.
            includeCompleteServer: Also export the companion-specification nodes
                below the Server object, such as their namespace metadata and
                dictionaries.
            includeValues: Export the Value attribute of Variables and
                VariableTypes. With `"types"`, only the Values that types depend
                on: those of VariableTypes, of instance declarations and of
                DataType properties such as EnumStrings. With `False`, no Value
                elements are written.
            includeAccessAttributes: Also export the RolePermissions,
                AccessRestrictions and AccessLevelEx of every exported node.

        Raises:
            RuntimeError: The client is not connected.
            ValueError: `includeValues` is not `True`, `False` or `"types"`.
        """
        from o6._information_model_generation import _Crawler

        if includeValues not in (True, False, "types"):
            raise ValueError(f'includeValues must be True, False or "types", not {includeValues!r}')

        async def _export() -> list[Path]:
            crawler = _Crawler(
                self,
                includeInstances=includeInstances,
                includeCompleteServer=includeCompleteServer,
                includeValues=includeValues,
                includeAccessAttributes=includeAccessAttributes,
            )
            model = await crawler.run()
            return model.save(directory)

        return self._run_on_loop(_export)

    # NodeManagement Service Set

    def serviceAddNodes(
        self, request: ns0.datatypes.AddNodesRequest
    ) -> MaybeAwaitable[ns0.datatypes.AddNodesResponse]:
        """Call the AddNodes service to add one or more nodes to the address space.

        [OPC UA Part 4 §5.8.2](https://reference.opcfoundation.org/specs/OPC-10000-4/5.8.2)"""
        return self._run_on_loop(
            lambda: self._mutate_address_space(self._service_addNodes(request))
        )

    def serviceDeleteNodes(
        self, request: ns0.datatypes.DeleteNodesRequest
    ) -> MaybeAwaitable[ns0.datatypes.DeleteNodesResponse]:
        """Call the DeleteNodes service to remove one or more nodes from the address space.

        [OPC UA Part 4 §5.8.4](https://reference.opcfoundation.org/specs/OPC-10000-4/5.8.4)"""
        return self._run_on_loop(
            lambda: self._mutate_address_space(self._service_deleteNodes(request))
        )

    def serviceAddReferences(
        self, request: ns0.datatypes.AddReferencesRequest
    ) -> MaybeAwaitable[ns0.datatypes.AddReferencesResponse]:
        """Call the AddReferences service to add references between nodes.

        [OPC UA Part 4 §5.8.3](https://reference.opcfoundation.org/specs/OPC-10000-4/5.8.3)"""
        return self._run_on_loop(
            lambda: self._mutate_address_space(self._service_addReferences(request))
        )

    def serviceDeleteReferences(
        self, request: ns0.datatypes.DeleteReferencesRequest
    ) -> MaybeAwaitable[ns0.datatypes.DeleteReferencesResponse]:
        """Call the DeleteReferences service to remove references between nodes.

        [OPC UA Part 4 §5.8.5](https://reference.opcfoundation.org/specs/OPC-10000-4/5.8.5)"""
        return self._run_on_loop(
            lambda: self._mutate_address_space(self._service_deleteReferences(request))
        )

    # View Service Set

    def serviceBrowse(
        self, request: ns0.datatypes.BrowseRequest
    ) -> MaybeAwaitable[ns0.datatypes.BrowseResponse]:
        """Call the Browse service to navigate the address space from one or more start nodes.

        Returns the references that match each `BrowseDescription`. If a
        result has a continuation point, continue with
        [serviceBrowseNext][o6.client.Client.serviceBrowseNext].

        [OPC UA Part 4 §5.9.2](https://reference.opcfoundation.org/specs/OPC-10000-4/5.9.2)"""
        return self._run_on_loop(partial(self._service_browse, request))

    def serviceBrowseNext(
        self, request: ns0.datatypes.BrowseNextRequest
    ) -> MaybeAwaitable[ns0.datatypes.BrowseNextResponse]:
        """Call the BrowseNext service to continue a Browse that returned a continuation point.

        [OPC UA Part 4 §5.9.3](https://reference.opcfoundation.org/specs/OPC-10000-4/5.9.3)"""
        return self._run_on_loop(partial(self._service_browseNext, request))

    def serviceTranslateBrowsePathsToNodeIds(
        self, request: ns0.datatypes.TranslateBrowsePathsToNodeIdsRequest
    ) -> MaybeAwaitable[ns0.datatypes.TranslateBrowsePathsToNodeIdsResponse]:
        """Call the TranslateBrowsePathsToNodeIds service to resolve BrowsePaths to NodeIds.

        [OPC UA Part 4 §5.9.4](https://reference.opcfoundation.org/specs/OPC-10000-4/5.9.4)"""
        return self._run_on_loop(partial(self._service_translateBrowsePathsToNodeIds, request))

    def serviceRegisterNodes(
        self, request: ns0.datatypes.RegisterNodesRequest
    ) -> MaybeAwaitable[ns0.datatypes.RegisterNodesResponse]:
        """Call the RegisterNodes service to obtain optimized NodeIds for repeated access.

        [OPC UA Part 4 §5.9.5](https://reference.opcfoundation.org/specs/OPC-10000-4/5.9.5)"""
        return self._run_on_loop(partial(self._service_registerNodes, request))

    def serviceUnregisterNodes(
        self, request: ns0.datatypes.UnregisterNodesRequest
    ) -> MaybeAwaitable[ns0.datatypes.UnregisterNodesResponse]:
        """Call the UnregisterNodes service to release NodeIds obtained with RegisterNodes.

        [OPC UA Part 4 §5.9.6](https://reference.opcfoundation.org/specs/OPC-10000-4/5.9.6)"""
        return self._run_on_loop(partial(self._service_unregisterNodes, request))

    # Attribute Service Set

    def serviceRead(
        self, request: ns0.datatypes.ReadRequest
    ) -> MaybeAwaitable[ns0.datatypes.ReadResponse]:
        """Call the Read service to read one or more node attributes.

        Decodes only the DataTypes the client already has; values of unknown
        DataTypes stay `ExtensionObject`s. Unlike `read()`, it never loads a
        DataType from the server.

        [OPC UA Part 4 §5.11.2](https://reference.opcfoundation.org/specs/OPC-10000-4/5.11.2)"""
        return self._run_on_loop(partial(self._service_read, request))

    def serviceHistoryRead(
        self, request: ns0.datatypes.HistoryReadRequest
    ) -> MaybeAwaitable[ns0.datatypes.HistoryReadResponse]:
        """Call the HistoryRead service to read historical values or events from nodes.

        Decodes only the DataTypes the client already has; values of unknown
        DataTypes stay `ExtensionObject`s. Unlike `historyRead()`, it never
        loads a DataType from the server.

        [OPC UA Part 4 §5.11.3](https://reference.opcfoundation.org/specs/OPC-10000-4/5.11.3)"""
        return self._run_on_loop(partial(self._service_historyRead, request))

    def serviceWrite(
        self, request: ns0.datatypes.WriteRequest
    ) -> MaybeAwaitable[ns0.datatypes.WriteResponse]:
        """Call the Write service to write one or more node attribute values.

        [OPC UA Part 4 §5.11.4](https://reference.opcfoundation.org/specs/OPC-10000-4/5.11.4)"""
        if any(item.attributeId == o6.AttributeId.BROWSE_NAME for item in request.nodesToWrite):
            return self._run_on_loop(
                lambda: self._mutate_address_space(self._service_write(request))
            )
        return self._run_on_loop(partial(self._service_write, request))

    def serviceHistoryUpdate(
        self, request: ns0.datatypes.HistoryUpdateRequest
    ) -> MaybeAwaitable[ns0.datatypes.HistoryUpdateResponse]:
        """Call the HistoryUpdate service to insert, replace, or delete historical data.

        [OPC UA Part 4 §5.11.5](https://reference.opcfoundation.org/specs/OPC-10000-4/5.11.5)"""
        return self._run_on_loop(partial(self._service_historyUpdate, request))

    # Method Service Set

    def serviceCall(
        self, request: ns0.datatypes.CallRequest
    ) -> MaybeAwaitable[ns0.datatypes.CallResponse]:
        """Call the Call service to invoke one or more Methods.

        Decodes only the DataTypes the client already has; values of unknown
        DataTypes stay `ExtensionObject`s. Unlike `call()`, it never loads a
        DataType from the server.

        [OPC UA Part 4 §5.12.2](https://reference.opcfoundation.org/specs/OPC-10000-4/5.12.2)"""
        return self._run_on_loop(partial(self._service_call, request))

    def getRemoteDataTypes(
        self, typeNodes: list[NodeIdLike] | None = None
    ) -> MaybeAwaitable[list[dict[str, Any]]]:
        # UA_Client_getRemoteDataTypes (the C equivalent) uses synchronous OPC UA
        # service calls internally. Those spin-wait in el->run expecting I/O events,
        # but AsyncIOLoop_run only processes delayed callbacks — actual TCP data
        # arrives exclusively through Python asyncio data_received callbacks, which
        # can only fire when the event loop thread is idle. The result is a
        # guaranteed deadlock: the event loop thread blocks in el->run waiting for
        # a response that can never arrive while it is blocked. Using
        # service_read / service_browse here sidesteps this entirely: each call
        # registers an async future and returns immediately, letting the event loop
        # deliver the TCP response via data_received before the next await.
        """Read custom `StructureDefinition` data types from the server.

        Browses the DataType hierarchy below `Structure` (`i=22`) and reads
        the DataTypeDefinition and BrowseName of every DataType found. Only
        DataTypes with a `StructureDefinition` are returned: structures,
        structures with optional fields, and unions. Subtypes referenced by
        an ExpandedNodeId with a namespace URI or server index are skipped.

        Args:
            typeNodes: DataType NodeIds to read instead of browsing the
                hierarchy. An empty list returns `[]` without contacting the
                server. `None` browses the whole hierarchy.

        Returns:
            One `dict` per DataType, with the keys:

            - `typeName` (`str`): `BrowseName.name` of the DataType.
            - `typeId` (`NodeId`): NodeId of the DataType.
            - `binaryEncodingId` (`NodeId`): the `StructureDefinition.defaultEncodingId`.
            - `structureType` ([`StructureType`][o6.ns.ns0.datatypes.StructureType]): the structure category.
            - `membersSize` (`int`): number of fields.
        """
        nodeids = [o6.NodeId(n) for n in typeNodes] if typeNodes is not None else None

        async def _browse_subtypes(root: o6.NodeId) -> list[o6.NodeId]:
            found: list[o6.NodeId] = []
            visited = {root}
            to_visit = [root]
            while to_visit:
                current = to_visit.pop()
                references = await self.browse(
                    current,
                    reftype=ns0.reftypes.HasSubtype,
                    refsubtypes=False,
                    nodeClassMask=ns0.datatypes.NodeClass.DATA_TYPE,
                )
                for reference in references:
                    target = reference.nodeId
                    # Expanded identities cannot be read as local NodeIds.
                    if target.svr or target.nsu:
                        continue
                    child = o6.NodeId(target)
                    if child not in visited:
                        visited.add(child)
                        found.append(child)
                        to_visit.append(child)
            return found

        async def _call() -> list[dict[str, Any]]:
            if nodeids is not None and len(nodeids) == 0:
                return []

            if nodeids is None:
                # UA_NS0ID_STRUCTURE = 22 — browse the DataType hierarchy
                actual: list[o6.NodeId] = await _browse_subtypes(o6.NodeId(22))
            else:
                actual = nodeids

            if not actual:
                return []

            # Read DataTypeDefinition + BrowseName attributes for all NodeIds
            read_req = ns0.datatypes.ReadRequest()
            rvis: list[ns0.datatypes.ReadValueId] = []
            for nid in actual:
                rvi = ns0.datatypes.ReadValueId()
                rvi.nodeId = nid
                rvi.attributeId = o6.AttributeId.DATA_TYPE_DEFINITION
                rvis.append(rvi)
            for nid in actual:
                rvi = ns0.datatypes.ReadValueId()
                rvi.nodeId = nid
                rvi.attributeId = o6.AttributeId.BROWSE_NAME
                rvis.append(rvi)
            read_req.nodesToRead = rvis  # type: ignore[assignment]

            # service_read is fully async — the asyncio event loop thread stays
            # free to deliver the response, so there is no deadlock.
            response = await self.serviceRead(read_req)  # type: ignore[attr-defined, misc]

            response.responseHeader.serviceResult.check(message="Read datatype definitions")
            n = len(actual)
            if len(response.results) != 2 * n:
                raise RuntimeError("Datatype Read result count does not match the request")
            result: list[dict[str, Any]] = []
            for i, nid in enumerate(actual):
                definition, name = response.results[i], response.results[i + n]
                o6.StatusCode(name.status or 0).check(message=f"BrowseName of {nid}")
                # Built-in and abstract types may not expose this optional attribute.
                if definition.status == o6.StatusCode.BAD_ATTRIBUTE_ID_INVALID:
                    continue
                o6.StatusCode(definition.status or 0).check(message=f"DataTypeDefinition of {nid}")
                sd = definition.value
                if not isinstance(sd, ns0.datatypes.StructureDefinition):
                    continue
                qn = name.value
                if not isinstance(qn, o6.QualifiedName):
                    raise RuntimeError(f"Datatype BrowseName of {nid} is not a QualifiedName")
                type_name = qn.name or ""
                result.append(
                    {
                        "typeName": type_name,
                        "typeId": nid,
                        "binaryEncodingId": sd.defaultEncodingId,
                        "structureType": sd.structureType,
                        "membersSize": len(sd.fields),
                    }
                )
            return result

        return self._run_on_loop(_call)

    def loadRemoteDataTypes(self) -> MaybeAwaitable[list[type]]:
        """Load the server's custom DataTypes, so their values decode to Python classes.

        Refreshes the namespace mapping, browses the DataType hierarchy and
        registers the structures of every server namespace the client has no
        package for, with the enumerations their fields use. Afterwards values
        of these types decode to Python classes on every path: reads, method
        outputs, history and subscriptions. Without the call, the client loads
        a DataType when it first receives a value of it (see
        `loadUnknownDataTypes`), but the first subscription notification of
        each type stays an [`ExtensionObject`][o6.ExtensionObject].

        Namespaces with a package, bundled or declared by the application, are
        never extended or replaced, even when the server has a newer version.
        Only the binary encoding is registered.

        A DataType that cannot be loaded logs a warning, and its values stay
        `ExtensionObject`s. This includes the structures of servers before
        OPC UA 1.04, which describe them in DataType dictionaries instead of the
        `DataTypeDefinition` attribute, and structures that contain
        themselves. Each call browses the DataTypes again; types the client
        already decodes are skipped, also after a reconnect.

        ```python
        with o6.Client("opc.tcp://localhost:4840") as client:
            client.loadRemoteDataTypes()
            print(client.read("ns=2;s=Demo.WorkOrder.WorkOrderVariable"))
        ```

        Returns:
            The Python classes this call registered, in registration order.

        Raises:
            RuntimeError: The client is not connected.
            StatusCodeError: A Browse or Read service call failed.
        """
        return self._run_on_loop(lambda: _RemoteDataTypes(self).run())

    def updateRemoteNamespaces(self) -> MaybeAwaitable[None]:
        """Refresh the namespace mapping and custom DataTypes from the server.

        When a URI has several compiled versions, the client reads the
        server's NamespaceMetadata and selects the exact version, or else the
        latest one. The Python mapping, the decoder mapping of the
        SecureChannel and the custom DataTypes are replaced together. A failed
        refresh leaves the previous state usable. An unchanged mapping is not
        rebuilt. Call it again when the server adds namespaces at runtime.

        Raises:
            RuntimeError: The client is not connected.
        """

        async def _update() -> None:
            self._node_backend.invalidate_children()

            METADATA_TYPE = o6.NodeId(ns0.objtypes.NamespaceMetadataType)

            async def _get_namespace_version_and_publication_date(
                mapped_index: int,
            ) -> tuple[str, str]:
                # browse Objects folder for NamespaceMetadataType nodes
                mask = int(
                    ns0.datatypes.BrowseResultMask.TYPE_DEFINITION
                    | ns0.datatypes.BrowseResultMask.BROWSE_NAME
                    | ns0.datatypes.BrowseResultMask.NODE_CLASS
                )
                version_val = ""
                pub_date_val = ""
                for ref in await cast(
                    Awaitable[Any],
                    self.browse(
                        o6.NodeId(ns0.instances.objects),
                        resultMask=mask,
                    ),
                ):
                    if str(ref.typeDefinition) != str(METADATA_TYPE):
                        continue
                    if ref.nodeId.ns != mapped_index:
                        continue

                    # browse children of the metadata object
                    for child in await cast(
                        Awaitable[Any],
                        self.browse(ref.nodeId, resultMask=_child_browse_result_mask()),
                    ):
                        if int(child.nodeClass) != int(ns0.datatypes.NodeClass.VARIABLE):
                            continue
                        if child.nodeId.ns != ref.nodeId.ns:
                            continue
                        bn = str(child.browseName)
                        name = bn.split(":", 1)[-1]
                        try:
                            val = await self.read(child.nodeId)
                        except o6.StatusCodeError:
                            continue
                        if name == "NamespaceVersion":
                            version_val = str(val) if val is not None else ""
                        elif name == "NamespacePublicationDate":
                            pub_date_val = str(val) if val is not None else ""
                    break  # found the matching metadata object

                return (version_val, pub_date_val)

            if not self.connected:
                raise RuntimeError("Client is not connected")

            namespace_array = await self.read(o6.NodeId(o6.ns["i=2255"]))
            if namespace_array is None:
                return
            uris = [str(uri) for uri in namespace_array]
            entries: list[tuple[str, int, int]] = []
            if uris:
                entries.append((uris[0], 0, 0))
            if len(uris) > 1:
                entries.append((uris[1], 1, 1))
                application_index = getattr(self, "_application_namespace_index", None)
                if application_index is not None:
                    entries.append((uris[1], application_index, 1))

            scope = self._name
            candidates: dict[int, list[Any]] = {}
            selected: dict[int, Any] = {}
            for wire_index, uri in enumerate(uris[2:], 2):
                if not uri:
                    continue
                hits = [
                    hit
                    for hit in o6.ns.filter(uri=uri)
                    if hit.scope in (scope, o6.ns._GLOBAL_SCOPE)
                ]
                if not hits:
                    hits = [
                        o6.ns.register(
                            shortname=_remote_namespace_shortname(uri, scope),
                            uri=uri,
                            scope=scope,
                        )
                    ]
                candidates[wire_index] = hits
                selected[wire_index] = _select_namespace_candidate(hits, scope)
            _load_namespace_modules(selected.values())

            provisional = [
                *entries,
                *(
                    (uris[wire_index], info.index, wire_index)
                    for wire_index, info in sorted(selected.items())
                ),
            ]
            ambiguous = {
                wire_index: hits for wire_index, hits in candidates.items() if len(hits) > 1
            }
            previous_uris = getattr(self, "_namespace_snapshot_uris", None)
            previous_selected = getattr(self, "_namespace_snapshot_selected", {})
            # The application count after the provisional mapping; None when not applied.
            provisional_applied: int | None = None
            if ambiguous and previous_uris != uris:
                self._apply_namespace_snapshot(uris, provisional)
                provisional_applied = self._namespace_applications
            try:
                for wire_index, hits in ambiguous.items():
                    mapped_index = previous_selected.get(wire_index, selected[wire_index].index)
                    server_version, _ = await _get_namespace_version_and_publication_date(
                        mapped_index
                    )
                    selected[wire_index] = _select_namespace_candidate(hits, scope, server_version)
                    chosen = selected[wire_index]
                    if (
                        chosen.version
                        and server_version
                        and _version_key(chosen.version) < _version_key(server_version)
                    ):
                        self._logger.warning(
                            f"Namespace URI {uris[wire_index]} from server has version "
                            f"{server_version} which is newer than the client's best match "
                            f"version {chosen.version}."
                        )
                if ambiguous:
                    _load_namespace_modules(selected.values())

                final = [
                    *entries,
                    *(
                        (uris[wire_index], info.index, wire_index)
                        for wire_index, info in sorted(selected.items())
                    ),
                ]
                final_snapshot = tuple(final)
                # A DataType lookup during the awaits re-applies the previous
                # snapshot; the provisional mapping is then no longer applied.
                if final_snapshot != getattr(self, "_namespace_snapshot", None) and not (
                    provisional_applied == self._namespace_applications and final == provisional
                ):
                    self._apply_namespace_snapshot(uris, final)
            # Not BaseException: a coroutine closed by the GC may outlive the native client.
            except (Exception, asyncio.CancelledError):
                current_uris = getattr(self, "_namespace_snapshot_uris", None)
                current = getattr(self, "_namespace_snapshot", None)
                if provisional_applied is not None and current_uris and current is not None:
                    # A failed refresh leaves the current snapshot applied.
                    try:
                        self._apply_namespace_snapshot(current_uris, list(current))
                    except Exception:
                        self._logger.exception(
                            "Restoring the namespace mapping after a failed refresh failed"
                        )
                raise
            self._namespace_snapshot = final_snapshot
            self._namespace_snapshot_uris = uris
            self._namespace_snapshot_selected = {
                wire_index: info.index for wire_index, info in selected.items()
            }

        return self._run_on_loop(_update)

    #
    # Simplified Service API
    #

    # Discovery

    def registerServer(
        self,
        serverUri: str,
        discoveryUrls: list[str],
        *,
        serverName: LocalizedTextLike,
        productUri: str = "",
        serverType: ns0.datatypes.ApplicationType = ns0.datatypes.ApplicationType.SERVER,
        mdnsServerName: str | None = None,
        serverCapabilities: list[str] | None = None,
    ) -> MaybeAwaitable[None]:
        """Register or update an application with the connected discovery server.

        A connection with `noSession=True` is enough. Calling it again with
        the same URI and at least one of the same discovery URLs renews or
        updates the registration. To replace every URL, unregister the old
        ones first. Renewal is not scheduled, and security settings are not
        changed. Async callers must await the result. An open62541 LDS
        requires a signed channel whose client certificate carries `serverUri`.

        Sends RegisterServer2. Falls back to RegisterServer only on
        `BadServiceUnsupported` and only when neither mDNS option is given,
        so no mDNS metadata is lost. An explicitly empty option also prevents
        the fallback.

        Args:
            serverUri: Stable URI of the application.
            discoveryUrls: URLs where clients can discover the application.
            serverName: Display name, optionally with a locale.
            productUri: Product URI of the application.
            serverType: Application type.
            mdnsServerName: mDNS name. Defaults to the text of `serverName`
                when only `serverCapabilities` is given.
            serverCapabilities: mDNS capability identifiers, such as `["DA"]`.
                Without both mDNS options, no discovery configuration is sent.

        Returns:
            `None` once the service and all configuration results succeed.
            mDNS publication or reception is not guaranteed.

        Raises:
            StatusCodeError: The registration or a configuration was rejected.
                The status code is preserved. A configuration can fail after
                the LDS accepted the registration; unregister to remove it.
            RuntimeError: The number of configuration results is wrong.
        """
        name = o6.LocalizedText(serverName)
        registered = ns0.datatypes.RegisteredServer(
            serverUri=serverUri,
            productUri=productUri,
            serverNames=[name],
            serverType=serverType,
            discoveryUrls=discoveryUrls,
            isOnline=True,
        )
        configuration = None
        if mdnsServerName is not None or serverCapabilities is not None:
            configuration = ns0.datatypes.MdnsDiscoveryConfiguration(
                mdnsServerName=name.text if mdnsServerName is None else mdnsServerName,
                serverCapabilities=[] if serverCapabilities is None else serverCapabilities,
            )
        return self._run_on_loop(partial(self._register_server, registered, configuration))

    def unregisterServer(self, serverUri: str, discoveryUrls: list[str]) -> MaybeAwaitable[None]:
        """Remove an application registration from the connected discovery server.

        Uses the current connection and security settings. Sends
        RegisterServer2 and falls back to RegisterServer only on
        `BadServiceUnsupported`. No local state is needed: the URI and the
        shared URLs identify the registration.

        Args:
            serverUri: URI used to register the application.
            discoveryUrls: At least one URL of the existing registration.

        Returns:
            `None` once the discovery server confirms the removal. Async
            callers must await it before disconnecting.

        Raises:
            StatusCodeError: The removal was rejected, also for an unknown
                registration.
            RuntimeError: The number of configuration results is wrong.
        """
        registered = ns0.datatypes.RegisteredServer(
            serverUri=serverUri,
            # Native removal validates a name before matching URI and URLs.
            serverNames=[o6.LocalizedText(serverUri)],
            discoveryUrls=discoveryUrls,
            isOnline=False,
        )
        return self._run_on_loop(partial(self._register_server, registered))

    async def _register_server(
        self,
        registered: ns0.datatypes.RegisteredServer,
        configuration: ns0.datatypes.MdnsDiscoveryConfiguration | None = None,
    ) -> None:
        configurations = [] if configuration is None else [o6.ExtensionObject(configuration)]
        request = ns0.datatypes.RegisterServer2Request(
            server=registered, discoveryConfiguration=configurations
        )
        response = await self._service_register_server2(request)
        status = response.responseHeader.serviceResult
        if status == o6.StatusCode.BAD_SERVICE_UNSUPPORTED and configuration is None:
            fallback = await self._service_register_server(
                ns0.datatypes.RegisterServerRequest(server=registered)
            )
            fallback.responseHeader.serviceResult.check(message="RegisterServer")
            return

        status.check(message="RegisterServer2")
        if len(response.configurationResults) != len(configurations):
            raise RuntimeError("RegisterServer2 returned an unexpected configuration result count")
        for index, result in enumerate(response.configurationResults):
            result.check(message=f"RegisterServer2 configuration {index}")

    def getEndpoints(
        self,
        endpointUrl: str,
        *,
        localeIds: list[str] | None = None,
        profileUris: list[str] | None = None,
    ) -> MaybeAwaitable[list[ns0.datatypes.EndpointDescription]]:
        """Return the endpoints advertised by a server.

        Sends GetEndpoints to `endpointUrl`. No Session is needed; a
        connection with `connect(noSession=True)` is enough.

        Args:
            endpointUrl: URL of the server, for example
                `"opc.tcp://localhost:4840"`.
            localeIds: Preferred locales for localized strings, for example
                `["en-US", "de-DE"]`. `None` uses the server default.
            profileUris: Return only endpoints with one of these transport
                profile URIs. `None` returns all endpoints.

        Returns:
            One [EndpointDescription][o6.ns.ns0.datatypes.EndpointDescription]
            per endpoint, with URL, security mode, security policy URI,
            transport profile URI, server certificate and
            [UserTokenPolicy][o6.ns.ns0.datatypes.UserTokenPolicy] entries.

        Raises:
            StatusCodeError: The discovery service failed or is unsupported.
        """

        async def _call():
            req = ns0.datatypes.GetEndpointsRequest()
            req.endpointUrl = endpointUrl
            if localeIds:
                req.localeIds = localeIds
            if profileUris:
                req.profileUris = profileUris
            response = await self._service_get_endpoints(req)
            response.responseHeader.serviceResult.check()
            return response.endpoints

        return self._run_on_loop(_call)

    def findServers(
        self,
        endpointUrl: str,
        *,
        serverUris: list[str] | None = None,
        localeIds: list[str] | None = None,
    ) -> MaybeAwaitable[list[ns0.datatypes.ApplicationDescription]]:
        """Return servers registered at a discovery server or known to a server.

        Sends FindServers to `endpointUrl`. An LDS returns the servers
        registered on its host. Any other server returns its own
        [ApplicationDescription][o6.ns.ns0.datatypes.ApplicationDescription].
        No Session is needed; `connect(noSession=True)` is enough.

        Args:
            endpointUrl: URL of the discovery server or server.
            localeIds: Preferred locales for `applicationName`. `None` uses
                the server default.
            serverUris: Return only servers with one of these application
                URIs. `None` returns all known servers.

        Returns:
            One [ApplicationDescription][o6.ns.ns0.datatypes.ApplicationDescription]
            per server, with application name, URI and type, product URI,
            and discovery URLs to pass to `getEndpoints`.

        Raises:
            StatusCodeError: The discovery service failed or is unsupported.
        """

        async def _call():
            req = ns0.datatypes.FindServersRequest()
            req.endpointUrl = endpointUrl
            if serverUris:
                req.serverUris = serverUris
            if localeIds:
                req.localeIds = localeIds
            response = await self._service_find_servers(req)
            response.responseHeader.serviceResult.check()
            return response.servers

        return self._run_on_loop(_call)

    def findServersOnNetwork(
        self,
        startingRecordId: int = 0,
        maxRecordsToReturn: int = 0,
        serverCapabilityFilter: list[str] | None = None,
    ) -> MaybeAwaitable[list[ns0.datatypes.ServerOnNetwork]]:
        """Return servers visible on the network via a Local Discovery Server (LDS).

        Sends FindServersOnNetwork to the connected LDS. The LDS lists the
        servers announced by mDNS or registered with RegisterServer2. A
        regular server returns an empty list or an error.

        Args:
            startingRecordId: Record ID to start from. `0` starts at the
                beginning. Use the `recordId` of the last entry to get the
                next page.
            maxRecordsToReturn: Maximum number of entries. `0` lets the server
                decide, usually all entries.
            serverCapabilityFilter: Return only servers that advertise all of
                these capabilities, such as `"DA"` (Data Access) or `"HE"`
                (Historical Events). `None` applies no filter.

        Returns:
            One [ServerOnNetwork][o6.ns.ns0.datatypes.ServerOnNetwork] per
            server, with name, discovery URL and capabilities.

        Raises:
            StatusCodeError: The discovery service failed or is unsupported.
        """

        async def _call():
            req = ns0.datatypes.FindServersOnNetworkRequest()
            req.startingRecordId = startingRecordId
            req.maxRecordsToReturn = maxRecordsToReturn
            if serverCapabilityFilter:
                req.serverCapabilityFilter = serverCapabilityFilter
            response = await self._service_find_servers_on_network(req)
            response.responseHeader.serviceResult.check()
            return response.servers

        return self._run_on_loop(_call)

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
            RuntimeError: The client is not connected.
        """
        is_scalar, request = _read_request(target, attr, timestampsToReturn, valueOnly, range)

        async def _read() -> Any:
            if not request.nodesToRead:
                return []
            if not self.connected:
                raise RuntimeError("Client is not connected")
            response = await self._service_read(request)
            _check_read_status(response.responseHeader.serviceResult)
            results = list(response.results)
            if len(results) != len(request.nodesToRead):
                raise RuntimeError("Read result count does not match the request")
            return await self._unknownDataTypes.decode(_read_results(results, is_scalar, valueOnly))

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

        Args:
            target: A NodeId-like value or Node, a list of them, or a mapping
                from target to value.
            value: The value for one target, or a list of equal length for a
                list of targets. Omit it for a mapping. A list for a single
                target is an array value. `None` writes a null value where the
                target allows it. Omitting the value for a single target
                raises `ValueError`. A DataValue keeps its supported status and
                timestamps. An attribute other than Value needs a value of its
                DataType, and status or timestamps give
                `BAD_WRITE_NOT_SUPPORTED`.
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
        request = ns0.datatypes.WriteRequest()
        items = []
        positions = []
        results = []
        for index, (nodeid, val, index_range) in enumerate(zip(nodeids, values, ranges)):
            payload = _write_payload(val)
            status = _write_payload_status(payload, attribute)
            results.append(status)
            if status != o6.StatusCode.GOOD:
                continue
            item = ns0.datatypes.WriteValue()
            item.nodeId = nodeid
            item.attributeId = attribute
            if index_range:
                item.indexRange = index_range
            item.value = payload
            items.append(item)
            positions.append(index)
        request.nodesToWrite = items

        async def _write() -> o6.StatusCode | list[o6.StatusCode]:
            if items:
                if not self.connected:
                    raise RuntimeError("Client is not connected")
                response = await self.serviceWrite(request)
                response.responseHeader.serviceResult.check(message="Write service")
                if len(response.results) != len(items):
                    raise RuntimeError("Write result count does not match the request")
                for index, status in zip(positions, response.results):
                    results[index] = status
            return results[0] if is_scalar else results

        return self._run_on_loop(_write)

    def call(
        self, objectId: NodeIdLike, methodId: NodeIdLike, inputArgs: list[Any] = []
    ) -> MaybeAwaitable[tuple[o6.StatusCode, *tuple[Any, ...]]]:
        """Call a Method on an Object.

        Args:
            objectId: The Object that owns the Method.
            methodId: The Method to call.
            inputArgs: InputArguments values, in declaration order.

        Returns:
            `(statusCode, output1, output2, ...)`, or `(statusCode,)` without
            outputs. Bad method statuses, including an invalid Method or
            invalid arguments, are returned with any available outputs.

        Raises:
            StatusCodeError: The Call service failed. `code` holds the status.
                Bad method results do not raise.
            TypeError: An argument cannot be converted to an OPC UA value.
            RuntimeError: The client is not connected.
        """

        async def _call() -> tuple[o6.StatusCode, *tuple[Any, ...]]:
            if not self.connected:
                raise RuntimeError("Client is not connected")

            # Create call request
            method_request = ns0.datatypes.CallMethodRequest()
            method_request.objectId = o6.NodeId(objectId)
            method_request.methodId = o6.NodeId(methodId)
            method_request.inputArguments = [_normalize_nodeids(arg) for arg in inputArgs]

            call_request = ns0.datatypes.CallRequest()
            call_request.methodsToCall = [method_request]

            # Call
            response = await self._service_call(call_request)

            # Consistency check the result
            if response.responseHeader.serviceResult != 0:
                raise o6.StatusCodeError(response.responseHeader.serviceResult)
            if len(response.results) != len(call_request.methodsToCall):
                raise RuntimeError("Call result count does not match the request")

            # Return result
            result = response.results[0]
            outputs = await self._unknownDataTypes.decode(list(result.outputArguments))
            return (result.statusCode, *outputs)

        return self._run_on_loop(_call)

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

        Continuation points are followed with BrowseNext until all references
        are collected.

        Args:
            target: The node to browse from.
            direction: `FORWARD`, `INVERSE` or `BOTH`.
            reftype: Only follow this ReferenceType, or `None` for all.
            refsubtypes: Also follow subtypes of `reftype`.
            nodeClassMask: `NodeClass` members combined with `|`. Only nodes
                of these NodeClasses are returned.
            resultMask: `BrowseResultMask` members combined with `|`, selecting
                the reference fields to fill in. Defaults to `ALL`. `NONE`
                returns only the target NodeIds.

        Returns:
            A flat list of every `ReferenceDescription`. Async tasks must
            await the call.

        Raises:
            StatusCodeError: Browse or BrowseNext failed. On failure or
                cancellation, open continuation points are released where
                possible.
            RuntimeError: The client is not connected.
        """

        async def _browse() -> list[ns0.datatypes.ReferenceDescription]:
            if not self.connected:
                raise RuntimeError("Client is not connected")

            # Prepare the BrowseRequest
            bd = ns0.datatypes.BrowseDescription()
            bd.nodeId = o6.NodeId(target)
            bd.browseDirection = direction
            bd.referenceTypeId = o6.NodeId(reftype)
            bd.includeSubtypes = refsubtypes
            bd.nodeClassMask = nodeClassMask
            bd.resultMask = resultMask
            request = ns0.datatypes.BrowseRequest()
            request.nodesToBrowse = [bd]

            async def next_page(token: bytes, release: bool = False) -> Any:
                next_request = ns0.datatypes.BrowseNextRequest(
                    releaseContinuationPoints=release, continuationPoints=[token]
                )
                return await self._service_browseNext(next_request)

            collection = _BrowseCollection()

            async def fetch(operation: Awaitable[Any]) -> None:
                response = await operation
                # Adopt the token before checking statuses so even failed pages
                # can be released after cancellation or a service failure.
                if len(response.results) == 1:
                    page = response.results[0]
                    if page.continuationPoint or (
                        response.responseHeader.serviceResult == 0 and page.statusCode == 0
                    ):
                        collection.continuation_point = page.continuationPoint
                response.responseHeader.serviceResult.check()
                if len(response.results) != 1:
                    raise RuntimeError("Browse result count does not match the request")
                collection.append(response.results[0])

            try:
                await _finish_request(fetch(self._service_browse(request)))
                while collection.continuation_point:
                    await _finish_request(fetch(next_page(collection.continuation_point)))
                self._node_backend.invalidate_children(bd.nodeId)
                return collection.references
            finally:
                if collection.continuation_point:
                    with suppress(Exception):
                        await _finish_request(
                            next_page(collection.continuation_point, release=True)
                        )

        return self._run_on_loop(_browse)

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
        """Fetch one page of references, like `Server.browsePage`.

        Args:
            target: The node to browse from.
            maxReferences: Requested page size. `0` means no client-side limit.
            direction: `FORWARD`, `INVERSE` or `BOTH`.
            reftype: Only follow this ReferenceType. Defaults to
                `HierarchicalReferences`.
            refsubtypes: Also follow subtypes of `reftype`.
            nodeClassMask: `NodeClass` members combined with `|`. `0` returns
                all NodeClasses.
            resultMask: `BrowseResultMask` members combined with `|`. Defaults
                to `ALL`. `0` returns only the target NodeIds.

        Returns:
            One BrowseResult. Continue with `browseNext(False, token)`, or
            release an unused token with `browseNext(True, token)`. Tokens
            belong to this Session. Await it in async code.

        Raises:
            StatusCodeError: The service or the browse of the node failed.
        """
        request = ns0.datatypes.BrowseRequest(
            requestedMaxReferencesPerNode=maxReferences,
            nodesToBrowse=[
                _browse_description(
                    target, direction, reftype, refsubtypes, nodeClassMask, resultMask
                )
            ],
        )

        async def first() -> ns0.datatypes.BrowseResult:
            pages = await self._browse_pages(self._service_browse(request), 1)
            return pages[0]

        return self._run_on_loop(first)

    async def _browse_pages(
        self, operation: Awaitable[Any], count: int, tokens: tuple[bytes, ...] = ()
    ) -> list[ns0.datatypes.BrowseResult]:
        outstanding = set(tokens)
        pages: list[ns0.datatypes.BrowseResult] = []

        async def fetch() -> None:
            response = await operation
            pages.extend(response.results)
            outstanding.update(page.continuationPoint for page in pages if page.continuationPoint)
            response.responseHeader.serviceResult.check()
            if len(pages) != count:
                raise RuntimeError("Browse result count does not match the request")
            for page in pages:
                page.statusCode.check()

        try:
            await _finish_request(fetch())
            return pages
        except BaseException:
            if outstanding:
                request = ns0.datatypes.BrowseNextRequest(
                    releaseContinuationPoints=True, continuationPoints=list(outstanding)
                )
                with suppress(Exception):
                    await _finish_request(self._service_browseNext(request))
            raise

    def browseNext(
        self,
        releaseContinuationPoint: bool,
        continuationPoint: bytes | list[bytes] | tuple[bytes, ...],
    ) -> MaybeAwaitable[list[ns0.datatypes.BrowseResult]]:
        """Continue or release pages from `browsePage`.

        Args:
            releaseContinuationPoint: Release the tokens instead of fetching
                pages.
            continuationPoint: One token, or a list or tuple of tokens of this
                Session.

        Returns:
            A list with one BrowseResult per token. An empty input returns
            `[]`. Await it in async code.

        Raises:
            StatusCodeError: The service or a continuation failed.
        """
        tokens = (
            tuple(continuationPoint)
            if isinstance(continuationPoint, (list, tuple))
            else (continuationPoint,)
        )

        async def next_pages() -> list[ns0.datatypes.BrowseResult]:
            if not tokens:
                return []
            request = ns0.datatypes.BrowseNextRequest(
                releaseContinuationPoints=releaseContinuationPoint,
                continuationPoints=list(tokens),
            )
            return await self._browse_pages(self._service_browseNext(request), len(tokens), tokens)

        return self._run_on_loop(next_pages)

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
        return self._run_on_loop(
            partial(_translate_paths, self._service_translateBrowsePathsToNodeIds, browsePath)
        )

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

    def browseInteractive(self, nodeId: NodeIdLike | None = None) -> Any:
        """Open a curses-based interactive browser for the address space.

        Requires the `curses` module. On Windows, install `windows-curses`.

        Args:
            nodeId: Start node. Defaults to the Objects folder.

        Returns:
            The selected NodeId string when the user quits with `n`, or the
            BrowsePath string with `p`. Otherwise `None`.

        Raises:
            ImportError: `curses` is not available.
        """
        try:
            from o6._browse_interactive import InteractiveBrowser
        except ImportError as e:
            raise ImportError(
                "browseInteractive() requires the 'curses' module. "
                "On Windows, install 'windows-curses': pip install windows-curses"
            ) from e
        return InteractiveBrowser(self, o6.NodeId(nodeId) if nodeId is not None else None).run()

    # History Access

    def historyRead(
        self,
        target: NodeIdLike | list[NodeIdLike],
        startTime: datetime.datetime,
        endTime: datetime.datetime,
        numValuesPerNode: int = 0,
        returnBounds: bool = False,
        timestampsToReturn: ns0.datatypes.TimestampsToReturn = ns0.datatypes.TimestampsToReturn.BOTH,
    ) -> Any:
        """Read raw historical values for one or more nodes.

        Continuation points are followed until the interval or the per-node
        limit is exhausted.

        Args:
            target: A node, or a list of nodes.
            startTime: Start of the interval.
            endTime: End of the interval.
            numValuesPerNode: Maximum number of values per node. `0` means no
                limit.
            returnBounds: Include the bounding values at the interval edges.
            timestampsToReturn: Timestamps to return with each value.

        Returns:
            The history data of one node, or a list in input order.

        Raises:
            StatusCodeError: The service or the read of a node failed.
            RuntimeError: The client is not connected.
        """

        async def _history_read() -> Any:
            if not self.connected:
                raise RuntimeError("Client is not connected")

            is_scalar = not isinstance(target, list)
            targets = cast(list[NodeIdLike], [target] if is_scalar else target)

            details = ns0.datatypes.ReadRawModifiedDetails()
            details.isReadModified = False
            details.startTime = o6.DateTime(startTime)
            details.endTime = o6.DateTime(endTime)
            details.numValuesPerNode = numValuesPerNode
            details.returnBounds = returnBounds

            request = ns0.datatypes.HistoryReadRequest()
            request.historyReadDetails = details
            request.timestampsToReturn = timestampsToReturn
            request.nodesToRead = [_history_read_value_id(nid) for nid in targets]

            nodes = request.nodesToRead
            tokens = [b""] * len(nodes)
            values: list[list[Any]] = [[] for _ in nodes]
            histories: list[Any] = [None] * len(nodes)
            active = list(range(len(nodes)))

            async def fetch() -> None:
                response = await self._service_historyRead(request)
                for index, result in zip(active, response.results):
                    tokens[index] = result.continuationPoint or b""
                if response.responseHeader.serviceResult == 0 and len(response.results) != len(
                    active
                ):
                    raise RuntimeError("HistoryRead returned an unexpected number of results")
                page = _unwrap_history_read(response, is_scalar, active)
                for index, history in zip(active, [page] if is_scalar else page):
                    histories[index] = history
                    values[index].extend(history.dataValues)

            try:
                while active:
                    request.nodesToRead = [nodes[index] for index in active]
                    await _finish_request(fetch())
                    active = [
                        index
                        for index in active
                        if tokens[index]
                        and (not numValuesPerNode or len(values[index]) < numValuesPerNode)
                    ]
                    for index in active:
                        nodes[index].continuationPoint = tokens[index]
                for index, history in enumerate(histories):
                    history.dataValues = await self._unknownDataTypes.decode(
                        values[index][:numValuesPerNode] if numValuesPerNode else values[index]
                    )
                return histories[0] if is_scalar else histories
            finally:
                outstanding = []
                for index, token in enumerate(tokens):
                    if token:
                        nodes[index].continuationPoint = token
                        outstanding.append(nodes[index])
                if outstanding:
                    request.nodesToRead = outstanding
                    request.releaseContinuationPoints = True
                    try:
                        await _finish_request(self._service_historyRead(request))
                    except Exception:
                        self._logger.warning(
                            "Could not release history continuation points", exc_info=True
                        )

        return self._run_on_loop(_history_read)

    def historyUpdateInsert(
        self,
        target: NodeIdLike,
        values: list[o6.DataValue],
    ) -> Any:
        """Insert new historical values into a node's history.

        Insertion fails for a timestamp that already has a value. Use
        `historyUpdateReplace` to overwrite values.

        Args:
            target: The node whose history is updated.
            values: The values to insert.

        Returns:
            The `HistoryUpdateResult` of the operation.
        """
        return self._history_update(target, values, ns0.datatypes.PerformUpdateType.INSERT)

    def historyUpdateReplace(
        self,
        target: NodeIdLike,
        values: list[o6.DataValue],
    ) -> Any:
        """Replace existing historical values for a node.

        A value must already exist at each timestamp. Use
        `historyUpdateInsert` to add values.

        Args:
            target: The node whose history is updated.
            values: The replacement values.

        Returns:
            The `HistoryUpdateResult` of the operation.
        """
        return self._history_update(target, values, ns0.datatypes.PerformUpdateType.REPLACE)

    def _history_update(
        self,
        target: NodeIdLike,
        values: list[o6.DataValue],
        mode: o6.PerformUpdateType,
    ) -> Any:

        async def _history_update() -> Any:
            if not self.connected:
                raise RuntimeError("Client is not connected")

            details = ns0.datatypes.UpdateDataDetails()
            details.nodeId = o6.NodeId(target)
            details.performInsertReplace = mode
            details.updateValues = values

            request = ns0.datatypes.HistoryUpdateRequest()
            request.historyUpdateDetails = [o6.ExtensionObject(details)]

            response = await self._service_historyUpdate(request)
            response.responseHeader.serviceResult.check(message="HistoryUpdate service")
            if len(response.results) != 1:
                raise RuntimeError("HistoryUpdate result count does not match the request")
            return response.results[0]

        return self._run_on_loop(_history_update)

    def historyUpdateDelete(
        self,
        target: NodeIdLike,
        startTime: datetime.datetime,
        endTime: datetime.datetime,
    ) -> Any:
        """Delete the raw historical values of a node in an interval.

        Args:
            target: The node whose history is deleted.
            startTime: Start of the interval.
            endTime: End of the interval.

        Returns:
            The `HistoryUpdateResult` of the operation.
        """

        async def _history_delete() -> Any:
            if not self.connected:
                raise RuntimeError("Client is not connected")

            details = ns0.datatypes.DeleteRawModifiedDetails()
            details.nodeId = o6.NodeId(target)
            details.isDeleteModified = False
            details.startTime = o6.DateTime(startTime)
            details.endTime = o6.DateTime(endTime)

            request = ns0.datatypes.HistoryUpdateRequest()
            request.historyUpdateDetails = [o6.ExtensionObject(details)]

            response = await self._service_historyUpdate(request)
            response.responseHeader.serviceResult.check(message="HistoryUpdate (delete) service")
            if len(response.results) != 1:
                raise RuntimeError("HistoryUpdate delete result count does not match the request")
            return response.results[0]

        return self._run_on_loop(_history_delete)

    # Node management

    def _add_node(
        self,
        *,
        parent: NodeIdLike,
        parent_reference: NodeIdLike,
        nodeclass: ns0.datatypes.NodeClass,
        browsename: o6.QualifiedName | str,
        requested_nodeid: NodeIdLike | None,
        attributes: Any,
        type_definition: NodeIdLike | None = None,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a generic node to the server address space.

        Parameters:
            parent: The parent node under which the new node is added.
            browseName: The BrowseName for the new node.
            nodeclass: The OPC UA node class for the new node.
            attributes: The node attributes object for the new node.
            requestedNodeId: Optionally request a specific node id.
            parentReference: The reference type used to link the new node.
            typeDefinition: The type definition node id, when applicable.

        Returns:
            The newly created node id."""

        async def _add() -> o6.NodeId:
            if not self.connected:
                raise RuntimeError("Client is not connected")

            item = ns0.datatypes.AddNodesItem()
            item.parentNodeId = o6.ExpandedNodeId(o6.NodeId(parent))
            item.referenceTypeId = o6.NodeId(parent_reference)
            item.requestedNewNodeId = (
                o6.ExpandedNodeId(o6.NodeId(requested_nodeid))
                if requested_nodeid
                else o6.ExpandedNodeId()
            )
            item.typeDefinition = (
                o6.ExpandedNodeId(o6.NodeId(type_definition))
                if type_definition
                else o6.ExpandedNodeId()
            )
            item.nodeClass = nodeclass

            if isinstance(browsename, str):
                item.browseName = o6.QualifiedName(browsename)
            else:
                item.browseName = browsename

            item.nodeAttributes = attributes

            request = ns0.datatypes.AddNodesRequest()
            request.nodesToAdd = [item]

            response = await self.serviceAddNodes(request)

            response.responseHeader.serviceResult.check(message="AddNodes service")
            if len(response.results) != 1:
                raise RuntimeError("Unexpected number of results from AddNodes")

            result = response.results[0]
            result.statusCode.check(message=f"AddNode {item.browseName}")

            return result.addedNodeId

        return self._run_on_loop(_add)

    def addObject(
        self,
        name: o6.LocalizedTextLike,
        parent: NodeIdLike,
        *,
        nodeId: NodeIdLike | None = None,
        typeDefinition: NodeIdLike = ns0.objtypes.BaseObjectType,
        ns: int = 1,
        parentReference: NodeIdLike = ns0.reftypes.Organizes,
    ) -> MaybeAwaitable[nodes.ObjectNode]:
        """Add an Object node and return its handle, like `Server.addObject`.

        Args:
            name: BrowseName and DisplayName of the Object.
            parent: Parent node.
            nodeId: Requested NodeId. The server assigns one when omitted;
                an o6 server uses its application namespace, index 1.
            typeDefinition: ObjectType of the new node.
            ns: Namespace index of the BrowseName.
            parentReference: ReferenceType from the parent to the new node.

        Returns:
            The ObjectNode, or an awaitable of it in async code. For an
            attribute-based call that returns a NodeId, use `addObjectNode`.

        Raises:
            StatusCodeError: Remote node creation failed.
        """
        name_id = o6.QualifiedName(f"{ns}:{name}")
        attributes = ns0.datatypes.ObjectAttributes(displayName=o6.LocalizedText(name))
        return self._run_on_loop(
            partial(
                self._create_convenience_node,
                nodes.ObjectNode,
                parent,
                parentReference,
                name_id,
                nodeId,
                attributes,
                typeDefinition,
            )
        )

    def addVariable(
        self,
        name: o6.LocalizedTextLike,
        parent: NodeIdLike,
        value: Any = None,
        *,
        nodeId: NodeIdLike | None = None,
        dataType: NodeIdLike | None = None,
        typeDefinition: NodeIdLike = ns0.vartypes.BaseDataVariableType,
        writable: bool = True,
        accessLevel: int | None = None,
        userAccessLevel: int | None = None,
        ns: int = 1,
        parentReference: NodeIdLike = ns0.reftypes.Organizes,
    ) -> MaybeAwaitable[nodes.VariableNode]:
        """Add a Variable node and return its handle, like `Server.addVariable`.

        History registration and Python behaviour are available on the server
        only.

        Args:
            name: BrowseName and DisplayName of the Variable.
            parent: Parent node.
            value: Initial value. Its DataType and ValueRank are inferred. An
                empty NumPy array keeps its DataType and ValueRank. An empty
                Python sequence requires `dataType`. A `DataValue` is
                rejected, because AddNodes carries no status or timestamps;
                write it after creation. With `dataType=o6.DataValue`, the
                DataValue is the value itself.
            nodeId: Requested NodeId. The server assigns one when omitted;
                an o6 server uses its application namespace, index 1.
            dataType: DataType of the Variable. Inferred from `value` when
                omitted.
            typeDefinition: VariableType of the new node.
            writable: Whether clients may write the Variable.
            accessLevel: The AccessLevel attribute as `AccessLevelType`
                flags. Replaces the level derived from `writable`.
            userAccessLevel: The UserAccessLevel attribute. Defaults to the
                AccessLevel. o6 servers derive UserAccessLevel from the
                AccessLevel and the session's permissions and ignore it.
            ns: Namespace index of the BrowseName.
            parentReference: ReferenceType from the parent to the new node.

        Returns:
            The VariableNode, or an awaitable of it in async code. For an
            attribute-based call that returns a NodeId, use `addVariableNode`.

        Raises:
            StatusCodeError: Remote node creation failed.
            TypeError: The initial value has no inferable datatype, or it is
                a `DataValue` and `dataType` is not DataValue.
        """
        if is_value_envelope(value, dataType):
            raise TypeError(
                "Client.addVariable() cannot create a Variable from a DataValue: AddNodes "
                "carries no status or timestamps. Pass the value and write the DataValue "
                "after creation."
            )
        attributes, _, _ = variable_attributes(
            name, value, dataType, writable, accessLevel, userAccessLevel
        )
        name_id = o6.QualifiedName(f"{ns}:{name}")
        return self._run_on_loop(
            partial(
                self._create_convenience_node,
                nodes.VariableNode,
                parent,
                parentReference,
                name_id,
                nodeId,
                attributes,
                typeDefinition,
            )
        )

    async def _create_convenience_node(
        self,
        node_type: type[nodes.Node],
        parent: NodeIdLike,
        reference: NodeIdLike,
        name: o6.QualifiedName,
        requested: NodeIdLike | None,
        attributes: Any,
        type_definition: NodeIdLike,
    ) -> Any:
        created = None

        async def create() -> None:
            nonlocal created
            created = await self._add_node(
                parent=parent,
                parent_reference=reference,
                nodeclass=(
                    ns0.datatypes.NodeClass.VARIABLE
                    if node_type is nodes.VariableNode
                    else ns0.datatypes.NodeClass.OBJECT
                ),
                browsename=name,
                requested_nodeid=requested,
                attributes=attributes,
                type_definition=type_definition,
            )

        try:
            await _finish_request(create())
            return node_type(self._node_backend, created, name)
        except BaseException as exc:
            if created is not None:

                async def rollback() -> None:
                    status = await self.deleteNode(created)
                    status.check()

                try:
                    await _finish_request(rollback())
                except Exception as rollback_error:
                    exc.add_note(f"Could not remove the incomplete node: {rollback_error}")
            raise

    def addVariableNode(
        self,
        *,
        parent: NodeIdLike,
        parentReference: NodeIdLike = ns0.reftypes.HasComponent,
        browseName: o6.QualifiedName | str,
        requestedNodeId: NodeIdLike | None = None,
        attributes: ns0.datatypes.VariableAttributes,
        typeDefinition: NodeIdLike = ns0.vartypes.BaseDataVariableType,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a Variable node from its attributes and return its NodeId.

        Args:
            parent: Parent node.
            parentReference: ReferenceType from the parent to the new node.
            browseName: BrowseName of the new node.
            requestedNodeId: Requested NodeId. The server assigns one when
                omitted.
            attributes: The `VariableAttributes` of the new node.
            typeDefinition: VariableType of the new node.

        Returns:
            The NodeId of the new node, or an awaitable of it in async code.

        Raises:
            StatusCodeError: The AddNodes service or the node creation failed.
            RuntimeError: The client is not connected.
        """
        return self._add_node(
            parent=parent,
            parent_reference=parentReference,
            nodeclass=ns0.datatypes.NodeClass.VARIABLE,
            browsename=browseName,
            requested_nodeid=requestedNodeId,
            attributes=attributes,
            type_definition=typeDefinition,
        )

    def addVariableTypeNode(
        self,
        *,
        parent: NodeIdLike,
        parentReference: NodeIdLike = ns0.reftypes.HasSubtype,
        browseName: o6.QualifiedName | str,
        requestedNodeId: NodeIdLike | None = None,
        attributes: ns0.datatypes.VariableTypeAttributes,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a VariableType node from its attributes and return its NodeId.

        Args:
            parent: Parent node.
            parentReference: ReferenceType from the parent to the new node.
            browseName: BrowseName of the new node.
            requestedNodeId: Requested NodeId. The server assigns one when
                omitted.
            attributes: The `VariableTypeAttributes` of the new node.

        Returns:
            The NodeId of the new node, or an awaitable of it in async code.

        Raises:
            StatusCodeError: The AddNodes service or the node creation failed.
            RuntimeError: The client is not connected.
        """
        return self._add_node(
            parent=parent,
            parent_reference=parentReference,
            nodeclass=ns0.datatypes.NodeClass.VARIABLE_TYPE,
            browsename=browseName,
            requested_nodeid=requestedNodeId,
            attributes=attributes,
        )

    def addObjectNode(
        self,
        *,
        parent: NodeIdLike,
        parentReference: NodeIdLike = ns0.reftypes.HasComponent,
        browseName: o6.QualifiedName | str,
        requestedNodeId: NodeIdLike | None = None,
        attributes: ns0.datatypes.ObjectAttributes,
        typeDefinition: NodeIdLike = ns0.objtypes.BaseObjectType,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add an Object node from its attributes and return its NodeId.

        Args:
            parent: Parent node.
            parentReference: ReferenceType from the parent to the new node.
            browseName: BrowseName of the new node.
            requestedNodeId: Requested NodeId. The server assigns one when
                omitted.
            attributes: The `ObjectAttributes` of the new node.
            typeDefinition: ObjectType of the new node.

        Returns:
            The NodeId of the new node, or an awaitable of it in async code.

        Raises:
            StatusCodeError: The AddNodes service or the node creation failed.
            RuntimeError: The client is not connected.
        """
        return self._add_node(
            parent=parent,
            parent_reference=parentReference,
            nodeclass=ns0.datatypes.NodeClass.OBJECT,
            browsename=browseName,
            requested_nodeid=requestedNodeId,
            attributes=attributes,
            type_definition=typeDefinition,
        )

    def addObjectTypeNode(
        self,
        *,
        parent: NodeIdLike,
        parentReference: NodeIdLike = ns0.reftypes.HasSubtype,
        browseName: o6.QualifiedName | str,
        requestedNodeId: NodeIdLike | None = None,
        attributes: ns0.datatypes.ObjectTypeAttributes,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add an ObjectType node from its attributes and return its NodeId.

        Args:
            parent: Parent node.
            parentReference: ReferenceType from the parent to the new node.
            browseName: BrowseName of the new node.
            requestedNodeId: Requested NodeId. The server assigns one when
                omitted.
            attributes: The `ObjectTypeAttributes` of the new node.

        Returns:
            The NodeId of the new node, or an awaitable of it in async code.

        Raises:
            StatusCodeError: The AddNodes service or the node creation failed.
            RuntimeError: The client is not connected.
        """
        return self._add_node(
            parent=parent,
            parent_reference=parentReference,
            nodeclass=ns0.datatypes.NodeClass.OBJECT_TYPE,
            browsename=browseName,
            requested_nodeid=requestedNodeId,
            attributes=attributes,
        )

    def addViewNode(
        self,
        *,
        parent: NodeIdLike,
        parentReference: NodeIdLike = ns0.reftypes.HasComponent,
        browseName: o6.QualifiedName | str,
        requestedNodeId: NodeIdLike | None = None,
        attributes: ns0.datatypes.ViewAttributes,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a View node from its attributes and return its NodeId.

        Args:
            parent: Parent node.
            parentReference: ReferenceType from the parent to the new node.
            browseName: BrowseName of the new node.
            requestedNodeId: Requested NodeId. The server assigns one when
                omitted.
            attributes: The `ViewAttributes` of the new node.

        Returns:
            The NodeId of the new node, or an awaitable of it in async code.

        Raises:
            StatusCodeError: The AddNodes service or the node creation failed.
            RuntimeError: The client is not connected.
        """
        return self._add_node(
            parent=parent,
            parent_reference=parentReference,
            nodeclass=ns0.datatypes.NodeClass.VIEW,
            browsename=browseName,
            requested_nodeid=requestedNodeId,
            attributes=attributes,
        )

    def addReferenceTypeNode(
        self,
        *,
        parent: NodeIdLike,
        parentReference: NodeIdLike = ns0.reftypes.HasSubtype,
        browseName: o6.QualifiedName | str,
        requestedNodeId: NodeIdLike | None = None,
        attributes: ns0.datatypes.ReferenceTypeAttributes,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a ReferenceType node from its attributes and return its NodeId.

        Args:
            parent: Parent node.
            parentReference: ReferenceType from the parent to the new node.
            browseName: BrowseName of the new node.
            requestedNodeId: Requested NodeId. The server assigns one when
                omitted.
            attributes: The `ReferenceTypeAttributes` of the new node.

        Returns:
            The NodeId of the new node, or an awaitable of it in async code.

        Raises:
            StatusCodeError: The AddNodes service or the node creation failed.
            RuntimeError: The client is not connected.
        """
        return self._add_node(
            parent=parent,
            parent_reference=parentReference,
            nodeclass=ns0.datatypes.NodeClass.REFERENCE_TYPE,
            browsename=browseName,
            requested_nodeid=requestedNodeId,
            attributes=attributes,
        )

    def addDataTypeNode(
        self,
        *,
        parent: NodeIdLike,
        parentReference: NodeIdLike = ns0.reftypes.HasSubtype,
        browseName: o6.QualifiedName | str,
        requestedNodeId: NodeIdLike | None = None,
        attributes: ns0.datatypes.DataTypeAttributes,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a DataType node from its attributes and return its NodeId.

        Args:
            parent: Parent node.
            parentReference: ReferenceType from the parent to the new node.
            browseName: BrowseName of the new node.
            requestedNodeId: Requested NodeId. The server assigns one when
                omitted.
            attributes: The `DataTypeAttributes` of the new node.

        Returns:
            The NodeId of the new node, or an awaitable of it in async code.

        Raises:
            StatusCodeError: The AddNodes service or the node creation failed.
            RuntimeError: The client is not connected.
        """
        return self._add_node(
            parent=parent,
            parent_reference=parentReference,
            nodeclass=ns0.datatypes.NodeClass.DATA_TYPE,
            browsename=browseName,
            requested_nodeid=requestedNodeId,
            attributes=attributes,
        )

    def addMethodNode(
        self,
        *,
        parent: NodeIdLike,
        parentReference: NodeIdLike = ns0.reftypes.HasComponent,
        browseName: o6.QualifiedName | str,
        requestedNodeId: NodeIdLike | None = None,
        attributes: ns0.datatypes.MethodAttributes,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a Method node from its attributes and return its NodeId.

        Args:
            parent: Parent node.
            parentReference: ReferenceType from the parent to the new node.
            browseName: BrowseName of the new node.
            requestedNodeId: Requested NodeId. The server assigns one when
                omitted.
            attributes: The `MethodAttributes` of the new node.

        Returns:
            The NodeId of the new node, or an awaitable of it in async code.

        Raises:
            StatusCodeError: The AddNodes service or the node creation failed.
            RuntimeError: The client is not connected.
        """
        return self._add_node(
            parent=parent,
            parent_reference=parentReference,
            nodeclass=ns0.datatypes.NodeClass.METHOD,
            browsename=browseName,
            requested_nodeid=requestedNodeId,
            attributes=attributes,
        )

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
        """Delete one or more nodes with the permissions of the Session.

        Args:
            nodeId: A node or NodeId, or a list of them.
            deleteTargetReferences: Remove references from remaining nodes
                to the deleted nodes. `False` leaves dangling references.

        Returns:
            One StatusCode for a single target, otherwise a list in input
            order, also for a one-element list. Every target is attempted,
            even after a failure. An empty list returns `[]` without a
            request. Async callers must await the result.

        Raises:
            StatusCodeError: The service failed.
            TypeError: An argument has an invalid Python type.
            ValueError: A target cannot be converted to a NodeId.
            RuntimeError: The client is not connected.
        """
        is_scalar, ids = _delete_inputs(nodeId, deleteTargetReferences)

        async def _delete_node() -> o6.StatusCode | list[o6.StatusCode]:
            if not ids:
                return []
            if not self.connected:
                raise RuntimeError("Client is not connected")

            items = []
            for nid in ids:
                item = ns0.datatypes.DeleteNodesItem()
                item.nodeId = nid
                item.deleteTargetReferences = deleteTargetReferences
                items.append(item)

            request = ns0.datatypes.DeleteNodesRequest()
            request.nodesToDelete = items
            response = await self.serviceDeleteNodes(request)

            if response.responseHeader.serviceResult != 0:
                raise o6.StatusCodeError(response.responseHeader.serviceResult)
            if len(response.results) != len(items):
                raise RuntimeError("DeleteNodes result count does not match the request")

            results = list(response.results)
            return results[0] if is_scalar else results

        return self._run_on_loop(_delete_node)

    def addReference(
        self,
        source: NodeIdLike,
        reftype: NodeIdLike,
        target: NodeIdLike | o6.ExpandedNodeId,
        forward: bool = True,
        targetNodeClass: ns0.datatypes.NodeClass = ns0.datatypes.NodeClass.UNSPECIFIED,
        targetServerUri: str = "",
    ) -> MaybeAwaitable[o6.StatusCode]:
        """Add a reference between two nodes.

        Args:
            source: Source NodeId.
            reftype: ReferenceType NodeId.
            target: Target NodeId or ExpandedNodeId.
            forward: Whether to create a forward reference.
            targetNodeClass: NodeClass of the target.
            targetServerUri: URI of the server that holds an external target.

        Returns:
            The StatusCode, or an awaitable of it. A rejected reference,
            including a duplicate, returns a bad status.

        Raises:
            StatusCodeError: The service failed.
            TypeError: An argument has an invalid Python type.
            ValueError: An argument cannot be converted to a NodeId or enum.
            RuntimeError: The client is not connected.
        """

        async def _add_reference() -> o6.StatusCode:
            if not self.connected:
                raise RuntimeError("Client is not connected")

            item = ns0.datatypes.AddReferencesItem()
            item.sourceNodeId = o6.NodeId(source)
            item.referenceTypeId = o6.NodeId(reftype)
            item.isForward = forward
            item.targetServerUri = targetServerUri
            item.targetNodeId = (
                target
                if isinstance(target, o6.ExpandedNodeId)
                else o6.ExpandedNodeId(o6.NodeId(target))
            )
            item.targetNodeClass = targetNodeClass

            request = ns0.datatypes.AddReferencesRequest()
            request.referencesToAdd = [item]

            response = await self.serviceAddReferences(request)

            if response.responseHeader.serviceResult != 0:
                raise o6.StatusCodeError(response.responseHeader.serviceResult)
            if len(response.results) != 1:
                raise RuntimeError("Unexpected number of results from AddReferences")

            return response.results[0]

        return self._run_on_loop(_add_reference)

    def deleteReference(
        self,
        source: NodeIdLike,
        reftype: NodeIdLike,
        target: NodeIdLike | o6.ExpandedNodeId,
        forward: bool = True,
        deleteBidirectional: bool = True,
    ) -> MaybeAwaitable[o6.StatusCode]:
        """Delete a reference between two nodes.

        Args:
            source: Source NodeId.
            reftype: ReferenceType NodeId.
            target: Target NodeId or ExpandedNodeId.
            forward: Whether to delete the forward reference.
            deleteBidirectional: Whether to also delete the inverse reference.

        Returns:
            The StatusCode, or an awaitable of it. A rejected deletion returns
            a non-Good status, `UNCERTAIN_REFERENCE_NOT_DELETED` for a missing
            reference.

        Raises:
            StatusCodeError: The service failed.
            TypeError: An argument has an invalid Python type.
            ValueError: An argument cannot be converted to a NodeId.
            RuntimeError: The client is not connected.
        """

        async def _delete_reference() -> o6.StatusCode:
            if not self.connected:
                raise RuntimeError("Client is not connected")

            item = ns0.datatypes.DeleteReferencesItem()
            item.sourceNodeId = o6.NodeId(source)
            item.referenceTypeId = o6.NodeId(reftype)
            item.isForward = forward
            item.targetNodeId = (
                target
                if isinstance(target, o6.ExpandedNodeId)
                else o6.ExpandedNodeId(o6.NodeId(target))
            )
            item.deleteBidirectional = deleteBidirectional

            request = ns0.datatypes.DeleteReferencesRequest()
            request.referencesToDelete = [item]

            response = await self.serviceDeleteReferences(request)

            if response.responseHeader.serviceResult != 0:
                raise o6.StatusCodeError(response.responseHeader.serviceResult)
            if len(response.results) != 1:
                raise RuntimeError("Unexpected number of results from DeleteReferences")

            return response.results[0]

        return self._run_on_loop(_delete_reference)

    def createSubscription(
        self,
        publishingInterval: float = 100.0,
        lifetimeCount: int = 36000,
        maxKeepaliveCount: int = 10,
        maxNotificationsPerPublish: int = 10,
        publishingEnabled: bool = True,
        *,
        onCreated: (
            Callable[
                ["o6.subscription.Subscription", ns0.datatypes.CreateSubscriptionResponse],
                MaybeAwaitable[None],
            ]
            | None
        ) = None,
        onStatusChange: (
            Callable[
                ["o6.subscription.Subscription", ns0.datatypes.StatusChangeNotification],
                MaybeAwaitable[None],
            ]
            | None
        ) = None,
        onDeleted: Callable[["o6.subscription.Subscription"], MaybeAwaitable[None]] | None = None,
    ) -> MaybeAwaitable[o6.subscription.Subscription]:
        """Create a subscription for monitoring data changes or events.

        Args:
            publishingInterval: Requested publishing interval in milliseconds.
            lifetimeCount: Requested lifetime count.
            maxKeepaliveCount: Requested maximum keep-alive count.
            maxNotificationsPerPublish: Maximum notifications per publish.
            publishingEnabled: Whether publishing starts enabled.
            onCreated: Called with `(subscription, response)` once the server
                has created the subscription.
            onStatusChange: Called with `(subscription, notification)` for each
                `StatusChangeNotification` of the subscription.
            onDeleted: Called with `(subscription,)` when the subscription is
                deleted, by `delete()` or when the Session closes.

        Returns:
            The new `o6.subscription.Subscription`.

        Raises:
            RuntimeError: The client is not connected.
        """

        async def _create_subscription() -> o6.subscription.Subscription:
            if not self.connected:
                raise RuntimeError("Client is not connected")

            subscription = await o6.subscription.Subscription(
                self,
                publishingInterval,
                lifetimeCount,
                maxKeepaliveCount,
                maxNotificationsPerPublish,
                publishingEnabled,
                onCreated=onCreated,
                onStatusChange=onStatusChange,
                onDeleted=onDeleted,
            )
            assert subscription.id is not None
            self._subscriptions[subscription.id] = subscription
            return subscription

        return self._run_on_loop(_create_subscription)

    def monitor(
        self,
        target: (
            NodeIdLike | ns0.datatypes.ReadValueId | list[NodeIdLike | ns0.datatypes.ReadValueId]
        ),
        callback: o6.subscription.MonitoredItem.DataChangeCallback | None = None,
        samplingInterval: float = 100.0,
        *,
        valueOnly: bool = True,
        subscription: o6.subscription.Subscription | None = None,
        filter: ns0.datatypes.DataChangeFilter | None = None,
        monitoringMode: ns0.datatypes.MonitoringMode = ns0.datatypes.MonitoringMode.REPORTING,
        queueSize: int = 1,
        discardOldest: bool = True,
        onCreated: o6.subscription.MonitoredItem.CreatedCallback | None = None,
        onDeleted: o6.subscription.MonitoredItem.DeletedCallback | None = None,
    ) -> MaybeAwaitable[o6.subscription.MonitoredItem | list[o6.subscription.MonitoredItem]]:
        """Monitor data changes on one or more nodes.

        Args:
            target: A NodeId or [ReadValueId][o6.ns.ns0.datatypes.ReadValueId],
                or a list of them.
            callback: Called for each data change. `None` prints
                `MonitoredItem {id}: {value}` to stdout.
            samplingInterval: Requested sampling interval in milliseconds.
            valueOnly: `True` passes the value to the callback. `False` passes
                the [DataValue][o6.DataValue].
            subscription: Subscription for the items. `None` uses
                `defaultSubscription`.
            filter: [DataChangeFilter][o6.ns.ns0.datatypes.DataChangeFilter]
                that controls when a change is reported.
            monitoringMode: Monitoring mode of the items.
            queueSize: Requested queue size.
            discardOldest: Discard the oldest entry when the queue is full.
            onCreated: Called with `(item, createResult)` once the server
                created the item. See `MonitoredItem.CreatedCallback`.
            onDeleted: Called when the item is deleted. See
                `MonitoredItem.DeletedCallback`.

        Returns:
            One MonitoredItem, or a list in input order for a list target.

        Raises:
            ValueError: `subscription` belongs to another client.
            RuntimeError: The client is not connected, or there is no default
                subscription.
        """

        async def _monitor() -> o6.subscription.MonitoredItem | list[o6.subscription.MonitoredItem]:
            sub = subscription if subscription is not None else self.defaultSubscription
            if sub._client is not self:
                raise ValueError("The subscription must belong to this client")
            sub._check_valid("monitor")

            if isinstance(target, list):
                return [
                    await sub._monitor(
                        nodeid,
                        callback,
                        samplingInterval,
                        on_created=onCreated,
                        value_only=valueOnly,
                        on_deleted=onDeleted,
                        filter=filter,
                        monitoring_mode=monitoringMode,
                        queue_size=queueSize,
                        discard_oldest=discardOldest,
                    )
                    for nodeid in target
                ]
            else:
                return await sub._monitor(
                    target,
                    callback,
                    samplingInterval,
                    on_created=onCreated,
                    value_only=valueOnly,
                    on_deleted=onDeleted,
                    filter=filter,
                    monitoring_mode=monitoringMode,
                    queue_size=queueSize,
                    discard_oldest=discardOldest,
                )

        return self._run_on_loop(_monitor)

    def monitorEvent(
        self,
        nodeId: NodeIdLike,
        callback: o6.subscription.MonitoredItem.EventCallback,
        filter: ns0.datatypes.EventFilter | str | None = None,
        *,
        subscription: o6.subscription.Subscription | None = None,
        monitoringMode: ns0.datatypes.MonitoringMode = ns0.datatypes.MonitoringMode.REPORTING,
        queueSize: int = 100,
        discardOldest: bool = True,
        onCreated: o6.subscription.MonitoredItem.CreatedCallback | None = None,
        onDeleted: o6.subscription.MonitoredItem.DeletedCallback | None = None,
    ) -> MaybeAwaitable[o6.subscription.MonitoredItem]:
        """Monitor events on a node.

        The callback receives a `dict[str, Any]` keyed by the selected
        event-filter paths, such as `"/Message"` or `"/ConditionName/Id"`.
        It may take the MonitoredItem as its first argument.

        Args:
            nodeId: The node to monitor, usually one with an EventNotifier.
            callback: Called for each matching event.
            filter: An EventFilter or a filter expression string. `None`
                selects `EventId`, `EventType`, `SourceName`, `Time`,
                `Message` and `Severity`.
            subscription: Subscription for the item. `None` uses
                `defaultSubscription`.
            monitoringMode: Monitoring mode of the item.
            queueSize: Requested queue size.
            discardOldest: Discard the oldest entry when the queue is full.
            onCreated: Called with `(item, createResult)` once the server
                created the item. See `MonitoredItem.CreatedCallback`.
            onDeleted: Called when the item is deleted. See
                `MonitoredItem.DeletedCallback`.

        Returns:
            The new MonitoredItem.

        Raises:
            ValueError: `subscription` belongs to another client.
            RuntimeError: The client is not connected, or there is no default
                subscription.
        """

        async def _monitor_event() -> o6.subscription.MonitoredItem:
            sub = subscription if subscription is not None else self.defaultSubscription
            if sub._client is not self:
                raise ValueError("The subscription must belong to this client")
            sub._check_valid("monitor")
            return await sub._monitor_event(
                nodeId,
                callback,
                filter=filter,
                on_created=onCreated,
                on_deleted=onDeleted,
                monitoring_mode=monitoringMode,
                queue_size=queueSize,
                discard_oldest=discardOldest,
            )

        return self._run_on_loop(_monitor_event)

    # Properties

    @property
    def subscriptions(self) -> dict[int, o6.subscription.Subscription]:
        """A copy of the active subscriptions of this client, keyed by ID."""
        return self._subscriptions.copy()

    @property
    def defaultSubscription(self) -> "o6.subscription.Subscription":
        """The default subscription of this client.

        After `connect(createDefaultSubscription=False)` there is none; create
        a subscription and pass it to `monitor()` or `monitorEvent()`.

        Raises:
            RuntimeError: The client is disconnected or has no default
                subscription.
        """
        if not self.connected:
            raise RuntimeError("Client is not connected")
        if (
            self._default_subscription_id is None
            or self._default_subscription_id not in self._subscriptions
        ):
            raise RuntimeError(
                "No default subscription; create one with createSubscription() "
                "and pass subscription= to monitor() or monitorEvent()"
            )
        return self._subscriptions[self._default_subscription_id]


del _NativeClient


__all__ = ["Client"]


def __dir__() -> list[str]:
    return sorted(__all__)
