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

PH_SENSOR_VALUE = "ns=62;i=6113"
PH_COMPENSATION_VALUE = "ns=62;i=6110"
PH_TEMPERATURE_SENSOR_VALUE = "ns=62;i=6118"
PH_CALIBRATION_VALUES = "ns=62;i=6109"
PH_TEMPLATE_CALIBRATE_OFFSET_ID = "ns=1;i=1036"
PH_TEMPLATE_CALIBRATE_SLOPE_ID = "ns=1;i=1043"


def test_ph_meter_connectivity(ph_meter_server):
    c = Client(ph_meter_server["endpoint"])
    c.connect()
    assert c.connected
    c.disconnect()


def test_ph_range(ph_meter_server):
    c = Client(ph_meter_server["endpoint"])
    c.connect()
    ph = c.read(PH_SENSOR_VALUE)
    assert isinstance(ph, (int, float))
    assert math.isfinite(ph)
    assert 0.0 <= ph <= 14.0
    c.disconnect()


def test_ph_temperature_compensation(ph_meter_server):
    c = Client(ph_meter_server["endpoint"])
    c.connect()
    for _ in range(5):
        time.sleep(0.4)
        temp = c.read(PH_TEMPERATURE_SENSOR_VALUE)
        comp = c.read(PH_COMPENSATION_VALUE)
        assert isinstance(temp, (int, float))
        assert isinstance(comp, (int, float))
        # pH compensation value tracks temperature in the simulator loop.
        assert abs(temp - comp) < 0.5
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

    calibration_values = c.read(PH_CALIBRATION_VALUES)
    assert isinstance(calibration_values, np.ndarray)
    assert len(calibration_values) == 2
    assert all(isinstance(v, (int, float)) for v in calibration_values)

    offset, slope = calibration_values
    assert -1.0 <= offset <= 1.0
    assert 80.0 <= slope <= 105.0
    c.disconnect()


def test_object_node(ph_meter_server):
    assert nodeclass2type(o6.NodeClass.OBJECT) is ObjectNode


def test_variable_node(ph_meter_server):
    assert nodeclass2type(o6.NodeClass.VARIABLE) is VariableNode


def test_method_node(ph_meter_server):
    assert nodeclass2type(o6.NodeClass.METHOD) is MethodNode
