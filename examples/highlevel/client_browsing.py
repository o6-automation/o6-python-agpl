import asyncio
import socket

import o6
from o6 import Client, types

localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"

with Client(endpoint_url) as client:
    print("=== Get a Node Directly from Client ===")
    node = client["ns=0;i=85"]
    print(node)  # Browse the Objects folder
    print(node(attr=o6.AttributeId.BROWSENAME))

    print("=== Traverse a Node ===")
    node = node.ScalarVariables
    print(node)  # Browse the Objects folder
    print(node(attr=o6.AttributeId.BROWSENAME))

    print("=== Get Node References ===")
    refs = client.browse(
        node,
        result_mask=o6.BrowseResultMask.BROWSENAME | o6.BrowseResultMask.NODECLASS,
    )
    for r in refs:
        print(f"{r.nodeid} browse_name: {r.browse_name} ({r.display_name})")

    print("=== Access / Modify Node Value ===")
    node = node.IntegerVariable
    print(node)  # Browse the IntegerVariable node
    print(node(attr=o6.AttributeId.BROWSENAME))
    print(f"value = {node()}")
    print("Now setting the value to 456123")
    node(types.UInt32(456123))
    print(f"value = {node()}")


async def main():
    async with Client(endpoint_url) as client:
        print("=== Access / Modify Node Value ===")
        node = await client["i=85"]
        node = await node.ScalarVariables.IntegerVariable
        print(node)  # Browse the IntegerVariable node
        c = await node(attr=o6.AttributeId.BROWSENAME)
        print(c)
        v = await node()
        print(v)
        await node(types.UInt32(456123))
        print(await node())


asyncio.run(main())
