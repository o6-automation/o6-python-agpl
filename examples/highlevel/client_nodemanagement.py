"""
Node Management Example

Demonstrates adding and deleting different node types and references
using the high-level API.
Requires a running OPC UA server (e.g. the testserver).
"""

from o6 import Client, types
import socket

localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"

# The Objects folder (i=85) is the standard parent for user-created nodes
OBJECTS_FOLDER = "i=85"


def main():
    with Client(endpoint_url) as client:
        print("Connected.\n")

        # --- Add an Object node (a folder-like container) ---
        obj_attr = types.ObjectAttributes()
        obj_attr.display_name = types.LocalizedText("MyFolder")
        obj_attr.description = types.LocalizedText("An example folder object")

        folder_id = client.add_object_node(
            parent_nodeid=OBJECTS_FOLDER,
            # browse_name="1:MyFolder",
            browse_name=types.QualifiedName(1, "MyFolder"),
            node_attributes=obj_attr,
            reference_type_id="i=35",  # Organizes
        )
        print(f"Added Object node: {folder_id}")

        # --- Add a Variable node under the new folder ---
        var_attr = types.VariableAttributes()
        var_attr.display_name = types.LocalizedText("Temperature")
        var_attr.description = types.LocalizedText("A temperature sensor value")
        var_attr.value = types.Double(21.5)
        var_attr.data_type = types.NodeId(11)  # Double
        var_attr.value_rank = -1  # Scalar
        var_attr.access_level = 3  # read + write
        var_attr.user_access_level = 3

        temp_id = client.add_variable_node(
            parent_nodeid=folder_id,
            browse_name=types.QualifiedName(1, "Temperature"),
            node_attributes=var_attr,
        )
        print(f"Added Variable node: {temp_id}")

        # Read back the value we set via the attributes
        value = client.read(temp_id)
        print(f"  Initial value: {value}")

        # --- Add a Method node ---
        method_attr = types.MethodAttributes()
        method_attr.display_name = types.LocalizedText("Reset")
        method_attr.description = types.LocalizedText("Reset the sensor")
        method_attr.executable = True
        method_attr.user_executable = True

        method_id = client.add_method_node(
            parent_nodeid=folder_id,
            browse_name=types.QualifiedName(1, "Reset"),
            node_attributes=method_attr,
        )
        print(f"Added Method node: {method_id}")

        # --- Add an ObjectType node ---
        objtype_attr = types.ObjectTypeAttributes()
        objtype_attr.display_name = types.LocalizedText("SensorType")
        objtype_attr.description = types.LocalizedText("A custom sensor type")

        objtype_id = client.add_object_type_node(
            parent_nodeid="i=58",  # BaseObjectType
            browse_name=types.QualifiedName(1, "SensorType"),
            node_attributes=objtype_attr,
        )
        print(f"Added ObjectType node: {objtype_id}")

        # --- Browse to verify the nodes exist ---
        print("\nBrowsing MyFolder children...")
        browse_request = types.BrowseRequest()
        bd = types.BrowseDescription()
        bd.nodeid = folder_id
        bd.browse_direction = types.BrowseDirection.FORWARD
        bd.result_mask = 63  # All fields
        browse_request.nodes_to_browse = [bd]
        browse_response = client.service_browse(browse_request)
        for ref in browse_response.results[0].references:
            print(f"  {ref.browse_name} ({ref.node_class})")

        # --- Add a second Object node to demonstrate references ---
        obj_attr2 = types.ObjectAttributes()
        obj_attr2.display_name = types.LocalizedText("MyFolder2")
        obj_attr2.description = types.LocalizedText("A second folder object")

        folder2_id = client.add_object_node(
            parent_nodeid=OBJECTS_FOLDER,
            browse_name=types.QualifiedName(1, "MyFolder2"),
            node_attributes=obj_attr2,
            reference_type_id="i=35",  # Organizes
        )
        print(f"\nAdded second Object node: {folder2_id}")

        # --- Add a reference between the two folders ---
        # Create an Organizes (i=35) reference from MyFolder to MyFolder2
        client.add_reference(
            source_nodeid=folder_id,
            reference_type_id="i=35",  # Organizes
            target_nodeid=folder2_id,
        )
        print(f"Added Organizes reference: {folder_id} -> {folder2_id}")

        # Browse MyFolder again to see the new reference
        print("\nBrowsing MyFolder children after adding reference...")
        bd.nodeid = folder_id
        browse_request.nodes_to_browse = [bd]
        browse_response = client.service_browse(browse_request)
        for ref in browse_response.results[0].references:
            print(f"  {ref.browse_name} ({ref.node_class})")

        # --- Delete the reference ---
        client.delete_reference(
            source_nodeid=folder_id,
            reference_type_id="i=35",  # Organizes
            target_nodeid=folder2_id,
        )
        print(f"\nDeleted Organizes reference: {folder_id} -> {folder2_id}")

        # Browse MyFolder again to confirm the reference is gone
        print("\nBrowsing MyFolder children after deleting reference...")
        browse_response = client.service_browse(browse_request)
        for ref in browse_response.results[0].references:
            print(f"  {ref.browse_name} ({ref.node_class})")

        # --- Delete all created nodes ---
        print("\nDeleting nodes...")
        client.delete_node([method_id, temp_id, objtype_id, folder2_id, folder_id])
        print("All nodes deleted.")


if __name__ == "__main__":
    main()
