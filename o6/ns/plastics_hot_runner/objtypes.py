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

"""Generated OPC UA plastics_hot_runner namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
import o6.ns.plastics_rubber as plastics_rubber
from . import datatypes as plastics_hot_runner_datypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.objecttype(
    nodeId="ns=plastics_hot_runner;i=1002",
    browseName="ns=plastics_hot_runner;ZoneAlarmType",
    displayName="ZoneAlarmType",
    description="Represent zone-related text messages of an HRD",
)
class ZoneAlarmType(plastics_rubber.objtypes.HelpOffNormalAlarmType):
    pass


@o6.objecttype(
    nodeId="ns=plastics_hot_runner;i=1007",
    browseName="ns=plastics_hot_runner;MaintenanceInformationType",
    displayName="MaintenanceInformationType",
    description="Information about the maintenance status of various parts of a hot runner device",
)
class MaintenanceInformationType(ns0.objtypes.BaseObjectType):
    coolingFan: plastics_rubber.objtypes.MaintenanceType | None
    heating: plastics_rubber.objtypes.MaintenanceType | None
    safetyTest: plastics_rubber.objtypes.MaintenanceType | None


@o6.objecttype(
    nodeId="ns=plastics_hot_runner;i=1003",
    browseName="ns=plastics_hot_runner;TemperatureRiseMonitoringType",
    displayName="TemperatureRiseMonitoringType",
    description="At maximum controller output, the temperature value must change in a given time by a specified value, otherwise there is an error in the measuring circuit.",
)
class TemperatureRiseMonitoringType(ns0.objtypes.BaseObjectType):
    errorDetected: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6003", browseName="ns=plastics_hot_runner;ErrorDetected", description="Result of the TemperatureRiseMonitoring", dataType=o6.Boolean
        )
    )
    setValueActive: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6002",
            browseName="ns=plastics_hot_runner;SetValueActive",
            description="On / Off for the TemperatureRiseMonitoring",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    setValueTemperatureChange: ns0.vartypes.AnalogItemType | None
    supervisionTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6004",
            browseName="ns=plastics_hot_runner;SupervisionTime",
            description="Specification of the time within the temperature must have changed",
            dataType=ns0.datatypes.Duration,
            value=0.0,
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_hot_runner;i=1006",
    browseName="ns=plastics_hot_runner;ZoneType",
    displayName="ZoneType",
    description="Represents all functionalities of a heating zone, such as temperature monitoring, control, heatup",
)
class ZoneType(ns0.objtypes.BaseObjectType):
    communicationProtocolType: ns0.vartypes.MultiStateValueDiscreteType | None
    controller: ControllerType
    heatUp: HeatUpType | None
    highestActiveAlarmSeverity: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6052",
            browseName="ns=plastics_hot_runner;HighestActiveAlarmSeverity",
            description="Indicates the severity of the highest active alarm related to the current zone",
            dataType=o6.UInt16,
        )
    )
    name: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6051",
            browseName="ns=plastics_hot_runner;Name",
            description="A user given name of the zone",
            dataType=o6.String,
            value="\n      ",
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    temperature: HRDTemperatureType
    temperatureRiseMonitoring: TemperatureRiseMonitoringType | None
    thermocoupleType: ns0.vartypes.MultiStateValueDiscreteType | None


@o6.objecttype(nodeId="ns=plastics_hot_runner;i=1008", browseName="ns=plastics_hot_runner;ZonesType", displayName="ZonesType", description="Container for the zones")
class ZonesType(ns0.objtypes.BaseObjectType):
    nodeVersion: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(nodeId="ns=plastics_hot_runner;i=6136", browseName="NodeVersion", dataType=o6.String, value="\n      ")
    )
    zone_LangleNrRangle: ZoneType


o6.reference(ZonesType, "i=41", "i=2133")


@o6.objecttype(
    nodeId="ns=plastics_hot_runner;i=1011",
    browseName="ns=plastics_hot_runner;HRDTemperatureType",
    displayName="HRDTemperatureType",
    description="Used for setting and monitoring the temperatures in a HRD",
)
class HRDTemperatureType(plastics_rubber.objtypes.ControlledParameterType):
    activeSetValue: ns0.vartypes.MultiStateValueDiscreteType
    boostSetValue: ns0.vartypes.AnalogItemType | None
    boostTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6118",
            browseName="ns=plastics_hot_runner;BoostTime",
            description="Duration of the boost mode after which the set value which was active before boost is becoming active again",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    secondSetValue: ns0.vartypes.AnalogItemType | None
    standbySetValue: ns0.vartypes.AnalogItemType | None
    timeMethodPIDParameters: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6164",
            browseName="ns=plastics_hot_runner;TimeMethodPIDParameters",
            description="Setting of PID parameters with time method",
            dataType=plastics_hot_runner_datypes.TimeMethodPIDParametersDataType,
            valueRank=1,
            arrayDimensions=[0],
            accessLevel=3,
            userAccessLevel=1,
        )
    )


@o6.objecttype(
    nodeId="ns=plastics_hot_runner;i=1010",
    browseName="ns=plastics_hot_runner;HRD_InterfaceType",
    displayName="HRD_InterfaceType",
    description="Root ObjectType representing a hot runner device with its subcomponents",
)
class HRD_InterfaceType(ns0.objtypes.BaseObjectType):
    diagnostics: plastics_rubber.objtypes.DiagnosticsType | None
    displayLanguage: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6240",
            browseName="ns=plastics_hot_runner;DisplayLanguage",
            description="Setting of desired language on the user interface at the HRD",
            dataType=ns0.datatypes.LocaleId,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    identification: plastics_rubber.objtypes.IdentificationType
    machineConfiguration: plastics_rubber.objtypes.MachineConfigurationType
    maintenanceInformation: MaintenanceInformationType | None
    operation: OperationType
    zones: ZonesType


o6.reference(HRD_InterfaceType, "i=41", "ns=plastics_rubber;i=1052")


@o6.objecttype(
    nodeId="ns=plastics_hot_runner;i=1004",
    browseName="ns=plastics_hot_runner;HeatUpType",
    displayName="HeatUpType",
    description="Alternative to the SetRamp functionality of MonitoredParameterType defined in OPC 40083. With HeatUpType, it can be pre-defined how the control circuit is to be operated when it is switched on for the next time; with or without heat-up process.",
)
class HeatUpType(ns0.objtypes.BaseObjectType):
    evenHeatUpEnabled: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6013",
            browseName="ns=plastics_hot_runner;EvenHeatUpEnabled",
            description="Enables even heat-up process until nominal SetValue of Temperature of ZoneType is reached",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    manualOutputLimitActive: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6008",
            browseName="ns=plastics_hot_runner;ManualOutputLimitActive",
            description="Activates heat-up process with pre-defined SetValueManualOutputLimit until SetValueTemperature is reached",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    relayHeatingGroup: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6238",
            browseName="ns=plastics_hot_runner;RelayHeatingGroup",
            description="Number of the heating group for relay heating",
            dataType=o6.Byte,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    relayHeatingTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6484",
            browseName="ns=plastics_hot_runner;RelayHeatingTime",
            description="Time for relay heating of the zone. When RelayHeatingTime of all zones of a heating group have expired, the next group starts heating.",
            dataType=ns0.datatypes.Duration,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    setValueManualOutputLimit: ns0.vartypes.AnalogItemType | None
    setValueTemperature: ns0.vartypes.AnalogItemType | None


@o6.objecttype(
    nodeId="ns=plastics_hot_runner;i=1005",
    browseName="ns=plastics_hot_runner;ControllerType",
    displayName="ControllerType",
    description="Configuration and operation of the zone controller",
)
class ControllerType(ns0.objtypes.BaseObjectType):
    actualOutput: ns0.vartypes.AnalogItemType | None
    actualType: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6025",
            browseName="ns=plastics_hot_runner;ActualType",
            description="Actual value for the controller type used by the zone",
            dataType=plastics_hot_runner_datypes.ControllerTypeEnumeration,
            value=plastics_hot_runner_datypes.ControllerTypeEnumeration.CLOSED_LOOP_CONTROL,
        )
    )
    actualValueActive: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6022",
            browseName="ns=plastics_hot_runner;ActualValueActive",
            description="Indicates the current status of the controller",
            dataType=o6.Boolean,
        )
    )
    automaticReferenceZoneSelection: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6500",
            browseName="ns=plastics_hot_runner;AutomaticReferenceZoneSelection",
            description="If true, the HRD selects automatically the reference zone.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    averageControllerOutput: ns0.vartypes.AnalogItemType | None
    loadCurrent: plastics_rubber.objtypes.MonitoredParameterType | None
    loadPower: plastics_rubber.objtypes.MonitoredParameterType | None
    lowerOutput: ns0.vartypes.AnalogItemType | None
    outputTime: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6030",
            browseName="ns=plastics_hot_runner;OutputTime",
            description="Time basis for operating the actuator",
            dataType=ns0.datatypes.Duration,
            value=0.0,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    referenceZone: ns0.vartypes.PropertyType | None = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6031",
            browseName="ns=plastics_hot_runner;ReferenceZone",
            description="If zones are to operate parallel to a control zone, the reference relation can be realised with this parameter.",
            dataType=o6.UInt32,
            value=0,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    setValueActive: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6021",
            browseName="ns=plastics_hot_runner;SetValueActive",
            description="A control zone is switched on and off with this parameter.",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    setValueManualOutput: ns0.vartypes.AnalogItemType | None
    setValueType: ns0.vartypes.MultiStateValueDiscreteType
    upperOutput: ns0.vartypes.AnalogItemType | None
    upperSetValueCascade: ns0.vartypes.AnalogItemType | None


ns0.vartypes.PropertyType(
    nodeId="ns=plastics_hot_runner;i=6378",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_hot_runner;i=7019",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="Id", dataType=o6.String, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_hot_runner;i=7019",
    browseName="ns=plastics_hot_runner;ResetErrorById",
    description="Method to reset one error of the device",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_hot_runner;i=6378"]),
)

ns0.vartypes.PropertyType(
    nodeId="ns=plastics_hot_runner;i=6651",
    browseName="InputArguments",
    modellingRule="Mandatory",
    parent="ns=plastics_hot_runner;i=7031",
    referenceType=ns0.reftypes.HasProperty,
    dataType=ns0.datatypes.Argument,
    valueRank=1,
    arrayDimensions=[1],
    value=[ns0.datatypes.Argument(name="ReactionOnDisconnect", dataType=o6.UInt16, valueRank=-1)],
)
o6.call(
    nodeId="ns=plastics_hot_runner;i=7031",
    browseName="ns=plastics_hot_runner;SetReactionOnDisconnect",
    description="Method to set ReactionOnDisconnect and SessionNameForReactionOnDisconnect",
    inputArgs=o6.hasProperty(o6.ns["ns=plastics_hot_runner;i=6651"]),
)


@o6.objecttype(
    nodeId="ns=plastics_hot_runner;i=1009",
    browseName="ns=plastics_hot_runner;OperationType",
    displayName="OperationType",
    description="Contains components which are necessary to operate the HRD",
)
class OperationType(ns0.objtypes.BaseObjectType):
    activeErrors: ns0.vartypes.BaseDataVariableType = o6.hasComponent(
        ns0.vartypes.BaseDataVariableType(
            nodeId="ns=plastics_hot_runner;i=6215",
            browseName="ns=plastics_hot_runner;ActiveErrors",
            description="List of the active errors of the device",
            dataType=plastics_rubber.datatypes.ClassifiedActiveErrorDataType,
            valueRank=1,
            arrayDimensions=[0],
        )
    )
    activeSetValues: ns0.vartypes.MultiStateValueDiscreteType
    deviceMappingNumber: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6214",
            browseName="ns=plastics_hot_runner;DeviceMappingNumber",
            description="Unique identifier/address/number for devices of the same DeviceType within a local network",
            dataType=o6.UInt32,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    enablePower: ns0.vartypes.PropertyType = o6.hasProperty(  # WARNING: The source NodeSet value does not match the declared DataType.
        # It is intentionally omitted; the server supplies a typed default.
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6216",
            browseName="ns=plastics_hot_runner;EnablePower",
            description="Global power control switch for all zone controllers",
            dataType=o6.Boolean,
            accessLevel=3,
            userAccessLevel=1,
        )
    )
    evenHeatUpMaxTemperatureDifference: ns0.vartypes.AnalogItemType | None
    highestActiveAlarmSeverity: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6213",
            browseName="ns=plastics_hot_runner;HighestActiveAlarmSeverity",
            description="Indication of the severity of the highest active alarm",
            dataType=o6.UInt16,
        )
    )
    identifyDevice: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(
            nodeId="ns=plastics_hot_runner;i=7006",
            browseName="ns=plastics_hot_runner;IdentifyDevice",
            description="The peripheral device on which this method is called shows itself by e.g. activation of a LED.",
        )
    )
    reactionOnDisconnect: ns0.vartypes.MultiStateValueDiscreteType
    resetAllErrors: o6.node.MethodNode | None = o6.hasComponent(
        o6.call(nodeId="ns=plastics_hot_runner;i=7007", browseName="ns=plastics_hot_runner;ResetAllErrors", description="Method to reset all errors of the device")
    )
    resetErrorById: o6.node.MethodNode | None = o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=7019"])
    sessionNameForReactionOnDisconnect: ns0.vartypes.PropertyType = o6.hasProperty(
        ns0.vartypes.PropertyType(
            nodeId="ns=plastics_hot_runner;i=6649",
            browseName="ns=plastics_hot_runner;SessionNameForReactionOnDisconnect",
            description="Contains the sessionName of the connection with the client relevant for ReactionOnDisconnect",
            dataType=o6.String,
        )
    )
    setReactionOnDisconnect: o6.node.MethodNode = o6.hasComponent(o6.ns["ns=plastics_hot_runner;i=7031"])


del Any, TYPE_CHECKING, uuid, o6, di, ns0, plastics_rubber, plastics_hot_runner_datypes
