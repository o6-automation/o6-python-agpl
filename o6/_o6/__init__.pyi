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
"""Type stubs for the _o6 C extension module."""

from __future__ import annotations

import asyncio
import builtins
import logging
from typing import Any, Callable

from o6._o6 import types

MULTITHREADING: int

class Exception(builtins.Exception): ...

class ClientConfig:
    timeout: int
    endpoint_url: str
    endpoint: types.EndpointDescription
    security_mode: int
    security_policy_uri: str
    application_uri: str
    application_description: types.ApplicationDescription
    user_identity_token: Any
    user_token_policy: types.UserTokenPolicy
    no_session: bool
    no_reconnect: bool
    no_new_session: bool
    tcp_reuse_addr: bool
    allow_none_policy_password: bool
    session_name: str
    secure_channel_life_time: int
    requested_session_timeout: int
    connectivity_check_interval: int
    outstanding_publish_requests: int
    auth_security_policy_uri: str
    max_trust_list_size: int
    max_rejected_list_size: int
    session_locale_ids: list[str]
    namespaces: list[str]
    send_buffer_size: int
    recv_buffer_size: int
    local_max_message_size: int
    local_max_chunk_count: int

    def set_username_password(self, username: str, password: str) -> None: ...
    def set_encryption(
        self,
        certificate: bytes,
        private_key: bytes,
        trust_list: list[bytes],
        revocation_list: list[bytes],
    ) -> None: ...
    def set_authentication_cert(
        self, certificate: bytes, private_key: bytes
    ) -> None: ...

class Client:
    config: ClientConfig

    def __init__(
        self,
        logger: logging.Logger | None = None,
        loop: asyncio.AbstractEventLoop | None = None,
    ) -> None: ...
    async def connect(self) -> None: ...
    async def connect_secure_channel(self) -> None: ...
    async def disconnect(self) -> None: ...
    async def disconnect_secure_channel(self) -> None: ...
    async def start_reverse_connect(self, port: int, hostnames: list[str]) -> None: ...
    def get_session_auth_token(self) -> tuple[types.NodeId, bytes]: ...
    async def activate_current_session(self) -> None: ...
    async def activate_session(
        self, auth_token: types.NodeId, server_nonce: bytes
    ) -> None: ...
    def _set_owns_loop(self, owns: bool, /) -> None: ...
    def _get_state(self) -> tuple[int, int, types.StatusCode]: ...
    def _cleanup(self) -> None: ...

    #
    # Raw service calls
    #

    # Discovery
    def _service_get_endpoints(
        self, request: types.GetEndpointsRequest
    ) -> asyncio.Future[types.GetEndpointsResponse]: ...
    def _service_find_servers(
        self, request: types.FindServersRequest
    ) -> asyncio.Future[types.FindServersResponse]: ...
    def _service_find_servers_on_network(
        self, request: types.FindServersOnNetworkRequest
    ) -> asyncio.Future[types.FindServersOnNetworkResponse]: ...

    # NodeManagement Service Set
    def _service_addNodes(
        self, request: types.AddNodesRequest
    ) -> asyncio.Future[types.AddNodesResponse]: ...
    def _service_addReferences(
        self, request: types.AddReferencesRequest
    ) -> asyncio.Future[types.AddReferencesResponse]: ...
    def _service_deleteNodes(
        self, request: types.DeleteNodesRequest
    ) -> asyncio.Future[types.DeleteNodesResponse]: ...
    def _service_deleteReferences(
        self, request: types.DeleteReferencesRequest
    ) -> asyncio.Future[types.DeleteReferencesResponse]: ...

    # View Service Set
    def _service_browse(
        self, request: types.BrowseRequest
    ) -> asyncio.Future[types.BrowseResponse]: ...
    def _service_browseNext(
        self, request: types.BrowseNextRequest
    ) -> asyncio.Future[types.BrowseNextResponse]: ...
    def _service_translateBrowsePathsToNodeIds(
        self, request: types.TranslateBrowsePathsToNodeIdsRequest
    ) -> asyncio.Future[types.TranslateBrowsePathsToNodeIdsResponse]: ...
    def _service_registerNodes(
        self, request: types.RegisterNodesRequest
    ) -> asyncio.Future[types.RegisterNodesResponse]: ...
    def _service_unregisterNodes(
        self, request: types.UnregisterNodesRequest
    ) -> asyncio.Future[types.UnregisterNodesResponse]: ...

    # Query Service Set
    def _service_queryFirst(
        self, request: types.QueryFirstRequest
    ) -> asyncio.Future[types.QueryFirstResponse]: ...
    def _service_queryNext(
        self, request: types.QueryNextRequest
    ) -> asyncio.Future[types.QueryNextResponse]: ...

    # Attribute Service Set
    def _service_read(
        self, request: types.ReadRequest
    ) -> asyncio.Future[types.ReadResponse]: ...
    def _service_historyRead(
        self, request: types.HistoryReadRequest
    ) -> asyncio.Future[types.HistoryReadResponse]: ...
    def _service_write(
        self, request: types.WriteRequest
    ) -> asyncio.Future[types.WriteResponse]: ...
    def _service_historyUpdate(
        self, request: types.HistoryUpdateRequest
    ) -> asyncio.Future[types.HistoryUpdateResponse]: ...

    # Method Service Set
    def _service_call(
        self, request: types.CallRequest
    ) -> asyncio.Future[types.CallResponse]: ...

    # MonitoredItem Service Set
    def _service_createMonitoredItems_datachange(
        self,
        request: types.CreateMonitoredItemsRequest,
        callback: Callable[[Any], Any],
    ) -> asyncio.Future[types.CreateMonitoredItemsResponse]: ...
    def _service_createMonitoredItems_event(
        self,
        request: types.CreateMonitoredItemsRequest,
        callback: Callable[[dict[str, Any]], Any],
    ) -> asyncio.Future[types.CreateMonitoredItemsResponse]: ...
    def _service_modifyMonitoredItems(
        self, request: types.ModifyMonitoredItemsRequest
    ) -> asyncio.Future[types.ModifyMonitoredItemsResponse]: ...
    def _service_setMonitoringMode(
        self, request: types.SetMonitoringModeRequest
    ) -> asyncio.Future[types.SetMonitoringModeResponse]: ...
    def _service_setTriggering(
        self, request: types.SetTriggeringRequest
    ) -> asyncio.Future[types.SetTriggeringResponse]: ...
    def _service_deleteMonitoredItems(
        self, request: types.DeleteMonitoredItemsRequest
    ) -> asyncio.Future[types.DeleteMonitoredItemsResponse]: ...

    # Subscription Service Set
    def _service_createSubscription(
        self, request: types.CreateSubscriptionRequest
    ) -> asyncio.Future[types.CreateSubscriptionResponse]: ...
    def _service_modifySubscription(
        self, request: types.ModifySubscriptionRequest
    ) -> asyncio.Future[types.ModifySubscriptionResponse]: ...
    def _service_setPublishingMode(
        self, request: types.SetPublishingModeRequest
    ) -> asyncio.Future[types.SetPublishingModeResponse]: ...
    def _service_deleteSubscriptions(
        self, request: types.DeleteSubscriptionsRequest
    ) -> asyncio.Future[types.DeleteSubscriptionsResponse]: ...

    # Timed Callbacks
    def add_timed_callback(
        self, callback: Callable[[], None], delay_ms: float
    ) -> int: ...
    def add_repeated_callback(
        self, callback: Callable[[], None], interval_ms: float
    ) -> int: ...
    def change_repeated_callback_interval(
        self, callback_id: int, interval_ms: float
    ) -> None: ...
    def remove_callback(self, callback_id: int) -> None: ...
    def get_custom_data_types(self) -> list[dict[str, Any]]: ...
    def link_custom_data_types(self, capsule: Any) -> None: ...
    def get_namespace_index(self, uri: str) -> int: ...
    def set_global_notification_callback(
        self, callback: Callable[[int, dict[str, Any]], None] | None
    ) -> None: ...
    def set_lifecycle_notification_callback(
        self, callback: Callable[[int, dict[str, Any]], None] | None
    ) -> None: ...
    def set_service_notification_callback(
        self, callback: Callable[[int, dict[str, Any]], None] | None
    ) -> None: ...
    def set_inactivity_callback(self, callback: Callable[[], None] | None) -> None: ...
    def set_subscription_inactivity_callback(
        self, callback: Callable[[int], None] | None
    ) -> None: ...

class Server:
    config: Any

    def __init__(
        self,
        *,
        port: int = 4840,
        loop: asyncio.AbstractEventLoop | None = None,
        logger: logging.Logger | None = None,
    ) -> None: ...
    @property
    def running(self) -> bool: ...
    @property
    def _is_fully_stopped(self) -> bool: ...
    def _stop_event_loop(self) -> None: ...
    def _cleanup(self) -> None: ...
    def run_startup(self) -> None: ...
    def run_shutdown(self) -> None: ...
    def run_iterate(self, wait_internal: bool = True) -> None: ...
    def add_variable_node(
        self,
        requested_id: types.NodeId,
        parent_id: types.NodeId,
        ref_type_id: types.NodeId,
        browse_name: types.QualifiedName,
        type_definition: types.NodeId,
        attributes: types.VariableAttributes,
    ) -> types.NodeId: ...
    def add_object_node(
        self,
        requested_id: types.NodeId,
        parent_id: types.NodeId,
        ref_type_id: types.NodeId,
        browse_name: types.QualifiedName,
        type_definition: types.NodeId,
        attributes: types.ObjectAttributes,
    ) -> types.NodeId: ...
    def add_object_type_node(
        self,
        requested_id: types.NodeId,
        parent_id: types.NodeId,
        ref_type_id: types.NodeId,
        browse_name: types.QualifiedName,
        attributes: types.ObjectTypeAttributes,
    ) -> types.NodeId: ...
    def add_data_type_node(
        self,
        requested_id: types.NodeId,
        parent_id: types.NodeId,
        ref_type_id: types.NodeId,
        browse_name: types.QualifiedName,
        attributes: types.DataTypeAttributes,
    ) -> types.NodeId: ...
    def add_variable_type_node(
        self,
        requested_id: types.NodeId,
        parent_id: types.NodeId,
        ref_type_id: types.NodeId,
        browse_name: types.QualifiedName,
        type_definition: types.NodeId,
        attributes: types.VariableTypeAttributes,
    ) -> types.NodeId: ...
    def add_method_node(
        self,
        requested_id: types.NodeId,
        parent_id: types.NodeId,
        ref_type_id: types.NodeId,
        browse_name: types.QualifiedName,
        attributes: types.MethodAttributes,
        callback: Callable[..., Any],
        input_arguments: list[types.Argument],
        output_arguments: list[types.Argument],
    ) -> types.NodeId: ...
    def add_reference(
        self,
        source_id: types.NodeId,
        ref_type_id: types.NodeId,
        target_id: types.NodeId,
        is_forward: bool = True,
    ) -> None: ...
    def delete_node(
        self,
        nodeid: types.NodeId,
        delete_references: bool = True,
    ) -> None: ...
    def read_value(self, nodeid: types.NodeId) -> Any: ...
    def write_value(self, nodeid: types.NodeId, value: Any) -> None: ...
    def add_reverse_connect(
        self, url: str, callback: Callable[[int, int], None] | None = None
    ) -> int: ...
    def remove_reverse_connect(self, handle: int) -> None: ...
    def link_custom_data_types(self, capsule: Any) -> None: ...
    def add_namespace(self, uri: str) -> int:
        """Register a namespace URI in the client's local namespace table and
        return its assigned index.

        If ``ns.append()`` is used to load pre-built companion specs,
        all ``ns.append()`` calls must come **before** any manual
        ``add_namespace()`` calls.  Pre-built Namespaces expect specific
        canonical indices; a manual ``add_namespace()`` beforehand would
        occupy a slot and cause ``ns.append()`` to raise ``ValueError``.

        Calling ``add_namespace()`` **after** all ``ns.append()`` calls
        is safe and simply appends at the next free index.

        .. note::
            End users should never need to call this directly —
            all namespace registration goes through
            ``client.ns.append()``.
        """
        ...

    def get_namespace_index(self, uri: str) -> int: ...
    def register_historizing(
        self,
        nodeid: types.NodeId,
        max_values: int = 100,
        max_response: int = 100,
    ) -> None: ...

def encryption_available() -> bool: ...
def build_custom_data_types(
    descriptions: list[Any],
    namespace_name: str | None = None,
    lookup_capsule: Any | None = None,
) -> tuple[Any, list[tuple[types.NodeId, type]]]: ...
def create_certificate(
    subject: list[str],
    san: list[str],
    *,
    expires_in_days: int = 365,
    key_size: int = 2048,
    fmt: str = "DER",
) -> tuple[bytes, bytes]: ...
