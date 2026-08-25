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

"""Generated OPC UA plastics_tcd namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_tcd_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=plastics_tcd;i=1004",
    browseName="ns=plastics_tcd;MaintenanceInformationType",
    displayName="MaintenanceInformationType",
    description="Information on the maintenance status of heating, cooling, pump and fluid",
)
class MaintenanceInformationType(ns0.objtypes.BaseObjectType):
    cooling: plastics_rubber.objtypes.MaintenanceType | None
    fluid: plastics_rubber.objtypes.MaintenanceType | None
    heating: plastics_rubber.objtypes.MaintenanceType | None
    pump: plastics_rubber.objtypes.MaintenanceType | None


@o6.objecttype(
    nodeId="ns=plastics_tcd;i=1008", browseName="ns=plastics_tcd;DeviceZoneType", displayName="DeviceZoneType", description="Represents the functional main component of a TCD"
)
class DeviceZoneType(ns0.objtypes.BaseObjectType):
    actualProcessPower: ns0.vartypes.AnalogItemType | None
    actualPumpPower: ns0.vartypes.AnalogItemType | None
    actualPumpSpeedRPM: ns0.vartypes.AnalogItemType | None
    actualRegulationRatio: ns0.vartypes.AnalogItemType | None
    delayTimeAfterCooling: ns0.vartypes.AnalogItemType | None
    externalChannels: ExternalChannelsType | None
    externalSensor: ExternalSensorType | None
    flowRate: plastics_rubber.objtypes.MonitoredParameterType | None
    internalMeasuringPoint: ns0.vartypes.MultiStateValueDiscreteType | None
    leakStopper: LeakStopperType | None
    maintenanceInformation: MaintenanceInformationType | None
    mouldEvacuation: MouldEvacuationType | None
    pressureDifference: plastics_rubber.objtypes.MonitoredParameterType | None
    pressureMainLine: ns0.vartypes.AnalogItemType | None
    pressureReturnLine: ns0.vartypes.AnalogItemType | None
    pumpControlMode: ns0.vartypes.MultiStateValueDiscreteType | None
    pumpSpeed: plastics_rubber.objtypes.MonitoredParameterType | None
    standbyTemperature: ns0.vartypes.AnalogItemType | None
    switchingOffTemperature: ns0.vartypes.AnalogItemType | None
    temperature: plastics_rubber.objtypes.ControlledParameterType
    temperatureDifference: plastics_rubber.objtypes.MonitoredParameterType | None
    temperatureLimitation: ns0.vartypes.AnalogItemType | None
    temperatureMainLine: ns0.vartypes.AnalogItemType | None
    temperatureReturnLine: ns0.vartypes.AnalogItemType | None


@o6.objecttype(
    nodeId="ns=plastics_tcd;i=1003", browseName="ns=plastics_tcd;ExternalChannelsType", displayName="ExternalChannelsType", description="Container for the external channel(s)"
)
class ExternalChannelsType(ns0.objtypes.BaseObjectType):
    externalChannel_LangleNrRangle: ExternalChannelType | None
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=6082", browseName="NodeVersion", dataType=o6.String, value="\n      ")
    )


o6.reference(ExternalChannelsType, "i=41", "i=2133")


@o6.objecttype(
    nodeId="ns=plastics_tcd;i=1012",
    browseName="ns=plastics_tcd;TCD_InterfaceType",
    displayName="TCD_InterfaceType",
    description="Root ObjectType representing a temperature control device with its subcomponents",
)
class TCD_InterfaceType(ns0.objtypes.BaseObjectType):
    deviceZone: DeviceZoneType
    displayLanguage: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_tcd;i=6557",
            browseName="ns=plastics_tcd;DisplayLanguage",
            description="With this Property the client can set the desired language on the user interface at the TCD",
            dataType=ns0.datatypes.LocaleId,
            value="\n      ",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    identification: plastics_rubber.objtypes.IdentificationType
    machineConfiguration: plastics_rubber.objtypes.MachineConfigurationType
    operation: OperationType
    tCDSpecification: TCDSpecificationType


@o6.objecttype(
    nodeId="ns=plastics_tcd;i=1005",
    browseName="ns=plastics_tcd;MouldEvacuationType",
    displayName="MouldEvacuationType",
    description="Includes parameters and nodes for mould evacuation",
)
class MouldEvacuationType(ns0.objtypes.BaseObjectType):
    mode: ns0.vartypes.MultiStateValueDiscreteType | None
    off: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7009", browseName="ns=plastics_tcd;Off", description="Deactivate evacuation mode"))
    on: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7008", browseName="ns=plastics_tcd;On", description="Activate evacuation mode"))
    sink: ns0.vartypes.MultiStateValueDiscreteType | None
    temperatureLimit: ns0.vartypes.AnalogItemType | None
    time: ns0.vartypes.AnalogItemType | None


@o6.objecttype(nodeId="ns=plastics_tcd;i=1006", browseName="ns=plastics_tcd;LeakStopperType", displayName="LeakStopperType", description="Used for switching the leak stopper mode")
class LeakStopperType(ns0.objtypes.BaseObjectType):
    off: o6.node.MethodNode = o6.hasComponent(o6.call(nodeId="ns=plastics_tcd;i=7014", browseName="ns=plastics_tcd;Off", description="Deactivate the leak stopper mode"))
    on: o6.node.MethodNode = o6.hasComponent(
        o6.call(nodeId="ns=plastics_tcd;i=7013", browseName="ns=plastics_tcd;On", description="Activate the leak stopper mode (emergency operation in case of leaks in the system)")
    )


@o6.objecttype(
    nodeId="ns=plastics_tcd;i=1007",
    browseName="ns=plastics_tcd;ExternalSensorType",
    displayName="ExternalSensorType",
    description="Includes variables for the operation with an external temperature sensor",
)
class ExternalSensorType(ns0.objtypes.BaseObjectType):
    actualValue: ns0.vartypes.AnalogItemType
    automaticModeSwitch: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_tcd;i=6210",
            browseName="ns=plastics_tcd;AutomaticModeSwitch",
            description="Setting whether switching to external sensor is performed automatically (TRUE) or manually (FALSE)",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    closedLoopControl: plastics_rubber.objtypes.ClosedLoopControlType | None
    communicationProtocolType: ns0.vartypes.MultiStateValueDiscreteType
    externalSensorModeOff: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_tcd;i=7016",
            browseName="ns=plastics_tcd;ExternalSensorModeOff",
            description="Deactivate the mode where the external temperature sensor is used for temperature control",
        )
    )
    externalSensorModeOn: o6.node.MethodNode = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_tcd;i=7015",
            browseName="ns=plastics_tcd;ExternalSensorModeOn",
            description="Activate the mode where the external temperature sensor is used for temperature control",
        )
    )
    thermocoupleType: ns0.vartypes.MultiStateValueDiscreteType
    used: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_tcd;i=6206",
            browseName="ns=plastics_tcd;Used",
            description="Return whether an external temperature sensor is used for control",
            dataType=o6.Boolean,
            value=False,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_tcd;i=1002",
    browseName="ns=plastics_tcd;ExternalChannelType",
    displayName="ExternalChannelType",
    description="Includes information for monitoring or controlling of external temperature, flow rate or pressure channels",
)
class ExternalChannelType(ns0.objtypes.BaseObjectType):
    controlMode: ns0.vartypes.MultiStateValueDiscreteType | None
    flowRate: plastics_rubber.objtypes.MonitoredParameterType | None
    pressureDifference: plastics_rubber.objtypes.MonitoredParameterType | None
    pressureMainLine: ns0.vartypes.AnalogItemType | None
    pressureReturnLine: ns0.vartypes.AnalogItemType | None
    switchOff: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_tcd;i=7067", browseName="ns=plastics_tcd;SwitchOff", description="Switch method of the external channel for switching off")
    )
    switchOn: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_tcd;i=7066", browseName="ns=plastics_tcd;SwitchOn", description="Switch method of the external channel for switching on")
    )
    switchedOn: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_tcd;i=6558",
            browseName="ns=plastics_tcd;SwitchedOn",
            description="Information if the external channel is switched on",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    temperature: plastics_rubber.objtypes.MonitoredParameterType | None
    temperatureDifference: plastics_rubber.objtypes.MonitoredParameterType | None
    temperatureMainLine: ns0.vartypes.AnalogItemType | None
    temperatureReturnLine: ns0.vartypes.AnalogItemType | None


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_tcd;i=6510",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_tcd;i=7127",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1, description=o6.LocalizedText("Id of the error, listed in ActiveErrors, that shall be reset"))],
)
o6.call(nodeId="ns=plastics_tcd;i=7127", browseName="ns=plastics_tcd;ResetErrorById", inputArgs=o6.hasProperty(o6.ns["ns=plastics_tcd;i=6510"]))


@o6.objecttype(
    nodeId="ns=plastics_tcd;i=1010",
    browseName="ns=plastics_tcd;OperationType",
    displayName="OperationType",
    description="Contains components which are necessary to operate the TCD",
)
class OperationType(ns0.objtypes.BaseObjectType):
    activeErrors: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_tcd;i=6551",
            browseName="ns=plastics_tcd;ActiveErrors",
            description="List of the active errors of the device",
            dataType=plastics_rubber.datatypes.ActiveErrorDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    deviceMappingNumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_tcd;i=6509",
            browseName="ns=plastics_tcd;DeviceMappingNumber",
            description="Unique identifier/address/number for devices of the same DeviceType within a local network",
            dataType=o6.UInt32,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    highestActiveAlarmSeverity: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_tcd;i=6121",
            browseName="ns=plastics_tcd;HighestActiveAlarmSeverity",
            description="Indication of the severity of the highest active alarm (0 = no active alarm – 1000 = possible error)",
            dataType=o6.UInt16,
        )
    )
    hoursOfOperation: ns0.vartypes.AnalogItemType | None
    identifyDevice: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_tcd;i=7044",
            browseName="ns=plastics_tcd;IdentifyDevice",
            description="The TCD on which this method is called shows itself by e.g. activation of a LED",
        )
    )
    operatingMode: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_tcd;i=6511",
            browseName="ns=plastics_tcd;OperatingMode",
            description="Actual operating mode of the TCD",
            dataType=plastics_tcd_datypes.OperatingModeEnumeration,
        )
    )
    reduceToStandByOff: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_tcd;i=7048",
            browseName="ns=plastics_tcd;ReduceToStandByOff",
            description="Deactivate the cooling down function on the TCD. If it is already in progress, it will be interrupted and the device changes back to the last selected operating mode.",
        )
    )
    reduceToStandByOn: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_tcd;i=7047", browseName="ns=plastics_tcd;ReduceToStandByOn", description="Activate the cooling down function on the TCD followed by switching off"
        )
    )
    resetAllErrors: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_tcd;i=7043", browseName="ns=plastics_tcd;ResetAllErrors", description="Method to reset all errors of the device")
    )
    resetErrorById: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_tcd;i=7127"])
    switchOff: o6.node.MethodNode = o6.hasComponent(
        o6.call(nodeId="ns=plastics_tcd;i=7046", browseName="ns=plastics_tcd;SwitchOff", description="Main switch method of the TCD for switching off")
    )
    switchOn: o6.node.MethodNode = o6.hasComponent(
        o6.call(nodeId="ns=plastics_tcd;i=7045", browseName="ns=plastics_tcd;SwitchOn", description="Main switch method of the TCD for switching on")
    )


@o6.objecttype(
    nodeId="ns=plastics_tcd;i=1009",
    browseName="ns=plastics_tcd;TCDHelpOffNormalAlarmType",
    displayName="TCDHelpOffNormalAlarmType",
    description="HelpOffNormalAlarmType with additional DeviceMappingNumber for identification",
)
class TCDHelpOffNormalAlarmType(plastics_rubber.objtypes.HelpOffNormalAlarmType):
    deviceMappingNumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_tcd;i=7137",
            browseName="ns=plastics_tcd;DeviceMappingNumber",
            description="Unique identifier/address/number for devices of the same DeviceType within a local network",
            dataType=o6.UInt32,
        )
    )


o6.reference(TCD_InterfaceType, "i=41", TCDHelpOffNormalAlarmType)


@o6.objecttype(nodeId="ns=plastics_tcd;i=1011", browseName="ns=plastics_tcd;TCDSpecificationType", displayName="TCDSpecificationType")
class TCDSpecificationType(ns0.objtypes.BaseObjectType):
    connectedLoad: ns0.vartypes.AnalogItemType
    coolingCapacity: ns0.vartypes.AnalogItemType | None
    deviceZoneId: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_tcd;i=7138", browseName="ns=plastics_tcd;DeviceZoneId", dataType=o6.String)
    )
    maxTemperature: ns0.vartypes.AnalogItemType
    nominalFlowRate: ns0.vartypes.AnalogItemType
    powerValue: ns0.vartypes.AnalogItemType


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber, plastics_tcd_datypes
