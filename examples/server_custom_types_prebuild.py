"""
Server + Client example with custom (complex) DataTypes loaded from a NodeSet2 XML.

Both sides load the same DI companion spec to learn about custom struct types.
The server creates a variable whose data type is the DI
``TransferResultDataDataType`` and the client reads, modifies and writes it back.
"""

import time
import o6
from o6 import Client, Server

ns = o6.namespaces.Namespaces()
di = ns.append("./examples/Opc.Ua.Di.NodeSet2.xml")


PORT = 4842

# ---------------------------------------------------------------------------
# 1. Server: load DI types and publish a variable with a custom struct value
# ---------------------------------------------------------------------------

server = Server(port=PORT)
di = server.ns.append(di)

print("=== Server: registered DI types ===")
for name in sorted(vars(di._types)):
    print(f"  {name}")

# Build an initial TransferResultDataDataType value
initial = di.TransferResultDataDataType()
initial.sequence_number = 1
initial.end_of_results = True

# Create a ParameterResultDataType element
param = di.ParameterResultDataType()
param.node_path = [o6.QualifiedName("1:Pump"), o6.QualifiedName("1:Speed")]
param.status_code = o6.StatusCode(0)
initial.parameter_defs = [param]

print(f"\nInitial value: {initial}")

# Expose it as a variable node.
# The custom type is inferred from the value automatically.
node = server.add_variable(
    "TransferResult",
    server.objects_node,
    initial,
    nodeid="ns=1;i=1000",
)
print(f"Server variable created: {node.nodeid}")

server.start()
time.sleep(0.2)

# ---------------------------------------------------------------------------
# 2. Client: connect, load same types, read, modify, write
# ---------------------------------------------------------------------------

client = Client(f"opc.tcp://localhost:{PORT}")
di_client = client.ns.append(di)
client.connect()

print("\n=== Client: registered DI types ===")
for name in sorted(vars(di_client._types)):
    print(f"  {name}")

# Read the structured value
val = client.read("ns=1;i=1000")
print(f"\nRead value: {val}")
print(f"  type = {type(val).__name__}")
print(f"  sequence_number = {val.sequence_number}")
print(f"  end_of_results  = {val.end_of_results}")
print(f"  parameter_defs  = {val.parameter_defs}")

# Modify and write back
val.sequence_number = 42
val.end_of_results = False

param2 = di_client.ParameterResultDataType()
param2.node_path = [o6.QualifiedName("1:Tank"), o6.QualifiedName("1:Level")]
param2.status_code = o6.StatusCode(0)
val.parameter_defs = [val.parameter_defs[0], param2]

client.write("ns=1;i=1000", val)
print("\nWrote modified value back to server")

# Verify round-trip from server side
server_val = server.read_value(o6.NodeId("ns=1;i=1000"))
print(f"\nServer sees: {server_val}")
print(f"  sequence_number = {server_val.sequence_number}")
print(f"  end_of_results  = {server_val.end_of_results}")
print(f"  parameter_defs  = {server_val.parameter_defs}")

# ---------------------------------------------------------------------------
# 3. Cleanup
# ---------------------------------------------------------------------------

client.disconnect()
del client
server.stop()

print("\nDone.")
