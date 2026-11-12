#!/usr/bin/env python3
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
"""

import socket
import time
from typing import Any

import o6
from o6 import Client, Server
from o6.ns import ns0



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



print("\n--- Step 4: @o6.referencetype (Monitors / IsMonitoredBy) ---")
print(f"[client] Monitors reference type NodeId  = {o6.NodeId(myns.Monitors)}")



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


print(f"[client] default_pose.position.j1 NodeId = {o6.NodeId(default_pose.position.j1)}")
print(f"[client] default_pose.tool        NodeId = {o6.NodeId(default_pose.tool)}")


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



print("\n--- Step 8: @o6.call (WithMethod.foo) ---")

mm = myns.WithMethod(
    nodeId="ns=myns;i=7001", parent=server.objectsNode, browseName="ns=myns;WithMethod"
)
print(f"[server] created WithMethod at {mm._nodeid}")
print(f"[client] mm.foo(123) = {mm.foo(123)}")


# ===========================================================================
# Teardown
# ===========================================================================

print("\n--- Teardown ---")
client.disconnect()
server.stop()
print("[client] disconnected, [server] stopped")

print("\n=== Example completed ===")