Server Tutorial: Adding Methods
===============================

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
Methods with no arguments are adapted if you just need to trigger a simple action (like a system reset).
Methods without outputs return a one-item tuple containing the status.

```python
def reset(node):
    """Reset the server-side counter."""
    print("  [Method] Reset called")
    return (o6.StatusCode.GOOD,)

server.addMethod(
    name="Reset",
    parent=calculator,
    callback=reset,
    nodeId="ns=1;i=2001",
)
```

## 2. Method with multiple inputs
Method arguments are described directly with `ns0.datatypes.Argument` structures.
to an OPC UA Data Type (e.g. "i=11" for a `Double` type), and a description.
Multiple inputs are listed as multiple `ns0.datatypes.Argument` structures.

```python
def add(node, a, b):
    """Add two doubles."""
    result = a + b
    print(f"  [Method] Add({a}, {b}) = {result}")
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
OPC UA supports various data types. Here we use 'i=12' to handle Strings,
demonstrating that methods aren't limited to numerical calculations.

```python
def greet(node, name):
    """Return a greeting string."""
    message = f"Hello, {name}!"
    print(f"  [Method] Greet('{name}') -> '{message}'")
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
Multiple outputs are listed as multiple `ns0.datatypes.Argument` structures.

```python
def divide(node, a, b):
    """Integer division returning quotient and remainder."""
    if b == 0:
        print("  [Method] Divide: division by zero!")
        return (o6.StatusCode.BAD_INVALID_ARGUMENT,)
    quotient = int(a // b)
    remainder = a - quotient * b
    print(f"  [Method] Divide({a}, {b}) -> q={quotient}, r={remainder}")
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

## Complete Source Code

```python
#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH (Author: Andreas Ebner)
"""
Server Tutorial: Adding Methods
===============================

Demonstrates how to expose callable methods on the server that
OPC UA clients can invoke remotely.

Topics covered:

- Simple method with no arguments
- Method with input and output arguments
- Method with multiple inputs/outputs
- Organising methods under objects
- Error handling in method callbacks

Connect with any OPC UA client at: `opc.tcp://localhost:4840`
"""

import time
import o6
from o6 import Server
from o6.ns import ns0


def main():
    server = Server(port=4840)

    # ── Organise under an object ─────────────────────────────────
    calculator = server.addObject("Calculator", server.objectsNode, nodeId="ns=1;i=100")

    # ── 1. Method with no arguments / no output ──────────────────

    def reset(node):
        """Reset the server-side counter."""
        print("  [Method] Reset called")
        return (o6.StatusCode.GOOD,)

    server.addMethod(
        name="Reset",
        parent=calculator,
        callback=reset,
        nodeId="ns=1;i=2001",
    )

    # ── 2. Simple add: two inputs, one output ────────────────────

    def add(node, a, b):
        """Add two doubles."""
        result = a + b
        print(f"  [Method] Add({a}, {b}) = {result}")
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

    # ── 3. String method ─────────────────────────────────────────

    def greet(node, name):
        """Return a greeting string."""
        message = f"Hello, {name}!"
        print(f"  [Method] Greet('{name}') -> '{message}'")
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

    # ── 4. Multiple outputs ──────────────────────────────────────

    def divide(node, a, b):
        """Integer division returning quotient and remainder."""
        if b == 0:
            print("  [Method] Divide: division by zero!")
            return (o6.StatusCode.BAD_INVALID_ARGUMENT,)
        quotient = int(a // b)
        remainder = a - quotient * b
        print(f"  [Method] Divide({a}, {b}) -> q={quotient}, r={remainder}")
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

    # ── Start ────────────────────────────────────────────────────
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
