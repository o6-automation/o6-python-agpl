# Server

See [Server callbacks](server-callbacks.md) for Method, Variable, ObjectType,
and VariableType callback signatures and status handling.

## Declared type instance ownership

Calling an `@o6.objecttype` or `@o6.variabletype` class creates either a live
server node or an ordinary declaration instance. The optional `server` argument is resolved
in this order:

1. An explicit `server=<Server>` selects that server. An explicit
   `server=None` forces a declaration instance.
2. A live parent node selects the server that owns that node. A conflicting
   explicit server is rejected.
3. A declaration parent produces another declaration.
4. Calls made while a registered Python namespace module is being evaluated
   remain declarations; `server.ns.append(module)` materializes them later.
5. Otherwise, exactly one live server in the Python process is inferred.
6. With no live server, the result is a declaration. With multiple live servers,
   construction is ambiguous and raises `TypeError`; pass `server=` explicitly.

A bare `NodeId` does not identify a server. It therefore relies on the unique
live-server rule:

```python
import o6

server = o6.Server()

# The only live server is inferred even though objects_node is a NodeId.
motor = MotorType(parent=server.objectsNode, browseName="Motor")

# Always a normal declaration instance, regardless of live servers.
declaration = MotorType(server=None)
```

Namespace declarations remain ordinary Python objects even if a server exists:

```python
import sys

import o6
from o6.ns import ns0

o6.ns.namespace(shortname="plant", uri="urn:example:plant")
motors = FolderType(parent=ns0.instances.objects, browseName="Motors")
server.ns.append(sys.modules[__name__])
```

## Views

Views are address-space instances, so they are declared with the `o6.view`
factory rather than a class decorator:

```python
productionView = o6.view(
    nodeId="ns=plant;i=5001",
    browseName="Production",
    containsNoLoops=True,
)
```

The default parent is the standard `Views` folder and the default reference is
`Organizes`. Server selection follows the same rules as other declared
instances: pass `server=` explicitly, let a live parent or the sole live server
select it, or use `server=None` to retain the declaration for a later
`server.ns.append(module)` call.

## Type child relationships

Children of an `@o6.variabletype` or `@o6.objecttype` are defined as node
instances first, then linked with one of two camel-case identity helpers:

```python
_name = ns0.vartypes.PropertyType(dataType=o6.String, browseName="Name")
_controller = ControllerType()
_reset = o6.call()

@o6.objecttype(nodeId="ns=plant;i=1001", browseName="MachineType")
class MachineType(ns0.objtypes.BaseObjectType):
    name: ns0.vartypes.PropertyType = o6.hasProperty(_name)
    controller: ControllerType = o6.hasComponent(_controller)
    reset: o6.node.MethodNode = o6.hasComponent(_reset)
```

`hasProperty` and `hasComponent` each take exactly one existing instance and
preserve its static type: an input of type `T` returns `T`. They work for
Variables, Objects, Methods, and their subtypes.

Optionality belongs to the relationship and is inferred exclusively from
`Optional[T]`:

```python
_componentName = ns0.vartypes.PropertyType(dataType=o6.LocalizedText)
componentName: Optional[ns0.vartypes.PropertyType] = o6.hasProperty(_componentName)

# The instance can also be left undefined.
documentation: Optional[ns0.vartypes.PropertyType] = o6.hasProperty(None)
```

Node constructors describe the node itself. They do not accept an `optional`
argument.

## Type interfaces

An ObjectType or VariableType implements OPC UA InterfaceTypes through the
decorator's `interfaces` argument:

```python
@o6.objecttype(
    nodeId="ns=plant;i=1001",
    browseName="MachineType",
    interfaces=[IMaintainableType, ns0.objtypes.IOrderedObjectType],
)
class MachineType(ns0.objtypes.BaseObjectType):
    pass
```

Interface markers are abstract ObjectTypes derived from
`ns0.objtypes.BaseInterfaceType`. Interfaces are OPC UA type metadata, not Python
mixins: they do not enter the implementing class's MRO and their members are
not copied into its class body. The server adds the `HasInterface` references
after all types in the module exist. Mandatory interface members are then
instantiated according to the normal OPC UA type-instantiation rules.

Properties owned directly by a DataType or EnumType are constructed before the
type and passed through the decorator's `children` argument:

```python
_enumStrings = ns0.vartypes.PropertyType(
    browseName="EnumStrings",
    value=[o6.LocalizedText("OFF"), o6.LocalizedText("ON")],
    dataType=o6.LocalizedText,
    valueRank=1,
)

@o6.enumtype(ns="plant", nodeId="ns=plant;i=1200", browseName="Mode")
class Mode(ns0.datatypes.Enumeration):
    enumStrings: ns0.vartypes.PropertyType = o6.hasProperty(_enumStrings)
    OFF = 0
    ON = 1
```

The relationship is declared on the type class, like other type children.
`o6.hasProperty` also keeps the linked node out of Python's enum member table.
These children are injected beneath the DataType node; they are not emitted as
free-standing instances with an explicit `parent` NodeId.

## Access control

`o6.AccessControl` maps to open62541's `UA_AccessControl` plugin. Subclass it
to authenticate sessions or restrict individual operations, then pass the
instance to `o6.Server`. Authorization callbacks receive an `o6.Session`
proxy. Its `context` is the object returned by `activateSession`; the proxy
also provides session attributes, assigned roles, and `close()`.

```python
import o6
from o6.ns import ns0


class PasswordAccessControl(o6.AccessControl):
    def __init__(self):
        super().__init__(anonymous=True, username=True)

    def activate_session(self, endpoint, remote_certificate, session, token):
        if isinstance(token, ns0.datatypes.AnonymousIdentityToken):
            return {"username": None}
        if (
            isinstance(token, ns0.datatypes.UserNameIdentityToken)
            and token.userName == "user1"
            and token.password == b"password"
        ):
            return {"username": token.userName}
        raise o6.StatusCodeError(o6.StatusCode.BAD_USER_ACCESS_DENIED)


server = o6.Server(
    accessControl=PasswordAccessControl(),
    allowNonePolicyPassword=True,
)
```

`allowNonePolicyPassword` is deliberately separate from access control. It
permits password tokens on an unencrypted endpoint and should normally only be
enabled for local tests. Access control and this transport setting cannot be
replaced after the server starts.

Inherited authorization hooks use native C defaults. Only hooks overridden by
the concrete subclass cross into Python, so a plugin that overrides only
`activateSession` and `closeSession` does not acquire the GIL for routine
reads, writes, browses, or method calls.

Access-control subclasses using the earlier `(session_id, session_context, ...)`
hook signatures continue to work. New code should use the `Session` form.

## Role-based access control

Permissions are `o6.Permission` flags and may be combined with `|`. The
well-known OPC UA roles are available from `o6.roles`.

```python
temperature.permissions = {
    o6.roles.observer: o6.Permission.BROWSE | o6.Permission.READ,
    o6.roles.operator: (
        o6.Permission.BROWSE | o6.Permission.READ | o6.Permission.WRITE
    ),
}

temperature.permissions.grant(
    o6.roles.engineer,
    o6.Permission.READ | o6.Permission.WRITE,
    recursive=True,
)
```

Roles can be registered and resolved through `server.roles`:

```python
maintenance = server.roles.add(
    o6.Role(
        "Maintenance",
        identities=(
            ns0.datatypes.IdentityMappingRuleType(
                criteriaType=ns0.datatypes.IdentityCriteriaType.USER_NAME,
                criteria="maintainer",
            ),
        ),
    )
)
```

Namespace defaults apply when a node has no explicit role permissions:

```python
server.ns.set_default_permissions(
    "urn:example:machines",
    {o6.roles.observer: o6.Permission.BROWSE | o6.Permission.READ},
)
```

Anonymous sessions remain permissive for compatibility. Enable RBAC checks for
them explicitly:

```python
server = o6.Server(rbacForAnonymous=True)
```

Authentication may explicitly assign roles. Assignment is applied immediately
after activation, after the server has evaluated the role identity mappings.

```python
def activate_session(self, endpoint, remote_certificate, session, token):
    user = authenticate(token)
    return o6.SessionActivation(context=user, roles=(maintenance,))
```

`Session` is a resolving proxy rather than a retained native pointer. Every
operation validates its NodeId against the server, so using it after the remote
session closes raises `BadSessionIdInvalid` safely.

## Events

Emit a one-shot event with `emitEvent`, or retain a reusable event draft from
`createEvent`:

```python
event = server.createEvent(
    ns0.objtypes.BaseEventType,
    source=ns0.server,
    message="Production started",
    severity=200,
)
event["/BatchId"] = "B-1042"
event_id = event.trigger()
```

Field keys are event-filter path strings such as `/BatchId`, or
`QualifiedName` values when a default namespace is needed. Explicit fields use
open62541's fast event-field map.

An existing object node can additionally supply the payload. Fields absent
from the explicit map are then resolved from that instance:

```python
event.payloadSource = machine_event_instance
event.trigger()
```

Resolution order is explicit `event.fields`, then `payloadSource`, then the
standard `BaseEventType` defaults. `trigger()` returns the generated 16-byte
`EventId`.

!!! warning
	The server is not yet part of the official realease yet.

<!--

Configure the server, start it, build the address space, and expose values, methods, and references to clients.


## Server Lifecycle

The main entry point is `o6.Server`.

```python
from o6 import Server

server = Server(port=4840)
server.start()
server.stop()
```

Like the client, the server can also be used as a context manager.

```python
from o6 import Server

with Server(port=4840) as server:
	...
```

The high-level lifecycle methods are:

- `Server(...)` to create a server with the default configuration
- `start()` to run startup and begin serving
- `stop()` to shut the server down cleanly
- `running` from the underlying object to inspect whether the server is active

The API manages the event loop details internally. In synchronous code, `start()` launches the event loop in a background thread when needed. In asynchronous code, startup runs directly on the active loop.

## Server Configuration

The server configuration is available through `server.config`. It should be adjusted before the server is running.

Common configuration areas exposed by the API include:

- `applicationUri`
- `applicationDescription`
- encryption and certificate handling
- accepting all certificates for test setups

Example:

```python
from o6 import Server, ApplicationDescription, LocalizedText

server = Server(port=4840)

app = server.config.applicationDescription
app.applicationName = LocalizedText("en-US", "o6\\Python Test Server")
server.config.applicationDescription = app
```

Encryption can be configured directly in the `Server(...)` constructor with:

- `certificate`
- `privateKey`
- `trustList`
- `issuerList`
- `revocationList`
- `secureOnly`
- `acceptAllCertificates`


## Address Space and Node Management

The Python server focuses on high-level node creation helpers rather than raw `AddNodes` structures.

Available helpers include:

- `addObject(...)`
- `addVariable(...)`
- `addMethod(...)`
- `addObjectType(...)`
- `addVariableType(...)`
- `addReference(...)`
- `deleteNode(...)`

These methods return `ServerNode` wrappers, which provide a compact Python interface over the created nodes.

### Objects

Objects are created below a parent node, usually the Objects folder.

```python
plant = server.addObject("Plant", server.objectsNode)
```

### Variables

Variables can be created with an initial value, an optional explicit NodeId, and a data type inferred from the Python value.

```python
temperature = server.addVariable(
	"Temperature",
	plant,
	22.5,
	nodeId="ns=1;i=1001",
)
```

By default, `addVariable(...)` creates readable and writable variables. The helper can also mark variables as historizing and can accept an explicit datatype.

### Methods

Methods are exposed by attaching a Python callback to an object node.

```python

def add_numbers(node, a, b):
	return (o6.StatusCode.GOOD, a + b)

server.addMethod(
	"Add",
	plant,
	add_numbers,
	inputArgs=[
		ns0.datatypes.Argument(name="A", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR),
		ns0.datatypes.Argument(name="B", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR),
	],
	outputArgs=[
		ns0.datatypes.Argument(name="Sum", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR),
	],
)
```

### References and deletion

References can be managed explicitly.

```python
server.addReference(source_node, target_node, reference_type)
server.deleteNode(nodeid, deleteReferences=True)
```

## Read and Write Operations

Server-side value access is intentionally simple:

- `read_value(nodeid)`
- `write_value(nodeid, value)`

The returned `ServerNode` objects expose the same functionality through the `value` property.

```python
temperature.value = 23.0
current = temperature.value
```

## Node Types

The API also exposes helpers for type nodes.

- `addObjectType(...)`
- `addVariableType(...)`


## Reverse Connect

The server API exposes reverse connect support:

- `addReverseConnect(url, callback=None)`
- `removeReverseConnect(handle)`


## Utility Helpers

Several commonly used node identifiers:

- `OBJECTS_FOLDER`
- `TYPES_FOLDER`
- `VIEWS_FOLDER`
- `SERVER_NODE`
- `BASE_OBJECT_TYPE`
- `BASE_VARIABLE_TYPE`
- `BASE_DATA_VARIABLE_TYPE`
- `ORGANIZES`
- `HAS_COMPONENT`
- `HAS_PROPERTY`
- `HAS_TYPE_DEFINITION`
- `HAS_SUBTYPE`

The helper `ns0.datatypes.Argument(...)` simplifies method signature creation.

```python

arg = ns0.datatypes.Argument(name="Temperature", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="Current value")
```

For concrete examples, start with the basic server walkthrough in [examples/server-basic.md](examples/server-basic.md) and the other server examples in the examples section.

-->
