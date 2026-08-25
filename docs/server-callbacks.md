# Server callbacks

`Server.implement` installs server-local Python behavior. With a UA type and
an implementation subclass it selects how future instances are constructed.
With `call=`, `read=`, or `write=` it replaces a callback slot on a Method,
Variable, or VariableType. Existing instances are never rewritten by a
type-level change.

Every callback starts with the node being acted on. Variable callbacks
additionally receive operation metadata as keyword arguments.

## One resolution rule

`read`, `write`, and `call` choose their callbacks in exactly the same way.
When a node is created, o6 starts at its concrete Python implementation type
and searches upwards through its base types. The first matching callback is
copied onto the concrete Variable or Method node. Then the containing Objects
finish from the inside out: every matching `@o6.read("path")`,
`@o6.write("path")`, or `@o6.call("path")` replaces that concrete slot. An
outer path therefore wins if several paths target the same node. A later
`Server.implement` replaces or clears the same slot directly.

That is the entire precedence model: **nearest type first, then path callbacks
in finish order, then explicit runtime changes**. Invocation never searches a
type hierarchy or resolves a path; it calls the callback already stored on the
concrete node. Passing `None` clears that slot and does not reveal or recompute
an earlier callback. A runtime callback placed on a VariableType is a template
for Variables created afterwards and does not modify existing Variables.

Read and write are separate slots on one Variable, whereas a Method has one
call slot. This is the only resolution difference between the three.

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
the order of the Method's `InputArguments` and `OutputArguments`. A bad status
may be returned alone. A non-Bad status must be followed by exactly the declared
number of outputs. Application state belongs on `node` or in a closure; Methods
have no callback context or registration context.

Method callbacks may be synchronous or `async def`; both forms have exactly the
same positional arguments and result-tuple behavior.

OPC UA Call identifies both the Object and the Method. Callback ownership
follows the Method node while `node`/`self` follows the individual invocation.

Pending async calls are represented by GC-tracked state owned by the server and
referenced by the asyncio Task. Cancellation resolves the native output pointer
against that server-owned state; there is no process-global callback registry.

### Methods declared on ObjectTypes

A Method declared by an ObjectType gets its Python behavior when its Object is
created:

- `@o6.call(...)` associates the qualified UA BrowseName with an ordinary
  Python instance method.
- Object creation selects the implementation from the Object's concrete Python
  type and stores it on the copied Method node.
- A subtype that does not override the Method inherits the nearest base
  implementation.
- A subtype may repeat `@o6.call(...)` on a differently named Python method;
  that nearest association wins.
- Per-object state belongs directly on the Object; it does not require a
  separate Method callback.

o6 configures open62541 to copy every Method declaration into each Object
instance. Mandatory and selected Optional Methods therefore have an independent
Method NodeId and callback slot. Construction checks the concrete Python class
first and proceeds upwards through its base classes only on a miss. Invocation
uses the callback already stored on the Method. There is one dispatcher and no
UA type query or global callback registry.

A dotted target binds behavior from a containing Object to a nested Method:

```python
class CellImpl(CellType):
    @o6.call("controller.reset")
    def resetController(self, mode):
        return (o6.StatusCode.GOOD,)
```

The target is a path of generated Python member names. It is resolved once when
the containing Object finishes and stored directly on that instance's Method
node together with its containing Object. Calls never browse the address space,
and instances remain independent.

The same simple rule decides every `read`, `write`, and `call` callback during
construction. First, search the concrete implementation type and then its base
types; copy the first matching callback onto the concrete target node. Then
apply dotted paths as containing Objects finish, replacing that slot. Nested
Objects finish before their containers, so an outer path targeting the same
node is applied last. Invocation performs no type or path lookup.

Optional Methods follow the same rule. Enabling one creates an independent
Method node from its declaration. An ordinary server Method retains its
construction Object and dot lookup through that Object returns the Method node
itself. A parentless Method, or the same Method reached through an additional
`Server.addReference` edge, uses a lightweight bound value for that call.

### Method resolution

Every Method node has at most one Python callback. There is no separate
"override" and "default" callback:

1. Search the Object's concrete Python type and then upwards through its base
   types; store the first matching `@o6.call(...)` implementation on the Method.
2. Apply dotted paths as the instance tree finishes; each path replaces the
   callback on its concrete target Method.
3. At invocation, call the stored callback or return `BAD_NOT_IMPLEMENTED`.

`Server.implement(method, call=callback)` sets the one callback on exactly the
given Method node. Passing `None` clears it; class and path resolution are not
repeated. Changing a class or ObjectType declaration affects future instances,
not Method nodes already created.

```python
class ConnectionManagerImpl(fx_cm.objtypes.ConnectionManagerType):
    @o6.call("ns=fx_cm;EditConnectionConfigurationSets")
    def edit_sets(self, action, sets):
        ...


class AuditedConnectionManagerImpl(ConnectionManagerImpl):
    @o6.call("ns=fx_cm;EditConnectionConfigurationSets")
    def edit_sets_with_audit(self, action, sets):
        ...
```

The second decorator deliberately changes the Python implementation name. If
the name stays `edit_sets`, an ordinary undecorated Python override is enough.
Two decorators on the same class may not target the same qualified UA Method;
class creation reports both competing Python names. Misspelled targets are
reported as unknown instead of becoming silently unreachable implementations.

## Variables

```python
@o6.variabletype(ns="demo", nodeId="ns=demo;i=1001", dataType=o6.Double)
class TemperatureType(o6.ns.ns0.vartypes.BaseDataVariableType):
    @o6.read
    def _read(self, *, range, session, includeSourceTimestamp):
        return (o6.StatusCode.GOOD, self.device.currentTemperature)

    @o6.write
    def _write(self, value, *, range, session):
        if value.value < 0:
            return (o6.StatusCode.BAD_OUT_OF_RANGE,)
        self.device.currentTemperature = value.value
        return (o6.StatusCode.GOOD,)
```

A read callback has the signature
`(self, *, range, session, includeSourceTimestamp) -> (StatusCode, value)`.
A Bad status is returned alone. A successful result has exactly one Python
value, converted using the Variable's declared datatype, or an `o6.DataValue`
when timestamps and picoseconds must be supplied explicitly.

A write callback has the signature
`(self, value, *, range, session) -> (StatusCode,)`. `value` is the requested
`o6.DataValue`. Variable callbacks are synchronous.

Synchronous callback dispatch rejects recursion with `BadInvalidState`. A
Variable cannot re-enter the same read or write callback, and a Method cannot
re-enter the same concrete Method node. The invoking Object is irrelevant to
this check. Any nested callback on the same Variable is rejected, including a
read calling write or a write calling read. Independent nodes are unaffected.
Async Method execution is not guarded after the callback has returned its
coroutine.

The decorators return the original methods. A Python subtype overrides `_read`
or `_write` normally and needs no second decorator. Application state belongs
directly on the Variable; there is no callback registration context.

### Implementing an existing companion type

Generated companion modules describe the UA interface and remain unchanged.
Define behavior in an undecorated subclass and bind the pair explicitly to one
server:

```python
from o6.ns.vendor.objtypes import MotorType
from o6.ns.vendor.vartypes import TemperatureType


class TemperatureImpl(TemperatureType):
    @o6.read
    def _read(self, **kwargs):
        return (o6.StatusCode.GOOD, self.device.temperature)


class MotorImpl(MotorType):
    temperature: TemperatureImpl

    @o6.call("Start")
    def start(self):
        return self.backend.start()


server.ns.append(o6.ns.vendor)
server.implement(MotorType, MotorImpl)
```

The binding is stored on the `MotorType` node in that server's own nodestore.
Since every server owns a distinct type node, the binding is naturally
server-specific and needs no separate registry. Register it before accepting
node creation. Objects subsequently created through `Server.addObject`, native
APIs, or a client's AddNodes request are exposed as `MotorImpl`; the global
node constructor applies its member annotations and decorators after native
type instantiation has completed. Its early phase creates selected member
implementations first; its normal phase runs `__init__` once and installs
callbacks after the complete Mandatory subtree exists.

The binding matches that exact UA TypeDefinition. Register companion subtypes
explicitly with their own implementation classes. Passing `None` restores the
declaration's own Python type for future instances without changing existing
Objects or Variables:

```python
server.implement(MotorType, None)
```

For direct Python construction, instantiate `MotorImpl(...)`. Calling
`MotorType(...)` explicitly retains the generated Python class; the server
binding is for nodes entering through native type instantiation.

Member implementations stay scoped. The annotation above makes
`motor.temperature` a `TemperatureImpl`, but an independently created
`TemperatureType` uses its generated Python class. Bind that separately when
global behavior is wanted:

```python
server.implement(TemperatureType, TemperatureImpl)
```

The first argument must be a generated or decorated ObjectType/VariableType;
the second must be its undecorated subclass. Repeating the same pair is
harmless. A competing pair on the same server is rejected. The binding does
not publish a UA subtype or change any companion metadata.

Normal Python `__init__` is also called for nodes originating in native code or
over AddNodes. The node is already complete before the initializer runs in
both paths; `super().__init__()` only continues ordinary Python initializer
inheritance. An AddNodes request carries no Python-only
arguments, so a class registered with `Server.implement` must provide defaults
for such arguments or obtain dependencies from server/node state.

An Object implementation can select a Python-only implementation class for an
inherited Variable member:

```python
class TemperatureImpl(TemperatureType):
    @o6.read
    def _read(self, **kwargs):
        return (o6.StatusCode.GOOD, self.device.currentTemperature)


class MachineImpl(vendor.objtypes.MachineType):
    temperature: TemperatureImpl
```

This changes only the concrete Python class. The Variable keeps its standard
UA TypeDefinition and all address-space metadata. The same annotation rule
composes through nested Object implementations.

For an inherited Optional UA member, `temperature: TemperatureImpl` includes
the member in every instance constructed as that implementation, whereas
`temperature: TemperatureImpl | None` leaves it optional. The UA declaration
and its ModellingRule remain unchanged.

A member-specific callback can instead be installed when an Object is
constructed:

```python
class MachineImpl(vendor.objtypes.MachineType):
    @o6.read("parameterSet.temperature")
    def _read_temperature(self, *, range, session, includeSourceTimestamp):
        return (o6.StatusCode.GOOD, self.device.readTemperature(range))

    @o6.write("parameterSet.temperature")
    def _write_temperature(self, value, *, range, session):
        self.device.writeTemperature(value.value, range)
        return (o6.StatusCode.GOOD,)
```

The string uses Python member names. When the containing Object finishes, o6
resolves it once and stores the callable with its containing Object in that
concrete Variable direction, replacing behavior copied from its VariableType.
Nested Objects finish before their containers, so an outer path targeting the
same Variable is applied last. Every operation keyword, including `range`, is
forwarded unchanged; invocation does not traverse the path. Missing paths and
non-Variable targets fail construction.

`range` is `None` for a complete value or a tuple of stop-exclusive Python
slices. For example, OPC UA range `2:5` becomes `(slice(2, 6),)`. `session` is
an `o6.Session` for client operations and `None` for internal operations.

### Runtime Variable overrides

Read and write can be overridden independently on one Variable or for a
VariableType and its subtypes:

```python
server.implement(TemperatureType, read=type_read)
server.implement(machine.temperature, read=instance_read)
```

During construction, each direction is copied from the nearest server-local or
Python VariableType implementation. A path decorator then replaces the same
concrete slot during Object finish. Keyword arguments replace individual slots:

```python
server.implement(machine.temperature, read=None)
server.implement(TemperatureType, read=None)
```

Removing the final callback from a concrete Variable needs an explicit whole-node
choice. Positional `None` repeats construction-time resolution; a positional
value switches to native storage without calling the old read callback:

```python
server.implement(machine.temperature, None)
server.implement(machine.temperature, o6.Double(20))
```

Changing a VariableType callback affects future Variables only. Reset uses the
type and containing-object behavior that apply when reset is requested.

The stored read and write slots select the value source together. If neither
slot is present, the Variable uses its native stored value. If a read slot is
present, the Variable uses Python callbacks; without a write slot it is
read-only. A write slot without a read slot is rejected because open62541
callback value sources must be readable.

Variable call syntax uses exactly that resolved source. `variable()` performs a
normal Value read and `variable(value)` performs a normal Value write; neither
form bypasses callbacks to reach native storage.

Once a Variable becomes callback-backed, its callbacks own the value state; o6
does not keep a shadow value.

Native Variables with a concrete datatype always have a value. When none is
provided during creation, open62541 supplies a zero-initialized scalar or a
typed empty array. A truly empty value is legal only for `BaseDataType`
(`Variant`), which is the datatype normally used by `BaseVariableType`.

## ObjectType and VariableType initialization

```python
@o6.objecttype(ns="demo", nodeId="ns=demo;i=1001")
class MachineType(o6.ns.ns0.objtypes.BaseObjectType):
    def __init__(self, *, device, **kwargs):
        super().__init__(**kwargs)
        self.device = device

    def __del__(self):
        self.device.close()
```

Declared ObjectTypes and VariableTypes use ordinary Python construction. Their
`__new__` completes OPC UA node construction first, then invokes the application
initializer on the fully usable node. `super().__init__(...)` is therefore only
the normal cooperative Python initializer call; it performs no OPC UA work.
Initializers inherit through the Python type hierarchy normally.

Python finalization is inherited normally as well. The server's nodestore
reference keeps the Python object alive while the OPC UA node exists. After the
node is removed, any remaining Python references may delay `__del__`, so use it
for Python-owned resources rather than protocol actions that must occur at the
exact instant of OPC UA deletion.
