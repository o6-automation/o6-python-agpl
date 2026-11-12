# Methods

Exposes methods on the server that OPC UA clients can call.

Topics covered:

- Simple method with no arguments
- Method with input and output arguments
- Method with multiple inputs/outputs
- Organizing methods under objects
- Error handling in method callbacks

Connect with any OPC UA client at: `opc.tcp://localhost:4840`

## 1. Method with no arguments
A method without arguments triggers an action, such as a system reset.
A method without outputs still returns a one-item tuple with the
status code.

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
Each method argument is an `ns0.datatypes.Argument` struct with a name,
an OPC UA data type (for example `o6.Double`) and a description. Each
input is one `Argument` entry in `inputArgs`.

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
This method takes and returns an OPC UA `String` (`o6.String`).

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
List each output as its own `Argument` in `outputArgs`. `Divide`
returns a quotient and a remainder.

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
