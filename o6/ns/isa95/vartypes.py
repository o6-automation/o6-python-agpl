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
from . import datatypes as isa95_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.variabletype(nodeId="ns=isa95;i=4878", browseName="ns=isa95;ISA95TestResultType", displayName="ISA95TestResultType", valueRank=o6.ValueRank.ANY)
class ISA95TestResultType(ns0.vartypes.BaseDataVariableType):
    expiration: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=4884", browseName="ns=isa95;Expiration", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"
    )
    id: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=4879", browseName="ns=isa95;Id", dataType=o6.NodeId, accessLevel=3), "ns=isa95;i=4713"
    )
    result: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=4882", browseName="ns=isa95;Result", accessLevel=3), "ns=isa95;i=4713"
    )
    resultDescription: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=4880", browseName="ns=isa95;ResultDescription", dataType=o6.LocalizedText, accessLevel=3), "ns=isa95;i=4713"
    )
    resultUnitOfMeasure: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=4883", browseName="ns=isa95;ResultUnitOfMeasure", accessLevel=3), "ns=isa95;i=4713"
    )
    testDate: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=4881", browseName="ns=isa95;TestDate", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"
    )


@o6.variabletype(
    nodeId="ns=isa95;i=4885",
    browseName="ns=isa95;ISA95ClassPropertyType",
    displayName="ISA95ClassPropertyType",
    description="This VariableType is used to define an ISA95ClassProperty for an ISA95Class",
    isAbstract=True,
    valueRank=o6.ValueRank.ANY,
)
class ISA95ClassPropertyType(ns0.vartypes.BaseDataVariableType):
    key: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=4886", browseName="ns=isa95;Key", dataType=isa95_datypes.CDTIdentifier, accessLevel=3), "ns=isa95;i=4713"
    )


@o6.variabletype(
    nodeId="ns=isa95;i=1123",
    browseName="ns=isa95;PersonnelClassPropertyType",
    displayName="PersonnelClassPropertyType",
    description="This VariableType indicates ISA95ClassProperties for PersonnelClass.",
)
class PersonnelClassPropertyType(ISA95ClassPropertyType):
    langlePropertyNameRangle: PersonnelClassPropertyType | None


@o6.variabletype(
    nodeId="ns=isa95;i=4263",
    browseName="ns=isa95;ISA95PropertyType",
    displayName="ISA95PropertyType",
    description="This VariableType is used to define an ISA95Property for an ISA95Object",
    isAbstract=True,
    valueRank=o6.ValueRank.ANY,
)
class ISA95PropertyType(ns0.vartypes.BaseDataVariableType):
    key: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=4887", browseName="ns=isa95;Key", dataType=isa95_datypes.CDTIdentifier, accessLevel=3), "ns=isa95;i=4713"
    )


@o6.variabletype(nodeId="ns=isa95;i=954", browseName="ns=isa95;EquipmentPropertyType", displayName="EquipmentPropertyType")
class EquipmentPropertyType(ISA95PropertyType):
    langlePropertyNameRangle: EquipmentPropertyType | None
    langleTestResultRangle: EquipmentCapabilityTestResultType | None


@o6.variabletype(
    nodeId="ns=isa95;i=4961",
    browseName="ns=isa95;QualificationTestResultType",
    displayName="QualificationTestResultType",
    dataType=ns0.datatypes.Structure,
    valueRank=o6.ValueRank.ANY,
)
class QualificationTestResultType(ISA95TestResultType):
    pass


@o6.variabletype(
    nodeId="ns=isa95;i=5008",
    browseName="ns=isa95;EquipmentCapabilityTestResultType",
    displayName="EquipmentCapabilityTestResultType",
    dataType=ns0.datatypes.Structure,
    valueRank=o6.ValueRank.ANY,
)
class EquipmentCapabilityTestResultType(ISA95TestResultType):
    pass


@o6.variabletype(nodeId="ns=isa95;i=5017", browseName="ns=isa95;EquipmentClassPropertyType", displayName="EquipmentClassPropertyType")
class EquipmentClassPropertyType(ISA95ClassPropertyType):
    langlePropertyNameRangle: EquipmentClassPropertyType | None


@o6.variabletype(
    nodeId="ns=isa95;i=5048",
    browseName="ns=isa95;GeoSpatialLocationType",
    displayName="GeoSpatialLocationType",
    description="This VariableType is used to provide details regarding Physical Location information for PhysicalAssetClassType",
    dataType=o6.String,
    valueRank=o6.ValueRank.ANY,
)
class GeoSpatialLocationType(ns0.vartypes.PropertyType):
    pass


@o6.variabletype(
    nodeId="ns=isa95;i=5049",
    browseName="ns=isa95;CompanyType",
    displayName="CompanyType",
    description="This VariableType is used to provide details regarding company information for PhysicalAssetClassTypes or for instances of PhysicalAssetType",
    valueRank=o6.ValueRank.ANY,
)
class CompanyType(ns0.vartypes.BaseDataVariableType):
    pass


@o6.variabletype(
    nodeId="ns=isa95;i=5050",
    browseName="ns=isa95;PhysicalAssetCapabilityTestResultType",
    displayName="PhysicalAssetCapabilityTestResultType",
    description="This VariableType indicates the results from a physical asset capability test for a specific physical asset.",
    dataType=ns0.datatypes.Structure,
    valueRank=o6.ValueRank.ANY,
)
class PhysicalAssetCapabilityTestResultType(ISA95TestResultType):
    pass


@o6.variabletype(
    nodeId="ns=isa95;i=5059",
    browseName="ns=isa95;PhysicalAssetClassPropertyType",
    displayName="PhysicalAssetClassPropertyType",
    description="This VariableType indicates ISA95ClassProperties for a PhysicalAssetClassType",
)
class PhysicalAssetClassPropertyType(ISA95ClassPropertyType):
    langlePropertyNameRangle: PhysicalAssetClassPropertyType | None


@o6.variabletype(
    nodeId="ns=isa95;i=5065",
    browseName="ns=isa95;PhysicalAssetPropertyType",
    displayName="PhysicalAssetPropertyType",
    description="This VariableType indicates ISA95Properties of a role based equipment.",
)
class PhysicalAssetPropertyType(ISA95ClassPropertyType):
    langlePropertyNameRangle: PhysicalAssetPropertyType | None
    langleTestResultRangle: PhysicalAssetCapabilityTestResultType | None


@o6.variabletype(
    nodeId="ns=isa95;i=5094",
    browseName="ns=isa95;ISA95TestResultNonEUType",
    displayName="ISA95TestResultNonEUType",
    dataType=isa95_datypes.ISA95TestResultDataType,
    valueRank=o6.ValueRank.ANY,
)
class ISA95TestResultNonEUType(ISA95TestResultType):
    resultUnitOfMeasure: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5099", browseName="ns=isa95;ResultUnitOfMeasure", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713"
    )


@o6.variabletype(
    nodeId="ns=isa95;i=5101",
    browseName="ns=isa95;ISA95TestResultEUType",
    displayName="ISA95TestResultEUType",
    dataType=isa95_datypes.ISA95TestResultMeasurementDataType,
    valueRank=o6.ValueRank.ANY,
)
class ISA95TestResultEUType(ISA95TestResultType):
    resultUnitOfMeasure: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5106", browseName="ns=isa95;ResultUnitOfMeasure", dataType=ns0.datatypes.EUInformation, accessLevel=3),
        "ns=isa95;i=4713",
    )


@o6.variabletype(nodeId="ns=isa95;i=5108", browseName="ns=isa95;ISA95AssetAssignmentType", displayName="ISA95AssetAssignmentType", valueRank=o6.ValueRank.ANY)
class ISA95AssetAssignmentType(ns0.vartypes.BaseDataVariableType):
    assignmentDescription: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5110", browseName="ns=isa95;AssignmentDescription", dataType=o6.LocalizedText, accessLevel=3), "ns=isa95;i=4713"
    )
    id: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5109", browseName="ns=isa95;Id", dataType=o6.NodeId, accessLevel=3), "ns=isa95;i=4713"
    )
    startTime: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5111", browseName="ns=isa95;StartTime", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"
    )
    stopTime: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5112", browseName="ns=isa95;StopTime", dataType=o6.DateTime, accessLevel=3), "ns=isa95;i=4713"
    )


@o6.variabletype(
    nodeId="ns=isa95;i=5118", browseName="ns=isa95;PersonPropertyType", displayName="PersonPropertyType", description="This VariableType indicates ISA95Properties of a person"
)
class PersonPropertyType(ISA95PropertyType):
    langlePropertyNameRangle: PersonPropertyType | None
    langleTestResultRangle: QualificationTestResultType | None


@o6.variabletype(
    nodeId="ns=isa95;i=5165",
    browseName="ns=isa95;MaterialTestResultType",
    displayName="MaterialTestResultType",
    description="This VariableType indicates the results from executing an instance of a MaterialTestSpecificationType for a specific MaterialLotType",
    dataType=ns0.datatypes.Structure,
    valueRank=o6.ValueRank.ANY,
)
class MaterialTestResultType(ISA95TestResultType):
    pass


@o6.variabletype(nodeId="ns=isa95;i=5174", browseName="ns=isa95;MaterialDefinitionPropertyType", displayName="MaterialDefinitionPropertyType")
class MaterialDefinitionPropertyType(ISA95ClassPropertyType):
    langlePropertyNameRangle: MaterialDefinitionPropertyType | None


@o6.variabletype(nodeId="ns=isa95;i=5180", browseName="ns=isa95;MaterialClassPropertyType", displayName="MaterialClassPropertyType")
class MaterialClassPropertyType(ISA95ClassPropertyType):
    langlePropertyNameRangle: MaterialClassPropertyType | None


@o6.variabletype(nodeId="ns=isa95;i=5186", browseName="ns=isa95;MaterialLotPropertyType", displayName="MaterialLotPropertyType", dataType=ns0.datatypes.Structure)
class MaterialLotPropertyType(MaterialTestResultType):
    langlePropertyNameRangle: MaterialLotPropertyType | None
    langleTestResultRangle: MaterialLotPropertyType | None


del Any, TYPE_CHECKING, uuid, o6, ns0, isa95_reftypes, isa95_datypes
