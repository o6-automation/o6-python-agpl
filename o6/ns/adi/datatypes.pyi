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

class AcquisitionResultStatusEnumeration(enum.IntFlag):
    NOT_USED = 0
    GOOD = 1
    BAD = 2
    UNKNOWN = 3
    PARTIAL = 4

class AlarmStateEnumeration(enum.IntFlag):
    NORMAL_0 = 0
    WARNING_LOW_1 = 1
    WARNING_HIGH_2 = 2
    WARNING_4 = 4
    ALARM_LOW_8 = 8
    ALARM_HIGH_16 = 16
    ALARM_32 = 32

class ExecutionCycleEnumeration(enum.IntFlag):
    IDLE = 0
    DIAGNOSTIC = 1
    CLEANING = 2
    CALIBRATION = 4
    VALIDATION = 8
    SAMPLING = 16
    DIAGNOSTIC_WITH_GRAB_SAMPLE = 32769
    CLEANING_WITH_GRAB_SAMPLE = 32770
    CALIBRATION_WITH_GRAB_SAMPLE = 32772
    VALIDATION_WITH_GRAB_SAMPLE = 32776
    SAMPLING_WITH_GRAB_SAMPLE = 32784
