# Local Discovery Server with mDNS

## Local Discovery Server

Three programs demonstrate registering an OPC UA application with an LDS,
discovering it, and reading a value. Download `server.py`, `registered_server.py`,
and `client.py` from the Source Code section into one folder on your machine.
Install the SDK in your Python environment:

```sh
python -m pip install o6
```

Run the commands below from that folder, using the same Python environment in
each terminal.

### Without mDNS

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

### With mDNS

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

### Stop

Press Ctrl+C in the application terminal first. It unregisters before stopping.
Run the client again to see `No application found.`, then stop the LDS with
Ctrl+C. A crash does not send an unregistration.

The LDS uses port 4840 and the application uses port 4841. Registration uses
SignAndEncrypt with self-signed certificates that both sides accept without
checking. Discovery and reading use SecurityPolicy None.


## server.py

Run a Local Discovery Server, optionally announcing registrations through mDNS.

### Start the LDS
An LDS accepts application registrations. Enable mDNS to also announce
registered applications and expose them through `FindServersOnNetwork`.
Registrations need an encrypted channel, so the LDS gets a certificate.
Use a `trustList` instead of `acceptAllCertificates` in production.

```python
def main(mdns=False):
    key, certificate = createSelfSignedCertificate(appUri="urn:o6:lds")
    server = o6.Server(
        port=PORT,
        applicationUri="urn:o6:lds",
        certificate=certificate,
        privateKey=key,
        acceptAllCertificates=True,
    )
    server.config.applicationType = ApplicationType.DISCOVERY_SERVER
    if mdns:
        server.setMdns(MdnsConfig(announceRegisteredServers=True))

    with server:
        print(f"LDS ready at opc.tcp://localhost:{PORT}", flush=True)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
    print("LDS stopped", flush=True)
```

## registered_server.py

Publish a value and register this application with the local LDS.

### Register an application
Start the application before registering its discovery URL. Renew the
registration every 30 seconds and unregister when Ctrl+C is pressed.
The client certificate must carry the registered application URI.

```python
def main():
    url = f"opc.tcp://localhost:{PORT}"
    server = o6.Server(port=PORT, applicationUri=APPLICATION_URI)
    server.addVariable(
        "LdsDemoValue",
        server.objectsNode,
        "Hello from the registered LDS application",
        nodeId="ns=1;s=LdsDemoValue",
    )
    key, certificate = createSelfSignedCertificate(appUri=APPLICATION_URI)
    lds = o6.Client(
        LDS_URL,
        certificate=certificate,
        privateKey=key,
        applicationUri=APPLICATION_URI,
        acceptAllCertificates=True,
        securityMode=o6.SecurityMode.SIGN_AND_ENCRYPT,
        securityPolicy=o6.SecurityPolicy.BASIC256SHA256,
    )
    try:
        lds.connect(noSession=True)
        with server:
            print(f"Application ready at {url}", flush=True)
            try:
                while True:
                    lds.registerServer(
                        APPLICATION_URI,
                        [url],
                        serverName=APPLICATION_NAME,
                        mdnsServerName=APPLICATION_NAME,
                        serverCapabilities=["DA"],
                    )
                    print("Registration confirmed", flush=True)
                    time.sleep(30)
            except KeyboardInterrupt:
                pass
            finally:
                lds.unregisterServer(APPLICATION_URI, [url])
                print("Unregistration confirmed", flush=True)
        print("Application stopped", flush=True)
    finally:
        lds.disconnect()
```

## client.py

Discover the registered application through the LDS and read its value.

### Discover and read
Use `FindServers` for explicit registrations, or `FindServersOnNetwork`
for mDNS records with the Data Access capability. Connect using the URL
returned by discovery.

```python
def main(mdns=False):
    url = None
    lds = o6.Client(LDS_URL)
    try:
        lds.connect(noSession=True)
        if mdns:
            for record in lds.findServersOnNetwork(serverCapabilityFilter=["DA"]):
                print(
                    f"Network: {record.serverName} {record.discoveryUrl} {list(record.serverCapabilities)}"
                )
                if record.serverName == APPLICATION_NAME:
                    url = record.discoveryUrl
        else:
            for application in lds.findServers(LDS_URL):
                print(f"Registered: {application.applicationUri} {list(application.discoveryUrls)}")
                if application.applicationUri == "urn:o6:lds:application":
                    url = application.discoveryUrls[0]
    finally:
        lds.disconnect()

    if url is None:
        print("No application found.")
        return
    with o6.Client(url) as client:
        print(f"Read: {client.read('ns=1;s=LdsDemoValue')}")
```

## Source Code

Download these files into the same folder to run the example:

- <a href="/o6-python/examples/advanced_applications-lds-server/README.md" download="README.md"><code>README.md</code></a>
- [`server.py`](advanced_applications-lds-server/server.py)
- [`registered_server.py`](advanced_applications-lds-server/registered_server.py)
- [`client.py`](advanced_applications-lds-server/client.py)
