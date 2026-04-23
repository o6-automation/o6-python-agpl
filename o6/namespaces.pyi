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
from ._o6 import Client, Server

from .namespace import Namespace

from typing import Union, List

class RemoteNamespaces:
    """Discovered server-side namespaces accessible after :meth:`discover`.

    Call :meth:`discover` on a connected client to browse and build types
    for every namespace on the remote server that is not already loaded
    locally.  Each discovered :class:`Namespace` is then stored as an
    attribute keyed by its *short_name*.
    """

    def get_namespace(self, key: str | int) -> Namespace:
        """Look up a discovered Namespace by short name, URI, or namespace index.

        Raises ``KeyError`` if no matching Namespace is found.
        """
        ...

    def discover(self) -> list[Namespace]:
        """Discover and register custom DataTypes from a connected server.

        Browses the server's DataType hierarchy, reads
        ``DataTypeDefinition`` attributes, and builds Python type classes
        for every namespace that is not already loaded in this context.

        Must be called on a client that is already connected.  Returns a
        list of newly created Namespaces (one per discovered namespace).
        """
        ...

class Namespaces:
    """Manages custom OPC UA DataType namespaces for a client, server, or
    standalone (ownerless) context.

    **Type sharing semantics**

    * **Clients** share pre-built Namespaces directly — ``append(namespace)``
      links the *same* Namespace object (and its Python type classes) into
      the client.  Multiple clients that ``append()`` the same pre-built
      Namespace will share a single set of type objects.
    * **Servers** always get their own copy — ``append(namespace)`` rebuilds
      types from the saved original NodeIds with the server's actual
      namespace indices, producing a distinct Namespace.
    * Types built for a client are therefore **not interchangeable** with
      types built for a server (different namespace index spaces).

    All ``append()`` calls on a client must happen **before** ``connect()``;
    attempting to load after the client is connected raises ``RuntimeError``.
    """

    remote: RemoteNamespaces

    def __init__(self, owner: Client | Server | None = None) -> None: ...
    def get_namespace(self, key: str | int) -> Namespace:
        """Look up a loaded Namespace by short name, URI, or namespace index.

        Raises ``KeyError`` if no matching Namespace is found.
        """
        ...

    def append(
        self,
        ns: Namespace,
        short_name: str | None = None,
    ) -> Namespace:
        """Append a namespace to the array (give it an index) and make it
        available under the shortname.

        **On a client**
            Registers the Namespace's canonical namespace URIs in the
            client's local table and links the pre-built capsules.  The
            *same* Namespace (and type objects) is reused — no rebuild.
            All ``append()`` calls must precede any manual
            ``client.add_namespace()`` calls; otherwise the canonical
            index slots may already be occupied and a ``ValueError`` is
            raised.

        **On a server**
            Creates a copy of the Namespace, restores its original
            (pre-remap) NodeIds, remaps them to the server's actual
            namespace indices, rebuilds the types, and links the new
            capsules.  The returned Namespace is distinct from the input.

        Raises ``ValueError`` if the namespace URI is already loaded in
        this context.

        """
        ...

    def load(
        self,
        nodeset2xml: str,
        short_name: str | None = None,
    ) -> Namespace:
        """Load a nodeset from an XML file path. Returns the list of previously
           unknown namespaces from the nodeset that have been appended. Note
           that loading a nodeset might also add nodes to existing namespaces.

        Parse the NodeSet2 XML, build Python type classes, and (if an owner is
        set) register them with the owner. The returned Namespace stores the
        built capsules and original NodeIds so it can later be passed to other
        clients/servers via ``append(namespace)``.

        Raises ``ValueError`` if the namespace URI is already loaded in
        this context.

        """
        ...

    def _parse_nodeset_prebuilt(self, module: object) -> Namespace: ...
    def __getattr__(self, name: str) -> Namespace: ...
