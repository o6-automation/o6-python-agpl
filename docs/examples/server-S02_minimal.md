# Minimal

The smallest possible server – just 6 lines of code.
Starts an OPC UA server on port 4840 and runs until Ctrl+C.

    opc.tcp://localhost:4840

This is the absolute baseline of an OPC UA Server.
Just by calling `server.start()`, this script provides a fully compliant OPC UA endpoint.

```python
import os

import time
from o6 import Server

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))

server = Server(port=EXAMPLE_PORT)
server.start()

print(f"Server running at opc.tcp://localhost:{EXAMPLE_PORT}")
print("Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutting down...")

server.stop()
print("Server stopped.")
```

## Source Code

Download [`S02_minimal.py`](server-S02_minimal/S02_minimal.py) to run it locally.
