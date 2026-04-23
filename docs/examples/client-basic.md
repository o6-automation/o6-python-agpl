# High-Level Client Example

Source example: `examples/highlevel/client_basic.py`

This example is the best starting point if you want to understand the high-level client API in one file. It combines several common client workflows in a single script and shows how the Python API is intended to be used in normal application code.

## Explanation

### Basic read and write

The first part connects to a server and uses `client.read(...)` and `client.write(...)` for standard value access. This is the most direct high-level interface for client applications.

```python
with Client(endpoint_url) as client:
	value = client.read("ns=1;s=IntegerVariable")
	client.write("ns=1;s=IntegerVariable", types.UInt32(42))
	new_value = client.read("ns=1;s=IntegerVariable")
```

### Multiple operations


```python
values = client.read([
	"ns=1;s=IntegerVariable",
	"ns=1;s=DoubleVariable",
])

client.write({
	"ns=1;s=IntegerVariable": types.UInt32(100),
	"ns=1;s=DoubleVariable": types.Double(2.7182),
})
```

### Method calls


```python
result = client.call(
	"ns=1;s=TestMethods",
	"ns=1;s=MethodHelloString",
	["World"],
)
```

### Subscriptions


```python
subscription = client.create_subscription(publishing_interval=1000)
monitored_item = subscription.monitor_data_change(
	"ns=1;s=IntegerVariable", on_data_change, sampling_interval=500
)
```

### Node-oriented access


```python
node = client["ns=0;i=85"]
print(node)
print(node.nodeclass)
```

## Full source

```python
from o6 import Client, StatusCodeError, types
import time
import socket

localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"


def main():
	print("=== High-Level O6 Client Example ===\n")

	print("1. Basic Read/Write Operations")
	print("-" * 40)

	try:
		with Client(endpoint_url) as client:
			print(f"Connected to server successfully!")

			try:
				value = client.read("ns=1;s=IntegerVariable")
				print(f"Read value: {value}")
			except StatusCodeError as e:
				print(f"Read failed: {e}")

			try:
				client.write("ns=1;s=IntegerVariable", types.UInt32(42))
				print("Write successful!")
				new_value = client.read("ns=1;s=IntegerVariable")
				print(f"Verified value: {new_value}")
			except StatusCodeError as e:
				print(f"Write failed: {e}")

			print("\n2. Multiple Operations")
			print("-" * 40)

			try:
				values = client.read(
					["ns=1;s=IntegerVariable", "ns=1;s=DoubleVariable"]
				)
				print(f"Multiple read results: {values}")
			except StatusCodeError as e:
				print(f"Multiple read failed: {e}")

			try:
				client.write(
					{
						"ns=1;s=IntegerVariable": types.UInt32(100),
						"ns=1;s=DoubleVariable": types.Double(2.7182),
					}
				)
				print("Multiple write successful!")
			except StatusCodeError as e:
				print(f"Multiple write failed: {e}")

			print("\n3. Method Call")
			print("-" * 40)

			try:
				result = client.call(
					"ns=1;s=TestMethods", "ns=1;s=MethodHelloString", ["World"]
				)
				print(f"Method call result: {result}")
			except Exception as e:
				print(f"Method call failed: {e}")

		print("\nDisconnected successfully!")

	except StatusCodeError as e:
		print(f"Connection failed: {e}")
		print("Note: Make sure an OPC UA server is running on localhost:4840")
	except Exception as e:
		print(f"Unexpected error: {e}")

	print("\n\n4. Subscription Example")
	print("-" * 40)

	def on_data_change(value):
		print(f"Data changed: {value}")

	try:
		with Client(endpoint_url) as client:
			print("Creating subscription...")

			subscription = client.create_subscription(publishing_interval=1000)

			monitored_item = subscription.monitor_data_change(
				"ns=1;s=IntegerVariable", on_data_change, sampling_interval=500
			)

			print("Monitoring started. Writing values to trigger notifications...")

			for i in range(5):
				client.write("ns=1;s=IntegerVariable", types.UInt32(200 + i))
				time.sleep(1)

			print("Cleaning up subscription...")
			monitored_item.delete()
			subscription.delete()

	except StatusCodeError as e:
		print(f"Connection failed: {e}")
		print("Note: Make sure an OPC UA server is running on localhost:4840")
	except Exception as e:
		print(f"Subscription error: {e}")

	print("\n\n4. Subscription Example")
	print("-" * 40)

	with Client(endpoint_url) as client:
		node = client["ns=0;i=85"]
		print(node)
		print(node.nodeclass)

	print("\n=== Example completed ===")


if __name__ == "__main__":
	main()
```