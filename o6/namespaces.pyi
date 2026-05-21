# Copyright 2026 (c) o6 Automation GmbH
from ._o6 import Client, Server

from .namespace import Namespace

class RemoteNamespaces:
    """Discovered server-side namespaces accessible after :meth:`discover`.

    Call :meth:`discover` on a connected client to browse and build types
    for every namespace on the remote server that is not already loaded
    locally.  Each discovered :class:`Namespace` is then stored as an
    attribute keyed by its *short_name*.
    """

    def __init__(self, namespaces: "Namespaces") -> None: ...
    def __repr__(self) -> str: ...
    def __getitem__(self, key: str | int) -> Namespace:
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
    standalone (ownerless) context.  Use it to register pre-built custom
    DataType namespaces or load NodeSet2 XML files before the client connects.

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

    Important:
        All ``append()`` calls on a client must happen **before** ``connect()``;
        attempting to load after the client is connected raises ``RuntimeError``.

    Use pre-built namespaces when available::

        client.ns.append(o6.ns.di)  # or
        server.ns.append(o6.ns.di)

    This links the global prebuilt ``o6.ns.di`` namespace and reuses the
    same type objects across clients.

    For custom or external nodesets, load XML definitions first::

        client.ns.load("path/to/custom_nodeset2.xml", short_name="MyTypes")

    This parses the nodeset XML, builds Python type classes, and registers the
    namespace URI in the client's local table.
    """

    remote: RemoteNamespaces

    def __init__(self, owner: Client | Server | None = None) -> None: ...
    def __getitem__(self, key: str | int) -> Namespace:
        """Look up a loaded Namespace by short name, URI, or namespace index.

        Raises ``KeyError`` if no matching Namespace is found.
        """
        ...

    def __getattr__(self, name: str) -> Namespace: ...
    def append(
        self,
        ns: Namespace,
        short_name: str | None = None,
    ) -> Namespace:
        """Register a namespace, assign it a namespace-index slot, and make it
        available as an attribute.

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
        """Parse a NodeSet2 XML file, build Python type classes, and register
        the namespace.

        The returned Namespace stores the built capsules and original NodeIds
        so it can later be passed to other clients/servers via
        ``append(namespace)``.

        Raises ``ValueError`` if the namespace URI is already loaded in
        this context.
        """
        ...

    def _parse_nodeset(self, nodeset2xml: str) -> Namespace:
        """Parse a NodeSet2 XML file and return a Namespace without appending it.

        Thread-safe: does not read or write any shared Namespaces state.
        Call ``append()`` sequentially in dependency order afterward.
        """
        ...

    def _parse_nodeset_prebuilt(self, module: object) -> Namespace:
        """Reconstruct a Namespace from a pre-generated nodeset module.

        Fast path used by the o6-ns package: no XML parsing, no
        nodeset-compiler overhead.  The module must expose the variables
        produced by ``tools/update_ns.py`` (``_URI``, ``_VERSION``,
        ``_REQUIRED``, ``_STRUCTURES``, ``_ENUMS``, ``_ORIGINAL_NODEIDS``,
        ``_NODES``).

        Thread-safe: does not read or write any shared Namespaces state.
        Call ``append()`` sequentially in dependency order afterward.
        """
        ...

    def _build_types(self, descriptor: Namespace) -> None:
        """Convert all descriptions to ``UA_DataType`` arrays and build Python
        type objects.  Stores all capsules on ``descriptor._capsule`` so the
        C arrays remain alive as long as the Namespace does.  Populates
        ``descriptor._types`` with the created classes.
        """
        ...

    @staticmethod
    def _link_namespace(
        descriptor: Namespace,
        owner: Client | Server,
    ) -> None:
        """Link all pre-built capsules of a Namespace into the given owner."""
        ...
