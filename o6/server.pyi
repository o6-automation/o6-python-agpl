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
"""
High-level OPC UA Server implementation.

This module provides a pythonic, high-level interface to OPC UA server functionality,
wrapping the low-level _o6 C extension module.

Basic usage:
    from o6 import Server

    server = Server(port=4840)
    with server:
        # Add a variable
        temp = server.add_variable("Temperature", server.objects_node,
                                   value=25.0)
        # Read/write
        print(server.read_value(temp.nodeid))
        server.write_value(temp.nodeid, 30.0)
"""

from __future__ import annotations
from types import TracebackType
from typing import Any, Callable, List, Optional, Union
from pathlib import Path
import asyncio
import logging

import o6
from . import _o6
from o6 import HasNodeId, NodeIdLike, LocalizedTextLike

# --- Well-known NodeIds (namespace 0) ----------------------------------------

OBJECTS_FOLDER: o6.NodeId
TYPES_FOLDER: o6.NodeId
VIEWS_FOLDER: o6.NodeId
SERVER_NODE: o6.NodeId

BASE_OBJECT_TYPE: o6.NodeId
BASE_VARIABLE_TYPE: o6.NodeId
BASE_DATA_VARIABLE_TYPE: o6.NodeId

ORGANIZES: o6.NodeId
HAS_COMPONENT: o6.NodeId
HAS_PROPERTY: o6.NodeId
HAS_TYPE_DEFINITION: o6.NodeId
HAS_SUBTYPE: o6.NodeId

# --- ServerNode ---------------------------------------------------------------

class ServerNode(HasNodeId):
    """A reference to a node in the server address space.

    Instances of this class are returned by the ``add_*`` methods on
    :class:`Server`.  They store the *nodeid* together with a back-reference
    to the server so that convenience properties like ``.value`` work
    directly.
    """

    _nodeid: o6.NodeId

    def __init__(self, server: Server, nodeid: o6.NodeId) -> None: ...
    @property
    def nodeid(self) -> o6.NodeId: ...
    @property
    def value(self) -> Any:
        """Read the current value attribute."""
        ...

    @value.setter
    def value(self, v: Any) -> None: ...
    def delete(self, delete_references: bool = True) -> None:
        """Remove this node from the server address space."""
        ...

    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...

# --- Server -------------------------------------------------------------------

class Server(_o6.Server):
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
    private_key : str, Path, or bytes, optional
        Server private key (file path or raw bytes).
    trust_list : list, optional
        Trusted certificates for client verification.
    issuer_list : list, optional
        Issuer certificates.
    revocation_list : list, optional
        Certificate revocation lists.
    secure_only : bool
        If True, reject unencrypted connections (default False).
    accept_all_certificates : bool
        If True, trust all client certificates (default False).
    application_uri : str, optional
        Override the default application URI.

    Example
    -------
    >>> server = Server(port=4840)
    >>> with server:
    ...     temp = server.add_variable("Temperature",
    ...                                server.objects_node, 22.5)
    ...     print(temp.value)
    22.5
    """

    ns: o6.namespaces.Namespaces

    def __init__(
        self,
        port: int = 4840,
        logger: Optional[logging.Logger] = None,
        loop: Optional[asyncio.AbstractEventLoop] = None,
        *,
        certificate: Union[str, Path, bytes, None] = None,
        private_key: Union[str, Path, bytes, None] = None,
        trust_list: Optional[List[Union[str, Path, bytes]]] = None,
        issuer_list: Optional[List[Union[str, Path, bytes]]] = None,
        revocation_list: Optional[List[Union[str, Path, bytes]]] = None,
        secure_only: bool = False,
        accept_all_certificates: bool = False,
        application_uri: Optional[str] = None,
    ) -> None: ...

    # -- Well-known nodes (convenience properties) ---------------------------

    @property
    def objects_node(self) -> o6.NodeId:
        """The Objects folder (i=85)."""
        ...

    @property
    def types_node(self) -> o6.NodeId:
        """The Types folder (i=86)."""
        ...

    @property
    def server_node(self) -> o6.NodeId:
        """The Server object (i=2253)."""
        ...
    # -- Lifecycle -----------------------------------------------------------

    def start(self) -> None:
        """Start the server networking layer.

        The asyncio event loop handles all I/O, timers, and callbacks.
        When no running loop is detected (synchronous callers), a
        lightweight background daemon thread drives the loop instead.
        """
        ...

    def stop(self) -> None:
        """Shut down the server."""
        ...

    def __enter__(self) -> Server: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    async def __aenter__(self) -> Server: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...

    # -- Reverse connect ------------------------------------------------------

    def add_reverse_connect(
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
            A handle that can be passed to :meth:`remove_reverse_connect`.
        """
        ...

    def remove_reverse_connect(self, handle: int) -> None:
        """Remove a reverse connect registration.

        Parameters
        ----------
        handle : int
            The handle returned by :meth:`add_reverse_connect`.
        """
        ...
    # -- Add nodes (high-level) -----------------------------------------------

    def add_variable(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike,
        value: Any = None,
        *,
        nodeid: NodeIdLike | None = None,
        data_type: NodeIdLike | None = None,
        writable: bool = True,
        historizing: bool = False,
        ns: int = 1,
    ) -> ServerNode:
        """Add a variable node to the address space.

        Parameters
        ----------
        name : str or LocalizedText
            Browse name (and display name) of the variable.
        parent : NodeIdLike
            Parent node (typically ``server.objects_node``).
        value : any, optional
            Initial value. The OPC UA data-type is inferred automatically
            unless *data_type* is given explicitly.
        nodeid : NodeIdLike, optional
            Requested node id.  ``None`` -> server assigns one.
        data_type : NodeIdLike, optional
            Explicit data type.  If ``None``, inferred from *value*.
        writable : bool
            Whether the variable is writable by clients (default ``True``).
        historizing : bool
            Whether the variable supports historical data access (default ``False``).
            Requires ``config.set_history_database()`` and a subsequent
            ``register_historizing()`` call.
        ns : int
            Namespace index for the browse name (default 1).

        Returns
        -------
        ServerNode
            A handle for the newly created variable node.
        """
        ...

    def add_object(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike,
        *,
        nodeid: NodeIdLike | None = None,
        type_definition: NodeIdLike = ...,
        ns: int = 1,
    ) -> ServerNode:
        """Add an object node to the address space.

        Parameters
        ----------
        name : str or LocalizedText
            Browse name / display name.
        parent : NodeIdLike
            Parent node.
        nodeid : NodeIdLike, optional
            Requested node id.
        type_definition : NodeIdLike, optional
            Type definition node (default: BaseObjectType i=58).
        ns : int
            Namespace index for the browse name.

        Returns
        -------
        ServerNode
        """
        ...

    def add_object_type(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike = ...,
        *,
        nodeid: NodeIdLike | None = None,
        ns: int = 1,
    ) -> ServerNode:
        """Add an object type node.

        Parameters
        ----------
        name : str or LocalizedText
            Browse name / display name.
        parent : NodeIdLike, optional
            Parent type node (default: BaseObjectType i=58).
        nodeid : NodeIdLike, optional
            Requested node id.
        ns : int
            Namespace index for the browse name.

        Returns
        -------
        ServerNode
        """
        ...

    def add_variable_type(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike = ...,
        *,
        data_type: NodeIdLike = ...,
        value_rank: int = -1,
        nodeid: NodeIdLike | None = None,
        ns: int = 1,
    ) -> ServerNode:
        """Add a variable type node.

        Parameters
        ----------
        name : str or LocalizedText
            Browse name / display name.
        parent : NodeIdLike, optional
            Parent type (default: BaseVariableType i=62).
        data_type : NodeIdLike, optional
            Data type (default: Double i=11).
        value_rank : int
            Value rank (default: -1 = scalar).
        nodeid : NodeIdLike, optional
            Requested node id.
        ns : int
            Namespace index for the browse name.

        Returns
        -------
        ServerNode
        """
        ...

    def add_method(
        self,
        name: LocalizedTextLike,
        parent: NodeIdLike,
        callback: Callable[..., Any],
        *,
        input_args: Optional[List[o6.Argument]] = None,
        output_args: Optional[List[o6.Argument]] = None,
        nodeid: o6.NodeId | None = None,
        ns: int = 1,
    ) -> ServerNode:
        """Add a method node to the address space.

        Parameters
        ----------
        name : str or LocalizedText
            Browse name / display name.
        parent : NodeIdLike
            Parent node (typically an object node).
        callback : callable
            Python function called when a client invokes the method.
            Signature: ``callback(*inputs) -> list[output_values]``
        input_args : list of Argument, optional
            Input argument descriptors.
        output_args : list of Argument, optional
            Output argument descriptors.
        nodeid : NodeId, optional
            Requested node id.
        ns : int
            Namespace index for the browse name.

        Returns
        -------
        ServerNode
        """
        ...
    # -- References / deletion ------------------------------------------------

    def add_reference(  # type: ignore[override]
        self,
        source: NodeIdLike,
        target: NodeIdLike,
        reference_type: NodeIdLike,
        *,
        forward: bool = True,
    ) -> None:
        """Add a reference between two nodes."""
        ...

    def delete_node(  # type: ignore[override]
        self,
        nodeid: NodeIdLike,
        *,
        delete_references: bool = True,
    ) -> None:
        """Delete a node from the address space."""
        ...
    # -- Read / write ---------------------------------------------------------

    def read_value(
        self,
        nodeid: NodeIdLike,
    ) -> Any:
        """Read the value attribute of a variable node."""
        ...

    def write_value(
        self,
        nodeid: NodeIdLike,
        value: Any,
    ) -> None:
        """Write the value attribute of a variable node."""
        ...

# -- Helper: build Argument objects easily ------------------------------------

def make_argument(
    name: str,
    data_type: NodeIdLike,
    *,
    value_rank: int = -1,
    description: LocalizedTextLike = "",
) -> o6.Argument:
    """Create an OPC UA Argument descriptor.

    Parameters
    ----------
    name : str
        Argument name.
    data_type : NodeIdLike
        Data type (e.g. ``"i=11"`` for Double).
    value_rank : int
        Value rank (-1 = scalar, 1 = 1D array, ...).
    description : str or LocalizedText
        Human-readable description.

    Returns
    -------
    o6.Argument
    """
    ...
