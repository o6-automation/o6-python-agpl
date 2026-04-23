# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 8ac55e581540258ee8de67617c2d3ef26e9d828dfceabb10f6ba5704c476357d
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/IA/"
_VERSION: str = "1.01.4"
_REQUIRED: list = [
    {"uri": "http://opcfoundation.org/UA/", "version": "1.05.01"},
    {"uri": "http://opcfoundation.org/UA/DI/", "version": "1.03.1"},
]
_STRUCTURES: list = [
    (
        "ns=1;i=3007",
        "RGBWDataType",
        "ns=1;i=5009",
        {
            "structure_type": 1,
            "fields": [
                {"name": "Red", "data_type": "i=3", "value_rank": -1},
                {"name": "Green", "data_type": "i=3", "value_rank": -1},
                {"name": "Blue", "data_type": "i=3", "value_rank": -1},
                {
                    "name": "White",
                    "data_type": "i=3",
                    "value_rank": -1,
                    "is_optional": True,
                },
            ],
        },
    )
]
_ENUMS: list = [
    (
        "ns=1;i=3003",
        "LevelDisplayMode",
        {
            "fields": [
                {"name": "Dimmed", "value": 0, "display_name": "Dimmed"},
                {"name": "Blinking", "value": 1, "display_name": "Blinking"},
                {"name": "Other", "value": 2, "display_name": "Other"},
            ]
        },
    ),
    (
        "ns=1;i=3004",
        "SignalColor",
        {
            "fields": [
                {"name": "Off", "value": 0, "display_name": "Off"},
                {"name": "Red", "value": 1, "display_name": "Red"},
                {"name": "Green", "value": 2, "display_name": "Green"},
                {"name": "Blue", "value": 3, "display_name": "Blue"},
                {"name": "Yellow", "value": 4, "display_name": "Yellow"},
                {"name": "Purple", "value": 5, "display_name": "Purple"},
                {"name": "Cyan", "value": 6, "display_name": "Cyan"},
                {"name": "White", "value": 7, "display_name": "White"},
            ]
        },
    ),
    (
        "ns=1;i=3005",
        "SignalModeLight",
        {
            "fields": [
                {"name": "Continuous", "value": 0, "display_name": "Continuous"},
                {"name": "Blinking", "value": 1, "display_name": "Blinking"},
                {"name": "Flashing", "value": 2, "display_name": "Flashing"},
                {"name": "Other", "value": 3, "display_name": "Other"},
            ]
        },
    ),
    (
        "ns=1;i=3002",
        "StacklightOperationMode",
        {
            "fields": [
                {"name": "Segmented", "value": 0, "display_name": "Segmented"},
                {"name": "Levelmeter", "value": 1, "display_name": "Levelmeter"},
                {"name": "Running_Light", "value": 2, "display_name": "Running_Light"},
                {"name": "Other", "value": 3, "display_name": "Other"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [("ns=1;i=3007", "ns=1;i=5009", ["i=3", "i=3", "i=3", "i=3"])],
    ["ns=1;i=3003", "ns=1;i=3004", "ns=1;i=3005", "ns=1;i=3002"],
)
_NODES: dict = {
    "datatypes": {
        "LevelDisplayMode": (
            "D",
            "ns=1;i=3003",
            {"EnumValues": ("V", "ns=1;i=6001", {})},
        ),
        "RGBWDataType": ("D", "ns=1;i=3007", {}),
        "SignalColor": ("D", "ns=1;i=3004", {"EnumValues": ("V", "ns=1;i=6007", {})}),
        "SignalModeLight": (
            "D",
            "ns=1;i=3005",
            {"EnumValues": ("V", "ns=1;i=6008", {})},
        ),
        "StacklightOperationMode": (
            "D",
            "ns=1;i=3002",
            {"EnumValues": ("V", "ns=1;i=6006", {})},
        ),
    },
    "ifacetypes": {
        "IStatisticsType": (
            "OT",
            "ns=1;i=1011",
            {
                "IAggregateStatisticsType": (
                    "OT",
                    "ns=1;i=1012",
                    {"ResetCondition": ("V", "ns=1;i=6047", {})},
                ),
                "IRollingStatisticsType": (
                    "OT",
                    "ns=1;i=1013",
                    {
                        "WindowDuration": ("V", "ns=1;i=6048", {}),
                        "WindowNumberOfValues": ("V", "ns=1;i=6049", {}),
                    },
                ),
                "ResetStatistics": ("M", "ns=1;i=7001", {}),
                "StartTime": ("V", "ns=1;i=6046", {}),
            },
        )
    },
    "objects": {
        "<OrderedObject>": (
            "O",
            "ns=1;i=5004",
            {"NumberInList": ("V", "ns=1;i=6030", {})},
        ),
        "Default Binary": ("O", "ns=1;i=5009", {}),
        "Default XML": ("O", "ns=1;i=5014", {}),
        "TypeDictionary": (
            "V",
            "ns=1;i=6004",
            {
                "Deprecated": ("V", "ns=1;i=6054", {}),
                "NamespaceUri": ("V", "ns=1;i=6005", {}),
                "RGBWDataType": ("V", "ns=1;i=6051", {}),
            },
        ),
        "http://opcfoundation.org/UA/IA/": (
            "O",
            "ns=1;i=5008",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6039", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6040", {}),
                "NamespaceUri": ("V", "ns=1;i=6041", {}),
                "NamespaceVersion": ("V", "ns=1;i=6042", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6043", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6044", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6045", {}),
            },
        ),
    },
    "objtypes": {
        "AcousticSignalType": (
            "OT",
            "ns=1;i=1009",
            {
                "AudioSample": ("V", "ns=1;i=6029", {}),
                "NumberInList": ("V", "ns=1;i=6028", {}),
            },
        ),
        "BaseCalibrationTargetCategoryType": (
            "OT",
            "ns=1;i=1014",
            {
                "DynamicCalibrationTargetCategoryType": ("OT", "ns=1;i=1018", {}),
                "OneTimeCalibrationTargetCategoryType": ("OT", "ns=1;i=1017", {}),
                "ReusableCalibrationTargetCategoryType": (
                    "OT",
                    "ns=1;i=1015",
                    {
                        "ReusableDeviceCalibrationTargetCategoryType": (
                            "OT",
                            "ns=1;i=1016",
                            {},
                        )
                    },
                ),
            },
        ),
        "BasicStacklightType": (
            "OT",
            "ns=1;i=1002",
            {
                "StackLevel": (
                    "O",
                    "ns=1;i=5001",
                    {
                        "DisplayMode": ("V", "ns=1;i=6034", {}),
                        "LevelPercent": (
                            "V",
                            "ns=1;i=6035",
                            {"EURange": ("V", "ns=1;i=6036", {})},
                        ),
                    },
                ),
                "StackRunning": ("O", "ns=1;i=5005", {}),
                "StacklightMode": ("V", "ns=1;i=6009", {}),
                "StacklightType": (
                    "OT",
                    "ns=1;i=1010",
                    {
                        "DeviceHealth": ("V", "ns=1;i=6038", {}),
                        "DeviceHealthAlarms": ("O", "ns=1;i=5007", {}),
                    },
                ),
            },
        ),
        "CalibrationTargetType": (
            "OT",
            "ns=1;i=1019",
            {
                "CalibrationTargetCategory": ("O", "ns=1;i=5011", {}),
                "CalibrationTargetFeatures": (
                    "O",
                    "ns=1;i=5013",
                    {
                        "<CalibrationValue>": (
                            "V",
                            "ns=1;i=6064",
                            {"EngineeringUnits": ("V", "ns=1;i=6065", {})},
                        ),
                        "<CapacityRange>": (
                            "V",
                            "ns=1;i=6066",
                            {
                                "EngineeringUnits": ("V", "ns=1;i=6067", {}),
                                "Resolution": ("V", "ns=1;i=6068", {}),
                            },
                        ),
                    },
                ),
                "CertificateUri": ("V", "ns=1;i=6063", {}),
                "Identification": (
                    "O",
                    "ns=1;i=5010",
                    {
                        "AssetId": ("V", "ns=1;i=6080", {}),
                        "ComponentName": ("V", "ns=1;i=6081", {}),
                        "DeviceClass": ("V", "ns=1;i=6076", {}),
                        "DeviceManual": ("V", "ns=1;i=6082", {}),
                        "DeviceRevision": ("V", "ns=1;i=6075", {}),
                        "HardwareRevision": ("V", "ns=1;i=6073", {}),
                        "Manufacturer": ("V", "ns=1;i=6069", {}),
                        "ManufacturerUri": ("V", "ns=1;i=6070", {}),
                        "Model": ("V", "ns=1;i=6071", {}),
                        "ProductCode": ("V", "ns=1;i=6072", {}),
                        "ProductInstanceUri": ("V", "ns=1;i=6078", {}),
                        "RevisionCounter": ("V", "ns=1;i=6079", {}),
                        "SerialNumber": ("V", "ns=1;i=6077", {}),
                        "SoftwareRevision": ("V", "ns=1;i=6074", {}),
                    },
                ),
                "LastValidationDate": ("V", "ns=1;i=6060", {}),
                "NextValidationDate": ("V", "ns=1;i=6061", {}),
                "OperationalConditions": ("O", "ns=1;i=5012", {}),
                "Quality": ("V", "ns=1;i=6062", {}),
            },
        ),
        "ControlChannelType": (
            "OT",
            "ns=1;i=1008",
            {
                "ChannelColor": ("V", "ns=1;i=6024", {}),
                "Intensity": (
                    "V",
                    "ns=1;i=6026",
                    {"EURange": ("V", "ns=1;i=6027", {})},
                ),
                "SignalMode": ("V", "ns=1;i=6025", {}),
                "SignalOn": ("V", "ns=1;i=6023", {}),
            },
        ),
        "StackElementType": (
            "OT",
            "ns=1;i=1005",
            {
                "IsPartOfBase": ("V", "ns=1;i=6014", {}),
                "NumberInList": ("V", "ns=1;i=6015", {}),
                "SignalOn": ("V", "ns=1;i=6013", {}),
                "StackElementAcousticType": (
                    "OT",
                    "ns=1;i=1007",
                    {
                        "AcousticSignals": ("O", "ns=1;i=5003", {}),
                        "Intensity": (
                            "V",
                            "ns=1;i=6021",
                            {"EURange": ("V", "ns=1;i=6022", {})},
                        ),
                        "OperationMode": ("V", "ns=1;i=6020", {}),
                    },
                ),
                "StackElementLightType": (
                    "OT",
                    "ns=1;i=1006",
                    {
                        "<ControlChannel>": (
                            "O",
                            "ns=1;i=5002",
                            {
                                "ChannelColor": ("V", "ns=1;i=6031", {}),
                                "SignalMode": ("V", "ns=1;i=6032", {}),
                                "SignalOn": ("V", "ns=1;i=6033", {}),
                            },
                        ),
                        "Intensity": (
                            "V",
                            "ns=1;i=6018",
                            {"EURange": ("V", "ns=1;i=6019", {})},
                        ),
                        "SignalColor": ("V", "ns=1;i=6016", {}),
                        "SignalMode": ("V", "ns=1;i=6017", {}),
                        "SignalRGBWValue": ("V", "ns=1;i=6052", {}),
                    },
                ),
            },
        ),
        "StackLevelType": (
            "OT",
            "ns=1;i=1003",
            {
                "DisplayMode": ("V", "ns=1;i=6012", {}),
                "LevelPercent": (
                    "V",
                    "ns=1;i=6010",
                    {"EURange": ("V", "ns=1;i=6011", {})},
                ),
            },
        ),
        "StackRunningType": ("OT", "ns=1;i=1004", {}),
    },
    "reftypes": {
        "HasReferenceMeasurementInstrument": ("RT", "ns=1;i=4003", {}),
        "HasStatisticComponent": ("RT", "ns=1;i=4002", {}),
    },
    "vartypes": {
        "CalibrationValueType": (
            "VT",
            "ns=1;i=2002",
            {"EngineeringUnits": ("V", "ns=1;i=6057", {})},
        ),
        "CapacityRangeType": (
            "VT",
            "ns=1;i=2003",
            {
                "EngineeringUnits": ("V", "ns=1;i=6058", {}),
                "Resolution": ("V", "ns=1;i=6059", {}),
            },
        ),
    },
}
