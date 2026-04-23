# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 9b432ab0798cdfee237c0e9ed44fc89919840bb3f2ea33ca7ef0ed96e0f56539
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/BACnet_V2/"
_VERSION: str = "2.00.1"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": "1.05.02"}]
_STRUCTURES: list = [
    (
        "ns=1;i=3022",
        "BACnetAddress",
        "ns=1;i=5041",
        {
            "structure_type": 0,
            "fields": [
                {"name": "NetworkNumber", "data_type": "i=5", "value_rank": -1},
                {"name": "MacAddress", "data_type": "i=15", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=103015",
        "BACnetAddressBinding",
        "ns=1;i=105025",
        {
            "structure_type": 0,
            "fields": [
                {
                    "name": "DeviceObjectIdentifier",
                    "data_type": "i=7",
                    "value_rank": -1,
                },
                {"name": "DeviceAddress", "data_type": "ns=1;i=3022", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=103017",
        "BACnetCOVSubscription",
        "ns=1;i=105027",
        {
            "structure_type": 1,
            "fields": [
                {"name": "Recipient", "data_type": "ns=1;i=103018", "value_rank": -1},
                {
                    "name": "MonitoredPropertyReference",
                    "data_type": "ns=1;i=103002",
                    "value_rank": -1,
                },
                {
                    "name": "IssueConfirmedNotifications",
                    "data_type": "i=1",
                    "value_rank": -1,
                },
                {"name": "TimeRemaining", "data_type": "i=7", "value_rank": -1},
                {
                    "name": "CovIncrement",
                    "data_type": "i=10",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=103001",
        "BACnetDailySchedule",
        "ns=1;i=105001",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Day-schedule", "data_type": "ns=1;i=103004", "value_rank": 1}
            ],
        },
    ),
    (
        "ns=1;i=3017",
        "BACnetDate",
        "ns=1;i=5019",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Year", "data_type": "i=5", "value_rank": -1},
                {"name": "Month", "data_type": "ns=1;i=3014", "value_rank": -1},
                {"name": "DayOfMonth", "data_type": "ns=1;i=3025", "value_rank": -1},
                {"name": "DayOfWeek", "data_type": "ns=1;i=103036", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3009",
        "BACnetDateRange",
        "ns=1;i=5017",
        {
            "structure_type": 0,
            "fields": [
                {"name": "StartDate", "data_type": "ns=1;i=3017", "value_rank": -1},
                {"name": "EndTime", "data_type": "ns=1;i=3017", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3006",
        "BACnetDateTime",
        "ns=1;i=5005",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Date", "data_type": "ns=1;i=3017", "value_rank": -1},
                {"name": "Time", "data_type": "ns=1;i=3019", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=103020",
        "BACnetDestination",
        "ns=1;i=105031",
        {
            "structure_type": 0,
            "fields": [
                {"name": "ValidDays", "data_type": "ns=1;i=3060", "value_rank": -1},
                {"name": "FromTime", "data_type": "ns=1;i=3019", "value_rank": -1},
                {"name": "ToTime", "data_type": "ns=1;i=3019", "value_rank": -1},
                {"name": "Recipient", "data_type": "ns=1;i=3054", "value_rank": -1},
                {"name": "ProcessIdentifier", "data_type": "i=7", "value_rank": -1},
                {
                    "name": "IssueConfirmedNotifications",
                    "data_type": "i=1",
                    "value_rank": -1,
                },
                {"name": "Transitions", "data_type": "ns=1;i=3061", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=103002",
        "BACnetDeviceObjectPropertyReference",
        "ns=1;i=105003",
        {
            "structure_type": 1,
            "fields": [
                {"name": "ObjectIdentifier", "data_type": "i=7", "value_rank": -1},
                {
                    "name": "PropertyIdentifier",
                    "data_type": "ns=1;i=3046",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "PropertyArrayIndex",
                    "data_type": "i=7",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {
                    "name": "DeviceIdentifier",
                    "data_type": "i=7",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    ),
    (
        "ns=1;i=103031",
        "BACnetEventFaultParameterExtended",
        "ns=1;i=105038",
        {
            "structure_type": 0,
            "fields": [
                {"name": "VendorId", "data_type": "i=5", "value_rank": -1},
                {"name": "Extended-fault-type", "data_type": "i=24", "value_rank": -1},
                {"name": "Parameters", "data_type": "ns=1;i=3068", "value_rank": 1},
            ],
        },
    ),
    (
        "ns=1;i=103042",
        "BACnetEventParameterBufferReady",
        "ns=1;i=105058",
        {
            "structure_type": 0,
            "fields": [
                {
                    "name": "Notification-threshold",
                    "data_type": "i=7",
                    "value_rank": -1,
                },
                {
                    "name": "Previous-notification-count",
                    "data_type": "i=7",
                    "value_rank": -1,
                },
            ],
        },
    ),
    (
        "ns=1;i=103005",
        "BACnetEventParameterChangeOfBitstring",
        "ns=1;i=105009",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Time-delay", "data_type": "i=7", "value_rank": -1},
                {"name": "Bitmask", "data_type": "i=12755", "value_rank": -1},
                {
                    "name": "List-of-bitstring-values",
                    "data_type": "i=12755",
                    "value_rank": 1,
                },
            ],
        },
    ),
    (
        "ns=1;i=3066",
        "BACnetEventParameterChangeOfCharacterString",
        "ns=1;i=5081",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Time-delay", "data_type": "i=7", "value_rank": -1},
                {"name": "AlarmValues", "data_type": "i=12", "value_rank": 1},
            ],
        },
    ),
    (
        "ns=1;i=3027",
        "BACnetEventParameterChangeOfLifeSafety",
        "ns=1;i=5024",
        {
            "structure_type": 0,
            "fields": [
                {"name": "NewState", "data_type": "ns=1;i=3036", "value_rank": -1},
                {"name": "NewMode", "data_type": "ns=1;i=3035", "value_rank": -1},
                {
                    "name": "OperationExtended",
                    "data_type": "ns=1;i=3044",
                    "value_rank": -1,
                },
            ],
        },
    ),
    (
        "ns=1;i=103009",
        "BACnetEventParameterChangeOfState",
        "ns=1;i=105017",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Time-delay", "data_type": "i=7", "value_rank": -1},
                {"name": "List-of-values", "data_type": "ns=1;i=3028", "value_rank": 1},
            ],
        },
    ),
    (
        "ns=1;i=103037",
        "BACnetEventParameterChangeOfValue",
        "ns=1;i=105048",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Time-delay", "data_type": "i=7", "value_rank": -1},
                {
                    "name": "Cov-criteria-bitmask",
                    "data_type": "i=12755",
                    "value_rank": -1,
                },
                {
                    "name": "Cov-criteria-referenced-property-increment",
                    "data_type": "i=10",
                    "value_rank": -1,
                },
            ],
        },
    ),
    (
        "ns=1;i=103039",
        "BACnetEventParameterCommandFailure",
        "ns=1;i=105052",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Time-delay", "data_type": "i=7", "value_rank": -1},
                {
                    "name": "Feedback-property-reference",
                    "data_type": "ns=1;i=103002",
                    "value_rank": -1,
                },
            ],
        },
    ),
    (
        "ns=1;i=3058",
        "BACnetEventParameterDoubleOutOfRange",
        "ns=1;i=5010",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Time-delay", "data_type": "i=7", "value_rank": -1},
                {"name": "Low-limit", "data_type": "i=11", "value_rank": -1},
                {"name": "High-limit", "data_type": "i=11", "value_rank": -1},
                {"name": "Deadband", "data_type": "i=11", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=103040",
        "BACnetEventParameterFloatingLimit",
        "ns=1;i=105054",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Time-delay", "data_type": "i=7", "value_rank": -1},
                {
                    "name": "Setpoint-reference",
                    "data_type": "ns=1;i=103002",
                    "value_rank": -1,
                },
                {"name": "Low-diff-limit", "data_type": "i=11", "value_rank": -1},
                {"name": "High-diff-limit", "data_type": "i=11", "value_rank": -1},
                {"name": "Deadband", "data_type": "i=11", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=103041",
        "BACnetEventParameterOutOfRange",
        "ns=1;i=105056",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Time-delay", "data_type": "i=7", "value_rank": -1},
                {"name": "Low-limit", "data_type": "i=11", "value_rank": -1},
                {"name": "High-limit", "data_type": "i=11", "value_rank": -1},
                {"name": "Deadband", "data_type": "i=11", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3059",
        "BACnetEventParameterSignedOutOfRange",
        "ns=1;i=5064",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Time-delay", "data_type": "i=7", "value_rank": -1},
                {"name": "Low-limit", "data_type": "i=6", "value_rank": -1},
                {"name": "High-limit", "data_type": "i=6", "value_rank": -1},
                {"name": "Deadband", "data_type": "i=7", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=103043",
        "BACnetEventParameterUnsignedOutOfRange",
        "ns=1;i=105060",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Time-delay", "data_type": "i=7", "value_rank": -1},
                {"name": "Low-limit", "data_type": "i=7", "value_rank": -1},
                {"name": "High-limit", "data_type": "i=7", "value_rank": -1},
                {"name": "Deadband", "data_type": "i=7", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3067",
        "BACnetEventParameterUnsignedRange",
        "ns=1;i=5083",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Time-delay", "data_type": "i=7", "value_rank": -1},
                {"name": "Low-limit", "data_type": "i=7", "value_rank": -1},
                {"name": "High-limit", "data_type": "i=7", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=103030",
        "BACnetFaultParameterFaultCharacterstring",
        "ns=1;i=105036",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Fault-characterstring", "data_type": "i=12", "value_rank": -1}
            ],
        },
    ),
    (
        "ns=1;i=103032",
        "BACnetFaultParameterFaultLifeSafety",
        "ns=1;i=105040",
        {
            "structure_type": 0,
            "fields": [
                {
                    "name": "List-of-fault-values",
                    "data_type": "ns=1;i=3036",
                    "value_rank": 1,
                },
                {
                    "name": "Mode-property-reference",
                    "data_type": "ns=1;i=103002",
                    "value_rank": -1,
                },
            ],
        },
    ),
    (
        "ns=1;i=103033",
        "BACnetFaultParameterFaultState",
        "ns=1;i=105042",
        {
            "structure_type": 0,
            "fields": [
                {
                    "name": "List-of-fault-values",
                    "data_type": "ns=1;i=3031",
                    "value_rank": 1,
                }
            ],
        },
    ),
    (
        "ns=1;i=103034",
        "BACnetFaultParameterFaultStatusFlags",
        "ns=1;i=105044",
        {
            "structure_type": 0,
            "fields": [
                {
                    "name": "Status-flags-reference",
                    "data_type": "ns=1;i=103002",
                    "value_rank": 1,
                }
            ],
        },
    ),
    (
        "ns=1;i=3028",
        "BACnetPropertyStates",
        "ns=1;i=5047",
        {
            "structure_type": 0,
            "fields": [
                {"name": "BooleanValue", "data_type": "i=1", "value_rank": -1},
                {"name": "BinaryValue", "data_type": "ns=1;i=3005", "value_rank": -1},
                {"name": "EventType", "data_type": "ns=1;i=3029", "value_rank": -1},
                {"name": "Polarity", "data_type": "ns=1;i=3007", "value_rank": -1},
                {"name": "ProgramChange", "data_type": "ns=1;i=3030", "value_rank": -1},
                {"name": "ProgramState", "data_type": "ns=1;i=3031", "value_rank": -1},
                {"name": "ProgramError", "data_type": "ns=1;i=3032", "value_rank": -1},
                {"name": "Reliability", "data_type": "ns=1;i=3001", "value_rank": -1},
                {"name": "State", "data_type": "ns=1;i=3003", "value_rank": -1},
                {"name": "SystemStatus", "data_type": "ns=1;i=3033", "value_rank": -1},
                {"name": "Units", "data_type": "i=887", "value_rank": -1},
                {"name": "UnsignedValue", "data_type": "i=7", "value_rank": -1},
                {
                    "name": "LifeSafetyMode",
                    "data_type": "ns=1;i=3035",
                    "value_rank": -1,
                },
                {
                    "name": "LifeSafetyState",
                    "data_type": "ns=1;i=3036",
                    "value_rank": -1,
                },
            ],
        },
    ),
    (
        "ns=1;i=103018",
        "BACnetRecipientProcess",
        "ns=1;i=105029",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Recipient", "data_type": "ns=1;i=3054", "value_rank": -1},
                {"name": "ProcessIdentifier", "data_type": "i=7", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=103003",
        "BACnetSpecialEvent",
        "ns=1;i=105005",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Period", "data_type": "ns=1;i=3055", "value_rank": -1},
                {
                    "name": "ListOfTimeValues",
                    "data_type": "ns=1;i=103004",
                    "value_rank": 1,
                },
                {"name": "EventPriority", "data_type": "i=3", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3019",
        "BACnetTime",
        "ns=1;i=5021",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Hour", "data_type": "i=3", "value_rank": -1},
                {"name": "Minute", "data_type": "i=3", "value_rank": -1},
                {"name": "Second", "data_type": "i=3", "value_rank": -1},
                {"name": "Hundredths", "data_type": "i=3", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=103004",
        "BACnetTimeValue",
        "ns=1;i=105007",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Time", "data_type": "ns=1;i=3019", "value_rank": -1},
                {"name": "Value", "data_type": "ns=1;i=103010", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=103010",
        "BACnetTimeValueValue",
        "ns=1;i=105019",
        {
            "structure_type": 0,
            "fields": [
                {"name": "BooleanValue", "data_type": "i=1", "value_rank": -1},
                {"name": "UnsignedValue", "data_type": "i=24", "value_rank": -1},
                {"name": "SignedValue", "data_type": "i=24", "value_rank": -1},
                {"name": "OctedStringValue", "data_type": "i=15", "value_rank": -1},
                {"name": "CharStringValue", "data_type": "i=12", "value_rank": -1},
                {"name": "ObjectIdentifierValue", "data_type": "i=7", "value_rank": -1},
                {"name": "EnumerationValue", "data_type": "i=6", "value_rank": -1},
                {"name": "BitStringValue", "data_type": "i=12755", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3024",
        "BACnetWeekNDay",
        "ns=1;i=5013",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Month", "data_type": "ns=1;i=3014", "value_rank": -1},
                {"name": "Day", "data_type": "ns=1;i=3021", "value_rank": -1},
                {"name": "DayOfWeek", "data_type": "ns=1;i=103036", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3016",
        "BACnetCalendarEntry",
        "ns=1;i=5002",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Date", "data_type": "ns=1;i=3017", "value_rank": -1},
                {"name": "DateRange", "data_type": "ns=1;i=3009", "value_rank": -1},
                {"name": "WeekNDay", "data_type": "ns=1;i=3024", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3023",
        "BACnetClientCOV",
        "ns=1;i=5011",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Real-increment", "data_type": "i=10", "value_rank": -1}
            ],
        },
    ),
    (
        "ns=1;i=3050",
        "BACnetEventParameter",
        "ns=1;i=5015",
        {
            "structure_type": 0,
            "fields": [
                {
                    "name": "Change-of-bitstring",
                    "data_type": "ns=1;i=103005",
                    "value_rank": -1,
                },
                {
                    "name": "Change-of-state",
                    "data_type": "ns=1;i=103009",
                    "value_rank": -1,
                },
                {
                    "name": "Change-of-value",
                    "data_type": "ns=1;i=103037",
                    "value_rank": -1,
                },
                {
                    "name": "Command-failure",
                    "data_type": "ns=1;i=103039",
                    "value_rank": -1,
                },
                {
                    "name": "Floating-limit",
                    "data_type": "ns=1;i=103040",
                    "value_rank": -1,
                },
                {
                    "name": "Out-of-range",
                    "data_type": "ns=1;i=103041",
                    "value_rank": -1,
                },
                {"name": "Extended", "data_type": "ns=1;i=103031", "value_rank": -1},
                {
                    "name": "Buffer-ready",
                    "data_type": "ns=1;i=103042",
                    "value_rank": -1,
                },
                {
                    "name": "Unsigned-range",
                    "data_type": "ns=1;i=3067",
                    "value_rank": -1,
                },
                {
                    "name": "Double-out-of-range",
                    "data_type": "ns=1;i=3058",
                    "value_rank": -1,
                },
                {
                    "name": "Signed-out-of-range",
                    "data_type": "ns=1;i=3059",
                    "value_rank": -1,
                },
                {
                    "name": "Unsigned-out-of-range",
                    "data_type": "ns=1;i=103043",
                    "value_rank": -1,
                },
                {
                    "name": "Change-of-characterstring",
                    "data_type": "ns=1;i=3066",
                    "value_rank": -1,
                },
                {
                    "name": "Change-of-life-safety",
                    "data_type": "ns=1;i=3027",
                    "value_rank": -1,
                },
            ],
        },
    ),
    (
        "ns=1;i=3068",
        "BACnetEventParameterExtendedParameters",
        "ns=1;i=5085",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Real", "data_type": "i=11", "value_rank": -1},
                {"name": "Unsigned", "data_type": "i=7", "value_rank": -1},
                {"name": "Boolean", "data_type": "i=1", "value_rank": -1},
                {"name": "Double", "data_type": "i=11", "value_rank": -1},
                {"name": "Octed", "data_type": "i=3", "value_rank": 1},
                {"name": "CharacterString", "data_type": "i=12", "value_rank": -1},
                {"name": "BitString", "data_type": "i=12755", "value_rank": -1},
                {"name": "Enum", "data_type": "i=7", "value_rank": -1},
                {"name": "Date", "data_type": "ns=1;i=3017", "value_rank": -1},
                {"name": "Time", "data_type": "ns=1;i=3019", "value_rank": -1},
                {"name": "ObjectIdentifier", "data_type": "i=7", "value_rank": -1},
                {"name": "Reference", "data_type": "ns=1;i=103002", "value_rank": -1},
                {"name": "Integer", "data_type": "i=6", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3051",
        "BACnetFaultParameter",
        "ns=1;i=5023",
        {
            "structure_type": 0,
            "fields": [
                {
                    "name": "Fault-characterstring",
                    "data_type": "ns=1;i=103030",
                    "value_rank": -1,
                },
                {
                    "name": "Fault-life-safety",
                    "data_type": "ns=1;i=103032",
                    "value_rank": -1,
                },
                {"name": "Fault-state", "data_type": "ns=1;i=103033", "value_rank": -1},
                {
                    "name": "Fault-status-flags",
                    "data_type": "ns=1;i=103034",
                    "value_rank": -1,
                },
                {
                    "name": "Fault-extended",
                    "data_type": "ns=1;i=103031",
                    "value_rank": -1,
                },
            ],
        },
    ),
    (
        "ns=1;i=3052",
        "BACnetMessageClass",
        "ns=1;i=5028",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Unsigned", "data_type": "i=24", "value_rank": -1},
                {"name": "String", "data_type": "i=12", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3053",
        "BACnetPriorityValue",
        "ns=1;i=5030",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Real", "data_type": "i=10", "value_rank": -1},
                {"name": "Enumerated", "data_type": "i=6", "value_rank": -1},
                {"name": "Unsigned", "data_type": "i=24", "value_rank": -1},
                {"name": "Boolean", "data_type": "i=1", "value_rank": -1},
                {"name": "Signed", "data_type": "i=24", "value_rank": -1},
                {"name": "Double", "data_type": "i=11", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3054",
        "BACnetRecipient",
        "ns=1;i=5032",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Device", "data_type": "i=7", "value_rank": -1},
                {"name": "Address", "data_type": "ns=1;i=3022", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3055",
        "BACnetSpecialEventPeriod",
        "ns=1;i=5034",
        {
            "structure_type": 0,
            "fields": [
                {"name": "CalendarEntry", "data_type": "ns=1;i=3016", "value_rank": -1},
                {"name": "CalendarReference", "data_type": "i=7", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3056",
        "BACnetTimeStamp",
        "ns=1;i=5069",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Time", "data_type": "ns=1;i=3019", "value_rank": -1},
                {"name": "SequenceNumber", "data_type": "i=5", "value_rank": -1},
                {"name": "DateTime", "data_type": "ns=1;i=3006", "value_rank": -1},
            ],
        },
    ),
]
_ENUMS: list = [
    (
        "ns=1;i=3008",
        "BACnetAction",
        {
            "fields": [
                {"name": "direct", "value": 0, "display_name": "direct"},
                {"name": "reverse", "value": 1, "display_name": "reverse"},
            ]
        },
    ),
    (
        "ns=1;i=103016",
        "BACnetBackupState",
        {
            "fields": [
                {"name": "Idle", "value": 0, "display_name": "Idle"},
                {
                    "name": "Preparing_For_Backup",
                    "value": 1,
                    "display_name": "Preparing_For_Backup",
                },
                {
                    "name": "Preparing_For_Restore",
                    "value": 2,
                    "display_name": "Preparing_For_Restore",
                },
                {
                    "name": "Performing_A_Backup",
                    "value": 3,
                    "display_name": "Performing_A_Backup",
                },
                {
                    "name": "Performing_A_Restore",
                    "value": 4,
                    "display_name": "Performing_A_Restore",
                },
                {
                    "name": "Backup_Failure",
                    "value": 5,
                    "display_name": "Backup_Failure",
                },
                {
                    "name": "Restore_Failure",
                    "value": 6,
                    "display_name": "Restore_Failure",
                },
            ]
        },
    ),
    (
        "ns=1;i=3005",
        "BACnetBinaryPV",
        {
            "fields": [
                {"name": "Inactive", "value": 0, "display_name": "Inactive"},
                {"name": "Active", "value": 1, "display_name": "Active"},
            ]
        },
    ),
    (
        "ns=1;i=3021",
        "BACnetDay",
        {
            "fields": [
                {
                    "name": "days numbered 1-7",
                    "value": 1,
                    "display_name": "days numbered 1-7",
                },
                {
                    "name": "days numbered 8-14",
                    "value": 2,
                    "display_name": "days numbered 8-14",
                },
                {
                    "name": "days numbered 15-21",
                    "value": 3,
                    "display_name": "days numbered 15-21",
                },
                {
                    "name": "days numbered 22-28",
                    "value": 4,
                    "display_name": "days numbered 22-28",
                },
                {
                    "name": "days numbered 29-31",
                    "value": 5,
                    "display_name": "days numbered 29-31",
                },
                {
                    "name": "last 7 days of this month",
                    "value": 6,
                    "display_name": "last 7 days of this month",
                },
                {
                    "name": "any week of this month",
                    "value": 255,
                    "display_name": "any week of this month",
                },
            ]
        },
    ),
    (
        "ns=1;i=3025",
        "BACnetDayOfMonth",
        {
            "fields": [
                {"name": "1", "value": 1, "display_name": "1"},
                {"name": "2", "value": 2, "display_name": "2"},
                {"name": "3", "value": 3, "display_name": "3"},
                {"name": "4", "value": 4, "display_name": "4"},
                {"name": "5", "value": 5, "display_name": "5"},
                {"name": "6", "value": 6, "display_name": "6"},
                {"name": "7", "value": 7, "display_name": "7"},
                {"name": "8", "value": 8, "display_name": "8"},
                {"name": "9", "value": 9, "display_name": "9"},
                {"name": "10", "value": 10, "display_name": "10"},
                {"name": "11", "value": 11, "display_name": "11"},
                {"name": "12", "value": 12, "display_name": "12"},
                {"name": "13", "value": 13, "display_name": "13"},
                {"name": "14", "value": 14, "display_name": "14"},
                {"name": "15", "value": 15, "display_name": "15"},
                {"name": "16", "value": 16, "display_name": "16"},
                {"name": "17", "value": 17, "display_name": "17"},
                {"name": "18", "value": 18, "display_name": "18"},
                {"name": "19", "value": 19, "display_name": "19"},
                {"name": "20", "value": 20, "display_name": "20"},
                {"name": "21", "value": 21, "display_name": "21"},
                {"name": "22", "value": 22, "display_name": "22"},
                {"name": "23", "value": 23, "display_name": "23"},
                {"name": "24", "value": 24, "display_name": "24"},
                {"name": "25", "value": 25, "display_name": "25"},
                {"name": "26", "value": 26, "display_name": "26"},
                {"name": "27", "value": 27, "display_name": "27"},
                {"name": "28", "value": 28, "display_name": "28"},
                {"name": "29", "value": 29, "display_name": "29"},
                {"name": "30", "value": 30, "display_name": "30"},
                {"name": "31", "value": 31, "display_name": "31"},
                {
                    "name": "Last day of month",
                    "value": 32,
                    "display_name": "Last day of month",
                },
                {
                    "name": "Odd day of month",
                    "value": 33,
                    "display_name": "Odd day of month",
                },
                {
                    "name": "Even day of month",
                    "value": 34,
                    "display_name": "Even day of month",
                },
                {"name": "Unspecified", "value": 255, "display_name": "Unspecified"},
            ]
        },
    ),
    (
        "ns=1;i=103036",
        "BACnetDayOfWeek",
        {
            "fields": [
                {"name": "Monday", "value": 1, "display_name": "Monday"},
                {"name": "Tuesday", "value": 2, "display_name": "Tuesday"},
                {"name": "Wednesday", "value": 3, "display_name": "Wednesday"},
                {"name": "Thursday", "value": 4, "display_name": "Thursday"},
                {"name": "Friday", "value": 5, "display_name": "Friday"},
                {"name": "Saturday", "value": 6, "display_name": "Saturday"},
                {"name": "Sunday", "value": 7, "display_name": "Sunday"},
                {"name": "unspecified", "value": 255, "display_name": "unspecified"},
            ]
        },
    ),
    (
        "ns=1;i=3018",
        "BACnetDeviceCommunicationEnabled",
        {
            "fields": [
                {"name": "Enable", "value": 0, "display_name": "Enable"},
                {"name": "Disable", "value": 1, "display_name": "Disable"},
                {
                    "name": "DisableInitiation",
                    "value": 2,
                    "display_name": "DisableInitiation",
                },
            ]
        },
    ),
    (
        "ns=1;i=3033",
        "BACnetDeviceStatus",
        {
            "fields": [
                {"name": "Operational", "value": 0, "display_name": "Operational"},
                {
                    "name": "OperationalReadOnly",
                    "value": 1,
                    "display_name": "OperationalReadOnly",
                },
                {
                    "name": "DownloadRequired",
                    "value": 2,
                    "display_name": "DownloadRequired",
                },
                {
                    "name": "DownloadInProgress",
                    "value": 3,
                    "display_name": "DownloadInProgress",
                },
                {
                    "name": "NonOperational",
                    "value": 4,
                    "display_name": "NonOperational",
                },
                {
                    "name": "BackupInProgress",
                    "value": 5,
                    "display_name": "BackupInProgress",
                },
            ]
        },
    ),
    (
        "ns=1;i=3029",
        "BACnetEventEnumType",
        {
            "fields": [
                {
                    "name": "ChangeOfBitstring",
                    "value": 0,
                    "display_name": "ChangeOfBitstring",
                },
                {"name": "ChangeOfState", "value": 1, "display_name": "ChangeOfState"},
                {"name": "ChangeOfValue", "value": 2, "display_name": "ChangeOfValue"},
                {
                    "name": "CommandFailure",
                    "value": 3,
                    "display_name": "CommandFailure",
                },
                {"name": "FloatingLimit", "value": 4, "display_name": "FloatingLimit"},
                {"name": "OutOfRange", "value": 5, "display_name": "OutOfRange"},
                {
                    "name": "ChangeOfLifeSafety",
                    "value": 8,
                    "display_name": "ChangeOfLifeSafety",
                },
                {"name": "Extended", "value": 9, "display_name": "Extended"},
                {"name": "BufferReady", "value": 10, "display_name": "BufferReady"},
                {"name": "UnsignedRange", "value": 11, "display_name": "UnsignedRange"},
            ]
        },
    ),
    (
        "ns=1;i=3003",
        "BACnetEventState",
        {
            "fields": [
                {"name": "Normal", "value": 0, "display_name": "Normal"},
                {"name": "Fault", "value": 1, "display_name": "Fault"},
                {"name": "OffNormal", "value": 2, "display_name": "OffNormal"},
                {"name": "HighLimit", "value": 3, "display_name": "HighLimit"},
                {"name": "LowLimit", "value": 4, "display_name": "LowLimit"},
                {
                    "name": "LifeSafetyAlarm",
                    "value": 5,
                    "display_name": "LifeSafetyAlarm",
                },
            ]
        },
    ),
    (
        "ns=1;i=103054",
        "BACnetEventType",
        {
            "fields": [
                {
                    "name": "change-of-bitstring",
                    "value": 0,
                    "display_name": "change-of-bitstring",
                },
                {
                    "name": "change-of-state",
                    "value": 1,
                    "display_name": "change-of-state",
                },
                {
                    "name": "change-of-value",
                    "value": 2,
                    "display_name": "change-of-value",
                },
                {
                    "name": "command-failure",
                    "value": 3,
                    "display_name": "command-failure",
                },
                {"name": "out-of-range", "value": 5, "display_name": "out-of-range"},
                {
                    "name": "change-of-life-safety",
                    "value": 8,
                    "display_name": "change-of-life-safety",
                },
                {
                    "name": "floating-limit",
                    "value": 4,
                    "display_name": "floating-limit",
                },
                {"name": "extended", "value": 9, "display_name": "extended"},
                {"name": "buffer-ready", "value": 10, "display_name": "buffer-ready"},
                {
                    "name": "unsigned-range",
                    "value": 11,
                    "display_name": "unsigned-range",
                },
                {"name": "access-event", "value": 13, "display_name": "access-event"},
                {
                    "name": "double-out-of-range",
                    "value": 14,
                    "display_name": "double-out-of-range",
                },
                {
                    "name": "signed-out-of-range",
                    "value": 15,
                    "display_name": "signed-out-of-range",
                },
                {
                    "name": "unsigned-out-of-range",
                    "value": 16,
                    "display_name": "unsigned-out-of-range",
                },
                {
                    "name": "change-of-characterstring",
                    "value": 17,
                    "display_name": "change-of-characterstring",
                },
                {
                    "name": "change-of-status-flags",
                    "value": 18,
                    "display_name": "change-of-status-flags",
                },
            ]
        },
    ),
    (
        "ns=1;i=103028",
        "BACnetFaultType",
        {
            "fields": [
                {"name": "none", "value": 0, "display_name": "none"},
                {
                    "name": "fault-characterstring",
                    "value": 1,
                    "display_name": "fault-characterstring",
                },
                {"name": "fault-exended", "value": 2, "display_name": "fault-exended"},
                {
                    "name": "fault-life-safety",
                    "value": 3,
                    "display_name": "fault-life-safety",
                },
                {"name": "fault-state", "value": 4, "display_name": "fault-state"},
                {
                    "name": "fault-status-flags",
                    "value": 5,
                    "display_name": "fault-status-flags",
                },
            ]
        },
    ),
    (
        "ns=1;i=3035",
        "BACnetLifeSafetyMode",
        {
            "fields": [
                {"name": "Off", "value": 0, "display_name": "Off"},
                {"name": "On", "value": 1, "display_name": "On"},
                {"name": "Test", "value": 2, "display_name": "Test"},
                {"name": "Manned", "value": 3, "display_name": "Manned"},
                {"name": "UnManned", "value": 4, "display_name": "UnManned"},
                {"name": "Armed", "value": 5, "display_name": "Armed"},
                {"name": "Disarmed", "value": 6, "display_name": "Disarmed"},
                {"name": "Prearmed", "value": 7, "display_name": "Prearmed"},
                {"name": "Slow", "value": 8, "display_name": "Slow"},
                {"name": "Fast", "value": 9, "display_name": "Fast"},
                {"name": "Disconnected", "value": 10, "display_name": "Disconnected"},
                {"name": "Enabled", "value": 11, "display_name": "Enabled"},
                {"name": "Disabled", "value": 12, "display_name": "Disabled"},
                {
                    "name": "AutomaticReleaseDisabled",
                    "value": 13,
                    "display_name": "AutomaticReleaseDisabled",
                },
                {"name": "Default", "value": 14, "display_name": "Default"},
            ]
        },
    ),
    (
        "ns=1;i=3044",
        "BACnetLifeSafetyOperation",
        {
            "fields": [
                {"name": "None", "value": 0, "display_name": "None"},
                {"name": "Silence", "value": 1, "display_name": "Silence"},
                {
                    "name": "SilenceAudible",
                    "value": 2,
                    "display_name": "SilenceAudible",
                },
                {
                    "name": "SilenceVisible",
                    "value": 3,
                    "display_name": "SilenceVisible",
                },
                {"name": "Reset", "value": 4, "display_name": "Reset"},
                {"name": "ResetAlarm", "value": 5, "display_name": "ResetAlarm"},
                {"name": "ResetFault", "value": 6, "display_name": "ResetFault"},
                {"name": "Unsilence", "value": 7, "display_name": "Unsilence"},
                {
                    "name": "UnsilenceAudible",
                    "value": 8,
                    "display_name": "UnsilenceAudible",
                },
                {
                    "name": "UnsilenceVisible",
                    "value": 9,
                    "display_name": "UnsilenceVisible",
                },
            ]
        },
    ),
    (
        "ns=1;i=3036",
        "BACnetLifeSafetyState",
        {
            "fields": [
                {"name": "Quiet", "value": 0, "display_name": "Quiet"},
                {"name": "PreAlarm", "value": 1, "display_name": "PreAlarm"},
                {"name": "Alarm", "value": 2, "display_name": "Alarm"},
                {"name": "Fault", "value": 3, "display_name": "Fault"},
                {"name": "FaultPreAlarm", "value": 4, "display_name": "FaultPreAlarm"},
                {"name": "FaultAlarm", "value": 5, "display_name": "FaultAlarm"},
                {"name": "NotReady", "value": 6, "display_name": "NotReady"},
                {"name": "Active", "value": 7, "display_name": "Active"},
                {"name": "Tamper", "value": 8, "display_name": "Tamper"},
                {"name": "TestAlarm", "value": 9, "display_name": "TestAlarm"},
                {"name": "TestActive", "value": 10, "display_name": "TestActive"},
                {"name": "TestFault", "value": 11, "display_name": "TestFault"},
                {
                    "name": "TestFaultAlarm",
                    "value": 12,
                    "display_name": "TestFaultAlarm",
                },
                {"name": "Holdup", "value": 13, "display_name": "Holdup"},
                {"name": "Duress", "value": 14, "display_name": "Duress"},
                {"name": "TamperAlarm", "value": 15, "display_name": "TamperAlarm"},
                {"name": "Abnormal", "value": 16, "display_name": "Abnormal"},
                {
                    "name": "EmergencyPower",
                    "value": 17,
                    "display_name": "EmergencyPower",
                },
                {"name": "Delayed", "value": 18, "display_name": "Delayed"},
                {"name": "Blocked", "value": 19, "display_name": "Blocked"},
                {"name": "LocalAlarm", "value": 20, "display_name": "LocalAlarm"},
                {"name": "GeneralAlarm", "value": 21, "display_name": "GeneralAlarm"},
                {"name": "Supervisory", "value": 22, "display_name": "Supervisory"},
                {
                    "name": "TestSupervisory",
                    "value": 23,
                    "display_name": "TestSupervisory",
                },
            ]
        },
    ),
    (
        "ns=1;i=103048",
        "BACnetLoggingType",
        {
            "fields": [
                {"name": "Polled", "value": 0, "display_name": "Polled"},
                {"name": "COV", "value": 1, "display_name": "COV"},
                {"name": "Triggered", "value": 2, "display_name": "Triggered"},
            ]
        },
    ),
    (
        "ns=1;i=3057",
        "BACnetMessagePriority",
        {
            "fields": [
                {"name": "normal", "value": 0, "display_name": "normal"},
                {"name": "urgent", "value": 1, "display_name": "urgent"},
            ]
        },
    ),
    (
        "ns=1;i=3014",
        "BACnetMonth",
        {
            "fields": [
                {"name": "January", "value": 1, "display_name": "January"},
                {"name": "February", "value": 2, "display_name": "February"},
                {"name": "March", "value": 3, "display_name": "March"},
                {"name": "April", "value": 4, "display_name": "April"},
                {"name": "May", "value": 5, "display_name": "May"},
                {"name": "June", "value": 6, "display_name": "June"},
                {"name": "July", "value": 7, "display_name": "July"},
                {"name": "August", "value": 8, "display_name": "August"},
                {"name": "September", "value": 9, "display_name": "September"},
                {"name": "October", "value": 10, "display_name": "October"},
                {"name": "November", "value": 11, "display_name": "November"},
                {"name": "December", "value": 12, "display_name": "December"},
                {"name": "Odd", "value": 13, "display_name": "Odd"},
                {"name": "Even", "value": 14, "display_name": "Even"},
                {"name": "Unspecified", "value": 255, "display_name": "Unspecified"},
            ]
        },
    ),
    (
        "ns=1;i=3045",
        "BACnetNodeType",
        {
            "fields": [
                {"name": "UNKNOWN", "value": 0, "display_name": "UNKNOWN"},
                {"name": "SYSTEM", "value": 1, "display_name": "SYSTEM"},
                {"name": "NETWORK", "value": 2, "display_name": "NETWORK"},
                {"name": "DEVICE", "value": 3, "display_name": "DEVICE"},
                {
                    "name": "ORGANIZATIONAL",
                    "value": 4,
                    "display_name": "ORGANIZATIONAL",
                },
                {"name": "AREA", "value": 5, "display_name": "AREA"},
                {"name": "EQUIPMENT", "value": 6, "display_name": "EQUIPMENT"},
                {"name": "POINT", "value": 7, "display_name": "POINT"},
                {"name": "COLLECTION", "value": 8, "display_name": "COLLECTION"},
                {"name": "PROPERTY", "value": 9, "display_name": "PROPERTY"},
                {"name": "FUNCTIONAL", "value": 10, "display_name": "FUNCTIONAL"},
                {"name": "OTHER", "value": 11, "display_name": "OTHER"},
            ]
        },
    ),
    (
        "ns=1;i=3002",
        "BACnetNotifyType",
        {
            "fields": [
                {"name": "Alarm", "value": 0, "display_name": "Alarm"},
                {"name": "Event", "value": 1, "display_name": "Event"},
                {
                    "name": "AckNotification",
                    "value": 2,
                    "display_name": "AckNotification",
                },
            ]
        },
    ),
    (
        "ns=1;i=103053",
        "BACnetObjectTypeEnum",
        {
            "fields": [
                {"name": "analog-input", "value": 0, "display_name": "analog-input"},
                {"name": "analog-output", "value": 1, "display_name": "analog-output"},
                {"name": "analog-value", "value": 2, "display_name": "analog-value"},
                {"name": "binary-input", "value": 3, "display_name": "binary-input"},
                {"name": "binary-output", "value": 4, "display_name": "binary-output"},
                {"name": "binary-value", "value": 5, "display_name": "binary-value"},
                {"name": "calendar", "value": 6, "display_name": "calendar"},
                {"name": "command", "value": 7, "display_name": "command"},
                {"name": "device", "value": 8, "display_name": "device"},
                {
                    "name": "event-enrollment",
                    "value": 9,
                    "display_name": "event-enrollment",
                },
                {"name": "file", "value": 10, "display_name": "file"},
                {"name": "group", "value": 11, "display_name": "group"},
                {"name": "loop", "value": 12, "display_name": "loop"},
                {
                    "name": "multi-state-input",
                    "value": 13,
                    "display_name": "multi-state-input",
                },
                {
                    "name": "multi-state-output",
                    "value": 14,
                    "display_name": "multi-state-output",
                },
                {
                    "name": "notification-class",
                    "value": 15,
                    "display_name": "notification-class",
                },
                {"name": "program", "value": 16, "display_name": "program"},
                {"name": "schedule", "value": 17, "display_name": "schedule"},
                {"name": "averaging", "value": 18, "display_name": "averaging"},
                {
                    "name": "multi-state-value",
                    "value": 19,
                    "display_name": "multi-state-value",
                },
                {"name": "trend-log", "value": 20, "display_name": "trend-log"},
                {
                    "name": "life-safety-point",
                    "value": 21,
                    "display_name": "life-safety-point",
                },
                {
                    "name": "life-safety-zone",
                    "value": 22,
                    "display_name": "life-safety-zone",
                },
                {"name": "accumulator", "value": 23, "display_name": "accumulator"},
                {
                    "name": "pulse-converter",
                    "value": 24,
                    "display_name": "pulse-converter",
                },
                {"name": "event-log", "value": 25, "display_name": "event-log"},
                {"name": "global-group", "value": 26, "display_name": "global-group"},
                {
                    "name": "trend-log-multiple",
                    "value": 27,
                    "display_name": "trend-log-multiple",
                },
                {"name": "load-control", "value": 28, "display_name": "load-control"},
                {
                    "name": "structured-view",
                    "value": 29,
                    "display_name": "structured-view",
                },
                {"name": "access-door", "value": 30, "display_name": "access-door"},
                {"name": "unassigned", "value": 31, "display_name": "unassigned"},
                {
                    "name": "access-credential",
                    "value": 32,
                    "display_name": "access-credential",
                },
                {"name": "access-point", "value": 33, "display_name": "access-point"},
                {"name": "access-rights", "value": 34, "display_name": "access-rights"},
                {"name": "access-user", "value": 35, "display_name": "access-user"},
                {"name": "access-zone", "value": 36, "display_name": "access-zone"},
                {
                    "name": "credentional-data-input",
                    "value": 37,
                    "display_name": "credentional-data-input",
                },
                {
                    "name": "network-security",
                    "value": 38,
                    "display_name": "network-security",
                },
                {
                    "name": "bitstring-value",
                    "value": 39,
                    "display_name": "bitstring-value",
                },
                {
                    "name": "characterstring-value",
                    "value": 40,
                    "display_name": "characterstring-value",
                },
                {
                    "name": "date-pattern-value",
                    "value": 41,
                    "display_name": "date-pattern-value",
                },
                {"name": "date-value", "value": 42, "display_name": "date-value"},
                {
                    "name": "datetime-pattern-value",
                    "value": 43,
                    "display_name": "datetime-pattern-value",
                },
                {
                    "name": "datetime-value",
                    "value": 44,
                    "display_name": "datetime-value",
                },
                {"name": "integer-value", "value": 45, "display_name": "integer-value"},
                {
                    "name": "large-analog-value",
                    "value": 46,
                    "display_name": "large-analog-value",
                },
                {
                    "name": "octetstring-value",
                    "value": 47,
                    "display_name": "octetstring-value",
                },
                {
                    "name": "positive-integer-value",
                    "value": 48,
                    "display_name": "positive-integer-value",
                },
                {
                    "name": "time-pattern-value",
                    "value": 49,
                    "display_name": "time-pattern-value",
                },
                {"name": "time-value", "value": 50, "display_name": "time-value"},
                {
                    "name": "notification-forwarder",
                    "value": 51,
                    "display_name": "notification-forwarder",
                },
                {
                    "name": "alert-enrollment",
                    "value": 52,
                    "display_name": "alert-enrollment",
                },
                {"name": "channel", "value": 53, "display_name": "channel"},
                {
                    "name": "lighting-output",
                    "value": 54,
                    "display_name": "lighting-output",
                },
            ]
        },
    ),
    (
        "ns=1;i=3007",
        "BACnetPolarity",
        {
            "fields": [
                {"name": "Normal", "value": 0, "display_name": "Normal"},
                {"name": "Reverse", "value": 1, "display_name": "Reverse"},
            ]
        },
    ),
    (
        "ns=1;i=3032",
        "BACnetProgramError",
        {
            "fields": [
                {"name": "Normal", "value": 0, "display_name": "Normal"},
                {"name": "LoadFailed", "value": 1, "display_name": "LoadFailed"},
                {"name": "Internal", "value": 2, "display_name": "Internal"},
                {"name": "Program", "value": 3, "display_name": "Program"},
                {"name": "Other", "value": 4, "display_name": "Other"},
            ]
        },
    ),
    (
        "ns=1;i=3030",
        "BACnetProgramRequest",
        {
            "fields": [
                {"name": "Ready", "value": 0, "display_name": "Ready"},
                {"name": "Load", "value": 1, "display_name": "Load"},
                {"name": "Run", "value": 2, "display_name": "Run"},
                {"name": "Halt", "value": 3, "display_name": "Halt"},
                {"name": "Restart", "value": 4, "display_name": "Restart"},
                {"name": "Unload", "value": 5, "display_name": "Unload"},
            ]
        },
    ),
    (
        "ns=1;i=3031",
        "BACnetProgramStates",
        {
            "fields": [
                {"name": "Idle", "value": 0, "display_name": "Idle"},
                {"name": "Loading", "value": 1, "display_name": "Loading"},
                {"name": "Running", "value": 2, "display_name": "Running"},
                {"name": "Waiting", "value": 3, "display_name": "Waiting"},
                {"name": "Halted", "value": 4, "display_name": "Halted"},
                {"name": "Unloading", "value": 5, "display_name": "Unloading"},
            ]
        },
    ),
    (
        "ns=1;i=3046",
        "BACnetPropertyIdentifier",
        {
            "fields": [
                {
                    "name": "AckedTransitions",
                    "value": 0,
                    "display_name": "AckedTransitions",
                },
                {"name": "AckRequired", "value": 1, "display_name": "AckRequired"},
                {"name": "Action", "value": 2, "display_name": "Action"},
                {"name": "ActionText", "value": 3, "display_name": "ActionText"},
                {"name": "ActiveText", "value": 4, "display_name": "ActiveText"},
                {
                    "name": "ActiveVtSessions",
                    "value": 5,
                    "display_name": "ActiveVtSessions",
                },
                {"name": "AlarmValue", "value": 6, "display_name": "AlarmValue"},
                {"name": "AlarmValues", "value": 7, "display_name": "AlarmValues"},
                {"name": "All", "value": 8, "display_name": "All"},
                {
                    "name": "AllWritesSuccessful",
                    "value": 9,
                    "display_name": "AllWritesSuccessful",
                },
                {
                    "name": "ApduSegmentTimeout",
                    "value": 10,
                    "display_name": "ApduSegmentTimeout",
                },
                {"name": "ApduTimeout", "value": 11, "display_name": "ApduTimeout"},
                {
                    "name": "ApplicationSoftwareVersion",
                    "value": 12,
                    "display_name": "ApplicationSoftwareVersion",
                },
                {"name": "Archive", "value": 13, "display_name": "Archive"},
                {"name": "Bias", "value": 14, "display_name": "Bias"},
                {
                    "name": "ChangeOfStateCount",
                    "value": 15,
                    "display_name": "ChangeOfStateCount",
                },
                {
                    "name": "ChangeOfStateTime",
                    "value": 16,
                    "display_name": "ChangeOfStateTime",
                },
                {
                    "name": "NotificationClass",
                    "value": 17,
                    "display_name": "NotificationClass",
                },
                {
                    "name": "this property deleted",
                    "value": 18,
                    "display_name": "this property deleted",
                },
                {
                    "name": "ControlledVariableReference",
                    "value": 19,
                    "display_name": "ControlledVariableReference",
                },
                {
                    "name": "ControlledVariableUnits",
                    "value": 20,
                    "display_name": "ControlledVariableUnits",
                },
                {
                    "name": "ControlledVariableValue",
                    "value": 21,
                    "display_name": "ControlledVariableValue",
                },
                {"name": "CovIncrement", "value": 22, "display_name": "CovIncrement"},
                {"name": "DateList", "value": 23, "display_name": "DateList"},
                {
                    "name": "DaylightSavingsStatus",
                    "value": 24,
                    "display_name": "DaylightSavingsStatus",
                },
                {"name": "Deadband", "value": 25, "display_name": "Deadband"},
                {
                    "name": "DerivativeConstant",
                    "value": 26,
                    "display_name": "DerivativeConstant",
                },
                {
                    "name": "DerivativeConstantUnits",
                    "value": 27,
                    "display_name": "DerivativeConstantUnits",
                },
                {"name": "Description", "value": 28, "display_name": "Description"},
                {
                    "name": "DescriptionOfHalt",
                    "value": 29,
                    "display_name": "DescriptionOfHalt",
                },
                {
                    "name": "DeviceAddressBinding",
                    "value": 30,
                    "display_name": "DeviceAddressBinding",
                },
                {"name": "DeviceType", "value": 31, "display_name": "DeviceType"},
                {
                    "name": "EffectivePeriod",
                    "value": 32,
                    "display_name": "EffectivePeriod",
                },
                {
                    "name": "ElapsedActiveTime",
                    "value": 33,
                    "display_name": "ElapsedActiveTime",
                },
                {"name": "ErrorLimit", "value": 34, "display_name": "ErrorLimit"},
                {"name": "EventEnable", "value": 35, "display_name": "EventEnable"},
                {"name": "EventState", "value": 36, "display_name": "EventState"},
                {"name": "EventType", "value": 37, "display_name": "EventType"},
                {
                    "name": "ExceptionSchedule",
                    "value": 38,
                    "display_name": "ExceptionSchedule",
                },
                {"name": "FaultValues", "value": 39, "display_name": "FaultValues"},
                {"name": "FeedbackValue", "value": 40, "display_name": "FeedbackValue"},
                {
                    "name": "FileAccessMethod",
                    "value": 41,
                    "display_name": "FileAccessMethod",
                },
                {"name": "FileSize", "value": 42, "display_name": "FileSize"},
                {"name": "FileType", "value": 43, "display_name": "FileType"},
                {
                    "name": "FirmwareRevision",
                    "value": 44,
                    "display_name": "FirmwareRevision",
                },
                {"name": "HighLimit", "value": 45, "display_name": "HighLimit"},
                {"name": "InactiveText", "value": 46, "display_name": "InactiveText"},
                {"name": "InProcess", "value": 47, "display_name": "InProcess"},
                {"name": "InstanceOf", "value": 48, "display_name": "InstanceOf"},
                {
                    "name": "IntegralConstant",
                    "value": 49,
                    "display_name": "IntegralConstant",
                },
                {
                    "name": "IntegralConstantUnits",
                    "value": 50,
                    "display_name": "IntegralConstantUnits",
                },
                {
                    "name": "Removed In Version 1 Revision 4_51",
                    "value": 51,
                    "display_name": "Removed In Version 1 Revision 4_51",
                },
                {"name": "LimitEnable", "value": 52, "display_name": "LimitEnable"},
                {
                    "name": "ListOfGroupMembers",
                    "value": 53,
                    "display_name": "ListOfGroupMembers",
                },
                {
                    "name": "ListOfObjectPropertyReferences",
                    "value": 54,
                    "display_name": "ListOfObjectPropertyReferences",
                },
                {"name": "Unassigned_55", "value": 55, "display_name": "Unassigned_55"},
                {"name": "LocalDate", "value": 56, "display_name": "LocalDate"},
                {"name": "LocalTime", "value": 57, "display_name": "LocalTime"},
                {"name": "Location", "value": 58, "display_name": "Location"},
                {"name": "LowLimit", "value": 59, "display_name": "LowLimit"},
                {
                    "name": "ManipulatedVariableReference",
                    "value": 60,
                    "display_name": "ManipulatedVariableReference",
                },
                {"name": "MaximumOutput", "value": 61, "display_name": "MaximumOutput"},
                {
                    "name": "MaxApduLengthAccepted",
                    "value": 62,
                    "display_name": "MaxApduLengthAccepted",
                },
                {"name": "MaxInfoFrames", "value": 63, "display_name": "MaxInfoFrames"},
                {"name": "MaxMaster", "value": 64, "display_name": "MaxMaster"},
                {"name": "MaxPresValue", "value": 65, "display_name": "MaxPresValue"},
                {
                    "name": "MinimumOffTime",
                    "value": 66,
                    "display_name": "MinimumOffTime",
                },
                {"name": "MinimumOnTime", "value": 67, "display_name": "MinimumOnTime"},
                {"name": "MinimumOutput", "value": 68, "display_name": "MinimumOutput"},
                {"name": "MinPresValue", "value": 69, "display_name": "MinPresValue"},
                {"name": "ModelName", "value": 70, "display_name": "ModelName"},
                {
                    "name": "ModificationDate",
                    "value": 71,
                    "display_name": "ModificationDate",
                },
                {"name": "NotifyType", "value": 72, "display_name": "NotifyType"},
                {
                    "name": "NumberOfApduRetries",
                    "value": 73,
                    "display_name": "NumberOfApduRetries",
                },
                {
                    "name": "NumberOfStates",
                    "value": 74,
                    "display_name": "NumberOfStates",
                },
                {
                    "name": "ObjectIdentifier",
                    "value": 75,
                    "display_name": "ObjectIdentifier",
                },
                {"name": "ObjectList", "value": 76, "display_name": "ObjectList"},
                {"name": "ObjectName", "value": 77, "display_name": "ObjectName"},
                {
                    "name": "ObjectPropertyReference",
                    "value": 78,
                    "display_name": "ObjectPropertyReference",
                },
                {"name": "ObjectType", "value": 79, "display_name": "ObjectType"},
                {"name": "Optional", "value": 80, "display_name": "Optional"},
                {"name": "OutOfService", "value": 81, "display_name": "OutOfService"},
                {"name": "OutputUnits", "value": 82, "display_name": "OutputUnits"},
                {
                    "name": "EventParameters",
                    "value": 83,
                    "display_name": "EventParameters",
                },
                {"name": "Polarity", "value": 84, "display_name": "Polarity"},
                {"name": "PresentValue", "value": 85, "display_name": "PresentValue"},
                {"name": "Priority", "value": 86, "display_name": "Priority"},
                {"name": "PriorityArray", "value": 87, "display_name": "PriorityArray"},
                {
                    "name": "PriorityForWriting",
                    "value": 88,
                    "display_name": "PriorityForWriting",
                },
                {
                    "name": "ProcessIdentifier",
                    "value": 89,
                    "display_name": "ProcessIdentifier",
                },
                {"name": "ProgramChange", "value": 90, "display_name": "ProgramChange"},
                {
                    "name": "ProgramLocation",
                    "value": 91,
                    "display_name": "ProgramLocation",
                },
                {"name": "ProgramState", "value": 92, "display_name": "ProgramState"},
                {
                    "name": "ProportionalConstant",
                    "value": 93,
                    "display_name": "ProportionalConstant",
                },
                {
                    "name": "ProportionalConstantUnits",
                    "value": 94,
                    "display_name": "ProportionalConstantUnits",
                },
                {
                    "name": "Removed In Version 1 Revision 2_95",
                    "value": 95,
                    "display_name": "Removed In Version 1 Revision 2_95",
                },
                {
                    "name": "ProtocolObjectTypesSupported",
                    "value": 96,
                    "display_name": "ProtocolObjectTypesSupported",
                },
                {
                    "name": "ProtocolServicesSupported",
                    "value": 97,
                    "display_name": "ProtocolServicesSupported",
                },
                {
                    "name": "ProtocolVersion",
                    "value": 98,
                    "display_name": "ProtocolVersion",
                },
                {"name": "ReadOnly", "value": 99, "display_name": "ReadOnly"},
                {
                    "name": "ReasonForHalt",
                    "value": 100,
                    "display_name": "ReasonForHalt",
                },
                {
                    "name": "Removed In Version 1 Revision 4_101",
                    "value": 101,
                    "display_name": "Removed In Version 1 Revision 4_101",
                },
                {
                    "name": "RecipientList",
                    "value": 102,
                    "display_name": "RecipientList",
                },
                {"name": "Reliability", "value": 103, "display_name": "Reliability"},
                {
                    "name": "RelinquishDefault",
                    "value": 104,
                    "display_name": "RelinquishDefault",
                },
                {"name": "Required", "value": 105, "display_name": "Required"},
                {"name": "Resolution", "value": 106, "display_name": "Resolution"},
                {
                    "name": "SegmentationSupported",
                    "value": 107,
                    "display_name": "SegmentationSupported",
                },
                {"name": "Setpoint", "value": 108, "display_name": "Setpoint"},
                {
                    "name": "SetpointReference",
                    "value": 109,
                    "display_name": "SetpointReference",
                },
                {"name": "StateText", "value": 110, "display_name": "StateText"},
                {"name": "StatusFlags", "value": 111, "display_name": "StatusFlags"},
                {"name": "SystemStatus", "value": 112, "display_name": "SystemStatus"},
                {"name": "TimeDelay", "value": 113, "display_name": "TimeDelay"},
                {
                    "name": "TimeOfActiveTimeReset",
                    "value": 114,
                    "display_name": "TimeOfActiveTimeReset",
                },
                {
                    "name": "TimeOfStateCountReset",
                    "value": 115,
                    "display_name": "TimeOfStateCountReset",
                },
                {
                    "name": "TimeSynchronizationRecipients",
                    "value": 116,
                    "display_name": "TimeSynchronizationRecipients",
                },
                {"name": "Units", "value": 117, "display_name": "Units"},
                {
                    "name": "UpdateInterval",
                    "value": 118,
                    "display_name": "UpdateInterval",
                },
                {"name": "UtcOffset", "value": 119, "display_name": "UtcOffset"},
                {
                    "name": "VendorIdentifier",
                    "value": 120,
                    "display_name": "VendorIdentifier",
                },
                {"name": "VendorName", "value": 121, "display_name": "VendorName"},
                {
                    "name": "VtClassesSupported",
                    "value": 122,
                    "display_name": "VtClassesSupported",
                },
                {
                    "name": "WeeklySchedule",
                    "value": 123,
                    "display_name": "WeeklySchedule",
                },
                {
                    "name": "AttemptedSamples",
                    "value": 124,
                    "display_name": "AttemptedSamples",
                },
                {"name": "AverageValue", "value": 125, "display_name": "AverageValue"},
                {"name": "BufferSize", "value": 126, "display_name": "BufferSize"},
                {
                    "name": "ClientCovIncrement",
                    "value": 127,
                    "display_name": "ClientCovIncrement",
                },
                {
                    "name": "CovResubscriptionInterval",
                    "value": 128,
                    "display_name": "CovResubscriptionInterval",
                },
                {
                    "name": "Removed In Version 1 Revision 3_129",
                    "value": 129,
                    "display_name": "Removed In Version 1 Revision 3_129",
                },
                {
                    "name": "EventTimeStamps",
                    "value": 130,
                    "display_name": "EventTimeStamps",
                },
                {"name": "LogBuffer", "value": 131, "display_name": "LogBuffer"},
                {
                    "name": "LogDeviceObjectProperty",
                    "value": 132,
                    "display_name": "LogDeviceObjectProperty",
                },
                {"name": "Enable", "value": 133, "display_name": "Enable"},
                {"name": "LogInterval", "value": 134, "display_name": "LogInterval"},
                {"name": "MaximumValue", "value": 135, "display_name": "MaximumValue"},
                {"name": "MinimumValue", "value": 136, "display_name": "MinimumValue"},
                {
                    "name": "NotificationThreshold",
                    "value": 137,
                    "display_name": "NotificationThreshold",
                },
                {
                    "name": "Removed In Version 1 Revision 3_138",
                    "value": 138,
                    "display_name": "Removed In Version 1 Revision 3_138",
                },
                {
                    "name": "ProtocolRevision",
                    "value": 139,
                    "display_name": "ProtocolRevision",
                },
                {
                    "name": "RecordsSinceNotification",
                    "value": 140,
                    "display_name": "RecordsSinceNotification",
                },
                {"name": "RecordCount", "value": 141, "display_name": "RecordCount"},
                {"name": "StartTime", "value": 142, "display_name": "StartTime"},
                {"name": "StopTime", "value": 143, "display_name": "StopTime"},
                {"name": "StopWhenFull", "value": 144, "display_name": "StopWhenFull"},
                {
                    "name": "TotalRecordCount",
                    "value": 145,
                    "display_name": "TotalRecordCount",
                },
                {"name": "ValidSamples", "value": 146, "display_name": "ValidSamples"},
                {
                    "name": "WindowInterval",
                    "value": 147,
                    "display_name": "WindowInterval",
                },
                {
                    "name": "WindowSamples",
                    "value": 148,
                    "display_name": "WindowSamples",
                },
                {
                    "name": "MaximumValueTimestamp",
                    "value": 149,
                    "display_name": "MaximumValueTimestamp",
                },
                {
                    "name": "MinimumValueTimestamp",
                    "value": 150,
                    "display_name": "MinimumValueTimestamp",
                },
                {
                    "name": "VarianceValue",
                    "value": 151,
                    "display_name": "VarianceValue",
                },
                {
                    "name": "ActiveCovSubscriptions",
                    "value": 152,
                    "display_name": "ActiveCovSubscriptions",
                },
                {
                    "name": "BackupFailureTimeout",
                    "value": 153,
                    "display_name": "BackupFailureTimeout",
                },
                {
                    "name": "ConfigurationFiles",
                    "value": 154,
                    "display_name": "ConfigurationFiles",
                },
                {
                    "name": "DatabaseRevision",
                    "value": 155,
                    "display_name": "DatabaseRevision",
                },
                {
                    "name": "DirectReading",
                    "value": 156,
                    "display_name": "DirectReading",
                },
                {
                    "name": "LastRestoreTime",
                    "value": 157,
                    "display_name": "LastRestoreTime",
                },
                {
                    "name": "MaintenanceRequired",
                    "value": 158,
                    "display_name": "MaintenanceRequired",
                },
                {"name": "MemberOf", "value": 159, "display_name": "MemberOf"},
                {"name": "Mode", "value": 160, "display_name": "Mode"},
                {
                    "name": "OperationExpected",
                    "value": 161,
                    "display_name": "OperationExpected",
                },
                {"name": "Setting", "value": 162, "display_name": "Setting"},
                {"name": "Silenced", "value": 163, "display_name": "Silenced"},
                {
                    "name": "TrackingValue",
                    "value": 164,
                    "display_name": "TrackingValue",
                },
                {"name": "ZoneMembers", "value": 165, "display_name": "ZoneMembers"},
                {
                    "name": "LifeSafetyAlarmValues",
                    "value": 166,
                    "display_name": "LifeSafetyAlarmValues",
                },
                {
                    "name": "MaxSegmentsAccepted",
                    "value": 167,
                    "display_name": "MaxSegmentsAccepted",
                },
                {"name": "ProfileName", "value": 168, "display_name": "ProfileName"},
                {
                    "name": "AutoSlaveDiscovery",
                    "value": 169,
                    "display_name": "AutoSlaveDiscovery",
                },
                {
                    "name": "ManualSlaveAddressBinding",
                    "value": 170,
                    "display_name": "ManualSlaveAddressBinding",
                },
                {
                    "name": "SlaveAddressBinding",
                    "value": 171,
                    "display_name": "SlaveAddressBinding",
                },
                {
                    "name": "SlaveProxyEnable",
                    "value": 172,
                    "display_name": "SlaveProxyEnable",
                },
                {
                    "name": "LastNotifyRecord",
                    "value": 173,
                    "display_name": "LastNotifyRecord",
                },
                {
                    "name": "ScheduleDefault",
                    "value": 174,
                    "display_name": "ScheduleDefault",
                },
                {
                    "name": "AcceptedModes",
                    "value": 175,
                    "display_name": "AcceptedModes",
                },
                {"name": "AdjustValue", "value": 176, "display_name": "AdjustValue"},
                {"name": "Count", "value": 177, "display_name": "Count"},
                {
                    "name": "CountBeforeChange",
                    "value": 178,
                    "display_name": "CountBeforeChange",
                },
                {
                    "name": "CountChangeTime",
                    "value": 179,
                    "display_name": "CountChangeTime",
                },
                {"name": "CovPeriod", "value": 180, "display_name": "CovPeriod"},
                {
                    "name": "InputReference",
                    "value": 181,
                    "display_name": "InputReference",
                },
                {
                    "name": "LimitMonitoringInterval",
                    "value": 182,
                    "display_name": "LimitMonitoringInterval",
                },
                {
                    "name": "LoggingObject",
                    "value": 183,
                    "display_name": "LoggingObject",
                },
                {
                    "name": "LoggingRecord",
                    "value": 184,
                    "display_name": "LoggingRecord",
                },
                {"name": "Prescale", "value": 185, "display_name": "Prescale"},
                {"name": "PulseRate", "value": 186, "display_name": "PulseRate"},
                {"name": "Scale", "value": 187, "display_name": "Scale"},
                {"name": "ScaleFactor", "value": 188, "display_name": "ScaleFactor"},
                {"name": "UpdateTime", "value": 189, "display_name": "UpdateTime"},
                {
                    "name": "ValueBeforeChange",
                    "value": 190,
                    "display_name": "ValueBeforeChange",
                },
                {"name": "ValueSet", "value": 191, "display_name": "ValueSet"},
                {
                    "name": "ValueChangeTime",
                    "value": 192,
                    "display_name": "ValueChangeTime",
                },
                {
                    "name": "AlignIntervals",
                    "value": 193,
                    "display_name": "AlignIntervals",
                },
                {
                    "name": "Unassigned_194",
                    "value": 194,
                    "display_name": "Unassigned_194",
                },
                {
                    "name": "IntervalOffset",
                    "value": 195,
                    "display_name": "IntervalOffset",
                },
                {
                    "name": "LastRestartReason",
                    "value": 196,
                    "display_name": "LastRestartReason",
                },
                {"name": "LoggingType", "value": 197, "display_name": "LoggingType"},
                {
                    "name": "Unassigned_198",
                    "value": 198,
                    "display_name": "Unassigned_198",
                },
                {
                    "name": "Unassigned_199",
                    "value": 199,
                    "display_name": "Unassigned_199",
                },
                {
                    "name": "Unassigned_200",
                    "value": 200,
                    "display_name": "Unassigned_200",
                },
                {
                    "name": "Unassigned_201",
                    "value": 201,
                    "display_name": "Unassigned_201",
                },
                {
                    "name": "RestartNotificationRecipients",
                    "value": 202,
                    "display_name": "RestartNotificationRecipients",
                },
                {
                    "name": "TimeOfDeviceRestart",
                    "value": 203,
                    "display_name": "TimeOfDeviceRestart",
                },
                {
                    "name": "TimeSynchronizationInterval",
                    "value": 204,
                    "display_name": "TimeSynchronizationInterval",
                },
                {"name": "Trigger", "value": 205, "display_name": "Trigger"},
                {
                    "name": "UtcTimeSynchronizationRecipients",
                    "value": 206,
                    "display_name": "UtcTimeSynchronizationRecipients",
                },
                {"name": "NodeSubtype", "value": 207, "display_name": "NodeSubtype"},
                {"name": "NodeType", "value": 208, "display_name": "NodeType"},
                {
                    "name": "StructuredObjectList",
                    "value": 209,
                    "display_name": "StructuredObjectList",
                },
                {
                    "name": "SubordinateAnnotations",
                    "value": 210,
                    "display_name": "SubordinateAnnotations",
                },
                {
                    "name": "SubordinateList",
                    "value": 211,
                    "display_name": "SubordinateList",
                },
                {
                    "name": "ActualShedLevel",
                    "value": 212,
                    "display_name": "ActualShedLevel",
                },
                {"name": "DutyWindow", "value": 213, "display_name": "DutyWindow"},
                {
                    "name": "ExpectedShedLevel",
                    "value": 214,
                    "display_name": "ExpectedShedLevel",
                },
                {
                    "name": "FullDutyBaseline",
                    "value": 215,
                    "display_name": "FullDutyBaseline",
                },
                {
                    "name": "Unassigned_216",
                    "value": 216,
                    "display_name": "Unassigned_216",
                },
                {
                    "name": "Unassigned_217",
                    "value": 217,
                    "display_name": "Unassigned_217",
                },
                {
                    "name": "RequestedShedLevel",
                    "value": 218,
                    "display_name": "RequestedShedLevel",
                },
                {"name": "ShedDuration", "value": 219, "display_name": "ShedDuration"},
                {
                    "name": "ShedLevelDescriptions",
                    "value": 220,
                    "display_name": "ShedLevelDescriptions",
                },
                {"name": "ShedLevels", "value": 221, "display_name": "ShedLevels"},
                {
                    "name": "StateDescription",
                    "value": 222,
                    "display_name": "StateDescription",
                },
                {
                    "name": "Unassigned_223",
                    "value": 223,
                    "display_name": "Unassigned_223",
                },
                {
                    "name": "Unassigned_224",
                    "value": 224,
                    "display_name": "Unassigned_224",
                },
                {
                    "name": "Unassigned_225",
                    "value": 225,
                    "display_name": "Unassigned_225",
                },
                {
                    "name": "DoorAlarmState",
                    "value": 226,
                    "display_name": "DoorAlarmState",
                },
                {
                    "name": "DoorExtendedPulseTime",
                    "value": 227,
                    "display_name": "DoorExtendedPulseTime",
                },
                {"name": "DoorMembers", "value": 228, "display_name": "DoorMembers"},
                {
                    "name": "DoorOpenTooLongTime",
                    "value": 229,
                    "display_name": "DoorOpenTooLongTime",
                },
                {
                    "name": "DoorPulseTime",
                    "value": 230,
                    "display_name": "DoorPulseTime",
                },
                {"name": "DoorStatus", "value": 231, "display_name": "DoorStatus"},
                {
                    "name": "DoorUnlockDelayTime",
                    "value": 232,
                    "display_name": "DoorUnlockDelayTime",
                },
                {"name": "LockStatus", "value": 233, "display_name": "LockStatus"},
                {
                    "name": "MaskedAlarmValues",
                    "value": 234,
                    "display_name": "MaskedAlarmValues",
                },
                {
                    "name": "SecuredStatus",
                    "value": 235,
                    "display_name": "SecuredStatus",
                },
                {
                    "name": "Unassigned_236",
                    "value": 236,
                    "display_name": "Unassigned_236",
                },
                {
                    "name": "Unassigned_237",
                    "value": 237,
                    "display_name": "Unassigned_237",
                },
                {
                    "name": "Unassigned_238",
                    "value": 238,
                    "display_name": "Unassigned_238",
                },
                {
                    "name": "Unassigned_239",
                    "value": 239,
                    "display_name": "Unassigned_239",
                },
                {
                    "name": "Unassigned_240",
                    "value": 240,
                    "display_name": "Unassigned_240",
                },
                {
                    "name": "Unassigned_241",
                    "value": 241,
                    "display_name": "Unassigned_241",
                },
                {
                    "name": "Unassigned_242",
                    "value": 242,
                    "display_name": "Unassigned_242",
                },
                {
                    "name": "Unassigned_243",
                    "value": 243,
                    "display_name": "Unassigned_243",
                },
                {
                    "name": "AbsenteeLimit",
                    "value": 244,
                    "display_name": "AbsenteeLimit",
                },
                {
                    "name": "AccessAlarmEvents",
                    "value": 245,
                    "display_name": "AccessAlarmEvents",
                },
                {"name": "AccessDoors", "value": 246, "display_name": "AccessDoors"},
                {"name": "AccessEvent", "value": 247, "display_name": "AccessEvent"},
                {
                    "name": "AccessEventAuthenticationFactor",
                    "value": 248,
                    "display_name": "AccessEventAuthenticationFactor",
                },
                {
                    "name": "AccessEventCredential",
                    "value": 249,
                    "display_name": "AccessEventCredential",
                },
                {
                    "name": "AccessEventTime",
                    "value": 250,
                    "display_name": "AccessEventTime",
                },
                {
                    "name": "AccessTransactionEvents",
                    "value": 251,
                    "display_name": "AccessTransactionEvents",
                },
                {
                    "name": "Accompaniment",
                    "value": 252,
                    "display_name": "Accompaniment",
                },
                {
                    "name": "AccompanimentTime",
                    "value": 253,
                    "display_name": "AccompanimentTime",
                },
                {
                    "name": "ActivationTime",
                    "value": 254,
                    "display_name": "ActivationTime",
                },
                {
                    "name": "ActiveAuthenticationPolicy",
                    "value": 255,
                    "display_name": "ActiveAuthenticationPolicy",
                },
                {
                    "name": "AssignedAccessRights",
                    "value": 256,
                    "display_name": "AssignedAccessRights",
                },
                {
                    "name": "AuthenticationFactors",
                    "value": 257,
                    "display_name": "AuthenticationFactors",
                },
                {
                    "name": "AuthenticationPolicyList",
                    "value": 258,
                    "display_name": "AuthenticationPolicyList",
                },
                {
                    "name": "AuthenticationPolicyNames",
                    "value": 259,
                    "display_name": "AuthenticationPolicyNames",
                },
                {
                    "name": "AuthenticationStatus",
                    "value": 260,
                    "display_name": "AuthenticationStatus",
                },
                {
                    "name": "AuthorizationMode",
                    "value": 261,
                    "display_name": "AuthorizationMode",
                },
                {"name": "BelongsTo", "value": 262, "display_name": "BelongsTo"},
                {
                    "name": "CredentialDisable",
                    "value": 263,
                    "display_name": "CredentialDisable",
                },
                {
                    "name": "CredentialStatus",
                    "value": 264,
                    "display_name": "CredentialStatus",
                },
                {"name": "Credentials", "value": 265, "display_name": "Credentials"},
                {
                    "name": "CredentialsInZone",
                    "value": 266,
                    "display_name": "CredentialsInZone",
                },
                {
                    "name": "DaysRemaining",
                    "value": 267,
                    "display_name": "DaysRemaining",
                },
                {"name": "EntryPoints", "value": 268, "display_name": "EntryPoints"},
                {"name": "ExitPoints", "value": 269, "display_name": "ExitPoints"},
                {"name": "ExpiryTime", "value": 270, "display_name": "ExpiryTime"},
                {
                    "name": "ExtendedTimeEnable",
                    "value": 271,
                    "display_name": "ExtendedTimeEnable",
                },
                {
                    "name": "FailedAttemptEvents",
                    "value": 272,
                    "display_name": "FailedAttemptEvents",
                },
                {
                    "name": "FailedAttempts",
                    "value": 273,
                    "display_name": "FailedAttempts",
                },
                {
                    "name": "FailedAttemptsTime",
                    "value": 274,
                    "display_name": "FailedAttemptsTime",
                },
                {
                    "name": "LastAccessEvent",
                    "value": 275,
                    "display_name": "LastAccessEvent",
                },
                {
                    "name": "LastAccessPoint",
                    "value": 276,
                    "display_name": "LastAccessPoint",
                },
                {
                    "name": "LastCredentialAdded",
                    "value": 277,
                    "display_name": "LastCredentialAdded",
                },
                {
                    "name": "LastCredentialAddedTime",
                    "value": 278,
                    "display_name": "LastCredentialAddedTime",
                },
                {
                    "name": "LastCredentialRemoved",
                    "value": 279,
                    "display_name": "LastCredentialRemoved",
                },
                {
                    "name": "LastCredentialRemovedTime",
                    "value": 280,
                    "display_name": "LastCredentialRemovedTime",
                },
                {"name": "LastUseTime", "value": 281, "display_name": "LastUseTime"},
                {"name": "Lockout", "value": 282, "display_name": "Lockout"},
                {
                    "name": "LockoutRelinquishTime",
                    "value": 283,
                    "display_name": "LockoutRelinquishTime",
                },
                {
                    "name": "Removed In Version 1 Revision 13_284",
                    "value": 284,
                    "display_name": "Removed In Version 1 Revision 13_284",
                },
                {
                    "name": "MaxFailedAttempts",
                    "value": 285,
                    "display_name": "MaxFailedAttempts",
                },
                {"name": "Members", "value": 286, "display_name": "Members"},
                {"name": "MusterPoint", "value": 287, "display_name": "MusterPoint"},
                {
                    "name": "NegativeAccessRules",
                    "value": 288,
                    "display_name": "NegativeAccessRules",
                },
                {
                    "name": "NumberOfAuthenticationPolicies",
                    "value": 289,
                    "display_name": "NumberOfAuthenticationPolicies",
                },
                {
                    "name": "OccupancyCount",
                    "value": 290,
                    "display_name": "OccupancyCount",
                },
                {
                    "name": "OccupancyCountAdjust",
                    "value": 291,
                    "display_name": "OccupancyCountAdjust",
                },
                {
                    "name": "OccupancyCountEnable",
                    "value": 292,
                    "display_name": "OccupancyCountEnable",
                },
                {
                    "name": "Removed In Version 1 Revision 13_293",
                    "value": 293,
                    "display_name": "Removed In Version 1 Revision 13_293",
                },
                {
                    "name": "OccupancyLowerLimit",
                    "value": 294,
                    "display_name": "OccupancyLowerLimit",
                },
                {
                    "name": "OccupancyLowerLimitEnforced",
                    "value": 295,
                    "display_name": "OccupancyLowerLimitEnforced",
                },
                {
                    "name": "OccupancyState",
                    "value": 296,
                    "display_name": "OccupancyState",
                },
                {
                    "name": "OccupancyUpperLimit",
                    "value": 297,
                    "display_name": "OccupancyUpperLimit",
                },
                {
                    "name": "OccupancyUpperLimitEnforced",
                    "value": 298,
                    "display_name": "OccupancyUpperLimitEnforced",
                },
                {
                    "name": "Removed In Version 1 Revision 13_299",
                    "value": 299,
                    "display_name": "Removed In Version 1 Revision 13_299",
                },
                {"name": "PassbackMode", "value": 300, "display_name": "PassbackMode"},
                {
                    "name": "PassbackTimeout",
                    "value": 301,
                    "display_name": "PassbackTimeout",
                },
                {
                    "name": "PositiveAccessRules",
                    "value": 302,
                    "display_name": "PositiveAccessRules",
                },
                {
                    "name": "ReasonForDisable",
                    "value": 303,
                    "display_name": "ReasonForDisable",
                },
                {
                    "name": "SupportedFormats",
                    "value": 304,
                    "display_name": "SupportedFormats",
                },
                {
                    "name": "SupportedFormatClasses",
                    "value": 305,
                    "display_name": "SupportedFormatClasses",
                },
                {
                    "name": "ThreatAuthority",
                    "value": 306,
                    "display_name": "ThreatAuthority",
                },
                {"name": "ThreatLevel", "value": 307, "display_name": "ThreatLevel"},
                {"name": "TraceFlag", "value": 308, "display_name": "TraceFlag"},
                {
                    "name": "TransactionNotificationClass",
                    "value": 309,
                    "display_name": "TransactionNotificationClass",
                },
                {
                    "name": "UserExternalIdentifier",
                    "value": 310,
                    "display_name": "UserExternalIdentifier",
                },
                {
                    "name": "UserInformationReference",
                    "value": 311,
                    "display_name": "UserInformationReference",
                },
                {
                    "name": "Unassigned_312",
                    "value": 312,
                    "display_name": "Unassigned_312",
                },
                {
                    "name": "Unassigned_313",
                    "value": 313,
                    "display_name": "Unassigned_313",
                },
                {
                    "name": "Unassigned_314",
                    "value": 314,
                    "display_name": "Unassigned_314",
                },
                {
                    "name": "Unassigned_315",
                    "value": 315,
                    "display_name": "Unassigned_315",
                },
                {
                    "name": "Unassigned_316",
                    "value": 316,
                    "display_name": "Unassigned_316",
                },
                {"name": "UserName", "value": 317, "display_name": "UserName"},
                {"name": "UserType", "value": 318, "display_name": "UserType"},
                {
                    "name": "UsesRemaining",
                    "value": 319,
                    "display_name": "UsesRemaining",
                },
                {"name": "ZoneFrom", "value": 320, "display_name": "ZoneFrom"},
                {"name": "ZoneTo", "value": 321, "display_name": "ZoneTo"},
                {
                    "name": "AccessEventTag",
                    "value": 322,
                    "display_name": "AccessEventTag",
                },
                {
                    "name": "GlobalIdentifier",
                    "value": 323,
                    "display_name": "GlobalIdentifier",
                },
                {
                    "name": "Unassigned_324",
                    "value": 324,
                    "display_name": "Unassigned_324",
                },
                {
                    "name": "Unassigned_325",
                    "value": 325,
                    "display_name": "Unassigned_325",
                },
                {
                    "name": "VerificationTime",
                    "value": 326,
                    "display_name": "VerificationTime",
                },
                {
                    "name": "BaseDeviceSecurityPolicy",
                    "value": 327,
                    "display_name": "BaseDeviceSecurityPolicy",
                },
                {
                    "name": "DistributionKeyRevision",
                    "value": 328,
                    "display_name": "DistributionKeyRevision",
                },
                {"name": "DoNotHide", "value": 329, "display_name": "DoNotHide"},
                {"name": "KeySets", "value": 330, "display_name": "KeySets"},
                {
                    "name": "LastKeyServer",
                    "value": 331,
                    "display_name": "LastKeyServer",
                },
                {
                    "name": "NetworkAccessSecurityPolicies",
                    "value": 332,
                    "display_name": "NetworkAccessSecurityPolicies",
                },
                {
                    "name": "PacketReorderTime",
                    "value": 333,
                    "display_name": "PacketReorderTime",
                },
                {
                    "name": "SecurityPduTimeout",
                    "value": 334,
                    "display_name": "SecurityPduTimeout",
                },
                {
                    "name": "SecurityTimeWindow",
                    "value": 335,
                    "display_name": "SecurityTimeWindow",
                },
                {
                    "name": "SupportedSecurityAlgorithms",
                    "value": 336,
                    "display_name": "SupportedSecurityAlgorithms",
                },
                {
                    "name": "UpdateKeySetTimeout",
                    "value": 337,
                    "display_name": "UpdateKeySetTimeout",
                },
                {
                    "name": "BackupAndRestoreState",
                    "value": 338,
                    "display_name": "BackupAndRestoreState",
                },
                {
                    "name": "BackupPreparationTime",
                    "value": 339,
                    "display_name": "BackupPreparationTime",
                },
                {
                    "name": "RestoreCompletionTime",
                    "value": 340,
                    "display_name": "RestoreCompletionTime",
                },
                {
                    "name": "RestorePreparationTime",
                    "value": 341,
                    "display_name": "RestorePreparationTime",
                },
                {"name": "BitMask", "value": 342, "display_name": "BitMask"},
                {"name": "BitText", "value": 343, "display_name": "BitText"},
                {"name": "IsUtc", "value": 344, "display_name": "IsUtc"},
                {"name": "GroupMembers", "value": 345, "display_name": "GroupMembers"},
                {
                    "name": "GroupMemberNames",
                    "value": 346,
                    "display_name": "GroupMemberNames",
                },
                {
                    "name": "MemberStatusFlags",
                    "value": 347,
                    "display_name": "MemberStatusFlags",
                },
                {
                    "name": "RequestedUpdateInterval",
                    "value": 348,
                    "display_name": "RequestedUpdateInterval",
                },
                {"name": "CovuPeriod", "value": 349, "display_name": "CovuPeriod"},
                {
                    "name": "CovuRecipients",
                    "value": 350,
                    "display_name": "CovuRecipients",
                },
                {
                    "name": "EventMessageTexts",
                    "value": 351,
                    "display_name": "EventMessageTexts",
                },
                {
                    "name": "EventMessageTextsConfig",
                    "value": 352,
                    "display_name": "EventMessageTextsConfig",
                },
                {
                    "name": "EventDetectionEnable",
                    "value": 353,
                    "display_name": "EventDetectionEnable",
                },
                {
                    "name": "EventAlgorithmInhibit",
                    "value": 354,
                    "display_name": "EventAlgorithmInhibit",
                },
                {
                    "name": "EventAlgorithmInhibitRef",
                    "value": 355,
                    "display_name": "EventAlgorithmInhibitRef",
                },
                {
                    "name": "TimeDelayNormal",
                    "value": 356,
                    "display_name": "TimeDelayNormal",
                },
                {
                    "name": "ReliabilityEvaluationInhibit",
                    "value": 357,
                    "display_name": "ReliabilityEvaluationInhibit",
                },
                {
                    "name": "FaultParameters",
                    "value": 358,
                    "display_name": "FaultParameters",
                },
                {"name": "FaultType", "value": 359, "display_name": "FaultType"},
                {
                    "name": "LocalForwardingOnly",
                    "value": 360,
                    "display_name": "LocalForwardingOnly",
                },
                {
                    "name": "ProcessIdentifierFilter",
                    "value": 361,
                    "display_name": "ProcessIdentifierFilter",
                },
                {
                    "name": "SubscribedRecipients",
                    "value": 362,
                    "display_name": "SubscribedRecipients",
                },
                {"name": "PortFilter", "value": 363, "display_name": "PortFilter"},
                {
                    "name": "AuthorizationExemptions",
                    "value": 364,
                    "display_name": "AuthorizationExemptions",
                },
                {
                    "name": "AllowGroupDelayInhibit",
                    "value": 365,
                    "display_name": "AllowGroupDelayInhibit",
                },
                {
                    "name": "ChannelNumber",
                    "value": 366,
                    "display_name": "ChannelNumber",
                },
                {
                    "name": "ControlGroups",
                    "value": 367,
                    "display_name": "ControlGroups",
                },
                {
                    "name": "ExecutionDelay",
                    "value": 368,
                    "display_name": "ExecutionDelay",
                },
                {"name": "LastPriority", "value": 369, "display_name": "LastPriority"},
                {"name": "WriteStatus", "value": 370, "display_name": "WriteStatus"},
                {"name": "PropertyList", "value": 371, "display_name": "PropertyList"},
                {"name": "SerialNumber", "value": 372, "display_name": "SerialNumber"},
                {
                    "name": "BlinkWarnEnable",
                    "value": 373,
                    "display_name": "BlinkWarnEnable",
                },
                {
                    "name": "DefaultFadeTime",
                    "value": 374,
                    "display_name": "DefaultFadeTime",
                },
                {
                    "name": "DefaultRampRate",
                    "value": 375,
                    "display_name": "DefaultRampRate",
                },
                {
                    "name": "DefaultStepIncrement",
                    "value": 376,
                    "display_name": "DefaultStepIncrement",
                },
                {"name": "EgressTime", "value": 377, "display_name": "EgressTime"},
                {"name": "InProgress", "value": 378, "display_name": "InProgress"},
                {
                    "name": "InstantaneousPower",
                    "value": 379,
                    "display_name": "InstantaneousPower",
                },
                {
                    "name": "LightingCommand",
                    "value": 380,
                    "display_name": "LightingCommand",
                },
                {
                    "name": "LightingCommandDefaultPriority",
                    "value": 381,
                    "display_name": "LightingCommandDefaultPriority",
                },
                {
                    "name": "MaxActualValue",
                    "value": 382,
                    "display_name": "MaxActualValue",
                },
                {
                    "name": "MinActualValue",
                    "value": 383,
                    "display_name": "MinActualValue",
                },
                {"name": "Power", "value": 384, "display_name": "Power"},
                {"name": "Transition", "value": 385, "display_name": "Transition"},
                {"name": "EgressActive", "value": 386, "display_name": "EgressActive"},
            ]
        },
    ),
    (
        "ns=1;i=3049",
        "BACnetReinitializedStateofDevice",
        {
            "fields": [
                {"name": "Coldstart", "value": 0, "display_name": "Coldstart"},
                {"name": "Warmstart", "value": 1, "display_name": "Warmstart"},
                {"name": "Startbackup", "value": 2, "display_name": "Startbackup"},
                {"name": "Endbackup", "value": 3, "display_name": "Endbackup"},
                {"name": "Startrestore", "value": 4, "display_name": "Startrestore"},
                {"name": "Endrestore", "value": 5, "display_name": "Endrestore"},
                {"name": "Abortrestore", "value": 6, "display_name": "Abortrestore"},
            ]
        },
    ),
    (
        "ns=1;i=3001",
        "BACnetReliability",
        {
            "fields": [
                {
                    "name": "NoFaultDetected",
                    "value": 0,
                    "display_name": "NoFaultDetected",
                },
                {"name": "NoSensor", "value": 1, "display_name": "NoSensor"},
                {"name": "OverRange", "value": 2, "display_name": "OverRange"},
                {"name": "UnderRange", "value": 3, "display_name": "UnderRange"},
                {"name": "OpenLoop", "value": 4, "display_name": "OpenLoop"},
                {"name": "ShortedLoop", "value": 5, "display_name": "ShortedLoop"},
                {"name": "NoOutput", "value": 6, "display_name": "NoOutput"},
                {
                    "name": "UnreliableOther",
                    "value": 7,
                    "display_name": "UnreliableOther",
                },
                {"name": "ProcessError", "value": 8, "display_name": "ProcessError"},
                {
                    "name": "MultiStateFault",
                    "value": 9,
                    "display_name": "MultiStateFault",
                },
                {
                    "name": "ConfigurationError",
                    "value": 10,
                    "display_name": "ConfigurationError",
                },
                {
                    "name": "CommunicationFailure",
                    "value": 12,
                    "display_name": "CommunicationFailure",
                },
                {"name": "MemberFault", "value": 13, "display_name": "MemberFault"},
                {
                    "name": "MONITORED_OBJECT_FAULT",
                    "value": 14,
                    "display_name": "MONITORED_OBJECT_FAULT",
                },
                {"name": "TRIPPED", "value": 15, "display_name": "TRIPPED"},
            ]
        },
    ),
    (
        "ns=1;i=103019",
        "BACnetRestartReason",
        {
            "fields": [
                {"name": "unknown", "value": 0, "display_name": "unknown"},
                {"name": "coldstart", "value": 1, "display_name": "coldstart"},
                {"name": "warmstart", "value": 2, "display_name": "warmstart"},
                {
                    "name": "detected_power_lost",
                    "value": 3,
                    "display_name": "detected_power_lost",
                },
                {
                    "name": "detected_powered_off",
                    "value": 4,
                    "display_name": "detected_powered_off",
                },
                {
                    "name": "hardware_watchdog",
                    "value": 5,
                    "display_name": "hardware_watchdog",
                },
                {
                    "name": "software_watchdog",
                    "value": 6,
                    "display_name": "software_watchdog",
                },
                {"name": "suspended", "value": 7, "display_name": "suspended"},
            ]
        },
    ),
    (
        "ns=1;i=103011",
        "BACnetSegmentation",
        {
            "fields": [
                {
                    "name": "segmented-both",
                    "value": 0,
                    "display_name": "segmented-both",
                },
                {
                    "name": "segmented-transmit",
                    "value": 1,
                    "display_name": "segmented-transmit",
                },
                {
                    "name": "segmented-receive",
                    "value": 2,
                    "display_name": "segmented-receive",
                },
                {
                    "name": "no-segmentation",
                    "value": 3,
                    "display_name": "no-segmentation",
                },
            ]
        },
    ),
    (
        "ns=1;i=3060",
        "BACnetDaysOfWeek",
        {
            "fields": [
                {"name": "monday", "value": 0, "display_name": "monday"},
                {"name": "tuesday", "value": 1, "display_name": "tuesday"},
                {"name": "wednesday", "value": 2, "display_name": "wednesday"},
                {"name": "thursday", "value": 3, "display_name": "thursday"},
                {"name": "friday", "value": 4, "display_name": "friday"},
                {"name": "saturday", "value": 5, "display_name": "saturday"},
                {"name": "sunday", "value": 6, "display_name": "sunday"},
            ]
        },
    ),
    (
        "ns=1;i=3061",
        "BACnetEventTransitionBits",
        {
            "fields": [
                {"name": "to-offnormal", "value": 0, "display_name": "to-offnormal"},
                {"name": "to-fault", "value": 1, "display_name": "to-fault"},
                {"name": "to-normal", "value": 2, "display_name": "to-normal"},
            ]
        },
    ),
    (
        "ns=1;i=3062",
        "BACnetLimitEnable",
        {
            "fields": [
                {
                    "name": "lowLimitEnable",
                    "value": 0,
                    "display_name": "lowLimitEnable",
                },
                {
                    "name": "highLimitEnable",
                    "value": 1,
                    "display_name": "highLimitEnable",
                },
            ]
        },
    ),
    (
        "ns=1;i=3063",
        "BACnetObjectTypeSupportedBits",
        {
            "fields": [
                {"name": "analog-input", "value": 0, "display_name": "analog-input"},
                {"name": "analog-output", "value": 1, "display_name": "analog-output"},
                {"name": "analog-value", "value": 2, "display_name": "analog-value"},
                {"name": "binary-input", "value": 3, "display_name": "binary-input"},
                {"name": "binary-output", "value": 4, "display_name": "binary-output"},
                {"name": "binary-value", "value": 5, "display_name": "binary-value"},
                {"name": "calendar", "value": 6, "display_name": "calendar"},
                {"name": "command", "value": 7, "display_name": "command"},
                {"name": "device", "value": 8, "display_name": "device"},
                {
                    "name": "event-enrollment",
                    "value": 9,
                    "display_name": "event-enrollment",
                },
                {"name": "file", "value": 10, "display_name": "file"},
                {"name": "group", "value": 11, "display_name": "group"},
                {"name": "loop", "value": 12, "display_name": "loop"},
                {
                    "name": "multi-state-input",
                    "value": 13,
                    "display_name": "multi-state-input",
                },
                {
                    "name": "multi-state-output",
                    "value": 14,
                    "display_name": "multi-state-output",
                },
                {
                    "name": "notification-class",
                    "value": 15,
                    "display_name": "notification-class",
                },
                {"name": "program", "value": 16, "display_name": "program"},
                {"name": "schedule", "value": 17, "display_name": "schedule"},
                {"name": "averaging", "value": 18, "display_name": "averaging"},
                {
                    "name": "multi-state-value",
                    "value": 19,
                    "display_name": "multi-state-value",
                },
                {"name": "trend-log", "value": 20, "display_name": "trend-log"},
                {
                    "name": "life-safety-point",
                    "value": 21,
                    "display_name": "life-safety-point",
                },
                {
                    "name": "life-safety-zone",
                    "value": 22,
                    "display_name": "life-safety-zone",
                },
                {"name": "accumulator", "value": 23, "display_name": "accumulator"},
                {
                    "name": "pulse-converter",
                    "value": 24,
                    "display_name": "pulse-converter",
                },
                {"name": "event-log", "value": 25, "display_name": "event-log"},
                {"name": "global-group", "value": 26, "display_name": "global-group"},
                {
                    "name": "trend-log-multiple",
                    "value": 27,
                    "display_name": "trend-log-multiple",
                },
                {"name": "load-control", "value": 28, "display_name": "load-control"},
                {
                    "name": "structured-view",
                    "value": 29,
                    "display_name": "structured-view",
                },
                {"name": "access-door", "value": 30, "display_name": "access-door"},
                {"name": "UNASSIGNED_31", "value": 31, "display_name": "UNASSIGNED_31"},
                {
                    "name": "access-credential",
                    "value": 32,
                    "display_name": "access-credential",
                },
                {"name": "access-point", "value": 33, "display_name": "access-point"},
                {"name": "access-rights", "value": 34, "display_name": "access-rights"},
                {"name": "access-user", "value": 35, "display_name": "access-user"},
                {"name": "access-zone", "value": 36, "display_name": "access-zone"},
                {
                    "name": "credential-data-input",
                    "value": 37,
                    "display_name": "credential-data-input",
                },
                {
                    "name": "network-security",
                    "value": 38,
                    "display_name": "network-security",
                },
                {
                    "name": "bitstring-value",
                    "value": 39,
                    "display_name": "bitstring-value",
                },
                {
                    "name": "characterstring-value",
                    "value": 40,
                    "display_name": "characterstring-value",
                },
                {
                    "name": "date-pattern-value",
                    "value": 41,
                    "display_name": "date-pattern-value",
                },
                {"name": "date-value", "value": 42, "display_name": "date-value"},
                {
                    "name": "datetime-pattern-value",
                    "value": 43,
                    "display_name": "datetime-pattern-value",
                },
                {
                    "name": "datetime-value",
                    "value": 44,
                    "display_name": "datetime-value",
                },
                {"name": "integer-value", "value": 45, "display_name": "integer-value"},
                {
                    "name": "large-analog-value",
                    "value": 46,
                    "display_name": "large-analog-value",
                },
                {
                    "name": "octetstring-value",
                    "value": 47,
                    "display_name": "octetstring-value",
                },
                {
                    "name": "positive-integer-value",
                    "value": 48,
                    "display_name": "positive-integer-value",
                },
                {
                    "name": "time-pattern-value",
                    "value": 49,
                    "display_name": "time-pattern-value",
                },
                {"name": "time-value", "value": 50, "display_name": "time-value"},
                {
                    "name": "notification-forwarder",
                    "value": 51,
                    "display_name": "notification-forwarder",
                },
                {
                    "name": "alert-enrollment",
                    "value": 52,
                    "display_name": "alert-enrollment",
                },
                {"name": "channel", "value": 53, "display_name": "channel"},
                {
                    "name": "lighting-output",
                    "value": 54,
                    "display_name": "lighting-output",
                },
            ]
        },
    ),
    (
        "ns=1;i=3064",
        "BACnetServicesSupportedBits",
        {
            "fields": [
                {
                    "name": "acknowledgeAlarm",
                    "value": 0,
                    "display_name": "acknowledgeAlarm",
                },
                {
                    "name": "confirmedCOVNotification",
                    "value": 1,
                    "display_name": "confirmedCOVNotification",
                },
                {
                    "name": "confirmedEventNotification",
                    "value": 2,
                    "display_name": "confirmedEventNotification",
                },
                {
                    "name": "getAlarmSummary",
                    "value": 3,
                    "display_name": "getAlarmSummary",
                },
                {
                    "name": "getEnrollmentSummary",
                    "value": 4,
                    "display_name": "getEnrollmentSummary",
                },
                {"name": "subscribeCOV", "value": 5, "display_name": "subscribeCOV"},
                {
                    "name": "atomicReadFile",
                    "value": 6,
                    "display_name": "atomicReadFile",
                },
                {
                    "name": "atomicWriteFile",
                    "value": 7,
                    "display_name": "atomicWriteFile",
                },
                {
                    "name": "addListElement",
                    "value": 8,
                    "display_name": "addListElement",
                },
                {
                    "name": "removeListElement",
                    "value": 9,
                    "display_name": "removeListElement",
                },
                {"name": "createObject", "value": 10, "display_name": "createObject"},
                {"name": "deleteObject", "value": 11, "display_name": "deleteObject"},
                {"name": "readProperty", "value": 12, "display_name": "readProperty"},
                {"name": "UNASSIGNED_13", "value": 13, "display_name": "UNASSIGNED_13"},
                {
                    "name": "readPropertyMultiple",
                    "value": 14,
                    "display_name": "readPropertyMultiple",
                },
                {"name": "writeProperty", "value": 15, "display_name": "writeProperty"},
                {
                    "name": "writePropertyMultiple",
                    "value": 16,
                    "display_name": "writePropertyMultiple",
                },
                {
                    "name": "deviceCommunicationControl",
                    "value": 17,
                    "display_name": "deviceCommunicationControl",
                },
                {
                    "name": "confirmedPrivateTransfer",
                    "value": 18,
                    "display_name": "confirmedPrivateTransfer",
                },
                {
                    "name": "reinitializeDevice",
                    "value": 19,
                    "display_name": "reinitializeDevice",
                },
                {"name": "vtOpen", "value": 20, "display_name": "vtOpen"},
                {"name": "vtClose", "value": 21, "display_name": "vtClose"},
                {"name": "vtData", "value": 22, "display_name": "vtData"},
                {"name": "UNASSIGNED_24", "value": 23, "display_name": "UNASSIGNED_24"},
                {"name": "UNASSIGNED_25", "value": 24, "display_name": "UNASSIGNED_25"},
                {"name": "i-Am", "value": 25, "display_name": "i-Am"},
                {"name": "i-Have", "value": 26, "display_name": "i-Have"},
                {
                    "name": "unconfirmedCOVNotification",
                    "value": 27,
                    "display_name": "unconfirmedCOVNotification",
                },
                {
                    "name": "unconfirmedEventNotification",
                    "value": 28,
                    "display_name": "unconfirmedEventNotification",
                },
                {
                    "name": "unconfirmedPrivateTransfer",
                    "value": 29,
                    "display_name": "unconfirmedPrivateTransfer",
                },
                {
                    "name": "unconfirmedTextMessage",
                    "value": 30,
                    "display_name": "unconfirmedTextMessage",
                },
                {
                    "name": "timeSynchronization",
                    "value": 31,
                    "display_name": "timeSynchronization",
                },
                {"name": "who-Has", "value": 32, "display_name": "who-Has"},
                {"name": "who-Is", "value": 33, "display_name": "who-Is"},
                {"name": "readRange", "value": 34, "display_name": "readRange"},
                {
                    "name": "utcTimeSynchronization",
                    "value": 35,
                    "display_name": "utcTimeSynchronization",
                },
                {
                    "name": "lifeSafetyOperation",
                    "value": 36,
                    "display_name": "lifeSafetyOperation",
                },
                {
                    "name": "subscribeCOVProperty",
                    "value": 37,
                    "display_name": "subscribeCOVProperty",
                },
                {
                    "name": "getEventInformation",
                    "value": 38,
                    "display_name": "getEventInformation",
                },
                {"name": "writeGroup", "value": 39, "display_name": "writeGroup"},
            ]
        },
    ),
    (
        "ns=1;i=3065",
        "BACnetStatusFlags",
        {
            "fields": [
                {"name": "InAlarm", "value": 0, "display_name": "InAlarm"},
                {"name": "Fault", "value": 1, "display_name": "Fault"},
                {"name": "Overriden", "value": 2, "display_name": "Overriden"},
                {"name": "OutOfService", "value": 3, "display_name": "OutOfService"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=1;i=3022", "ns=1;i=5041", ["i=5", "i=15"]),
        ("ns=1;i=103015", "ns=1;i=105025", ["i=7", "ns=1;i=3022"]),
        (
            "ns=1;i=103017",
            "ns=1;i=105027",
            ["ns=1;i=103018", "ns=1;i=103002", "i=1", "i=7", "i=10"],
        ),
        ("ns=1;i=103001", "ns=1;i=105001", ["ns=1;i=103004"]),
        (
            "ns=1;i=3017",
            "ns=1;i=5019",
            ["i=5", "ns=1;i=3014", "ns=1;i=3025", "ns=1;i=103036"],
        ),
        ("ns=1;i=3009", "ns=1;i=5017", ["ns=1;i=3017", "ns=1;i=3017"]),
        ("ns=1;i=3006", "ns=1;i=5005", ["ns=1;i=3017", "ns=1;i=3019"]),
        (
            "ns=1;i=103020",
            "ns=1;i=105031",
            [
                "ns=1;i=3060",
                "ns=1;i=3019",
                "ns=1;i=3019",
                "ns=1;i=3054",
                "i=7",
                "i=1",
                "ns=1;i=3061",
            ],
        ),
        ("ns=1;i=103002", "ns=1;i=105003", ["i=7", "ns=1;i=3046", "i=7", "i=7"]),
        ("ns=1;i=103031", "ns=1;i=105038", ["i=5", "i=24", "ns=1;i=3068"]),
        ("ns=1;i=103042", "ns=1;i=105058", ["i=7", "i=7"]),
        ("ns=1;i=103005", "ns=1;i=105009", ["i=7", "i=12755", "i=12755"]),
        ("ns=1;i=3066", "ns=1;i=5081", ["i=7", "i=12"]),
        ("ns=1;i=3027", "ns=1;i=5024", ["ns=1;i=3036", "ns=1;i=3035", "ns=1;i=3044"]),
        ("ns=1;i=103009", "ns=1;i=105017", ["i=7", "ns=1;i=3028"]),
        ("ns=1;i=103037", "ns=1;i=105048", ["i=7", "i=12755", "i=10"]),
        ("ns=1;i=103039", "ns=1;i=105052", ["i=7", "ns=1;i=103002"]),
        ("ns=1;i=3058", "ns=1;i=5010", ["i=7", "i=11", "i=11", "i=11"]),
        (
            "ns=1;i=103040",
            "ns=1;i=105054",
            ["i=7", "ns=1;i=103002", "i=11", "i=11", "i=11"],
        ),
        ("ns=1;i=103041", "ns=1;i=105056", ["i=7", "i=11", "i=11", "i=11"]),
        ("ns=1;i=3059", "ns=1;i=5064", ["i=7", "i=6", "i=6", "i=7"]),
        ("ns=1;i=103043", "ns=1;i=105060", ["i=7", "i=7", "i=7", "i=7"]),
        ("ns=1;i=3067", "ns=1;i=5083", ["i=7", "i=7", "i=7"]),
        ("ns=1;i=103030", "ns=1;i=105036", ["i=12"]),
        ("ns=1;i=103032", "ns=1;i=105040", ["ns=1;i=3036", "ns=1;i=103002"]),
        ("ns=1;i=103033", "ns=1;i=105042", ["ns=1;i=3031"]),
        ("ns=1;i=103034", "ns=1;i=105044", ["ns=1;i=103002"]),
        (
            "ns=1;i=3028",
            "ns=1;i=5047",
            [
                "i=1",
                "ns=1;i=3005",
                "ns=1;i=3029",
                "ns=1;i=3007",
                "ns=1;i=3030",
                "ns=1;i=3031",
                "ns=1;i=3032",
                "ns=1;i=3001",
                "ns=1;i=3003",
                "ns=1;i=3033",
                "i=887",
                "i=7",
                "ns=1;i=3035",
                "ns=1;i=3036",
            ],
        ),
        ("ns=1;i=103018", "ns=1;i=105029", ["ns=1;i=3054", "i=7"]),
        ("ns=1;i=103003", "ns=1;i=105005", ["ns=1;i=3055", "ns=1;i=103004", "i=3"]),
        ("ns=1;i=3019", "ns=1;i=5021", ["i=3", "i=3", "i=3", "i=3"]),
        ("ns=1;i=103004", "ns=1;i=105007", ["ns=1;i=3019", "ns=1;i=103010"]),
        (
            "ns=1;i=103010",
            "ns=1;i=105019",
            ["i=1", "i=24", "i=24", "i=15", "i=12", "i=7", "i=6", "i=12755"],
        ),
        ("ns=1;i=3024", "ns=1;i=5013", ["ns=1;i=3014", "ns=1;i=3021", "ns=1;i=103036"]),
        ("ns=1;i=3016", "ns=1;i=5002", ["ns=1;i=3017", "ns=1;i=3009", "ns=1;i=3024"]),
        ("ns=1;i=3023", "ns=1;i=5011", ["i=10"]),
        (
            "ns=1;i=3050",
            "ns=1;i=5015",
            [
                "ns=1;i=103005",
                "ns=1;i=103009",
                "ns=1;i=103037",
                "ns=1;i=103039",
                "ns=1;i=103040",
                "ns=1;i=103041",
                "ns=1;i=103031",
                "ns=1;i=103042",
                "ns=1;i=3067",
                "ns=1;i=3058",
                "ns=1;i=3059",
                "ns=1;i=103043",
                "ns=1;i=3066",
                "ns=1;i=3027",
            ],
        ),
        (
            "ns=1;i=3068",
            "ns=1;i=5085",
            [
                "i=11",
                "i=7",
                "i=1",
                "i=11",
                "i=3",
                "i=12",
                "i=12755",
                "i=7",
                "ns=1;i=3017",
                "ns=1;i=3019",
                "i=7",
                "ns=1;i=103002",
                "i=6",
            ],
        ),
        (
            "ns=1;i=3051",
            "ns=1;i=5023",
            [
                "ns=1;i=103030",
                "ns=1;i=103032",
                "ns=1;i=103033",
                "ns=1;i=103034",
                "ns=1;i=103031",
            ],
        ),
        ("ns=1;i=3052", "ns=1;i=5028", ["i=24", "i=12"]),
        ("ns=1;i=3053", "ns=1;i=5030", ["i=10", "i=6", "i=24", "i=1", "i=24", "i=11"]),
        ("ns=1;i=3054", "ns=1;i=5032", ["i=7", "ns=1;i=3022"]),
        ("ns=1;i=3055", "ns=1;i=5034", ["ns=1;i=3016", "i=7"]),
        ("ns=1;i=3056", "ns=1;i=5069", ["ns=1;i=3019", "i=5", "ns=1;i=3006"]),
    ],
    [
        "ns=1;i=3008",
        "ns=1;i=103016",
        "ns=1;i=3005",
        "ns=1;i=3021",
        "ns=1;i=3025",
        "ns=1;i=103036",
        "ns=1;i=3018",
        "ns=1;i=3033",
        "ns=1;i=3029",
        "ns=1;i=3003",
        "ns=1;i=103054",
        "ns=1;i=103028",
        "ns=1;i=3035",
        "ns=1;i=3044",
        "ns=1;i=3036",
        "ns=1;i=103048",
        "ns=1;i=3057",
        "ns=1;i=3014",
        "ns=1;i=3045",
        "ns=1;i=3002",
        "ns=1;i=103053",
        "ns=1;i=3007",
        "ns=1;i=3032",
        "ns=1;i=3030",
        "ns=1;i=3031",
        "ns=1;i=3046",
        "ns=1;i=3049",
        "ns=1;i=3001",
        "ns=1;i=103019",
        "ns=1;i=103011",
        "ns=1;i=3060",
        "ns=1;i=3061",
        "ns=1;i=3062",
        "ns=1;i=3063",
        "ns=1;i=3064",
        "ns=1;i=3065",
    ],
)
_NODES: dict = {
    "datatypes": {
        "BACnetAction": ("D", "ns=1;i=3008", {"EnumStrings": ("V", "ns=1;i=6121", {})}),
        "BACnetAddress": ("D", "ns=1;i=3022", {}),
        "BACnetAddressBinding": ("D", "ns=1;i=103015", {}),
        "BACnetBackupState": (
            "D",
            "ns=1;i=103016",
            {"EnumStrings": ("V", "ns=1;i=106116", {})},
        ),
        "BACnetBinaryPV": (
            "D",
            "ns=1;i=3005",
            {"EnumStrings": ("V", "ns=1;i=6008", {})},
        ),
        "BACnetCOVSubscription": ("D", "ns=1;i=103017", {}),
        "BACnetCalendarEntry": ("D", "ns=1;i=3016", {}),
        "BACnetClientCOV": ("D", "ns=1;i=3023", {}),
        "BACnetDailySchedule": ("D", "ns=1;i=103001", {}),
        "BACnetDate": ("D", "ns=1;i=3017", {}),
        "BACnetDateRange": ("D", "ns=1;i=3009", {}),
        "BACnetDateTime": ("D", "ns=1;i=3006", {}),
        "BACnetDay": ("D", "ns=1;i=3021", {"EnumValues": ("V", "ns=1;i=6165", {})}),
        "BACnetDayOfMonth": (
            "D",
            "ns=1;i=3025",
            {"EnumValues": ("V", "ns=1;i=6159", {})},
        ),
        "BACnetDayOfWeek": (
            "D",
            "ns=1;i=103036",
            {"EnumValues": ("V", "ns=1;i=106169", {})},
        ),
        "BACnetDaysOfWeek": (
            "D",
            "ns=1;i=3060",
            {"OptionSetValues": ("V", "ns=1;i=6169", {})},
        ),
        "BACnetDestination": ("D", "ns=1;i=103020", {}),
        "BACnetDeviceCommunicationEnabled": (
            "D",
            "ns=1;i=3018",
            {"EnumStrings": ("V", "ns=1;i=6166", {})},
        ),
        "BACnetDeviceCount": ("D", "ns=1;i=3013", {}),
        "BACnetDeviceObjectPropertyReference": ("D", "ns=1;i=103002", {}),
        "BACnetDeviceStatus": (
            "D",
            "ns=1;i=3033",
            {"EnumStrings": ("V", "ns=1;i=6155", {})},
        ),
        "BACnetElementCount": ("D", "ns=1;i=3010", {}),
        "BACnetEventEnumType": (
            "D",
            "ns=1;i=3029",
            {"EnumValues": ("V", "ns=1;i=6152", {})},
        ),
        "BACnetEventFaultParameterExtended": ("D", "ns=1;i=103031", {}),
        "BACnetEventParameter": ("D", "ns=1;i=3050", {}),
        "BACnetEventParameterBufferReady": ("D", "ns=1;i=103042", {}),
        "BACnetEventParameterChangeOfBitstring": ("D", "ns=1;i=103005", {}),
        "BACnetEventParameterChangeOfCharacterString": ("D", "ns=1;i=3066", {}),
        "BACnetEventParameterChangeOfLifeSafety": ("D", "ns=1;i=3027", {}),
        "BACnetEventParameterChangeOfState": ("D", "ns=1;i=103009", {}),
        "BACnetEventParameterChangeOfValue": ("D", "ns=1;i=103037", {}),
        "BACnetEventParameterCommandFailure": ("D", "ns=1;i=103039", {}),
        "BACnetEventParameterDoubleOutOfRange": ("D", "ns=1;i=3058", {}),
        "BACnetEventParameterExtendedParameters": ("D", "ns=1;i=3068", {}),
        "BACnetEventParameterFloatingLimit": ("D", "ns=1;i=103040", {}),
        "BACnetEventParameterOutOfRange": ("D", "ns=1;i=103041", {}),
        "BACnetEventParameterSignedOutOfRange": ("D", "ns=1;i=3059", {}),
        "BACnetEventParameterUnsignedOutOfRange": ("D", "ns=1;i=103043", {}),
        "BACnetEventParameterUnsignedRange": ("D", "ns=1;i=3067", {}),
        "BACnetEventState": (
            "D",
            "ns=1;i=3003",
            {"EnumStrings": ("V", "ns=1;i=6055", {})},
        ),
        "BACnetEventTransitionBits": (
            "D",
            "ns=1;i=3061",
            {"OptionSetValues": ("V", "ns=1;i=6702", {})},
        ),
        "BACnetEventType": (
            "D",
            "ns=1;i=103054",
            {"EnumValues": ("V", "ns=1;i=106277", {})},
        ),
        "BACnetFaultParameter": ("D", "ns=1;i=3051", {}),
        "BACnetFaultParameterFaultCharacterstring": ("D", "ns=1;i=103030", {}),
        "BACnetFaultParameterFaultLifeSafety": ("D", "ns=1;i=103032", {}),
        "BACnetFaultParameterFaultState": ("D", "ns=1;i=103033", {}),
        "BACnetFaultParameterFaultStatusFlags": ("D", "ns=1;i=103034", {}),
        "BACnetFaultType": (
            "D",
            "ns=1;i=103028",
            {"EnumStrings": ("V", "ns=1;i=106083", {})},
        ),
        "BACnetLifeSafetyMode": (
            "D",
            "ns=1;i=3035",
            {"EnumStrings": ("V", "ns=1;i=6160", {})},
        ),
        "BACnetLifeSafetyOperation": (
            "D",
            "ns=1;i=3044",
            {"EnumStrings": ("V", "ns=1;i=6500", {})},
        ),
        "BACnetLifeSafetyState": (
            "D",
            "ns=1;i=3036",
            {"EnumStrings": ("V", "ns=1;i=6161", {})},
        ),
        "BACnetLimitEnable": (
            "D",
            "ns=1;i=3062",
            {"OptionSetValues": ("V", "ns=1;i=6701", {})},
        ),
        "BACnetLoggingType": (
            "D",
            "ns=1;i=103048",
            {"EnumStrings": ("V", "ns=1;i=106235", {})},
        ),
        "BACnetMessageClass": ("D", "ns=1;i=3052", {}),
        "BACnetMessagePriority": (
            "D",
            "ns=1;i=3057",
            {"EnumStrings": ("V", "ns=1;i=6270", {})},
        ),
        "BACnetMonth": ("D", "ns=1;i=3014", {"EnumValues": ("V", "ns=1;i=6167", {})}),
        "BACnetNodeType": (
            "D",
            "ns=1;i=3045",
            {"EnumStrings": ("V", "ns=1;i=6044", {})},
        ),
        "BACnetNotifyType": (
            "D",
            "ns=1;i=3002",
            {"EnumStrings": ("V", "ns=1;i=6054", {})},
        ),
        "BACnetObjectCount": ("D", "ns=1;i=3012", {}),
        "BACnetObjectIdentifier": ("D", "ns=1;i=3020", {}),
        "BACnetObjectTypeEnum": (
            "D",
            "ns=1;i=103053",
            {"EnumStrings": ("V", "ns=1;i=106272", {})},
        ),
        "BACnetObjectTypeSupportedBits": (
            "D",
            "ns=1;i=3063",
            {"OptionSetValues": ("V", "ns=1;i=6641", {})},
        ),
        "BACnetPolarity": (
            "D",
            "ns=1;i=3007",
            {"EnumStrings": ("V", "ns=1;i=6097", {})},
        ),
        "BACnetPriorityValue": ("D", "ns=1;i=3053", {}),
        "BACnetProgramError": (
            "D",
            "ns=1;i=3032",
            {"EnumStrings": ("V", "ns=1;i=6154", {})},
        ),
        "BACnetProgramRequest": (
            "D",
            "ns=1;i=3030",
            {"EnumStrings": ("V", "ns=1;i=6151", {})},
        ),
        "BACnetProgramStates": (
            "D",
            "ns=1;i=3031",
            {"EnumStrings": ("V", "ns=1;i=6153", {})},
        ),
        "BACnetPropertyCount": ("D", "ns=1;i=3011", {}),
        "BACnetPropertyIdentifier": (
            "D",
            "ns=1;i=3046",
            {"EnumStrings": ("V", "ns=1;i=6210", {})},
        ),
        "BACnetPropertyStates": ("D", "ns=1;i=3028", {}),
        "BACnetRecipient": ("D", "ns=1;i=3054", {}),
        "BACnetRecipientProcess": ("D", "ns=1;i=103018", {}),
        "BACnetReinitializedStateofDevice": (
            "D",
            "ns=1;i=3049",
            {"EnumStrings": ("V", "ns=1;i=6168", {})},
        ),
        "BACnetReliability": (
            "D",
            "ns=1;i=3001",
            {"EnumValues": ("V", "ns=1;i=106001", {})},
        ),
        "BACnetRestartReason": (
            "D",
            "ns=1;i=103019",
            {"EnumStrings": ("V", "ns=1;i=106127", {})},
        ),
        "BACnetSegmentation": (
            "D",
            "ns=1;i=103011",
            {"EnumStrings": ("V", "ns=1;i=106086", {})},
        ),
        "BACnetServicesSupportedBits": (
            "D",
            "ns=1;i=3064",
            {"OptionSetValues": ("V", "ns=1;i=6647", {})},
        ),
        "BACnetSpecialEvent": ("D", "ns=1;i=103003", {}),
        "BACnetSpecialEventPeriod": ("D", "ns=1;i=3055", {}),
        "BACnetStatusFlags": (
            "D",
            "ns=1;i=3065",
            {"OptionSetValues": ("V", "ns=1;i=6700", {})},
        ),
        "BACnetTime": ("D", "ns=1;i=3019", {}),
        "BACnetTimeStamp": ("D", "ns=1;i=3056", {}),
        "BACnetTimeValue": ("D", "ns=1;i=103004", {}),
        "BACnetTimeValueValue": ("D", "ns=1;i=103010", {}),
        "BACnetWeekNDay": ("D", "ns=1;i=3024", {}),
        "BACnetYear": ("D", "ns=1;i=3015", {}),
    },
    "objects": {
        "<Notifier_Object_Name>": (
            "O",
            "ns=1;i=5036",
            {
                "Object_Identifier": ("V", "ns=1;i=6211", {}),
                "Recipient_List": ("V", "ns=1;i=6206", {}),
            },
        ),
        "Default Binary": ("O", "ns=1;i=105060", {}),
        "Default JSON": ("O", "ns=1;i=5116", {}),
        "Default XML": ("O", "ns=1;i=105061", {}),
        "TypeDictionary": (
            "V",
            "ns=1;i=6158",
            {
                "BACnetAddress": ("V", "ns=1;i=6164", {}),
                "BACnetAddressBinding": ("V", "ns=1;i=6171", {}),
                "BACnetCOVSubscription": ("V", "ns=1;i=6173", {}),
                "BACnetCalendarEntry": ("V", "ns=1;i=6442", {}),
                "BACnetClientCOV": ("V", "ns=1;i=6444", {}),
                "BACnetDailySchedule": ("V", "ns=1;i=6177", {}),
                "BACnetDate": ("V", "ns=1;i=6179", {}),
                "BACnetDateRange": ("V", "ns=1;i=6181", {}),
                "BACnetDateTime": ("V", "ns=1;i=6184", {}),
                "BACnetDaysOfWeek": ("V", "ns=1;i=6427", {}),
                "BACnetDestination": ("V", "ns=1;i=6186", {}),
                "BACnetDeviceObjectPropertyReference": ("V", "ns=1;i=6188", {}),
                "BACnetEventFaultParameterExtended": ("V", "ns=1;i=6190", {}),
                "BACnetEventParameter": ("V", "ns=1;i=6446", {}),
                "BACnetEventParameterBufferReady": ("V", "ns=1;i=6192", {}),
                "BACnetEventParameterChangeOfBitstring": ("V", "ns=1;i=6194", {}),
                "BACnetEventParameterChangeOfCharacterString": ("V", "ns=1;i=6196", {}),
                "BACnetEventParameterChangeOfLifeSafety": ("V", "ns=1;i=6462", {}),
                "BACnetEventParameterChangeOfState": ("V", "ns=1;i=6198", {}),
                "BACnetEventParameterChangeOfValue": ("V", "ns=1;i=6200", {}),
                "BACnetEventParameterCommandFailure": ("V", "ns=1;i=6203", {}),
                "BACnetEventParameterDoubleOutOfRange": ("V", "ns=1;i=6205", {}),
                "BACnetEventParameterExtendedParameters": ("V", "ns=1;i=6448", {}),
                "BACnetEventParameterFloatingLimit": ("V", "ns=1;i=6212", {}),
                "BACnetEventParameterOutOfRange": ("V", "ns=1;i=6250", {}),
                "BACnetEventParameterSignedOutOfRange": ("V", "ns=1;i=6257", {}),
                "BACnetEventParameterUnsignedOutOfRange": ("V", "ns=1;i=6341", {}),
                "BACnetEventParameterUnsignedRange": ("V", "ns=1;i=6400", {}),
                "BACnetEventTransitionBits": ("V", "ns=1;i=6429", {}),
                "BACnetFaultParameter": ("V", "ns=1;i=6450", {}),
                "BACnetFaultParameterFaultCharacterstring": ("V", "ns=1;i=6402", {}),
                "BACnetFaultParameterFaultLifeSafety": ("V", "ns=1;i=6404", {}),
                "BACnetFaultParameterFaultState": ("V", "ns=1;i=6406", {}),
                "BACnetFaultParameterFaultStatusFlags": ("V", "ns=1;i=6408", {}),
                "BACnetLimitEnable": ("V", "ns=1;i=6431", {}),
                "BACnetMessageClass": ("V", "ns=1;i=6452", {}),
                "BACnetObjectTypeSupportedBits": ("V", "ns=1;i=6433", {}),
                "BACnetPriorityValue": ("V", "ns=1;i=6454", {}),
                "BACnetPropertyStates": ("V", "ns=1;i=6411", {}),
                "BACnetRecipient": ("V", "ns=1;i=6456", {}),
                "BACnetRecipientProcess": ("V", "ns=1;i=6413", {}),
                "BACnetServicesSupportedBits": ("V", "ns=1;i=6436", {}),
                "BACnetSpecialEvent": ("V", "ns=1;i=6417", {}),
                "BACnetSpecialEventPeriod": ("V", "ns=1;i=6458", {}),
                "BACnetStatusFlags": ("V", "ns=1;i=6438", {}),
                "BACnetTime": ("V", "ns=1;i=6419", {}),
                "BACnetTimeStamp": ("V", "ns=1;i=6460", {}),
                "BACnetTimeValue": ("V", "ns=1;i=6421", {}),
                "BACnetTimeValueValue": ("V", "ns=1;i=6423", {}),
                "BACnetWeekNDay": ("V", "ns=1;i=6425", {}),
                "NamespaceUri": ("V", "ns=1;i=6162", {}),
            },
        ),
        "http://opcfoundation.org/UA/BACnet_V2/": (
            "O",
            "ns=1;i=5004",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6390", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6391", {}),
                "NamespaceUri": ("V", "ns=1;i=6392", {}),
                "NamespaceVersion": ("V", "ns=1;i=6393", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6394", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6395", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6396", {}),
            },
        ),
    },
    "objtypes": {
        "BACnetBackupRestoreType": (
            "OT",
            "ns=1;i=101020",
            {
                "BACnetBackup": ("M", "ns=1;i=107004", {}),
                "BACnetRestore": ("M", "ns=1;i=107005", {}),
                "Backup_And_Restore_State": ("V", "ns=1;i=106251", {}),
                "Backup_Failure_Timeout": ("V", "ns=1;i=106132", {}),
                "Backup_Preparation_Time": ("V", "ns=1;i=106133", {}),
                "Configuration_Files": ("V", "ns=1;i=106101", {}),
                "Last_Restore_Time": ("V", "ns=1;i=106131", {}),
                "Restore_Completion_Time": ("V", "ns=1;i=106250", {}),
                "Restore_Preparation_Time": ("V", "ns=1;i=106134", {}),
            },
        ),
        "BACnetChangeOfStateCountType": (
            "OT",
            "ns=1;i=1016",
            {
                "Change_Of_State_Count": ("V", "ns=1;i=6035", {}),
                "Change_Of_State_Time": ("V", "ns=1;i=6034", {}),
                "Reset": ("M", "ns=1;i=7001", {}),
                "Time_Of_State_Count_Reset": ("V", "ns=1;i=6041", {}),
            },
        ),
        "BACnetDeviceRestartType": (
            "OT",
            "ns=1;i=101022",
            {
                "AddRestartRecipients": (
                    "M",
                    "ns=1;i=107006",
                    {
                        "InputArguments": ("V", "ns=1;i=6108", {}),
                        "OutputArguments": ("V", "ns=1;i=6137", {}),
                    },
                ),
                "Last_Restart_Reason": ("V", "ns=1;i=106104", {}),
                "RemoveRestartRecipients": (
                    "M",
                    "ns=1;i=107007",
                    {
                        "InputArguments": ("V", "ns=1;i=6147", {}),
                        "OutputArguments": ("V", "ns=1;i=6141", {}),
                    },
                ),
                "Restart_Notification_Recipients": ("V", "ns=1;i=106117", {}),
                "Time_Of_Device_Restart": ("V", "ns=1;i=106105", {}),
            },
        ),
        "BACnetElapsedActiveTimeType": (
            "OT",
            "ns=1;i=1017",
            {
                "Elapsed_Active_Time": ("V", "ns=1;i=6042", {}),
                "Reset": ("M", "ns=1;i=7003", {}),
                "Time_Of_Active_Time_Reset": ("V", "ns=1;i=6043", {}),
            },
        ),
        "BACnetEventAlgorithmType": (
            "OT",
            "ns=1;i=1026",
            {
                "BACnetBufferReadyAlgorithmType": (
                    "OT",
                    "ns=1;i=101005",
                    {
                        "PreviousCount": ("V", "ns=1;i=106051", {}),
                        "Threshold": ("V", "ns=1;i=106052", {}),
                    },
                ),
                "BACnetChangeOfBitStringAlgorithmType": (
                    "OT",
                    "ns=1;i=101003",
                    {"AlarmValues": ("V", "ns=1;i=106043", {})},
                ),
                "BACnetChangeOfCharacterStringAlgorithmType": (
                    "OT",
                    "ns=1;i=101034",
                    {"AlarmValues": ("V", "ns=1;i=6373", {})},
                ),
                "BACnetChangeOfLifeSafetyAlgorithmType": (
                    "OT",
                    "ns=1;i=101028",
                    {
                        "AlarmValues": ("V", "ns=1;i=106311", {}),
                        "LifeSafetyAlarmValues": ("V", "ns=1;i=106312", {}),
                    },
                ),
                "BACnetChangeOfStateAlgorithmType": (
                    "OT",
                    "ns=1;i=1010",
                    {"AlarmValues": ("V", "ns=1;i=6016", {})},
                ),
                "BACnetChangeOfStatusFlagsAlgorithmType": (
                    "OT",
                    "ns=1;i=101030",
                    {"SelectedFlags": ("V", "ns=1;i=6364", {})},
                ),
                "BACnetChangeOfValueAlgorithmType": (
                    "OT",
                    "ns=1;i=101004",
                    {
                        "Bitmask": ("V", "ns=1;i=106049", {}),
                        "Increment": ("V", "ns=1;i=106048", {}),
                    },
                ),
                "BACnetCommandFailureAlgorithmType": (
                    "OT",
                    "ns=1;i=1029",
                    {"FeedbackValueRef": ("V", "ns=1;i=6017", {})},
                ),
                "BACnetDoubleOutOfRangeAlgorithmType": (
                    "OT",
                    "ns=1;i=101031",
                    {
                        "Deadband": ("V", "ns=1;i=6022", {}),
                        "HighLimit": ("V", "ns=1;i=6249", {}),
                        "LimitEnable": ("V", "ns=1;i=6345", {}),
                        "LowLimit": ("V", "ns=1;i=6399", {}),
                    },
                ),
                "BACnetFloatingLimitAlgorithmType": (
                    "OT",
                    "ns=1;i=101002",
                    {
                        "Deadband": ("V", "ns=1;i=106326", {}),
                        "HighDiffLimit": ("V", "ns=1;i=106325", {}),
                        "LowDiffLimit": ("V", "ns=1;i=106045", {}),
                        "SetpointReference": ("V", "ns=1;i=106046", {}),
                    },
                ),
                "BACnetOutOfRangeAlgorithmType": (
                    "OT",
                    "ns=1;i=1009",
                    {
                        "Deadband": ("V", "ns=1;i=6049", {}),
                        "HighLimit": ("V", "ns=1;i=6047", {}),
                        "LimitEnable": ("V", "ns=1;i=6051", {}),
                        "LowLimit": ("V", "ns=1;i=6048", {}),
                    },
                ),
                "BACnetSignedOutOfRangeAlgorithmType": (
                    "OT",
                    "ns=1;i=101032",
                    {
                        "Deadband": ("V", "ns=1;i=6365", {}),
                        "HighLimit": ("V", "ns=1;i=6366", {}),
                        "LimitEnable": ("V", "ns=1;i=6367", {}),
                        "LowLimit": ("V", "ns=1;i=6368", {}),
                    },
                ),
                "BACnetUnsignedOutOfRangeAlgorithmType": (
                    "OT",
                    "ns=1;i=101033",
                    {
                        "Deadband": ("V", "ns=1;i=6369", {}),
                        "HighLimit": ("V", "ns=1;i=6370", {}),
                        "LimitEnable": ("V", "ns=1;i=6371", {}),
                        "LowLimit": ("V", "ns=1;i=6372", {}),
                    },
                ),
                "BACnetUnsignedRangeAlgorithmType": (
                    "OT",
                    "ns=1;i=101029",
                    {
                        "HighLimit": ("V", "ns=1;i=6362", {}),
                        "LowLimit": ("V", "ns=1;i=6363", {}),
                    },
                ),
                "TimeDelay": ("V", "ns=1;i=6415", {}),
                "TimeDelayNormal": ("V", "ns=1;i=6416", {}),
            },
        ),
        "BACnetEventReportingType": (
            "OT",
            "ns=1;i=1003",
            {
                "Acked_Transitions": ("V", "ns=1;i=6053", {}),
                "BACnetIntrinsicReportingTrendLogType": (
                    "OT",
                    "ns=1;i=101016",
                    {"Recorded_Since_Notification": ("V", "ns=1;i=106232", {})},
                ),
                "EventAlgorithm": (
                    "O",
                    "ns=1;i=5026",
                    {
                        "TimeDelay": ("V", "ns=1;i=6440", {}),
                        "TimeDelayNormal": ("V", "ns=1;i=6441", {}),
                    },
                ),
                "Event_Algorithm_Inhibit": ("V", "ns=1;i=106304", {}),
                "Event_Algorithm_Inhibit_Ref": ("V", "ns=1;i=106303", {}),
                "Event_Detection_Enable": ("V", "ns=1;i=106302", {}),
                "Event_Enable": ("V", "ns=1;i=6052", {}),
                "Event_Message_Texts": ("V", "ns=1;i=6064", {}),
                "Event_Message_Texts_Config": ("V", "ns=1;i=106063", {}),
                "Event_State": ("V", "ns=1;i=6007", {}),
                "Event_Time_Stamps": ("V", "ns=1;i=6059", {}),
                "Notification_Class": ("V", "ns=1;i=6050", {}),
                "Notify_Type": ("V", "ns=1;i=6091", {}),
            },
        ),
        "BACnetFaultAlgorithmType": (
            "OT",
            "ns=1;i=101025",
            {
                "BACnetFaultCharacterStringAlgorithmType": (
                    "OT",
                    "ns=1;i=101009",
                    {"FaultValues": ("V", "ns=1;i=106168", {})},
                ),
                "BACnetFaultStateAlgorithmType": (
                    "OT",
                    "ns=1;i=101011",
                    {"FaultValues": ("V", "ns=1;i=106172", {})},
                ),
                "BACnetFaultStatusFlagsAlgorithmType": ("OT", "ns=1;i=101012", {}),
            },
        ),
        "BACnetFaultEvaluationType": (
            "OT",
            "ns=1;i=1025",
            {
                "FaultAlgorithm": (
                    "O",
                    "ns=1;i=105096",
                    {"Object_Identifier": ("V", "ns=1;i=106329", {})},
                ),
                "Reliability": ("V", "ns=1;i=6304", {}),
                "Reliability_Evaluation_Inhibit": ("V", "ns=1;i=6305", {}),
            },
        ),
        "BACnetInternetworkType": (
            "OT",
            "ns=1;i=1030",
            {
                "<BACnetDeviceName>": (
                    "O",
                    "ns=1;i=5040",
                    {
                        "APDU_Timeout": ("V", "ns=1;i=6225", {}),
                        "Application_Software_Version": ("V", "ns=1;i=6221", {}),
                        "Database_Revision": ("V", "ns=1;i=6229", {}),
                        "Device_Address_Binding": ("V", "ns=1;i=6228", {}),
                        "Firmware_Revision": ("V", "ns=1;i=6220", {}),
                        "Max_APDU_Length_Accepted": ("V", "ns=1;i=6224", {}),
                        "Model_Name": ("V", "ns=1;i=6217", {}),
                        "Number_Of_APDU_Retries": ("V", "ns=1;i=6226", {}),
                        "Object_Identifier": ("V", "ns=1;i=6028", {}),
                        "Object_List": (
                            "O",
                            "ns=1;i=105095",
                            {
                                "<BACnetObjectName>": (
                                    "O",
                                    "ns=1;i=5038",
                                    {"Object_Identifier": ("V", "ns=1;i=6232", {})},
                                ),
                                "Object_List": ("V", "ns=1;i=6233", {}),
                            },
                        ),
                        "Protocol_Object_Types_Supported": ("V", "ns=1;i=6397", {}),
                        "Protocol_Revision": ("V", "ns=1;i=6219", {}),
                        "Protocol_Services_Supported": ("V", "ns=1;i=6227", {}),
                        "Protocol_Version": ("V", "ns=1;i=6218", {}),
                        "Segmentation_Supported": ("V", "ns=1;i=6223", {}),
                        "Serial_Number": ("V", "ns=1;i=6214", {}),
                        "System_Status": ("V", "ns=1;i=6244", {}),
                        "Vendor_Identifier": ("V", "ns=1;i=6216", {}),
                        "Vendor_Name": ("V", "ns=1;i=6215", {}),
                    },
                ),
                "AddDeviceByAddress": (
                    "M",
                    "ns=1;i=7012",
                    {"InputArguments": ("V", "ns=1;i=6252", {})},
                ),
                "AddDeviceById": (
                    "M",
                    "ns=1;i=7011",
                    {"InputArguments": ("V", "ns=1;i=6248", {})},
                ),
                "GetDeviceIdList": (
                    "M",
                    "ns=1;i=7010",
                    {"OutputArguments": ("V", "ns=1;i=6247", {})},
                ),
                "NetworkScan": (
                    "M",
                    "ns=1;i=7023",
                    {
                        "InputArguments": ("V", "ns=1;i=6660", {}),
                        "OutputArguments": ("V", "ns=1;i=6661", {}),
                    },
                ),
                "TimeSynchronization": (
                    "M",
                    "ns=1;i=7021",
                    {"InputArguments": ("V", "ns=1;i=6662", {})},
                ),
                "TranslateBACnetIds": (
                    "M",
                    "ns=1;i=7009",
                    {
                        "InputArguments": ("V", "ns=1;i=6245", {}),
                        "OutputArguments": ("V", "ns=1;i=6246", {}),
                    },
                ),
            },
        ),
        "BACnetMstpMasterType": (
            "OT",
            "ns=1;i=101021",
            {
                "Auto_Slave_Discovery": ("V", "ns=1;i=106114", {}),
                "Manual_Slave_Address_Binding": ("V", "ns=1;i=106113", {}),
                "Max_Info_Frames": ("V", "ns=1;i=106111", {}),
                "Max_Master": ("V", "ns=1;i=106110", {}),
                "Slave_Address_Binding": ("V", "ns=1;i=106115", {}),
                "Slave_Proxy_Enable": ("V", "ns=1;i=106112", {}),
            },
        ),
        "BACnetNotificationType": (
            "OT",
            "ns=1;i=1001",
            {
                "BACnetEventNotificationType": (
                    "OT",
                    "ns=1;i=1028",
                    {
                        "BACnetBufferReadyNotificationType": (
                            "OT",
                            "ns=1;i=1042",
                            {
                                "BufferProperty": ("V", "ns=1;i=6085", {}),
                                "CurrentNotification": ("V", "ns=1;i=6098", {}),
                                "PreviousNotification": ("V", "ns=1;i=6093", {}),
                            },
                        ),
                        "BACnetChangeOfBitStringNotificationType": (
                            "OT",
                            "ns=1;i=1037",
                            {
                                "ReferencedBitString": ("V", "ns=1;i=6018", {}),
                                "StatusFlags": ("V", "ns=1;i=6026", {}),
                            },
                        ),
                        "BACnetChangeOfCharacterStringNotificationType": (
                            "OT",
                            "ns=1;i=1047",
                            {
                                "AlarmValue": ("V", "ns=1;i=6156", {}),
                                "ChangedValue": ("V", "ns=1;i=6146", {}),
                                "StatusFlags": ("V", "ns=1;i=6157", {}),
                            },
                        ),
                        "BACnetChangeOfRealValueNotificationType": (
                            "OT",
                            "ns=1;i=1039",
                            {
                                "NewValue": ("V", "ns=1;i=6031", {}),
                                "StatusFlags": ("V", "ns=1;i=6039", {}),
                            },
                        ),
                        "BACnetChangeOfStateNotificationType": (
                            "OT",
                            "ns=1;i=1038",
                            {
                                "NewState": ("V", "ns=1;i=6029", {}),
                                "StatusFlags": ("V", "ns=1;i=6030", {}),
                            },
                        ),
                        "BACnetChangeOfValueNotificationType": (
                            "OT",
                            "ns=1;i=1053",
                            {
                                "NewValue": ("V", "ns=1;i=6209", {}),
                                "StatusFlags": ("V", "ns=1;i=6398", {}),
                            },
                        ),
                        "BACnetCommandFailureNotificationType": (
                            "OT",
                            "ns=1;i=1040",
                            {
                                "CommandValue": ("V", "ns=1;i=6040", {}),
                                "FeedbackValue": ("V", "ns=1;i=6046", {}),
                                "StatusFlags": ("V", "ns=1;i=6058", {}),
                            },
                        ),
                        "BACnetDoubleOutOfRangeNotificationType": (
                            "OT",
                            "ns=1;i=1044",
                            {
                                "Deadband": ("V", "ns=1;i=6104", {}),
                                "ExceedingLimit": ("V", "ns=1;i=6112", {}),
                                "ExceedingValue": ("V", "ns=1;i=6103", {}),
                                "StatusFlags": ("V", "ns=1;i=6113", {}),
                            },
                        ),
                        "BACnetFloatingLimitNotificationType": (
                            "OT",
                            "ns=1;i=1041",
                            {
                                "ErrorLimit": ("V", "ns=1;i=6062", {}),
                                "ReferenceValue": ("V", "ns=1;i=6060", {}),
                                "SetpointValue": ("V", "ns=1;i=6061", {}),
                                "StatusFlags": ("V", "ns=1;i=6063", {}),
                            },
                        ),
                        "BACnetOutOfRangeNotificationType": (
                            "OT",
                            "ns=1;i=1031",
                            {
                                "Deadband": ("V", "ns=1;i=6012", {}),
                                "ExceedingLimit": ("V", "ns=1;i=6013", {}),
                                "ExceedingValue": ("V", "ns=1;i=6004", {}),
                                "StatusFlags": ("V", "ns=1;i=6014", {}),
                            },
                        ),
                        "BACnetSignedOutOfRangeNotificationType": (
                            "OT",
                            "ns=1;i=1045",
                            {
                                "Deadband": ("V", "ns=1;i=6115", {}),
                                "ExceedingLimit": ("V", "ns=1;i=6129", {}),
                                "ExceedingValue": ("V", "ns=1;i=6114", {}),
                                "StatusFlags": ("V", "ns=1;i=6138", {}),
                            },
                        ),
                        "BACnetUnsignedOutOfRangeNotificationType": (
                            "OT",
                            "ns=1;i=1046",
                            {
                                "Deadband": ("V", "ns=1;i=6143", {}),
                                "ExceedingLimit": ("V", "ns=1;i=6144", {}),
                                "ExceedingValue": ("V", "ns=1;i=6140", {}),
                                "StatusFlags": ("V", "ns=1;i=6145", {}),
                            },
                        ),
                        "BACnetUnsignedRangeNotificationType": (
                            "OT",
                            "ns=1;i=1043",
                            {
                                "ExceedingLimit": ("V", "ns=1;i=6100", {}),
                                "ExceedingValue": ("V", "ns=1;i=6099", {}),
                                "StatusFlags": ("V", "ns=1;i=6101", {}),
                            },
                        ),
                        "Event_Values": ("V", "ns=1;i=6136", {}),
                    },
                ),
                "BACnetFaultNotificationType": (
                    "OT",
                    "ns=1;i=1027",
                    {
                        "BACnetChangeOfReliabilityNotificationType": (
                            "OT",
                            "ns=1;i=1036",
                            {"PropertyValues": ("V", "ns=1;i=6208", {})},
                        ),
                        "BACnetEventEnrollmentNotificationType": (
                            "OT",
                            "ns=1;i=1035",
                            {},
                        ),
                        "BACnetFeedbackNotificationType": ("OT", "ns=1;i=1034", {}),
                        "BACnetLoopNotificationType": ("OT", "ns=1;i=1033", {}),
                        "BACnetSimpleNotificationType": ("OT", "ns=1;i=1032", {}),
                        "Reliability": ("V", "ns=1;i=6134", {}),
                        "Status_Flags": ("V", "ns=1;i=6015", {}),
                    },
                ),
                "From_State": ("V", "ns=1;i=6322", {}),
                "Notification_Class": ("V", "ns=1;i=6132", {}),
                "Notify_Type": ("V", "ns=1;i=6133", {}),
                "To_State": ("V", "ns=1;i=6698", {}),
            },
        ),
        "BACnetObjectType": (
            "OT",
            "ns=1;i=1002",
            {
                "BACnetAnalogType": (
                    "OT",
                    "ns=1;i=1004",
                    {
                        "BACnetAnalogInputType": (
                            "OT",
                            "ns=1;i=1005",
                            {"Device_Type": ("V", "ns=1;i=6037", {})},
                        ),
                        "BACnetAnalogOutputType": (
                            "OT",
                            "ns=1;i=1006",
                            {
                                "Device_Type": ("V", "ns=1;i=6045", {}),
                                "Priority_Array": ("V", "ns=1;i=6070", {}),
                                "Relinquish_Default": ("V", "ns=1;i=6086", {}),
                            },
                        ),
                        "BACnetAnalogValueType": (
                            "OT",
                            "ns=1;i=1007",
                            {
                                "Priority_Array": ("V", "ns=1;i=6071", {}),
                                "Relinquish_Default": ("V", "ns=1;i=6087", {}),
                            },
                        ),
                        "COV_Increment": ("V", "ns=1;i=6068", {}),
                        "EventReporting": (
                            "O",
                            "ns=1;i=5001",
                            {
                                "Acked_Transitions": ("V", "ns=1;i=6005", {}),
                                "EventAlgorithm": (
                                    "O",
                                    "ns=1;i=105068",
                                    {
                                        "Deadband": ("V", "ns=1;i=106257", {}),
                                        "HighLimit": ("V", "ns=1;i=106258", {}),
                                        "LimitEnable": ("V", "ns=1;i=106259", {}),
                                        "LowLimit": ("V", "ns=1;i=106260", {}),
                                        "TimeDelay": ("V", "ns=1;i=6650", {}),
                                        "TimeDelayNormal": ("V", "ns=1;i=6651", {}),
                                    },
                                ),
                                "Event_Algorithm_Inhibit": ("V", "ns=1;i=6036", {}),
                                "Event_Algorithm_Inhibit_Ref": ("V", "ns=1;i=6275", {}),
                                "Event_Detection_Enable": ("V", "ns=1;i=6276", {}),
                                "Event_Enable": ("V", "ns=1;i=6006", {}),
                                "Event_Message_Texts": ("V", "ns=1;i=6277", {}),
                                "Event_Message_Texts_Config": ("V", "ns=1;i=6278", {}),
                                "Event_State": ("V", "ns=1;i=6056", {}),
                                "Event_Time_Stamps": ("V", "ns=1;i=6009", {}),
                                "Notification_Class": ("V", "ns=1;i=6010", {}),
                                "Notify_Type": ("V", "ns=1;i=6011", {}),
                            },
                        ),
                        "FaultEvaluation": (
                            "O",
                            "ns=1;i=105097",
                            {
                                "FaultAlgorithm": (
                                    "O",
                                    "ns=1;i=5071",
                                    {"Object_Identifier": ("V", "ns=1;i=6379", {})},
                                ),
                                "Reliability": ("V", "ns=1;i=6380", {}),
                            },
                        ),
                        "Out_Of_Service": ("V", "ns=1;i=6038", {}),
                        "Present_Value": (
                            "V",
                            "ns=1;i=6002",
                            {"EngineeringUnits": ("V", "ns=1;i=6003", {})},
                        ),
                        "Resolution": ("V", "ns=1;i=6409", {}),
                        "Status_Flags": ("V", "ns=1;i=6024", {}),
                    },
                ),
                "BACnetBinaryType": (
                    "OT",
                    "ns=1;i=1012",
                    {
                        "BACnetBinaryInputType": (
                            "OT",
                            "ns=1;i=1013",
                            {
                                "Device_Type": ("V", "ns=1;i=6032", {}),
                                "EventReporting": (
                                    "O",
                                    "ns=1;i=5072",
                                    {
                                        "Acked_Transitions": ("V", "ns=1;i=6279", {}),
                                        "EventAlgorithm": (
                                            "O",
                                            "ns=1;i=5137",
                                            {
                                                "AlarmValues": ("V", "ns=1;i=6434", {}),
                                                "TimeDelay": ("V", "ns=1;i=6663", {}),
                                                "TimeDelayNormal": (
                                                    "V",
                                                    "ns=1;i=6664",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Event_Enable": ("V", "ns=1;i=6280", {}),
                                        "Event_State": ("V", "ns=1;i=6281", {}),
                                        "Event_Time_Stamps": ("V", "ns=1;i=6282", {}),
                                        "Notification_Class": ("V", "ns=1;i=6283", {}),
                                        "Notify_Type": ("V", "ns=1;i=6284", {}),
                                    },
                                ),
                                "Polarity": ("V", "ns=1;i=6096", {}),
                            },
                        ),
                        "BACnetBinaryOutputType": (
                            "OT",
                            "ns=1;i=1014",
                            {
                                "Device_Type": ("V", "ns=1;i=6033", {}),
                                "EventReporting": (
                                    "O",
                                    "ns=1;i=5073",
                                    {
                                        "Acked_Transitions": ("V", "ns=1;i=6285", {}),
                                        "EventAlgorithm": (
                                            "O",
                                            "ns=1;i=5138",
                                            {
                                                "FeedbackValueRef": (
                                                    "V",
                                                    "ns=1;i=6665",
                                                    {},
                                                ),
                                                "TimeDelay": ("V", "ns=1;i=6666", {}),
                                                "TimeDelayNormal": (
                                                    "V",
                                                    "ns=1;i=6667",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Event_Enable": ("V", "ns=1;i=6286", {}),
                                        "Event_State": ("V", "ns=1;i=6287", {}),
                                        "Event_Time_Stamps": ("V", "ns=1;i=6288", {}),
                                        "Notification_Class": ("V", "ns=1;i=6289", {}),
                                        "Notify_Type": ("V", "ns=1;i=6290", {}),
                                    },
                                ),
                                "Feedback_Value": ("V", "ns=1;i=6291", {}),
                                "Minimum_Off_Time": ("V", "ns=1;i=6089", {}),
                                "Minimum_On_Time": ("V", "ns=1;i=6090", {}),
                                "Polarity": ("V", "ns=1;i=6102", {}),
                                "Priority_Array": ("V", "ns=1;i=6088", {}),
                                "Relinquish_Default": ("V", "ns=1;i=106146", {}),
                            },
                        ),
                        "BACnetBinaryValueType": (
                            "OT",
                            "ns=1;i=1015",
                            {
                                "EventReporting": (
                                    "O",
                                    "ns=1;i=5074",
                                    {
                                        "Acked_Transitions": ("V", "ns=1;i=6292", {}),
                                        "EventAlgorithm": (
                                            "O",
                                            "ns=1;i=5139",
                                            {
                                                "AlarmValues": ("V", "ns=1;i=6668", {}),
                                                "TimeDelay": ("V", "ns=1;i=6669", {}),
                                                "TimeDelayNormal": (
                                                    "V",
                                                    "ns=1;i=6670",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Event_Enable": ("V", "ns=1;i=6293", {}),
                                        "Event_State": ("V", "ns=1;i=6294", {}),
                                        "Event_Time_Stamps": ("V", "ns=1;i=6295", {}),
                                        "Notification_Class": ("V", "ns=1;i=6296", {}),
                                        "Notify_Type": ("V", "ns=1;i=6297", {}),
                                    },
                                ),
                                "Minimum_Off_Time": ("V", "ns=1;i=6095", {}),
                                "Minimum_On_Time": ("V", "ns=1;i=6094", {}),
                                "Priority_Array": ("V", "ns=1;i=6092", {}),
                                "Relinquish_Default": ("V", "ns=1;i=106149", {}),
                            },
                        ),
                        "ChangeOfState": (
                            "O",
                            "ns=1;i=5007",
                            {
                                "Change_Of_State_Count": ("V", "ns=1;i=6065", {}),
                                "Change_Of_State_Time": ("V", "ns=1;i=6066", {}),
                                "Reset": ("M", "ns=1;i=7002", {}),
                                "Time_Of_State_Count_Reset": ("V", "ns=1;i=6067", {}),
                            },
                        ),
                        "ElapsedActiveTime": (
                            "O",
                            "ns=1;i=5008",
                            {
                                "Elapsed_Active_Time": ("V", "ns=1;i=6074", {}),
                                "Reset": ("M", "ns=1;i=7004", {}),
                                "Time_Of_Active_Time_Reset": ("V", "ns=1;i=6075", {}),
                            },
                        ),
                        "EventReporting": (
                            "O",
                            "ns=1;i=105092",
                            {
                                "Acked_Transitions": ("V", "ns=1;i=106264", {}),
                                "Event_Enable": ("V", "ns=1;i=106265", {}),
                                "Event_State": ("V", "ns=1;i=6360", {}),
                                "Event_Time_Stamps": ("V", "ns=1;i=106267", {}),
                                "Notification_Class": ("V", "ns=1;i=106268", {}),
                                "Notify_Type": ("V", "ns=1;i=106269", {}),
                            },
                        ),
                        "FaultEvaluation": (
                            "O",
                            "ns=1;i=105098",
                            {"Reliability": ("V", "ns=1;i=6381", {})},
                        ),
                        "Out_Of_Service": ("V", "ns=1;i=6023", {}),
                        "Present_Value": (
                            "V",
                            "ns=1;i=6019",
                            {
                                "FalseState": ("V", "ns=1;i=6020", {}),
                                "TrueState": ("V", "ns=1;i=6021", {}),
                            },
                        ),
                        "Status_Flags": ("V", "ns=1;i=6111", {}),
                    },
                ),
                "BACnetCalendarType": (
                    "OT",
                    "ns=1;i=1008",
                    {
                        "AddDateListElements": (
                            "M",
                            "ns=1;i=7005",
                            {
                                "InputArguments": ("V", "ns=1;i=6083", {}),
                                "OutputArguments": ("V", "ns=1;i=106294", {}),
                            },
                        ),
                        "Date_List": ("V", "ns=1;i=6076", {}),
                        "Present_Value": ("V", "ns=1;i=6073", {}),
                        "RemoveDateListElements": (
                            "M",
                            "ns=1;i=7006",
                            {
                                "InputArguments": ("V", "ns=1;i=6084", {}),
                                "OutputArguments": ("V", "ns=1;i=106295", {}),
                            },
                        ),
                    },
                ),
                "BACnetDeviceType": (
                    "OT",
                    "ns=1;i=1011",
                    {
                        "APDU_Segment_Timeout": ("V", "ns=1;i=106098", {}),
                        "APDU_Timeout": ("V", "ns=1;i=106099", {}),
                        "Active_COV_Subscriptions": ("V", "ns=1;i=106122", {}),
                        "AddDeviceAddressBindings": (
                            "M",
                            "ns=1;i=7024",
                            {
                                "InputArguments": ("V", "ns=1;i=6271", {}),
                                "OutputArguments": ("V", "ns=1;i=6272", {}),
                            },
                        ),
                        "Application_Software_Version": ("V", "ns=1;i=106078", {}),
                        "BackupRestore": (
                            "O",
                            "ns=1;i=105086",
                            {
                                "BACnetBackup": ("M", "ns=1;i=107008", {}),
                                "BACnetRestore": ("M", "ns=1;i=107009", {}),
                                "Backup_And_Restore_State": ("V", "ns=1;i=106082", {}),
                                "Backup_Failure_Timeout": ("V", "ns=1;i=6253", {}),
                                "Backup_Preparation_Time": ("V", "ns=1;i=6259", {}),
                                "Configuration_Files": ("V", "ns=1;i=106123", {}),
                                "Last_Restore_Time": ("V", "ns=1;i=106124", {}),
                                "Restore_Completion_Time": ("V", "ns=1;i=6261", {}),
                                "Restore_Preparation_Time": ("V", "ns=1;i=6260", {}),
                            },
                        ),
                        "CreateObject": (
                            "M",
                            "ns=1;i=7013",
                            {"InputArguments": ("V", "ns=1;i=6254", {})},
                        ),
                        "Database_Revision": ("V", "ns=1;i=106109", {}),
                        "DeleteObject": (
                            "M",
                            "ns=1;i=7014",
                            {"InputArguments": ("V", "ns=1;i=6256", {})},
                        ),
                        "DeviceCommunicationControl": (
                            "M",
                            "ns=1;i=7015",
                            {"InputArguments": ("V", "ns=1;i=6266", {})},
                        ),
                        "DeviceRestart": (
                            "O",
                            "ns=1;i=105088",
                            {
                                "AddRestartRecipients": (
                                    "M",
                                    "ns=1;i=107010",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6110", {}),
                                        "OutputArguments": ("V", "ns=1;i=6139", {}),
                                    },
                                ),
                                "Last_Restart_Reason": ("V", "ns=1;i=106128", {}),
                                "RemoveRestartRecipients": (
                                    "M",
                                    "ns=1;i=107011",
                                    {
                                        "InputArguments": ("V", "ns=1;i=6148", {}),
                                        "OutputArguments": ("V", "ns=1;i=6142", {}),
                                    },
                                ),
                                "Restart_Notification_Recipients": (
                                    "V",
                                    "ns=1;i=106129",
                                    {},
                                ),
                                "Time_Of_Device_Restart": ("V", "ns=1;i=106130", {}),
                            },
                        ),
                        "Device_Address_Binding": ("V", "ns=1;i=106108", {}),
                        "Firmware_Revision": ("V", "ns=1;i=106077", {}),
                        "Location": ("V", "ns=1;i=106072", {}),
                        "Max_APDU_Length_Accepted": ("V", "ns=1;i=106087", {}),
                        "Max_Segments_Accepted": ("V", "ns=1;i=106088", {}),
                        "Model_Name": ("V", "ns=1;i=106071", {}),
                        "MstpMaster": (
                            "O",
                            "ns=1;i=105087",
                            {
                                "Auto_Slave_Discovery": ("V", "ns=1;i=6262", {}),
                                "Manual_Slave_Address_Binding": (
                                    "V",
                                    "ns=1;i=6263",
                                    {},
                                ),
                                "Max_Info_Frames": ("V", "ns=1;i=106125", {}),
                                "Max_Master": ("V", "ns=1;i=106126", {}),
                                "Slave_Address_Binding": ("V", "ns=1;i=6264", {}),
                                "Slave_Proxy_Enable": ("V", "ns=1;i=6265", {}),
                            },
                        ),
                        "Number_Of_APDU_Retries": ("V", "ns=1;i=106100", {}),
                        "Object_List": (
                            "O",
                            "ns=1;i=105084",
                            {
                                "<BACnetObjectName>": (
                                    "O",
                                    "ns=1;i=5037",
                                    {"Object_Identifier": ("V", "ns=1;i=6231", {})},
                                ),
                                "Object_List": ("V", "ns=1;i=6230", {}),
                            },
                        ),
                        "Protocol_Object_Types_Supported": ("V", "ns=1;i=6222", {}),
                        "Protocol_Revision": ("V", "ns=1;i=106074", {}),
                        "Protocol_Services_Supported": ("V", "ns=1;i=6213", {}),
                        "Protocol_Version": ("V", "ns=1;i=106073", {}),
                        "ReinitializeDevice": (
                            "M",
                            "ns=1;i=7016",
                            {"InputArguments": ("V", "ns=1;i=6255", {})},
                        ),
                        "RemoveDeviceAddressBindings": (
                            "M",
                            "ns=1;i=7025",
                            {
                                "InputArguments": ("V", "ns=1;i=6273", {}),
                                "OutputArguments": ("V", "ns=1;i=6274", {}),
                            },
                        ),
                        "Segmentation_Supported": ("V", "ns=1;i=106085", {}),
                        "Serial_Number": ("V", "ns=1;i=106044", {}),
                        "Structured_Object_List": (
                            "O",
                            "ns=1;i=105094",
                            {
                                "<BACnetStructuredViewName>": (
                                    "O",
                                    "ns=1;i=5039",
                                    {
                                        "Node_Type": ("V", "ns=1;i=6079", {}),
                                        "Object_Identifier": ("V", "ns=1;i=6239", {}),
                                        "Subordinate_List": ("V", "ns=1;i=6080", {}),
                                    },
                                ),
                                "Structured_Object_List": ("V", "ns=1;i=6235", {}),
                            },
                        ),
                        "System_Status": ("V", "ns=1;i=106068", {}),
                        "TextMessage": (
                            "M",
                            "ns=1;i=7019",
                            {"InputArguments": ("V", "ns=1;i=6267", {})},
                        ),
                        "TimeManagement": (
                            "O",
                            "ns=1;i=105085",
                            {
                                "Daylight_Savings_Status": ("V", "ns=1;i=6243", {}),
                                "Local_Date": ("V", "ns=1;i=6240", {}),
                                "Local_Time": ("V", "ns=1;i=6241", {}),
                                "TimeSynchronization": (
                                    "M",
                                    "ns=1;i=7026",
                                    {"InputArguments": ("V", "ns=1;i=6347", {})},
                                ),
                                "UTC_Offse": ("V", "ns=1;i=6242", {}),
                            },
                        ),
                        "Vendor_Identifier": ("V", "ns=1;i=106070", {}),
                        "Vendor_Name": ("V", "ns=1;i=106069", {}),
                    },
                ),
                "BACnetEventEnrollmentType": (
                    "OT",
                    "ns=1;i=101006",
                    {
                        "EventReporting": (
                            "O",
                            "ns=1;i=105073",
                            {
                                "Acked_Transitions": ("V", "ns=1;i=106054", {}),
                                "Event_Enable": ("V", "ns=1;i=106192", {}),
                                "Event_State": ("V", "ns=1;i=6358", {}),
                                "Event_Time_Stamps": ("V", "ns=1;i=106278", {}),
                                "Notification_Class": ("V", "ns=1;i=106279", {}),
                                "Notify_Type": ("V", "ns=1;i=106280", {}),
                            },
                        ),
                        "Event_State": ("V", "ns=1;i=106062", {}),
                        "Event_Type": ("V", "ns=1;i=106053", {}),
                        "FaultEvaluation": (
                            "O",
                            "ns=1;i=105074",
                            {"Reliability": ("V", "ns=1;i=6377", {})},
                        ),
                        "Fault_Type": ("V", "ns=1;i=106079", {}),
                        "Object_Property_Reference": ("V", "ns=1;i=106061", {}),
                        "SetEventAlgorithm": (
                            "M",
                            "ns=1;i=107016",
                            {"InputArguments": ("V", "ns=1;i=6331", {})},
                        ),
                        "SetFaultAlgorithm": (
                            "M",
                            "ns=1;i=107017",
                            {"InputArguments": ("V", "ns=1;i=6332", {})},
                        ),
                        "Status_Flags": ("V", "ns=1;i=6330", {}),
                    },
                ),
                "BACnetLogType": (
                    "OT",
                    "ns=1;i=101014",
                    {
                        "BACnetEventLogType": ("OT", "ns=1;i=101018", {}),
                        "BACnetTrendLogBaseType": (
                            "OT",
                            "ns=1;i=101026",
                            {
                                "Align_Intervals": ("V", "ns=1;i=6334", {}),
                                "BACnetTrendLogMultipleType": (
                                    "OT",
                                    "ns=1;i=101027",
                                    {
                                        "Log_Buffer": ("V", "ns=1;i=106291", {}),
                                        "Log_DeviceObjectProperty": (
                                            "V",
                                            "ns=1;i=6340",
                                            {},
                                        ),
                                    },
                                ),
                                "BACnetTrendLogType": (
                                    "OT",
                                    "ns=1;i=101017",
                                    {
                                        "BACnetClockAlignedTrendLogType": (
                                            "OT",
                                            "ns=1;i=101015",
                                            {
                                                "Align_Interval": (
                                                    "V",
                                                    "ns=1;i=106216",
                                                    {},
                                                ),
                                                "Interval_Offset": (
                                                    "V",
                                                    "ns=1;i=106217",
                                                    {},
                                                ),
                                                "Log_Interval": (
                                                    "V",
                                                    "ns=1;i=106207",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "COV_Resubscription_Interval": (
                                            "V",
                                            "ns=1;i=106244",
                                            {},
                                        ),
                                        "Client_COV_Increment": (
                                            "V",
                                            "ns=1;i=106228",
                                            {},
                                        ),
                                        "Log_Buffer": ("V", "ns=1;i=6339", {}),
                                        "Log_DeviceObjectProperty": (
                                            "V",
                                            "ns=1;i=106245",
                                            {},
                                        ),
                                    },
                                ),
                                "Interval_Offset": ("V", "ns=1;i=6335", {}),
                                "Log_Interval": ("V", "ns=1;i=6336", {}),
                                "Logging_Type": ("V", "ns=1;i=6337", {}),
                                "Trigger": ("V", "ns=1;i=6338", {}),
                            },
                        ),
                        "Buffer_Size": ("V", "ns=1;i=106211", {}),
                        "Enable": ("V", "ns=1;i=106206", {}),
                        "EventReporting": (
                            "O",
                            "ns=1;i=105076",
                            {
                                "Acked_Transitions": ("V", "ns=1;i=106221", {}),
                                "EventAlgorithm": (
                                    "O",
                                    "ns=1;i=105077",
                                    {
                                        "PreviousCount": ("V", "ns=1;i=106231", {}),
                                        "Threshold": ("V", "ns=1;i=106230", {}),
                                        "TimeDelay": ("V", "ns=1;i=6654", {}),
                                        "TimeDelayNormal": ("V", "ns=1;i=6655", {}),
                                    },
                                ),
                                "Event_Enable": ("V", "ns=1;i=106222", {}),
                                "Event_Message_Texts": ("V", "ns=1;i=106220", {}),
                                "Event_Message_Texts_Config": (
                                    "V",
                                    "ns=1;i=106227",
                                    {},
                                ),
                                "Event_State": ("V", "ns=1;i=6359", {}),
                                "Event_Time_Stamps": ("V", "ns=1;i=106224", {}),
                                "Notification_Class": ("V", "ns=1;i=106225", {}),
                                "Notify_Type": ("V", "ns=1;i=106226", {}),
                            },
                        ),
                        "FaultEvaluation": (
                            "O",
                            "ns=1;i=105075",
                            {"Reliability": ("V", "ns=1;i=6378", {})},
                        ),
                        "Record_Count": ("V", "ns=1;i=106213", {}),
                        "Records_Since_Notification": ("V", "ns=1;i=106284", {}),
                        "Start_Time": ("V", "ns=1;i=106208", {}),
                        "Status_Flags": ("V", "ns=1;i=6333", {}),
                        "Stop_Time": ("V", "ns=1;i=106209", {}),
                        "Stop_When_Full": ("V", "ns=1;i=106210", {}),
                        "Total_Record_Count": ("V", "ns=1;i=106214", {}),
                    },
                ),
                "BACnetLoopType": (
                    "OT",
                    "ns=1;i=101001",
                    {
                        "Action": ("V", "ns=1;i=106033", {}),
                        "Bias": (
                            "V",
                            "ns=1;i=6386",
                            {"EngineeringUnits": ("V", "ns=1;i=6387", {})},
                        ),
                        "COV_Increment": ("V", "ns=1;i=106042", {}),
                        "Controlled_Variable_Reference": ("V", "ns=1;i=106015", {}),
                        "Controlled_Variable_Value": (
                            "V",
                            "ns=1;i=6268",
                            {"EngineeringUnits": ("V", "ns=1;i=6269", {})},
                        ),
                        "Derivative_Constant": (
                            "V",
                            "ns=1;i=6388",
                            {"EngineeringUnits": ("V", "ns=1;i=6389", {})},
                        ),
                        "EventReporting": (
                            "O",
                            "ns=1;i=105013",
                            {
                                "Acked_Transitions": ("V", "ns=1;i=106016", {}),
                                "EventAlgorithm": (
                                    "O",
                                    "ns=1;i=5145",
                                    {
                                        "Deadband": ("V", "ns=1;i=6683", {}),
                                        "HighDiffLimit": ("V", "ns=1;i=6684", {}),
                                        "LowDiffLimit": ("V", "ns=1;i=6685", {}),
                                        "SetpointReference": ("V", "ns=1;i=6686", {}),
                                        "TimeDelay": ("V", "ns=1;i=6687", {}),
                                        "TimeDelayNormal": ("V", "ns=1;i=6688", {}),
                                    },
                                ),
                                "Event_Enable": ("V", "ns=1;i=106023", {}),
                                "Event_State": ("V", "ns=1;i=6357", {}),
                                "Event_Time_Stamps": ("V", "ns=1;i=106025", {}),
                                "Notification_Class": ("V", "ns=1;i=106026", {}),
                                "Notify_Type": ("V", "ns=1;i=106027", {}),
                            },
                        ),
                        "FaultEvaluation": (
                            "O",
                            "ns=1;i=105072",
                            {"Reliability": ("V", "ns=1;i=6376", {})},
                        ),
                        "Integral_Constant": (
                            "V",
                            "ns=1;i=6384",
                            {"EngineeringUnits": ("V", "ns=1;i=6385", {})},
                        ),
                        "Manipulated_Variable_Reference": ("V", "ns=1;i=106014", {}),
                        "Out_Of_Service": ("V", "ns=1;i=106012", {}),
                        "Present_Value": (
                            "V",
                            "ns=1;i=6025",
                            {"EngineeringUnits": ("V", "ns=1;i=6027", {})},
                        ),
                        "Priority_For_Writing": ("V", "ns=1;i=106041", {}),
                        "Proportional_Constant": (
                            "V",
                            "ns=1;i=6382",
                            {"EngineeringUnits": ("V", "ns=1;i=6383", {})},
                        ),
                        "Setpoint": (
                            "V",
                            "ns=1;i=6327",
                            {"EngineeringUnits": ("V", "ns=1;i=6328", {})},
                        ),
                        "Setpoint_Reference": ("V", "ns=1;i=106029", {}),
                        "Status_Flags": ("V", "ns=1;i=6329", {}),
                    },
                ),
                "BACnetMultiStateType": (
                    "OT",
                    "ns=1;i=1018",
                    {
                        "BACnetMultiStateInputType": (
                            "OT",
                            "ns=1;i=1019",
                            {
                                "Device_Type": ("V", "ns=1;i=6122", {}),
                                "EventReporting": (
                                    "O",
                                    "ns=1;i=5075",
                                    {
                                        "Acked_Transitions": ("V", "ns=1;i=6298", {}),
                                        "EventAlgorithm": (
                                            "O",
                                            "ns=1;i=5140",
                                            {
                                                "AlarmValues": ("V", "ns=1;i=6671", {}),
                                                "TimeDelay": ("V", "ns=1;i=6672", {}),
                                                "TimeDelayNormal": (
                                                    "V",
                                                    "ns=1;i=6673",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Event_Enable": ("V", "ns=1;i=6299", {}),
                                        "Event_State": ("V", "ns=1;i=6300", {}),
                                        "Event_Time_Stamps": ("V", "ns=1;i=6301", {}),
                                        "Notification_Class": ("V", "ns=1;i=6302", {}),
                                        "Notify_Type": ("V", "ns=1;i=6303", {}),
                                    },
                                ),
                                "FaultEvaluation": (
                                    "O",
                                    "ns=1;i=5076",
                                    {
                                        "FaultAlgorithm": (
                                            "O",
                                            "ns=1;i=5141",
                                            {"FaultValues": ("V", "ns=1;i=6674", {})},
                                        ),
                                        "Reliability": ("V", "ns=1;i=6319", {}),
                                    },
                                ),
                            },
                        ),
                        "BACnetMultiStateOutputType": (
                            "OT",
                            "ns=1;i=1020",
                            {
                                "Device_Type": ("V", "ns=1;i=6123", {}),
                                "EventReporting": (
                                    "O",
                                    "ns=1;i=5077",
                                    {
                                        "Acked_Transitions": ("V", "ns=1;i=6306", {}),
                                        "EventAlgorithm": (
                                            "O",
                                            "ns=1;i=5142",
                                            {
                                                "FeedbackValueRef": (
                                                    "V",
                                                    "ns=1;i=6675",
                                                    {},
                                                ),
                                                "TimeDelay": ("V", "ns=1;i=6676", {}),
                                                "TimeDelayNormal": (
                                                    "V",
                                                    "ns=1;i=6677",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Event_Enable": ("V", "ns=1;i=6307", {}),
                                        "Event_State": ("V", "ns=1;i=6308", {}),
                                        "Event_Time_Stamps": ("V", "ns=1;i=6309", {}),
                                        "Notification_Class": ("V", "ns=1;i=6310", {}),
                                        "Notify_Type": ("V", "ns=1;i=6311", {}),
                                    },
                                ),
                                "Feedback_Value": ("V", "ns=1;i=6312", {}),
                                "Priority_Array": ("V", "ns=1;i=6124", {}),
                                "Relinquish_Default": ("V", "ns=1;i=6125", {}),
                            },
                        ),
                        "BACnetMultiStateValueType": (
                            "OT",
                            "ns=1;i=1021",
                            {
                                "EventReporting": (
                                    "O",
                                    "ns=1;i=5078",
                                    {
                                        "Acked_Transitions": ("V", "ns=1;i=6313", {}),
                                        "EventAlgorithm": (
                                            "O",
                                            "ns=1;i=5143",
                                            {
                                                "AlarmValues": ("V", "ns=1;i=6678", {}),
                                                "TimeDelay": ("V", "ns=1;i=6679", {}),
                                                "TimeDelayNormal": (
                                                    "V",
                                                    "ns=1;i=6680",
                                                    {},
                                                ),
                                            },
                                        ),
                                        "Event_Enable": ("V", "ns=1;i=6314", {}),
                                        "Event_State": ("V", "ns=1;i=6315", {}),
                                        "Event_Time_Stamps": ("V", "ns=1;i=6316", {}),
                                        "Notification_Class": ("V", "ns=1;i=6317", {}),
                                        "Notify_Type": ("V", "ns=1;i=6318", {}),
                                    },
                                ),
                                "FaultEvaluation": (
                                    "O",
                                    "ns=1;i=5079",
                                    {
                                        "FaultAlgorithm": (
                                            "O",
                                            "ns=1;i=5144",
                                            {"FaultValues": ("V", "ns=1;i=6681", {})},
                                        ),
                                        "Reliability": ("V", "ns=1;i=6320", {}),
                                    },
                                ),
                                "Priority_Array": ("V", "ns=1;i=6126", {}),
                                "Relinquish_Default": ("V", "ns=1;i=6127", {}),
                            },
                        ),
                        "EventReporting": (
                            "O",
                            "ns=1;i=5009",
                            {
                                "Acked_Transitions": ("V", "ns=1;i=6105", {}),
                                "Event_Enable": ("V", "ns=1;i=6116", {}),
                                "Event_State": ("V", "ns=1;i=6117", {}),
                                "Event_Time_Stamps": ("V", "ns=1;i=6118", {}),
                                "Notification_Class": ("V", "ns=1;i=6119", {}),
                                "Notify_Type": ("V", "ns=1;i=6120", {}),
                            },
                        ),
                        "FaultEvaluation": (
                            "O",
                            "ns=1;i=105070",
                            {"Reliability": ("V", "ns=1;i=6374", {})},
                        ),
                        "Out_Of_Service": ("V", "ns=1;i=6109", {}),
                        "Present_Value": (
                            "V",
                            "ns=1;i=6106",
                            {"EnumStrings": ("V", "ns=1;i=6107", {})},
                        ),
                        "Status_Flags": ("V", "ns=1;i=6135", {}),
                    },
                ),
                "BACnetNotifierType": (
                    "OT",
                    "ns=1;i=1048",
                    {
                        "BACnetNotificationClassType": (
                            "OT",
                            "ns=1;i=1024",
                            {
                                "Ack_Required": ("V", "ns=1;i=6344", {}),
                                "Notification_Class": ("V", "ns=1;i=6131", {}),
                                "Priority": ("V", "ns=1;i=6343", {}),
                            },
                        ),
                        "Recipient_List": ("V", "ns=1;i=6201", {}),
                    },
                ),
                "BACnetObjectTypeUnknown": (
                    "OT",
                    "ns=1;i=101024",
                    {"Object_Type": ("V", "ns=1;i=106084", {})},
                ),
                "BACnetScheduleType": (
                    "OT",
                    "ns=1;i=1022",
                    {
                        "AddObjectPropertyReferences": (
                            "M",
                            "ns=1;i=107014",
                            {
                                "InputArguments": ("V", "ns=1;i=6323", {}),
                                "OutputArguments": ("V", "ns=1;i=6324", {}),
                            },
                        ),
                        "Effective_Period": ("V", "ns=1;i=6182", {}),
                        "EventReporting": (
                            "O",
                            "ns=1;i=105093",
                            {
                                "Acked_Transitions": ("V", "ns=1;i=106296", {}),
                                "Event_Enable": ("V", "ns=1;i=106297", {}),
                                "Event_State": ("V", "ns=1;i=6361", {}),
                                "Event_Time_Stamps": ("V", "ns=1;i=106299", {}),
                                "Notification_Class": ("V", "ns=1;i=106300", {}),
                                "Notify_Type": ("V", "ns=1;i=106301", {}),
                            },
                        ),
                        "Exception_Schedule": ("V", "ns=1;i=106003", {}),
                        "FaultEvaluation": (
                            "O",
                            "ns=1;i=105071",
                            {"Reliability": ("V", "ns=1;i=6375", {})},
                        ),
                        "List_Of_Object_Property_References": (
                            "V",
                            "ns=1;i=106004",
                            {},
                        ),
                        "Out_Of_Service": ("V", "ns=1;i=6175", {}),
                        "Present_Value": ("V", "ns=1;i=6128", {}),
                        "Priority_For_Writing": ("V", "ns=1;i=6130", {}),
                        "RemoveObjectPropertyReferences": (
                            "M",
                            "ns=1;i=107015",
                            {
                                "InputArguments": ("V", "ns=1;i=6325", {}),
                                "OutputArguments": ("V", "ns=1;i=6326", {}),
                            },
                        ),
                        "Schedule_Default": ("V", "ns=1;i=6321", {}),
                        "Status_Flags": ("V", "ns=1;i=6176", {}),
                        "Weekly_Schedule": ("V", "ns=1;i=106002", {}),
                    },
                ),
                "BACnetStructuredViewType": (
                    "OT",
                    "ns=1;i=1049",
                    {
                        "<BACnetObject>": (
                            "O",
                            "ns=1;i=5044",
                            {"Object_Identifier": ("V", "ns=1;i=6237", {})},
                        ),
                        "<BACnetStructuredView>": (
                            "O",
                            "ns=1;i=5043",
                            {
                                "Node_Type": ("V", "ns=1;i=6081", {}),
                                "Object_Identifier": ("V", "ns=1;i=6236", {}),
                                "Subordinate_List": ("V", "ns=1;i=6082", {}),
                            },
                        ),
                        "Node_Subtype": ("V", "ns=1;i=6238", {}),
                        "Node_Type": ("V", "ns=1;i=6057", {}),
                        "Subordinate_Annotations": ("V", "ns=1;i=6078", {}),
                        "Subordinate_List": ("V", "ns=1;i=6077", {}),
                    },
                ),
                "Object_Identifier": ("V", "ns=1;i=6072", {}),
                "Profile_Name": ("V", "ns=1;i=6069", {}),
            },
        ),
        "BACnetTimeManagementType": (
            "OT",
            "ns=1;i=101019",
            {
                "BACnetAutomaticTimeSynchronizationMasterType": (
                    "OT",
                    "ns=1;i=1052",
                    {
                        "AddTimeSynchronizationRecipients": (
                            "M",
                            "ns=1;i=7027",
                            {
                                "InputArguments": ("V", "ns=1;i=6353", {}),
                                "OutputArguments": ("V", "ns=1;i=6354", {}),
                            },
                        ),
                        "Align_Intervals": ("V", "ns=1;i=6351", {}),
                        "Interval_Offset": ("V", "ns=1;i=6352", {}),
                        "RemoveTimeSynchronizationRecipients": (
                            "M",
                            "ns=1;i=7028",
                            {
                                "InputArguments": ("V", "ns=1;i=6355", {}),
                                "OutputArguments": ("V", "ns=1;i=6356", {}),
                            },
                        ),
                        "Time_Synchronization_Interval": ("V", "ns=1;i=6350", {}),
                        "Time_Synchronization_Recipients": ("V", "ns=1;i=6348", {}),
                        "UTC_Time_Synchronization_Recipients": ("V", "ns=1;i=6349", {}),
                    },
                ),
                "Daylight_Savings_Status": ("V", "ns=1;i=106248", {}),
                "Local_Date": ("V", "ns=1;i=106215", {}),
                "Local_Time": ("V", "ns=1;i=106218", {}),
                "TimeSynchronization": (
                    "M",
                    "ns=1;i=107001",
                    {"InputArguments": ("V", "ns=1;i=6346", {})},
                ),
                "UTC_Offset": ("V", "ns=1;i=106242", {}),
            },
        ),
    },
    "vartypes": {
        "BACNetAnalogItemType": (
            "VT",
            "ns=1;i=2001",
            {"EngineeringUnits": ("V", "ns=1;i=6001", {})},
        )
    },
}
