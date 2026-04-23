import o6
from o6 import Client, Server

# server = Server(port=4840)
# server.add_variable(
#    "A",
#    server.objects_node,
#    o6.UInt32(10),
#    nodeid="ns=1;i=101",
#    data_type=o6.NodeId(o6.ns.ns0.datatypes.BaseDataType.Number.UInteger.UInt32()),
# )
#
# server.start()
#
#
# c = Client("opc.tcp://localhost:4840")
#
# d = c.ns.append("./examples/Opc.Ua.Di.NodeSet2.xml")
#
#
## Show registered types
# print("=== Registered types ===")
# for name in sorted(vars(d.types)):
#    cls = getattr(d.types, name)
#    print(f"  {name}: {cls}")
#
# print()
#
## Try instantiating a custom struct type
# if hasattr(d.types, "TransferResultDataDataType"):
#    # t = d.types.TransferResultDataDataType()
#    t = c.ns.DI.TransferResultDataDataType()
#    print(f"Instance: {t}")
#    print(f"Type: {type(t)}")
#
#
# print("======== DONE ==========")
#
# del c
#
#
# server.stop()


dv = o6.DataValue()

print("a")
dv.value = [1, 2, 3]
print("b")
dv.value = o6.ReadRequest()
print("c")

quit()

import socket

import timeit

print("Loading nodesets...")
start = timeit.default_timer()

print(type(o6.ns.di.FetchResultDataType()))

elapsed = timeit.default_timer() - start

print(f"Elapsed time: {elapsed:.6f} seconds")
quit()

localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"

c = o6.Client()
c.config.endpoint_url = endpoint_url

c.connect()
v = c.read("i=2258")
print(f'Reading value v="{v}"')

o = c.root.Objects

o.ScalarVariables.IntegerVariable(42)
i = o.ScalarVariables.IntegerVariable()

print(i)

print(o.__dir__())


c.disconnect()
