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

"""Generated OPC UA surface_technology_plasma namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=surface_technology_plasma;i=1008",
    browseName="ns=surface_technology_plasma;LowPressurePlasmaMachineryItemState_StateMachineType",
    displayName="LowPressurePlasmaMachineryItemState_StateMachineType",
)
class LowPressurePlasmaMachineryItemState_StateMachineType(machinery.objtypes.MachineryItemState_StateMachineType):
    lowPressurePlasmaNotExecutingSubState: LowPressurePlasmaNotExecutingSubState_StateMachineType


@o6.objecttype(
    nodeId="ns=surface_technology_plasma;i=1010",
    browseName="ns=surface_technology_plasma;AtmosphericPressurePlasmaMachineryItemState_StateMachineType",
    displayName="AtmosphericPressurePlasmaMachineryItemState_StateMachineType",
)
class AtmosphericPressurePlasmaMachineryItemState_StateMachineType(machinery.objtypes.MachineryItemState_StateMachineType):
    atmosphericPressurePlasmaNotExecutingSubState: AtmosphericPressurePlasmaNotExecutingSubState_StateMachineType


@o6.objecttype(nodeId="ns=surface_technology_plasma;i=1017", browseName="ns=surface_technology_plasma;CirculationSystemType", displayName="CirculationSystemType")
class CirculationSystemType(ns0.objtypes.BaseObjectType):
    coolingCircuitFlowRate: ns0.vartypes.AnalogUnitType | None
    coolingCircuitTemperatureOutlet: ns0.vartypes.AnalogUnitType | None


ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5010", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(nodeId="ns=surface_technology_plasma;i=1003", browseName="ns=surface_technology_plasma;PlasmaSurfaceMachineType", displayName="PlasmaSurfaceMachineType")
class PlasmaSurfaceMachineType(ns0.objtypes.BaseObjectType):
    components: machinery.objtypes.MachineComponentsType
    identification: machinery.objtypes.MachineIdentificationType
    jobManagement: machinery_jobs.objtypes.JobManagementType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5010"])
    monitoring: machinery.objtypes.MonitoringType


@o6.objecttype(
    nodeId="ns=surface_technology_plasma;i=1006", browseName="ns=surface_technology_plasma;LowPressurePlasmaSurfaceMachineType", displayName="LowPressurePlasmaSurfaceMachineType"
)
class LowPressurePlasmaSurfaceMachineType(PlasmaSurfaceMachineType):
    components: machinery.objtypes.MachineComponentsType
    monitoring: machinery.objtypes.MonitoringType


@o6.objecttype(
    nodeId="ns=surface_technology_plasma;i=1009",
    browseName="ns=surface_technology_plasma;AtmosphericPressurePlasmaSurfaceMachineType",
    displayName="AtmosphericPressurePlasmaSurfaceMachineType",
)
class AtmosphericPressurePlasmaSurfaceMachineType(PlasmaSurfaceMachineType):
    components: machinery.objtypes.MachineComponentsType
    monitoring: machinery.objtypes.MonitoringType


ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5032", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(nodeId="ns=surface_technology_plasma;i=1004", browseName="ns=surface_technology_plasma;PlasmaGeneratorType", displayName="PlasmaGeneratorType")
class PlasmaGeneratorType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5032"])
    monitoring: machinery.objtypes.MonitoringType


ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5038", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(nodeId="ns=surface_technology_plasma;i=1005", browseName="ns=surface_technology_plasma;PrecursorSystemType", displayName="PrecursorSystemType")
class PrecursorSystemType(ns0.objtypes.BaseObjectType):
    components: machinery.objtypes.MachineComponentsType
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5038"])
    monitoring: machinery.objtypes.MonitoringType


ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5044", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(nodeId="ns=surface_technology_plasma;i=1007", browseName="ns=surface_technology_plasma;GasSystemType", displayName="GasSystemType")
class GasSystemType(ns0.objtypes.BaseObjectType):
    components: machinery.objtypes.MachineComponentsType
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5044"])
    monitoring: machinery.objtypes.MonitoringType


ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5050", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(nodeId="ns=surface_technology_plasma;i=1014", browseName="ns=surface_technology_plasma;PlantCoolingSystemType", displayName="PlantCoolingSystemType")
class PlantCoolingSystemType(ns0.objtypes.BaseObjectType):
    components: machinery.objtypes.MachineComponentsType
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5050"])
    monitoring: machinery.objtypes.MonitoringType


ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5056", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(nodeId="ns=surface_technology_plasma;i=1020", browseName="ns=surface_technology_plasma;ProcessingChamberType", displayName="ProcessingChamberType")
class ProcessingChamberType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5056"])
    monitoring: machinery.objtypes.MonitoringType


ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5060", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(nodeId="ns=surface_technology_plasma;i=1023", browseName="ns=surface_technology_plasma;HeatingSystemType", displayName="HeatingSystemType")
class HeatingSystemType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5060"])
    monitoring: machinery.objtypes.MonitoringType


ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5064", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(nodeId="ns=surface_technology_plasma;i=1026", browseName="ns=surface_technology_plasma;WorkpieceMotionDeviceType", displayName="WorkpieceMotionDeviceType")
class WorkpieceMotionDeviceType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5064"])
    monitoring: machinery.objtypes.MonitoringType


ns0.objtypes.FolderType(nodeId="ns=surface_technology_plasma;i=5070", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(nodeId="ns=surface_technology_plasma;i=1029", browseName="ns=surface_technology_plasma;PlasmaJetType", displayName="PlasmaJetType")
class PlasmaJetType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryComponentIdentificationType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=surface_technology_plasma;i=5070"])
    monitoring: machinery.objtypes.MonitoringType


@o6.objecttype(nodeId="ns=surface_technology_plasma;i=1011", browseName="ns=surface_technology_plasma;RegulatorType", displayName="RegulatorType")
class RegulatorType(ns0.objtypes.BaseObjectType):
    correctionFactor: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=surface_technology_plasma;i=6087", browseName="ns=surface_technology_plasma;CorrectionFactor", dataType=o6.Double, accessLevel=3, userAccessLevel=1
        )
    )
    gasConsumption: ns0.vartypes.AnalogUnitType | None
    gasFlow: ns0.vartypes.AnalogUnitType | None
    heaterTemperature: ns0.vartypes.AnalogUnitType | None
    jetHeadTemperature: ns0.vartypes.AnalogUnitType | None
    precursorMassFlow: ns0.vartypes.AnalogUnitType | None
    precursorVolumeFlow: ns0.vartypes.AnalogUnitType | None
    tFittingTemperature: ns0.vartypes.AnalogUnitType | None
    typeOfGas: ns0.vartypes.MultiStateValueDiscreteType | None
    typeOfPrecursorFluid: ns0.vartypes.MultiStateValueDiscreteType | None


@o6.objecttype(
    nodeId="ns=surface_technology_plasma;i=1013",
    browseName="ns=surface_technology_plasma;LowPressurePlasmaNotExecutingSubState_StateMachineType",
    displayName="LowPressurePlasmaNotExecutingSubState_StateMachineType",
)
class LowPressurePlasmaNotExecutingSubState_StateMachineType(ns0.objtypes.FiniteStateMachineType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=surface_technology_plasma;i=6166",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("LowPressurePlasmaNotExecutingSubState"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    fromStandbyToVented: ns0.objtypes.TransitionType
    fromVentedToStandby: ns0.objtypes.TransitionType
    standby: ns0.objtypes.StateType
    vented: ns0.objtypes.StateType


@o6.objecttype(
    nodeId="ns=surface_technology_plasma;i=1016",
    browseName="ns=surface_technology_plasma;AtmosphericPressurePlasmaNotExecutingSubState_StateMachineType",
    displayName="AtmosphericPressurePlasmaNotExecutingSubState_StateMachineType",
)
class AtmosphericPressurePlasmaNotExecutingSubState_StateMachineType(ns0.objtypes.FiniteStateMachineType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=surface_technology_plasma;i=6173",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("AtmosphericPressurePlasmaNotExecutingSubState"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    fromIdleToStandby: ns0.objtypes.TransitionType
    fromStandbyToIdle: ns0.objtypes.TransitionType
    idle: ns0.objtypes.StateType
    standby: ns0.objtypes.StateType


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0
