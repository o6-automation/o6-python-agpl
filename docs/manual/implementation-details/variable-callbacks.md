# Variable callbacks

Use this page to understand how Variable callbacks are stored and dispatched
between Python and open62541. It assumes the application contracts in
[Callbacks & External Data](../server/callbacks.md) and
[Callback Binding & Overrides](../information-model-authoring/callback-binding.md).

## The canonical Variable

Every Variable is an open62541 node and a distinct Python object. The Python
object is the canonical Variable and holds the read and write slots. The
binding does not look them up on a type or in a global registry at dispatch
time.

The VariableType's server-local Python object holds callback templates for
future instances. The concrete Variable holds the resolved callables used at
runtime. These are distinct roles; dispatch reads the concrete node's slots.

The C trampoline invokes those callables on the retained Python object. It
does not repeat type lookup or browse a member path for each operation.

## Construction and replacement

Children are constructed before their containing Object's Python initializer
runs. Callback resolution uses the declared member tree and the selected
implementation classes. The public
[precedence rules](../information-model-authoring/callback-binding.md#precedence)
describe how type callbacks and containing-Object paths populate the concrete
slots.

All sources write to the same slot per direction. There is no stack of earlier
callbacks underneath a runtime replacement. The exact clear, reset, and
native-value forms are defined in
[Clearing, resetting, or storing a value](../information-model-authoring/callback-binding.md#clearing-resetting-or-storing-a-value).

## Result conversion

The trampoline validates the
[callback result tuple](../server/callbacks.md#variables) before converting it.
A malformed result becomes a Bad status on the wire. A normal read value is
converted as a Variant; an explicit DataValue is converted with its metadata.
The tuple's status is then written into the outgoing DataValue.

## Native value invariant

An empty value is legal only when the Variable's `DataType` is
`BaseDataType` (a `Variant`). For every other concrete data type, open62541
creates a default value when the node is added without one: a zero-initialized
scalar, or an empty array with the declared element type.

Installing a callback source clears the native value. To return to native
storage, pass an explicit `DataValue` or typed value. o6\\Python passes it
directly to `UA_Server_setVariableNode_internalValueSource` and never invokes
the outgoing read callback. There is no snapshot, rollback state or shadow
value.

A Variable cannot switch storage from inside its own active callback, because
replacing the node would invalidate the native pointer the trampoline is
using. The native side rejects the transition.

A write callback can be copied together with an inherited read callback. A
write-only callback on an otherwise native Variable is rejected at
construction: a callback value source must be readable. See
[Value sources](../server/callbacks.md#value-sources).

## Reentrancy and the trampoline contract

The [public callback contract](../server/callbacks.md#variables) defines sync
completion and async Task scheduling. Native cancellation and server cleanup
cancel the Task and invalidate its native result storage before Python resumes.

During initial dispatch, the trampoline keeps an allocation-free thread-local
stack of active `UA_Node *` pointers. Re-entering the same read or write
returns `BadInvalidState` before Python is called. Read and write share the
Variable's pointer key, so the converse operation is rejected too. A longer
synchronous cycle stops when it reaches an already-active node. A scheduled
async callback runs outside this initial dispatch stack.

## What lives where

| Location | What it stores |
| --- | --- |
| Concrete `VariableNode` | The active `read` callable (or `None` for native storage) and the active `write` callable (or `None`). |
| Canonical `VariableTypeNode` | The current type-level `read` and `write` overrides installed via `Server.implement`; the Python class for instances. |
| Python class | The decorator slots from `@o6.read` / `@o6.write`, plus plain overridden methods. |
| C trampoline | The thread-local reentrancy stack and the call into the resolved concrete `PyNode` callable. |

There is no global Python callback registry or second index. The trampoline
reads the callable from the concrete `PyNode` field populated during
construction. Runtime replacement writes to that same field.

## Related topics

| Topic | What it covers |
|---|---|
| [Callbacks & External Data](../server/callbacks.md) | Callback signatures, results, and value sources. |
| [Callback Binding & Overrides](../information-model-authoring/callback-binding.md) | Target selection, precedence, and reset operations. |
| [Node API](../node-api/index.md) | The `o6.Node` objects callbacks operate on. |
| [Memory management](memory-management.md) | The ownership rules that tie callback lifetimes to their server. |
