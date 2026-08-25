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


@o6.datatype(nodeId="ns=isa95;i=927", browseName="Decimal", parent="i=15")
class Decimal:
    pass


@o6.datatype(nodeId="ns=isa95;i=4772", browseName="DecimalString", parent="i=12")
class DecimalString:
    pass


@o6.datatype(nodeId="ns=isa95;i=4773", browseName="DateString", parent="i=12")
class DateString:
    pass


@o6.datatype(nodeId="ns=isa95;i=4774", browseName="TimeString", parent="i=12")
class TimeString:
    pass


@o6.datatype(nodeId="ns=isa95;i=4775", browseName="DurationString", parent="i=12")
class DurationString:
    pass


@o6.datatype(nodeId="ns=isa95;i=4776", browseName="CurrencyCode", defaultEncodingId="ns=isa95;i=4788")
class CurrencyCode(ns0.datatypes.Structure):
    namespaceUri: o6.String
    unitId: o6.Int32
    charId: list[o6.Byte]
    displayName: o6.LocalizedText
    description: o6.LocalizedText


@o6.datatype(nodeId="ns=isa95;i=4777", browseName="CDTIdentifier", parent="i=12")
class CDTIdentifier:
    pass


@o6.datatype(nodeId="ns=isa95;i=4792", browseName="CDTCode", parent="i=12")
class CDTCode:
    pass


@o6.datatype(nodeId="ns=isa95;i=4796", browseName="CDTAmountDecimal", parent="ns=isa95;i=927")
class CDTAmountDecimal:
    pass


@o6.datatype(nodeId="ns=isa95;i=4798", browseName="CDTBinaryObject", parent="i=15")
class CDTBinaryObject:
    pass


@o6.datatype(nodeId="ns=isa95;i=4803", browseName="CDTDateTime", parent="i=294")
class CDTDateTime:
    pass


@o6.datatype(nodeId="ns=isa95;i=4806", browseName="CDTGraphic", parent="i=15")
class CDTGraphic:
    pass


@o6.datatype(nodeId="ns=isa95;i=4809", browseName="CDTMeasureDecimal", parent="ns=isa95;i=927")
class CDTMeasureDecimal:
    pass


@o6.datatype(nodeId="ns=isa95;i=4811", browseName="CDTMeasureDouble", parent="i=11")
class CDTMeasureDouble:
    pass


@o6.datatype(nodeId="ns=isa95;i=4813", browseName="CDTMeasureFloat", parent="i=10")
class CDTMeasureFloat:
    pass


@o6.datatype(nodeId="ns=isa95;i=4815", browseName="CDTMeasureInt16", parent="i=4")
class CDTMeasureInt16:
    pass


@o6.datatype(nodeId="ns=isa95;i=4817", browseName="CDTMeasureInt32", parent="i=6")
class CDTMeasureInt32:
    pass


@o6.datatype(nodeId="ns=isa95;i=4819", browseName="CDTMeasureInt64", parent="i=8")
class CDTMeasureInt64:
    pass


@o6.datatype(nodeId="ns=isa95;i=4821", browseName="CDTOrdinal", parent="i=6")
class CDTOrdinal:
    pass


@o6.datatype(nodeId="ns=isa95;i=4822", browseName="CDTPicture", parent="i=30")
class CDTPicture:
    pass


@o6.datatype(nodeId="ns=isa95;i=4825", browseName="CDTRateDecimal", parent="ns=isa95;i=927")
class CDTRateDecimal:
    pass


@o6.datatype(nodeId="ns=isa95;i=4832", browseName="CDTRateDouble", parent="i=11")
class CDTRateDouble:
    pass


@o6.datatype(nodeId="ns=isa95;i=4839", browseName="CDTRateFloat", parent="i=10")
class CDTRateFloat:
    pass


@o6.datatype(nodeId="ns=isa95;i=4846", browseName="CDTRateInt32", parent="i=6")
class CDTRateInt32:
    pass


@o6.datatype(nodeId="ns=isa95;i=4853", browseName="CDTSound", parent="i=15")
class CDTSound:
    pass


@o6.datatype(nodeId="ns=isa95;i=4856", browseName="CDTVideo", parent="i=15")
class CDTVideo:
    pass


@o6.datatype(nodeId="ns=isa95;i=4862", browseName="ISA95TestResultMeasurementDataType", defaultEncodingId="ns=isa95;i=4867")
class ISA95TestResultMeasurementDataType(ns0.datatypes.Structure):
    id: o6.NodeId
    testResultDescription: o6.LocalizedText
    date: o6.DateTime
    result: Any
    resultUnitOfMeasure: ns0.datatypes.EUInformation
    expiration: o6.DateTime


@o6.enumtype(nodeId="ns=isa95;i=4871", browseName="ISA95EquipmentElementLevelEnum")
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


@o6.datatype(nodeId="ns=isa95;i=4873", browseName="ISA95TestResultDataType", defaultEncodingId="ns=isa95;i=4902")
class ISA95TestResultDataType(ns0.datatypes.Structure):
    id: o6.NodeId
    testResultDescription: o6.LocalizedText
    date: o6.DateTime
    result: Any
    resultUnitOfMeasure: o6.String
    expiration: o6.DateTime


@o6.datatype(nodeId="ns=isa95;i=4929", browseName="NormalizedString", parent="i=12")
class NormalizedString:
    pass


@o6.datatype(nodeId="ns=isa95;i=4956", browseName="ISA95AssetAssignmentDataType", defaultEncodingId="ns=isa95;i=4973")
class ISA95AssetAssignmentDataType(ns0.datatypes.Structure):
    id: o6.NodeId
    assinmentDescription: o6.LocalizedText
    startTime: o6.DateTime
    endTime: o6.DateTime


del Any, TYPE_CHECKING, uuid, o6, ns0, isa95_reftypes
