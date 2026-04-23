# Client Browsing Example

Source example: `examples/highlevel/client_browsing.py`

This example demonstrates the higher-level node browsing API. It shows how to navigate the address space as a tree of Python objects.

## Explanation

### Fetching node directly from client

```python 
node = client["ns=0;i=85"]
print(node(attr=o6.AttributeId.NODECLASS).name)
```

### Traversing Nodes


```python 
node = node.ScalarVariables
print(node(attr=o6.AttributeId.NODECLASS).name)
```

### Node References 

```python 
refs = client.browse(
    node,
    result_mask=o6.BrowseResultMask.BrowseName | o6.BrowseResultMask.NodeClass,
)
for r in refs:
    print(f"{r.nodeid} browse_name: {r.browse_name} ({r.node_class.name})")
```

### Direct Access
```python 
node = node.IntegerVariable
node(types.UInt32(456123))
```

## Full source

```python
import asyncio
import socket

import o6
from o6 import Client, types

localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"

with Client(endpoint_url) as client:
    print("=== Get a Node Directly from Client ===")
    node = client["ns=0;i=85"]
    print(node)
    print(node(attr=o6.AttributeId.NODECLASS).name)

    print("=== Traverse a Node ===")
    node = node.ScalarVariables
    print(node)
    print(node(attr=o6.AttributeId.NODECLASS).name)

    print("=== Get Node References ===")
    refs = client.browse(
        node,
        result_mask=o6.BrowseResultMask.BrowseName | o6.BrowseResultMask.NodeClass,
    )
    for r in refs:
        print(f"{r.nodeid} browse_name: {r.browse_name} ({r.node_class.name})")

    print("=== Access / Modify Node Value ===")
    node = node.IntegerVariable
    print(node)
    print(node(attr=o6.AttributeId.NODECLASS).name)
    print(f"value = {node()}")
    print("Now setting the value to 456123")
    node(types.UInt32(456123))
    print(f"value = {node()}")


async def main():
    async with Client(endpoint_url) as client:
        print("=== Access / Modify Node Value ===")
    node = await client["i=85"]
    node = await node.ScalarVariables.IntegerVariable
        print(node)
    c = await node(attr=o6.AttributeId.NODECLASS)
        print(c.name)
    v = await node()
        print(v)
    await node(types.UInt32(456123))
    print(await node())

asyncio.run(main())
```