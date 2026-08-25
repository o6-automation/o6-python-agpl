# Node API — Usage

This page is a hands-on tour of the Node API once a client is connected. It assumes you have an OPC UA server reachable at `opc.tcp://localhost:4840`.
The companion [Overview](../node-api.md) page explains the design and motivation; this page is about the syntax you actually type.

## Setting the stage

A running example is the fastest way to learn. The snippets below assume a server that exposes an object with a few variables and a method, similar to the [server example](../../examples/example-server/server.py):

```
Objects/
├── MyVariables      (Object)
│   ├── MyInteger    (Variable, Int32, read/write)
│   └── MyString     (Variable, String, read/write)
└── TestMethods      (Object)
    └── Hello        (Method, input: String, output: String)
```

The exact path is irrelevant — replace it with the structure of your own server.
What matters is the three navigation patterns you'll see below: **`.` to browse**, **`[]` to look up by path**, **`()` to act on a node**.

## Connecting

A Node-API session is a regular `Client` session. The Node API is layered on top of an active client connection.

```python
from o6 import Client

client = Client("opc.tcp://localhost:4840")
client.connect()
```

Once `client.connect()` returns, the client has an active session and the entry-point nodes (`client.root`, `client.objects`, `client.types`, `client.views`) are live and ready to be navigated.

---

# Browsing

Browsing is how you navigate from a node to its children.
Two syntaxes are available: dotted attribute access for the common case, and bracket indexing for paths that are not safe as identifiers.

## Entry points

A connected `Client` exposes four top-level nodes that correspond to the four standard folders of the OPC UA address space:

| Attribute | NodeId | What's inside |
|---|---|---|
| `client.root` | `i=84` | The address-space root. The three folders below are also reachable from here. |
| `client.objects` | `i=85` | The instance address space — your application's objects, variables, methods. |
| `client.types` | `i=86` | The type hierarchy — `ObjectTypes`, `VariableTypes`, `ReferenceTypes`, `DataTypes`. |
| `client.views` | `i=87` | Server-defined views over the address space, if any. |


## Dot syntax

Every entry point is an `ObjectNode` that supports the same dot, bracket, and call syntaxes as any other node. Most user code starts from `client.objects`; the others are useful when you need to walk the type hierarchy or query a server-defined view.

`.` triggers a server-side `Browse` for the named child. Children are resolved lazily and cached on the parent node, so repeated access to the same child is free.

```python
# A single step — resolve one child of Objects
parent = client.objects.MyVariables

# Chained steps — each `.` resolves one level
var = client.objects.MyVariables.MyInteger

# We can continue from the cached parent
var = parent.MyInteger
```

Names are matched case-insensitively against `BrowseName`. The result is a `Node` subclass (`VariableNode`, `ObjectNode`, `MethodNode`, …) depending on the child's `NodeClass`.

In interactive shells, `dir(node)` and `<TAB>` completion both run a browse and list the children — see [Interactive completion](#interactive-completion) below.

## Bracket syntax `[]`

The dot syntax fails when a `BrowseName` is ambiguous: if a node has more than one child with the same name (case-insensitively), `node.child` raises because the path does not pin it down to a single target. In these cases you have to use `[]`, which returns a list of matching targets that you can disambiguate yourself.

```python
# Two children both called "Status" → dot syntax can't pick one
nodes = client.objects["MyDevice/Status"]    # list of targets
status = nodes[0]                            # pick the right one
```

`[]` is translated server-side through `TranslateBrowsePathsToNodeIds` and handles the full range of the browse path syntax specified in the spcefication [here]().

---

# Node access — the `()` operator

Once you have a node, the python call operator `()` handles every interaction: read, write, call.
The distinction is by argument shape, not by a different method.

## What `()` does

Every `Node` subclass overloads `__call__`. Calling a node with no value is a **read**, calling it with a value is a **write**, and calling a `MethodNode` is a **call**. An optional `attr=` keyword selects which attribute to act on; `None` (the default) means the `Value` attribute for variables and the method invocation for methods.

```python
# Read
node()

# Read a specific attribute
node(attr="BrowseName")
node(attr=o6.AttributeId.DISPLAY_NAME)

# Write
node(42)
node("hello")

# Call (method nodes only)
parent.MyMethod("arg1", "arg2")
```

The `attr=` keyword accepts either an `o6.AttributeId` member or a case-insensitive `o6.AttributeId`-like string such as `"BrowseName"`, `"NodeClass"`, `"DisplayName"`, `"Description"`, `"DataType"`, `"ValueRank"`, `"AccessLevel"`, …

## Reading values

Call with no argument to read the current value of a variable:

```python
value = client.objects.MyVariables.MyInteger()
print(value)
```

Reading a different attribute:

```python
name = client.objects.MyVariables.MyInteger(attr="BrowseName")
print(name)             # QualifiedName('1:MyInteger')

class_ = client.objects.MyVariables.MyInteger(attr="NodeClass")
```

## Writing values

Pass the new value as the first positional argument:

```python
client.objects.MyVariables.MyInteger(42)
client.objects.MyVariables.MyString("hello")
```

Writing a non-`Value` attribute: pass both `value=` and `attr=`:

```python
client.objects.MyVariables.MyInteger(value="NewName", attr="BrowseName")
```

This is equivalent to `client.write(nodeid, value)` on the high-level client API — but the node is reached through the address-space path, so no `NodeId` string is required.

## Calling methods

Method nodes are called by passing the input arguments positionally. When the method is reached through its parent object, the parent is picked up automatically:

```python
result = client.objects.TestMethods.Hello("World")
print(result)           # "Hello, World!"
```

The Object is part of an OPC UA Call; it is not intrinsic to Method identity.
Dot lookup returns a lightweight bound Method containing both the Object used
for that lookup and the Method node. A Method obtained directly by
NodeId has no lookup context, so pass the Object explicitly with `object=`. It
can be an Object node or a NodeId-like value:

```python
method = client[helloMethodNodeId]
result = method("World", object=client.objects.TestMethods)
```

`addReference` only adds an address-space edge. It does not change which
callback a Method uses or mutate the Method node. If the same Method is
referenced from several Objects, every dot lookup receives its own binding and
therefore calls it with the correct Object.

Methods that take no inputs are invoked with an empty call:

```python
client.objects.TestMethods.GetCurrentTime()
```

## Async — one rule covers everything

Every call above is awaitable. Sync and async share the same syntax — just add or drop the `await`:

```python
import asyncio
from o6 import Client

async def main():
    client = Client("opc.tcp://localhost:4840")
    await client.connect()

    # Read
    value = await client.objects.MyVariables.MyInteger()

    # Write
    await client.objects.MyVariables.MyInteger(42)

    # Call
    greeting = await client.objects.TestMethods.Hello("World")

    # Browse (also awaitable)
    node = await client.objects.MyVariables.MyInteger

    await client.disconnect()

asyncio.run(main())
```

Under the hood, a sync call on a `Client` schedules a coroutine on the client's background loop and blocks the caller; an `await` on the same expression suspends until the result is available. The dot syntax, bracket syntax, and call syntax are identical in both modes — only the `await` keyword changes.

---

# Interactive completion

The Node API is designed to be driven from a Python REPL (the standard `>>>` prompt, IPython, or any IDE / notebook that uses Jedi for completion):

- `client.objects.<TAB>` shows the children of the `Objects` folder.
- After a child is resolved, `<TAB>` on it shows *its* children, and so on.
- `dir(node)` returns the same names explicitly.
- Type hints on `Node` (via the bundled `.pyi` stubs) let your editor autocomplete the `attr=` keyword, the `value=` keyword for writes, and the available `o6.AttributeId` values.

```python
>>> from o6 import Client
>>> client = Client("opc.tcp://localhost:4840")
>>> client.connect()
>>> client.objects.<TAB>
# Lists the children of the Objects folder:
#   MyVariables  TestMethods  Server  ...
>>> client.objects.MyVariables.<TAB>
# Lists the children of the MyVariables object:
#   MyInteger  MyString  ...
>>> client.objects.MyVariables.MyInteger.<TAB>
# Lists the Node API members on the resolved node:
#   nodeid  value  ...
>>> client.objects.MyVariables.MyInteger(attr=<TAB>
# Lists the AttributeId enum members:
#   NODEID  NODECLASS  BROWSENAME  DISPLAYNAME  VALUE  ...
```

The dotted navigation fetches and caches child nodes on demand; the first `<TAB>` after connecting pays a single `Browse` round-trip, subsequent `<TAB>` presses on the same node are served from the cache.

> **Tip:** `dir(node)` returns a list synchronously, even though the children are resolved from the server. It is implemented with `asyncio.run_coroutine_threadsafe` against the client's background loop, so it works in a regular interactive shell without `await`.

---

# Putting it together

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
    # browse (dot and bracket)
    var = client.objects.MyVariables.MyInteger
    method = client.objects["TestMethods/Hello"]

    # read
    print("before:", var())

    # write
    var(7)

    # read again
    print("after: ", var())

    # call
    greeting = method("o6")
    print("call:  ", greeting)
```

Expected output (values will differ):

```text
before: 0
after:  7
call:   Hello, o6!
```

## Quick reference

| Operation | Node API | Equivalent service call |
|---|---|---|
| Browse by name | `node.child` | `Browse` |
| Translate path | `node["a/b/c"]` | `TranslateBrowsePathsToNodeIds` |
| Read value | `node()` | `Read` of `Value` |
| Read attribute | `node(attr="BrowseName")` | `Read` of the given attribute |
| Write value | `node(42)` | `Write` of `Value` |
| Write attribute | `node(value=..., attr=...)` | `Write` of the given attribute |
| Read via property | `var.value` | `Read` of `Value` |
| Call method | `parent.MyMethod(arg1, arg2)` | `Call` |
| Async variant | `await …` (same syntax) | — |
| List children | `dir(node)` / `<TAB>` | `Browse` |

For the underlying service calls (when you need full control over the request payload), see the [Client](../client.md) and [Service API reference](../api_reference/index.md).
