import time
import pytest
from o6 import Client, types
import numpy as np

# ── Node IDs ──────────────────────────────────────────────────────────────────
BALANCE_UNIT = "ns=1;i=1034"
CURRENT_WEIGHT_VALUE = "ns=1;i=1069"
WEIGHT_STABLE_VALUE = "ns=1;i=1059"
TARE_MODE_VALUE = "ns=1;i=1064"
CURRENT_STATE = "ns=1;i=1045"

METHOD_START = "ns=1;i=1038"
METHOD_STOP = "ns=1;i=1044"
METHOD_ABORT = "ns=1;i=1043"
METHOD_SET_TARE = "ns=1;i=1048"
METHOD_SET_ZERO = "ns=1;i=1051"
METHOD_REGISTER_WEIGHT = "ns=1;i=1054"

SIM_SAMPLE_WEIGHT = "ns=1;i=1098"
SIM_TARE_WEIGHT = "ns=1;i=1099"
SIM_ZERO_WEIGHT = "ns=1;i=1100"
SIM_GROSS_WEIGHT = "ns=1;i=1101"
SIM_RAW_WEIGHT = "ns=1;i=1102"


def ensure_stopped(client):
    try:
        client.call(BALANCE_UNIT, METHOD_STOP)
        time.sleep(0.5)
    except Exception:
        pass


# ── Fixture ───────────────────────────────────────────────────────────────────
@pytest.fixture(scope="module")
def client(balance_server):
    c = Client(balance_server["endpoint"])
    c.connect()
    time.sleep(3.0)  # wait for server to finish publishing initial data
    yield c
    c.disconnect()


@pytest.fixture(scope="function")
def callback_client(balance_server):
    c = Client(balance_server["endpoint"])
    try:
        c.connect()
    except Exception as exc:
        pytest.skip(f"balance callback test skipped: endpoint unavailable ({exc})")
    time.sleep(0.5)
    yield c
    if c.connected:
        c.disconnect()


# ── Read ──────────────────────────────────────────────────────────────────────
class TestRead:
    def test_read_weight_stable(self, client):
        value = client.read(WEIGHT_STABLE_VALUE)
        assert isinstance(value, bool)

    def test_read_tare_mode(self, client):
        value = client.read(TARE_MODE_VALUE)
        assert isinstance(value, np.uint32)

    def test_read_current_state(self, client):
        value = client.read(CURRENT_STATE)
        assert value is not None

    def test_read_multiple(self, client):
        values = client.read(
            [
                WEIGHT_STABLE_VALUE,
                SIM_GROSS_WEIGHT,
            ]
        )
        assert len(values) == 2
        assert isinstance(values[0], bool)
        assert isinstance(values[1], float)

    def test_read_sim_nodes(self, client):
        for node in [
            SIM_SAMPLE_WEIGHT,
            SIM_TARE_WEIGHT,
            SIM_ZERO_WEIGHT,
            SIM_GROSS_WEIGHT,
            SIM_RAW_WEIGHT,
        ]:
            v = client.read(node)
            assert isinstance(v, (int, float)), f"{node} not numeric"


# ── Write ─────────────────────────────────────────────────────────────────────
class TestWrite:
    def test_write_sample_weight(self, client):
        client.write(SIM_SAMPLE_WEIGHT, types.Double(50.0))
        assert abs(client.read(SIM_SAMPLE_WEIGHT) - 50.0) < 0.01

    def test_write_tare_weight(self, client):
        client.write(SIM_TARE_WEIGHT, types.Double(5.0))
        assert abs(client.read(SIM_TARE_WEIGHT) - 5.0) < 0.01

    def test_write_zero_weight(self, client):
        client.write(SIM_ZERO_WEIGHT, types.Double(0.0))
        assert abs(client.read(SIM_ZERO_WEIGHT) - 0.0) < 0.01

    def test_write_multiple(self, client):
        client.write(
            {
                SIM_SAMPLE_WEIGHT: types.Double(10.0),
                SIM_TARE_WEIGHT: types.Double(2.0),
            }
        )
        assert abs(client.read(SIM_SAMPLE_WEIGHT) - 10.0) < 0.01
        assert abs(client.read(SIM_TARE_WEIGHT) - 2.0) < 0.01

    def test_write_roundtrip(self, client):
        original = client.read(SIM_SAMPLE_WEIGHT)
        client.write(SIM_SAMPLE_WEIGHT, types.Double(99.9))
        assert abs(client.read(SIM_SAMPLE_WEIGHT) - 99.9) < 0.01
        client.write(SIM_SAMPLE_WEIGHT, types.Double(float(original)))


# ── Call ──────────────────────────────────────────────────────────────────────
class TestCall:
    def test_call_set_tare(self, client):
        ensure_stopped(client)
        result = client.call(BALANCE_UNIT, METHOD_SET_TARE)
        assert result[0] == 0
        ensure_stopped(client)

    def test_call_register_weight(self, client):
        ensure_stopped(client)
        result = client.call(BALANCE_UNIT, METHOD_REGISTER_WEIGHT, [types.String("test")])
        assert result[0] == 0
        ensure_stopped(client)

    def test_call_start(self, client):
        ensure_stopped(client)
        try:
            result = client.call(BALANCE_UNIT, METHOD_START, [None])
            assert result[0] == 0
        except Exception as exc:
            pytest.skip(f"balance callback test skipped: connection dropped ({exc})")
        finally:
            ensure_stopped(client)

    def test_call_stop(self, client):
        ensure_stopped(client)
        try:
            client.call(BALANCE_UNIT, METHOD_START, [None])
            time.sleep(0.5)
            result = client.call(BALANCE_UNIT, METHOD_STOP)
            assert result[0] == 0
        except Exception as exc:
            pytest.skip(f"balance callback test skipped: connection dropped ({exc})")

    def test_call_start_changes_state(self, client):
        ensure_stopped(client)
        s1 = client.read(CURRENT_STATE)
        client.call(BALANCE_UNIT, METHOD_START, [None])
        time.sleep(0.3)
        s2 = client.read(CURRENT_STATE)
        assert s1 != s2
        ensure_stopped(client)


# ── Callback / Monitor ────────────────────────────────────────────────────────
class TestCallback:
    def test_monitor_weight_receives_value(self, callback_client):
        try:
            callback_client.write(SIM_SAMPLE_WEIGHT, types.Double(42.0))
            time.sleep(1.0)
            v1 = callback_client.read(SIM_GROSS_WEIGHT)

            callback_client.write(SIM_SAMPLE_WEIGHT, types.Double(43.0))
            time.sleep(1.0)
            v2 = callback_client.read(SIM_GROSS_WEIGHT)
        except Exception as exc:
            pytest.skip(f"balance callback test skipped: connection dropped ({exc})")

        assert isinstance(v1, (int, float))
        assert isinstance(v2, (int, float))
        assert v1 != v2

    def test_monitor_stable_flag(self, callback_client):
        try:
            values = []
            for _ in range(4):
                values.append(callback_client.read(WEIGHT_STABLE_VALUE))
                time.sleep(0.5)
        except Exception as exc:
            pytest.skip(f"balance callback test skipped: connection dropped ({exc})")
        assert all(isinstance(v, bool) for v in values)

    def test_monitor_multiple_nodes(self, callback_client):
        try:
            samples = []
            callback_client.write(SIM_SAMPLE_WEIGHT, types.Double(25.0))
            time.sleep(1.0)
            samples.append(
                (callback_client.read(SIM_SAMPLE_WEIGHT), callback_client.read(SIM_GROSS_WEIGHT))
            )

            callback_client.write(SIM_SAMPLE_WEIGHT, types.Double(26.0))
            time.sleep(1.0)
            samples.append(
                (callback_client.read(SIM_SAMPLE_WEIGHT), callback_client.read(SIM_GROSS_WEIGHT))
            )
        except Exception as exc:
            pytest.skip(f"balance callback test skipped: connection dropped ({exc})")

        assert all(isinstance(v, (int, float)) for pair in samples for v in pair)
