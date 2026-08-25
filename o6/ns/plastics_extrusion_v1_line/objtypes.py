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

"""Generated OPC UA plastics_extrusion_v1_line namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_extrusion_v1_line_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_line;i=1002", browseName="ns=plastics_extrusion_v1_line;ProductionParametersType", displayName="ProductionParametersType")
class ProductionParametersType(ns0.objtypes.BaseObjectType):
    electricalEnergy: plastics_rubber.objtypes.EnergyType | None
    fluidEnergy: plastics_rubber.objtypes.EnergyType | None
    goodProduct: ns0.vartypes.BaseDataVariableType = o6.hasComponent(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6001", browseName="ns=plastics_extrusion_v1_line;GoodProduct", dataType=o6.Boolean)
    )
    lineSpeed: ns0.vartypes.AnalogUnitType | None
    pressureAir: plastics_rubber.objtypes.EnergyType | None
    productWeight: ns0.vartypes.AnalogUnitType | None
    throughput: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_line;i=1007", browseName="ns=plastics_extrusion_v1_line;JobType", displayName="JobType")
class JobType(ns0.objtypes.BaseObjectType):
    actualBadOutput: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6092", browseName="ns=plastics_extrusion_v1_line;ActualBadOutput", dataType=o6.Double, value=0.0)
    )
    actualGoodOutput: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6091", browseName="ns=plastics_extrusion_v1_line;ActualGoodOutput", dataType=o6.Double, value=0.0)
    )
    actualLot: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6088", browseName="ns=plastics_extrusion_v1_line;ActualLot", dataType=o6.UInt32)
    )
    actualLotName: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_extrusion_v1_line;i=6089",
            browseName="ns=plastics_extrusion_v1_line;ActualLotName",
            dataType=o6.String,
            value="\n      ",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    actualOutput: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6090", browseName="ns=plastics_extrusion_v1_line;ActualOutput", dataType=o6.Double)
    )
    actualOutputRate: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6094", browseName="ns=plastics_extrusion_v1_line;ActualOutputRate", dataType=o6.Double)
    )
    actualSampleOutput: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_extrusion_v1_line;i=6093", browseName="ns=plastics_extrusion_v1_line;ActualSampleOutput", dataType=o6.Double, value=0.0
        )
    )
    customerName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6079", browseName="ns=plastics_extrusion_v1_line;CustomerName", dataType=o6.String)
    )
    description: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6078", browseName="ns=plastics_extrusion_v1_line;Description", dataType=o6.String)
    )
    goodProduct: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=plastics_extrusion_v1_line;i=6026", browseName="ns=plastics_extrusion_v1_line;GoodProduct", dataType=o6.Boolean)
    )
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6077", browseName="ns=plastics_extrusion_v1_line;Id", dataType=o6.String, value="\n      ")
    )
    lineSpeed: ns0.vartypes.AnalogUnitType | None
    lotSize: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6086", browseName="ns=plastics_extrusion_v1_line;LotSize", dataType=o6.Double)
    )
    parameterSetting: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_line;i=6084",
            browseName="ns=plastics_extrusion_v1_line;ParameterSetting",
            dataType=plastics_rubber.datatypes.ParameterSettingType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    productDescription: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6081", browseName="ns=plastics_extrusion_v1_line;ProductDescription", dataType=o6.String)
    )
    productId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6080", browseName="ns=plastics_extrusion_v1_line;ProductId", dataType=o6.String)
    )
    productWeight: ns0.vartypes.AnalogUnitType | None
    sequence: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6083", browseName="ns=plastics_extrusion_v1_line;Sequence", dataType=o6.UInt32)
    )
    setOutput: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6085", browseName="ns=plastics_extrusion_v1_line;SetOutput", dataType=o6.Double)
    )
    status: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_line;i=6087", browseName="ns=plastics_extrusion_v1_line;Status", dataType=plastics_rubber.datatypes.JobStatusEnumeration
        )
    )
    strand: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6082", browseName="ns=plastics_extrusion_v1_line;Strand", dataType=o6.UInt32)
    )
    throughput: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=plastics_extrusion_v1_line;i=1008", browseName="ns=plastics_extrusion_v1_line;JobStatusChangedEventType", displayName="JobStatusChangedEventType", isAbstract=True
)
class JobStatusChangedEventType(ns0.objtypes.BaseEventType):
    activeStatus: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_line;i=6098",
            browseName="ns=plastics_extrusion_v1_line;ActiveStatus",
            dataType=plastics_rubber.datatypes.JobStatusEnumeration,
            value=plastics_rubber.datatypes.JobStatusEnumeration.OTHER,
        )
    )
    jobGroupId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6095", browseName="ns=plastics_extrusion_v1_line;JobGroupId", dataType=o6.String, value="\n      ")
    )
    jobId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6096", browseName="ns=plastics_extrusion_v1_line;JobId", dataType=o6.String, value="\n      ")
    )
    lastStatus: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_line;i=6097",
            browseName="ns=plastics_extrusion_v1_line;LastStatus",
            dataType=plastics_rubber.datatypes.JobStatusEnumeration,
            value=plastics_rubber.datatypes.JobStatusEnumeration.OTHER,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_extrusion_v1_line;i=1009", browseName="ns=plastics_extrusion_v1_line;UnitFinishedEventType", displayName="UnitFinishedEventType", isAbstract=True
)
class UnitFinishedEventType(ns0.objtypes.BaseEventType):
    goodProduct: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6102", browseName="ns=plastics_extrusion_v1_line;GoodProduct", dataType=o6.Boolean)
    )
    jobGroupId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6099", browseName="ns=plastics_extrusion_v1_line;JobGroupId", dataType=o6.String, value="\n      ")
    )
    jobId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6100", browseName="ns=plastics_extrusion_v1_line;JobId", dataType=o6.String, value="\n      ")
    )
    unit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6101", browseName="ns=plastics_extrusion_v1_line;Unit", dataType=o6.UInt32, value=0)
    )


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_line;i=1010", browseName="ns=plastics_extrusion_v1_line;LotFinishedEventType", displayName="LotFinishedEventType", isAbstract=True)
class LotFinishedEventType(ns0.objtypes.BaseEventType):
    jobGroupId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6103", browseName="ns=plastics_extrusion_v1_line;JobGroupId", dataType=o6.String, value="\n      ")
    )
    jobId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6104", browseName="ns=plastics_extrusion_v1_line;JobId", dataType=o6.String, value="\n      ")
    )
    lot: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6105", browseName="ns=plastics_extrusion_v1_line;Lot", dataType=o6.UInt32, value=0)
    )


@o6.objecttype(
    nodeId="ns=plastics_extrusion_v1_line;i=1006",
    browseName="ns=plastics_extrusion_v1_line;RequestAddMaterialEventType",
    displayName="RequestAddMaterialEventType",
    isAbstract=True,
)
class RequestAddMaterialEventType(ns0.objtypes.BaseEventType):
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_line;i=6142", browseName="ns=plastics_extrusion_v1_line;Id", dataType=o6.String, accessLevel=3, userAccessLevel=1
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_extrusion_v1_line;i=1012",
    browseName="ns=plastics_extrusion_v1_line;JobGroupStatusChangedEventType",
    displayName="JobGroupStatusChangedEventType",
    isAbstract=True,
)
class JobGroupStatusChangedEventType(ns0.objtypes.BaseEventType):
    activeStatus: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_line;i=6189",
            browseName="ns=plastics_extrusion_v1_line;ActiveStatus",
            dataType=plastics_rubber.datatypes.JobStatusEnumeration,
            value=plastics_rubber.datatypes.JobStatusEnumeration.OTHER,
        )
    )
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6187", browseName="ns=plastics_extrusion_v1_line;Id", dataType=o6.String, value="\n      ")
    )
    lastStatus: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_line;i=6188",
            browseName="ns=plastics_extrusion_v1_line;LastStatus",
            dataType=plastics_rubber.datatypes.JobStatusEnumeration,
            value=plastics_rubber.datatypes.JobStatusEnumeration.OTHER,
        )
    )


ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6190", browseName="NodeVersion", dataType=o6.String, value="\n      ")
o6.reference(o6.ns["ns=plastics_extrusion_v1_line;i=6190"], "i=41", JobStatusChangedEventType)
o6.reference(o6.ns["ns=plastics_extrusion_v1_line;i=6190"], "i=41", UnitFinishedEventType)
o6.reference(o6.ns["ns=plastics_extrusion_v1_line;i=6190"], "i=41", LotFinishedEventType)
o6.reference(o6.ns["ns=plastics_extrusion_v1_line;i=6190"], "i=41", JobGroupStatusChangedEventType)


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6057",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7004",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Message", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Message2", dataType=o6.UInt16, valueRank=-1),
    ],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7004", browseName="ns=plastics_extrusion_v1_line;SetMESMessage", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6057"])
)


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_line;i=1003", browseName="ns=plastics_extrusion_v1_line;ExtrusionLine_InterfaceType", displayName="ExtrusionLine_InterfaceType")
class ExtrusionLine_InterfaceType(ns0.objtypes.BaseObjectType):
    clearMESMessage: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=plastics_extrusion_v1_line;i=7005", browseName="ns=plastics_extrusion_v1_line;ClearMESMessage"))
    configurationParameters: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_line;i=6165",
            browseName="ns=plastics_extrusion_v1_line;ConfigurationParameters",
            dataType=plastics_rubber.datatypes.ConfigurationParameterType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    jobGroups: JobGroupsType | None
    lineId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_line;i=6031", browseName="ns=plastics_extrusion_v1_line;LineId", dataType=o6.String, accessLevel=3, userAccessLevel=1
        )
    )
    lineStatus: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_line;i=6058",
            browseName="ns=plastics_extrusion_v1_line;LineStatus",
            dataType=plastics_rubber.datatypes.ProductionStatusEnumeration,
            value=plastics_rubber.datatypes.ProductionStatusEnumeration.OTHER,
        )
    )
    mESMessage: plastics_rubber.objtypes.MESMessageType | None
    machineConfiguration: plastics_rubber.objtypes.MachineConfigurationType
    machineInformation: plastics_rubber.objtypes.MachineInformationType
    machineMESConfiguration: plastics_rubber.objtypes.MachineMESConfigurationType
    materialList: plastics_rubber.objtypes.MaterialListType
    productionDatasetManagement: plastics_rubber.objtypes.ProductionDatasetManagementType | None
    productionParameters: ProductionParametersType
    setMESMessage: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7004"])
    users: plastics_rubber.objtypes.UsersType


o6.reference(ExtrusionLine_InterfaceType, "i=41", "ns=plastics_rubber;i=1004")
o6.reference(ExtrusionLine_InterfaceType, "i=41", "ns=plastics_rubber;i=1011")


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6171",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[10],
    value=[
        ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Description", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="CustomerName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductDescription", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Strand", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="Sequence", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="ParameterSetting", dataType=o6.NodeId("ns=plastics_rubber;i=3026"), valueRank=1),
        ns0.datatypes.Argument(name="SetOutput", dataType=o6.Double, valueRank=-1),
        ns0.datatypes.Argument(name="LotSize", dataType=o6.Double, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6173",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7006",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="JobNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7006",
    browseName="ns=plastics_extrusion_v1_line;AddJob",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6171"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6173"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6174",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7007",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7007", browseName="ns=plastics_extrusion_v1_line;RemoveJobById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6174"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6175",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7008",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7008", browseName="ns=plastics_extrusion_v1_line;StartJobById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6175"])
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6176",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7009",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7009",
    browseName="ns=plastics_extrusion_v1_line;InterruptJobById",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6176"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6177",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7010",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7010", browseName="ns=plastics_extrusion_v1_line;FinishJobById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6177"])
)


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_line;i=1011", browseName="ns=plastics_extrusion_v1_line;JobGroupType", displayName="JobGroupType")
class JobGroupType(ns0.objtypes.BaseObjectType):
    addJob: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7006"])
    configurationParameters: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_line;i=6112",
            browseName="ns=plastics_extrusion_v1_line;ConfigurationParameters",
            dataType=plastics_rubber.datatypes.ConfigurationParameterType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    description: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6108", browseName="ns=plastics_extrusion_v1_line;Description", dataType=o6.String, value="\n      ")
    )
    electricalEnergyConsumption: ns0.vartypes.AnalogUnitType | None
    equipmentDescription: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6109", browseName="ns=plastics_extrusion_v1_line;EquipmentDescription", dataType=o6.String)
    )
    finishJobById: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7010"])
    fluidEnergyConsumption: ns0.vartypes.AnalogUnitType | None
    id: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6107", browseName="ns=plastics_extrusion_v1_line;Id", dataType=o6.String, value="\n      ")
    )
    interruptJobById: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7009"])
    job_LangleNrRangle: JobType | None
    latestEnd: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6148", browseName="ns=plastics_extrusion_v1_line;LatestEnd", dataType=ns0.datatypes.UtcTime)
    )
    materialMapping: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_line;i=6111",
            browseName="ns=plastics_extrusion_v1_line;MaterialMapping",
            dataType=plastics_extrusion_v1_line_datypes.MaterialMappingType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6106", browseName="NodeVersion", dataType=o6.String, value="\n      ")
    )
    plannedProductionTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6149", browseName="ns=plastics_extrusion_v1_line;PlannedProductionTime", dataType=ns0.datatypes.Duration)
    )
    plannedSetUpTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6150", browseName="ns=plastics_extrusion_v1_line;PlannedSetUpTime", dataType=ns0.datatypes.Duration)
    )
    plannedStart: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6116", browseName="ns=plastics_extrusion_v1_line;PlannedStart", dataType=ns0.datatypes.UtcTime)
    )
    pressureAirConsumption: ns0.vartypes.AnalogUnitType | None
    priority: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6113", browseName="ns=plastics_extrusion_v1_line;Priority", dataType=o6.UInt32)
    )
    productionDatasetName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_extrusion_v1_line;i=6110", browseName="ns=plastics_extrusion_v1_line;ProductionDatasetName", dataType=o6.String)
    )
    removeJobById: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7007"])
    startJobById: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7008"])
    status: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_extrusion_v1_line;i=6151", browseName="ns=plastics_extrusion_v1_line;Status", dataType=plastics_rubber.datatypes.JobStatusEnumeration
        )
    )


o6.reference(JobGroupType, "i=41", "i=2133")


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6217",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[10],
    value=[
        ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="Description", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="EquipmentDescription", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="ProductionDatasetName", dataType=o6.String, valueRank=-1),
        ns0.datatypes.Argument(name="MaterialMapping", dataType=o6.NodeId("ns=plastics_extrusion_v1_line;i=3003"), valueRank=1),
        ns0.datatypes.Argument(name="Priority", dataType=o6.UInt32, valueRank=-1),
        ns0.datatypes.Argument(name="PlannedStart", dataType=ns0.datatypes.UtcTime, valueRank=-1),
        ns0.datatypes.Argument(name="PlannedProductionTime", dataType=ns0.datatypes.Duration, valueRank=-1),
        ns0.datatypes.Argument(name="PlannedSetUpTime", dataType=ns0.datatypes.Duration, valueRank=-1),
        ns0.datatypes.Argument(name="LatestEnd", dataType=ns0.datatypes.UtcTime, valueRank=-1),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6218",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7027",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="JobGroupNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7027",
    browseName="ns=plastics_extrusion_v1_line;AddJobGroup",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6217"]),
    outputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6218"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6214",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7028",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7028",
    browseName="ns=plastics_extrusion_v1_line;RemoveJobGroupById",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6214"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6213",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7029",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7029",
    browseName="ns=plastics_extrusion_v1_line;StartJobGroupById",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6213"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6215",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7030",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7030",
    browseName="ns=plastics_extrusion_v1_line;InterruptJobGroupById",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6215"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_extrusion_v1_line;i=6216",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_extrusion_v1_line;i=7031",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_extrusion_v1_line;i=7031",
    browseName="ns=plastics_extrusion_v1_line;FinishJobGroupById",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6216"]),
)


@o6.objecttype(nodeId="ns=plastics_extrusion_v1_line;i=1013", browseName="ns=plastics_extrusion_v1_line;JobGroupsType", displayName="JobGroupsType")
class JobGroupsType(ns0.objtypes.BaseObjectType):
    addJobGroup: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7027"])
    finishJobGroupById: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7031"])
    interruptJobGroupById: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7030"])
    jobGroup_LangleNrRangle: JobGroupType | None
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(o6.ns["ns=plastics_extrusion_v1_line;i=6190"])
    removeJobGroupById: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7028"])
    startJobGroupById: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_extrusion_v1_line;i=7029"])


o6.reference(JobGroupsType, "i=41", "i=2133")
o6.reference(JobGroupsType, "i=41", JobStatusChangedEventType)
o6.reference(JobGroupsType, "i=41", UnitFinishedEventType)
o6.reference(JobGroupsType, "i=41", LotFinishedEventType)
o6.reference(JobGroupsType, "i=41", JobGroupStatusChangedEventType)


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber, plastics_extrusion_v1_line_datypes
