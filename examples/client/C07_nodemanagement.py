#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
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
Client-Side Node Management
===========================

Extends the server's address space at runtime from the *client* with
the high-level ``o6.Client`` API. The example adds an Object, a
Variable, a Method and an ObjectType, links two Objects with a
reference, browses the result and deletes everything it created.

The example runs against ``S03_firststeps.py``.
"""

# BEGIN MD
# The API on the ``o6.Client`` instance:
#
# - ``addObjectNode`` / ``addVariableNode`` / ``addMethodNode`` /
#   ``addObjectTypeNode``
# - ``addReference`` / ``deleteReference``
# - ``deleteNode`` (accepts a single NodeId or a list)
#
# All ``add*Node`` calls are keyword-only. They return the NodeId of the
# new node, requested by the client or chosen by the server.
# END MD

import os

import socket
import o6
from o6 import Client
from o6.ns.ns0 import datatypes as ns0dt
from o6.ns.ns0.datatypes import (
    MethodAttributes,
    ObjectAttributes,
    ObjectTypeAttributes,
    VariableAttributes,
)

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"

# BEGIN MD
# ## 1. Connection Setup
# The Objects folder (``i=85``) is the usual parent for user-defined
# nodes. ``Organizes`` (``i=35``) is the standard reference type that
# attaches a new node to its parent folder.
# END MD

# BEGIN CODE
localhost = "localhost"
endpoint_url = EXAMPLE_ENDPOINT

OBJECTS_FOLDER = "i=85"
ORGANIZES = "i=35"

print("--- 1. Connection Setup ---")
print(f"Connecting to {endpoint_url} ...")
# END CODE


# BEGIN MD
# ## 2. Add an Object Node
# Every node creation has the same shape:
#
# 1. Build an ``*Attributes`` struct.
# 2. Set the human-readable fields (``displayName``, ``description``).
# 3. Pass the struct to the matching ``add*Node`` method with ``parent``,
#    ``browseName`` and the reference type to the parent.
#
# ``browseName`` is a plain string or an ``o6.QualifiedName``.
# ``o6.QualifiedName(1, "MyFolder")`` places the node in namespace 1,
# the namespace ``S03_firststeps.py`` uses for its own objects.
#
# Every ``add*Node`` call accepts ``requestedNodeId=`` (for example
# ``requestedNodeId="ns=1;i=5000"``) to fix the NodeId. Without it the
# server picks one. On the server side the equivalent is the ``nodeId=``
# keyword of ``addObject`` / ``addVariable`` / ``addMethod``.
# END MD

# BEGIN CODE
with Client(endpoint_url) as client:
    print("Connected.")

    print()
    print("--- 2. Add an Object Node ---")
    obj_attr = ObjectAttributes()
    obj_attr.displayName = o6.LocalizedText("MyFolder")
    obj_attr.description = o6.LocalizedText("An example folder object")

    folder_id = client.addObjectNode(
        parent=OBJECTS_FOLDER,
        browseName=o6.QualifiedName(1, "MyFolder"),
        attributes=obj_attr,
        parentReference=ORGANIZES,
    )
    print(f"Added object: {folder_id}")
    # END CODE

    # BEGIN MD
    # ## 3. Add a Variable Node
    # ``VariableAttributes`` is the only one of the four attribute types
    # with a ``value``: the initial value of the variable.
    # ``valueRank = -1`` means scalar; a positive value is an array of that
    # rank. ``accessLevel = 3`` means readable and writable.
    # END MD

    # BEGIN CODE
    print()
    print("--- 3. Add a Variable Node ---")
    var_attr = VariableAttributes()
    var_attr.displayName = o6.LocalizedText("Temperature")
    var_attr.description = o6.LocalizedText("A temperature sensor value")
    var_attr.value = o6.Double(21.5)
    var_attr.dataType = o6.NodeId(11)  # i=11 in ns=0 is the Double data type
    var_attr.valueRank = -1  # scalar
    var_attr.accessLevel = 3  # readable + writable
    var_attr.userAccessLevel = 3

    temp_id = client.addVariableNode(
        parent=folder_id,
        browseName=o6.QualifiedName(1, "Temperature"),
        requestedNodeId="ns=1;i=5001",  # pin a stable address
        attributes=var_attr,
    )
    print(f"Added variable: {temp_id}")

    # Read back the initial value we just stored on the server
    initial = client.read(temp_id)
    print(f"Initial value = {initial}")
    # END CODE

    # BEGIN MD
    # ## 4. Add a Method Node
    # Build a ``MethodAttributes`` and call ``addMethodNode``. The node
    # exists when the call returns, but it is not callable until the
    # server registers a callback for it. ``S03_firststeps.py`` registers
    # none for ``Reset``, so ``client.call(method_id, ...)`` would return
    # ``BAD_NOT_IMPLEMENTED``.
    # END MD

    # BEGIN CODE
    print()
    print("--- 4. Add a Method Node ---")
    method_attr = MethodAttributes()
    method_attr.displayName = o6.LocalizedText("Reset")
    method_attr.description = o6.LocalizedText("Reset the sensor")
    method_attr.executable = True
    method_attr.userExecutable = True

    method_id = client.addMethodNode(
        parent=folder_id,
        browseName=o6.QualifiedName(1, "Reset"),
        attributes=method_attr,
    )
    print(f"Added method: {method_id}")
    # END CODE

    # BEGIN MD
    # ## 5. Add an ObjectType Node
    # An ObjectType is a *template*. Adding one does not change existing
    # objects. To use it, add an object node whose ``typeDefinition`` is the
    # NodeId of the new ObjectType.
    # END MD

    # BEGIN CODE
    print()
    print("--- 5. Add an ObjectType Node ---")
    objtype_attr = ObjectTypeAttributes()
    objtype_attr.displayName = o6.LocalizedText("SensorType")
    objtype_attr.description = o6.LocalizedText("A custom sensor type")
    objtype_attr.isAbstract = False

    objtype_id = client.addObjectTypeNode(
        parent="i=58",  # BaseObjectType
        browseName=o6.QualifiedName(1, "SensorType"),
        attributes=objtype_attr,
    )
    print(f"Added ObjectType: {objtype_id}")
    # END CODE

    # BEGIN MD
    # ## 6. Browse the New Object's Children
    # ``client.browse(nodeid)`` returns the references leading out of the
    # node. With ``resultMask=BrowseResultMask.ALL`` each reference carries
    # every field (BrowseName, display name, node class, type definition,
    # ...).
    # END MD

    # BEGIN CODE
    print()
    print("--- 6. Browse the New Object's Children ---")
    print("MyFolder children:")
    for ref in client.browse(folder_id, resultMask=ns0dt.BrowseResultMask.ALL):
        print(
            f"  {ref.browseName}  class={ref.nodeClass}  "
            f"forward={ref.isForward}  target={ref.nodeId}"
        )
    # END CODE

    # BEGIN MD
    # ## 7. Add an Explicit Reference Between Two Objects
    # The code adds a second folder and creates an ``Organizes`` reference
    # from ``MyFolder`` to ``MyFolder2``, a forward reference to a sibling.
    # END MD

    # BEGIN CODE
    print()
    print("--- 7. Add an Explicit Reference Between Two Objects ---")
    obj_attr2 = ObjectAttributes()
    obj_attr2.displayName = o6.LocalizedText("MyFolder2")
    obj_attr2.description = o6.LocalizedText("A second folder object")

    folder2_id = client.addObjectNode(
        parent=OBJECTS_FOLDER,
        browseName=o6.QualifiedName(1, "MyFolder2"),
        attributes=obj_attr2,
        parentReference=ORGANIZES,
    )
    print(f"Added second object: {folder2_id}")

    add_status = client.addReference(
        source=folder_id,
        reftype=ORGANIZES,
        target=folder2_id,
    )
    print(f"Added reference {folder_id} -Organizes-> {folder2_id}, status = {add_status}")

    print("MyFolder children after adding the reference:")
    for ref in client.browse(folder_id, resultMask=ns0dt.BrowseResultMask.ALL):
        print(
            f"  {ref.browseName}  class={ref.nodeClass}  "
            f"forward={ref.isForward}  target={ref.nodeId}"
        )

    del_status = client.deleteReference(
        source=folder_id,
        reftype=ORGANIZES,
        target=folder2_id,
    )
    print(f"Deleted reference {folder_id} -Organizes-> {folder2_id}, status = {del_status}")

    print("MyFolder children after deleting the reference:")
    for ref in client.browse(folder_id, resultMask=ns0dt.BrowseResultMask.ALL):
        print(
            f"  {ref.browseName}  class={ref.nodeClass}  "
            f"forward={ref.isForward}  target={ref.nodeId}"
        )
    # END CODE

    # BEGIN MD
    # ## 8. Clean Up
    # ``deleteNode`` accepts a single NodeId or a list.
    # ``deleteTargetReferences`` defaults to ``True``, so deleting the second
    # folder also removes the ``Organizes`` reference created above.
    # END MD

    # BEGIN CODE
    print()
    print("--- 8. Clean Up ---")
    targets = [method_id, temp_id, objtype_id, folder2_id, folder_id]
    del_statuses = client.deleteNode(targets)
    for target, status in zip(targets, del_statuses):
        print(f"Delete {target}: {status}")
        status.check()

print()
print("=== Example completed ===")
# END CODE
