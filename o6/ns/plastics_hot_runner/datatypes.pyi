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

from typing import Any, Sequence, SupportsFloat

import numpy as np

_Integer = int | np.integer[Any]

_Boolean = bool | np.bool_

import enum

from o6.node import ObjectNode as _ObjectNode, VariableNode as _VariableNode

import uuid

import o6

import o6.ns.di as di

import o6.ns.ns0 as ns0

import o6.ns.plastics_rubber as plastics_rubber

class ControllerTypeEnumeration(enum.IntFlag):
    CLOSED_LOOP_CONTROL = 0
    MANUAL = 1
    SYNCHRONOUS_ZONE = 2
    CASCADE = 3
    COOL_ZONE = 4
    MEASURING_ZONE = 5
    NOT_USED = 6

class ZoneStatusEnumeration(enum.IntFlag):
    OTHER = 0
    GOOD = 1
    SENSOR_FAULT = 2
    TEMPERATURE_SENSOR_BROKEN = 3
    TEMPERATURE_SENSOR_REVERSED = 4
    POWER_UNIT_FAILED = 5
    HEATING_OUTPUT_TO_LOW = 6
    ERROR = 7
    WARNING = 8
    LEAKAGE_DETECTED = 9

class TimeMethodPIDParametersDataType(ns0.datatypes.Structure):
    @property
    def xp(self) -> o6.Double: ...
    @xp.setter
    def xp(self, value: SupportsFloat) -> None: ...
    @property
    def tn(self) -> o6.Double: ...
    @tn.setter
    def tn(self, value: SupportsFloat) -> None: ...
    @property
    def tv(self) -> o6.Double: ...
    @tv.setter
    def tv(self, value: SupportsFloat) -> None: ...
    @property
    def ts(self) -> o6.Double: ...
    @ts.setter
    def ts(self, value: SupportsFloat) -> None: ...
