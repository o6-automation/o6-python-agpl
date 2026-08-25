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

"""Generated OPC UA adi namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as adi_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=adi;i=3003", browseName="AcquisitionResultStatusEnumeration")
class AcquisitionResultStatusEnumeration(ns0.datatypes.Enumeration):
    NOT_USED = o6.enumfield(0, name="NOT_USED")
    GOOD = o6.enumfield(1, name="GOOD")
    BAD = o6.enumfield(2, name="BAD")
    UNKNOWN = o6.enumfield(3, name="UNKNOWN")
    PARTIAL = o6.enumfield(4, name="PARTIAL")


@o6.enumtype(nodeId="ns=adi;i=3009", browseName="AlarmStateEnumeration")
class AlarmStateEnumeration(ns0.datatypes.Enumeration):
    NORMAL_0 = o6.enumfield(0, name="NORMAL_0")
    WARNING_LOW_1 = o6.enumfield(1, name="WARNING_LOW_1")
    WARNING_HIGH_2 = o6.enumfield(2, name="WARNING_HIGH_2")
    WARNING_4 = o6.enumfield(4, name="WARNING_4")
    ALARM_LOW_8 = o6.enumfield(8, name="ALARM_LOW_8")
    ALARM_HIGH_16 = o6.enumfield(16, name="ALARM_HIGH_16")
    ALARM_32 = o6.enumfield(32, name="ALARM_32")


@o6.enumtype(nodeId="ns=adi;i=9378", browseName="ExecutionCycleEnumeration")
class ExecutionCycleEnumeration(ns0.datatypes.Enumeration):
    IDLE = o6.enumfield(0, name="IDLE")
    DIAGNOSTIC = o6.enumfield(1, name="DIAGNOSTIC")
    CLEANING = o6.enumfield(2, name="CLEANING")
    CALIBRATION = o6.enumfield(4, name="CALIBRATION")
    VALIDATION = o6.enumfield(8, name="VALIDATION")
    SAMPLING = o6.enumfield(16, name="SAMPLING")
    DIAGNOSTIC_WITH_GRAB_SAMPLE = o6.enumfield(32769, name="DIAGNOSTIC_WITH_GRAB_SAMPLE")
    CLEANING_WITH_GRAB_SAMPLE = o6.enumfield(32770, name="CLEANING_WITH_GRAB_SAMPLE")
    CALIBRATION_WITH_GRAB_SAMPLE = o6.enumfield(32772, name="CALIBRATION_WITH_GRAB_SAMPLE")
    VALIDATION_WITH_GRAB_SAMPLE = o6.enumfield(32776, name="VALIDATION_WITH_GRAB_SAMPLE")
    SAMPLING_WITH_GRAB_SAMPLE = o6.enumfield(32784, name="SAMPLING_WITH_GRAB_SAMPLE")


del Any, TYPE_CHECKING, uuid, o6, di, ns0, adi_reftypes
