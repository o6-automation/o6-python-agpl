# Minimal Server Example

Source example: `examples/highlevel/server_minimal.py`

This is the smallest server example in the repository.

## Explanation

### Starting the server

```python
server = Server(port=4840)
server.start()
```

## Full source

```python
#!/usr/bin/env python3

from o6 import Server

server = Server(port=4840)
server.start()

print("Server running – press Ctrl+C to stop")

try:
    while True:
        import time

        time.sleep(1)
except KeyboardInterrupt:
    pass

server.stop()
```