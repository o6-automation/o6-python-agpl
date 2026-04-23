"""
Low-level O6 Client Example

Demonstrates direct use of the service_xxx functions, which map 1:1 to the
OPC UA services defined in the OPC UA specification.
"""

import socket
from urllib import response
import o6
from o6 import Client, types

localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"

with Client(endpoint_url) as client:

    # --- service_read ---
    # Read the server's current time (node i=2258, ServerTime)
    read_request = types.ReadRequest()
    rvi = types.ReadValueId()
    rvi.nodeid = "i=2258"
    rvi.attribute_id = o6.AttributeId.VALUE
    read_request.nodes_to_read = [rvi]

    read_response = client.service_read(read_request)
    print("ServerTime:", read_response.results[0].value)

    # --- service_write ---
    write_request = types.WriteRequest()
    wv = types.WriteValue()
    wv.nodeid = "ns=1;s=IntegerVariable"
    wv.attribute_id = o6.AttributeId.VALUE
    wv.value.value = types.UInt32(42)
    write_request.nodes_to_write = [wv]

    write_response = client.service_write(write_request)
    print("Write status:", write_response.results[0])

    # --- service_browse ---
    # Browse the Objects folder (i=85)
    browse_request = types.BrowseRequest()
    bd = types.BrowseDescription()
    bd.nodeid = "i=85"
    bd.browse_direction = types.BrowseDirection.FORWARD
    bd.result_mask = 63  # return all reference fields
    browse_request.nodes_to_browse = [bd]

    browse_response = client.service_browse(browse_request)
    print("Children of Objects folder:")
    for ref in browse_response.results[0].references:
        print(" ", ref.display_name, ref.nodeid)

    # --- service_translate_browse_paths_to_nodeids ---
    # Resolve /Objects/Server from the root folder (i=84)
    translate_request = types.TranslateBrowsePathsToNodeIdsRequest()
    bp = types.BrowsePath()
    bp.starting_node = "i=84"  # RootFolder
    elem1 = types.RelativePathElement()
    elem1.target_name = types.QualifiedName("Objects")
    elem2 = types.RelativePathElement()
    elem2.target_name = types.QualifiedName("Server")
    bp.relative_path.elements = [elem1, elem2]
    translate_request.browse_paths = [bp]

    translate_response = client.service_translate_browse_paths_to_nodeids(
        translate_request
    )
    print("Resolved NodeId:", translate_response.results[0].targets[0].target_id)

    # --- service_browse_next ---
    # Fetch references in pages by limiting the max references per browse call.
    # When a result has a non-empty continuation_point, pass it to
    # service_browse_next to retrieve the remaining references.
    browse_request = types.BrowseRequest()
    browse_request.requested_max_references_per_node = 2  # small page for demo
    bd = types.BrowseDescription()
    bd.nodeid = "i=85"  # Objects folder
    bd.browse_direction = types.BrowseDirection.FORWARD
    bd.result_mask = 63
    browse_request.nodes_to_browse = [bd]

    browse_response = client.service_browse(browse_request)
    result = browse_response.results[0]

    all_refs = list(result.references)
    while result.continuation_point:
        next_request = types.BrowseNextRequest()
        next_request.release_continuation_points = False
        next_request.continuation_points = [result.continuation_point]

        next_response = client.service_browse_next(next_request)
        result = next_response.results[0]
        all_refs.extend(result.references)

    print("All children of Objects folder (paged):")
    for ref in all_refs:
        print(" ", ref.display_name, ref.nodeid)
