# Callback Binding & Overrides

Choose which callback supplies behavior when types, containing Objects, and
runtime overrides all contribute. For callback inputs and results, see
[Callbacks & External Data](../server/callbacks.md).
These are reference fragments using the declarations, implementations, and
configured server from [Implementing Declared Types](implementing-types.md).
Substitute your application's node handles and callback functions where named.

## Methods

### Binding a target

`@o6.call(target)` takes the UA Method's BrowseName. A bare name is resolved against the Methods the type declares or inherits:

```python
@o6.call("Increment")                                  # resolved for you
@o6.call("ns=tutorial;Increment")                       # explicitly qualified
```

Use the qualified form when the type declares or inherits Methods with the
same local name in different namespaces. An ambiguous bare name raises
`TypeError` with the qualifying names; a bare name does not mean namespace zero.

For an undecorated implementation, `server.implement(Declaration, Implementation)`
checks direct Method targets during registration. An unknown target raises
`TypeError` there, before an instance is created:

```
TypeError: Broken._x uses @o6.call for unknown UA Method 'ns=0;Rset';
declare or inherit that Method child
```

If you construct the implementation directly without registering it, the same
check occurs during construction. Callbacks on a decorated declaration are
checked when the declaration is decorated.

A *dotted target* reaches a Method on a nested child. The path is made of Python member names, not BrowseNames:
In this alternative declaration fragment, `ControllerType` stands for a
previously declared ObjectType with a `reset` Method, and `demo` is your
registered namespace.

```python
@o6.objecttype(ns="demo", browseName="CellType")
class CellType(ns0.objtypes.BaseObjectType):
    controller: ControllerType = o6.hasComponent(ControllerType())


class CellImpl(CellType):
    @o6.call("controller.reset")
    def _reset_controller(self) -> tuple[o6.StatusCode, o6.Boolean]:
        return (o6.StatusCode.GOOD, o6.Boolean(True))
```

An outer type can own behavior that spans its children: the cell decides what resetting its controller means, and the controller type needs no implementation. The path is resolved once, when the containing Object finishes construction, and the callable is stored on that instance's Method node. Calls never browse the address space.

!!! warning
    A dotted path traverses Objects. A segment naming a complex Variable child fails construction with `a construction owner must be an Object or ObjectType`. Implement the VariableType itself instead (see [Variables](implementing-types.md#variables)).

### Overriding in a subclass

An ordinary Python override (same method name, new body) needs no decorator. Repeat `@o6.call(...)` only when the Python name changes:

```python
class AuditedCounterImpl(CounterImpl):
    @o6.call("Increment")
    def _increment_with_audit(self, step: o6.Int32):
        self.log(step)
        return super()._increment(step)
```

Two Python methods in one class must not target the same UA Method. Target
validation rejects the conflict and reports both Python names.

The annotation of a parameter such as `step: o6.Int32` documents the input; it
does not convert it. Integer inputs arrive as fixed-width NumPy scalars of the
declared DataType, here `numpy.int32`, whose arithmetic wraps around at that
width with only a NumPy `RuntimeWarning`. Use `int(step)` for range checks and
arithmetic that must not overflow, and return values of the declared output
type.

---

## Replacing a single slot at runtime

`call=`, `read=` and `write=` set one slot on one concrete node, or on a VariableType as a template for future Variables of that type and its subtypes:

```python
server.implement(method, call=divide)                      # one Method node
server.implement(machine.temperature, read=instance_read)   # one Variable
server.implement(TemperatureType, read=type_read)           # future Variables of that type
```

These are fragments using plain functions with the signatures introduced in
[Callbacks & External Data](../server/callbacks.md). Their first parameter is
the node; path-decorated methods instead receive their containing Object as
`self`.

### Clearing, resetting, or storing a value

The position of `None` and the target determine the operation:

| Call | Effect |
|---|---|
| `server.implement(variable, write=None)` | Clears the write slot, leaving a callback-backed Variable read-only. |
| `server.implement(variable, read=None)` | Attempts to clear the read slot; rejected if the Variable would lose its readable value source. |
| `server.implement(method, call=None)` | Clears the Method callback; subsequent calls return `BAD_NOT_IMPLEMENTED`. |
| `server.implement(variable, None)` | Re-resolves callbacks from its type and containing Objects. |
| `server.implement(method, None)` | Re-resolves declared behavior; an `addMethod` callback is cleared because it has no declaration to restore. |
| `server.implement(variable, o6.Double(20))` | Removes both callbacks and stores the supplied value in native storage. |
| `server.implement(Declaration, None)` | Removes the Python class binding for future instances; existing instances keep their classes. |

A keyword clear does not reveal an earlier callback or repeat resolution.
Removing a concrete Variable's last callback requires the explicit-value form;
it never reads the outgoing callback to obtain a replacement value.

Changing a VariableType callback affects future Variables only. A reset uses
the type and containing-Object behavior in effect when the reset is requested.
This callback-template inheritance differs from a Python class binding with
`server.implement(Declaration, Implementation)`, which matches an exact TypeDefinition.

If positional `None` cannot resolve a read callback, it raises `TypeError`
with `use implement(variable, value) to restore it`. It cannot restore a
previous native value.

## Precedence

Initial callback resolution happens during construction. Later overrides
replace its result:

1. Start at the node's concrete type and search upwards through its bases. For Variables, each slot comes from the nearest server-local VariableType callback or Python implementation. For Methods, it comes from the Python implementation. Copy the resolved callback onto the concrete node.
2. As containing Objects finish construction, innermost first, every matching `@o6.read("path")`, `@o6.write("path")` or `@o6.call("path")` replaces that slot. An outer path therefore wins when two paths target the same node.
3. A later `Server.implement` replaces or clears the slot directly.

Invocation never searches a type hierarchy or resolves a path; it calls the callback stored on the node. Optional-member implementation annotations are described in
[Implementing Declared Types](implementing-types.md#narrowing-a-members-python-class).
Callback arguments and async execution are covered in
[Callbacks & External Data](../server/callbacks.md).

---

## Pitfalls

| Symptom | Cause |
|---|---|
| `addObject` returns the declaration class, not the implementation | `implement` not called, called after the node was created, or the node's TypeDefinition is a subtype of the registered one |
| `implementation must be undecorated; it must not declare a UA subtype` | the implementation carries `@o6.objecttype` / `@o6.variabletype` |
| `uses @o6.call for unknown UA Method 'ns=0;X'` | misspelled or undeclared target |
| a bare Method name is ambiguous across namespaces | more than one declared Method has that local name; qualify the target |
| `one Python method cannot implement two UA Methods` | two `@o6.call` decorators on one function |
| `a construction owner must be an Object or ObjectType` | a dotted `read`/`write`/`call` path traverses a complex Variable child |
| a `@o6.read("…")` never fires | the target is the Python member name, not the BrowseName |
| writes silently do nothing | a `write` callback that returns `GOOD` without storing — a callback-backed Variable has no native storage behind it |
| behavior missing on a Python-constructed instance | direct construction of the declaration class bypasses `implement` |

---
