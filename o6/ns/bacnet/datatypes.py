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

"""Generated OPC UA bacnet namespace declarations."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
import uuid
import o6
import o6.ns.ns0 as ns0

if TYPE_CHECKING:
    from o6.node import ObjectNode as _ObjectNode
    from o6.node import VariableNode as _VariableNode
else:
    _ObjectNode = object
    _VariableNode = object


@o6.enumtype(nodeId="ns=bacnet;i=3001", browseName="BACnetReliability")
class BACnetReliability(ns0.datatypes.Enumeration):
    NO_FAULT_DETECTED = o6.enumfield(0, name="NoFaultDetected")
    NO_SENSOR = o6.enumfield(1, name="NoSensor")
    OVER_RANGE = o6.enumfield(2, name="OverRange")
    UNDER_RANGE = o6.enumfield(3, name="UnderRange")
    OPEN_LOOP = o6.enumfield(4, name="OpenLoop")
    SHORTED_LOOP = o6.enumfield(5, name="ShortedLoop")
    NO_OUTPUT = o6.enumfield(6, name="NoOutput")
    UNRELIABLE_OTHER = o6.enumfield(7, name="UnreliableOther")
    PROCESS_ERROR = o6.enumfield(8, name="ProcessError")
    MULTI_STATE_FAULT = o6.enumfield(9, name="MultiStateFault")
    CONFIGURATION_ERROR = o6.enumfield(10, name="ConfigurationError")
    COMMUNICATION_FAILURE = o6.enumfield(12, name="CommunicationFailure")
    MEMBER_FAULT = o6.enumfield(13, name="MemberFault")
    MONITORED_OBJECT_FAULT = o6.enumfield(14, name="MONITORED_OBJECT_FAULT")
    TRIPPED = o6.enumfield(15, name="TRIPPED")


@o6.enumtype(nodeId="ns=bacnet;i=3002", browseName="BACnetNotifyType")
class BACnetNotifyType(ns0.datatypes.Enumeration):
    ALARM = o6.enumfield(0, name="Alarm")
    EVENT = o6.enumfield(1, name="Event")
    ACK_NOTIFICATION = o6.enumfield(2, name="AckNotification")


@o6.enumtype(nodeId="ns=bacnet;i=3003", browseName="BACnetEventState")
class BACnetEventState(ns0.datatypes.Enumeration):
    NORMAL = o6.enumfield(0, name="Normal")
    FAULT = o6.enumfield(1, name="Fault")
    OFF_NORMAL = o6.enumfield(2, name="OffNormal")
    HIGH_LIMIT = o6.enumfield(3, name="HighLimit")
    LOW_LIMIT = o6.enumfield(4, name="LowLimit")
    LIFE_SAFETY_ALARM = o6.enumfield(5, name="LifeSafetyAlarm")


@o6.enumtype(nodeId="ns=bacnet;i=3005", browseName="BACnetBinaryPV")
class BACnetBinaryPV(ns0.datatypes.Enumeration):
    INACTIVE = o6.enumfield(0, name="Inactive")
    ACTIVE = o6.enumfield(1, name="Active")


@o6.enumtype(nodeId="ns=bacnet;i=3007", browseName="BACnetPolarity")
class BACnetPolarity(ns0.datatypes.Enumeration):
    NORMAL = o6.enumfield(0, name="Normal")
    REVERSE = o6.enumfield(1, name="Reverse")


@o6.enumtype(nodeId="ns=bacnet;i=3008", browseName="BACnetAction")
class BACnetAction(ns0.datatypes.Enumeration):
    DIRECT = o6.enumfield(0, name="direct")
    REVERSE = o6.enumfield(1, name="reverse")


@o6.datatype(nodeId="ns=bacnet;i=3010", browseName="BACnetElementCount", parent="i=7")
class BACnetElementCount:
    pass


@o6.datatype(nodeId="ns=bacnet;i=3011", browseName="BACnetPropertyCount", parent="i=7")
class BACnetPropertyCount:
    pass


@o6.datatype(nodeId="ns=bacnet;i=3012", browseName="BACnetObjectCount", parent="i=7")
class BACnetObjectCount:
    pass


@o6.datatype(nodeId="ns=bacnet;i=3013", browseName="BACnetDeviceCount", parent="i=7")
class BACnetDeviceCount:
    pass


@o6.enumtype(nodeId="ns=bacnet;i=3014", browseName="BACnetMonth")
class BACnetMonth(ns0.datatypes.Enumeration):
    JANUARY = o6.enumfield(1, name="January")
    FEBRUARY = o6.enumfield(2, name="February")
    MARCH = o6.enumfield(3, name="March")
    APRIL = o6.enumfield(4, name="April")
    MAY = o6.enumfield(5, name="May")
    JUNE = o6.enumfield(6, name="June")
    JULY = o6.enumfield(7, name="July")
    AUGUST = o6.enumfield(8, name="August")
    SEPTEMBER = o6.enumfield(9, name="September")
    OCTOBER = o6.enumfield(10, name="October")
    NOVEMBER = o6.enumfield(11, name="November")
    DECEMBER = o6.enumfield(12, name="December")
    ODD = o6.enumfield(13, name="Odd")
    EVEN = o6.enumfield(14, name="Even")
    UNSPECIFIED = o6.enumfield(255, name="Unspecified")


@o6.datatype(nodeId="ns=bacnet;i=3015", browseName="BACnetYear", description="0 = Undefined", parent="i=5")
class BACnetYear:
    pass


@o6.enumtype(nodeId="ns=bacnet;i=3018", browseName="BACnetDeviceCommunicationEnabled")
class BACnetDeviceCommunicationEnabled(ns0.datatypes.Enumeration):
    ENABLE = o6.enumfield(0, name="Enable")
    DISABLE = o6.enumfield(1, name="Disable")
    DISABLE_INITIATION = o6.enumfield(2, name="DisableInitiation")


@o6.datatype(nodeId="ns=bacnet;i=3019", browseName="BACnetTime", defaultEncodingId="ns=bacnet;i=5021")
class BACnetTime(ns0.datatypes.Structure):
    hour: o6.Byte
    minute: o6.Byte
    second: o6.Byte
    hundredths: o6.Byte


@o6.datatype(nodeId="ns=bacnet;i=3020", browseName="BACnetObjectIdentifier", parent="i=7")
class BACnetObjectIdentifier:
    pass


@o6.enumtype(nodeId="ns=bacnet;i=3021", browseName="BACnetDay")
class BACnetDay(ns0.datatypes.Enumeration):
    DAYS_NUMBERED_1_7 = o6.enumfield(1, name="days numbered 1-7")
    DAYS_NUMBERED_8_14 = o6.enumfield(2, name="days numbered 8-14")
    DAYS_NUMBERED_15_21 = o6.enumfield(3, name="days numbered 15-21")
    DAYS_NUMBERED_22_28 = o6.enumfield(4, name="days numbered 22-28")
    DAYS_NUMBERED_29_31 = o6.enumfield(5, name="days numbered 29-31")
    LAST_7_DAYS_OF_THIS_MONTH = o6.enumfield(6, name="last 7 days of this month")
    ANY_WEEK_OF_THIS_MONTH = o6.enumfield(255, name="any week of this month")


@o6.datatype(nodeId="ns=bacnet;i=3022", browseName="BACnetAddress", defaultEncodingId="ns=bacnet;i=5041")
class BACnetAddress(ns0.datatypes.Structure):
    networkNumber: o6.UInt16
    macAddress: o6.ByteString


@o6.datatype(nodeId="ns=bacnet;i=3023", browseName="BACnetClientCOV", defaultEncodingId="ns=bacnet;i=5011")
class BACnetClientCOV(ns0.datatypes.Union):
    real_increment: o6.Float


@o6.enumtype(nodeId="ns=bacnet;i=3025", browseName="BACnetDayOfMonth")
class BACnetDayOfMonth(ns0.datatypes.Enumeration):
    _1 = o6.enumfield(1, name="1")
    _2 = o6.enumfield(2, name="2")
    _3 = o6.enumfield(3, name="3")
    _4 = o6.enumfield(4, name="4")
    _5 = o6.enumfield(5, name="5")
    _6 = o6.enumfield(6, name="6")
    _7 = o6.enumfield(7, name="7")
    _8 = o6.enumfield(8, name="8")
    _9 = o6.enumfield(9, name="9")
    _10 = o6.enumfield(10, name="10")
    _11 = o6.enumfield(11, name="11")
    _12 = o6.enumfield(12, name="12")
    _13 = o6.enumfield(13, name="13")
    _14 = o6.enumfield(14, name="14")
    _15 = o6.enumfield(15, name="15")
    _16 = o6.enumfield(16, name="16")
    _17 = o6.enumfield(17, name="17")
    _18 = o6.enumfield(18, name="18")
    _19 = o6.enumfield(19, name="19")
    _20 = o6.enumfield(20, name="20")
    _21 = o6.enumfield(21, name="21")
    _22 = o6.enumfield(22, name="22")
    _23 = o6.enumfield(23, name="23")
    _24 = o6.enumfield(24, name="24")
    _25 = o6.enumfield(25, name="25")
    _26 = o6.enumfield(26, name="26")
    _27 = o6.enumfield(27, name="27")
    _28 = o6.enumfield(28, name="28")
    _29 = o6.enumfield(29, name="29")
    _30 = o6.enumfield(30, name="30")
    _31 = o6.enumfield(31, name="31")
    LAST_DAY_OF_MONTH = o6.enumfield(32, name="Last day of month")
    ODD_DAY_OF_MONTH = o6.enumfield(33, name="Odd day of month")
    EVEN_DAY_OF_MONTH = o6.enumfield(34, name="Even day of month")
    UNSPECIFIED = o6.enumfield(255, name="Unspecified")


@o6.enumtype(nodeId="ns=bacnet;i=3029", browseName="BACnetEventEnumType")
class BACnetEventEnumType(ns0.datatypes.Enumeration):
    CHANGE_OF_BITSTRING = o6.enumfield(0, name="ChangeOfBitstring")
    CHANGE_OF_STATE = o6.enumfield(1, name="ChangeOfState")
    CHANGE_OF_VALUE = o6.enumfield(2, name="ChangeOfValue")
    COMMAND_FAILURE = o6.enumfield(3, name="CommandFailure")
    FLOATING_LIMIT = o6.enumfield(4, name="FloatingLimit")
    OUT_OF_RANGE = o6.enumfield(5, name="OutOfRange")
    CHANGE_OF_LIFE_SAFETY = o6.enumfield(8, name="ChangeOfLifeSafety")
    EXTENDED = o6.enumfield(9, name="Extended")
    BUFFER_READY = o6.enumfield(10, name="BufferReady")
    UNSIGNED_RANGE = o6.enumfield(11, name="UnsignedRange")


@o6.enumtype(nodeId="ns=bacnet;i=3030", browseName="BACnetProgramRequest")
class BACnetProgramRequest(ns0.datatypes.Enumeration):
    READY = o6.enumfield(0, name="Ready")
    LOAD = o6.enumfield(1, name="Load")
    RUN = o6.enumfield(2, name="Run")
    HALT = o6.enumfield(3, name="Halt")
    RESTART = o6.enumfield(4, name="Restart")
    UNLOAD = o6.enumfield(5, name="Unload")


@o6.enumtype(nodeId="ns=bacnet;i=3031", browseName="BACnetProgramStates")
class BACnetProgramStates(ns0.datatypes.Enumeration):
    IDLE = o6.enumfield(0, name="Idle")
    LOADING = o6.enumfield(1, name="Loading")
    RUNNING = o6.enumfield(2, name="Running")
    WAITING = o6.enumfield(3, name="Waiting")
    HALTED = o6.enumfield(4, name="Halted")
    UNLOADING = o6.enumfield(5, name="Unloading")


@o6.enumtype(nodeId="ns=bacnet;i=3032", browseName="BACnetProgramError")
class BACnetProgramError(ns0.datatypes.Enumeration):
    NORMAL = o6.enumfield(0, name="Normal")
    LOAD_FAILED = o6.enumfield(1, name="LoadFailed")
    INTERNAL = o6.enumfield(2, name="Internal")
    PROGRAM = o6.enumfield(3, name="Program")
    OTHER = o6.enumfield(4, name="Other")


@o6.enumtype(nodeId="ns=bacnet;i=3033", browseName="BACnetDeviceStatus")
class BACnetDeviceStatus(ns0.datatypes.Enumeration):
    OPERATIONAL = o6.enumfield(0, name="Operational")
    OPERATIONAL_READ_ONLY = o6.enumfield(1, name="OperationalReadOnly")
    DOWNLOAD_REQUIRED = o6.enumfield(2, name="DownloadRequired")
    DOWNLOAD_IN_PROGRESS = o6.enumfield(3, name="DownloadInProgress")
    NON_OPERATIONAL = o6.enumfield(4, name="NonOperational")
    BACKUP_IN_PROGRESS = o6.enumfield(5, name="BackupInProgress")


@o6.enumtype(nodeId="ns=bacnet;i=3035", browseName="BACnetLifeSafetyMode")
class BACnetLifeSafetyMode(ns0.datatypes.Enumeration):
    OFF = o6.enumfield(0, name="Off")
    ON = o6.enumfield(1, name="On")
    TEST = o6.enumfield(2, name="Test")
    MANNED = o6.enumfield(3, name="Manned")
    UN_MANNED = o6.enumfield(4, name="UnManned")
    ARMED = o6.enumfield(5, name="Armed")
    DISARMED = o6.enumfield(6, name="Disarmed")
    PREARMED = o6.enumfield(7, name="Prearmed")
    SLOW = o6.enumfield(8, name="Slow")
    FAST = o6.enumfield(9, name="Fast")
    DISCONNECTED = o6.enumfield(10, name="Disconnected")
    ENABLED = o6.enumfield(11, name="Enabled")
    DISABLED = o6.enumfield(12, name="Disabled")
    AUTOMATIC_RELEASE_DISABLED = o6.enumfield(13, name="AutomaticReleaseDisabled")
    DEFAULT = o6.enumfield(14, name="Default")


@o6.enumtype(nodeId="ns=bacnet;i=3036", browseName="BACnetLifeSafetyState")
class BACnetLifeSafetyState(ns0.datatypes.Enumeration):
    QUIET = o6.enumfield(0, name="Quiet")
    PRE_ALARM = o6.enumfield(1, name="PreAlarm")
    ALARM = o6.enumfield(2, name="Alarm")
    FAULT = o6.enumfield(3, name="Fault")
    FAULT_PRE_ALARM = o6.enumfield(4, name="FaultPreAlarm")
    FAULT_ALARM = o6.enumfield(5, name="FaultAlarm")
    NOT_READY = o6.enumfield(6, name="NotReady")
    ACTIVE = o6.enumfield(7, name="Active")
    TAMPER = o6.enumfield(8, name="Tamper")
    TEST_ALARM = o6.enumfield(9, name="TestAlarm")
    TEST_ACTIVE = o6.enumfield(10, name="TestActive")
    TEST_FAULT = o6.enumfield(11, name="TestFault")
    TEST_FAULT_ALARM = o6.enumfield(12, name="TestFaultAlarm")
    HOLDUP = o6.enumfield(13, name="Holdup")
    DURESS = o6.enumfield(14, name="Duress")
    TAMPER_ALARM = o6.enumfield(15, name="TamperAlarm")
    ABNORMAL = o6.enumfield(16, name="Abnormal")
    EMERGENCY_POWER = o6.enumfield(17, name="EmergencyPower")
    DELAYED = o6.enumfield(18, name="Delayed")
    BLOCKED = o6.enumfield(19, name="Blocked")
    LOCAL_ALARM = o6.enumfield(20, name="LocalAlarm")
    GENERAL_ALARM = o6.enumfield(21, name="GeneralAlarm")
    SUPERVISORY = o6.enumfield(22, name="Supervisory")
    TEST_SUPERVISORY = o6.enumfield(23, name="TestSupervisory")


@o6.datatype(nodeId="ns=bacnet;i=3028", browseName="BACnetPropertyStates", defaultEncodingId="ns=bacnet;i=5047")
class BACnetPropertyStates(ns0.datatypes.Structure):
    booleanValue: o6.Boolean
    binaryValue: BACnetBinaryPV
    eventType: BACnetEventEnumType
    polarity: BACnetPolarity
    programChange: BACnetProgramRequest
    programState: BACnetProgramStates
    programError: BACnetProgramError
    reliability: BACnetReliability
    state: BACnetEventState
    systemStatus: BACnetDeviceStatus
    units: ns0.datatypes.EUInformation
    unsignedValue: o6.UInt32
    lifeSafetyMode: BACnetLifeSafetyMode
    lifeSafetyState: BACnetLifeSafetyState


@o6.enumtype(nodeId="ns=bacnet;i=3044", browseName="BACnetLifeSafetyOperation")
class BACnetLifeSafetyOperation(ns0.datatypes.Enumeration):
    NONE = o6.enumfield(0, name="None")
    SILENCE = o6.enumfield(1, name="Silence")
    SILENCE_AUDIBLE = o6.enumfield(2, name="SilenceAudible")
    SILENCE_VISIBLE = o6.enumfield(3, name="SilenceVisible")
    RESET = o6.enumfield(4, name="Reset")
    RESET_ALARM = o6.enumfield(5, name="ResetAlarm")
    RESET_FAULT = o6.enumfield(6, name="ResetFault")
    UNSILENCE = o6.enumfield(7, name="Unsilence")
    UNSILENCE_AUDIBLE = o6.enumfield(8, name="UnsilenceAudible")
    UNSILENCE_VISIBLE = o6.enumfield(9, name="UnsilenceVisible")


@o6.datatype(nodeId="ns=bacnet;i=3027", browseName="BACnetEventParameterChangeOfLifeSafety", defaultEncodingId="ns=bacnet;i=5024")
class BACnetEventParameterChangeOfLifeSafety(ns0.datatypes.Structure):
    newState: BACnetLifeSafetyState
    newMode: BACnetLifeSafetyMode
    operationExtended: BACnetLifeSafetyOperation


@o6.enumtype(nodeId="ns=bacnet;i=3045", browseName="BACnetNodeType")
class BACnetNodeType(ns0.datatypes.Enumeration):
    UNKNOWN = o6.enumfield(0, name="UNKNOWN")
    SYSTEM = o6.enumfield(1, name="SYSTEM")
    NETWORK = o6.enumfield(2, name="NETWORK")
    DEVICE = o6.enumfield(3, name="DEVICE")
    ORGANIZATIONAL = o6.enumfield(4, name="ORGANIZATIONAL")
    AREA = o6.enumfield(5, name="AREA")
    EQUIPMENT = o6.enumfield(6, name="EQUIPMENT")
    POINT = o6.enumfield(7, name="POINT")
    COLLECTION = o6.enumfield(8, name="COLLECTION")
    PROPERTY = o6.enumfield(9, name="PROPERTY")
    FUNCTIONAL = o6.enumfield(10, name="FUNCTIONAL")
    OTHER = o6.enumfield(11, name="OTHER")


@o6.enumtype(nodeId="ns=bacnet;i=3046", browseName="BACnetPropertyIdentifier")
class BACnetPropertyIdentifier(ns0.datatypes.Enumeration):
    ACKED_TRANSITIONS = o6.enumfield(0, name="AckedTransitions")
    ACK_REQUIRED = o6.enumfield(1, name="AckRequired")
    ACTION = o6.enumfield(2, name="Action")
    ACTION_TEXT = o6.enumfield(3, name="ActionText")
    ACTIVE_TEXT = o6.enumfield(4, name="ActiveText")
    ACTIVE_VT_SESSIONS = o6.enumfield(5, name="ActiveVtSessions")
    ALARM_VALUE = o6.enumfield(6, name="AlarmValue")
    ALARM_VALUES = o6.enumfield(7, name="AlarmValues")
    ALL = o6.enumfield(8, name="All")
    ALL_WRITES_SUCCESSFUL = o6.enumfield(9, name="AllWritesSuccessful")
    APDU_SEGMENT_TIMEOUT = o6.enumfield(10, name="ApduSegmentTimeout")
    APDU_TIMEOUT = o6.enumfield(11, name="ApduTimeout")
    APPLICATION_SOFTWARE_VERSION = o6.enumfield(12, name="ApplicationSoftwareVersion")
    ARCHIVE = o6.enumfield(13, name="Archive")
    BIAS = o6.enumfield(14, name="Bias")
    CHANGE_OF_STATE_COUNT = o6.enumfield(15, name="ChangeOfStateCount")
    CHANGE_OF_STATE_TIME = o6.enumfield(16, name="ChangeOfStateTime")
    NOTIFICATION_CLASS = o6.enumfield(17, name="NotificationClass")
    THIS_PROPERTY_DELETED = o6.enumfield(18, name="this property deleted")
    CONTROLLED_VARIABLE_REFERENCE = o6.enumfield(19, name="ControlledVariableReference")
    CONTROLLED_VARIABLE_UNITS = o6.enumfield(20, name="ControlledVariableUnits")
    CONTROLLED_VARIABLE_VALUE = o6.enumfield(21, name="ControlledVariableValue")
    COV_INCREMENT = o6.enumfield(22, name="CovIncrement")
    DATE_LIST = o6.enumfield(23, name="DateList")
    DAYLIGHT_SAVINGS_STATUS = o6.enumfield(24, name="DaylightSavingsStatus")
    DEADBAND = o6.enumfield(25, name="Deadband")
    DERIVATIVE_CONSTANT = o6.enumfield(26, name="DerivativeConstant")
    DERIVATIVE_CONSTANT_UNITS = o6.enumfield(27, name="DerivativeConstantUnits")
    DESCRIPTION = o6.enumfield(28, name="Description")
    DESCRIPTION_OF_HALT = o6.enumfield(29, name="DescriptionOfHalt")
    DEVICE_ADDRESS_BINDING = o6.enumfield(30, name="DeviceAddressBinding")
    DEVICE_TYPE = o6.enumfield(31, name="DeviceType")
    EFFECTIVE_PERIOD = o6.enumfield(32, name="EffectivePeriod")
    ELAPSED_ACTIVE_TIME = o6.enumfield(33, name="ElapsedActiveTime")
    ERROR_LIMIT = o6.enumfield(34, name="ErrorLimit")
    EVENT_ENABLE = o6.enumfield(35, name="EventEnable")
    EVENT_STATE = o6.enumfield(36, name="EventState")
    EVENT_TYPE = o6.enumfield(37, name="EventType")
    EXCEPTION_SCHEDULE = o6.enumfield(38, name="ExceptionSchedule")
    FAULT_VALUES = o6.enumfield(39, name="FaultValues")
    FEEDBACK_VALUE = o6.enumfield(40, name="FeedbackValue")
    FILE_ACCESS_METHOD = o6.enumfield(41, name="FileAccessMethod")
    FILE_SIZE = o6.enumfield(42, name="FileSize")
    FILE_TYPE = o6.enumfield(43, name="FileType")
    FIRMWARE_REVISION = o6.enumfield(44, name="FirmwareRevision")
    HIGH_LIMIT = o6.enumfield(45, name="HighLimit")
    INACTIVE_TEXT = o6.enumfield(46, name="InactiveText")
    IN_PROCESS = o6.enumfield(47, name="InProcess")
    INSTANCE_OF = o6.enumfield(48, name="InstanceOf")
    INTEGRAL_CONSTANT = o6.enumfield(49, name="IntegralConstant")
    INTEGRAL_CONSTANT_UNITS = o6.enumfield(50, name="IntegralConstantUnits")
    REMOVED__IN__VERSION_1__REVISION_4_51 = o6.enumfield(51, name="Removed In Version 1 Revision 4_51")
    LIMIT_ENABLE = o6.enumfield(52, name="LimitEnable")
    LIST_OF_GROUP_MEMBERS = o6.enumfield(53, name="ListOfGroupMembers")
    LIST_OF_OBJECT_PROPERTY_REFERENCES = o6.enumfield(54, name="ListOfObjectPropertyReferences")
    UNASSIGNED_55 = o6.enumfield(55, name="Unassigned_55")
    LOCAL_DATE = o6.enumfield(56, name="LocalDate")
    LOCAL_TIME = o6.enumfield(57, name="LocalTime")
    LOCATION = o6.enumfield(58, name="Location")
    LOW_LIMIT = o6.enumfield(59, name="LowLimit")
    MANIPULATED_VARIABLE_REFERENCE = o6.enumfield(60, name="ManipulatedVariableReference")
    MAXIMUM_OUTPUT = o6.enumfield(61, name="MaximumOutput")
    MAX_APDU_LENGTH_ACCEPTED = o6.enumfield(62, name="MaxApduLengthAccepted")
    MAX_INFO_FRAMES = o6.enumfield(63, name="MaxInfoFrames")
    MAX_MASTER = o6.enumfield(64, name="MaxMaster")
    MAX_PRES_VALUE = o6.enumfield(65, name="MaxPresValue")
    MINIMUM_OFF_TIME = o6.enumfield(66, name="MinimumOffTime")
    MINIMUM_ON_TIME = o6.enumfield(67, name="MinimumOnTime")
    MINIMUM_OUTPUT = o6.enumfield(68, name="MinimumOutput")
    MIN_PRES_VALUE = o6.enumfield(69, name="MinPresValue")
    MODEL_NAME = o6.enumfield(70, name="ModelName")
    MODIFICATION_DATE = o6.enumfield(71, name="ModificationDate")
    NOTIFY_TYPE = o6.enumfield(72, name="NotifyType")
    NUMBER_OF_APDU_RETRIES = o6.enumfield(73, name="NumberOfApduRetries")
    NUMBER_OF_STATES = o6.enumfield(74, name="NumberOfStates")
    OBJECT_IDENTIFIER = o6.enumfield(75, name="ObjectIdentifier")
    OBJECT_LIST = o6.enumfield(76, name="ObjectList")
    OBJECT_NAME = o6.enumfield(77, name="ObjectName")
    OBJECT_PROPERTY_REFERENCE = o6.enumfield(78, name="ObjectPropertyReference")
    OBJECT_TYPE = o6.enumfield(79, name="ObjectType")
    OPTIONAL = o6.enumfield(80, name="Optional")
    OUT_OF_SERVICE = o6.enumfield(81, name="OutOfService")
    OUTPUT_UNITS = o6.enumfield(82, name="OutputUnits")
    EVENT_PARAMETERS = o6.enumfield(83, name="EventParameters")
    POLARITY = o6.enumfield(84, name="Polarity")
    PRESENT_VALUE = o6.enumfield(85, name="PresentValue")
    PRIORITY = o6.enumfield(86, name="Priority")
    PRIORITY_ARRAY = o6.enumfield(87, name="PriorityArray")
    PRIORITY_FOR_WRITING = o6.enumfield(88, name="PriorityForWriting")
    PROCESS_IDENTIFIER = o6.enumfield(89, name="ProcessIdentifier")
    PROGRAM_CHANGE = o6.enumfield(90, name="ProgramChange")
    PROGRAM_LOCATION = o6.enumfield(91, name="ProgramLocation")
    PROGRAM_STATE = o6.enumfield(92, name="ProgramState")
    PROPORTIONAL_CONSTANT = o6.enumfield(93, name="ProportionalConstant")
    PROPORTIONAL_CONSTANT_UNITS = o6.enumfield(94, name="ProportionalConstantUnits")
    REMOVED__IN__VERSION_1__REVISION_2_95 = o6.enumfield(95, name="Removed In Version 1 Revision 2_95")
    PROTOCOL_OBJECT_TYPES_SUPPORTED = o6.enumfield(96, name="ProtocolObjectTypesSupported")
    PROTOCOL_SERVICES_SUPPORTED = o6.enumfield(97, name="ProtocolServicesSupported")
    PROTOCOL_VERSION = o6.enumfield(98, name="ProtocolVersion")
    READ_ONLY = o6.enumfield(99, name="ReadOnly")
    REASON_FOR_HALT = o6.enumfield(100, name="ReasonForHalt")
    REMOVED__IN__VERSION_1__REVISION_4_101 = o6.enumfield(101, name="Removed In Version 1 Revision 4_101")
    RECIPIENT_LIST = o6.enumfield(102, name="RecipientList")
    RELIABILITY = o6.enumfield(103, name="Reliability")
    RELINQUISH_DEFAULT = o6.enumfield(104, name="RelinquishDefault")
    REQUIRED = o6.enumfield(105, name="Required")
    RESOLUTION = o6.enumfield(106, name="Resolution")
    SEGMENTATION_SUPPORTED = o6.enumfield(107, name="SegmentationSupported")
    SETPOINT = o6.enumfield(108, name="Setpoint")
    SETPOINT_REFERENCE = o6.enumfield(109, name="SetpointReference")
    STATE_TEXT = o6.enumfield(110, name="StateText")
    STATUS_FLAGS = o6.enumfield(111, name="StatusFlags")
    SYSTEM_STATUS = o6.enumfield(112, name="SystemStatus")
    TIME_DELAY = o6.enumfield(113, name="TimeDelay")
    TIME_OF_ACTIVE_TIME_RESET = o6.enumfield(114, name="TimeOfActiveTimeReset")
    TIME_OF_STATE_COUNT_RESET = o6.enumfield(115, name="TimeOfStateCountReset")
    TIME_SYNCHRONIZATION_RECIPIENTS = o6.enumfield(116, name="TimeSynchronizationRecipients")
    UNITS = o6.enumfield(117, name="Units")
    UPDATE_INTERVAL = o6.enumfield(118, name="UpdateInterval")
    UTC_OFFSET = o6.enumfield(119, name="UtcOffset")
    VENDOR_IDENTIFIER = o6.enumfield(120, name="VendorIdentifier")
    VENDOR_NAME = o6.enumfield(121, name="VendorName")
    VT_CLASSES_SUPPORTED = o6.enumfield(122, name="VtClassesSupported")
    WEEKLY_SCHEDULE = o6.enumfield(123, name="WeeklySchedule")
    ATTEMPTED_SAMPLES = o6.enumfield(124, name="AttemptedSamples")
    AVERAGE_VALUE = o6.enumfield(125, name="AverageValue")
    BUFFER_SIZE = o6.enumfield(126, name="BufferSize")
    CLIENT_COV_INCREMENT = o6.enumfield(127, name="ClientCovIncrement")
    COV_RESUBSCRIPTION_INTERVAL = o6.enumfield(128, name="CovResubscriptionInterval")
    REMOVED__IN__VERSION_1__REVISION_3_129 = o6.enumfield(129, name="Removed In Version 1 Revision 3_129")
    EVENT_TIME_STAMPS = o6.enumfield(130, name="EventTimeStamps")
    LOG_BUFFER = o6.enumfield(131, name="LogBuffer")
    LOG_DEVICE_OBJECT_PROPERTY = o6.enumfield(132, name="LogDeviceObjectProperty")
    ENABLE = o6.enumfield(133, name="Enable")
    LOG_INTERVAL = o6.enumfield(134, name="LogInterval")
    MAXIMUM_VALUE = o6.enumfield(135, name="MaximumValue")
    MINIMUM_VALUE = o6.enumfield(136, name="MinimumValue")
    NOTIFICATION_THRESHOLD = o6.enumfield(137, name="NotificationThreshold")
    REMOVED__IN__VERSION_1__REVISION_3_138 = o6.enumfield(138, name="Removed In Version 1 Revision 3_138")
    PROTOCOL_REVISION = o6.enumfield(139, name="ProtocolRevision")
    RECORDS_SINCE_NOTIFICATION = o6.enumfield(140, name="RecordsSinceNotification")
    RECORD_COUNT = o6.enumfield(141, name="RecordCount")
    START_TIME = o6.enumfield(142, name="StartTime")
    STOP_TIME = o6.enumfield(143, name="StopTime")
    STOP_WHEN_FULL = o6.enumfield(144, name="StopWhenFull")
    TOTAL_RECORD_COUNT = o6.enumfield(145, name="TotalRecordCount")
    VALID_SAMPLES = o6.enumfield(146, name="ValidSamples")
    WINDOW_INTERVAL = o6.enumfield(147, name="WindowInterval")
    WINDOW_SAMPLES = o6.enumfield(148, name="WindowSamples")
    MAXIMUM_VALUE_TIMESTAMP = o6.enumfield(149, name="MaximumValueTimestamp")
    MINIMUM_VALUE_TIMESTAMP = o6.enumfield(150, name="MinimumValueTimestamp")
    VARIANCE_VALUE = o6.enumfield(151, name="VarianceValue")
    ACTIVE_COV_SUBSCRIPTIONS = o6.enumfield(152, name="ActiveCovSubscriptions")
    BACKUP_FAILURE_TIMEOUT = o6.enumfield(153, name="BackupFailureTimeout")
    CONFIGURATION_FILES = o6.enumfield(154, name="ConfigurationFiles")
    DATABASE_REVISION = o6.enumfield(155, name="DatabaseRevision")
    DIRECT_READING = o6.enumfield(156, name="DirectReading")
    LAST_RESTORE_TIME = o6.enumfield(157, name="LastRestoreTime")
    MAINTENANCE_REQUIRED = o6.enumfield(158, name="MaintenanceRequired")
    MEMBER_OF = o6.enumfield(159, name="MemberOf")
    MODE = o6.enumfield(160, name="Mode")
    OPERATION_EXPECTED = o6.enumfield(161, name="OperationExpected")
    SETTING = o6.enumfield(162, name="Setting")
    SILENCED = o6.enumfield(163, name="Silenced")
    TRACKING_VALUE = o6.enumfield(164, name="TrackingValue")
    ZONE_MEMBERS = o6.enumfield(165, name="ZoneMembers")
    LIFE_SAFETY_ALARM_VALUES = o6.enumfield(166, name="LifeSafetyAlarmValues")
    MAX_SEGMENTS_ACCEPTED = o6.enumfield(167, name="MaxSegmentsAccepted")
    PROFILE_NAME = o6.enumfield(168, name="ProfileName")
    AUTO_SLAVE_DISCOVERY = o6.enumfield(169, name="AutoSlaveDiscovery")
    MANUAL_SLAVE_ADDRESS_BINDING = o6.enumfield(170, name="ManualSlaveAddressBinding")
    SLAVE_ADDRESS_BINDING = o6.enumfield(171, name="SlaveAddressBinding")
    SLAVE_PROXY_ENABLE = o6.enumfield(172, name="SlaveProxyEnable")
    LAST_NOTIFY_RECORD = o6.enumfield(173, name="LastNotifyRecord")
    SCHEDULE_DEFAULT = o6.enumfield(174, name="ScheduleDefault")
    ACCEPTED_MODES = o6.enumfield(175, name="AcceptedModes")
    ADJUST_VALUE = o6.enumfield(176, name="AdjustValue")
    COUNT = o6.enumfield(177, name="Count")
    COUNT_BEFORE_CHANGE = o6.enumfield(178, name="CountBeforeChange")
    COUNT_CHANGE_TIME = o6.enumfield(179, name="CountChangeTime")
    COV_PERIOD = o6.enumfield(180, name="CovPeriod")
    INPUT_REFERENCE = o6.enumfield(181, name="InputReference")
    LIMIT_MONITORING_INTERVAL = o6.enumfield(182, name="LimitMonitoringInterval")
    LOGGING_OBJECT = o6.enumfield(183, name="LoggingObject")
    LOGGING_RECORD = o6.enumfield(184, name="LoggingRecord")
    PRESCALE = o6.enumfield(185, name="Prescale")
    PULSE_RATE = o6.enumfield(186, name="PulseRate")
    SCALE = o6.enumfield(187, name="Scale")
    SCALE_FACTOR = o6.enumfield(188, name="ScaleFactor")
    UPDATE_TIME = o6.enumfield(189, name="UpdateTime")
    VALUE_BEFORE_CHANGE = o6.enumfield(190, name="ValueBeforeChange")
    VALUE_SET = o6.enumfield(191, name="ValueSet")
    VALUE_CHANGE_TIME = o6.enumfield(192, name="ValueChangeTime")
    ALIGN_INTERVALS = o6.enumfield(193, name="AlignIntervals")
    UNASSIGNED_194 = o6.enumfield(194, name="Unassigned_194")
    INTERVAL_OFFSET = o6.enumfield(195, name="IntervalOffset")
    LAST_RESTART_REASON = o6.enumfield(196, name="LastRestartReason")
    LOGGING_TYPE = o6.enumfield(197, name="LoggingType")
    UNASSIGNED_198 = o6.enumfield(198, name="Unassigned_198")
    UNASSIGNED_199 = o6.enumfield(199, name="Unassigned_199")
    UNASSIGNED_200 = o6.enumfield(200, name="Unassigned_200")
    UNASSIGNED_201 = o6.enumfield(201, name="Unassigned_201")
    RESTART_NOTIFICATION_RECIPIENTS = o6.enumfield(202, name="RestartNotificationRecipients")
    TIME_OF_DEVICE_RESTART = o6.enumfield(203, name="TimeOfDeviceRestart")
    TIME_SYNCHRONIZATION_INTERVAL = o6.enumfield(204, name="TimeSynchronizationInterval")
    TRIGGER = o6.enumfield(205, name="Trigger")
    UTC_TIME_SYNCHRONIZATION_RECIPIENTS = o6.enumfield(206, name="UtcTimeSynchronizationRecipients")
    NODE_SUBTYPE = o6.enumfield(207, name="NodeSubtype")
    NODE_TYPE = o6.enumfield(208, name="NodeType")
    STRUCTURED_OBJECT_LIST = o6.enumfield(209, name="StructuredObjectList")
    SUBORDINATE_ANNOTATIONS = o6.enumfield(210, name="SubordinateAnnotations")
    SUBORDINATE_LIST = o6.enumfield(211, name="SubordinateList")
    ACTUAL_SHED_LEVEL = o6.enumfield(212, name="ActualShedLevel")
    DUTY_WINDOW = o6.enumfield(213, name="DutyWindow")
    EXPECTED_SHED_LEVEL = o6.enumfield(214, name="ExpectedShedLevel")
    FULL_DUTY_BASELINE = o6.enumfield(215, name="FullDutyBaseline")
    UNASSIGNED_216 = o6.enumfield(216, name="Unassigned_216")
    UNASSIGNED_217 = o6.enumfield(217, name="Unassigned_217")
    REQUESTED_SHED_LEVEL = o6.enumfield(218, name="RequestedShedLevel")
    SHED_DURATION = o6.enumfield(219, name="ShedDuration")
    SHED_LEVEL_DESCRIPTIONS = o6.enumfield(220, name="ShedLevelDescriptions")
    SHED_LEVELS = o6.enumfield(221, name="ShedLevels")
    STATE_DESCRIPTION = o6.enumfield(222, name="StateDescription")
    UNASSIGNED_223 = o6.enumfield(223, name="Unassigned_223")
    UNASSIGNED_224 = o6.enumfield(224, name="Unassigned_224")
    UNASSIGNED_225 = o6.enumfield(225, name="Unassigned_225")
    DOOR_ALARM_STATE = o6.enumfield(226, name="DoorAlarmState")
    DOOR_EXTENDED_PULSE_TIME = o6.enumfield(227, name="DoorExtendedPulseTime")
    DOOR_MEMBERS = o6.enumfield(228, name="DoorMembers")
    DOOR_OPEN_TOO_LONG_TIME = o6.enumfield(229, name="DoorOpenTooLongTime")
    DOOR_PULSE_TIME = o6.enumfield(230, name="DoorPulseTime")
    DOOR_STATUS = o6.enumfield(231, name="DoorStatus")
    DOOR_UNLOCK_DELAY_TIME = o6.enumfield(232, name="DoorUnlockDelayTime")
    LOCK_STATUS = o6.enumfield(233, name="LockStatus")
    MASKED_ALARM_VALUES = o6.enumfield(234, name="MaskedAlarmValues")
    SECURED_STATUS = o6.enumfield(235, name="SecuredStatus")
    UNASSIGNED_236 = o6.enumfield(236, name="Unassigned_236")
    UNASSIGNED_237 = o6.enumfield(237, name="Unassigned_237")
    UNASSIGNED_238 = o6.enumfield(238, name="Unassigned_238")
    UNASSIGNED_239 = o6.enumfield(239, name="Unassigned_239")
    UNASSIGNED_240 = o6.enumfield(240, name="Unassigned_240")
    UNASSIGNED_241 = o6.enumfield(241, name="Unassigned_241")
    UNASSIGNED_242 = o6.enumfield(242, name="Unassigned_242")
    UNASSIGNED_243 = o6.enumfield(243, name="Unassigned_243")
    ABSENTEE_LIMIT = o6.enumfield(244, name="AbsenteeLimit")
    ACCESS_ALARM_EVENTS = o6.enumfield(245, name="AccessAlarmEvents")
    ACCESS_DOORS = o6.enumfield(246, name="AccessDoors")
    ACCESS_EVENT = o6.enumfield(247, name="AccessEvent")
    ACCESS_EVENT_AUTHENTICATION_FACTOR = o6.enumfield(248, name="AccessEventAuthenticationFactor")
    ACCESS_EVENT_CREDENTIAL = o6.enumfield(249, name="AccessEventCredential")
    ACCESS_EVENT_TIME = o6.enumfield(250, name="AccessEventTime")
    ACCESS_TRANSACTION_EVENTS = o6.enumfield(251, name="AccessTransactionEvents")
    ACCOMPANIMENT = o6.enumfield(252, name="Accompaniment")
    ACCOMPANIMENT_TIME = o6.enumfield(253, name="AccompanimentTime")
    ACTIVATION_TIME = o6.enumfield(254, name="ActivationTime")
    ACTIVE_AUTHENTICATION_POLICY = o6.enumfield(255, name="ActiveAuthenticationPolicy")
    ASSIGNED_ACCESS_RIGHTS = o6.enumfield(256, name="AssignedAccessRights")
    AUTHENTICATION_FACTORS = o6.enumfield(257, name="AuthenticationFactors")
    AUTHENTICATION_POLICY_LIST = o6.enumfield(258, name="AuthenticationPolicyList")
    AUTHENTICATION_POLICY_NAMES = o6.enumfield(259, name="AuthenticationPolicyNames")
    AUTHENTICATION_STATUS = o6.enumfield(260, name="AuthenticationStatus")
    AUTHORIZATION_MODE = o6.enumfield(261, name="AuthorizationMode")
    BELONGS_TO = o6.enumfield(262, name="BelongsTo")
    CREDENTIAL_DISABLE = o6.enumfield(263, name="CredentialDisable")
    CREDENTIAL_STATUS = o6.enumfield(264, name="CredentialStatus")
    CREDENTIALS = o6.enumfield(265, name="Credentials")
    CREDENTIALS_IN_ZONE = o6.enumfield(266, name="CredentialsInZone")
    DAYS_REMAINING = o6.enumfield(267, name="DaysRemaining")
    ENTRY_POINTS = o6.enumfield(268, name="EntryPoints")
    EXIT_POINTS = o6.enumfield(269, name="ExitPoints")
    EXPIRY_TIME = o6.enumfield(270, name="ExpiryTime")
    EXTENDED_TIME_ENABLE = o6.enumfield(271, name="ExtendedTimeEnable")
    FAILED_ATTEMPT_EVENTS = o6.enumfield(272, name="FailedAttemptEvents")
    FAILED_ATTEMPTS = o6.enumfield(273, name="FailedAttempts")
    FAILED_ATTEMPTS_TIME = o6.enumfield(274, name="FailedAttemptsTime")
    LAST_ACCESS_EVENT = o6.enumfield(275, name="LastAccessEvent")
    LAST_ACCESS_POINT = o6.enumfield(276, name="LastAccessPoint")
    LAST_CREDENTIAL_ADDED = o6.enumfield(277, name="LastCredentialAdded")
    LAST_CREDENTIAL_ADDED_TIME = o6.enumfield(278, name="LastCredentialAddedTime")
    LAST_CREDENTIAL_REMOVED = o6.enumfield(279, name="LastCredentialRemoved")
    LAST_CREDENTIAL_REMOVED_TIME = o6.enumfield(280, name="LastCredentialRemovedTime")
    LAST_USE_TIME = o6.enumfield(281, name="LastUseTime")
    LOCKOUT = o6.enumfield(282, name="Lockout")
    LOCKOUT_RELINQUISH_TIME = o6.enumfield(283, name="LockoutRelinquishTime")
    REMOVED__IN__VERSION_1__REVISION_13_284 = o6.enumfield(284, name="Removed In Version 1 Revision 13_284")
    MAX_FAILED_ATTEMPTS = o6.enumfield(285, name="MaxFailedAttempts")
    MEMBERS = o6.enumfield(286, name="Members")
    MUSTER_POINT = o6.enumfield(287, name="MusterPoint")
    NEGATIVE_ACCESS_RULES = o6.enumfield(288, name="NegativeAccessRules")
    NUMBER_OF_AUTHENTICATION_POLICIES = o6.enumfield(289, name="NumberOfAuthenticationPolicies")
    OCCUPANCY_COUNT = o6.enumfield(290, name="OccupancyCount")
    OCCUPANCY_COUNT_ADJUST = o6.enumfield(291, name="OccupancyCountAdjust")
    OCCUPANCY_COUNT_ENABLE = o6.enumfield(292, name="OccupancyCountEnable")
    REMOVED__IN__VERSION_1__REVISION_13_293 = o6.enumfield(293, name="Removed In Version 1 Revision 13_293")
    OCCUPANCY_LOWER_LIMIT = o6.enumfield(294, name="OccupancyLowerLimit")
    OCCUPANCY_LOWER_LIMIT_ENFORCED = o6.enumfield(295, name="OccupancyLowerLimitEnforced")
    OCCUPANCY_STATE = o6.enumfield(296, name="OccupancyState")
    OCCUPANCY_UPPER_LIMIT = o6.enumfield(297, name="OccupancyUpperLimit")
    OCCUPANCY_UPPER_LIMIT_ENFORCED = o6.enumfield(298, name="OccupancyUpperLimitEnforced")
    REMOVED__IN__VERSION_1__REVISION_13_299 = o6.enumfield(299, name="Removed In Version 1 Revision 13_299")
    PASSBACK_MODE = o6.enumfield(300, name="PassbackMode")
    PASSBACK_TIMEOUT = o6.enumfield(301, name="PassbackTimeout")
    POSITIVE_ACCESS_RULES = o6.enumfield(302, name="PositiveAccessRules")
    REASON_FOR_DISABLE = o6.enumfield(303, name="ReasonForDisable")
    SUPPORTED_FORMATS = o6.enumfield(304, name="SupportedFormats")
    SUPPORTED_FORMAT_CLASSES = o6.enumfield(305, name="SupportedFormatClasses")
    THREAT_AUTHORITY = o6.enumfield(306, name="ThreatAuthority")
    THREAT_LEVEL = o6.enumfield(307, name="ThreatLevel")
    TRACE_FLAG = o6.enumfield(308, name="TraceFlag")
    TRANSACTION_NOTIFICATION_CLASS = o6.enumfield(309, name="TransactionNotificationClass")
    USER_EXTERNAL_IDENTIFIER = o6.enumfield(310, name="UserExternalIdentifier")
    USER_INFORMATION_REFERENCE = o6.enumfield(311, name="UserInformationReference")
    UNASSIGNED_312 = o6.enumfield(312, name="Unassigned_312")
    UNASSIGNED_313 = o6.enumfield(313, name="Unassigned_313")
    UNASSIGNED_314 = o6.enumfield(314, name="Unassigned_314")
    UNASSIGNED_315 = o6.enumfield(315, name="Unassigned_315")
    UNASSIGNED_316 = o6.enumfield(316, name="Unassigned_316")
    USER_NAME = o6.enumfield(317, name="UserName")
    USER_TYPE = o6.enumfield(318, name="UserType")
    USES_REMAINING = o6.enumfield(319, name="UsesRemaining")
    ZONE_FROM = o6.enumfield(320, name="ZoneFrom")
    ZONE_TO = o6.enumfield(321, name="ZoneTo")
    ACCESS_EVENT_TAG = o6.enumfield(322, name="AccessEventTag")
    GLOBAL_IDENTIFIER = o6.enumfield(323, name="GlobalIdentifier")
    UNASSIGNED_324 = o6.enumfield(324, name="Unassigned_324")
    UNASSIGNED_325 = o6.enumfield(325, name="Unassigned_325")
    VERIFICATION_TIME = o6.enumfield(326, name="VerificationTime")
    BASE_DEVICE_SECURITY_POLICY = o6.enumfield(327, name="BaseDeviceSecurityPolicy")
    DISTRIBUTION_KEY_REVISION = o6.enumfield(328, name="DistributionKeyRevision")
    DO_NOT_HIDE = o6.enumfield(329, name="DoNotHide")
    KEY_SETS = o6.enumfield(330, name="KeySets")
    LAST_KEY_SERVER = o6.enumfield(331, name="LastKeyServer")
    NETWORK_ACCESS_SECURITY_POLICIES = o6.enumfield(332, name="NetworkAccessSecurityPolicies")
    PACKET_REORDER_TIME = o6.enumfield(333, name="PacketReorderTime")
    SECURITY_PDU_TIMEOUT = o6.enumfield(334, name="SecurityPduTimeout")
    SECURITY_TIME_WINDOW = o6.enumfield(335, name="SecurityTimeWindow")
    SUPPORTED_SECURITY_ALGORITHMS = o6.enumfield(336, name="SupportedSecurityAlgorithms")
    UPDATE_KEY_SET_TIMEOUT = o6.enumfield(337, name="UpdateKeySetTimeout")
    BACKUP_AND_RESTORE_STATE = o6.enumfield(338, name="BackupAndRestoreState")
    BACKUP_PREPARATION_TIME = o6.enumfield(339, name="BackupPreparationTime")
    RESTORE_COMPLETION_TIME = o6.enumfield(340, name="RestoreCompletionTime")
    RESTORE_PREPARATION_TIME = o6.enumfield(341, name="RestorePreparationTime")
    BIT_MASK = o6.enumfield(342, name="BitMask")
    BIT_TEXT = o6.enumfield(343, name="BitText")
    IS_UTC = o6.enumfield(344, name="IsUtc")
    GROUP_MEMBERS = o6.enumfield(345, name="GroupMembers")
    GROUP_MEMBER_NAMES = o6.enumfield(346, name="GroupMemberNames")
    MEMBER_STATUS_FLAGS = o6.enumfield(347, name="MemberStatusFlags")
    REQUESTED_UPDATE_INTERVAL = o6.enumfield(348, name="RequestedUpdateInterval")
    COVU_PERIOD = o6.enumfield(349, name="CovuPeriod")
    COVU_RECIPIENTS = o6.enumfield(350, name="CovuRecipients")
    EVENT_MESSAGE_TEXTS = o6.enumfield(351, name="EventMessageTexts")
    EVENT_MESSAGE_TEXTS_CONFIG = o6.enumfield(352, name="EventMessageTextsConfig")
    EVENT_DETECTION_ENABLE = o6.enumfield(353, name="EventDetectionEnable")
    EVENT_ALGORITHM_INHIBIT = o6.enumfield(354, name="EventAlgorithmInhibit")
    EVENT_ALGORITHM_INHIBIT_REF = o6.enumfield(355, name="EventAlgorithmInhibitRef")
    TIME_DELAY_NORMAL = o6.enumfield(356, name="TimeDelayNormal")
    RELIABILITY_EVALUATION_INHIBIT = o6.enumfield(357, name="ReliabilityEvaluationInhibit")
    FAULT_PARAMETERS = o6.enumfield(358, name="FaultParameters")
    FAULT_TYPE = o6.enumfield(359, name="FaultType")
    LOCAL_FORWARDING_ONLY = o6.enumfield(360, name="LocalForwardingOnly")
    PROCESS_IDENTIFIER_FILTER = o6.enumfield(361, name="ProcessIdentifierFilter")
    SUBSCRIBED_RECIPIENTS = o6.enumfield(362, name="SubscribedRecipients")
    PORT_FILTER = o6.enumfield(363, name="PortFilter")
    AUTHORIZATION_EXEMPTIONS = o6.enumfield(364, name="AuthorizationExemptions")
    ALLOW_GROUP_DELAY_INHIBIT = o6.enumfield(365, name="AllowGroupDelayInhibit")
    CHANNEL_NUMBER = o6.enumfield(366, name="ChannelNumber")
    CONTROL_GROUPS = o6.enumfield(367, name="ControlGroups")
    EXECUTION_DELAY = o6.enumfield(368, name="ExecutionDelay")
    LAST_PRIORITY = o6.enumfield(369, name="LastPriority")
    WRITE_STATUS = o6.enumfield(370, name="WriteStatus")
    PROPERTY_LIST = o6.enumfield(371, name="PropertyList")
    SERIAL_NUMBER = o6.enumfield(372, name="SerialNumber")
    BLINK_WARN_ENABLE = o6.enumfield(373, name="BlinkWarnEnable")
    DEFAULT_FADE_TIME = o6.enumfield(374, name="DefaultFadeTime")
    DEFAULT_RAMP_RATE = o6.enumfield(375, name="DefaultRampRate")
    DEFAULT_STEP_INCREMENT = o6.enumfield(376, name="DefaultStepIncrement")
    EGRESS_TIME = o6.enumfield(377, name="EgressTime")
    IN_PROGRESS = o6.enumfield(378, name="InProgress")
    INSTANTANEOUS_POWER = o6.enumfield(379, name="InstantaneousPower")
    LIGHTING_COMMAND = o6.enumfield(380, name="LightingCommand")
    LIGHTING_COMMAND_DEFAULT_PRIORITY = o6.enumfield(381, name="LightingCommandDefaultPriority")
    MAX_ACTUAL_VALUE = o6.enumfield(382, name="MaxActualValue")
    MIN_ACTUAL_VALUE = o6.enumfield(383, name="MinActualValue")
    POWER = o6.enumfield(384, name="Power")
    TRANSITION = o6.enumfield(385, name="Transition")
    EGRESS_ACTIVE = o6.enumfield(386, name="EgressActive")


@o6.enumtype(nodeId="ns=bacnet;i=3049", browseName="BACnetReinitializedStateofDevice")
class BACnetReinitializedStateofDevice(ns0.datatypes.Enumeration):
    COLDSTART = o6.enumfield(0, name="Coldstart")
    WARMSTART = o6.enumfield(1, name="Warmstart")
    STARTBACKUP = o6.enumfield(2, name="Startbackup")
    ENDBACKUP = o6.enumfield(3, name="Endbackup")
    STARTRESTORE = o6.enumfield(4, name="Startrestore")
    ENDRESTORE = o6.enumfield(5, name="Endrestore")
    ABORTRESTORE = o6.enumfield(6, name="Abortrestore")


@o6.datatype(nodeId="ns=bacnet;i=3052", browseName="BACnetMessageClass", defaultEncodingId="ns=bacnet;i=5028")
class BACnetMessageClass(ns0.datatypes.Union):
    unsigned: o6.ExtensionObject
    string: o6.String


@o6.datatype(nodeId="ns=bacnet;i=3053", browseName="BACnetPriorityValue", defaultEncodingId="ns=bacnet;i=5030")
class BACnetPriorityValue(ns0.datatypes.Union):
    real: o6.Float
    enumerated: o6.Int32
    unsigned: o6.ExtensionObject
    boolean: o6.Boolean
    signed: o6.ExtensionObject
    double: o6.Double


@o6.datatype(nodeId="ns=bacnet;i=3054", browseName="BACnetRecipient", defaultEncodingId="ns=bacnet;i=5032")
class BACnetRecipient(ns0.datatypes.Union):
    device: o6.UInt32
    address: BACnetAddress


@o6.enumtype(nodeId="ns=bacnet;i=3057", browseName="BACnetMessagePriority")
class BACnetMessagePriority(ns0.datatypes.Enumeration):
    NORMAL = o6.enumfield(0, name="normal")
    URGENT = o6.enumfield(1, name="urgent")


@o6.datatype(nodeId="ns=bacnet;i=3058", browseName="BACnetEventParameterDoubleOutOfRange", defaultEncodingId="ns=bacnet;i=5010")
class BACnetEventParameterDoubleOutOfRange(ns0.datatypes.Structure):
    time_delay: o6.UInt32
    low_limit: o6.Double
    high_limit: o6.Double
    deadband: o6.Double


@o6.datatype(nodeId="ns=bacnet;i=3059", browseName="BACnetEventParameterSignedOutOfRange", defaultEncodingId="ns=bacnet;i=5064")
class BACnetEventParameterSignedOutOfRange(ns0.datatypes.Structure):
    time_delay: o6.UInt32
    low_limit: o6.Int32
    high_limit: o6.Int32
    deadband: o6.UInt32


@o6.datatype(nodeId="ns=bacnet;i=3060", browseName="BACnetDaysOfWeek", defaultEncodingId="ns=bacnet;i=5125")
class BACnetDaysOfWeek(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString


@o6.datatype(nodeId="ns=bacnet;i=3061", browseName="BACnetEventTransitionBits", defaultEncodingId="ns=bacnet;i=5129")
class BACnetEventTransitionBits(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString


@o6.datatype(nodeId="ns=bacnet;i=3062", browseName="BACnetLimitEnable", defaultEncodingId="ns=bacnet;i=5131")
class BACnetLimitEnable(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString


@o6.datatype(nodeId="ns=bacnet;i=3063", browseName="BACnetObjectTypeSupportedBits", defaultEncodingId="ns=bacnet;i=5133")
class BACnetObjectTypeSupportedBits(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString


@o6.datatype(nodeId="ns=bacnet;i=3064", browseName="BACnetServicesSupportedBits", defaultEncodingId="ns=bacnet;i=5135")
class BACnetServicesSupportedBits(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString


@o6.datatype(nodeId="ns=bacnet;i=3065", browseName="BACnetStatusFlags", defaultEncodingId="ns=bacnet;i=5146")
class BACnetStatusFlags(ns0.datatypes.OptionSet):
    value: o6.ByteString
    validBits: o6.ByteString


@o6.datatype(nodeId="ns=bacnet;i=3066", browseName="BACnetEventParameterChangeOfCharacterString", defaultEncodingId="ns=bacnet;i=5081")
class BACnetEventParameterChangeOfCharacterString(ns0.datatypes.Structure):
    time_delay: o6.UInt32
    alarmValues: list[o6.String] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=bacnet;i=3067", browseName="BACnetEventParameterUnsignedRange", defaultEncodingId="ns=bacnet;i=5083")
class BACnetEventParameterUnsignedRange(ns0.datatypes.Structure):
    time_delay: o6.UInt32
    low_limit: o6.UInt32
    high_limit: o6.UInt32


@o6.datatype(nodeId="ns=bacnet;i=103002", browseName="BACnetDeviceObjectPropertyReference", defaultEncodingId="ns=bacnet;i=105003")
class BACnetDeviceObjectPropertyReference(ns0.datatypes.Structure):
    objectIdentifier: o6.UInt32
    propertyIdentifier: BACnetPropertyIdentifier | None
    propertyArrayIndex: o6.UInt32 | None
    deviceIdentifier: o6.UInt32 | None


@o6.datatype(nodeId="ns=bacnet;i=103005", browseName="BACnetEventParameterChangeOfBitstring", defaultEncodingId="ns=bacnet;i=105009")
class BACnetEventParameterChangeOfBitstring(ns0.datatypes.Structure):
    time_delay: o6.UInt32
    bitmask: ns0.datatypes.OptionSet
    list_of_bitstring_values: list[ns0.datatypes.OptionSet] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=bacnet;i=103009", browseName="BACnetEventParameterChangeOfState", defaultEncodingId="ns=bacnet;i=105017")
class BACnetEventParameterChangeOfState(ns0.datatypes.Structure):
    time_delay: o6.UInt32
    list_of_values: list[BACnetPropertyStates] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=bacnet;i=103010", browseName="BACnetTimeValueValue", defaultEncodingId="ns=bacnet;i=105019")
class BACnetTimeValueValue(ns0.datatypes.Structure):
    booleanValue: o6.Boolean
    unsignedValue: o6.ExtensionObject
    signedValue: o6.ExtensionObject
    octedStringValue: o6.ByteString
    charStringValue: o6.String
    objectIdentifierValue: o6.UInt32
    enumerationValue: o6.Int32
    bitStringValue: ns0.datatypes.OptionSet


@o6.datatype(nodeId="ns=bacnet;i=103004", browseName="BACnetTimeValue", defaultEncodingId="ns=bacnet;i=105007")
class BACnetTimeValue(ns0.datatypes.Structure):
    time: BACnetTime
    value: BACnetTimeValueValue


@o6.datatype(nodeId="ns=bacnet;i=103001", browseName="BACnetDailySchedule", defaultEncodingId="ns=bacnet;i=105001")
class BACnetDailySchedule(ns0.datatypes.Structure):
    day_schedule: list[BACnetTimeValue] = o6.field(arrayDimensions=[0])


@o6.enumtype(nodeId="ns=bacnet;i=103011", browseName="BACnetSegmentation")
class BACnetSegmentation(ns0.datatypes.Enumeration):
    SEGMENTED_BOTH = o6.enumfield(0, name="segmented-both")
    SEGMENTED_TRANSMIT = o6.enumfield(1, name="segmented-transmit")
    SEGMENTED_RECEIVE = o6.enumfield(2, name="segmented-receive")
    NO_SEGMENTATION = o6.enumfield(3, name="no-segmentation")


@o6.datatype(nodeId="ns=bacnet;i=103015", browseName="BACnetAddressBinding", defaultEncodingId="ns=bacnet;i=105025")
class BACnetAddressBinding(ns0.datatypes.Structure):
    deviceObjectIdentifier: o6.UInt32
    deviceAddress: BACnetAddress


@o6.enumtype(nodeId="ns=bacnet;i=103016", browseName="BACnetBackupState")
class BACnetBackupState(ns0.datatypes.Enumeration):
    IDLE = o6.enumfield(0, name="Idle")
    PREPARING__FOR__BACKUP = o6.enumfield(1, name="Preparing_For_Backup")
    PREPARING__FOR__RESTORE = o6.enumfield(2, name="Preparing_For_Restore")
    PERFORMING_A__BACKUP = o6.enumfield(3, name="Performing_A_Backup")
    PERFORMING_A__RESTORE = o6.enumfield(4, name="Performing_A_Restore")
    BACKUP__FAILURE = o6.enumfield(5, name="Backup_Failure")
    RESTORE__FAILURE = o6.enumfield(6, name="Restore_Failure")


@o6.datatype(nodeId="ns=bacnet;i=103018", browseName="BACnetRecipientProcess", defaultEncodingId="ns=bacnet;i=105029")
class BACnetRecipientProcess(ns0.datatypes.Structure):
    recipient: BACnetRecipient
    processIdentifier: o6.UInt32


@o6.datatype(nodeId="ns=bacnet;i=103017", browseName="BACnetCOVSubscription", defaultEncodingId="ns=bacnet;i=105027")
class BACnetCOVSubscription(ns0.datatypes.Structure):
    recipient: BACnetRecipientProcess
    monitoredPropertyReference: BACnetDeviceObjectPropertyReference
    issueConfirmedNotifications: o6.Boolean
    timeRemaining: o6.UInt32
    covIncrement: o6.Float | None


@o6.enumtype(nodeId="ns=bacnet;i=103019", browseName="BACnetRestartReason")
class BACnetRestartReason(ns0.datatypes.Enumeration):
    UNKNOWN = o6.enumfield(0, name="unknown")
    COLDSTART = o6.enumfield(1, name="coldstart")
    WARMSTART = o6.enumfield(2, name="warmstart")
    DETECTED_POWER_LOST = o6.enumfield(3, name="detected_power_lost")
    DETECTED_POWERED_OFF = o6.enumfield(4, name="detected_powered_off")
    HARDWARE_WATCHDOG = o6.enumfield(5, name="hardware_watchdog")
    SOFTWARE_WATCHDOG = o6.enumfield(6, name="software_watchdog")
    SUSPENDED = o6.enumfield(7, name="suspended")


@o6.datatype(nodeId="ns=bacnet;i=103020", browseName="BACnetDestination", defaultEncodingId="ns=bacnet;i=105031")
class BACnetDestination(ns0.datatypes.Structure):
    validDays: BACnetDaysOfWeek
    fromTime: BACnetTime
    toTime: BACnetTime
    recipient: BACnetRecipient
    processIdentifier: o6.UInt32
    issueConfirmedNotifications: o6.Boolean
    transitions: BACnetEventTransitionBits


@o6.enumtype(nodeId="ns=bacnet;i=103028", browseName="BACnetFaultType")
class BACnetFaultType(ns0.datatypes.Enumeration):
    NONE = o6.enumfield(0, name="none")
    FAULT_CHARACTERSTRING = o6.enumfield(1, name="fault-characterstring")
    FAULT_EXENDED = o6.enumfield(2, name="fault-exended")
    FAULT_LIFE_SAFETY = o6.enumfield(3, name="fault-life-safety")
    FAULT_STATE = o6.enumfield(4, name="fault-state")
    FAULT_STATUS_FLAGS = o6.enumfield(5, name="fault-status-flags")


@o6.datatype(nodeId="ns=bacnet;i=103030", browseName="BACnetFaultParameterFaultCharacterstring", defaultEncodingId="ns=bacnet;i=105036")
class BACnetFaultParameterFaultCharacterstring(ns0.datatypes.Structure):
    fault_characterstring: o6.String


@o6.datatype(nodeId="ns=bacnet;i=103032", browseName="BACnetFaultParameterFaultLifeSafety", defaultEncodingId="ns=bacnet;i=105040")
class BACnetFaultParameterFaultLifeSafety(ns0.datatypes.Structure):
    list_of_fault_values: list[BACnetLifeSafetyState] = o6.field(arrayDimensions=[0])
    mode_property_reference: BACnetDeviceObjectPropertyReference


@o6.datatype(nodeId="ns=bacnet;i=103033", browseName="BACnetFaultParameterFaultState", defaultEncodingId="ns=bacnet;i=105042")
class BACnetFaultParameterFaultState(ns0.datatypes.Structure):
    list_of_fault_values: list[BACnetProgramStates] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=bacnet;i=103034", browseName="BACnetFaultParameterFaultStatusFlags", defaultEncodingId="ns=bacnet;i=105044")
class BACnetFaultParameterFaultStatusFlags(ns0.datatypes.Structure):
    status_flags_reference: list[BACnetDeviceObjectPropertyReference] = o6.field(arrayDimensions=[0])


@o6.enumtype(nodeId="ns=bacnet;i=103036", browseName="BACnetDayOfWeek")
class BACnetDayOfWeek(ns0.datatypes.Enumeration):
    MONDAY = o6.enumfield(1, name="Monday")
    TUESDAY = o6.enumfield(2, name="Tuesday")
    WEDNESDAY = o6.enumfield(3, name="Wednesday")
    THURSDAY = o6.enumfield(4, name="Thursday")
    FRIDAY = o6.enumfield(5, name="Friday")
    SATURDAY = o6.enumfield(6, name="Saturday")
    SUNDAY = o6.enumfield(7, name="Sunday")
    UNSPECIFIED = o6.enumfield(255, name="unspecified")


@o6.datatype(nodeId="ns=bacnet;i=3017", browseName="BACnetDate", defaultEncodingId="ns=bacnet;i=5019")
class BACnetDate(ns0.datatypes.Structure):
    year: o6.UInt16
    month: BACnetMonth
    dayOfMonth: BACnetDayOfMonth
    dayOfWeek: BACnetDayOfWeek


@o6.datatype(nodeId="ns=bacnet;i=3006", browseName="BACnetDateTime", defaultEncodingId="ns=bacnet;i=5005")
class BACnetDateTime(ns0.datatypes.Structure):
    date: BACnetDate
    time: BACnetTime


@o6.datatype(nodeId="ns=bacnet;i=3009", browseName="BACnetDateRange", defaultEncodingId="ns=bacnet;i=5017")
class BACnetDateRange(ns0.datatypes.Structure):
    startDate: BACnetDate
    endTime: BACnetDate


@o6.datatype(nodeId="ns=bacnet;i=3024", browseName="BACnetWeekNDay", defaultEncodingId="ns=bacnet;i=5013")
class BACnetWeekNDay(ns0.datatypes.Structure):
    month: BACnetMonth
    day: BACnetDay
    dayOfWeek: BACnetDayOfWeek


@o6.datatype(nodeId="ns=bacnet;i=3016", browseName="BACnetCalendarEntry", defaultEncodingId="ns=bacnet;i=5002")
class BACnetCalendarEntry(ns0.datatypes.Union):
    date: BACnetDate
    dateRange: BACnetDateRange
    weekNDay: BACnetWeekNDay


@o6.datatype(nodeId="ns=bacnet;i=3055", browseName="BACnetSpecialEventPeriod", defaultEncodingId="ns=bacnet;i=5034")
class BACnetSpecialEventPeriod(ns0.datatypes.Union):
    calendarEntry: BACnetCalendarEntry
    calendarReference: o6.UInt32


@o6.datatype(nodeId="ns=bacnet;i=3056", browseName="BACnetTimeStamp", defaultEncodingId="ns=bacnet;i=5069")
class BACnetTimeStamp(ns0.datatypes.Union):
    time: BACnetTime
    sequenceNumber: o6.UInt16
    dateTime: BACnetDateTime


@o6.datatype(nodeId="ns=bacnet;i=3068", browseName="BACnetEventParameterExtendedParameters", defaultEncodingId="ns=bacnet;i=5085")
class BACnetEventParameterExtendedParameters(ns0.datatypes.Union):
    real: o6.Double
    unsigned: o6.UInt32
    boolean: o6.Boolean
    double: o6.Double
    octed: list[o6.Byte] = o6.field(arrayDimensions=[0])
    characterString: o6.String
    bitString: ns0.datatypes.OptionSet
    enum: o6.UInt32
    date: BACnetDate
    time: BACnetTime
    objectIdentifier: o6.UInt32
    reference: BACnetDeviceObjectPropertyReference
    integer: o6.Int32


@o6.datatype(nodeId="ns=bacnet;i=103003", browseName="BACnetSpecialEvent", defaultEncodingId="ns=bacnet;i=105005")
class BACnetSpecialEvent(ns0.datatypes.Structure):
    period: BACnetSpecialEventPeriod
    listOfTimeValues: list[BACnetTimeValue] = o6.field(arrayDimensions=[0])
    eventPriority: o6.Byte


@o6.datatype(nodeId="ns=bacnet;i=103031", browseName="BACnetEventFaultParameterExtended", defaultEncodingId="ns=bacnet;i=105038")
class BACnetEventFaultParameterExtended(ns0.datatypes.Structure):
    vendorId: o6.UInt16
    extended_fault_type: o6.ExtensionObject
    parameters: list[BACnetEventParameterExtendedParameters] = o6.field(arrayDimensions=[0])


@o6.datatype(nodeId="ns=bacnet;i=3051", browseName="BACnetFaultParameter", defaultEncodingId="ns=bacnet;i=5023")
class BACnetFaultParameter(ns0.datatypes.Union):
    fault_characterstring: BACnetFaultParameterFaultCharacterstring
    fault_life_safety: BACnetFaultParameterFaultLifeSafety
    fault_state: BACnetFaultParameterFaultState
    fault_status_flags: BACnetFaultParameterFaultStatusFlags
    fault_extended: BACnetEventFaultParameterExtended


@o6.datatype(nodeId="ns=bacnet;i=103037", browseName="BACnetEventParameterChangeOfValue", defaultEncodingId="ns=bacnet;i=105048")
class BACnetEventParameterChangeOfValue(ns0.datatypes.Structure):
    time_delay: o6.UInt32
    cov_criteria_bitmask: ns0.datatypes.OptionSet
    cov_criteria_referenced_property_increment: o6.Float


@o6.datatype(nodeId="ns=bacnet;i=103039", browseName="BACnetEventParameterCommandFailure", defaultEncodingId="ns=bacnet;i=105052")
class BACnetEventParameterCommandFailure(ns0.datatypes.Structure):
    time_delay: o6.UInt32
    feedback_property_reference: BACnetDeviceObjectPropertyReference


@o6.datatype(nodeId="ns=bacnet;i=103040", browseName="BACnetEventParameterFloatingLimit", defaultEncodingId="ns=bacnet;i=105054")
class BACnetEventParameterFloatingLimit(ns0.datatypes.Structure):
    time_delay: o6.UInt32
    setpoint_reference: BACnetDeviceObjectPropertyReference
    low_diff_limit: o6.Double
    high_diff_limit: o6.Double
    deadband: o6.Double


@o6.datatype(nodeId="ns=bacnet;i=103041", browseName="BACnetEventParameterOutOfRange", defaultEncodingId="ns=bacnet;i=105056")
class BACnetEventParameterOutOfRange(ns0.datatypes.Structure):
    time_delay: o6.UInt32
    low_limit: o6.Double
    high_limit: o6.Double
    deadband: o6.Double


@o6.datatype(nodeId="ns=bacnet;i=103042", browseName="BACnetEventParameterBufferReady", defaultEncodingId="ns=bacnet;i=105058")
class BACnetEventParameterBufferReady(ns0.datatypes.Structure):
    notification_threshold: o6.UInt32
    previous_notification_count: o6.UInt32


@o6.datatype(nodeId="ns=bacnet;i=103043", browseName="BACnetEventParameterUnsignedOutOfRange", defaultEncodingId="ns=bacnet;i=105060")
class BACnetEventParameterUnsignedOutOfRange(ns0.datatypes.Structure):
    time_delay: o6.UInt32
    low_limit: o6.UInt32
    high_limit: o6.UInt32
    deadband: o6.UInt32


@o6.datatype(nodeId="ns=bacnet;i=3050", browseName="BACnetEventParameter", defaultEncodingId="ns=bacnet;i=5015")
class BACnetEventParameter(ns0.datatypes.Union):
    change_of_bitstring: BACnetEventParameterChangeOfBitstring
    change_of_state: BACnetEventParameterChangeOfState
    change_of_value: BACnetEventParameterChangeOfValue
    command_failure: BACnetEventParameterCommandFailure
    floating_limit: BACnetEventParameterFloatingLimit
    out_of_range: BACnetEventParameterOutOfRange
    extended: BACnetEventFaultParameterExtended
    buffer_ready: BACnetEventParameterBufferReady
    unsigned_range: BACnetEventParameterUnsignedRange
    double_out_of_range: BACnetEventParameterDoubleOutOfRange
    signed_out_of_range: BACnetEventParameterSignedOutOfRange
    unsigned_out_of_range: BACnetEventParameterUnsignedOutOfRange
    change_of_characterstring: BACnetEventParameterChangeOfCharacterString
    change_of_life_safety: BACnetEventParameterChangeOfLifeSafety


@o6.enumtype(nodeId="ns=bacnet;i=103048", browseName="BACnetLoggingType")
class BACnetLoggingType(ns0.datatypes.Enumeration):
    POLLED = o6.enumfield(0, name="Polled")
    COV = o6.enumfield(1, name="COV")
    TRIGGERED = o6.enumfield(2, name="Triggered")


@o6.enumtype(nodeId="ns=bacnet;i=103053", browseName="BACnetObjectTypeEnum")
class BACnetObjectTypeEnum(ns0.datatypes.Enumeration):
    ANALOG_INPUT = o6.enumfield(0, name="analog-input")
    ANALOG_OUTPUT = o6.enumfield(1, name="analog-output")
    ANALOG_VALUE = o6.enumfield(2, name="analog-value")
    BINARY_INPUT = o6.enumfield(3, name="binary-input")
    BINARY_OUTPUT = o6.enumfield(4, name="binary-output")
    BINARY_VALUE = o6.enumfield(5, name="binary-value")
    CALENDAR = o6.enumfield(6, name="calendar")
    COMMAND = o6.enumfield(7, name="command")
    DEVICE = o6.enumfield(8, name="device")
    EVENT_ENROLLMENT = o6.enumfield(9, name="event-enrollment")
    FILE = o6.enumfield(10, name="file")
    GROUP = o6.enumfield(11, name="group")
    LOOP = o6.enumfield(12, name="loop")
    MULTI_STATE_INPUT = o6.enumfield(13, name="multi-state-input")
    MULTI_STATE_OUTPUT = o6.enumfield(14, name="multi-state-output")
    NOTIFICATION_CLASS = o6.enumfield(15, name="notification-class")
    PROGRAM = o6.enumfield(16, name="program")
    SCHEDULE = o6.enumfield(17, name="schedule")
    AVERAGING = o6.enumfield(18, name="averaging")
    MULTI_STATE_VALUE = o6.enumfield(19, name="multi-state-value")
    TREND_LOG = o6.enumfield(20, name="trend-log")
    LIFE_SAFETY_POINT = o6.enumfield(21, name="life-safety-point")
    LIFE_SAFETY_ZONE = o6.enumfield(22, name="life-safety-zone")
    ACCUMULATOR = o6.enumfield(23, name="accumulator")
    PULSE_CONVERTER = o6.enumfield(24, name="pulse-converter")
    EVENT_LOG = o6.enumfield(25, name="event-log")
    GLOBAL_GROUP = o6.enumfield(26, name="global-group")
    TREND_LOG_MULTIPLE = o6.enumfield(27, name="trend-log-multiple")
    LOAD_CONTROL = o6.enumfield(28, name="load-control")
    STRUCTURED_VIEW = o6.enumfield(29, name="structured-view")
    ACCESS_DOOR = o6.enumfield(30, name="access-door")
    UNASSIGNED = o6.enumfield(31, name="unassigned")
    ACCESS_CREDENTIAL = o6.enumfield(32, name="access-credential")
    ACCESS_POINT = o6.enumfield(33, name="access-point")
    ACCESS_RIGHTS = o6.enumfield(34, name="access-rights")
    ACCESS_USER = o6.enumfield(35, name="access-user")
    ACCESS_ZONE = o6.enumfield(36, name="access-zone")
    CREDENTIONAL_DATA_INPUT = o6.enumfield(37, name="credentional-data-input")
    NETWORK_SECURITY = o6.enumfield(38, name="network-security")
    BITSTRING_VALUE = o6.enumfield(39, name="bitstring-value")
    CHARACTERSTRING_VALUE = o6.enumfield(40, name="characterstring-value")
    DATE_PATTERN_VALUE = o6.enumfield(41, name="date-pattern-value")
    DATE_VALUE = o6.enumfield(42, name="date-value")
    DATETIME_PATTERN_VALUE = o6.enumfield(43, name="datetime-pattern-value")
    DATETIME_VALUE = o6.enumfield(44, name="datetime-value")
    INTEGER_VALUE = o6.enumfield(45, name="integer-value")
    LARGE_ANALOG_VALUE = o6.enumfield(46, name="large-analog-value")
    OCTETSTRING_VALUE = o6.enumfield(47, name="octetstring-value")
    POSITIVE_INTEGER_VALUE = o6.enumfield(48, name="positive-integer-value")
    TIME_PATTERN_VALUE = o6.enumfield(49, name="time-pattern-value")
    TIME_VALUE = o6.enumfield(50, name="time-value")
    NOTIFICATION_FORWARDER = o6.enumfield(51, name="notification-forwarder")
    ALERT_ENROLLMENT = o6.enumfield(52, name="alert-enrollment")
    CHANNEL = o6.enumfield(53, name="channel")
    LIGHTING_OUTPUT = o6.enumfield(54, name="lighting-output")


@o6.enumtype(nodeId="ns=bacnet;i=103054", browseName="BACnetEventType")
class BACnetEventType(ns0.datatypes.Enumeration):
    CHANGE_OF_BITSTRING = o6.enumfield(0, name="change-of-bitstring")
    CHANGE_OF_STATE = o6.enumfield(1, name="change-of-state")
    CHANGE_OF_VALUE = o6.enumfield(2, name="change-of-value")
    COMMAND_FAILURE = o6.enumfield(3, name="command-failure")
    FLOATING_LIMIT = o6.enumfield(4, name="floating-limit")
    OUT_OF_RANGE = o6.enumfield(5, name="out-of-range")
    CHANGE_OF_LIFE_SAFETY = o6.enumfield(8, name="change-of-life-safety")
    EXTENDED = o6.enumfield(9, name="extended")
    BUFFER_READY = o6.enumfield(10, name="buffer-ready")
    UNSIGNED_RANGE = o6.enumfield(11, name="unsigned-range")
    ACCESS_EVENT = o6.enumfield(13, name="access-event")
    DOUBLE_OUT_OF_RANGE = o6.enumfield(14, name="double-out-of-range")
    SIGNED_OUT_OF_RANGE = o6.enumfield(15, name="signed-out-of-range")
    UNSIGNED_OUT_OF_RANGE = o6.enumfield(16, name="unsigned-out-of-range")
    CHANGE_OF_CHARACTERSTRING = o6.enumfield(17, name="change-of-characterstring")
    CHANGE_OF_STATUS_FLAGS = o6.enumfield(18, name="change-of-status-flags")


del Any, TYPE_CHECKING, uuid, o6, ns0
