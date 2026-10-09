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

"""Generated OPC UA plastics_foam_cutting namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ia as ia
import o6.ns.machinery as machinery
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_foam_cutting_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=plastics_foam_cutting;i=1004",
    browseName="ns=plastics_foam_cutting;ProcessMonitoringType",
    displayName="ProcessMonitoringType",
    description="Provides the process values of the different components of the foam cutting machine.",
)
class ProcessMonitoringType(ns0.objtypes.BaseObjectType):
    conveyorProcessMonitoring: ns0.objtypes.FolderType
    cuttingSpeedFeed: ns0.objtypes.FolderType
    cuttingUnitParameters: ns0.objtypes.FolderType
    knifes: ns0.objtypes.FolderType
    mainAxisDrives: plastics_rubber.objtypes.DrivesType
    materialSupport: ns0.objtypes.FolderType
    supply: ns0.objtypes.FolderType
    windingSystem: ns0.objtypes.FolderType


@o6.objecttype(
    nodeId="ns=plastics_foam_cutting;i=1013",
    browseName="ns=plastics_foam_cutting;FoamCuttingMachineType",
    displayName="FoamCuttingMachineType",
    description="This OPC UA ObjectType is used for the root Object representing a foam cutting machine.",
)
class FoamCuttingMachineType(ns0.objtypes.BaseObjectType):
    errorHandling: ErrorHandlingType | None
    identification: machinery.objtypes.MachineIdentificationType
    machineConfiguration: MachineConfigurationType
    machineryBuildingBlocks: ns0.objtypes.FolderType
    operation: OperationType
    processMonitoring: ProcessMonitoringType


@o6.objecttype(
    nodeId="ns=plastics_foam_cutting;i=1003",
    browseName="ns=plastics_foam_cutting;FoamCuttingCycleInformationEventType",
    displayName="FoamCuttingCycleInformationEventType",
    description="Provides collected information about a production cycle on the foam cutting machine.",
    isAbstract=True,
)
class FoamCuttingCycleInformationEventType(ns0.objtypes.BaseEventType):
    cycleTime: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_foam_cutting;i=6018",
            browseName="ns=plastics_foam_cutting;CycleTime",
            description="Duration of the cycle.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    finishedParts: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_foam_cutting;i=6017",
            browseName="ns=plastics_foam_cutting;FinishedParts",
            description="Number of finished parts in the period under review.",
            dataType=o6.UInt32,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    jobName: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_foam_cutting;i=6016",
            browseName="ns=plastics_foam_cutting;JobName",
            description="Provides the name of the job.",
            dataType=o6.String,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    startTime: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_foam_cutting;i=6019",
            browseName="ns=plastics_foam_cutting;StartTime",
            description="Start time of the cycle.",
            dataType=ns0.datatypes.UtcTime,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


o6.reference(FoamCuttingMachineType, "i=41", FoamCuttingCycleInformationEventType)


@o6.objecttype(
    nodeId="ns=plastics_foam_cutting;i=1006",
    browseName="ns=plastics_foam_cutting;ErrorHandlingType",
    displayName="ErrorHandlingType",
    description="The ErrorHandlingType provides Variables and Methods for simple error handling.",
)
class ErrorHandlingType(ns0.objtypes.BaseObjectType):
    activeErrors: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_foam_cutting;i=6020",
            browseName="ns=plastics_foam_cutting;ActiveErrors",
            description="List of the active errors of the device.",
            dataType=plastics_rubber.datatypes.ActiveErrorDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    highestActiveAlarmSeverity: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_foam_cutting;i=6021",
            browseName="ns=plastics_foam_cutting;HighestActiveAlarmSeverity",
            description="Indication of the severity of the highest active alarm.",
            dataType=o6.UInt16,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_foam_cutting;i=1005",
    browseName="ns=plastics_foam_cutting;MaterialSupportType",
    displayName="MaterialSupportType",
    description="This ObjectType defines the configuration of the physical part of the machine that supports, holds and feeds the foam to be cut. The information model for this ObjectType is structured based on the category of the material support, the kinds of fixtures, quantity of vacuum units that hold the foam block in place and the general dimensions of the table.",
)
class MaterialSupportType(ns0.objtypes.BaseObjectType):
    fixture: ns0.objtypes.FolderType
    materialSupportCategory: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_foam_cutting;i=6785",
            browseName="ns=plastics_foam_cutting;MaterialSupportCategory",
            description="This Property provides information about the category of the material support system.",
            dataType=plastics_foam_cutting_datypes.MaterialSupportCategoryEnumeration,
        )
    )
    tableDimensions: ns0.objtypes.FolderType
    vacuumUnitsQuantity: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_foam_cutting;i=6786",
            browseName="ns=plastics_foam_cutting;VacuumUnitsQuantity",
            description="This Property provides information about the total number of vacuum units on the material support system.",
            dataType=o6.UInt16,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_foam_cutting;i=1007",
    browseName="ns=plastics_foam_cutting;MachineConfigurationType",
    displayName="MachineConfigurationType",
    description="The MachineConfigurationType lists the current configuration of the foam cutting machine.",
)
class MachineConfigurationType(ns0.objtypes.BaseObjectType):
    conveyorConfigurations: ns0.objtypes.FolderType
    grindingUnit: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_foam_cutting;i=6840",
            browseName="ns=plastics_foam_cutting;GrindingUnit",
            description="A property with 0:Boolean data type. Its value is 1 if a grinding unit is physically present in a foam cutting machine.",
            dataType=o6.Boolean,
        )
    )
    knife: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_foam_cutting;i=6839",
            browseName="ns=plastics_foam_cutting;Knife",
            description="A property with 0:Boolean data type. Its value is 1 if is physically present in a foam cutting machine and is used for its normal operation.",
            dataType=o6.Boolean,
        )
    )
    materialSupport: MaterialSupportType


@o6.objecttype(
    nodeId="ns=plastics_foam_cutting;i=1009",
    browseName="ns=plastics_foam_cutting;OperationType",
    displayName="OperationType",
    description="Provides Objects and Variables relevant for the operation of the machine.",
)
class OperationType(ns0.objtypes.BaseObjectType):
    controlVoltageSwitch: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_foam_cutting;i=6023",
            browseName="ns=plastics_foam_cutting;ControlVoltageSwitch",
            description="Provides information, if the control voltage switch is switched on or off. The drives can only be operated with active control voltage.",
            dataType=o6.Boolean,
        )
    )
    jobInformation: ns0.objtypes.FolderType
    peripheralDevices: ns0.objtypes.FolderType
    processingMode: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_foam_cutting;i=6947", browseName="ns=plastics_foam_cutting;ProcessingMode", dataType=plastics_foam_cutting_datypes.ProcessingModeEnumeration
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_foam_cutting;i=1012",
    browseName="ns=plastics_foam_cutting;ConveyorProcessMonitoringType",
    displayName="ConveyorProcessMonitoringType",
    description="Provides information about the process values of one conveyor.",
)
class ConveyorProcessMonitoringType(ns0.objtypes.BaseObjectType):
    active: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_foam_cutting;i=6032", browseName="ns=plastics_foam_cutting;Active", description="Indicates if the conveyor is active.", dataType=o6.Boolean
        )
    )
    description: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_foam_cutting;i=7598",
            browseName="ns=plastics_foam_cutting;Description",
            description="Provides a user-defined textual description or identifier to distinguish and locate the conveyor within the machine or system.",
            dataType=o6.String,
        )
    )
    direction: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_foam_cutting;i=6029",
            browseName="ns=plastics_foam_cutting;Direction",
            description="Provides information about the current transportation direction of the conveyor.",
            dataType=plastics_foam_cutting_datypes.DirectionEnumeration,
        )
    )
    drives: plastics_rubber.objtypes.DrivesType
    speed: ns0.vartypes.AnalogUnitType


@o6.objecttype(
    nodeId="ns=plastics_foam_cutting;i=1010",
    browseName="ns=plastics_foam_cutting;ConveyorConfigurationType",
    displayName="ConveyorConfigurationType",
    description="The ConveyorConfigurationType details the configuration of the conveyor that is used to feed material towards or away from the cutting edge of the knife.",
)
class ConveyorConfigurationType(ns0.objtypes.BaseObjectType):
    conveyorCategory: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_foam_cutting;i=6815",
            browseName="ns=plastics_foam_cutting;ConveyorCategory",
            description="This property provides information, if this conveyor is used for unloading, loading or transportation of material.",
            dataType=plastics_foam_cutting_datypes.ConveyorCategoryEnumeration,
        )
    )
    conveyorSpeed: ns0.vartypes.AnalogUnitRangeType
    conveyorSubCategory: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_foam_cutting;i=6816",
            browseName="ns=plastics_foam_cutting;ConveyorSubCategory",
            description="This property provides information on what type of conveyor this instance is.",
            dataType=plastics_foam_cutting_datypes.ConveyorSubCategoryEnumeration,
        )
    )
    description: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_foam_cutting;i=7601",
            browseName="ns=plastics_foam_cutting;Description",
            description="Provides a user-defined textual description or identifier to distinguish and locate the conveyor within the machine or system.",
            dataType=o6.String,
        )
    )
    fixedSpeedConveyor: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_foam_cutting;i=6817",
            browseName="ns=plastics_foam_cutting;FixedSpeedConveyor",
            description="This Property provides information, if the conveyor has a fixed speed.",
            dataType=o6.Boolean,
        )
    )
    isPresent: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_foam_cutting;i=6814",
            browseName="ns=plastics_foam_cutting;IsPresent",
            description="The IsPresent Property provides information, if an instance of the conveyor is present in the current configuration of the machine.",
            dataType=o6.Boolean,
        )
    )
    length: ns0.vartypes.AnalogUnitType
    lightBarriers: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_foam_cutting;i=6826",
            browseName="ns=plastics_foam_cutting;LightBarriers",
            description="Provides information about the positions of light barriers on this instance of conveyor.\nEach array entry represents one light barrier.",
            dataType=plastics_foam_cutting_datypes.LightBarrierEnumeration,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    numberOfBelts: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_foam_cutting;i=6825",
            browseName="ns=plastics_foam_cutting;NumberOfBelts",
            description="Provides the number of individual belts on the conveyor.",
            dataType=o6.UInt16,
        )
    )
    possibleDirection: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_foam_cutting;i=6827",
            browseName="ns=plastics_foam_cutting;PossibleDirection",
            description="Provides information about the possible working directions of the conveyor.",
            dataType=plastics_foam_cutting_datypes.PossibleDirectionEnumeration,
        )
    )
    width: ns0.vartypes.AnalogUnitType


@o6.objecttype(
    nodeId="ns=plastics_foam_cutting;i=1008", browseName="ns=plastics_foam_cutting;KnifeType", displayName="KnifeType", description="Contains process values of one knife."
)
class KnifeType(ns0.objtypes.BaseObjectType):
    grindDrives: plastics_rubber.objtypes.DrivesType | None
    grindingUnitState: ns0.vartypes.BaseDataVariableType | None = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_foam_cutting;i=7610",
            browseName="ns=plastics_foam_cutting;GrindingUnitState",
            description="Provides information about the current state of the grinding unit.",
            dataType=plastics_foam_cutting_datypes.GrindingUnitStateEnumeration,
        )
    )
    knifeDrives: plastics_rubber.objtypes.DrivesType | None
    knifeRunning: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_foam_cutting;i=7604",
            browseName="ns=plastics_foam_cutting;KnifeRunning",
            description="Indicates if the knife is switched on (true) or off (false).",
            dataType=o6.Boolean,
        )
    )
    knifeSpeed: ns0.vartypes.AnalogUnitType | None
    readjustment: ns0.vartypes.AnalogUnitType | None
    wearStatus: plastics_rubber.objtypes.MaintenanceType | None


del Any, TYPE_CHECKING, uuid, o6, di, ia, machinery, ns0, plastics_rubber, plastics_foam_cutting_datypes
