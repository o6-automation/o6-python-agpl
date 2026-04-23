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
from typing import Any, Awaitable, Callable, Self, TypeAlias
from types import TracebackType
import asyncio
import datetime
import logging
import weakref

from . import _o6
import o6
import o6.client_nodes as nodes
from o6 import MaybeAwaitable, AwaitReturn, Future, NodeIdLike

from pathlib import Path

class Client(_o6.Client):
    """High-level OPC UA client.

    `Client` provides two layers of access to OPC UA services.

    **Raw service layer** — the `service_*` methods accept the generated
    request types and return the full response objects, mirroring the OPC UA
    service sets (Discovery, NodeManagement, View, Attribute, Method,
    Subscription, History).  Use this layer when you need complete control over
    request parameters or when the high-level API does not cover a specific
    service variant.

    **High-level layer** — methods such as `read`, `write`, `browse`,
    `call`, `history_read`, `create_subscription`, and the node-management
    helpers encapsulate request construction, session and channel lifecycle,
    NodeId resolution, value decoding, and error handling.  Application code
    should use this layer in the normal case.

    Lifecycle
    ---------
    The client manages an asyncio event loop internally.  In synchronous code,
    high-level methods block until the request completes.  In asynchronous code,
    the same methods are awaitable — the only difference at the call site is the
    `await` keyword.  The context-manager protocol (`with` / `async with`)
    handles `connect` and `disconnect` automatically.

    Synchronous usage::

        with Client("opc.tcp://localhost:4840") as client:
            value = client.read("ns=1;s=Temperature")
            client.write("ns=1;s=SetPoint", 25.0)

    Asynchronous usage::

        async with Client("opc.tcp://localhost:4840") as client:
            value = await client.read("ns=1;s=Temperature")

    The connection state is available through the `connected`,
    `fully_connected`, and `state` properties.

    Read and write
    --------------
    `read` and `write` operate on a single NodeId or on multiple NodeIds in
    one call.  The `attributeid` parameter selects which OPC UA attribute to
    target (default: `AttributeId.VALUE`)::

        value = client.read("ns=1;s=IntegerVariable")
        client.write("ns=1;s=IntegerVariable", 42)

        values = client.read(["ns=1;s=A", "ns=1;s=B"])
        client.write({"ns=1;s=A": 1, "ns=1;s=B": 2.0})

    Browsing and node access
    ------------------------
    `browse` returns the references of a node.  Direction, reference type,
    node-class mask and result mask can all be narrowed::

        refs = client.browse("i=85")

    Convenience entry-point properties `root`, `objects`, `types`, and
    `views` return `Node` objects that support attribute-style child access
    and can be called to read or write their value::

        current_time = client.root.Objects.Server.ServerStatus.CurrentTime()

    Subscriptions
    -------------
    `create_subscription` returns a `Subscription` object.  Monitored items
    for data-change or event notifications are created from the subscription::

        sub = client.create_subscription(publishing_interval=500)
        sub.monitor("ns=1;s=Temperature", lambda item, value: print(value))

    `monitor` and `monitor_event` are also available directly on the client
    and use a default subscription created automatically on `connect`.

    Raw service API
    ---------------
    The full set of OPC UA service families is accessible:

    - Discovery: `service_find_servers`, `service_find_servers_on_network`,
      `service_get_endpoints`
    - Node management: `service_add_nodes`, `service_delete_nodes`,
      `service_add_references`, `service_delete_references`
    - View: `service_browse`, `service_browse_next`,
      `service_translate_browse_paths_to_nodeids`,
      `service_register_nodes`, `service_unregister_nodes`
    - Attributes and history: `service_read`, `service_write`,
      `service_history_read`, `service_history_update`
    - Methods: `service_call`

    Configuration
    -------------
    Security, credentials, and session parameters are set at construction time
    via keyword arguments.  Username/password authentication::

        client = Client(
            "opc.tcp://localhost:4840",
            username="user1",
            password="secret",
        )

    Certificate-based security::

        client = Client(
            "opc.tcp://localhost:4840",
            security_mode=SecurityMode.SIGN_AND_ENCRYPT,
            security_policy=SecurityPolicy.BASIC256SHA256,
            certificate="client_cert.der",
            private_key="client_key.pem",
        )
    """

    config: _o6.ClientConfig
    ns: o6.namespaces.Namespaces
    """Namespace manager for the client.

    This is the core namespace registration point for clients.  Use it to
    register pre-built custom DataType namespaces or load NodeSet2 XML files
    before the client connects.

    A client must know the namespace URI to namespace index mapping before
    opening a session, because the library uses that mapping to translate
    type and node ids correctly between Python objects and remote server
    namespace indices.

    Use pre-built namespaces when available:

        client.ns.append(o6.ns.di)

    This links the global prebuilt `o6.ns.di` namespace and reuses the
    same type objects across clients.

    For custom or external nodesets, load XML definitions first:

        client.ns.load("path/to/custom_nodeset2.xml", short_name="MyTypes")

    This parses the nodeset XML, builds Python type classes, and registers the
    namespace URI in the client's local table.

    Example:

        client = Client("opc.tcp://localhost:4840")
        client.ns.append(o6.ns.di)
        client.ns.load("nodesets/MyCustomTypes.xml", short_name="MyTypes")
        client.connect()

    After connecting, server-side namespaces that were not already loaded can
    be discovered through `client.ns.remote.discover()`.

    Important:
        All namespace registration or loading must happen before `connect()`.
        `client.ns.append()` and `client.ns.load()` are required pre-connection
        so that namespace index translation can be set up correctly.  Attempting
        to add namespaces after the session is established raises `RuntimeError`.

    Attributes:
        root (nodes.Node): The OPC UA Root folder node (i=84) and primary entry
            point for the node-style API.

            `Node` objects support attribute-style child traversal: each
            attribute access issues a `Browse` request to resolve the child by
            BrowseName, returning a new `Node`. Calling the node reads its
            value; passing a value writes it. Passing `attr=` selects a
            different OPC UA attribute:

            # Read the current server time
            current_time = client.root.Objects.Server.ServerStatus.CurrentTime()

            # Read the BrowseName attribute of a node
            name = client.root.Objects.Server(attr=o6.AttributeId.BROWSENAME)

            # Write a value
            client.root.Objects.MyDevice.SetPoint(42.0)

           Child nodes can also be accessed by subscription index (`[i=...]`,
           `[ns=1;s=Name]`) or browse-path syntax.

        objects (nodes.Node): The Objects folder node (i=85); shortcut into the
            application-level address space. See `root` for node-style API details.

        types (nodes.Node): The Types folder node (i=86); entry point for
            browsing the server's type hierarchies. See `root` for node-style API
            details.

        views (nodse.Node): The Views folder node (i=87); entry point for
            server-defined address-space views. See `root` for node-style API
            details.
    
        Important:
            `Node` objects cache their children after the first browse.
            Storing a `Node` reference and reusing it across reconnects or
            server restarts may return stale NodeIds or miss structural changes
            in the server address space.  Obtain a fresh node from `root`
            (or `objects` / `types` / `views`) after each time the server
            addresses may have changed.
        """

    # Default nodes as entry-points
    root: nodes.Node
    objects: nodes.Node
    types: nodes.Node
    views: nodes.Node

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
    ) -> None: ...
    def _maybe_async(self, aw: Awaitable[Any]) -> MaybeAwaitable[Any]: ...
    @property
    def state(self) -> tuple[int, int, o6.StatusCode]:
        """Return (channel_state, session_state, connect_status)."""
        ...

    @property
    def connected(self) -> bool:
        """Test if the client is connected; partially connected also returns True."""
        ...

    @property
    def fully_connected(self) -> bool:
        """Test if a client has both SecureChannel and Session connected."""
        ...

    def connect(
        self,
        endpoint_url: str | None = None,
    ) -> Any: ...
    def disconnect(self) -> Any: ...
    def connect_secure_channel(self, endpoint_url: str | None = None) -> Any: ...
    def disconnect_secure_channel(self) -> Any: ...
    def start_reverse_connect(
        self, port: int, hostnames: list[str] | None = None
    ) -> Any: ...
    def activate_current_session(self) -> Any: ...
    def activate_session(self, auth_token: o6.NodeId, server_nonce: bytes) -> Any: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None: ...
    async def __aenter__(self) -> Self: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None: ...

    #
    # Raw Service API
    #

    # Discovery Service Set

    def service_find_servers(
        self, request: o6.FindServersRequest
    ) -> MaybeAwaitable[o6.FindServersResponse]: ...
    def service_find_servers_on_network(
        self, request: o6.FindServersOnNetworkRequest
    ) -> MaybeAwaitable[o6.FindServersOnNetworkResponse]: ...
    def service_get_endpoints(
        self, request: o6.GetEndpointsRequest
    ) -> MaybeAwaitable[o6.GetEndpointsResponse]: ...

    # NodeManagement Service Set

    def service_add_nodes(
        self, request: o6.AddNodesRequest
    ) -> MaybeAwaitable[o6.AddNodesResponse]: ...
    def service_delete_nodes(
        self, request: o6.DeleteNodesRequest
    ) -> MaybeAwaitable[o6.DeleteNodesResponse]: ...
    def service_add_references(
        self, request: o6.AddReferencesRequest
    ) -> MaybeAwaitable[o6.AddReferencesResponse]: ...
    def service_delete_references(
        self, request: o6.DeleteReferencesRequest
    ) -> MaybeAwaitable[o6.DeleteReferencesResponse]: ...

    # View Service Set

    def service_browse(
        self, request: o6.BrowseRequest
    ) -> MaybeAwaitable[o6.BrowseResponse]: ...
    def service_browse_next(
        self, request: o6.BrowseNextRequest
    ) -> MaybeAwaitable[o6.BrowseNextResponse]: ...
    def service_translate_browse_paths_to_nodeids(
        self, request: o6.TranslateBrowsePathsToNodeIdsRequest
    ) -> MaybeAwaitable[o6.TranslateBrowsePathsToNodeIdsResponse]: ...
    def service_register_nodes(
        self, request: o6.RegisterNodesRequest
    ) -> MaybeAwaitable[o6.RegisterNodesResponse]: ...
    def service_unregister_nodes(
        self, request: o6.UnregisterNodesRequest
    ) -> MaybeAwaitable[o6.UnregisterNodesResponse]: ...

    # Attribute Service Set

    def service_read(
        self, request: o6.ReadRequest
    ) -> MaybeAwaitable[o6.ReadResponse]: ...
    def service_history_read(
        self, request: o6.HistoryReadRequest
    ) -> MaybeAwaitable[o6.HistoryReadResponse]: ...
    def service_write(
        self, request: o6.WriteRequest
    ) -> MaybeAwaitable[o6.WriteResponse]: ...
    def service_history_update(
        self, request: o6.HistoryUpdateRequest
    ) -> MaybeAwaitable[o6.HistoryUpdateResponse]: ...

    # Method Service Set

    def service_call(
        self, request: o6.CallRequest
    ) -> MaybeAwaitable[o6.CallResponse]: ...

    # DataType Utilities
    def get_remote_data_types(
        self, type_nodes: list[NodeIdLike] | None = None
    ) -> MaybeAwaitable[list[dict[str, Any]]]: ...

    # Discovery
    def get_endpoints(
        self,
        server_url: str,
        locale_ids: list[str] | None = None,
        profile_uris: list[str] | None = None,
    ) -> Any:
        """Get a list of endpoints of a server.

        Returns a list of `EndpointDescription` objects.
        """
        ...

    def find_servers(
        self,
        server_url: str,
        server_uris: list[str] | None = None,
        locale_ids: list[str] | None = None,
    ) -> Any:
        """Get a list of all registered servers at the given server.

        Returns a list of `ApplicationDescription` objects.
        """
        ...

    def find_servers_on_network(
        self,
        starting_record_id: int = 0,
        max_records_to_return: int = 0,
        server_capability_filter: list[str] | None = None,
    ) -> Any:
        """Get a list of all known servers on the network (LDS only).

        Returns a list of `ServerOnNetwork` objects.
        """
        ...

    def read(
        self,
        target: NodeIdLike | list[NodeIdLike],
        attribute_id: o6.AttributeId = ...,
        timestamps_to_return: int | None = None,
        as_datavalue: bool = False,
    ) -> Any:
        """Read one or more node attributes from the server.

        Parameters:
            target: A single node id or a list of node ids to read.
            attributeid: The attribute to read, typically `o6.AttributeId.VALUE`.
            timestamps_to_return: If provided, return the data value timestamps.
            as_datavalue: If `True`, return raw `DataValue` objects instead of
                converted Python values.

        Returns:
            The attribute value for a single target, or a list of values when a
            list of targets is provided. If `as_datavalue` is `True`, the
            returned values are the corresponding `DataValue` objects.
        """
        ...

    def write(
        self,
        target: NodeIdLike | dict[NodeIdLike, Any],
        value: Any | None = None,
        attribute_id: o6.AttributeId = ...,
    ) -> MaybeAwaitable[o6.StatusCode | list[o6.StatusCode]]:
        """Write a value to one or more nodes.

        Parameters:
            target: A node id to write, or a mapping of node ids to values for
                batch writes.
            value: The value to write when `target` is a single node id.
            attribute_id: The attribute to write, typically
                `o6.AttributeId.VALUE`.

        Returns:
            A status code for a single write, or a list of status codes for a
            batched write.
        """
        ...

    def call(
        self,
        object_id: NodeIdLike,
        method_id: NodeIdLike,
        input_args: list[Any] = ...,
    ) -> MaybeAwaitable[tuple[o6.StatusCode, ...]]:
        """Invoke a method on a node.

        Parameters:
            objectid: The object node id that owns the method.
            methodid: The method node id to invoke.
            input_args: Positional input arguments to pass to the method.

        Returns:
            A tuple of status codes for the method outputs.
        """
        ...

    def browse(
        self,
        target: NodeIdLike,
        direction: o6.BrowseDirection = ...,
        reftype: NodeIdLike = ...,
        refsubtypes: bool = True,
        nodeclass_mask: o6.NodeClass = ...,
        result_mask: o6.BrowseResultMask = ...,
    ) -> MaybeAwaitable[list[o6.ReferenceDescription]]:
        """Browse references from a node.

        Parameters:
            target: The node id to browse from.
            direction: The browse direction (forward, inverse, or both).
            reftype: A reference type to filter by, or `None` for all types.
            refsubtypes: If `True`, include subtypes of the reference type.
            nodeclass_mask: A node-class mask to filter the target nodes.
            result_mask: A browse result mask to customize returned fields.

        Returns:
            A list of `ReferenceDescription` objects describing the found
            references.
        """
        ...
    # History Access
    def history_read(
        self,
        target: NodeIdLike | list[NodeIdLike],
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        num_values_per_node: int = 0,
        return_bounds: bool = False,
        timestamps_to_return: o6.TimestampsToReturn = ...,
    ) -> Any:
        """Read raw historical values for one or more nodes.

        Parameters:
            target: A node id or list of node ids to read history from.
            start_time: The start time for the history interval.
            end_time: The end time for the history interval.
            num_values_per_node: Maximum number of values to return per node.
            return_bounds: If `True`, include boundary values at the interval edges.
            timestamps_to_return: Which timestamps to return with each value.

        Returns:
            Historical values or data values for the requested nodes.
        """
        ...

    def history_read_modified(
        self,
        target: NodeIdLike | list[NodeIdLike],
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        num_values_per_node: int = 0,
        return_bounds: bool = False,
        timestamps_to_return: o6.TimestampsToReturn = ...,
    ) -> Any:
        """Read raw modified historical values for one or more nodes.

        Parameters:
            target: A node id or list of node ids to read modified history from.
            start_time: The start time for the interval.
            end_time: The end time for the interval.
            num_values_per_node: Maximum number of values to return per node.
            return_bounds: If `True`, include boundary values.
            timestamps_to_return: Which timestamps to return with each value.

        Returns:
            Modified historical values or data values for the requested nodes.
        """
        ...

    def history_read_at_time(
        self,
        target: NodeIdLike | list[NodeIdLike],
        timestamps: list[datetime.datetime],
        use_simple_bounds: bool = False,
    ) -> Any:
        """Read historical values at specific timestamps.

        Parameters:
            target: A node id or list of node ids to read values for.
            timestamps: The timestamps at which to read historical values.
            use_simple_bounds: If `True`, use simple boundary handling.

        Returns:
            Historical values or data values at the requested timestamps.
        """
        ...

    def history_read_processed(
        self,
        target: NodeIdLike | list[NodeIdLike],
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        processing_interval: float,
        aggregate_type: NodeIdLike = ...,
    ) -> Any:
        """Read processed historical values using aggregation.

        Parameters:
            target: A node id or list of node ids to process.
            start_time: The start of the history interval.
            end_time: The end of the history interval.
            processing_interval: The interval for aggregation.
            aggregate_type: The aggregate type node id to use.

        Returns:
            Aggregated historical values or data values.
        """
        ...

    def history_update(
        self,
        target: NodeIdLike,
        values: list[o6.DataValue],
        mode: o6.PerformUpdateType = ...,
    ) -> Any:
        """Update raw historical data for a node.

        Parameters:
            target: The node id whose history is updated.
            values: The historical values to write.
            mode: The update mode describing how to apply the values.

        Returns:
            The raw result of the history update operation.
        """
        ...

    def history_delete(
        self,
        target: NodeIdLike,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
    ) -> Any:
        """Delete historical values from a node.

        Parameters:
            target: The node id whose history should be deleted.
            start_time: The start of the deletion interval.
            end_time: The end of the deletion interval.

        Returns:
            The raw result of the history delete operation.
        """
        ...
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
        """Add a generic node to the server address space.

        Parameters:
            parent_nodeid: The parent node under which the new node is added.
            browse_name: The BrowseName for the new node.
            node_class: The OPC UA node class for the new node.
            node_attributes: The node attributes object for the new node.
            requested_new_nodeid: Optionally request a specific node id.
            reference_typeid: The reference type used to link the new node.
            type_definition: The type definition node id, when applicable.

        Returns:
            The newly created node id.
        """
        ...

    def add_variable_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_attributes: o6.VariableAttributes,
        requested_new_nodeid: NodeIdLike | None = None,
        reference_type_id: NodeIdLike = ...,
        type_definition: NodeIdLike = ...,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a variable node to the server.

        Parameters:
            parent_nodeid: The parent node id for the variable.
            browse_name: The BrowseName for the variable.
            node_attributes: The variable attributes.
            requested_new_nodeid: Optionally request a specific node id.
            reference_typeid: The reference type used to link the variable.
            type_definition: The variable type definition node id.

        Returns:
            The newly created variable node id.
        """
        ...

    def add_variable_type_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_attributes: o6.VariableTypeAttributes,
        requested_new_nodeid: NodeIdLike | None = None,
        reference_type_id: NodeIdLike = ...,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a variable type node to the server.

        Parameters:
            parent_nodeid: The parent node id for the type node.
            browse_name: The BrowseName for the variable type.
            node_attributes: The variable type attributes.
            requested_new_nodeid: Optionally request a specific node id.
            reference_type_id: The reference type used to link the type node.

        Returns:
            The newly created variable type node id.
        """
        ...

    def add_object_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_attributes: o6.ObjectAttributes,
        requested_new_nodeid: NodeIdLike | None = None,
        reference_type_id: NodeIdLike = ...,
        type_definition: NodeIdLike = ...,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add an object node to the server.

        Parameters:
            parent_nodeid: The parent node id for the object.
            browse_name: The BrowseName for the object.
            node_attributes: The object attributes.
            requested_new_nodeid: Optionally request a specific node id.
            reference_typeid: The reference type used to link the object.
            type_definition: The object type definition node id.

        Returns:
            The newly created object node id.
        """
        ...

    def add_object_type_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_attributes: o6.ObjectTypeAttributes,
        requested_new_nodeid: NodeIdLike | None = None,
        reference_type_id: NodeIdLike = ...,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add an object type node to the server.

        Parameters:
            parent_nodeid: The parent node id for the type.
            browse_name: The BrowseName for the object type.
            node_attributes: The object type attributes.
            requested_new_nodeid: Optionally request a specific node id.
            reference_type_id: The reference type used to link the type node.

        Returns:
            The newly created object type node id.
        """
        ...

    def add_view_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_attributes: o6.ViewAttributes,
        requested_new_nodeid: NodeIdLike | None = None,
        reference_type_id: NodeIdLike = ...,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a view node to the server.

        Parameters:
            parent_nodeid: The parent node id for the view.
            browse_name: The BrowseName for the view.
            node_attributes: The view attributes.
            requested_new_nodeid: Optionally request a specific node id.
            reference_type_id: The reference type used to link the view.

        Returns:
            The newly created view node id.
        """
        ...

    def add_reference_type_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_attributes: o6.ReferenceTypeAttributes,
        requested_new_nodeid: NodeIdLike | None = None,
        reference_type_id: NodeIdLike = ...,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a reference type node to the server.

        Parameters:
            parent_nodeid: The parent node id for the reference type.
            browse_name: The BrowseName for the reference type.
            node_attributes: The reference type attributes.
            requested_new_nodeid: Optionally request a specific node id.
            reference_type_id: The reference type used to link the node.

        Returns:
            The newly created reference type node id.
        """
        ...

    def add_data_type_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_attributes: o6.DataTypeAttributes,
        requested_new_nodeid: NodeIdLike | None = None,
        reference_type_id: NodeIdLike = ...,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a data type node to the server.

        Parameters:
            parent_nodeid: The parent node id for the data type.
            browse_name: The BrowseName for the data type.
            node_attributes: The data type attributes.
            requested_new_nodeid: Optionally request a specific node id.
            reference_type_id: The reference type used to link the node.

        Returns:
            The newly created data type node id.
        """
        ...

    def add_method_node(
        self,
        parent_nodeid: NodeIdLike,
        browse_name: o6.QualifiedName | str,
        node_attributes: o6.MethodAttributes,
        requested_new_nodeid: NodeIdLike | None = None,
        reference_type_id: NodeIdLike = ...,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a method node to the server.

        Parameters:
            parent_nodeid: The parent node id for the method.
            browse_name: The BrowseName for the method.
            node_attributes: The method attributes.
            requested_new_nodeid: Optionally request a specific node id.
            reference_type_id: The reference type used to link the method.

        Returns:
            The newly created method node id.
        """
        ...

    def delete_node(
        self,
        nodeid: NodeIdLike | list[NodeIdLike],
        delete_target_references: bool = True,
    ) -> MaybeAwaitable[None]:
        """Delete one or more nodes from the address space.

        Parameters:
            nodeid: A single node id or list of node ids to delete.
            delete_target_references: If `True`, also delete references to the
                node targets.

        Returns:
            `None` when the deletion request is complete.
        """
        ...

    def add_reference(
        self,
        source_nodeid: NodeIdLike,
        reference_type_id: NodeIdLike,
        target_nodeid: NodeIdLike,
        is_forward: bool = True,
        target_node_class: o6.NodeClass = ...,
        target_server_uri: str = "",
    ) -> MaybeAwaitable[None]:
        """Add a reference between two nodes.

        Parameters:
            source_nodeid: The source node id for the reference.
            reference_typeid: The reference type id.
            target_nodeid: The target node id.
            is_forward: If `True`, create a forward reference.
            target_node_class: Optional target node class for the reference.
            target_server_uri: Optional server uri when referencing an external node.

        Returns:
            `None` when the reference addition is complete.
        """
        ...

    def delete_reference(
        self,
        source_nodeid: NodeIdLike,
        reference_type_id: NodeIdLike,
        target_nodeid: NodeIdLike,
        is_forward: bool = True,
        delete_bidirectional: bool = True,
    ) -> MaybeAwaitable[None]:
        """Delete a reference between two nodes.

        Parameters:
            source_nodeid: The source node id for the reference.
            reference_typeid: The reference type id.
            target_nodeid: The target node id.
            is_forward: If `True`, delete the forward reference.
            delete_bidirectional: If `True`, also delete the reverse reference.

        Returns:
            `None` when the reference deletion is complete.
        """
        ...

    def __getitem__(self, key: NodeIdLike) -> MaybeAwaitable[nodes.Node]: ...

    # Subscriptions and Monitored Items
    def create_subscription(
        self,
        req: o6.CreateSubscriptionRequest | None = None,
        publishing_interval: float = 100.0,
        lifetime_count: int = 36000,
        max_keepalive_count: int = 10,
    ) -> MaybeAwaitable[Subscription]:
        """Create a subscription to monitor data or events.

        Parameters:
            req: Optional raw create subscription request object.
            publishing_interval: The desired publishing interval in milliseconds.
            lifetime_count: The subscription lifetime count.
            max_keepalive_count: The maximum keepalive count.

        Returns:
            A `Subscription` object representing the created subscription.
        """
        ...

    def monitor(
        self,
        target: NodeIdLike | list[NodeIdLike],
        callback: MonitoredItem.DataChangeCallback | None = None,
        sampling_interval: float = 100.0,
        subscription: Subscription | None = None,
        context: Any = None,
    ) -> MaybeAwaitable[MonitoredItem | list[MonitoredItem]]:
        """Monitor data changes on one or more nodes.

        Parameters:
            target: A node id or list of node ids to monitor.
            callback: Optional callback invoked for each data change.
            sampling_interval: The requested sampling interval in milliseconds.
            subscription: Optional subscription to attach the monitored items to.
            context: Optional user context passed to the callback.

        Returns:
            A monitored item or list of monitored items created for the target nodes.
        """
        ...

    def monitor_event(
        self,
        nodeid: NodeIdLike,
        callback: MonitoredItem.EventCallback,
        event_filter: o6.EventFilter | str | None = None,
        subscription: Subscription | None = None,
        sampling_interval: float = 0.0,
        context: Any = None,
    ) -> MaybeAwaitable[MonitoredItem]:
        """Monitor events on a node.

        Parameters:
            nodeid: The node id to monitor for events.
            callback: Callback invoked for each matching event.
            event_filter: Optional event filter or filter expression.
            subscription: Optional subscription to attach the monitored item to.
            sampling_interval: The requested sampling interval.
            context: Optional user context passed to the callback.

        Returns:
            The created monitored event item.
        """
        ...

    @property
    def subscriptions(self) -> dict[int, Subscription]: ...
    @property
    def default_subscription(self) -> Subscription: ...

class Subscription:
    """Represents an OPC UA subscription for monitoring data changes."""

    def __init__(
        self,
        client: Client,
        publishing_interval: float,
        lifetime_count: int,
        max_keepalive_count: int,
        max_notifications_per_publish: int = 10,
        publishing_enabled: bool = True,
    ) -> None: ...
    def __await__(self) -> AwaitReturn[Subscription]: ...
    def __bool__(self) -> bool: ...
    def monitor(
        self,
        nodeid: NodeIdLike,
        callback: MonitoredItem.DataChangeCallback | None = None,
        sampling_interval: float = 100.0,
        context: Any = None,
    ) -> MaybeAwaitable[MonitoredItem]:
        """Create a data change monitored item on this subscription.

        Parameters:
            nodeid: The node id to monitor.
            callback: Optional callback for data change notifications.
            sampling_interval: The requested sampling interval.
            context: Optional user context passed to the callback.

        Returns:
            The created monitored item.
        """
        ...

    def monitor_event(
        self,
        nodeid: NodeIdLike,
        callback: MonitoredItem.EventCallback,
        event_filter: o6.EventFilter | str | None = None,
        sampling_interval: float = 0.0,
        context: Any = None,
    ) -> MaybeAwaitable[MonitoredItem]:
        """Create an event monitored item on this subscription.

        Parameters:
            nodeid: The node id to monitor for events.
            callback: Callback invoked for each matching event.
            event_filter: Optional event filter or filter expression.
            sampling_interval: The requested sampling interval.
            context: Optional user context passed to the callback.

        Returns:
            The created event monitored item.
        """
        ...

    def delete(self) -> Any:
        """Delete this subscription from the server.

        Returns:
            The raw result of the delete operation.
        """
        ...

    def modify(
        self,
        publishing_interval: float | None = None,
        lifetime_count: int | None = None,
        max_keepalive_count: int | None = None,
        max_notifications_per_publish: int | None = None,
        publishing_enabled: bool | None = None,
    ) -> Any:
        """Modify subscription parameters.

        Parameters:
            publishing_interval: Optional new publishing interval.
            lifetime_count: Optional new lifetime count.
            max_keepalive_count: Optional new keepalive count.
            max_notifications_per_publish: Optional maximum notifications per publish.
            publishing_enabled: Optional publishing enabled flag.

        Returns:
            The raw result of the modify operation.
        """
        ...

    @property
    def client(self) -> Client: ...
    @property
    def subscription_id(self) -> int | None: ...
    @property
    def monitored_items(self) -> dict[int, MonitoredItem]: ...
    @property
    def publishing_interval(self) -> float: ...
    @property
    def lifetime_count(self) -> int: ...
    @property
    def max_keepalive_count(self) -> int: ...
    @property
    def max_notifications_per_publish(self) -> int: ...
    @property
    def publishing_enabled(self) -> bool: ...

class MonitoredItem:
    """Represents a monitored item within a subscription."""

    context: Any

    DataChangeCallback: TypeAlias = (
        Callable[[Any], None] | Callable[[MonitoredItem, Any], None]
    )
    EventCallback: TypeAlias = (
        Callable[[dict], None] | Callable[[MonitoredItem, dict], None]
    )

    def __init__(self, subscription: Subscription) -> None: ...
    @classmethod
    def data_change(
        cls,
        subscription: Subscription,
        nodeid: NodeIdLike,
        callback: MonitoredItem.DataChangeCallback,
        attribute_id: o6.AttributeId = ...,
        index_range: str = "",
        data_encoding: o6.QualifiedName | str = "",
        sampling_interval: float = 250.0,
        context: Any = None,
    ) -> MonitoredItem:
        """Create a data change monitored item.

        Parameters:
            subscription: The subscription to attach the monitored item to.
            nodeid: The node id to monitor.
            callback: Callback invoked on data changes.
            attributeid: The attribute to monitor.
            index_range: Optional index range for array values.
            data_encoding: Optional data encoding for the monitored item.
            sampling_interval: The requested sampling interval.
            context: Optional user context passed to the callback.

        Returns:
            The created monitored item.
        """
        ...

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
        """Create an event monitored item.

        Parameters:
            subscription: The subscription to attach the monitored item to.
            nodeid: The node id to monitor for events.
            callback: Callback invoked for each matching event.
            event_filter: Optional event filter or filter expression.
            sampling_interval: The requested sampling interval.
            context: Optional user context passed to the callback.

        Returns:
            The created monitored event item.
        """
        ...

    def __await__(self) -> AwaitReturn[MonitoredItem]: ...
    def __bool__(self) -> bool: ...
    def delete(self) -> Any:
        """Delete this monitored item from its subscription.

        Returns:
            The raw result of the delete operation.
        """
        ...

    def modify(
        self,
        sampling_interval: float | None = None,
        queue_size: int | None = None,
        discard_oldest: bool | None = None,
        filter: o6.DataChangeFilter | o6.EventFilter | str | None = None,
    ) -> Any:
        """Modify monitored item parameters.

        Parameters:
            sampling_interval: Optional new sampling interval.
            queue_size: Optional new queue size.
            discard_oldest: Optional discard-oldest flag.
            filter: Optional data change or event filter.

        Returns:
            The raw result of the modify operation.
        """
        ...

    def set_monitoring_mode(self, mode: o6.MonitoringMode) -> Any:
        """Change the monitoring mode for this monitored item.

        Parameters:
            mode: The new monitoring mode.

        Returns:
            The raw result of the operation.
        """
        ...

    def set_triggering(
        self,
        links_to_add: list[MonitoredItem] | None = None,
        links_to_remove: list[MonitoredItem] | None = None,
    ) -> Any:
        """Configure triggering links for this monitored item.

        Parameters:
            links_to_add: Monitored items to add as triggered links.
            links_to_remove: Monitored items to remove from triggered links.

        Returns:
            The raw result of the operation.
        """
        ...

    @property
    def client(self) -> Client: ...
    @property
    def subscription(self) -> Subscription: ...
    @property
    def item_to_monitor(self) -> o6.ReadValueId: ...
    @property
    def monitoring_params(self) -> o6.MonitoringParameters: ...
    @property
    def monitoring_mode(self) -> o6.MonitoringMode: ...
    @property
    def monitored_item_id(self) -> int | None: ...
