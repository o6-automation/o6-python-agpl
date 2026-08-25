# Copyright (c) 2026 o6 Automation GmbH
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Generated OPC UA plastics_hot_runner namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=plastics_hot_runner;i=3002", browseName="ControllerTypeEnumeration")
class ControllerTypeEnumeration(ns0.datatypes.Enumeration):
    CLOSED_LOOP_CONTROL = o6.enumfield(0, name="CLOSED_LOOP_CONTROL")
    MANUAL = o6.enumfield(1, name="MANUAL")
    SYNCHRONOUS_ZONE = o6.enumfield(2, name="SYNCHRONOUS_ZONE")
    CASCADE = o6.enumfield(3, name="CASCADE")
    COOL_ZONE = o6.enumfield(4, name="COOL_ZONE")
    MEASURING_ZONE = o6.enumfield(5, name="MEASURING_ZONE")
    NOT_USED = o6.enumfield(6, name="NOT_USED")


@o6.enumtype(nodeId="ns=plastics_hot_runner;i=3003", browseName="ZoneStatusEnumeration")
class ZoneStatusEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    GOOD = o6.enumfield(1, name="GOOD")
    SENSOR_FAULT = o6.enumfield(2, name="SENSOR_FAULT")
    TEMPERATURE_SENSOR_BROKEN = o6.enumfield(3, name="TEMPERATURE_SENSOR_BROKEN")
    TEMPERATURE_SENSOR_REVERSED = o6.enumfield(4, name="TEMPERATURE_SENSOR_REVERSED")
    POWER_UNIT_FAILED = o6.enumfield(5, name="POWER_UNIT_FAILED")
    HEATING_OUTPUT_TO_LOW = o6.enumfield(6, name="HEATING_OUTPUT_TO_LOW")
    ERROR = o6.enumfield(7, name="ERROR")
    WARNING = o6.enumfield(8, name="WARNING")
    LEAKAGE_DETECTED = o6.enumfield(9, name="LEAKAGE_DETECTED")


@o6.datatype(nodeId="ns=plastics_hot_runner;i=3005", browseName="TimeMethodPIDParametersDataType", defaultEncodingId="ns=plastics_hot_runner;i=5037")
class TimeMethodPIDParametersDataType(ns0.datatypes.Structure):
    xp: o6.Double
    tn: o6.Double
    tv: o6.Double
    ts: o6.Double


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber
