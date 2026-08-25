import subprocess
import os
import time
import pytest
from o6 import Client

SERVERS = [
    {
        "name": "lads-balance",
        "cwd": "../lads-server-collection",
        "start": ["npm", "run", "lads-balance"],
        "endpoint": "opc.tcp://localhost:4844",
    },
    {
        "name": "lads-ph-meter",
        "cwd": "../lads-server-collection",
        "start": ["npm", "run", "lads-ph-meter"],
        "endpoint": "opc.tcp://localhost:4841",
    },
    {
        "name": "lads-viscometer",
        "cwd": "../lads-server-collection",
        "start": ["npm", "run", "lads-viscometer"],
        "endpoint": "opc.tcp://localhost:4840",
    },
    {
        "name": "lads-freezer",
        "cwd": "../lads-server-collection",
        "start": ["npm", "run", "lads-freezer"],
        "endpoint": "opc.tcp://localhost:4842",
    },
]


def wait_for_opcua(endpoint: str, timeout: int = 60):
    """Poll until the OPC UA server accepts a real o6 Client connection."""
    deadline = time.time() + timeout
    last_err = None
    while time.time() < deadline:
        try:
            c = Client(endpoint)
            c.connect()
            c.disconnect()
            return  # success
        except Exception as e:
            last_err = e
            time.sleep(0.5)
    raise RuntimeError(
        f"OPC UA server at {endpoint} not ready after {timeout}s. " f"Last error: {last_err}"
    )


def start_server(server):

    port = int(server["endpoint"].split(":")[-1])

    # Kill anything already holding the port
    try:
        import psutil

        for p in psutil.process_iter(["pid", "connections"]):
            for c in p.info.get("connections") or []:
                if c.laddr and c.laddr.port == port:
                    p.kill()
    except Exception:
        pass

    cwd = os.path.abspath(os.path.join(os.path.dirname(__file__), server["cwd"]))
    result = subprocess.run(["which", "npm"], capture_output=True, text=True)
    print(result.stdout)
    proc = subprocess.Popen(
        server["start"],
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )

    try:
        wait_for_opcua(server["endpoint"])
    except RuntimeError:
        proc.terminate()
        proc.wait()
        raise

    return proc


@pytest.fixture(scope="session")
def balance_server():
    proc = start_server(SERVERS[0])
    yield SERVERS[0]
    proc.terminate()
    proc.wait()


@pytest.fixture(scope="session")
def ph_meter_server():
    proc = start_server(SERVERS[1])
    yield SERVERS[1]
    proc.terminate()
    proc.wait()


@pytest.fixture(scope="session")
def viscometer_server():
    proc = start_server(SERVERS[2])
    yield SERVERS[2]
    proc.terminate()
    proc.wait()


@pytest.fixture(scope="session")
def freezer_server():
    proc = start_server(SERVERS[3])
    yield SERVERS[3]
    proc.terminate()
    proc.wait()
