# Low-level

Demonstrates building a server's address space with explicit NodeIds,
data types, and access levels instead of the defaults that ``addVariable`` /
``addObject`` / ``addMethod`` fall back to.

Topics covered:
- Creating a server with an explicit application URI
- Adding object, variable, and method nodes with explicit NodeIds
- A read-only variable via an explicit access level
- Reading and writing node values through ``server.read()`` / ``server.write()``
  (as opposed to calling a node handle directly, as in the other tutorials)

Connect with any OPC UA client at: opc.tcp://localhost:4840

`Server(applicationUri=...)` sets the URI advertised in the server's
`ApplicationDescription`; every other tutorial leaves it at the default,
but a low-level server that pins its own NodeIds is a good place to also
pin an explicit identity.

```python
server = Server(port=EXAMPLE_PORT, applicationUri="urn:example:lowlevel-server")
```

## 1. Explicit NodeIds
`addObject()` / `addVariable()` / `addMethod()` all accept a `nodeId=`
keyword. Passing an `o6.NodeId` (instead of letting the server assign
one) keeps ids stable across restarts, which matters once other code —
a client script, a nodeset export — starts referencing them by id.

```python
print("--- 1. Explicit NodeIds ---")

device_id = o6.NodeId("ns=1;i=100")
server.addObject(
    "MyDevice",
    server.objectsNode,
    nodeId=device_id,
)
print(f"Added object node: {device_id}")

temp_id = o6.NodeId("ns=1;i=1001")
server.addVariable(
    "Temperature",
    device_id,
    22.5,
    nodeId=temp_id,
    dataType=o6.Double,
)
print(f"Added variable node: {temp_id}")
```

## 2. Explicit data type and access level
`dataType=` pins the OPC UA data type explicitly instead of inferring
it from the Python value, and `writable=False` clears the write bit in
the access level so clients can read the value but any write request
is rejected with `Bad_NotWritable`.

```python
print()
print("--- 2. Explicit Data Type and Access Level ---")

counter_id = o6.NodeId("ns=1;i=1002")
server.addVariable(
    "Counter",
    device_id,
    0,
    nodeId=counter_id,
    dataType=o6.Int32,
    writable=False,
)
print(f"Added variable node: {counter_id}")
```

## 3. A method with typed arguments
`addMethod()` takes the callback plus `inputArgs=` / `outputArgs=`
lists of `Argument` structs, each describing one parameter's name,
data type and value rank. The callback returns a
`(StatusCode, *outputs)` tuple; `StatusCode.GOOD` tells the caller the
call succeeded.

```python
print()
print("--- 3. A Method With Typed Arguments ---")

def add_numbers(node, a, b):
    print(f"Add({a}, {b}) = {a + b}")
    return (o6.StatusCode.GOOD, a + b)

method_id = o6.NodeId("ns=1;i=2001")
server.addMethod(
    name="Add",
    parent=device_id,
    callback=add_numbers,
    inputArgs=[
        ns0.datatypes.Argument(
            name="A",
            dataType=o6.Double,
            valueRank=o6.ValueRank.SCALAR,
            description="First operand",
        ),
        ns0.datatypes.Argument(
            name="B",
            dataType=o6.Double,
            valueRank=o6.ValueRank.SCALAR,
            description="Second operand",
        ),
    ],
    outputArgs=[
        ns0.datatypes.Argument(
            name="Sum", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="A + B"
        ),
    ],
    nodeId=method_id,
)
print(f"Added method node: {method_id}")
```

## 4. Read and write by NodeId
`server.read(nodeId)` / `server.write(nodeId, value)` operate directly
on a NodeId, as opposed to calling a node handle directly (`node()` /
`node(value)`) as in the other tutorials — useful when the id was
computed or looked up rather than kept around as a variable.

```python
    print()
    print("--- 4. Read and Write by NodeId ---")

    server.start()
    print(f"Server running at opc.tcp://localhost:{EXAMPLE_PORT}")
    print("Press Ctrl+C to stop.")

    try:
        cycle = 0
        while True:
            cycle += 1

            server.write(temp_id, 22.5 + (cycle % 50) * 0.1)
            server.write(counter_id, cycle)

            if cycle % 10 == 0:
                temp_val = server.read(temp_id)
                counter_val = server.read(counter_id)
                print(f"Cycle {cycle}: Temp = {temp_val}, Counter = {counter_val}")

            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        server.stop()
        print("Server stopped.")


if __name__ == "__main__":
    main()
```

## Source Code

Download [`S01_lowlevel.py`](server-S01_lowlevel/S01_lowlevel.py) to run it locally.
