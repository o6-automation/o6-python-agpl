"""
Example nodeset: a tiny 6-DOF industrial robot arm.

Every concept an OPC UA nodeset2.xml author needs is showcased here:

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
Companion `example.py` shows how every type above is used from a client/server.
"""

from typing import Optional

import o6
from o6.ns import ns0
from o6.node import MethodNode

# ---------------------------------------------------------------------------
# Namespace registration
# ---------------------------------------------------------------------------
o6.ns.namespace("myns", uri="http://o6.example.org/Myns/", version="1.0")


# ===========================================================================
# @o6.datatype — wire layouts
# ===========================================================================
# A datatype is a struct on the wire: each annotated attribute becomes a field in the UA_StructureDefinition.
# The decorator registers the type with open62541 (so a struct value of this shape encodes/decodes correctly)


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


# ===========================================================================
# @o6.enumtype
# ===========================================================================
# A plain concrete enum is enough for the robot's high-level state.
# Members are bare ints; `o6.enumfield(...)` adds per-member UA metadata
# (Description, DisplayName) when you want it to show up in standard Address Space browsing.


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


# ---------------------------------------------------------------------------
# Abstract enum + concrete subclasses
# ---------------------------------------------------------------------------


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


# ===========================================================================
# @o6.referencetype — a custom non-hierarchical reference
# ===========================================================================
# ReferenceTypes are pure address-space metadata — no UA_DataType, no encoding.
# The marker carries the NodeId, BrowseName, IsAbstract, Symmetric and InverseName that the C side will publish.
# Subtyping (HasSubtype chains) is plain Python inheritance.


@o6.referencetype(
    ns="myns",
    browseName="Monitors",
    displayName="Monitors",
    inverseName="IsMonitoredBy",
    description="Axis Monitors its Drive controller",
)
class Monitors:
    pass


# ===========================================================================
# @o6.variabletype — typed Variable definitions
# ===========================================================================


@o6.variabletype(
    ns="myns",
    dataType=o6.Double,
    valueRank=o6.ValueRank.SCALAR,
    description="3-axis joint position (J1, J2, J3), one Double per axis",
)
class JointVectorType(ns0.vartypes.BaseDataVariableType):
    j1: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            accessLevel=o6.AccessLevel.READ | o6.AccessLevel.WRITE,
            description="J1 angle in radians",
            dataType=float,
        )
    )
    j2: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            accessLevel=o6.AccessLevel.READ | o6.AccessLevel.WRITE,
            description="J2 angle in radians",
            dataType=float,
        )
    )
    j3: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            accessLevel=o6.AccessLevel.READ | o6.AccessLevel.WRITE,
            description="J3 angle in radians",
            dataType=float,
        )
    )


@o6.variabletype(
    ns="myns",
    description="A robot pose: where the joints are + how the gripper is set",
)
class JointPoseType(ns0.vartypes.BaseDataVariableType):
    # A complex child is declared by ANNOTATING the member with its concrete type
    # and passing an instance of that type to hasComponent/hasProperty.
    position: JointVectorType = o6.hasComponent(JointVectorType())
    gripper: Optional[JointVectorType] = o6.hasComponent(JointVectorType(browseName="Gripper"))
    tool: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(description="currently mounted tool ID", dataType=str)
    )


# ===========================================================================
# @o6.objecttype — typed Object definitions
# ===========================================================================


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


# ---------------------------------------------------------------------------
# Detached mode as a TYPE declaration default
# ---------------------------------------------------------------------------

# A detached instance is what a type marker returns whenever no server owns it
# (inside a namespace module that is always the case). Children are supplied via
# `values=`: a plain Python value seeds a leaf, a nested dict seeds a whole
# subtree, and a nested *declaration* does the same while pinning its NodeId.
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


@o6.objecttype(
    ns="myns",
    description="Second-generation robot arm: same axis shape as RobotType, but its "
    "`pose` default is a detached template baked into the TYPE declaration itself",
)
class RobotType2(AxisType):
    serial: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(description="manufacturer serial number", dataType=str)
    )
    # The positional argument is `_HOME_POSE` — a detached JointPoseType
    # detached template above, complete with predetermined
    # NodeIds). It is NOT a per-instance value: it is RobotType2's own
    # default child subtree, materialised once when the type is injected.
    pose: JointPoseType = o6.hasComponent(_HOME_POSE)
    # A leaf DataVariable — the commanded tool speed, in mm/s.
    speed: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(description="commanded TCP speed [mm/s]", dataType=float)
    )


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

    # The behaviour is bound by BrowseName: `@o6.call("foo")` is
    # identity-preserving, so `_foo` also stays a normal Python method.
    @o6.call("foo")
    def _foo(self, n: o6.Int32) -> tuple[o6.StatusCode, o6.Int32]:
        print(f"[server] WithMethod.foo called with n = {n}")
        return (o6.StatusCode.GOOD, int(n) + 1)
