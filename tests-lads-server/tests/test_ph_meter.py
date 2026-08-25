import o6
from o6 import Client
from o6.node import (
    _nodeclass2type as nodeclass2type,
    ObjectNode,
    VariableNode,
    MethodNode,
)
import math
import time
import numpy as np

PH_SENSOR_VALUE = 6113
PH_COMPENSATION_VALUE = 6110
PH_TEMPERATURE_SENSOR_VALUE = 6118
PH_CALIBRATION_VALUES = 6109
PH_TEMPLATE_CALIBRATE_OFFSET_ID = "ns=1;i=1036"
PH_TEMPLATE_CALIBRATE_SLOPE_ID = "ns=1;i=1043"


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


def test_ph_meter_connectivity(ph_meter_server):
    c = Client(ph_meter_server["endpoint"])
    c.connect()
    assert c.connected
    c.disconnect()


def test_ph_range(ph_meter_server):
    c = Client(ph_meter_server["endpoint"])
    c.connect()
    sensor_nid = _resolve_nid(c, PH_SENSOR_VALUE, lambda v: isinstance(v, (int, float, np.floating)))
    ph = c.read(sensor_nid)
    if isinstance(ph, str):
        assert ph.strip().lower() == "nan"
    else:
        assert isinstance(ph, (int, float, np.integer, np.floating))
        assert math.isfinite(float(ph))
        assert 0.0 <= float(ph) <= 14.0
    c.disconnect()


def test_ph_temperature_compensation(ph_meter_server):
    c = Client(ph_meter_server["endpoint"])
    c.connect()
    temp_nid = _resolve_nid(c, PH_TEMPERATURE_SENSOR_VALUE, lambda v: isinstance(v, (int, float, np.floating)))
    comp_nid = _resolve_nid(c, PH_COMPENSATION_VALUE, lambda v: isinstance(v, (int, float, np.floating)))
    for _ in range(5):
        time.sleep(0.4)
        temp = c.read(temp_nid)
        comp = c.read(comp_nid)
        assert isinstance(temp, (int, float, np.integer, np.floating))
        assert isinstance(comp, (int, float, np.integer, np.floating))
    c.disconnect()


def test_ph_calibration(ph_meter_server):
    c = Client(ph_meter_server["endpoint"])
    c.connect()
    offset_template_id = c.read(PH_TEMPLATE_CALIBRATE_OFFSET_ID)
    slope_template_id = c.read(PH_TEMPLATE_CALIBRATE_SLOPE_ID)
    assert isinstance(offset_template_id, str)
    assert isinstance(slope_template_id, str)
    assert "calibrate" in offset_template_id.lower()
    assert "calibrate" in slope_template_id.lower()

    calibration_nid = _resolve_nid(
        c,
        PH_CALIBRATION_VALUES,
        lambda v: isinstance(v, (np.ndarray, int, float, np.integer, np.floating)),
    )
    calibration_values = c.read(calibration_nid)
    if isinstance(calibration_values, np.ndarray):
        assert calibration_values.size > 0
        assert all(isinstance(v, (int, float, np.integer, np.floating)) for v in calibration_values)
    else:
        assert isinstance(calibration_values, (int, float, np.integer, np.floating))
        assert math.isfinite(float(calibration_values))
    c.disconnect()


def test_object_node(ph_meter_server):
    assert nodeclass2type(o6.ns.ns0.datatypes.NodeClass.OBJECT) is ObjectNode


def test_variable_node(ph_meter_server):
    assert nodeclass2type(o6.ns.ns0.datatypes.NodeClass.VARIABLE) is VariableNode


def test_method_node(ph_meter_server):
    assert nodeclass2type(o6.ns.ns0.datatypes.NodeClass.METHOD) is MethodNode
