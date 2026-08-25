from o6 import Client
import time
import numpy as np

FREEZER_STATE_CURRENT = 6047
FREEZER_TEMP_TARGET = 6057
FREEZER_TEMP_SENSOR = 6060
FREEZER_ALARM_RETAIN = 6094


def _resolve_nid(client: Client, ident: int, validator) -> str:
    ns_array = client.read("i=2255").tolist()
    candidates = [f"ns=65529;i={ident}"]
    candidates.extend(f"ns={idx};i={ident}" for idx in range(len(ns_array) + 2))

    fallback = None
    for nid in candidates:
        try:
            value = client.read(nid)
        except Exception:
            continue
        if fallback is None:
            fallback = nid
        try:
            if validator(value):
                return nid
        except Exception:
            continue

    if fallback is not None:
        return fallback
    raise ValueError(f"Could not resolve node id for i={ident}")


def test_freezer_connectivity(freezer_server):
    c = Client(freezer_server["endpoint"])
    c.connect()
    assert c.connected
    c.disconnect()


def test_freezer_alarm_state(freezer_server):
    c = Client(freezer_server["endpoint"])
    c.connect()
    retain_nid = _resolve_nid(c, FREEZER_ALARM_RETAIN, lambda v: isinstance(v, bool))
    retain = c.read(retain_nid)
    assert isinstance(retain, bool)
    c.disconnect()


def test_freezer_startup_state(freezer_server):
    c = Client(freezer_server["endpoint"])
    c.connect()
    state_nid = _resolve_nid(c, FREEZER_STATE_CURRENT, lambda v: "running" in str(v).lower())
    state = c.read(state_nid)
    assert "running" in str(state).lower()
    c.disconnect()


def test_freezer_cooling_cycle(freezer_server):
    c = Client(freezer_server["endpoint"])
    c.connect()
    temp_sensor_nid = _resolve_nid(c, FREEZER_TEMP_SENSOR, lambda v: isinstance(v, (int, float, np.floating)))
    temp_target_nid = _resolve_nid(c, FREEZER_TEMP_TARGET, lambda v: isinstance(v, (int, float, np.floating)))
    start_temp = c.read(temp_sensor_nid)
    c.write(temp_target_nid, float(start_temp) - 10.0)

    samples = [start_temp]
    for _ in range(8):
        time.sleep(0.5)
        samples.append(c.read(temp_sensor_nid))

    assert min(samples[1:]) < samples[0]
    c.disconnect()


def test_endpoints(freezer_server):
    c = Client(freezer_server["endpoint"])
    c.connect()
    endpoints = c.getEndpoints(freezer_server["endpoint"])
    assert isinstance(endpoints, list)
    assert len(endpoints) > 0
    for ep in endpoints:
        endpoint_url = getattr(ep, "endpointUrl", None)
        if endpoint_url is None:
            endpoint_url = getattr(ep, "endpoint_url", None)
        assert endpoint_url
    c.disconnect()


def test_find_server(freezer_server):
    c = Client(freezer_server["endpoint"])
    c.connect()
    print(f"Testing find_servers with endpoint {freezer_server['endpoint']}")
    servers = c.findServers(freezer_server["endpoint"])
    assert isinstance(servers, list)
    assert len(servers) > 0
    for srv in servers:
        app_uri = getattr(srv, "applicationUri", None)
        if app_uri is None:
            app_uri = getattr(srv, "application_uri", None)
        assert app_uri
    c.disconnect()


def test_subscriptions(freezer_server):
    c = Client(freezer_server["endpoint"])
    c.connect()
    sub = c.createSubscription()
    assert sub is not None
    assert isinstance(sub.id, (int, np.integer))
    assert sub.id > 0
    sub.delete()

    c.disconnect()


def test_config_options(freezer_server):
    c = Client(freezer_server["endpoint"])
    c.config.timeout = 30000
    assert c.config.timeout == 30000

    c.config.noSession = True
    assert c.config.noSession is True
    c.config.noSession = False
    assert c.config.noSession is False

    test_url = freezer_server["endpoint"]
    c.config.endpointUrl = test_url
    assert c.config.endpointUrl == test_url

    c.config.securityMode = 1
    assert c.config.securityMode == 1

    test_policy = "http://opcfoundation.org/UA/SecurityPolicy#Basic256Sha256"
    c.config.securityPolicyUri = test_policy
    assert c.config.securityPolicyUri == test_policy
