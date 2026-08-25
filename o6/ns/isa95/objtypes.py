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
from . import vartypes as isa95_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=isa95;i=4957",
    browseName="ns=isa95;ISA95ClassType",
    displayName="ISA95ClassType",
    description="This abstract ObjectType is used to define groupings of functionality that is associated with an ISA95Object",
    isAbstract=True,
)
class ISA95ClassType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(nodeId="ns=isa95;i=4958", browseName="ns=isa95;ISA95ObjectType", displayName="ISA95ObjectType", description="This abstract ObjectType", isAbstract=True)
class ISA95ObjectType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(
    nodeId="ns=isa95;i=4959",
    browseName="ns=isa95;ISA95TestSpecificationType",
    displayName="ISA95TestSpecificationType",
    description="This ObjectType indicates the existence of a test specification.",
    isAbstract=True,
)
class ISA95TestSpecificationType(ns0.objtypes.BaseObjectType):
    version: ns0.vartypes.BaseDataVariableType = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=4960", browseName="ns=isa95;Version", dataType=o6.String, accessLevel=3), "ns=isa95;i=4713"
    )


@o6.objecttype(
    nodeId="ns=isa95;i=4977",
    browseName="ns=isa95;QualificationTestSpecificationType",
    displayName="QualificationTestSpecificationType",
    description="This ObjectType indicates the existence of a test specification.",
)
class QualificationTestSpecificationType(ISA95TestSpecificationType):
    pass


@o6.objecttype(
    nodeId="ns=isa95;i=4996",
    browseName="ns=isa95;PersonnelClassType",
    displayName="PersonnelClassType",
    description="This ObjectType indicates a grouping of persons with similar characteristics for a definite purpose such as manufacturing operations definition, scheduling, capability and performance",
)
class PersonnelClassType(ISA95ClassType):
    langlePropertyNameRangle: isa95_vartypes.PersonnelClassPropertyType | None = o6.reference(
        isa95_vartypes.PersonnelClassPropertyType(nodeId="ns=isa95;i=4997", browseName="ns=isa95;<PropertyName>", modellingRule="OptionalPlaceholder"), "ns=isa95;i=4910"
    )


@o6.objecttype(
    nodeId="ns=isa95;i=5015",
    browseName="ns=isa95;EquipmentCapabilityTestSpecificationType",
    displayName="EquipmentCapabilityTestSpecificationType",
    description="This ObjectType indicates the existence of a test specification.",
)
class EquipmentCapabilityTestSpecificationType(ISA95TestSpecificationType):
    pass


@o6.objecttype(
    nodeId="ns=isa95;i=5034",
    browseName="ns=isa95;EquipmentClassType",
    displayName="EquipmentClassType",
    description="This ObjectType indicates a grouping of equipment with similar characteristics for a definite purpose such as manufacturing operations definition, scheduling, capability and performance",
)
class EquipmentClassType(ISA95ClassType):
    equipmentLevel: ns0.vartypes.PropertyType | None = o6.reference(
        ns0.vartypes.PropertyType(nodeId="ns=isa95;i=5039", browseName="ns=isa95;EquipmentLevel", dataType=isa95_datypes.ISA95EquipmentElementLevelEnum), "ns=isa95;i=4713"
    )
    langlePropertyNameRangle: isa95_vartypes.EquipmentClassPropertyType | None = o6.reference(
        isa95_vartypes.EquipmentClassPropertyType(nodeId="ns=isa95;i=5035", browseName="ns=isa95;<PropertyName>", modellingRule="OptionalPlaceholder"), "ns=isa95;i=4910"
    )


@o6.objecttype(nodeId="ns=isa95;i=5040", browseName="ns=isa95;EquipmentType", displayName="EquipmentType", description="This ObjectType defines a piece of equipment")
class EquipmentType(ISA95ObjectType):
    assetAssignment: isa95_vartypes.ISA95AssetAssignmentType | None
    equipmentLevel: ns0.vartypes.PropertyType | None = o6.reference(
        ns0.vartypes.PropertyType(nodeId="ns=isa95;i=5047", browseName="ns=isa95;EquipmentLevel", dataType=isa95_datypes.ISA95EquipmentElementLevelEnum), "ns=isa95;i=4713"
    )
    langleEquipmentRangle: EquipmentType | None
    langlePropertyNameRangle: isa95_vartypes.EquipmentPropertyType | None = o6.reference(
        isa95_vartypes.EquipmentPropertyType(nodeId="ns=isa95;i=5041", browseName="ns=isa95;<PropertyName>", modellingRule="OptionalPlaceholder"), "ns=isa95;i=4910"
    )


@o6.objecttype(
    nodeId="ns=isa95;i=5057",
    browseName="ns=isa95;PhysicalAssetCapabilityTestSpecificationType",
    displayName="PhysicalAssetCapabilityTestSpecificationType",
    description="This ObjectType indicates the existence of a test specification.",
)
class PhysicalAssetCapabilityTestSpecificationType(ISA95TestSpecificationType):
    pass


@o6.objecttype(
    nodeId="ns=isa95;i=5078",
    browseName="ns=isa95;PhysicalAssetClassType",
    displayName="PhysicalAssetClassType",
    description="This ObjectType indicates a grouping of equipment with similar characteristics for a definite purpose such as manufacturing operations definition, scheduling, capability and performance",
)
class PhysicalAssetClassType(ISA95ClassType):
    langlePropertyNameRangle: isa95_vartypes.PhysicalAssetClassPropertyType | None = o6.reference(
        isa95_vartypes.PhysicalAssetClassPropertyType(nodeId="ns=isa95;i=5079", browseName="ns=isa95;<PropertyName>", modellingRule="OptionalPlaceholder"), "ns=isa95;i=4910"
    )
    manufacturer: isa95_vartypes.CompanyType | None = o6.reference(isa95_vartypes.CompanyType(nodeId="ns=isa95;i=5083", browseName="ns=isa95;Manufacturer"), "ns=isa95;i=4713")
    modelNumber: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5084", browseName="ns=isa95;ModelNumber", dataType=o6.String), "ns=isa95;i=4713"
    )


@o6.objecttype(nodeId="ns=isa95;i=5131", browseName="ns=isa95;PersonType", displayName="PersonType", description="This ObjectType indicates a specifically identified individual")
class PersonType(ISA95ObjectType):
    langlePropertyNameRangle: isa95_vartypes.PersonPropertyType | None = o6.reference(
        isa95_vartypes.PersonPropertyType(nodeId="ns=isa95;i=5132", browseName="ns=isa95;<PropertyName>", modellingRule="OptionalPlaceholder"), "ns=isa95;i=2009"
    )


@o6.objecttype(nodeId="ns=isa95;i=5085", browseName="ns=isa95;PhysicalAssetType", displayName="PhysicalAssetType", description="This ObjectType defines a piece of equipment")
class PhysicalAssetType(ISA95ObjectType):
    assetAssignment: isa95_vartypes.ISA95AssetAssignmentType | None
    fixedAssetId: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5153", browseName="ns=isa95;FixedAssetId", dataType=isa95_datypes.CDTIdentifier), "ns=isa95;i=4713"
    )
    langlePhysicalAssetRangle: PhysicalAssetType | None
    langlePropertyNameRangle: isa95_vartypes.PhysicalAssetPropertyType | None = o6.reference(
        isa95_vartypes.PhysicalAssetPropertyType(nodeId="ns=isa95;i=5086", browseName="ns=isa95;<PropertyName>", modellingRule="OptionalPlaceholder"), "ns=isa95;i=2009"
    )
    physicalLocation: isa95_vartypes.GeoSpatialLocationType | None = o6.reference(
        isa95_vartypes.GeoSpatialLocationType(nodeId="ns=isa95;i=5138", browseName="ns=isa95;PhysicalLocation", dataType=o6.String), "ns=isa95;i=5114"
    )
    vendorId: isa95_vartypes.CompanyType | None = o6.reference(isa95_vartypes.CompanyType(nodeId="ns=isa95;i=5154", browseName="ns=isa95;VendorId"), "ns=isa95;i=4713")


@o6.objecttype(
    nodeId="ns=isa95;i=5172",
    browseName="ns=isa95;MaterialTestSpecificationType",
    displayName="MaterialTestSpecificationType",
    description="This ObjectType indicates the existence of a test specification.",
)
class MaterialTestSpecificationType(ISA95TestSpecificationType):
    pass


@o6.objecttype(nodeId="ns=isa95;i=5209", browseName="ns=isa95;MaterialClassType", displayName="MaterialClassType")
class MaterialClassType(ISA95ClassType):
    assemblyRelationship: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5218", browseName="ns=isa95;AssemblyRelationship"), "ns=isa95;i=4713"
    )
    assemblyType: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5217", browseName="ns=isa95;AssemblyType"), "ns=isa95;i=4713"
    )
    langleAssemblyClassRangle: MaterialClassType | None
    langlePropertyNameRangle: isa95_vartypes.MaterialClassPropertyType | None = o6.reference(
        isa95_vartypes.MaterialClassPropertyType(nodeId="ns=isa95;i=5210", browseName="ns=isa95;<PropertyName>", modellingRule="OptionalPlaceholder"), "ns=isa95;i=4910"
    )


@o6.objecttype(nodeId="ns=isa95;i=5219", browseName="ns=isa95;MaterialDefinitionType", displayName="MaterialDefinitionType")
class MaterialDefinitionType(ISA95ClassType):
    assemblyRelationship: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5231", browseName="ns=isa95;AssemblyRelationship"), "ns=isa95;i=4713"
    )
    assemblyType: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5230", browseName="ns=isa95;AssemblyType"), "ns=isa95;i=4713"
    )
    langleAssemblyClassRangle: MaterialDefinitionType | None
    langlePropertyNameRangle: isa95_vartypes.MaterialDefinitionPropertyType | None = o6.reference(
        isa95_vartypes.MaterialDefinitionPropertyType(nodeId="ns=isa95;i=5220", browseName="ns=isa95;<PropertyName>", modellingRule="OptionalPlaceholder"), "ns=isa95;i=4910"
    )


@o6.objecttype(nodeId="ns=isa95;i=5232", browseName="ns=isa95;MaterialLotType", displayName="MaterialLotType")
class MaterialLotType(ISA95ObjectType):
    assemblyRelationship: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5255", browseName="ns=isa95;AssemblyRelationship"), "ns=isa95;i=4713"
    )
    assemblyType: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5254", browseName="ns=isa95;AssemblyType"), "ns=isa95;i=4713"
    )
    langleAssemblyLotRangle: MaterialLotType | None
    langlePropertyNameRangle: isa95_vartypes.MaterialLotPropertyType | None
    quantity: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5258", browseName="ns=isa95;Quantity"), "ns=isa95;i=4713"
    )
    status: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5256", browseName="ns=isa95;Status", dataType=isa95_datypes.CDTIdentifier), "ns=isa95;i=4713"
    )
    storageLocation: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5257", browseName="ns=isa95;StorageLocation", dataType=isa95_datypes.CDTIdentifier), "ns=isa95;i=4713"
    )


@o6.objecttype(nodeId="ns=isa95;i=5259", browseName="ns=isa95;MaterialSublotType", displayName="MaterialSublotType")
class MaterialSublotType(ISA95ObjectType):
    assemblyRelationship: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5285", browseName="ns=isa95;AssemblyRelationship"), "ns=isa95;i=4713"
    )
    assemblyType: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5284", browseName="ns=isa95;AssemblyType"), "ns=isa95;i=4713"
    )
    langleAssemblyLotRangle: MaterialLotType | None = o6.reference(
        MaterialLotType(nodeId="ns=isa95;i=5269", browseName="ns=isa95;<AssemblyLot>", modellingRule="OptionalPlaceholder"), "ns=isa95;i=4928"
    )
    langlePropertyNameRangle: isa95_vartypes.MaterialLotPropertyType | None
    langleSublotRangle: MaterialSublotType | None
    quantity: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5294", browseName="ns=isa95;Quantity"), "ns=isa95;i=4713"
    )
    status: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5292", browseName="ns=isa95;Status", dataType=isa95_datypes.CDTIdentifier), "ns=isa95;i=4713"
    )
    storageLocation: ns0.vartypes.BaseDataVariableType | None = o6.reference(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=isa95;i=5293", browseName="ns=isa95;StorageLocation", dataType=isa95_datypes.CDTIdentifier), "ns=isa95;i=4713"
    )


del Any, TYPE_CHECKING, uuid, o6, ns0, isa95_reftypes, isa95_datypes, isa95_vartypes
