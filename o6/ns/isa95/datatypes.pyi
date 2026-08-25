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

import o6.ns.ns0 as ns0

class Decimal:
    pass

class DecimalString:
    pass

class DateString:
    pass

class TimeString:
    pass

class DurationString:
    pass

class CurrencyCode(ns0.datatypes.Structure):
    @property
    def namespaceUri(self) -> o6.String: ...
    @namespaceUri.setter
    def namespaceUri(self, value: o6.String) -> None: ...
    @property
    def unitId(self) -> o6.Int32: ...
    @unitId.setter
    def unitId(self, value: _Integer) -> None: ...
    @property
    def charId(self) -> list[o6.Byte]: ...
    @charId.setter
    def charId(self, value: Sequence[_Integer]) -> None: ...
    @property
    def displayName(self) -> o6.LocalizedText: ...
    @displayName.setter
    def displayName(self, value: o6.LocalizedText) -> None: ...
    @property
    def description(self) -> o6.LocalizedText: ...
    @description.setter
    def description(self, value: o6.LocalizedText) -> None: ...

class CDTIdentifier:
    pass

class CDTCode:
    pass

class CDTAmountDecimal:
    pass

class CDTBinaryObject:
    pass

class CDTDateTime:
    pass

class CDTGraphic:
    pass

class CDTMeasureDecimal:
    pass

class CDTMeasureDouble:
    pass

class CDTMeasureFloat:
    pass

class CDTMeasureInt16:
    pass

class CDTMeasureInt32:
    pass

class CDTMeasureInt64:
    pass

class CDTOrdinal:
    pass

class CDTPicture:
    pass

class CDTRateDecimal:
    pass

class CDTRateDouble:
    pass

class CDTRateFloat:
    pass

class CDTRateInt32:
    pass

class CDTSound:
    pass

class CDTVideo:
    pass

class ISA95TestResultMeasurementDataType(ns0.datatypes.Structure):
    @property
    def id(self) -> o6.NodeId: ...
    @id.setter
    def id(self, value: o6.NodeId) -> None: ...
    @property
    def testResultDescription(self) -> o6.LocalizedText: ...
    @testResultDescription.setter
    def testResultDescription(self, value: o6.LocalizedText) -> None: ...
    @property
    def date(self) -> o6.DateTime: ...
    @date.setter
    def date(self, value: o6.DateTime) -> None: ...
    @property
    def result(self) -> Any: ...
    @result.setter
    def result(self, value: Any) -> None: ...
    @property
    def resultUnitOfMeasure(self) -> ns0.datatypes.EUInformation: ...
    @resultUnitOfMeasure.setter
    def resultUnitOfMeasure(self, value: ns0.datatypes.EUInformation) -> None: ...
    @property
    def expiration(self) -> o6.DateTime: ...
    @expiration.setter
    def expiration(self, value: o6.DateTime) -> None: ...

class ISA95EquipmentElementLevelEnum(enum.IntFlag):
    ENTERPRISE = 0
    SITE = 1
    AREA = 2
    PROCESS_CELL = 3
    UNIT = 4
    PRODUCTION_LINE = 5
    WORK_CELL = 6
    PRODUCTION_UNIT = 7
    STORAGE_ZONE = 8
    STORAGE_UNIT = 9
    WORK_CENTER = 10
    WORK_UNIT = 11
    EQUIPMENT_MODULE = 12
    CONTROL_MODULE = 13
    OTHER = 14

class ISA95TestResultDataType(ns0.datatypes.Structure):
    @property
    def id(self) -> o6.NodeId: ...
    @id.setter
    def id(self, value: o6.NodeId) -> None: ...
    @property
    def testResultDescription(self) -> o6.LocalizedText: ...
    @testResultDescription.setter
    def testResultDescription(self, value: o6.LocalizedText) -> None: ...
    @property
    def date(self) -> o6.DateTime: ...
    @date.setter
    def date(self, value: o6.DateTime) -> None: ...
    @property
    def result(self) -> Any: ...
    @result.setter
    def result(self, value: Any) -> None: ...
    @property
    def resultUnitOfMeasure(self) -> o6.String: ...
    @resultUnitOfMeasure.setter
    def resultUnitOfMeasure(self, value: o6.String) -> None: ...
    @property
    def expiration(self) -> o6.DateTime: ...
    @expiration.setter
    def expiration(self, value: o6.DateTime) -> None: ...

class NormalizedString:
    pass

class ISA95AssetAssignmentDataType(ns0.datatypes.Structure):
    @property
    def id(self) -> o6.NodeId: ...
    @id.setter
    def id(self, value: o6.NodeId) -> None: ...
    @property
    def assinmentDescription(self) -> o6.LocalizedText: ...
    @assinmentDescription.setter
    def assinmentDescription(self, value: o6.LocalizedText) -> None: ...
    @property
    def startTime(self) -> o6.DateTime: ...
    @startTime.setter
    def startTime(self, value: o6.DateTime) -> None: ...
    @property
    def endTime(self) -> o6.DateTime: ...
    @endTime.setter
    def endTime(self, value: o6.DateTime) -> None: ...
