"""
Playground: LADS extension object namespace-index translation

Goal:
  Verify that when a client writes a LADS extension object (struct) to a
  server variable, the extension object's encoding NodeId is translated
  correctly — i.e. the server decodes the struct without any manual index
  remapping on its side.

Setup:
  Both server and client open with an application namespace slot at ns=1, so
  canonical pre-registration would give them the same indices.  To create a
  real difference the server is created with canonical pre-registration
  suppressed, so it builds a fresh (shorter) namespace table:

    Server: ns=0 UA | ns=1 app | ns=2 DI | ns=3 IA | ns=4 AMB | ns=5 LADS
    Client: ns=0 UA | ns=1 …  | ns=2 DI | ns=3 IA | ns=4 Mach | ns=5 AMB | ns=6 LADS

The extension object's binary encoding NodeId carries the CLIENT's LADS index
(ns=6) on the wire.  open62541 maps it to the server's LADS index (ns=5)
during decoding.
"""

import time

import o6
import o6.namespaces
from o6 import Client, Server

PORT = 4843

# ────────────────────────────────────────────────────────────────────
# 1. Server — suppress canonical pre-registration so LADS gets a
#    fresh, lower index than on the client.
# ────────────────────────────────────────────────────────────────────

# Temporarily replace _reserve_canonical_owner_namespaces with a no-op
# so the server does NOT pre-register all canonical companion namespace
# URIs at init time.  This lets us register only the deps we actually
# need, in order, giving LADS a smaller index than on the client.
_orig_reserve = o6.namespaces.Namespaces._reserve_canonical_owner_namespaces
o6.namespaces.Namespaces._reserve_canonical_owner_namespaces = lambda self, owner: None
try:
    server = Server(port=PORT)
finally:
    o6.namespaces.Namespaces._reserve_canonical_owner_namespaces = _orig_reserve

# Load only what LADS needs, in dependency order.
# ns=0 UA, ns=1 server-app are automatic; we assign:
#   ns=2 DI, ns=3 IA, ns=4 AMB, ns=5 LADS
server.ns.append(o6.ns.di)
server.ns.append(o6.ns.ia)
# machinery has no struct/enum types — skip its append.
server.ns.append(o6.ns.amb)
srv_lads = server.ns.append(o6.ns.lads)

print(f"Server  LADS ns index : {srv_lads.metadata.index}")

# Declare a variable whose DataType is LADS KeyValueType.
initial = srv_lads.KeyValueType()
initial.key = "sensor_id"
initial.value = "0"

var_nodeid = "ns=1;i=2000"
server.add_variable("SensorKV", server.objects_node, initial, nodeid=var_nodeid)

server.start()
time.sleep(0.2)

# ────────────────────────────────────────────────────────────────────
# 2. Client — created normally; canonical pre-registration gives it
#    LADS at a HIGHER index than the server.
# ────────────────────────────────────────────────────────────────────

client = Client(f"opc.tcp://localhost:{PORT}")

# The client's _reserve_canonical_owner_namespaces pre-registers
# Machinery at ns=4 before AMB, so LADS lands at ns=6 here vs ns=5 on
# the server.
client.ns.append(o6.ns.di)
client.ns.append(o6.ns.ia)
client.ns.append(o6.ns.amb)
cli_lads = client.ns.append(o6.ns.lads)

print(f"Client  LADS ns index : {cli_lads.metadata.index}")

assert srv_lads.metadata.index != cli_lads.metadata.index, (
    f"Server and client LADS indices are identical ({srv_lads.metadata.index}); "
    "the test would not exercise index translation."
)

client.connect()

# Read the initial value to confirm baseline decoding works.
val_initial = client.read(var_nodeid)
print(f"\nInitial read  : {val_initial!r}")
print(f"  key   = {val_initial.key!r}")
print(f"  value = {val_initial.value!r}")

# Build a KeyValueType on the CLIENT side.
# When written over the wire its ExtensionObject encoding NodeId carries
# the CLIENT's LADS namespace index.  The server must translate that index
# to its own before it can decode the struct.
new_val = o6.ns.lads.datatypes.KeyValueType()
new_val.key = "temperature"
new_val.value = "98.6"

# Sanity-check: server's, client's and global descriptor's Python type
# objects are identical instances.
assert type(new_val) is type(cli_lads.datatypes.KeyValueType())
assert type(new_val) is type(srv_lads.datatypes.KeyValueType())

print(
    f"\nClient writing KeyValueType (encoding NodeId uses client ns="
    f"{cli_lads.metadata.index}) …"
)
client.write(var_nodeid, new_val)

# ────────────────────────────────────────────────────────────────────
# 3. Server-side read-back — must decode without any manual translation
# ────────────────────────────────────────────────────────────────────

srv_val = server.read(o6.NodeId(var_nodeid))
print(f"\nServer read-back : {srv_val!r}")
print(f"  key   = {srv_val.key!r}")
print(f"  value = {srv_val.value!r}")

assert srv_val.key == "temperature", f"key mismatch: {srv_val.key!r}"
assert srv_val.value == "98.6", f"value mismatch: {srv_val.value!r}"

print(
    "\n✓  Server decoded the extension object correctly "
    f"(client ns={cli_lads.metadata.index} → server ns={srv_lads.metadata.index})."
)

# ────────────────────────────────────────────────────────────────────
# 4. Cleanup
# ────────────────────────────────────────────────────────────────────

client.disconnect()
del client
server.stop()
print("Done.")

