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

class EncoderChannelStateEnumeration(enum.IntFlag):
    NORMAL_OPERATION = 0
    ERROR_ACKNOWLEDGEMENT = 1
    ERROR = 2
    REFERENCE_VALUE__GX_XIST2 = 3
    WAIT_FOR_REFERENCE_MARKS = 4
    SET_SHIFT_HOME_POSITION = 5
    WAIT_FOR_MEASURED_VALUE = 6
    MEASURED_VALUE_IN_XIST2 = 7
    PARKING = 8
    PARKING_ERROR = 9
    PARKING_ERROR_ACK = 10

class EventTypeEnumeration(enum.IntFlag):
    FAULT = 0
    WARNING = 1
    UNSPECIFIED = 255

class EncoderAxisTypeEnumeration(enum.IntFlag):
    ROTARY = 0
    LINEAR = 1

class EncoderCodeSequenceEnumeration(enum.IntFlag):
    INCREASING_CLOCKWISE = 0
    INCREASING_COUNTERCLOCKWISE = 1

class EncoderAlarmChannelControlEnumeration(enum.IntFlag):
    ALARM_CHANNEL_DISABLED = 0
    ALARM_CHANNEL_ENABLED = 1

class EncoderPresetControlEnumeration(enum.IntFlag):
    ENABLE_PRESET_CONTROL = 0
    DISABLE_PRESET_CONTROL = 1

class EncoderSensorAbsoluteTypeEnumeration(enum.IntFlag):
    SINGLETURN = 0
    MULTITURN = 1

class EncoderSignalTypeEnumeration(enum.IntFlag):
    OTHER = 0
    BISS_C = 1
    ENDAT2_1 = 2
    ENDAT2_2 = 3
    HIPERFACE = 4
    HIPERFACE_DSL = 5
    SSI_BINARY = 6
    SSI_GRAY_CODE = 7
    SINCOS_1_VSS = 8
    SCS_OPEN_LINK = 9
    DRIVECLIQ = 10
    BISS_LINE = 11
    FANUC_37_BIT_SERIAL_COMM = 12
    MITSUBISHI_40_BIT_SERIAL_COMM = 13
    OMRON_PANASONIC_48_BIT_SERIAL_COMM = 14
    YASKAWA_36_BIT_SERIAL_COMM = 15
    RS422_5_V_TTL = 16
    RS422_5__30_V = 17
    SINCOS_1_VPP = 18
    RESOLVER = 19
    HTL_PUSH_PULL = 20
    RS485 = 21
    RS485_SINCOS = 22
    RS485_HTL = 23
    RS485_TTL = 24

class EncoderConfigParameterResultEnumeration(enum.IntFlag):
    INVALID = 0
    NOT_SUPPORTED = 1
    READ_ONLY = 2

class EncoderConfigTypeEnumeration(enum.IntFlag):
    STATIC = 0
    DYNAMIC = 1

class EncoderDiagnosisReasonEnumeration(enum.IntFlag):
    ALL_DISAPPEARS = 0
    APPEARS = 1
    DISAPPEARS = 2
    DISAPPEARS_OTHER_REMAIN = 3

class LogEntryDataType(ns0.datatypes.Structure):
    @property
    def faultSituationNumber(self) -> o6.Byte: ...
    @faultSituationNumber.setter
    def faultSituationNumber(self, value: _Integer) -> None: ...
    @property
    def eventNumber(self) -> o6.UInt32: ...
    @eventNumber.setter
    def eventNumber(self, value: _Integer) -> None: ...
    @property
    def eventType(self) -> EventTypeEnumeration: ...
    @eventType.setter
    def eventType(self, value: _Integer) -> None: ...
    @property
    def eventCode(self) -> o6.Int32: ...
    @eventCode.setter
    def eventCode(self, value: _Integer) -> None: ...
    @property
    def eventText(self) -> o6.LocalizedText: ...
    @eventText.setter
    def eventText(self, value: o6.LocalizedText) -> None: ...
    @property
    def eventComing(self) -> o6.DateTime: ...
    @eventComing.setter
    def eventComing(self, value: o6.DateTime) -> None: ...
    @property
    def eventGoing(self) -> o6.DateTime: ...
    @eventGoing.setter
    def eventGoing(self, value: o6.DateTime) -> None: ...
    @property
    def eventAcknowledged(self) -> o6.DateTime: ...
    @eventAcknowledged.setter
    def eventAcknowledged(self, value: o6.DateTime) -> None: ...
