# Methods

Demonstrates how to expose callable methods on the server that
OPC UA clients can invoke remotely.

Topics covered:

- Simple method with no arguments
- Method with input and output arguments
- Method with multiple inputs/outputs
- Organising methods under objects
- Error handling in method callbacks

Connect with any OPC UA client at: `opc.tcp://localhost:4840`

## 1. Method with no arguments
Methods with no arguments are useful for triggering a simple action,
like a system reset. A method with no outputs still returns a
one-item tuple containing just the status code.

```python
print("--- 1. Method with no arguments ---")

def reset(node):
    """Reset the server-side counter."""
    print("Reset called")
    return (o6.StatusCode.GOOD,)

server.addMethod(
    name="Reset",
    parent=calculator,
    callback=reset,
    nodeId="ns=1;i=2001",
)
```

## 2. Method with multiple inputs
Each method argument is described with an `ns0.datatypes.Argument`
structure: a name, an OPC UA data type (e.g. `o6.Double`), and a
description. Multiple inputs are simply multiple `Argument` entries
in `inputArgs`.

```python
print("\n--- 2. Method with multiple inputs ---")

def add(node, a, b):
    """Add two doubles."""
    result = a + b
    print(f"Add({a}, {b}) = {result}")
    return (o6.StatusCode.GOOD, result)

server.addMethod(
    name="Add",
    parent=calculator,
    callback=add,
    inputArgs=[
        ns0.datatypes.Argument(
            name="A",
            dataType=o6.Double,
            valueRank=o6.ValueRank.SCALAR,
            description="First operand",
        ),
        ns0.datatypes.Argument(
            name="B",
            dataType=o6.Double,
            valueRank=o6.ValueRank.SCALAR,
            description="Second operand",
        ),
    ],
    outputArgs=[
        ns0.datatypes.Argument(
            name="Sum", dataType=o6.Double, valueRank=o6.ValueRank.SCALAR, description="A + B"
        ),
    ],
    nodeId="ns=1;i=2002",
)
```

## 3. String Method
Method arguments aren't limited to numbers — this method takes and
returns an OPC UA `String` (`o6.String`).

```python
print("\n--- 3. String Method ---")

def greet(node, name):
    """Return a greeting string."""
    message = f"Hello, {name}!"
    print(f"Greet('{name}') -> '{message}'")
    return (o6.StatusCode.GOOD, message)

server.addMethod(
    "Greet",
    calculator,
    greet,
    inputArgs=[
        ns0.datatypes.Argument(
            name="Name",
            dataType=o6.String,
            valueRank=o6.ValueRank.SCALAR,
            description="Name to greet",
        ),
    ],
    outputArgs=[
        ns0.datatypes.Argument(
            name="Greeting",
            dataType=o6.String,
            valueRank=o6.ValueRank.SCALAR,
            description="Greeting message",
        ),
    ],
    nodeId="ns=1;i=2003",
)
```

## 4. Method with multiple outputs
Multiple outputs work the same way as multiple inputs: list each one
as its own `Argument` in `outputArgs`. `Divide` returns both a
quotient and a remainder.

```python
print("\n--- 4. Method with multiple outputs ---")

def divide(node, a, b):
    """Integer division returning quotient and remainder."""
    if b == 0:
        print("Divide: division by zero")
        return (o6.StatusCode.BAD_INVALID_ARGUMENT,)
    quotient = int(a // b)
    remainder = a - quotient * b
    print(f"Divide({a}, {b}) -> quotient={quotient}, remainder={remainder}")
    return (o6.StatusCode.GOOD, quotient, remainder)

server.addMethod(
    "Divide",
    calculator,
    divide,
    inputArgs=[
        ns0.datatypes.Argument(
            name="Dividend",
            dataType=o6.Double,
            valueRank=o6.ValueRank.SCALAR,
            description="Dividend",
        ),
        ns0.datatypes.Argument(
            name="Divisor",
            dataType=o6.Double,
            valueRank=o6.ValueRank.SCALAR,
            description="Divisor",
        ),
    ],
    outputArgs=[
        ns0.datatypes.Argument(
            name="Quotient",
            dataType=o6.Double,
            valueRank=o6.ValueRank.SCALAR,
            description="Integer quotient",
        ),
        ns0.datatypes.Argument(
            name="Remainder",
            dataType=o6.Double,
            valueRank=o6.ValueRank.SCALAR,
            description="Remainder",
        ),
    ],
    nodeId="ns=1;i=2004",
)
```

## Source Code

Download [`S06_methods.py`](server-S06_methods/S06_methods.py) to run it locally.
