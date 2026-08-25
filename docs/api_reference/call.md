# call

Canonical path: `o6.call`

With keyword arguments, `o6.call(...)` declares an OPC UA Method child. With
a positional target, `@o6.call("BrowseName")` binds an implementation to
a declared or inherited Method child on an ObjectType or on an undecorated
Python implementation subclass.

A dotted positional target is a Python member path. It is resolved once when
the containing Object finishes, and stores the implementation with that Object
on the concrete Method node:

```python
class CellImpl(CellType):
    @o6.call("controller.reset")
    def resetController(self, mode):
        return (o6.StatusCode.GOOD,)
```

The path uses generated Python member names, not OPC UA BrowseNames. It
overrides behavior copied from the Method's type implementation. As with
`read` and `write` paths, clearing a callback later does not rerun Object
construction or restore an earlier callback.

Resolution happens once during Object creation. The most-derived matching type
implementation is copied onto the concrete Method first. Dotted paths are then
applied as containing Objects finish, replacing that concrete slot. Nested
Objects finish before their containers, so an outer path that targets the same
Method is applied last.

The creation-time class lookup starts at the Object's concrete Python type and
proceeds upwards through its base types. A subclass can override the same
Python method normally, or repeat `@o6.call("BrowseName")` on a different
Python method name. Invocation performs no class or path lookup: it calls the
stored callback, or returns `BAD_NOT_IMPLEMENTED`.

Every Object instance owns copies of its Mandatory and selected Optional
Methods. Per-instance callbacks are therefore isolated while both cases use the
same construction-time resolution.

The invoking Object is part of the call, not part of Method identity. Dot
lookup returns a lightweight bound Method containing the Object and Method node
for that lookup:

```python
machine.Reset()
```

Each lookup has its own Object, on clients and local servers alike. For a
Method obtained directly by NodeId, pass the Object explicitly. It may be a
node or a NodeId-like value:

```python
reset = client[resetNodeId]
reset(object=machine)
```

Adding a reference never changes callback ownership.

Each class may associate only one Python method with a given qualified UA
BrowseName. Competing `@o6.call(...)` decorators raise `TypeError` naming the
class, UA Method, and both Python attributes. A decorator that matches no
declared, inherited, or interface Method is also rejected as an unknown UA
Method. Multiple inheritance is not ambiguous: normal Python type-hierarchy
order selects the nearest base implementation.

See [Server callbacks](../server-callbacks.md#one-resolution-rule) for the
shared `read`/`write`/`call` precedence and reset behavior.
