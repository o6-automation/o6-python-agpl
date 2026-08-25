# Building a Simple Server

Source: `examples/highlevel/c-tutorial-examples/tutorial_server_firststeps.py`

## Server Configuration and Plugins

```python
from o6 import Server

server = Server(
	port=4840,
	applicationUri="urn:o6-python:server:first-steps",
)

server.config.applicationDescription.applicationName.text = "My Python Server"
server.config.applicationDescription.productUri = "urn:o6-python:product"
```

## Server Lifecycle

```python
from o6 import Server

with Server(port=4840) as server:
	temperature = server.addVariable("Temperature", server.objectsNode, 25.0)
	print(server.read(temperature.nodeId))

	server.write(temperature.nodeId, 26.5)
	print(server.read(temperature.nodeId))
```
