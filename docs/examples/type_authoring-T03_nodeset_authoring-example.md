# Nodeset Authoring

## myns.py

Example nodeset: a tiny 6-DOF industrial robot arm.

The concepts a nodeset2.xml author needs:

  * ``@o6.datatype``                    — a wire-layout struct (Point, BoundingBox)
  * ``@o6.enumtype``                    — a concrete IntFlag enum (RobotState)
  * ``@o6.enumtype(isAbstract=...)``   — an abstract enum parent shared by
                                          several concrete enums (VelocityLimits / JointVelocity / LinearVelocity)
  * ``@o6.referencetype``               — a custom non-hierarchical reference
                                          (Axis "Monitors" Drive)
  * ``@o6.variabletype``                — a typed value definition (JointVector,
                                          JointPose) with leaf + complex children
  * ``@o6.objecttype``                  — a typed object definition (DriveType,
                                          AxisType, RobotType) with complex Object
                                          and Variable children

This file is the OPC UA equivalent of a small nodeset2.xml.
`example.py` uses every type above from a client and a server.

### Namespace registration
Every custom type in this file belongs to `myns`. The module-level
`o6.ns.namespace(...)` call registers the namespace before any
decorator below runs, so `ns="myns"` resolves to it. `uri` is the OPC UA
namespace URI that identifies `myns` globally. `version` is
informational metadata written into the generated nodeset.

```python
o6.ns.namespace("myns", uri="http://o6.example.org/Myns/", version="1.0")
```

### `@o6.datatype` — wire layouts
A `@o6.datatype` class is a struct on the wire. Every annotated
attribute becomes a field in the UA `StructureDefinition`. The
decorator registers the type with open62541, so struct values of this
shape encode and decode correctly. `Point` is a flat struct of three
doubles. `BoundingBox` nests two `Point` fields: struct fields can be
other `@o6.datatype` classes.

```python
@o6.datatype(ns="myns", description="3-D vector of doubles; the canonical Point in the world model")
class Point:
    x: float
    y: float
    z: float

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y}, z={self.z})"


@o6.datatype(ns="myns", description="Axis-aligned box in 3-D space")
class BoundingBox:
    min: Point
    max: Point

    def __init__(self, min: "Point | None" = None, max: "Point | None" = None) -> None:
        self.min = min if min is not None else Point()
        self.max = max if max is not None else Point()

    @property
    def size(self) -> Point:
        return Point(self.max.x - self.min.x, self.max.y - self.min.y, self.max.z - self.min.z)
```

### `@o6.enumtype`
A concrete enum describes the robot's high-level state. Members are
bare ints. `o6.enumfield(...)` adds UA metadata per member
(`description`, `displayName`), which clients see when they browse the
address space.

```python
@o6.enumtype(
    ns="myns",
    description="Top-level robot state",
)
class RobotState:
    IDLE = 0
    RUNNING = o6.enumfield(1, description="executing a program")
    HOLD = o6.enumfield(2, description="paused by operator", displayName="HOLD")
    ESTOP = o6.enumfield(3, description="emergency stop asserted", displayName="E-Stop")
    FAULT = 4
```

### Abstract enum + concrete subclasses
`isAbstract=True` declares an enum without members, used as a common
Python base for several concrete enums. `JointVelocity` and
`LinearVelocity` both subclass `VelocityLimits`. So
`issubclass(myns.JointVelocity, myns.VelocityLimits)` is true, and code
can accept any velocity limit enum.

```python
@o6.enumtype(ns="myns", isAbstract=True, browseName="VelocityLimits")
class VelocityLimits:
    pass


@o6.enumtype(ns="myns", browseName="JointVelocity")
class JointVelocity(VelocityLimits):
    SLOW = 0
    NORMAL = 1
    FAST = 2
    SPORT = o6.enumfield(3, description="above nominal — warranty-voiding")


@o6.enumtype(ns="myns", browseName="LinearVelocity")
class LinearVelocity(VelocityLimits):
    CAREFUL = 0
    STANDARD = 1
    EXPRESS = 2
```

### `@o6.referencetype` — a custom non-hierarchical reference
A ReferenceType only links two nodes. It never carries a value, so it
has no `UA_DataType` and no encoding. The decorator carries the NodeId,
BrowseName, `isAbstract`, `symmetric` and `inverseName` that the server
publishes. Subtyping (HasSubtype chains) is plain Python inheritance,
as everywhere in this file.

```python
@o6.referencetype(
    ns="myns",
    browseName="Monitors",
    displayName="Monitors",
    inverseName="IsMonitoredBy",
    description="Axis Monitors its Drive controller",
)
class Monitors:
    pass
```

### `@o6.variabletype` — typed Variable definitions
A `@o6.variabletype` class defines a typed Variable. `dataType` and
`valueRank` describe the Variable's own value; annotated members become
child nodes. `JointVectorType` has only leaves: three `PropertyType`
children (`j1`, `j2`, `j3`), each declared with `o6.hasProperty(...)`.

```python
@o6.variabletype(
    ns="myns",
    dataType=o6.Double,
    valueRank=o6.ValueRank.SCALAR,
    description="3-axis joint position (J1, J2, J3), one Double per axis",
)
class JointVectorType(ns0.vartypes.BaseDataVariableType):
    j1: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            accessLevel=AccessLevelType.CURRENT_READ | AccessLevelType.CURRENT_WRITE,
            description="J1 angle in radians",
            dataType=float,
        )
    )
    j2: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            accessLevel=AccessLevelType.CURRENT_READ | AccessLevelType.CURRENT_WRITE,
            description="J2 angle in radians",
            dataType=float,
        )
    )
    j3: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            accessLevel=AccessLevelType.CURRENT_READ | AccessLevelType.CURRENT_WRITE,
            description="J3 angle in radians",
            dataType=float,
        )
    )
```

`JointPoseType` nests a `JointVectorType` under `position`. A complex
child is declared like a leaf: annotate the member with its concrete
type and pass an instance of that type to
`o6.hasComponent`/`o6.hasProperty`. `gripper` is an `Optional` member,
so instances may omit it.

```python
@o6.variabletype(
    ns="myns",
    description="A robot pose: where the joints are + how the gripper is set",
)
class JointPoseType(ns0.vartypes.BaseDataVariableType):
    position: JointVectorType = o6.hasComponent(JointVectorType())
    gripper: Optional[JointVectorType] = o6.hasComponent(JointVectorType(browseName="Gripper"))
    tool: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(description="currently mounted tool ID", dataType=str)
    )
```

### `@o6.objecttype` — typed Object definitions
A `@o6.objecttype` class defines a typed Object. Its annotated members
become child Properties, Variables and Objects, declared with
`o6.hasProperty`/`o6.hasComponent` as on a VariableType. `DriveType`
has only leaves: two string Properties and two float DataVariables
(`max_current` is `Optional`, so instances may omit it).

```python
@o6.objecttype(
    ns="myns",
    description="A servo drive: a leaf object with metadata and live telemetry",
)
class DriveType(ns0.objtypes.BaseObjectType):
    manufacturer: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(description="vendor name", dataType=str)
    )
    firmware: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(description="firmware version string", dataType=str)
    )
    current: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(description="measured motor current [A]", dataType=float)
    )
    max_current: Optional[ns0.vartypes.BaseDataVariableType] = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(description="nameplate current limit [A]", dataType=float)
    )
```

`AxisType` has `DriveType` and `JointVectorType` as complex children
(`drive`, `position`) next to its own leaf Properties. The
`o6.hasComponent`/`o6.hasProperty` pattern nests to any depth.

```python
@o6.objecttype(
    ns="myns",
    description="A single robot axis (one joint + its drive + its position)",
)
class AxisType(ns0.objtypes.BaseObjectType):
    name: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(description="human-readable axis name (e.g. 'J1')", dataType=str)
    )
    state: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(description="high-level axis state", dataType=RobotState)
    )
    limits: Optional[ns0.vartypes.BaseDataVariableType] = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            description="soft limits as a world-space axis-aligned BoundingBox",
            dataType=BoundingBox,
        )
    )
    drive: DriveType = o6.hasComponent(DriveType())  # complex Object child
    position: JointVectorType = o6.hasComponent(JointVectorType())  # complex Variable child
```

`RobotType` subclasses `AxisType` in Python. It inherits every field of
`AxisType` (`name`, `state`, `limits`, `drive`, `position`) and adds
`serial`, `pose` and `speed`. The `values={...}` dict of a `RobotType`
instance is keyed by BrowseName, whichever class declared the field.

```python
@o6.objecttype(
    ns="myns",
    description="The whole robot arm: serial, a base pose, and its axes",
)
class RobotType(AxisType):
    serial: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(description="manufacturer serial number", dataType=str)
    )
    pose: JointPoseType = o6.hasComponent(JointPoseType())
    speed: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(description="commanded TCP speed [mm/s]", dataType=float)
    )
```

### Detached mode as a TYPE declaration default
A type marker returns a detached instance when no server owns it. In a
namespace module that is always the case, because the module is
imported before any server exists. Children are supplied via
`values=`:

- a plain Python value seeds a leaf,
- a nested dict seeds a subtree,
- a nested declaration (an instance, not a dict) seeds a subtree and
  fixes its NodeId up front.

`_HOME_POSE` builds such a template offline, with every NodeId fixed in
advance.

```python
_HOME_POSE = JointPoseType(
    nodeId="ns=myns;i=5000",
    values={
        "position": JointVectorType(
            nodeId="ns=myns;i=5001",
            values={
                "j1": ns0.vartypes.PropertyType(nodeId="ns=myns;i=5002", value=0.0, dataType=float),
                "j2": ns0.vartypes.PropertyType(nodeId="ns=myns;i=5003", value=0.0, dataType=float),
                "j3": ns0.vartypes.PropertyType(nodeId="ns=myns;i=5004", value=0.0, dataType=float),
            },
        ),
        "tool": ns0.vartypes.PropertyType(nodeId="ns=myns;i=5005", value="none", dataType=str),
    },
)
```

`RobotType2` uses `_HOME_POSE` as the default of `pose` instead of a
fresh `JointPoseType()`. A detached template is not a per-instance
value. It is the TYPE's default child subtree, materialized with its
fixed NodeIds each time the type marker is injected into a server.

```python
@o6.objecttype(
    ns="myns",
    description="Second-generation robot arm: same axis shape as RobotType, but its "
    "`pose` default is a detached template baked into the TYPE declaration itself",
)
class RobotType2(AxisType):
    serial: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(description="manufacturer serial number", dataType=str)
    )
    pose: JointPoseType = o6.hasComponent(_HOME_POSE)
    speed: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(description="commanded TCP speed [mm/s]", dataType=float)
    )
```

### `@o6.call` — a Method node with a bound handler
`o6.call(...)` declares the Method node (its NodeId and input/output
`Argument`s) as the value of a `hasComponent` child, like any other
component. `@o6.call("foo")` binds a Python method as that Method's
handler by BrowseName. The decorator returns the function unchanged, so
`_foo` stays a normal Python method you can call directly.

```python
@o6.objecttype(ns="myns", browseName="WithMethod")
class WithMethod(ns0.objtypes.BaseObjectType):
    foo: MethodNode = o6.hasComponent(
        o6.call(
            browseName="foo",
            inputArgs=[
                ns0.datatypes.Argument(name="n", dataType=o6.Int32, valueRank=o6.ValueRank.SCALAR)
            ],
            outputArgs=[
                ns0.datatypes.Argument(name="out", dataType=o6.Int32, valueRank=o6.ValueRank.SCALAR)
            ],
        )
    )

    @o6.call("foo")
    def _foo(self, n: o6.Int32) -> tuple[o6.StatusCode, o6.Int32]:
        print(f"[server] WithMethod.foo called with n = {n}")
        return (o6.StatusCode.GOOD, int(n) + 1)
```

## example.py

End-to-end nodeset demo: a 6-DOF robot arm defined in `myns.py`.

The OPC UA equivalent of "load a nodeset2.xml and try it out". The
script uses the `myns` module step by step:

  Step 1 - start a server, publish `myns`, connect a client
  Step 2 - @o6.datatype round-trip             (Point)
  Step 3 - @o6.enumtype + abstract inheritance (RobotState, VelocityLimits)
  Step 4 - @o6.referencetype                   (Monitors / IsMonitoredBy)
  Step 5 - @o6.variabletype                    (JointVector, JointPose with complex child)
  Step 6 - @o6.objecttype                      (Drive, Axis, Robot, with complex children)
  Step 7 - piecewise composition               (build a sub-tree off-line with pinned
                                                NodeIds, then materialise it onto ONE
                                                instance's `values=`)
  Step 8 - @o6.call                            (WithMethod.foo)

Run it directly (it owns its server and cleans up on exit)::

    .venv/bin/python3 examples/type_authoring/T03_nodeset_authoring/example.py

The helpers below keep the assertions and prints readable.
`_browse_names()`, `_child_nodeid()` and `_has_reference()` wrap
`client.browse()` to answer "what is under this node" without repeating
the filter arguments.

```python
def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _browse_names(client: o6.Client, node_id: Any) -> list[str]:
    """Convenience: return the BrowseName *suffix* (after the namespace colon) of every
    forward hierarchical child of *node_id* on the server."""
    refs = client.browse(
        node_id,
        direction=ns0.datatypes.BrowseDirection.FORWARD,
        reftype=ns0.reftypes.HierarchicalReferences,
        refsubtypes=True,
        nodeClassMask=ns0.datatypes.NodeClass.OBJECT | ns0.datatypes.NodeClass.VARIABLE,
        resultMask=ns0.datatypes.BrowseResultMask.BROWSE_NAME,
    )
    return [str(r.browseName).split(":", 1)[-1] for r in refs]


def _child_nodeid(client: o6.Client, node_id: Any, browse_suffix: str) -> Any:
    """Return the NodeId of the forward hierarchical child of *node_id* whose BrowseName
    suffix matches *browse_suffix* (used to walk a TYPE's own instance-declaration nodes,
    which have no Python-side handle the way a live instance's dot-access does)."""
    refs = client.browse(
        node_id,
        direction=ns0.datatypes.BrowseDirection.FORWARD,
        reftype=ns0.reftypes.HierarchicalReferences,
        refsubtypes=True,
        resultMask=ns0.datatypes.BrowseResultMask.BROWSE_NAME,
    )
    return next(r.nodeId for r in refs if str(r.browseName).endswith(":" + browse_suffix))


def _has_reference(client: o6.Client, src: Any, reftype: Any, browse_suffix: str) -> bool:
    """True iff *src* has a forward reference of type *reftype* pointing at a node whose
    BrowseName suffix matches *browse_suffix*."""
    refs = client.browse(
        src,
        direction=ns0.datatypes.BrowseDirection.FORWARD,
        reftype=reftype,
        refsubtypes=True,
        resultMask=ns0.datatypes.BrowseResultMask.BROWSE_NAME,
    )
    return any(str(r.browseName).endswith(":" + browse_suffix) for r in refs)
```

### Step 1 — publish the nodeset
The decorators in `myns.py` (`@o6.datatype`, `@o6.objecttype`, ...)
register the types in the process at import time. A server exposes them
to clients only after the module is appended to `server.ns`.
`o6.ns.myns.index` is the namespace index the server assigned. You need
it to build a NodeId by hand; `ns=myns;...` below resolves through the
same registration.

```python
print("--- Step 1: publish the nodeset ---")

PORT = _free_port()
server = Server(port=PORT)
server.start()
time.sleep(0.1)

import myns  # the nodeset module, sitting next to this file

server.ns.append(myns)

print(f"[server] listening on opc.tcp://localhost:{PORT}")
print(f"[server] myns published; namespace index = {o6.ns.myns.index}")

client = Client(f"opc.tcp://localhost:{PORT}")
client.connect()
print(f"[client] connected; namespaces = {list(client.read(o6.NodeId('ns=0;i=2255')))}")
```

### Step 2 — `@o6.datatype` round-trip
A `@o6.datatype` class is a plain Python object on the client and a UA
struct on the wire. `addVariable()` accepts an instance directly.
Reading the Variable back returns the same class, and fields
(`origin_back.x`) are native Python values, not wrapped in an
`ExtensionObject`.

```python
print("\n--- Step 2: @o6.datatype round-trip (Point) ---")

origin = myns.Point(0.0, 0.0, 0.0)
origin_var = server.addVariable("Origin", server.objectsNode, origin, nodeId="ns=myns;i=2001")
print(f"[server] added variable Origin at {origin_var._nodeid}")

origin_back = origin_var()
print(f"[client] read back: {origin_back!r}")
print(f"[client] origin_back.x = {origin_back.x}  (a Python float, not an ExtensionObject)")

# Write a new value through the structured wire layout.
new_origin = myns.Point(1.0, 2.0, 3.0)
client.write(origin_var._nodeid, new_origin)
print(f"[client] wrote {new_origin!r}; round-trip: {client.read(origin_var._nodeid)!r}")
```

### Step 3 — `@o6.enumtype` and abstract inheritance
A concrete enum (`RobotState`) is sent as an Int32 with the member's
int value. An abstract enum (`VelocityLimits`) has no members. It is a
common Python base for concrete enums (`JointVelocity`,
`LinearVelocity`), so
`isinstance(myns.JointVelocity.SPORT, myns.VelocityLimits)` is true.

```python
print("\n--- Step 3: @o6.enumtype + abstract inheritance ---")

state_var = server.addVariable(
    "State", server.objectsNode, int(myns.RobotState.ESTOP), nodeId="ns=myns;i=2002"
)
print(f"[server] added variable State at {state_var._nodeid}")

state_back = state_var()
print(f"[client] read back: {state_back}")
assert state_back == myns.RobotState.ESTOP

assert issubclass(myns.JointVelocity, myns.VelocityLimits)
assert issubclass(myns.LinearVelocity, myns.VelocityLimits)
assert isinstance(myns.JointVelocity.SPORT, myns.VelocityLimits)
```

### Step 4 — `@o6.referencetype`
A custom ReferenceType has a NodeId and a name but no data type, because
it only links two nodes and never carries a value.
`o6.NodeId(myns.Monitors)` resolves the type marker to the NodeId the
server registered.

```python
print("\n--- Step 4: @o6.referencetype (Monitors / IsMonitoredBy) ---")
print(f"[client] Monitors reference type NodeId  = {o6.NodeId(myns.Monitors)}")
```

### Step 5 — `@o6.variabletype`
`JointVectorType(...)` against a live server creates the Variable and
its declared child Properties (`j1`/`j2`/`j3`) in one call.
`values={...}` seeds each child by BrowseName. A plain value becomes the
child's initial value (a nested declaration behaves differently, see
Step 7).

```python
print("\n--- Step 5: @o6.variabletype (JointVector / JointPose) ---")

joints = myns.JointVectorType(
    nodeId="ns=myns;i=3001",
    parent=server.objectsNode,
    browseName="Joints",
    values={"j1": 0.0, "j2": 0.5, "j3": -0.25},
)
print(
    f"[server] created JointVectorType instance at {joints._nodeid} "
    f"(TypeDefinition = JointVectorType at {o6.NodeId(myns.JointVectorType)})"
)
print(f"[server] children of Joints: {_browse_names(client, joints._nodeid)}")
print(f"[client] joints.j1() = {joints.j1()}")
print(f"[client] joints.j2() = {joints.j2()}")
print(f"[client] joints.j3() = {joints.j3()}")
```

`JointPoseType` nests a `JointVectorType` under `position`, a complex
child instead of a leaf. `values={"position": {...}}` seeds it with a
nested dict. Dot access on the returned handle
(`pose.position.j1(...)`) works at any depth.

```python
pose = myns.JointPoseType(
    nodeId="ns=myns;i=3002",
    parent=server.objectsNode,
    browseName="CurrentPose",
    values={
        "position": {"j1": 0.0, "j2": 0.0, "j3": 0.0},
        "tool": "gripper",
    },
)
print(
    f"\n[server] created JointPoseType instance at {pose._nodeid}"
    f"(TypeDefinition = JointPoseType at {o6.NodeId(myns.JointPoseType)})"
)

print(f"[server] children of CurrentPose: {_browse_names(client, pose._nodeid)}")

pose.position.j1(1.5)
print(f"[client] wrote pose.position.j1 = 1.5; round-trip = {pose.position.j1()}")
```

### Step 6 — `@o6.objecttype` and subtyping
`RobotType` subclasses `AxisType` in Python. It has its own fields
(`serial`, `pose`, `speed`) and all fields of `AxisType` (`name`,
`state`, `limits`, `drive`, `position`). One `values={...}` dict seeds
both, keyed by BrowseName, whichever class declared the field.

```python
robot = myns.RobotType(
    nodeId="ns=myns;i=4003",
    parent=server.objectsNode,
    browseName="RobotArm1",
    values={
        # Inherited from AxisType:
        "name": "Arm-001",
        "state": int(myns.RobotState.IDLE),
        "limits": myns.BoundingBox(
            min=myns.Point(-3.0, -3.0, -3.0),
            max=myns.Point(3.0, 3.0, 3.0),
        ),
        "drive": {
            "manufacturer": "ACME Robotics",
            "firmware": "v1.0.0",
            "current": 0.0,
        },
        "position": {"j1": 0.0, "j2": 0.0, "j3": 0.0},
        # New on RobotType:
        "serial": "SN-001-2026",
        "pose": {
            "position": {"j1": 0.0, "j2": 0.0, "j3": 0.0},
            "tool": "gripper",
        },
        "speed": 250.0,
    },
)
print(f"\n[server] created RobotArm1 at {o6.NodeId(robot)} (TypeDefinition = RobotType)")
print(f"[server] children of RobotArm1: {_browse_names(client, o6.NodeId(robot))}")
print(f"[client] RobotArm1.serial          = {robot.serial()!r}")
print(f"[client] RobotArm1.pose.tool       = {robot.pose.tool()!r}")
print(f"[client] RobotArm1.speed           = {robot.speed()} mm/s")
print(f"[client] RobotArm1.drive.firmware  = {robot.drive.firmware()!r}")
```

### Step 7 — piecewise composition
`server=None` builds a subtree offline, before any server exists. In
`values=`:

- a plain value seeds a leaf; the server allocates its NodeId on
  materialization,
- a nested declaration (an instance, not a dict) seeds the child and
  fixes its NodeId up front.

With fixed NodeIds the template's NodeIds are known before any server
exists, so other artifacts (for example a nodeset export) can refer to
them before the type is used.

```python
print("\n--- Step 7: piecewise composition ---")

default_pose = myns.JointPoseType(
    server=None,
    nodeId="ns=myns;i=9001",
    value=None,
    values={
        "position": myns.JointVectorType(
            server=None,
            nodeId="ns=myns;i=9002",
            values={
                "j1": ns0.vartypes.PropertyType(
                    server=None, nodeId="ns=myns;i=9010", value=0.0, dataType=float
                ),
                "j2": ns0.vartypes.PropertyType(
                    server=None, nodeId="ns=myns;i=9011", value=0.0, dataType=float
                ),
                "j3": ns0.vartypes.PropertyType(
                    server=None, nodeId="ns=myns;i=9012", value=0.0, dataType=float
                ),
            },
        ),
        "tool": ns0.vartypes.PropertyType(
            server=None, nodeId="ns=myns;i=9013", value="gripper", dataType=str
        ),
    },
)
print(
    f"[client] default_pose is a detached template, "
    f"isinstance(default_pose, myns.JointPoseType) = {isinstance(default_pose, myns.JointPoseType)}"
)
```

A detached declaration is not a live node. Dot access still walks it
offline, but it returns `o6.NodeId(...)`, not a value: there is no
server node to read yet. The values appear after materialization,
below.

```python
print(f"[client] default_pose.position.j1 NodeId = {o6.NodeId(default_pose.position.j1)}")
print(f"[client] default_pose.tool        NodeId = {o6.NodeId(default_pose.tool)}")
```

Passing the detached `default_pose` template as the value of `pose`
materializes the whole subtree on the server in one step. The
template's NodeIds carry over unchanged.

```python
robot2 = myns.RobotType(
    nodeId="ns=myns;i=4004",
    parent=server.objectsNode,
    browseName="RobotArm2",
    values={
        "name": "Arm-002",
        "state": int(myns.RobotState.IDLE),
        "drive": {
            "manufacturer": "ACME Robotics",
            "firmware": "v1.0.0",
            "current": 0.0,
        },
        "position": {"j1": 0.0, "j2": 0.0, "j3": 0.0},
        "serial": "SN-002-2026",
        "pose": default_pose,  # <-- detached template, preseeded
        "speed": 100.0,
    },
)
print(f"[server] RobotArm2.pose at {o6.NodeId(robot2.pose)}")
print(
    f"[client] RobotArm2.pose.tool = {robot2.pose.tool()!r} "
    f"at {o6.NodeId(robot2.pose.tool)}"
)
```

### Step 8 — `@o6.call`
`o6.call(...)` declares the Method node (its NodeId and arguments).
`@o6.call("foo")` binds a Python method as its handler by BrowseName.
`mm.foo(123)` invokes `WithMethod._foo` on the server and returns its
`(StatusCode, result)` tuple.

```python
print("\n--- Step 8: @o6.call (WithMethod.foo) ---")

mm = myns.WithMethod(
    nodeId="ns=myns;i=7001", parent=server.objectsNode, browseName="ns=myns;WithMethod"
)
print(f"[server] created WithMethod at {mm._nodeid}")
print(f"[client] mm.foo(123) = {mm.foo(123)}")
```

## Source Code

Download these files into the same folder to run the example:

- [`myns.py`](type_authoring-T03_nodeset_authoring-example/myns.py)
- [`example.py`](type_authoring-T03_nodeset_authoring-example/example.py)
