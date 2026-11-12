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
Low-level OPC UA Client Example
===============================

Drives an OPC UA server with the raw ``serviceX`` methods of
``o6.Client``. Each ``serviceX`` method maps 1:1 to a service of OPC UA
Part 4. The high-level ``client.read(...)`` and ``client.write(...)``
shortcuts wrap them.

The example runs against the tutorial server, which exposes the
``DistillingSystem`` object under ``Objects/``.

Topics covered:

- ``serviceBrowse`` and ``serviceTranslateBrowsePathsToNodeIds``:
  enumerate references and resolve a browse path to a NodeId.
- ``serviceRead``: read the ``Value`` attribute, plus ``NodeId``,
  ``BrowseName`` and ``DisplayName``.
- ``serviceWrite``: write a value and verify it with a read.
- ``serviceCall``: call a method and inspect its input and output
  arguments.
"""

# BEGIN MD
# Each `serviceX` method takes one request struct, returns the matching
# response struct and maps to one OPC UA service. Request and response
# types live under `o6.ns.ns0`. Never import from `o6._o6` directly.
# END MD

import os

import socket

import o6
from o6.ns import ns0

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))
EXAMPLE_ENDPOINT = f"opc.tcp://localhost:{EXAMPLE_PORT}"

# Use the canonical hostname so the server's reported EndpointUrl
# matches what we used to dial in. Some servers reject requests when
# the discovery EndpointUrl differs from the connection URL.
localhost = "localhost"
endpoint_url = EXAMPLE_ENDPOINT
print(f"Connecting to {endpoint_url} ...")


# ---------------------------------------------------------------------------
# The client connection is held open for the whole script — every section
# below calls a `client.serviceX()` method against the same session.
# ---------------------------------------------------------------------------
with o6.Client(endpoint_url) as client:

    # BEGIN MD
    # ## 1. Browse — serviceBrowse
    #
    # `serviceBrowse` enumerates the references of one or more nodes. The
    # request holds a list of `BrowseDescription`s. The response holds one
    # `BrowseResult` per description, each with a list of
    # `ReferenceDescription`s (display name, BrowseName, target NodeId,
    # reference type, ...).
    #
    # `BrowseDirection.FORWARD` follows references out of the node.
    # `resultMask = 63` requests every reference field. The mask is a
    # bitfield; Part 4 §7.6.2 lists the bits.
    # END MD

    # BEGIN CODE
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
    # END CODE

    # BEGIN MD
    # ### 1b. Translate browse paths — serviceTranslateBrowsePathsToNodeIds
    # `serviceTranslateBrowsePathsToNodeIds` resolves a chain of BrowseName
    # steps to a NodeId without walking the tree. The path is a list of
    # `RelativePathElement`s. Each element's `targetName` is the
    # `QualifiedName` (namespace, name) of one step.
    #
    # The code resolves `<DistillingSystem>/Identification`. The namespace
    # index of `targetName` comes from the browse result, so it is not
    # hard-coded.
    # END MD

    # BEGIN CODE
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
    # END CODE

    # BEGIN MD
    # ## 2. Read — serviceRead
    # `serviceRead` reads one or more attributes of one or more nodes. Each
    # `ReadValueId` names a NodeId and an `attributeId`
    # (`o6.AttributeId.VALUE` for the value, `o6.AttributeId.BROWSE_NAME` for
    # the BrowseName, ...). The response holds one `DataValue` per
    # `ReadValueId`: `.value` is the payload, `.status` the per-node
    # StatusCode.
    # END MD

    # BEGIN CODE
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
    # END CODE

    # BEGIN MD
    # ### 2b. Read multiple attributes
    # One `ReadRequest` can carry several `ReadValueId`s, for the same or
    # different nodes. This one reads `NodeId` (1), `BrowseName` (3) and
    # `DisplayName` (4) of `Status/State` in a single round-trip.
    # END MD

    # BEGIN CODE
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
    # END CODE

    # BEGIN MD
    # ## 3. Write — serviceWrite
    # `serviceWrite` mirrors `serviceRead`. Each `WriteValue` carries a
    # NodeId, an `attributeId` and a `DataValue` (`wv.value.value = ...`).
    # The response holds one `StatusCode` per write. Check that each one is
    # `Good` before you rely on the write.
    #
    # `Status/Setpoint` is writable. Most of the tutorial server's address
    # space is read-only (see "Set the Stage" for the full address space).
    # END MD

    # BEGIN CODE
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
    # END CODE

    # BEGIN MD
    # ## 4. Call — serviceCall
    # `serviceCall` invokes one or more methods in a single round-trip. Each
    # `CallMethodRequest` carries the `objectId`, the `methodId` and a list
    # of `inputArguments`. The response holds one `CallMethodResult` per
    # call, with its own `statusCode`, `inputArgumentResults` (per-input
    # diagnostics) and `outputArguments`.
    #
    # `DistillingSystem` has `Start` and `Shutdown` methods. Neither takes or
    # returns arguments. Section 1 resolved their NodeIds by BrowseName as
    # `start_node` and `shutdown_node`.
    # END MD

    # BEGIN CODE
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
    # END CODE

    # BEGIN MD
    # ### 4b. Call without input/output arguments
    # This call invokes `Shutdown` on the same object. It has the same
    # signature as `Start`; the server uses it to request a clean shutdown.
    # One `CallRequest` can also carry several `CallMethodRequest`s.
    # END MD

    # BEGIN CODE
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
    # END CODE


# Connection is closed automatically when the `with` block exits.
print()
print("Connection closed.")
print("=== Example completed ===")
