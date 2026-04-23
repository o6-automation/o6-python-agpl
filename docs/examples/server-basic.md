# Basic Server Example

Source example: `examples/highlevel/basic_server.py`

This server creates a small address space with variables and a method below a custom object. It is a compact example of how the high-level server API maps Python code to OPC UA nodes.

## Explanation

### Building the object tree

The script creates a `Plant` object below the Objects folder and then adds variables underneath it.

```python
plant = server.add_object("Plant", server.objects_node)

temperature = server.add_variable("Temperature", plant, 22.5, nodeid="ns=1;i=1001")
pressure = server.add_variable("Pressure", plant, 1013.25, nodeid="ns=1;i=1002")
status = server.add_variable("Status", plant, "idle", nodeid="ns=1;i=1003")
counter = server.add_variable("Counter", plant, 0, nodeid="ns=1;i=1004")
```

### Adding a callable method

```python
def add_numbers(a, b):
	return [a + b]

server.add_method(
	"Add",
	plant,
	add_numbers,
	input_args=[
		make_argument("A", "i=11", description="First operand"),
		make_argument("B", "i=11", description="Second operand"),
	],
	output_args=[
		make_argument("Sum", "i=11", description="A + B"),
	],
	nodeid="ns=1;i=2001",
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
from o6 import Server
from o6.server import make_argument


def main():
	server = Server(port=4840)

	plant = server.add_object("Plant", server.objects_node)

	temperature = server.add_variable(
		"Temperature",
		plant,
		22.5,
		nodeid="ns=1;i=1001",
	)
	pressure = server.add_variable(
		"Pressure",
		plant,
		1013.25,
		nodeid="ns=1;i=1002",
	)
	status = server.add_variable(
		"Status",
		plant,
		"idle",
		nodeid="ns=1;i=1003",
	)
	counter = server.add_variable(
		"Counter",
		plant,
		0,
		nodeid="ns=1;i=1004",
	)

	def add_numbers(a, b):
		print(f"  Method called: {a} + {b} = {a + b}")
		return [a + b]

	server.add_method(
		"Add",
		plant,
		add_numbers,
		input_args=[
			make_argument("A", "i=11", description="First operand"),
			make_argument("B", "i=11", description="Second operand"),
		],
		output_args=[
			make_argument("Sum", "i=11", description="A + B"),
		],
		nodeid="ns=1;i=2001",
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