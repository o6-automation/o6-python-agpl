# Reading, Writing & Calling

Calling a node with `()` acts on it. On a Variable, it reads or writes the
Value; on a Method, it invokes the Method. The optional `attr=` keyword
selects an OPC UA attribute instead.

The synchronous client fragments below belong inside the connected
`with o6.Client(...) as client:` block from
[Nodes as Objects](using-nodes.md#a-taste), with its example server running.
Run them in order within that block, starting with
`plant = client.objects.plant`. The same operations
work on `server.objects.plant` inside that server.

## Reading values and attributes

Call a Variable without a value to read:

```python
counter = plant.counter
counter(42)
value = counter()
print(value)                          # 42
```

For another attribute, select it by name or by `o6.AttributeId`:

```python
name = counter(attr="BrowseName")     # An o6.QualifiedName.
node_class = counter(attr=o6.AttributeId.NODE_CLASS)
object_name = plant(attr="BrowseName")
```

Attribute names are case-insensitive. Objects do not have a Value attribute,
so use an explicit `attr=` when reading an Object. A value read returns the
Python value, without a DataValue's status or timestamps. Use
[`client.read(..., valueOnly=False)`](../client/read-write-call.md)
when you need those fields.

## Writing values and attributes

Pass the new value as the first argument, or use `value=`:

```python
counter(42)
plant.label(value="running")
```

A successful Node write returns `None`; a failed write raises
`o6.StatusCodeError`. It differs from `client.write(...)`, which returns the
operation's StatusCode for you to check. Values must have a compatible OPC UA
type; see [Primitive Types](../sdk-fundamentals/builtin/primitive-types.md)
for explicit numeric types.

Attribute writes require the attribute's actual type and server support.
For example, DisplayName takes an `o6.LocalizedText`. This server-side
fragment, inserted before `input(...)` in the example server, changes the
Variable's display text and restores it:

```python
counter = server.objects.plant.counter
original_name = counter(attr="DisplayName")
counter(value=o6.LocalizedText("Count"), attr="DisplayName")
counter(value=original_name, attr="DisplayName")
```

BrowseName instead takes an `o6.QualifiedName`, such as
`o6.QualifiedName(1, "Count")`, not a plain string. The example server rejects
BrowseName writes with `BAD_WRITE_NOT_SUPPORTED`, including local writes.
A client also needs permission for any remotely writable attribute;
permission alone does not make an unsupported attribute writable.

For synchronous code, `counter._value` and `counter._value = 42` are
convenience forms. Prefer call syntax if the code may become asynchronous:
property assignment cannot be awaited.

## Calling Methods

Pass inputs as positional arguments and unpack the status and outputs:

```python
status, greeting = plant.hello("World")
print(greeting)                       # Hello, World!
```

A typed Method call returns `(StatusCode, *output_arguments)` on success.
Even with one output, the result is a tuple. With no outputs it contains only
the status. A Method with no inputs is invoked with empty parentheses;
`hello()` would still be a Method call, but would fail because Hello requires
one input. To read a Method's attributes, use `attr=`, for example
`plant.hello(attr="BrowseName")`.

### Which Object receives the call?

OPC UA Call identifies both a Method and the Object on which to invoke it.
Dot lookup binds the Method to the Object used for that lookup, so
`plant.hello("World")` supplies `plant` automatically.

A Method obtained directly by NodeId on a client has no parent lookup
context. Pass the Object explicitly, as a node or NodeId-like value:

```python
method = client[o6.NodeId("ns=1;i=2001")]
status, greeting = method("World", object=plant)
```

Local server Method handles can retain their construction Object. Passing
`object=` explicitly also works there. If several Objects reference the same
Method, each dot lookup binds it to that lookup's Object. Adding a reference
changes the address-space relationship; it does not replace the Method's
callback.

## Results and failures

The shared [error-handling contract](../sdk-fundamentals/builtin/statuscode.md#errors-and-status-codes)
applies to client and server handles. Reads return values for Good severity
and raise for Uncertain or Bad. Writes and typed Method calls check for exact
`GOOD`, raising `o6.StatusCodeError` for any other status. Successful writes
return `None`; Method calls return `(StatusCode, *outputs)`.

For example, handle a rejected operation around the actual call:

```python
try:
    plant.counter(42)
except o6.StatusCodeError as error:
    print("Write failed:", error)
```

Python argument errors and missing or ambiguous child names are separate
from OPC UA operation failures. To inspect a returned bad Method status
instead of raising on it, use `client.call(...)` or `server.call(...)`;
service failures still raise. The
[client operation contracts](../client/read-write-call.md) describe these
lower-level result shapes.

## Async operations

Inside an async task, client and server node operations are awaitable,
including local operations that can finish immediately. Await navigation as
well as reads, writes, and Method calls. A complete client for the same
example server is:

```python
import asyncio
import o6


async def main():
    async with o6.Client("opc.tcp://localhost:4840") as client:
        plant = await client.objects.plant
        await plant.counter(42)
        print("value:", await plant.counter())
        status, greeting = await plant.hello("o6")
        print("greeting:", greeting)


asyncio.run(main())
```

It prints the same two lines as the synchronous introduction and disconnects
on exit. Chained dot navigation and the final call can share one `await`, as
in `await client.objects.plant.counter()`. To retain a handle, resolve it
with `counter = await plant.counter` and later use `await counter()`.
Use `await counter(42)` for writes, not assignment to `_value`.

## Quick reference

| Task | Synchronous Node syntax |
|---|---|
| Read a Variable | `counter()` |
| Write a Variable | `counter(42)` |
| Read an attribute | `counter(attr="BrowseName")` |
| Write an attribute | `counter(value=text, attr="DisplayName")`, where `text` is a LocalizedText and the write is allowed |
| Call a Method | `status, greeting = plant.hello("o6")` |
| Identify a node | `counter._nodeid` |

In async tasks, await the read, write, and call expressions. `_nodeid` is
already held by a resolved node and needs no await.

Server Object and View handles can also emit events with `<<`; see
[Firing an event from a Node handle](../server/events.md#firing-an-event-from-a-node-handle).
