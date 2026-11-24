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

"""Generated OPC UA isa95 namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0
from . import reftypes as isa95_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=isa95;i=927", browseName="ns=isa95;Decimal", parent="i=15")
class Decimal:
    pass


@o6.datatype(nodeId="ns=isa95;i=4772", browseName="ns=isa95;DecimalString", parent="i=12")
class DecimalString:
    pass


@o6.datatype(nodeId="ns=isa95;i=4773", browseName="ns=isa95;DateString", parent="i=12")
class DateString:
    pass


@o6.datatype(nodeId="ns=isa95;i=4774", browseName="ns=isa95;TimeString", parent="i=12")
class TimeString:
    pass


@o6.datatype(nodeId="ns=isa95;i=4775", browseName="ns=isa95;DurationString", parent="i=12")
class DurationString:
    pass


@o6.datatype(nodeId="ns=isa95;i=4776", browseName="ns=isa95;CurrencyCode", defaultEncodingId="ns=isa95;i=4788")
class CurrencyCode(ns0.datatypes.Structure):
    namespaceUri: o6.String
    unitId: o6.Int32
    charId: list[o6.Byte]
    displayName: o6.LocalizedText
    description: o6.LocalizedText = o6.field(name="Description")


@o6.datatype(nodeId="ns=isa95;i=4777", browseName="ns=isa95;CDTIdentifier", parent="i=12")
class CDTIdentifier:
    pass


@o6.datatype(nodeId="ns=isa95;i=4792", browseName="ns=isa95;CDTCode", parent="i=12")
class CDTCode:
    pass


@o6.datatype(nodeId="ns=isa95;i=4796", browseName="ns=isa95;CDTAmountDecimal", parent="ns=isa95;i=927")
class CDTAmountDecimal:
    pass


@o6.datatype(nodeId="ns=isa95;i=4798", browseName="ns=isa95;CDTBinaryObject", parent="i=15")
class CDTBinaryObject:
    pass


@o6.datatype(nodeId="ns=isa95;i=4803", browseName="ns=isa95;CDTDateTime", parent="i=294")
class CDTDateTime:
    pass


@o6.datatype(nodeId="ns=isa95;i=4806", browseName="ns=isa95;CDTGraphic", parent="i=15")
class CDTGraphic:
    pass


@o6.datatype(nodeId="ns=isa95;i=4809", browseName="ns=isa95;CDTMeasureDecimal", parent="ns=isa95;i=927")
class CDTMeasureDecimal:
    pass


@o6.datatype(nodeId="ns=isa95;i=4811", browseName="ns=isa95;CDTMeasureDouble", parent="i=11")
class CDTMeasureDouble:
    pass


@o6.datatype(nodeId="ns=isa95;i=4813", browseName="ns=isa95;CDTMeasureFloat", parent="i=10")
class CDTMeasureFloat:
    pass


@o6.datatype(nodeId="ns=isa95;i=4815", browseName="ns=isa95;CDTMeasureInt16", parent="i=4")
class CDTMeasureInt16:
    pass


@o6.datatype(nodeId="ns=isa95;i=4817", browseName="ns=isa95;CDTMeasureInt32", parent="i=6")
class CDTMeasureInt32:
    pass


@o6.datatype(nodeId="ns=isa95;i=4819", browseName="ns=isa95;CDTMeasureInt64", parent="i=8")
class CDTMeasureInt64:
    pass


@o6.datatype(nodeId="ns=isa95;i=4821", browseName="ns=isa95;CDTOrdinal", parent="i=6")
class CDTOrdinal:
    pass


@o6.datatype(nodeId="ns=isa95;i=4822", browseName="ns=isa95;CDTPicture", parent="i=30")
class CDTPicture:
    pass


@o6.datatype(nodeId="ns=isa95;i=4825", browseName="ns=isa95;CDTRateDecimal", parent="ns=isa95;i=927")
class CDTRateDecimal:
    pass


@o6.datatype(nodeId="ns=isa95;i=4832", browseName="ns=isa95;CDTRateDouble", parent="i=11")
class CDTRateDouble:
    pass


@o6.datatype(nodeId="ns=isa95;i=4839", browseName="ns=isa95;CDTRateFloat", parent="i=10")
class CDTRateFloat:
    pass


@o6.datatype(nodeId="ns=isa95;i=4846", browseName="ns=isa95;CDTRateInt32", parent="i=6")
class CDTRateInt32:
    pass


@o6.datatype(nodeId="ns=isa95;i=4853", browseName="ns=isa95;CDTSound", parent="i=15")
class CDTSound:
    pass


@o6.datatype(nodeId="ns=isa95;i=4856", browseName="ns=isa95;CDTVideo", parent="i=15")
class CDTVideo:
    pass


@o6.datatype(nodeId="ns=isa95;i=4862", browseName="ns=isa95;ISA95TestResultMeasurementDataType", defaultEncodingId="ns=isa95;i=4867")
class ISA95TestResultMeasurementDataType(ns0.datatypes.Structure):
    id: o6.NodeId = o6.field(name="Id")
    testResultDescription: o6.LocalizedText = o6.field(name="TestResultDescription")
    date: o6.DateTime = o6.field(name="Date")
    result: Any = o6.field(name="Result")
    resultUnitOfMeasure: ns0.datatypes.EUInformation = o6.field(name="ResultUnitOfMeasure")
    expiration: o6.DateTime = o6.field(name="Expiration")


@o6.enumtype(nodeId="ns=isa95;i=4871", browseName="ns=isa95;ISA95EquipmentElementLevelEnum")
class ISA95EquipmentElementLevelEnum(ns0.datatypes.Enumeration):
    ENTERPRISE = o6.enumfield(0, name="Enterprise")
    SITE = o6.enumfield(1, name="Site")
    AREA = o6.enumfield(2, name="Area")
    PROCESS_CELL = o6.enumfield(3, name="ProcessCell")
    UNIT = o6.enumfield(4, name="Unit")
    PRODUCTION_LINE = o6.enumfield(5, name="ProductionLine")
    WORK_CELL = o6.enumfield(6, name="WorkCell")
    PRODUCTION_UNIT = o6.enumfield(7, name="ProductionUnit")
    STORAGE_ZONE = o6.enumfield(8, name="StorageZone")
    STORAGE_UNIT = o6.enumfield(9, name="StorageUnit")
    WORK_CENTER = o6.enumfield(10, name="WorkCenter")
    WORK_UNIT = o6.enumfield(11, name="WorkUnit")
    EQUIPMENT_MODULE = o6.enumfield(12, name="EquipmentModule")
    CONTROL_MODULE = o6.enumfield(13, name="ControlModule")
    OTHER = o6.enumfield(14, name="Other")


@o6.datatype(nodeId="ns=isa95;i=4873", browseName="ns=isa95;ISA95TestResultDataType", defaultEncodingId="ns=isa95;i=4902")
class ISA95TestResultDataType(ns0.datatypes.Structure):
    id: o6.NodeId = o6.field(name="Id")
    testResultDescription: o6.LocalizedText = o6.field(name="TestResultDescription")
    date: o6.DateTime = o6.field(name="Date")
    result: Any = o6.field(name="Result")
    resultUnitOfMeasure: o6.String = o6.field(name="ResultUnitOfMeasure")
    expiration: o6.DateTime = o6.field(name="Expiration")


@o6.datatype(nodeId="ns=isa95;i=4929", browseName="ns=isa95;NormalizedString", parent="i=12")
class NormalizedString:
    pass


@o6.datatype(nodeId="ns=isa95;i=4956", browseName="ns=isa95;ISA95AssetAssignmentDataType", defaultEncodingId="ns=isa95;i=4973")
class ISA95AssetAssignmentDataType(ns0.datatypes.Structure):
    id: o6.NodeId = o6.field(name="Id")
    assinmentDescription: o6.LocalizedText = o6.field(name="AssinmentDescription")
    startTime: o6.DateTime = o6.field(name="StartTime")
    endTime: o6.DateTime = o6.field(name="EndTime")


del Any, TYPE_CHECKING, uuid, o6, ns0, isa95_reftypes
