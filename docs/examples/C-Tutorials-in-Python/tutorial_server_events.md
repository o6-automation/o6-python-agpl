# Generating Events

Source: `examples/highlevel/c-tutorial-examples/tutorial_server_events.py`

The open62541 tutorial emits events from the server. The high-level Python API
in this repository does not yet expose server-side event creation helpers, so
this page demonstrates the matching client-side event monitoring workflow.

```python
import time
from o6 import Client


def on_event(event):
	print("Event:", event)


with Client("opc.tcp://localhost:4840") as client:
	listener = client.monitorEvent("i=2253", on_event)

	try:
		time.sleep(10)
	finally:
		listener.delete()
```
