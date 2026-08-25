# Observing Attributes with Local MonitoredItems

Source: `examples/highlevel/c-tutorial-examples/tutorial_server_monitoreditems.py`

The open62541 tutorial demonstrates local server-side monitored items. The
high-level Python API currently exposes client monitoring, so this page uses the
closest available workflow while keeping the same tutorial intent.

```python
import time
from o6 import Client


def on_change(value):
	print("Monitored value changed:", value)


with Client("opc.tcp://localhost:4840") as client:
	subscription = client.createSubscription(publishingInterval=500.0)
	monitored_item = client.monitor(
		"ns=1;s=IntegerVariable",
		on_change,
		subscription=subscription,
	)

	try:
		time.sleep(10)
	finally:
		monitored_item.delete()
		subscription.delete()
```
