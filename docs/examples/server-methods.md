# Server Methods Example

Source example: `examples/highlevel/server_methods.py`

This example concentrates on server-side methods. It shows how to group several callbacks under one object and how different OPC UA method signatures are declared in Python.

## Explanation

### Organizing methods below an object


```python
calculator = server.addObject(
	"Calculator", server.objectsNode, nodeId="ns=1;i=100"
)
```


### A method without arguments

`Reset` is the smallest possible method example. The callback takes no parameters and returns an empty list.

```python
def reset():
	return []

server.addMethod("Reset", calculator, reset, nodeId="ns=1;i=2001")
```

### Methods with typed inputs and outputs

`Add` pairs the Python callback with explicit input and output argument metadata.

```python
def add(a, b):
	return [a + b]

server.addMethod(
	"Add",
	calculator,
	add,
	inputArgs=[
		ns0.datatypes.Argument(name="A", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="First operand"),
		ns0.datatypes.Argument(name="B", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="Second operand"),
	],
	outputArgs=[
		ns0.datatypes.Argument(name="Sum", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="A + B"),
	],
	nodeId="ns=1;i=2002",
)
```


### Returning multiple values

`Divide` returns two outputs. The callback returns a list whose order matches the declared output arguments.

```python
def divide(a, b):
	if b == 0:
		return [0, 0]
	quotient = int(a // b)
	remainder = a - quotient * b
	return [quotient, remainder]
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

	calculator = server.addObject(
		"Calculator", server.objectsNode, nodeId="ns=1;i=100"
	)

	def reset():
		print("  [Method] Reset called")
		return []

	server.addMethod(
		"Reset",
		calculator,
		reset,
		nodeId="ns=1;i=2001",
	)

	def add(a, b):
		result = a + b
		print(f"  [Method] Add({a}, {b}) = {result}")
		return [result]

	server.addMethod(
		"Add",
		calculator,
		add,
		inputArgs=[
			ns0.datatypes.Argument(name="A", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="First operand"),
			ns0.datatypes.Argument(name="B", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="Second operand"),
		],
		outputArgs=[
			ns0.datatypes.Argument(name="Sum", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="A + B"),
		],
		nodeId="ns=1;i=2002",
	)

	def greet(name):
		message = f"Hello, {name}!"
		print(f"  [Method] Greet('{name}') -> '{message}'")
		return [message]

	server.addMethod(
		"Greet",
		calculator,
		greet,
		inputArgs=[
			ns0.datatypes.Argument(name="Name", dataType=o6.String, valueRank=o6.ValueRank.SCALAR, description="Name to greet"),
		],
		outputArgs=[
			ns0.datatypes.Argument(name="Greeting", dataType=o6.String, valueRank=o6.ValueRank.SCALAR, description="Greeting message"),
		],
		nodeId="ns=1;i=2003",
	)

	def divide(a, b):
		if b == 0:
			print("  [Method] Divide: division by zero!")
			return [0, 0]
		quotient = int(a // b)
		remainder = a - quotient * b
		print(f"  [Method] Divide({a}, {b}) -> q={quotient}, r={remainder}")
		return [quotient, remainder]

	server.addMethod(
		"Divide",
		calculator,
		divide,
		inputArgs=[
			ns0.datatypes.Argument(name="Dividend", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="Dividend"),
			ns0.datatypes.Argument(name="Divisor", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="Divisor"),
		],
		outputArgs=[
			ns0.datatypes.Argument(name="Quotient", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="Integer quotient"),
			ns0.datatypes.Argument(name="Remainder", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="Remainder"),
		],
		nodeId="ns=1;i=2004",
	)

	server.start()
	print("Server running at opc.tcp://localhost:4840")
	print("Methods available under Calculator (ns=1;i=100):")
	print("  - Reset      (ns=1;i=2001)  no args")
	print("  - Add        (ns=1;i=2002)  Double + Double -> Double")
	print("  - Greet      (ns=1;i=2003)  String -> String")
	print("  - Divide     (ns=1;i=2004)  Double, Double -> Double, Double")
	print("\nPress Ctrl+C to stop.\n")

	try:
		while True:
			time.sleep(1.0)
	except KeyboardInterrupt:
		print("\nShutting down…")
	finally:
		server.stop()
		print("Server stopped.")


if __name__ == "__main__":
	main()
```