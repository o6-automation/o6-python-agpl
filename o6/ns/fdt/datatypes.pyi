# Copyright (c) 2026 o6 Automation GmbH
#
# SPDX-License-Identifier: AGPL-3.0-or-later
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

class AlarmType(enum.IntEnum):
    """Identifier for the alarm type to show the association between high- and low alarm and high-high- and low-low-alarm. (Provides mapping for Fdt.Dtm.DataAccess.AlarmType.)"""

    HIGH_HIGH_ALARM = 0
    HIGH_ALARM = 1
    LOW_LOW_ALARM = 2
    LOW_ALARM = 3

class ApplicationIdEnumeration(enum.IntEnum):
    """Identifies type of an application or function. (Provides mapping for Fdt.ApplicationId)"""

    ADJUST_SET_VALUE = 0
    ASSET_MANAGEMENT = 1
    AUDIT_TRAIL = 2
    CONFIGURATION = 3
    DIAGNOSIS = 4
    FORCE = 5
    OBSERVE = 6
    OFFLINE_COMPARE = 7
    OFFLINE_PARAMETERIZE = 8
    ONLINE_COMPARE = 9
    ONLINE_PARAMETERIZE = 10
    IDENTIFY = 11
    CALIBRATION = 12
    MAIN_OPERATION = 13
    NETWORK_MANAGEMENT = 14

class RangeType(enum.IntEnum):
    """Type of a range device data. (Provides mapping to Fdt.Dtm.DataAccess.RangeType)"""

    LOWER_RANGE = 0
    UPPER_RANGE = 1

class SubstitutionType(enum.IntEnum):
    """Type of substitution data. (Provides mapping to Fdt.Dtm.DataAccess.SubstitutionType)"""

    LAST_VALUE = 0
    LAST_VALID_VALUE = 1
    UPPER_RANGE = 2
    LOWER_RANGE = 3

class ClassificationDomainId(enum.IntEnum):
    POWER_DISTRIBUTION = 0
    MOTION_CONTROL = 1
    MEASUREMENT = 2
    OPERATOR_INTERFACE = 3
    MODULES_AND_CONTROLLERS = 4
    COMMUNICATION = 5

class IECDatatype(enum.IntEnum):
    BOOL = 0
    SINT = 1
    INT = 2
    DINT = 3
    LINT = 4
    USINT = 5
    UINT = 6
    UDINT = 7
    ULINT = 8
    REAL = 9
    LREAL = 10
    TIME = 11
    DATE = 12
    TIME_OF_DAY = 13
    DATE_AND_TIME = 14
    STRING = 15
    BYTE = 16
    WORD = 17
    DWORD = 18
    LWORD = 19
    WSTRING = 20

class ClassificationId(enum.IntEnum):
    """Classification according to device primary function.
    (Provides mapping to Fdt.Dtm.DeviceClassification.ClassificationId)"""

    FLOW = 0
    LEVEL = 1
    PRESSURE = 2
    TEMPERATURE = 3
    VALVE = 4
    POSITIONER = 5
    ACTUATOR = 6
    NC_RC = 7
    ENCODER = 8
    SPEED_DRIVE = 9
    HMI = 10
    ANALOG_INPUT = 11
    ANALOG_OUTPUT = 12
    DIGITAL_INPUT = 13
    DIGITAL_OUTPUT = 14
    ELECTROCHEMICAL_ANALYSER = 15
    DTM_SPECIFIC = 16
    UNIVERSAL = 17
    ANALYSER = 18
    REMOTE_IO = 19
    ANALOG_COMBINED_IO = 20
    DIGITAL_COMBINED_IO = 21
    RECORDER = 22
    CONTROLLER = 23
    ANGLE = 24
    LIMIT_SWITCH = 25
    CONVERTER = 26
    MOTOR = 27
    SWITCHBOARD = 28
    CIRCUIT_BREAKER = 29
    POWER_MONITORING = 30
    DISTRIBUTION_PANEL = 31
    CONTACTOR = 32
    PROTECTION_STARTER = 33
    SOFT_STARTER = 34
    DRIVE = 35
    AXIS_CONTROL = 36
    MOTOR_CONTROL_CENTER = 37
    CONTROL_VALVE = 38
    ELECTRICAL = 39
    DENSITY = 40
    QUALITY = 41
    SPEED_OR_ROTARY_FREQUENCY = 42
    RADIATION = 43
    WEIGHT_MASS = 44
    DISTANCE_OR_POSITION_PRESENCE = 45
    PUSH_BUTTON = 46
    JOYSTICK = 47
    KEYPAD = 48
    PILOT_LIGHT = 49
    STACK_LIGHT = 50
    DISPLAY = 51
    COMBINED_BUTTONS_AND_LIGHTS = 52
    OPERATOR_STATION = 53
    GENERAL_INPUT = 54
    GENERAL_OUTPUT = 55
    COMBINED_INPUT_OUTPUT = 56
    RELAY = 57
    TIMER = 58
    SCANNER = 59
    PROGRAMMABLE_CONTROLLER = 60
    COMMUNICATION_ADAPTER = 61
    GATEWAY = 62

class SupportedTransfer(enum.IntEnum):
    """This enumeration provides values to describe the types of transfers provided for a device. (Provides mapping to Fdt.Dtm.SupportedTransfer)"""

    NONE = 0
    ONLY_DOWNLOAD = 1
    ONLY_UPLOAD = 2
    BOTH_UPLOAD_AND_DOWNLOAD = 3

class DocumentClassification(enum.IntEnum):
    """Classification of a document. (Provides mapping for Fdt.Dtm.DocumentClassification)"""

    HELP = 0
    TECHNICAL_DOCUMENTATION = 1
    ORDERING_INFORMATION = 2
    MISCELLANEOUS = 3
    TENDER_SPECIFICATION = 4

class FdtDeviceClassificationType(ns0.datatypes.Structure):
    @property
    def classificationDomain(self) -> ClassificationDomainId: ...
    @classificationDomain.setter
    def classificationDomain(self, value: _Integer) -> None: ...
    @property
    def deviceClassification(self) -> ClassificationId: ...
    @deviceClassification.setter
    def deviceClassification(self, value: _Integer) -> None: ...

class FunctionExecutionResultState(enum.IntEnum):
    CANCEL = 0
    SUCCESS = 1
    FAIL = 2

class SignalTypeEnumeration(enum.IntEnum):
    INPUT = 0
    OUTPUT = 1

class SemanticInfoType(ns0.datatypes.Structure):
    @property
    def applicationDomain(self) -> o6.String: ...
    @applicationDomain.setter
    def applicationDomain(self, value: o6.String) -> None: ...
    @property
    def semanticId(self) -> o6.String: ...
    @semanticId.setter
    def semanticId(self, value: o6.String) -> None: ...

class DataRefType(ns0.datatypes.Structure):
    """Reference to a data item"""

    @property
    def dataId(self) -> o6.String: ...
    @dataId.setter
    def dataId(self, value: o6.String) -> None: ...
    @property
    def semanticInfo(self) -> SemanticInfoType: ...
    @semanticInfo.setter
    def semanticInfo(self, value: SemanticInfoType) -> None: ...
