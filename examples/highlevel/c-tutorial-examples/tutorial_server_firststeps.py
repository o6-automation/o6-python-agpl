#!/usr/bin/env python3
"""Python parity for open62541 tutorial_server_firststeps.

C tutorial topics:
- Server Configuration and Plugins
- Server Lifecycle
"""

import time
from o6 import LocalizedText, Server


def main() -> None:
    server = Server(port=4840)

    # Server configuration equivalent in high-level API.
    app = server.config.applicationDescription
    app.applicationName = LocalizedText("en-US", "o6 tutorial parity server")
    app.applicationUri = "urn:o6:tutorial:firststeps"
    server.config.applicationDescription = app

    print("Starting server...")
    server.start()
    server.addVariable("Temperature", server.objectsNode, 25.0)

    print("Server running at opc.tcp://localhost:4840")
    print("Press Ctrl+C to stop")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        print("Stopping server...")
        server.stop()


if __name__ == "__main__":
    main()
