from o6 import Client, StatusCodeError, types
import time
import socket

localhost = socket.gethostname()
endpoint_url = f"opc.tcp://{localhost}:4840"


# --- OPC UA Client Example ---
# Read and write a variable on the OPC UA server.
# The nodeid of the variable must match the one defined in the server.
# The value that is being  written needs to be one of the o6 types.

try:
    with Client(endpoint_url) as client:
        print(f"Connected to server successfully!")
        value = client.read("ns=1;s=PumpLIOpen")
        print(f"Initial value of left inflow pump: {value}")
        # open
        client.write("ns=1;s=PumpLIOpen", types.Double(0.5))
        value = client.read("ns=1;s=PumpLIOpen")
        print(f"Value of left inflow pump after opening: {value}")
        # wait a bit
        # time.sleep(5)
        # close
        client.write("ns=1;s=PumpLIOpen", types.Double(0.0))  #

        # This is the main outer object of the OPC UA server, which contains all other nodes.
        # It is always present and has the nodeid "ns=0;i=85"
        for item in client.browse("ns=0;i=85"):
            print(item)

        print(
            client.read(
                [
                    "ns=1;s=PumpLOOpen",
                    "ns=1;s=PumpRIOpen",
                    "ns=1;s=PumpROOpen",
                    "ns=1;s=PumpCOpen",
                ]
            )
        )

except StatusCodeError as e:
    print(f"Connection failed: {e}")
    print("Note: Make sure an OPC UA server is running on localhost:4840")
except Exception as e:
    print(f"Unexpected error: {e}")


## Subscription example

try:
    with Client(endpoint_url) as client:

        print("end")

except StatusCodeError as e:
    print(f"Connection failed: {e}")
    print("Note: Make sure an OPC UA server is running on localhost:4840")
except Exception as e:
    print(f"Unexpected error: {e}")
