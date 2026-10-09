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
from typing import TYPE_CHECKING, Any, Callable, Awaitable, Mapping, TypeAlias, TypeVar, overload
from types import TracebackType
from functools import partial

import builtins
from contextlib import suppress
import asyncio
import datetime
import hashlib
import logging
import operator
import inspect
import re

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
from o6._creation import variable_attributes
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
from o6 import MaybeAwaitable, NodeIdLike
from o6.util import _WorkerLoop
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


def _remote_namespace_shortname(uri: str, scope: str) -> str:
    """Return a stable, client-scoped shortname for a remote namespace URI."""
    path = re.sub(r"^\w+://|^\w+:", "", uri)
    segments = re.findall(r"[^/:]+", path)
    name = next((segment for segment in reversed(segments) if segment), "namespace")
    name = re.sub(r"[.\-\s]+", "_", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    name = re.sub(r"[^a-zA-Z0-9_]", "_", name).lower().strip("_") or "namespace"
    if name[0].isdigit():
        name = f"ns_{name}"

    base = f"{scope}_{name}"
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


_client_name_counter = 0


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

    Every request-issuing method returns a plain value when the client drives its
    own event loop, and an awaitable when it runs on an external one; see
    [`MaybeAwaitable`][o6.MaybeAwaitable]. Operations on a client that is not
    connected raise instead of silently doing nothing.

    See the [Client guide](manual/client/index.md) for the whole picture, and the
    [tutorials](tutorials/index.md) for task-by-task walkthroughs.
    """

    config: o6.ClientConfig
    """This client's [`ClientConfig`][o6.ClientConfig]."""

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
        securityMode: int | None = None,
        securityPolicy: str | None = None,
        applicationUri: str | None = None,
        username: str | None = None,
        password: str | None = None,
        allowNonePolicyPassword: bool = False,
        name: str = "",
    ) -> None:
        """Create a new OPC UA client.

        The constructor accepts the most commonly needed settings as keyword
        arguments. Everything else — `sessionName`,
        `requestedSessionTimeout`, `sessionLocaleIds`, `endpoint`, and every other
        [`ClientConfig`][o6.ClientConfig] property — is set on `client.config`
        before calling `connect()`:

        ```python
        client = o6.Client("opc.tcp://localhost:4840")
        client.config.sessionName = "my-session"
        client.config.requestedSessionTimeout = 60_000
        client.config.sessionLocaleIds = ["en-US"]
        client.config.endpoint = my_endpoint_description
        client.config.setUsernamePassword("user", "secret")
        client.connect()
        ```

        Args:
            endpointUrl: OPC UA endpoint to connect to, e.g.
                `"opc.tcp://localhost:4840"`.  May also be passed later via
                `client.config.endpointUrl` and/or `connect()`.
            loop: Asyncio event loop to use.  Defaults to the running loop,
                or a newly created one if none is running.
            logger: Python logger used for all client-level log output.
                Equivalent to `client.config.logger`.
            certificate: Client certificate as a file path (`str` /
                `Path`) or raw bytes (DER/PEM).
                Equivalent to `client.config.certificate`.
            privateKey: Private key matching *certificate*, as a file path
                or raw bytes.
                Equivalent to `client.config.privateKey`.
            trustList: Trusted server certificates, each as a file path or
                raw bytes.
                Equivalent to `client.config.trustList`.
            revocationList: Certificate revocation lists (CRL), each as a
                file path or raw bytes.
                Equivalent to `client.config.revocationList`.
            securityMode: OPC UA message security mode
                (`UA_MessageSecurityMode` integer or
                `o6.ns.ns0.datatypes.MessageSecurityMode` enum).
                Equivalent to `client.config.securityMode`.
            securityPolicy: URI or short name of the security policy, e.g.
                `"Basic256Sha256"`.
                Equivalent to `client.config.securityPolicy`.
            applicationUri: Application URI sent in the
                `ApplicationDescription`.
                Equivalent to `client.config.applicationUri`.
            username: Username for `UserNameIdentityToken` authentication.
                Equivalent to calling
                `client.config.setUsernamePassword(username, password)`.
            password: Password for `UserNameIdentityToken` authentication.
                Used together with *username*.
            allowNonePolicyPassword: Permit transmitting a username/password
                token without encryption. Defaults to False, including when
                credentials are supplied. Equivalent to
                `client.config.allowNonePolicyPassword`.
            name: Optional client name.  Must be a valid Python identifier,
                not match `server<digits>` or `::global`/`global`, and must
                be unique within the process.  When omitted, an auto-generated
                `clientN` name is assigned."""
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
        self._subscriptions: dict[int, o6.subscription.Subscription] = {}
        self._default_subscription_id: int | None = None
        self._notification_scopes: dict[str, NotificationHandlers] = {
            scope: NotificationHandlers(partial(self._sync_notification_scope, scope))
            for scope in _NOTIFICATION_SCOPES
        }

        global _client_name_counter
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
            _client_name_counter += 1
            name = f"client{_client_name_counter}"

        self._name = name
        if self._name + "_ns1" in o6.ns:
            raise ValueError(f"Client name {self._name} is not unique")

        super().__init__(logger=logger, loop=loop)
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

        # Initialize the well-known entry-points into the namespace 0
        self._node_backend = _ClientBackend(self)
        self.root = nodes.ObjectNode(self._node_backend, "i=84", o6.QualifiedName(0, "Root"))
        self.objects = nodes.ObjectNode(self._node_backend, "i=85", o6.QualifiedName(0, "Objects"))
        self.types = nodes.ObjectNode(self._node_backend, "i=86", o6.QualifiedName(0, "Types"))
        self.views = nodes.ObjectNode(self._node_backend, "i=87", o6.QualifiedName(0, "Views"))

        # Start the worker thread
        if self._worker is not None:
            self._worker.start()

    def __del__(self) -> None:
        # Release the native client while this complete Python object and its
        # worker loop still exist. Native cleanup closes any live channel;
        # calling the public disconnect API here could create an unawaited
        # coroutine for async-mode clients. The C deallocator is the fallback.
        try:
            self._cleanup()
        except Exception:
            pass
        try:
            if self._worker is not None:
                self._worker.stop(close=True)
        except Exception:
            pass

    T = TypeVar("T")

    def _maybe_async(self, aw: Awaitable[T]) -> MaybeAwaitable[T]:
        if self._worker is not None and not self._worker.running:
            if asyncio.iscoroutine(aw):
                aw.close()
            raise RuntimeError("Client event loop is not running")

        try:
            loop = asyncio.get_running_loop()
            if loop == self._loop:
                return aw
        except RuntimeError:
            loop = None

        async def _await(f):
            return await f

        # Sync caller on an external loop that nobody is driving.  Scheduling
        # threadsafe would queue the coroutine on an idle loop and block the
        # caller forever, so drive it to completion inline instead (same as
        # Server._maybe_async).  Only for external loops — an owned loop is
        # driven by our worker thread, which may not have reached run_forever
        # yet.
        if (
            loop is None
            and self._worker is None
            and not self._loop.is_running()
            and not self._loop.is_closed()
        ):
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
            raise RuntimeError("Client event loop is not running")

        if loop is None or asyncio.current_task() is None:
            return fut.result()
        else:
            return asyncio.wrap_future(fut)

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        """The asyncio event loop used by this client. Set at construction time, not modifiable afterwards."""
        return self._loop

    @property
    def state(self) -> tuple[o6.SecureChannelState, o6.SessionState, o6.StatusCode]:
        """Return (channel_state, session_state, connect_status)."""
        channel_state, session_state, status_code = self._get_state()
        return (
            o6.SecureChannelState(channel_state),
            o6.SessionState(session_state),
            status_code,
        )

    @property
    def connected(self) -> bool:
        """Test if a client has both SecureChannel and Session connected."""
        _, session_state, _ = self.state
        return session_state == o6.SessionState.ACTIVATED

    @property
    def onGlobalNotification(self) -> NotificationHandlers:
        """Registry of handlers for every notification this client's underlying
        connection produces (lifecycle, service calls, ...).

        Use as a decorator, a callable, or a list, exactly like the
        `Server.on<category>Notification` registries.

        See [Notification handler](manual/client/notification-handler.md).
        """
        return self._notification_scopes["global"]

    @onGlobalNotification.setter
    def onGlobalNotification(self, value: Any) -> None:
        self.onGlobalNotification.replace(value)

    @property
    def onLifecycleNotification(self) -> NotificationHandlers:
        """Registry of handlers for this client's own lifecycle notifications
        (connection started/stopped), independent of `onGlobalNotification`.

        See [Notification handler](manual/client/notification-handler.md).
        """
        return self._notification_scopes["lifecycle"]

    @onLifecycleNotification.setter
    def onLifecycleNotification(self, value: Any) -> None:
        self.onLifecycleNotification.replace(value)

    @property
    def onServiceNotification(self) -> NotificationHandlers:
        """Registry of handlers for this client's own service-call begin/end
        notifications, independent of `onGlobalNotification`.

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
        setter(partial(self._dispatch_notification, scope) if registry else None)

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

        return self._maybe_async(_create())

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

        Establishes a SecureChannel and, by default, a Session. Finalizes
        encryption settings (certificate / key) before connecting.

        If `noSession` is `True`, only the SecureChannel is opened
        (useful for discovery or when a session will be activated manually
        later).

        Creates the default subscription unless `createDefaultSubscription=False`.
        Opt out for sessions that only read, write, call, or browse, or supply
        an explicit subscription to monitoring methods. If post-session setup
        fails, including default-subscription creation, the session is closed
        before the error is raised.

        Starts the background worker thread.

        ```python
        # sync
        client.connect()

        # async
        await client.connect()
        ```

        Args:
            noSession: Open only the SecureChannel, skip Session creation.
            createDefaultSubscription: Create the convenience subscription after
                connecting (default: `True`). Ignored when `noSession=True`."""
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
                        pass  # best-effort; surface the original failure
                    raise

        if self._worker is not None and not self._worker.running:
            self._worker.start()

        return self._maybe_async(_connect())

    def disconnect(
        self,
        closeSession: bool = True,
        deleteSubscriptions: bool = True,
    ) -> MaybeAwaitable[None]:
        """Disconnect from the server.

        By default closes all subscriptions, ends the Session, and closes the
        SecureChannel, then stops the background worker thread.

        Pass `closeSession=False` to close only the SecureChannel while
        keeping the Session alive (e.g. for session transfer). In that case
        `deleteSubscriptions` is ignored.

        Safe to call when already disconnected or when the event loop is
        closed — returns `None` without raising.

        ```python
        # sync
        client.disconnect()

        # async
        await client.disconnect()
        ```

        Args:
            closeSession: Close the Session (and SecureChannel). When
                `False`, only the SecureChannel is closed.
            deleteSubscriptions: Delete all active subscriptions before
                disconnecting. Ignored when `closeSession` is `False`."""
        sup = super()

        if closeSession:
            if self._loop.is_closed():
                return None

            if self._worker is not None and not self._worker.running:
                return None

            async def _disconnect() -> None:
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
                    pass  # ignore errors from the underlying C disconnect
                # Drain: let asyncio process pending transport close events
                # (connection_lost, etc.) before stopping the event loop.
                for _ in range(10):
                    await asyncio.sleep(0)

            result = self._maybe_async(_disconnect())

            # In synchronous context _maybe_async blocks until _disconnect
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

            return self._maybe_async(_disconnect())

    def startReverseConnect(
        self,
        port: int,
        hostnames: list[str] | None = None,
    ) -> MaybeAwaitable[None]:
        """Listen for an incoming OPC UA reverse connection from the server.

        In the reverse-connect scenario the *server* initiates the TCP
        connection to the client.  The client opens a listen socket on
        `port` and waits for the server to connect.

        Close the connection with the standard [disconnect][o6.client.Client.disconnect].

        ```python
        client.startReverseConnect(port=4840, hostnames=["0.0.0.0"])
        # ... use client ...
        client.disconnect()
        ```

        Args:
            port: TCP port to listen on.
            hostnames: Network interfaces to advertise.  `None` or an
                empty list lets the stack decide (typically all interfaces)."""
        sup = super()

        async def _connect() -> None:
            await sup._start_reverse_connect(port, hostnames or [])  # type: ignore[attr-defined]

        if self._worker is not None and not self._worker.running:
            self._worker.start()

        return self._maybe_async(_connect())

    def activateCurrentSession(self) -> Any:
        """Re-activate the session that is already associated with this client.

        Sends an *ActivateSession* request using the client's stored identity
        token and credentials.  Also creates the default subscription.

        Typical use — session transfer, step 2 on the *receiving* client when
        the session was originally opened by *this* client and the
        SecureChannel has been renewed or re-established:

        ```python
        client.connect()                  # establishes session
        # ... channel re-established ...
        client.activateCurrentSession() # re-bind session to new channel
        ```
        """
        sup = super()

        async def _call() -> None:
            await sup._activate_current_session()  # type: ignore[attr-defined]
            await self._create_default_subscription()

        return self._maybe_async(_call())

    def activateSession(
        self,
        authToken: o6.NodeId,
        serverNonce: bytes,
    ) -> Any:
        """Activate a session that was created by *another* client.

        Used for session transfer: client A's session is handed off to
        client B.  Client B must first open a SecureChannel without a session
        (`connect(noSession=True)`), then call this method with the token
        and nonce obtained from the originating session.

        ```python
        # Client B — take over a session using credentials supplied
        # by the originating session
        client_b.connect(noSession=True)
        client_b.activateSession(token, nonce)
        ```

        Args:
            authToken: Authentication token (`NodeId`) from the originating session.
            serverNonce: Server nonce bytes from the originating session."""
        sup = super()

        async def _call() -> None:
            await sup._activate_session(authToken, serverNonce)  # type: ignore[attr-defined]
            await self._create_default_subscription()

        return self._maybe_async(_call())

    def __enter__(self) -> Self:
        """Enter the sync context manager; connect if not already connected.

        Calls [connect][o6.client.Client.connect] when the client is not yet connected, then
        returns `self`.  [__exit__][o6.client.Client.__exit__] calls [disconnect][o6.client.Client.disconnect] if the
        client is still connected when the block ends.

        ```python
        with Client("opc.tcp://localhost:4840") as client:
            value = client.read("ns=1;s=Temperature")
        ```
        """
        if not self.connected:
            self.connect()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Exit the sync context manager; disconnect if still connected.

        Calls [disconnect][o6.client.Client.disconnect] when the client is still connected.
        Exceptions from the `with` block are not suppressed.
        See [__enter__][o6.client.Client.__enter__] for full usage."""
        if self.connected:
            self.disconnect()

    async def __aenter__(self) -> Self:
        """Async counterpart of [__enter__][o6.client.Client.__enter__].

        Same semantics — connects if not already connected and returns
        `self` — but uses `await` internally.  [__aexit__][o6.client.Client.__aexit__] awaits
        [disconnect][o6.client.Client.disconnect].

        ```python
        async with Client("opc.tcp://localhost:4840") as client:
            value = await client.read("ns=1;s=Temperature")
        ```
        """
        if not self.connected:
            await self.connect()  # type: ignore[misc]
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Exit the async context manager; disconnect if still connected.

        Awaits [disconnect][o6.client.Client.disconnect] when the client is still connected.
        Exceptions from the `async with` block are not suppressed.
        See [__aenter__][o6.client.Client.__aenter__] for full usage."""
        if self.connected:
            await self.disconnect()  # type: ignore[misc]

    def __getitem__(self, key: NodeIdLike) -> MaybeAwaitable[nodes.Node]:
        """Resolve a node ID to a typed [Node][o6.Node] object.

        Reads `NodeClass` and `BrowseName` from the server and returns the
        matching [Node][o6.Node] subclass (e.g. `VariableNode`,
        `ObjectNode`, …). Service and attribute failures raise `StatusCodeError`;
        an unknown ID has code `BAD_NODE_ID_UNKNOWN`. Malformed responses
        raise `RuntimeError`.

        *key* accepts anything that can be converted to a `NodeId`:
        a string (`"ns=1;s=Temperature"`), an integer (numeric node id in
        namespace 0), or a [NodeId][o6.NodeId] instance.

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
            return self._maybe_async(_get_node())
        except Exception as exc:
            raise _without_traceback(exc) from None

    #
    # Raw Service API
    #
    # These explicit methods preserve a discoverable, typed public API while
    # _maybe_async provides the shared sync/async dispatch policy.

    # Discovery Service Set

    def serviceFindServers(
        self, request: ns0.datatypes.FindServersRequest
    ) -> MaybeAwaitable[ns0.datatypes.FindServersResponse]:
        """Raw *FindServers* service call — discover servers known to a discovery server.

        [OPC UA Part 4 §5.5.2](https://reference.opcfoundation.org/specs/OPC-10000-4/5.5.2)"""
        return self._maybe_async(self._service_find_servers(request))

    def serviceFindServersOnNetwork(
        self, request: ns0.datatypes.FindServersOnNetworkRequest
    ) -> MaybeAwaitable[ns0.datatypes.FindServersOnNetworkResponse]:
        """Raw *FindServersOnNetwork* service call — enumerate servers registered via mDNS/LDS.

        [OPC UA Part 4 §5.5.3](https://reference.opcfoundation.org/specs/OPC-10000-4/5.5.3)"""
        return self._maybe_async(self._service_find_servers_on_network(request))

    def serviceGetEndpoints(
        self, request: ns0.datatypes.GetEndpointsRequest
    ) -> MaybeAwaitable[ns0.datatypes.GetEndpointsResponse]:
        """Raw *GetEndpoints* service call — retrieve the endpoint descriptions of a server.

        [OPC UA Part 4 §5.5.4](https://reference.opcfoundation.org/specs/OPC-10000-4/5.5.4)"""
        return self._maybe_async(self._service_get_endpoints(request))

    def invalidateNodeCache(self, target: NodeIdLike | None = None) -> MaybeAwaitable[None]:
        """Invalidate cached child navigation for this client's existing handles.

        Args:
            target: Invalidate every handle for this node, or all handles when
                omitted. The next navigation browses again. Async callers must
                await this operation.

        Use this after external address-space changes or raw service browsing.
        Complete `browse()` calls invalidate their target automatically, and
        client node/reference mutations and namespace refresh invalidate all
        handles. Cached misses are browsed again once before raising.
        """
        nodeid = o6.NodeId(target) if target is not None else None

        async def _invalidate() -> None:
            self._node_backend.invalidate_children(nodeid)

        return self._maybe_async(_invalidate())

    async def _mutate_address_space(self, operation: Awaitable[Any]) -> Any:
        try:
            return await operation
        finally:
            # Partial failures can still change the address space.
            self._node_backend.invalidate_children()

    # NodeManagement Service Set

    def serviceAddNodes(
        self, request: ns0.datatypes.AddNodesRequest
    ) -> MaybeAwaitable[ns0.datatypes.AddNodesResponse]:
        """Raw *AddNodes* service call — add one or more nodes to the address space.

        [OPC UA Part 4 §5.8.2](https://reference.opcfoundation.org/specs/OPC-10000-4/5.8.2)"""
        return self._maybe_async(self._mutate_address_space(self._service_addNodes(request)))

    def serviceDeleteNodes(
        self, request: ns0.datatypes.DeleteNodesRequest
    ) -> MaybeAwaitable[ns0.datatypes.DeleteNodesResponse]:
        """Raw *DeleteNodes* service call — remove one or more nodes from the address space.

        [OPC UA Part 4 §5.8.4](https://reference.opcfoundation.org/specs/OPC-10000-4/5.8.4)"""
        return self._maybe_async(self._mutate_address_space(self._service_deleteNodes(request)))

    def serviceAddReferences(
        self, request: ns0.datatypes.AddReferencesRequest
    ) -> MaybeAwaitable[ns0.datatypes.AddReferencesResponse]:
        """Raw *AddReferences* service call — add references between nodes.

        [OPC UA Part 4 §5.8.3](https://reference.opcfoundation.org/specs/OPC-10000-4/5.8.3)"""
        return self._maybe_async(self._mutate_address_space(self._service_addReferences(request)))

    def serviceDeleteReferences(
        self, request: ns0.datatypes.DeleteReferencesRequest
    ) -> MaybeAwaitable[ns0.datatypes.DeleteReferencesResponse]:
        """Raw *DeleteReferences* service call — remove references between nodes.

        [OPC UA Part 4 §5.8.5](https://reference.opcfoundation.org/specs/OPC-10000-4/5.8.5)"""
        return self._maybe_async(
            self._mutate_address_space(self._service_deleteReferences(request))
        )

    # View Service Set

    def serviceBrowse(
        self, request: ns0.datatypes.BrowseRequest
    ) -> MaybeAwaitable[ns0.datatypes.BrowseResponse]:
        """Raw *Browse* service call — navigate the address space from one or more start nodes.

        Returns references according to the `BrowseDescription` filter in the
        request.  Use [serviceBrowseNext][o6.client.Client.serviceBrowseNext] to continue if the response
        indicates more results are available.

        [OPC UA Part 4 §5.9.2](https://reference.opcfoundation.org/specs/OPC-10000-4/5.9.2)"""
        return self._maybe_async(self._service_browse(request))

    def serviceBrowseNext(
        self, request: ns0.datatypes.BrowseNextRequest
    ) -> MaybeAwaitable[ns0.datatypes.BrowseNextResponse]:
        """Raw *BrowseNext* service call — continue a Browse that returned a continuation point.

        [OPC UA Part 4 §5.9.3](https://reference.opcfoundation.org/specs/OPC-10000-4/5.9.3)"""
        return self._maybe_async(self._service_browseNext(request))

    def serviceTranslateBrowsePathsToNodeIds(
        self, request: ns0.datatypes.TranslateBrowsePathsToNodeIdsRequest
    ) -> MaybeAwaitable[ns0.datatypes.TranslateBrowsePathsToNodeIdsResponse]:
        """Raw *TranslateBrowsePathsToNodeIds* service call — resolve browse paths to NodeIds.

        [OPC UA Part 4 §5.9.4](https://reference.opcfoundation.org/specs/OPC-10000-4/5.9.4)"""
        return self._maybe_async(self._service_translateBrowsePathsToNodeIds(request))

    def serviceRegisterNodes(
        self, request: ns0.datatypes.RegisterNodesRequest
    ) -> MaybeAwaitable[ns0.datatypes.RegisterNodesResponse]:
        """Raw *RegisterNodes* service call — obtain optimised NodeIds for repeated access.

        [OPC UA Part 4 §5.9.5](https://reference.opcfoundation.org/specs/OPC-10000-4/5.9.5)"""
        return self._maybe_async(self._service_registerNodes(request))

    def serviceUnregisterNodes(
        self, request: ns0.datatypes.UnregisterNodesRequest
    ) -> MaybeAwaitable[ns0.datatypes.UnregisterNodesResponse]:
        """Raw *UnregisterNodes* service call — release NodeIds obtained via *RegisterNodes*.

        [OPC UA Part 4 §5.9.6](https://reference.opcfoundation.org/specs/OPC-10000-4/5.9.6)"""
        return self._maybe_async(self._service_unregisterNodes(request))

    # Attribute Service Set

    def serviceRead(
        self, request: ns0.datatypes.ReadRequest
    ) -> MaybeAwaitable[ns0.datatypes.ReadResponse]:
        """Raw *Read* service call — read one or more node attributes.

        [OPC UA Part 4 §5.11.2](https://reference.opcfoundation.org/specs/OPC-10000-4/5.11.2)"""
        return self._maybe_async(self._service_read(request))

    def serviceHistoryRead(
        self, request: ns0.datatypes.HistoryReadRequest
    ) -> MaybeAwaitable[ns0.datatypes.HistoryReadResponse]:
        """Raw *HistoryRead* service call — read historical values or events from nodes.

        [OPC UA Part 4 §5.11.3](https://reference.opcfoundation.org/specs/OPC-10000-4/5.11.3)"""
        return self._maybe_async(self._service_historyRead(request))

    def serviceWrite(
        self, request: ns0.datatypes.WriteRequest
    ) -> MaybeAwaitable[ns0.datatypes.WriteResponse]:
        """Raw *Write* service call — write one or more node attribute values.

        [OPC UA Part 4 §5.11.4](https://reference.opcfoundation.org/specs/OPC-10000-4/5.11.4)"""
        operation = self._service_write(request)
        if any(item.attributeId == o6.AttributeId.BROWSE_NAME for item in request.nodesToWrite):
            operation = self._mutate_address_space(operation)
        return self._maybe_async(operation)

    def serviceHistoryUpdate(
        self, request: ns0.datatypes.HistoryUpdateRequest
    ) -> MaybeAwaitable[ns0.datatypes.HistoryUpdateResponse]:
        """Raw *HistoryUpdate* service call — insert, replace, or delete historical data.

        [OPC UA Part 4 §5.11.5](https://reference.opcfoundation.org/specs/OPC-10000-4/5.11.5)"""
        return self._maybe_async(self._service_historyUpdate(request))

    # Method Service Set

    def serviceCall(
        self, request: ns0.datatypes.CallRequest
    ) -> MaybeAwaitable[ns0.datatypes.CallResponse]:
        """Raw *Call* service call — invoke one or more OPC UA methods.

        [OPC UA Part 4 §5.12.2](https://reference.opcfoundation.org/specs/OPC-10000-4/5.12.2)"""
        return self._maybe_async(self._service_call(request))

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

        Browses the server's DataType hierarchy (rooted at `Structure`,
        NodeId `i=22`) and reads the `DataTypeDefinition` and
        `BrowseName` attributes for every discovered node.  Only nodes that
        carry a `StructureDefinition` (structs, structs-with-optional-fields,
        and unions) are included in the result.

        Pass `typeNodes` to restrict the query to a specific set of DataType
        NodeIds instead of walking the full hierarchy.  Passing an empty list
        returns `[]` immediately without contacting the server. Expanded references
        with a namespace URI or remote server index are skipped; only local
        NodeIds can be read through this session.

        Each entry in the returned list is a `dict` with the following keys:

        - `typeName` (`str`) — `BrowseName.name` of the DataType node.
        - `typeId` (`NodeId`) — NodeId of the DataType node.
        - `binaryEncodingId` (`NodeId`) — default binary encoding NodeId
          (`StructureDefinition.defaultEncodingId`).
        - `structureType` ([`StructureType`][o6.ns.ns0.datatypes.StructureType]) —
          the information-model structure category.
        - `membersSize` (`int`) — number of fields in the structure.

        Args:
            typeNodes: Explicit DataType NodeIds to query.  `None` (default)
                walks the full `Structure` subtype hierarchy."""
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

        return self._maybe_async(_call())

    def updateRemoteNamespaces(self) -> MaybeAwaitable[None]:
        """Atomically synchronize namespace mappings and custom datatypes.

        The client first installs a provisional wire-index mapping when a URI
        has several compiled versions, reads the server's NamespaceMetadata,
        then selects an exact version or the latest available fallback. The
        final Python mapping, SecureChannel decoder mapping, and custom
        datatype chain are replaced as one snapshot. A failed refresh leaves
        the preceding snapshot usable. Call this again if a connected server
        adds namespaces at runtime; unchanged snapshots are not rebuilt.
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
            provisional_applied = False
            if ambiguous:
                if previous_uris != uris:
                    self._apply_namespace_snapshot(uris, provisional)
                    provisional_applied = True
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

            final = [
                *entries,
                *(
                    (uris[wire_index], info.index, wire_index)
                    for wire_index, info in sorted(selected.items())
                ),
            ]
            final_snapshot = tuple(final)
            if final_snapshot != getattr(self, "_namespace_snapshot", None) and not (
                provisional_applied and final == provisional
            ):
                self._apply_namespace_snapshot(uris, final)
            self._namespace_snapshot = final_snapshot
            self._namespace_snapshot_uris = uris
            self._namespace_snapshot_selected = {
                wire_index: info.index for wire_index, info in selected.items()
            }

        return self._maybe_async(_update())

    #
    # Simplified Service API
    #

    # Discovery

    def getEndpoints(
        self,
        endpointUrl: str,
        *,
        localeIds: list[str] | None = None,
        profileUris: list[str] | None = None,
    ) -> MaybeAwaitable[list[ns0.datatypes.EndpointDescription]]:
        """Return the endpoints advertised by a server.

        Sends a *GetEndpoints* request to `endpointUrl`.  No active session
        is required — connect with `connect(noSession=True)` first if the
        client is not yet connected.

        Each [EndpointDescription][o6.ns.ns0.datatypes.EndpointDescription] in the result describes one
        available endpoint and includes the endpoint URL, security mode,
        security policy URI, transport profile URI, server certificate, and
        the list of supported [UserTokenPolicy][o6.ns.ns0.datatypes.UserTokenPolicy] entries.

            client.connect(noSession=True)
            endpoints = client.getEndpoints("opc.tcp://localhost:4840")
            for ep in endpoints:
                print(ep.endpointUrl, ep.securityMode, ep.securityPolicyUri)

        Args:
            endpointUrl: URL of the server to query, e.g.
                `"opc.tcp://localhost:4840"`.
            localeIds: Preferred locales for localised strings in the
                response (e.g. `["en-US", "de-DE"]`).  `None` returns
                the server's default locale.
            profileUris: Restrict the result to endpoints that match one of
                these transport profile URIs.  `None` returns all endpoints.

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

        return self._maybe_async(_call())

    def findServers(
        self,
        endpointUrl: str,
        *,
        serverUris: list[str] | None = None,
        localeIds: list[str] | None = None,
    ) -> MaybeAwaitable[list[ns0.datatypes.ApplicationDescription]]:
        """Return servers registered at a discovery server or known to a server.

        Sends a *FindServers* request to `endpointUrl`.  Typically called
        against a Local Discovery Server (LDS) at
        `"opc.tcp://localhost:4840"` to enumerate all servers registered on
        the host, or against any server to retrieve its own
        [ApplicationDescription][o6.ns.ns0.datatypes.ApplicationDescription].

        No active session is required — `connect(noSession=True)` is
        sufficient.

        Each [ApplicationDescription][o6.ns.ns0.datatypes.ApplicationDescription] in the result contains the
        application name, application URI, application type, product URI, and
        a list of discovery URLs that can be passed to
        `getEndpoints`.

        ```python
        client.connect(noSession=True)
        servers = client.findServers("opc.tcp://localhost:4840")
        for srv in servers:
            print(srv.applicationUri, srv.discovery_urls)
        ```

        Args:
            endpointUrl: URL of the discovery server or server to query.
            localeIds: Preferred locales for the
                `ApplicationDescription.application_name` field.  `None`
                uses the server's default locale.
            serverUris: Restrict the result to servers whose
                `applicationUri` matches one of these strings.  `None`
                returns all known servers.

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

        return self._maybe_async(_call())

    def findServersOnNetwork(
        self,
        startingRecordId: int = 0,
        maxRecordsToReturn: int = 0,
        serverCapabilityFilter: list[str] | None = None,
    ) -> MaybeAwaitable[list[ns0.datatypes.ServerOnNetwork]]:
        """Return servers visible on the network via a Local Discovery Server (LDS).

        Sends a *FindServersOnNetwork* request to the connected LDS.  The LDS
        maintains a registry of servers that have announced themselves via
        mDNS or the *RegisterServer2* service.  This call is only meaningful
        when connected to an LDS; a regular OPC UA server will return an
        empty list or an error.

        The result is paginated: use `startingRecordId` and
        `maxRecordsToReturn` to page through large registries.  The
        `record_id` field on each [ServerOnNetwork][o6.ns.ns0.datatypes.ServerOnNetwork] entry can
        be used as the `startingRecordId` for the next page.

        Each [ServerOnNetwork][o6.ns.ns0.datatypes.ServerOnNetwork] entry contains the server name,
        discovery URL, and a list of capability strings (e.g. `"DA"` for
        Data Access, `"HE"` for Historical Events).

        ```python
        # Fetch the first 100 servers that support Data Access
        servers = client.findServersOnNetwork(
            maxRecordsToReturn=100,
            serverCapabilityFilter=["DA"],
        )
        ```

        Args:
            startingRecordId: Record ID to start from for pagination.
                `0` starts from the beginning of the registry.
            maxRecordsToReturn: Maximum number of entries to return.
                `0` lets the server decide (typically returns all entries).
            serverCapabilityFilter: Restrict the result to servers that
                advertise all of the given capability strings.  `None`
                returns servers regardless of capabilities.

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

        return self._maybe_async(_call())

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
                Non-Value attributes require their expected datatype and reject
                status/timestamp metadata with BAD_WRITE_NOT_SUPPORTED.
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

        return self._maybe_async(_write())

    def call(
        self, objectId: NodeIdLike, methodId: NodeIdLike, inputArgs: list[Any] = []
    ) -> MaybeAwaitable[tuple[o6.StatusCode, *tuple[Any, ...]]]:
        """Invoke a method on a node.

        Parameters:
            objectId: The object node id that owns the method.
            methodId: The method node id to invoke.
            inputArgs: Positional input arguments to pass to the method.

        Returns:
            `(statusCode, output1, output2, ...)`, including bad method statuses
            and any available outputs. Invalid method selection and argument
            validation also produce method results. A zero-output result is
            `(statusCode,)`.

        Raises:
            StatusCodeError: The Call service failed; `code` retains the original
                status. Method-result failures do not raise.
            TypeError: An argument cannot be converted to an OPC UA value.
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
            return (result.statusCode, *result.outputArguments)

        return self._maybe_async(_call())

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
        """Browse references from a node.

        The method transparently follows server-issued continuation points by
        calling `BrowseNext` until all references have been collected, so the
        returned list is always complete even when the server splits the
        response into multiple batches.

        Parameters:
            target: The node id to browse from.
            direction: The browse direction (forward, inverse, or both).
            reftype: A reference type to filter by, or `None` for all types.
            refsubtypes: If `True`, include subtypes of the reference type.
            nodeClassMask: A node-class mask to filter the target nodes, as the
                `UInt32` the service takes. Compose the `NodeClass` members you
                want with `|`.
            resultMask: A browse result mask to customize returned fields, as
                the `UInt32` the service takes. Compose the
                `BrowseResultMask` members you want with `|`.

        Returns:
            A list of `ReferenceDescription` objects describing the found
            references. Sync callers receive the list directly; async tasks
            must await the call. Node and NodeId targets have the same contract.

        Raises:
            StatusCodeError: Browse or BrowseNext returned a service or result
                failure. Outstanding continuation points are released on failure
                or cancellation where the connection permits release.
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

        return self._maybe_async(_browse())

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
        """Fetch one page of references, matching `Server.browsePage`.

        Args:
            target: Node to browse from.
            maxReferences: Requested page size; zero means no client-side cap.
            direction: Forward, inverse, or both reference directions.
            reftype: ReferenceType to follow; defaults to HierarchicalReferences.
            refsubtypes: Include subtypes of the reference type.
            nodeClassMask: Restrict target node classes; zero means all classes.
            resultMask: Reference fields to return; zero returns target IDs only.

        Returns:
            One BrowseResult, directly for sync callers or awaitable in async
            code. Continue with `browseNext(False, token)`, or release an unused
            token with `browseNext(True, token)`. Tokens belong to this session.

        Raises:
            StatusCodeError: The service or individual browse failed.
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

        return self._maybe_async(first())

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
            releaseContinuationPoint: Release tokens instead of fetching pages.
            continuationPoint: One token or a list/tuple of session-owned tokens.

        Returns:
            One BrowseResult per token, always as a list. An empty input returns
            an empty list. Await the operation in async code.

        Raises:
            StatusCodeError: The service or any continuation operation failed.
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

        return self._maybe_async(next_pages())

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
        return self._maybe_async(
            _translate_paths(self._service_translateBrowsePathsToNodeIds, browsePath)
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
            origin: Node at which the path starts.
            browsePath: One QualifiedName/string or a list/tuple forming one path.

        Returns:
            One BrowsePathResult, retaining unresolved-path status. Await in
            async code. Unlike `browseRecursive`, this follows a specified path.
        """
        return self.translateBrowsePathsToNodeIds(_simplified_browse_path(origin, browsePath))

    def browseInteractive(self, nodeId: NodeIdLike | None = None) -> Any:
        """Open a curses-based interactive browser for the address space.

        Requires the `curses` module (install `windows-curses` on
        Windows).  Returns the selected NodeId string (or BrowsePath string)
        when the user quits with `n` / `p`; returns `None` otherwise.

        Parameters:
            nodeId: Optional starting node id (defaults to `Objects`)."""
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

        Parameters:
            target: A node id or list of node ids to read history from.
            startTime: The start time for the history interval.
            endTime: The end time for the history interval.
            numValuesPerNode: Maximum number of values to return per node.
            returnBounds: If `True`, include boundary values at the interval edges.
            timestampsToReturn: Which timestamps to return with each value.

        Returns:
            Historical data for the requested nodes. Server-issued continuation
            points are followed until the interval or per-node limit is exhausted."""

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
                    history.dataValues = (
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

        return self._maybe_async(_history_read())

    def historyUpdateInsert(
        self,
        target: NodeIdLike,
        values: list[o6.DataValue],
    ) -> Any:
        """Insert new historical values into a node's history.

        Insertion fails for any timestamp that already has a value stored.
        Use `historyUpdateReplace` to overwrite existing entries.

        Parameters:
            target: The node id whose history is being updated.
            values: The historical values to insert.

        Returns:
            The raw result of the history update operation."""
        return self._history_update(target, values, ns0.datatypes.PerformUpdateType.INSERT)

    def historyUpdateReplace(
        self,
        target: NodeIdLike,
        values: list[o6.DataValue],
    ) -> Any:
        """Replace existing historical values for a node.

        Replacement requires that a value already exists at each provided
        timestamp. Use `historyUpdateInsert` to add new entries.

        Parameters:
            target: The node id whose history is being updated.
            values: The historical values to replace existing entries with.

        Returns:
            The raw result of the history update operation."""
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

        return self._maybe_async(_history_update())

    def historyUpdateDelete(
        self,
        target: NodeIdLike,
        startTime: datetime.datetime,
        endTime: datetime.datetime,
    ) -> Any:
        """Delete historical values from a node.

        Parameters:
            target: The node id whose history should be deleted.
            startTime: The start of the deletion interval.
            endTime: The end of the deletion interval.

        Returns:
            The raw result of the history delete operation."""

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

        return self._maybe_async(_history_delete())

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

        return self._maybe_async(_add())

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
        """Create an Object and return a usable handle, matching `Server.addObject`.

        Args:
            name: BrowseName and DisplayName of the Object.
            parent: Parent node.
            nodeId: Requested NodeId; the server assigns one when omitted.
            typeDefinition: ObjectType, defaulting to BaseObjectType.
            ns: Namespace index for the BrowseName.
            parentReference: Parent reference, defaulting to Organizes.

        Returns:
            An ObjectNode, directly in sync code or awaitable in async code.
            `addObjectNode` remains the attribute-based API returning a NodeId.

        Raises:
            StatusCodeError: Remote node creation failed.
        """
        name_id = o6.QualifiedName(f"{ns}:{name}")
        attributes = ns0.datatypes.ObjectAttributes(displayName=o6.LocalizedText(name))
        return self._maybe_async(
            self._create_convenience_node(
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
        ns: int = 1,
        parentReference: NodeIdLike = ns0.reftypes.Organizes,
    ) -> MaybeAwaitable[nodes.VariableNode]:
        """Create a Variable with friendly inputs, matching `Server.addVariable`.

        Args:
            name: BrowseName and DisplayName of the Variable.
            parent: Parent node.
            value: Initial value; its datatype and array rank are inferred.
                Typed empty NumPy arrays preserve their datatype and rank;
                empty Python sequences require an explicit dataType.
            nodeId: Requested NodeId; assigned by the server when omitted.
            dataType: Explicit OPC UA datatype, otherwise inferred from value.
            typeDefinition: VariableType, defaulting to BaseDataVariableType.
            writable: Allow client writes; defaults to True.
            ns: Namespace index for the BrowseName.
            parentReference: Parent reference, defaulting to Organizes.

        Returns:
            A VariableNode, directly in sync code or awaitable in async code.
            `addVariableNode` retains attribute-based creation and NodeId results.
            History registration and Python behavior installation are server-only.

        Raises:
            StatusCodeError: Remote node creation failed.
            TypeError: The initial value has no inferable datatype.
        """
        attributes, _, _ = variable_attributes(name, value, dataType, writable)
        name_id = o6.QualifiedName(f"{ns}:{name}")
        return self._maybe_async(
            self._create_convenience_node(
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
        """Add a variable node to the server.

        Parameters:
            parent: The parent node id for the variable.
            browseName: The BrowseName for the variable.
            attributes: The variable attributes.
            requestedNodeId: Optionally request a specific node id.
            parentReference: The reference type used to link the variable.
            typeDefinition: The variable type definition node id.

        Returns:
            The newly created variable node id."""
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
        """Add a variable type node to the server.

        Parameters:
            parent: The parent node id for the type node.
            browseName: The BrowseName for the variable type.
            attributes: The variable type attributes.
            requestedNodeId: Optionally request a specific node id.
            parentReference: The reference type used to link the type node.

        Returns:
            The newly created variable type node id."""
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
        """Add an object node to the server.

        Parameters:
            parent: The parent node id for the object.
            browseName: The BrowseName for the object.
            attributes: The object attributes.
            requestedNodeId: Optionally request a specific node id.
            parentReference: The reference type used to link the object.
            typeDefinition: The object type definition node id.

        Returns:
            The newly created object node id."""
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
        """Add an object type node to the server.

        Parameters:
            parent: The parent node id for the type.
            browseName: The BrowseName for the object type.
            attributes: The object type attributes.
            requestedNodeId: Optionally request a specific node id.
            parentReference: The reference type used to link the type node.

        Returns:
            The newly created object type node id."""
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
        """Add a view node to the server.

        Parameters:
            parent: The parent node id for the view.
            browseName: The BrowseName for the view.
            attributes: The view attributes.
            requestedNodeId: Optionally request a specific node id.
            parentReference: The reference type used to link the view.

        Returns:
            The newly created view node id."""
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
        """Add a reference type node to the server.

        Parameters:
            parent: The parent node id for the reference type.
            browseName: The BrowseName for the reference type.
            attributes: The reference type attributes.
            requestedNodeId: Optionally request a specific node id.
            parentReference: The reference type used to link the node.

        Returns:
            The newly created reference type node id."""
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
        """Add a data type node to the server.

        Parameters:
            parent: The parent node id for the data type.
            browseName: The BrowseName for the data type.
            attributes: The data type attributes.
            requestedNodeId: Optionally request a specific node id.
            parentReference: The reference type used to link the node.

        Returns:
            The newly created data type node id."""
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
        """Add a method node to the server.

        Parameters:
            parent: The parent node id for the method.
            browseName: The BrowseName for the method.
            attributes: The method attributes.
            requestedNodeId: Optionally request a specific node id.
            parentReference: The reference type used to link the method.

        Returns:
            The newly created method node id."""
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
        """Delete one or more nodes using the remote session permissions.

        Parameters:
            nodeId: A node, node id, or list of these targets.
            deleteTargetReferences: If True (default), remove incoming
                references from remaining nodes. False leaves dangling references.

        Returns:
            One StatusCode for a scalar target, otherwise a list in input order,
            including one-element batches. All targets are attempted despite
            per-target failures. An empty list returns [] without a request.
            Async callers must await the result.

        Raises:
            StatusCodeError: The service failed.
            TypeError: An argument has an invalid Python type.
            ValueError: A target cannot be converted to a node id.
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

        return self._maybe_async(_delete_node())

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

        Parameters:
            source: The source node id for the reference.
            reftype: The reference type id.
            target: The target node id.
            forward: If `True`, create a forward reference.
            targetNodeClass: Optional target node class for the reference.
            targetServerUri: Optional server uri when referencing an external node.

        Returns:
            The individual StatusCode, or an awaitable resolving to it.
            Rejected mutations, including duplicate local edges, return bad statuses.

        Raises:
            StatusCodeError: The service failed.
            TypeError: An argument has an invalid Python type.
            ValueError: An argument cannot be converted to a node id or enum.
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

        return self._maybe_async(_add_reference())

    def deleteReference(
        self,
        source: NodeIdLike,
        reftype: NodeIdLike,
        target: NodeIdLike | o6.ExpandedNodeId,
        forward: bool = True,
        deleteBidirectional: bool = True,
    ) -> MaybeAwaitable[o6.StatusCode]:
        """Delete a reference between two nodes.

        Parameters:
            source: The source node id for the reference.
            reftype: The reference type id.
            target: The target node id.
            forward: If `True`, delete the forward reference.
            deleteBidirectional: If `True`, also delete the reverse reference.

        Returns:
            The individual StatusCode, or an awaitable resolving to it.
            Rejected deletions return non-Good statuses, including
            UNCERTAIN_REFERENCE_NOT_DELETED for an absent edge.

        Raises:
            StatusCodeError: The service failed.
            TypeError: An argument has an invalid Python type.
            ValueError: An argument cannot be converted to a node id.
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

        return self._maybe_async(_delete_reference())

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
        """Create a subscription to monitor data or events.

        Parameters:
            publishingInterval: The desired publishing interval in milliseconds.
            lifetimeCount: The subscription lifetime count.
            maxKeepaliveCount: The maximum keepalive count.
            maxNotificationsPerPublish: The maximum number of notifications per publish.
            publishingEnabled: Whether the subscription is initially enabled.
            onCreated: Optional callback invoked with `(subscription, response)`
                once the server has acknowledged subscription creation.
            onStatusChange: Optional callback invoked with
                `(subscription, notification)` when the server publishes a
                `StatusChangeNotification` for this subscription.
            onDeleted: Optional callback invoked with `(subscription,)` when
                the subscription is destroyed — explicitly via `delete()`, or
                implicitly on session close / disconnect.

        Returns:
            A `o6.subscription.Subscription` object representing the created subscription."""

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

        return self._maybe_async(_create_subscription())

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

        Parameters:
            target: A node id, [ReadValueId][o6.ns.ns0.datatypes.ReadValueId], or list thereof to monitor.
            callback: Optional callback invoked for each data change. If `None`,
                a default callback that prints `o6.subscription.MonitoredItem {id}: {value}` to
                stdout is used.
            samplingInterval: The requested sampling interval in milliseconds.
            valueOnly: If `True` (default), the callback receives the unwrapped
                value. If `False`, it receives the full [DataValue][o6.DataValue].
            subscription: Optional subscription to attach the monitored items to.
                If `None` (default), the clients' default subscription is used.
                A subscription owned by another client raises `ValueError`.
            filter: Optional [DataChangeFilter][o6.ns.ns0.datatypes.DataChangeFilter] to control triggering.
            monitoringMode: Monitoring mode for the item (default: `REPORTING`).
            queueSize: Requested queue size (default: `1`).
            discardOldest: Whether to discard the oldest entry when the queue is
                full (default: `True`).
            onCreated: Optional lifecycle callback; see `o6.subscription.MonitoredItem._data_change`.
            onDeleted: Optional lifecycle callback; see `o6.subscription.MonitoredItem._data_change`.

        Returns:
            A monitored item or list of monitored items created for the target nodes."""

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

        return self._maybe_async(_monitor())

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

        Callbacks receive a `dict[str, Any]` keyed by selected event-filter paths,
        such as `"/Message"` or `"/ConditionName/Id"`, optionally preceded by the
        monitored item handle.

        Parameters:
            nodeId: The node id to monitor for events.
            callback: Callback invoked for each matching event.
            filter: Optional event filter or filter expression string. If `None`,
                a default filter selecting `EventId`, `EventType`,
                `SourceName`, `Time`, `Message`, and `Severity` is used.
            subscription: Optional subscription to attach the monitored item to.
                Defaults to `defaultSubscription`; a subscription owned by another
                client raises `ValueError`.
            monitoringMode: Monitoring mode for the item (default: `REPORTING`).
            queueSize: Requested queue size (default: `100`).
            discardOldest: Whether to discard the oldest entry when the queue is
                full (default: `True`).
            onCreated: Optional lifecycle callback; see `o6.subscription.MonitoredItem._event`.
            onDeleted: Optional lifecycle callback; see `o6.subscription.MonitoredItem._event`.

        Returns:
            The created monitored event item."""

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

        return self._maybe_async(_monitor_event())

    # Properties

    @property
    def subscriptions(self) -> dict[int, o6.subscription.Subscription]:
        """A copy of the active subscriptions for this client, keyed by id."""
        return self._subscriptions.copy()

    @property
    def defaultSubscription(self) -> "o6.subscription.Subscription":
        """The clients' default subscription.

        Raises `RuntimeError` when disconnected or when no default exists.
        With `connect(createDefaultSubscription=False)`, create a subscription
        explicitly and pass it to `monitor()` or `monitorEvent()`.
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
