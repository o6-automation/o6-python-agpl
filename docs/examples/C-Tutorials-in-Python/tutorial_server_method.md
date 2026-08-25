# Adding Methods to Objects

Source: `examples/highlevel/c-tutorial-examples/tutorial_server_method.py`

## Hello World

```python
import o6
from o6 import Server
from o6.ns import ns0


def hello_world(name: str) -> list[str]:
	return [f"Hello {name}"]


with Server() as server:
	server.addMethod(
		"Hello World",
		server.objectsNode,
		hello_world,
		inputArgs=[ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=o6.ValueRank.SCALAR)],
		outputArgs=[ns0.datatypes.Argument(name="Greeting", dataType=o6.String, valueRank=o6.ValueRank.SCALAR)],
	)
```

## Increase Array Values

```python
import o6
from o6 import Server
from o6.ns import ns0


def increase_array_values(values: list[float], delta: float) -> list[list[float]]:
	return [[value + delta for value in values]]


with Server() as server:
	server.addMethod(
		"Increase Array Values",
		server.objectsNode,
		increase_array_values,
		inputArgs=[ns0.datatypes.Argument(name="Values", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR), ns0.datatypes.Argument(name="Delta", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR)],
		outputArgs=[ns0.datatypes.Argument(name="Result", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR)],
	)
```
