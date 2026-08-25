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

import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2

import o6.ns.ns0 as ns0

class JobExecutionMode(enum.IntFlag):
    SIMULATION_MODE = 0
    TEST_MODE = 1
    PRODUCTION_MODE = 2

class ProcessIrregularity(enum.IntFlag):
    CAPABILITY_UNAVAILABLE = 0
    DETECTED = 1
    NOT_DETECTED = 2
    NOT_YET_DETERMINED = 3

class JobResult(enum.IntFlag):
    UNKNOWN = 0
    SUCCESSFUL = 1
    UNSUCCESSFUL = 2

class OutputInfoType(enum.IntFlag):
    ORDER_NUMBER = 0
    LOT_NUMBER = 1
    SERIAL_NUMBER = 2

class OutputInformationDataType(ns0.datatypes.Structure):
    @property
    def itemNumber(self) -> o6.String: ...
    @itemNumber.setter
    def itemNumber(self, value: o6.String) -> None: ...
    @property
    def outputInfo(self) -> OutputInfoType: ...
    @outputInfo.setter
    def outputInfo(self, value: _Integer) -> None: ...
    @property
    def orderNumber(self) -> o6.String | None: ...
    @orderNumber.setter
    def orderNumber(self, value: o6.String | None) -> None: ...
    @property
    def lotNumber(self) -> o6.String | None: ...
    @lotNumber.setter
    def lotNumber(self, value: o6.String | None) -> None: ...
    @property
    def serialNumber(self) -> o6.String | None: ...
    @serialNumber.setter
    def serialNumber(self, value: o6.String | None) -> None: ...

class BOMComponentInformationDataType(ns0.datatypes.Structure):
    @property
    def identification(self) -> OutputInformationDataType: ...
    @identification.setter
    def identification(self, value: OutputInformationDataType) -> None: ...
    @property
    def quantity(self) -> o6.Double: ...
    @quantity.setter
    def quantity(self, value: SupportsFloat) -> None: ...
    @property
    def engineeringUnits(self) -> ns0.datatypes.EUInformation: ...
    @engineeringUnits.setter
    def engineeringUnits(self, value: ns0.datatypes.EUInformation) -> None: ...

class BOMInformationDataType(ns0.datatypes.Structure):
    @property
    def identification(self) -> OutputInformationDataType: ...
    @identification.setter
    def identification(self, value: OutputInformationDataType) -> None: ...
    @property
    def componentInformation(self) -> list[BOMComponentInformationDataType]: ...
    @componentInformation.setter
    def componentInformation(self, value: Sequence[BOMComponentInformationDataType]) -> None: ...

class OutputPerformanceInfoDataType(ns0.datatypes.Structure):
    @property
    def identification(self) -> OutputInformationDataType: ...
    @identification.setter
    def identification(self, value: OutputInformationDataType) -> None: ...
    @property
    def startTime(self) -> o6.DateTime | None: ...
    @startTime.setter
    def startTime(self, value: o6.DateTime | None) -> None: ...
    @property
    def endTime(self) -> o6.DateTime | None: ...
    @endTime.setter
    def endTime(self, value: o6.DateTime | None) -> None: ...
    @property
    def parameters(self) -> list[isa95_jobcontrol_v2.datatypes.ISA95ParameterDataType]: ...
    @parameters.setter
    def parameters(self, value: Sequence[isa95_jobcontrol_v2.datatypes.ISA95ParameterDataType]) -> None: ...
