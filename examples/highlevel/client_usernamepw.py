"""
Username/Password Authentication Example

Demonstrates connecting to an OPC UA server using username and password
credentials via the o6 high-level client API.
"""

import socket
from o6 import Client, StatusCodeError

localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"

USERNAME = "user1"
PASSWORD = "password"


def main():
    print("=== OPC UA Username/Password Authentication Example ===\n")

    client = Client(endpoint_url, username=USERNAME, password=PASSWORD)
    try:
        client.connect()
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
