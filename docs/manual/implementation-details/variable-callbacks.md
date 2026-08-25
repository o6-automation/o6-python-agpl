# Variable callbacks

This page describes how o6\\Python dispatches Variable read and write
operations between Python and open62541. It does not cover how to *write*
callbacks — that is the job of the [tutorials][tutorials] and the
[Server / Implementing behaviour][behaviour] manual page. The goal here is
to spell out the rules the binding follows so that a reader can answer
"why does this happen" and "what does this guarantee".

!!! info "Prerequisites"
    The user-facing pages [Server / Implementing behaviour][behaviour] and
    the [Node API tutorial][tut-node-api] describe the decorator and
    `Server.implement` API from the application's side. The rest of this
    page assumes that surface.

[tutorials]: ../../tutorials/index.md
[tut-node-api]: ../../tutorials/client/140_node-api-syntax.md
[behaviour]: ../server/behaviour.md

## Why the design is the way it is

A Variable callback must do two things at once: it must be dispatched by
the open62541 server like any other value source, and it must be
re-entrant against Python in a way that does not corrupt the C call stack.
The binding's solution is to put the callback on a *canonical* Python
object — the VariableType — and let inheritance and construction order
do the rest. The C side is reduced to a thin trampoline that
allocation-freely calls into a callable already stored on a known
`PyNode`. There is no second registry, no callback table to keep in
sync, and no Python-side dispatch fallback.

The rules that follow are the consequences of that decision.

## The canonical Variable

Every Variable is an open62541 node and a distinct Python object. The
Python object is the canonical Variable. A Variable's read and write
slots live on that object — not on a type that the binding looks up at
dispatch time, and not on a global registry the binding scans on each
call.

The decorators `@o6.read` and `@o6.write` register a method as a Variable
callback when the class is a `VariableType` declared with
`@o6.variabletype(...)`. The decorator does not transform the function;
it stores it on the class's slot. A Python subtype can override either
slot with an ordinary method:

```python
@o6.variabletype(ns="demo", nodeId="ns=demo;i=1001", dataType=o6.Double)
class TemperatureType(o6.ns.ns0.vartypes.BaseDataVariableType):
    @o6.read
    def _read(self, *, range=None, session=None, includeSourceTimestamp=False):
        return (o6.StatusCode.GOOD, self.sensor.temperature)

    @o6.write
    def _write(self, value, *, range=None, session=None):
        if value.value < 0:
            return (o6.StatusCode.BAD_OUT_OF_RANGE,)
        self.sensor.temperature = value.value
        return (o6.StatusCode.GOOD,)


class SimulatedTemperatureType(TemperatureType):
    def _read(self, **kwargs):
        return (o6.StatusCode.GOOD, self.simulatedValue)
```

`SimulatedTemperatureType._read` overrides the parent slot without
re-decorating. Override resolution is plain Python MRO.

The trampoline never performs a `UA_Server_getNodeType` call. It invokes
the callable that the resolved concrete `PyNode` already holds, on the
retained Variable object. The Python class is consulted exactly once,
during construction.

## Callback return shapes

Read and write use different return shapes because they answer different
questions.

A **read** returns `(StatusCode, value)`:

- a `Bad` status may be returned alone as `(StatusCode,)`;
- a non-`Bad` status must have exactly one value;
- a normal Python value is converted using the Variable's declared
  data type;
- an `o6.DataValue` may be returned in place of a value to set
  timestamps and picoseconds explicitly;
- the tuple's `StatusCode` is authoritative.

A **write** receives the requested `o6.DataValue` — its status,
timestamps, and other metadata are preserved — and returns exactly
`(StatusCode,)`.

The trampoline shape-checks the return value. A non-conforming return
raises a Python exception, which the binding surfaces as a `Bad`
status on the wire.

## Construction-order resolution

When an Object is constructed, its members are constructed first. The
binding resolves each Variable's read and write slot from three sources,
in this fixed order:

1. **Type lookup, walking the MRO.** The constructor walks the concrete
   implementation type and then its base types. The first matching type
   callback is copied onto the concrete node. The result is the *initial*
   slot for the variable; nothing else has run yet.
2. **Containing-Object path decorators.** `@o6.read("path.to.variable")`
   and `@o6.write("path.to.variable")` are resolved when the containing
   Object finishes. The path is resolved against the instance-declaration
   tree that the `__init__` chain has built. Each direction replaces the
   final Variable's slot. Because construction is inside-out, a path on
   an outer Object is applied *after* a path on an inner Object that
   targets the same Variable, so the outer path wins.
3. **A later `Server.implement` call.** `server.implement(variable, read=...)`
   directly replaces the slot. The constructor has already returned;
   this is a runtime override.

The three sources share one concrete slot per direction. There is no
fallback layer. Clearing an instance callback does not re-run type
lookup or Object finish; it leaves the slot empty.

A path keyword argument or a `Server.implement` keyword set to `None`
clears that direction. `None` for one of `read` or `write` clears only
that direction:

```python
server.implement(motor.temperature, read=None)   # clear only the read override
server.implement(motor.temperature, write=None)  # clear only the write override
```

Passing a bare `None` re-runs construction-time resolution for the
Variable; passing a value installs that value as native storage.

## Implementation subclassing

An undecorated implementation subclass is selected by Python type
annotation, not by UA type:

```python
class TemperatureImpl(vendor.vartypes.TemperatureType):
    @o6.read
    def _read(self, **kwargs):
        return (o6.StatusCode.GOOD, self.sensor.temperature)


class MotorImpl(vendor.objtypes.MotorType):
    temperature: TemperatureImpl
```

The annotation changes only the existing child's Python class. Its
NodeId, TypeDefinition, BrowseName, ModellingRule, and references
remain unchanged. Implementation selection composes recursively through
nested Object members. If the inherited UA declaration is `Optional`,
annotation optionality controls whether the member is constructed on
the instance:

```python
class MotorImpl(vendor.objtypes.MotorType):
    requiredTemperature: TemperatureImpl
    optionalTemperature: TemperatureImpl | None
```

The first member is included automatically in every `MotorImpl`; the
second is included only when it would have been included otherwise.
Both UA declarations remain `Optional` — the annotation is a Python
implementation guarantee, not a new UA ModellingRule.

## Runtime overrides via `Server.implement`

`Server.implement` is the one public API for installing behavior on
nodes after construction. It accepts either a VariableType or a
concrete Variable, and either or both of `read=` and `write=`:

```python
# Type-level: affects only Variables created from this type afterwards.
server.implement(TemperatureType, read=read_temperature)

# Instance-level: overrides one specific Variable.
server.implement(motor.temperature, read=read_simulated_temperature)
```

Type overrides are local to one server and are copied into future
instances. They do not modify existing Variables — the callback is
copied onto each concrete Variable during construction, so no instance
scan is needed when a type override changes.

The same `read=` / `write=` keyword convention applies: `None` clears
exactly that stored slot, except that a concrete Variable cannot be
left with no value source.

## Source-of-value rules

The two resolved slots together select one value source:

- **no read and no write callback** — use the native value stored in the
  `UA_VariableNode`;
- **a read callback, with or without a write callback** — use the Python
  callback source;
- **a write callback without a read callback** — invalid; rejected at
  construction.

The last case is invalid because open62541 requires every callback
value source to be readable. Native storage is not a fallback for a
missing direction once a callback source is active: without a write
callback, the Variable is read-only.

`variable()` and `variable(value)` are the call-syntax shortcuts for
the read and write services. They go through the same dispatch path as
every other access; they do not bypass a read callback, and they do
not bypass a missing write callback to reach native storage.

## Native value invariant

An empty value is legal only when the Variable's `DataType` is
`BaseDataType` (a `Variant`). For every other concrete datatype,
open62541 creates a default value while adding the node when none is
supplied: a zero-initialized scalar, or an empty array carrying the
declared element type.

Installing a callback source clears that native value. Returning to
native storage therefore requires an explicit `DataValue` or typed
value. o6\\Python passes the new value directly to
`UA_Server_setVariableNode_internalValueSource`; it never invokes the
outgoing read callback. There is no snapshot, no rollback state, and
no shadow value.

A Variable may not switch storage from inside its own active callback.
Replacing the node would invalidate the dispatching native pointer the
trampoline is using. The native side rejects the transition in that
case.

A write callback may be copied together with an inherited read
callback, but a write-only callback on an otherwise native Variable is
rejected at construction. The reason is the same as the
source-of-value rule: a write-only callback would leave the Variable
unreadable through the callback path, and open62541 will not accept
that.

## Reentrancy and the trampoline contract

Variable callbacks are synchronous. The underlying open62541 value
operation is synchronous, and making a synchronous read or write
asynchronous from inside the binding would require an entirely
different cancellation model.

The native trampoline keeps an allocation-free thread-local stack of
active `UA_Node *` pointers. Re-entering the same read, or the same
write, returns `BadInvalidState` before Python is called. Read and
write share the Variable's single pointer key, so the converse
operation is rejected as well. A longer cycle is stopped when it
reaches an already-active node.

The keyword-only arguments to a callback describe the current UA
operation:

- `range` is `None` for a full value or a tuple of stop-exclusive
  slices;
- `session` identifies a client operation and is `None` for an
  internal one;
- `includeSourceTimestamp` is present only for reads.

The arguments are forwarded unchanged to path-decorated callbacks and
to runtime-installed callables. There is no separate keyword set for
runtime-installed callables.

## What lives where

| Location | What it stores |
| --- | --- |
| Concrete `VariableNode` | The active `read` callable (or `None` for native storage) and the active `write` callable (or `None`). |
| Canonical `VariableTypeNode` | The current type-level `read` and `write` overrides installed via `Server.implement`; the Python class for instances. |
| Python class | The decorator slots from `@o6.read` / `@o6.write`, plus plain overridden methods. |
| C trampoline | The thread-local reentrancy stack and the call into the resolved concrete `PyNode` callable. |

There is no global Python registry of callbacks. There is no second
index. The trampoline resolves the callable by reading the concrete
`PyNode` field that was populated during construction. The Python
class is consulted exactly once, when the node is built; runtime
replacement is a write to that same field.

## See also

- [Server / Implementing behaviour](../server/behaviour.md) — the
  user-facing description of the callback API.
- [Node API](../node-api.md) — the `o6.Node` projection that callbacks
  operate through.
- [Memory management](memory-management.md) — the
  ownership rules that keep callback lifetimes aligned with their
  owning server.
- [Variable callback tests][tests-variable-callback] — the test
  coverage for the rules in this page.

[tests-variable-callback]: https://github.com/o6-automation/o6-python/blob/main/tests/server/test_variable_callback.py
