# AUTO-GENERATED — DO NOT EDIT
# source-sha256: 3b78dc0abe6307b7e58918af0d35ee88c456b5260de764e65df308f122655475
# Run tools/update_ns.py to regenerate.
from __future__ import annotations

_URI: str = "http://opcfoundation.org/UA/PROFINET/"
_VERSION: str = "1.0.1"
_REQUIRED: list = [{"uri": "http://opcfoundation.org/UA/", "version": "1.04.7"}]
_STRUCTURES: list = [
    (
        "ns=1;i=3019",
        "PnDeviceDiagnosisDataType",
        "ns=1;i=5004",
        {
            "structure_type": 0,
            "fields": [
                {"name": "API", "data_type": "i=7", "value_rank": -1},
                {"name": "Slot", "data_type": "i=5", "value_rank": -1},
                {"name": "Subslot", "data_type": "i=5", "value_rank": -1},
                {"name": "ChannelNumber", "data_type": "i=5", "value_rank": -1},
                {"name": "Type", "data_type": "ns=1;i=3010", "value_rank": -1},
                {"name": "Accumulative", "data_type": "ns=1;i=3011", "value_rank": -1},
                {"name": "Maintenance", "data_type": "ns=1;i=3012", "value_rank": -1},
                {"name": "Specifier", "data_type": "ns=1;i=3013", "value_rank": -1},
                {"name": "Direction", "data_type": "ns=1;i=3014", "value_rank": -1},
                {
                    "name": "UserStructureIdentifier",
                    "data_type": "i=5",
                    "value_rank": -1,
                },
                {"name": "ChannelErrorType", "data_type": "i=5", "value_rank": -1},
                {"name": "ExtChannelErrorType", "data_type": "i=5", "value_rank": -1},
                {"name": "ExtChannelAddValue", "data_type": "i=7", "value_rank": -1},
                {
                    "name": "QualifiedChannelQualifier",
                    "data_type": "i=7",
                    "value_rank": -1,
                },
                {"name": "ManufacturerData", "data_type": "i=15", "value_rank": -1},
                {"name": "Message", "data_type": "i=21", "value_rank": -1},
                {"name": "HelpText", "data_type": "i=21", "value_rank": -1},
            ],
        },
    ),
    (
        "ns=1;i=3020",
        "PnIM5DataType",
        "ns=1;i=5007",
        {
            "structure_type": 0,
            "fields": [
                {"name": "Annotation", "data_type": "i=12", "value_rank": -1},
                {"name": "OrderId", "data_type": "i=12", "value_rank": -1},
                {"name": "VendorId", "data_type": "i=5", "value_rank": -1},
                {"name": "SerialNumber", "data_type": "i=12", "value_rank": -1},
                {"name": "HardwareRevision", "data_type": "i=12", "value_rank": -1},
                {"name": "SoftwareRevision", "data_type": "i=12", "value_rank": -1},
            ],
        },
    ),
]
_ENUMS: list = [
    (
        "ns=1;i=3021",
        "IMTagSelectorEnumeration",
        {
            "fields": [
                {"name": "FUNCTION", "value": 0, "display_name": "FUNCTION"},
                {"name": "LOCATION", "value": 1, "display_name": "LOCATION"},
                {"name": "BOTH", "value": 2, "display_name": "BOTH"},
            ]
        },
    ),
    (
        "ns=1;i=3004",
        "PnARStateEnumeration",
        {
            "fields": [
                {"name": "CONNECTED", "value": 0, "display_name": "CONNECTED"},
                {"name": "UNCONNECTED", "value": 1, "display_name": "UNCONNECTED"},
                {
                    "name": "UNCONNECTED_ERR_DEVICE_NOT_FOUND",
                    "value": 2,
                    "display_name": "UNCONNECTED_ERR_DEVICE_NOT_FOUND",
                },
                {
                    "name": "UNCONNECTED_ERR_DUPLICATE_IP",
                    "value": 3,
                    "display_name": "UNCONNECTED_ERR_DUPLICATE_IP",
                },
                {
                    "name": "UNCONNECTED_ERR_DUPLICATE_NOS",
                    "value": 4,
                    "display_name": "UNCONNECTED_ERR_DUPLICATE_NOS",
                },
            ]
        },
    ),
    (
        "ns=1;i=3005",
        "PnARTypeEnumeration",
        {
            "fields": [
                {"name": "IOCARSingle", "value": 0, "display_name": "IOCARSingle"},
                {"name": "IOSAR", "value": 6, "display_name": "IOSAR"},
                {
                    "name": "IOCARSingleUsingRT_CLASS_3",
                    "value": 16,
                    "display_name": "IOCARSingleUsingRT_CLASS_3",
                },
                {"name": "IOCARSR", "value": 32, "display_name": "IOCARSR"},
            ]
        },
    ),
    (
        "ns=1;i=3016",
        "PnAssetChangeEnumeration",
        {
            "fields": [
                {"name": "INSERTED", "value": 0, "display_name": "INSERTED"},
                {"name": "REMOVED", "value": 1, "display_name": "REMOVED"},
                {"name": "CHANGED", "value": 2, "display_name": "CHANGED"},
            ]
        },
    ),
    (
        "ns=1;i=3015",
        "PnAssetTypeEnumeration",
        {
            "fields": [
                {"name": "DEVICE", "value": 0, "display_name": "DEVICE"},
                {"name": "MODULE", "value": 1, "display_name": "MODULE"},
                {"name": "SUBMODULE", "value": 2, "display_name": "SUBMODULE"},
                {"name": "ASSET", "value": 3, "display_name": "ASSET"},
            ]
        },
    ),
    (
        "ns=1;i=3011",
        "PnChannelAccumulativeEnumeration",
        {
            "fields": [
                {"name": "SINGLE", "value": 0, "display_name": "SINGLE"},
                {"name": "ACCUMULATIVE", "value": 256, "display_name": "ACCUMULATIVE"},
            ]
        },
    ),
    (
        "ns=1;i=3014",
        "PnChannelDirectionEnumeration",
        {
            "fields": [
                {
                    "name": "MANUFACTURER_SPECIFIC",
                    "value": 0,
                    "display_name": "MANUFACTURER_SPECIFIC",
                },
                {
                    "name": "INPUT_CHANNEL",
                    "value": 8192,
                    "display_name": "INPUT_CHANNEL",
                },
                {
                    "name": "OUTPUT_CHANNEL",
                    "value": 16384,
                    "display_name": "OUTPUT_CHANNEL",
                },
                {
                    "name": "BIDIRECTIONAL_CHANNEL",
                    "value": 24576,
                    "display_name": "BIDIRECTIONAL_CHANNEL",
                },
            ]
        },
    ),
    (
        "ns=1;i=3012",
        "PnChannelMaintenanceEnumeration",
        {
            "fields": [
                {"name": "FAULT", "value": 0, "display_name": "FAULT"},
                {
                    "name": "MAINTENANCE_REQUIRED",
                    "value": 512,
                    "display_name": "MAINTENANCE_REQUIRED",
                },
                {
                    "name": "MAINTENANCE_DEMANDED",
                    "value": 1024,
                    "display_name": "MAINTENANCE_DEMANDED",
                },
                {
                    "name": "USE_QUALIFIED_CHANNEL_QUALIFIER",
                    "value": 1536,
                    "display_name": "USE_QUALIFIED_CHANNEL_QUALIFIER",
                },
            ]
        },
    ),
    (
        "ns=1;i=3013",
        "PnChannelSpecifierEnumeration",
        {
            "fields": [
                {
                    "name": "ALL_DISAPPEARS",
                    "value": 0,
                    "display_name": "ALL_DISAPPEARS",
                },
                {"name": "APPEARS", "value": 2048, "display_name": "APPEARS"},
                {"name": "DISAPPEARS", "value": 4096, "display_name": "DISAPPEARS"},
                {
                    "name": "DISAPPEARS_OTHER_REMAIN",
                    "value": 6144,
                    "display_name": "DISAPPEARS_OTHER_REMAIN",
                },
            ]
        },
    ),
    (
        "ns=1;i=3010",
        "PnChannelTypeEnumeration",
        {
            "fields": [
                {"name": "UNSPECIFIC", "value": 0, "display_name": "UNSPECIFIC"},
                {"name": "1BIT", "value": 1, "display_name": "1BIT"},
                {"name": "2BIT", "value": 2, "display_name": "2BIT"},
                {"name": "4BIT", "value": 3, "display_name": "4BIT"},
                {"name": "8BIT", "value": 4, "display_name": "8BIT"},
                {"name": "16BIT", "value": 5, "display_name": "16BIT"},
                {"name": "32BIT", "value": 6, "display_name": "32BIT"},
                {"name": "64BIT", "value": 7, "display_name": "64BIT"},
            ]
        },
    ),
    (
        "ns=1;i=3003",
        "PnDeviceStateEnumeration",
        {
            "fields": [
                {"name": "OFFLINE", "value": 0, "display_name": "OFFLINE"},
                {
                    "name": "OFFLINE_DOCKING",
                    "value": 1,
                    "display_name": "OFFLINE_DOCKING",
                },
                {"name": "ONLINE", "value": 2, "display_name": "ONLINE"},
                {
                    "name": "ONLINE_DOCKING",
                    "value": 3,
                    "display_name": "ONLINE_DOCKING",
                },
            ]
        },
    ),
    (
        "ns=1;i=3017",
        "PnLinkStateEnumeration",
        {
            "fields": [
                {"name": "UP", "value": 1, "display_name": "UP"},
                {"name": "DOWN", "value": 2, "display_name": "DOWN"},
                {"name": "TESTING", "value": 3, "display_name": "TESTING"},
                {"name": "UNKNOWN", "value": 4, "display_name": "UNKNOWN"},
                {"name": "DORMANT", "value": 5, "display_name": "DORMANT"},
                {"name": "NOT_PRESENT", "value": 6, "display_name": "NOT_PRESENT"},
                {
                    "name": "LOWER_LAYER_DOWN",
                    "value": 7,
                    "display_name": "LOWER_LAYER_DOWN",
                },
            ]
        },
    ),
    (
        "ns=1;i=3006",
        "PnModuleStateEnumeration",
        {
            "fields": [
                {"name": "NO_MODULE", "value": 0, "display_name": "NO_MODULE"},
                {"name": "WRONG_MODULE", "value": 1, "display_name": "WRONG_MODULE"},
                {"name": "PROPER_MODULE", "value": 2, "display_name": "PROPER_MODULE"},
                {"name": "SUBSTITUTE", "value": 3, "display_name": "SUBSTITUTE"},
                {"name": "OK", "value": 4, "display_name": "OK"},
            ]
        },
    ),
    (
        "ns=1;i=3018",
        "PnPortStateEnumeration",
        {
            "fields": [
                {"name": "UNKNOWN", "value": 0, "display_name": "UNKNOWN"},
                {
                    "name": "DISABLED_DISCARDING",
                    "value": 1,
                    "display_name": "DISABLED_DISCARDING",
                },
                {"name": "BLOCKING", "value": 2, "display_name": "BLOCKING"},
                {"name": "LISTENING", "value": 3, "display_name": "LISTENING"},
                {"name": "LEARNING", "value": 4, "display_name": "LEARNING"},
                {"name": "FORWARDING", "value": 5, "display_name": "FORWARDING"},
                {"name": "BROKEN", "value": 6, "display_name": "BROKEN"},
            ]
        },
    ),
    (
        "ns=1;i=3007",
        "PnSubmoduleAddInfoEnumeration",
        {
            "fields": [
                {"name": "NO_ADD_INFO", "value": 0, "display_name": "NO_ADD_INFO"},
                {
                    "name": "TAKEOVER_NOT_ALLOWED",
                    "value": 1,
                    "display_name": "TAKEOVER_NOT_ALLOWED",
                },
            ]
        },
    ),
    (
        "ns=1;i=3008",
        "PnSubmoduleARInfoEnumeration",
        {
            "fields": [
                {"name": "OWN", "value": 0, "display_name": "OWN"},
                {
                    "name": "APPLICATION_READY_PENDING",
                    "value": 128,
                    "display_name": "APPLICATION_READY_PENDING",
                },
                {
                    "name": "SUPERORDINATED_LOCKED",
                    "value": 256,
                    "display_name": "SUPERORDINATED_LOCKED",
                },
                {
                    "name": "LOCKED_BY_IO_CONTROLLER",
                    "value": 384,
                    "display_name": "LOCKED_BY_IO_CONTROLLER",
                },
                {
                    "name": "LOCKED_BY_IO_SUPERVISOR",
                    "value": 512,
                    "display_name": "LOCKED_BY_IO_SUPERVISOR",
                },
            ]
        },
    ),
    (
        "ns=1;i=3009",
        "PnSubmoduleIdentInfoEnumeration",
        {
            "fields": [
                {"name": "OK", "value": 0, "display_name": "OK"},
                {"name": "SUBSTITUTE", "value": 2048, "display_name": "SUBSTITUTE"},
                {"name": "WRONG", "value": 4096, "display_name": "WRONG"},
                {"name": "NO_SUBMODULE", "value": 6144, "display_name": "NO_SUBMODULE"},
            ]
        },
    ),
    (
        "ns=1;i=3002",
        "PnDeviceRoleOptionSet",
        {
            "fields": [
                {"name": "IO_DEVICE", "value": 0, "display_name": "IO_DEVICE"},
                {"name": "IO_CONTROLLER", "value": 1, "display_name": "IO_CONTROLLER"},
                {
                    "name": "IO_MULTIDEVICE",
                    "value": 2,
                    "display_name": "IO_MULTIDEVICE",
                },
                {"name": "IO_SUPERVISOR", "value": 3, "display_name": "IO_SUPERVISOR"},
                {"name": "IO_CIM", "value": 4, "display_name": "IO_CIM"},
            ]
        },
    ),
]
_ORIGINAL_NODEIDS: tuple = (
    [
        (
            "ns=1;i=3019",
            "ns=1;i=5004",
            [
                "i=7",
                "i=5",
                "i=5",
                "i=5",
                "ns=1;i=3010",
                "ns=1;i=3011",
                "ns=1;i=3012",
                "ns=1;i=3013",
                "ns=1;i=3014",
                "i=5",
                "i=5",
                "i=5",
                "i=7",
                "i=7",
                "i=15",
                "i=21",
                "i=21",
            ],
        ),
        ("ns=1;i=3020", "ns=1;i=5007", ["i=12", "i=12", "i=5", "i=12", "i=12", "i=12"]),
    ],
    [
        "ns=1;i=3021",
        "ns=1;i=3004",
        "ns=1;i=3005",
        "ns=1;i=3016",
        "ns=1;i=3015",
        "ns=1;i=3011",
        "ns=1;i=3014",
        "ns=1;i=3012",
        "ns=1;i=3013",
        "ns=1;i=3010",
        "ns=1;i=3003",
        "ns=1;i=3017",
        "ns=1;i=3006",
        "ns=1;i=3018",
        "ns=1;i=3007",
        "ns=1;i=3008",
        "ns=1;i=3009",
        "ns=1;i=3002",
    ],
)
_NODES: dict = {
    "datatypes": {
        "IMTagSelectorEnumeration": (
            "D",
            "ns=1;i=3021",
            {"EnumStrings": ("V", "ns=1;i=6194", {})},
        ),
        "PnARStateEnumeration": (
            "D",
            "ns=1;i=3004",
            {"EnumValues": ("V", "ns=1;i=6009", {})},
        ),
        "PnARTypeEnumeration": (
            "D",
            "ns=1;i=3005",
            {"EnumValues": ("V", "ns=1;i=6010", {})},
        ),
        "PnAssetChangeEnumeration": (
            "D",
            "ns=1;i=3016",
            {"EnumValues": ("V", "ns=1;i=6021", {})},
        ),
        "PnAssetTypeEnumeration": (
            "D",
            "ns=1;i=3015",
            {"EnumValues": ("V", "ns=1;i=6020", {})},
        ),
        "PnChannelAccumulativeEnumeration": (
            "D",
            "ns=1;i=3011",
            {"EnumValues": ("V", "ns=1;i=6016", {})},
        ),
        "PnChannelDirectionEnumeration": (
            "D",
            "ns=1;i=3014",
            {"EnumValues": ("V", "ns=1;i=6019", {})},
        ),
        "PnChannelMaintenanceEnumeration": (
            "D",
            "ns=1;i=3012",
            {"EnumValues": ("V", "ns=1;i=6017", {})},
        ),
        "PnChannelSpecifierEnumeration": (
            "D",
            "ns=1;i=3013",
            {"EnumValues": ("V", "ns=1;i=6018", {})},
        ),
        "PnChannelTypeEnumeration": (
            "D",
            "ns=1;i=3010",
            {"EnumValues": ("V", "ns=1;i=6015", {})},
        ),
        "PnDeviceDiagnosisDataType": ("D", "ns=1;i=3019", {}),
        "PnDeviceRoleOptionSet": (
            "D",
            "ns=1;i=3002",
            {"OptionSetValues": ("V", "ns=1;i=6001", {})},
        ),
        "PnDeviceStateEnumeration": (
            "D",
            "ns=1;i=3003",
            {"EnumValues": ("V", "ns=1;i=6008", {})},
        ),
        "PnIM5DataType": ("D", "ns=1;i=3020", {}),
        "PnLinkStateEnumeration": (
            "D",
            "ns=1;i=3017",
            {"EnumValues": ("V", "ns=1;i=6022", {})},
        ),
        "PnModuleStateEnumeration": (
            "D",
            "ns=1;i=3006",
            {"EnumValues": ("V", "ns=1;i=6011", {})},
        ),
        "PnPortStateEnumeration": (
            "D",
            "ns=1;i=3018",
            {"EnumValues": ("V", "ns=1;i=6023", {})},
        ),
        "PnSubmoduleARInfoEnumeration": (
            "D",
            "ns=1;i=3008",
            {"EnumValues": ("V", "ns=1;i=6013", {})},
        ),
        "PnSubmoduleAddInfoEnumeration": (
            "D",
            "ns=1;i=3007",
            {"EnumValues": ("V", "ns=1;i=6012", {})},
        ),
        "PnSubmoduleIdentInfoEnumeration": (
            "D",
            "ns=1;i=3009",
            {"EnumValues": ("V", "ns=1;i=6014", {})},
        ),
    },
    "eventtypes": {
        "PnAssetChangedEventType": (
            "OT",
            "ns=1;i=1003",
            {
                "AssetChange": ("V", "ns=1;i=6041", {}),
                "AssetType": ("V", "ns=1;i=6040", {}),
            },
        ),
        "PnTopologyChangedEventType": ("OT", "ns=1;i=1004", {}),
    },
    "ifacetypes": {
        "IPnDomainType": ("OT", "ns=1;i=1031", {"Nodes": ("O", "ns=1;i=5036", {})}),
        "IPnEquipmentType": (
            "OT",
            "ns=1;i=1032",
            {
                "Alarms": ("O", "ns=1;i=5041", {}),
                "Assets": ("O", "ns=1;i=5039", {}),
                "Diagnosis": ("V", "ns=1;i=6176", {}),
                "IM": (
                    "O",
                    "ns=1;i=5040",
                    {
                        "HardwareRevision": ("V", "ns=1;i=6167", {}),
                        "OrderId": ("V", "ns=1;i=6168", {}),
                        "ProfileId": ("V", "ns=1;i=6169", {}),
                        "ProfileSpecificType": ("V", "ns=1;i=6170", {}),
                        "SerialNumber": ("V", "ns=1;i=6171", {}),
                        "SoftwareRevision": ("V", "ns=1;i=6172", {}),
                        "VendorId": ("V", "ns=1;i=6173", {}),
                        "Version": ("V", "ns=1;i=6174", {}),
                    },
                ),
                "IPnControllerType": (
                    "OT",
                    "ns=1;i=1035",
                    {"ARs": ("O", "ns=1;i=5043", {})},
                ),
                "IPnDeviceType": (
                    "OT",
                    "ns=1;i=1034",
                    {
                        "GSDDescription": ("V", "ns=1;i=6177", {}),
                        "State": ("V", "ns=1;i=6178", {}),
                    },
                ),
                "Interfaces": ("O", "ns=1;i=5037", {}),
                "Modules": ("O", "ns=1;i=5038", {}),
                "ShowLocation": ("M", "ns=1;i=7005", {}),
                "Vendor": ("V", "ns=1;i=6175", {}),
            },
        ),
        "IPnInterfaceType": (
            "OT",
            "ns=1;i=1008",
            {
                "DeviceId": ("V", "ns=1;i=6091", {}),
                "DeviceInstance": ("V", "ns=1;i=6092", {}),
                "DeviceRole": ("V", "ns=1;i=6088", {}),
                "DeviceVendor": ("V", "ns=1;i=6089", {}),
                "NameOfStation": ("V", "ns=1;i=6087", {}),
                "OEMDeviceId": ("V", "ns=1;i=6094", {}),
                "OEMVendorId": ("V", "ns=1;i=6093", {}),
                "Ports": ("O", "ns=1;i=5020", {}),
                "SetNameOfStation": (
                    "M",
                    "ns=1;i=7004",
                    {"InputArguments": ("V", "ns=1;i=6095", {})},
                ),
                "Statistic": ("O", "ns=1;i=5021", {}),
                "VendorId": ("V", "ns=1;i=6090", {}),
            },
        ),
        "IPnModuleType": (
            "OT",
            "ns=1;i=1024",
            {
                "GSDDescription": ("V", "ns=1;i=6147", {}),
                "GSDName": ("V", "ns=1;i=6146", {}),
                "IPnExpectedModuleType": (
                    "OT",
                    "ns=1;i=1027",
                    {
                        "State": ("V", "ns=1;i=6157", {}),
                        "Submodules": ("O", "ns=1;i=5032", {}),
                    },
                ),
                "IPnRealModuleType": (
                    "OT",
                    "ns=1;i=1025",
                    {
                        "Alarms": ("O", "ns=1;i=5030", {}),
                        "Diagnosis": ("V", "ns=1;i=6156", {}),
                        "IM": (
                            "O",
                            "ns=1;i=5029",
                            {
                                "HardwareRevision": ("V", "ns=1;i=6148", {}),
                                "OrderId": ("V", "ns=1;i=6149", {}),
                                "ProfileId": ("V", "ns=1;i=6150", {}),
                                "ProfileSpecificType": ("V", "ns=1;i=6151", {}),
                                "SerialNumber": ("V", "ns=1;i=6152", {}),
                                "SoftwareRevision": ("V", "ns=1;i=6153", {}),
                                "VendorId": ("V", "ns=1;i=6154", {}),
                                "Version": ("V", "ns=1;i=6155", {}),
                            },
                        ),
                        "Submodules": ("O", "ns=1;i=5028", {}),
                    },
                ),
                "IdentNumber": ("V", "ns=1;i=6145", {}),
                "Slot": ("V", "ns=1;i=6144", {}),
            },
        ),
        "IPnSubmoduleType": (
            "OT",
            "ns=1;i=1019",
            {
                "API": ("V", "ns=1;i=6130", {}),
                "GSDDescription": ("V", "ns=1;i=6134", {}),
                "GSDName": ("V", "ns=1;i=6133", {}),
                "IPnExpectedSubmoduleType": (
                    "OT",
                    "ns=1;i=1022",
                    {"State": ("O", "ns=1;i=5026", {})},
                ),
                "IPnRealSubmoduleType": (
                    "OT",
                    "ns=1;i=1020",
                    {
                        "Alarms": ("O", "ns=1;i=5024", {}),
                        "Diagnosis": ("V", "ns=1;i=6143", {}),
                        "IM": (
                            "O",
                            "ns=1;i=5023",
                            {
                                "HardwareRevision": ("V", "ns=1;i=6135", {}),
                                "OrderId": ("V", "ns=1;i=6136", {}),
                                "ProfileId": ("V", "ns=1;i=6137", {}),
                                "ProfileSpecificType": ("V", "ns=1;i=6138", {}),
                                "SerialNumber": ("V", "ns=1;i=6139", {}),
                                "SoftwareRevision": ("V", "ns=1;i=6140", {}),
                                "VendorId": ("V", "ns=1;i=6141", {}),
                                "Version": ("V", "ns=1;i=6142", {}),
                            },
                        ),
                    },
                ),
                "IdentNumber": ("V", "ns=1;i=6132", {}),
                "Subslot": ("V", "ns=1;i=6131", {}),
            },
        ),
    },
    "objects": {
        "<ARs>": (
            "O",
            "ns=1;i=5035",
            {
                "Id": ("V", "ns=1;i=6164", {}),
                "State": ("V", "ns=1;i=6165", {}),
                "Type": ("V", "ns=1;i=6166", {}),
            },
        ),
        "<Assets>": (
            "O",
            "ns=1;i=5010",
            {
                "Annotation": ("V", "ns=1;i=6077", {}),
                "DeviceId": ("V", "ns=1;i=6078", {}),
                "DeviceSubId": ("V", "ns=1;i=6079", {}),
                "Location": ("V", "ns=1;i=6080", {}),
                "OrderId": ("V", "ns=1;i=6081", {}),
                "Organization": ("V", "ns=1;i=6082", {}),
                "SerialNumber": ("V", "ns=1;i=6083", {}),
                "TypeIdentification": ("V", "ns=1;i=6084", {}),
                "UniqueIdentifier": ("V", "ns=1;i=6085", {}),
                "VendorId": ("V", "ns=1;i=6086", {}),
            },
        ),
        "<ComponentName>": ("O", "ns=1;i=5015", {}),
        "<EthernetPort>": ("O", "ns=1;i=5016", {}),
        "<Interfaces>": (
            "O",
            "ns=1;i=5012",
            {
                "DeviceId": ("V", "ns=1;i=6193", {}),
                "DeviceInstance": ("V", "ns=1;i=6232", {}),
                "DeviceRole": ("V", "ns=1;i=6191", {}),
                "DeviceVendor": ("V", "ns=1;i=6231", {}),
                "NameOfStation": ("V", "ns=1;i=6190", {}),
                "OEMDeviceId": ("V", "ns=1;i=6234", {}),
                "OEMVendorId": ("V", "ns=1;i=6233", {}),
                "Ports": ("O", "ns=1;i=5045", {}),
                "SetNameOfStation": (
                    "M",
                    "ns=1;i=7007",
                    {"InputArguments": ("V", "ns=1;i=6236", {})},
                ),
                "Statistic": ("O", "ns=1;i=5058", {}),
                "VendorId": ("V", "ns=1;i=6192", {}),
            },
        ),
        "<Modules>": (
            "O",
            "ns=1;i=5031",
            {
                "Alarms": ("O", "ns=1;i=5052", {}),
                "Diagnosis": ("V", "ns=1;i=6215", {}),
                "GSDDescription": ("V", "ns=1;i=6206", {}),
                "GSDName": ("V", "ns=1;i=6205", {}),
                "IM": (
                    "O",
                    "ns=1;i=5051",
                    {
                        "HardwareRevision": ("V", "ns=1;i=6207", {}),
                        "OrderId": ("V", "ns=1;i=6208", {}),
                        "ProfileId": ("V", "ns=1;i=6209", {}),
                        "ProfileSpecificType": ("V", "ns=1;i=6210", {}),
                        "SerialNumber": ("V", "ns=1;i=6211", {}),
                        "SoftwareRevision": ("V", "ns=1;i=6212", {}),
                        "VendorId": ("V", "ns=1;i=6213", {}),
                        "Version": ("V", "ns=1;i=6214", {}),
                    },
                ),
                "IdentNumber": ("V", "ns=1;i=6180", {}),
                "Slot": ("V", "ns=1;i=6098", {}),
                "Submodules": ("O", "ns=1;i=5050", {}),
            },
        ),
        "<PortName>": ("O", "ns=1;i=5017", {}),
        "<Ports>": ("O", "ns=1;i=5013", {}),
        "<Submodules>": (
            "O",
            "ns=1;i=5025",
            {
                "API": ("V", "ns=1;i=6184", {}),
                "Alarms": ("O", "ns=1;i=5055", {}),
                "Diagnosis": ("V", "ns=1;i=6228", {}),
                "GSDDescription": ("V", "ns=1;i=6219", {}),
                "GSDName": ("V", "ns=1;i=6218", {}),
                "IM": (
                    "O",
                    "ns=1;i=5054",
                    {
                        "HardwareRevision": ("V", "ns=1;i=6220", {}),
                        "OrderId": ("V", "ns=1;i=6221", {}),
                        "ProfileId": ("V", "ns=1;i=6222", {}),
                        "ProfileSpecificType": ("V", "ns=1;i=6223", {}),
                        "SerialNumber": ("V", "ns=1;i=6224", {}),
                        "SoftwareRevision": ("V", "ns=1;i=6225", {}),
                        "VendorId": ("V", "ns=1;i=6226", {}),
                        "Version": ("V", "ns=1;i=6227", {}),
                    },
                ),
                "IdentNumber": ("V", "ns=1;i=6186", {}),
                "Subslot": ("V", "ns=1;i=6185", {}),
            },
        ),
        "Default Binary": ("O", "ns=1;i=5007", {}),
        "Default JSON": ("O", "ns=1;i=5009", {}),
        "Default XML": ("O", "ns=1;i=5008", {}),
        "EthernetInterface": (
            "O",
            "ns=1;i=5057",
            {"MacAddress": ("V", "ns=1;i=6235", {})},
        ),
        "EthernetPort": ("O", "ns=1;i=5018", {}),
        "TypeDictionary": (
            "V",
            "ns=1;i=6004",
            {
                "NamespaceUri": ("V", "ns=1;i=6005", {}),
                "PnDeviceDiagnosisDataType": ("V", "ns=1;i=6043", {}),
                "PnDeviceRoleOptionSet": ("V", "ns=1;i=6007", {}),
                "PnIM5DataType": ("V", "ns=1;i=6045", {}),
            },
        ),
        "http://opcfoundation.org/UA/PROFINET/": (
            "O",
            "ns=1;i=5022",
            {
                "IsNamespaceSubset": ("V", "ns=1;i=6116", {}),
                "NamespacePublicationDate": ("V", "ns=1;i=6117", {}),
                "NamespaceUri": ("V", "ns=1;i=6118", {}),
                "NamespaceVersion": ("V", "ns=1;i=6119", {}),
                "StaticNodeIdTypes": ("V", "ns=1;i=6120", {}),
                "StaticNumericNodeIdRange": ("V", "ns=1;i=6121", {}),
                "StaticStringNodeIdPattern": ("V", "ns=1;i=6122", {}),
            },
        ),
    },
    "objtypes": {
        "NetworkComponentFeatureType": (
            "OT",
            "ns=1;i=1016",
            {
                "IPv4FeatureType": (
                    "OT",
                    "ns=1;i=1017",
                    {
                        "DefaultGateway": ("V", "ns=1;i=6113", {}),
                        "DhcpEnabled": ("V", "ns=1;i=6114", {}),
                        "IpAddress": ("V", "ns=1;i=6111", {}),
                        "SubnetMask": ("V", "ns=1;i=6112", {}),
                    },
                )
            },
        ),
        "NetworkComponentType": (
            "OT",
            "ns=1;i=1013",
            {
                "<FeatureName>": ("O", "ns=1;i=5014", {}),
                "Enabled": ("V", "ns=1;i=6109", {}),
                "EthernetInterfaceType": (
                    "OT",
                    "ns=1;i=1014",
                    {"MacAddress": ("V", "ns=1;i=6110", {})},
                ),
                "EthernetPortType": (
                    "OT",
                    "ns=1;i=1015",
                    {"PhysAddress": ("V", "ns=1;i=6179", {})},
                ),
            },
        ),
        "PnApplicationRelationContainerType": ("OT", "ns=1;i=1030", {}),
        "PnApplicationRelationType": (
            "OT",
            "ns=1;i=1029",
            {
                "DataHoldFactor": ("V", "ns=1;i=6163", {}),
                "Id": ("V", "ns=1;i=6159", {}),
                "Modules": ("O", "ns=1;i=5034", {}),
                "ReductionRatio": ("V", "ns=1;i=6162", {}),
                "SendClockFactor": ("V", "ns=1;i=6161", {}),
                "State": ("V", "ns=1;i=6158", {}),
                "Type": ("V", "ns=1;i=6160", {}),
            },
        ),
        "PnAssetContainerType": ("OT", "ns=1;i=1007", {}),
        "PnAssetType": (
            "OT",
            "ns=1;i=1006",
            {
                "Annotation": ("V", "ns=1;i=6067", {}),
                "DeviceId": ("V", "ns=1;i=6075", {}),
                "DeviceSubId": ("V", "ns=1;i=6076", {}),
                "HardwareRevision": ("V", "ns=1;i=6070", {}),
                "Location": ("V", "ns=1;i=6066", {}),
                "OrderId": ("V", "ns=1;i=6068", {}),
                "Organization": ("V", "ns=1;i=6073", {}),
                "SerialNumber": ("V", "ns=1;i=6071", {}),
                "SoftwareRevision": ("V", "ns=1;i=6069", {}),
                "TypeIdentification": ("V", "ns=1;i=6072", {}),
                "UniqueIdentifier": ("V", "ns=1;i=6065", {}),
                "VendorId": ("V", "ns=1;i=6074", {}),
            },
        ),
        "PnDiagnosisAlarmType": (
            "OT",
            "ns=1;i=1002",
            {
                "API": ("V", "ns=1;i=6024", {}),
                "Accumulative": ("V", "ns=1;i=6029", {}),
                "ChannelErrorType": ("V", "ns=1;i=6034", {}),
                "ChannelNumber": ("V", "ns=1;i=6027", {}),
                "Direction": ("V", "ns=1;i=6032", {}),
                "ExtChannelAddValue": ("V", "ns=1;i=6036", {}),
                "ExtChannelErrorType": ("V", "ns=1;i=6035", {}),
                "HelpText": ("V", "ns=1;i=6039", {}),
                "Maintenance": ("V", "ns=1;i=6030", {}),
                "ManufacturerData": ("V", "ns=1;i=6038", {}),
                "QualifiedChannelQualifier": ("V", "ns=1;i=6037", {}),
                "Slot": ("V", "ns=1;i=6025", {}),
                "Specifier": ("V", "ns=1;i=6031", {}),
                "Subslot": ("V", "ns=1;i=6026", {}),
                "Type": ("V", "ns=1;i=6028", {}),
                "UserStructureIdentifier": ("V", "ns=1;i=6033", {}),
            },
        ),
        "PnEquipmentContainerType": (
            "OT",
            "ns=1;i=1033",
            {
                "<PnEquipments>": (
                    "O",
                    "ns=1;i=5042",
                    {
                        "Alarms": ("O", "ns=1;i=5049", {}),
                        "Assets": ("O", "ns=1;i=5047", {}),
                        "Diagnosis": ("V", "ns=1;i=6204", {}),
                        "IM": (
                            "O",
                            "ns=1;i=5048",
                            {
                                "HardwareRevision": ("V", "ns=1;i=6195", {}),
                                "OrderId": ("V", "ns=1;i=6196", {}),
                                "ProfileId": ("V", "ns=1;i=6197", {}),
                                "ProfileSpecificType": ("V", "ns=1;i=6198", {}),
                                "SerialNumber": ("V", "ns=1;i=6199", {}),
                                "SoftwareRevision": ("V", "ns=1;i=6200", {}),
                                "VendorId": ("V", "ns=1;i=6201", {}),
                                "Version": ("V", "ns=1;i=6202", {}),
                            },
                        ),
                        "Interfaces": ("O", "ns=1;i=5044", {}),
                        "Modules": ("O", "ns=1;i=5046", {}),
                        "ShowLocation": ("M", "ns=1;i=7006", {}),
                        "Vendor": ("V", "ns=1;i=6203", {}),
                    },
                )
            },
        ),
        "PnExpectedModuleContainerType": ("OT", "ns=1;i=1028", {}),
        "PnExpectedSubmoduleContainerType": ("OT", "ns=1;i=1023", {}),
        "PnIdentificationType": (
            "OT",
            "ns=1;i=1005",
            {
                "Date": ("V", "ns=1;i=6058", {}),
                "Descriptor": ("V", "ns=1;i=6059", {}),
                "HardwareRevision": ("V", "ns=1;i=6050", {}),
                "IM5": ("V", "ns=1;i=6061", {}),
                "IMSupported": ("V", "ns=1;i=6055", {}),
                "OrderId": ("V", "ns=1;i=6047", {}),
                "ProfileId": ("V", "ns=1;i=6051", {}),
                "ProfileSpecificType": ("V", "ns=1;i=6052", {}),
                "RevisionCounter": ("V", "ns=1;i=6054", {}),
                "SerialNumber": ("V", "ns=1;i=6048", {}),
                "SetDate": (
                    "M",
                    "ns=1;i=7002",
                    {"InputArguments": ("V", "ns=1;i=6063", {})},
                ),
                "SetDescriptor": (
                    "M",
                    "ns=1;i=7003",
                    {"InputArguments": ("V", "ns=1;i=6064", {})},
                ),
                "SetTags": (
                    "M",
                    "ns=1;i=7001",
                    {"InputArguments": ("V", "ns=1;i=6062", {})},
                ),
                "Signature": ("V", "ns=1;i=6060", {}),
                "SoftwareRevision": ("V", "ns=1;i=6049", {}),
                "TagFunction": ("V", "ns=1;i=6056", {}),
                "TagLocation": ("V", "ns=1;i=6057", {}),
                "VendorId": ("V", "ns=1;i=6046", {}),
                "Version": ("V", "ns=1;i=6053", {}),
            },
        ),
        "PnInterfaceContainerType": ("OT", "ns=1;i=1009", {}),
        "PnPortContainerType": ("OT", "ns=1;i=1011", {}),
        "PnPortStatisticType": (
            "OT",
            "ns=1;i=1012",
            {
                "InDiscards": ("V", "ns=1;i=6105", {}),
                "InErrors": ("V", "ns=1;i=6107", {}),
                "InOctets": ("V", "ns=1;i=6103", {}),
                "OutDiscards": ("V", "ns=1;i=6106", {}),
                "OutErrors": ("V", "ns=1;i=6108", {}),
                "OutOctets": ("V", "ns=1;i=6104", {}),
            },
        ),
        "PnPortType": (
            "OT",
            "ns=1;i=1010",
            {
                "CableDelay": ("V", "ns=1;i=6100", {}),
                "IsWireless": ("V", "ns=1;i=6102", {}),
                "LinkState": ("V", "ns=1;i=6096", {}),
                "MAUType": ("V", "ns=1;i=6099", {}),
                "PortState": ("V", "ns=1;i=6097", {}),
                "PowerBudget": ("V", "ns=1;i=6101", {}),
                "Statistic": ("O", "ns=1;i=5019", {}),
            },
        ),
        "PnRealModuleContainerType": ("OT", "ns=1;i=1026", {}),
        "PnRealSubmoduleContainerType": ("OT", "ns=1;i=1021", {}),
        "PnSubmoduleStateType": (
            "OT",
            "ns=1;i=1018",
            {
                "ARInfo": ("V", "ns=1;i=6128", {}),
                "AddInfo": ("V", "ns=1;i=6123", {}),
                "DiagInfo": ("V", "ns=1;i=6127", {}),
                "IdentInfo": ("V", "ns=1;i=6129", {}),
                "MaintenanceDemanded": ("V", "ns=1;i=6126", {}),
                "MaintenanceRequired": ("V", "ns=1;i=6125", {}),
                "QualifiedInfo": ("V", "ns=1;i=6124", {}),
            },
        ),
    },
    "reftypes": {
        "CommLinkTo": ("RT", "ns=1;i=4015", {}),
        "HasPnApplicationRelation": ("RT", "ns=1;i=4016", {}),
        "HasPnAsset": ("RT", "ns=1;i=4006", {}),
        "HasPnExpectedModule": ("RT", "ns=1;i=4004", {}),
        "HasPnExpectedSubmodule": ("RT", "ns=1;i=4005", {}),
        "HasPnInterface": ("RT", "ns=1;i=4007", {}),
        "HasPnPort": ("RT", "ns=1;i=4008", {}),
        "HasPnRealModule": ("RT", "ns=1;i=4002", {}),
        "HasPnRealSubmodule": ("RT", "ns=1;i=4003", {}),
        "IsPnApplicationRelationControllerInterface": ("RT", "ns=1;i=4012", {}),
        "IsPnApplicationRelationDeviceInterface": ("RT", "ns=1;i=4011", {}),
        "IsPnInterface": ("RT", "ns=1;i=4013", {}),
        "IsPnPort": ("RT", "ns=1;i=4014", {}),
        "IsPnRealModule": ("RT", "ns=1;i=4009", {}),
        "IsPnRealSubmodule": ("RT", "ns=1;i=4010", {}),
    },
}
