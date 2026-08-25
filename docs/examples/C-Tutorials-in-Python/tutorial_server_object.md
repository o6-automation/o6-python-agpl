# Working with Objects and Object Types

Source: `examples/highlevel/c-tutorial-examples/tutorial_server_object.py`

## Using Objects to Structure Information Models

```python
from o6 import Server

with Server() as server:
	plant = server.addObject("Plant", server.objectsNode)
	pump = server.addObject("Pump", plant.nodeId)
	server.addVariable("Speed", pump.nodeId, 1450.0)
	server.addVariable("Status", pump.nodeId, True)
```

## Object Types and Hierarchies

```python
from o6 import Server

with Server() as server:
	device_type = server.addObjectType("DeviceType")
	pump_type = server.addObjectType("PumpType", parent=device_type.nodeId)

	pump = server.addObject(
		"Boiler Pump",
		server.objectsNode,
		typeDefinition=pump_type.nodeId,
	)
	server.addVariable("Flow", pump.nodeId, 12.5)
```

## Instantiation

```python
from o6 import Server

with Server() as server:
	pump_type = server.addObjectType("PumpType")
	pump = server.addObject("Pump 1", server.objectsNode, typeDefinition=pump_type.nodeId)
	print(pump.nodeId)
```
