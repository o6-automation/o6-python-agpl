# o6.namespaces.Namespaces

Manages custom OPC UA DataType namespaces for a client, server, or
standalone (ownerless) context. Used it to register pre-built custom
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

Use pre-built namespaces when available:

    client.ns.append(o6.ns.di) # or
    server.ns.append(o6.ns.di)

This links the global prebuilt `o6.ns.di` namespace and reuses the
same type objects across clients.

For custom or external nodesets, load XML definitions first:

    client.ns.load("path/to/custom_nodeset2.xml", short_name="MyTypes")

This parses the nodeset XML, builds Python type classes, and registers the
namespace URI in the client's local table.

::: o6.namespaces.Namespaces
    options:
      show_root_heading: true
      show_source: false
      show_category_heading: true
      members_order: source
      inherited_members: true
      show_signature: true
      separate_signature: true