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

"""Generated OPC UA fdt namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.di as di
import o6.ns.ns0 as ns0
from . import reftypes as fdt_reftypes

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(
    nodeId="ns=fdt;i=3001",
    browseName="AlarmType",
    description="Identifier for the alarm type to show the association between high- and low alarm and high-high- and low-low-alarm. (Provides mapping for Fdt.Dtm.DataAccess.AlarmType.)",
)
class AlarmType(ns0.datatypes.Enumeration):
    HIGH_HIGH_ALARM = o6.enumfield(0, name="HighHighAlarm")
    HIGH_ALARM = o6.enumfield(1, name="HighAlarm")
    LOW_LOW_ALARM = o6.enumfield(2, name="LowLowAlarm")
    LOW_ALARM = o6.enumfield(3, name="LowAlarm")


@o6.enumtype(nodeId="ns=fdt;i=3002", browseName="ApplicationIdEnumeration", description="Identifies type of an application or function. (Provides mapping for Fdt.ApplicationId)")
class ApplicationIdEnumeration(ns0.datatypes.Enumeration):
    ADJUST_SET_VALUE = o6.enumfield(0, name="AdjustSetValue")
    ASSET_MANAGEMENT = o6.enumfield(1, name="AssetManagement")
    AUDIT_TRAIL = o6.enumfield(2, name="AuditTrail")
    CONFIGURATION = o6.enumfield(3, name="Configuration")
    DIAGNOSIS = o6.enumfield(4, name="Diagnosis")
    FORCE = o6.enumfield(5, name="Force")
    OBSERVE = o6.enumfield(6, name="Observe")
    OFFLINE_COMPARE = o6.enumfield(7, name="OfflineCompare")
    OFFLINE_PARAMETERIZE = o6.enumfield(8, name="OfflineParameterize")
    ONLINE_COMPARE = o6.enumfield(9, name="OnlineCompare")
    ONLINE_PARAMETERIZE = o6.enumfield(10, name="OnlineParameterize")
    IDENTIFY = o6.enumfield(11, name="Identify")
    CALIBRATION = o6.enumfield(12, name="Calibration")
    MAIN_OPERATION = o6.enumfield(13, name="MainOperation")
    NETWORK_MANAGEMENT = o6.enumfield(14, name="NetworkManagement")


@o6.enumtype(nodeId="ns=fdt;i=3003", browseName="RangeType", description="Type of a range device data. (Provides mapping to Fdt.Dtm.DataAccess.RangeType)")
class RangeType(ns0.datatypes.Enumeration):
    LOWER_RANGE = o6.enumfield(0, name="LowerRange")
    UPPER_RANGE = o6.enumfield(1, name="UpperRange")


@o6.enumtype(nodeId="ns=fdt;i=3004", browseName="SubstitutionType", description="Type of substitution data. (Provides mapping to Fdt.Dtm.DataAccess.SubstitutionType)")
class SubstitutionType(ns0.datatypes.Enumeration):
    LAST_VALUE = o6.enumfield(0, name="LastValue")
    LAST_VALID_VALUE = o6.enumfield(1, name="LastValidValue")
    UPPER_RANGE = o6.enumfield(2, name="UpperRange")
    LOWER_RANGE = o6.enumfield(3, name="LowerRange")


@o6.enumtype(nodeId="ns=fdt;i=3005", browseName="ClassificationDomainId")
class ClassificationDomainId(ns0.datatypes.Enumeration):
    POWER_DISTRIBUTION = o6.enumfield(0, name="PowerDistribution")
    MOTION_CONTROL = o6.enumfield(1, name="MotionControl")
    MEASUREMENT = o6.enumfield(2, name="Measurement")
    OPERATOR_INTERFACE = o6.enumfield(3, name="OperatorInterface")
    MODULES_AND_CONTROLLERS = o6.enumfield(4, name="ModulesAndControllers")
    COMMUNICATION = o6.enumfield(5, name="Communication")


@o6.enumtype(nodeId="ns=fdt;i=3007", browseName="IECDatatype")
class IECDatatype(ns0.datatypes.Enumeration):
    BOOL = o6.enumfield(0, name="BOOL")
    SINT = o6.enumfield(1, name="SINT")
    INT = o6.enumfield(2, name="INT")
    DINT = o6.enumfield(3, name="DINT")
    LINT = o6.enumfield(4, name="LINT")
    USINT = o6.enumfield(5, name="USINT")
    UINT = o6.enumfield(6, name="UINT")
    UDINT = o6.enumfield(7, name="UDINT")
    ULINT = o6.enumfield(8, name="ULINT")
    REAL = o6.enumfield(9, name="REAL")
    LREAL = o6.enumfield(10, name="LREAL")
    TIME = o6.enumfield(11, name="TIME")
    DATE = o6.enumfield(12, name="DATE")
    TIME_OF_DAY = o6.enumfield(13, name="TimeOfDay")
    DATE_AND_TIME = o6.enumfield(14, name="DateAndTime")
    STRING = o6.enumfield(15, name="STRING")
    BYTE = o6.enumfield(16, name="BYTE")
    WORD = o6.enumfield(17, name="WORD")
    DWORD = o6.enumfield(18, name="DWORD")
    LWORD = o6.enumfield(19, name="LWORD")
    WSTRING = o6.enumfield(20, name="WSTRING")


@o6.enumtype(
    nodeId="ns=fdt;i=3008",
    browseName="ClassificationId",
    description="Classification according to device primary function. \n(Provides mapping to Fdt.Dtm.DeviceClassification.ClassificationId)",
)
class ClassificationId(ns0.datatypes.Enumeration):
    FLOW = o6.enumfield(0, name="Flow")
    LEVEL = o6.enumfield(1, name="Level")
    PRESSURE = o6.enumfield(2, name="Pressure")
    TEMPERATURE = o6.enumfield(3, name="Temperature")
    VALVE = o6.enumfield(4, name="Valve")
    POSITIONER = o6.enumfield(5, name="Positioner")
    ACTUATOR = o6.enumfield(6, name="Actuator")
    NC_RC = o6.enumfield(7, name="Nc_rc")
    ENCODER = o6.enumfield(8, name="Encoder")
    SPEED_DRIVE = o6.enumfield(9, name="SpeedDrive")
    HMI = o6.enumfield(10, name="Hmi")
    ANALOG_INPUT = o6.enumfield(11, name="AnalogInput")
    ANALOG_OUTPUT = o6.enumfield(12, name="AnalogOutput")
    DIGITAL_INPUT = o6.enumfield(13, name="DigitalInput")
    DIGITAL_OUTPUT = o6.enumfield(14, name="DigitalOutput")
    ELECTROCHEMICAL_ANALYSER = o6.enumfield(15, name="ElectrochemicalAnalyser")
    DTM_SPECIFIC = o6.enumfield(16, name="DtmSpecific")
    UNIVERSAL = o6.enumfield(17, name="Universal")
    ANALYSER = o6.enumfield(18, name="Analyser")
    REMOTE_IO = o6.enumfield(19, name="RemoteIO")
    ANALOG_COMBINED_IO = o6.enumfield(20, name="AnalogCombinedIO")
    DIGITAL_COMBINED_IO = o6.enumfield(21, name="DigitalCombinedIO")
    RECORDER = o6.enumfield(22, name="Recorder")
    CONTROLLER = o6.enumfield(23, name="Controller")
    ANGLE = o6.enumfield(24, name="Angle")
    LIMIT_SWITCH = o6.enumfield(25, name="LimitSwitch")
    CONVERTER = o6.enumfield(26, name="Converter")
    MOTOR = o6.enumfield(27, name="Motor")
    SWITCHBOARD = o6.enumfield(28, name="Switchboard")
    CIRCUIT_BREAKER = o6.enumfield(29, name="CircuitBreaker")
    POWER_MONITORING = o6.enumfield(30, name="PowerMonitoring")
    DISTRIBUTION_PANEL = o6.enumfield(31, name="DistributionPanel")
    CONTACTOR = o6.enumfield(32, name="Contactor")
    PROTECTION_STARTER = o6.enumfield(33, name="ProtectionStarter")
    SOFT_STARTER = o6.enumfield(34, name="SoftStarter")
    DRIVE = o6.enumfield(35, name="Drive")
    AXIS_CONTROL = o6.enumfield(36, name="AxisControl")
    MOTOR_CONTROL_CENTER = o6.enumfield(37, name="MotorControlCenter")
    CONTROL_VALVE = o6.enumfield(38, name="ControlValve")
    ELECTRICAL = o6.enumfield(39, name="Electrical")
    DENSITY = o6.enumfield(40, name="Density")
    QUALITY = o6.enumfield(41, name="Quality")
    SPEED_OR_ROTARY_FREQUENCY = o6.enumfield(42, name="SpeedOrRotaryFrequency")
    RADIATION = o6.enumfield(43, name="Radiation")
    WEIGHT_MASS = o6.enumfield(44, name="WeightMass")
    DISTANCE_OR_POSITION_PRESENCE = o6.enumfield(45, name="DistanceOrPositionPresence")
    PUSH_BUTTON = o6.enumfield(46, name="PushButton")
    JOYSTICK = o6.enumfield(47, name="Joystick")
    KEYPAD = o6.enumfield(48, name="Keypad")
    PILOT_LIGHT = o6.enumfield(49, name="PilotLight")
    STACK_LIGHT = o6.enumfield(50, name="StackLight")
    DISPLAY = o6.enumfield(51, name="Display")
    COMBINED_BUTTONS_AND_LIGHTS = o6.enumfield(52, name="CombinedButtonsAndLights")
    OPERATOR_STATION = o6.enumfield(53, name="OperatorStation")
    GENERAL_INPUT = o6.enumfield(54, name="GeneralInput")
    GENERAL_OUTPUT = o6.enumfield(55, name="GeneralOutput")
    COMBINED_INPUT_OUTPUT = o6.enumfield(56, name="CombinedInputOutput")
    RELAY = o6.enumfield(57, name="Relay")
    TIMER = o6.enumfield(58, name="Timer")
    SCANNER = o6.enumfield(59, name="Scanner")
    PROGRAMMABLE_CONTROLLER = o6.enumfield(60, name="ProgrammableController")
    COMMUNICATION_ADAPTER = o6.enumfield(61, name="CommunicationAdapter")
    GATEWAY = o6.enumfield(62, name="Gateway")


@o6.enumtype(
    nodeId="ns=fdt;i=3009",
    browseName="SupportedTransfer",
    description="This enumeration provides values to describe the types of transfers provided for a device. (Provides mapping to Fdt.Dtm.SupportedTransfer)",
)
class SupportedTransfer(ns0.datatypes.Enumeration):
    NONE = o6.enumfield(0, name="None")
    ONLY_DOWNLOAD = o6.enumfield(1, name="OnlyDownload")
    ONLY_UPLOAD = o6.enumfield(2, name="OnlyUpload")
    BOTH_UPLOAD_AND_DOWNLOAD = o6.enumfield(3, name="BothUploadAndDownload")


@o6.enumtype(nodeId="ns=fdt;i=3010", browseName="DocumentClassification", description="Classification of a document. (Provides mapping for Fdt.Dtm.DocumentClassification)")
class DocumentClassification(ns0.datatypes.Enumeration):
    HELP = o6.enumfield(0, name="Help")
    TECHNICAL_DOCUMENTATION = o6.enumfield(1, name="TechnicalDocumentation")
    ORDERING_INFORMATION = o6.enumfield(2, name="OrderingInformation")
    MISCELLANEOUS = o6.enumfield(3, name="Miscellaneous")
    TENDER_SPECIFICATION = o6.enumfield(4, name="TenderSpecification")


@o6.datatype(nodeId="ns=fdt;i=3011", browseName="FdtDeviceClassificationType", defaultEncodingId="ns=fdt;i=5007")
class FdtDeviceClassificationType(ns0.datatypes.Structure):
    classificationDomain: ClassificationDomainId
    deviceClassification: ClassificationId


@o6.enumtype(nodeId="ns=fdt;i=3012", browseName="FunctionExecutionResultState")
class FunctionExecutionResultState(ns0.datatypes.Enumeration):
    CANCEL = o6.enumfield(0, name="Cancel")
    SUCCESS = o6.enumfield(1, name="Success")
    FAIL = o6.enumfield(2, name="Fail")


@o6.enumtype(nodeId="ns=fdt;i=3013", browseName="SignalTypeEnumeration")
class SignalTypeEnumeration(ns0.datatypes.Enumeration):
    INPUT = o6.enumfield(0, name="Input")
    OUTPUT = o6.enumfield(1, name="Output")


@o6.datatype(nodeId="ns=fdt;i=3014", browseName="SemanticInfoType", defaultEncodingId="ns=fdt;i=5005")
class SemanticInfoType(ns0.datatypes.Structure):
    applicationDomain: o6.String
    semanticId: o6.String


@o6.datatype(nodeId="ns=fdt;i=3015", browseName="DataRefType", description="Reference to a data item", defaultEncodingId="ns=fdt;i=5012")
class DataRefType(ns0.datatypes.Structure):
    dataId: o6.String
    semanticInfo: SemanticInfoType


del Any, TYPE_CHECKING, uuid, o6, di, ns0, fdt_reftypes
