# Server Methods Example

Source example: `examples/highlevel/server_methods.py`

This example concentrates on server-side methods. It shows how to group several callbacks under one object and how different OPC UA method signatures are declared in Python.

## Explanation

### Organizing methods below an object


```python
calculator = server.add_object(
	"Calculator", server.objects_node, nodeid="ns=1;i=100"
)
```


### A method without arguments

`Reset` is the smallest possible method example. The callback takes no parameters and returns an empty list.

```python
def reset():
	return []

server.add_method("Reset", calculator, reset, nodeid="ns=1;i=2001")
```

### Methods with typed inputs and outputs

`Add` pairs the Python callback with explicit input and output argument metadata.

```python
def add(a, b):
	return [a + b]

server.add_method(
	"Add",
	calculator,
	add,
	input_args=[
		make_argument("A", "i=11", description="First operand"),
		make_argument("B", "i=11", description="Second operand"),
	],
	output_args=[
		make_argument("Sum", "i=11", description="A + B"),
	],
	nodeid="ns=1;i=2002",
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
from o6 import Server
from o6.server import make_argument


def main():
	server = Server(port=4840)

	calculator = server.add_object(
		"Calculator", server.objects_node, nodeid="ns=1;i=100"
	)

	def reset():
		print("  [Method] Reset called")
		return []

	server.add_method(
		"Reset",
		calculator,
		reset,
		nodeid="ns=1;i=2001",
	)

	def add(a, b):
		result = a + b
		print(f"  [Method] Add({a}, {b}) = {result}")
		return [result]

	server.add_method(
		"Add",
		calculator,
		add,
		input_args=[
			make_argument("A", "i=11", description="First operand"),
			make_argument("B", "i=11", description="Second operand"),
		],
		output_args=[
			make_argument("Sum", "i=11", description="A + B"),
		],
		nodeid="ns=1;i=2002",
	)

	def greet(name):
		message = f"Hello, {name}!"
		print(f"  [Method] Greet('{name}') -> '{message}'")
		return [message]

	server.add_method(
		"Greet",
		calculator,
		greet,
		input_args=[
			make_argument("Name", "i=12", description="Name to greet"),
		],
		output_args=[
			make_argument("Greeting", "i=12", description="Greeting message"),
		],
		nodeid="ns=1;i=2003",
	)

	def divide(a, b):
		if b == 0:
			print("  [Method] Divide: division by zero!")
			return [0, 0]
		quotient = int(a // b)
		remainder = a - quotient * b
		print(f"  [Method] Divide({a}, {b}) -> q={quotient}, r={remainder}")
		return [quotient, remainder]

	server.add_method(
		"Divide",
		calculator,
		divide,
		input_args=[
			make_argument("Dividend", "i=11", description="Dividend"),
			make_argument("Divisor", "i=11", description="Divisor"),
		],
		output_args=[
			make_argument("Quotient", "i=11", description="Integer quotient"),
			make_argument("Remainder", "i=11", description="Remainder"),
		],
		nodeid="ns=1;i=2004",
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