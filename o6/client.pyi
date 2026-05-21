# Copyright 2026 (c) o6 Automation GmbH
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Awaitable, Callable, Self, TypeAlias, overload
from types import TracebackType
import asyncio
import datetime
import logging
import weakref

from . import _o6
import o6
from o6 import MaybeAwaitable, AwaitReturn, Future, NodeIdLike

from pathlib import Path

class Client(_o6.Client):
    """High-level OPC UA client. See the [client guide](/client/) for more details."""

    config: o6.ClientConfig
    ns: o6.namespaces.Namespaces
    """Namespace manager for the client. See the [Namespaces API](/api_reference/o6/namespaces/Namespaces/) for details.

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
    """

    # Default nodes as entry-points
    _loop: asyncio.AbstractEventLoop
    root: o6.Node
    """The OPC UA Root folder node (i=84) and primary entry point for the node-style API."""
    objects: o6.Node
    """The Objects folder node (i=85); shortcut into the application-level address space."""
    types: o6.Node
    """The Types folder node (i=86); entry point for browsing the server's type hierarchies."""
    views: o6.Node
    """The Views folder node (i=87); entry point for server-defined address-space views."""

    def __getitem__(self, key: NodeIdLike) -> MaybeAwaitable[o6.Node]:
        """Resolve a node ID to a typed [Node][o6.Node] object.

        Reads ``NodeClass`` and ``BrowseName`` from the server and returns the
        matching [Node][o6.Node] subclass (e.g. ``VariableNode``,
        ``ObjectNode``, …).

        *key* accepts anything that can be converted to a ``NodeId``:
        a string (``"ns=1;s=Temperature"``), an integer (numeric node id in
        namespace 0), or a [NodeId][o6.NodeId] instance.

        .. code-block:: python

            node = client["ns=1;s=Temperature"]        # sync
            node = await client["ns=1;s=Temperature"]  # async
        """
        ...

    def __init__(
        self,
        endpoint_url: str | None = None,
        loop: asyncio.AbstractEventLoop | None = None,
        *,
        logger: logging.Logger | None = None,
        certificate: str | Path | bytes | None = None,
        private_key: str | Path | bytes | None = None,
        trust_list: list[str | Path | bytes] | None = None,
        revocation_list: list[str | Path | bytes] | None = None,
        security_mode: int | None = None,
        security_policy: str | None = None,
        application_uri: str | None = None,
        username: str | None = None,
        password: str | None = None,
    ) -> None:
        """Create a new OPC UA client.

        The constructor accepts the most commonly needed settings as keyword
        arguments.  All remaining configuration — such as
        ``session_name``, ``requested_session_timeout``, ``session_locale_ids``,
        ``endpoint``, and any other ``ClientConfig`` property — can be set
        lazily on ``client.config`` before calling ``connect()``:

        .. code-block:: python

            client = Client("opc.tcp://localhost:4840")
            client.config.session_name = "my-session"
            client.config.requested_session_timeout = 60_000
            client.config.session_locale_ids = ["en-US"]
            client.config.endpoint = my_endpoint_description
            client.config.set_username_password("user", "secret")
            client.connect()

        Parameters:
            endpoint_url: OPC UA endpoint to connect to, e.g.
                ``"opc.tcp://localhost:4840"``.  Can also be passed to
                `connect()`.
            loop: Asyncio event loop to use.  Defaults to the running loop,
                or a newly created one if none is running.
            logger: Python logger used for all client-level log output.
                Equivalent to ``client.config.logger``.
            certificate: Client certificate as a file path (``str`` /
                ``Path``) or raw bytes (DER/PEM).
                Equivalent to ``client.config.certificate``.
            private_key: Private key matching *certificate*, as a file path
                or raw bytes.
                Equivalent to ``client.config.private_key``.
            trust_list: Trusted server certificates, each as a file path or
                raw bytes.
                Equivalent to ``client.config.trust_list``.
            revocation_list: Certificate revocation lists (CRL), each as a
                file path or raw bytes.
                Equivalent to ``client.config.revocation_list``.
            security_mode: OPC UA message security mode
                (``UA_MessageSecurityMode`` integer or
                ``o6.MessageSecurityMode`` enum).
                Equivalent to ``client.config.security_mode``.
            security_policy: URI or short name of the security policy, e.g.
                ``"Basic256Sha256"``.
                Equivalent to ``client.config.security_policy``.
            application_uri: Application URI sent in the
                ``ApplicationDescription``.
                Equivalent to ``client.config.application_uri``.
            username: Username for ``UserNameIdentityToken`` authentication.
                Equivalent to calling
                ``client.config.set_username_password(username, password)``.
            password: Password for ``UserNameIdentityToken`` authentication.
                Used together with *username*.
        """
        ...

    def _maybe_async(self, aw: Awaitable[Any]) -> MaybeAwaitable[Any]: ...
    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        """The asyncio event loop used by this client. Set at construction time, not modifiable afterwards."""
        ...

    @property
    def state(self) -> tuple[o6.SecureChannelState, o6.SessionState, o6.StatusCode]:
        """Return (channel_state, session_state, connect_status)."""
        ...

    @property
    def connected(self) -> bool:
        """Test if a client has both SecureChannel and Session connected."""
        ...

    def connect(
        self,
        no_session: bool = False,
    ) -> MaybeAwaitable[None]:
        """Connect to the server.

        Establishes a SecureChannel and, by default, a Session. Finalizes
        encryption settings (certificate / key) before connecting.

        If ``no_session`` is ``True``, only the SecureChannel is opened
        (useful for discovery or when a session will be activated manually
        later).

        Creates the default subscription.

        Starts the background worker thread.

        .. code-block:: python

            # sync
            client.connect()

            # async
            await client.connect()

        Args:
            no_session: Open only the SecureChannel, skip Session creation.
        """
        ...

    def disconnect(
        self, close_session: bool = True, delete_subscriptions: bool = True
    ) -> MaybeAwaitable[None]:
        """Disconnect from the server.

        By default closes all subscriptions, ends the Session, and closes the
        SecureChannel, then stops the background worker thread.

        Pass ``close_session=False`` to close only the SecureChannel while
        keeping the Session alive (e.g. for session transfer). In that case
        ``delete_subscriptions`` is ignored.

        Safe to call when already disconnected or when the event loop is
        closed — returns ``None`` without raising.

        .. code-block:: python

            # sync
            client.disconnect()

            # async
            await client.disconnect()

        Args:
            close_session: Close the Session (and SecureChannel). When
                ``False``, only the SecureChannel is closed.
            delete_subscriptions: Delete all active subscriptions before
                disconnecting. Ignored when ``close_session`` is ``False``.
        """
        ...

    def start_reverse_connect(
        self, port: int, hostnames: list[str] | None = None
    ) -> MaybeAwaitable[None]:
        """Listen for an incoming OPC UA reverse connection from the server.

        In the reverse-connect scenario the *server* initiates the TCP
        connection to the client.  The client opens a listen socket on
        ``port`` and waits for the server to connect.

        Close the connection with the standard [disconnect][o6.client.Client.disconnect].

        .. code-block:: python

            client.start_reverse_connect(port=4840, hostnames=["0.0.0.0"])
            # ... use client ...
            client.disconnect()

        Args:
            port: TCP port to listen on.
            hostnames: Network interfaces to advertise.  ``None`` or an
                empty list lets the stack decide (typically all interfaces).
        """
        ...

    def activate_current_session(self) -> Any:
        """Re-activate the session that is already associated with this client.

        Sends an *ActivateSession* request using the client's stored identity
        token and credentials.  Also creates the default subscription.

        Typical use — session transfer, step 2 on the *receiving* client when
        the session was originally opened by *this* client and the
        SecureChannel has been renewed or re-established:

        .. code-block:: python

            client.connect()                  # establishes session
            # ... channel re-established ...
            client.activate_current_session() # re-bind session to new channel
        """
        ...

    def activate_session(self, auth_token: o6.NodeId, server_nonce: bytes) -> Any:
        """Activate a session that was created by *another* client.

        Used for session transfer: client A's session is handed off to
        client B.  Client B must first open a SecureChannel without a session
        (``connect(no_session=True)``), then call this method with the token
        and nonce retrieved from client A via
        ``get_session_authentication_token()``.

        .. code-block:: python

            # Client A — get transfer credentials
            token, nonce = client_a.get_session_authentication_token()

            # Client B — take over the session
            client_b.connect(no_session=True)
            client_b.activate_session(token, nonce)

        Args:
            auth_token: Authentication token (``NodeId``) from the
                originating client's ``get_session_authentication_token()``.
            server_nonce: Server nonce bytes from the same call.
        """
        ...

    def __enter__(self) -> Self:
        """Enter the sync context manager; connect if not already connected.

        Calls [connect][o6.client.Client.connect] when the client is not yet connected, then
        returns ``self``.  [\_\_exit\_\_][o6.client.Client.__exit__] calls [disconnect][o6.client.Client.disconnect] if the
        client is still connected when the block ends.

        .. code-block:: python

            with Client("opc.tcp://localhost:4840") as client:
                value = client.read("ns=1;s=Temperature")
        """
        ...

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Exit the sync context manager; disconnect if still connected.

        Calls [disconnect][o6.client.Client.disconnect] when the client is still connected.
        Exceptions from the ``with`` block are not suppressed.
        See [\_\_enter\_\_][o6.client.Client.__enter__] for full usage.
        """
        ...

    async def __aenter__(self) -> Self:
        """Async counterpart of [\_\_enter\_\_][o6.client.Client.__enter__].

        Same semantics — connects if not already connected and returns
        ``self`` — but uses ``await`` internally.  [\_\_aexit\_\_][o6.client.Client.__aexit__] awaits
        [disconnect][o6.client.Client.disconnect].

        .. code-block:: python

            async with Client("opc.tcp://localhost:4840") as client:
                value = await client.read("ns=1;s=Temperature")
        """
        ...

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Exit the async context manager; disconnect if still connected.

        Awaits [disconnect][o6.client.Client.disconnect] when the client is still connected.
        Exceptions from the ``async with`` block are not suppressed.
        See [\_\_aenter\_\_][o6.client.Client.__aenter__] for full usage.
        """
        ...
    #
    # Raw Service API
    #

    # Discovery Service Set

    def service_find_servers(
        self, request: o6.FindServersRequest
    ) -> MaybeAwaitable[o6.FindServersResponse]:
        """Raw *FindServers* service call — discover servers known to a discovery server.

        [OPC UA Part 4 §5.5.2](https://reference.opcfoundation.org/specs/OPC-10000-4/5.5.2)
        """
        ...

    def service_find_servers_on_network(
        self, request: o6.FindServersOnNetworkRequest
    ) -> MaybeAwaitable[o6.FindServersOnNetworkResponse]:
        """Raw *FindServersOnNetwork* service call — enumerate servers registered via mDNS/LDS.

        [OPC UA Part 4 §5.5.3](https://reference.opcfoundation.org/specs/OPC-10000-4/5.5.3)
        """
        ...

    def service_get_endpoints(
        self, request: o6.GetEndpointsRequest
    ) -> MaybeAwaitable[o6.GetEndpointsResponse]:
        """Raw *GetEndpoints* service call — retrieve the endpoint descriptions of a server.

        [OPC UA Part 4 §5.5.4](https://reference.opcfoundation.org/specs/OPC-10000-4/5.5.4)
        """
        ...
    # NodeManagement Service Set

    def service_add_nodes(
        self, request: o6.AddNodesRequest
    ) -> MaybeAwaitable[o6.AddNodesResponse]:
        """Raw *AddNodes* service call — add one or more nodes to the address space.

        [OPC UA Part 4 §5.8.2](https://reference.opcfoundation.org/specs/OPC-10000-4/5.8.2)
        """
        ...

    def service_delete_nodes(
        self, request: o6.DeleteNodesRequest
    ) -> MaybeAwaitable[o6.DeleteNodesResponse]:
        """Raw *DeleteNodes* service call — remove one or more nodes from the address space.

        [OPC UA Part 4 §5.8.4](https://reference.opcfoundation.org/specs/OPC-10000-4/5.8.4)
        """
        ...

    def service_add_references(
        self, request: o6.AddReferencesRequest
    ) -> MaybeAwaitable[o6.AddReferencesResponse]:
        """Raw *AddReferences* service call — add references between nodes.

        [OPC UA Part 4 §5.8.3](https://reference.opcfoundation.org/specs/OPC-10000-4/5.8.3)
        """
        ...

    def service_delete_references(
        self, request: o6.DeleteReferencesRequest
    ) -> MaybeAwaitable[o6.DeleteReferencesResponse]:
        """Raw *DeleteReferences* service call — remove references between nodes.

        [OPC UA Part 4 §5.8.5](https://reference.opcfoundation.org/specs/OPC-10000-4/5.8.5)
        """
        ...
    # View Service Set

    def service_browse(
        self, request: o6.BrowseRequest
    ) -> MaybeAwaitable[o6.BrowseResponse]:
        """Raw *Browse* service call — navigate the address space from one or more start nodes.

        Returns references according to the ``BrowseDescription`` filter in the
        request.  Use [service_browse_next][o6.client.Client.service_browse_next] to continue if the response
        indicates more results are available.

        [OPC UA Part 4 §5.9.2](https://reference.opcfoundation.org/specs/OPC-10000-4/5.9.2)
        """
        ...

    def service_browse_next(
        self, request: o6.BrowseNextRequest
    ) -> MaybeAwaitable[o6.BrowseNextResponse]:
        """Raw *BrowseNext* service call — continue a Browse that returned a continuation point.

        [OPC UA Part 4 §5.9.3](https://reference.opcfoundation.org/specs/OPC-10000-4/5.9.3)
        """
        ...

    def service_translate_browse_paths_to_nodeids(
        self, request: o6.TranslateBrowsePathsToNodeIdsRequest
    ) -> MaybeAwaitable[o6.TranslateBrowsePathsToNodeIdsResponse]:
        """Raw *TranslateBrowsePathsToNodeIds* service call — resolve browse paths to NodeIds.

        [OPC UA Part 4 §5.9.4](https://reference.opcfoundation.org/specs/OPC-10000-4/5.9.4)
        """
        ...

    def service_register_nodes(
        self, request: o6.RegisterNodesRequest
    ) -> MaybeAwaitable[o6.RegisterNodesResponse]:
        """Raw *RegisterNodes* service call — obtain optimised NodeIds for repeated access.

        [OPC UA Part 4 §5.9.5](https://reference.opcfoundation.org/specs/OPC-10000-4/5.9.5)
        """
        ...

    def service_unregister_nodes(
        self, request: o6.UnregisterNodesRequest
    ) -> MaybeAwaitable[o6.UnregisterNodesResponse]:
        """Raw *UnregisterNodes* service call — release NodeIds obtained via *RegisterNodes*.

        [OPC UA Part 4 §5.9.6](https://reference.opcfoundation.org/specs/OPC-10000-4/5.9.6)
        """
        ...
    # Attribute Service Set

    def service_read(self, request: o6.ReadRequest) -> MaybeAwaitable[o6.ReadResponse]:
        """Raw *Read* service call — read one or more node attributes.

        [OPC UA Part 4 §5.11.2](https://reference.opcfoundation.org/specs/OPC-10000-4/5.11.2)
        """
        ...

    def service_history_read(
        self, request: o6.HistoryReadRequest
    ) -> MaybeAwaitable[o6.HistoryReadResponse]:
        """Raw *HistoryRead* service call — read historical values or events from nodes.

        [OPC UA Part 4 §5.11.3](https://reference.opcfoundation.org/specs/OPC-10000-4/5.11.3)
        """
        ...

    def service_write(
        self, request: o6.WriteRequest
    ) -> MaybeAwaitable[o6.WriteResponse]:
        """Raw *Write* service call — write one or more node attribute values.

        [OPC UA Part 4 §5.11.4](https://reference.opcfoundation.org/specs/OPC-10000-4/5.11.4)
        """
        ...

    def service_history_update(
        self, request: o6.HistoryUpdateRequest
    ) -> MaybeAwaitable[o6.HistoryUpdateResponse]:
        """Raw *HistoryUpdate* service call — insert, replace, or delete historical data.

        [OPC UA Part 4 §5.11.5](https://reference.opcfoundation.org/specs/OPC-10000-4/5.11.5)
        """
        ...
    # Method Service Set

    def service_call(self, request: o6.CallRequest) -> MaybeAwaitable[o6.CallResponse]:
        """Raw *Call* service call — invoke one or more OPC UA methods.

        [OPC UA Part 4 §5.12.2](https://reference.opcfoundation.org/specs/OPC-10000-4/5.12.2)
        """
        ...
    #
    # Utilities
    #

    def get_remote_data_types(
        self, type_nodes: list[NodeIdLike] | None = None
    ) -> MaybeAwaitable[list[dict[str, Any]]]:
        """Read custom ``StructureDefinition`` data types from the server.

        Browses the server's DataType hierarchy (rooted at ``Structure``,
        NodeId ``i=22``) and reads the ``DataTypeDefinition`` and
        ``BrowseName`` attributes for every discovered node.  Only nodes that
        carry a ``StructureDefinition`` (structs, structs-with-optional-fields,
        and unions) are included in the result.

        Pass ``type_nodes`` to restrict the query to a specific set of DataType
        NodeIds instead of walking the full hierarchy.  Passing an empty list
        returns ``[]`` immediately without contacting the server.

        Each entry in the returned list is a ``dict`` with the following keys:

        - ``type_name`` (``str``) — ``BrowseName.name`` of the DataType node.
        - ``type_id`` (``NodeId``) — NodeId of the DataType node.
        - ``binary_encoding_id`` (``NodeId``) — default binary encoding NodeId
          (``StructureDefinition.defaultEncodingId``).
        - ``type_kind`` (``DataTypeKind``) — ``Structure``, ``OptStruct``
          (structure with optional fields), or ``Union``.
        - ``members_size`` (``int``) — number of fields in the structure.

        The result can be passed directly to
        [register_data_types][o6.register_data_types] to enable encoding/decoding of these
        types on the client.

        Args:
            type_nodes: Explicit DataType NodeIds to query.  ``None`` (default)
                walks the full ``Structure`` subtype hierarchy.
        """
        ...
    #
    # Discovery
    #

    def get_endpoints(
        self,
        endpoint_url: str,
        *,
        locale_ids: list[str] | None = None,
        profile_uris: list[str] | None = None,
    ) -> MaybeAwaitable[list[o6.EndpointDescription]]:
        """Return the endpoints advertised by a server.

        Sends a *GetEndpoints* request to ``endpoint_url``.  No active session
        is required — connect with ``connect(no_session=True)`` first if the
        client is not yet connected.

        Each [EndpointDescription][o6.EndpointDescription] in the result describes one
        available endpoint and includes the endpoint URL, security mode,
        security policy URI, transport profile URI, server certificate, and
        the list of supported [UserTokenPolicy][o6.UserTokenPolicy] entries.

            client.connect(no_session=True)
            endpoints = client.get_endpoints("opc.tcp://localhost:4840")
            for ep in endpoints:
                print(ep.endpoint_url, ep.security_mode, ep.security_policy_uri)

        Args:
            endpoint_url: URL of the server to query, e.g.
                ``"opc.tcp://localhost:4840"``.
            locale_ids: Preferred locales for localised strings in the
                response (e.g. ``["en-US", "de-DE"]``).  ``None`` returns
                the server's default locale.
            profile_uris: Restrict the result to endpoints that match one of
                these transport profile URIs.  ``None`` returns all endpoints.
        """
        ...

    def find_servers(
        self,
        endpoint_url: str,
        *,
        locale_ids: list[str] | None = None,
        server_uris: list[str] | None = None,
    ) -> MaybeAwaitable[list[o6.ApplicationDescription]]:
        """Return servers registered at a discovery server or known to a server.

        Sends a *FindServers* request to ``endpoint_url``.  Typically called
        against a Local Discovery Server (LDS) at
        ``"opc.tcp://localhost:4840"`` to enumerate all servers registered on
        the host, or against any server to retrieve its own
        [ApplicationDescription][o6.ApplicationDescription].

        No active session is required — ``connect(no_session=True)`` is
        sufficient.

        Each [ApplicationDescription][o6.ApplicationDescription] in the result contains the
        application name, application URI, application type, product URI, and
        a list of discovery URLs that can be passed to
        `get_endpoints`.

        .. code-block:: python

            client.connect(no_session=True)
            servers = client.find_servers("opc.tcp://localhost:4840")
            for srv in servers:
                print(srv.application_uri, srv.discovery_urls)

        Args:
            endpoint_url: URL of the discovery server or server to query.
            locale_ids: Preferred locales for the
                ``ApplicationDescription.application_name`` field.  ``None``
                uses the server's default locale.
            server_uris: Restrict the result to servers whose
                ``applicationUri`` matches one of these strings.  ``None``
                returns all known servers.
        """
        ...

    def find_servers_on_network(
        self,
        *,
        starting_record_id: int = 0,
        max_records_to_return: int = 0,
        server_capability_filter: list[str] | None = None,
    ) -> MaybeAwaitable[list[o6.ServerOnNetwork]]:
        """Return servers visible on the network via a Local Discovery Server (LDS).

        Sends a *FindServersOnNetwork* request to the connected LDS.  The LDS
        maintains a registry of servers that have announced themselves via
        mDNS or the *RegisterServer2* service.  This call is only meaningful
        when connected to an LDS; a regular OPC UA server will return an
        empty list or an error.

        The result is paginated: use ``starting_record_id`` and
        ``max_records_to_return`` to page through large registries.  The
        ``record_id`` field on each [ServerOnNetwork][o6.ServerOnNetwork] entry can
        be used as the ``starting_record_id`` for the next page.

        Each [ServerOnNetwork][o6.ServerOnNetwork] entry contains the server name,
        discovery URL, and a list of capability strings (e.g. ``"DA"`` for
        Data Access, ``"HE"`` for Historical Events).

        .. code-block:: python

            # Fetch the first 100 servers that support Data Access
            servers = client.find_servers_on_network(
                max_records_to_return=100,
                server_capability_filter=["DA"],
            )

        Args:
            starting_record_id: Record ID to start from for pagination.
                ``0`` starts from the beginning of the registry.
            max_records_to_return: Maximum number of entries to return.
                ``0`` lets the server decide (typically returns all entries).
            server_capability_filter: Restrict the result to servers that
                advertise all of the given capability strings.  ``None``
                returns servers regardless of capabilities.
        """
        ...
    #
    # Attribute Service Set
    #

    @overload
    def read(
        self,
        target: NodeIdLike,
        *,
        attr: o6.AttributeId | str = o6.AttributeId.VALUE,
        timestamps_to_return: o6.TimestampsToReturn | None = None,
        value_only: bool = True,
        range: str | None = None,
    ) -> Any:
        """Read a single node attribute from the server.

        Parameters:
            target: A single node id to read.
            attr: The attribute to read, typically `o6.AttributeId.VALUE`.
                Can also be an attribute name as string, such as 'browsename'.
            timestamps_to_return: If provided, return the data value timestamps.
            value_only: If `True`, return only the data value (default). If `False`, return the raw `DataValue` object.
            range: An optional range string for array attributes, e.g. "1:10"

        Returns:
            The attribute value for the target node. If `value_only` is `False`,
            returns the corresponding `DataValue` object.
        """
        ...

    @overload
    def read(
        self,
        target: list[NodeIdLike],
        *,
        attr: o6.AttributeId | str = o6.AttributeId.VALUE,
        timestamps_to_return: o6.TimestampsToReturn | None = None,
        value_only: bool = True,
        range: str | list[str] | None = None,
    ) -> list[Any]:
        """Read multiple node attributes from the server in a single batch.

        Parameters:
            target: A list of node ids to read.
            attr: The attribute to read, typically `o6.AttributeId.VALUE`.
                Can also be an attribute name as string, such as 'browsename'.
            timestamps_to_return: If provided, return the data value timestamps.
            value_only: If `True`, return only the data values (default). If `False`, return the raw `DataValue` objects.
            range: An optional list of range strings for array attributes, one per target node, e.g. ["1:10", "0:5"]
                Or a single range string to apply to all nodes


        Returns:
            A list of attribute values, one per target node. If `value_only` is
            `False`, the list contains the corresponding `DataValue` objects.
        """
        ...

    @overload
    def write(
        self,
        target: NodeIdLike,
        value: Any,
        *,
        attr: o6.AttributeId | str = o6.AttributeId.VALUE,
        range: str | None = None,
    ) -> MaybeAwaitable[o6.StatusCode]:
        """Write a value to a single node.

        Parameters:
            target: A single node id to write.
            value: The value to write. Can be a Python value (it will be
                wrapped in a `DataValue`) or an already-built `DataValue`.
            attr: The attribute to write, typically `o6.AttributeId.VALUE`.
                Can also be an attribute name as string, such as 'browsename'.
            range: An optional OPC UA NumericRange string for array
                attributes, e.g. ``"0"`` or ``"1:3"``.

        Returns:
            The `StatusCode` returned by the server for this write.
        """
        ...

    @overload
    def write(
        self,
        target: list[NodeIdLike],
        value: list[Any],
        *,
        attr: o6.AttributeId | str = o6.AttributeId.VALUE,
        range: str | list[str] | None = None,
    ) -> MaybeAwaitable[list[o6.StatusCode]]:
        """Write values to multiple nodes in a single batched request.

        Parameters:
            target: A list of node ids to write.
            value: A list of values to write, one per target node and in the
                same order. Must have the same length as `target`.
            attr: The attribute to write, typically `o6.AttributeId.VALUE`.
                Can also be an attribute name as string, such as 'browsename'.
            range: An optional OPC UA NumericRange. Pass a single string to
                broadcast the same range to every node, or a list of strings
                (one per target node, in the same order) for per-node ranges.

        Returns:
            A list of `StatusCode` values, one per target node.
        """
        ...

    @overload
    def write(
        self,
        target: dict[NodeIdLike, Any],
        *,
        attr: o6.AttributeId | str = o6.AttributeId.VALUE,
    ) -> MaybeAwaitable[list[o6.StatusCode]]:
        """Write values to multiple nodes given as a `{node: value}` mapping.

        Parameters:
            target: A mapping of node ids to the values to write.
            attr: The attribute to write, typically `o6.AttributeId.VALUE`.
                Can also be an attribute name as string, such as 'browsename'.

        Returns:
            A list of `StatusCode` values, one per entry in `target`, in the
            mapping's iteration order.

        Note:
            The `range` argument is not supported for this form — use the
            list form (`target=[...], value=[...], range=...`) if per-node
            ranges are needed.
        """
        ...

    def call(
        self,
        object: NodeIdLike,
        method: NodeIdLike,
        args: list[Any] = ...,
    ) -> MaybeAwaitable[tuple[o6.StatusCode, ...]]:
        """Invoke a method on a node.

        Parameters:
            object_id: The object node id that owns the method.
            method_id: The method node id to invoke.
            input_args: Positional input arguments to pass to the method.

        Returns:
            A tuple of status codes for the method outputs.
        """
        ...

    def browse(
        self,
        target: NodeIdLike,
        *,
        direction: o6.BrowseDirection = ...,
        reftype: NodeIdLike = ...,
        refsubtypes: bool = True,
        nodeclass_mask: o6.NodeClass = ...,
        result_mask: o6.BrowseResultMask = ...,
    ) -> MaybeAwaitable[list[o6.ReferenceDescription]]:
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
            nodeclass_mask: A node-class mask to filter the target nodes.
            result_mask: A browse result mask to customize returned fields.

        Returns:
            A list of `ReferenceDescription` objects describing the found
            references.
        """
        ...
    #
    # History Access
    #

    def history_read(
        self,
        target: NodeIdLike | list[NodeIdLike],
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
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

    def history_update_insert(
        self,
        target: NodeIdLike,
        values: list[o6.DataValue],
    ) -> Any:
        """Insert new historical values into a node's history.

        Insertion fails for any timestamp that already has a value stored.
        Use `history_update_replace` to overwrite existing entries.

        Parameters:
            target: The node id whose history is being updated.
            values: The historical values to insert.

        Returns:
            The raw result of the history update operation.
        """
        ...

    def history_update_replace(
        self,
        target: NodeIdLike,
        values: list[o6.DataValue],
    ) -> Any:
        """Replace existing historical values for a node.

        Replacement requires that a value already exists at each provided
        timestamp. Use `history_update_insert` to add new entries.

        Parameters:
            target: The node id whose history is being updated.
            values: The historical values to replace existing entries with.

        Returns:
            The raw result of the history update operation.
        """
        ...

    def history_update_delete(
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
    #
    # Node management
    #

    def _add_node(
        self,
        *,
        parent: NodeIdLike,
        parent_reference: NodeIdLike,
        nodeclass: o6.NodeClass,
        browsename: o6.QualifiedName | str,
        requested_nodeid: NodeIdLike | None,
        attributes: Any,
        type_definition: NodeIdLike | None = None,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a generic node to the server address space.

        Parameters:
            parent: The parent node under which the new node is added.
            browsename: The BrowseName for the new node.
            nodeclass: The OPC UA node class for the new node.
            attributes: The node attributes object for the new node.
            requested_nodeid: Optionally request a specific node id.
            parent_reference: The reference type used to link the new node.
            type_definition: The type definition node id, when applicable.

        Returns:
            The newly created node id.
        """
        ...

    def add_variable_node(
        self,
        *,
        parent: NodeIdLike,
        parent_reference: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.Aggregates.HasComponent,
        browsename: o6.QualifiedName | str,
        requested_nodeid: NodeIdLike | None = None,
        attributes: o6.VariableAttributes | None,
        type_definition: NodeIdLike = o6.ns.ns0.vartypes.BaseVariableType.BaseDataVariableType,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a variable node to the server.

        Parameters:
            parent: The parent node id for the variable.
            browsename: The BrowseName for the variable.
            attributes: The variable attributes.
            requested_nodeid: Optionally request a specific node id.
            parent_reference: The reference type used to link the variable.
            type_definition: The variable type definition node id.

        Returns:
            The newly created variable node id.
        """
        ...

    def add_variable_type_node(
        self,
        *,
        parent: NodeIdLike,
        parent_reference: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.HasSubtype,
        browsename: o6.QualifiedName | str,
        requested_nodeid: NodeIdLike | None = None,
        attributes: o6.VariableTypeAttributes,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a variable type node to the server.

        Parameters:
            parent: The parent node id for the type node.
            browsename: The BrowseName for the variable type.
            attributes: The variable type attributes.
            requested_nodeid: Optionally request a specific node id.
            parent_reference: The reference type used to link the type node.

        Returns:
            The newly created variable type node id.
        """
        ...

    def add_object_node(
        self,
        *,
        parent: NodeIdLike,
        parent_reference: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.Aggregates.HasComponent,
        browsename: o6.QualifiedName | str,
        requested_nodeid: NodeIdLike | None = None,
        attributes: o6.ObjectAttributes,
        type_definition: NodeIdLike = o6.ns.ns0.objtypes.BaseObjectType,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add an object node to the server.

        Parameters:
            parent: The parent node id for the object.
            browsename: The BrowseName for the object.
            attributes: The object attributes.
            requested_nodeid: Optionally request a specific node id.
            parent_reference: The reference type used to link the object.
            type_definition: The object type definition node id.

        Returns:
            The newly created object node id.
        """
        ...

    def add_object_type_node(
        self,
        *,
        parent: NodeIdLike,
        parent_reference: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.HasSubtype,
        browsename: o6.QualifiedName | str,
        requested_nodeid: NodeIdLike | None = None,
        attributes: o6.ObjectTypeAttributes,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add an object type node to the server.

        Parameters:
            parent: The parent node id for the type.
            browsename: The BrowseName for the object type.
            attributes: The object type attributes.
            requested_nodeid: Optionally request a specific node id.
            parent_reference: The reference type used to link the type node.

        Returns:
            The newly created object type node id.
        """
        ...

    def add_view_node(
        self,
        *,
        parent: NodeIdLike,
        parent_reference: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.Aggregates.HasComponent,
        browsename: o6.QualifiedName | str,
        requested_nodeid: NodeIdLike | None = None,
        attributes: o6.ViewAttributes,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a view node to the server.

        Parameters:
            parent: The parent node id for the view.
            browsename: The BrowseName for the view.
            attributes: The view attributes.
            requested_nodeid: Optionally request a specific node id.
            parent_reference: The reference type used to link the view.

        Returns:
            The newly created view node id.
        """
        ...

    def add_reference_type_node(
        self,
        *,
        parent: NodeIdLike,
        parent_reference: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.HasSubtype,
        browsename: o6.QualifiedName | str,
        requested_nodeid: NodeIdLike | None = None,
        attributes: o6.ReferenceTypeAttributes,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a reference type node to the server.

        Parameters:
            parent: The parent node id for the reference type.
            browsename: The BrowseName for the reference type.
            attributes: The reference type attributes.
            requested_nodeid: Optionally request a specific node id.
            parent_reference: The reference type used to link the node.

        Returns:
            The newly created reference type node id.
        """
        ...

    def add_data_type_node(
        self,
        *,
        parent: NodeIdLike,
        parent_reference: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.HasSubtype,
        browsename: o6.QualifiedName | str,
        requested_nodeid: NodeIdLike | None = None,
        attributes: o6.DataTypeAttributes,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a data type node to the server.

        Parameters:
            parent: The parent node id for the data type.
            browsename: The BrowseName for the data type.
            attributes: The data type attributes.
            requested_nodeid: Optionally request a specific node id.
            parent_reference: The reference type used to link the node.

        Returns:
            The newly created data type node id.
        """
        ...

    def add_method_node(
        self,
        *,
        parent: NodeIdLike,
        parent_reference: NodeIdLike = o6.ns.ns0.reftypes.References.HierarchicalReferences.HasChild.Aggregates.HasComponent,
        browsename: o6.QualifiedName | str,
        requested_nodeid: NodeIdLike | None = None,
        attributes: o6.MethodAttributes,
    ) -> MaybeAwaitable[o6.NodeId]:
        """Add a method node to the server.

        Parameters:
            parent: The parent node id for the method.
            browsename: The BrowseName for the method.
            attributes: The method attributes.
            requested_nodeid: Optionally request a specific node id.
            parent_reference: The reference type used to link the method.

        Returns:
            The newly created method node id.
        """
        ...

    def delete_node(
        self,
        nodeid: NodeIdLike | list[NodeIdLike],
        delete_target_references: bool = True,
    ) -> MaybeAwaitable[o6.StatusCode]:
        """Delete one or more nodes from the address space.

        Parameters:
            nodeid: A single node id or list of node ids to delete.
            delete_target_references: If `True`, also delete references to the
                node targets.

        Returns:
            The first non-Good `StatusCode` from the per-node results, or
            `StatusCode.Good` if all deletions succeeded.
        """
        ...

    def add_reference(
        self,
        source: NodeIdLike,
        reftype: NodeIdLike,
        target: NodeIdLike | o6.ExpandedNodeId,
        forward: bool = True,
        target_nodeclass: o6.NodeClass = ...,
        target_server_uri: str = "",
    ) -> MaybeAwaitable[o6.StatusCode]:
        """Add a reference between two nodes.

        Parameters:
            source: The source node id for the reference.
            reftype: The reference type id.
            target: The target node id.
            forward: If `True`, create a forward reference.
            target_nodeclass: Optional target node class for the reference.
            target_server_uri: Optional server uri when referencing an external node.

        Returns:
            The `StatusCode` returned by the server for this reference.
        """
        ...

    def delete_reference(
        self,
        source: NodeIdLike,
        reftype: NodeIdLike,
        target: NodeIdLike,
        forward: bool = True,
        delete_bidirectional: bool = True,
    ) -> MaybeAwaitable[o6.StatusCode]:
        """Delete a reference between two nodes.

        Parameters:
            source: The source node id for the reference.
            reftype: The reference type id.
            target: The target node id.
            forward: If `True`, delete the forward reference.
            delete_bidirectional: If `True`, also delete the reverse reference.

        Returns:
            The `StatusCode` returned by the server for this deletion.
        """
        ...
    #
    # Subscriptions and Monitored Items
    #

    def create_subscription(
        self,
        publishing_interval: float = 100.0,
        lifetime_count: int = 36000,
        max_keepalive_count: int = 10,
        max_notifications_per_publish: int = 10,
        publishing_enabled: bool = True,
        *,
        on_created: (
            Callable[[Subscription, o6.CreateSubscriptionResponse], None] | None
        ) = None,
        on_status_change: (
            Callable[[Subscription, o6.StatusChangeNotification], None] | None
        ) = None,
        on_deleted: Callable[[Subscription], None] | None = None,
    ) -> MaybeAwaitable[Subscription]:
        """Create a subscription to monitor data or events.

        Parameters:
            req: Optional raw create subscription request object.
            publishing_interval: The desired publishing interval in milliseconds.
            lifetime_count: The subscription lifetime count.
            max_keepalive_count: The maximum keepalive count.
            max_notifications_per_publish: The maximum number of notifications per publish.
            publishing_enabled: Whether the subscription is initially enabled.
            on_created: Optional callback invoked with `(subscription, response)`
                once the server has acknowledged subscription creation.
            on_status_change: Optional callback invoked with
                `(subscription, notification)` when the server publishes a
                `StatusChangeNotification` for this subscription.
            on_deleted: Optional callback invoked with `(subscription,)` when
                the subscription is destroyed — explicitly via `delete()`, or
                implicitly on session close / disconnect.

        Returns:
            A `Subscription` object representing the created subscription.
        """
        ...

    def monitor(
        self,
        target: NodeIdLike | o6.ReadValueId | list[NodeIdLike | o6.ReadValueId],
        callback: MonitoredItem.DataChangeCallback | None = None,
        sampling_interval: float = 100.0,
        *,
        value_only: bool = True,
        subscription: Subscription | None = None,
        filter: o6.DataChangeFilter | None = None,
        monitoring_mode: o6.MonitoringMode = ...,
        queue_size: int = 1,
        discard_oldest: bool = True,
        on_created: MonitoredItem.CreatedCallback | None = None,
        on_deleted: MonitoredItem.DeletedCallback | None = None,
    ) -> MaybeAwaitable[MonitoredItem | list[MonitoredItem]]:
        """Monitor data changes on one or more nodes.

        Parameters:
            target: A node id, [ReadValueId][o6.ReadValueId], or list thereof to monitor.
            callback: Optional callback invoked for each data change. If ``None``,
                a default callback that prints ``MonitoredItem {id}: {value}`` to
                stdout is used.
            sampling_interval: The requested sampling interval in milliseconds.
            value_only: If ``True`` (default), the callback receives the unwrapped
                value. If ``False``, it receives the full [DataValue][o6.DataValue].
            subscription: Optional subscription to attach the monitored items to.
                If ``None`` (default), the clients' default subscription is used.
            filter: Optional [DataChangeFilter][o6.DataChangeFilter] to control triggering.
            monitoring_mode: Monitoring mode for the item (default: ``REPORTING``).
            queue_size: Requested queue size (default: ``1``).
            discard_oldest: Whether to discard the oldest entry when the queue is
                full (default: ``True``).
            on_created: Optional lifecycle callback; see `MonitoredItem._data_change`.
            on_deleted: Optional lifecycle callback; see `MonitoredItem._data_change`.

        Returns:
            A monitored item or list of monitored items created for the target nodes.
        """
        ...

    def monitor_event(
        self,
        nodeid: NodeIdLike,
        callback: MonitoredItem.EventCallback,
        filter: o6.EventFilter | str | None = None,
        *,
        subscription: Subscription | None = None,
        monitoring_mode: o6.MonitoringMode = ...,
        queue_size: int = 100,
        discard_oldest: bool = True,
        on_created: MonitoredItem.CreatedCallback | None = None,
        on_deleted: MonitoredItem.DeletedCallback | None = None,
    ) -> MaybeAwaitable[MonitoredItem]:
        """Monitor events on a node.

        Parameters:
            nodeid: The node id to monitor for events.
            callback: Callback invoked for each matching event.
            filter: Optional event filter or filter expression string. If ``None``,
                a default filter selecting ``EventId``, ``EventType``,
                ``SourceName``, ``Time``, ``Message``, and ``Severity`` is used.
            subscription: Optional subscription to attach the monitored item to.
                Defaults to :attr:`default_subscription`.
            monitoring_mode: Monitoring mode for the item (default: ``REPORTING``).
            queue_size: Requested queue size (default: ``100``).
            discard_oldest: Whether to discard the oldest entry when the queue is
                full (default: ``True``).
            on_created: Optional lifecycle callback; see `MonitoredItem._event`.
            on_deleted: Optional lifecycle callback; see `MonitoredItem._event`.

        Returns:
            The created monitored event item.
        """
        ...

    @property
    def subscriptions(self) -> list[Subscription]: ...
    """The list of active subscriptions for this client."""

    @property
    def default_subscription(self) -> Subscription: ...
    """Gets the clients' default subscription.
    Throws RuntimeError when accessed, in a not connected state.
    """

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
    def __await__(self) -> AwaitReturn[Subscription]:
        """Allow ``await Subscription(...)`` to work.

        Creating a subscription requires a server round-trip, but ``__init__``
        cannot be async. The round-trip is therefore started in ``__init__`` and
        awaited here, so callers can write ``sub = await Subscription(...)`` and
        be sure the subscription is fully set up before proceeding.
        """
        ...

    def __bool__(self) -> bool:
        """Check if this is a valid subscription.

        A deleted subscription evaluates to ``False``. ``delete()`` cleans up
        the subscription on the server and client side, but cannot interfere
        with garbage collection of the Python object itself. Garbage collecting
        a ``delete``d subscription is a noop in terms of state cleanup, but
        until then ``__bool__`` indicates that the subscription is invalid.
        """
        ...

    def _monitor(
        self,
        nodeid: NodeIdLike | o6.ReadValueId,
        callback: MonitoredItem.DataChangeCallback | None = None,
        sampling_interval: float = 100.0,
        on_created: MonitoredItem.CreatedCallback | None = None,
        on_deleted: MonitoredItem.DeletedCallback | None = None,
        *,
        value_only: bool = True,
        filter: o6.DataChangeFilter | None = None,
        monitoring_mode: o6.MonitoringMode = ...,
        queue_size: int = 1,
        discard_oldest: bool = True,
    ) -> MaybeAwaitable[MonitoredItem]:
        """Create a data change monitored item on this subscription.

        Parameters:
            nodeid: The node id or [ReadValueId][o6.ReadValueId] to monitor.
            callback: Optional callback for data change notifications.
            sampling_interval: The requested sampling interval.
            value_only: If ``True``, callback receives the unwrapped value.
            on_created: Optional lifecycle callback; see `MonitoredItem._data_change`.
            on_deleted: Optional lifecycle callback; see `MonitoredItem._data_change`.
            filter: Optional [DataChangeFilter][o6.DataChangeFilter].
            monitoring_mode: Monitoring mode (default: ``REPORTING``).
            queue_size: Requested queue size (default: ``1``).
            discard_oldest: Discard oldest when queue full (default: ``True``).

        Returns:
            The created monitored item.
        """
        ...

    def _monitor_event(
        self,
        nodeid: NodeIdLike,
        callback: MonitoredItem.EventCallback,
        on_created: MonitoredItem.CreatedCallback | None = None,
        on_deleted: MonitoredItem.DeletedCallback | None = None,
        *,
        filter: o6.EventFilter | str | None = None,
        monitoring_mode: o6.MonitoringMode = ...,
        queue_size: int = 100,
        discard_oldest: bool = True,
    ) -> MaybeAwaitable[MonitoredItem]:
        """Create an event monitored item on this subscription.

        Parameters:
            nodeid: The node id to monitor for events.
            callback: Callback invoked for each matching event.
            on_created: Optional lifecycle callback; see `MonitoredItem._event`.
            on_deleted: Optional lifecycle callback; see `MonitoredItem._event`.
            filter: Optional event filter or filter expression string.
            monitoring_mode: Monitoring mode (default: ``REPORTING``).
            queue_size: Requested queue size (default: ``100``).
            discard_oldest: Discard oldest when queue full (default: ``True``).

        Returns:
            The created event monitored item.
        """
        ...

    def delete(self) -> MaybeAwaitable[None]:
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
    def id(self) -> int | None: ...
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
    def enabled(self) -> bool: ...

class MonitoredItem:
    """Represents a monitored item within a subscription."""

    DataChangeCallback: TypeAlias = (
        Callable[[Any], None] | Callable[[MonitoredItem, Any], None]
    )
    EventCallback: TypeAlias = (
        Callable[[dict], None] | Callable[[MonitoredItem, dict], None]
    )
    CreatedCallback: TypeAlias = Callable[
        [MonitoredItem, o6.MonitoredItemCreateResult], None
    ]
    DeletedCallback: TypeAlias = Callable[[MonitoredItem, int, int], None]

    def __init__(self, subscription: Subscription) -> None: ...
    @classmethod
    def _data_change(
        cls,
        subscription: Subscription,
        nodeid: NodeIdLike,
        callback: MonitoredItem.DataChangeCallback,
        attribute_id: o6.AttributeId = ...,
        index_range: str = "",
        data_encoding: o6.QualifiedName | str = "",
        sampling_interval: float = 250.0,
        on_created: MonitoredItem.CreatedCallback | None = None,
        on_deleted: MonitoredItem.DeletedCallback | None = None,
    ) -> MonitoredItem:
        """Create a data change monitored item.

        Parameters:
            subscription: The subscription to attach the monitored item to.
            nodeid: The node id to monitor.
            callback: Callback invoked on data changes.
            attribute_id: The attribute to monitor.
            index_range: Optional index range for array values.
            data_encoding: Optional data encoding for the monitored item.
            sampling_interval: The requested sampling interval.
            on_created: Optional callback invoked once with the per-item
                ``MonitoredItemCreateResult`` when the server's create response
                arrives (regardless of result status).
            on_deleted: Optional callback invoked when the monitored item is
                destroyed (explicit delete, subscription delete, session close,
                disconnect, or create failure). Signature:
                ``(item, subscription_id, monitored_item_id)``.

        Returns:
            The created monitored item.
        """
        ...

    @classmethod
    def _event(
        cls,
        subscription: Subscription,
        nodeid: NodeIdLike,
        callback: MonitoredItem.EventCallback,
        on_created: MonitoredItem.CreatedCallback | None = None,
        on_deleted: MonitoredItem.DeletedCallback | None = None,
        *,
        filter: o6.EventFilter | str | None = None,
        monitoring_mode: o6.MonitoringMode = ...,
        queue_size: int = 100,
        discard_oldest: bool = True,
    ) -> MonitoredItem:
        """Create an event monitored item.

        Parameters:
            subscription: The subscription to attach the monitored item to.
            nodeid: The node id to monitor for events.
            callback: Callback invoked for each matching event.
            on_created: Optional callback invoked once with the per-item
                ``MonitoredItemCreateResult`` when the server's create response
                arrives.
            on_deleted: Optional callback invoked when the monitored item is
                destroyed. Signature: ``(item, subscription_id, monitored_item_id)``.
            filter: Optional event filter or filter expression string.
            monitoring_mode: Monitoring mode (default: ``REPORTING``).
            queue_size: Requested queue size (default: ``100``).
            discard_oldest: Discard oldest when queue full (default: ``True``).

        Returns:
            The created monitored event item.
        """
        ...

    def __await__(self) -> AwaitReturn[MonitoredItem]:
        """Allow ``await MonitoredItem(...)`` to work.

        Creating a monitored item requires a server round-trip, but ``__init__``
        cannot be async. The round-trip is therefore started in ``__init__`` and
        awaited here, so callers can write ``item = await MonitoredItem(...)`` and
        be sure the item is fully set up before proceeding.
        """
        ...

    def __bool__(self) -> bool:
        """Check if this is a valid MonitoredItem.

        A deleted monitored item evaluates to ``False``. ``delete()`` cleans up
        the monitored item on the server and client side, but cannot interfere
        with garbage collection of the Python object itself. Garbage collecting
        a ``delete``d monitored item is a noop in terms of state cleanup, but
        until then ``__bool__`` indicates that the monitored item is invalid.
        """
        ...

    def delete(self) -> MaybeAwaitable[None]:
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
    ) -> MaybeAwaitable[None]:
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

    def set_monitoring_mode(self, mode: o6.MonitoringMode) -> MaybeAwaitable[None]:
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
    ) -> MaybeAwaitable[None]:
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
    def params(self) -> o6.MonitoringParameters: ...
    @property
    def mode(self) -> o6.MonitoringMode: ...
    @property
    def id(self) -> int | None: ...
