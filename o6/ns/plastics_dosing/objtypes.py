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

"""Generated OPC UA plastics_dosing namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_dosing_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=plastics_dosing;i=1010",
    browseName="ns=plastics_dosing;DosingMaintenanceType",
    displayName="DosingMaintenanceType",
    description="Information on the maintenance status of the dosing system.",
)
class DosingMaintenanceType(plastics_rubber.objtypes.MaintenanceType):
    interval: ns0.vartypes.AnalogItemType


@o6.objecttype(
    nodeId="ns=plastics_dosing;i=1013", browseName="ns=plastics_dosing;DosingMaterialType", displayName="DosingMaterialType", description="Provides information about the material"
)
class DosingMaterialType(plastics_rubber.objtypes.MaterialType):
    materialClass: ns0.vartypes.MultiStateValueDiscreteType


@o6.objecttype(
    nodeId="ns=plastics_dosing;i=1003",
    browseName="ns=plastics_dosing;DosingSystemType",
    displayName="DosingSystemType",
    description="Subtype of BaseObjectType used for a root dosing system Object as part of a production cell/line.",
)
class DosingSystemType(ns0.objtypes.BaseObjectType):
    deviceMappingNumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_dosing;i=6017",
            browseName="ns=plastics_dosing;DeviceMappingNumber",
            description="Unique identifier/address/number for devices of the same DeviceType within a local network.",
            dataType=o6.UInt32,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    displayLanguage: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_dosing;i=6015",
            browseName="ns=plastics_dosing;DisplayLanguage",
            description="With the DisplayLanguage Property the client can set the desired language on the user interface at the Dosing System.",
            dataType=ns0.datatypes.LocaleId,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    feeder: ContinuousComponentType | None
    identification: machinery.objtypes.MachineIdentificationType
    isContinuous: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_dosing;i=6016",
            browseName="ns=plastics_dosing;IsContinuous",
            description="The dosing device can be installed on an extruder (EXT) or an injection moulding machine (IMM). EXT is a continuous process, IMM is a cyclic process. For inline dosing devices, directly mounted on the feed throat of an IMM the IsContinuous flag is false, when installed on an EXT this flag is true.",
            dataType=o6.Boolean,
        )
    )
    machineConfiguration: plastics_rubber.objtypes.MachineConfigurationType
    machineryBuildingBlocks: ns0.objtypes.FolderType
    operation: OperationType


o6.reference(DosingSystemType, "i=41", "ns=plastics_rubber;i=1004")
o6.reference(DosingSystemType, "i=41", "ns=plastics_rubber;i=1011")
o6.reference(DosingSystemType, "i=41", "ns=plastics_rubber;i=1052")


@o6.objecttype(
    nodeId="ns=plastics_dosing;i=1007",
    browseName="ns=plastics_dosing;MixingType",
    displayName="MixingType",
    description="In case the dosing station is equipped with an active mixing device like on a batch blender, the mixing process can be controlled with the type MixingType.",
)
class MixingType(ns0.objtypes.BaseObjectType):
    idleMixing: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_dosing;i=6058",
            browseName="ns=plastics_dosing;IdleMixing",
            description="With idle mixing the mixer of the batch blender rotates once in a while to keep the material in the mixer flowing and material does not get blocked by the mixer blades.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    mixingDuration: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_dosing;i=6057",
            browseName="ns=plastics_dosing;MixingDuration",
            description="Duration of a mixing process.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    mixingInterval: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_dosing;i=6031",
            browseName="ns=plastics_dosing;MixingInterval",
            description="Interval between two mixing processes, in number of shots.",
            dataType=o6.UInt16,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    mixingMode: ns0.vartypes.MultiStateValueDiscreteType


@o6.objecttype(
    nodeId="ns=plastics_dosing;i=1011",
    browseName="ns=plastics_dosing;WeighingProcessType",
    displayName="WeighingProcessType",
    description="The weighing process can be used to perform a material pre-calibration or to determine the feedrate of the dosing system used by this component.",
)
class WeighingProcessType(ns0.objtypes.BaseObjectType):
    testWeight: ns0.vartypes.AnalogUnitRangeType
    weighingTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_dosing;i=6092",
            browseName="ns=plastics_dosing;WeighingTime",
            description="Duration of the weighing process.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_dosing;i=1008",
    browseName="ns=plastics_dosing;ComponentsType",
    displayName="ComponentsType",
    description="This ObjectType is a container for all Components in the DosingSystem.",
)
class ComponentsType(ns0.objtypes.BaseObjectType):
    component_Nr_: ComponentType
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=plastics_dosing;i=6108", browseName="NodeVersion", dataType=o6.String))


o6.reference(ComponentsType, "i=41", "i=2133")


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_dosing;i=6142",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_dosing;i=7013",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[
        ns0.datatypes.Argument(
            name="Id", dataType=o6.NodeId("i=12"), valueRank=-1, arrayDimensions=[], description=o6.LocalizedText("Id of the error, listed in ActiveErrors, that shall be reset.")
        )
    ],
)
o6.call(
    nodeId="ns=plastics_dosing;i=7013",
    browseName="ns=plastics_dosing;ResetErrorById",
    description="Method to reset one error of the device.",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_dosing;i=6142"]),
)


@o6.objecttype(
    nodeId="ns=plastics_dosing;i=1005",
    browseName="ns=plastics_dosing;MaterialConsumptionType",
    displayName="MaterialConsumptionType",
    description="Provides information about the material consumption.",
)
class MaterialConsumptionType(ns0.objtypes.BaseObjectType):
    reset: o6.node.MethodNode = o6.hasComponent(
        o6.call(nodeId="ns=plastics_dosing;i=7015", browseName="ns=plastics_dosing;Reset", description="The Method Reset resets the two counters TotalConsumption and Scrap.")
    )
    scrap: ns0.vartypes.AnalogUnitType | None
    totalConsumption: ns0.vartypes.AnalogUnitType


@o6.objecttype(
    nodeId="ns=plastics_dosing;i=1012",
    browseName="ns=plastics_dosing;LevelsType",
    displayName="LevelsType",
    description="Gives information about the filling of the dosing component.",
)
class LevelsType(ns0.objtypes.BaseObjectType):
    abortFilling: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_dosing;i=7021", browseName="ns=plastics_dosing;AbortFilling", description="Method to abort filling the Component.")
    )
    filling: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_dosing;i=6085",
            browseName="ns=plastics_dosing;Filling",
            description="Flag to indicate if the hopper is being filled right now.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    level: plastics_rubber.objtypes.MonitoredParameterType
    startFilling: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_dosing;i=7020",
            browseName="ns=plastics_dosing;StartFilling",
            description="Method to fill the Component up to the MaxValue of the MonitoredParameterType in the Level Variable.",
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_dosing;i=1004",
    browseName="ns=plastics_dosing;OperationType",
    displayName="OperationType",
    description="Contains objects which are necessary to operate the DosingSystem.",
)
class OperationType(ns0.objtypes.BaseObjectType):
    activeErrors: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_dosing;i=6050",
            browseName="ns=plastics_dosing;ActiveErrors",
            description="List of the active errors of the device.",
            dataType=plastics_rubber.datatypes.ActiveErrorDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    batchWeight: plastics_rubber.objtypes.ControlledParameterType | None
    components: ComponentsType
    disableDevice: o6.node.MethodNode = o6.hasComponent(
        o6.call(nodeId="ns=plastics_dosing;i=7004", browseName="ns=plastics_dosing;DisableDevice", description="Disables the device, for example deactivate motor drives.")
    )
    dosingDuration: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_dosing;i=6037",
            browseName="ns=plastics_dosing;DosingDuration",
            description="This parameter defines the duration the dosing shall be active after receiving the StartDosingShot signal.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    electricalEnergy: plastics_rubber.objtypes.EnergyType | None
    enableDevice: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_dosing;i=7003",
            browseName="ns=plastics_dosing;EnableDevice",
            description="Enables the device, for example activate motor drives. Triggers the transition from MachineryItemState NotAvailable to NotExecuting.",
        )
    )
    enableDosingOpcUa: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_dosing;i=6102",
            browseName="ns=plastics_dosing;EnableDosingOpcUa",
            description="Variable to set and read the actual state how the dosing signal is transferred from the client to the dosing system in addition to RemoteControlOpcUa.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    firstFilling: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_dosing;i=7014",
            browseName="ns=plastics_dosing;FirstFilling",
            description="Method to fill the DosingSystem for the first time with the mixture of materials from the current recipe.",
        )
    )
    highestActiveAlarmSeverity: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_dosing;i=6049",
            browseName="ns=plastics_dosing;HighestActiveAlarmSeverity",
            description="Indication of the severity of the highest active alarm.",
            dataType=o6.UInt16,
        )
    )
    identifyDevice: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_dosing;i=7002",
            browseName="ns=plastics_dosing;IdentifyDevice",
            description="The DosingSystem on which this method is called shows itself by e.g. activation of a LED.",
        )
    )
    isActive: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_dosing;i=6024",
            browseName="ns=plastics_dosing;IsActive",
            description="The IsActive Property provides information if the dosing unit is active in the current production.",
            dataType=o6.Boolean,
        )
    )
    maintenance: DosingMaintenanceType | None
    mixing: MixingType | None
    productionDataSetManagement: plastics_rubber.objtypes.ProductionDatasetManagementType | None
    purgeDuration: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_dosing;i=6028",
            browseName="ns=plastics_dosing;PurgeDuration",
            description="Duration of the purging function of the dosing system.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    remoteControlOpcUa: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_dosing;i=6027", browseName="ns=plastics_dosing;RemoteControlOpcUa", dataType=o6.Boolean, accessLevel=3, userAccessLevel=1
        )
    )
    resetAllErrors: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_dosing;i=7012", browseName="ns=plastics_dosing;ResetAllErrors", description="Method to reset all errors of the device.")
    )
    resetErrorById: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_dosing;i=7013"])
    setActive: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_dosing;i=6025",
            browseName="ns=plastics_dosing;SetActive",
            description="Activates the dosing unit for the current production.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    shotWeight: plastics_rubber.objtypes.ControlledParameterType | None
    startDosingContinuous: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_dosing;i=7060",
            browseName="ns=plastics_dosing;StartDosingContinuous",
            description="If EnableDosingOpcUa is TRUE, this method can be used to start dosing continuously.",
        )
    )
    startDosingShot: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_dosing;i=7005",
            browseName="ns=plastics_dosing;StartDosingShot",
            description="If EnableDosingOpcUa is TRUE, this method can be used to start dosing for one shot with a defined duration specified by DosingDuration.",
        )
    )
    startPurge: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_dosing;i=7061", browseName="ns=plastics_dosing;StartPurge", description="Method to start the purging function on the dosing system.")
    )
    stopDosing: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_dosing;i=7006", browseName="ns=plastics_dosing;StopDosing", description="Method to stop dosing immediately.")
    )
    stopDosingAfterCycle: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_dosing;i=7007",
            browseName="ns=plastics_dosing;StopDosingAfterCycle",
            description="Method to stop dosing after the current dosing cycle (e.g. to get a valid batch mix with batch blending).",
        )
    )
    throughput: plastics_rubber.objtypes.ControlledParameterType | None


@o6.objecttype(
    nodeId="ns=plastics_dosing;i=1009",
    browseName="ns=plastics_dosing;ComponentType",
    displayName="ComponentType",
    description="The ComponentType represents a device which brings material into the dosing system.",
    isAbstract=True,
)
class ComponentType(ns0.objtypes.BaseObjectType):
    abortCalibration: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_dosing;i=7073", browseName="ns=plastics_dosing;AbortCalibration", description="Abort the current calibration sequence for this component.")
    )
    abortCleaning: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_dosing;i=7019", browseName="ns=plastics_dosing;AbortCleaning", description="Method without arguments to abort the current cleaning sequence.")
    )
    bulkDensity: ns0.vartypes.AnalogUnitType | None
    dosingMode: ns0.vartypes.MultiStateValueDiscreteType
    electricalEnergy: plastics_rubber.objtypes.EnergyType | None
    feedRateScalingFactor: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_dosing;i=6068",
            browseName="ns=plastics_dosing;FeedRateScalingFactor",
            description="Material-specific output of the Component per DrivePercentage.",
            dataType=o6.Double,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    identifyComponent: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_dosing;i=7017",
            browseName="ns=plastics_dosing;IdentifyComponent",
            description="The dosing component on which this method is called shows itself by e.g. activation of a LED.",
        )
    )
    isActive: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_dosing;i=6065",
            browseName="ns=plastics_dosing;IsActive",
            description="Provides information if the dosing component is active in the current production.",
            dataType=o6.Boolean,
        )
    )
    isPresent: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_dosing;i=6064",
            browseName="ns=plastics_dosing;IsPresent",
            description="Indicates if the hardware of this component is installed.",
            dataType=o6.Boolean,
        )
    )
    levels: LevelsType | None
    material: DosingMaterialType | None
    materialConsumption: MaterialConsumptionType | None
    setActive: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_dosing;i=6066",
            browseName="ns=plastics_dosing;SetActive",
            description="Activates the dosing component for the current production.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    startCalibration: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_dosing;i=7024", browseName="ns=plastics_dosing;StartCalibration", description="Start the automated calibration sequence for this component.")
    )
    startCleaning: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_dosing;i=7018", browseName="ns=plastics_dosing;StartCleaning", description="Start the automated cleaning sequence for this component.")
    )
    state: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_dosing;i=6067",
            browseName="ns=plastics_dosing;State",
            description="The actual working state of the component.",
            dataType=plastics_dosing_datypes.ComponentStateEnumeration,
        )
    )
    throughput: plastics_rubber.objtypes.ControlledParameterType | None
    weight: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(
    nodeId="ns=plastics_dosing;i=1006",
    browseName="ns=plastics_dosing;ContinuousComponentType",
    displayName="ContinuousComponentType",
    description="Describes Components, where the materials are fed to the production machine in a continuous flow instead of batches.",
)
class ContinuousComponentType(ComponentType):
    drivePercentage: plastics_rubber.objtypes.ControlledParameterType | None
    percentage: plastics_rubber.objtypes.ControlledParameterType | None
    startPriming: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_dosing;i=7062", browseName="ns=plastics_dosing;StartPriming", description="Method to start the priming function on the component.")
    )
    stopPriming: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_dosing;i=7063", browseName="ns=plastics_dosing;StopPriming", description="Method to stop the priming function on the component.")
    )
    weighingProcess: WeighingProcessType | None


@o6.objecttype(
    nodeId="ns=plastics_dosing;i=1015",
    browseName="ns=plastics_dosing;BatchComponentType",
    displayName="BatchComponentType",
    description="Describes Components, where the materials are fed to the production machine in batches e.g. prepared by a batch blender.",
)
class BatchComponentType(ComponentType):
    percentage: plastics_rubber.objtypes.ControlledParameterType


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, plastics_rubber, plastics_dosing_datypes
