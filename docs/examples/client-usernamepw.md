# Client Username and Password Example

Source example: `examples/highlevel/client_usernamepw.py`

This example connects with explicit username and password credentials.

## Explanation

### Passing credentials to `Client`

The credentials are passed when constructing the client.

```python
client = Client(endpoint_url, username=USERNAME, password=PASSWORD)
client.connect()
```

## Full source

```python
import socket
from o6 import Client, StatusCodeError

localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"

USERNAME = "user1"
PASSWORD = "password"


def main():
    print("=== OPC UA Username/Password Authentication Example ===\n")

    client = Client()
    try:
        client.connect(endpoint_url, username=USERNAME, password=PASSWORD)
    except Exception as e:
        print(f"Failed to connect to {endpoint_url} with username '{USERNAME}': {e}")
        return

    print(f"Connected to {endpoint_url} as '{USERNAME}'")

    try:
        try:
            value = client.read("ns=1;s=IntegerVariable")
            print(f"Read value: {value}")
        except StatusCodeError as e:
            print(f"Read failed (node may not exist on this server): {e}")
    finally:
        client.disconnect()
        print("Disconnected.")


if __name__ == "__main__":
    main()
```