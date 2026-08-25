# Connecting a Variable with a Physical Process

Source: `examples/highlevel/c-tutorial-examples/tutorial_server_datasource.py`

The low-level open62541 tutorial uses a data source callback. The high-level
Python API does not expose that exact hook yet, so this page mirrors the intent
with direct variable updates and a small wrapper around the physical value.

## Updating Variables Manually

```python
from datetime import datetime
from o6 import Server

with Server() as server:
	current_time = server.addVariable("Current Time", server.objectsNode, str(datetime.now()))

	server.write(current_time.nodeId, str(datetime.now()))
	print(server.read(current_time.nodeId))
```

## Variable Value Callback

```python
from datetime import datetime
from o6 import Server


class TimeSource:
	def read(self) -> str:
		return str(datetime.now())


with Server() as server:
	source = TimeSource()
	current_time = server.addVariable("Current Time", server.objectsNode, source.read())

	server.write(current_time.nodeId, source.read())
	print(server.read(current_time.nodeId))
```

## Variable Data Sources

```python
from o6 import Server


class ProcessValue:
	def __init__(self) -> None:
		self.temperature = 20.0

	def sample(self) -> float:
		self.temperature += 0.1
		return self.temperature


with Server() as server:
	process = ProcessValue()
	temperature = server.addVariable("Temperature", server.objectsNode, process.sample())

	server.write(temperature.nodeId, process.sample())
	print(server.read(temperature.nodeId))
```
