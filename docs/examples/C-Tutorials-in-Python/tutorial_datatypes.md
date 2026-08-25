# Working with Data Types

Source: `examples/highlevel/c-tutorial-examples/tutorial_datatypes.py`

## Basic Data Handling

```python
from o6 import Server

with Server() as server:
	answer = server.addVariable("The Answer", server.objectsNode, 42)
	greeting = server.addVariable("Greeting", server.objectsNode, "Hello")

	print(server.read(answer.nodeId))
	server.write(answer.nodeId, 43)
	server.write(greeting.nodeId, "Hello World")
```

## NodeIds

```python
from o6 import NodeId, Server

with Server() as server:
	nodeId = NodeId("ns=1;s=my.node")
	variable = server.addVariable("My Node", server.objectsNode, 1, nodeId=nodeid)
	print(variable.nodeId)
```

## Variants

```python
from o6 import Server, types

with Server() as server:
	data = server.addVariable("Variant Value", server.objectsNode, [1, 2, 3])
	server.write(data.nodeId, [4, 5, 6])

	wrapped = types.DataValue()
	wrapped.value = types.Variant([1.0, 2.0, 3.0])
	server.write(data.nodeId, wrapped)
```
