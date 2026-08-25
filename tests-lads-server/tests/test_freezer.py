from o6 import Client, types
import time
import numpy as np

FREEZER_STATE_CURRENT = "ns=61;i=6047"
FREEZER_TEMP_TARGET = "ns=61;i=6057"
FREEZER_TEMP_SENSOR = "ns=61;i=6060"
FREEZER_ALARM_RETAIN = "ns=61;i=6094"


def test_freezer_connectivity(freezer_server):
    c = Client(freezer_server["endpoint"])
    c.connect()
    assert c.connected
    c.disconnect()


def test_freezer_alarm_state(freezer_server):
    c = Client(freezer_server["endpoint"])
    c.connect()
    retain = c.read(FREEZER_ALARM_RETAIN)
    assert isinstance(retain, bool)
    c.disconnect()


def test_freezer_startup_state(freezer_server):
    c = Client(freezer_server["endpoint"])
    c.connect()
    state = c.read(FREEZER_STATE_CURRENT)
    assert "running" in str(state).lower()
    c.disconnect()


def test_freezer_cooling_cycle(freezer_server):
    c = Client(freezer_server["endpoint"])
    c.connect()
    start_temp = c.read(FREEZER_TEMP_SENSOR)
    c.write(FREEZER_TEMP_TARGET, float(start_temp) - 10.0)

    samples = [start_temp]
    for _ in range(8):
        time.sleep(0.5)
        samples.append(c.read(FREEZER_TEMP_SENSOR))

    assert min(samples[1:]) < samples[0]
    c.disconnect()


def test_endpoints(freezer_server):
    c = Client(freezer_server["endpoint"])
    c.connect()
    endpoints = c.get_endpoints(freezer_server["endpoint"])
    assert isinstance(endpoints, list)
    assert len(endpoints) > 0
    for ep in endpoints:
        assert isinstance(ep, types.EndpointDescription)
        assert ep.endpoint_url
    c.disconnect()


def test_find_server(freezer_server):
    c = Client(freezer_server["endpoint"])
    c.connect()
    print(f"Testing find_servers with endpoint {freezer_server['endpoint']}")
    servers = c.find_servers(freezer_server["endpoint"])
    assert isinstance(servers, list)
    assert len(servers) > 0
    for srv in servers:
        assert isinstance(srv, types.ApplicationDescription)
    c.disconnect()


def test_subscriptions(freezer_server):
    c = Client(freezer_server["endpoint"])
    c.connect()
    sub = c.create_subscription()
    assert sub is not None
    assert isinstance(sub.id, (int, np.integer))
    assert sub.id > 0
    sub.delete()

    c.disconnect()


def test_config_options(freezer_server):
    c = Client()
    c.config.timeout = 30000
    assert c.config.timeout == 30000

    c.config.no_session = True
    assert c.config.no_session is True
    c.config.no_session = False
    assert c.config.no_session is False

    test_url = freezer_server["endpoint"]
    c.config.endpoint_url = test_url
    assert c.config.endpoint_url == test_url

    c.config.security_mode = 1
    assert c.config.security_mode == 1

    test_policy = "http://opcfoundation.org/UA/SecurityPolicy#Basic256Sha256"
    c.config.security_policy_uri = test_policy
    assert c.config.security_policy_uri == test_policy
