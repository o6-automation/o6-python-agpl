# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
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
"""

from typing import Optional

import o6
from o6.ns import ns0
from o6.ns.ns0.datatypes import AccessLevelType
from o6.node import MethodNode

# BEGIN MD
# ## Namespace registration
# Every custom type in this file belongs to `myns`. The module-level
# `o6.ns.namespace(...)` call registers the namespace before any
# decorator below runs, so `ns="myns"` resolves to it. `uri` is the OPC UA
# namespace URI that identifies `myns` globally. `version` is
# informational metadata written into the generated nodeset.
# END MD

# BEGIN CODE
o6.ns.namespace("myns", uri="http://o6.example.org/Myns/", version="1.0")
# END CODE


# BEGIN MD
# ## `@o6.datatype` — wire layouts
# A `@o6.datatype` class is a struct on the wire. Every annotated
# attribute becomes a field in the UA `StructureDefinition`. The
# decorator registers the type with open62541, so struct values of this
# shape encode and decode correctly. `Point` is a flat struct of three
# doubles. `BoundingBox` nests two `Point` fields: struct fields can be
# other `@o6.datatype` classes.
# END MD

# BEGIN CODE
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
# END CODE


# BEGIN MD
# ## `@o6.enumtype`
# A concrete enum describes the robot's high-level state. Members are
# bare ints. `o6.enumfield(...)` adds UA metadata per member
# (`description`, `displayName`), which clients see when they browse the
# address space.
# END MD

# BEGIN CODE
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
# END CODE


# BEGIN MD
# ## Abstract enum + concrete subclasses
# `isAbstract=True` declares an enum without members, used as a common
# Python base for several concrete enums. `JointVelocity` and
# `LinearVelocity` both subclass `VelocityLimits`. So
# `issubclass(myns.JointVelocity, myns.VelocityLimits)` is true, and code
# can accept any velocity limit enum.
# END MD

# BEGIN CODE
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
# END CODE


# BEGIN MD
# ## `@o6.referencetype` — a custom non-hierarchical reference
# A ReferenceType only links two nodes. It never carries a value, so it
# has no `UA_DataType` and no encoding. The decorator carries the NodeId,
# BrowseName, `isAbstract`, `symmetric` and `inverseName` that the server
# publishes. Subtyping (HasSubtype chains) is plain Python inheritance,
# as everywhere in this file.
# END MD

# BEGIN CODE
@o6.referencetype(
    ns="myns",
    browseName="Monitors",
    displayName="Monitors",
    inverseName="IsMonitoredBy",
    description="Axis Monitors its Drive controller",
)
class Monitors:
    pass
# END CODE


# BEGIN MD
# ## `@o6.variabletype` — typed Variable definitions
# A `@o6.variabletype` class defines a typed Variable. `dataType` and
# `valueRank` describe the Variable's own value; annotated members become
# child nodes. `JointVectorType` has only leaves: three `PropertyType`
# children (`j1`, `j2`, `j3`), each declared with `o6.hasProperty(...)`.
# END MD

# BEGIN CODE
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
# END CODE

# BEGIN MD
# `JointPoseType` nests a `JointVectorType` under `position`. A complex
# child is declared like a leaf: annotate the member with its concrete
# type and pass an instance of that type to
# `o6.hasComponent`/`o6.hasProperty`. `gripper` is an `Optional` member,
# so instances may omit it.
# END MD

# BEGIN CODE
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
# END CODE


# BEGIN MD
# ## `@o6.objecttype` — typed Object definitions
# A `@o6.objecttype` class defines a typed Object. Its annotated members
# become child Properties, Variables and Objects, declared with
# `o6.hasProperty`/`o6.hasComponent` as on a VariableType. `DriveType`
# has only leaves: two string Properties and two float DataVariables
# (`max_current` is `Optional`, so instances may omit it).
# END MD

# BEGIN CODE
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
# END CODE

# BEGIN MD
# `AxisType` has `DriveType` and `JointVectorType` as complex children
# (`drive`, `position`) next to its own leaf Properties. The
# `o6.hasComponent`/`o6.hasProperty` pattern nests to any depth.
# END MD

# BEGIN CODE
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
# END CODE

# BEGIN MD
# `RobotType` subclasses `AxisType` in Python. It inherits every field of
# `AxisType` (`name`, `state`, `limits`, `drive`, `position`) and adds
# `serial`, `pose` and `speed`. The `values={...}` dict of a `RobotType`
# instance is keyed by BrowseName, whichever class declared the field.
# END MD

# BEGIN CODE
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
# END CODE


# BEGIN MD
# ## Detached mode as a TYPE declaration default
# A type marker returns a detached instance when no server owns it. In a
# namespace module that is always the case, because the module is
# imported before any server exists. Children are supplied via
# `values=`:
#
# - a plain Python value seeds a leaf,
# - a nested dict seeds a subtree,
# - a nested declaration (an instance, not a dict) seeds a subtree and
#   fixes its NodeId up front.
#
# `_HOME_POSE` builds such a template offline, with every NodeId fixed in
# advance.
# END MD

# BEGIN CODE
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
# END CODE

# BEGIN MD
# `RobotType2` uses `_HOME_POSE` as the default of `pose` instead of a
# fresh `JointPoseType()`. A detached template is not a per-instance
# value. It is the TYPE's default child subtree, materialized with its
# fixed NodeIds each time the type marker is injected into a server.
# END MD

# BEGIN CODE
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
# END CODE


# BEGIN MD
# ## `@o6.call` — a Method node with a bound handler
# `o6.call(...)` declares the Method node (its NodeId and input/output
# `Argument`s) as the value of a `hasComponent` child, like any other
# component. `@o6.call("foo")` binds a Python method as that Method's
# handler by BrowseName. The decorator returns the function unchanged, so
# `_foo` stays a normal Python method you can call directly.
# END MD

# BEGIN CODE
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
# END CODE
