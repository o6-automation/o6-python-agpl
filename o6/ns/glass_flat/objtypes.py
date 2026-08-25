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

"""Generated OPC UA glass_flat namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
from . import datatypes as glass_flat_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=glass_flat;i=1023", browseName="ns=glass_flat;ProductionPlanType", displayName="ProductionPlanType")
class ProductionPlanType(ns0.objtypes.OrderedListType):
    langleOrderedObjectRangle: ProductionJobType | None


@o6.objecttype(nodeId="ns=glass_flat;i=1024", browseName="ns=glass_flat;InitializingSubStateMachineType", displayName="InitializingSubStateMachineType")
class InitializingSubStateMachineType(ns0.objtypes.FiniteStateMachineType):
    idle: ns0.objtypes.InitialStateType
    idleToQueued: ns0.objtypes.TransitionType
    queued: ns0.objtypes.StateType
    queuedToIdle: ns0.objtypes.TransitionType
    queuedToReleased: ns0.objtypes.TransitionType
    released: ns0.objtypes.StateType
    releasedToQueued: ns0.objtypes.TransitionType


@o6.objecttype(nodeId="ns=glass_flat;i=1006", browseName="ns=glass_flat;BaseMaterialType", displayName="BaseMaterialType")
class BaseMaterialType(ns0.objtypes.BaseObjectType):
    description: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6017", browseName="ns=glass_flat;Description", dataType=o6.LocalizedText, accessLevel=3, userAccessLevel=1)
    )
    identifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6002", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
        )
    )
    location: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6070", browseName="ns=glass_flat;Location", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1)
    )
    materialIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6003", browseName="ns=glass_flat;MaterialIdentifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
        )
    )
    weight: ns0.vartypes.AnalogUnitType | None
    x: ns0.vartypes.AnalogUnitType | None
    y: ns0.vartypes.AnalogUnitType | None
    z: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=glass_flat;i=1002", browseName="ns=glass_flat;AssemblyType", displayName="AssemblyType")
class AssemblyType(BaseMaterialType):
    pass


@o6.objecttype(nodeId="ns=glass_flat;i=1010", browseName="ns=glass_flat;GasMixType", displayName="GasMixType")
class GasMixType(BaseMaterialType):
    gasFilling: ns0.vartypes.AnalogUnitType | None
    gas_1: BaseMaterialType | None
    gas_2: BaseMaterialType | None
    mixingRatio: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=glass_flat;i=1019", browseName="ns=glass_flat;FoilType", displayName="FoilType")
class FoilType(BaseMaterialType):
    z: ns0.vartypes.AnalogUnitType


@o6.objecttype(nodeId="ns=glass_flat;i=1011", browseName="ns=glass_flat;GlassType", displayName="GlassType")
class GlassType(BaseMaterialType):
    absorption: ns0.vartypes.AnalogUnitType | None
    coatingClass: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6088", browseName="ns=glass_flat;CoatingClass", dataType=glass_flat_datypes.CoatingClassEnumeration, accessLevel=3, userAccessLevel=1
        )
    )
    coatingEmessivity: ns0.vartypes.AnalogUnitType | None
    coatingSubClass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6128", browseName="ns=glass_flat;CoatingSubClass", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
        )
    )
    electricalConductivity: ns0.vartypes.AnalogUnitType | None
    orientation: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6132", browseName="ns=glass_flat;Orientation", dataType=ns0.datatypes.Number, accessLevel=3, userAccessLevel=1)
    )
    reflection: ns0.vartypes.AnalogUnitType | None
    significantSide: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6097", browseName="ns=glass_flat;SignificantSide", dataType=glass_flat_datypes.SignificantSideEnumeration, accessLevel=3, userAccessLevel=1
        )
    )
    structureAlignment: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6098",
            browseName="ns=glass_flat;StructureAlignment",
            dataType=glass_flat_datypes.StructureAlignmentEnumeration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    structureClass: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6087", browseName="ns=glass_flat;StructureClass", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
        )
    )
    transmission: ns0.vartypes.AnalogUnitType | None
    x: ns0.vartypes.AnalogUnitType
    y: ns0.vartypes.AnalogUnitType


@o6.objecttype(nodeId="ns=glass_flat;i=1016", browseName="ns=glass_flat;SpacerType", displayName="SpacerType")
class SpacerType(BaseMaterialType):
    filling: ns0.vartypes.BaseDataVariableType | None
    sealantDepth: ns0.vartypes.AnalogUnitType | None
    spacerMaterialClass: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6163", browseName="ns=glass_flat;SpacerMaterialClass", dataType=glass_flat_datypes.SpacerMaterialClass, accessLevel=3, userAccessLevel=1
        )
    )
    spacerMaterialSubClass: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6165", browseName="ns=glass_flat;SpacerMaterialSubClass", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
        )
    )


@o6.objecttype(nodeId="ns=glass_flat;i=1041", browseName="ns=glass_flat;ManualFolderType", displayName="ManualFolderType")
class ManualFolderType(ns0.objtypes.FolderType):
    externalManuals: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6176", browseName="ns=glass_flat;ExternalManuals", dataType=glass_flat_datypes.LimitedString64, valueRank=1, arrayDimensions=[0]
        )
    )
    langleLocalManualsRangle: ns0.objtypes.FileType | None


@o6.objecttype(nodeId="ns=glass_flat;i=1015", browseName="ns=glass_flat;GlassMachineType", displayName="GlassMachineType")
class GlassMachineType(ns0.objtypes.BaseObjectType):
    components: machinery.objtypes.MachineComponentsType | None = o6.hasAddIn(
        machinery.objtypes.MachineComponentsType(nodeId="ns=glass_flat;i=5002", browseName="ns=glass_flat;Components")
    )
    configurationRules: ConfigurationRulesType
    identification: GlassMachineIdentificationType
    maintenanceManuals: ManualFolderType | None = o6.hasComponent(ManualFolderType(nodeId="ns=glass_flat;i=5009", browseName="ns=glass_flat;MaintenanceManuals"))
    operationManuals: ManualFolderType | None = o6.hasComponent(ManualFolderType(nodeId="ns=glass_flat;i=5011", browseName="ns=glass_flat;OperationManuals"))
    production: ProductionType


@o6.objecttype(nodeId="ns=glass_flat;i=1018", browseName="ns=glass_flat;SealingMaterialType", displayName="SealingMaterialType")
class SealingMaterialType(BaseMaterialType):
    addOnMaterial: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=glass_flat;i=6181", browseName="ns=glass_flat;AddOnMaterial", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
        )
    )
    hardener: BaseMaterialType | None
    mixingRatio: ns0.vartypes.AnalogUnitType
    resin: BaseMaterialType | None


@o6.objecttype(nodeId="ns=glass_flat;i=1063", browseName="ns=glass_flat;ConfigurationRulesType", displayName="ConfigurationRulesType")
class ConfigurationRulesType(ns0.objtypes.BaseObjectType):
    allowedEngineeringUnits: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6186", browseName="ns=glass_flat;AllowedEngineeringUnits", dataType=ns0.datatypes.EUInformation, valueRank=1, arrayDimensions=[0]
        )
    )
    allowedFileFormats: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6174", browseName="ns=glass_flat;AllowedFileFormats", dataType=glass_flat_datypes.FileFormatType, valueRank=1, arrayDimensions=[0]
        )
    )
    machineProcessingCoordinateSystem: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6188",
            browseName="ns=glass_flat;MachineProcessingCoordinateSystem",
            dataType=glass_flat_datypes.CoordinateSystemEnumeration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=glass_flat;i=1003", browseName="ns=glass_flat;InstructionType", displayName="InstructionType")
class InstructionType(ns0.objtypes.BaseObjectType):
    plan: ns0.objtypes.FileType
    planFileFormat: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6273",
            browseName="ns=glass_flat;PlanFileFormat",
            dataType=glass_flat_datypes.FileFormatType,
            value=glass_flat_datypes.FileFormatType(name="", fileExtension="", version=""),
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=glass_flat;i=1005", browseName="ns=glass_flat;ProductionStateMachineType", displayName="ProductionStateMachineType")
class ProductionStateMachineType(ns0.objtypes.FiniteStateMachineType):
    aborted: ns0.objtypes.StateType
    abortedToInitializing: ns0.objtypes.TransitionType
    currentState: ns0.vartypes.FiniteStateVariableType = o6.hasComponent(
        ns0.vartypes.FiniteStateVariableType(nodeId="ns=glass_flat;i=6280", browseName="CurrentState", dataType=o6.LocalizedText)
    )
    ended: ns0.objtypes.StateType
    endedToInitializing: ns0.objtypes.TransitionType
    initializing: ns0.objtypes.InitialStateType
    initializingState: InitializingSubStateMachineType
    initializingToAborted: ns0.objtypes.TransitionType
    initializingToRunning: ns0.objtypes.TransitionType
    interrupted: ns0.objtypes.StateType
    interruptedToAborted: ns0.objtypes.TransitionType
    interruptedToRunning: ns0.objtypes.TransitionType
    running: ns0.objtypes.StateType
    runningToAborted: ns0.objtypes.TransitionType
    runningToEnded: ns0.objtypes.TransitionType
    runningToInterrupted: ns0.objtypes.TransitionType
    runningToRunning: ns0.objtypes.TransitionType


@o6.objecttype(nodeId="ns=glass_flat;i=1017", browseName="ns=glass_flat;PackagingType", displayName="PackagingType")
class PackagingType(BaseMaterialType):
    cornerProtection: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=glass_flat;i=6399", browseName="ns=glass_flat;CornerProtection", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
        )
    )
    perimeterProtection: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=glass_flat;i=6400", browseName="ns=glass_flat;PerimeterProtection", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
        )
    )
    spacer: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=glass_flat;i=6398", browseName="ns=glass_flat;Spacer", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
        )
    )


@o6.objecttype(nodeId="ns=glass_flat;i=1030", browseName="ns=glass_flat;GlassEventType", displayName="GlassEventType", isAbstract=True)
class GlassEventType(ns0.objtypes.BaseEventType):
    identifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6405", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, value="\n      ", accessLevel=3, userAccessLevel=1
        )
    )
    jobdIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6410",
            browseName="ns=glass_flat;JobdIdentifier",
            dataType=glass_flat_datypes.LimitedString64,
            value="\n      ",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    location: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6406", browseName="ns=glass_flat;Location", dataType=glass_flat_datypes.LimitedString64, value="\n      ", accessLevel=3, userAccessLevel=1
        )
    )
    materialIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6411",
            browseName="ns=glass_flat;MaterialIdentifier",
            dataType=glass_flat_datypes.LimitedString64,
            value="\n      ",
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(nodeId="ns=glass_flat;i=1031", browseName="ns=glass_flat;GlassMaterialEventType", displayName="GlassMaterialEventType", isAbstract=True)
class GlassMaterialEventType(GlassEventType):
    pass


@o6.objecttype(nodeId="ns=glass_flat;i=1025", browseName="ns=glass_flat;MaterialExitEventType", displayName="MaterialExitEventType", isAbstract=True)
class MaterialExitEventType(GlassMaterialEventType):
    pass


@o6.objecttype(nodeId="ns=glass_flat;i=1026", browseName="ns=glass_flat;MaterialReceivedEventType", displayName="MaterialReceivedEventType", isAbstract=True)
class MaterialReceivedEventType(GlassMaterialEventType):
    pass


@o6.objecttype(nodeId="ns=glass_flat;i=1027", browseName="ns=glass_flat;MaterialMissingEventType", displayName="MaterialMissingEventType", isAbstract=True)
class MaterialMissingEventType(GlassMaterialEventType):
    pass


@o6.objecttype(nodeId="ns=glass_flat;i=1032", browseName="ns=glass_flat;InterruptedEventType", displayName="InterruptedEventType", isAbstract=True)
class InterruptedEventType(GlassEventType):
    processName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6403", browseName="ns=glass_flat;ProcessName", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
        )
    )


@o6.objecttype(nodeId="ns=glass_flat;i=1033", browseName="ns=glass_flat;OpenSecurityFenceType", displayName="OpenSecurityFenceType", isAbstract=True)
class OpenSecurityFenceType(InterruptedEventType):
    pass


@o6.objecttype(nodeId="ns=glass_flat;i=1034", browseName="ns=glass_flat;ProcessParameterOutOfRangeType", displayName="ProcessParameterOutOfRangeType", isAbstract=True)
class ProcessParameterOutOfRangeType(InterruptedEventType):
    pass


@o6.objecttype(nodeId="ns=glass_flat;i=1035", browseName="ns=glass_flat;ToolMissingEventType", displayName="ToolMissingEventType", isAbstract=True)
class ToolMissingEventType(InterruptedEventType):
    pass


@o6.objecttype(nodeId="ns=glass_flat;i=1036", browseName="ns=glass_flat;OutOfJobEventType", displayName="OutOfJobEventType", isAbstract=True)
class OutOfJobEventType(InterruptedEventType):
    pass


@o6.objecttype(nodeId="ns=glass_flat;i=1037", browseName="ns=glass_flat;JobMovedEventType", displayName="JobMovedEventType", isAbstract=True)
class JobMovedEventType(GlassEventType):
    jobdIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6404",
            browseName="ns=glass_flat;JobdIdentifier",
            dataType=glass_flat_datypes.LimitedString64,
            value="\n      ",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    newPosition: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6407", browseName="ns=glass_flat;NewPosition", dataType=ns0.datatypes.Number, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=glass_flat;i=1038", browseName="ns=glass_flat;EmergencyButtonPressedEventType", displayName="EmergencyButtonPressedEventType", isAbstract=True)
class EmergencyButtonPressedEventType(InterruptedEventType):
    pass


@o6.objecttype(nodeId="ns=glass_flat;i=1039", browseName="ns=glass_flat;MotorTemperatureTooHighEventType", displayName="MotorTemperatureTooHighEventType", isAbstract=True)
class MotorTemperatureTooHighEventType(InterruptedEventType):
    pass


@o6.objecttype(nodeId="ns=glass_flat;i=1040", browseName="ns=glass_flat;CommunicationErrorEventType", displayName="CommunicationErrorEventType", isAbstract=True)
class CommunicationErrorEventType(GlassEventType):
    pass


@o6.objecttype(nodeId="ns=glass_flat;i=1029", browseName="ns=glass_flat;IntermediateStepEvent", displayName="IntermediateStepEvent", isAbstract=True)
class IntermediateStepEvent(GlassEventType):
    processStep: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6412", browseName="ns=glass_flat;ProcessStep", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
        )
    )
    status: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6413", browseName="ns=glass_flat;Status", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1)
    )


@o6.objecttype(nodeId="ns=glass_flat;i=1020", browseName="ns=glass_flat;GlassMachineIdentificationType", displayName="GlassMachineIdentificationType")
class GlassMachineIdentificationType(machinery.objtypes.MachineIdentificationType):
    loggedInProfiles: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6414", browseName="ns=glass_flat;LoggedInProfiles", dataType=glass_flat_datypes.UserProfileType, valueRank=1, arrayDimensions=[0]
        )
    )


o6.call(nodeId="ns=glass_flat;i=7003", browseName="ns=glass_flat;ReleaseJob")

o6.call(nodeId="ns=glass_flat;i=7004", browseName="ns=glass_flat;SuspendJob")

o6.call(nodeId="ns=glass_flat;i=7021", browseName="ns=glass_flat;QueueJob")


@o6.objecttype(nodeId="ns=glass_flat;i=1004", browseName="ns=glass_flat;ProductionJobType", displayName="ProductionJobType", interfaces=[ns0.objtypes.IOrderedObjectType])
class ProductionJobType(ns0.objtypes.BaseObjectType):
    abortJob: o6.node.MethodNode | None = o6.hasComponent(o6.call(nodeId="ns=glass_flat;i=7022", browseName="ns=glass_flat;AbortJob"))
    endTime: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=glass_flat;i=6054", browseName="ns=glass_flat;EndTime", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
    )
    identifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6050", browseName="ns=glass_flat;Identifier", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1
        )
    )
    inputMaterials: ns0.objtypes.FolderType
    instruction: InstructionType
    jobGroup: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6055", browseName="ns=glass_flat;JobGroup", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1)
    )
    lock: di.objtypes.LockingServicesType | None
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6051", browseName="ns=glass_flat;Name", dataType=glass_flat_datypes.LimitedString64, accessLevel=3, userAccessLevel=1)
    )
    numberInList: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6001", browseName="ns=glass_flat;NumberInList", dataType=o6.UInt16, accessLevel=3, userAccessLevel=1)
    )
    outputMaterials: ns0.objtypes.FolderType
    queueJob: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=glass_flat;i=7021"])
    releaseJob: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=glass_flat;i=7003"])
    startTime: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=glass_flat;i=6053", browseName="ns=glass_flat;StartTime", dataType=o6.DateTime, accessLevel=3, userAccessLevel=1)
    )
    state: ProductionStateMachineType
    suspendJob: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=glass_flat;i=7004"])


@o6.objecttype(nodeId="ns=glass_flat;i=1007", browseName="ns=glass_flat;CuttingJobType", displayName="CuttingJobType")
class CuttingJobType(ProductionJobType):
    langleInputMaterialRangle: BaseMaterialType
    langleOutputMaterialRangle: GlassType


@o6.objecttype(nodeId="ns=glass_flat;i=1008", browseName="ns=glass_flat;AssemblyJobType", displayName="AssemblyJobType")
class AssemblyJobType(ProductionJobType):
    langleInputMaterialRangle: BaseMaterialType
    langleOutputMaterialRangle: AssemblyType


@o6.objecttype(nodeId="ns=glass_flat;i=1009", browseName="ns=glass_flat;ProcessingJobType", displayName="ProcessingJobType")
class ProcessingJobType(ProductionJobType):
    langleInputMaterialRangle: BaseMaterialType
    langleOutputMaterialRangle: BaseMaterialType


ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6156",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7048",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[4],
    value=[
        ns0.datatypes.Argument(name="Identifier", dataType=o6.NodeId("ns=glass_flat;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="Name", dataType=o6.NodeId("ns=glass_flat;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="InputMaterial", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0]),
        ns0.datatypes.Argument(name="OutputMaterial", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0]),
    ],
)
ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6331",
    browseName="OutputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7048",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="JobNodeId", dataType=o6.NodeId, valueRank=-1)],
)
o6.call(
    nodeId="ns=glass_flat;i=7048",
    browseName="ns=glass_flat;InsertJob",
    inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6156"]),
    outputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6331"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6123",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7049",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Identifier", dataType=o6.NodeId("ns=glass_flat;i=3002"), valueRank=-1)],
)
o6.call(nodeId="ns=glass_flat;i=7049", browseName="ns=glass_flat;DeleteJob", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6123"]))

ns0.vartypes.PropertyType(
    nodeId="ns=glass_flat;i=6064",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=glass_flat;i=7050",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[3],
    value=[
        ns0.datatypes.Argument(name="Target", dataType=o6.NodeId("ns=glass_flat;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="Source", dataType=o6.NodeId("ns=glass_flat;i=3002"), valueRank=-1),
        ns0.datatypes.Argument(name="Before", dataType=o6.Boolean, valueRank=-1),
    ],
)
o6.call(nodeId="ns=glass_flat;i=7050", browseName="ns=glass_flat;ChangePositionInList", inputArgs=o6.hasProperty(o6.ns["ns=glass_flat;i=6064"]))


@o6.objecttype(nodeId="ns=glass_flat;i=1021", browseName="ns=glass_flat;ProductionType", displayName="ProductionType")
class ProductionType(ns0.objtypes.BaseObjectType):
    changePositionInList: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=glass_flat;i=7050"])
    currentCountOfJobs: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6178", browseName="ns=glass_flat;CurrentCountOfJobs", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    deleteJob: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=glass_flat;i=7049"])
    insertJob: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=glass_flat;i=7048"])
    jobListIsRecommendation: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6269", browseName="ns=glass_flat;JobListIsRecommendation", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1)
    )
    maxCountOfJobs: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=glass_flat;i=6177", browseName="ns=glass_flat;MaxCountOfJobs", dataType=o6.UInt32, accessLevel=3, userAccessLevel=1)
    )
    productionPlan: ProductionPlanType = o6.hasComponent(ProductionPlanType(nodeId="ns=glass_flat;i=5007", browseName="ns=glass_flat;ProductionPlan"))
    supportedMaterialTypes: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=glass_flat;i=6079", browseName="ns=glass_flat;SupportedMaterialTypes", dataType=o6.NodeId, valueRank=1, arrayDimensions=[0], accessLevel=3, userAccessLevel=1
        )
    )


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, glass_flat_datypes
