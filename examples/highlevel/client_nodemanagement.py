#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Client-Side Node Management
===========================

Demonstrates how to extend the server's address space at runtime from
the *client* side, using the high-level ``o6.Client`` API. The example
adds an Object, a Variable, a Method, and an ObjectType, links two
Objects with an explicit reference, browses the result, and finally
deletes everything it created.

The example talks to ``basic_server.py`` so start that script in one
terminal before running this one.
"""

# BEGIN MD
# The relevant API surface lives on the ``o6.Client`` instance:
#
# - ``add_object_node`` / ``add_variable_node`` / ``add_method_node`` /
#   ``add_object_type_node``
# - ``add_reference`` / ``delete_reference``
# - ``delete_node`` (with a list argument).
#
# All ``add_*_node`` calls are keyword-only and return the `NodeId` the client (or the server
# if the NodeId is not specified by the client) chose for the new node.
# END MD

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

# BEGIN MD
# ## 1. Connection Setup
# The endpoint URL is the same one ``basic_server.py`` listens on. The
# Objects folder (``i=85``) is the conventional parent for user-defined
# nodes, so we cache its NodeId as a constant. The ``Organizes``
# reference type (``i=35``) is the standard "folder-contains-folder"
# reference. That is what the existing examples use to put nodes
# under the Objects folder.
# END MD

# BEGIN CODE
localhost = "localhost"
endpoint_url = f"opc.tcp://{localhost}:4840"

OBJECTS_FOLDER = "i=85"
ORGANIZES = "i=35"

print(f"Connecting to {endpoint_url} ...")
# END CODE


# BEGIN MD
# ## 2. Add an Object Node
# Every node creation follows the same shape: build an ``*Attributes``
# struct, set the human-readable fields (``display_name``,
# ``description``), and pass the struct to the matching
# ``add_*_node`` method along with ``parent``, ``browsename``, and the
# reference type that connects the new node to its parent.
#
# ``browsename`` can be either a plain string or an
# ``o6.QualifiedName``; passing ``o6.QualifiedName(1, "MyFolder")``
# explicitly places the new node in namespace 1, which is the same
# namespace ``basic_server.py`` uses for its own objects.
#
# Note: every ``add_*_node`` call on the client accepts a
# ``requested_nodeid=`` keyword (e.g.
# ``requested_nodeid="ns=1;i=5000"``) to pin a stable address for
# the new node. If you omit it, the server picks one and returns
# it. The same pattern is available on the server-side
# ``add_object`` / ``add_variable`` / ``add_method`` etc. via
# ``nodeId=``.
# END MD

# BEGIN CODE
with Client(endpoint_url) as client:
    print("[INFO] Connected to server successfully!\n")

    obj_attr = ObjectAttributes()
    obj_attr.displayName = o6.LocalizedText("MyFolder")
    obj_attr.description = o6.LocalizedText("An example folder object")

    folder_id = client.addObjectNode(
        parent=OBJECTS_FOLDER,
        browseName=o6.QualifiedName(1, "MyFolder"),
        attributes=obj_attr,
        parentReference=ORGANIZES,
    )
    print(f"[ADD]   Object    = {folder_id}")
    # END CODE

    # BEGIN MD
    # ## 3. Add a Variable Node
    # ``VariableAttributes`` is the only one of the four attribute types
    # that carries a ``value``: the initial value of the variable. ``valueRank = -1``
    # means *scalar*; positive values would indicate an array of that
    # rank. ``access_level = 3`` means "readable and writable".
    # END MD

    # BEGIN CODE
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
    print(f"[ADD]   Variable  = {temp_id}")

    # Read back the initial value we just stored on the server
    initial = client.read(temp_id)
    print(f"[READ]   Initial    = {initial}")
    # END CODE

    # BEGIN MD
    # ## 4. Add a Method Node
    # Adding a method node is structurally identical to adding an object:
    # build a ``MethodAttributes`` and call ``add_method_node``. The
    # catch is that the *server* needs to register a callable for the
    # method or the node exists but is not invokable. For instance, ``basic_server.py``
    # does not register a callback for ``Reset``, so this call succeeds
    # (the method node is created) but a later ``client.call(method_id,
    # ...)`` would return ``Bad_NotImplemented``.
    #
    # END MD

    # BEGIN CODE
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
    print(f"[ADD]   Method    = {method_id}")
    # END CODE

    # BEGIN MD
    # ## 5. Add an ObjectType Node
    # ObjectTypes are *templates* so adding one to the address space does
    # not affect existing objects. To use it you add an
    # object  `node` whose ``type_definition`` references the new ObjectType's
    # NodeId.
    # END MD

    # BEGIN CODE
    objtype_attr = ObjectTypeAttributes()
    objtype_attr.displayName = o6.LocalizedText("SensorType")
    objtype_attr.description = o6.LocalizedText("A custom sensor type")
    objtype_attr.isAbstract = False

    objtype_id = client.addObjectTypeNode(
        parent="i=58",  # BaseObjectType
        browseName=o6.QualifiedName(1, "SensorType"),
        attributes=objtype_attr,
    )
    print(f"[ADD]   ObjectType = {objtype_id}")
    # END CODE

    # BEGIN MD
    # ## 6. Browse the New Object's Children
    # ``client.browse(nodeid)`` returns the list of references leading
    # out from the given node. With ``result_mask=BrowseResultMask.ALL``
    # each reference carries every field (browse name, display name,
    # node class, type definition, ...).
    # END MD

    # BEGIN CODE
    print("\n[BRW]   MyFolder children:")
    for ref in client.browse(folder_id, resultMask=ns0dt.BrowseResultMask.ALL):
        print(
            f"        {ref.browseName}  class={ref.nodeClass}  "
            f"forward={ref.isForward}  target={ref.nodeId}"
        )
    # END CODE

    # BEGIN MD
    # ## 7. Add an Explicit Reference Between Two Objects
    # To demonstrate ``add_reference`` / ``delete_reference`` we add a
    # second folder and then create an ``Organizes`` reference from
    # ``MyFolder`` to ``MyFolder2``. The
    # ``Organizes`` reference we pick is *forward* and points at a
    # sibling, which is the simplest valid case.
    # END MD

    # BEGIN CODE
    obj_attr2 = ObjectAttributes()
    obj_attr2.displayName = o6.LocalizedText("MyFolder2")
    obj_attr2.description = o6.LocalizedText("A second folder object")

    folder2_id = client.addObjectNode(
        parent=OBJECTS_FOLDER,
        browseName=o6.QualifiedName(1, "MyFolder2"),
        attributes=obj_attr2,
        parentReference=ORGANIZES,
    )
    print(f"\n[ADD]   Second Object = {folder2_id}")

    add_status = client.addReference(
        source=folder_id,
        reftype=ORGANIZES,
        target=folder2_id,
    )
    print(f"[REF+]   {folder_id} -Organizes-> {folder2_id}  status={add_status}")

    # Reuse the same BrowseRequest: just re-point bd at the same
    # folder, the server returns the new reference in the next call.
    print("[BRW]   MyFolder children after adding reference:")
    for ref in client.browse(folder_id, resultMask=ns0dt.BrowseResultMask.ALL):
        print(
            f"        {ref.browseName}  class={ref.nodeClass}  "
            f"forward={ref.isForward}  target={ref.nodeId}"
        )

    del_status = client.deleteReference(
        source=folder_id,
        reftype=ORGANIZES,
        target=folder2_id,
    )
    print(f"\n[REF-]   {folder_id} -Organizes-> {folder2_id}  status={del_status}")

    print("[BRW]   MyFolder children after deleting reference:")
    for ref in client.browse(folder_id, resultMask=ns0dt.BrowseResultMask.ALL):
        print(
            f"        {ref.browseName}  class={ref.nodeClass}  "
            f"forward={ref.isForward}  target={ref.nodeId}"
        )
    # END CODE

    # BEGIN MD
    # ## 8. Clean Up
    # ``delete_node`` accepts either a single NodeId or a list of NodeIds.
    # ``delete_target_references`` defaults to ``True``, so the ``Organizes`` reference we just created
    # is removed as part of the second folder's deletion.
    # END MD

    # BEGIN CODE
    print("\n[DEL]   Removing all created nodes ...")
    del_status = client.deleteNode([method_id, temp_id, objtype_id, folder2_id, folder_id])
    print(f"        status = {del_status}")

print("\n=== Example completed ===")
# END CODE
