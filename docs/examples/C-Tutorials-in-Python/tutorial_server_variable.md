# Adding Variables to a Server

Source: `examples/highlevel/c-tutorial-examples/tutorial_server_variable.py`

## Adding a Variable

```python
from o6 import Server

with Server() as server:
	my_variable = server.addVariable("The Answer", server.objectsNode, 42)
	print(server.read(my_variable.nodeId))
```

## Writing to a Variable

```python
from o6 import Server

with Server() as server:
	my_variable = server.addVariable("The Answer", server.objectsNode, 42)
	server.write(my_variable.nodeId, 43)
	print(server.read(my_variable.nodeId))
```

## Matrix Values

```python
from o6 import Server

with Server() as server:
	matrix = server.addVariable(
		"Double Matrix",
		server.objectsNode,
		[[1.1, 1.2], [2.1, 2.2]],
	)
	print(server.read(matrix.nodeId))
```

## Type Checking

```python
from o6 import Server

with Server() as server:
	my_variable = server.addVariable("The Answer", server.objectsNode, 42)

	try:
		server.write(my_variable.nodeId, "forty-two")
	except Exception as exc:
		print(f"Rejected incompatible write: {exc}")
```
