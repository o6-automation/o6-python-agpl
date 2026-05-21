# High-Level O6 Python Library

This directory contains the high-level, pythonic interface for the O6 OPC UA library.

## Overview

The high-level `o6` module provides a user-friendly Python API that wraps the low-level `_o6` C extension module. It follows Python best practices and provides:

- Pythonic interfaces with context managers
- Automatic error handling with custom exceptions
- Type helpers for common OPC UA types
- Simplified client operations
- Subscription management with callbacks

## Structure

```
o6/
├── __init__.py          # Main package exports
├── client.py           # High-level Client class
├── types.py            # Type helpers and utilities  
├── exceptions.py       # Custom exception classes
├── utils.py            # Utility functions
└── README.md          # This file
```

## Basic Usage

### Simple Client Operations

```python
from o6 import Client

# Context manager automatically handles connection/disconnection
with Client("opc.tcp://localhost:4840") as client:
    # Read a value
    temperature = client.read("ns=1;s=Temperature")
    print(f"Temperature: {temperature}")
    
    # Write a value
    client.write("ns=1;s=SetPoint", 25.0)
    
    # Read multiple values
    values = client.read_multiple([
        "ns=1;s=Temperature",
        "ns=1;s=Pressure"
    ])
    
    # Write multiple values
    client.write_multiple([
        ("ns=1;s=SetPoint", 25.0),
        ("ns=1;s=Mode", "Auto")
    ])
```

### Subscriptions

```python
from o6 import Client

def on_temperature_change(value):
    print(f"Temperature changed to: {value}")

with Client("opc.tcp://localhost:4840") as client:
    # Create subscription
    subscription = client.create_subscription(publishing_interval=1000)
    
    # Monitor for data changes
    monitored_item = subscription.monitor_data_change(
        "ns=1;s=Temperature",
        on_temperature_change
    )
    
    # Let it run for a while...
    time.sleep(30)
    
    # Cleanup (automatic with context manager)
    monitored_item.delete()
    subscription.delete()
```

### Error Handling

```python
from o6 import Client
from o6.exceptions import ConnectionError, ReadError, WriteError

try:
    with Client("opc.tcp://localhost:4840") as client:
        value = client.read("ns=1;s=NonExistentNode")
except ConnectionError:
    print("Could not connect to server")
except ReadError as e:
    print(f"Read failed: {e}")
    if e.status_code:
        print(f"Status code: 0x{e.status_code:08x}")
```

## Design Principles

1. **Pythonic**: Follows Python conventions and idioms
2. **Context Managers**: Automatic resource management
3. **Type Safety**: Helper functions for type creation
4. **Error Handling**: Meaningful exceptions instead of status codes
5. **Documentation**: Comprehensive docstrings and examples
6. **Extensible**: Easy to add new functionality

## Implementation Details

- **Client Class**: Wraps `_o6.Client` with high-level methods
- **Subscription Management**: Automatic thread management for callbacks
- **Type System**: Convenient wrappers around `_o6.types`
- **Exception Hierarchy**: Structured error handling
- **Utilities**: Helper functions for common operations

## Future Enhancements

- [ ] Browse operations
- [ ] Server implementation
- [ ] Security configuration
- [ ] Advanced subscription filtering
- [ ] Batch operations
- [ ] Async/await support
- [ ] Configuration management
- [ ] Logging integration
