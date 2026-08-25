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

"""Generated OPC UA tmc namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.pack_ml as pack_ml
from . import reftypes as tmc_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.datatype(nodeId="ns=tmc;i=3002", browseName="MessageType", description="The MessageType provides a uniquely identified localised text.", defaultEncodingId="ns=tmc;i=5036")
class MessageType(ns0.datatypes.Structure):
    iD: o6.String
    localText: o6.LocalizedText


@o6.datatype(
    nodeId="ns=tmc;i=3004",
    browseName="DataSetEntryType",
    description="The DataSetEntryType structure contains the value of a single parameter, or data value.",
    defaultEncodingId="ns=tmc;i=5003",
)
class DataSetEntryType(ns0.datatypes.Structure):
    iD: o6.String
    value: Any


@o6.enumtype(nodeId="ns=tmc;i=3005", browseName="ParameterDependencyEnumeration", description="The ParameterDependencyEnumeration contains what a parameter is depending upon.")
class ParameterDependencyEnumeration(ns0.datatypes.Enumeration):
    MACHINE = o6.enumfield(0, name="Machine")
    BRAND = o6.enumfield(1, name="Brand")
    MACHINE_AND__BRAND = o6.enumfield(2, name="Machine and Brand")


@o6.enumtype(nodeId="ns=tmc;i=3007", browseName="CommandEnumeration", description="The CommandEnumeration provides standardized commands that can be sent to a state machine.")
class CommandEnumeration(ns0.datatypes.Enumeration):
    ABORT = o6.enumfield(0, name="Abort")
    START = o6.enumfield(1, name="Start")
    STOP = o6.enumfield(2, name="Stop")
    RESET = o6.enumfield(3, name="Reset")
    HOLD = o6.enumfield(4, name="Hold")
    UNHOLD = o6.enumfield(5, name="Unhold")
    CLEAR = o6.enumfield(6, name="Clear")
    SUSPEND = o6.enumfield(7, name="Suspend")
    UNSUSPEND = o6.enumfield(8, name="Unsuspend")


@o6.enumtype(nodeId="ns=tmc;i=3008", browseName="StateEnumeration", description="The StateEnumeration contains the PackML states for a machine.")
class StateEnumeration(ns0.datatypes.Enumeration):
    STOPPED = o6.enumfield(0, name="Stopped")
    RESETTING = o6.enumfield(1, name="Resetting")
    IDLE = o6.enumfield(2, name="Idle")
    STARTING = o6.enumfield(3, name="Starting")
    EXECUTE = o6.enumfield(4, name="Execute")
    COMPLETING = o6.enumfield(5, name="Completing")
    COMPLETE = o6.enumfield(6, name="Complete")
    ABORTING = o6.enumfield(7, name="Aborting")
    ABORTED = o6.enumfield(8, name="Aborted")
    STOPPING = o6.enumfield(9, name="Stopping")
    CLEARING = o6.enumfield(10, name="Clearing")
    SUSPENDING = o6.enumfield(11, name="Suspending")
    SUSPENDED = o6.enumfield(12, name="Suspended")
    UNSUSPENDING = o6.enumfield(13, name="Unsuspending")
    HOLDING = o6.enumfield(14, name="Holding")
    HELD = o6.enumfield(15, name="Held")
    UNHOLDING = o6.enumfield(16, name="Unholding")


@o6.datatype(
    nodeId="ns=tmc;i=3009",
    browseName="MethodExecutionFeedbackType",
    description="The MethodExecutionFeedbackType provides suitable feedback, both positive and negative, to an OPC UA client invoking a method.",
    defaultEncodingId="ns=tmc;i=5052",
)
class MethodExecutionFeedbackType(ns0.datatypes.Structure):
    success: o6.Boolean
    message: list[MessageType]


@o6.enumtype(
    nodeId="ns=tmc;i=3015", browseName="StorageLogicEnumeration", description="The StorageLogicEnumeration describes standard loading and unloading material \nconfigurations."
)
class StorageLogicEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    FIFO = o6.enumfield(1, name="FIFO")
    LIFO = o6.enumfield(2, name="LIFO")
    FEFO = o6.enumfield(3, name="FEFO")


@o6.enumtype(nodeId="ns=tmc;i=3017", browseName="ProductionStatusEnumeration", description="The ProductionStatusEnumeration contains the production state of a machine module.")
class ProductionStatusEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="Other")
    BRAND_CHANGE = o6.enumfield(1, name="BrandChange")
    PRODUCTION = o6.enumfield(2, name="Production")
    NO_PRODUCTION = o6.enumfield(3, name="NoProduction")


@o6.datatype(nodeId="ns=tmc;i=3018", browseName="DataSetType", description="The DataSetType structure contains a set of data values.", defaultEncodingId="ns=tmc;i=5045")
class DataSetType(ns0.datatypes.Structure):
    iD: o6.String
    description: o6.LocalizedText
    values: list[DataSetEntryType]


@o6.datatype(
    nodeId="ns=tmc;i=3019",
    browseName="DataDescriptionType",
    description="The DataDescriptionType structure contains a metadata, i.e. a description.",
    defaultEncodingId="ns=tmc;i=5024",
)
class DataDescriptionType(ns0.datatypes.Structure):
    iD: o6.String
    mES_ID: o6.String
    description: o6.LocalizedText


@o6.datatype(
    nodeId="ns=tmc;i=3003",
    browseName="DataDefinitionType",
    description="The DataDefinitionType structure contains the metadata that describes a parameter.",
    defaultEncodingId="ns=tmc;i=5001",
)
class DataDefinitionType(DataDescriptionType):
    iD: o6.String
    mES_ID: o6.String
    description: o6.LocalizedText
    engineeringUnits: ns0.datatypes.EUInformation
    displayFormat: o6.String
    dependency: ParameterDependencyEnumeration
    dataType: o6.String
    userSubset: o6.Boolean
    controlRange: ns0.datatypes.Range
    alarmRange: ns0.datatypes.Range


@o6.datatype(nodeId="ns=tmc;i=3011", browseName="DataValueType", description="The DataValueType structure contains a data value.", defaultEncodingId="ns=tmc;i=5005")
class DataValueType(DataDescriptionType):
    iD: o6.String
    mES_ID: o6.String
    description: o6.LocalizedText
    value: Any
    engineeringUnits: ns0.datatypes.EUInformation


@o6.datatype(
    nodeId="ns=tmc;i=3010",
    browseName="MaterialDefinitionType",
    description="The MaterialDefinitionType structure contains the definition of a material. It is harmonised with \nISA 95 Material Definition.",
    defaultEncodingId="ns=tmc;i=5007",
)
class MaterialDefinitionType(ns0.datatypes.Structure):
    iD: o6.String
    mES_ID: o6.String
    description: o6.LocalizedText
    baseUnitOfMeasure: ns0.datatypes.EUInformation
    batchManaged: o6.Boolean
    groupID: o6.String | None
    parentGroupID: o6.String | None
    shelfLife: o6.UInt32 | None
    properties: list[DataValueType] | None


@o6.datatype(
    nodeId="ns=tmc;i=3013",
    browseName="MaterialPointType",
    description="The MaterialPointType structure provides the description of the capability of a load or\nunload point.",
    defaultEncodingId="ns=tmc;i=5039",
)
class MaterialPointType(ns0.datatypes.Structure):
    iD: o6.String
    description: o6.LocalizedText
    materialCapability: list[MaterialDefinitionType]
    connectedMaterialPoint: o6.ExpandedNodeId
    propagatesProductionOrder: o6.Boolean


@o6.datatype(
    nodeId="ns=tmc;i=3016",
    browseName="ProductionOrderHeaderType",
    description="The ProductionOrderHeaderType structure contains the header information for a production \norder.",
    defaultEncodingId="ns=tmc;i=5043",
)
class ProductionOrderHeaderType(ns0.datatypes.Structure):
    number: o6.String
    producedMaterial: MaterialDefinitionType
    targetQuantity: o6.Double
    continueAtJobEnd: o6.Boolean
    targetStartTime: o6.DateTime
    targetEndTime: o6.DateTime
    dataSetID: o6.String
    dataSetDescription: o6.LocalizedText
    materialListID: o6.String
    materialListDescription: o6.LocalizedText


@o6.enumtype(
    nodeId="ns=tmc;i=3020",
    browseName="MaterialIntegrityAgentEnumeration",
    description="The MaterialIntegrityAgentEnumeration identifies the possible agents responsible for material integrity checking.",
)
class MaterialIntegrityAgentEnumeration(ns0.datatypes.Enumeration):
    NONE = o6.enumfield(0, name="None")
    LOCAL = o6.enumfield(1, name="Local")
    EXTERNAL = o6.enumfield(2, name="External")


@o6.datatype(
    nodeId="ns=tmc;i=3021",
    browseName="DataSetDefinitionType",
    description="The DataSetDefinition structure contains the description and other necessary metadata of the \ncomplete set of machine settings required for production.",
    defaultEncodingId="ns=tmc;i=5064",
)
class DataSetDefinitionType(ns0.datatypes.Structure):
    iD: o6.String
    description: o6.LocalizedText
    definitions: list[DataDefinitionType]


@o6.enumtype(nodeId="ns=tmc;i=3023", browseName="ControlModeEnumeration", description="The ControlModeEnumeration contains the PackML modes of operation of a machine.")
class ControlModeEnumeration(ns0.datatypes.Enumeration):
    OTHER = o6.enumfield(0, name="OTHER")
    PRODUCTION = o6.enumfield(1, name="PRODUCTION")
    MAINTENANCE = o6.enumfield(2, name="MAINTENANCE")
    MANUAL = o6.enumfield(3, name="MANUAL")
    CHANGE_OVER = o6.enumfield(4, name="CHANGE OVER")
    CLEAN = o6.enumfield(5, name="CLEAN")
    SET_UP = o6.enumfield(6, name="SET UP")
    EMPTY_OUT = o6.enumfield(7, name="EMPTY OUT")
    REMOTE_SERVICE = o6.enumfield(8, name="REMOTE SERVICE")


@o6.enumtype(nodeId="ns=tmc;i=3026", browseName="MotorDirectionEnumeration", description="The MotorDirectionEnumeration provides the rotation direction of a motor.")
class MotorDirectionEnumeration(ns0.datatypes.Enumeration):
    CLOCKWISE = o6.enumfield(0, name="Clockwise")
    COUNTER_CLOCKWISE = o6.enumfield(1, name="CounterClockwise")


@o6.datatype(
    nodeId="ns=tmc;i=3029",
    browseName="RootCauseMessageType",
    description="The RootCauseMessageType structure contains a root cause message and its group identifier.",
    defaultEncodingId="ns=tmc;i=5144",
)
class RootCauseMessageType(MessageType):
    iD: o6.String
    localText: o6.LocalizedText
    groupID: o6.String


@o6.datatype(
    nodeId="ns=tmc;i=3030",
    browseName="RootCauseGroupType",
    description="The RootCauseGroupType structure contains a root cause message and its group identifier.",
    defaultEncodingId="ns=tmc;i=5146",
)
class RootCauseGroupType(ns0.datatypes.Structure):
    iD: o6.String
    parentID: o6.String
    description: o6.LocalizedText


@o6.enumtype(
    nodeId="ns=tmc;i=3035",
    browseName="StorageMixingLogicEnumeration",
    description="The StorageMixingLogicEnumeration describes standard ways of mixing material in a material \nstorage buffer.",
)
class StorageMixingLogicEnumeration(ns0.datatypes.Enumeration):
    MIXING = o6.enumfield(0, name="Mixing")
    NON_MIXING_BY_PRODUCT = o6.enumfield(1, name="NonMixingByProduct")
    NON_MIXING_BY_BATCH = o6.enumfield(2, name="NonMixingByBatch")


@o6.datatype(
    nodeId="ns=tmc;i=3014",
    browseName="MaterialStorageBufferDataType",
    description="The MaterialStorageBufferDataType structure provides the description of the capability of a \nmaterial storage buffer.",
    defaultEncodingId="ns=tmc;i=5041",
)
class MaterialStorageBufferDataType(ns0.datatypes.Structure):
    iD: o6.String
    storedMaterial: MaterialDefinitionType
    engineeringUnits: ns0.datatypes.EUInformation
    totalStorageCapacity: o6.Double
    storageLogic: StorageLogicEnumeration
    mixingLogic: StorageMixingLogicEnumeration


@o6.enumtype(nodeId="ns=tmc;i=3039", browseName="MaterialStockStatusEnumeration", description="The MaterialStockStatusEnumeration provides the stock status for a material lot.")
class MaterialStockStatusEnumeration(ns0.datatypes.Enumeration):
    UNRESTRICTED = o6.enumfield(0, name="Unrestricted")
    QUALITY_INSPECTION = o6.enumfield(1, name="QualityInspection")
    BLOCKED = o6.enumfield(2, name="Blocked")


@o6.datatype(
    nodeId="ns=tmc;i=3012",
    browseName="MaterialLotType",
    description="The MaterialLotType structure contains the material lot information. It is harmonised with ISA \n95 Material Lot.",
    defaultEncodingId="ns=tmc;i=5010",
)
class MaterialLotType(ns0.datatypes.Structure):
    iD: o6.String
    mES_ID: o6.String
    description: o6.LocalizedText
    materialDefinition: MaterialDefinitionType
    status: MaterialStockStatusEnumeration
    productionDate: o6.DateTime
    bestUsedBeforeDate: o6.DateTime | None
    properties: list[DataValueType] | None


@o6.datatype(
    nodeId="ns=tmc;i=3025",
    browseName="MaterialSublotType",
    description="The MaterialSublotType structure contains the material sublot information. It is harmonised with \nISA 95 Material Sublot.",
    defaultEncodingId="ns=tmc;i=5013",
)
class MaterialSublotType(ns0.datatypes.Structure):
    iD: o6.String
    mES_ID: o6.String
    materialLot: MaterialLotType
    materialStorageLocationID: o6.String
    quantity: o6.Double
    carrierID: o6.String | None
    relativePositionID: o6.String | None
    parentSublotID: o6.String | None
    sublots: list[MaterialSublotType] | None


@o6.datatype(
    nodeId="ns=tmc;i=3036",
    browseName="MaterialListItemType",
    description="The MaterialListItemType structure contains a single material to be processed.",
    defaultEncodingId="ns=tmc;i=5307",
)
class MaterialListItemType(ns0.datatypes.Structure):
    assemblyID: o6.String
    materialPointID: o6.String
    materialPointMES_ID: o6.String
    materialSublot: MaterialSublotType
    materialStockStatus: MaterialStockStatusEnumeration
    followUpMaterials: list[MaterialSublotType]


@o6.datatype(
    nodeId="ns=tmc;i=3037", browseName="MaterialListType", description="The MaterialListType structure contains a set of material list items.", defaultEncodingId="ns=tmc;i=5309"
)
class MaterialListType(ns0.datatypes.Structure):
    iD: o6.String
    description: o6.LocalizedText
    items: list[MaterialListItemType]


@o6.datatype(
    nodeId="ns=tmc;i=3038",
    browseName="ProductionOrderType",
    description="The ProductionOrderType structure contains the complete production order information.",
    defaultEncodingId="ns=tmc;i=5311",
)
class ProductionOrderType(ns0.datatypes.Structure):
    header: ProductionOrderHeaderType
    materialList: MaterialListType
    dataSet: DataSetType


@o6.datatype(
    nodeId="ns=tmc;i=3006",
    browseName="OrchestrationProductionOrderType",
    description="The OrchestrationProductionOrderType structure contains the complete production order \ninformation used by the Production Order Orchestration Layer.",
    defaultEncodingId="ns=tmc;i=9261",
)
class OrchestrationProductionOrderType(ProductionOrderType):
    header: ProductionOrderHeaderType
    materialList: MaterialListType
    dataSet: DataSetType
    activeMachineModules: list[o6.String]


@o6.enumtype(
    nodeId="ns=tmc;i=3040",
    browseName="MaterialValidationStatusEnumeration",
    description="The MaterialValidationStatusEnumeration describes the status of the material validation \nprocess.",
)
class MaterialValidationStatusEnumeration(ns0.datatypes.Enumeration):
    NONE = o6.enumfield(0, name="None")
    WAITING = o6.enumfield(1, name="Waiting")
    PASSED = o6.enumfield(2, name="Passed")
    FAILED = o6.enumfield(3, name="Failed")


del Any, TYPE_CHECKING, uuid, o6, di, ns0, pack_ml, tmc_reftypes
