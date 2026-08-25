#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
import o6
import asyncio

c = o6.Client("opc.tcp://localhost:4840")
c.connect()
n = c["i=85"]
# print(type(n))
# print(n(attr=o6.AttributeId.BROWSE_NAME))
#
# print(c.browse(n._nodeid, result_mask=o6.ns.ns0.datatypes.BrowseResultMask.BROWSE_NAME))
# print(n)
# print(dir(n))

c.root.objects.scalarVariables.BooleanVariable(True)
v = c.root.objects.scalarVariables.BooleanVariable()
print(v)

c.disconnect()


async def run_async():
    c = o6.Client("opc.tcp://localhost:4840")
    await c.connect()
    # n = await c["i=85"]
    # print(type(n))
    # print(await n(attr=o6.AttributeId.BROWSE_NAME))
    # print(await c.browse(n._nodeid, result_mask=o6.ns.ns0.datatypes.BrowseResultMask.BROWSE_NAME))
    # print(await n.scalarVariables)

    bv = await c.root.objects.scalarVariables.BooleanVariable

    await bv(False)
    print(await bv())

    # await c.root.objects.scalarVariables.BooleanVariable(True)
    # await v = c.root.objects.scalarVariables.BooleanVariable()
    await c.disconnect()


print("async")
result = asyncio.run(run_async())
print(result)
