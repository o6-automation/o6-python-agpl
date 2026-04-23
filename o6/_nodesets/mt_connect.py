# AUTO-GENERATED — DO NOT EDIT
# source-sha256: a9cbddef66c7ed9f5d80a838b07e31ad83f7d103a39a65a8057530b4572b7f84
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/MTConnect/v2/"
_VERSION: str = "2.00.01"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": "1.04.6"}]
_STRUCTURES: list = [
    (
        "ns=1;i=2618",
        "AssetEventDataType",
        "ns=1;i=2745",
        {
            "structure_type": 0,
            "fields": [
                {"name": "AssetId", "data_type": "i=12", "value_rank": -1},
                {"name": "AssetType", "data_type": "i=12", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=2653",
        "MessageDataType",
        "ns=1;i=2903",
        {
            "structure_type": 1,
            "fields": [
                {
                    "name": "NativeCode",
                    "data_type": "i=12",
                    "value_rank": -1,
                    "is_optional": True,
                },
                {"name": "Text", "data_type": "i=12", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=2637",
        "ThreeSpaceSampleDataType",
        "ns=1;i=2909",
        {
            "structure_type": 0,
            "fields": [
                {"name": "X", "data_type": "i=11", "value_rank": -1},
                {"name": "Y", "data_type": "i=11", "value_rank": -1},
                {"name": "Z", "data_type": "i=11", "value_rank": -1},
            ],
        },
    ),
]
_ENUMS: list = [
    (
        "ns=1;i=2634",
        "MTCategoryType",
        {
            "fields": [
                {"name": "EVENT", "value": 0, "display_name": "EVENT"},
                {"name": "CONDITION", "value": 1, "display_name": "CONDITION"},
                {"name": "SAMPLE", "value": 2, "display_name": "SAMPLE"},
            ]
        },
    ),
    (
        "ns=1;i=2635",
        "MTCoordinateSystemType",
        {
            "fields": [
                {"name": "MACHINE", "value": 0, "display_name": "MACHINE"},
                {"name": "WORK", "value": 1, "display_name": "WORK"},
            ]
        },
    ),
    (
        "ns=1;i=2633",
        "MTRepresentationType",
        {
            "fields": [
                {"name": "DISCRETE", "value": 0, "display_name": "DISCRETE"},
                {"name": "TIME_SERIES", "value": 1, "display_name": "TIME_SERIES"},
                {"name": "VALUE", "value": 2, "display_name": "VALUE"},
            ]
        },
    ),
    (
        "ns=1;i=2636",
        "MTResetTriggerType",
        {
            "fields": [
                {
                    "name": "ACTION_COMPLETE",
                    "value": 0,
                    "display_name": "ACTION_COMPLETE",
                },
                {"name": "ANNUAL", "value": 1, "display_name": "ANNUAL"},
                {"name": "DAY", "value": 2, "display_name": "DAY"},
                {"name": "MAINTENANCE", "value": 3, "display_name": "MAINTENANCE"},
                {"name": "MANUAL", "value": 4, "display_name": "MANUAL"},
                {"name": "MONTH", "value": 5, "display_name": "MONTH"},
                {"name": "POWER_ON", "value": 6, "display_name": "POWER_ON"},
                {"name": "SHIFT", "value": 7, "display_name": "SHIFT"},
                {"name": "WEEK", "value": 8, "display_name": "WEEK"},
            ]
        },
    ),
    (
        "ns=1;i=2659",
        "MTStatisticType",
        {
            "fields": [
                {"name": "AVERAGE", "value": 0, "display_name": "AVERAGE"},
                {"name": "MAXIMUM", "value": 1, "display_name": "MAXIMUM"},
                {"name": "MEDIAN", "value": 2, "display_name": "MEDIAN"},
                {"name": "MINIMUM", "value": 3, "display_name": "MINIMUM"},
                {"name": "MODE", "value": 4, "display_name": "MODE"},
                {"name": "RANGE", "value": 5, "display_name": "RANGE"},
                {
                    "name": "ROOT_MEAN_SQUARE",
                    "value": 6,
                    "display_name": "ROOT_MEAN_SQUARE",
                },
                {
                    "name": "STANDARD_DEVIATION",
                    "value": 7,
                    "display_name": "STANDARD_DEVIATION",
                },
            ]
        },
    ),
    (
        "ns=1;i=2669",
        "MTSeverityDataType",
        {
            "fields": [
                {"name": "FAULT", "value": 0, "display_name": "FAULT"},
                {"name": "NORMAL", "value": 1, "display_name": "NORMAL"},
                {"name": "WARNING", "value": 2, "display_name": "WARNING"},
            ]
        },
    ),
    (
        "ns=1;i=2668",
        "QualifierDataType",
        {
            "fields": [
                {"name": "HIGH", "value": 0, "display_name": "HIGH"},
                {"name": "LOW", "value": 1, "display_name": "LOW"},
            ]
        },
    ),
    (
        "ns=1;i=2197",
        "ActiveStateDataType",
        {
            "fields": [
                {"name": "ACTIVE", "value": 0, "display_name": "ACTIVE"},
                {"name": "INACTIVE", "value": 1, "display_name": "INACTIVE"},
            ]
        },
    ),
    (
        "ns=1;i=2198",
        "AvailabilityDataType",
        {
            "fields": [
                {"name": "AVAILABLE", "value": 0, "display_name": "AVAILABLE"},
                {"name": "UNAVAILABLE", "value": 1, "display_name": "UNAVAILABLE"},
            ]
        },
    ),
    (
        "ns=1;i=2199",
        "AxisCouplingDataType",
        {
            "fields": [
                {"name": "MASTER", "value": 0, "display_name": "MASTER"},
                {"name": "SLAVE", "value": 1, "display_name": "SLAVE"},
                {"name": "SYNCHRONOUS", "value": 2, "display_name": "SYNCHRONOUS"},
                {"name": "TANDEM", "value": 3, "display_name": "TANDEM"},
            ]
        },
    ),
    (
        "ns=1;i=2200",
        "AxisStateDataType",
        {
            "fields": [
                {"name": "HOME", "value": 0, "display_name": "HOME"},
                {"name": "PARKED", "value": 1, "display_name": "PARKED"},
                {"name": "STOPPED", "value": 2, "display_name": "STOPPED"},
                {"name": "TRAVEL", "value": 3, "display_name": "TRAVEL"},
            ]
        },
    ),
    (
        "ns=1;i=2202",
        "CompositionStateDataType",
        {
            "fields": [
                {"name": "ACTIVE", "value": 0, "display_name": "ACTIVE"},
                {"name": "CLOSED", "value": 1, "display_name": "CLOSED"},
                {"name": "DOWN", "value": 2, "display_name": "DOWN"},
                {"name": "INACTIVE", "value": 3, "display_name": "INACTIVE"},
                {"name": "LEFT", "value": 4, "display_name": "LEFT"},
                {"name": "OFF", "value": 5, "display_name": "OFF"},
                {"name": "ON", "value": 6, "display_name": "ON"},
                {"name": "OPEN", "value": 7, "display_name": "OPEN"},
                {"name": "RIGHT", "value": 8, "display_name": "RIGHT"},
                {"name": "TRANSITIONING", "value": 9, "display_name": "TRANSITIONING"},
                {"name": "UNLATCHED", "value": 10, "display_name": "UNLATCHED"},
                {"name": "UP", "value": 11, "display_name": "UP"},
            ]
        },
    ),
    (
        "ns=1;i=2203",
        "ControllerModeDataType",
        {
            "fields": [
                {"name": "AUTOMATIC", "value": 0, "display_name": "AUTOMATIC"},
                {"name": "EDIT", "value": 1, "display_name": "EDIT"},
                {"name": "MANUAL", "value": 2, "display_name": "MANUAL"},
                {
                    "name": "MANUAL_DATA_INPUT",
                    "value": 3,
                    "display_name": "MANUAL_DATA_INPUT",
                },
                {
                    "name": "SEMI_AUTOMATIC",
                    "value": 4,
                    "display_name": "SEMI_AUTOMATIC",
                },
            ]
        },
    ),
    (
        "ns=1;i=2205",
        "DirectionDataType",
        {
            "fields": [
                {"name": "CLOCKWISE", "value": 0, "display_name": "CLOCKWISE"},
                {
                    "name": "COUNTER_CLOCKWISE",
                    "value": 1,
                    "display_name": "COUNTER_CLOCKWISE",
                },
                {"name": "NEGATIVE", "value": 2, "display_name": "NEGATIVE"},
                {"name": "POSITIVE", "value": 3, "display_name": "POSITIVE"},
            ]
        },
    ),
    (
        "ns=1;i=2207",
        "EmergencyStopDataType",
        {
            "fields": [
                {"name": "ARMED", "value": 0, "display_name": "ARMED"},
                {"name": "TRIGGERED", "value": 1, "display_name": "TRIGGERED"},
            ]
        },
    ),
    (
        "ns=1;i=2262",
        "ExecutionDataType",
        {
            "fields": [
                {"name": "ACTIVE", "value": 0, "display_name": "ACTIVE"},
                {"name": "FEED_HOLD", "value": 1, "display_name": "FEED_HOLD"},
                {"name": "INTERRUPTED", "value": 2, "display_name": "INTERRUPTED"},
                {"name": "OPTIONAL_STOP", "value": 3, "display_name": "OPTIONAL_STOP"},
                {"name": "READY", "value": 4, "display_name": "READY"},
                {
                    "name": "PROGRAM_COMPLETED",
                    "value": 5,
                    "display_name": "PROGRAM_COMPLETED",
                },
                {
                    "name": "PROGRAM_STOPPED",
                    "value": 6,
                    "display_name": "PROGRAM_STOPPED",
                },
                {"name": "STOPPED", "value": 7, "display_name": "STOPPED"},
            ]
        },
    ),
    (
        "ns=1;i=2208",
        "FunctionalModeDataType",
        {
            "fields": [
                {"name": "MAINTENANCE", "value": 0, "display_name": "MAINTENANCE"},
                {"name": "PRODUCTION", "value": 1, "display_name": "PRODUCTION"},
                {
                    "name": "PROCESS_DEVELOPMENT",
                    "value": 2,
                    "display_name": "PROCESS_DEVELOPMENT",
                },
                {"name": "SETUP", "value": 3, "display_name": "SETUP"},
                {"name": "TEARDOWN", "value": 4, "display_name": "TEARDOWN"},
            ]
        },
    ),
    (
        "ns=1;i=2234",
        "InterfaceStateDataType",
        {
            "fields": [
                {"name": "ACTIVE", "value": 0, "display_name": "ACTIVE"},
                {"name": "COMPLETE", "value": 1, "display_name": "COMPLETE"},
                {"name": "FAIL", "value": 2, "display_name": "FAIL"},
                {"name": "NOT_READY", "value": 4, "display_name": "NOT_READY"},
                {"name": "READY", "value": 5, "display_name": "READY"},
            ]
        },
    ),
    (
        "ns=1;i=2230",
        "InterfaceStatusDataType",
        {
            "fields": [
                {"name": "DISABLED", "value": 0, "display_name": "DISABLED"},
                {"name": "ENABLED", "value": 1, "display_name": "ENABLED"},
            ]
        },
    ),
    (
        "ns=1;i=2204",
        "OnOffDataType",
        {
            "fields": [
                {"name": "OFF", "value": 0, "display_name": "OFF"},
                {"name": "ON", "value": 1, "display_name": "ON"},
            ]
        },
    ),
    (
        "ns=1;i=2201",
        "OpenStateDataType",
        {
            "fields": [
                {"name": "CLOSED", "value": 0, "display_name": "CLOSED"},
                {"name": "OPEN", "value": 1, "display_name": "OPEN"},
                {"name": "UNLATCHED", "value": 2, "display_name": "UNLATCHED"},
            ]
        },
    ),
    (
        "ns=1;i=2209",
        "PathModeDataType",
        {
            "fields": [
                {"name": "INDEPENDENT", "value": 0, "display_name": "INDEPENDENT"},
                {"name": "MASTER", "value": 1, "display_name": "MASTER"},
                {"name": "MIRROR", "value": 2, "display_name": "MIRROR"},
                {"name": "SYNCHRONOUS", "value": 3, "display_name": "SYNCHRONOUS"},
            ]
        },
    ),
    (
        "ns=1;i=2210",
        "ProgramEditDataType",
        {
            "fields": [
                {"name": "ACTIVE", "value": 0, "display_name": "ACTIVE"},
                {"name": "NOT_READY", "value": 1, "display_name": "NOT_READY"},
                {"name": "READY", "value": 2, "display_name": "READY"},
            ]
        },
    ),
    (
        "ns=1;i=2211",
        "RotaryModeDataType",
        {
            "fields": [
                {"name": "CONTOUR", "value": 0, "display_name": "CONTOUR"},
                {"name": "INDEX", "value": 1, "display_name": "INDEX"},
                {"name": "SPINDLE", "value": 2, "display_name": "SPINDLE"},
            ]
        },
    ),
    (
        "ns=1;i=2206",
        "YesNoDataType",
        {
            "fields": [
                {"name": "NO", "value": 0, "display_name": "NO"},
                {"name": "YES", "value": 1, "display_name": "YES"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [
        ("ns=1;i=2618", "ns=1;i=2745", ["i=12", "i=12"]),
        ("ns=1;i=2653", "ns=1;i=2903", ["i=12", "i=12"]),
        ("ns=1;i=2637", "ns=1;i=2909", ["i=11", "i=11", "i=11"]),
    ],
    [
        "ns=1;i=2634",
        "ns=1;i=2635",
        "ns=1;i=2633",
        "ns=1;i=2636",
        "ns=1;i=2659",
        "ns=1;i=2669",
        "ns=1;i=2668",
        "ns=1;i=2197",
        "ns=1;i=2198",
        "ns=1;i=2199",
        "ns=1;i=2200",
        "ns=1;i=2202",
        "ns=1;i=2203",
        "ns=1;i=2205",
        "ns=1;i=2207",
        "ns=1;i=2262",
        "ns=1;i=2208",
        "ns=1;i=2234",
        "ns=1;i=2230",
        "ns=1;i=2204",
        "ns=1;i=2201",
        "ns=1;i=2209",
        "ns=1;i=2210",
        "ns=1;i=2211",
        "ns=1;i=2206",
    ],
)
_NODES: dict = {
    "datatypes": {
        "ActiveStateDataType": (
            "D",
            "ns=1;i=2197",
            {"EnumStrings": ("V", "ns=1;i=2949", {})},
        ),
        "AssetEventDataType": ("D", "ns=1;i=2618", {}),
        "AvailabilityDataType": (
            "D",
            "ns=1;i=2198",
            {"EnumStrings": ("V", "ns=1;i=2955", {})},
        ),
        "AxisCouplingDataType": (
            "D",
            "ns=1;i=2199",
            {"EnumStrings": ("V", "ns=1;i=2961", {})},
        ),
        "AxisStateDataType": (
            "D",
            "ns=1;i=2200",
            {"EnumStrings": ("V", "ns=1;i=2967", {})},
        ),
        "CompositionStateDataType": (
            "D",
            "ns=1;i=2202",
            {"EnumStrings": ("V", "ns=1;i=2973", {})},
        ),
        "ControllerModeDataType": (
            "D",
            "ns=1;i=2203",
            {"EnumStrings": ("V", "ns=1;i=2979", {})},
        ),
        "DirectionDataType": (
            "D",
            "ns=1;i=2205",
            {"EnumStrings": ("V", "ns=1;i=2985", {})},
        ),
        "EmergencyStopDataType": (
            "D",
            "ns=1;i=2207",
            {"EnumStrings": ("V", "ns=1;i=2991", {})},
        ),
        "ExecutionDataType": (
            "D",
            "ns=1;i=2262",
            {"EnumStrings": ("V", "ns=1;i=2997", {})},
        ),
        "FunctionalModeDataType": (
            "D",
            "ns=1;i=2208",
            {"EnumStrings": ("V", "ns=1;i=3003", {})},
        ),
        "InterfaceStateDataType": (
            "D",
            "ns=1;i=2234",
            {"EnumStrings": ("V", "ns=1;i=3009", {})},
        ),
        "InterfaceStatusDataType": (
            "D",
            "ns=1;i=2230",
            {"EnumStrings": ("V", "ns=1;i=3015", {})},
        ),
        "MTCategoryType": (
            "D",
            "ns=1;i=2634",
            {"EnumStrings": ("V", "ns=1;i=2765", {})},
        ),
        "MTCoordinateSystemType": (
            "D",
            "ns=1;i=2635",
            {"EnumStrings": ("V", "ns=1;i=2785", {})},
        ),
        "MTRepresentationType": (
            "D",
            "ns=1;i=2633",
            {"EnumStrings": ("V", "ns=1;i=2827", {})},
        ),
        "MTResetTriggerType": (
            "D",
            "ns=1;i=2636",
            {"EnumStrings": ("V", "ns=1;i=2833", {})},
        ),
        "MTSeverityDataType": (
            "D",
            "ns=1;i=2669",
            {"EnumStrings": ("V", "ns=1;i=2937", {})},
        ),
        "MTStatisticType": (
            "D",
            "ns=1;i=2659",
            {"EnumStrings": ("V", "ns=1;i=2861", {})},
        ),
        "MessageDataType": ("D", "ns=1;i=2653", {}),
        "OnOffDataType": (
            "D",
            "ns=1;i=2204",
            {"EnumStrings": ("V", "ns=1;i=3021", {})},
        ),
        "OpenStateDataType": (
            "D",
            "ns=1;i=2201",
            {"EnumStrings": ("V", "ns=1;i=3027", {})},
        ),
        "PathModeDataType": (
            "D",
            "ns=1;i=2209",
            {"EnumStrings": ("V", "ns=1;i=3033", {})},
        ),
        "ProgramEditDataType": (
            "D",
            "ns=1;i=2210",
            {"EnumStrings": ("V", "ns=1;i=3039", {})},
        ),
        "QualifierDataType": (
            "D",
            "ns=1;i=2668",
            {"EnumStrings": ("V", "ns=1;i=2943", {})},
        ),
        "RotaryModeDataType": (
            "D",
            "ns=1;i=2211",
            {"EnumStrings": ("V", "ns=1;i=3045", {})},
        ),
        "ThreeSpaceSampleDataType": ("D", "ns=1;i=2637", {}),
        "YesNoDataType": (
            "D",
            "ns=1;i=2206",
            {"EnumStrings": ("V", "ns=1;i=3051", {})},
        ),
    },
    "eventtypes": {
        "MTConditionEventType": (
            "OT",
            "ns=1;i=4326",
            {
                "ActiveState": ("V", "ns=1;i=4336", {}),
                "DataItemId": ("V", "ns=1;i=4327", {}),
                "MTSeverity": ("V", "ns=1;i=4328", {}),
                "MTSubTypeName": ("V", "ns=1;i=4329", {}),
                "MTTypeName": ("V", "ns=1;i=4330", {}),
                "NativeCode": ("V", "ns=1;i=4331", {}),
                "NativeSeverity": ("V", "ns=1;i=4332", {}),
                "Qualifier": ("V", "ns=1;i=4333", {}),
            },
        ),
        "MTMessageEventType": (
            "OT",
            "ns=1;i=2656",
            {"NativeCode": ("V", "ns=1;i=2657", {})},
        ),
    },
    "objects": {
        "Default Binary": ("O", "ns=1;i=2909", {}),
        "Default JSON": ("O", "ns=1;i=2914", {}),
        "Default XML": ("O", "ns=1;i=3055", {}),
        "Opc.Ua.MTConnect": (
            "V",
            "ns=1;i=2733",
            {
                "ActiveStateDataType": ("V", "ns=1;i=2954", {}),
                "AssetEventDataType": ("V", "ns=1;i=2749", {}),
                "AvailabilityDataType": ("V", "ns=1;i=2960", {}),
                "AxisCouplingDataType": ("V", "ns=1;i=2966", {}),
                "AxisStateDataType": ("V", "ns=1;i=2972", {}),
                "CompositionStateDataType": ("V", "ns=1;i=2978", {}),
                "ControllerModeDataType": ("V", "ns=1;i=2984", {}),
                "Deprecated": ("V", "ns=1;i=2736", {}),
                "DirectionDataType": ("V", "ns=1;i=2990", {}),
                "EmergencyStopDataType": ("V", "ns=1;i=2996", {}),
                "ExecutionDataType": ("V", "ns=1;i=3002", {}),
                "FunctionalModeDataType": ("V", "ns=1;i=3008", {}),
                "InterfaceStateDataType": ("V", "ns=1;i=3014", {}),
                "InterfaceStatusDataType": ("V", "ns=1;i=3020", {}),
                "MTCategoryType": ("V", "ns=1;i=2770", {}),
                "MTCoordinateSystemType": ("V", "ns=1;i=2790", {}),
                "MTRepresentationType": ("V", "ns=1;i=2832", {}),
                "MTResetTriggerType": ("V", "ns=1;i=2838", {}),
                "MTSeverityDataType": ("V", "ns=1;i=2942", {}),
                "MTStatisticType": ("V", "ns=1;i=2866", {}),
                "MessageDataType": ("V", "ns=1;i=2907", {}),
                "NamespaceUri": ("V", "ns=1;i=2735", {}),
                "OnOffDataType": ("V", "ns=1;i=3026", {}),
                "OpenStateDataType": ("V", "ns=1;i=3032", {}),
                "PathModeDataType": ("V", "ns=1;i=3038", {}),
                "ProgramEditDataType": ("V", "ns=1;i=3044", {}),
                "QualifierDataType": ("V", "ns=1;i=2948", {}),
                "RotaryModeDataType": ("V", "ns=1;i=3050", {}),
                "ThreeSpaceSampleDataType": ("V", "ns=1;i=2913", {}),
                "YesNoDataType": ("V", "ns=1;i=3056", {}),
            },
        ),
        "http://opcfoundation.org/UA/MTConnect/2.0/": (
            "O",
            "ns=1;i=3630",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=3635", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=3634", {}),
                "NamespaceUri": ("V", "ns=1;i=3632", {}),
                "NamespaceVersion": ("V", "ns=1;i=3633", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=3636", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=3637", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=3638", {}),
            },
        ),
    },
    "objtypes": {
        "MTChannelType": (
            "OT",
            "ns=1;i=2059",
            {
                "CalibrationDate": ("V", "ns=1;i=2063", {}),
                "CalibrationInitials": ("V", "ns=1;i=2065", {}),
                "MTDescription": ("V", "ns=1;i=2062", {}),
                "Name": ("V", "ns=1;i=2061", {}),
                "NextCalibrationDate": ("V", "ns=1;i=2064", {}),
                "Number": ("V", "ns=1;i=2060", {}),
            },
        ),
        "MTComponentType": (
            "OT",
            "ns=1;i=2021",
            {
                "ActuatorType": ("OT", "ns=1;i=2074", {}),
                "AuxiliariesType": (
                    "OT",
                    "ns=1;i=2076",
                    {
                        "BarFeederType": ("OT", "ns=1;i=2082", {}),
                        "EnvironmentalType": ("OT", "ns=1;i=2102", {}),
                        "LoaderType": ("OT", "ns=1;i=2112", {}),
                        "SensorType": ("OT", "ns=1;i=2134", {}),
                        "ToolingDeliveryType": ("OT", "ns=1;i=2140", {}),
                        "WasteDisposalType": ("OT", "ns=1;i=2142", {}),
                    },
                ),
                "AxesType": (
                    "OT",
                    "ns=1;i=2078",
                    {
                        "LinearType": ("OT", "ns=1;i=2110", {}),
                        "RotaryType": (
                            "OT",
                            "ns=1;i=2132",
                            {"ChuckType": ("OT", "ns=1;i=2086", {})},
                        ),
                    },
                ),
                "Components": ("O", "ns=1;i=2042", {}),
                "Compositions": ("O", "ns=1;i=2043", {}),
                "Configuration": ("O", "ns=1;i=2029", {}),
                "ControllerType": (
                    "OT",
                    "ns=1;i=2088",
                    {"PathType": ("OT", "ns=1;i=2120", {})},
                ),
                "Description": (
                    "O",
                    "ns=1;i=2028",
                    {
                        "Data": ("V", "ns=1;i=2740", {}),
                        "Manufacturer": ("V", "ns=1;i=2739", {}),
                        "SerialNumber": ("V", "ns=1;i=2738", {}),
                        "Station": ("V", "ns=1;i=2737", {}),
                    },
                ),
                "DoorType": ("OT", "ns=1;i=2096", {}),
                "InterfacesType": (
                    "OT",
                    "ns=1;i=2108",
                    {
                        "BarFeederInterfaceType": ("OT", "ns=1;i=2080", {}),
                        "ChuckInterfaceType": ("OT", "ns=1;i=2084", {}),
                        "DoorInterfaceType": ("OT", "ns=1;i=2094", {}),
                        "MaterialHandlerInterfaceType": ("OT", "ns=1;i=2116", {}),
                    },
                ),
                "MTDeviceType": (
                    "OT",
                    "ns=1;i=2015",
                    {
                        "Iso841Class": ("V", "ns=1;i=2017", {}),
                        "Name": ("V", "ns=1;i=3668", {}),
                        "Uuid": ("V", "ns=1;i=3669", {}),
                        "Version": ("V", "ns=1;i=2016", {}),
                    },
                ),
                "Name": ("V", "ns=1;i=2023", {}),
                "NativeName": ("V", "ns=1;i=2024", {}),
                "ResourcesType": (
                    "OT",
                    "ns=1;i=2130",
                    {
                        "MaterialsType": (
                            "OT",
                            "ns=1;i=2118",
                            {"StockType": ("OT", "ns=1;i=2136", {})},
                        ),
                        "PersonnelType": ("OT", "ns=1;i=2122", {}),
                    },
                ),
                "SampleInterval": ("V", "ns=1;i=2027", {}),
                "SampleRate": ("V", "ns=1;i=2026", {}),
                "SystemsType": (
                    "OT",
                    "ns=1;i=2138",
                    {
                        "CoolantType": ("OT", "ns=1;i=2090", {}),
                        "DielectricType": ("OT", "ns=1;i=2092", {}),
                        "ElectricType": ("OT", "ns=1;i=2098", {}),
                        "EnclosureType": ("OT", "ns=1;i=2100", {}),
                        "FeederType": ("OT", "ns=1;i=2104", {}),
                        "HydraulicType": ("OT", "ns=1;i=2106", {}),
                        "LubricationType": ("OT", "ns=1;i=2114", {}),
                        "PneumaticType": ("OT", "ns=1;i=2124", {}),
                        "ProcessPowerType": ("OT", "ns=1;i=2126", {}),
                        "ProtectiveType": ("OT", "ns=1;i=2128", {}),
                    },
                ),
                "Uuid": ("V", "ns=1;i=2025", {}),
                "XmlId": ("V", "ns=1;i=2022", {}),
            },
        ),
        "MTCompositionType": (
            "OT",
            "ns=1;i=2067",
            {
                "MTTypeName": ("V", "ns=1;i=2069", {}),
                "Name": ("V", "ns=1;i=2071", {}),
                "Uuid": ("V", "ns=1;i=2070", {}),
                "XmlId": ("V", "ns=1;i=2068", {}),
            },
        ),
        "MTConditionType": (
            "OT",
            "ns=1;i=2660",
            {
                "Category": ("V", "ns=1;i=2917", {}),
                "Constraints": (
                    "O",
                    "ns=1;i=2924",
                    {
                        "Maximum": ("V", "ns=1;i=2927", {}),
                        "Minimum": ("V", "ns=1;i=2926", {}),
                        "Nominal": ("V", "ns=1;i=2928", {}),
                        "Values": ("V", "ns=1;i=2925", {}),
                    },
                ),
                "MTSubTypeName": ("V", "ns=1;i=2919", {}),
                "MTTypeName": ("V", "ns=1;i=2918", {}),
                "Name": ("V", "ns=1;i=2916", {}),
                "PeriodFilter": ("V", "ns=1;i=2923", {}),
                "Representation": ("V", "ns=1;i=2922", {}),
                "SampleRate": ("V", "ns=1;i=2921", {}),
                "SourceData": ("V", "ns=1;i=2920", {}),
                "XmlId": ("V", "ns=1;i=2915", {}),
            },
        ),
        "MTConfigurationType": (
            "OT",
            "ns=1;i=2044",
            {
                "MTSensorConfigurationType": (
                    "OT",
                    "ns=1;i=2046",
                    {
                        "CalibrationDate": ("V", "ns=1;i=2048", {}),
                        "CalibrationInitials": ("V", "ns=1;i=2050", {}),
                        "Channels": ("O", "ns=1;i=2052", {}),
                        "FirwareVersion": ("V", "ns=1;i=2047", {}),
                        "NextCalibrationDate": ("V", "ns=1;i=2049", {}),
                    },
                )
            },
        ),
        "MTConstraintType": (
            "OT",
            "ns=1;i=2647",
            {
                "Maximum": ("V", "ns=1;i=2650", {}),
                "Minimum": ("V", "ns=1;i=2649", {}),
                "Nominal": ("V", "ns=1;i=2651", {}),
                "Values": ("V", "ns=1;i=2648", {}),
            },
        ),
        "MTDataItemClassType": (
            "OT",
            "ns=1;i=2425",
            {
                "MTConditionClassType": (
                    "OT",
                    "ns=1;i=2629",
                    {
                        "ActuatorClassType": ("OT", "ns=1;i=2411", {}),
                        "CommunicationsClassType": ("OT", "ns=1;i=2413", {}),
                        "DataRangeClassType": ("OT", "ns=1;i=2415", {}),
                        "HardwareClassType": ("OT", "ns=1;i=2419", {}),
                        "LogicProgramClassType": ("OT", "ns=1;i=2417", {}),
                        "MotionProgramClassType": ("OT", "ns=1;i=2421", {}),
                        "SystemClassType": ("OT", "ns=1;i=2423", {}),
                    },
                ),
                "MTEventClassType": (
                    "OT",
                    "ns=1;i=2631",
                    {
                        "MTControlledVocabEventClassType": (
                            "OT",
                            "ns=1;i=2144",
                            {
                                "ActuatorStateClassType": ("OT", "ns=1;i=2146", {}),
                                "AvailabilityClassType": ("OT", "ns=1;i=2149", {}),
                                "AxisCouplingClassType": ("OT", "ns=1;i=2152", {}),
                                "AxisInterlockClassType": ("OT", "ns=1;i=2155", {}),
                                "AxisStateClassType": ("OT", "ns=1;i=2158", {}),
                                "ChuckInterlockClassType": ("OT", "ns=1;i=2161", {}),
                                "ChuckStateClassType": ("OT", "ns=1;i=2164", {}),
                                "CloseChuckClassType": ("OT", "ns=1;i=2256", {}),
                                "CloseDoorClassType": ("OT", "ns=1;i=2250", {}),
                                "CompositionStateClassType": ("OT", "ns=1;i=2173", {}),
                                "ControllerModeClassType": ("OT", "ns=1;i=2167", {}),
                                "ControllerModeOverrideClassType": (
                                    "OT",
                                    "ns=1;i=2176",
                                    {},
                                ),
                                "DirectionClassType": ("OT", "ns=1;i=2179", {}),
                                "DoorStateClassType": ("OT", "ns=1;i=2182", {}),
                                "EmergencyStopClassType": ("OT", "ns=1;i=2185", {}),
                                "EndOfBarClassType": ("OT", "ns=1;i=2188", {}),
                                "EquipmentModeClassType": ("OT", "ns=1;i=2191", {}),
                                "ExecutionClassType": ("OT", "ns=1;i=2170", {}),
                                "FunctionalModeClassType": ("OT", "ns=1;i=2194", {}),
                                "InterfaceStateClassType": ("OT", "ns=1;i=2227", {}),
                                "MaterialChangeClassType": ("OT", "ns=1;i=2235", {}),
                                "MaterialFeedClassType": ("OT", "ns=1;i=2231", {}),
                                "MaterialLoadClassType": ("OT", "ns=1;i=2241", {}),
                                "MaterialRetractClassType": ("OT", "ns=1;i=2238", {}),
                                "MaterialUnloadClassType": ("OT", "ns=1;i=2244", {}),
                                "OpenChuckClassType": ("OT", "ns=1;i=2253", {}),
                                "OpenDoorClassType": ("OT", "ns=1;i=2247", {}),
                                "PartChangeClassType": ("OT", "ns=1;i=2259", {}),
                                "PathModeClassType": ("OT", "ns=1;i=2215", {}),
                                "PowerStateClassType": ("OT", "ns=1;i=2218", {}),
                                "ProgramEditClassType": ("OT", "ns=1;i=2221", {}),
                                "RotaryModeClassType": ("OT", "ns=1;i=2224", {}),
                                "SpindleInterlockClassType": ("OT", "ns=1;i=2212", {}),
                            },
                        ),
                        "MTMessageClassType": ("OT", "ns=1;i=2427", {}),
                        "MTNumericEventClassType": (
                            "OT",
                            "ns=1;i=2359",
                            {
                                "AxisFeedrateOverrideClassType": (
                                    "OT",
                                    "ns=1;i=2347",
                                    {},
                                ),
                                "BlockCountClassType": ("OT", "ns=1;i=2349", {}),
                                "HardnessClassType": ("OT", "ns=1;i=2351", {}),
                                "LineNumberClassType": ("OT", "ns=1;i=2353", {}),
                                "PartCountClassType": ("OT", "ns=1;i=2355", {}),
                                "PathFeedrateOverrideClassType": (
                                    "OT",
                                    "ns=1;i=3628",
                                    {},
                                ),
                                "RotaryVelocityOverrideClassType": (
                                    "OT",
                                    "ns=1;i=2357",
                                    {},
                                ),
                            },
                        ),
                        "MTStringEventClassType": (
                            "OT",
                            "ns=1;i=2361",
                            {
                                "AssetChangedClassType": ("OT", "ns=1;i=2405", {}),
                                "AssetRemovedClassType": ("OT", "ns=1;i=2407", {}),
                                "BlockClassType": ("OT", "ns=1;i=2363", {}),
                                "CoupledAxesClassType": ("OT", "ns=1;i=2365", {}),
                                "LineClassType": ("OT", "ns=1;i=2409", {}),
                                "LineLabelClassType": ("OT", "ns=1;i=2367", {}),
                                "MaterialClassType": ("OT", "ns=1;i=2369", {}),
                                "MessageClassType": ("OT", "ns=1;i=2403", {}),
                                "OperatorIdClassType": ("OT", "ns=1;i=2371", {}),
                                "PalletIdClassType": ("OT", "ns=1;i=2373", {}),
                                "PartIdClassType": ("OT", "ns=1;i=2375", {}),
                                "PartNumberClassType": ("OT", "ns=1;i=2377", {}),
                                "ProgramClassType": ("OT", "ns=1;i=2379", {}),
                                "ProgramCommentClassType": ("OT", "ns=1;i=2385", {}),
                                "ProgramEditNameClassType": ("OT", "ns=1;i=2381", {}),
                                "ProgramHeaderClassType": ("OT", "ns=1;i=2383", {}),
                                "SerialNumberClassType": ("OT", "ns=1;i=2387", {}),
                                "ToolAssetIdClassType": ("OT", "ns=1;i=2389", {}),
                                "ToolNumberClassType": ("OT", "ns=1;i=2391", {}),
                                "ToolOffsetClassType": ("OT", "ns=1;i=2393", {}),
                                "UserClassType": ("OT", "ns=1;i=2395", {}),
                                "WireClassType": ("OT", "ns=1;i=2397", {}),
                                "WorkOffsetClassType": ("OT", "ns=1;i=2401", {}),
                                "WorkholdingClassType": ("OT", "ns=1;i=2399", {}),
                            },
                        ),
                    },
                ),
                "MTSampleClassType": (
                    "OT",
                    "ns=1;i=2345",
                    {
                        "AccelerationClassType": ("OT", "ns=1;i=2265", {}),
                        "AccumulatedTimeClassType": ("OT", "ns=1;i=2267", {}),
                        "AmperageClassType": ("OT", "ns=1;i=2273", {}),
                        "AngleClassType": ("OT", "ns=1;i=2275", {}),
                        "AngularAccelerationClassType": ("OT", "ns=1;i=2269", {}),
                        "AngularVelocityClassType": ("OT", "ns=1;i=2271", {}),
                        "AxisFeedrateClassType": ("OT", "ns=1;i=2277", {}),
                        "ClockTimeClassType": ("OT", "ns=1;i=2279", {}),
                        "ConcentrationClassType": ("OT", "ns=1;i=2281", {}),
                        "ConductivityClassType": ("OT", "ns=1;i=2283", {}),
                        "DisplacementClassType": ("OT", "ns=1;i=2285", {}),
                        "ElectricalEnergyClassType": ("OT", "ns=1;i=2287", {}),
                        "EquipmentTimerClassType": ("OT", "ns=1;i=2289", {}),
                        "FillLevelClassType": ("OT", "ns=1;i=2291", {}),
                        "FlowClassType": ("OT", "ns=1;i=2293", {}),
                        "FrequencyClassType": ("OT", "ns=1;i=2295", {}),
                        "LengthClassType": ("OT", "ns=1;i=2297", {}),
                        "LinearForceClassType": ("OT", "ns=1;i=2299", {}),
                        "LoadClassType": ("OT", "ns=1;i=2263", {}),
                        "MassClassType": ("OT", "ns=1;i=2301", {}),
                        "PHClassType": ("OT", "ns=1;i=2307", {}),
                        "PathFeedrateClassType": ("OT", "ns=1;i=2303", {}),
                        "PathPositionClassType": ("OT", "ns=1;i=2305", {}),
                        "PositionClassType": ("OT", "ns=1;i=2309", {}),
                        "PowerFactorClassType": ("OT", "ns=1;i=2311", {}),
                        "PressureClassType": ("OT", "ns=1;i=2313", {}),
                        "ProcessTimerClassType": ("OT", "ns=1;i=2315", {}),
                        "ResistenceClassType": ("OT", "ns=1;i=2317", {}),
                        "RotaryVelocityClassType": ("OT", "ns=1;i=2319", {}),
                        "SoundLevelClassType": ("OT", "ns=1;i=2321", {}),
                        "StrainClassType": ("OT", "ns=1;i=2323", {}),
                        "TemperatureClassType": ("OT", "ns=1;i=2325", {}),
                        "TensionClassType": ("OT", "ns=1;i=2327", {}),
                        "TiltClassType": ("OT", "ns=1;i=2329", {}),
                        "TorqueClassType": ("OT", "ns=1;i=2331", {}),
                        "VelocityClassType": ("OT", "ns=1;i=2335", {}),
                        "ViscosityClassType": ("OT", "ns=1;i=2339", {}),
                        "VoltAmpereClassType": ("OT", "ns=1;i=2333", {}),
                        "VoltAmpereReactiveClassType": ("OT", "ns=1;i=2337", {}),
                        "VoltageClassType": ("OT", "ns=1;i=2341", {}),
                        "WattageClassType": ("OT", "ns=1;i=2343", {}),
                    },
                ),
            },
        ),
        "MTDataItemSubClassType": (
            "OT",
            "ns=1;i=2476",
            {
                "AScaleSubClassType": ("OT", "ns=1;i=2488", {}),
                "AbsoluteSubClassType": ("OT", "ns=1;i=2478", {}),
                "ActionSubClassType": ("OT", "ns=1;i=2482", {}),
                "ActualSubClassType": ("OT", "ns=1;i=2480", {}),
                "AllSubClassType": ("OT", "ns=1;i=2484", {}),
                "AlternatingSubClassType": ("OT", "ns=1;i=2486", {}),
                "AuxiliarySubClassType": ("OT", "ns=1;i=2490", {}),
                "BScaleSubClassType": ("OT", "ns=1;i=2496", {}),
                "BadSubClassType": ("OT", "ns=1;i=2492", {}),
                "BrinellSubClassType": ("OT", "ns=1;i=2494", {}),
                "CScaleSubClassType": ("OT", "ns=1;i=2504", {}),
                "CommandedSubClassType": ("OT", "ns=1;i=2498", {}),
                "ControlSubClassType": ("OT", "ns=1;i=2502", {}),
                "DScaleSubClassType": ("OT", "ns=1;i=2512", {}),
                "DelaySubClassType": ("OT", "ns=1;i=2506", {}),
                "DirectSubClassType": ("OT", "ns=1;i=2508", {}),
                "DryRunSubClassType": ("OT", "ns=1;i=2510", {}),
                "FixtureSubClassType": ("OT", "ns=1;i=2514", {}),
                "GoodSubClassType": ("OT", "ns=1;i=2500", {}),
                "IncrementalSubClassType": ("OT", "ns=1;i=2516", {}),
                "JobSubClassType": ("OT", "ns=1;i=2518", {}),
                "KineticSubClassType": ("OT", "ns=1;i=2520", {}),
                "LateralSubClassType": ("OT", "ns=1;i=2522", {}),
                "LeebSubClassType": ("OT", "ns=1;i=2524", {}),
                "LengthSubClassType": ("OT", "ns=1;i=2526", {}),
                "LineSubClassType": ("OT", "ns=1;i=2530", {}),
                "LinearSubClassType": ("OT", "ns=1;i=2528", {}),
                "LoadedSubClassType": ("OT", "ns=1;i=2532", {}),
                "MachineAxisLockSubClassType": ("OT", "ns=1;i=2534", {}),
                "MaintenanceSubClassType": ("OT", "ns=1;i=2536", {}),
                "ManualUnclampSubClassType": ("OT", "ns=1;i=2538", {}),
                "MaximumSubClassType": ("OT", "ns=1;i=2540", {}),
                "MinimumSubClassType": ("OT", "ns=1;i=2542", {}),
                "MohsSubClassType": ("OT", "ns=1;i=2544", {}),
                "MoleSubClassType": ("OT", "ns=1;i=2546", {}),
                "MotionSubClassType": ("OT", "ns=1;i=2548", {}),
                "NoScaleSubClassType": ("OT", "ns=1;i=2550", {}),
                "OperatingSubClassType": ("OT", "ns=1;i=2552", {}),
                "OperatorSubClassType": ("OT", "ns=1;i=2554", {}),
                "OptionalStopSubClassType": ("OT", "ns=1;i=2556", {}),
                "OverrideSubClassType": ("OT", "ns=1;i=2558", {}),
                "PoweredSubClassType": ("OT", "ns=1;i=2562", {}),
                "PrimarySubClassType": ("OT", "ns=1;i=2560", {}),
                "ProbeSubClassType": ("OT", "ns=1;i=2564", {}),
                "ProcessSubClassType": ("OT", "ns=1;i=2566", {}),
                "ProgrammedSubClassType": ("OT", "ns=1;i=2568", {}),
                "RadialSubClassType": ("OT", "ns=1;i=2570", {}),
                "RapidSubClassType": ("OT", "ns=1;i=2572", {}),
                "RelativeSubClassType": ("OT", "ns=1;i=2574", {}),
                "RemainingSubClassType": ("OT", "ns=1;i=2576", {}),
                "RequestSubClassType": ("OT", "ns=1;i=2578", {}),
                "ResponseSubClassType": ("OT", "ns=1;i=2580", {}),
                "RockwellSubClassType": ("OT", "ns=1;i=2582", {}),
                "RotarySubClassType": ("OT", "ns=1;i=2584", {}),
                "SetUpSubClassType": ("OT", "ns=1;i=2586", {}),
                "ShoreSubClassType": ("OT", "ns=1;i=2588", {}),
                "StandardSubClassType": ("OT", "ns=1;i=2590", {}),
                "SwitchedSubClassType": ("OT", "ns=1;i=2592", {}),
                "TargetSubClassType": ("OT", "ns=1;i=2594", {}),
                "ToolChangeStopSubClassType": ("OT", "ns=1;i=2596", {}),
                "ToolEdgeSubClassType": ("OT", "ns=1;i=2598", {}),
                "ToolGroupSubClassType": ("OT", "ns=1;i=2600", {}),
                "ToolSubClassType": ("OT", "ns=1;i=2602", {}),
                "UasbleSubClassType": ("OT", "ns=1;i=2604", {}),
                "VerticalSubClassType": ("OT", "ns=1;i=2606", {}),
                "VickersSubClassType": ("OT", "ns=1;i=2610", {}),
                "VolumeSubClassType": ("OT", "ns=1;i=2608", {}),
                "WeightSubClassType": ("OT", "ns=1;i=2612", {}),
                "WorkingSubClassType": ("OT", "ns=1;i=2614", {}),
                "WorkpieceSubClassType": ("OT", "ns=1;i=2616", {}),
            },
        ),
        "MTDescriptionType": (
            "OT",
            "ns=1;i=2053",
            {
                "Data": ("V", "ns=1;i=2057", {}),
                "Manufacturer": ("V", "ns=1;i=2056", {}),
                "SerialNumber": ("V", "ns=1;i=2055", {}),
                "Station": ("V", "ns=1;i=2054", {}),
            },
        ),
    },
    "reftypes": {
        "HasMTClassType": ("RT", "ns=1;i=2680", {}),
        "HasMTComposition": ("RT", "ns=1;i=2687", {}),
        "HasMTReference": ("RT", "ns=1;i=2672", {}),
        "HasMTSource": ("RT", "ns=1;i=2689", {}),
        "HasMTSubClassType": ("RT", "ns=1;i=2683", {}),
    },
    "vartypes": {
        "MTAssetEventType": (
            "VT",
            "ns=1;i=2621",
            {
                "Category": ("V", "ns=1;i=2753", {}),
                "Constraints": (
                    "O",
                    "ns=1;i=2760",
                    {
                        "Maximum": ("V", "ns=1;i=2763", {}),
                        "Minimum": ("V", "ns=1;i=2762", {}),
                        "Nominal": ("V", "ns=1;i=2764", {}),
                        "Values": ("V", "ns=1;i=2761", {}),
                    },
                ),
                "MTSubTypeName": ("V", "ns=1;i=2755", {}),
                "MTTypeName": ("V", "ns=1;i=2754", {}),
                "Name": ("V", "ns=1;i=2752", {}),
                "PeriodFilter": ("V", "ns=1;i=2759", {}),
                "Representation": ("V", "ns=1;i=2758", {}),
                "SampleRate": ("V", "ns=1;i=2757", {}),
                "SourceData": ("V", "ns=1;i=2756", {}),
                "XmlId": ("V", "ns=1;i=2751", {}),
            },
        ),
        "MTControlledVocabEventType": (
            "VT",
            "ns=1;i=2626",
            {
                "Category": ("V", "ns=1;i=2773", {}),
                "Constraints": (
                    "O",
                    "ns=1;i=2780",
                    {
                        "Maximum": ("V", "ns=1;i=2783", {}),
                        "Minimum": ("V", "ns=1;i=2782", {}),
                        "Nominal": ("V", "ns=1;i=2784", {}),
                        "Values": ("V", "ns=1;i=2781", {}),
                    },
                ),
                "MTSubTypeName": ("V", "ns=1;i=2775", {}),
                "MTTypeName": ("V", "ns=1;i=2774", {}),
                "Name": ("V", "ns=1;i=2772", {}),
                "PeriodFilter": ("V", "ns=1;i=2779", {}),
                "Representation": ("V", "ns=1;i=2778", {}),
                "SampleRate": ("V", "ns=1;i=2777", {}),
                "SourceData": ("V", "ns=1;i=2776", {}),
                "ValueAsText": ("V", "ns=1;i=3090", {}),
                "XmlId": ("V", "ns=1;i=2771", {}),
            },
        ),
        "MTMessageType": (
            "VT",
            "ns=1;i=2471",
            {
                "Category": ("V", "ns=1;i=2793", {}),
                "Constraints": (
                    "O",
                    "ns=1;i=2800",
                    {
                        "Maximum": ("V", "ns=1;i=2803", {}),
                        "Minimum": ("V", "ns=1;i=2802", {}),
                        "Nominal": ("V", "ns=1;i=2804", {}),
                        "Values": ("V", "ns=1;i=2801", {}),
                    },
                ),
                "MTSubTypeName": ("V", "ns=1;i=2795", {}),
                "MTTypeName": ("V", "ns=1;i=2794", {}),
                "Name": ("V", "ns=1;i=2792", {}),
                "PeriodFilter": ("V", "ns=1;i=2799", {}),
                "Representation": ("V", "ns=1;i=2798", {}),
                "SampleRate": ("V", "ns=1;i=2797", {}),
                "SourceData": ("V", "ns=1;i=2796", {}),
                "XmlId": ("V", "ns=1;i=2791", {}),
            },
        ),
        "MTNumericEventType": (
            "VT",
            "ns=1;i=2438",
            {
                "Category": ("V", "ns=1;i=2807", {}),
                "Constraints": (
                    "O",
                    "ns=1;i=2814",
                    {
                        "Maximum": ("V", "ns=1;i=2817", {}),
                        "Minimum": ("V", "ns=1;i=2816", {}),
                        "Nominal": ("V", "ns=1;i=2818", {}),
                        "Values": ("V", "ns=1;i=2815", {}),
                    },
                ),
                "CoordinateSystem": ("V", "ns=1;i=2822", {}),
                "Duration": ("V", "ns=1;i=3671", {}),
                "InitialValue": ("V", "ns=1;i=2823", {}),
                "MTSubTypeName": ("V", "ns=1;i=2809", {}),
                "MTTypeName": ("V", "ns=1;i=2808", {}),
                "MinimumDeltaFilter": ("V", "ns=1;i=2826", {}),
                "Name": ("V", "ns=1;i=2806", {}),
                "NativeUnits": ("V", "ns=1;i=2821", {}),
                "PeriodFilter": ("V", "ns=1;i=2813", {}),
                "Representation": ("V", "ns=1;i=2812", {}),
                "ResetTrigger": ("V", "ns=1;i=2824", {}),
                "ResetTriggeredReason": ("V", "ns=1;i=3675", {}),
                "SampleRate": ("V", "ns=1;i=2811", {}),
                "SignificantDigits": ("V", "ns=1;i=2819", {}),
                "SourceData": ("V", "ns=1;i=2810", {}),
                "Statistic": ("V", "ns=1;i=2820", {}),
                "Units": ("V", "ns=1;i=2825", {}),
                "XmlId": ("V", "ns=1;i=2805", {}),
            },
        ),
        "MTSampleType": (
            "VT",
            "ns=1;i=2429",
            {
                "Category": ("V", "ns=1;i=2841", {}),
                "Constraints": (
                    "O",
                    "ns=1;i=2848",
                    {
                        "Maximum": ("V", "ns=1;i=2851", {}),
                        "Minimum": ("V", "ns=1;i=2850", {}),
                        "Nominal": ("V", "ns=1;i=2852", {}),
                        "Values": ("V", "ns=1;i=2849", {}),
                    },
                ),
                "CoordinateSystem": ("V", "ns=1;i=2856", {}),
                "Duration": ("V", "ns=1;i=3672", {}),
                "InitialValue": ("V", "ns=1;i=2857", {}),
                "MTSubTypeName": ("V", "ns=1;i=2843", {}),
                "MTTypeName": ("V", "ns=1;i=2842", {}),
                "MinimumDeltaFilter": ("V", "ns=1;i=2860", {}),
                "Name": ("V", "ns=1;i=2840", {}),
                "NativeUnits": ("V", "ns=1;i=2855", {}),
                "PeriodFilter": ("V", "ns=1;i=2847", {}),
                "Representation": ("V", "ns=1;i=2846", {}),
                "ResetTrigger": ("V", "ns=1;i=2858", {}),
                "ResetTriggeredReason": ("V", "ns=1;i=3676", {}),
                "SampleRate": ("V", "ns=1;i=2845", {}),
                "SignificantDigits": ("V", "ns=1;i=2853", {}),
                "SourceData": ("V", "ns=1;i=2844", {}),
                "Statistic": ("V", "ns=1;i=2854", {}),
                "Units": ("V", "ns=1;i=2859", {}),
                "XmlId": ("V", "ns=1;i=2839", {}),
            },
        ),
        "MTStringEventType": (
            "VT",
            "ns=1;i=2433",
            {
                "Category": ("V", "ns=1;i=2869", {}),
                "Constraints": (
                    "O",
                    "ns=1;i=2876",
                    {
                        "Maximum": ("V", "ns=1;i=2879", {}),
                        "Minimum": ("V", "ns=1;i=2878", {}),
                        "Nominal": ("V", "ns=1;i=2880", {}),
                        "Values": ("V", "ns=1;i=2877", {}),
                    },
                ),
                "MTSubTypeName": ("V", "ns=1;i=2871", {}),
                "MTTypeName": ("V", "ns=1;i=2870", {}),
                "Name": ("V", "ns=1;i=2868", {}),
                "PeriodFilter": ("V", "ns=1;i=2875", {}),
                "Representation": ("V", "ns=1;i=2874", {}),
                "SampleRate": ("V", "ns=1;i=2873", {}),
                "SourceData": ("V", "ns=1;i=2872", {}),
                "XmlId": ("V", "ns=1;i=2867", {}),
            },
        ),
        "MTThreeSpaceSampleType": (
            "VT",
            "ns=1;i=2641",
            {
                "Category": ("V", "ns=1;i=2883", {}),
                "Constraints": (
                    "O",
                    "ns=1;i=2890",
                    {
                        "Maximum": ("V", "ns=1;i=2893", {}),
                        "Minimum": ("V", "ns=1;i=2892", {}),
                        "Nominal": ("V", "ns=1;i=2894", {}),
                        "Values": ("V", "ns=1;i=2891", {}),
                    },
                ),
                "CoordinateSystem": ("V", "ns=1;i=2898", {}),
                "Duration": ("V", "ns=1;i=3673", {}),
                "EngineeringUnits": ("V", "ns=1;i=2642", {}),
                "InitialValue": ("V", "ns=1;i=2899", {}),
                "MTSubTypeName": ("V", "ns=1;i=2885", {}),
                "MTTypeName": ("V", "ns=1;i=2884", {}),
                "MinimumDeltaFilter": ("V", "ns=1;i=2902", {}),
                "Name": ("V", "ns=1;i=2882", {}),
                "NativeUnits": ("V", "ns=1;i=2897", {}),
                "PeriodFilter": ("V", "ns=1;i=2889", {}),
                "Representation": ("V", "ns=1;i=2888", {}),
                "ResetTrigger": ("V", "ns=1;i=2900", {}),
                "ResetTriggeredReason": ("V", "ns=1;i=3677", {}),
                "SampleRate": ("V", "ns=1;i=2887", {}),
                "SignificantDigits": ("V", "ns=1;i=2895", {}),
                "SourceData": ("V", "ns=1;i=2886", {}),
                "Statistic": ("V", "ns=1;i=2896", {}),
                "Units": ("V", "ns=1;i=2901", {}),
                "XmlId": ("V", "ns=1;i=2881", {}),
            },
        ),
    },
}
