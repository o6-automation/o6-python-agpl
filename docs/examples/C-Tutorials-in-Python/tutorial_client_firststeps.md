# Building a Simple Client

Source: `examples/highlevel/c-tutorial-examples/tutorial_client_firststeps.py`

## Read the Current Time

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
	current_time = client.read("i=2258")
	print(current_time)
```

## Further Tasks

```python
from o6 import Client

with Client("opc.tcp://localhost:4840") as client:
	answer = client.read("ns=1;s=TheAnswer")
	print("The Answer:", answer)
```
