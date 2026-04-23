"""
High-level O6 Client Example

This example demonstrates the high-level pythonic interface of the o6 library.
"""

from o6 import Client, StatusCodeError, types
import time
import socket

localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"


def main():
    """Main example function."""
    print("=== High-Level O6 Client Example ===\n")

    # Example 1: Basic usage with context manager
    print("1. Basic Read/Write Operations")
    print("-" * 40)

    try:
        with Client(endpoint_url) as client:
            print(f"Connected to server successfully!")

            # Read a value
            try:
                value = client.read("ns=1;s=IntegerVariable")
                print(f"Read value: {value}")
            except StatusCodeError as e:
                print(f"Read failed: {e}")

            # Write a value
            try:
                client.write("ns=1;s=IntegerVariable", types.UInt32(42))
                print("Write successful!")

                # Read back to verify
                new_value = client.read("ns=1;s=IntegerVariable")
                print(f"Verified value: {new_value}")
            except StatusCodeError as e:
                print(f"Write failed: {e}")

            # Multiple read/write operations
            print("\n2. Multiple Operations")
            print("-" * 40)

            # Read multiple values at once
            try:
                values = client.read(
                    ["ns=1;s=IntegerVariable", "ns=1;s=DoubleVariable"]
                )
                print(f"Multiple read results: {values}")
            except StatusCodeError as e:
                print(f"Multiple read failed: {e}")

            # Write multiple values at once
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

            # Method call example
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

            # Create subscription
            subscription = client.create_subscription(publishing_interval=1000)

            # Monitor a node for changes
            monitored_item = subscription.monitor(
                "ns=1;s=IntegerVariable", on_data_change, sampling_interval=500
            )

            print("Monitoring started. Writing values to trigger notifications...")

            # Write some values to trigger notifications
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
        print(node)  # Browse the Objects folder
        print(node.nodeclass)

    print("\n=== Example completed ===")


if __name__ == "__main__":
    main()
