# Node API

The Node API lets you browse an OPC UA address space and work with its nodes
through Python objects. Use it to read and write variables, call methods, and
navigate from one node to another on a connected client or a local server.

## Contents

| Topic | What it covers |
|---|---|
| [Nodes as Objects](using-nodes.md) | An example, the object-oriented model, and client and server entry points. |
| [Reading, Writing & Calling](read-write-call.md) | Values, attributes, Method binding, results, errors, and async operations. |
| [Navigation & Lookup](navigation.md) | Dotted navigation, NodeIds, browse paths, completion, and navigation caches. |
| [BrowseName to Python Names](name-conversion.md) | How OPC UA BrowseNames become Python attributes, including punctuation, namespaces, and name collisions. |

Start with [Nodes as Objects](using-nodes.md) and its runnable example server.
Then learn how to operate on nodes and find them in the address space.
Read [BrowseName to Python Names](name-conversion.md) when a node's name needs
conversion or conflicts with a Python attribute.

The [Client](../client/index.md) and [Server](../server/index.md) chapters cover
connection and server lifecycles and the operations available through their
service and high-level interfaces.
