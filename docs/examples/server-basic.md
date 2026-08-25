# Basic Server Example

Source example: `examples/highlevel/basic_server.py`

This server creates a small address space with variables and a method below a custom object. It is a compact example of how the high-level server API maps Python code to OPC UA nodes.

## Explanation

### Building the object tree

The script creates a `Plant` object below the Objects folder and then adds variables underneath it.

```python
plant = server.addObject("Plant", server.objectsNode)

temperature = server.addVariable("Temperature", plant, 22.5, nodeId="ns=1;i=1001")
pressure = server.addVariable("Pressure", plant, 1013.25, nodeId="ns=1;i=1002")
status = server.addVariable("Status", plant, "idle", nodeId="ns=1;i=1003")
counter = server.addVariable("Counter", plant, 0, nodeId="ns=1;i=1004")
```

### Adding a callable method

```python
def add_numbers(a, b):
	return [a + b]

server.addMethod(
	"Add",
	plant,
	add_numbers,
	inputArgs=[
		ns0.datatypes.Argument(name="A", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="First operand"),
		ns0.datatypes.Argument(name="B", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="Second operand"),
	],
	outputArgs=[
		ns0.datatypes.Argument(name="Sum", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="A + B"),
	],
	nodeId="ns=1;i=2001",
)
```

### Updating values at runtime

```python
while True:
	i += 1
	temperature.value = 22.5 + (i % 10) * 0.1
	counter.value = i
	time.sleep(1.0)
```

## Full source

```python
#!/usr/bin/env python3

import time
import o6
from o6 import Server
from o6.ns import ns0


def main():
	server = Server(port=4840)

	plant = server.addObject("Plant", server.objectsNode)

	temperature = server.addVariable(
		"Temperature",
		plant,
		22.5,
		nodeId="ns=1;i=1001",
	)
	pressure = server.addVariable(
		"Pressure",
		plant,
		1013.25,
		nodeId="ns=1;i=1002",
	)
	status = server.addVariable(
		"Status",
		plant,
		"idle",
		nodeId="ns=1;i=1003",
	)
	counter = server.addVariable(
		"Counter",
		plant,
		0,
		nodeId="ns=1;i=1004",
	)

	def add_numbers(a, b):
		print(f"  Method called: {a} + {b} = {a + b}")
		return [a + b]

	server.addMethod(
		"Add",
		plant,
		add_numbers,
		inputArgs=[
			ns0.datatypes.Argument(name="A", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="First operand"),
			ns0.datatypes.Argument(name="B", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="Second operand"),
		],
		outputArgs=[
			ns0.datatypes.Argument(name="Sum", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="A + B"),
		],
		nodeId="ns=1;i=2001",
	)

	server.start()
	print("Server running at opc.tcp://localhost:4840")
	print("Press Ctrl+C to stop.\n")

	try:
		i = 0
		while True:
			i += 1
			temperature.value = 22.5 + (i % 10) * 0.1
			counter.value = i

			if i % 10 == 0:
				print(f"  Counter={i}, Temp={temperature.value:.1f}")

			time.sleep(1.0)
	except KeyboardInterrupt:
		print("\nShutting down…")
	finally:
		server.stop()
		print("Server stopped.")


if __name__ == "__main__":
	main()
```