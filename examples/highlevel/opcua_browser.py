import o6

c = o6.Client("opc.tcp://localhost:4840")
c.connect()

print(c.browse_interactive(o6.NodeId("ns=0;i=85")))

c.disconnect()
