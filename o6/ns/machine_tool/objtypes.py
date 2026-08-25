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

"""Generated OPC UA machine_tool namespace declarations."""

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
from . import datatypes as machine_tool_datypes
from . import vartypes as machine_tool_vartypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(nodeId="ns=machine_tool;i=11", browseName="ns=machine_tool;MachineToolIdentificationType", displayName="MachineToolIdentificationType")
class MachineToolIdentificationType(machinery.objtypes.MachineIdentificationType):
    softwareIdentification: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=machine_tool;i=14", browseName="ns=machine_tool;MonitoringType", displayName="MonitoringType")
class MonitoringType(ns0.objtypes.BaseObjectType):
    langleMonitoredElementRangle: ElementMonitoringType | None
    machineTool: MachineOperationMonitoringType
    stacklight: ia.objtypes.BasicStacklightType | None


@o6.objecttype(nodeId="ns=machine_tool;i=24", browseName="ns=machine_tool;ProductionStateMachineType", displayName="ProductionStateMachineType")
class ProductionStateMachineType(ns0.objtypes.FiniteStateMachineType):
    aborted: ns0.objtypes.StateType
    abortedToInitializing: ns0.objtypes.TransitionType
    currentState: ns0.vartypes.FiniteStateVariableType
    ended: ns0.objtypes.StateType
    endedToInitializing: ns0.objtypes.TransitionType
    initializing: ns0.objtypes.InitialStateType
    initializingToAborted: ns0.objtypes.TransitionType
    initializingToRunning: ns0.objtypes.TransitionType
    interrupted: ns0.objtypes.StateType
    interruptedToAborted: ns0.objtypes.TransitionType
    interruptedToRunning: ns0.objtypes.TransitionType
    lastTransition: ns0.vartypes.FiniteTransitionVariableType | None
    running: ns0.objtypes.StateType
    runningToAborted: ns0.objtypes.TransitionType
    runningToEnded: ns0.objtypes.TransitionType
    runningToInterrupted: ns0.objtypes.TransitionType
    runningToRunning: ns0.objtypes.TransitionType


@o6.objecttype(nodeId="ns=machine_tool;i=15", browseName="ns=machine_tool;ProductionProgramStateMachineType", displayName="ProductionProgramStateMachineType")
class ProductionProgramStateMachineType(ProductionStateMachineType):
    aborted: ns0.objtypes.StateType
    abortedToInitializing: ns0.objtypes.TransitionType
    ended: ns0.objtypes.StateType
    endedToInitializing: ns0.objtypes.TransitionType
    initializing: ns0.objtypes.InitialStateType
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


@o6.objecttype(nodeId="ns=machine_tool;i=28", browseName="ns=machine_tool;ProductionJobStateMachineType", displayName="ProductionJobStateMachineType")
class ProductionJobStateMachineType(ProductionStateMachineType):
    aborted: ns0.objtypes.StateType
    abortedToInitializing: ns0.objtypes.TransitionType
    ended: ns0.objtypes.StateType
    endedToInitializing: ns0.objtypes.TransitionType
    initializing: ns0.objtypes.InitialStateType
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


@o6.objecttype(nodeId="ns=machine_tool;i=30", browseName="ns=machine_tool;ProductionJobListType", displayName="ProductionJobListType")
class ProductionJobListType(ns0.objtypes.OrderedListType):
    langleOrderedObjectRangle: ProductionJobType | None


@o6.objecttype(nodeId="ns=machine_tool;i=38", browseName="ns=machine_tool;MessagesType", displayName="MessagesType")
class MessagesType(ns0.objtypes.BaseObjectType):
    pass


@o6.objecttype(nodeId="ns=machine_tool;i=40", browseName="ns=machine_tool;ProductionPartStateMachineType", displayName="ProductionPartStateMachineType")
class ProductionPartStateMachineType(ProductionStateMachineType):
    aborted: ns0.objtypes.StateType
    abortedToInitializing: ns0.objtypes.TransitionType
    ended: ns0.objtypes.StateType
    endedToInitializing: ns0.objtypes.TransitionType
    initializing: ns0.objtypes.InitialStateType
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


@o6.objecttype(nodeId="ns=machine_tool;i=47", browseName="ns=machine_tool;OperatorConditionClassType", displayName="OperatorConditionClassType", isAbstract=True)
class OperatorConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


@o6.objecttype(nodeId="ns=machine_tool;i=48", browseName="ns=machine_tool;ClampingConditionClassType", displayName="ClampingConditionClassType", isAbstract=True)
class ClampingConditionClassType(ns0.objtypes.ProcessConditionClassType):
    pass


@o6.objecttype(nodeId="ns=machine_tool;i=52", browseName="ns=machine_tool;ManualProcessStepConditionClassType", displayName="ManualProcessStepConditionClassType", isAbstract=True)
class ManualProcessStepConditionClassType(ns0.objtypes.ProcessConditionClassType):
    pass


@o6.objecttype(nodeId="ns=machine_tool;i=53", browseName="ns=machine_tool;MeasurementConditionClassType", displayName="MeasurementConditionClassType", isAbstract=True)
class MeasurementConditionClassType(ns0.objtypes.ProcessConditionClassType):
    pass


@o6.objecttype(nodeId="ns=machine_tool;i=54", browseName="ns=machine_tool;PartMissingConditionClassType", displayName="PartMissingConditionClassType", isAbstract=True)
class PartMissingConditionClassType(ns0.objtypes.ProcessConditionClassType):
    pass


@o6.objecttype(
    nodeId="ns=machine_tool;i=55", browseName="ns=machine_tool;ProcessIrregularityConditionClassType", displayName="ProcessIrregularityConditionClassType", isAbstract=True
)
class ProcessIrregularityConditionClassType(ns0.objtypes.ProcessConditionClassType):
    pass


@o6.objecttype(nodeId="ns=machine_tool;i=57", browseName="ns=machine_tool;ToolBreakageConditionClassType", displayName="ToolBreakageConditionClassType", isAbstract=True)
class ToolBreakageConditionClassType(ns0.objtypes.ProcessConditionClassType):
    pass


@o6.objecttype(nodeId="ns=machine_tool;i=58", browseName="ns=machine_tool;ToolChangeConditionClassType", displayName="ToolChangeConditionClassType", isAbstract=True)
class ToolChangeConditionClassType(ns0.objtypes.ProcessConditionClassType):
    pass


@o6.objecttype(nodeId="ns=machine_tool;i=60", browseName="ns=machine_tool;UtilityConditionClassType", displayName="UtilityConditionClassType", isAbstract=True)
class UtilityConditionClassType(ns0.objtypes.BaseConditionClassType):
    pass


ProductionJobListType(nodeId="ns=machine_tool;i=81", browseName="ns=machine_tool;ProductionPlan")


@o6.objecttype(nodeId="ns=machine_tool;i=21", browseName="ns=machine_tool;ProductionType", displayName="ProductionType")
class ProductionType(ns0.objtypes.BaseObjectType):
    activeProgram: ProductionActiveProgramType
    productionPlan: ProductionJobListType | None = o6.hasComponent(o6.ns["ns=machine_tool;i=81"])
    statistics: ProductionStatisticsType | None


MessagesType(nodeId="ns=machine_tool;i=90", browseName="ns=machine_tool;Messages", eventNotifier=1)


@o6.objecttype(nodeId="ns=machine_tool;i=3", browseName="ns=machine_tool;PrognosisType", displayName="PrognosisType", isAbstract=True)
class PrognosisType(ns0.objtypes.BaseObjectType):
    predictedTime: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_tool;i=162", browseName="ns=machine_tool;PredictedTime", dataType=ns0.datatypes.UtcTime, value=o6.DateTime("2000-01-01T00:00:00Z")
        )
    )


@o6.objecttype(nodeId="ns=machine_tool;i=9", browseName="ns=machine_tool;MaintenancePrognosisType", displayName="MaintenancePrognosisType")
class MaintenancePrognosisType(PrognosisType):
    activity: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=170", browseName="ns=machine_tool;Activity", dataType=o6.LocalizedText)
    )


@o6.objecttype(nodeId="ns=machine_tool;i=10", browseName="ns=machine_tool;ManualActivityPrognosisType", displayName="ManualActivityPrognosisType")
class ManualActivityPrognosisType(PrognosisType):
    activity: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=171", browseName="ns=machine_tool;Activity", dataType=o6.LocalizedText)
    )


@o6.objecttype(nodeId="ns=machine_tool;i=43", browseName="ns=machine_tool;SoftwareIdentificationType", displayName="SoftwareIdentificationType")
class SoftwareIdentificationType(ns0.objtypes.BaseObjectType):
    identifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=185", browseName="ns=machine_tool;Identifier", dataType=o6.String, value="0")
    )
    manufacturer: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=186", browseName="ns=di;Manufacturer", dataType=o6.LocalizedText)
    )
    softwareRevision: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=184", browseName="ns=di;SoftwareRevision", dataType=o6.String, value="0")
    )


@o6.objecttype(nodeId="ns=machine_tool;i=59", browseName="ns=machine_tool;ProductionProgramType", displayName="ProductionProgramType", interfaces=[ns0.objtypes.IOrderedObjectType])
class ProductionProgramType(ns0.objtypes.BaseObjectType):
    name: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=193", browseName="ns=machine_tool;Name", dataType=o6.String))
    numberInList: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=230", browseName="NumberInList", dataType=o6.UInt16))
    state: ProductionProgramStateMachineType | None


@o6.objecttype(nodeId="ns=machine_tool;i=39", browseName="ns=machine_tool;AlertType", displayName="AlertType")
class AlertType(ns0.objtypes.AlarmConditionType):
    errorCode: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=231", browseName="ns=machine_tool;ErrorCode", dataType=o6.String))


o6.reference(MessagesType, "i=41", AlertType)
o6.reference(o6.ns["ns=machine_tool;i=90"], "i=41", AlertType)


@o6.objecttype(nodeId="ns=machine_tool;i=35", browseName="ns=machine_tool;NotificationEventType", displayName="NotificationEventType", isAbstract=True)
class NotificationEventType(ns0.objtypes.BaseEventType):
    identifier: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=232", browseName="ns=machine_tool;Identifier", dataType=o6.String))


o6.reference(MessagesType, "i=41", NotificationEventType)
o6.reference(o6.ns["ns=machine_tool;i=90"], "i=41", NotificationEventType)


@o6.objecttype(nodeId="ns=machine_tool;i=23", browseName="ns=machine_tool;ElementMonitoringType", displayName="ElementMonitoringType", isAbstract=True)
class ElementMonitoringType(ns0.objtypes.BaseObjectType):
    name: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=234", browseName="ns=machine_tool;Name", dataType=o6.String))


@o6.objecttype(nodeId="ns=machine_tool;i=41", browseName="ns=machine_tool;WorkingUnitMonitoringType", displayName="WorkingUnitMonitoringType", isAbstract=True)
class WorkingUnitMonitoringType(ElementMonitoringType):
    pass


@o6.objecttype(nodeId="ns=machine_tool;i=19", browseName="ns=machine_tool;InterruptionConditionType", displayName="InterruptionConditionType", isAbstract=True)
class InterruptionConditionType(ns0.objtypes.ConditionType):
    isAutomated: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=244", browseName="ns=machine_tool;IsAutomated", dataType=o6.Boolean, value=False)
    )


o6.reference(ProductionJobStateMachineType, "i=41", InterruptionConditionType)


ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=261", browseName="ns=machine_tool;PowerOnDuration", dataType=o6.UInt32)


@o6.objecttype(nodeId="ns=machine_tool;i=49", browseName="ns=machine_tool;BaseToolType", displayName="BaseToolType", isAbstract=True)
class BaseToolType(ns0.objtypes.BaseObjectType):
    identifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=316", browseName="ns=machine_tool;Identifier", dataType=o6.String)
    )
    location: ns0.objtypes.BaseObjectType | None
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=176", browseName="ns=machine_tool;Name", dataType=o6.String))


@o6.objecttype(nodeId="ns=machine_tool;i=51", browseName="ns=machine_tool;MultiToolType", displayName="MultiToolType")
class MultiToolType(BaseToolType):
    langleToolRangle: ToolType | None


@o6.objecttype(nodeId="ns=machine_tool;i=44", browseName="ns=machine_tool;ToolListType", displayName="ToolListType")
class ToolListType(ns0.objtypes.BaseObjectType):
    langleToolRangle: BaseToolType | None = o6.hasComponent(
        BaseToolType(nodeId="ns=machine_tool;i=98", browseName="ns=machine_tool;<Tool>", modellingRule="OptionalPlaceholder", _allow_abstract=True)
    )
    nodeVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=213", browseName="NodeVersion", dataType=o6.String))


o6.reference(ToolListType, "i=41", "i=2133")


@o6.objecttype(nodeId="ns=machine_tool;i=12", browseName="ns=machine_tool;EquipmentType", displayName="EquipmentType")
class EquipmentType(ns0.objtypes.BaseObjectType):
    tools: ToolListType | None = o6.hasComponent(ToolListType(nodeId="ns=machine_tool;i=116", browseName="ns=machine_tool;Tools"))


@o6.objecttype(nodeId="ns=machine_tool;i=50", browseName="ns=machine_tool;ToolType", displayName="ToolType")
class ToolType(BaseToolType):
    controlIdentifier1: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=178", browseName="ns=machine_tool;ControlIdentifier1", dataType=o6.UInt32)
    )
    controlIdentifier2: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=220", browseName="ns=machine_tool;ControlIdentifier2", dataType=o6.UInt32)
    )
    controlIdentifierInterpretation: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=machine_tool;i=296", browseName="ns=machine_tool;ControlIdentifierInterpretation", dataType=machine_tool_datypes.ToolManagement
        )
    )
    lastUsage: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=319", browseName="ns=machine_tool;LastUsage", dataType=ns0.datatypes.UtcTime)
    )
    locked: ns0.vartypes.BaseDataVariableType
    plannedForOperating: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=322", browseName="ns=machine_tool;PlannedForOperating", dataType=o6.Boolean)
    )
    toolLife: ns0.objtypes.BaseObjectType | None


@o6.objecttype(nodeId="ns=machine_tool;i=36", browseName="ns=machine_tool;LaserMonitoringType", displayName="LaserMonitoringType")
class LaserMonitoringType(WorkingUnitMonitoringType):
    controllerIsOn: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=323", browseName="ns=machine_tool;ControllerIsOn", dataType=o6.Boolean, value=False)
    )
    laserState: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=324", browseName="ns=machine_tool;LaserState", dataType=machine_tool_datypes.LaserState)
    )


@o6.objecttype(nodeId="ns=machine_tool;i=16", browseName="ns=machine_tool;ChannelMonitoringType", displayName="ChannelMonitoringType")
class ChannelMonitoringType(ElementMonitoringType):
    channelMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=249", browseName="ns=machine_tool;ChannelMode", dataType=machine_tool_datypes.ChannelMode)
    )
    channelModifiers: ChannelModifierType | None
    channelState: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=332", browseName="ns=machine_tool;ChannelState", dataType=machine_tool_datypes.ChannelState)
    )
    feedOverride: ns0.vartypes.AnalogUnitRangeType
    rapidOverride: ns0.vartypes.AnalogUnitRangeType | None


@o6.objecttype(nodeId="ns=machine_tool;i=46", browseName="ns=machine_tool;CombinedChannelMonitoringType", displayName="CombinedChannelMonitoringType")
class CombinedChannelMonitoringType(ChannelMonitoringType):
    pass


@o6.objecttype(nodeId="ns=machine_tool;i=33", browseName="ns=machine_tool;ChannelModifierType", displayName="ChannelModifierType")
class ChannelModifierType(ns0.objtypes.BaseObjectType):
    blockSkip: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=248", browseName="ns=machine_tool;BlockSkip", dataType=o6.Boolean)
    )
    dryRun: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=340", browseName="ns=machine_tool;DryRun", dataType=o6.Boolean)
    )
    optionalStop: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=325", browseName="ns=machine_tool;OptionalStop", dataType=o6.Boolean)
    )
    singleStep: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=317", browseName="ns=machine_tool;SingleStep", dataType=o6.Boolean)
    )
    testMode: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=338", browseName="ns=machine_tool;TestMode", dataType=o6.Boolean)
    )


@o6.objecttype(nodeId="ns=machine_tool;i=2", browseName="ns=machine_tool;PrognosisListType", displayName="PrognosisListType")
class PrognosisListType(ns0.objtypes.BaseObjectType):
    langlePrognosisRangle: PrognosisType | None
    nodeVersion: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=341", browseName="NodeVersion", dataType=o6.String))


o6.reference(PrognosisListType, "i=41", "i=2133")


@o6.objecttype(nodeId="ns=machine_tool;i=7", browseName="ns=machine_tool;NotificationType", displayName="NotificationType")
class NotificationType(ns0.objtypes.BaseObjectType):
    messages: MessagesType | None = o6.hasComponent(o6.ns["ns=machine_tool;i=90"])
    prognoses: PrognosisListType | None = o6.hasComponent(PrognosisListType(nodeId="ns=machine_tool;i=96", browseName="ns=machine_tool;Prognoses"))


@o6.objecttype(
    nodeId="ns=machine_tool;i=17", browseName="ns=machine_tool;ProductionProgramTransitionEventType", displayName="ProductionProgramTransitionEventType", isAbstract=True
)
class ProductionProgramTransitionEventType(ns0.objtypes.TransitionEventType):
    jobIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=301", browseName="ns=machine_tool;JobIdentifier", dataType=o6.String)
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=344", browseName="ns=machine_tool;Name", dataType=o6.String))


@o6.objecttype(nodeId="ns=machine_tool;i=56", browseName="ns=machine_tool;ProductionPartType", displayName="ProductionPartType")
class ProductionPartType(ns0.objtypes.BaseObjectType):
    customerOrderIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=201", browseName="ns=machine_tool;CustomerOrderIdentifier", dataType=o6.String)
    )
    identifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=172", browseName="ns=machine_tool;Identifier", dataType=o6.String)
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=348", browseName="ns=machine_tool;Name", dataType=o6.String))
    partQuality: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=167", browseName="ns=machine_tool;PartQuality", dataType=machine_tool_datypes.PartQuality)
    )
    processIrregularity: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=302", browseName="ns=machine_tool;ProcessIrregularity", dataType=machine_tool_datypes.ProcessIrregularity)
    )
    state: ProductionPartStateMachineType | None


@o6.objecttype(nodeId="ns=machine_tool;i=8", browseName="ns=machine_tool;ProcessChangeoverPrognosisType", displayName="ProcessChangeoverPrognosisType")
class ProcessChangeoverPrognosisType(PrognosisType):
    activity: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=169", browseName="ns=machine_tool;Activity", dataType=o6.LocalizedText)
    )
    location: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=362", browseName="ns=machine_tool;Location", dataType=o6.LocalizedText)
    )


@o6.objecttype(nodeId="ns=machine_tool;i=6", browseName="ns=machine_tool;UtilityChangePrognosisType", displayName="UtilityChangePrognosisType")
class UtilityChangePrognosisType(PrognosisType):
    utilityName: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=363", browseName="ns=machine_tool;UtilityName", dataType=o6.String)
    )


@o6.objecttype(nodeId="ns=machine_tool;i=34", browseName="ns=machine_tool;ProductionPartSetType", displayName="ProductionPartSetType")
class ProductionPartSetType(ns0.objtypes.BaseObjectType):
    containsMixedParts: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=365", browseName="ns=machine_tool;ContainsMixedParts", dataType=o6.Boolean)
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=262", browseName="ns=machine_tool;Name", dataType=o6.String))
    partsCompletedPerRun: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=267", browseName="ns=machine_tool;PartsCompletedPerRun", dataType=o6.UInt32)
    )
    partsPerRun: ns0.objtypes.BaseObjectType | None
    partsPlannedPerRun: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=264", browseName="ns=machine_tool;PartsPlannedPerRun", dataType=o6.UInt32)
    )


@o6.objecttype(nodeId="ns=machine_tool;i=4", browseName="ns=machine_tool;ToolLoadPrognosisType", displayName="ToolLoadPrognosisType")
class ToolLoadPrognosisType(PrognosisType):
    location: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=163", browseName="ns=machine_tool;Location", dataType=o6.LocalizedText)
    )
    toolIdentifier: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=279", browseName="ns=machine_tool;ToolIdentifier", dataType=o6.String)
    )
    toolName: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=368", browseName="ns=machine_tool;ToolName", dataType=o6.String)
    )


@o6.objecttype(nodeId="ns=machine_tool;i=26", browseName="ns=machine_tool;MachineOperationMonitoringType", displayName="MachineOperationMonitoringType")
class MachineOperationMonitoringType(ns0.objtypes.BaseObjectType):
    feedOverride: ns0.vartypes.AnalogUnitRangeType | None
    isWarmUp: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=370", browseName="ns=machine_tool;IsWarmUp", dataType=o6.Boolean)
    )
    machineryItemState: machinery.objtypes.MachineryItemState_StateMachineType | None
    machineryOperationMode: MachineOperationModeStateMachineType | None
    obligation: ObligationType | None
    operationCounters: machinery.objtypes.MachineryOperationCounterType | None
    operationMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=225", browseName="ns=machine_tool;OperationMode", dataType=machine_tool_datypes.MachineOperationMode)
    )
    powerOnDuration: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=machine_tool;i=261"])


@o6.objecttype(nodeId="ns=machine_tool;i=22", browseName="ns=machine_tool;SpindleMonitoringType", displayName="SpindleMonitoringType")
class SpindleMonitoringType(WorkingUnitMonitoringType):
    isRotating: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=247", browseName="ns=machine_tool;IsRotating", dataType=o6.Boolean, value=False)
    )
    isUsedAsAxis: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=371", browseName="ns=machine_tool;IsUsedAsAxis", dataType=o6.Boolean)
    )
    override: ns0.vartypes.AnalogUnitRangeType | None


@o6.objecttype(nodeId="ns=machine_tool;i=32", browseName="ns=machine_tool;ProductionActiveProgramType", displayName="ProductionActiveProgramType")
class ProductionActiveProgramType(ProductionProgramType):
    jobIdentifier: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=384", browseName="ns=machine_tool;JobIdentifier", dataType=o6.String)
    )
    jobNodeId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=382", browseName="ns=machine_tool;JobNodeId", dataType=o6.NodeId)
    )
    state: ProductionProgramStateMachineType


@o6.objecttype(nodeId="ns=machine_tool;i=42", browseName="ns=machine_tool;EDMGeneratorMonitoringType", displayName="EDMGeneratorMonitoringType")
class EDMGeneratorMonitoringType(WorkingUnitMonitoringType):
    eDMGeneratorState: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=390", browseName="ns=machine_tool;EDMGeneratorState", dataType=machine_tool_datypes.EDMGeneratorState)
    )
    isOn: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=389", browseName="ns=machine_tool;IsOn", dataType=o6.Boolean)
    )


@o6.objecttype(nodeId="ns=machine_tool;i=45", browseName="ns=machine_tool;ToolChangePrognosisType", displayName="ToolChangePrognosisType")
class ToolChangePrognosisType(PrognosisType):
    location: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=218", browseName="ns=machine_tool;Location", dataType=o6.LocalizedText)
    )
    toolIdentifier: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=238", browseName="ns=machine_tool;ToolIdentifier", dataType=o6.String)
    )
    toolName: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=280", browseName="ns=machine_tool;ToolName", dataType=o6.String)
    )
    toolNodeId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=393", browseName="ns=machine_tool;ToolNodeId", dataType=o6.NodeId)
    )


@o6.objecttype(nodeId="ns=machine_tool;i=18", browseName="ns=machine_tool;ToolUnloadPrognosisType", displayName="ToolUnloadPrognosisType")
class ToolUnloadPrognosisType(PrognosisType):
    location: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=281", browseName="ns=machine_tool;Location", dataType=o6.LocalizedText)
    )
    toolIdentifier: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=282", browseName="ns=machine_tool;ToolIdentifier", dataType=o6.String)
    )
    toolName: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=369", browseName="ns=machine_tool;ToolName", dataType=o6.String)
    )
    toolNodeId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=394", browseName="ns=machine_tool;ToolNodeId", dataType=o6.NodeId)
    )


ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=395", browseName="ns=machine_tool;PartNodeId", dataType=o6.NodeId)


@o6.objecttype(nodeId="ns=machine_tool;i=5", browseName="ns=machine_tool;PartUnloadPrognosisType", displayName="PartUnloadPrognosisType")
class PartUnloadPrognosisType(PrognosisType):
    location: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=165", browseName="ns=machine_tool;Location", dataType=o6.LocalizedText)
    )
    partIdentifier: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=166", browseName="ns=machine_tool;PartIdentifier", dataType=o6.String)
    )
    partName: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=180", browseName="ns=machine_tool;PartName", dataType=o6.String)
    )
    partNodeId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=machine_tool;i=395"])


ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=401", browseName="ns=machine_tool;PartNodeId", dataType=o6.NodeId)


@o6.objecttype(nodeId="ns=machine_tool;i=27", browseName="ns=machine_tool;ProductionPartTransitionEventType", displayName="ProductionPartTransitionEventType", isAbstract=True)
class ProductionPartTransitionEventType(ns0.objtypes.TransitionEventType):
    customerOrderIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=404", browseName="ns=machine_tool;CustomerOrderIdentifier", dataType=o6.String)
    )
    identifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=173", browseName="ns=machine_tool;Identifier", dataType=o6.String)
    )
    jobIdentifier: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=300", browseName="ns=machine_tool;JobIdentifier", dataType=o6.String)
    )
    name: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=351", browseName="ns=machine_tool;Name", dataType=o6.String))
    partQuality: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=391", browseName="ns=machine_tool;PartQuality", dataType=machine_tool_datypes.PartQuality)
    )
    processIrregularity: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=403", browseName="ns=machine_tool;ProcessIrregularity", dataType=machine_tool_datypes.ProcessIrregularity)
    )


@o6.objecttype(nodeId="ns=machine_tool;i=20", browseName="ns=machine_tool;ProductionStatisticsType", displayName="ProductionStatisticsType")
class ProductionStatisticsType(ns0.objtypes.BaseObjectType):
    partsProducedInLifetime: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=405", browseName="ns=machine_tool;PartsProducedInLifetime", dataType=o6.UInt32, value=0)
    )


@o6.objecttype(nodeId="ns=machine_tool;i=1", browseName="ns=machine_tool;PartLoadPrognosisType", displayName="PartLoadPrognosisType")
class PartLoadPrognosisType(PrognosisType):
    location: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=402", browseName="ns=machine_tool;Location", dataType=o6.LocalizedText)
    )
    partIdentifier: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=408", browseName="ns=machine_tool;PartIdentifier", dataType=o6.String)
    )
    partName: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=409", browseName="ns=machine_tool;PartName", dataType=o6.String)
    )
    partNodeId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=machine_tool;i=401"])


ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=414", browseName="ns=machine_tool;JobNodeId", dataType=o6.NodeId)


@o6.objecttype(nodeId="ns=machine_tool;i=37", browseName="ns=machine_tool;ProductionJobEndPrognosisType", displayName="ProductionJobEndPrognosisType")
class ProductionJobEndPrognosisType(PrognosisType):
    jobNodeId: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(o6.ns["ns=machine_tool;i=414"])
    sourceIdentifier: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=412", browseName="ns=machine_tool;SourceIdentifier", dataType=o6.String)
    )


@o6.objecttype(nodeId="ns=machine_tool;i=31", browseName="ns=machine_tool;ProductionJobTransitionEventType", displayName="ProductionJobTransitionEventType", isAbstract=True)
class ProductionJobTransitionEventType(ns0.objtypes.TransitionEventType):
    customerOrderIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=416", browseName="ns=machine_tool;CustomerOrderIdentifier", dataType=o6.String)
    )
    identifier: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=243", browseName="ns=machine_tool;Identifier", dataType=o6.String))
    orderIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=417", browseName="ns=machine_tool;OrderIdentifier", dataType=o6.String)
    )
    runsCompleted: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=418", browseName="ns=machine_tool;RunsCompleted", dataType=o6.UInt32)
    )
    runsPlanned: ns0.vartypes.BaseDataVariableType


@o6.objecttype(nodeId="ns=machine_tool;i=1004", browseName="ns=machine_tool;MaintenanceModeStateMachineType", displayName="MaintenanceModeStateMachineType")
class MaintenanceModeStateMachineType(ns0.objtypes.FiniteStateMachineType):
    inspection: ns0.objtypes.StateType
    other: ns0.objtypes.StateType
    repair: ns0.objtypes.StateType
    service: ns0.objtypes.StateType
    upgrade: ns0.objtypes.StateType


@o6.objecttype(nodeId="ns=machine_tool;i=13", browseName="ns=machine_tool;MachineToolType", displayName="MachineToolType")
class MachineToolType(ns0.objtypes.BaseObjectType):
    components: machinery.objtypes.MachineComponentsType | None = o6.hasAddIn(
        machinery.objtypes.MachineComponentsType(nodeId="ns=machine_tool;i=5005", browseName="ns=machinery;Components")
    )
    equipment: EquipmentType
    fileSystem: ns0.objtypes.FileDirectoryType | None
    identification: MachineToolIdentificationType
    machineryBuildingBlocks: ns0.objtypes.FolderType | None
    monitoring: MonitoringType
    notification: NotificationType
    production: ProductionType


@o6.objecttype(nodeId="ns=machine_tool;i=1002", browseName="ns=machine_tool;ObligationType", displayName="ObligationType")
class ObligationType(ns0.objtypes.BaseObjectType):
    endUserObligated: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=6011", browseName="ns=machine_tool;EndUserObligated", dataType=o6.Boolean)
    )
    machineBuilderObligated: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=6012", browseName="ns=machine_tool;MachineBuilderObligated", dataType=o6.Boolean)
    )


@o6.objecttype(nodeId="ns=machine_tool;i=29", browseName="ns=machine_tool;ProductionJobType", displayName="ProductionJobType", interfaces=[ns0.objtypes.IOrderedObjectType])
class ProductionJobType(ns0.objtypes.BaseObjectType):
    customerOrderIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=181", browseName="ns=machine_tool;CustomerOrderIdentifier", dataType=o6.String)
    )
    identifier: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=189", browseName="ns=machine_tool;Identifier", dataType=o6.String))
    numberInList: ns0.vartypes.PropertyType = o6.hasProperty(ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=196", browseName="NumberInList", dataType=o6.UInt16))
    orderIdentifier: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=machine_tool;i=251", browseName="ns=machine_tool;OrderIdentifier", dataType=o6.String)
    )
    partSets: ns0.objtypes.BaseObjectType | None
    partsCompleted: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=6015", browseName="ns=machine_tool;PartsCompleted", dataType=o6.UInt32)
    )
    partsGood: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=6016", browseName="ns=machine_tool;PartsGood", dataType=o6.UInt32)
    )
    productionPrograms: ns0.objtypes.OrderedListType
    runsCompleted: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=machine_tool;i=191", browseName="ns=machine_tool;RunsCompleted", dataType=o6.UInt32)
    )
    runsPlanned: ns0.vartypes.BaseDataVariableType
    state: ProductionJobStateMachineType


@o6.objecttype(nodeId="ns=machine_tool;i=1003", browseName="ns=machine_tool;MachineOperationModeStateMachineType", displayName="MachineOperationModeStateMachineType")
class MachineOperationModeStateMachineType(machinery.objtypes.MachineryOperationModeStateMachineType):
    defaultInstanceBrowseName: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=machine_tool;i=6063",
            browseName="DefaultInstanceBrowseName",
            description="The default BrowseName for instances of the type",
            dataType=o6.QualifiedName,
            value=o6.QualifiedName("machinery:MachineryOperationMode"),
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    fromMaintenanceToMaintenance: ns0.objtypes.TransitionType
    fromMaintenanceToNone: ns0.objtypes.TransitionType
    fromMaintenanceToProcessing: ns0.objtypes.TransitionType
    fromMaintenanceToSetup: ns0.objtypes.TransitionType
    fromNoneToMaintenance: ns0.objtypes.TransitionType
    fromNoneToNone: ns0.objtypes.TransitionType
    fromNoneToProcessing: ns0.objtypes.TransitionType
    fromNoneToSetup: ns0.objtypes.TransitionType
    fromProcessingToMaintenance: ns0.objtypes.TransitionType
    fromProcessingToNone: ns0.objtypes.TransitionType
    fromProcessingToProcessing: ns0.objtypes.TransitionType
    fromProcessingToSetup: ns0.objtypes.TransitionType
    fromSetupToMaintenance: ns0.objtypes.TransitionType
    fromSetupToNone: ns0.objtypes.TransitionType
    fromSetupToProcessing: ns0.objtypes.TransitionType
    fromSetupToSetup: ns0.objtypes.TransitionType
    maintenance: ns0.objtypes.StateType
    maintenanceMode: MaintenanceModeStateMachineType | None
    none: ns0.objtypes.StateType
    processing: ns0.objtypes.StateType
    setup: ns0.objtypes.StateType


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0, machine_tool_datypes, machine_tool_vartypes
