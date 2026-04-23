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
from typing import Any, Callable, Coroutine, Self, Awaitable, TypeVar
from types import TracebackType

import builtins
import asyncio
import concurrent.futures
import copy
import datetime
import logging
import inspect
import threading
import weakref

from pathlib import Path
import sys

import o6
import o6.namespaces
from . import _o6
import o6.client_nodes as nodes
from o6 import MaybeAwaitable, AwaitReturn, Future, NodeIdLike
from o6.crypto import _load_cert_or_bytes, _load_cert_list
from o6.utils import _WorkerLoop
from typing import TypeAlias, cast


def check_status_code(status: o6.StatusCode, message: str) -> None:
    if status.code != 0:
        raise Exception(message + f" {status}")


def check_response_status(response, message: str) -> None:
    check_status_code(response.response_header.service_result, message)


def _history_read_value_id(nodeid: NodeIdLike) -> o6.HistoryReadValueId:
    rvid = o6.HistoryReadValueId()
    rvid.nodeid = o6.NodeId(nodeid)
    return rvid


def _unwrap_history_read(response: Any, is_scalar: bool) -> Any:
    if response.response_header.service_result.code != 0:
        raise ValueError(
            f"HistoryRead service failed with StatusCode "
            f"{response.response_header.service_result}"
        )
    results = response.results
    if is_scalar:
        if len(results) != 1:
            raise Exception("Results returned from server do not match")
        result = results[0]
        if result.status_code.code != 0:
            raise o6.StatusCodeError(result.status_code.code)
        hd = result.history_data
        if hasattr(hd, "body") and hd.body is not None:
            return hd.body
        return hd
    for i, result in enumerate(results):
        if result.status_code.code != 0:
            raise ValueError(
                f"HistoryRead result at index {i} has a bad StatusCode {result.status_code}"
            )
    out = []
    for r in results:
        hd = r.history_data
        if hasattr(hd, "body") and hd.body is not None:
            out.append(hd.body)
        else:
            out.append(hd)
    return out


class Client(_o6.Client):

    def __init__(
        self,
        endpoint_url: str | None = None,
        logger: logging.Logger | None = None,
        loop: asyncio.AbstractEventLoop | None = None,
        *,
        certificate: str | Path | bytes | None = None,
        private_key: str | Path | bytes | None = None,
        trust_list: list[str | Path | bytes] | None = None,
        revocation_list: list[str | Path | bytes] | None = None,
        security_mode: int | None = None,
        security_policy: str | None = None,
        application_uri: str | None = None,
        endpoint: o6.EndpointDescription | None = None,
        session_name: str | None = None,
        requested_session_timeout: int | None = None,
        session_locale_ids: list[str] | None = None,
        username: str | None = None,
        password: str | None = None,
    ) -> None:
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
        self._subscriptions: dict[int, Subscription] = {}
        self._default_subscription_id: int | None = None

        super().__init__(logger=logger, loop=loop)
        self._set_owns_loop(owns_loop)
        self.ns = o6.namespaces.Namespaces(self)
        self.config.tcp_reuse_addr = True
        if endpoint_url:
            self.config.endpoint_url = endpoint_url

        # Apply encryption if certificate and key are provided
        cert_bytes = _load_cert_or_bytes(certificate)
        key_bytes = _load_cert_or_bytes(private_key)
        tl = _load_cert_list(trust_list)
        if cert_bytes and key_bytes:
            rl = _load_cert_list(revocation_list)
            self.config.set_encryption(cert_bytes, key_bytes, tl, rl)

        if security_mode is not None:
            self.config.security_mode = int(security_mode)
        if security_policy is not None:
            policy_str = (
                security_policy.value
                if hasattr(security_policy, "value")
                else str(security_policy)
            )
            self.config.security_policy_uri = policy_str
        if application_uri is not None:
            self.config.application_uri = application_uri
        if session_name is not None:
            self.config.session_name = session_name
        if requested_session_timeout is not None:
            self.config.requested_session_timeout = requested_session_timeout
        if session_locale_ids is not None:
            self.config.session_locale_ids = session_locale_ids

        # Pre-populate config.endpoint so open62541 skips the discovery
        # phase.  The caller must build the EndpointDescription themselves
        # (including user_identity_tokens matching the server).
        if endpoint is not None:
            self.config.endpoint = endpoint
            if cert_bytes and key_bytes:
                self.config.set_authentication_cert(cert_bytes, key_bytes)

        if username is not None:
            self.config.set_username_password(username, password or "")
            self.config.allow_none_policy_password = True

        # Initialize the well-known entry-points into the namespace 0
        self.root = nodes.ObjectNode(self, "i=84", o6.QualifiedName(0, "Root"))
        self.objects = nodes.ObjectNode(self, "i=85", o6.QualifiedName(0, "Objects"))
        self.types = nodes.ObjectNode(self, "i=86", o6.QualifiedName(0, "Types"))
        self.views = nodes.ObjectNode(self, "i=87", o6.QualifiedName(0, "Views"))

        # Start the worker thread
        if self._worker is not None:
            self._worker.start()

    def __del__(self) -> None:
        # Check if still connected — if so, the deferred cleanup path in C
        # needs the asyncio loop alive for connection_lost to fire.
        connected = False
        try:
            channel_state, _, _ = self._get_state()
            connected = channel_state not in (0, 13)
        except Exception:
            pass
        if not connected:
            # Eagerly clean up C resources (UA_Client, C event loop) in
            # __del__ where Python API calls are safe, rather than
            # leaving it to tp_dealloc which runs inside the GC sweep.
            # After _cleanup(), self.client is NULL so tp_dealloc just
            # calls tp_free.
            try:
                self._cleanup()
            except Exception:
                pass
            if self._worker is not None:
                self._worker.stop(close=True)

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

        try:
            if asyncio.iscoroutine(aw) or inspect.iscoroutine(aw):
                fut = asyncio.run_coroutine_threadsafe(aw, self._loop)
            else:
                fut = asyncio.run_coroutine_threadsafe(_await(aw), self._loop)
        except RuntimeError:
            if asyncio.iscoroutine(aw):
                aw.close()
            raise RuntimeError("Client event loop is not running")

        if loop is None or hasattr(builtins, "__IPYTHON__"):
            return fut.result()
        else:
            return asyncio.wrap_future(fut)

    def add_namespace(self, uri: str) -> int:
        raise NotImplementedError(
            "Use client.ns.append() to register namespaces — "
            "calling add_namespace() directly bypasses type registration "
            "and breaks namespace index alignment."
        )

    @property
    def state(self) -> tuple[int, int, o6.StatusCode]:
        return self._get_state()

    @property
    def connected(self) -> bool:
        channel_state, _, _ = self.state
        return channel_state != o6.SecureChannelState.CLOSED

    @property
    def fully_connected(self) -> bool:
        _, session_state, _ = self.state
        return session_state == o6.SessionState.ACTIVATED

    def connect(
        self,
        endpoint_url: str | None = None,
    ) -> Any:
        sup = super()

        async def _connect() -> None:
            if endpoint_url:
                self.config.endpoint_url = endpoint_url
            await sup.connect()  # type: ignore[attr-defined]
            sub = await self.create_subscription(publishing_interval=100.0)
            self._default_subscription_id = sub.subscription_id

        if self._worker is not None and not self._worker.running:
            self._worker.start()

        return self._maybe_async(_connect())

    def disconnect(self) -> Any:
        if self._loop.is_closed():
            return None

        if self._worker is not None and not self._worker.running:
            return None

        sup = super()

        async def _disconnect() -> None:
            for subscription in list(self._subscriptions.values()):
                try:
                    await subscription.delete()
                except Exception:
                    pass  # channel may already be closed; proceed with disconnect
            self._subscriptions.clear()
            try:
                result = sup.disconnect()  # type: ignore[attr-defined]
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

    def connect_secure_channel(self, endpoint_url: str | None = None) -> Any:
        sup = super()

        async def _connect() -> None:
            if endpoint_url:
                self.config.endpoint_url = endpoint_url
            await sup.connect_secure_channel()  # type: ignore[attr-defined]

        if self._worker is not None and not self._worker.running:
            self._worker.start()

        return self._maybe_async(_connect())

    def disconnect_secure_channel(self) -> Any:
        sup = super()

        async def _disconnect() -> None:
            await sup.disconnect_secure_channel()  # type: ignore[attr-defined]

        return self._maybe_async(_disconnect())

    def start_reverse_connect(
        self,
        port: int,
        hostnames: list[str] | None = None,
    ) -> Any:
        sup = super()

        async def _connect() -> None:
            await sup.start_reverse_connect(port, hostnames or [])  # type: ignore[attr-defined]

        if self._worker is not None and not self._worker.running:
            self._worker.start()

        return self._maybe_async(_connect())

    def activate_current_session(self) -> Any:
        sup = super()

        async def _call() -> None:
            await sup.activate_current_session()  # type: ignore[attr-defined]

        return self._maybe_async(_call())

    def activate_session(
        self,
        auth_token: o6.NodeId,
        server_nonce: bytes,
    ) -> Any:
        sup = super()

        async def _call() -> None:
            await sup.activate_session(auth_token, server_nonce)  # type: ignore[attr-defined]

        return self._maybe_async(_call())

    def __enter__(self) -> Self:
        if not self.connected:
            self.connect()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        if self.connected:
            self.disconnect()

    async def __aenter__(self) -> Self:
        if not self.connected:
            await self.connect()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        if self.connected:
            await self.disconnect()

    #
    # Raw Service API
    #
    # These wrap the C-level async service calls so they work in both
    # sync and async contexts via _maybe_async.
    # The C extension methods must be called from within the event loop thread,
    # so each call is wrapped in an async def.

    async def _raw_service(self, service, request):
        return await service(request)

    # Discovery Service Set

    def service_find_servers(
        self, request: o6.FindServersRequest
    ) -> MaybeAwaitable[o6.FindServersResponse]:
        return self._maybe_async(self._service_find_servers(request))

    def service_find_servers_on_network(
        self, request: o6.FindServersOnNetworkRequest
    ) -> MaybeAwaitable[o6.FindServersOnNetworkResponse]:
        return self._maybe_async(self._service_find_servers_on_network(request))

    def service_get_endpoints(
        self, request: o6.GetEndpointsRequest
    ) -> MaybeAwaitable[o6.GetEndpointsResponse]:
        return self._maybe_async(self._service_get_endpoints(request))

    # TODO: RegisterServer, RegisterServer2

    # NodeManagement Service Set

    def service_add_nodes(
        self, request: o6.AddNodesRequest
    ) -> MaybeAwaitable[o6.AddNodesResponse]:
        return self._maybe_async(self._service_addNodes(request))

    def service_delete_nodes(
        self, request: o6.DeleteNodesRequest
    ) -> MaybeAwaitable[o6.DeleteNodesResponse]:
        return self._maybe_async(self._service_deleteNodes(request))

    def service_add_references(
        self, request: o6.AddReferencesRequest
    ) -> MaybeAwaitable[o6.AddReferencesResponse]:
        return self._maybe_async(self._service_addReferences(request))

    def service_delete_references(
        self, request: o6.DeleteReferencesRequest
    ) -> MaybeAwaitable[o6.DeleteReferencesResponse]:
        return self._maybe_async(self._service_deleteReferences(request))

    # View Service Set

    def service_browse(
        self, request: o6.BrowseRequest
    ) -> MaybeAwaitable[o6.BrowseResponse]:
        return self._maybe_async(self._service_browse(request))

    def service_browse_next(
        self, request: o6.BrowseNextRequest
    ) -> MaybeAwaitable[o6.BrowseNextResponse]:
        return self._maybe_async(self._service_browseNext(request))

    def service_translate_browse_paths_to_nodeids(
        self, request: o6.TranslateBrowsePathsToNodeIdsRequest
    ) -> MaybeAwaitable[o6.TranslateBrowsePathsToNodeIdsResponse]:
        return self._maybe_async(self._service_translateBrowsePathsToNodeIds(request))

    def service_register_nodes(
        self, request: o6.RegisterNodesRequest
    ) -> MaybeAwaitable[o6.RegisterNodesResponse]:
        return self._maybe_async(self._service_registerNodes(request))

    def service_unregister_nodes(
        self, request: o6.UnregisterNodesRequest
    ) -> MaybeAwaitable[o6.UnregisterNodesResponse]:
        return self._maybe_async(self._service_unregisterNodes(request))

    # Attribute Service Set

    def service_read(self, request: o6.ReadRequest) -> MaybeAwaitable[o6.ReadResponse]:
        return self._maybe_async(self._service_read(request))

    def service_history_read(
        self, request: o6.HistoryReadRequest
    ) -> MaybeAwaitable[o6.HistoryReadResponse]:
        return self._maybe_async(self._service_historyRead(request))

    def service_write(
        self, request: o6.WriteRequest
    ) -> MaybeAwaitable[o6.WriteResponse]:
        return self._maybe_async(self._service_write(request))

    def service_history_update(
        self, request: o6.HistoryUpdateRequest
    ) -> MaybeAwaitable[o6.HistoryUpdateResponse]:
        return self._maybe_async(self._service_historyUpdate(request))

    # Method Service Set

    def service_call(self, request: o6.CallRequest) -> MaybeAwaitable[o6.CallResponse]:
        return self._maybe_async(self._service_call(request))

    def get_remote_data_types(
        self, type_nodes: list[NodeIdLike] | None = None
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
        nodeids = [o6.NodeId(n) for n in type_nodes] if type_nodes is not None else None

        async def _browse_subtypes(root: o6.NodeId) -> list[o6.NodeId]:
            """Recursively browse HasSubtype of DataType nodes."""
            found: list[o6.NodeId] = []
            to_visit = [root]
            while to_visit:
                current = to_visit.pop()
                bd = o6.BrowseDescription()
                bd.nodeid = current
                bd.browse_direction = o6.BrowseDirection.FORWARD
                bd.reference_type_id = o6.NodeId(45)  # HasSubtype
                bd.node_class_mask = 64  # DataType
                req = o6.BrowseRequest()
                req.nodes_to_browse = [bd]
                resp = await self.service_browse(req)  # type: ignore[attr-defined, misc]
                if not resp.results or resp.results[0].status_code.code != 0:
                    continue
                for rd in resp.results[0].references:
                    child = o6.NodeId(f"ns={rd.nodeid.ns};i={rd.nodeid.id}")
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
            read_req = o6.ReadRequest()
            rvis: list[o6.ReadValueId] = []
            for nid in actual:
                rvi = o6.ReadValueId()
                rvi.nodeid = nid
                rvi.attribute_id = o6.AttributeId.DATATYPEDEFINITION
                rvis.append(rvi)
            for nid in actual:
                rvi = o6.ReadValueId()
                rvi.nodeid = nid
                rvi.attribute_id = o6.AttributeId.BROWSENAME
                rvis.append(rvi)
            read_req.nodes_to_read = rvis  # type: ignore[assignment]

            # service_read is fully async — the asyncio event loop thread stays
            # free to deliver the response, so there is no deadlock.
            response = await self.service_read(read_req)  # type: ignore[attr-defined, misc]

            n = len(actual)
            result: list[dict[str, Any]] = []
            for i, nid in enumerate(actual):
                sd = response.results[i].value
                if not isinstance(sd, o6.StructureDefinition):
                    continue
                type_name = ""
                qn = response.results[i + n].value
                if isinstance(qn, o6.QualifiedName):
                    type_name = qn.name or ""
                result.append(
                    {
                        "type_name": type_name,
                        "type_id": nid,
                        "binary_encoding_id": sd.default_encoding_id,
                        "type_kind": (
                            o6.DataTypeKind.Structure
                            if sd.structure_type == o6.StructureType.STRUCTURE
                            else (
                                o6.DataTypeKind.OptStruct
                                if sd.structure_type
                                == o6.StructureType.STRUCTUREWITHOPTIONALFIELDS
                                else o6.DataTypeKind.Union
                            )
                        ),
                        "members_size": len(sd.fields),
                    }
                )
            return result

        return self._maybe_async(_call())

    # Simplified Service API

    # Discovery

    def get_endpoints(  # type: ignore[override]
        self,
        server_url: str,
        locale_ids: list[str] | None = None,
        profile_uris: list[str] | None = None,
    ) -> Any:
        async def _call():
            req = o6.GetEndpointsRequest()
            req.endpoint_url = server_url
            if locale_ids:
                req.locale_ids = locale_ids
            if profile_uris:
                req.profile_uris = profile_uris
            response = await self._service_get_endpoints(req)
            return response.endpoints

        return self._maybe_async(_call())

    def find_servers(  # type: ignore[override]
        self,
        server_url: str,
        server_uris: list[str] | None = None,
        locale_ids: list[str] | None = None,
    ) -> Any:
        async def _call():
            req = o6.FindServersRequest()
            req.endpoint_url = server_url
            if server_uris:
                req.server_uris = server_uris
            if locale_ids:
                req.locale_ids = locale_ids
            response = await self._service_find_servers(req)
            return response.servers

        return self._maybe_async(_call())

    def find_servers_on_network(  # type: ignore[override]
        self,
        starting_record_id: int = 0,
        max_records_to_return: int = 0,
        server_capability_filter: list[str] | None = None,
    ) -> Any:
        async def _call():
            req = o6.FindServersOnNetworkRequest()
            req.starting_record_id = starting_record_id
            req.max_records_to_return = max_records_to_return
            if server_capability_filter:
                req.server_capability_filter = server_capability_filter
            response = await self._service_find_servers_on_network(req)
            return response.servers

        return self._maybe_async(_call())

    def read(
        self,
        target: NodeIdLike | list[NodeIdLike],
        attribute_id: o6.AttributeId = o6.AttributeId.VALUE,
        timestamps_to_return: int | None = None,
        as_datavalue: bool = False,
    ) -> Any:

        async def _read() -> Any:
            if not self.fully_connected:
                raise Exception("Client is not connected")

            is_scalar = not isinstance(target, list)

            # Prepare the ReadRequest
            read_request = o6.ReadRequest()
            if not isinstance(target, list):
                rvi = o6.ReadValueId()
                rvi.nodeid = o6.NodeId(target)
                rvi.attribute_id = attribute_id
                read_request.nodes_to_read = [rvi]
            else:
                rvis = [o6.ReadValueId() for id in target]
                for i, id in enumerate(target):
                    rvis[i].nodeid = o6.NodeId(id)
                    rvis[i].attribute_id = attribute_id
                read_request.nodes_to_read = rvis  # type: ignore[assignment]

            # Read
            response = await self._service_read(read_request)

            # Check the response consistency
            if response.response_header.service_result.code != 0:
                raise ValueError(
                    f"Read service failed with a bad StatusCode {response.response_header.service_result}"
                )
            if len(response.results) != len(read_request.nodes_to_read):
                raise Exception("Results returned from server do not match")

            # Return array result
            if not is_scalar:
                if not as_datavalue:
                    # Check if any value has a bad statuscode
                    for i, dv in enumerate(response.results):
                        if dv.status and dv.status.code != 0:
                            raise ValueError(
                                f"Read result at index {i} has a bad StatusCode {dv.status}"
                            )
                    return [dv.value for dv in response.results]
                return response.results

            # Return scalar result
            result = response.results[0]
            if as_datavalue:
                return result
            if result.status and result.status.code != 0:
                raise o6.StatusCodeError(result.status.code)
            return result.value

        return self._maybe_async(_read())

    def write(
        self,
        target: NodeIdLike | dict[NodeIdLike, Any],
        value: Any | None = None,
        attribute_id: o6.AttributeId = o6.AttributeId.VALUE,
    ) -> MaybeAwaitable[o6.StatusCode | list[o6.StatusCode]]:
        async def _write() -> o6.StatusCode | list[o6.StatusCode]:
            if not self.fully_connected:
                raise Exception("Client is not connected")

            # Dict form: write({nodeid: value, ...})
            if isinstance(target, dict):
                write_values = []
                for nodeid, val in target.items():
                    wv = o6.WriteValue()
                    wv.nodeid = o6.NodeId(nodeid)
                    wv.attribute_id = attribute_id
                    if isinstance(val, o6.DataValue):
                        wv.value = val
                    else:
                        wv.value.value = val
                    write_values.append(wv)
                write_request = o6.WriteRequest()
                write_request.nodes_to_write = write_values

                response = await self._service_write(write_request)
                if response.response_header.service_result.code != 0:
                    raise ValueError(
                        f"Write service failed with a bad StatusCode {response.response_header.service_result}"
                    )
                if len(response.results) != len(write_request.nodes_to_write):
                    raise Exception("Results returned from server do not match")
                return response.results

            if value is None:
                raise ValueError("value must be provided when target is not a dict")

            # Scalar write
            write_value = o6.WriteValue()
            write_value.nodeid = o6.NodeId(target)
            write_value.attribute_id = attribute_id
            if isinstance(value, o6.DataValue):
                write_value.value = value
            else:
                write_value.value.value = value
            write_request = o6.WriteRequest()
            write_request.nodes_to_write = [write_value]

            # Write
            response = await self._service_write(write_request)

            # Consistency check response
            if response.response_header.service_result.code != 0:
                raise ValueError(
                    f"Write service failed with a bad StatusCode {response.response_header.service_result}"
                )
            if len(response.results) != len(write_request.nodes_to_write):
                raise Exception("Results returned from server do not match")

            return response.results[0]

        return self._maybe_async(_write())

    def call(
        self, object_id: NodeIdLike, method_id: NodeIdLike, input_args: list[Any] = []
    ) -> MaybeAwaitable[tuple[o6.StatusCode, ...]]:
        async def _call() -> tuple[o6.StatusCode, ...]:
            if not self.fully_connected:
                raise Exception("Client is not connected")

            # Create call request
            method_request = o6.CallMethodRequest()
            method_request.object_id = o6.NodeId(object_id)
            method_request.method_id = o6.NodeId(method_id)
            method_request.input_arguments = input_args

            call_request = o6.CallRequest()
            call_request.methods_to_call = [method_request]

            # Call
            response = await self._service_call(call_request)

            # Consistency check the result
            if response.response_header.service_result.code != 0:
                raise Exception(
                    "Call service failed with a bad StatusCode "
                    f"{response.response_header.service_result}"
                )
            if len(response.results) != len(call_request.methods_to_call):
                raise Exception("Results returned from server do not match")

            # Return result
            result = response.results[0]
            return (result.status_code, *result.output_arguments)

        return self._maybe_async(_call())

    def browse(
        self,
        target: NodeIdLike,
        direction: o6.BrowseDirection = o6.BrowseDirection.FORWARD,
        reftype: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences,
        refsubtypes: bool = True,
        nodeclass_mask: o6.NodeClass = o6.NodeClass.UNSPECIFIED,
        result_mask: o6.BrowseResultMask = o6.BrowseResultMask(0),
    ) -> MaybeAwaitable[o6.BrowseResult]:

        async def _browse() -> Any:
            if not self.fully_connected:
                raise Exception("Client is not connected")

            # Prepare the BrowseRequest
            bd = o6.BrowseDescription()
            bd.nodeid = o6.NodeId(target)
            bd.browse_direction = direction
            bd.reference_type_id = o6.NodeId(reftype)
            bd.include_subtypes = refsubtypes
            bd.node_class_mask = nodeclass_mask
            bd.result_mask = result_mask
            request = o6.BrowseRequest()
            request.nodes_to_browse = [bd]

            # Browse
            response = await self._service_browse(request)
            if response.response_header.service_result.code != 0:
                raise ValueError(
                    f"Browse service failed with StatusCode {response.response_header.service_result}"
                )
            if len(response.results) != len(request.nodes_to_browse):
                raise Exception("Results returned from server do not match")
            res = response.results[0]
            if res.status_code.code != 0:
                raise ValueError(
                    f"Browse service failed with StatusCode {res.status_code}"
                )
            return res.references

        return self._maybe_async(_browse())

    # History Access

    def history_read(
        self,
        target: NodeIdLike | list[NodeIdLike],
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        num_values_per_node: int = 0,
        return_bounds: bool = False,
        timestamps_to_return: o6.TimestampsToReturn = o6.TimestampsToReturn.BOTH,
    ) -> Any:

        async def _history_read() -> Any:
            if not self.fully_connected:
                raise Exception("Client is not connected")

            is_scalar = not isinstance(target, list)
            targets = cast(list[NodeIdLike], [target] if is_scalar else target)

            details = o6.ReadRawModifiedDetails()
            details.is_read_modified = False
            details.start_time = o6.DateTime(start_time)
            details.end_time = o6.DateTime(end_time)
            details.num_values_per_node = num_values_per_node
            details.return_bounds = return_bounds

            request = o6.HistoryReadRequest()
            request.history_read_details = details
            request.timestamps_to_return = timestamps_to_return
            request.nodes_to_read = [_history_read_value_id(nid) for nid in targets]

            response = await self._service_historyRead(request)
            return _unwrap_history_read(response, is_scalar)

        return self._maybe_async(_history_read())

    def history_read_modified(
        self,
        target: NodeIdLike | list[NodeIdLike],
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        num_values_per_node: int = 0,
        return_bounds: bool = False,
        timestamps_to_return: o6.TimestampsToReturn = o6.TimestampsToReturn.BOTH,
    ) -> Any:

        async def _history_read_modified() -> Any:
            if not self.fully_connected:
                raise Exception("Client is not connected")

            is_scalar = not isinstance(target, list)
            targets = cast(list[NodeIdLike], [target] if is_scalar else target)

            details = o6.ReadRawModifiedDetails()
            details.is_read_modified = True
            details.start_time = o6.DateTime(start_time)
            details.end_time = o6.DateTime(end_time)
            details.num_values_per_node = num_values_per_node
            details.return_bounds = return_bounds

            request = o6.HistoryReadRequest()
            request.history_read_details = details
            request.timestamps_to_return = timestamps_to_return
            request.nodes_to_read = [_history_read_value_id(nid) for nid in targets]

            response = await self._service_historyRead(request)
            return _unwrap_history_read(response, is_scalar)

        return self._maybe_async(_history_read_modified())

    def history_read_at_time(
        self,
        target: NodeIdLike | list[NodeIdLike],
        timestamps: list[datetime.datetime],
        use_simple_bounds: bool = False,
    ) -> Any:

        async def _history_read_at_time() -> Any:
            if not self.fully_connected:
                raise Exception("Client is not connected")

            is_scalar = not isinstance(target, list)
            targets = cast(list[NodeIdLike], [target] if is_scalar else target)

            details = o6.ReadAtTimeDetails()
            details.req_times = [o6.DateTime(t) for t in timestamps]
            details.use_simple_bounds = use_simple_bounds

            request = o6.HistoryReadRequest()
            request.history_read_details = details
            request.timestamps_to_return = o6.TimestampsToReturn.BOTH
            request.nodes_to_read = [_history_read_value_id(nid) for nid in targets]

            response = await self._service_historyRead(request)
            return _unwrap_history_read(response, is_scalar)

        return self._maybe_async(_history_read_at_time())

    def history_read_processed(
        self,
        target: NodeIdLike | list[NodeIdLike],
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        processing_interval: float,
        aggregate_type: NodeIdLike = "i=2341",
    ) -> Any:

        async def _history_read_processed() -> Any:
            if not self.fully_connected:
                raise Exception("Client is not connected")

            is_scalar = not isinstance(target, list)
            targets = cast(list[NodeIdLike], [target] if is_scalar else target)

            details = o6.ReadProcessedDetails()
            details.start_time = o6.DateTime(start_time)
            details.end_time = o6.DateTime(end_time)
            details.processing_interval = processing_interval
            details.aggregate_type = [o6.NodeId(aggregate_type) for _ in targets]

            request = o6.HistoryReadRequest()
            request.history_read_details = details
            request.timestamps_to_return = o6.TimestampsToReturn.BOTH
            request.nodes_to_read = [_history_read_value_id(nid) for nid in targets]

            response = await self._service_historyRead(request)
            return _unwrap_history_read(response, is_scalar)

        return self._maybe_async(_history_read_processed())

    def history_update(
        self,
        target: NodeIdLike,
        values: list[o6.DataValue],
        mode: o6.PerformUpdateType = o6.PerformUpdateType.INSERT,
    ) -> Any:

        async def _history_update() -> Any:
            if not self.fully_connected:
                raise Exception("Client is not connected")

            details = o6.UpdateDataDetails()
            details.nodeid = o6.NodeId(target)
            details.perform_insert_replace = mode
            details.update_values = values

            request = o6.HistoryUpdateRequest()
            request.history_update_details = [o6.ExtensionObject(details)]

            response = await self._service_historyUpdate(request)
            if response.response_header.service_result.code != 0:
                raise ValueError(
                    f"HistoryUpdate service failed with StatusCode "
                    f"{response.response_header.service_result}"
                )
            if len(response.results) != 1:
                raise Exception("Results returned from server do not match")
            return response.results[0]

        return self._maybe_async(_history_update())

    def history_delete(
        self,
        target: NodeIdLike,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
    ) -> Any:

        async def _history_delete() -> Any:
            if not self.fully_connected:
                raise Exception("Client is not connected")

            details = o6.DeleteRawModifiedDetails()
            details.nodeid = o6.NodeId(target)
            details.is_delete_modified = False
            details.start_time = o6.DateTime(start_time)
            details.end_time = o6.DateTime(end_time)

            request = o6.HistoryUpdateRequest()
            request.history_update_details = [o6.ExtensionObject(details)]

            response = await self._service_historyUpdate(request)
            if response.response_header.service_result.code != 0:
                raise ValueError(
                    f"HistoryUpdate (delete) service failed with StatusCode "
                    f"{response.response_header.service_result}"
                )
            if len(response.results) != 1:
                raise Exception("Results returned from server do not match")
            return response.results[0]

        return self._maybe_async(_history_delete())

    # Node management

    def add_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_class: o6.NodeClass,
        node_attributes: Any,
        requested_new_nodeid: NodeIdLike | None,
        reference_type_id: NodeIdLike,
        type_definition: NodeIdLike | None = None,
    ) -> MaybeAwaitable[o6.NodeId]:

        async def _add() -> o6.NodeId:
            if not self.fully_connected:
                raise Exception("Client is not connected")

            item = o6.AddNodesItem()
            item.parent_nodeid = o6.ExpandedNodeId(o6.NodeId(parent_nodeid))
            item.reference_type_id = o6.NodeId(reference_type_id)
            item.requested_new_nodeid = (
                o6.ExpandedNodeId(o6.NodeId(requested_new_nodeid))
                if requested_new_nodeid
                else o6.ExpandedNodeId()
            )
            item.type_definition = (
                o6.ExpandedNodeId(o6.NodeId(type_definition))
                if type_definition
                else o6.ExpandedNodeId()
            )
            item.node_class = node_class

            if isinstance(browse_name, str):
                item.browse_name = o6.QualifiedName(browse_name)
            else:
                item.browse_name = browse_name

            item.node_attributes = node_attributes

            request = o6.AddNodesRequest()
            request.nodes_to_add = [item]

            response = await self._service_addNodes(request)

            if response.response_header.service_result.code != 0:
                raise ValueError(
                    f"AddNodes service failed with StatusCode {response.response_header.service_result}"
                )
            if len(response.results) != 1:
                raise Exception("Unexpected number of results from AddNodes")

            result = response.results[0]
            if result.status_code.code != 0:
                raise Exception(f"AddNode failed: {result.status_code}")

            return result.added_nodeid

        return self._maybe_async(_add())

    def add_variable_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_attributes: o6.VariableAttributes,
        requested_new_nodeid: NodeIdLike | None = None,
        reference_type_id: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.Aggregates.HasComponent,
        type_definition: NodeIdLike = o6.ns.ns0.vartypes.BaseVariableType.BaseDataVariableType,
    ) -> MaybeAwaitable[o6.NodeId]:
        return self.add_node(
            parent_nodeid,
            browse_name,
            o6.NodeClass.VARIABLE,
            node_attributes,
            requested_new_nodeid,
            reference_type_id,
            type_definition,
        )

    def add_variable_type_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_attributes: o6.VariableTypeAttributes,
        requested_new_nodeid: NodeIdLike | None = None,
        reference_type_id: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.HasSubtype,
    ) -> MaybeAwaitable[o6.NodeId]:
        return self.add_node(
            parent_nodeid,
            browse_name,
            o6.NodeClass.VARIABLETYPE,
            node_attributes,
            requested_new_nodeid,
            reference_type_id,
        )

    def add_object_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_attributes: o6.ObjectAttributes,
        requested_new_nodeid: NodeIdLike | None = None,
        reference_type_id: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.Aggregates.HasComponent,
        type_definition: NodeIdLike = o6.ns.ns0.objtypes.BaseObjectType,
    ) -> MaybeAwaitable[o6.NodeId]:
        return self.add_node(
            parent_nodeid,
            browse_name,
            o6.NodeClass.OBJECT,
            node_attributes,
            requested_new_nodeid,
            reference_type_id,
            type_definition,
        )

    def add_object_type_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_attributes: o6.ObjectTypeAttributes,
        requested_new_nodeid: NodeIdLike | None = None,
        reference_type_id: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.HasSubtype,
    ) -> MaybeAwaitable[o6.NodeId]:
        return self.add_node(
            parent_nodeid,
            browse_name,
            o6.NodeClass.OBJECTTYPE,
            node_attributes,
            requested_new_nodeid,
            reference_type_id,
        )

    def add_view_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_attributes: o6.ViewAttributes,
        requested_new_nodeid: NodeIdLike | None = None,
        reference_type_id: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.Aggregates.HasComponent,
    ) -> MaybeAwaitable[o6.NodeId]:
        return self.add_node(
            parent_nodeid,
            browse_name,
            o6.NodeClass.VIEW,
            node_attributes,
            requested_new_nodeid,
            reference_type_id,
        )

    def add_reference_type_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_attributes: o6.ReferenceTypeAttributes,
        requested_new_nodeid: NodeIdLike | None = None,
        reference_type_id: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.HasSubtype,
    ) -> MaybeAwaitable[o6.NodeId]:
        return self.add_node(
            parent_nodeid,
            browse_name,
            o6.NodeClass.REFERENCETYPE,
            node_attributes,
            requested_new_nodeid,
            reference_type_id,
        )

    def add_data_type_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_attributes: o6.DataTypeAttributes,
        requested_new_nodeid: NodeIdLike | None = None,
        reference_type_id: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.HasSubtype,
    ) -> MaybeAwaitable[o6.NodeId]:
        return self.add_node(
            parent_nodeid,
            browse_name,
            o6.NodeClass.DATATYPE,
            node_attributes,
            requested_new_nodeid,
            reference_type_id,
        )

    def add_method_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_attributes: o6.MethodAttributes,
        requested_new_nodeid: NodeIdLike | None = None,
        reference_type_id: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.Aggregates.HasComponent,
    ) -> MaybeAwaitable[o6.NodeId]:
        return self.add_node(
            parent_nodeid,
            browse_name,
            o6.NodeClass.METHOD,
            node_attributes,
            requested_new_nodeid,
            reference_type_id,
        )

    def delete_node(
        self,
        nodeid: NodeIdLike | list[NodeIdLike],
        delete_target_references: bool = True,
    ) -> MaybeAwaitable[None]:

        async def _delete_node() -> None:
            if not self.fully_connected:
                raise Exception("Client is not connected")

            ids: list[NodeIdLike] = nodeid if isinstance(nodeid, list) else [nodeid]

            items = []
            for nid in ids:
                item = o6.DeleteNodesItem()
                item.nodeid = o6.NodeId(nid)
                item.delete_target_references = delete_target_references
                items.append(item)

            request = o6.DeleteNodesRequest()
            request.nodes_to_delete = items

            response = await self._service_deleteNodes(request)

            if response.response_header.service_result.code != 0:
                raise ValueError(
                    f"DeleteNodes service failed with StatusCode {response.response_header.service_result}"
                )
            if len(response.results) != len(items):
                raise Exception("Results returned from server do not match")

            for i, result in enumerate(response.results):
                if result.code != 0:
                    raise o6.StatusCodeError(result.code)

        return self._maybe_async(_delete_node())

    def add_reference(
        self,
        source_nodeid: NodeIdLike,
        reference_type_id: NodeIdLike,
        target_nodeid: NodeIdLike,
        is_forward: bool = True,
        target_node_class: o6.NodeClass = o6.NodeClass.UNSPECIFIED,
        target_server_uri: str = "",
    ) -> MaybeAwaitable[None]:

        async def _add_reference() -> None:
            if not self.fully_connected:
                raise Exception("Client is not connected")

            item = o6.AddReferencesItem()
            item.source_nodeid = o6.NodeId(source_nodeid)
            item.reference_type_id = o6.NodeId(reference_type_id)
            item.is_forward = is_forward
            item.target_server_uri = target_server_uri
            item.target_nodeid = o6.ExpandedNodeId(o6.NodeId(target_nodeid))
            item.target_node_class = target_node_class

            request = o6.AddReferencesRequest()
            request.references_to_add = [item]

            response = await self._service_addReferences(request)

            if response.response_header.service_result.code != 0:
                raise ValueError(
                    f"AddReferences service failed with StatusCode {response.response_header.service_result}"
                )
            if len(response.results) != 1:
                raise Exception("Unexpected number of results from AddReferences")

            result = response.results[0]
            if result.code != 0:
                raise o6.StatusCodeError(result.code)

        return self._maybe_async(_add_reference())

    def delete_reference(
        self,
        source_nodeid: NodeIdLike,
        reference_type_id: NodeIdLike,
        target_nodeid: NodeIdLike,
        is_forward: bool = True,
        delete_bidirectional: bool = True,
    ) -> MaybeAwaitable[None]:

        async def _delete_reference() -> None:
            if not self.fully_connected:
                raise Exception("Client is not connected")

            item = o6.DeleteReferencesItem()
            item.source_nodeid = o6.NodeId(source_nodeid)
            item.reference_type_id = o6.NodeId(reference_type_id)
            item.is_forward = is_forward
            item.target_nodeid = o6.ExpandedNodeId(o6.NodeId(target_nodeid))
            item.delete_bidirectional = delete_bidirectional

            request = o6.DeleteReferencesRequest()
            request.references_to_delete = [item]

            response = await self._service_deleteReferences(request)

            if response.response_header.service_result.code != 0:
                raise ValueError(
                    f"DeleteReferences service failed with StatusCode {response.response_header.service_result}"
                )
            if len(response.results) != 1:
                raise Exception("Unexpected number of results from DeleteReferences")

            result = response.results[0]
            if result.code != 0:
                raise o6.StatusCodeError(result.code)

        return self._maybe_async(_delete_reference())

    def __getitem__(self, key: NodeIdLike) -> MaybeAwaitable[nodes.Node]:
        async def _get_node() -> nodes.Node:
            # Read NodeClass and BrowseName
            rvi_nc = o6.ReadValueId()
            rvi_nc.nodeid = o6.NodeId(key)
            rvi_nc.attribute_id = o6.AttributeId.NODECLASS
            rvi_bn = o6.ReadValueId()
            rvi_bn.nodeid = o6.NodeId(key)
            rvi_bn.attribute_id = o6.AttributeId.BROWSENAME
            read_request = o6.ReadRequest()
            read_request.nodes_to_read = [rvi_nc, rvi_bn]
            read_response = await self._service_read(read_request)

            # Create the Node
            node_class = o6.NodeClass(read_response.results[0].value)
            browse_name = read_response.results[1].value
            node_type = nodes._nodeclass2type(node_class)
            return node_type(self, key, browse_name)

        return self._maybe_async(_get_node())

    def create_subscription(
        self,
        req: o6.CreateSubscriptionRequest | None = None,
        publishing_interval: float = 100.0,
        lifetime_count: int = 36000,
        max_keepalive_count: int = 10,
    ) -> MaybeAwaitable[Subscription]:

        async def _create_subscription() -> Subscription:
            if not self.fully_connected:
                raise Exception("Client is not connected")

            subscription = await Subscription(
                self, publishing_interval, lifetime_count, max_keepalive_count
            )
            assert subscription.subscription_id is not None
            self._subscriptions[subscription.subscription_id] = subscription
            return subscription

        return self._maybe_async(_create_subscription())

    def monitor(
        self,
        target: NodeIdLike | list[NodeIdLike],
        callback: MonitoredItem.DataChangeCallback | None = None,
        sampling_interval: float = 100.0,
        subscription: Subscription | None = None,
        context: Any = None,
    ) -> MaybeAwaitable[MonitoredItem | list[MonitoredItem]]:

        async def _monitor() -> MonitoredItem | list[MonitoredItem]:
            sub = (
                subscription if subscription is not None else self.default_subscription
            )

            if isinstance(target, list):
                return [
                    await sub.monitor(nodeid, callback, sampling_interval, context)
                    for nodeid in target
                ]
            else:
                return await sub.monitor(target, callback, sampling_interval, context)

        return self._maybe_async(_monitor())

    def monitor_event(
        self,
        nodeid: NodeIdLike,
        callback: MonitoredItem.EventCallback,
        event_filter: o6.EventFilter | str | None = None,
        subscription: Subscription | None = None,
        sampling_interval: float = 0.0,
        context: Any = None,
    ) -> MaybeAwaitable[MonitoredItem]:

        async def _monitor_event() -> MonitoredItem:
            sub = (
                subscription if subscription is not None else self.default_subscription
            )
            return await sub.monitor_event(
                nodeid, callback, event_filter, sampling_interval, context
            )

        return self._maybe_async(_monitor_event())

    # Properties

    @property
    def subscriptions(self) -> dict[int, Subscription]:
        return self._subscriptions.copy()

    @property
    def default_subscription(self) -> "Subscription":
        if (
            self._default_subscription_id is None
            or self._default_subscription_id not in self._subscriptions
        ):
            raise RuntimeError("No default subscription — client is not connected")
        return self._subscriptions[self._default_subscription_id]


class Subscription:
    def __init__(
        self,
        client: Client,
        publishing_interval: float,
        lifetime_count: int,
        max_keepalive_count: int,
        max_notifications_per_publish: int = 10,
        publishing_enabled: bool = True,
    ) -> None:
        self._client_ref: weakref.ref[Client] = weakref.ref(client)
        self._subscription_id: int | None = None
        self._monitored_items: dict[int, MonitoredItem] = {}
        self._publishing_interval = publishing_interval
        self._lifetime_count = lifetime_count
        self._max_keepalive_count = max_keepalive_count
        self._max_notifications_per_publish = max_notifications_per_publish
        self._publishing_enabled = publishing_enabled

        async def _create_subscription() -> None:
            create_request = o6.CreateSubscriptionRequest()
            create_request.requested_publishing_interval = publishing_interval
            create_request.requested_lifetime_count = lifetime_count
            create_request.requested_max_keep_alive_count = max_keepalive_count
            create_request.max_notifications_per_publish = max_notifications_per_publish
            create_request.publishing_enabled = publishing_enabled
            create_request.priority = 0

            response = await client._service_createSubscription(create_request)
            check_response_status(response, "Subscription creation")
            self._subscription_id = response.subscription_id

        self._pending_init = client._maybe_async(_create_subscription())

    def __await__(self) -> AwaitReturn[Subscription]:
        async def _init() -> Subscription:
            if self._pending_init is not None:
                await self._pending_init
                self._pending_init = None
            return self

        return _init().__await__()

    def __bool__(self) -> bool:
        return self._subscription_id is not None

    def _check_valid(self, op: str) -> None:
        if not self:
            raise RuntimeError(
                f"Cannot call {op!r} on an uninitialized or already-deleted Subscription"
            )

    def monitor(
        self,
        nodeid: NodeIdLike,
        callback: MonitoredItem.DataChangeCallback | None = None,
        sampling_interval: float = 100.0,
        context: Any = None,
    ) -> MaybeAwaitable[MonitoredItem]:

        def printout(mon: MonitoredItem, value) -> None:
            print(f"MonitoredItem {mon._monitored_item_id}: {value}")

        typed_callback: MonitoredItem.DataChangeCallback = printout
        if callback is not None:
            typed_callback = callback

        # if isinstance(nodeid, nodes.Node):
        #    nodeid = nodeid._nodeid

        async def _monitor_async() -> MonitoredItem:
            self._check_valid("monitor_data_change")
            monitored_item = await MonitoredItem.data_change(
                self,
                nodeid,
                typed_callback,
                sampling_interval=sampling_interval,
                context=context,
            )
            assert monitored_item.monitored_item_id is not None
            self._monitored_items[monitored_item.monitored_item_id] = monitored_item
            return monitored_item

        return self._client._maybe_async(_monitor_async())

    def monitor_event(
        self,
        nodeid: NodeIdLike,
        callback: MonitoredItem.EventCallback,
        event_filter: o6.EventFilter | str | None = None,
        sampling_interval: float = 0.0,
        context: Any = None,
    ) -> MaybeAwaitable[MonitoredItem]:

        async def _monitor_event_async() -> MonitoredItem:
            self._check_valid("monitor_event")
            ef = None
            if isinstance(event_filter, str):
                ef = o6.EventFilter.parse(event_filter, logger=self._client._logger)
            elif isinstance(event_filter, o6.EventFilter):
                ef = event_filter
            monitored_item = await MonitoredItem.event(
                self,
                nodeid,
                callback,
                event_filter=ef,
                sampling_interval=sampling_interval,
                context=context,
            )
            assert monitored_item.monitored_item_id is not None
            self._monitored_items[monitored_item.monitored_item_id] = monitored_item
            return monitored_item

        return self._client._maybe_async(_monitor_event_async())

    def delete(self) -> Any:

        async def _delete() -> None:
            if self._subscription_id is None:
                self._client._logger.warning(
                    "Subscription.delete() called on an uninitialized or already-deleted subscription"
                )
                return

            subscription_id = self._subscription_id

            # Delete all monitored items first (before clearing _subscription_id,
            # because item.delete() reads self._subscription._subscription_id)
            for item in list(self._monitored_items.values()):
                await item.delete()

            self._subscription_id = None

            # Delete subscription
            delete_request = o6.DeleteSubscriptionsRequest()
            delete_request.subscription_ids = [subscription_id]

            response = await self._client._service_deleteSubscriptions(delete_request)
            check_response_status(response, "Subscription deletion")

            if subscription_id in self._client._subscriptions:
                del self._client._subscriptions[subscription_id]

        return self._client._maybe_async(_delete())

    def modify(
        self,
        publishing_interval: float | None = None,
        lifetime_count: int | None = None,
        max_keepalive_count: int | None = None,
        max_notifications_per_publish: int | None = None,
        publishing_enabled: bool | None = None,
    ) -> Any:

        async def _modify() -> None:
            self._check_valid("modify")
            assert self._subscription_id is not None  # _check_valid ensures non-None

            modify_request = o6.ModifySubscriptionRequest()
            modify_request.subscription_id = self._subscription_id
            modify_request.requested_publishing_interval = (
                publishing_interval
                if publishing_interval is not None
                else self._publishing_interval
            )
            modify_request.requested_lifetime_count = (
                lifetime_count if lifetime_count is not None else self._lifetime_count
            )
            modify_request.requested_max_keep_alive_count = (
                max_keepalive_count
                if max_keepalive_count is not None
                else self._max_keepalive_count
            )
            modify_request.max_notifications_per_publish = (
                max_notifications_per_publish
                if max_notifications_per_publish is not None
                else self._max_notifications_per_publish
            )

            response = await self._client._service_modifySubscription(modify_request)
            check_response_status(response, "Subscription modification")

            self._publishing_interval = response.revised_publishing_interval
            self._lifetime_count = response.revised_lifetime_count
            self._max_keepalive_count = response.revised_max_keep_alive_count

            # publishing_enabled requires a separate SetPublishingMode service call
            if (
                publishing_enabled is not None
                and publishing_enabled != self._publishing_enabled
            ):
                spm_request = o6.SetPublishingModeRequest()
                spm_request.publishing_enabled = publishing_enabled
                spm_request.subscription_ids = [self._subscription_id]
                spm_response = await self._client._service_setPublishingMode(
                    spm_request
                )
                check_response_status(spm_response, "Set publishing mode")
                self._publishing_enabled = publishing_enabled

        return self._client._maybe_async(_modify())

    # Properties

    @property
    def _client(self) -> Client:
        c = self._client_ref()
        if c is None:
            raise RuntimeError("Client has been garbage-collected")
        return c

    @property
    def client(self) -> Client:
        return self._client

    @property
    def subscription_id(self) -> int | None:
        return self._subscription_id

    @property
    def monitored_items(self) -> dict[int, MonitoredItem]:
        return self._monitored_items.copy()

    @property
    def publishing_interval(self) -> float:
        return self._publishing_interval

    @property
    def lifetime_count(self) -> int:
        return self._lifetime_count

    @property
    def max_keepalive_count(self) -> int:
        return self._max_keepalive_count

    @property
    def max_notifications_per_publish(self) -> int:
        return self._max_notifications_per_publish

    @property
    def publishing_enabled(self) -> bool:
        return self._publishing_enabled


class MonitoredItem:

    DataChangeCallback: TypeAlias = (
        Callable[[Any], None] | Callable[["MonitoredItem", Any], None]
    )
    EventCallback: TypeAlias = (
        Callable[[dict], None] | Callable[["MonitoredItem", dict], None]
    )

    def __init__(self, subscription: Subscription) -> None:
        self.context: Any = None  # Can be set directly
        self._subscription_ref: weakref.ref[Subscription] = weakref.ref(subscription)
        self._monitored_item_id: int | None = None
        self._pending_init: Any | None = None
        self._sampling_interval: float = 0.0
        self._queue_size: int = 0
        self._item_to_monitor = o6.ReadValueId()
        self._monitoring_params = o6.MonitoringParameters()
        self._monitoring_mode: o6.MonitoringMode = o6.MonitoringMode.REPORTING

    @classmethod
    def data_change(
        cls,
        subscription: Subscription,
        nodeid: NodeIdLike,
        callback: MonitoredItem.DataChangeCallback,
        attribute_id: o6.AttributeId = o6.AttributeId.VALUE,
        index_range: str = "",
        data_encoding: o6.QualifiedName | str = "",
        sampling_interval: float = 250.0,
        context: Any = None,
    ) -> MonitoredItem:
        item = cls(subscription)
        item.context = context
        item._item_to_monitor.nodeid = o6.NodeId(nodeid)
        item._item_to_monitor.attribute_id = attribute_id
        item._item_to_monitor.index_range = index_range
        item._item_to_monitor.data_encoding = (
            o6.QualifiedName(data_encoding)
            if isinstance(data_encoding, str)
            else data_encoding
        )
        item._monitoring_params.sampling_interval = sampling_interval
        item._monitoring_params.queue_size = 1
        item._monitoring_params.discard_oldest = True

        async def _create() -> None:
            assert (
                subscription.subscription_id is not None
            )  # subscription awaited before use
            create_request = o6.CreateMonitoredItemsRequest()
            create_request.subscription_id = subscription.subscription_id
            create_request.timestamps_to_return = o6.TimestampsToReturn.BOTH

            monitored_item_request = o6.MonitoredItemCreateRequest()
            monitored_item_request.item_to_monitor = copy.copy(item._item_to_monitor)
            monitored_item_request.monitoring_mode = o6.MonitoringMode.REPORTING
            monitored_item_request.requested_parameters = copy.copy(
                item._monitoring_params
            )

            create_request.items_to_create = [monitored_item_request]

            n_params = len(inspect.signature(callback).parameters)
            if n_params == 1:

                def wrapper(data_value):
                    callback(data_value)

            else:

                def wrapper(data_value):
                    callback(item, data_value)

            response = (
                await subscription._client._service_createMonitoredItems_datachange(
                    create_request, wrapper
                )
            )
            check_response_status(response, "Monitored item creation")

            if response.results and len(response.results) != 1:
                raise Exception("Wrong results returned from monitored item creation")

            result = response.results[0]
            check_status_code(result.status_code, "Monitored item result")
            item._monitored_item_id = result.monitored_item_id
            item._sampling_interval = result.revised_sampling_interval
            item._queue_size = result.revised_queue_size

        item._pending_init = subscription._client._maybe_async(_create())
        return item

    @classmethod
    def event(
        cls,
        subscription: Subscription,
        nodeid: NodeIdLike,
        callback: MonitoredItem.EventCallback,
        event_filter: o6.EventFilter | str | None = None,
        sampling_interval: float = 0.0,
        context: Any = None,
    ) -> MonitoredItem:
        item = cls(subscription)
        item.context = context
        item._item_to_monitor = o6.ReadValueId()
        item._item_to_monitor.nodeid = o6.NodeId(nodeid)
        item._item_to_monitor.attribute_id = o6.AttributeId.EVENTNOTIFIER

        async def _create() -> None:
            assert (
                subscription.subscription_id is not None
            )  # subscription awaited before use
            create_request = o6.CreateMonitoredItemsRequest()
            create_request.subscription_id = subscription.subscription_id
            create_request.timestamps_to_return = o6.TimestampsToReturn.BOTH

            monitored_item_request = o6.MonitoredItemCreateRequest()
            monitored_item_request.item_to_monitor = copy.copy(item._item_to_monitor)
            monitored_item_request.monitoring_mode = o6.MonitoringMode.REPORTING

            monitoring_params = o6.MonitoringParameters()
            monitoring_params.client_handle = 0  # Will be overwritten by server anyway
            monitoring_params.sampling_interval = sampling_interval
            monitoring_params.queue_size = 100
            monitoring_params.discard_oldest = True
            if isinstance(event_filter, str):
                ef = o6.EventFilter.parse(
                    event_filter, logger=subscription._client._logger
                )
            elif event_filter is None:
                ef = o6.EventFilter.parse(
                    "SELECT /EventId, /EventType, /SourceName, /Time, /Message, /Severity"
                )
            else:
                ef = event_filter
            monitoring_params.filter = ef
            monitored_item_request.requested_parameters = monitoring_params

            create_request.items_to_create = [monitored_item_request]

            n_params = len(inspect.signature(callback).parameters)
            if n_params == 1:

                def wrapper(event_fields):
                    callback(event_fields)

            else:

                def wrapper(event_fields):
                    callback(item, event_fields)

            response = await subscription._client._service_createMonitoredItems_event(
                create_request, wrapper
            )
            check_response_status(response, "Event monitored item creation")

            if response.results and len(response.results) != 1:
                raise Exception(
                    "Wrong results returned from event monitored item creation"
                )

            result = response.results[0]
            check_status_code(result.status_code, "Event monitored item result")
            item._monitored_item_id = result.monitored_item_id
            item._monitoring_params.sampling_interval = result.revised_sampling_interval
            item._monitoring_params.queue_size = result.revised_queue_size

        item._pending_init = subscription._client._maybe_async(_create())
        return item

    def __await__(self) -> AwaitReturn[MonitoredItem]:
        async def _init() -> MonitoredItem:
            if self._pending_init is not None:
                await self._pending_init
                self._pending_init = None
            return self

        return _init().__await__()

    def __bool__(self) -> bool:
        return self._monitored_item_id is not None

    def _check_valid(self, op: str) -> None:
        if not self:
            raise RuntimeError(
                f"Cannot call {op!r} on an uninitialized or already-deleted MonitoredItem"
            )

    def delete(self) -> Any:

        async def _delete() -> None:
            if self._monitored_item_id is None:
                self._subscription._client._logger.warning(
                    "MonitoredItem.delete() called on an uninitialized or already-deleted monitored item"
                )
                return

            monitored_item_id = self._monitored_item_id
            self._monitored_item_id = None

            delete_request = o6.DeleteMonitoredItemsRequest()
            assert (
                self._subscription.subscription_id is not None
            )  # subscription must be valid
            delete_request.subscription_id = self._subscription.subscription_id
            delete_request.monitored_item_ids = [monitored_item_id]

            response = await self._subscription._client._service_deleteMonitoredItems(
                delete_request
            )
            check_response_status(response, "Monitored item deletion")

            if monitored_item_id in self._subscription._monitored_items:
                del self._subscription._monitored_items[monitored_item_id]

        return self._subscription._client._maybe_async(_delete())

    def modify(
        self,
        sampling_interval: float | None = None,
        queue_size: int | None = None,
        discard_oldest: bool | None = None,
        filter: o6.DataChangeFilter | o6.EventFilter | str | None = None,
    ) -> Any:

        async def _modify() -> None:
            self._check_valid("modify")
            assert (
                self._subscription.subscription_id is not None
            )  # _check_valid ensures non-None
            assert self._monitored_item_id is not None  # _check_valid ensures non-None

            resolved_filter = filter
            if isinstance(filter, str):
                is_event = (
                    self._item_to_monitor.attribute_id == o6.AttributeId.EVENTNOTIFIER
                )
                if not is_event:
                    raise TypeError(
                        "String filter queries are only supported for EventFilter "
                        "(event monitored items). Use DataChangeFilter() for data-change items."
                    )
                resolved_filter = o6.EventFilter.parse(
                    filter, logger=self._subscription._client._logger
                )

            if resolved_filter is not None:
                is_event = (
                    self._item_to_monitor.attribute_id == o6.AttributeId.EVENTNOTIFIER
                )
                if is_event and isinstance(resolved_filter, o6.DataChangeFilter):
                    raise TypeError(
                        "Cannot set a DataChangeFilter on an event MonitoredItem, use EventFilter instead"
                    )
                if not is_event and isinstance(resolved_filter, o6.EventFilter):
                    raise TypeError(
                        "Cannot set an EventFilter on a data-change MonitoredItem, use DataChangeFilter instead"
                    )

            modify_request = o6.ModifyMonitoredItemsRequest()
            modify_request.subscription_id = self._subscription.subscription_id
            modify_request.timestamps_to_return = o6.TimestampsToReturn.BOTH

            item_modify = o6.MonitoredItemModifyRequest()
            item_modify.monitored_item_id = self._monitored_item_id

            params = copy.copy(self._monitoring_params)
            if sampling_interval is not None:
                params.sampling_interval = sampling_interval
            if queue_size is not None:
                params.queue_size = queue_size
            if discard_oldest is not None:
                params.discard_oldest = discard_oldest
            if resolved_filter is not None:
                params.filter = resolved_filter

            item_modify.requested_parameters = params

            modify_request.items_to_modify = [item_modify]

            response = await self._subscription._client._service_modifyMonitoredItems(
                modify_request
            )
            check_response_status(response, "Monitored item modification")

            result = response.results[0]
            check_status_code(result.status_code, "Monitored item modify result")
            self._monitoring_params.sampling_interval = result.revised_sampling_interval
            self._monitoring_params.queue_size = result.revised_queue_size
            # TODO what to do with result.filterResoult?

        return self._subscription._client._maybe_async(_modify())

    def set_monitoring_mode(self, mode: o6.MonitoringMode) -> Any:

        async def _set_mode() -> None:
            self._check_valid("set_monitoring_mode")
            assert (
                self._subscription.subscription_id is not None
            )  # _check_valid ensures non-None
            assert self._monitored_item_id is not None  # _check_valid ensures non-None

            request = o6.SetMonitoringModeRequest()
            request.subscription_id = self._subscription.subscription_id
            request.monitoring_mode = mode
            request.monitored_item_ids = [self._monitored_item_id]

            response = await self._subscription._client._service_setMonitoringMode(
                request
            )
            check_response_status(response, "Set monitoring mode")

            result = response.results[0]
            check_status_code(result, "Set monitoring mode result")
            self._monitoring_mode = mode

        return self._subscription._client._maybe_async(_set_mode())

    def set_triggering(
        self,
        links_to_add: list[MonitoredItem] | None = None,
        links_to_remove: list[MonitoredItem] | None = None,
    ) -> Any:

        async def _set_triggering() -> None:
            self._check_valid("set_triggering")
            assert (
                self._subscription.subscription_id is not None
            )  # _check_valid ensures non-None
            assert self._monitored_item_id is not None  # _check_valid ensures non-None

            request = o6.SetTriggeringRequest()
            request.subscription_id = self._subscription.subscription_id
            request.triggering_item_id = self._monitored_item_id
            if links_to_add:
                request.links_to_add = [item.monitored_item_id for item in links_to_add]  # type: ignore[misc]
            if links_to_remove:
                request.links_to_remove = [item.monitored_item_id for item in links_to_remove]  # type: ignore[misc]

            response = await self._subscription._client._service_setTriggering(request)
            check_response_status(response, "Set triggering")

            for i, result in enumerate(response.add_results):
                check_status_code(result, f"Set triggering add link [{i}]")
            for i, result in enumerate(response.remove_results):
                check_status_code(result, f"Set triggering remove link [{i}]")

        return self._subscription._client._maybe_async(_set_triggering())

    @property
    def _subscription(self) -> Subscription:
        s = self._subscription_ref()
        if s is None:
            raise RuntimeError("Subscription has been garbage-collected")
        return s

    @property
    def client(self) -> Client:
        return self._subscription._client

    @property
    def subscription(self) -> Subscription:
        return self._subscription

    @property
    def item_to_monitor(self) -> o6.ReadValueId:
        # return a copy so that
        return copy.copy(self._item_to_monitor)

    @property
    def monitoring_params(self) -> o6.MonitoringParameters:
        # return a copy so that
        return copy.copy(self._monitoring_params)

    @property
    def monitoring_mode(self) -> o6.MonitoringMode:
        return self._monitoring_mode

    @property
    def monitored_item_id(self) -> int | None:
        return self._monitored_item_id


__all__ = ["Client", "Subscription", "MonitoredItem"]
