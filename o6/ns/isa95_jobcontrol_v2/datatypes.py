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

"""Generated OPC UA isa95_jobcontrol_v2 namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(
    nodeId="ns=isa95_jobcontrol_v2;i=3002",
    browseName="ns=isa95_jobcontrol_v2;ISA95PropertyDataType",
    description="A subtype of OPC UA Structure that defines two linked data items: an ID, which is a unique identifier for a property within the scope of the associated resource, and the value, which is the data for the property.",
    defaultEncodingId="ns=isa95_jobcontrol_v2;i=5002",
)
class ISA95PropertyDataType(ns0.datatypes.Structure):
    iD: o6.String = o6.field(name="ID")
    value: Any = o6.field(name="Value")
    description: list[o6.LocalizedText] | None = o6.field(name="Description", arrayDimensions=[0])
    engineeringUnits: ns0.datatypes.EUInformation | None = o6.field(name="EngineeringUnits")
    subproperties: list[ISA95PropertyDataType] | None = o6.field(name="Subproperties", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=isa95_jobcontrol_v2;i=3003",
    browseName="ns=isa95_jobcontrol_v2;ISA95ParameterDataType",
    description="A subtype of OPC UA Structure that defines three linked data items: the ID, which is a unique identifier for a property, the value, which is the data that is identified, and an optional description of the parameter.",
    defaultEncodingId="ns=isa95_jobcontrol_v2;i=5005",
)
class ISA95ParameterDataType(ns0.datatypes.Structure):
    iD: o6.String = o6.field(name="ID")
    value: Any = o6.field(name="Value")
    description: list[o6.LocalizedText] | None = o6.field(name="Description", arrayDimensions=[0])
    engineeringUnits: ns0.datatypes.EUInformation | None = o6.field(name="EngineeringUnits")
    subparameters: list[ISA95ParameterDataType] | None = o6.field(name="Subparameters", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=isa95_jobcontrol_v2;i=3005",
    browseName="ns=isa95_jobcontrol_v2;ISA95EquipmentDataType",
    description="Defines an equipment resource or a piece of equipment, a quantity, an optional description, and an optional collection of properties.",
    defaultEncodingId="ns=isa95_jobcontrol_v2;i=5008",
)
class ISA95EquipmentDataType(ns0.datatypes.Structure):
    iD: o6.String = o6.field(name="ID")
    description: list[o6.LocalizedText] | None = o6.field(name="Description", arrayDimensions=[0])
    equipmentUse: o6.String | None = o6.field(name="EquipmentUse")
    quantity: o6.String | None = o6.field(name="Quantity")
    engineeringUnits: ns0.datatypes.EUInformation | None = o6.field(name="EngineeringUnits")
    properties: list[ISA95PropertyDataType] | None = o6.field(name="Properties", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=isa95_jobcontrol_v2;i=3006",
    browseName="ns=isa95_jobcontrol_v2;ISA95StateDataType",
    description="Defines the information needed to schedule and execute a job.",
    defaultEncodingId="ns=isa95_jobcontrol_v2;i=5029",
)
class ISA95StateDataType(ns0.datatypes.Structure):
    browsePath: ns0.datatypes.RelativePath = o6.field(name="BrowsePath")
    stateText: o6.LocalizedText = o6.field(name="StateText")
    stateNumber: o6.UInt32 = o6.field(name="StateNumber")


@o6.datatype(
    nodeId="ns=isa95_jobcontrol_v2;i=3007",
    browseName="ns=isa95_jobcontrol_v2;ISA95WorkMasterDataType",
    description="Defines a Work Master ID and the defined parameters for the Work Master.",
    defaultEncodingId="ns=isa95_jobcontrol_v2;i=5011",
)
class ISA95WorkMasterDataType(ns0.datatypes.Structure):
    iD: o6.String = o6.field(name="ID")
    description: o6.LocalizedText | None = o6.field(name="Description")
    parameters: list[ISA95ParameterDataType] | None = o6.field(name="Parameters", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=isa95_jobcontrol_v2;i=3010",
    browseName="ns=isa95_jobcontrol_v2;ISA95MaterialDataType",
    description="Defines a material resource, a quantity, an optional description, and an optional collection of properties.",
    defaultEncodingId="ns=isa95_jobcontrol_v2;i=5017",
)
class ISA95MaterialDataType(ns0.datatypes.Structure):
    materialClassID: o6.String | None = o6.field(name="MaterialClassID")
    materialDefinitionID: o6.String | None = o6.field(name="MaterialDefinitionID")
    materialLotID: o6.String | None = o6.field(name="MaterialLotID")
    materialSublotID: o6.String | None = o6.field(name="MaterialSublotID")
    description: list[o6.LocalizedText] | None = o6.field(name="Description", arrayDimensions=[0])
    materialUse: o6.String | None = o6.field(name="MaterialUse")
    quantity: o6.String | None = o6.field(name="Quantity")
    engineeringUnits: ns0.datatypes.EUInformation | None = o6.field(name="EngineeringUnits")
    properties: list[ISA95PropertyDataType] | None = o6.field(name="Properties", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=isa95_jobcontrol_v2;i=3011",
    browseName="ns=isa95_jobcontrol_v2;ISA95PersonnelDataType",
    description="Defines a personnel resource or a person, a quantity, an optional description, and an optional collection of properties.",
    defaultEncodingId="ns=isa95_jobcontrol_v2;i=5020",
)
class ISA95PersonnelDataType(ns0.datatypes.Structure):
    iD: o6.String = o6.field(name="ID")
    description: list[o6.LocalizedText] | None = o6.field(name="Description", arrayDimensions=[0])
    personnelUse: o6.String | None = o6.field(name="PersonnelUse")
    quantity: o6.String | None = o6.field(name="Quantity")
    engineeringUnits: ns0.datatypes.EUInformation | None = o6.field(name="EngineeringUnits")
    properties: list[ISA95PropertyDataType] | None = o6.field(name="Properties", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=isa95_jobcontrol_v2;i=3012",
    browseName="ns=isa95_jobcontrol_v2;ISA95PhysicalAssetDataType",
    description="Defines a physical asset, a quantity, an optional description, and an optional collection of properties.",
    defaultEncodingId="ns=isa95_jobcontrol_v2;i=5023",
)
class ISA95PhysicalAssetDataType(ns0.datatypes.Structure):
    iD: o6.String = o6.field(name="ID")
    description: list[o6.LocalizedText] | None = o6.field(name="Description", arrayDimensions=[0])
    physicalAssetUse: o6.String | None = o6.field(name="PhysicalAssetUse")
    quantity: o6.String | None = o6.field(name="Quantity")
    engineeringUnits: ns0.datatypes.EUInformation | None = o6.field(name="EngineeringUnits")
    properties: list[ISA95PropertyDataType] | None = o6.field(name="Properties", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=isa95_jobcontrol_v2;i=3008",
    browseName="ns=isa95_jobcontrol_v2;ISA95JobOrderDataType",
    description="Defines the information needed to schedule and execute a job.",
    defaultEncodingId="ns=isa95_jobcontrol_v2;i=5014",
)
class ISA95JobOrderDataType(ns0.datatypes.Structure):
    jobOrderID: o6.String = o6.field(name="JobOrderID")
    description: list[o6.LocalizedText] | None = o6.field(name="Description", arrayDimensions=[0])
    workMasterID: list[ISA95WorkMasterDataType] | None = o6.field(name="WorkMasterID", arrayDimensions=[0])
    startTime: o6.DateTime | None = o6.field(name="StartTime")
    endTime: o6.DateTime | None = o6.field(name="EndTime")
    priority: o6.Int16 | None = o6.field(name="Priority")
    jobOrderParameters: list[ISA95ParameterDataType] | None = o6.field(name="JobOrderParameters", arrayDimensions=[0])
    personnelRequirements: list[ISA95PersonnelDataType] | None = o6.field(name="PersonnelRequirements", arrayDimensions=[0])
    equipmentRequirements: list[ISA95EquipmentDataType] | None = o6.field(name="EquipmentRequirements", arrayDimensions=[0])
    physicalAssetRequirements: list[ISA95PhysicalAssetDataType] | None = o6.field(name="PhysicalAssetRequirements", arrayDimensions=[0])
    materialRequirements: list[ISA95MaterialDataType] | None = o6.field(name="MaterialRequirements", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=isa95_jobcontrol_v2;i=3013",
    browseName="ns=isa95_jobcontrol_v2;ISA95JobResponseDataType",
    description="Defines the information needed to schedule and execute a job.",
    defaultEncodingId="ns=isa95_jobcontrol_v2;i=5026",
)
class ISA95JobResponseDataType(ns0.datatypes.Structure):
    jobResponseID: o6.String = o6.field(name="JobResponseID")
    description: o6.LocalizedText | None = o6.field(name="Description")
    jobOrderID: o6.String = o6.field(name="JobOrderID")
    startTime: o6.DateTime | None = o6.field(name="StartTime")
    endTime: o6.DateTime | None = o6.field(name="EndTime")
    jobState: list[ISA95StateDataType] = o6.field(name="JobState", arrayDimensions=[0])
    jobResponseData: list[ISA95ParameterDataType] | None = o6.field(name="JobResponseData", arrayDimensions=[0])
    personnelActuals: list[ISA95PersonnelDataType] | None = o6.field(name="PersonnelActuals", arrayDimensions=[0])
    equipmentActuals: list[ISA95EquipmentDataType] | None = o6.field(name="EquipmentActuals", arrayDimensions=[0])
    physicalAssetActuals: list[ISA95PhysicalAssetDataType] | None = o6.field(name="PhysicalAssetActuals", arrayDimensions=[0])
    materialActuals: list[ISA95MaterialDataType] | None = o6.field(name="MaterialActuals", arrayDimensions=[0])


@o6.datatype(
    nodeId="ns=isa95_jobcontrol_v2;i=3015",
    browseName="ns=isa95_jobcontrol_v2;ISA95JobOrderAndStateDataType",
    description="Defines the information needed to schedule and execute a job.",
    defaultEncodingId="ns=isa95_jobcontrol_v2;i=5032",
)
class ISA95JobOrderAndStateDataType(ns0.datatypes.Structure):
    jobOrder: ISA95JobOrderDataType = o6.field(name="JobOrder")
    state: list[ISA95StateDataType] = o6.field(name="State", arrayDimensions=[0])


del Any, TYPE_CHECKING, uuid, o6, ns0
