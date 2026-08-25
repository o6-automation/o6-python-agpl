Client Browsing : Address Space Traversal
=========================================
Demonstrates how to walk an OPC UA server's address space from the
client: starting from the standard `Objects` folder, navigating to a
specific node by *browse name* (dot syntax) or *browse path* (index
syntax), enumerating the references coming out of a node with
`client.browse(...)`, and reading / writing the value of a leaf
variable through the resulting `Node` handle.

The example is wired against `basic_server.py` so start that script in
one terminal before running this one. The address space we walk is:

    Objects/
    └── Plant/                  (Object)
        ├── Temperature         (Double,  ns=1;i=1001)
        ├── Pressure            (Double,  ns=1;i=1002)
        ├── Status              (String,  ns=1;i=1003)
        ├── Counter             (Int32,   ns=1;i=1004)
        ├── Running             (Boolean, ns=1;i=1005)
        └── Add                 (Method,  ns=1;i=2001)

The example shows both the **synchronous** style (blocking `with
Client(...)` and direct attribute / value access) and the **asynchronous**
style (`async with`, `await` everywhere) so you can compare the two.

Browsing the address space is one of the most useful patterns in a
real OPC UA client: server-assigned NodeIds are often not known by the client,
and the *browse name* of a node is the stable
identifier you actually want to program against. The `o6` SDK gives
you three layers of convenience on top of the raw `Browse` service:
`client.browse(...)` returns a list of references, `client[NodeId]`
hands back a `Node`, and `Node` itself supports dot syntax
(`.Plant`) and browse-path syntax (`["/Objects/Plant"]`) so you can
walk the tree without manually tracking NodeIds.

## 1. Connection Setup
Same as in `client_basic.py`: build the
endpoint URL from the local hostname so it matches the URL the
server advertises during discovery.

```python
localhost = "localhost"
endpoint_url = f"opc.tcp://{localhost}:4840"
print(f"Connecting to {endpoint_url} ...")
```

## 2. Sync: Get a Node Directly
`client[nodeid]` returns a `Node` object that mirrors the address
space entry. In a synchronous `with` block the call blocks until the
`NodeClass` and `BrowseName` attributes have been read; from there
the `Node` is a local handle that can be printed, browsed, and
indexed.

```python
with Client(endpoint_url) as client:
    print("\n=== Get a Node Directly from Client ===")
    node = client["i=85"]  # The standard `Objects` folder
    print(f"node              = {node}")
    print(f"node.BROWSENAME   = {node(attr=AttributeId.BROWSE_NAME)}")
    print(f"node.NODECLASS    = {node(attr=AttributeId.NODE_CLASS)}")
```

## 3. Sync: Dot Traversal
`node.Child` walks one level into the address space by browse name
(the same way you'd navigate Python objects).

We use this to reach `Plant` and then `Plant.Temperature`. Both
`Plant` (its NodeId is allocated at server startup) and
`Temperature` (its data type is `Double`) live in the user namespace.

```python
print("\n=== Traverse a Node ===")
node = node.Plant
print(f"node              = {node}")
print(f"node.BROWSENAME   = {node(attr=AttributeId.BROWSE_NAME)}")
print(f"node.NODECLASS    = {node(attr=AttributeId.NODE_CLASS)}")
```

## 4. Sync: Enumerate Children with `client.browse(...)`
`client.browse(node, ...)` walks one level out from `node` and
returns a list of `ReferenceDescription`s. The `result_mask` keyword
controls which fields each reference carries back: `63` asks for
every reference field (browse name, display name, node class, type
definition, …) so we can print the children with full detail.

```python
print("\n=== Get Node References ===")
refs = client.browse(
    node,
    resultMask=(
        ns0.datatypes.BrowseResultMask.BROWSE_NAME
        | ns0.datatypes.BrowseResultMask.NODE_CLASS
        | ns0.datatypes.BrowseResultMask.DISPLAY_NAME
        | ns0.datatypes.BrowseResultMask.TYPE_DEFINITION
    ),
)
for r in refs:
    print(
        f"  {r.nodeId}  "
        f"browseName={r.browseName}  "
        f"display_name={r.displayName}  "
        f"type={r.nodeClass.name}"
    )
```

## 5. Sync: Read and Write Through the `Node`
Calling a `Node` with no arguments (`node()`) returns the current
value of its `Value` attribute; calling it with a value
(`node(value)`) writes that value. The ``o6`` DK interprets the OPC UA data
type from the Python type of the value, so a Python `float` is
written as a `Double`, a Python `int` as an `Int32`, and so on.

```python
print("\n=== Access / Modify Node Value ===")
node = node.Temperature  # Drill into a leaf variable
print(f"node              = {node}")
print(f"node.BROWSENAME   = {node(attr=AttributeId.BROWSE_NAME)}")
print(f"value             = {node()}")

print("Now setting the value to 25.0")
node(25.0)  # Plain Python float -> OPC UA Double
print(f"value             = {node()}")
```

## 6. Async: The Same, Inside an Event Loop
The asynchronous form is useful when the surrounding application
(a web server, a UI loop, ...) is already running its own
`asyncio` event loop. Inside an `async with Client(...) as client:`
the same `client[...]` and `client.browse(...)` calls become
awaitable. The dot-traversal also returns an `AwaitableNode` that
chains `await`s for you.

```python
async def main() -> None:
    async with Client(endpoint_url) as client:
        print("\n=== Async: Get + Traverse + Read + Write ===")
        # client["..."] returns an awaitable; the `await` resolves it
        # to a Node handle.
        node = await client["i=85"]
        node = await node.Plant  # async dot-traversal
        node = await node.Temperature  # async dot-traversal into a leaf

        c = await node(attr=AttributeId.BROWSE_NAME)
        print(f"node              = {node}")
        print(f"node.BROWSENAME   = {c}")

        v = await node()
        print(f"value             = {v}")

        await node(30.0)
        print(f"value (after write) = {await node()}")


asyncio.run(main())
print("\n=== Example completed ===")
```

## Complete Source Code

```python
#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Client Browsing : Address Space Traversal
=========================================
Demonstrates how to walk an OPC UA server's address space from the
client: starting from the standard `Objects` folder, navigating to a
specific node by *browse name* (dot syntax) or *browse path* (index
syntax), enumerating the references coming out of a node with
`client.browse(...)`, and reading / writing the value of a leaf
variable through the resulting `Node` handle.

The example is wired against `basic_server.py` so start that script in
one terminal before running this one. The address space we walk is:

    Objects/
    └── Plant/                  (Object)
        ├── Temperature         (Double,  ns=1;i=1001)
        ├── Pressure            (Double,  ns=1;i=1002)
        ├── Status              (String,  ns=1;i=1003)
        ├── Counter             (Int32,   ns=1;i=1004)
        ├── Running             (Boolean, ns=1;i=1005)
        └── Add                 (Method,  ns=1;i=2001)

The example shows both the **synchronous** style (blocking `with
Client(...)` and direct attribute / value access) and the **asynchronous**
style (`async with`, `await` everywhere) so you can compare the two.
"""


import asyncio
import socket
import o6
from o6 import Client, AttributeId
from o6.ns import ns0


localhost = "localhost"
endpoint_url = f"opc.tcp://{localhost}:4840"
print(f"Connecting to {endpoint_url} ...")



with Client(endpoint_url) as client:
    print("\n=== Get a Node Directly from Client ===")
    node = client["i=85"]  # The standard `Objects` folder
    print(f"node              = {node}")
    print(f"node.BROWSENAME   = {node(attr=AttributeId.BROWSE_NAME)}")
    print(f"node.NODECLASS    = {node(attr=AttributeId.NODE_CLASS)}")


    print("\n=== Traverse a Node ===")
    node = node.Plant
    print(f"node              = {node}")
    print(f"node.BROWSENAME   = {node(attr=AttributeId.BROWSE_NAME)}")
    print(f"node.NODECLASS    = {node(attr=AttributeId.NODE_CLASS)}")


    print("\n=== Get Node References ===")
    refs = client.browse(
        node,
        resultMask=(
            ns0.datatypes.BrowseResultMask.BROWSE_NAME
            | ns0.datatypes.BrowseResultMask.NODE_CLASS
            | ns0.datatypes.BrowseResultMask.DISPLAY_NAME
            | ns0.datatypes.BrowseResultMask.TYPE_DEFINITION
        ),
    )
    for r in refs:
        print(
            f"  {r.nodeId}  "
            f"browseName={r.browseName}  "
            f"display_name={r.displayName}  "
            f"type={r.nodeClass.name}"
        )


    print("\n=== Access / Modify Node Value ===")
    node = node.Temperature  # Drill into a leaf variable
    print(f"node              = {node}")
    print(f"node.BROWSENAME   = {node(attr=AttributeId.BROWSE_NAME)}")
    print(f"value             = {node()}")

    print("Now setting the value to 25.0")
    node(25.0)  # Plain Python float -> OPC UA Double
    print(f"value             = {node()}")




async def main() -> None:
    async with Client(endpoint_url) as client:
        print("\n=== Async: Get + Traverse + Read + Write ===")
        # client["..."] returns an awaitable; the `await` resolves it
        # to a Node handle.
        node = await client["i=85"]
        node = await node.Plant  # async dot-traversal
        node = await node.Temperature  # async dot-traversal into a leaf

        c = await node(attr=AttributeId.BROWSE_NAME)
        print(f"node              = {node}")
        print(f"node.BROWSENAME   = {c}")

        v = await node()
        print(f"value             = {v}")

        await node(30.0)
        print(f"value (after write) = {await node()}")


asyncio.run(main())
print("\n=== Example completed ===")
```
