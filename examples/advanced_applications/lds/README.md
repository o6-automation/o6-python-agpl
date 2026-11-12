# Local Discovery Server

Three programs demonstrate registering an OPC UA application with an LDS,
discovering it, and reading a value. Download `server.py`, `registered_server.py`,
and `client.py` from the Source Code section into one folder on your machine.
Install the SDK in your Python environment:

```sh
python -m pip install o6
```

Run the commands below from that folder, using the same Python environment in
each terminal.

## Without mDNS

Start the LDS in one terminal:

```sh
python server.py
```

Start the application in another:

```sh
python registered_server.py
```

After `Registration confirmed`, run the client:

```sh
python client.py
```

The client uses `FindServers` to discover the application, connects to its
returned URL, and prints:

```text
Read: Hello from the registered LDS application
```

## With mDNS

Stop the application and LDS with Ctrl+C. Restart them in separate terminals,
enabling mDNS on the LDS:

```sh
python server.py --mdns
python registered_server.py
```

After registration, run the client:

```sh
python client.py --mdns
```

The LDS announces the registration through mDNS. The client uses
`FindServersOnNetwork` with the `DA` (Data Access) capability filter and reads
the same value. This local example queries the announcing LDS's own records.
The regular client command still works while mDNS is enabled.

The mDNS mode requires a Linux SDK build with mDNS support. Check availability:

```sh
python -c 'from o6.discovery import mdnsAvailable; print(mdnsAvailable)'
```

Enabling mDNS on an unsupported build raises `NotImplementedError`.

## Stop

Press Ctrl+C in the application terminal first. It unregisters before stopping.
Run the client again to see `No application found.`, then stop the LDS with
Ctrl+C. A crash does not send an unregistration.

The LDS uses port 4840 and the application uses port 4841. Registration uses
SignAndEncrypt with self-signed certificates that both sides accept without
checking. Discovery and reading use SecurityPolicy None.
