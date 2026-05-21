# Copyright 2026 (c) o6 Automation GmbH
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
                {"name": "DIRECT", "value": 0, "display_name": "DIRECT"},
                {"name": "REVERSE", "value": 1, "display_name": "REVERSE"},
            ]
        },
    ),
    (
        "ns=1;i=103016",
        "BACnetBackupState",
        {
            "fields": [
                {"name": "IDLE", "value": 0, "display_name": "IDLE"},
                {
                    "name": "PREPARING_FOR_BACKUP",
                    "value": 1,
                    "display_name": "PREPARING_FOR_BACKUP",
                },
                {
                    "name": "PREPARING_FOR_RESTORE",
                    "value": 2,
                    "display_name": "PREPARING_FOR_RESTORE",
                },
                {
                    "name": "PERFORMING_A_BACKUP",
                    "value": 3,
                    "display_name": "PERFORMING_A_BACKUP",
                },
                {
                    "name": "PERFORMING_A_RESTORE",
                    "value": 4,
                    "display_name": "PERFORMING_A_RESTORE",
                },
                {
                    "name": "BACKUP_FAILURE",
                    "value": 5,
                    "display_name": "BACKUP_FAILURE",
                },
                {
                    "name": "RESTORE_FAILURE",
                    "value": 6,
                    "display_name": "RESTORE_FAILURE",
                },
            ]
        },
    ),
    (
        "ns=1;i=3005",
        "BACnetBinaryPV",
        {
            "fields": [
                {"name": "INACTIVE", "value": 0, "display_name": "INACTIVE"},
                {"name": "ACTIVE", "value": 1, "display_name": "ACTIVE"},
            ]
        },
    ),
    (
        "ns=1;i=3021",
        "BACnetDay",
        {
            "fields": [
                {
                    "name": "DAYS NUMBERED 1-7",
                    "value": 1,
                    "display_name": "DAYS NUMBERED 1-7",
                },
                {
                    "name": "DAYS NUMBERED 8-14",
                    "value": 2,
                    "display_name": "DAYS NUMBERED 8-14",
                },
                {
                    "name": "DAYS NUMBERED 15-21",
                    "value": 3,
                    "display_name": "DAYS NUMBERED 15-21",
                },
                {
                    "name": "DAYS NUMBERED 22-28",
                    "value": 4,
                    "display_name": "DAYS NUMBERED 22-28",
                },
                {
                    "name": "DAYS NUMBERED 29-31",
                    "value": 5,
                    "display_name": "DAYS NUMBERED 29-31",
                },
                {
                    "name": "LAST 7 DAYS OF THIS MONTH",
                    "value": 6,
                    "display_name": "LAST 7 DAYS OF THIS MONTH",
                },
                {
                    "name": "ANY WEEK OF THIS MONTH",
                    "value": 255,
                    "display_name": "ANY WEEK OF THIS MONTH",
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
                    "name": "LAST DAY OF MONTH",
                    "value": 32,
                    "display_name": "LAST DAY OF MONTH",
                },
                {
                    "name": "ODD DAY OF MONTH",
                    "value": 33,
                    "display_name": "ODD DAY OF MONTH",
                },
                {
                    "name": "EVEN DAY OF MONTH",
                    "value": 34,
                    "display_name": "EVEN DAY OF MONTH",
                },
                {"name": "UNSPECIFIED", "value": 255, "display_name": "UNSPECIFIED"},
            ]
        },
    ),
    (
        "ns=1;i=103036",
        "BACnetDayOfWeek",
        {
            "fields": [
                {"name": "MONDAY", "value": 1, "display_name": "MONDAY"},
                {"name": "TUESDAY", "value": 2, "display_name": "TUESDAY"},
                {"name": "WEDNESDAY", "value": 3, "display_name": "WEDNESDAY"},
                {"name": "THURSDAY", "value": 4, "display_name": "THURSDAY"},
                {"name": "FRIDAY", "value": 5, "display_name": "FRIDAY"},
                {"name": "SATURDAY", "value": 6, "display_name": "SATURDAY"},
                {"name": "SUNDAY", "value": 7, "display_name": "SUNDAY"},
                {"name": "UNSPECIFIED", "value": 255, "display_name": "UNSPECIFIED"},
            ]
        },
    ),
    (
        "ns=1;i=3018",
        "BACnetDeviceCommunicationEnabled",
        {
            "fields": [
                {"name": "ENABLE", "value": 0, "display_name": "ENABLE"},
                {"name": "DISABLE", "value": 1, "display_name": "DISABLE"},
                {
                    "name": "DISABLEINITIATION",
                    "value": 2,
                    "display_name": "DISABLEINITIATION",
                },
            ]
        },
    ),
    (
        "ns=1;i=3033",
        "BACnetDeviceStatus",
        {
            "fields": [
                {"name": "OPERATIONAL", "value": 0, "display_name": "OPERATIONAL"},
                {
                    "name": "OPERATIONALREADONLY",
                    "value": 1,
                    "display_name": "OPERATIONALREADONLY",
                },
                {
                    "name": "DOWNLOADREQUIRED",
                    "value": 2,
                    "display_name": "DOWNLOADREQUIRED",
                },
                {
                    "name": "DOWNLOADINPROGRESS",
                    "value": 3,
                    "display_name": "DOWNLOADINPROGRESS",
                },
                {
                    "name": "NONOPERATIONAL",
                    "value": 4,
                    "display_name": "NONOPERATIONAL",
                },
                {
                    "name": "BACKUPINPROGRESS",
                    "value": 5,
                    "display_name": "BACKUPINPROGRESS",
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
                    "name": "CHANGEOFBITSTRING",
                    "value": 0,
                    "display_name": "CHANGEOFBITSTRING",
                },
                {"name": "CHANGEOFSTATE", "value": 1, "display_name": "CHANGEOFSTATE"},
                {"name": "CHANGEOFVALUE", "value": 2, "display_name": "CHANGEOFVALUE"},
                {
                    "name": "COMMANDFAILURE",
                    "value": 3,
                    "display_name": "COMMANDFAILURE",
                },
                {"name": "FLOATINGLIMIT", "value": 4, "display_name": "FLOATINGLIMIT"},
                {"name": "OUTOFRANGE", "value": 5, "display_name": "OUTOFRANGE"},
                {
                    "name": "CHANGEOFLIFESAFETY",
                    "value": 8,
                    "display_name": "CHANGEOFLIFESAFETY",
                },
                {"name": "EXTENDED", "value": 9, "display_name": "EXTENDED"},
                {"name": "BUFFERREADY", "value": 10, "display_name": "BUFFERREADY"},
                {"name": "UNSIGNEDRANGE", "value": 11, "display_name": "UNSIGNEDRANGE"},
            ]
        },
    ),
    (
        "ns=1;i=3003",
        "BACnetEventState",
        {
            "fields": [
                {"name": "NORMAL", "value": 0, "display_name": "NORMAL"},
                {"name": "FAULT", "value": 1, "display_name": "FAULT"},
                {"name": "OFFNORMAL", "value": 2, "display_name": "OFFNORMAL"},
                {"name": "HIGHLIMIT", "value": 3, "display_name": "HIGHLIMIT"},
                {"name": "LOWLIMIT", "value": 4, "display_name": "LOWLIMIT"},
                {
                    "name": "LIFESAFETYALARM",
                    "value": 5,
                    "display_name": "LIFESAFETYALARM",
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
                    "name": "CHANGE-OF-BITSTRING",
                    "value": 0,
                    "display_name": "CHANGE-OF-BITSTRING",
                },
                {
                    "name": "CHANGE-OF-STATE",
                    "value": 1,
                    "display_name": "CHANGE-OF-STATE",
                },
                {
                    "name": "CHANGE-OF-VALUE",
                    "value": 2,
                    "display_name": "CHANGE-OF-VALUE",
                },
                {
                    "name": "COMMAND-FAILURE",
                    "value": 3,
                    "display_name": "COMMAND-FAILURE",
                },
                {"name": "OUT-OF-RANGE", "value": 5, "display_name": "OUT-OF-RANGE"},
                {
                    "name": "CHANGE-OF-LIFE-SAFETY",
                    "value": 8,
                    "display_name": "CHANGE-OF-LIFE-SAFETY",
                },
                {
                    "name": "FLOATING-LIMIT",
                    "value": 4,
                    "display_name": "FLOATING-LIMIT",
                },
                {"name": "EXTENDED", "value": 9, "display_name": "EXTENDED"},
                {"name": "BUFFER-READY", "value": 10, "display_name": "BUFFER-READY"},
                {
                    "name": "UNSIGNED-RANGE",
                    "value": 11,
                    "display_name": "UNSIGNED-RANGE",
                },
                {"name": "ACCESS-EVENT", "value": 13, "display_name": "ACCESS-EVENT"},
                {
                    "name": "DOUBLE-OUT-OF-RANGE",
                    "value": 14,
                    "display_name": "DOUBLE-OUT-OF-RANGE",
                },
                {
                    "name": "SIGNED-OUT-OF-RANGE",
                    "value": 15,
                    "display_name": "SIGNED-OUT-OF-RANGE",
                },
                {
                    "name": "UNSIGNED-OUT-OF-RANGE",
                    "value": 16,
                    "display_name": "UNSIGNED-OUT-OF-RANGE",
                },
                {
                    "name": "CHANGE-OF-CHARACTERSTRING",
                    "value": 17,
                    "display_name": "CHANGE-OF-CHARACTERSTRING",
                },
                {
                    "name": "CHANGE-OF-STATUS-FLAGS",
                    "value": 18,
                    "display_name": "CHANGE-OF-STATUS-FLAGS",
                },
            ]
        },
    ),
    (
        "ns=1;i=103028",
        "BACnetFaultType",
        {
            "fields": [
                {"name": "NONE", "value": 0, "display_name": "NONE"},
                {
                    "name": "FAULT-CHARACTERSTRING",
                    "value": 1,
                    "display_name": "FAULT-CHARACTERSTRING",
                },
                {"name": "FAULT-EXENDED", "value": 2, "display_name": "FAULT-EXENDED"},
                {
                    "name": "FAULT-LIFE-SAFETY",
                    "value": 3,
                    "display_name": "FAULT-LIFE-SAFETY",
                },
                {"name": "FAULT-STATE", "value": 4, "display_name": "FAULT-STATE"},
                {
                    "name": "FAULT-STATUS-FLAGS",
                    "value": 5,
                    "display_name": "FAULT-STATUS-FLAGS",
                },
            ]
        },
    ),
    (
        "ns=1;i=3035",
        "BACnetLifeSafetyMode",
        {
            "fields": [
                {"name": "OFF", "value": 0, "display_name": "OFF"},
                {"name": "ON", "value": 1, "display_name": "ON"},
                {"name": "TEST", "value": 2, "display_name": "TEST"},
                {"name": "MANNED", "value": 3, "display_name": "MANNED"},
                {"name": "UNMANNED", "value": 4, "display_name": "UNMANNED"},
                {"name": "ARMED", "value": 5, "display_name": "ARMED"},
                {"name": "DISARMED", "value": 6, "display_name": "DISARMED"},
                {"name": "PREARMED", "value": 7, "display_name": "PREARMED"},
                {"name": "SLOW", "value": 8, "display_name": "SLOW"},
                {"name": "FAST", "value": 9, "display_name": "FAST"},
                {"name": "DISCONNECTED", "value": 10, "display_name": "DISCONNECTED"},
                {"name": "ENABLED", "value": 11, "display_name": "ENABLED"},
                {"name": "DISABLED", "value": 12, "display_name": "DISABLED"},
                {
                    "name": "AUTOMATICRELEASEDISABLED",
                    "value": 13,
                    "display_name": "AUTOMATICRELEASEDISABLED",
                },
                {"name": "DEFAULT", "value": 14, "display_name": "DEFAULT"},
            ]
        },
    ),
    (
        "ns=1;i=3044",
        "BACnetLifeSafetyOperation",
        {
            "fields": [
                {"name": "NONE", "value": 0, "display_name": "NONE"},
                {"name": "SILENCE", "value": 1, "display_name": "SILENCE"},
                {
                    "name": "SILENCEAUDIBLE",
                    "value": 2,
                    "display_name": "SILENCEAUDIBLE",
                },
                {
                    "name": "SILENCEVISIBLE",
                    "value": 3,
                    "display_name": "SILENCEVISIBLE",
                },
                {"name": "RESET", "value": 4, "display_name": "RESET"},
                {"name": "RESETALARM", "value": 5, "display_name": "RESETALARM"},
                {"name": "RESETFAULT", "value": 6, "display_name": "RESETFAULT"},
                {"name": "UNSILENCE", "value": 7, "display_name": "UNSILENCE"},
                {
                    "name": "UNSILENCEAUDIBLE",
                    "value": 8,
                    "display_name": "UNSILENCEAUDIBLE",
                },
                {
                    "name": "UNSILENCEVISIBLE",
                    "value": 9,
                    "display_name": "UNSILENCEVISIBLE",
                },
            ]
        },
    ),
    (
        "ns=1;i=3036",
        "BACnetLifeSafetyState",
        {
            "fields": [
                {"name": "QUIET", "value": 0, "display_name": "QUIET"},
                {"name": "PREALARM", "value": 1, "display_name": "PREALARM"},
                {"name": "ALARM", "value": 2, "display_name": "ALARM"},
                {"name": "FAULT", "value": 3, "display_name": "FAULT"},
                {"name": "FAULTPREALARM", "value": 4, "display_name": "FAULTPREALARM"},
                {"name": "FAULTALARM", "value": 5, "display_name": "FAULTALARM"},
                {"name": "NOTREADY", "value": 6, "display_name": "NOTREADY"},
                {"name": "ACTIVE", "value": 7, "display_name": "ACTIVE"},
                {"name": "TAMPER", "value": 8, "display_name": "TAMPER"},
                {"name": "TESTALARM", "value": 9, "display_name": "TESTALARM"},
                {"name": "TESTACTIVE", "value": 10, "display_name": "TESTACTIVE"},
                {"name": "TESTFAULT", "value": 11, "display_name": "TESTFAULT"},
                {
                    "name": "TESTFAULTALARM",
                    "value": 12,
                    "display_name": "TESTFAULTALARM",
                },
                {"name": "HOLDUP", "value": 13, "display_name": "HOLDUP"},
                {"name": "DURESS", "value": 14, "display_name": "DURESS"},
                {"name": "TAMPERALARM", "value": 15, "display_name": "TAMPERALARM"},
                {"name": "ABNORMAL", "value": 16, "display_name": "ABNORMAL"},
                {
                    "name": "EMERGENCYPOWER",
                    "value": 17,
                    "display_name": "EMERGENCYPOWER",
                },
                {"name": "DELAYED", "value": 18, "display_name": "DELAYED"},
                {"name": "BLOCKED", "value": 19, "display_name": "BLOCKED"},
                {"name": "LOCALALARM", "value": 20, "display_name": "LOCALALARM"},
                {"name": "GENERALALARM", "value": 21, "display_name": "GENERALALARM"},
                {"name": "SUPERVISORY", "value": 22, "display_name": "SUPERVISORY"},
                {
                    "name": "TESTSUPERVISORY",
                    "value": 23,
                    "display_name": "TESTSUPERVISORY",
                },
            ]
        },
    ),
    (
        "ns=1;i=103048",
        "BACnetLoggingType",
        {
            "fields": [
                {"name": "POLLED", "value": 0, "display_name": "POLLED"},
                {"name": "COV", "value": 1, "display_name": "COV"},
                {"name": "TRIGGERED", "value": 2, "display_name": "TRIGGERED"},
            ]
        },
    ),
    (
        "ns=1;i=3057",
        "BACnetMessagePriority",
        {
            "fields": [
                {"name": "NORMAL", "value": 0, "display_name": "NORMAL"},
                {"name": "URGENT", "value": 1, "display_name": "URGENT"},
            ]
        },
    ),
    (
        "ns=1;i=3014",
        "BACnetMonth",
        {
            "fields": [
                {"name": "JANUARY", "value": 1, "display_name": "JANUARY"},
                {"name": "FEBRUARY", "value": 2, "display_name": "FEBRUARY"},
                {"name": "MARCH", "value": 3, "display_name": "MARCH"},
                {"name": "APRIL", "value": 4, "display_name": "APRIL"},
                {"name": "MAY", "value": 5, "display_name": "MAY"},
                {"name": "JUNE", "value": 6, "display_name": "JUNE"},
                {"name": "JULY", "value": 7, "display_name": "JULY"},
                {"name": "AUGUST", "value": 8, "display_name": "AUGUST"},
                {"name": "SEPTEMBER", "value": 9, "display_name": "SEPTEMBER"},
                {"name": "OCTOBER", "value": 10, "display_name": "OCTOBER"},
                {"name": "NOVEMBER", "value": 11, "display_name": "NOVEMBER"},
                {"name": "DECEMBER", "value": 12, "display_name": "DECEMBER"},
                {"name": "ODD", "value": 13, "display_name": "ODD"},
                {"name": "EVEN", "value": 14, "display_name": "EVEN"},
                {"name": "UNSPECIFIED", "value": 255, "display_name": "UNSPECIFIED"},
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
                {"name": "ALARM", "value": 0, "display_name": "ALARM"},
                {"name": "EVENT", "value": 1, "display_name": "EVENT"},
                {
                    "name": "ACKNOTIFICATION",
                    "value": 2,
                    "display_name": "ACKNOTIFICATION",
                },
            ]
        },
    ),
    (
        "ns=1;i=103053",
        "BACnetObjectTypeEnum",
        {
            "fields": [
                {"name": "ANALOG-INPUT", "value": 0, "display_name": "ANALOG-INPUT"},
                {"name": "ANALOG-OUTPUT", "value": 1, "display_name": "ANALOG-OUTPUT"},
                {"name": "ANALOG-VALUE", "value": 2, "display_name": "ANALOG-VALUE"},
                {"name": "BINARY-INPUT", "value": 3, "display_name": "BINARY-INPUT"},
                {"name": "BINARY-OUTPUT", "value": 4, "display_name": "BINARY-OUTPUT"},
                {"name": "BINARY-VALUE", "value": 5, "display_name": "BINARY-VALUE"},
                {"name": "CALENDAR", "value": 6, "display_name": "CALENDAR"},
                {"name": "COMMAND", "value": 7, "display_name": "COMMAND"},
                {"name": "DEVICE", "value": 8, "display_name": "DEVICE"},
                {
                    "name": "EVENT-ENROLLMENT",
                    "value": 9,
                    "display_name": "EVENT-ENROLLMENT",
                },
                {"name": "FILE", "value": 10, "display_name": "FILE"},
                {"name": "GROUP", "value": 11, "display_name": "GROUP"},
                {"name": "LOOP", "value": 12, "display_name": "LOOP"},
                {
                    "name": "MULTI-STATE-INPUT",
                    "value": 13,
                    "display_name": "MULTI-STATE-INPUT",
                },
                {
                    "name": "MULTI-STATE-OUTPUT",
                    "value": 14,
                    "display_name": "MULTI-STATE-OUTPUT",
                },
                {
                    "name": "NOTIFICATION-CLASS",
                    "value": 15,
                    "display_name": "NOTIFICATION-CLASS",
                },
                {"name": "PROGRAM", "value": 16, "display_name": "PROGRAM"},
                {"name": "SCHEDULE", "value": 17, "display_name": "SCHEDULE"},
                {"name": "AVERAGING", "value": 18, "display_name": "AVERAGING"},
                {
                    "name": "MULTI-STATE-VALUE",
                    "value": 19,
                    "display_name": "MULTI-STATE-VALUE",
                },
                {"name": "TREND-LOG", "value": 20, "display_name": "TREND-LOG"},
                {
                    "name": "LIFE-SAFETY-POINT",
                    "value": 21,
                    "display_name": "LIFE-SAFETY-POINT",
                },
                {
                    "name": "LIFE-SAFETY-ZONE",
                    "value": 22,
                    "display_name": "LIFE-SAFETY-ZONE",
                },
                {"name": "ACCUMULATOR", "value": 23, "display_name": "ACCUMULATOR"},
                {
                    "name": "PULSE-CONVERTER",
                    "value": 24,
                    "display_name": "PULSE-CONVERTER",
                },
                {"name": "EVENT-LOG", "value": 25, "display_name": "EVENT-LOG"},
                {"name": "GLOBAL-GROUP", "value": 26, "display_name": "GLOBAL-GROUP"},
                {
                    "name": "TREND-LOG-MULTIPLE",
                    "value": 27,
                    "display_name": "TREND-LOG-MULTIPLE",
                },
                {"name": "LOAD-CONTROL", "value": 28, "display_name": "LOAD-CONTROL"},
                {
                    "name": "STRUCTURED-VIEW",
                    "value": 29,
                    "display_name": "STRUCTURED-VIEW",
                },
                {"name": "ACCESS-DOOR", "value": 30, "display_name": "ACCESS-DOOR"},
                {"name": "UNASSIGNED", "value": 31, "display_name": "UNASSIGNED"},
                {
                    "name": "ACCESS-CREDENTIAL",
                    "value": 32,
                    "display_name": "ACCESS-CREDENTIAL",
                },
                {"name": "ACCESS-POINT", "value": 33, "display_name": "ACCESS-POINT"},
                {"name": "ACCESS-RIGHTS", "value": 34, "display_name": "ACCESS-RIGHTS"},
                {"name": "ACCESS-USER", "value": 35, "display_name": "ACCESS-USER"},
                {"name": "ACCESS-ZONE", "value": 36, "display_name": "ACCESS-ZONE"},
                {
                    "name": "CREDENTIONAL-DATA-INPUT",
                    "value": 37,
                    "display_name": "CREDENTIONAL-DATA-INPUT",
                },
                {
                    "name": "NETWORK-SECURITY",
                    "value": 38,
                    "display_name": "NETWORK-SECURITY",
                },
                {
                    "name": "BITSTRING-VALUE",
                    "value": 39,
                    "display_name": "BITSTRING-VALUE",
                },
                {
                    "name": "CHARACTERSTRING-VALUE",
                    "value": 40,
                    "display_name": "CHARACTERSTRING-VALUE",
                },
                {
                    "name": "DATE-PATTERN-VALUE",
                    "value": 41,
                    "display_name": "DATE-PATTERN-VALUE",
                },
                {"name": "DATE-VALUE", "value": 42, "display_name": "DATE-VALUE"},
                {
                    "name": "DATETIME-PATTERN-VALUE",
                    "value": 43,
                    "display_name": "DATETIME-PATTERN-VALUE",
                },
                {
                    "name": "DATETIME-VALUE",
                    "value": 44,
                    "display_name": "DATETIME-VALUE",
                },
                {"name": "INTEGER-VALUE", "value": 45, "display_name": "INTEGER-VALUE"},
                {
                    "name": "LARGE-ANALOG-VALUE",
                    "value": 46,
                    "display_name": "LARGE-ANALOG-VALUE",
                },
                {
                    "name": "OCTETSTRING-VALUE",
                    "value": 47,
                    "display_name": "OCTETSTRING-VALUE",
                },
                {
                    "name": "POSITIVE-INTEGER-VALUE",
                    "value": 48,
                    "display_name": "POSITIVE-INTEGER-VALUE",
                },
                {
                    "name": "TIME-PATTERN-VALUE",
                    "value": 49,
                    "display_name": "TIME-PATTERN-VALUE",
                },
                {"name": "TIME-VALUE", "value": 50, "display_name": "TIME-VALUE"},
                {
                    "name": "NOTIFICATION-FORWARDER",
                    "value": 51,
                    "display_name": "NOTIFICATION-FORWARDER",
                },
                {
                    "name": "ALERT-ENROLLMENT",
                    "value": 52,
                    "display_name": "ALERT-ENROLLMENT",
                },
                {"name": "CHANNEL", "value": 53, "display_name": "CHANNEL"},
                {
                    "name": "LIGHTING-OUTPUT",
                    "value": 54,
                    "display_name": "LIGHTING-OUTPUT",
                },
            ]
        },
    ),
    (
        "ns=1;i=3007",
        "BACnetPolarity",
        {
            "fields": [
                {"name": "NORMAL", "value": 0, "display_name": "NORMAL"},
                {"name": "REVERSE", "value": 1, "display_name": "REVERSE"},
            ]
        },
    ),
    (
        "ns=1;i=3032",
        "BACnetProgramError",
        {
            "fields": [
                {"name": "NORMAL", "value": 0, "display_name": "NORMAL"},
                {"name": "LOADFAILED", "value": 1, "display_name": "LOADFAILED"},
                {"name": "INTERNAL", "value": 2, "display_name": "INTERNAL"},
                {"name": "PROGRAM", "value": 3, "display_name": "PROGRAM"},
                {"name": "OTHER", "value": 4, "display_name": "OTHER"},
            ]
        },
    ),
    (
        "ns=1;i=3030",
        "BACnetProgramRequest",
        {
            "fields": [
                {"name": "READY", "value": 0, "display_name": "READY"},
                {"name": "LOAD", "value": 1, "display_name": "LOAD"},
                {"name": "RUN", "value": 2, "display_name": "RUN"},
                {"name": "HALT", "value": 3, "display_name": "HALT"},
                {"name": "RESTART", "value": 4, "display_name": "RESTART"},
                {"name": "UNLOAD", "value": 5, "display_name": "UNLOAD"},
            ]
        },
    ),
    (
        "ns=1;i=3031",
        "BACnetProgramStates",
        {
            "fields": [
                {"name": "IDLE", "value": 0, "display_name": "IDLE"},
                {"name": "LOADING", "value": 1, "display_name": "LOADING"},
                {"name": "RUNNING", "value": 2, "display_name": "RUNNING"},
                {"name": "WAITING", "value": 3, "display_name": "WAITING"},
                {"name": "HALTED", "value": 4, "display_name": "HALTED"},
                {"name": "UNLOADING", "value": 5, "display_name": "UNLOADING"},
            ]
        },
    ),
    (
        "ns=1;i=3046",
        "BACnetPropertyIdentifier",
        {
            "fields": [
                {
                    "name": "ACKEDTRANSITIONS",
                    "value": 0,
                    "display_name": "ACKEDTRANSITIONS",
                },
                {"name": "ACKREQUIRED", "value": 1, "display_name": "ACKREQUIRED"},
                {"name": "ACTION", "value": 2, "display_name": "ACTION"},
                {"name": "ACTIONTEXT", "value": 3, "display_name": "ACTIONTEXT"},
                {"name": "ACTIVETEXT", "value": 4, "display_name": "ACTIVETEXT"},
                {
                    "name": "ACTIVEVTSESSIONS",
                    "value": 5,
                    "display_name": "ACTIVEVTSESSIONS",
                },
                {"name": "ALARMVALUE", "value": 6, "display_name": "ALARMVALUE"},
                {"name": "ALARMVALUES", "value": 7, "display_name": "ALARMVALUES"},
                {"name": "ALL", "value": 8, "display_name": "ALL"},
                {
                    "name": "ALLWRITESSUCCESSFUL",
                    "value": 9,
                    "display_name": "ALLWRITESSUCCESSFUL",
                },
                {
                    "name": "APDUSEGMENTTIMEOUT",
                    "value": 10,
                    "display_name": "APDUSEGMENTTIMEOUT",
                },
                {"name": "APDUTIMEOUT", "value": 11, "display_name": "APDUTIMEOUT"},
                {
                    "name": "APPLICATIONSOFTWAREVERSION",
                    "value": 12,
                    "display_name": "APPLICATIONSOFTWAREVERSION",
                },
                {"name": "ARCHIVE", "value": 13, "display_name": "ARCHIVE"},
                {"name": "BIAS", "value": 14, "display_name": "BIAS"},
                {
                    "name": "CHANGEOFSTATECOUNT",
                    "value": 15,
                    "display_name": "CHANGEOFSTATECOUNT",
                },
                {
                    "name": "CHANGEOFSTATETIME",
                    "value": 16,
                    "display_name": "CHANGEOFSTATETIME",
                },
                {
                    "name": "NOTIFICATIONCLASS",
                    "value": 17,
                    "display_name": "NOTIFICATIONCLASS",
                },
                {
                    "name": "THIS PROPERTY DELETED",
                    "value": 18,
                    "display_name": "THIS PROPERTY DELETED",
                },
                {
                    "name": "CONTROLLEDVARIABLEREFERENCE",
                    "value": 19,
                    "display_name": "CONTROLLEDVARIABLEREFERENCE",
                },
                {
                    "name": "CONTROLLEDVARIABLEUNITS",
                    "value": 20,
                    "display_name": "CONTROLLEDVARIABLEUNITS",
                },
                {
                    "name": "CONTROLLEDVARIABLEVALUE",
                    "value": 21,
                    "display_name": "CONTROLLEDVARIABLEVALUE",
                },
                {"name": "COVINCREMENT", "value": 22, "display_name": "COVINCREMENT"},
                {"name": "DATELIST", "value": 23, "display_name": "DATELIST"},
                {
                    "name": "DAYLIGHTSAVINGSSTATUS",
                    "value": 24,
                    "display_name": "DAYLIGHTSAVINGSSTATUS",
                },
                {"name": "DEADBAND", "value": 25, "display_name": "DEADBAND"},
                {
                    "name": "DERIVATIVECONSTANT",
                    "value": 26,
                    "display_name": "DERIVATIVECONSTANT",
                },
                {
                    "name": "DERIVATIVECONSTANTUNITS",
                    "value": 27,
                    "display_name": "DERIVATIVECONSTANTUNITS",
                },
                {"name": "DESCRIPTION", "value": 28, "display_name": "DESCRIPTION"},
                {
                    "name": "DESCRIPTIONOFHALT",
                    "value": 29,
                    "display_name": "DESCRIPTIONOFHALT",
                },
                {
                    "name": "DEVICEADDRESSBINDING",
                    "value": 30,
                    "display_name": "DEVICEADDRESSBINDING",
                },
                {"name": "DEVICETYPE", "value": 31, "display_name": "DEVICETYPE"},
                {
                    "name": "EFFECTIVEPERIOD",
                    "value": 32,
                    "display_name": "EFFECTIVEPERIOD",
                },
                {
                    "name": "ELAPSEDACTIVETIME",
                    "value": 33,
                    "display_name": "ELAPSEDACTIVETIME",
                },
                {"name": "ERRORLIMIT", "value": 34, "display_name": "ERRORLIMIT"},
                {"name": "EVENTENABLE", "value": 35, "display_name": "EVENTENABLE"},
                {"name": "EVENTSTATE", "value": 36, "display_name": "EVENTSTATE"},
                {"name": "EVENTTYPE", "value": 37, "display_name": "EVENTTYPE"},
                {
                    "name": "EXCEPTIONSCHEDULE",
                    "value": 38,
                    "display_name": "EXCEPTIONSCHEDULE",
                },
                {"name": "FAULTVALUES", "value": 39, "display_name": "FAULTVALUES"},
                {"name": "FEEDBACKVALUE", "value": 40, "display_name": "FEEDBACKVALUE"},
                {
                    "name": "FILEACCESSMETHOD",
                    "value": 41,
                    "display_name": "FILEACCESSMETHOD",
                },
                {"name": "FILESIZE", "value": 42, "display_name": "FILESIZE"},
                {"name": "FILETYPE", "value": 43, "display_name": "FILETYPE"},
                {
                    "name": "FIRMWAREREVISION",
                    "value": 44,
                    "display_name": "FIRMWAREREVISION",
                },
                {"name": "HIGHLIMIT", "value": 45, "display_name": "HIGHLIMIT"},
                {"name": "INACTIVETEXT", "value": 46, "display_name": "INACTIVETEXT"},
                {"name": "INPROCESS", "value": 47, "display_name": "INPROCESS"},
                {"name": "INSTANCEOF", "value": 48, "display_name": "INSTANCEOF"},
                {
                    "name": "INTEGRALCONSTANT",
                    "value": 49,
                    "display_name": "INTEGRALCONSTANT",
                },
                {
                    "name": "INTEGRALCONSTANTUNITS",
                    "value": 50,
                    "display_name": "INTEGRALCONSTANTUNITS",
                },
                {
                    "name": "REMOVED IN VERSION 1 REVISION 4_51",
                    "value": 51,
                    "display_name": "REMOVED IN VERSION 1 REVISION 4_51",
                },
                {"name": "LIMITENABLE", "value": 52, "display_name": "LIMITENABLE"},
                {
                    "name": "LISTOFGROUPMEMBERS",
                    "value": 53,
                    "display_name": "LISTOFGROUPMEMBERS",
                },
                {
                    "name": "LISTOFOBJECTPROPERTYREFERENCES",
                    "value": 54,
                    "display_name": "LISTOFOBJECTPROPERTYREFERENCES",
                },
                {"name": "UNASSIGNED_55", "value": 55, "display_name": "UNASSIGNED_55"},
                {"name": "LOCALDATE", "value": 56, "display_name": "LOCALDATE"},
                {"name": "LOCALTIME", "value": 57, "display_name": "LOCALTIME"},
                {"name": "LOCATION", "value": 58, "display_name": "LOCATION"},
                {"name": "LOWLIMIT", "value": 59, "display_name": "LOWLIMIT"},
                {
                    "name": "MANIPULATEDVARIABLEREFERENCE",
                    "value": 60,
                    "display_name": "MANIPULATEDVARIABLEREFERENCE",
                },
                {"name": "MAXIMUMOUTPUT", "value": 61, "display_name": "MAXIMUMOUTPUT"},
                {
                    "name": "MAXAPDULENGTHACCEPTED",
                    "value": 62,
                    "display_name": "MAXAPDULENGTHACCEPTED",
                },
                {"name": "MAXINFOFRAMES", "value": 63, "display_name": "MAXINFOFRAMES"},
                {"name": "MAXMASTER", "value": 64, "display_name": "MAXMASTER"},
                {"name": "MAXPRESVALUE", "value": 65, "display_name": "MAXPRESVALUE"},
                {
                    "name": "MINIMUMOFFTIME",
                    "value": 66,
                    "display_name": "MINIMUMOFFTIME",
                },
                {"name": "MINIMUMONTIME", "value": 67, "display_name": "MINIMUMONTIME"},
                {"name": "MINIMUMOUTPUT", "value": 68, "display_name": "MINIMUMOUTPUT"},
                {"name": "MINPRESVALUE", "value": 69, "display_name": "MINPRESVALUE"},
                {"name": "MODELNAME", "value": 70, "display_name": "MODELNAME"},
                {
                    "name": "MODIFICATIONDATE",
                    "value": 71,
                    "display_name": "MODIFICATIONDATE",
                },
                {"name": "NOTIFYTYPE", "value": 72, "display_name": "NOTIFYTYPE"},
                {
                    "name": "NUMBEROFAPDURETRIES",
                    "value": 73,
                    "display_name": "NUMBEROFAPDURETRIES",
                },
                {
                    "name": "NUMBEROFSTATES",
                    "value": 74,
                    "display_name": "NUMBEROFSTATES",
                },
                {
                    "name": "OBJECTIDENTIFIER",
                    "value": 75,
                    "display_name": "OBJECTIDENTIFIER",
                },
                {"name": "OBJECTLIST", "value": 76, "display_name": "OBJECTLIST"},
                {"name": "OBJECTNAME", "value": 77, "display_name": "OBJECTNAME"},
                {
                    "name": "OBJECTPROPERTYREFERENCE",
                    "value": 78,
                    "display_name": "OBJECTPROPERTYREFERENCE",
                },
                {"name": "OBJECTTYPE", "value": 79, "display_name": "OBJECTTYPE"},
                {"name": "OPTIONAL", "value": 80, "display_name": "OPTIONAL"},
                {"name": "OUTOFSERVICE", "value": 81, "display_name": "OUTOFSERVICE"},
                {"name": "OUTPUTUNITS", "value": 82, "display_name": "OUTPUTUNITS"},
                {
                    "name": "EVENTPARAMETERS",
                    "value": 83,
                    "display_name": "EVENTPARAMETERS",
                },
                {"name": "POLARITY", "value": 84, "display_name": "POLARITY"},
                {"name": "PRESENTVALUE", "value": 85, "display_name": "PRESENTVALUE"},
                {"name": "PRIORITY", "value": 86, "display_name": "PRIORITY"},
                {"name": "PRIORITYARRAY", "value": 87, "display_name": "PRIORITYARRAY"},
                {
                    "name": "PRIORITYFORWRITING",
                    "value": 88,
                    "display_name": "PRIORITYFORWRITING",
                },
                {
                    "name": "PROCESSIDENTIFIER",
                    "value": 89,
                    "display_name": "PROCESSIDENTIFIER",
                },
                {"name": "PROGRAMCHANGE", "value": 90, "display_name": "PROGRAMCHANGE"},
                {
                    "name": "PROGRAMLOCATION",
                    "value": 91,
                    "display_name": "PROGRAMLOCATION",
                },
                {"name": "PROGRAMSTATE", "value": 92, "display_name": "PROGRAMSTATE"},
                {
                    "name": "PROPORTIONALCONSTANT",
                    "value": 93,
                    "display_name": "PROPORTIONALCONSTANT",
                },
                {
                    "name": "PROPORTIONALCONSTANTUNITS",
                    "value": 94,
                    "display_name": "PROPORTIONALCONSTANTUNITS",
                },
                {
                    "name": "REMOVED IN VERSION 1 REVISION 2_95",
                    "value": 95,
                    "display_name": "REMOVED IN VERSION 1 REVISION 2_95",
                },
                {
                    "name": "PROTOCOLOBJECTTYPESSUPPORTED",
                    "value": 96,
                    "display_name": "PROTOCOLOBJECTTYPESSUPPORTED",
                },
                {
                    "name": "PROTOCOLSERVICESSUPPORTED",
                    "value": 97,
                    "display_name": "PROTOCOLSERVICESSUPPORTED",
                },
                {
                    "name": "PROTOCOLVERSION",
                    "value": 98,
                    "display_name": "PROTOCOLVERSION",
                },
                {"name": "READONLY", "value": 99, "display_name": "READONLY"},
                {
                    "name": "REASONFORHALT",
                    "value": 100,
                    "display_name": "REASONFORHALT",
                },
                {
                    "name": "REMOVED IN VERSION 1 REVISION 4_101",
                    "value": 101,
                    "display_name": "REMOVED IN VERSION 1 REVISION 4_101",
                },
                {
                    "name": "RECIPIENTLIST",
                    "value": 102,
                    "display_name": "RECIPIENTLIST",
                },
                {"name": "RELIABILITY", "value": 103, "display_name": "RELIABILITY"},
                {
                    "name": "RELINQUISHDEFAULT",
                    "value": 104,
                    "display_name": "RELINQUISHDEFAULT",
                },
                {"name": "REQUIRED", "value": 105, "display_name": "REQUIRED"},
                {"name": "RESOLUTION", "value": 106, "display_name": "RESOLUTION"},
                {
                    "name": "SEGMENTATIONSUPPORTED",
                    "value": 107,
                    "display_name": "SEGMENTATIONSUPPORTED",
                },
                {"name": "SETPOINT", "value": 108, "display_name": "SETPOINT"},
                {
                    "name": "SETPOINTREFERENCE",
                    "value": 109,
                    "display_name": "SETPOINTREFERENCE",
                },
                {"name": "STATETEXT", "value": 110, "display_name": "STATETEXT"},
                {"name": "STATUSFLAGS", "value": 111, "display_name": "STATUSFLAGS"},
                {"name": "SYSTEMSTATUS", "value": 112, "display_name": "SYSTEMSTATUS"},
                {"name": "TIMEDELAY", "value": 113, "display_name": "TIMEDELAY"},
                {
                    "name": "TIMEOFACTIVETIMERESET",
                    "value": 114,
                    "display_name": "TIMEOFACTIVETIMERESET",
                },
                {
                    "name": "TIMEOFSTATECOUNTRESET",
                    "value": 115,
                    "display_name": "TIMEOFSTATECOUNTRESET",
                },
                {
                    "name": "TIMESYNCHRONIZATIONRECIPIENTS",
                    "value": 116,
                    "display_name": "TIMESYNCHRONIZATIONRECIPIENTS",
                },
                {"name": "UNITS", "value": 117, "display_name": "UNITS"},
                {
                    "name": "UPDATEINTERVAL",
                    "value": 118,
                    "display_name": "UPDATEINTERVAL",
                },
                {"name": "UTCOFFSET", "value": 119, "display_name": "UTCOFFSET"},
                {
                    "name": "VENDORIDENTIFIER",
                    "value": 120,
                    "display_name": "VENDORIDENTIFIER",
                },
                {"name": "VENDORNAME", "value": 121, "display_name": "VENDORNAME"},
                {
                    "name": "VTCLASSESSUPPORTED",
                    "value": 122,
                    "display_name": "VTCLASSESSUPPORTED",
                },
                {
                    "name": "WEEKLYSCHEDULE",
                    "value": 123,
                    "display_name": "WEEKLYSCHEDULE",
                },
                {
                    "name": "ATTEMPTEDSAMPLES",
                    "value": 124,
                    "display_name": "ATTEMPTEDSAMPLES",
                },
                {"name": "AVERAGEVALUE", "value": 125, "display_name": "AVERAGEVALUE"},
                {"name": "BUFFERSIZE", "value": 126, "display_name": "BUFFERSIZE"},
                {
                    "name": "CLIENTCOVINCREMENT",
                    "value": 127,
                    "display_name": "CLIENTCOVINCREMENT",
                },
                {
                    "name": "COVRESUBSCRIPTIONINTERVAL",
                    "value": 128,
                    "display_name": "COVRESUBSCRIPTIONINTERVAL",
                },
                {
                    "name": "REMOVED IN VERSION 1 REVISION 3_129",
                    "value": 129,
                    "display_name": "REMOVED IN VERSION 1 REVISION 3_129",
                },
                {
                    "name": "EVENTTIMESTAMPS",
                    "value": 130,
                    "display_name": "EVENTTIMESTAMPS",
                },
                {"name": "LOGBUFFER", "value": 131, "display_name": "LOGBUFFER"},
                {
                    "name": "LOGDEVICEOBJECTPROPERTY",
                    "value": 132,
                    "display_name": "LOGDEVICEOBJECTPROPERTY",
                },
                {"name": "ENABLE", "value": 133, "display_name": "ENABLE"},
                {"name": "LOGINTERVAL", "value": 134, "display_name": "LOGINTERVAL"},
                {"name": "MAXIMUMVALUE", "value": 135, "display_name": "MAXIMUMVALUE"},
                {"name": "MINIMUMVALUE", "value": 136, "display_name": "MINIMUMVALUE"},
                {
                    "name": "NOTIFICATIONTHRESHOLD",
                    "value": 137,
                    "display_name": "NOTIFICATIONTHRESHOLD",
                },
                {
                    "name": "REMOVED IN VERSION 1 REVISION 3_138",
                    "value": 138,
                    "display_name": "REMOVED IN VERSION 1 REVISION 3_138",
                },
                {
                    "name": "PROTOCOLREVISION",
                    "value": 139,
                    "display_name": "PROTOCOLREVISION",
                },
                {
                    "name": "RECORDSSINCENOTIFICATION",
                    "value": 140,
                    "display_name": "RECORDSSINCENOTIFICATION",
                },
                {"name": "RECORDCOUNT", "value": 141, "display_name": "RECORDCOUNT"},
                {"name": "STARTTIME", "value": 142, "display_name": "STARTTIME"},
                {"name": "STOPTIME", "value": 143, "display_name": "STOPTIME"},
                {"name": "STOPWHENFULL", "value": 144, "display_name": "STOPWHENFULL"},
                {
                    "name": "TOTALRECORDCOUNT",
                    "value": 145,
                    "display_name": "TOTALRECORDCOUNT",
                },
                {"name": "VALIDSAMPLES", "value": 146, "display_name": "VALIDSAMPLES"},
                {
                    "name": "WINDOWINTERVAL",
                    "value": 147,
                    "display_name": "WINDOWINTERVAL",
                },
                {
                    "name": "WINDOWSAMPLES",
                    "value": 148,
                    "display_name": "WINDOWSAMPLES",
                },
                {
                    "name": "MAXIMUMVALUETIMESTAMP",
                    "value": 149,
                    "display_name": "MAXIMUMVALUETIMESTAMP",
                },
                {
                    "name": "MINIMUMVALUETIMESTAMP",
                    "value": 150,
                    "display_name": "MINIMUMVALUETIMESTAMP",
                },
                {
                    "name": "VARIANCEVALUE",
                    "value": 151,
                    "display_name": "VARIANCEVALUE",
                },
                {
                    "name": "ACTIVECOVSUBSCRIPTIONS",
                    "value": 152,
                    "display_name": "ACTIVECOVSUBSCRIPTIONS",
                },
                {
                    "name": "BACKUPFAILURETIMEOUT",
                    "value": 153,
                    "display_name": "BACKUPFAILURETIMEOUT",
                },
                {
                    "name": "CONFIGURATIONFILES",
                    "value": 154,
                    "display_name": "CONFIGURATIONFILES",
                },
                {
                    "name": "DATABASEREVISION",
                    "value": 155,
                    "display_name": "DATABASEREVISION",
                },
                {
                    "name": "DIRECTREADING",
                    "value": 156,
                    "display_name": "DIRECTREADING",
                },
                {
                    "name": "LASTRESTORETIME",
                    "value": 157,
                    "display_name": "LASTRESTORETIME",
                },
                {
                    "name": "MAINTENANCEREQUIRED",
                    "value": 158,
                    "display_name": "MAINTENANCEREQUIRED",
                },
                {"name": "MEMBEROF", "value": 159, "display_name": "MEMBEROF"},
                {"name": "MODE", "value": 160, "display_name": "MODE"},
                {
                    "name": "OPERATIONEXPECTED",
                    "value": 161,
                    "display_name": "OPERATIONEXPECTED",
                },
                {"name": "SETTING", "value": 162, "display_name": "SETTING"},
                {"name": "SILENCED", "value": 163, "display_name": "SILENCED"},
                {
                    "name": "TRACKINGVALUE",
                    "value": 164,
                    "display_name": "TRACKINGVALUE",
                },
                {"name": "ZONEMEMBERS", "value": 165, "display_name": "ZONEMEMBERS"},
                {
                    "name": "LIFESAFETYALARMVALUES",
                    "value": 166,
                    "display_name": "LIFESAFETYALARMVALUES",
                },
                {
                    "name": "MAXSEGMENTSACCEPTED",
                    "value": 167,
                    "display_name": "MAXSEGMENTSACCEPTED",
                },
                {"name": "PROFILENAME", "value": 168, "display_name": "PROFILENAME"},
                {
                    "name": "AUTOSLAVEDISCOVERY",
                    "value": 169,
                    "display_name": "AUTOSLAVEDISCOVERY",
                },
                {
                    "name": "MANUALSLAVEADDRESSBINDING",
                    "value": 170,
                    "display_name": "MANUALSLAVEADDRESSBINDING",
                },
                {
                    "name": "SLAVEADDRESSBINDING",
                    "value": 171,
                    "display_name": "SLAVEADDRESSBINDING",
                },
                {
                    "name": "SLAVEPROXYENABLE",
                    "value": 172,
                    "display_name": "SLAVEPROXYENABLE",
                },
                {
                    "name": "LASTNOTIFYRECORD",
                    "value": 173,
                    "display_name": "LASTNOTIFYRECORD",
                },
                {
                    "name": "SCHEDULEDEFAULT",
                    "value": 174,
                    "display_name": "SCHEDULEDEFAULT",
                },
                {
                    "name": "ACCEPTEDMODES",
                    "value": 175,
                    "display_name": "ACCEPTEDMODES",
                },
                {"name": "ADJUSTVALUE", "value": 176, "display_name": "ADJUSTVALUE"},
                {"name": "COUNT", "value": 177, "display_name": "COUNT"},
                {
                    "name": "COUNTBEFORECHANGE",
                    "value": 178,
                    "display_name": "COUNTBEFORECHANGE",
                },
                {
                    "name": "COUNTCHANGETIME",
                    "value": 179,
                    "display_name": "COUNTCHANGETIME",
                },
                {"name": "COVPERIOD", "value": 180, "display_name": "COVPERIOD"},
                {
                    "name": "INPUTREFERENCE",
                    "value": 181,
                    "display_name": "INPUTREFERENCE",
                },
                {
                    "name": "LIMITMONITORINGINTERVAL",
                    "value": 182,
                    "display_name": "LIMITMONITORINGINTERVAL",
                },
                {
                    "name": "LOGGINGOBJECT",
                    "value": 183,
                    "display_name": "LOGGINGOBJECT",
                },
                {
                    "name": "LOGGINGRECORD",
                    "value": 184,
                    "display_name": "LOGGINGRECORD",
                },
                {"name": "PRESCALE", "value": 185, "display_name": "PRESCALE"},
                {"name": "PULSERATE", "value": 186, "display_name": "PULSERATE"},
                {"name": "SCALE", "value": 187, "display_name": "SCALE"},
                {"name": "SCALEFACTOR", "value": 188, "display_name": "SCALEFACTOR"},
                {"name": "UPDATETIME", "value": 189, "display_name": "UPDATETIME"},
                {
                    "name": "VALUEBEFORECHANGE",
                    "value": 190,
                    "display_name": "VALUEBEFORECHANGE",
                },
                {"name": "VALUESET", "value": 191, "display_name": "VALUESET"},
                {
                    "name": "VALUECHANGETIME",
                    "value": 192,
                    "display_name": "VALUECHANGETIME",
                },
                {
                    "name": "ALIGNINTERVALS",
                    "value": 193,
                    "display_name": "ALIGNINTERVALS",
                },
                {
                    "name": "UNASSIGNED_194",
                    "value": 194,
                    "display_name": "UNASSIGNED_194",
                },
                {
                    "name": "INTERVALOFFSET",
                    "value": 195,
                    "display_name": "INTERVALOFFSET",
                },
                {
                    "name": "LASTRESTARTREASON",
                    "value": 196,
                    "display_name": "LASTRESTARTREASON",
                },
                {"name": "LOGGINGTYPE", "value": 197, "display_name": "LOGGINGTYPE"},
                {
                    "name": "UNASSIGNED_198",
                    "value": 198,
                    "display_name": "UNASSIGNED_198",
                },
                {
                    "name": "UNASSIGNED_199",
                    "value": 199,
                    "display_name": "UNASSIGNED_199",
                },
                {
                    "name": "UNASSIGNED_200",
                    "value": 200,
                    "display_name": "UNASSIGNED_200",
                },
                {
                    "name": "UNASSIGNED_201",
                    "value": 201,
                    "display_name": "UNASSIGNED_201",
                },
                {
                    "name": "RESTARTNOTIFICATIONRECIPIENTS",
                    "value": 202,
                    "display_name": "RESTARTNOTIFICATIONRECIPIENTS",
                },
                {
                    "name": "TIMEOFDEVICERESTART",
                    "value": 203,
                    "display_name": "TIMEOFDEVICERESTART",
                },
                {
                    "name": "TIMESYNCHRONIZATIONINTERVAL",
                    "value": 204,
                    "display_name": "TIMESYNCHRONIZATIONINTERVAL",
                },
                {"name": "TRIGGER", "value": 205, "display_name": "TRIGGER"},
                {
                    "name": "UTCTIMESYNCHRONIZATIONRECIPIENTS",
                    "value": 206,
                    "display_name": "UTCTIMESYNCHRONIZATIONRECIPIENTS",
                },
                {"name": "NODESUBTYPE", "value": 207, "display_name": "NODESUBTYPE"},
                {"name": "NODETYPE", "value": 208, "display_name": "NODETYPE"},
                {
                    "name": "STRUCTUREDOBJECTLIST",
                    "value": 209,
                    "display_name": "STRUCTUREDOBJECTLIST",
                },
                {
                    "name": "SUBORDINATEANNOTATIONS",
                    "value": 210,
                    "display_name": "SUBORDINATEANNOTATIONS",
                },
                {
                    "name": "SUBORDINATELIST",
                    "value": 211,
                    "display_name": "SUBORDINATELIST",
                },
                {
                    "name": "ACTUALSHEDLEVEL",
                    "value": 212,
                    "display_name": "ACTUALSHEDLEVEL",
                },
                {"name": "DUTYWINDOW", "value": 213, "display_name": "DUTYWINDOW"},
                {
                    "name": "EXPECTEDSHEDLEVEL",
                    "value": 214,
                    "display_name": "EXPECTEDSHEDLEVEL",
                },
                {
                    "name": "FULLDUTYBASELINE",
                    "value": 215,
                    "display_name": "FULLDUTYBASELINE",
                },
                {
                    "name": "UNASSIGNED_216",
                    "value": 216,
                    "display_name": "UNASSIGNED_216",
                },
                {
                    "name": "UNASSIGNED_217",
                    "value": 217,
                    "display_name": "UNASSIGNED_217",
                },
                {
                    "name": "REQUESTEDSHEDLEVEL",
                    "value": 218,
                    "display_name": "REQUESTEDSHEDLEVEL",
                },
                {"name": "SHEDDURATION", "value": 219, "display_name": "SHEDDURATION"},
                {
                    "name": "SHEDLEVELDESCRIPTIONS",
                    "value": 220,
                    "display_name": "SHEDLEVELDESCRIPTIONS",
                },
                {"name": "SHEDLEVELS", "value": 221, "display_name": "SHEDLEVELS"},
                {
                    "name": "STATEDESCRIPTION",
                    "value": 222,
                    "display_name": "STATEDESCRIPTION",
                },
                {
                    "name": "UNASSIGNED_223",
                    "value": 223,
                    "display_name": "UNASSIGNED_223",
                },
                {
                    "name": "UNASSIGNED_224",
                    "value": 224,
                    "display_name": "UNASSIGNED_224",
                },
                {
                    "name": "UNASSIGNED_225",
                    "value": 225,
                    "display_name": "UNASSIGNED_225",
                },
                {
                    "name": "DOORALARMSTATE",
                    "value": 226,
                    "display_name": "DOORALARMSTATE",
                },
                {
                    "name": "DOOREXTENDEDPULSETIME",
                    "value": 227,
                    "display_name": "DOOREXTENDEDPULSETIME",
                },
                {"name": "DOORMEMBERS", "value": 228, "display_name": "DOORMEMBERS"},
                {
                    "name": "DOOROPENTOOLONGTIME",
                    "value": 229,
                    "display_name": "DOOROPENTOOLONGTIME",
                },
                {
                    "name": "DOORPULSETIME",
                    "value": 230,
                    "display_name": "DOORPULSETIME",
                },
                {"name": "DOORSTATUS", "value": 231, "display_name": "DOORSTATUS"},
                {
                    "name": "DOORUNLOCKDELAYTIME",
                    "value": 232,
                    "display_name": "DOORUNLOCKDELAYTIME",
                },
                {"name": "LOCKSTATUS", "value": 233, "display_name": "LOCKSTATUS"},
                {
                    "name": "MASKEDALARMVALUES",
                    "value": 234,
                    "display_name": "MASKEDALARMVALUES",
                },
                {
                    "name": "SECUREDSTATUS",
                    "value": 235,
                    "display_name": "SECUREDSTATUS",
                },
                {
                    "name": "UNASSIGNED_236",
                    "value": 236,
                    "display_name": "UNASSIGNED_236",
                },
                {
                    "name": "UNASSIGNED_237",
                    "value": 237,
                    "display_name": "UNASSIGNED_237",
                },
                {
                    "name": "UNASSIGNED_238",
                    "value": 238,
                    "display_name": "UNASSIGNED_238",
                },
                {
                    "name": "UNASSIGNED_239",
                    "value": 239,
                    "display_name": "UNASSIGNED_239",
                },
                {
                    "name": "UNASSIGNED_240",
                    "value": 240,
                    "display_name": "UNASSIGNED_240",
                },
                {
                    "name": "UNASSIGNED_241",
                    "value": 241,
                    "display_name": "UNASSIGNED_241",
                },
                {
                    "name": "UNASSIGNED_242",
                    "value": 242,
                    "display_name": "UNASSIGNED_242",
                },
                {
                    "name": "UNASSIGNED_243",
                    "value": 243,
                    "display_name": "UNASSIGNED_243",
                },
                {
                    "name": "ABSENTEELIMIT",
                    "value": 244,
                    "display_name": "ABSENTEELIMIT",
                },
                {
                    "name": "ACCESSALARMEVENTS",
                    "value": 245,
                    "display_name": "ACCESSALARMEVENTS",
                },
                {"name": "ACCESSDOORS", "value": 246, "display_name": "ACCESSDOORS"},
                {"name": "ACCESSEVENT", "value": 247, "display_name": "ACCESSEVENT"},
                {
                    "name": "ACCESSEVENTAUTHENTICATIONFACTOR",
                    "value": 248,
                    "display_name": "ACCESSEVENTAUTHENTICATIONFACTOR",
                },
                {
                    "name": "ACCESSEVENTCREDENTIAL",
                    "value": 249,
                    "display_name": "ACCESSEVENTCREDENTIAL",
                },
                {
                    "name": "ACCESSEVENTTIME",
                    "value": 250,
                    "display_name": "ACCESSEVENTTIME",
                },
                {
                    "name": "ACCESSTRANSACTIONEVENTS",
                    "value": 251,
                    "display_name": "ACCESSTRANSACTIONEVENTS",
                },
                {
                    "name": "ACCOMPANIMENT",
                    "value": 252,
                    "display_name": "ACCOMPANIMENT",
                },
                {
                    "name": "ACCOMPANIMENTTIME",
                    "value": 253,
                    "display_name": "ACCOMPANIMENTTIME",
                },
                {
                    "name": "ACTIVATIONTIME",
                    "value": 254,
                    "display_name": "ACTIVATIONTIME",
                },
                {
                    "name": "ACTIVEAUTHENTICATIONPOLICY",
                    "value": 255,
                    "display_name": "ACTIVEAUTHENTICATIONPOLICY",
                },
                {
                    "name": "ASSIGNEDACCESSRIGHTS",
                    "value": 256,
                    "display_name": "ASSIGNEDACCESSRIGHTS",
                },
                {
                    "name": "AUTHENTICATIONFACTORS",
                    "value": 257,
                    "display_name": "AUTHENTICATIONFACTORS",
                },
                {
                    "name": "AUTHENTICATIONPOLICYLIST",
                    "value": 258,
                    "display_name": "AUTHENTICATIONPOLICYLIST",
                },
                {
                    "name": "AUTHENTICATIONPOLICYNAMES",
                    "value": 259,
                    "display_name": "AUTHENTICATIONPOLICYNAMES",
                },
                {
                    "name": "AUTHENTICATIONSTATUS",
                    "value": 260,
                    "display_name": "AUTHENTICATIONSTATUS",
                },
                {
                    "name": "AUTHORIZATIONMODE",
                    "value": 261,
                    "display_name": "AUTHORIZATIONMODE",
                },
                {"name": "BELONGSTO", "value": 262, "display_name": "BELONGSTO"},
                {
                    "name": "CREDENTIALDISABLE",
                    "value": 263,
                    "display_name": "CREDENTIALDISABLE",
                },
                {
                    "name": "CREDENTIALSTATUS",
                    "value": 264,
                    "display_name": "CREDENTIALSTATUS",
                },
                {"name": "CREDENTIALS", "value": 265, "display_name": "CREDENTIALS"},
                {
                    "name": "CREDENTIALSINZONE",
                    "value": 266,
                    "display_name": "CREDENTIALSINZONE",
                },
                {
                    "name": "DAYSREMAINING",
                    "value": 267,
                    "display_name": "DAYSREMAINING",
                },
                {"name": "ENTRYPOINTS", "value": 268, "display_name": "ENTRYPOINTS"},
                {"name": "EXITPOINTS", "value": 269, "display_name": "EXITPOINTS"},
                {"name": "EXPIRYTIME", "value": 270, "display_name": "EXPIRYTIME"},
                {
                    "name": "EXTENDEDTIMEENABLE",
                    "value": 271,
                    "display_name": "EXTENDEDTIMEENABLE",
                },
                {
                    "name": "FAILEDATTEMPTEVENTS",
                    "value": 272,
                    "display_name": "FAILEDATTEMPTEVENTS",
                },
                {
                    "name": "FAILEDATTEMPTS",
                    "value": 273,
                    "display_name": "FAILEDATTEMPTS",
                },
                {
                    "name": "FAILEDATTEMPTSTIME",
                    "value": 274,
                    "display_name": "FAILEDATTEMPTSTIME",
                },
                {
                    "name": "LASTACCESSEVENT",
                    "value": 275,
                    "display_name": "LASTACCESSEVENT",
                },
                {
                    "name": "LASTACCESSPOINT",
                    "value": 276,
                    "display_name": "LASTACCESSPOINT",
                },
                {
                    "name": "LASTCREDENTIALADDED",
                    "value": 277,
                    "display_name": "LASTCREDENTIALADDED",
                },
                {
                    "name": "LASTCREDENTIALADDEDTIME",
                    "value": 278,
                    "display_name": "LASTCREDENTIALADDEDTIME",
                },
                {
                    "name": "LASTCREDENTIALREMOVED",
                    "value": 279,
                    "display_name": "LASTCREDENTIALREMOVED",
                },
                {
                    "name": "LASTCREDENTIALREMOVEDTIME",
                    "value": 280,
                    "display_name": "LASTCREDENTIALREMOVEDTIME",
                },
                {"name": "LASTUSETIME", "value": 281, "display_name": "LASTUSETIME"},
                {"name": "LOCKOUT", "value": 282, "display_name": "LOCKOUT"},
                {
                    "name": "LOCKOUTRELINQUISHTIME",
                    "value": 283,
                    "display_name": "LOCKOUTRELINQUISHTIME",
                },
                {
                    "name": "REMOVED IN VERSION 1 REVISION 13_284",
                    "value": 284,
                    "display_name": "REMOVED IN VERSION 1 REVISION 13_284",
                },
                {
                    "name": "MAXFAILEDATTEMPTS",
                    "value": 285,
                    "display_name": "MAXFAILEDATTEMPTS",
                },
                {"name": "MEMBERS", "value": 286, "display_name": "MEMBERS"},
                {"name": "MUSTERPOINT", "value": 287, "display_name": "MUSTERPOINT"},
                {
                    "name": "NEGATIVEACCESSRULES",
                    "value": 288,
                    "display_name": "NEGATIVEACCESSRULES",
                },
                {
                    "name": "NUMBEROFAUTHENTICATIONPOLICIES",
                    "value": 289,
                    "display_name": "NUMBEROFAUTHENTICATIONPOLICIES",
                },
                {
                    "name": "OCCUPANCYCOUNT",
                    "value": 290,
                    "display_name": "OCCUPANCYCOUNT",
                },
                {
                    "name": "OCCUPANCYCOUNTADJUST",
                    "value": 291,
                    "display_name": "OCCUPANCYCOUNTADJUST",
                },
                {
                    "name": "OCCUPANCYCOUNTENABLE",
                    "value": 292,
                    "display_name": "OCCUPANCYCOUNTENABLE",
                },
                {
                    "name": "REMOVED IN VERSION 1 REVISION 13_293",
                    "value": 293,
                    "display_name": "REMOVED IN VERSION 1 REVISION 13_293",
                },
                {
                    "name": "OCCUPANCYLOWERLIMIT",
                    "value": 294,
                    "display_name": "OCCUPANCYLOWERLIMIT",
                },
                {
                    "name": "OCCUPANCYLOWERLIMITENFORCED",
                    "value": 295,
                    "display_name": "OCCUPANCYLOWERLIMITENFORCED",
                },
                {
                    "name": "OCCUPANCYSTATE",
                    "value": 296,
                    "display_name": "OCCUPANCYSTATE",
                },
                {
                    "name": "OCCUPANCYUPPERLIMIT",
                    "value": 297,
                    "display_name": "OCCUPANCYUPPERLIMIT",
                },
                {
                    "name": "OCCUPANCYUPPERLIMITENFORCED",
                    "value": 298,
                    "display_name": "OCCUPANCYUPPERLIMITENFORCED",
                },
                {
                    "name": "REMOVED IN VERSION 1 REVISION 13_299",
                    "value": 299,
                    "display_name": "REMOVED IN VERSION 1 REVISION 13_299",
                },
                {"name": "PASSBACKMODE", "value": 300, "display_name": "PASSBACKMODE"},
                {
                    "name": "PASSBACKTIMEOUT",
                    "value": 301,
                    "display_name": "PASSBACKTIMEOUT",
                },
                {
                    "name": "POSITIVEACCESSRULES",
                    "value": 302,
                    "display_name": "POSITIVEACCESSRULES",
                },
                {
                    "name": "REASONFORDISABLE",
                    "value": 303,
                    "display_name": "REASONFORDISABLE",
                },
                {
                    "name": "SUPPORTEDFORMATS",
                    "value": 304,
                    "display_name": "SUPPORTEDFORMATS",
                },
                {
                    "name": "SUPPORTEDFORMATCLASSES",
                    "value": 305,
                    "display_name": "SUPPORTEDFORMATCLASSES",
                },
                {
                    "name": "THREATAUTHORITY",
                    "value": 306,
                    "display_name": "THREATAUTHORITY",
                },
                {"name": "THREATLEVEL", "value": 307, "display_name": "THREATLEVEL"},
                {"name": "TRACEFLAG", "value": 308, "display_name": "TRACEFLAG"},
                {
                    "name": "TRANSACTIONNOTIFICATIONCLASS",
                    "value": 309,
                    "display_name": "TRANSACTIONNOTIFICATIONCLASS",
                },
                {
                    "name": "USEREXTERNALIDENTIFIER",
                    "value": 310,
                    "display_name": "USEREXTERNALIDENTIFIER",
                },
                {
                    "name": "USERINFORMATIONREFERENCE",
                    "value": 311,
                    "display_name": "USERINFORMATIONREFERENCE",
                },
                {
                    "name": "UNASSIGNED_312",
                    "value": 312,
                    "display_name": "UNASSIGNED_312",
                },
                {
                    "name": "UNASSIGNED_313",
                    "value": 313,
                    "display_name": "UNASSIGNED_313",
                },
                {
                    "name": "UNASSIGNED_314",
                    "value": 314,
                    "display_name": "UNASSIGNED_314",
                },
                {
                    "name": "UNASSIGNED_315",
                    "value": 315,
                    "display_name": "UNASSIGNED_315",
                },
                {
                    "name": "UNASSIGNED_316",
                    "value": 316,
                    "display_name": "UNASSIGNED_316",
                },
                {"name": "USERNAME", "value": 317, "display_name": "USERNAME"},
                {"name": "USERTYPE", "value": 318, "display_name": "USERTYPE"},
                {
                    "name": "USESREMAINING",
                    "value": 319,
                    "display_name": "USESREMAINING",
                },
                {"name": "ZONEFROM", "value": 320, "display_name": "ZONEFROM"},
                {"name": "ZONETO", "value": 321, "display_name": "ZONETO"},
                {
                    "name": "ACCESSEVENTTAG",
                    "value": 322,
                    "display_name": "ACCESSEVENTTAG",
                },
                {
                    "name": "GLOBALIDENTIFIER",
                    "value": 323,
                    "display_name": "GLOBALIDENTIFIER",
                },
                {
                    "name": "UNASSIGNED_324",
                    "value": 324,
                    "display_name": "UNASSIGNED_324",
                },
                {
                    "name": "UNASSIGNED_325",
                    "value": 325,
                    "display_name": "UNASSIGNED_325",
                },
                {
                    "name": "VERIFICATIONTIME",
                    "value": 326,
                    "display_name": "VERIFICATIONTIME",
                },
                {
                    "name": "BASEDEVICESECURITYPOLICY",
                    "value": 327,
                    "display_name": "BASEDEVICESECURITYPOLICY",
                },
                {
                    "name": "DISTRIBUTIONKEYREVISION",
                    "value": 328,
                    "display_name": "DISTRIBUTIONKEYREVISION",
                },
                {"name": "DONOTHIDE", "value": 329, "display_name": "DONOTHIDE"},
                {"name": "KEYSETS", "value": 330, "display_name": "KEYSETS"},
                {
                    "name": "LASTKEYSERVER",
                    "value": 331,
                    "display_name": "LASTKEYSERVER",
                },
                {
                    "name": "NETWORKACCESSSECURITYPOLICIES",
                    "value": 332,
                    "display_name": "NETWORKACCESSSECURITYPOLICIES",
                },
                {
                    "name": "PACKETREORDERTIME",
                    "value": 333,
                    "display_name": "PACKETREORDERTIME",
                },
                {
                    "name": "SECURITYPDUTIMEOUT",
                    "value": 334,
                    "display_name": "SECURITYPDUTIMEOUT",
                },
                {
                    "name": "SECURITYTIMEWINDOW",
                    "value": 335,
                    "display_name": "SECURITYTIMEWINDOW",
                },
                {
                    "name": "SUPPORTEDSECURITYALGORITHMS",
                    "value": 336,
                    "display_name": "SUPPORTEDSECURITYALGORITHMS",
                },
                {
                    "name": "UPDATEKEYSETTIMEOUT",
                    "value": 337,
                    "display_name": "UPDATEKEYSETTIMEOUT",
                },
                {
                    "name": "BACKUPANDRESTORESTATE",
                    "value": 338,
                    "display_name": "BACKUPANDRESTORESTATE",
                },
                {
                    "name": "BACKUPPREPARATIONTIME",
                    "value": 339,
                    "display_name": "BACKUPPREPARATIONTIME",
                },
                {
                    "name": "RESTORECOMPLETIONTIME",
                    "value": 340,
                    "display_name": "RESTORECOMPLETIONTIME",
                },
                {
                    "name": "RESTOREPREPARATIONTIME",
                    "value": 341,
                    "display_name": "RESTOREPREPARATIONTIME",
                },
                {"name": "BITMASK", "value": 342, "display_name": "BITMASK"},
                {"name": "BITTEXT", "value": 343, "display_name": "BITTEXT"},
                {"name": "ISUTC", "value": 344, "display_name": "ISUTC"},
                {"name": "GROUPMEMBERS", "value": 345, "display_name": "GROUPMEMBERS"},
                {
                    "name": "GROUPMEMBERNAMES",
                    "value": 346,
                    "display_name": "GROUPMEMBERNAMES",
                },
                {
                    "name": "MEMBERSTATUSFLAGS",
                    "value": 347,
                    "display_name": "MEMBERSTATUSFLAGS",
                },
                {
                    "name": "REQUESTEDUPDATEINTERVAL",
                    "value": 348,
                    "display_name": "REQUESTEDUPDATEINTERVAL",
                },
                {"name": "COVUPERIOD", "value": 349, "display_name": "COVUPERIOD"},
                {
                    "name": "COVURECIPIENTS",
                    "value": 350,
                    "display_name": "COVURECIPIENTS",
                },
                {
                    "name": "EVENTMESSAGETEXTS",
                    "value": 351,
                    "display_name": "EVENTMESSAGETEXTS",
                },
                {
                    "name": "EVENTMESSAGETEXTSCONFIG",
                    "value": 352,
                    "display_name": "EVENTMESSAGETEXTSCONFIG",
                },
                {
                    "name": "EVENTDETECTIONENABLE",
                    "value": 353,
                    "display_name": "EVENTDETECTIONENABLE",
                },
                {
                    "name": "EVENTALGORITHMINHIBIT",
                    "value": 354,
                    "display_name": "EVENTALGORITHMINHIBIT",
                },
                {
                    "name": "EVENTALGORITHMINHIBITREF",
                    "value": 355,
                    "display_name": "EVENTALGORITHMINHIBITREF",
                },
                {
                    "name": "TIMEDELAYNORMAL",
                    "value": 356,
                    "display_name": "TIMEDELAYNORMAL",
                },
                {
                    "name": "RELIABILITYEVALUATIONINHIBIT",
                    "value": 357,
                    "display_name": "RELIABILITYEVALUATIONINHIBIT",
                },
                {
                    "name": "FAULTPARAMETERS",
                    "value": 358,
                    "display_name": "FAULTPARAMETERS",
                },
                {"name": "FAULTTYPE", "value": 359, "display_name": "FAULTTYPE"},
                {
                    "name": "LOCALFORWARDINGONLY",
                    "value": 360,
                    "display_name": "LOCALFORWARDINGONLY",
                },
                {
                    "name": "PROCESSIDENTIFIERFILTER",
                    "value": 361,
                    "display_name": "PROCESSIDENTIFIERFILTER",
                },
                {
                    "name": "SUBSCRIBEDRECIPIENTS",
                    "value": 362,
                    "display_name": "SUBSCRIBEDRECIPIENTS",
                },
                {"name": "PORTFILTER", "value": 363, "display_name": "PORTFILTER"},
                {
                    "name": "AUTHORIZATIONEXEMPTIONS",
                    "value": 364,
                    "display_name": "AUTHORIZATIONEXEMPTIONS",
                },
                {
                    "name": "ALLOWGROUPDELAYINHIBIT",
                    "value": 365,
                    "display_name": "ALLOWGROUPDELAYINHIBIT",
                },
                {
                    "name": "CHANNELNUMBER",
                    "value": 366,
                    "display_name": "CHANNELNUMBER",
                },
                {
                    "name": "CONTROLGROUPS",
                    "value": 367,
                    "display_name": "CONTROLGROUPS",
                },
                {
                    "name": "EXECUTIONDELAY",
                    "value": 368,
                    "display_name": "EXECUTIONDELAY",
                },
                {"name": "LASTPRIORITY", "value": 369, "display_name": "LASTPRIORITY"},
                {"name": "WRITESTATUS", "value": 370, "display_name": "WRITESTATUS"},
                {"name": "PROPERTYLIST", "value": 371, "display_name": "PROPERTYLIST"},
                {"name": "SERIALNUMBER", "value": 372, "display_name": "SERIALNUMBER"},
                {
                    "name": "BLINKWARNENABLE",
                    "value": 373,
                    "display_name": "BLINKWARNENABLE",
                },
                {
                    "name": "DEFAULTFADETIME",
                    "value": 374,
                    "display_name": "DEFAULTFADETIME",
                },
                {
                    "name": "DEFAULTRAMPRATE",
                    "value": 375,
                    "display_name": "DEFAULTRAMPRATE",
                },
                {
                    "name": "DEFAULTSTEPINCREMENT",
                    "value": 376,
                    "display_name": "DEFAULTSTEPINCREMENT",
                },
                {"name": "EGRESSTIME", "value": 377, "display_name": "EGRESSTIME"},
                {"name": "INPROGRESS", "value": 378, "display_name": "INPROGRESS"},
                {
                    "name": "INSTANTANEOUSPOWER",
                    "value": 379,
                    "display_name": "INSTANTANEOUSPOWER",
                },
                {
                    "name": "LIGHTINGCOMMAND",
                    "value": 380,
                    "display_name": "LIGHTINGCOMMAND",
                },
                {
                    "name": "LIGHTINGCOMMANDDEFAULTPRIORITY",
                    "value": 381,
                    "display_name": "LIGHTINGCOMMANDDEFAULTPRIORITY",
                },
                {
                    "name": "MAXACTUALVALUE",
                    "value": 382,
                    "display_name": "MAXACTUALVALUE",
                },
                {
                    "name": "MINACTUALVALUE",
                    "value": 383,
                    "display_name": "MINACTUALVALUE",
                },
                {"name": "POWER", "value": 384, "display_name": "POWER"},
                {"name": "TRANSITION", "value": 385, "display_name": "TRANSITION"},
                {"name": "EGRESSACTIVE", "value": 386, "display_name": "EGRESSACTIVE"},
            ]
        },
    ),
    (
        "ns=1;i=3049",
        "BACnetReinitializedStateofDevice",
        {
            "fields": [
                {"name": "COLDSTART", "value": 0, "display_name": "COLDSTART"},
                {"name": "WARMSTART", "value": 1, "display_name": "WARMSTART"},
                {"name": "STARTBACKUP", "value": 2, "display_name": "STARTBACKUP"},
                {"name": "ENDBACKUP", "value": 3, "display_name": "ENDBACKUP"},
                {"name": "STARTRESTORE", "value": 4, "display_name": "STARTRESTORE"},
                {"name": "ENDRESTORE", "value": 5, "display_name": "ENDRESTORE"},
                {"name": "ABORTRESTORE", "value": 6, "display_name": "ABORTRESTORE"},
            ]
        },
    ),
    (
        "ns=1;i=3001",
        "BACnetReliability",
        {
            "fields": [
                {
                    "name": "NOFAULTDETECTED",
                    "value": 0,
                    "display_name": "NOFAULTDETECTED",
                },
                {"name": "NOSENSOR", "value": 1, "display_name": "NOSENSOR"},
                {"name": "OVERRANGE", "value": 2, "display_name": "OVERRANGE"},
                {"name": "UNDERRANGE", "value": 3, "display_name": "UNDERRANGE"},
                {"name": "OPENLOOP", "value": 4, "display_name": "OPENLOOP"},
                {"name": "SHORTEDLOOP", "value": 5, "display_name": "SHORTEDLOOP"},
                {"name": "NOOUTPUT", "value": 6, "display_name": "NOOUTPUT"},
                {
                    "name": "UNRELIABLEOTHER",
                    "value": 7,
                    "display_name": "UNRELIABLEOTHER",
                },
                {"name": "PROCESSERROR", "value": 8, "display_name": "PROCESSERROR"},
                {
                    "name": "MULTISTATEFAULT",
                    "value": 9,
                    "display_name": "MULTISTATEFAULT",
                },
                {
                    "name": "CONFIGURATIONERROR",
                    "value": 10,
                    "display_name": "CONFIGURATIONERROR",
                },
                {
                    "name": "COMMUNICATIONFAILURE",
                    "value": 12,
                    "display_name": "COMMUNICATIONFAILURE",
                },
                {"name": "MEMBERFAULT", "value": 13, "display_name": "MEMBERFAULT"},
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
                {"name": "UNKNOWN", "value": 0, "display_name": "UNKNOWN"},
                {"name": "COLDSTART", "value": 1, "display_name": "COLDSTART"},
                {"name": "WARMSTART", "value": 2, "display_name": "WARMSTART"},
                {
                    "name": "DETECTED_POWER_LOST",
                    "value": 3,
                    "display_name": "DETECTED_POWER_LOST",
                },
                {
                    "name": "DETECTED_POWERED_OFF",
                    "value": 4,
                    "display_name": "DETECTED_POWERED_OFF",
                },
                {
                    "name": "HARDWARE_WATCHDOG",
                    "value": 5,
                    "display_name": "HARDWARE_WATCHDOG",
                },
                {
                    "name": "SOFTWARE_WATCHDOG",
                    "value": 6,
                    "display_name": "SOFTWARE_WATCHDOG",
                },
                {"name": "SUSPENDED", "value": 7, "display_name": "SUSPENDED"},
            ]
        },
    ),
    (
        "ns=1;i=103011",
        "BACnetSegmentation",
        {
            "fields": [
                {
                    "name": "SEGMENTED-BOTH",
                    "value": 0,
                    "display_name": "SEGMENTED-BOTH",
                },
                {
                    "name": "SEGMENTED-TRANSMIT",
                    "value": 1,
                    "display_name": "SEGMENTED-TRANSMIT",
                },
                {
                    "name": "SEGMENTED-RECEIVE",
                    "value": 2,
                    "display_name": "SEGMENTED-RECEIVE",
                },
                {
                    "name": "NO-SEGMENTATION",
                    "value": 3,
                    "display_name": "NO-SEGMENTATION",
                },
            ]
        },
    ),
    (
        "ns=1;i=3060",
        "BACnetDaysOfWeek",
        {
            "fields": [
                {"name": "MONDAY", "value": 0, "display_name": "MONDAY"},
                {"name": "TUESDAY", "value": 1, "display_name": "TUESDAY"},
                {"name": "WEDNESDAY", "value": 2, "display_name": "WEDNESDAY"},
                {"name": "THURSDAY", "value": 3, "display_name": "THURSDAY"},
                {"name": "FRIDAY", "value": 4, "display_name": "FRIDAY"},
                {"name": "SATURDAY", "value": 5, "display_name": "SATURDAY"},
                {"name": "SUNDAY", "value": 6, "display_name": "SUNDAY"},
            ]
        },
    ),
    (
        "ns=1;i=3061",
        "BACnetEventTransitionBits",
        {
            "fields": [
                {"name": "TO-OFFNORMAL", "value": 0, "display_name": "TO-OFFNORMAL"},
                {"name": "TO-FAULT", "value": 1, "display_name": "TO-FAULT"},
                {"name": "TO-NORMAL", "value": 2, "display_name": "TO-NORMAL"},
            ]
        },
    ),
    (
        "ns=1;i=3062",
        "BACnetLimitEnable",
        {
            "fields": [
                {
                    "name": "LOWLIMITENABLE",
                    "value": 0,
                    "display_name": "LOWLIMITENABLE",
                },
                {
                    "name": "HIGHLIMITENABLE",
                    "value": 1,
                    "display_name": "HIGHLIMITENABLE",
                },
            ]
        },
    ),
    (
        "ns=1;i=3063",
        "BACnetObjectTypeSupportedBits",
        {
            "fields": [
                {"name": "ANALOG-INPUT", "value": 0, "display_name": "ANALOG-INPUT"},
                {"name": "ANALOG-OUTPUT", "value": 1, "display_name": "ANALOG-OUTPUT"},
                {"name": "ANALOG-VALUE", "value": 2, "display_name": "ANALOG-VALUE"},
                {"name": "BINARY-INPUT", "value": 3, "display_name": "BINARY-INPUT"},
                {"name": "BINARY-OUTPUT", "value": 4, "display_name": "BINARY-OUTPUT"},
                {"name": "BINARY-VALUE", "value": 5, "display_name": "BINARY-VALUE"},
                {"name": "CALENDAR", "value": 6, "display_name": "CALENDAR"},
                {"name": "COMMAND", "value": 7, "display_name": "COMMAND"},
                {"name": "DEVICE", "value": 8, "display_name": "DEVICE"},
                {
                    "name": "EVENT-ENROLLMENT",
                    "value": 9,
                    "display_name": "EVENT-ENROLLMENT",
                },
                {"name": "FILE", "value": 10, "display_name": "FILE"},
                {"name": "GROUP", "value": 11, "display_name": "GROUP"},
                {"name": "LOOP", "value": 12, "display_name": "LOOP"},
                {
                    "name": "MULTI-STATE-INPUT",
                    "value": 13,
                    "display_name": "MULTI-STATE-INPUT",
                },
                {
                    "name": "MULTI-STATE-OUTPUT",
                    "value": 14,
                    "display_name": "MULTI-STATE-OUTPUT",
                },
                {
                    "name": "NOTIFICATION-CLASS",
                    "value": 15,
                    "display_name": "NOTIFICATION-CLASS",
                },
                {"name": "PROGRAM", "value": 16, "display_name": "PROGRAM"},
                {"name": "SCHEDULE", "value": 17, "display_name": "SCHEDULE"},
                {"name": "AVERAGING", "value": 18, "display_name": "AVERAGING"},
                {
                    "name": "MULTI-STATE-VALUE",
                    "value": 19,
                    "display_name": "MULTI-STATE-VALUE",
                },
                {"name": "TREND-LOG", "value": 20, "display_name": "TREND-LOG"},
                {
                    "name": "LIFE-SAFETY-POINT",
                    "value": 21,
                    "display_name": "LIFE-SAFETY-POINT",
                },
                {
                    "name": "LIFE-SAFETY-ZONE",
                    "value": 22,
                    "display_name": "LIFE-SAFETY-ZONE",
                },
                {"name": "ACCUMULATOR", "value": 23, "display_name": "ACCUMULATOR"},
                {
                    "name": "PULSE-CONVERTER",
                    "value": 24,
                    "display_name": "PULSE-CONVERTER",
                },
                {"name": "EVENT-LOG", "value": 25, "display_name": "EVENT-LOG"},
                {"name": "GLOBAL-GROUP", "value": 26, "display_name": "GLOBAL-GROUP"},
                {
                    "name": "TREND-LOG-MULTIPLE",
                    "value": 27,
                    "display_name": "TREND-LOG-MULTIPLE",
                },
                {"name": "LOAD-CONTROL", "value": 28, "display_name": "LOAD-CONTROL"},
                {
                    "name": "STRUCTURED-VIEW",
                    "value": 29,
                    "display_name": "STRUCTURED-VIEW",
                },
                {"name": "ACCESS-DOOR", "value": 30, "display_name": "ACCESS-DOOR"},
                {"name": "UNASSIGNED_31", "value": 31, "display_name": "UNASSIGNED_31"},
                {
                    "name": "ACCESS-CREDENTIAL",
                    "value": 32,
                    "display_name": "ACCESS-CREDENTIAL",
                },
                {"name": "ACCESS-POINT", "value": 33, "display_name": "ACCESS-POINT"},
                {"name": "ACCESS-RIGHTS", "value": 34, "display_name": "ACCESS-RIGHTS"},
                {"name": "ACCESS-USER", "value": 35, "display_name": "ACCESS-USER"},
                {"name": "ACCESS-ZONE", "value": 36, "display_name": "ACCESS-ZONE"},
                {
                    "name": "CREDENTIAL-DATA-INPUT",
                    "value": 37,
                    "display_name": "CREDENTIAL-DATA-INPUT",
                },
                {
                    "name": "NETWORK-SECURITY",
                    "value": 38,
                    "display_name": "NETWORK-SECURITY",
                },
                {
                    "name": "BITSTRING-VALUE",
                    "value": 39,
                    "display_name": "BITSTRING-VALUE",
                },
                {
                    "name": "CHARACTERSTRING-VALUE",
                    "value": 40,
                    "display_name": "CHARACTERSTRING-VALUE",
                },
                {
                    "name": "DATE-PATTERN-VALUE",
                    "value": 41,
                    "display_name": "DATE-PATTERN-VALUE",
                },
                {"name": "DATE-VALUE", "value": 42, "display_name": "DATE-VALUE"},
                {
                    "name": "DATETIME-PATTERN-VALUE",
                    "value": 43,
                    "display_name": "DATETIME-PATTERN-VALUE",
                },
                {
                    "name": "DATETIME-VALUE",
                    "value": 44,
                    "display_name": "DATETIME-VALUE",
                },
                {"name": "INTEGER-VALUE", "value": 45, "display_name": "INTEGER-VALUE"},
                {
                    "name": "LARGE-ANALOG-VALUE",
                    "value": 46,
                    "display_name": "LARGE-ANALOG-VALUE",
                },
                {
                    "name": "OCTETSTRING-VALUE",
                    "value": 47,
                    "display_name": "OCTETSTRING-VALUE",
                },
                {
                    "name": "POSITIVE-INTEGER-VALUE",
                    "value": 48,
                    "display_name": "POSITIVE-INTEGER-VALUE",
                },
                {
                    "name": "TIME-PATTERN-VALUE",
                    "value": 49,
                    "display_name": "TIME-PATTERN-VALUE",
                },
                {"name": "TIME-VALUE", "value": 50, "display_name": "TIME-VALUE"},
                {
                    "name": "NOTIFICATION-FORWARDER",
                    "value": 51,
                    "display_name": "NOTIFICATION-FORWARDER",
                },
                {
                    "name": "ALERT-ENROLLMENT",
                    "value": 52,
                    "display_name": "ALERT-ENROLLMENT",
                },
                {"name": "CHANNEL", "value": 53, "display_name": "CHANNEL"},
                {
                    "name": "LIGHTING-OUTPUT",
                    "value": 54,
                    "display_name": "LIGHTING-OUTPUT",
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
                    "name": "ACKNOWLEDGEALARM",
                    "value": 0,
                    "display_name": "ACKNOWLEDGEALARM",
                },
                {
                    "name": "CONFIRMEDCOVNOTIFICATION",
                    "value": 1,
                    "display_name": "CONFIRMEDCOVNOTIFICATION",
                },
                {
                    "name": "CONFIRMEDEVENTNOTIFICATION",
                    "value": 2,
                    "display_name": "CONFIRMEDEVENTNOTIFICATION",
                },
                {
                    "name": "GETALARMSUMMARY",
                    "value": 3,
                    "display_name": "GETALARMSUMMARY",
                },
                {
                    "name": "GETENROLLMENTSUMMARY",
                    "value": 4,
                    "display_name": "GETENROLLMENTSUMMARY",
                },
                {"name": "SUBSCRIBECOV", "value": 5, "display_name": "SUBSCRIBECOV"},
                {
                    "name": "ATOMICREADFILE",
                    "value": 6,
                    "display_name": "ATOMICREADFILE",
                },
                {
                    "name": "ATOMICWRITEFILE",
                    "value": 7,
                    "display_name": "ATOMICWRITEFILE",
                },
                {
                    "name": "ADDLISTELEMENT",
                    "value": 8,
                    "display_name": "ADDLISTELEMENT",
                },
                {
                    "name": "REMOVELISTELEMENT",
                    "value": 9,
                    "display_name": "REMOVELISTELEMENT",
                },
                {"name": "CREATEOBJECT", "value": 10, "display_name": "CREATEOBJECT"},
                {"name": "DELETEOBJECT", "value": 11, "display_name": "DELETEOBJECT"},
                {"name": "READPROPERTY", "value": 12, "display_name": "READPROPERTY"},
                {"name": "UNASSIGNED_13", "value": 13, "display_name": "UNASSIGNED_13"},
                {
                    "name": "READPROPERTYMULTIPLE",
                    "value": 14,
                    "display_name": "READPROPERTYMULTIPLE",
                },
                {"name": "WRITEPROPERTY", "value": 15, "display_name": "WRITEPROPERTY"},
                {
                    "name": "WRITEPROPERTYMULTIPLE",
                    "value": 16,
                    "display_name": "WRITEPROPERTYMULTIPLE",
                },
                {
                    "name": "DEVICECOMMUNICATIONCONTROL",
                    "value": 17,
                    "display_name": "DEVICECOMMUNICATIONCONTROL",
                },
                {
                    "name": "CONFIRMEDPRIVATETRANSFER",
                    "value": 18,
                    "display_name": "CONFIRMEDPRIVATETRANSFER",
                },
                {
                    "name": "REINITIALIZEDEVICE",
                    "value": 19,
                    "display_name": "REINITIALIZEDEVICE",
                },
                {"name": "VTOPEN", "value": 20, "display_name": "VTOPEN"},
                {"name": "VTCLOSE", "value": 21, "display_name": "VTCLOSE"},
                {"name": "VTDATA", "value": 22, "display_name": "VTDATA"},
                {"name": "UNASSIGNED_24", "value": 23, "display_name": "UNASSIGNED_24"},
                {"name": "UNASSIGNED_25", "value": 24, "display_name": "UNASSIGNED_25"},
                {"name": "I-AM", "value": 25, "display_name": "I-AM"},
                {"name": "I-HAVE", "value": 26, "display_name": "I-HAVE"},
                {
                    "name": "UNCONFIRMEDCOVNOTIFICATION",
                    "value": 27,
                    "display_name": "UNCONFIRMEDCOVNOTIFICATION",
                },
                {
                    "name": "UNCONFIRMEDEVENTNOTIFICATION",
                    "value": 28,
                    "display_name": "UNCONFIRMEDEVENTNOTIFICATION",
                },
                {
                    "name": "UNCONFIRMEDPRIVATETRANSFER",
                    "value": 29,
                    "display_name": "UNCONFIRMEDPRIVATETRANSFER",
                },
                {
                    "name": "UNCONFIRMEDTEXTMESSAGE",
                    "value": 30,
                    "display_name": "UNCONFIRMEDTEXTMESSAGE",
                },
                {
                    "name": "TIMESYNCHRONIZATION",
                    "value": 31,
                    "display_name": "TIMESYNCHRONIZATION",
                },
                {"name": "WHO-HAS", "value": 32, "display_name": "WHO-HAS"},
                {"name": "WHO-IS", "value": 33, "display_name": "WHO-IS"},
                {"name": "READRANGE", "value": 34, "display_name": "READRANGE"},
                {
                    "name": "UTCTIMESYNCHRONIZATION",
                    "value": 35,
                    "display_name": "UTCTIMESYNCHRONIZATION",
                },
                {
                    "name": "LIFESAFETYOPERATION",
                    "value": 36,
                    "display_name": "LIFESAFETYOPERATION",
                },
                {
                    "name": "SUBSCRIBECOVPROPERTY",
                    "value": 37,
                    "display_name": "SUBSCRIBECOVPROPERTY",
                },
                {
                    "name": "GETEVENTINFORMATION",
                    "value": 38,
                    "display_name": "GETEVENTINFORMATION",
                },
                {"name": "WRITEGROUP", "value": 39, "display_name": "WRITEGROUP"},
            ]
        },
    ),
    (
        "ns=1;i=3065",
        "BACnetStatusFlags",
        {
            "fields": [
                {"name": "INALARM", "value": 0, "display_name": "INALARM"},
                {"name": "FAULT", "value": 1, "display_name": "FAULT"},
                {"name": "OVERRIDEN", "value": 2, "display_name": "OVERRIDEN"},
                {"name": "OUTOFSERVICE", "value": 3, "display_name": "OUTOFSERVICE"},
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
