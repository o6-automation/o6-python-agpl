# Node Management

Demonstrates how to extend the server's address space at runtime from
the *client* side, using the high-level ``o6.Client`` API. The example
adds an Object, a Variable, a Method, and an ObjectType, links two
Objects with an explicit reference, browses the result, and finally
deletes everything it created.

The example talks to ``S03_firststeps.py``.

!!! info "This example needs a running server"
    Start [Server First Steps](server-S03_firststeps.md) first:

    ```
    python examples/server/S03_firststeps.py
    ```

The relevant API surface lives on the ``o6.Client`` instance:

- ``addObjectNode`` / ``addVariableNode`` / ``addMethodNode`` /
  ``addObjectTypeNode``
- ``addReference`` / ``deleteReference``
- ``deleteNode`` (accepts a single NodeId or a list)

All ``add*Node`` calls are keyword-only and return the NodeId the
client (or the server, if none was requested) chose for the new node.

## 1. Connection Setup
The endpoint URL is the same one ``S03_firststeps.py`` listens on. The
Objects folder (``i=85``) is the conventional parent for user-defined
nodes, and ``Organizes`` (``i=35``) is the standard "folder contains
folder" reference type used to attach a new node to its parent.

```python
localhost = "localhost"
endpoint_url = EXAMPLE_ENDPOINT

OBJECTS_FOLDER = "i=85"
ORGANIZES = "i=35"

print("--- 1. Connection Setup ---")
print(f"Connecting to {endpoint_url} ...")
```

## 2. Add an Object Node
Every node creation follows the same shape: build an ``*Attributes``
struct, set the human-readable fields (``displayName``,
``description``), and pass the struct to the matching
``add*Node`` method along with ``parent``, ``browseName``, and the
reference type that connects the new node to its parent.

``browseName`` can be either a plain string or an
``o6.QualifiedName``; passing ``o6.QualifiedName(1, "MyFolder")``
explicitly places the new node in namespace 1, the same namespace
``S03_firststeps.py`` uses for its own objects.

Every ``add*Node`` call also accepts a ``requestedNodeId=``
keyword (e.g. ``requestedNodeId="ns=1;i=5000"``) to pin a stable
address for the new node; omitting it lets the server pick one. The
server-side equivalent is the ``nodeId=`` keyword on ``addObject`` /
``addVariable`` / ``addMethod``.

```python
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
```

## 3. Add a Variable Node
``VariableAttributes`` is the only one of the four attribute types
that carries a ``value``: the initial value of the variable.
``valueRank = -1`` means *scalar*; positive values indicate an
array of that rank. ``accessLevel = 3`` means "readable and
writable".

```python
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
```

## 4. Add a Method Node
Adding a method node is structurally identical to adding an
object: build a ``MethodAttributes`` and call
``addMethodNode``. The node exists once this call returns, but
it is not invokable until the *server* registers a callback for
it — ``S03_firststeps.py`` does not register one for ``Reset``, so a
later ``client.call(method_id, ...)`` would return
``BAD_NOT_IMPLEMENTED``.

```python
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
```

## 5. Add an ObjectType Node
ObjectTypes are *templates*, so adding one to the address space
does not affect existing objects. To use it, add an object node
whose ``typeDefinition`` references the new ObjectType's NodeId.

```python
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
```

## 6. Browse the New Object's Children
``client.browse(nodeid)`` returns the list of references leading
out from the given node. With ``result_mask=BrowseResultMask.ALL``
each reference carries every field (browse name, display name,
node class, type definition, ...).

```python
print()
print("--- 6. Browse the New Object's Children ---")
print("MyFolder children:")
for ref in client.browse(folder_id, resultMask=ns0dt.BrowseResultMask.ALL):
    print(
        f"  {ref.browseName}  class={ref.nodeClass}  "
        f"forward={ref.isForward}  target={ref.nodeId}"
    )
```

## 7. Add an Explicit Reference Between Two Objects
To demonstrate ``addReference`` / ``deleteReference`` we add a
second folder and create an ``Organizes`` reference from
``MyFolder`` to ``MyFolder2`` — a forward reference to a sibling,
the simplest valid case.

```python
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
```

## 8. Clean Up
``deleteNode`` accepts either a single NodeId or a list of
NodeIds. ``deleteTargetReferences`` defaults to ``True``, so the
``Organizes`` reference created above is removed as part of the
second folder's deletion.

```python
    print()
    print("--- 8. Clean Up ---")
    targets = [method_id, temp_id, objtype_id, folder2_id, folder_id]
    del_statuses = client.deleteNode(targets)
    for target, status in zip(targets, del_statuses):
        print(f"Delete {target}: {status}")
        status.check()

print()
print("=== Example completed ===")
```

## Source Code

Download [`C07_nodemanagement.py`](client-C07_nodemanagement/C07_nodemanagement.py) to run it locally.
