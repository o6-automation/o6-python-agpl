# Callbacks & External Data

Use Python callbacks to implement Methods or obtain Variable values from an
external source. `server.implement(node, call=..., read=..., write=...)` installs
callbacks on existing nodes. The snippets assume a configured `server`.

Keep blocking device I/O off the server loop. The
[slow device read example](timers.md#slow-device-reads) shows how to obtain
values in a worker thread and publish them without overlapping device calls.

## Methods

```python
def divide(node, dividend, divisor):
    if divisor == 0:
        return (o6.StatusCode.BAD_INVALID_ARGUMENT,)
    return (o6.StatusCode.GOOD, dividend / divisor)

server.implement(method, call=divide)
```

The callback signature is:

```python
(node, *inputs) -> (o6.StatusCode, *outputs)
```

`node` is the Object on which the Method was invoked. Inputs and outputs follow
the order of the Method's `InputArguments` and `OutputArguments`. A Bad status
can be returned alone. A non-Bad status must be followed by exactly the declared
number of outputs. Keep application state on `node` or in a closure; Methods
have no callback context or registration context.

Method callbacks can be synchronous or `async def`, with the same positional
arguments and result tuples.

An OPC UA Call identifies both the Object and the Method. The callback belongs
to the Method node; `node`/`self` is the Object of the individual invocation.

## Variables

This complete example keeps the value in application state and installs ordinary
Python functions on a Variable:

```python
import o6

state = {"temperature": 20.0}

def read_temperature(node, *, range, session, includeSourceTimestamp):
    return (o6.StatusCode.GOOD, o6.Double(state["temperature"]))

def write_temperature(node, value, *, range, session):
    state["temperature"] = float(value.value)
    return (o6.StatusCode.GOOD,)

with o6.Server(port=4840) as server:
    temperature = server.addVariable("Temperature", server.objects, 20.0)
    server.implement(temperature, read=read_temperature, write=write_temperature)
    temperature(23.5)
    print(temperature())  # 23.5
```

The functions receive the node as their first argument. An implementation class
receives the same node as `self`; see
[Implementing Declared Types](../information-model-authoring/implementing-types.md).

A read callback has the signature
`(self, *, range, session, includeSourceTimestamp) -> (StatusCode, value)`.
A Bad status is returned alone. A non-Bad result has exactly one value: a
Python value with the appropriate OPC UA type, or an `o6.DataValue` when you
supply timestamps and picoseconds explicitly. Ordinary values use
[type inference](../sdk-fundamentals/builtin/primitive-types.md#choosing-a-values-type);
return `o6.Float(...)` for a Float Variable, for example. The tuple's status
overrides any status in a returned `DataValue`.

A write callback has the signature
`(self, value, *, range, session) -> (StatusCode,)`. `value` is the requested
`o6.DataValue`. Read and write callbacks can also be `async def`, with the same
arguments and result tuples.

An async call, read or write callback runs in an asyncio Task from its start.
o6\\Python keeps the native operation pending until the Task finishes, even
when the callback returns without awaiting. Use an ordinary `def` callback for
immediate synchronous completion. Native cancellation, including server
cleanup, cancels the Task and its current await.

Synchronous callback dispatch rejects recursion with `BadInvalidState`:

- A Variable cannot re-enter its own read or write callback. This includes a
  read calling write and a write calling read.
- A Method cannot re-enter the same concrete Method node, whichever Object
  invokes it.
- Independent nodes are unaffected.
- A suspended async callback is not guarded after it has returned to the native
  dispatcher.

`range` is `None` for a complete value, or a tuple of stop-exclusive Python
slices. For example, OPC UA range `2:5` becomes `(slice(2, 6),)`. `session` is
an `o6.Session` for client operations and `None` for internal operations.

## Value sources

The read and write slots together select the value source:

| Read slot | Write slot | Value source |
|---|---|---|
| No | No | Native stored value |
| Yes | No | Python callbacks, read-only |
| Yes | Yes | Python callbacks |
| No | Yes | Rejected: open62541 callback value sources must be readable |

`variable()` performs a normal Value read and `variable(value)` a normal Value
write through that source. Neither bypasses callbacks to reach native storage.
A callback-backed Variable keeps no shadow value; its callbacks own the state.

Native Variables with a concrete DataType always have a value. When you provide
none at creation, open62541 supplies a zero-initialized scalar or a typed empty
array. An empty value is legal only for `BaseDataType` (`Variant`), the
DataType normally used by `BaseVariableType`.

## Calling the API from callbacks

A synchronous SDK callback gets immediate local results: `value = node()`
works when the operation completes inline. If the operation needs more work on
the same event loop, it returns an awaitable without blocking. A callback that
needs that result before continuing must use `async def` and `await`. This also
applies when a synchronous callback is invoked inside an async operation. Async
callbacks, tasks started by callbacks, and synchronous helpers called by an
async task always use the async contract.

This includes application-notification handlers, timers, and local
monitored-item callbacks. A plain handler has the synchronous callback
contract; an `async def` handler has the async contract. Neither can block
the owning loop while waiting for pending work on that same loop.

```python
async def read(node, **kwargs):
    value = await other_variable()
    return o6.StatusCode.GOOD, o6.DataValue(value=value)
```

Node creation helpers and dynamic child navigation follow the same rule. Async
callbacks await them even when the result is already available. Metadata
properties, Python constructors and synchronous configuration APIs stay
ordinary Python operations.

## Replacing behavior

Replace a concrete node's callback with `server.implement(variable, read=...)`
or `server.implement(method, call=...)`. A callback-backed Variable needs a read
callback; a write callback alone is invalid. To switch a Variable back to stored
values, supply an explicit value:

```python
server.implement(temperature, o6.Double(20.0))
```

Type bindings, member paths, and the distinction between clearing one slot and
resetting a whole node are covered in
[Callback Binding & Overrides](../information-model-authoring/callback-binding.md).
