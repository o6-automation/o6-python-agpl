import o6
import asyncio

async def test_async():
    async with o6.AsyncClient("opc.tcp://localhost:4840") as c:
        result = await c.read(o6.types.NodeId("i=2256"))
        print("Async read result: ", result)

asyncio.run(test_async())
