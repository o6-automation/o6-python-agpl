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

"""Generated OPC UA woodworking namespace declarations."""

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
from . import datatypes as woodworking_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=woodworking;i=6",
    browseName="ns=woodworking;IWwBaseStateType",
    displayName="IWwBaseStateType",
    description="The IWwBaseStateType represents the state of an unit. An unit can be a machine of part of a machine.",
    isAbstract=True,
)
class IWwBaseStateType(ns0.objtypes.BaseInterfaceType):
    flags: ns0.objtypes.BaseObjectType | None
    overview: ns0.objtypes.BaseObjectType
    values: ns0.objtypes.BaseObjectType | None


@o6.objecttype(
    nodeId="ns=woodworking;i=7",
    browseName="ns=woodworking;IWwSubUnitsType",
    displayName="IWwSubUnitsType",
    description="The IWwSubUnitsType provides a list of subUnits.",
    isAbstract=True,
)
class IWwSubUnitsType(ns0.objtypes.BaseInterfaceType):
    langleSubUnitRangle: ns0.objtypes.BaseObjectType


@o6.objecttype(
    nodeId="ns=woodworking;i=8",
    browseName="ns=woodworking;IWwStateType",
    displayName="IWwStateType",
    description="The IWwStateType provides a list of machine states.",
    isAbstract=True,
)
class IWwStateType(ns0.objtypes.BaseInterfaceType):
    machine: ns0.objtypes.BaseObjectType
    subUnits: ns0.objtypes.BaseObjectType | None


@o6.objecttype(
    nodeId="ns=woodworking;i=15",
    browseName="ns=woodworking;WwEventsDispatcherType",
    displayName="WwEventsDispatcherType",
    description="The WwEventsDispatcherType represents a container that is an event dispatcher for machine events.",
)
class WwEventsDispatcherType(ns0.objtypes.BaseObjectType):
    pass


o6.reference(WwEventsDispatcherType, "i=41", "i=2041")


@o6.objecttype(
    nodeId="ns=woodworking;i=5",
    browseName="ns=woodworking;IWwUnitOverviewType",
    displayName="IWwUnitOverviewType",
    description="The IWwUnitOverviewType represents the generalized state of a unit.",
    isAbstract=True,
)
class IWwUnitOverviewType(ns0.objtypes.BaseInterfaceType):
    currentMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=130",
            browseName="ns=woodworking;CurrentMode",
            description="The CurrentMode Variable provides the generalized mode of the component.",
            dataType=woodworking_datypes.WwUnitModeEnumeration,
        )
    )
    currentState: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=129",
            browseName="ns=woodworking;CurrentState",
            description="The CurrentState Variable provides the generalized state of the component.",
            dataType=woodworking_datypes.WwUnitStateEnumeration,
            value=woodworking_datypes.WwUnitStateEnumeration.OFFLINE,
        )
    )


@o6.objecttype(
    nodeId="ns=woodworking;i=1006",
    browseName="ns=woodworking;IWwUnitValuesType",
    displayName="IWwUnitValuesType",
    description="The IWwUnitValuesType represents the values of a unit",
    isAbstract=True,
)
class IWwUnitValuesType(ns0.objtypes.BaseInterfaceType):
    absoluteErrorTime: ns0.vartypes.BaseAnalogType | None
    absoluteLength: ns0.vartypes.BaseAnalogType | None
    absoluteMachineOffTime: ns0.vartypes.BaseAnalogType | None
    absoluteMachineOnTime: ns0.vartypes.BaseAnalogType | None
    absolutePiecesIn: ns0.vartypes.BaseAnalogType | None
    absolutePiecesOut: ns0.vartypes.BaseAnalogType | None
    absolutePowerPresentTime: ns0.vartypes.BaseAnalogType | None
    absoluteProductionTime: ns0.vartypes.BaseAnalogType | None
    absoluteProductionWaitWorkpieceTime: ns0.vartypes.BaseAnalogType | None
    absoluteProductionWithoutWorkpieceTime: ns0.vartypes.BaseAnalogType | None
    absoluteReadyTime: ns0.vartypes.BaseAnalogType | None
    absoluteRunsAborted: ns0.vartypes.BaseAnalogType | None
    absoluteRunsGood: ns0.vartypes.BaseAnalogType | None
    absoluteRunsTotal: ns0.vartypes.BaseAnalogType | None
    absoluteStandbyTime: ns0.vartypes.BaseAnalogType | None
    absoluteWorkingTime: ns0.vartypes.BaseAnalogType | None
    actualCycle: ns0.vartypes.BaseAnalogType | None
    axisOverride: ns0.vartypes.BaseAnalogType | None
    feedSpeed: ns0.vartypes.BaseAnalogType | None
    relativeErrorTime: ns0.vartypes.BaseAnalogType | None
    relativeLength: ns0.vartypes.BaseAnalogType | None
    relativeMachineOnTime: ns0.vartypes.BaseAnalogType | None
    relativePiecesIn: ns0.vartypes.BaseAnalogType | None
    relativePiecesOut: ns0.vartypes.BaseAnalogType | None
    relativePowerPresentTime: ns0.vartypes.BaseAnalogType | None
    relativeProductionTime: ns0.vartypes.BaseAnalogType | None
    relativeProductionWaitWorkpieceTime: ns0.vartypes.BaseAnalogType | None
    relativeProductionWithoutWorkpieceTime: ns0.vartypes.BaseAnalogType | None
    relativeReadyTime: ns0.vartypes.BaseAnalogType | None
    relativeRunsAborted: ns0.vartypes.BaseAnalogType | None
    relativeRunsGood: ns0.vartypes.BaseAnalogType | None
    relativeRunsTotal: ns0.vartypes.BaseAnalogType | None
    relativeStandbyTime: ns0.vartypes.BaseAnalogType | None
    relativeWorkingTime: ns0.vartypes.BaseAnalogType | None
    spindleOverride: ns0.vartypes.BaseAnalogType | None


@o6.objecttype(
    nodeId="ns=woodworking;i=2", browseName="ns=woodworking;WwMachineType", displayName="WwMachineType", description="The WwMachineType represents a woodworking machine."
)
class WwMachineType(ns0.objtypes.BaseObjectType):
    events: WwEventsDispatcherType | None = o6.hasComponent(
        WwEventsDispatcherType(nodeId="ns=woodworking;i=5008", browseName="ns=woodworking;Events", description="The Event Object provides events.", eventNotifier=1)
    )
    identification: machinery.objtypes.MachineIdentificationType
    jobManagement: machinery_jobs.objtypes.JobManagementType | None
    machineryBuildingBlocks: ns0.objtypes.FolderType | None
    manufacturerSpecific: ns0.objtypes.FolderType | None
    state: ns0.objtypes.BaseObjectType


@o6.objecttype(
    nodeId="ns=woodworking;i=4",
    browseName="ns=woodworking;IWwUnitFlagsType",
    displayName="IWwUnitFlagsType",
    description="The IWwUnitFlagsType represents the flags of a unit",
    isAbstract=True,
)
class IWwUnitFlagsType(ns0.objtypes.BaseInterfaceType):
    airPresent: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=88",
            browseName="ns=woodworking;AirPresent",
            description="The AirPresent Variable is true if the air pressure is present in the machine.",
            dataType=o6.Boolean,
        )
    )
    alarm: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=97", browseName="ns=woodworking;Alarm", description="The Alarm Variable is true if at least one alarm exists.", dataType=o6.Boolean
        )
    )
    calibrated: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=92", browseName="ns=woodworking;Calibrated", description="The Calibrated Variable is true if all devices are calibrated.", dataType=o6.Boolean
        )
    )
    dustChipSuction: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=89",
            browseName="ns=woodworking;DustChipSuction",
            description="The DustChipSuction Variable is true if the dust and chip suction is ready.",
            dataType=o6.Boolean,
        )
    )
    emergency: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=90",
            browseName="ns=woodworking;Emergency",
            description="The Emergency Variable is true if at least one emergency button is pressed.",
            dataType=o6.Boolean,
        )
    )
    energySaving: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=108",
            browseName="ns=woodworking;EnergySaving",
            description="The EnergySaving Variable is true if energy saving is activated on the machine.",
            dataType=o6.Boolean,
        )
    )
    error: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=96",
            browseName="ns=woodworking;Error",
            description="The Error Variable is true if at least one reason exists which prevents the machine from working.",
            dataType=o6.Boolean,
        )
    )
    externalEmergency: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=109",
            browseName="ns=woodworking;ExternalEmergency",
            description="The ExternalEmergency Variable is true if there is an emergency from the line controller.",
            dataType=o6.Boolean,
        )
    )
    feedRuns: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=111",
            browseName="ns=woodworking;FeedRuns",
            description="The FeedRuns Variable is true if the feed is running on a throughfeed machine.",
            dataType=o6.Boolean,
        )
    )
    hold: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=99",
            browseName="ns=woodworking;Hold",
            description="The Hold Variable is true if the movements are paused by the operator.",
            dataType=o6.Boolean,
        )
    )
    loadingEnabled: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(nodeId="ns=woodworking;i=6033", browseName="ns=woodworking;LoadingEnabled", dataType=o6.Boolean)
    )
    machineInitialized: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=86",
            browseName="ns=woodworking;MachineInitialized",
            description="The MachineInitialized Variable is true if the MachineOn is true, the PLC and the control processes are running. The machine is ready for usage for the operator.",
            dataType=o6.Boolean,
        )
    )
    machineOn: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=85",
            browseName="ns=woodworking;MachineOn",
            description="The MachineOn Variable is true if the machine is switched on. If the OPC UA Server runs on the machine this value is always true.",
            dataType=o6.Boolean,
        )
    )
    maintenanceRequired: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=110",
            browseName="ns=woodworking;MaintenanceRequired",
            description="The MaintenanceRequired Variable is true if maintenance is required.",
            dataType=o6.Boolean,
        )
    )
    manualActivityRequired: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=103",
            browseName="ns=woodworking;ManualActivityRequired",
            description="The ManualActivityRequired Variable is true if a manual activity by the operator is required. The RecipeInRun is not affected.",
            dataType=o6.Boolean,
        )
    )
    moving: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=95", browseName="ns=woodworking;Moving", description="The Moving Variable is true if at least one axis is moving.", dataType=o6.Boolean
        )
    )
    powerPresent: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=87",
            browseName="ns=woodworking;PowerPresent",
            description="The PowerPresent Variable is true if 400V are present (the drives are ready to move).",
            dataType=o6.Boolean,
        )
    )
    recipeInHold: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=102",
            browseName="ns=woodworking;RecipeInHold",
            description="The RecipeInHold Variable is true if the machine is paused by the program. This is only possible if the RecipeInRun Variable is also true.",
            dataType=o6.Boolean,
        )
    )
    recipeInRun: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=100",
            browseName="ns=woodworking;RecipeInRun",
            description="The RecipeInRun Variable is true if the machine runs its program. This is only possible if the Error Variable is false. However, if the machine is paused by the program, the machine is considered to still be running its program, i.e. while the RecipeInHold Variable is true, the RecipeInRun cannot be false.",
            dataType=o6.Boolean,
        )
    )
    recipeInSetup: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=101",
            browseName="ns=woodworking;RecipeInSetup",
            description="The RecipeInSetup Variable is true if the RecipeInRun is true and the machine is in the setup phase (example: automatic tool change).",
            dataType=o6.Boolean,
        )
    )
    remote: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=93",
            browseName="ns=woodworking;Remote",
            description="The Remote Variable is true if the machine is working with programs sent by the supervisor or other external application.",
            dataType=o6.Boolean,
        )
    )
    safety: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=91",
            browseName="ns=woodworking;Safety",
            description="The Safety Variable is true if at least one safety device (light curtain, safety mat, …) has intervened.",
            dataType=o6.Boolean,
        )
    )
    waitLoad: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=107",
            browseName="ns=woodworking;WaitLoad",
            description="The WaitLoad Variable is true if the machine is waiting for pieces.",
            dataType=o6.Boolean,
        )
    )
    waitUnload: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=106",
            browseName="ns=woodworking;WaitUnload",
            description="The WaitUnload Variable is true if the machine is waiting to unload pieces.",
            dataType=o6.Boolean,
        )
    )
    warning: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=98", browseName="ns=woodworking;Warning", description="The Warning Variable is true if at least one warning exists.", dataType=o6.Boolean
        )
    )
    workpiecePresent: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=woodworking;i=94",
            browseName="ns=woodworking;WorkpiecePresent",
            description="The WorkpiecePresent Variable is true if at least one piece is inside the machine.",
            dataType=o6.Boolean,
        )
    )


@o6.objecttype(
    nodeId="ns=woodworking;i=1002",
    browseName="ns=woodworking;IWwEventMessageType",
    displayName="IWwEventMessageType",
    description="The interface definition IWwEventMessageType describes the common extensions for all events and conditions. Each instance definition that includes this interface with a HasInterface reference defines the predefined extensions",
    isAbstract=True,
)
class IWwEventMessageType(ns0.objtypes.BaseInterfaceType):
    arguments: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6222",
            browseName="ns=woodworking;Arguments",
            description="The Arguments Variable is an argument value array of one dimension that can be used to parameterize the message. The number of the indexing in the array corresponds to the placeholder number in the message text. This ensures that the formatting functions of the implementations enable the localized message texts to be created.",
            dataType=woodworking_datypes.WwMessageArgumentDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    eventCategory: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6169",
            browseName="ns=woodworking;EventCategory",
            description="The EventCategory Variable provides the category of the event.",
            dataType=woodworking_datypes.WwEventCategoryEnumeration,
        )
    )
    group: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6220",
            browseName="ns=woodworking;Group",
            description="The Group Variable specifies the class or group of the Message like “safety”, “emergency”, “consumable”.  See chapter “Categorizing and grouping the messages, events, alarms and conditions”.",
            dataType=o6.String,
        )
    )
    localizedMessages: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6221",
            browseName="ns=woodworking;LocalizedMessages",
            description="The LocalizedMessages Variable contains an array of localized messages corresponding to the installed server languages.",
            dataType=o6.LocalizedText,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    messageId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6217",
            browseName="ns=woodworking;MessageId",
            description="The MessageId Variable is a unique Identifier like a number or name of the message in the cause path (PathParts) determined Module. Example: “A4711” or “1”",
            dataType=o6.String,
        )
    )
    messageName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6218",
            browseName="ns=woodworking;MessageName",
            description="The MessageName Variable is a short name like a number or title to reference a translation of the general message text. Example: “ID_MSG_EmergencyAlarm”.",
            dataType=o6.String,
        )
    )
    pathParts: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6219",
            browseName="ns=woodworking;PathParts",
            description="The PathParts Variable is an array of Path information strings based on a server independent hierarchical structure of modules or an application specific expansion of that. It is an additional location information beside the SourceName. Example:  “Machine”, “FixedSide”, “Sizing”, “Milling1”",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


@o6.objecttype(
    nodeId="ns=woodworking;i=1004",
    browseName="ns=woodworking;WwConditionType",
    displayName="WwConditionType",
    description="The WwConditionType represents a state of a woodworking system or one of its components.",
    interfaces=[IWwEventMessageType],
)
class WwConditionType(ns0.objtypes.ConditionType):
    arguments: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6009",
            browseName="ns=woodworking;Arguments",
            description="The Arguments Variable is an argument value array of one dimension that can be used to parameterize the message. The number of the indexing in the array corresponds to the placeholder number in the message text. This ensures that the formatting functions of the implementations enable the localized message texts to be created.",
            dataType=woodworking_datypes.WwMessageArgumentDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    eventCategory: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6010",
            browseName="ns=woodworking;EventCategory",
            description="The EventCategory Variable provides the category of the event.",
            dataType=woodworking_datypes.WwEventCategoryEnumeration,
        )
    )
    group: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6011",
            browseName="ns=woodworking;Group",
            description="The Group Variable specifies the class or group of the Message like “safety”, “emergency”, “consumable”.  See chapter “Categorizing and grouping the messages, events, alarms and conditions”.",
            dataType=o6.String,
        )
    )
    localizedMessages: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6012",
            browseName="ns=woodworking;LocalizedMessages",
            description="The LocalizedMessages Variable contains an array of localized messages corresponding to the installed server languages.",
            dataType=o6.LocalizedText,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    messageId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6013",
            browseName="ns=woodworking;MessageId",
            description="The MessageId Variable is a unique Identifier like a number or name of the message in the cause path (PathParts) determined Module. Example: “A4711” or “1”",
            dataType=o6.String,
        )
    )
    messageName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6135",
            browseName="ns=woodworking;MessageName",
            description="The MessageName Variable is a short name like a number or title to reference a translation of the general message text. Example: “ID_MSG_EmergencyAlarm”.",
            dataType=o6.String,
        )
    )
    pathParts: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6136",
            browseName="ns=woodworking;PathParts",
            description="The PathParts Variable is an array of Path information strings based on a server independent hierarchical structure of modules or an application specific expansion of that. It is an additional location information beside the SourceName. Example:  “Machine”, “FixedSide”, “Sizing”, “Milling1”",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


o6.reference(WwEventsDispatcherType, "i=41", WwConditionType)


@o6.objecttype(
    nodeId="ns=woodworking;i=13",
    browseName="ns=woodworking;WwBaseEventType",
    displayName="WwBaseEventType",
    description="The WwBaseEventType represents a message event from a module.",
    interfaces=[IWwEventMessageType],
)
class WwBaseEventType(ns0.objtypes.BaseEventType):
    arguments: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6232",
            browseName="ns=woodworking;Arguments",
            description="The Arguments Variable is an argument value array of one dimension that can be used to parameterize the message. The number of the indexing in the array corresponds to the placeholder number in the message text. This ensures that the formatting functions of the implementations enable the localized message texts to be created.",
            dataType=woodworking_datypes.WwMessageArgumentDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    eventCategory: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6056",
            browseName="ns=woodworking;EventCategory",
            description="The EventCategory Variable provides the category of the event.",
            dataType=woodworking_datypes.WwEventCategoryEnumeration,
        )
    )
    group: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=259",
            browseName="ns=woodworking;Group",
            description="The Group Variable specifies the class or group of the Message like “safety”, “emergency”, “consumable”.  See chapter “Categorizing and grouping the messages, events, alarms and conditions”.",
            dataType=o6.String,
        )
    )
    localizedMessages: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=260",
            browseName="ns=woodworking;LocalizedMessages",
            description="The LocalizedMessages Variable contains an array of localized messages corresponding to the installed server languages.",
            dataType=o6.LocalizedText,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    messageId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=256",
            browseName="ns=woodworking;MessageId",
            description="The MessageId Variable is a unique Identifier like a number or name of the message in the cause path (PathParts) determined Module. Example: “A4711” or “1”",
            dataType=o6.String,
        )
    )
    messageName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=257",
            browseName="ns=woodworking;MessageName",
            description="The MessageName Variable is a short name like a number or title to reference a translation of the general message text. Example: “ID_MSG_EmergencyAlarm”.",
            dataType=o6.String,
        )
    )
    pathParts: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=258",
            browseName="ns=woodworking;PathParts",
            description="The PathParts Variable is an array of Path information strings based on a server independent hierarchical structure of modules or an application specific expansion of that. It is an additional location information beside the SourceName.",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


o6.reference(WwEventsDispatcherType, "i=41", WwBaseEventType)


@o6.objecttype(
    nodeId="ns=woodworking;i=1005",
    browseName="ns=woodworking;WwAcknowledgeableConditionType",
    displayName="WwAcknowledgeableConditionType",
    description="The WwAcknowledgeableConditionType represents an acknowledgeable and confirmable state of a woodworking system or one of its components.",
    interfaces=[IWwEventMessageType],
)
class WwAcknowledgeableConditionType(ns0.objtypes.AcknowledgeableConditionType):
    arguments: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6182",
            browseName="ns=woodworking;Arguments",
            description="The Arguments Variable is an argument value array of one dimension that can be used to parameterize the message. The number of the indexing in the array corresponds to the placeholder number in the message text. This ensures that the formatting functions of the implementations enable the localized message texts to be created.",
            dataType=woodworking_datypes.WwMessageArgumentDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    eventCategory: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6183",
            browseName="ns=woodworking;EventCategory",
            description="The EventCategory Variable provides the category of the event.",
            dataType=woodworking_datypes.WwEventCategoryEnumeration,
        )
    )
    group: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6203",
            browseName="ns=woodworking;Group",
            description="The Group Variable specifies the class or group of the Message like “safety”, “emergency”, “consumable”.  See chapter “Categorizing and grouping the messages, events, alarms and conditions”.",
            dataType=o6.String,
        )
    )
    localizedMessages: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6204",
            browseName="ns=woodworking;LocalizedMessages",
            description="The LocalizedMessages Variable contains an array of localized messages corresponding to the installed server languages.",
            dataType=o6.LocalizedText,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    messageId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6205",
            browseName="ns=woodworking;MessageId",
            description="The MessageId Variable is a unique Identifier like a number or name of the message in the cause path (PathParts) determined Module. Example: “A4711” or “1”",
            dataType=o6.String,
        )
    )
    messageName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6206",
            browseName="ns=woodworking;MessageName",
            description="The MessageName Variable is a short name like a number or title to reference a translation of the general message text. Example: “ID_MSG_EmergencyAlarm”.",
            dataType=o6.String,
        )
    )
    pathParts: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6242",
            browseName="ns=woodworking;PathParts",
            description="The PathParts Variable is an array of Path information strings based on a server independent hierarchical structure of modules or an application specific expansion of that. It is an additional location information beside the SourceName. Example:  “Machine”, “FixedSide”, “Sizing”, “Milling1”",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


o6.reference(WwEventsDispatcherType, "i=41", WwAcknowledgeableConditionType)


@o6.objecttype(
    nodeId="ns=woodworking;i=1007",
    browseName="ns=woodworking;WwAlarmConditionType",
    displayName="WwAlarmConditionType",
    description="The WwAlarmContitionType represents an acknowledgeable and confirmable state of a woodworking system or one of its components containing an active state.",
    interfaces=[IWwEventMessageType],
)
class WwAlarmConditionType(ns0.objtypes.AlarmConditionType):
    arguments: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6243",
            browseName="ns=woodworking;Arguments",
            description="The Arguments Variable is an argument value array of one dimension that can be used to parameterize the message. The number of the indexing in the array corresponds to the placeholder number in the message text. This ensures that the formatting functions of the implementations enable the localized message texts to be created.",
            dataType=woodworking_datypes.WwMessageArgumentDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    eventCategory: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6244",
            browseName="ns=woodworking;EventCategory",
            description="The EventCategory Variable provides the category of the event.",
            dataType=woodworking_datypes.WwEventCategoryEnumeration,
        )
    )
    group: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6245",
            browseName="ns=woodworking;Group",
            description="The Group Variable specifies the class or group of the Message like “safety”, “emergency”, “consumable”.  See chapter “Categorizing and grouping the messages, events, alarms and conditions”.",
            dataType=o6.String,
        )
    )
    localizedMessages: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6246",
            browseName="ns=woodworking;LocalizedMessages",
            description="The LocalizedMessages Variable contains an array of localized messages corresponding to the installed server languages.",
            dataType=o6.LocalizedText,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    messageId: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6247",
            browseName="ns=woodworking;MessageId",
            description="The MessageId Variable is a unique Identifier like a number or name of the message in the cause path (PathParts) determined Module. Example: “A4711” or “1”",
            dataType=o6.String,
        )
    )
    messageName: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6394",
            browseName="ns=woodworking;MessageName",
            description="The MessageName Variable is a short name like a number or title to reference a translation of the general message text. Example: “ID_MSG_EmergencyAlarm”.",
            dataType=o6.String,
        )
    )
    pathParts: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=woodworking;i=6395",
            browseName="ns=woodworking;PathParts",
            description="The PathParts Variable is an array of Path information strings based on a server independent hierarchical structure of modules or an application specific expansion of that. It is an additional location information beside the SourceName. Example:  “Machine”, “FixedSide”, “Sizing”, “Milling1”",
            dataType=o6.String,
            valueRank=1,
            arrayDimensions=[0],
        )
    )


o6.reference(WwEventsDispatcherType, "i=41", WwAlarmConditionType)


del Any, TYPE_CHECKING, uuid, o6, di, ia, isa95_jobcontrol_v2, machinery, machinery_jobs, ns0, woodworking_datypes
