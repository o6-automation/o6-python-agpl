# Low-level

Demonstrates how to drive an OPC UA server with the raw ``serviceX``
methods exposed by ``o6.Client``. Each ``serviceX`` function maps 1:1
to one of the services defined in the OPC UA specification (Part 4) —
the high-level ``client.read(...)`` / ``client.write(...)`` shortcuts
wrap them internally.

This example talks to the **distilling example server** that ships with
``o6`` in ``examples/advanced_applications/tutorial_server/``; once
running it exposes the ``DistillingSystem`` object under ``Objects/``.

Topics covered:

- ``serviceBrowse`` + ``serviceTranslateBrowsePathsToNodeIds`` —
  enumerating references and resolving a browse path to a NodeId.
- ``serviceRead`` — reading the ``Value`` attribute, plus reading
  ``NodeId`` / ``BrowseName`` / ``DisplayName``.
- ``serviceWrite`` — writing a value back and verifying with a read.
- ``serviceCall`` — calling a method on an object, inspecting input
  and output argument lists.

!!! info "This example needs a running server"
    Start `Distilling Simulation Example: Server` first:

    ```
    python examples/advanced_applications/tutorial_server/server.py
    ```

Every operation in this example goes through the low-level
`serviceX` API. Each method takes a single request struct, returns
the matching response struct, and maps directly to an OPC UA service.
Request/response types live under `o6.ns.ns0`. Never import anything
from `o6._o6` directly.

## 1. Browse — serviceBrowse

`serviceBrowse` enumerates the references of one or more nodes.
Each request contains a list of `BrowseDescription`s; the response
returns matching `BrowseResult`s, each carrying a list of
`ReferenceDescription`s (display name, browse name, target
NodeId, reference type, ...).

`BrowseDirection.FORWARD` follows references out from the node;
`result_mask = 63` asks the server to return every reference
field. The mask is a bitfield — see Part 4 §7.6.2 for the bits.

```python
print("--- 1. Browse — serviceBrowse ---")
browse_request = ns0.datatypes.BrowseRequest()
bd = ns0.datatypes.BrowseDescription()
bd.nodeId = "i=85"  # Objects folder
bd.browseDirection = ns0.datatypes.BrowseDirection.FORWARD
bd.resultMask = 63  # all reference fields
browse_request.nodesToBrowse = [bd]

browse_response = client.serviceBrowse(browse_request)
result = browse_response.results[0]
print(f"Status = {result.statusCode.name} ({hex(int(result.statusCode))})")
print("Children of the Objects folder (i=85):")
for ref in result.references:
    try:
        display = ref.displayName.text
    except AttributeError:
        display = str(ref.displayName)
    print(f"  {display:32s}  {ref.nodeId}  " f"(browseName={ref.browseName})")

# Pick out the `DistillingSystem` child by browse name.  We need
# its full NodeId (including namespace) for everything below —
# the namespace index is allocated dynamically by the server on
# startup, so it is not safe to hard-code.
distilling_node = next(
    r.nodeId for r in result.references if r.browseName.name == "DistillingSystem"
)

# Browse `DistillingSystem` and pick out the children we are going
# to read, write, or call below.  The NodeId for each of them is
# stored in a named Python variable so the later sections can just
# use the variable and not the (server-assigned) numeric id.
sys_request = ns0.datatypes.BrowseRequest()
bd_sys = ns0.datatypes.BrowseDescription()
bd_sys.nodeId = distilling_node
bd_sys.browseDirection = ns0.datatypes.BrowseDirection.FORWARD
bd_sys.resultMask = 63
sys_request.nodesToBrowse = [bd_sys]
sys_response = client.serviceBrowse(sys_request)
sys_children = {r.browseName.name: r.nodeId for r in sys_response.results[0].references}
kettle_node = sys_children["Kettle"]
status_node = sys_children["Status"]
start_node = sys_children["Start"]
shutdown_node = sys_children["Shutdown"]

# Browse the sub-objects for the variables we are going to touch.
sub_request = ns0.datatypes.BrowseRequest()
for parent in (kettle_node, status_node):
    bd = ns0.datatypes.BrowseDescription()
    bd.nodeId = parent
    bd.browseDirection = ns0.datatypes.BrowseDirection.FORWARD
    bd.resultMask = 63
    sub_request.nodesToBrowse.append(bd)
sub_response = client.serviceBrowse(sub_request)
kettle_children = {r.browseName.name: r.nodeId for r in sub_response.results[0].references}
status_children = {r.browseName.name: r.nodeId for r in sub_response.results[1].references}
temperature_node = kettle_children["Temperature"]
state_node = status_children["State"]
setpoint_node = status_children["Setpoint"]
```

### 1b. Translate browse paths — serviceTranslateBrowsePathsToNodeIds
`serviceTranslateBrowsePathsToNodeIds` resolves a chain of
browse-name steps into a NodeId without having to walk the tree.
The path is built from `RelativePathElement`s; each element's
`target_name` is the `QualifiedName` (namespace, name) of one
step in the path.

Below we resolve `<DistillingSystem>/Identification` starting
from the NodeId we picked out of the browse result — the
`target_name` for the path step is built from the namespace
index that the browse returned, so we do not hard-code it.

```python
print()
print("--- 1b. Translate browse paths — serviceTranslateBrowsePathsToNodeIds ---")
translate_request = ns0.datatypes.TranslateBrowsePathsToNodeIdsRequest()
bp = ns0.datatypes.BrowsePath()
bp.startingNode = distilling_node
elem = ns0.datatypes.RelativePathElement()
elem.targetName = o6.QualifiedName(distilling_node.ns.index, "Identification")
bp.relativePath.elements = [elem]
translate_request.browsePaths = [bp]

translate_response = client.serviceTranslateBrowsePathsToNodeIds(translate_request)
target = translate_response.results[0].targets[0]
print(f"<DistillingSystem>/Identification -> {target.targetId}")
```

## 2. Read — serviceRead
`serviceRead` reads one or more *attributes* of one or more
nodes. Each `ReadValueId` picks a NodeId plus an `attribute_id`
(`o6.AttributeId.VALUE` for the variable value,
`o6.AttributeId.BROWSE_NAME` for the browse name, ...).
The response carries a `DataValue` per requested node — `.value`
is the payload, `.status` is the per-node StatusCode.

```python
print()
print("--- 2. Read — serviceRead ---")
read_request = ns0.datatypes.ReadRequest()
rvi = ns0.datatypes.ReadValueId()
rvi.nodeId = temperature_node  # Kettle/Temperature
rvi.attributeId = o6.AttributeId.VALUE
read_request.nodesToRead = [rvi]

read_response = client.serviceRead(read_request)
dv = read_response.results[0]
print(f"Kettle/Temperature = {dv.value} (status {dv.status})")
```

### 2b. Read multiple attributes
The same `ReadRequest` can carry multiple `ReadValueId`s — each
one targets a different attribute of the same or different nodes.
Below we read `NodeId` (1), `BrowseName` (3), and `DisplayName`
(4) for `Status/State` in a single round-trip.

```python
print()
print("--- 2b. Read multiple attributes ---")
rr = ns0.datatypes.ReadRequest()
for attr_id in (
    o6.AttributeId.NODE_ID,
    o6.AttributeId.BROWSE_NAME,
    o6.AttributeId.DISPLAY_NAME,
):
    rvi = ns0.datatypes.ReadValueId()
    rvi.nodeId = state_node  # Status/State
    rvi.attributeId = attr_id
    rr.nodesToRead.append(rvi)

multi = client.serviceRead(rr)
labels = ("NodeId", "BrowseName", "DisplayName")
for label, r in zip(labels, multi.results):
    print(f"  {label} = {r.value}")
```

## 3. Write — serviceWrite
`serviceWrite` mirrors `serviceRead` but assigns values. Each
`WriteValue` carries a NodeId, an `attribute_id`, and a
`DataValue` (`wv.value.value = ...`).  The response contains one
`StatusCode` per write — verify each one is `Good` before
assuming the write landed.

The example server exposes a writable setpoint at
`Status/Setpoint`; most of the address space is read-only (see
"Set the Stage" in the docs for the full address space).

```python
print()
print("--- 3. Write — serviceWrite ---")
write_request = ns0.datatypes.WriteRequest()
wv = ns0.datatypes.WriteValue()
wv.nodeId = setpoint_node  # Status/Setpoint
wv.attributeId = o6.AttributeId.VALUE
wv.value.value = o6.Double(82.5)
write_request.nodesToWrite = [wv]

write_response = client.serviceWrite(write_request)
print(f"Write status -> {write_response.results[0]}")

# Read back to confirm.
rr = ns0.datatypes.ReadRequest()
rvi = ns0.datatypes.ReadValueId()
rvi.nodeId = setpoint_node
rvi.attributeId = o6.AttributeId.VALUE
rr.nodesToRead = [rvi]
verify = client.serviceRead(rr)
print(f"Status/Setpoint = {verify.results[0].value}")
```

## 4. Call — serviceCall
`serviceCall` invokes one or more methods on one or more objects
in a single round-trip. Each `CallMethodRequest` carries the
`object_id`, the `method_id`, and a list of `input_arguments`.
The response holds one `CallMethodResult` per call, with its own
`status_code`, `input_argument_results` (per-input diagnostics),
and `output_arguments` list.

The distilling example server exposes `Start` and `Shutdown`
methods on the `DistillingSystem` object; both take no arguments
and return no arguments.  We resolved the method NodeIds in
section 1 by browsing `DistillingSystem` and looking them up by
browse name; they are passed in here as `start_node` /
`shutdown_node`.

```python
print()
print("--- 4. Call — serviceCall ---")
call_request = ns0.datatypes.CallRequest()
call_request.requestHeader = ns0.datatypes.RequestHeader()
m = ns0.datatypes.CallMethodRequest()
m.objectId = distilling_node
m.methodId = start_node
m.inputArguments = []
call_request.methodsToCall.append(m)

call_response = client.serviceCall(call_request)
result = call_response.results[0]
print(f"Start -> status {result.statusCode}, output {result.outputArguments}")
```

### 4b. Call without input/output arguments
`serviceCall` accepts any number of `CallMethodRequest`s in a
single request. Below we invoke `Shutdown` on the same object —
it has the same nullary signature as `Start`, but the server
uses it to ask for a clean shutdown.

```python
print()
print("--- 4b. Call without input/output arguments ---")
call_request = ns0.datatypes.CallRequest()
call_request.requestHeader = ns0.datatypes.RequestHeader()
m = ns0.datatypes.CallMethodRequest()
m.objectId = distilling_node
m.methodId = shutdown_node
m.inputArguments = []
call_request.methodsToCall.append(m)

call_response = client.serviceCall(call_request)
result = call_response.results[0]
print(f"Shutdown -> status {result.statusCode}, output {result.outputArguments}")
```

## Source Code

Download [`C01_lowlevel.py`](client-C01_lowlevel/C01_lowlevel.py) to run it locally.
