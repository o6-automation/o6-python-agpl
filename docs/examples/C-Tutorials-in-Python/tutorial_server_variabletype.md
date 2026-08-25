# Working with Variable Types

Source: `examples/highlevel/c-tutorial-examples/tutorial_server_variabletype.py`

## 2DPoint Type

```python
from o6 import Server

with Server() as server:
	point_type = server.addVariableType(
		"2DPoint Type",
		dataType="i=11",
		valueRank=1,
	)
	print(point_type.nodeId)
```

## Adding a 2DPoint Variable

```python
from o6 import Server

with Server() as server:
	point_type = server.addVariableType("2DPoint Type", dataType="i=11", valueRank=1)
	point_variable = server.addVariable(
		"2DPoint Variable",
		server.objectsNode,
		[0.0, 0.0],
		dataType="i=11",
	)
	print(server.read(point_variable.nodeId))
```

## Type Mismatch

```python
from o6 import Server

with Server() as server:
	point_variable = server.addVariable(
		"2DPoint Variable",
		server.objectsNode,
		[0.0, 0.0],
		dataType="i=11",
	)

	try:
		server.write(point_variable.nodeId, "2dpoint")
	except Exception as exc:
		print(f"Type mismatch rejected: {exc}")
```

## Write Constraints

```python
from o6 import Server

with Server() as server:
	point_variable = server.addVariable(
		"2DPoint Variable",
		server.objectsNode,
		[0.0, 0.0],
		dataType="i=11",
	)

	server.write(point_variable.nodeId, [1.0, 1.0])
	print(server.read(point_variable.nodeId))
```
