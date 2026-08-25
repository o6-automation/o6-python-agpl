import time
import math
import pytest
import o6
import o6.ns.ns0.datatypes as nsdt0
from o6 import Client

VISCOSITY_SENSOR_VALUE = "ns=1;i=1092"
RELATIVE_TORQUE_SENSOR_VALUE = "ns=1;i=1087"


def test_viscometer_connectivity(viscometer_server):
    c = Client(viscometer_server["endpoint"])
    c.connect()
    assert c.connected
    c.disconnect()


def test_viscometer_value_changes(viscometer_server):
    c = Client(viscometer_server["endpoint"])
    c.connect()
    # Relative torque changes with simulator noise, even when speed controller is not running.
    values = []
    for _ in range(8):
        values.append(c.read(RELATIVE_TORQUE_SENSOR_VALUE))
        time.sleep(0.3)

    rounded = {round(v, 5) for v in values}
    assert len(rounded) >= 2
    c.disconnect()


def test_viscometer_positive_values(viscometer_server):
    c = Client(viscometer_server["endpoint"])
    c.connect()
    torque = c.read(RELATIVE_TORQUE_SENSOR_VALUE)
    assert isinstance(torque, (int, float))
    assert math.isfinite(torque)
    # In idle state the relative torque is noise around 0%, but should stay bounded.
    assert abs(torque) < 5.0
    c.disconnect()


def test_viscometer_sensor_stability(viscometer_server):
    c = Client(viscometer_server["endpoint"])
    c.connect()
    values = []
    for _ in range(6):
        values.append(c.read(RELATIVE_TORQUE_SENSOR_VALUE))
        time.sleep(0.4)

    delta = max(abs(values[i] - values[i - 1]) for i in range(1, len(values)))
    assert delta < 2.0
    c.disconnect()


def test_service_history_read_request_response(viscometer_server):
    c = Client(viscometer_server["endpoint"])
    c.connect()
    request = nsdt0.HistoryReadRequest()
    rvid = nsdt0.HistoryReadValueId()
    rvid.nodeId = o6.NodeId("ns=1;s=BooleanVariable")
    request.nodesToRead = [rvid]

    response = c.serviceHistoryRead(request)

    assert response is not None
    assert hasattr(response, "responseHeader")
    assert response.responseHeader.serviceResult is not None
    c.disconnect()


def test_service_history_read_no_args(viscometer_server):
    """Calling with no arguments raises TypeError."""
    c = Client(viscometer_server["endpoint"])
    c.connect()
    with pytest.raises(TypeError):
        c.serviceHistoryRead()
    c.disconnect()
