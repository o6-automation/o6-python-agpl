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

"""Generated OPC UA laser_systems namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.isa95_jobcontrol_v2 as isa95_jobcontrol_v2
import o6.ns.machine_tool as machine_tool
import o6.ns.machinery as machinery
import o6.ns.machinery_jobs as machinery_jobs
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=laser_systems;i=1002", browseName="ns=laser_systems;LaserSystemMonitoringType", displayName="LaserSystemMonitoringType")
class LaserSystemMonitoringType(ns0.objtypes.BaseObjectType):
    activityData: ns0.objtypes.OrderedListType | None
    conditionData: ns0.objtypes.FolderType | None
    consumptionData: ns0.objtypes.FolderType | None
    laserSystemStatus: LaserSystemStatusType
    stacklight: ia.objtypes.BasicStacklightType | None


@o6.objecttype(nodeId="ns=laser_systems;i=1003", browseName="ns=laser_systems;LaserSystemProductionType", displayName="LaserSystemProductionType")
class LaserSystemProductionType(ns0.objtypes.BaseObjectType):
    recipeSettingsAndOverviews: ns0.objtypes.FolderType | None


@o6.objecttype(nodeId="ns=laser_systems;i=1012", browseName="ns=laser_systems;LaserSystemStatusType", displayName="LaserSystemStatusType")
class LaserSystemStatusType(ns0.objtypes.BaseObjectType):
    laserSystemState: LaserSystemState_StateMachineType
    machineToolsLaserStatus: machine_tool.objtypes.LaserMonitoringType
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType
    machineryOperationMode: machinery.objtypes.MachineryOperationModeStateMachineType
    operationCounters: LaserSystemOperationCounterType


ns0.objtypes.FolderType(nodeId="ns=laser_systems;i=5103", browseName="ns=machinery;MachineryBuildingBlocks")


@o6.objecttype(nodeId="ns=laser_systems;i=1005", browseName="ns=laser_systems;LaserSystemType", displayName="LaserSystemType")
class LaserSystemType(ns0.objtypes.BaseObjectType):
    identification: machinery.objtypes.MachineryComponentIdentificationType
    machineryBuildingBlocks: ns0.objtypes.FolderType = o6.hasComponent(o6.ns["ns=laser_systems;i=5103"])
    monitoring: LaserSystemMonitoringType
    notification: machine_tool.objtypes.NotificationType = o6.hasComponent(
        machine_tool.objtypes.NotificationType(nodeId="ns=laser_systems;i=5011", browseName="ns=machine_tool;Notification")
    )
    production: LaserSystemProductionType = o6.hasComponent(LaserSystemProductionType(nodeId="ns=laser_systems;i=5012", browseName="ns=laser_systems;Production"))


@o6.objecttype(nodeId="ns=laser_systems;i=1004", browseName="ns=laser_systems;ConsumptionDataMonitoringType", displayName="ConsumptionDataMonitoringType")
class ConsumptionDataMonitoringType(machine_tool.objtypes.ElementMonitoringType):
    consumableIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6001", browseName="ns=laser_systems;ConsumableIdentifier", dataType=o6.String)
    )
    description: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=laser_systems;i=6002", browseName="ns=laser_systems;Description", dataType=o6.LocalizedText, value=o6.LocalizedText("Description of consumption data", "en")
        )
    )
    value: ns0.vartypes.AnalogUnitType


@o6.objecttype(
    nodeId="ns=laser_systems;i=1010",
    browseName="ns=laser_systems;LaserSystemOperationCounterType",
    displayName="LaserSystemOperationCounterType",
    interfaces=[di.objtypes.IOperationCounterType],
)
class LaserSystemOperationCounterType(machinery.objtypes.MachineryOperationCounterType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=laser_systems;i=6027",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("di:OperationCounters"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    operationDuration: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6042", browseName="ns=di;OperationDuration", dataType=ns0.datatypes.Duration)
    )
    powerOnDuration: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6041", browseName="ns=di;PowerOnDuration", dataType=ns0.datatypes.Duration)
    )


@o6.objecttype(
    nodeId="ns=laser_systems;i=1008",
    browseName="ns=laser_systems;ActivityDataMonitoringType",
    displayName="ActivityDataMonitoringType",
    interfaces=[ns0.objtypes.IOrderedObjectType],
)
class ActivityDataMonitoringType(machine_tool.objtypes.ElementMonitoringType):
    currentValue: ns0.vartypes.AnalogUnitType
    description: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=laser_systems;i=6062", browseName="ns=laser_systems;Description", dataType=o6.LocalizedText, value=o6.LocalizedText("Description of activity data", "en")
        )
    )
    numberInList: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6024", browseName="NumberInList", dataType=o6.UInt16))
    parameterIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6009", browseName="ns=laser_systems;ParameterIdentifier", dataType=o6.String, value="ID987")
    )
    previousValue: ns0.vartypes.AnalogUnitType | None


@o6.objecttype(nodeId="ns=laser_systems;i=1006", browseName="ns=laser_systems;ConditionDataMonitoringType", displayName="ConditionDataMonitoringType")
class ConditionDataMonitoringType(machine_tool.objtypes.ElementMonitoringType):
    conditionParameterIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6005", browseName="ns=laser_systems;ConditionParameterIdentifier", dataType=o6.String, value="ID123")
    )
    description: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=laser_systems;i=6070",
            browseName="ns=laser_systems;Description",
            dataType=o6.LocalizedText,
            value=o6.LocalizedText("Description of Condition Parameter", "en"),
        )
    )
    lowerErrorLevel: ns0.vartypes.AnalogUnitType | None
    lowerWarningLevel: ns0.vartypes.AnalogUnitType | None
    upperErrorLevel: ns0.vartypes.AnalogUnitType | None
    upperWarningLevel: ns0.vartypes.AnalogUnitType | None
    value: ns0.vartypes.AnalogUnitType


@o6.objecttype(nodeId="ns=laser_systems;i=1007", browseName="ns=laser_systems;RecipeSettingsAndOverviewType", displayName="RecipeSettingsAndOverviewType")
class RecipeSettingsAndOverviewType(ns0.objtypes.BaseObjectType):
    creationDate: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6074", browseName="ns=laser_systems;CreationDate", dataType=ns0.datatypes.UtcTime)
    )
    description: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=laser_systems;i=6075", browseName="ns=laser_systems;Description", dataType=o6.LocalizedText)
    )
    lastModification: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6073", browseName="ns=laser_systems;LastModification", dataType=ns0.datatypes.UtcTime)
    )
    lastUsage: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6014", browseName="ns=laser_systems;LastUsage", dataType=ns0.datatypes.UtcTime)
    )
    recipeIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6072", browseName="ns=laser_systems;RecipeIdentifier", dataType=o6.String)
    )
    recipeName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6071", browseName="ns=laser_systems;RecipeName", dataType=o6.String)
    )
    recipeRevision: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6016", browseName="ns=laser_systems;RecipeRevision", dataType=o6.String)
    )
    runsCompleted: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=laser_systems;i=6015", browseName="ns=laser_systems;RunsCompleted", dataType=o6.UInt64)
    )


@o6.objecttype(nodeId="ns=laser_systems;i=1013", browseName="ns=laser_systems;LaserSystemMaintenancePrognosisType", displayName="LaserSystemMaintenancePrognosisType")
class LaserSystemMaintenancePrognosisType(machine_tool.objtypes.MaintenancePrognosisType):
    code: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6077", browseName="ns=laser_systems;Code", dataType=o6.String))
    description: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=laser_systems;i=6076", browseName="ns=laser_systems;Description", dataType=o6.LocalizedText)
    )


@o6.objecttype(nodeId="ns=laser_systems;i=1014", browseName="ns=laser_systems;LaserSystemUtilityChangePrognosisType", displayName="LaserSystemUtilityChangePrognosisType")
class LaserSystemUtilityChangePrognosisType(machine_tool.objtypes.UtilityChangePrognosisType):
    code: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=laser_systems;i=6079", browseName="ns=laser_systems;Code", dataType=o6.String))
    description: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=laser_systems;i=6078", browseName="ns=laser_systems;Description", dataType=o6.LocalizedText)
    )


@o6.objecttype(nodeId="ns=laser_systems;i=1009", browseName="ns=laser_systems;LaserSystemState_StateMachineType", displayName="LaserSystemState_StateMachineType")
class LaserSystemState_StateMachineType(ns0.objtypes.FiniteStateMachineType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=laser_systems;i=6152",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("laser_systems:LaserSystemState"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    energySaving: ns0.objtypes.StateType
    error: ns0.objtypes.StateType
    fromEnergySavingToEnergySaving: ns0.objtypes.TransitionType
    fromEnergySavingToError: ns0.objtypes.TransitionType
    fromEnergySavingToIdle: ns0.objtypes.TransitionType
    fromEnergySavingToLaserOn: ns0.objtypes.TransitionType
    fromEnergySavingToLaserReady: ns0.objtypes.TransitionType
    fromEnergySavingToMaintenance: ns0.objtypes.TransitionType
    fromEnergySavingToOff: ns0.objtypes.TransitionType
    fromEnergySavingToSetUp: ns0.objtypes.TransitionType
    fromErrorToEnergySaving: ns0.objtypes.TransitionType
    fromErrorToError: ns0.objtypes.TransitionType
    fromErrorToIdle: ns0.objtypes.TransitionType
    fromErrorToLaserOn: ns0.objtypes.TransitionType
    fromErrorToLaserReady: ns0.objtypes.TransitionType
    fromErrorToMaintenance: ns0.objtypes.TransitionType
    fromErrorToOff: ns0.objtypes.TransitionType
    fromErrorToSetUp: ns0.objtypes.TransitionType
    fromIdleToEnergySaving: ns0.objtypes.TransitionType
    fromIdleToError: ns0.objtypes.TransitionType
    fromIdleToIdle: ns0.objtypes.TransitionType
    fromIdleToLaserOn: ns0.objtypes.TransitionType
    fromIdleToLaserReady: ns0.objtypes.TransitionType
    fromIdleToMaintenance: ns0.objtypes.TransitionType
    fromIdleToOff: ns0.objtypes.TransitionType
    fromIdleToSetUp: ns0.objtypes.TransitionType
    fromLaserOnToEnergySaving: ns0.objtypes.TransitionType
    fromLaserOnToError: ns0.objtypes.TransitionType
    fromLaserOnToIdle: ns0.objtypes.TransitionType
    fromLaserOnToLaserOn: ns0.objtypes.TransitionType
    fromLaserOnToLaserReady: ns0.objtypes.TransitionType
    fromLaserOnToMaintenance: ns0.objtypes.TransitionType
    fromLaserOnToOff: ns0.objtypes.TransitionType
    fromLaserOnToSetUp: ns0.objtypes.TransitionType
    fromLaserReadyToEnergySaving: ns0.objtypes.TransitionType
    fromLaserReadyToError: ns0.objtypes.TransitionType
    fromLaserReadyToIdle: ns0.objtypes.TransitionType
    fromLaserReadyToLaserOn: ns0.objtypes.TransitionType
    fromLaserReadyToLaserReady: ns0.objtypes.TransitionType
    fromLaserReadyToMaintenance: ns0.objtypes.TransitionType
    fromLaserReadyToOff: ns0.objtypes.TransitionType
    fromLaserReadyToSetUp: ns0.objtypes.TransitionType
    fromMaintenanceToEnergySaving: ns0.objtypes.TransitionType
    fromMaintenanceToError: ns0.objtypes.TransitionType
    fromMaintenanceToIdle: ns0.objtypes.TransitionType
    fromMaintenanceToLaserOn: ns0.objtypes.TransitionType
    fromMaintenanceToLaserReady: ns0.objtypes.TransitionType
    fromMaintenanceToMaintenance: ns0.objtypes.TransitionType
    fromMaintenanceToOff: ns0.objtypes.TransitionType
    fromMaintenanceToSetUp: ns0.objtypes.TransitionType
    fromOffToEnergySaving: ns0.objtypes.TransitionType
    fromOffToError: ns0.objtypes.TransitionType
    fromOffToIdle: ns0.objtypes.TransitionType
    fromOffToLaserOn: ns0.objtypes.TransitionType
    fromOffToLaserReady: ns0.objtypes.TransitionType
    fromOffToMaintenance: ns0.objtypes.TransitionType
    fromOffToOff: ns0.objtypes.TransitionType
    fromOffToSetUp: ns0.objtypes.TransitionType
    fromSetUpToEnergySaving: ns0.objtypes.TransitionType
    fromSetUpToError: ns0.objtypes.TransitionType
    fromSetUpToIdle: ns0.objtypes.TransitionType
    fromSetUpToLaserOn: ns0.objtypes.TransitionType
    fromSetUpToLaserReady: ns0.objtypes.TransitionType
    fromSetUpToMaintenance: ns0.objtypes.TransitionType
    fromSetUpToOff: ns0.objtypes.TransitionType
    fromSetUpToSetUp: ns0.objtypes.TransitionType
    idle: ns0.objtypes.StateType
    laserOn: ns0.objtypes.StateType
    laserReady: ns0.objtypes.StateType
    maintenance: ns0.objtypes.StateType
    off: ns0.objtypes.StateType
    setUp: ns0.objtypes.StateType


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machine_tool, machinery, machinery_jobs, ns0
